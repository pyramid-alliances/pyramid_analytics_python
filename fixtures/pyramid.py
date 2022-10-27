import sys
import os
import json
from typing import (
    List
)

from pathlib import Path
import pytest
from uuid import uuid4
from dataclasses import dataclass
from os.path import exists

import logging

import pyramid_api
from pyramid_api.objects import ModifiedItemsResult

log = logging.getLogger(__name__)



class PyramidTestSettings:
    """Pyramid Specific Test Settings."""
    def __init__(self, settings_file_path: Path=None):
        self.__aliases =  {
            'url':'pyramid_server_url',
            'user' : 'pyramid_server_admin_user',
            'password' : 'pyramid_server_admin_password'
        }
        self.__settings = dict(
            tenant_name     = '_T_valid-tenant-name',
            new_tenant_id   = 't_new_tenant',
            folder_name     = "_T_folder",
            admin_role_name = '_T_admin-role',
            admin_role_id   = 't_admin',
            admin_user_name = 't_admin_name',
            admin_user_pw   = 'password',
            user_role_name  = '_T_not-important-user-role',
            user_role_id    = 't_not_important_user_role',
            tenant_creation_name = "_T_valid-tenant-creation-name",

            pie_content_file_path   = '',
            pie_model_file_path   = '',
            dataServer_name = '',
            dataServer      = {},
            tearDown = True,
            use_default_tenant = False,
            page_timeout = 5000,
            pyramid_saved_admin_token = ".session_token"
        )
        if settings_file_path and settings_file_path.exists():
            with open(settings_file_path) as f:
                settings = json.load(f)
                self.__settings.update(settings)
                log.info(f"settings loaded from '{settings_file_path}'")

    
    def __getattr__(self, key):
        return self.get(key)
    
    def get(self, key):
        key = self.__aliases.get(key,key)
        if key in self.__settings:
            # .. then use the config file
            return  self.__settings.get(key)
        else:
            # or error
            raise ValueError(f"unknown key {key}")
    
@pytest.fixture(scope='session')
def pyramid_settings(request):
    settings_file_path = Path(
        request.config.getoption("--pyramid_settings") or 
        os.environ.get("PYRAMID_TEST_SETTINGS", "test_settings.json")
    )
    print(settings_file_path)
    settings = PyramidTestSettings(settings_file_path)
    
    return settings


@pytest.fixture
def pa_domain(pyramid_settings):
    return pyramid_settings.url

@pytest.fixture
def pa_user(pyramid_settings):
    return pyramid_settings.user

@pytest.fixture
def pa_password(pyramid_settings):
    return pyramid_settings.password

@pytest.fixture
def empty_user_obj():
    user : User = None
    return user

@pytest.fixture(scope='session')
def pa_api(pyramid_settings):
    session = pyramid_api.get_session(pyramid_settings.url)
    session.authenticate(pyramid_api.PasswordGrant(username=pyramid_settings.user, password=pyramid_settings.password))
    #return session
    #, pyramid_settings.user, pyramid_settings.password)
    #import ipdb;ipdb.set_trace()
    print(f"SESSION:  {session}")
    try:
        if pyramid_settings.pyramid_saved_admin_token != None:
            f = open(pyramid_settings.pyramid_saved_admin_token, "w")
            f.write(session.token)
            f.close()
            log.info("Auth token saved")
    except ValueError:
        log.info("No auth token saved")
    pyramid_api.set_session(session)
    yield session

@pytest.fixture(scope='session')
def pa_api_from_token(pyramid_settings):
    try:
        if exists(pyramid_settings.pyramid_saved_admin_token):
            saved_token = open(pyramid_settings.pyramid_saved_admin_token, "r").read()
            session = pyramid_api.get_session(domain=domain)
            grant = TokenGrant(domain = pyramid_settings.url, token = saved_token)
            session.validate_grant(grant)
            pyramid_api.set_session(session)
            yield session
    except ValueError:
        assert False

    assert False

@pytest.fixture(scope='module')
def me(pa_api):
    return pyramid_api.access.getMe()

@pytest.fixture(scope='module')
def new_tenant_id(pa_api):
    return str(uuid4())


@pytest.fixture(scope='module')
def new_role_id(pa_api):
    return str(uuid4())


@pytest.fixture(scope='module')
def new_user_name(pa_api):
    return str(uuid4())

@pytest.fixture(scope='module')
def new_user_id(pa_api):
    return str(uuid4())


@pytest.fixture(scope='module')
def existing_tenant(pa_api, pyramid_settings):
    return pa_api.getTenantByName(pyramid_settings.tenant_name)


@pytest.fixture(scope='module')
def tenant(pa_api, pyramid_settings, new_tenant_id, default_tenant):
    if pyramid_settings.use_default_tenant == False:
        #import ipdb;ipdb.set_trace()
        res = pyramid_api.access.createTenant(
            pyramid_api.objects.NewTenantObject(
                id=new_tenant_id,
                name=pyramid_settings.tenant_name,
                viewerSeats=1,
                proSeats=1,
                showGroupFolder=True))

        assert res.success
        log.info(f"created tenant {pyramid_settings.tenant_name} with id '{new_tenant_id}'")
        tenantId = res.modifiedList[0].id
    else:
        tenantId = default_tenant

    yield tenantId

    # cleanup
    if pyramid_settings.tearDown == True and pyramid_settings.use_default_tenant == False:
        log.info("deleting tenant from fixture")
        res = pyramid_api.access.deleteTenants(
            pyramid_api.objects.DeleteTenantApiData(
                tenantIds=[new_tenant_id], deleteUsers=True, deleteServers=True
            )
        )
        assert res.success


@pytest.fixture(scope='module')
def default_tenant(pa_api):
    tenantId = pyramid_api.access.getDefaultTenant()

    yield tenantId


@pytest.fixture(scope='module')
def role(pyramid_settings, pa_api, tenant, new_role_id):
    res = pyramid_api.access.createRole(
            pyramid_api.objects.RoleData(
                tenantId = tenant,
                roleName = pyramid_settings.admin_role_name,
                roleId = new_role_id,
                isHidden = False,
                isPrivate = False,
                isGroupRole =  False

            )
        )
    assert res.success
    roleId = res.modifiedList[0].id
    log.info(f"created role {roleId} - {pyramid_settings.admin_role_name} in tenant {tenant}")

    yield roleId
    
    if (pyramid_settings.tearDown == True):
        res = pyramid_api.access.deleteRole(roleId)
        assert res.success



@pytest.fixture(scope='module')
def new_domain_admin_user(pyramid_settings, pa_api, new_user_id,  new_user_name, tenant, role):
    # 
    user_req = pyramid_api.objects.CreateUserDbObject(
        id=new_user_id,
        userName=new_user_name,
        password=pyramid_settings.password,
        roleIds=[role],
        statusID=pyramid_api.enum.UserStatusID.enabled,   
        adminType=pyramid_api.enum.AdminType.domainadmin,
        clientLicenseType=pyramid_api.enum.ClientLicenseType.professional,
    )
    assert(isinstance(
            result := pyramid_api.access.createUserDb(user_req),
            pyramid_api.objects.ModifiedItemsResult
    ))
    #if not result.success and "User already exists" in result.errorMessage:
    #    log.error("user already exists, this looks like a leftover from a previous run")
    #    result = pa_api.getUsersByName(user_req)

    assert result.success
    userId = result.modifiedList[0].id
    log.info(f"created user {userId} in tenant {tenant} with roleId {role}")
    
    yield userId

    if (pyramid_settings.tearDown == True):
        assert(isinstance(
                result := pyramid_api.access.deleteUser(userId=userId),
                pyramid_api.objects.ModifiedItemsResult
        ))

@pytest.fixture(scope='module')
def pa_api_domain_admin_user(pa_api, new_user_name, new_domain_admin_user):
    with pyramid_api.UserContext(new_user_name) as context:
        yield context


# @pytest.fixture
# def all_role_users(pyramid_settings, pa_api):
#     roles = pa_api.getAllRoles()
#     role_users = {}
#     for role in roles:
#         role_users[role.name] = pa_api.getUsersByRole(role.id)

#     return role_users

@pytest.fixture(scope='module')
def folder(pyramid_settings, pa_api, tenant, role):
    publicRoot: ContentItem = pyramid_api.content.getPublicOrGroupFolderByTenantId(
         pyramid_api.objects.FolderTenantObject(
             tenantId=tenant,
             validRootFolderType=pyramid_api.enum.ValidRootFolderType.public
             )
    )
    # userRoot: ContentItem = pa_api_domain_admin_user.getUserPublicRootFolder(pa_api_domain_admin_user.getMe().id)

    # addRole: ModifiedItemsResult = pa_api_domain_admin_user.addRoleToItem(
    #     itemId = userRoot.id,
    #     roleId = role,
    #     accessType = AccessType.admin,
    #     propagateRoles = True)
    # assert(addRole.success == True)

    folder_create_operation: ModifiedItemsResult = pyramid_api.content.createNewFolder(
        pyramid_api.objects.NewFolderApiData(
            folderName = pyramid_settings.folder_name,
            parentFolderId = publicRoot.id
    ))
    assert(folder_create_operation.success == True)

    new_folder_id = folder_create_operation.modifiedList[0].id

    log.info(f"created folder {new_folder_id} - {pyramid_settings.folder_name} in tenant {tenant}")

    addRole: ModifiedItemsResult = pyramid_api.content.addRoleToItem(
        pyramid_api.objects.RoleToItemApiData(
            itemId = new_folder_id,
            roleId = role,
            accessType = pyramid_api.enum.AccessType.admin,
            propagateRoles = True
    ))
    assert(addRole.success == True)

    # log.info(pa_api.generic('/API2/content/getContentItemSecurityRoles', {
    #     'contentItemId': new_folder_id
    #     }
    # ))

    folderRoles: List[Role] = pyramid_api.content.getContentItemSecurityRoles(
        contentItemId = new_folder_id
    )
    assert(folderRoles)
    assert(len(list(filter(lambda roleElem: roleElem.roleId == role, folderRoles))) == 1)

    yield new_folder_id

    if (pyramid_settings.tearDown == True):
        assert(isinstance(
                result := pyramid_api.content.purgeContentItems([new_folder_id]),
                ModifiedItemsResult
        ))

def resolveApiEnumValue(configValue, enumName):
    # replace "<enum type>.<enum name>"
    if configValue != None and isinstance(configValue, str):
        enumTypeParts = configValue.split(".")
        if len(enumTypeParts) == 2 and enumTypeParts[0] == enumName :
            enum = getattr(sys.modules["pyramid_api.api_types"], enumName)
            return enum[enumTypeParts[1]]

    return configValue

@pytest.fixture(scope='module')
def data_server(pyramid_settings, pa_api, tenant, role):
    server_config = pyramid_settings.dataServer

    # # replace "ServerType.postgresql"
    server_config["serverType"] = resolveApiEnumValue(server_config["serverType"], "ServerType")

    # replace "ServerAuthenticationMethod.userpassword"
    server_config["serverAuthenticationMethod"] = resolveApiEnumValue(server_config["serverAuthenticationMethod"], "ServerAuthenticationMethod")

    if pyramid_settings.use_default_tenant == False:
        server_config["tenantId"] = tenant
    server_config["serverName"] = str(uuid4())

    server_req: Server = Server(**server_config)
    log.info(server_req)
    assert(isinstance(
            result := pa_api.createDataServer(server_req),
            ModifiedItemsResult
        ))
    assert(result.success == True)

    ds_id = result.modifiedList[0].get('id');
    # assert(isinstance(
    #         result := pa_api.addRoleToServer(
    #             ds_id,
    #             role,
    #             AccessType.write
    #         ),
    #         ModifiedItemsResult
    #     ))
    # assert(result.success == True)

    assert(isinstance(
            result := pa_api.findServerByName(
                server_config["serverName"],
                SearchMatchType.contains
            ),
            list
        ))
    all_ids = [r.itemId for r in result]
    assert(ds_id in all_ids)

    log.info(f"Created data source {ds_id} - {server_config['serverName']}")

    # log.info(pa_api.generic('/API2/dataSources/getServerDataById', {
    #     'dataServerId': ds_id
    #     }
    # ))

    yield ds_id

    if (pyramid_settings.tearDown == True):
        assert(isinstance(
                result := pa_api.deleteDataSource(ds_id),
                ModifiedItemsResult
        ))

@pytest.fixture(scope='module')
def database(pyramid_settings, pa_api, data_server, role):
    server_config = pyramid_settings.dataServer

    assert(isinstance(
            result := pa_api.recognizeDataBase(
                data_server,
                server_config["defaultDatabaseName"]
            ),
            ModifiedItemsResult
        ))
    assert(result.success == True)
    databaseId: str = result.modifiedList[0].get('id')
    assert(databaseId)

    log.info(f"Recognized database {server_config['defaultDatabaseName']} on data source {data_server}")

    assert(isinstance(
            result := pa_api.addRolesToServerAndPropagate(
                serverId = data_server,
                rolesAndAccess = [ ItemRolePair(role, AccessType.admin) ]
                # roleId = role,
                # accessType = AccessType.write
            ),
            ModifiedItemsResult
        ))
    assert(result.success == True)
# Caused by: Duplicate key 10000000-0000-0000-0000-000000000001 (attempted merging values api.models.cms.ItemRoleData@e71808e7 and api.models.cms.ItemRoleData@19d06c93),
# type: java.lang.IllegalStateException
# at java.base/java.util.stream.Collectors.duplicateKeyException(Collectors.java:133)

# at java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)

# at bl.cms.services.api2.RoleServiceApi2Impl.addRolesToMaterializedItemInternal(RoleServiceApi2Impl.java:209)

    yield databaseId

    if (pyramid_settings.tearDown == True):
        assert(isinstance(
                result := pa_api.deleteDataBase(databaseId),
                ModifiedItemsResult
        ))

