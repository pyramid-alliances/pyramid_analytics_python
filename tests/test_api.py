import json
import logging
import os
from typing import (
    List
)
from uuid import uuid4

import pytest
import pyramid_api

log = logging.getLogger()


@pytest.mark.content
def test_get_tenant_domain_admin_user(pa_api, new_domain_admin_user, new_user_name):   
    normal_user = pyramid_api.access.getMe()
    assert normal_user.userName == "admin"
    with pyramid_api.UserContext(new_user_name) as context:
        new_user = pyramid_api.access.getMe()
        log.info(new_user)
        assert new_user.userName == new_user_name
        assert(isinstance(new_user, pyramid_api.objects.PyramidViewUserObject))
    

@pytest.mark.unit
@pytest.mark.integration
def test__content_get_folders(pa_api, me):
    assert(isinstance(
        folder := pyramid_api.content.getUserPublicRootFolder(me.id),
        pyramid_api.objects.PyramidContentItem
    ))

    assert(isinstance(
        pyramid_api.content.getPrivateRootFolder(me.id),
        pyramid_api.objects.PyramidContentItem
    ))
    
    assert(isinstance(
        pyramid_api.content.getPrivateFolderForUser(me.id),
        pyramid_api.objects.PyramidContentItem
    ))

    assert(isinstance(
        pyramid_api.content.getUserGroupRootFolder(me.id),
        pyramid_api.objects.PyramidContentItem
    ))

    for i in pyramid_api.content.getFolderItems(folder.id):
        assert(isinstance(
            i,
            pyramid_api.objects.PyramidContentItem
        ))
    

@pytest.mark.unit
@pytest.mark.integration
def test__notifications_status(me):
    assert(isinstance(
        pyramid_api.notification.getNotificationIndicators(me.id),
        pyramid_api.objects.NotificationIndicatorsResult
    ))

@pytest.mark.unit
def test__client_license_count(pa_api, default_tenant):
    result = pyramid_api.access.getAvailableTenantLicenseCount(
        pyramid_api.objects.TenantLicenseTypeData(
            tenantId=default_tenant, licenseType=pyramid_api.enum.ClientLicenseType.viewer
        )
    )
    assert result > 0



@pytest.mark.unit
@pytest.mark.integration
@pytest.mark.order("first")
def test__tenancy_create(pa_api, me, pyramid_settings):
    assert(isinstance(
        pyramid_api.access.createTenant(
            pyramid_api.objects.NewTenantObject(
                id=str(uuid4()),
                name=pyramid_settings.tenant_creation_name,
                viewerSeats=1,
                proSeats=1,
                showGroupFolder=True)),
        pyramid_api.objects.ModifiedItemsResult
    ))

    assert(isinstance(
        tenant_obj := pyramid_api.access.getTenantByName(pyramid_settings.tenant_creation_name),
        pyramid_api.objects.AdminMultiTenantData
    ))

    assert(tenant_obj.name == pyramid_settings.tenant_creation_name)


@pytest.mark.unit
@pytest.mark.integration
@pytest.mark.order(after="test__tenancy_create")
def test__tenancy_delete(pa_api, me, pyramid_settings):
    assert(isinstance(
        tenant_obj := pyramid_api.access.getTenantByName(pyramid_settings.tenant_creation_name),
        pyramid_api.objects.AdminMultiTenantData
    ))
    # cleanup
    if pyramid_settings.tearDown == True and pyramid_settings.use_default_tenant == False:
        res = pyramid_api.access.deleteTenants(
            pyramid_api.objects.DeleteTenantApiData(
                tenantIds=[tenant_obj.id], deleteUsers=True, deleteServers=True
            )
        )
        assert res.success

"""

@pytest.mark.unit
@pytest.mark.integration
def test__role_create(pa_api, pyramid_settings, tenant):
    assert(isinstance(
        res := pyramid_api.access.createRole(
            pyramid_api.objects.RoleData(
                tenantId=tenant,
                roleName=pyramid_settings.admin_role_name
            )
        ),
        pyramid_api.objects.ModifiedItemsResult

    ))

@pytest.mark.unit
@pytest.mark.integration
@pytest.mark.order(after="test__role_create")
def test__role_delete(pa_api, pyramid_settings, tenant):
    roles = pyramid_api.access.getRolesByName(
        pyramid_api.objects.SearchCriteria(searchValue=pyramid_settings.admin_role_name)
    )
    assert len(roles) > 0
    roleId = roles[0].roleId
    assert roleId != None
    assert(isinstance(
        res := pyramid_api.access.deleteRole(roleId),
        pyramid_api.objects.ModifiedItemsResult
    ))


@pytest.mark.unit
@pytest.mark.integration
@pytest.mark.order(after="test__role_delete")
def test__user_create(pa_api, pyramid_settings, tenant):
    user_req = pyramid_api.objects.CreateUserDbObject(
        tenantId=tenant,
        userName=pyramid_settings.admin_user_name,
        password=pyramid_settings.admin_user_pw,
        firstName="userFirstname",
        lastName="userLastname",
        email="testuser@pyramidanalytics.com",
        roleIds=[pyramid_settings.admin_role_id],
        adminType=pyramid_api.enum.AdminType.none,
        clientLicenseType=pyramid_api.enum.ClientLicenseType.viewer,
        statusID=pyramid_api.enum.UserStatusID.enabled
    )
    result = pyramid_api.access.createUserDb(user_req)
    assert(isinstance(result, pyramid_api.objects.ModifiedItemsResult))
    assert(result.success == True)
"""

@pytest.mark.unit
@pytest.mark.integration
@pytest.mark.order("last")
def test__report__called_apis(pa_api):
    if not pa_api.called_endpoints:
        return
    for endpoint in sorted(list(pa_api.called_endpoints)):
        log.info(f"called endpoint: {endpoint}")


@pytest.mark.content
def test_imported_discovers(pa_api, folder):

    for itemMetadata in pyramid_api.content.getFolderItems(folderId=folder):
        if itemMetadata.contentType == pyramid_api.enum.ContentType.datadiscovery:
            log.info(f"QueryExportData: {itemMetadata.id} - {itemMetadata.caption}")
            queryData: pyramid_api.objects.QueryExportData(
                    itemId = itemMetadata.id, 
                    exportType = pyramid_api.enum.ApiResponseFormat.json
                )
            res = pyramid_api.content.extractQueryResult(queryData)
            assert(("You don't have access" in res) == False)
            log.info(res[:100])



"""
@pytest.mark.integration
def test__data_source_create_PG():
    server_req: Server = Server(**{
        'serverName': PG_NAME,
        'serverType': ServerType.postgresql,
        'serverIp': PG_HOST,
        'port': PG_PORT,
        'serverAuthenticationMethod': 0,
        'userName': PG_USER,
        'password': PG_PASSWORD,
        'tenantId': NEW_TENANT_ID,
        'defaultDatabaseName': PG_DB_NAME
    })
    assert(isinstance(
            result := API.createDataServer(server_req),
            ModifiedItemsResult
        ))
    assert(result.success == True)

    ds_id = result.modifiedList[0].get('id');
    assert(isinstance(
            result := API.addRoleToServer(
                ds_id,
                ADMIN_ROLE_ID,
                AccessType.admin
            ),
            ModifiedItemsResult
        ))
    assert(result.success == True)

    assert(isinstance(
            result := API.recognizeDataBase(
                ds_id,
                PG_DB_NAME
            ),
            ModifiedItemsResult
        ))
    assert(result.success == True)
    databaseId: str = result.modifiedList[0].get('id')
    assert(databaseId)
    global PG_DATABASE_ID
    PG_DATABASE_ID = databaseId

    assert(isinstance(
            result := API.findServerByName(
                PG_NAME,
                SearchMatchType.contains
            ),
            list
        ))
    all_ids = [r.itemId for r in result]
    assert(ds_id in all_ids)

    assert(isinstance(
            result := API.findServerByName(
                'fake-server-name',
                SearchMatchType.equals
            ),
            list
        ))
    assert(len(result) == 0)


@pytest.mark.unit
@pytest.mark.integration
def test__data_source_create(pa_api, pyramid_settings, role, new_tenant_id):
    _SRV_NAME = 'fake-internal-imdb'
    server_req: Server = pyramid_api.objects.ServerData(
        serverName =  _SRV_NAME,
        serverType =  pyramid_api.enum.ConnectionStringType.pa_imdb,
        serverIp =  '127.0.0.1',
        port =  3308,
        serverAuthenticationMethod =  0,
        userName =  '',
        password =  '',
        tenantId =  new_tenant_id
    )
    assert(isinstance(
            result := pyramid_api.dataSources.createDataServer(server_req),
            pyramid_api.objects.ModifiedItemsResult
        ))
    assert(result.success == True)

    ds_id = result.modifiedList[0].id

    assert(isinstance(
            result := pyramid_api.dataSources.addRolesToServer(
                pyramid_api.objects.ItemRolesToBeAdded(
                    itemId=ds_id,
                    itemRolePairList=[
                        pyramid_api.objects.ItemRolePair(
                            roleId=role,
                            accessType=pyramid_api.enum.AccessType.admin
                        )
                    ]
                )
            ),
            pyramid_api.objects.ModifiedItemsResult
        ))
    assert(result.success == True)

    assert(isinstance(
            result := pyramid_api.dataSources.recognizeDataBase(
                pyramid_api.objects.DataBaseRecognitionObject(
                    serverId=ds_id,
                    dbName='somedb'
            )),
            pyramid_api.objects.ModifiedItemsResult
        ))
    # TODO make this work with a real external DB
    assert(result.success == False)

    assert(isinstance(
            result := pyramid_api.dataSources.findServerByName(
                pyramid_api.objects.SearchCriteria(
                    searchValue=_SRV_NAME,
                    searchMatchType=pyramid_api.enum.SearchMatchType.contains
                )
            ),
            list
        ))
    all_ids = [r.itemId for r in result]
    log.info(result)
    assert(ds_id in all_ids)

    assert(isinstance(
            result := pyramid_api.dataSources.findServerByName(
                pyramid_api.objects.SearchCriteria(
                    searchValue='fake-server-name',
                    searchMatchType=pyramid_api.enum.SearchMatchType.equals
                )
            ),
            list
        ))
    assert(len(result) == 0)

    for sourceId in all_ids:
        result = pyramid_api.dataSources.deleteDataSource(sourceId=sourceId)
        log.info(f"removing datasource {sourceId}")
        log.info(result)
        assert result.success


@pytest.mark.integration
def test__upload_content(pa_api, pyramid_settings, new_tenant_id):
    # make a folder in public content for the Content
    publicRoot = pyramid_api.content.getPublicOrGroupFolderByTenantId(
        pyramid_api.objects.FolderTenantObject(
            validRootFolderType=pyramid_api.enum.ValidRootFolderType.public 
            tenantId=new_tenant_id
        )
    )

    new_folder_id = str(uuid4())
    folder_create_operation = pyramid_api.content.createNewFolder(
        pyramid_api.objects.NewFolderApiData (
            folderId=new_folder_id,
            folderName='somechild',
            parentFolderId=publicRoot.id
    ))
    assert isinstance(folder_create_operation, pyramid_api.objects.ModifiedItemsResult)
    assert(folder_create_operation.success == True)
    # import the content
    importResult = API.importContent(
        PieApiObject(
            new_folder_id,
            PieApiObject.dataFromPath(PIE_PATH_DASH)
    ))
    assert(isinstance(importResult, ImportApiResultObject))
    # The return from the server is currently bugged and does 
    # notifiy the client of which IDs were created for the content
    res: ModifiedItemsResult = API.addRoleToItem(
        new_folder_id,
        ADMIN_ROLE_ID,
        AccessType.admin,
        True
    )
    assert(res.success == True)

    # # change the datasource to this tenant's connection
    result: List[MaterializedItemObject] = API.findServerByName(
        PG_NAME,
        SearchMatchType.contains
    )
    pg_server_id: str = result[0].itemId

    modelId = API.importModel(
            PG_DATABASE_ID,
            PieApiObject.dataFromPath(PIE_PATH_MODEL)
            # RoleAssignmentType.forceexternalroles,
            # [ADMIN_ROLE_ID]
    )
    assert(importResult)
    res = API.addRoleToModel(modelId, ADMIN_ROLE_ID, AccessType.write)
    assert(res.success == True)

    params = SearchParams(**{
        "searchString":PIE_CONTENT_NAME,
		"filterTypes":[ContentType.datadiscovery],
		"searchMatchType": SearchMatchType.equals,
		"searchRootFolderType": SearchRootFolderType.public
    })
    results: List[ContentItem] =  API.findContentItem(params)
    assert(len(results) > 0)
    assert(results[0].caption == PIE_CONTENT_NAME)
    LOG.debug(results[0])
    content_id = results[0].id

    props: ConnectionStringProperties = API.getItemConnectionString(
        content_id,
        ContentItemObjectType.datadiscovery
    )
    # old_connection_id = props[0].serverId
    old_connection_id = props[0].id
    
    res: ModifiedItemsResult = API.changeDataSource(
        old_connection_id,
        modelId,
        content_id
    )
    assert(res.success == True)

"""