
from typing import (
    Any,
    Dict,
    List,
    Optional
)
from .objects import *
from .enum import *
from .api_interface import call_api

def addDomainSettings(domainSecurityData: DomainSecurityObject) -> ModifiedItemsResult:
    """
    Description:
        Add new AD LDAP server
    
    Input:
        Name: domainSecurityData
        Object Type: DomainSecurityObject
        Description: The security settings object.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/addDomainSettings.htm
    """
    data = { "domainSecurityData" : domainSecurityData }
    return call_api("/API2/access/addDomainSettings",
                data=data, 
                response_type=ModifiedItemsResult
           )



def addProfile(profileApiData: ProfileApiData) -> ModifiedItemsResult:
    """
    Description:
        Adds a User Profile
    
    Input:
        Name: profileApiData
        Object Type: ProfileApiData
        Description: The Profile definition object contains the definition for a user profile.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/addProfile.htm
    """
    data = { "profileApiData" : profileApiData }
    return call_api("/API2/access/addProfile",
                data=data, 
                response_type=ModifiedItemsResult
           )



def addUserToRole(addUserRoleData: AddUserRoleData) -> ModifiedItemsResult:
    """
    Description:
        Add a user to a Role
    
    Input:
        Name: addUserRoleData
        Object Type: AddUserRoleData
        Description: 
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/addUserToRole.htm
    """
    data = { "addUserRoleData" : addUserRoleData }
    return call_api("/API2/access/addUserToRole",
                data=data, 
                response_type=ModifiedItemsResult
           )



def addUsersToRole(addUsersRoleData: AddUsersRoleData) -> ModifiedItemsResult:
    """
    Description:
        Add Users to a Role
    
    Input:
        Name: addUsersRoleData
        Object Type: AddUsersRoleData
        Description: An object for defining which suers are attached a role.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/addUsersToRole.htm
    """
    data = { "addUsersRoleData" : addUsersRoleData }
    return call_api("/API2/access/addUsersToRole",
                data=data, 
                response_type=ModifiedItemsResult
           )



def changeLicenseForUser(changeUserLicense: ChangeUserLicenseObject) -> ModifiedItemsResult:
    """
    Description:
        Change a Userâs License Type
    
    Input:
        Name: changeUserLicense
        Object Type: ChangeUserLicenseObject
        Description: The change license type object contains the license settings for a given user.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/changeLicenseForUser.htm
    """
    data = { "changeUserLicense" : changeUserLicense }
    return call_api("/API2/access/changeLicenseForUser",
                data=data, 
                response_type=ModifiedItemsResult
           )



def changeRoleAdGroupMembership(roleAdGroups: RoleAdGroupsModifyObject) -> ModifiedItemsResult:
    """
    Description:
        Modify Active Directory Groups in a Role
    
    Input:
        Name: roleAdGroups
        Object Type: RoleAdGroupsModifyObject
        Description: The user object contains all relevant meta-data for the user.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/changeRoleAdGroupMembership.htm
    """
    data = { "roleAdGroups" : roleAdGroups }
    return call_api("/API2/access/changeRoleAdGroupMembership",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createRole(roleData: RoleData) -> ModifiedItemsResult:
    """
    Description:
        Create a Security Role
    
    Input:
        Name: roleData
        Object Type: RoleData
        Description: 
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/createRole.htm
    """
    data = { "roleData" : roleData }
    return call_api("/API2/access/createRole",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createRoles(roleData: List[RoleData]) -> ModifiedItemsResult:
    """
    Description:
        Create Security Roles
    
    Input:
        Name: roleData
        Object Type: RoleData[]
        Description: 
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/createRoles.htm
    """
    data = { "roleData" : roleData }
    return call_api("/API2/access/createRoles",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createTenant(newTenant: NewTenantObject) -> ModifiedItemsResult:
    """
    Description:
        Create a Tenant
    
    Input:
        Name: newTenant
        Object Type: NewTenantObject
        Description: The tenant object for creating new tenants.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/createTenant.htm
    """
    data = { "newTenant" : newTenant }
    return call_api("/API2/access/createTenant",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createTenants(newTenant: List[NewTenantObject]) -> ModifiedItemsResult:
    """
    Description:
        Create Multiple Tenants
    
    Input:
        Name: newTenant
        Object Type: NewTenantObject[]
        Description: The tenant object for creating new tenants.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/createTenants.htm
    """
    data = { "newTenant" : newTenant }
    return call_api("/API2/access/createTenants",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createUserAd(createUserAd: CreateUserAdObject) -> ModifiedItemsResult:
    """
    Description:
        Create a new user (ACTIVE DIRECTORY)
    
    Input:
        Name: createUserAd
        Object Type: CreateUserAdObject
        Description: The object used to create a new user when AD authentication is used.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/createUserAd.htm
    """
    data = { "createUserAd" : createUserAd }
    return call_api("/API2/access/createUserAd",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createUserDb(createUserDb: CreateUserDbObject) -> ModifiedItemsResult:
    """
    Description:
        Create a new user (DATABASE)
    
    Input:
        Name: createUserDb
        Object Type: CreateUserDbObject
        Description: The object used to create a new user when DB authentication is used.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/createUserDb.htm
    """
    data = { "createUserDb" : createUserDb }
    return call_api("/API2/access/createUserDb",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createUserOpenId(createUserOpenId: CreateUserOpenIdObject) -> ModifiedItemsResult:
    """
    Description:
        Create a new user (OpenID)
    
    Input:
        Name: createUserOpenId
        Object Type: CreateUserOpenIdObject
        Description: The object used to create a new user when OpenID authentication is used.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/createUserOpenId.htm
    """
    data = { "createUserOpenId" : createUserOpenId }
    return call_api("/API2/access/createUserOpenId",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createUserSaml(createUserSaml: CreateUserSamlObject) -> ModifiedItemsResult:
    """
    Description:
        Create a new user (SAML)
    
    Input:
        Name: createUserSaml
        Object Type: CreateUserSamlObject
        Description: The object used to create a new user when SAML authentication is used.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/createUserSaml.htm
    """
    data = { "createUserSaml" : createUserSaml }
    return call_api("/API2/access/createUserSaml",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createUsersAd(createUserAdArr: List[CreateUserAdObject]) -> ModifiedItemsResult:
    """
    Description:
        Create multiple users (ACTIVE DIRECTORY)
    
    Input:
        Name: createUserAdArr
        Object Type: CreateUserAdObject[]
        Description: The object used to create a new user when AD authentication is used.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/createUsersAd.htm
    """
    data = { "createUserAdArr" : createUserAdArr }
    return call_api("/API2/access/createUsersAd",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createUsersDb(createUserDbArr: List[CreateUserDbObject]) -> ModifiedItemsResult:
    """
    Description:
        Create multiple users (Internal / Database)
    
    Input:
        Name: createUserDbArr
        Object Type: CreateUserDbObject[]
        Description: The object used to create a new user when DB authentication is used.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/createUsersDb.htm
    """
    data = { "createUserDbArr" : createUserDbArr }
    return call_api("/API2/access/createUsersDb",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createUsersOpenId(createUserOpenIdArr: List[CreateUserOpenIdObject]) -> ModifiedItemsResult:
    """
    Description:
        Create multiple users (OpenID)
    
    Input:
        Name: createUserOpenIdArr
        Object Type: CreateUserOpenIdObject[]
        Description: The object used to create a new user when OpenID authentication is used.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/createUsersOpenId.htm
    """
    data = { "createUserOpenIdArr" : createUserOpenIdArr }
    return call_api("/API2/access/createUsersOpenId",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createUsersSaml(createUserSamlArr: List[CreateUserSamlObject]) -> ModifiedItemsResult:
    """
    Description:
        Create multiple users (SAML)
    
    Input:
        Name: createUserSamlArr
        Object Type: CreateUserSamlObject[]
        Description: The object used to create a new user when SAML authentication is used.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/createUsersSaml.htm
    """
    data = { "createUserSamlArr" : createUserSamlArr }
    return call_api("/API2/access/createUsersSaml",
                data=data, 
                response_type=ModifiedItemsResult
           )



def deleteProfile(profileId: str) -> ModifiedItemsResult:
    """
    Description:
        Removes a user profile from the system
    
    Input:
        Name: profileId
        Type: string
        Description: The system profile's ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/deleteProfile.htm
    """
    
    data = {"profileId" : profileId,}
    return call_api("/API2/access/deleteProfile",
                data=data, 
                response_type=ModifiedItemsResult
           )



def deleteRole(roleId: str) -> ModifiedItemsResult:
    """
    Description:
        Delete a Role
    
    Input:
        Name: roleId
        Type: string
        Description: The system role ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/deleteRole.htm
    """
    
    data = {"roleId" : roleId,}
    return call_api("/API2/access/deleteRole",
                data=data, 
                response_type=ModifiedItemsResult
           )



def deleteTenants(deleteTenantApiData: DeleteTenantApiData) -> ModifiedItemsResult:
    """
    Description:
        Delete Tenants
    
    Input:
        Name: deleteTenantApiData
        Object Type: DeleteTenantApiData
        Description: The listing of tenants that will be removed from the system.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/deleteTenants.htm
    """
    data = { "deleteTenantApiData" : deleteTenantApiData }
    return call_api("/API2/access/deleteTenants",
                data=data, 
                response_type=ModifiedItemsResult
           )



def deleteUser(userId: str) -> ModifiedItemsResult:
    """
    Description:
        Delete a User
    
    Input:
        Name: userId
        Type: string
        Description: The system user ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/deleteUser.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/access/deleteUser",
                data=data, 
                response_type=ModifiedItemsResult
           )



def getAllNonPrivateRoles() -> List[ItemId]:
    """
    Description:
        Get All Public Roles
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: Returns a generic response object with the list of public roles in the system Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getAllNonPrivateRoles.htm
    """
    
    return call_api("/API2/access/getAllNonPrivateRoles",
                data=None, 
                response_type=List[ItemId]
           )



def getAllNonPrivateRolesByTenant(tenantId: str) -> List[RoleData]:
    """
    Description:
        Get All Public Roles for a Tenant
    
    Input:
        Name: tenantId
        Type: string
        Description: The system tenant ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: RoleData[]
        Description of Response Type: Returns a generic response object with the list of public roles in the system Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getAllNonPrivateRolesByTenant.htm
    """
    
    data = {"tenantId" : tenantId,}
    return call_api("/API2/access/getAllNonPrivateRolesByTenant",
                data=data, 
                response_type=List[RoleData]
           )



def getAllNonPrivateRolesIDByTenant(tenantId: str) -> List[ItemId]:
    """
    Description:
        Get All Public Roles for a Tenant
    
    Input:
        Name: tenantId
        Type: string
        Description: The system tenant ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: Returns a generic response object with the list of public roles in the system Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getAllNonPrivateRolesIDByTenant.htm
    """
    
    data = {"tenantId" : tenantId,}
    return call_api("/API2/access/getAllNonPrivateRolesIDByTenant",
                data=data, 
                response_type=List[ItemId]
           )



def getAllProfiles() -> List[ProfileApiData]:
    """
    Description:
        Get a list of al user profiles in the System
    
    Output:
        Successful Result Code: 200
        Response List Type: ProfileApiData[]
        Description of Response Type: Returns a list of profile data objects profiles in the system Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getAllProfiles.htm
    """
    
    return call_api("/API2/access/getAllProfiles",
                data=None, 
                response_type=List[ProfileApiData]
           )



def getAllProfilesByTenantId(tenantId: str) -> List[ProfileApiData]:
    """
    Description:
        Get a list of all user profiles in the system for a specific tenant
    
    Input:
        Name: tenantId
        Type: string
        Description: The system tenant ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ProfileApiData[]
        Description of Response Type: Returns a list of profile data objects profiles in the system. The listing is specific to the selected tenant Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getAllProfilesByTenantId.htm
    """
    
    data = {"tenantId" : tenantId,}
    return call_api("/API2/access/getAllProfilesByTenantId",
                data=data, 
                response_type=List[ProfileApiData]
           )



def getAllRoles() -> List[ItemId]:
    """
    Description:
        Get All Roles
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: Returns a generic response object with the list of all role IDs Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getAllRoles.htm
    """
    
    return call_api("/API2/access/getAllRoles",
                data=None, 
                response_type=List[ItemId]
           )



def getAllRolesByProfileId(profileId: str) -> List[RoleData]:
    """
    Description:
        Returns a list of roles assigned to the specified user profile
    
    Input:
        Name: profileId
        Type: string
        Description: The system profile's ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: RoleData[]
        Description of Response Type: Returns a list of roles assigned to the specified profile Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getAllRolesByProfileId.htm
    """
    
    data = {"profileId" : profileId,}
    return call_api("/API2/access/getAllRolesByProfileId",
                data=data, 
                response_type=List[RoleData]
           )



def getAllRolesByUser(userId: str) -> List[ItemId]:
    """
    Description:
        Get all Roles for a User
    
    Input:
        Name: userId
        Type: string
        Description: The system user ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: Returns a generic response object with the list of all role IDs Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getAllRolesByUser.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/access/getAllRolesByUser",
                data=data, 
                response_type=List[ItemId]
           )



def getAllTenants() -> List[AdminMultiTenantData]:
    """
    Description:
        Get all Tenants
    
    Output:
        Successful Result Code: 200
        Response List Type: AdminMultiTenantData[]
        Description of Response Type: Tenant response object with details of each tenant found in the system. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getAllTenants.htm
    """
    
    return call_api("/API2/access/getAllTenants",
                data=None, 
                response_type=List[AdminMultiTenantData]
           )



def getAllUsersByCurrentTenant() -> List[ItemId]:
    """
    Description:
        Get the Current Tenant's Users
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: Returns a generic response object with the list of users for 'CURRENT' tenant Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getAllUsersByCurrentTenant.htm
    """
    
    return call_api("/API2/access/getAllUsersByCurrentTenant",
                data=None, 
                response_type=List[ItemId]
           )



def getAllUsersByTenant(tenantId: str) -> List[ItemId]:
    """
    Description:
        Get a Tenant's Users
    
    Input:
        Name: tenantId
        Type: string
        Description: The system tenant ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: Returns a generic response object with the list of users for the tenant in the system Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getAllUsersByTenant.htm
    """
    
    data = {"tenantId" : tenantId,}
    return call_api("/API2/access/getAllUsersByTenant",
                data=data, 
                response_type=List[ItemId]
           )



def getAllUsersDataByTenantAndLicenceType(tenantUsersGetObject: TenantUsersGetObject) -> List[PyramidViewUserObject]:
    """
    Description:
        Get a Tenant's Users with specific license type
    
    Input:
        Name: tenantUsersGetObject
        Object Type: TenantUsersGetObject
        Description: The tenant object for fetching users.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidViewUserObject[]
        Description of Response Type: Returns a generic response object with the list of users for the tenant in the system Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getAllUsersDataByTenantAndLicenceType.htm
    """
    data = { "tenantUsersGetObject" : tenantUsersGetObject }
    return call_api("/API2/access/getAllUsersDataByTenantAndLicenceType",
                data=data, 
                response_type=List[PyramidViewUserObject]
           )



def getAvailableTenantLicenseCount(tenantLicenseTypeData: TenantLicenseTypeData) -> None:
    """
    Description:
        Get Available License Count for a Tenant
    
    Input:
        Name: tenantLicenseTypeData
        Object Type: TenantLicenseTypeData
        Description: The tenant license object with its license type.
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: successful operation
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getAvailableTenantLicenseCount.htm
    """
    data = { "tenantLicenseTypeData" : tenantLicenseTypeData }
    return call_api("/API2/access/getAvailableTenantLicenseCount",
                data=data, 
                response_type=None
           )



def getDefaultTenant() -> None:
    """
    Description:
        Get the default tenant ID
    
    Output:
        Successful Result Code: 200
        Description of Response Type: successful operation
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getDefaultTenant.htm
    """
    
    return call_api("/API2/access/getDefaultTenant",
                data=None, 
                response_type=None
           )



def getGroupsByRole(roleId: str) -> List[LdapGroupDetails]:
    """
    Description:
        Get Active Directory Groups for a Role
    
    Input:
        Name: roleId
        Type: string
        Description: The system role ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: LdapGroupDetails[]
        Description of Response Type: LDAP Group object with details of the groups found in the role. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getGroupsByRole.htm
    """
    
    data = {"roleId" : roleId,}
    return call_api("/API2/access/getGroupsByRole",
                data=data, 
                response_type=List[LdapGroupDetails]
           )



def getLicenseCount(tenantId: str) -> None:
    """
    Description:
        Get Tenant License Count
    
    Input:
        Name: tenantId
        Type: string
        Description: The system tenant ID
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: successful operation
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getLicenseCount.htm
    """
    
    data = {"tenantId" : tenantId,}
    return call_api("/API2/access/getLicenseCount",
                data=data, 
                response_type=None
           )



def getLicenseExpirationDate() -> None:
    """
    Description:
        Get License Expiration Date
    
    Output:
        Successful Result Code: 200
        Description of Response Type: The date on which the subscription license for the system will expire.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getLicenseExpirationDate.htm
    """
    
    return call_api("/API2/access/getLicenseExpirationDate",
                data=None, 
                response_type=None
           )



def getLicenseValidationStatus() -> ApiResultLicenseStatus:
    """
    Description:
        Get License Status
    
    Output:
        Successful Result Code: 200
        Response Type: ApiResultLicenseStatus
        Description of Response Type: An enumeration with the current status of the license.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getLicenseValidationStatus.htm
    """
    
    return call_api("/API2/access/getLicenseValidationStatus",
                data=None, 
                response_type=ApiResultLicenseStatus
           )



def getMe() -> PyramidViewUserObject:
    """
    Description:
        Gets details for the current user.
    
    Output:
        Successful Result Code: 200
        Response Type: PyramidViewUserObject
        Description of Response Type: The user object contains all relevant meta-data for the user.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getMe.htm
    """
    
    return call_api("/API2/access/getMe",
                data=None, 
                response_type=PyramidViewUserObject
           )



def getPrivateProfileIdForUser(userId: str) -> ItemId:
    """
    Description:
        Returns the profile assigned to the specified user
    
    Input:
        Name: userId
        Type: string
        Description: The system user's ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ItemId
        Description of Response Type: A generic object used to contain ID's of items.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getPrivateProfileIdForUser.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/access/getPrivateProfileIdForUser",
                data=data, 
                response_type=ItemId
           )



def getRoleById(roleId: str) -> RoleData:
    """
    Description:
        Get a Security Role by ID
    
    Input:
        Name: roleId
        Type: string
        Description: The system role ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: RoleData
        Description of Response Type: Role response object with details of the role found in the system.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getRoleById.htm
    """
    
    data = {"roleId" : roleId,}
    return call_api("/API2/access/getRoleById",
                data=data, 
                response_type=RoleData
           )



def getRolesByName(searchCriteria: SearchCriteria) -> List[RoleMinimalData]:
    """
    Description:
        Find Security Roles
    
    Input:
        Name: searchCriteria
        Object Type: SearchCriteria
        Description: The search criteria for finding materialized data elements.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: RoleMinimalData[]
        Description of Response Type: Role response object with details of each role found in the system. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getRolesByName.htm
    """
    data = { "searchCriteria" : searchCriteria }
    return call_api("/API2/access/getRolesByName",
                data=data, 
                response_type=List[RoleMinimalData]
           )



def getTenantByName(name: str) -> AdminMultiTenantData:
    """
    Description:
        Get Tenant by Name
    
    Input:
        Name: name
        Type: string
        Description: The tenant's name
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: AdminMultiTenantData
        Description of Response Type: The tenant object contains all relevant meta-data for the tenant.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getTenantByName.htm
    """
    
    data = {"name" : name,}
    return call_api("/API2/access/getTenantByName",
                data=data, 
                response_type=AdminMultiTenantData
           )



def getUser(userId: str) -> PyramidViewUserObject:
    """
    Description:
        Get a User via ID
    
    Input:
        Name: userId
        Type: string
        Description: The system user ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: PyramidViewUserObject
        Description of Response Type: The user object contains all relevant meta-data for the user.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getUser.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/access/getUser",
                data=data, 
                response_type=PyramidViewUserObject
           )



def getUserByOpenIdPrincipalName(PrincipalName: str) -> PyramidViewUserObject:
    """
    Description:
        Get a User by UPN (OpenID)
    
    Input:
        Name: PrincipalName
        Type: string
        Description: The user's principal name (UPN)
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: PyramidViewUserObject
        Description of Response Type: The user object contains all relevant meta-data for the user.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getUserByOpenIdPrincipalName.htm
    """
    
    data = {"PrincipalName" : PrincipalName,}
    return call_api("/API2/access/getUserByOpenIdPrincipalName",
                data=data, 
                response_type=PyramidViewUserObject
           )



def getUserBySamlPrincipalName(PrincipalName: str) -> PyramidViewUserObject:
    """
    Description:
        Get a User by UPN (SAML)
    
    Input:
        Name: PrincipalName
        Type: string
        Description: The user's UPN
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: PyramidViewUserObject
        Description of Response Type: The user object contains all relevant meta-data for the user.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getUserBySamlPrincipalName.htm
    """
    
    data = {"PrincipalName" : PrincipalName,}
    return call_api("/API2/access/getUserBySamlPrincipalName",
                data=data, 
                response_type=PyramidViewUserObject
           )



def getUserLastLogin(userName: str) -> None:
    """
    Description:
        Get User Last Login Timestamp
    
    Input:
        Name: userName
        Type: string
        Description: The user's login name
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: successful operation
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getUserLastLogin.htm
    """
    
    data = {"userName" : userName,}
    return call_api("/API2/access/getUserLastLogin",
                data=data, 
                response_type=None
           )



def getUserStatusById(userId: str) -> None:
    """
    Description:
        Get User's System Status by User ID
    
    Input:
        Name: userId
        Type: string
        Description: The system user ID
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: Enabled/Disabled flag
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getUserStatusById.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/access/getUserStatusById",
                data=data, 
                response_type=None
           )



def getUserStatusByName(userName: str) -> None:
    """
    Description:
        Get User's System Status by Name
    
    Input:
        Name: userName
        Type: string
        Description: The user's login name
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: Enabled/Disabled flag
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getUserStatusByName.htm
    """
    
    data = {"userName" : userName,}
    return call_api("/API2/access/getUserStatusByName",
                data=data, 
                response_type=None
           )



def getUsersByName(userName: str) -> List[PyramidViewUserObject]:
    """
    Description:
        Get a User by UserName
    
    Input:
        Name: userName
        Type: string
        Description: The user's login name
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidViewUserObject[]
        Description of Response Type: User response object with details of the user found in the system. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getUsersByName.htm
    """
    
    data = {"userName" : userName,}
    return call_api("/API2/access/getUsersByName",
                data=data, 
                response_type=List[PyramidViewUserObject]
           )



def getUsersByRole(roleId: str) -> List[PyramidViewUserObject]:
    """
    Description:
        Get all Users in a Role
    
    Input:
        Name: roleId
        Type: string
        Description: The system role ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidViewUserObject[]
        Description of Response Type: User response object with details of the users found in the system. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/getUsersByRole.htm
    """
    
    data = {"roleId" : roleId,}
    return call_api("/API2/access/getUsersByRole",
                data=data, 
                response_type=List[PyramidViewUserObject]
           )



def searchAdGroups(searchdata: LdapSearchObject) -> List[LdapGroupDetails]:
    """
    Description:
        Search AD Groups
    
    Input:
        Name: searchdata
        Object Type: LdapSearchObject
        Description: The LDAP search object that contains the parameters to be used in Active Directory searches.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: LdapGroupDetails[]
        Description of Response Type: LDAP Group object with details of the groups found in the search. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/searchAdGroups.htm
    """
    data = { "searchdata" : searchdata }
    return call_api("/API2/access/searchAdGroups",
                data=data, 
                response_type=List[LdapGroupDetails]
           )



def searchAdGroupsForUser(searchdata: SearchAdUserGroupsData) -> List[LdapGroupDetails]:
    """
    Description:
        Search Userâs AD Groups
    
    Input:
        Name: searchdata
        Object Type: SearchAdUserGroupsData
        Description: The LDAP search object that contains the parameters to be used in Active Directory searches.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: LdapGroupDetails[]
        Description of Response Type: LDAP Group object with details of the groups found in the search. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/searchAdGroupsForUser.htm
    """
    data = { "searchdata" : searchdata }
    return call_api("/API2/access/searchAdGroupsForUser",
                data=data, 
                response_type=List[LdapGroupDetails]
           )



def searchAdUsers(ldapUsersSearch: LdapUsersSearchObject) -> List[LdapUserObject]:
    """
    Description:
        Search for Active Directory users
    
    Input:
        Name: ldapUsersSearch
        Object Type: LdapUsersSearchObject
        Description: The LDAP search object used to find users in teh LDAP directory.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: LdapUserObject[]
        Description of Response Type: LDAP response object with details of each user found in the search. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/searchAdUsers.htm
    """
    data = { "ldapUsersSearch" : ldapUsersSearch }
    return call_api("/API2/access/searchAdUsers",
                data=data, 
                response_type=List[LdapUserObject]
           )



def searchAdUsersForGroups(searchdata: SearchAdGroupUsersData) -> List[LdapUserObject]:
    """
    Description:
        Search Active Directory Group Members
    
    Input:
        Name: searchdata
        Object Type: SearchAdGroupUsersData
        Description: The LDAP search object that contains the parameters to be used in Active Directory searches.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: LdapUserObject[]
        Description of Response Type: LDAP user object with details of the users found in the search. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/searchAdUsersForGroups.htm
    """
    data = { "searchdata" : searchdata }
    return call_api("/API2/access/searchAdUsersForGroups",
                data=data, 
                response_type=List[LdapUserObject]
           )



def setUserAdministrationLevel(adminTypeApiData: AdminTypeApiData) -> ModifiedItemsResult:
    """
    Description:
        Set User's Administration Level
    
    Input:
        Name: adminTypeApiData
        Object Type: AdminTypeApiData
        Description: The admin type object contains the admin settings for a given user.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/setUserAdministrationLevel.htm
    """
    data = { "adminTypeApiData" : adminTypeApiData }
    return call_api("/API2/access/setUserAdministrationLevel",
                data=data, 
                response_type=ModifiedItemsResult
           )



def toggleEnableUser(toggleUserApiData: ToggleUserApiData) -> ModifiedItemsResult:
    """
    Description:
        Change User's Status
    
    Input:
        Name: toggleUserApiData
        Object Type: ToggleUserApiData
        Description: The toggle object to indicate the user state in the system.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/toggleEnableUser.htm
    """
    data = { "toggleUserApiData" : toggleUserApiData }
    return call_api("/API2/access/toggleEnableUser",
                data=data, 
                response_type=ModifiedItemsResult
           )



def updateRolesByProfileId(profileRolesData: ProfileRolesData) -> List[ItemId]:
    """
    Description:
        Update Role Profiles
    
    Input:
        Name: profileRolesData
        Object Type: ProfileRolesData
        Description: The profile-role object contains a list of all roles to add or remove for the specified profile.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: Returns a generic response object with the list of the added/removed role IDs Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/updateRolesByProfileId.htm
    """
    data = { "profileRolesData" : profileRolesData }
    return call_api("/API2/access/updateRolesByProfileId",
                data=data, 
                response_type=List[ItemId]
           )



def updateTenantSeats(updateTenantSeatsObject: UpdateTenantSeatsObject) -> ModifiedItemsResult:
    """
    Description:
        Updates a tenant seats
    
    Input:
        Name: updateTenantSeatsObject
        Object Type: UpdateTenantSeatsObject
        Description: The tenant object for updating tenant seats.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/updateTenantSeats.htm
    """
    data = { "updateTenantSeatsObject" : updateTenantSeatsObject }
    return call_api("/API2/access/updateTenantSeats",
                data=data, 
                response_type=ModifiedItemsResult
           )



def updateUserAd(updateUserAd: UpdateUserAdObject) -> ModifiedItemsResult:
    """
    Description:
        Update user settings (ACTIVE DIRECTORY)
    
    Input:
        Name: updateUserAd
        Object Type: UpdateUserAdObject
        Description: The object used to update an AD/LDAP based user.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/updateUserAd.htm
    """
    data = { "updateUserAd" : updateUserAd }
    return call_api("/API2/access/updateUserAd",
                data=data, 
                response_type=ModifiedItemsResult
           )



def updateUserDb(updateUserDb: UpdateUserDbObject) -> ModifiedItemsResult:
    """
    Description:
        Update user settings (Internal / DATABASE)
    
    Input:
        Name: updateUserDb
        Object Type: UpdateUserDbObject
        Description: The object used to update a database authentication user.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/updateUserDb.htm
    """
    data = { "updateUserDb" : updateUserDb }
    return call_api("/API2/access/updateUserDb",
                data=data, 
                response_type=ModifiedItemsResult
           )



def updateUserOpenId(updateUserOpenId: UpdateUserOpenIdObject) -> ModifiedItemsResult:
    """
    Description:
        Update user settings (OpenID)
    
    Input:
        Name: updateUserOpenId
        Object Type: UpdateUserOpenIdObject
        Description: The object used to update a OpenID user.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/updateUserOpenId.htm
    """
    data = { "updateUserOpenId" : updateUserOpenId }
    return call_api("/API2/access/updateUserOpenId",
                data=data, 
                response_type=ModifiedItemsResult
           )



def updateUserRoles(userRolesData: UserRolesData) -> List[ItemId]:
    """
    Description:
        Update a Userâs Roles
    
    Input:
        Name: userRolesData
        Object Type: UserRolesData
        Description: The user-role object contains a list of all roles to add or remove for the specified user.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: Returns a generic response object with the list of all user's final role IDs Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/updateUserRoles.htm
    """
    data = { "userRolesData" : userRolesData }
    return call_api("/API2/access/updateUserRoles",
                data=data, 
                response_type=List[ItemId]
           )



def updateUserSaml(updateUserSaml: UpdateUserSamlObject) -> ModifiedItemsResult:
    """
    Description:
        Update user settings (SAML)
    
    Input:
        Name: updateUserSaml
        Object Type: UpdateUserSamlObject
        Description: The object used to update a SAML user.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/updateUserSaml.htm
    """
    data = { "updateUserSaml" : updateUserSaml }
    return call_api("/API2/access/updateUserSaml",
                data=data, 
                response_type=ModifiedItemsResult
           )



def updateUsersAd(updateUserAdArr: List[UpdateUserAdObject]) -> ModifiedItemsResult:
    """
    Description:
        Update user settings (ACTIVE DIRECTORY)
    
    Input:
        Name: updateUserAdArr
        Object Type: UpdateUserAdObject[]
        Description: The object used to update an AD/LDAP based user.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/updateUsersAd.htm
    """
    data = { "updateUserAdArr" : updateUserAdArr }
    return call_api("/API2/access/updateUsersAd",
                data=data, 
                response_type=ModifiedItemsResult
           )



def updateUsersDb(updateUserDbArr: List[UpdateUserDbObject]) -> ModifiedItemsResult:
    """
    Description:
        Update user settings (Internal / DATABASE)
    
    Input:
        Name: updateUserDbArr
        Object Type: UpdateUserDbObject[]
        Description: The object used to update a database authentication user.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/updateUsersDb.htm
    """
    data = { "updateUserDbArr" : updateUserDbArr }
    return call_api("/API2/access/updateUsersDb",
                data=data, 
                response_type=ModifiedItemsResult
           )



def updateUsersOpenId(updateUserOpenIdArr: List[UpdateUserOpenIdObject]) -> ModifiedItemsResult:
    """
    Description:
        Update settings for multiple users (OpenID)
    
    Input:
        Name: updateUserOpenIdArr
        Object Type: UpdateUserOpenIdObject[]
        Description: The object used to update a OpenID user.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/updateUsersOpenId.htm
    """
    data = { "updateUserOpenIdArr" : updateUserOpenIdArr }
    return call_api("/API2/access/updateUsersOpenId",
                data=data, 
                response_type=ModifiedItemsResult
           )



def updateUsersPhones(updateUser: dict) -> None:
    """
    Description:
        Update phones of users
    
    Input:
        Name: updateUser
        Type: object
        Description: 
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: Result object with success or failure flag and related messages. Also includes updated user IDs
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/updateUsersPhones.htm
    """
    
    data = {"updateUser" : updateUser,}
    return call_api("/API2/access/updateUsersPhones",
                data=data, 
                response_type=None
           )



def updateUsersSaml(updateUserSamlArr: List[UpdateUserSamlObject]) -> ModifiedItemsResult:
    """
    Description:
        Update settings for multiple users (SAML)
    
    Input:
        Name: updateUserSamlArr
        Object Type: UpdateUserSamlObject[]
        Description: The object used to update a SAML user.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/access/updateUsersSaml.htm
    """
    data = { "updateUserSamlArr" : updateUserSamlArr }
    return call_api("/API2/access/updateUsersSaml",
                data=data, 
                response_type=ModifiedItemsResult
           )


