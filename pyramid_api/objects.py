
from typing import (
    Any,
    Dict,
    List,
    Optional
)
from pydantic import BaseModel
from .enum import *


class ApiModifierResult(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ApiModifierResult.htm
    """
    success: Optional[bool]  # Format:"" Descr:"Boolean showing success or failure result."
    errorMessage: Optional[str]  # Format:"" Descr:"Error message in case of failure"
    modifiedList: Optional[List[str]]  # Format:"" Descr:"List of item ID's that have been affected by the function call. The type of ID depends on the function."
    

class ApiResultTaskStatus(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ApiResultTaskStatus.htm
    """
    status: Optional[TaskStatus]  # Format:"" Descr:"A schedule's task status."
    

class MemberDataApi(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MemberDataApi.htm
    """
    caption: Optional[str]  # Format:"" Descr:""
    uniqueName: Optional[str]  # Format:"" Descr:""
    

class EnumerationOutput(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/EnumerationOutput.htm
    """
    members: Optional[List[MemberDataApi]]  # Format:"" Descr:"-"
    

class CalcProps(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CalcProps.htm
    """
    executionArea: Optional[ExecutionArea]  # Format:"" Descr:"-"
    categoryType: Optional[CalcCategoryType]  # Format:"" Descr:"-"
    isHiddenCalc: Optional[bool]  # Format:"" Descr:""
    

class CmsTreeNodeMetadata(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CmsTreeNodeMetadata.htm
    """
    id: Optional[str]  # Format:"" Descr:""
    parentId: Optional[str]  # Format:"" Descr:""
    caption: Optional[str]  # Format:"" Descr:""
    type: Optional[int]  # Format:"int32" Descr:""
    hasChildren: Optional[bool]  # Format:"" Descr:""
    databaseName: Optional[str]  # Format:"" Descr:""
    childrenTypes: Optional[int]  # Format:"int32" Descr:""
    hasWriteAccess: Optional[bool]  # Format:"" Descr:""
    rootFolderType: Optional[RootFolderType]  # Format:"" Descr:"-"
    subType: Optional[int]  # Format:"int32" Descr:""
    documentId: Optional[str]  # Format:"" Descr:""
    isTenantRootFolder: Optional[bool]  # Format:"" Descr:""
    isDeleted: Optional[bool]  # Format:"" Descr:""
    serverId: Optional[str]  # Format:"" Descr:""
    model: Optional[str]  # Format:"" Descr:""
    databaseId: Optional[str]  # Format:"" Descr:""
    attributeUniqueName: Optional[str]  # Format:"" Descr:""
    modelName: Optional[str]  # Format:"" Descr:""
    kpiStyleOption: Optional[KpiStylesOptions]  # Format:"" Descr:"-"
    extraData: Optional[dict]  # Format:"" Descr:""
    noAccess: Optional[bool]  # Format:"" Descr:""
    folderPath: Optional[str]  # Format:"" Descr:""
    calcProps: Optional[CalcProps]  # Format:"" Descr:"-"
    tenantId: Optional[str]  # Format:"" Descr:""
    extraNameTag: Optional[str]  # Format:"" Descr:""
    securityHash: Optional[str]  # Format:"" Descr:""
    createdBy: Optional[str]  # Format:"" Descr:""
    rating: Optional[int]  # Format:"int32" Descr:""
    mruPinned: Optional[bool]  # Format:"" Descr:""
    contentType: Optional[ContentType]  # Format:"" Descr:"-"
    

class ExternalServerData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ExternalServerData.htm
    """
    externalServerId: Optional[str]  # Format:"" Descr:""
    internalServerId: Optional[str]  # Format:"" Descr:""
    databaseName: Optional[str]  # Format:"" Descr:""
    schemaName: Optional[str]  # Format:"" Descr:""
    

class OdbcDirectQueryOptions(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/OdbcDirectQueryOptions.htm
    """
    baseSqlStyle: Optional[ConnectionStringType]  # Format:"" Descr:"The data source server type enumeration."
    

class TenantSettings(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TenantSettings.htm
    """
    showGroupFolder: Optional[bool]  # Format:"" Descr:"Boolean to show or hide the tenant's group folders"
    allowWebhookChannels: Optional[bool]  # Format:"" Descr:""
    firstWorkday: Optional[FirstWorkday]  # Format:"" Descr:"-"
    

class TenantInfo(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TenantInfo.htm
    """
    tenantId: Optional[str]  # Format:"" Descr:""
    name: Optional[str]  # Format:"" Descr:""
    

class ConnectionStringProperties(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ConnectionStringProperties.htm
    """
    id: Optional[str]  # Format:"" Descr:"The connection object's system ID"
    modelId: Optional[str]  # Format:"" Descr:"The materialized model's system ID"
    modelName: Optional[str]  # Format:"" Descr:"The model's name"
    serverId: Optional[str]  # Format:"" Descr:"The data source  server's system ID"
    serverName: Optional[str]  # Format:"" Descr:"The data source server's name"
    dataBaseId: Optional[str]  # Format:"" Descr:"The data source  database's system ID"
    dataBaseName: Optional[str]  # Format:"" Descr:"The data source database's name"
    connectionStringType: Optional[ConnectionStringType]  # Format:"" Descr:"The type of connection"
    isDynamicModel: Optional[bool]  # Format:"" Descr:"Boolean showing if a model is dynamic"
    modelParamsStatus: Optional[str]  # Format:"" Descr:""
    securityHash: Optional[str]  # Format:"" Descr:""
    

class ConnectionStringData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ConnectionStringData.htm
    """
    serverId: Optional[str]  # Format:"" Descr:""
    dataBaseName: Optional[str]  # Format:"" Descr:""
    model: Optional[str]  # Format:"" Descr:""
    serverName: Optional[str]  # Format:"" Descr:""
    dynamicModel: Optional[bool]  # Format:"" Descr:""
    uniqueKey: Optional[str]  # Format:"" Descr:""
    

class SearchCriteria(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SearchCriteria.htm
    """
    searchValue: str  # Format:"" Descr:"Search string"
    searchMatchType: Optional[SearchMatchType]  # Format:"" Descr:"Search match enumeration type. Default:Equals."
    

class RelatedItemData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RelatedItemData.htm
    """
    name: Optional[str]  # Format:"" Descr:"The related item's name"
    itemId: Optional[str]  # Format:"uuid" Descr:"The related item's ID"
    contentType: Optional[ContentType]  # Format:"" Descr:"The item's content type enumeration"
    children: Optional[List['RelatedItemData']]  # Format:"" Descr:"The related item's children"
    rootFolderType: Optional[RootFolderType]  # Format:"" Descr:"The item's root folder type enumeration"
    hasWriteAccess: Optional[bool]  # Format:"" Descr:"Boolean to indicate if the user can change and save the item."
    numberOfUsages: Optional[int]  # Format:"int32" Descr:"The amount of times the items is being used by other items"
    sourceItemId: Optional[str]  # Format:"uuid" Descr:""
    level: Optional[int]  # Format:"int32" Descr:""
    createdDate: Optional[str]  # Format:"date-time" Descr:"The create date of the item"
    createdBy: Optional[str]  # Format:"" Descr:"The creator's user ID"
    dataSourceProperties: Optional[ConnectionStringData]  # Format:"" Descr:"The item's Connection string data"
    folderPath: Optional[str]  # Format:"" Descr:"The item's folder absolute file path"
    tenantId: Optional[str]  # Format:"" Descr:"The item's related tenant ID"
    securityHash: Optional[str]  # Format:"" Descr:""
    folderId: Optional[str]  # Format:"" Descr:"The item's parent folder ID"
    lockedByUser: Optional[str]  # Format:"" Descr:""
    itemIdAsString: Optional[str]  # Format:"" Descr:""
    

class ApiModifierResultString(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ApiModifierResultString.htm
    """
    success: Optional[bool]  # Format:"" Descr:"Boolean showing success or failure result."
    errorMessage: Optional[str]  # Format:"" Descr:"Error message in case of failure"
    modifiedList: Optional[List[str]]  # Format:"" Descr:"List of item ID's that have been affected by the function call. The type of ID depends on the function."
    

class ModelingServerInfo(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelingServerInfo.htm
    """
    serverName: Optional[str]  # Format:"" Descr:""
    serverType: Optional[ConnectionStringType]  # Format:"" Descr:"The data source server type enumeration."
    customJdbcId: Optional[str]  # Format:"uuid" Descr:""
    

class FormData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/FormData.htm
    """
    machineKey: Optional[str]  # Format:"" Descr:""
    installationType: Optional[int]  # Format:"int32" Descr:""
    version: Optional[str]  # Format:"" Descr:""
    country: Optional[str]  # Format:"" Descr:""
    firstName: Optional[str]  # Format:"" Descr:""
    lastName: Optional[str]  # Format:"" Descr:""
    email: Optional[str]  # Format:"" Descr:""
    phone: Optional[str]  # Format:"" Descr:""
    

class RegistrationData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RegistrationData.htm
    """
    formData: Optional[FormData]  # Format:"" Descr:"-"
    

class UserWorkspaceSettings(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UserWorkspaceSettings.htm
    """
    customDiscoveryWorkspace: Optional[str]  # Format:"" Descr:""
    discoveryWorkspaceType: Optional[DiscoveryWorkspaceType]  # Format:"" Descr:"-"
    

class CmsLayoutSettings(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CmsLayoutSettings.htm
    """
    measureCalcTreeFlatListView: Optional[bool]  # Format:"" Descr:""
    elementsCalcTreeFlatListView: Optional[bool]  # Format:"" Descr:""
    parametersCalcTreeFlatListView: Optional[bool]  # Format:"" Descr:""
    

class UserSettingsData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UserSettingsData.htm
    """
    mode: Optional[str]  # Format:"" Descr:""
    language: Optional[str]  # Format:"" Descr:""
    showSplashScreen: Optional[bool]  # Format:"" Descr:""
    showViewerMode: Optional[bool]  # Format:"" Descr:""
    firstUse: Optional[bool]  # Format:"" Descr:""
    cmsViewSelection: Optional[int]  # Format:"int32" Descr:""
    homeScreenFavoritesViewSelection: Optional[int]  # Format:"int32" Descr:""
    homeScreenRecentViewSelection: Optional[int]  # Format:"int32" Descr:""
    diagnosticsRefreshTime: Optional[int]  # Format:"int32" Descr:""
    registrationData: Optional[RegistrationData]  # Format:"" Descr:"-"
    homepageLayout: Optional[str]  # Format:"" Descr:""
    userWorkspace: Optional[UserWorkspaceSettings]  # Format:"" Descr:"-"
    cmsLayoutSettings: Optional[CmsLayoutSettings]  # Format:"" Descr:"-"
    isFeedsAdminView: Optional[bool]  # Format:"" Descr:""
    

class AddUserRoleData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AddUserRoleData.htm
    """
    userId: str  # Format:"" Descr:""
    roleId: str  # Format:"" Descr:""
    

class ApiResultLicenseStatus(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ApiResultLicenseStatus.htm
    """
    status: Optional[LicenseStatus]  # Format:"" Descr:"License status enumeration."
    

class HierarchyOverlayData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/HierarchyOverlayData.htm
    """
    uniqueName: str  # Format:"" Descr:"The unique name of the hierarchy that the overlays apply to"
    displayFolder: Optional[str]  # Format:"" Descr:"The display folder of the hierarchy"
    description: Optional[str]  # Format:"" Descr:"The description of the hierarchy"
    alternativeName: Optional[str]  # Format:"" Descr:"The alternative name of the hierarchy"
    type: Optional[ModelingColumnCategories]  # Format:"" Descr:"The type of the hierarchy"
    

class HierarchyOverlayToDeleteData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/HierarchyOverlayToDeleteData.htm
    """
    uniqueName: str  # Format:"" Descr:"The unique name of the hierarchy"
    propertiesToDelete: Optional[List[HierarchyOverlayProperty]]  # Format:"" Descr:"The list of properties to delete from the hierarchy overlay."
    

class DeleteHierarchyOverlayApiObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DeleteHierarchyOverlayApiObject.htm
    """
    modelId: str  # Format:"" Descr:"The model's ID"
    roleId: str  # Format:"" Descr:"The role id the overlays apply to"
    overlayPropertiesToDelete: List[HierarchyOverlayToDeleteData]  # Format:"" Descr:"The overlay properties to delete"
    

class ErrorMessage(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ErrorMessage.htm
    """
    exceptionCategory: Optional[int]  # Format:"int32" Descr:""
    msg: Optional[str]  # Format:"" Descr:""
    code: Optional[int]  # Format:"int32" Descr:""
    params: Optional[List[str]]  # Format:"" Descr:""
    customData: Optional[dict]  # Format:"" Descr:""
    stackTrace: Optional[str]  # Format:"" Descr:""
    showErrorPopUpDialog: Optional[bool]  # Format:"" Descr:""
    

class TaskSummary(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TaskSummary.htm
    """
    message: Optional[str]  # Format:"" Descr:""
    params: Optional[List[str]]  # Format:"" Descr:""
    error: Optional[ErrorMessage]  # Format:"" Descr:"-"
    

class ModelSyncColumnsSettings(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelSyncColumnsSettings.htm
    """
    categoryType: Optional[str]  # Format:"" Descr:""
    dataTypes: Optional[List[str]]  # Format:"" Descr:""
    isVisible: Optional[bool]  # Format:"" Descr:""
    aggregationType: Optional[AggregationType]  # Format:"" Descr:"-"
    

class AdUserData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AdUserData.htm
    """
    userName: str  # Format:"" Descr:"Active Directory username of the user"
    domain: str  # Format:"" Descr:"Active Directory domain name of the user"
    adminType: AdminType  # Format:"" Descr:"The user's administration type flag."
    clientLicenseType: ClientLicenseType  # Format:"" Descr:"The user's client license type."
    tenantId: str  # Format:"" Descr:"The user's tenant (ID)."
    

class AddHierarchyOverlayApiObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AddHierarchyOverlayApiObject.htm
    """
    modelId: str  # Format:"" Descr:"The model's ID"
    roleId: str  # Format:"" Descr:"The role id the overlays apply to"
    overlaysToAdd: List[HierarchyOverlayData]  # Format:"" Descr:"The overlays to add"
    

class AddUsersRoleData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AddUsersRoleData.htm
    """
    userIds: List[str]  # Format:"" Descr:"List of user ID's that will be attached to a role"
    roleId: str  # Format:"" Descr:"The role's ID"
    

class AdditionalServerProperties(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AdditionalServerProperties.htm
    """
    sharedFolderPath: Optional[str]  # Format:"" Descr:"Shared Folder Path"
    relativeFolderName: Optional[str]  # Format:"" Descr:"Relative Folder Path"
    hiveIP: Optional[str]  # Format:"" Descr:"Hadoop HIVE IP address"
    hivePort: Optional[int]  # Format:"int32" Descr:"Hadoop HIVE port number"
    hdfsIP: Optional[str]  # Format:"" Descr:"Hadoop HDFS IP address"
    hdfsPort: Optional[int]  # Format:"int32" Descr:"Hadoop HDFS port number"
    authMethod: Optional[CubeAuthMethod]  # Format:"" Descr:"relevant to olap datasources, specify the auth method used against the cube for end user"
    machineAccountFallback: Optional[bool]  # Format:"" Descr:""
    keytabPath: Optional[str]  # Format:"" Descr:""
    keytabId: Optional[str]  # Format:"uuid" Descr:""
    awsAccessKeyId: Optional[str]  # Format:"" Descr:""
    awsSecretAccessKey: Optional[str]  # Format:"" Descr:""
    awsRegion: Optional[str]  # Format:"" Descr:""
    awsBucketName: Optional[str]  # Format:"" Descr:""
    bulkWritingType: Optional[str]  # Format:"" Descr:""
    athenaRegion: Optional[str]  # Format:"" Descr:""
    s3StagingDir: Optional[str]  # Format:"" Descr:""
    resolveColumnLabel: Optional[bool]  # Format:"" Descr:""
    disableDBTables: Optional[bool]  # Format:"" Descr:""
    disableAttributeViews: Optional[bool]  # Format:"" Descr:""
    disableAnalyticViews: Optional[bool]  # Format:"" Descr:""
    disableCalculationViews: Optional[bool]  # Format:"" Descr:""
    hierarchyType: Optional[HierarchyType]  # Format:"" Descr:"Type of the modeling hierarchy: Drill path, parent-child tree, regular"
    salesforceSecurityToken: Optional[str]  # Format:"" Descr:""
    warehouse: Optional[str]  # Format:"" Descr:""
    accessToken: Optional[str]  # Format:"" Descr:""
    accessTokenSecret: Optional[str]  # Format:"" Descr:""
    consumerKey: Optional[str]  # Format:"" Descr:""
    consumerSecret: Optional[str]  # Format:"" Descr:""
    useSSL: Optional[bool]  # Format:"" Descr:"Use SSL to connect"
    shouldValidateServerCert: Optional[bool]  # Format:"" Descr:"Should validate Server certificate"
    isCustomCertHostname: Optional[bool]  # Format:"" Descr:"Should validate a different hostname than the server hostname"
    customCertHostname: Optional[str]  # Format:"" Descr:"Hostname in certificate that we should validate"
    isCustomKeyStore: Optional[bool]  # Format:"" Descr:"Using a different keystore than the java VM keystore?"
    customKeyStore: Optional[str]  # Format:"" Descr:"Path to custom keystore (in Pyramid server filesystem)"
    customKeyStoreType: Optional[str]  # Format:"" Descr:"Custom keystore type (JKS / PKCS12)"
    customKeyStorePassword: Optional[str]  # Format:"" Descr:"Keystore password"
    isCustomTrustStore: Optional[bool]  # Format:"" Descr:"Using a different java trust store than the java VM trust store?"
    customTrustStore: Optional[str]  # Format:"" Descr:"Path to custom java trust store (in Pyramid server filesystem)"
    customTrustStorePassword: Optional[str]  # Format:"" Descr:"Trust store password"
    isDatabaseSchema: Optional[bool]  # Format:"" Descr:"Treat schemas names as database names in Pyramid"
    accountId: Optional[str]  # Format:"" Descr:"Account ID"
    roleId: Optional[str]  # Format:"" Descr:"Role ID"
    sysNumber: Optional[str]  # Format:"" Descr:""
    clientNumber: Optional[str]  # Format:"" Descr:"Custom client parameter for SAP HANA and BW"
    sncPartnerName: Optional[str]  # Format:"" Descr:""
    sapRouter: Optional[str]  # Format:"" Descr:""
    bwInfoAreaIconIds: Optional[str]  # Format:"" Descr:""
    defaultCulture: Optional[str]  # Format:"" Descr:"Language option for SAP HANA and BW"
    urlPortal: Optional[str]  # Format:"" Descr:""
    bringNonOleDbComponents: Optional[bool]  # Format:"" Descr:""
    showInfoAreaTree: Optional[bool]  # Format:"" Descr:""
    mdxCompatibility: Optional[int]  # Format:"int32" Descr:""
    supportsBwFlatQueries: Optional[bool]  # Format:"" Descr:""
    sapBwServerConnectionType: Optional[str]  # Format:"" Descr:""
    messageServerHost: Optional[str]  # Format:"" Descr:""
    messageServerService: Optional[str]  # Format:"" Descr:""
    systemR3Name: Optional[str]  # Format:"" Descr:""
    groupServer: Optional[str]  # Format:"" Descr:""
    avoidMultiPassAuthentication: Optional[bool]  # Format:"" Descr:""
    msOlapConnectionType: Optional[str]  # Format:"" Descr:""
    externalServers: Optional[List[ExternalServerData]]  # Format:"" Descr:"-"
    odbcDirectQueryOptions: Optional[OdbcDirectQueryOptions]  # Format:"" Descr:"-"
    customJdbcId: Optional[str]  # Format:"uuid" Descr:"Required when serverType is CustomJdbc and specifies which custom jdbc it is"
    customJdbcProps: Optional[dict]  # Format:"" Descr:""
    sparkTransportMode: Optional[str]  # Format:"" Descr:"Transport mode for Spark connection: Binary, SASL or HTTP or HTTPS"
    isOverrideConnectionString: Optional[bool]  # Format:"" Descr:"Should we override the connection string - if so, use optionalJdbcParameters to specify the full JDBC connection string"
    

class AdminMultiTenantData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AdminMultiTenantData.htm
    """
    id: Optional[str]  # Format:"" Descr:"The tenant's system ID"
    name: Optional[str]  # Format:"" Descr:"The tenant's name"
    viewerSeats: Optional[int]  # Format:"int32" Descr:"The total number of viewer licenses for the tenant"
    usedViewerSeats: Optional[int]  # Format:"int32" Descr:"The total number of USED viewer licenses for the tenant"
    proSeats: Optional[int]  # Format:"int32" Descr:"The total number of professional licenses for the tenant"
    usedProSeats: Optional[int]  # Format:"int32" Descr:"The total number of USED professional licenses for the tenant"
    tenantSettings: Optional[TenantSettings]  # Format:"" Descr:"The tenants settings"
    pulseKey: Optional[str]  # Format:"" Descr:"The PULSE server key for the tenant"
    selectedUserDefaultsId: Optional[str]  # Format:"" Descr:""
    selectedUserDefaultsName: Optional[str]  # Format:"" Descr:""
    defaultThemeId: Optional[str]  # Format:"" Descr:""
    defaultAiServer: Optional[str]  # Format:"" Descr:"The id of the default ai server of the tenant"
    userDefaultsOverridable: Optional[bool]  # Format:"" Descr:""
    

class AdminTypeApiData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AdminTypeApiData.htm
    """
    userId: str  # Format:"" Descr:"The user's system ID"
    adminType: AdminType  # Format:"" Descr:"An enum of the administration type"
    

class ChangeItemDescriptionData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ChangeItemDescriptionData.htm
    """
    itemId: str  # Format:"" Descr:"The content item's system ID"
    description: str  # Format:"" Descr:"The description for the content item"
    

class ChangeUserLicenseData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ChangeUserLicenseData.htm
    """
    userId: str  # Format:"" Descr:"The user's system ID"
    licenseType: ClientLicenseType  # Format:"" Descr:"An enum of the license type"
    tenantId: Optional[str]  # Format:"" Descr:""
    

class ChangeUserLicenseObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ChangeUserLicenseObject.htm
    """
    userId: str  # Format:"" Descr:"The user's system ID"
    licenseType: ClientLicenseType  # Format:"" Descr:"An enum of the license type"
    

class ConnStringDscApiObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ConnStringDscApiObject.htm
    """
    connectionStringProperties: Optional[ConnectionStringProperties]  # Format:"" Descr:"The connection strings object"
    needsToPerformDsc: Optional[bool]  # Format:"" Descr:"A boolean to denote if the data source changer is required or not"
    

class ConnectedItemsSearchCriteria(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ConnectedItemsSearchCriteria.htm
    """
    dataContainerId: str  # Format:"" Descr:"This is the container or 'parent' system ID: If searching for databases, this is the data source server's ID. If searching for materialized models, its the data source database's ID"
    searchCriteria: SearchCriteria  # Format:"" Descr:"Search criteria object for specifying search conditions and strings"
    

class ConnectionStringProperties(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ConnectionStringProperties.htm
    """
    id: Optional[str]  # Format:"" Descr:"The connection object's system ID"
    modelId: Optional[str]  # Format:"" Descr:"The materialized model's system ID"
    modelName: Optional[str]  # Format:"" Descr:"The model's name"
    serverId: Optional[str]  # Format:"" Descr:"The data source  server's system ID"
    serverName: Optional[str]  # Format:"" Descr:"The data source server's name"
    dataBaseId: Optional[str]  # Format:"" Descr:"The data source  database's system ID"
    dataBaseName: Optional[str]  # Format:"" Descr:"The data source database's name"
    connectionStringType: Optional[ConnectionStringType]  # Format:"" Descr:"The type of connection"
    isDynamicModel: Optional[bool]  # Format:"" Descr:"Boolean showing if a model is dynamic"
    modelParamsStatus: Optional[str]  # Format:"" Descr:""
    securityHash: Optional[str]  # Format:"" Descr:""
    

class ContentSearchParamsObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ContentSearchParamsObject.htm
    """
    searchString: str  # Format:"" Descr:"The terms to be used in the search"
    isAdvancedSearch: Optional[bool]  # Format:"" Descr:"Boolean to indicate if this is an advanced search. Advanced searches will use other provided criteria. Otherwise, the simple search will just use the search string only"
    filterTypes: List[ContentTypeObject]  # Format:"" Descr:"A listing of different content types to narrow the search"
    searchMatchType: SearchMatchType  # Format:"" Descr:"Enumeration of the type osf search term matching"
    startCreatedDate: Optional[str]  # Format:"date-time" Descr:"Starting date for range searching on create dates"
    endCreatedDate: Optional[str]  # Format:"date-time" Descr:"Ending date for range searching on create dates"
    startModifiedDate: Optional[str]  # Format:"date-time" Descr:"Starting date for range searching on modified dates"
    endModifiedDate: Optional[str]  # Format:"date-time" Descr:"Ending date for range searching on modified dates"
    server: Optional[str]  # Format:"" Descr:"Server name when searching by data source"
    model: Optional[str]  # Format:"" Descr:"Model name when searching by data source"
    dataBase: Optional[str]  # Format:"" Descr:"Database name when searching by data source"
    searchRootFolderType: SearchRootFolderType  # Format:"" Descr:"Enumeration of which content domain to search in (private, public etc)"
    folderPathToSearch: Optional[str]  # Format:"" Descr:"This is a folder path to use in searching. Use in the format folderA\folderB\..... using the folder captions, not their IDs"
    

class CreateUserAdObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CreateUserAdObject.htm
    """
    id: str  # Format:"uuid" Descr:"The user's system ID."
    userName: str  # Format:"" Descr:"The login username for the user"
    adminType: Optional[AdminType]  # Format:"" Descr:"The user's administration level using the admin type enumeration"
    roleIds: Optional[List[str]]  # Format:"" Descr:"The user's list of roles"
    clientLicenseType: ClientLicenseType  # Format:"" Descr:"The user's license type using the type enumeration"
    statusID: Optional[UserStatusID]  # Format:"" Descr:"The user's status using the status type enumeration"
    tenantId: Optional[str]  # Format:"" Descr:"The user's tenant ID"
    adDomainName: str  # Format:"" Descr:"The domain net bios"
    profileId: Optional[str]  # Format:"" Descr:"The profile ID to be applied for this user"
    

class CreateUserDbObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CreateUserDbObject.htm
    """
    id: Optional[str]  # Format:"uuid" Descr:"The user ID. If provided, the GUID will be used. Otherwise, the function will auto-create it."
    userName: str  # Format:"" Descr:"The login username for the user"
    firstName: Optional[str]  # Format:"" Descr:"User's first name"
    lastName: Optional[str]  # Format:"" Descr:"User's last name"
    email: Optional[str]  # Format:"" Descr:"User's email address - needed for automation and messaging"
    proxyAccount: Optional[str]  # Format:"" Descr:"The user's proxy account needed for connecting to different data sources"
    adminType: AdminType  # Format:"" Descr:"Set the user's administration level using the admin type enumeration"
    roleIds: Optional[List[str]]  # Format:"" Descr:"The user's roles using role ID's"
    clientLicenseType: ClientLicenseType  # Format:"" Descr:"The user's license type using the type enumeration"
    statusID: UserStatusID  # Format:"" Descr:"The user's status using the status type enumeration"
    tenantId: Optional[str]  # Format:"" Descr:"The user's tenancy if using multi-tenancy. If not, use the default tenancy of '90000000-0000-0000-0000-000000000009'"
    privateProfileId: Optional[str]  # Format:"" Descr:"The user's Profile Id"
    password: str  # Format:"" Descr:"User's password. The user can manually change their password later if enabled from the admin"
    phone: Optional[str]  # Format:"" Descr:"User's phone - needed for automation and messaging"
    

class CreateUserOpenIdObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CreateUserOpenIdObject.htm
    """
    id: Optional[str]  # Format:"uuid" Descr:"The user ID. If provided, the GUID will be used. Otherwise, the function will auto-create it."
    userName: str  # Format:"" Descr:"The login username for the user"
    firstName: Optional[str]  # Format:"" Descr:"User's first name"
    lastName: Optional[str]  # Format:"" Descr:"User's last name"
    email: Optional[str]  # Format:"" Descr:"User's email address - needed for automation and messaging"
    proxyAccount: Optional[str]  # Format:"" Descr:"The user's proxy account needed for connecting to different data sources"
    adminType: AdminType  # Format:"" Descr:"Set the user's administration level using the admin type enumeration"
    roleIds: Optional[List[str]]  # Format:"" Descr:"The user's roles using role ID's"
    clientLicenseType: ClientLicenseType  # Format:"" Descr:"The user's license type using the type enumeration"
    statusID: UserStatusID  # Format:"" Descr:"The user's status using the status type enumeration"
    tenantId: Optional[str]  # Format:"" Descr:"The user's tenancy if using multi-tenancy. If not, use the default tenancy of '90000000-0000-0000-0000-000000000009'"
    privateProfileId: Optional[str]  # Format:"" Descr:"The user's Profile Id"
    principalName: Optional[str]  # Format:"" Descr:"The user's OpenID principal name identifier"
    password: Optional[str]  # Format:"" Descr:"User's password. relevant only for enterprise admin users"
    phone: Optional[str]  # Format:"" Descr:"User's phone - needed for automation and messaging"
    

class CreateUserSamlObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CreateUserSamlObject.htm
    """
    id: Optional[str]  # Format:"uuid" Descr:"The user ID. If provided, the GUID will be used. Otherwise, the function will auto-create it."
    userName: str  # Format:"" Descr:"The login username for the user"
    firstName: Optional[str]  # Format:"" Descr:"User's first name"
    lastName: Optional[str]  # Format:"" Descr:"User's last name"
    email: Optional[str]  # Format:"" Descr:"User's email address - needed for automation and messaging"
    proxyAccount: Optional[str]  # Format:"" Descr:"The user's proxy account needed for connecting to different data sources"
    adminType: AdminType  # Format:"" Descr:"Set the user's administration level using the admin type enumeration"
    roleIds: Optional[List[str]]  # Format:"" Descr:"The user's roles using role ID's"
    clientLicenseType: ClientLicenseType  # Format:"" Descr:"The user's license type using the type enumeration"
    statusID: UserStatusID  # Format:"" Descr:"The user's status using the status type enumeration"
    tenantId: Optional[str]  # Format:"" Descr:"The user's tenancy if using multi-tenancy. If not, use the default tenancy of '90000000-0000-0000-0000-000000000009'"
    privateProfileId: Optional[str]  # Format:"" Descr:"The user's Profile Id"
    principalName: Optional[str]  # Format:"" Descr:"The user's SAML identifier"
    password: Optional[str]  # Format:"" Descr:"User's password. relevant only for enterprise admin users"
    phone: Optional[str]  # Format:"" Descr:"User's phone - needed for automation and messaging"
    

class DataBaseRecognitionObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DataBaseRecognitionObject.htm
    """
    serverId: str  # Format:"" Descr:"The data source server's ID"
    dbName: str  # Format:"" Descr:"The name of the database"
    

class DataSourceTableResult(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DataSourceTableResult.htm
    """
    tableName: Optional[str]  # Format:"" Descr:"The table name."
    schemaName: Optional[str]  # Format:"" Descr:"The schema name."
    

class DataSourceUsedTablesResult(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DataSourceUsedTablesResult.htm
    """
    tables: List[DataSourceTableResult]  # Format:"" Descr:"List of tables. Each table contains table name and schema name."
    

class DeleteHierarchyOverlayApiObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DeleteHierarchyOverlayApiObject.htm
    """
    modelId: str  # Format:"" Descr:"The model's ID"
    roleId: str  # Format:"" Descr:"The role id the overlays apply to"
    overlayPropertiesToDelete: List[HierarchyOverlayToDeleteData]  # Format:"" Descr:"The overlay properties to delete"
    

class DeleteTenantApiData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DeleteTenantApiData.htm
    """
    tenantIds: List[str]  # Format:"" Descr:"A list of tenant ID's"
    deleteUsers: bool  # Format:"" Descr:"A boolean flag to mark if related users should be deleted as well"
    deleteServers: bool  # Format:"" Descr:"A boolean flag to mark if related data servers should be deleted as well"
    

class DomainSecurityObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DomainSecurityObject.htm
    """
    securityType: SecurityType  # Format:"" Descr:"Enumeration of the domain server type"
    securedModelEnabled: Optional[bool] = False # Format:"" Descr:"Default:FALSE"
    secureSocketsLayerEnabled: Optional[bool] = True # Format:"" Descr:"Default:TRUE"
    port: Optional[int]  # Format:"int32" Descr:"Default LDAP:389, LDAPS:636"
    ldapAddress: str  # Format:"" Descr:"LDAP address"
    domainName: str  # Format:"" Descr:"Domain name"
    defaultDomain: Optional[bool] = False # Format:"" Descr:"Default:FALSE"
    domainUserName: str  # Format:"" Descr:"Domain user account"
    domainUserPassword: str  # Format:"" Descr:"Domain user account password"
    domainUserDomainName: Optional[str]  # Format:"" Descr:"Default:domainName"
    

class MasterFlowSourceObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowSourceObject.htm
    """
    masterFlowNodeId: Optional[str]  # Format:"" Descr:"Master Flow node id"
    masterFlowNodeName: Optional[str]  # Format:"" Descr:"Master Flow node name"
    dataFlowNodeId: Optional[str]  # Format:"" Descr:"Data Flow node id"
    description: Optional[str]  # Format:"" Descr:"Description of the data flow node"
    serverId: Optional[str]  # Format:"" Descr:"Server id"
    serverName: Optional[str]  # Format:"" Descr:"Server name"
    serverType: Optional[ConnectionStringType]  # Format:"" Descr:"Server Type - one of the ConnectionStringType enumeration"
    databaseName: Optional[str]  # Format:"" Descr:"Database name"
    validationMessage: Optional[str]  # Format:"" Descr:"Validation message"
    

class MasterFlowOtherObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowOtherObject.htm
    """
    masterFlowNodeId: Optional[str]  # Format:"" Descr:"Master Flow node ID"
    masterFlowNodeName: Optional[str]  # Format:"" Descr:"Master Flow node name"
    dataFlowNodeId: Optional[str]  # Format:"" Descr:"Data Flow node ID"
    dataFlowNodeType: Optional[str]  # Format:"" Descr:"Data Flow node type"
    dataFlowNodeName: Optional[str]  # Format:"" Descr:"Data Flow node name"
    description: Optional[str]  # Format:"" Descr:"Description of the data flow node"
    validationMessage: Optional[str]  # Format:"" Descr:"Validation message"
    

class MasterFlowTargetObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowTargetObject.htm
    """
    masterFlowNodeId: Optional[str]  # Format:"" Descr:"Master Flow node id"
    masterFlowNodeName: Optional[str]  # Format:"" Descr:"Master Flow node name"
    dataFlowNodeId: Optional[str]  # Format:"" Descr:"Data Flow node id"
    description: Optional[str]  # Format:"" Descr:"Description of the data flow node"
    serverId: Optional[str]  # Format:"" Descr:"Server id"
    serverName: Optional[str]  # Format:"" Descr:"Server name"
    serverType: Optional[ConnectionStringType]  # Format:"" Descr:"Server Type - one of the ConnectionStringType enumeration"
    createNewDb: Optional[bool]  # Format:"" Descr:"Create a new database or use existing one"
    databaseName: Optional[str]  # Format:"" Descr:"Database name"
    validationMessage: Optional[str]  # Format:"" Descr:"Validation message"
    

class MasterFlowVariableObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowVariableObject.htm
    """
    variableId: Optional[str]  # Format:"" Descr:"Variable ID"
    variableName: Optional[str]  # Format:"" Descr:"Variable name"
    serverId: Optional[str]  # Format:"" Descr:"The ID of the server where the variable is stored"
    serverName: Optional[str]  # Format:"" Descr:"The name of the server where the variable is stored"
    serverType: Optional[ConnectionStringType]  # Format:"" Descr:"Server Type - one of the ConnectionStringType enumeration"
    databaseName: Optional[str]  # Format:"" Descr:"Database name"
    validationMessage: Optional[str]  # Format:"" Descr:"Validation message"
    variableCurrentValue: Optional[str]  # Format:"" Descr:"Variable current value"
    variableDataType: Optional[str]  # Format:"" Descr:"Variable data type"
    variableType: Optional[str]  # Format:"" Descr:"Variable type - single value or list"
    

class DscApiData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DscApiData.htm
    """
    fromConnId: str  # Format:"" Descr:"The connection ID of the data source to change FROM"
    toConnId: str  # Format:"" Descr:"The connection ID of the data source to change TO"
    itemId: str  # Format:"" Descr:"The content item's system ID"
    

class MasterFlowValidationResult(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowValidationResult.htm
    """
    sources: Optional[List[MasterFlowSourceObject]]  # Format:"" Descr:"Validation results for sources objects"
    targets: Optional[List[MasterFlowTargetObject]]  # Format:"" Descr:"Validation results for targets objects"
    others: Optional[List[MasterFlowOtherObject]]  # Format:"" Descr:"Validation results for other objects"
    variables: Optional[List[MasterFlowVariableObject]]  # Format:"" Descr:"Validation results for variables objects"
    

class ExecuteMasterFlowObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ExecuteMasterFlowObject.htm
    """
    itemId: str  # Format:"" Descr:"The ID depends on the source: For Model files it is the item's system ID. For materialized/deployed models it is its materialized model ID."
    executionTitle: Optional[str]  # Format:"" Descr:"A title to describe the execution of the job."
    syncModelColumnsType: Optional[EtlSyncModelColumnsType]  # Format:"" Descr:"In the case of adding or removing columns in the database, the model columns can be synchronized according to this property."
    

class ExecuteMasterFlowResult(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ExecuteMasterFlowResult.htm
    """
    scheduleId: Optional[str]  # Format:"" Descr:"Schedule's system ID"
    masterFlowValidationResult: Optional[MasterFlowValidationResult]  # Format:"" Descr:"Master Flow validation result"
    valid: Optional[bool]  # Format:"" Descr:""
    

class TaskViewData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TaskViewData.htm
    """
    id: Optional[str]  # Format:"" Descr:"The tasks's system ID"
    outputId: Optional[str]  # Format:"" Descr:"The tasks's first output ID, there could be multiple outputs"
    executorId: Optional[str]  # Format:"" Descr:"The tasks's executor's ID"
    description: Optional[str]  # Format:"" Descr:"The tasks's description"
    status: Optional[TaskStatus]  # Format:"" Descr:"The tasks's status enumeration"
    resultType: Optional[ScheduleResultType]  # Format:"" Descr:"The tasks's result type enumeration"
    result: Optional[str]  # Format:"" Descr:"The tasks's result"
    summary: Optional[str]  # Format:"" Descr:"The tasks's summary"
    taskSummary: Optional[TaskSummary]  # Format:"" Descr:"The tasks's summary detailed object"
    startDate: Optional[str]  # Format:"date-time" Descr:"The task's start date"
    endDate: Optional[str]  # Format:"date-time" Descr:"The task's end date"
    

class ExecuteScheduleApiData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ExecuteScheduleApiData.htm
    """
    scheduleId: str  # Format:"" Descr:"The schedule's system ID"
    checkTriggers: Optional[bool]  # Format:"" Descr:"Boolean to include a schedule's trigger logic for execution. Set to false to ignore triggers"
    

class ExecutionViewData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ExecutionViewData.htm
    """
    id: Optional[str]  # Format:"" Descr:"The execution's system ID"
    startDate: Optional[str]  # Format:"date-time" Descr:"The execution's start date"
    endDate: Optional[str]  # Format:"date-time" Descr:"The execution's end date"
    outputType: Optional[PrintingOutputType]  # Format:"" Descr:"The type's of output enumeration"
    successPct: Optional[float]  # Format:"float" Descr:"Percentage of the execution's tasks that succeeded"
    successCount: Optional[int]  # Format:"int32" Descr:""
    partialSuccessPct: Optional[float]  # Format:"float" Descr:"Percentage of the execution's tasks that partially succeeded"
    partialSuccessCount: Optional[int]  # Format:"int32" Descr:""
    failedPct: Optional[float]  # Format:"float" Descr:"Percentage of the execution's tasks that failed"
    failedCount: Optional[int]  # Format:"int32" Descr:""
    canceledPct: Optional[float]  # Format:"float" Descr:"Percentage of the execution's tasks that were canceled"
    canceledCount: Optional[int]  # Format:"int32" Descr:""
    runningPct: Optional[float]  # Format:"float" Descr:"Percentage of the execution's tasks that are running"
    runningCount: Optional[int]  # Format:"int32" Descr:""
    pendingPct: Optional[float]  # Format:"float" Descr:"Percentage of the execution's tasks that are pending"
    pendingCount: Optional[int]  # Format:"int32" Descr:""
    triggerStoppedPct: Optional[float]  # Format:"float" Descr:"Percentage of the execution's tasks that stopped after trigger evaluation"
    triggerStoppedCount: Optional[int]  # Format:"int32" Descr:""
    items: Optional[List[TaskViewData]]  # Format:"" Descr:"The a list of tasks in the execution"
    error: Optional[str]  # Format:"" Descr:""
    

class ExportData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ExportData.htm
    """
    fileName: Optional[str]  # Format:"" Descr:"The file name of the exported data"
    fileData: Optional[str]  # Format:"" Descr:"The encrypted file as Base64"
    

class FilterParameter(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/FilterParameter.htm
    """
    value: Optional[str]  # Format:"" Descr:"The filter string"
    

class TargetParameter(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TargetParameter.htm
    """
    name: Optional[str]  # Format:"" Descr:"The target's string"
    filters: Optional[List[FilterParameter]]  # Format:"" Descr:"A list of filter strings"
    syntaxType: Optional[SyntaxType]  # Format:"" Descr:"The target's syntax type (PQL, MS, BW)"
    

class ExportOptions(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ExportOptions.htm
    """
    showUniqueName: Optional[bool]  # Format:"" Descr:"Boolean to show or hide unique names in the exported results"
    columnHeaderAsCaption: Optional[bool]  # Format:"" Descr:"Boolean to add the column caption as the first row after the unique names"
    

class ExternalParameters(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ExternalParameters.htm
    """
    reportFilters: Optional[List[FilterParameter]]  # Format:"" Descr:"A list of filter parameters for the report"
    targets: Optional[List[TargetParameter]]  # Format:"" Descr:"A list of target parameters for the report/presentation"
    slideNumber: Optional[int]  # Format:"int32" Descr:"The slide number that will be opened"
    

class FolderTenantObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/FolderTenantObject.htm
    """
    validRootFolderType: ValidRootFolderType  # Format:"" Descr:"The type of root folder"
    tenantId: str  # Format:"" Descr:"Then tenant's ID"
    

class HierarchyMeasureSecurity(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/HierarchyMeasureSecurity.htm
    """
    modelId: str  # Format:"" Descr:"The model's ID"
    roleId: str  # Format:"" Descr:"The role id the settings apply to"
    uniqueNames: List[str]  # Format:"" Descr:"The unique names of the items, in a list. Use hierarchies for hierarchy security, use measures for measures security"
    

class HierarchyMeasureSecurityApiObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/HierarchyMeasureSecurityApiObject.htm
    """
    modelId: str  # Format:"" Descr:"The model's ID"
    roleId: str  # Format:"" Descr:"The role id the settings apply to"
    uniqueNames: List[str]  # Format:"" Descr:"The unique names of the items, in a list. Use hierarchies for hierarchy security, use measures for measures security"
    enableMode: bool  # Format:"" Descr:"Set to true for 'Enable' mode. Set to false for 'Disable' mode."
    

class HierarchyOverlayData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/HierarchyOverlayData.htm
    """
    uniqueName: str  # Format:"" Descr:"The unique name of the hierarchy that the overlays apply to"
    displayFolder: Optional[str]  # Format:"" Descr:"The display folder of the hierarchy"
    description: Optional[str]  # Format:"" Descr:"The description of the hierarchy"
    alternativeName: Optional[str]  # Format:"" Descr:"The alternative name of the hierarchy"
    type: Optional[ModelingColumnCategories]  # Format:"" Descr:"The type of the hierarchy"
    

class HierarchyOverlayToDeleteData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/HierarchyOverlayToDeleteData.htm
    """
    uniqueName: str  # Format:"" Descr:"The unique name of the hierarchy"
    propertiesToDelete: Optional[List[HierarchyOverlayProperty]]  # Format:"" Descr:"The list of properties to delete from the hierarchy overlay."
    

class ImportApiResultObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ImportApiResultObject.htm
    """
    importDscMap: Optional[Optional[Dict[str,List[ConnStringDscApiObject]]]]  # Format:"" Descr:"A 'map' of the content items and their matching connection strings needed for data source management"
    itemsIds: Optional[Dict[str,str]]  # Format:"" Descr:"A 'map' of the ids of all items in the source & the destination"
    failedItems: Optional[List['RelatedItemData']]  # Format:"" Descr:"A 'list' of the content items that failed to be imported"
    

class ItemId(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ItemId.htm
    """
    id: Optional[str]  # Format:"" Descr:"The item's ID."
    name: Optional[str]  # Format:"" Descr:"The name of the item only when relevant."
    

class ItemParentApiData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ItemParentApiData.htm
    """
    itemId: str  # Format:"" Descr:"The content item's system ID"
    parentId: str  # Format:"" Descr:"The content item's parent system ID"
    

class ItemRolePair(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ItemRolePair.htm
    """
    roleId: str  # Format:"" Descr:"Role's system ID"
    accessType: AccessType  # Format:"" Descr:"Enumeration of role access types"
    

class ItemRolesForRemoval(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ItemRolesForRemoval.htm
    """
    itemId: str  # Format:"" Descr:"The item's system ID"
    roleIds: List[str]  # Format:"" Descr:"The listing of roles to be removed"
    

class ItemRolesToBeAdded(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ItemRolesToBeAdded.htm
    """
    itemId: str  # Format:"" Descr:"The item's system ID"
    itemRolePairList: List[ItemRolePair]  # Format:"" Descr:"The listing of roles and their access levels"
    serverId: Optional[str]  # Format:"" Descr:"The data server's ID"
    databaseId: Optional[str]  # Format:"" Descr:"The database's ID"
    modelId: Optional[str]  # Format:"" Descr:"The data model's ID"
    

class ItemsForFavorites(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ItemsForFavorites.htm
    """
    userId: str  # Format:"" Descr:"The system user ID"
    itemIds: List[str]  # Format:"" Descr:"The list of content item IDs to mark as 'favorites'"
    

class LdapGroupDetails(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/LdapGroupDetails.htm
    """
    samAccountName: Optional[str]  # Format:"" Descr:"The group's AD account name"
    name: str  # Format:"" Descr:"The group's name"
    guid: str  # Format:"" Descr:"The group's AD GUID"
    sid: str  # Format:"" Descr:"The group's AD SID"
    domainAddress: str  # Format:"" Descr:"The group's LDAP domain address"
    

class LdapGroupIdentifier(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/LdapGroupIdentifier.htm
    """
    domainNetBios: str  # Format:"" Descr:"Domain name"
    groupName: str  # Format:"" Descr:"Group's AD/LDAP name"
    

class LdapSearchObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/LdapSearchObject.htm
    """
    domainNetBios: str  # Format:"" Descr:"The AD domain"
    searchValue: str  # Format:"" Descr:"The search string"
    searchType: LdapSearchType  # Format:"" Descr:"Enumeration of string search types"
    

class LdapUserObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/LdapUserObject.htm
    """
    firstName: Optional[str]  # Format:"" Descr:"The user's first name"
    lastName: Optional[str]  # Format:"" Descr:"The user's last name"
    userName: Optional[str]  # Format:"" Descr:"The user's account name"
    domain: Optional[str]  # Format:"" Descr:"The user's domain"
    principalName: Optional[str]  # Format:"" Descr:"The user's user principal name"
    

class LdapUsersSearchObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/LdapUsersSearchObject.htm
    """
    domainNetBios: str  # Format:"" Descr:"The domain name"
    searchValue: str  # Format:"" Descr:"The search string to be used in the search"
    ldapSearchType: LdapSearchType  # Format:"" Descr:"The search type using the type enumeration"
    

class LicenseCountObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/LicenseCountObject.htm
    """
    totalViewerSeats: Optional[int]  # Format:"int32" Descr:"The total number of viewer licenses for the tenant"
    totalProSeats: Optional[int]  # Format:"int32" Descr:"The total number of professional licenses for the tenant"
    

class MasterFlowFindDataSourceObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowFindDataSourceObject.htm
    """
    itemId: str  # Format:"" Descr:"The item's system ID."
    dataFlowNodeId: str  # Format:"" Descr:"Data Flow node's ID. The ID can be found in the node's property pane within the 'description' card."
    

class MasterFlowModelNameObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowModelNameObject.htm
    """
    itemId: str  # Format:"" Descr:"The ID depends on the source: For Model files it is the item's system ID. For materialized/deployed models it is its materialized model ID."
    masterFlowModelNodeId: str  # Format:"" Descr:"The master flow model node ID."
    newModelName: str  # Format:"" Descr:"The new model name."
    

class MasterFlowProgressResult(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowProgressResult.htm
    """
    taskStatus: Optional[TaskStatus]  # Format:"" Descr:"The task status"
    message: Optional[str]  # Format:"" Descr:"Attached message to the task status"
    errors: Optional[List[str]]  # Format:"" Descr:"Attached errors to the task status"
    

class MasterFlowSchemasObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowSchemasObject.htm
    """
    itemId: str  # Format:"" Descr:"The ID depends on the source: For Model files it is the item's system ID. For materialized/deployed models it is its materialized model ID."
    dataFlowNodeId: str  # Format:"" Descr:"Data Flow node's ID. The ID can be found in the node's property pane within the 'description' card. For materialized/deployed model of direct query, this value can by blank."
    fromSchema: str  # Format:"" Descr:"Current schema name."
    toSchema: str  # Format:"" Descr:"New schema name."
    schemaValidation: Optional[str]  # Format:"" Descr:"Define whether to check if the new schema exists, before changing."
    

class MasterFlowSourceConnectionObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowSourceConnectionObject.htm
    """
    dataFlowNodeId: str  # Format:"" Descr:"The data flow node ID."
    serverId: Optional[str]  # Format:"" Descr:"The new server ID. The original server ID will be used if this is left empty."
    databaseName: Optional[str]  # Format:"" Descr:"The new database name. The original database name will be used if this is left empty."
    itemId: str  # Format:"" Descr:"The ID depends on the source: For Model files it is the item's system ID. For materialized/deployed models it is its materialized model ID."
    

class MasterFlowTargetConnectionObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowTargetConnectionObject.htm
    """
    dataFlowNodeId: str  # Format:"" Descr:"The data flow node ID."
    serverId: Optional[str]  # Format:"" Descr:"The new server ID. The original server ID will be used if this is left empty."
    databaseName: Optional[str]  # Format:"" Descr:"The new database name. The original database name will be used if this is left empty."
    itemId: str  # Format:"" Descr:"The item's system ID."
    useExistingDatabase: Optional[bool]  # Format:"" Descr:"Flag to use the existing database or not"
    

class MasterFlowUpdatedVariableResult(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowUpdatedVariableResult.htm
    """
    results: Optional[List[ApiModifierResultString]]  # Format:"" Descr:"List of result. each result shows the updated response - success or error message."
    

class MasterFlowVariableConnectionObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowVariableConnectionObject.htm
    """
    itemId: str  # Format:"" Descr:"The ID depends on the source: For Model files it is the item's system ID. For materialized/deployed models it is its materialized model ID."
    variableName: str  # Format:"" Descr:"The variable's unique name."
    serverId: Optional[str]  # Format:"" Descr:"The new server ID. The original server ID will be used if this is left empty."
    databaseName: Optional[str]  # Format:"" Descr:"The new database name. The original database name will be used if this is left empty."
    

class MasterFlowVariableValueObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowVariableValueObject.htm
    """
    itemId: str  # Format:"" Descr:"The ID depends on the source: For Model files it is the item's system ID. For materialized/deployed models it is its materialized model ID."
    variableName: Optional[str]  # Format:"" Descr:"The variable's name."
    variableValue: Optional[str]  # Format:"" Descr:"New value."
    

class MasterFlowVariablesResult(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowVariablesResult.htm
    """
    variablesObjects: List[MasterFlowVariableObject]  # Format:"" Descr:"List of MasterFlowVariableObject. Each object contains a variable and its datasource details."
    

class MasterFlowVariablesValueObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowVariablesValueObject.htm
    """
    variableValueList: List[MasterFlowVariableValueObject]  # Format:"" Descr:"List of Variables to update."
    

class MaterializedApiObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MaterializedApiObject.htm
    """
    fileZippedData: str  # Format:"" Descr:"The PIE file contents (base64 data payload)"
    databaseId: str  # Format:"" Descr:""
    materializedRoleAssignmentType: MaterializedRoleAssignmentType  # Format:"" Descr:"The settings for how to set roles on imported model. Default:UseDefaultBehavior"
    rolesIds: Optional[List[str]]  # Format:"" Descr:"The roles ID's to be applied to the imported content. Relevant only for 'MaterializedRoleAssignmentType.ForceExternalRoles'"
    

class ModelDataFlowSourceInfo(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelDataFlowSourceInfo.htm
    """
    flowId: Optional[str]  # Format:"uuid" Descr:"Source Data Flow system ID"
    flowDestinationNodeId: Optional[str]  # Format:"uuid" Descr:"Destination node system ID from the source Data Flow"
    

class MaterializedItemObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MaterializedItemObject.htm
    """
    itemId: Optional[str]  # Format:"" Descr:"The item's system ID"
    itemCaption: Optional[str]  # Format:"" Descr:"The item's name or caption"
    itemType: Optional[MaterializedItemType]  # Format:"" Descr:"The item's enumerated type"
    

class MeasureGroup(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MeasureGroup.htm
    """
    Name: Optional[str]  # Format:"" Descr:"Measure group name"
    Caption: Optional[str]  # Format:"" Descr:"Measure group caption"
    Description: Optional[str]  # Format:"" Descr:"Measure group description"
    

class MembersSecurity(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MembersSecurity.htm
    """
    modelId: str  # Format:"" Descr:"The model's ID"
    roleId: str  # Format:"" Descr:"The role id that the settings apply to"
    hierarchyUniqueName: str  # Format:"" Descr:"The unique name of the hierarchy that contain the members"
    

class MembersSecurityApiObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MembersSecurityApiObject.htm
    """
    modelId: str  # Format:"" Descr:"The model's ID"
    roleId: str  # Format:"" Descr:"The role id that the settings apply to"
    hierarchyUniqueName: str  # Format:"" Descr:"The unique name of the hierarchy that contain the members"
    enableMode: bool  # Format:"" Descr:"Set to true for 'Enabled' (included) mode. Set to false for 'Disabled' (excluded) mode."
    visualTotals: Optional[bool]  # Format:"" Descr:"Enable or disable visual totals. Relevant in parent-child hierarchies security only."
    members: Optional[List[str]]  # Format:"" Descr:"A listing of the unique names of members that need to be secured."
    script: Optional[str]  # Format:"" Descr:"The PQL script to be used to evaluate the member listing that needs to be secured."
    

class ModelingProperty(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelingProperty.htm
    """
    uniqueName: Optional[str]  # Format:"" Descr:"Unique Name of the property column"
    caption: Optional[str]  # Format:"" Descr:"Caption of the property column"
    sourceColumnUniqueName: Optional[str]  # Format:"" Descr:"Unique identifier of this property's source column"
    shortCaption: Optional[str]  # Format:"" Descr:"shortened caption of the property column"
    subProps: Optional[List['ModelingProperty']]  # Format:"" Descr:"A property column of another column, example: state could have country as a property"
    name: Optional[str]  # Format:"" Descr:""
    displayName: Optional[str]  # Format:"" Descr:""
    modelAttributeType: Optional[ModelAttributeType]  # Format:"" Descr:"-"
    

class ModelRecognitionObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelRecognitionObject.htm
    """
    serverId: str  # Format:"" Descr:"The data source server's ID"
    databaseName: str  # Format:"" Descr:"The name of the database"
    modelName: str  # Format:"" Descr:"The name of the model (existing OLAP cube, tabular model or view)"
    dynamicModel: Optional[bool]  # Format:"" Descr:""
    

class ModelingHierarchyLevel(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelingHierarchyLevel.htm
    """
    levelId: Optional[str]  # Format:"uuid" Descr:"System ID of this hierarchy level"
    levelNumber: Optional[int]  # Format:"int32" Descr:"Level number"
    uniqueName: Optional[str]  # Format:"" Descr:"Unique identifier of this hierarchy level"
    displayName: Optional[str]  # Format:"" Descr:"Display name of this hierarchy level"
    sourceColumnUniqueName: Optional[str]  # Format:"" Descr:"Unique identifier of this level's source column"
    customCategoryId: Optional[str]  # Format:"" Descr:"User-defined category of this hierarchy level"
    description: Optional[str]  # Format:"" Descr:"Description of this hierarchy level"
    sortByColumn: Optional[str]  # Format:"" Descr:"column unique name to sort by"
    isDefaultSortDescending: Optional[bool]  # Format:"" Descr:"Is the default sorting descending"
    properties: Optional[List['ModelingProperty']]  # Format:"" Descr:"Modeling properties of this hierarchy level"
    hideMemberType: Optional[HideMemberType]  # Format:"" Descr:"When to hide a member on this level"
    

class ModelingColumn(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelingColumn.htm
    """
    columnId: Optional[str]  # Format:"uuid" Descr:"The column's system ID"
    displayName: Optional[str]  # Format:"" Descr:"The column's display name"
    description: Optional[str]  # Format:"" Descr:"The column's description"
    format: Optional[str]  # Format:"" Descr:"The column's data format"
    uniqueName: Optional[str]  # Format:"" Descr:"The column's unique identifier, used in relationships, hierarchies and measures"
    parentUniqueName: Optional[str]  # Format:"" Descr:"Unique identifier of the table that contains this column"
    sourceColumnName: Optional[str]  # Format:"" Descr:"The column's name in the database"
    type: Optional[str]  # Format:"" Descr:"The column's data type"
    defaultSortColumnUniqueName: Optional[str]  # Format:"" Descr:"Unique identifier of the default column to sort by when the user sorts by this column"
    isDefaultSortDescending: Optional[bool]  # Format:"" Descr:"Is the default sorting descending"
    size: Optional[int]  # Format:"int32" Descr:"Size of the source column type (string length or decimal precision)"
    scale: Optional[int]  # Format:"int32" Descr:"Scale of the source column type (if decimal)"
    isVisible: Optional[bool]  # Format:"" Descr:"Is the column displayed in the"
    isSecurity: Optional[bool]  # Format:"" Descr:"Is this a column used in the security panel"
    isDistribution: Optional[bool]  # Format:"" Descr:"Is column for publication distribution"
    displayFolder: Optional[str]  # Format:"" Descr:"Column's display folder name"
    isIndexed: Optional[bool]  # Format:"" Descr:"Is this column indexed in the source database"
    columnIndex: Optional[int]  # Format:"int32" Descr:"Index of this column in the table, start at 0"
    hasMultiMeasures: Optional[bool]  # Format:"" Descr:"Boolean indicating if this column has multi-measures"
    isAggregatable: Optional[bool]  # Format:"" Descr:"Can this column be aggregated"
    columnCategory: Optional[ModelingColumnCategories]  # Format:"" Descr:"Predefined category of this column (time intelligence part, location part, etc)"
    customCategoryId: Optional[str]  # Format:"" Descr:"User defined category of this column"
    keyColumn: Optional[str]  # Format:"" Descr:"Unique identifier of the key column for this column"
    hasDefaultMember: Optional[bool]  # Format:"" Descr:"Does this column has a default member"
    

class ModelingRelationshipColumnPair(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelingRelationshipColumnPair.htm
    """
    primaryColumnUniqueName: Optional[str]  # Format:"" Descr:"The primary column's unique name"
    foreignColumnUniqueName: Optional[str]  # Format:"" Descr:"The foreign column's unique name"
    operatorType: Optional[OperatorType]  # Format:"" Descr:"The Operator Type (Equals, Greater, Less, GreaterOrEqual, LessOrEqual, NotEqual, Between direction is: primaryColumnUniqueName  operatorType  foreignColumnUniqueName)"
    

class ModelingHierarchy(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelingHierarchy.htm
    """
    hierarchyId: Optional[str]  # Format:"uuid" Descr:"The hierarchy's System ID"
    levels: Optional[List[ModelingHierarchyLevel]]  # Format:"" Descr:"The hierarchy levels"
    displayName: Optional[str]  # Format:"" Descr:"The hierarchy's Display Name"
    uniqueName: Optional[str]  # Format:"" Descr:"The hierarchy's Unique identifier"
    displayFolder: Optional[str]  # Format:"" Descr:"The hierarchy's display folder name"
    description: Optional[str]  # Format:"" Descr:"The hierarchy's description"
    isAggregatable: Optional[bool]  # Format:"" Descr:"Is it possible to aggregate by this hierarchy"
    hasDefaultMember: Optional[bool]  # Format:"" Descr:"Does this hierarchy have a default member"
    hierarchyType: Optional[HierarchyType]  # Format:"" Descr:"The hierarchy's type"
    hierarchyCategory: Optional[HierarchyCategory]  # Format:"" Descr:"Predefined hierarchy category"
    parentKeySourceColumnUniqueName: Optional[str]  # Format:"" Descr:"Parent-Child hierarchy's parent column"
    keySourceColumnUniqueName: Optional[str]  # Format:"" Descr:"Parent-Child hierarchy's key column"
    orderSourceColumnUniqueName: Optional[str]  # Format:"" Descr:"Parent-Child hierarchy's order column"
    captionSourceColumnUniqueName: Optional[str]  # Format:"" Descr:"Parent-Child hierarchy's caption column"
    unaryOperatorSourceColumnUniqueName: Optional[str]  # Format:"" Descr:"Parent-Child hierarchy's unary-operator column"
    parentChildRollupType: Optional[ParentChildRollupType]  # Format:"" Descr:"Parent-Child hierarchy's rollup type"
    parentChildOrphanHandlingType: Optional[ParentChildOrphanHandlingType]  # Format:"" Descr:"Parent-Child hierarchy's handling for orphan nodes"
    startingLevel: Optional[int]  # Format:"int32" Descr:""
    orderColumnUniqueNameOrNullIfSelf: Optional[str]  # Format:"" Descr:""
    captionColumnUniqueNameOrNullIfSelf: Optional[str]  # Format:"" Descr:""
    

class ModelingMeasure(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelingMeasure.htm
    """
    measureId: Optional[str]  # Format:"uuid" Descr:"The measure's System ID"
    displayName: Optional[str]  # Format:"" Descr:"The measure's display name"
    uniqueName: Optional[str]  # Format:"" Descr:"The measure's Unique identifier"
    description: Optional[str]  # Format:"" Descr:"The measure's description"
    sourceColumnUniqueName: Optional[str]  # Format:"" Descr:"The Unique identifier of the column this measure is based on"
    expression: Optional[str]  # Format:"" Descr:"The expression inside the aggregation type"
    format: Optional[str]  # Format:"" Descr:"The measure's format string"
    aggregationType: Optional[AggregationType]  # Format:"" Descr:"The measure's aggregation type (sum,count,etc)"
    dataType: Optional[str]  # Format:"" Descr:"The measure's data type"
    displayFolder: Optional[str]  # Format:"" Descr:"The measure's display folder name"
    measureType: Optional[ModelAttributeType]  # Format:"" Descr:"The measure's Attribute Type"
    measureGroup: Optional[str]  # Format:"" Descr:"This measure's measure group name"
    scale: Optional[int]  # Format:"int32" Descr:"The measure's scale"
    suffixColumnUniqueName: Optional[str]  # Format:"" Descr:"The column to take the suffix from"
    prefixColumnUniqueName: Optional[str]  # Format:"" Descr:"The column to take the prefix from"
    

class ModelingRelationship(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelingRelationship.htm
    """
    relationshipId: Optional[str]  # Format:"uuid" Descr:"The relationship's system ID"
    columns: Optional[List[ModelingRelationshipColumnPair]]  # Format:"" Descr:"The model's system ID"
    primaryTableUniqueName: Optional[str]  # Format:"" Descr:"The primary table's unique name"
    foreignTableUniqueName: Optional[str]  # Format:"" Descr:"The foreign table's unique name"
    type: Optional[JoinType]  # Format:"" Descr:"The join type (inner, right, left, full outer, or cross join)"
    isBiDirectional: Optional[bool]  # Format:"" Descr:"Boolean indicating if the join is bi-directional"
    

class ModelingTable(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelingTable.htm
    """
    tableId: Optional[str]  # Format:"uuid" Descr:"The table's system ID"
    displayName: Optional[str]  # Format:"" Descr:"The table's display name"
    description: Optional[str]  # Format:"" Descr:"The tables's description"
    modelingColumns: Optional[List[ModelingColumn]]  # Format:"" Descr:"List of columns in this table"
    modelingMeasures: Optional[List[ModelingMeasure]]  # Format:"" Descr:"List of measures in this table"
    modelingHierarchies: Optional[List[ModelingHierarchy]]  # Format:"" Descr:"List of hierarchies in this table"
    uniqueName: Optional[str]  # Format:"" Descr:"Unique identifier of this table"
    schemaName: Optional[str]  # Format:"" Descr:"Schema name in the source database"
    sourceTableName: Optional[str]  # Format:"" Descr:"Tables name in the source database"
    isVisible: Optional[bool]  # Format:"" Descr:"Visible in the relationship diagram"
    primaryKeyColumnUniqueName: Optional[str]  # Format:"" Descr:"Unique identifier of the primary key column of this table"
    measureGroups: Optional[List[str]]  # Format:"" Descr:"List of measure group ids"
    customQuery: Optional[str]  # Format:"" Descr:"If this tables is based on a query, instead of schema and table name"
    modelingTableType: Optional[ModelingTableType]  # Format:"" Descr:"Table type"
    syncColumnsWithDb: Optional[bool]  # Format:"" Descr:"Defines whether to synchronize columns with DB columns."
    modelAttributeType: Optional[ModelAttributeType]  # Format:"" Descr:"-"
    

class ModelingModel(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelingModel.htm
    """
    modelId: Optional[str]  # Format:"uuid" Descr:"The model's system ID"
    displayName: Optional[str]  # Format:"" Descr:"The model's display name"
    description: Optional[str]  # Format:"" Descr:"A description of the model"
    tables: Optional[List[ModelingTable]]  # Format:"" Descr:"A list of tables/dimensions in the model"
    relationships: Optional[List[ModelingRelationship]]  # Format:"" Descr:"A list of the relationships between tables in the model"
    serverId: Optional[str]  # Format:"" Descr:"The host server's name"
    databaseName: Optional[str]  # Format:"" Descr:"The model's database name"
    modelType: Optional[DataFlowModelType]  # Format:"" Descr:"The type of model."
    modelDataFlowSourceInfo: Optional[ModelDataFlowSourceInfo]  # Format:"" Descr:"Info about the source Data Flow used to drive this model"
    isAutoIndexing: Optional[bool]  # Format:"" Descr:"Set to true for heuristic index creation"
    defaultMeasureUniqueName: Optional[str]  # Format:"" Descr:"Unique identifier of the default measure"
    measureGroups: Optional[List[MeasureGroup]]  # Format:"" Descr:"The model's measure groups."
    culture: Optional[str]  # Format:"" Descr:"The model's culture name"
    disableCacheMode: Optional[bool]  # Format:"" Descr:"Should disable cache"
    additionalLanguages: Optional[dict]  # Format:"" Descr:"Additional languages in the model"
    serverInfo: Optional[ModelingServerInfo]  # Format:"" Descr:"-"
    nullMemberCaption: Optional[str]  # Format:"" Descr:""
    calculatedMembersByAttribute: Optional[dict]  # Format:"" Descr:""
    syncColumnsSettings: Optional[List[ModelSyncColumnsSettings]]  # Format:"" Descr:"settings for sync columns by schedule. defines an aggregation and visibility for each new column data type."
    materializedItemType: Optional[MaterializedItemType]  # Format:"" Descr:"The type of materialized model or data item."
    

class ModifiedItemsResult(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModifiedItemsResult.htm
    """
    success: Optional[bool]  # Format:"" Descr:"Boolean showing success or failure result."
    errorMessage: Optional[str]  # Format:"" Descr:"Error message in case of failure"
    modifiedList: Optional[List[ItemId]]  # Format:"" Descr:"List of item ID's that have been affected by the function call. The type of ID depends on the function."
    

class MoveItemsObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MoveItemsObject.htm
    """
    itemsForMove: List[str]  # Format:"" Descr:"List of content item ID's"
    destinationFolder: str  # Format:"" Descr:"The system folder ID"
    

class NewFolderApiData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/NewFolderApiData.htm
    """
    folderId: Optional[str]  # Format:"" Descr:"The system ID of the new folder. If provided, the GUID will be used. Otherwise, the function will auto-create it."
    parentFolderId: str  # Format:"" Descr:"The system ID of the parent folder for the new folder."
    folderName: str  # Format:"" Descr:"The new folder's name"
    

class NewTenantObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/NewTenantObject.htm
    """
    id: Optional[str]  # Format:"" Descr:"The tenant ID. If provided, the GUID will be used. Otherwise, the function will auto-create it."
    name: str  # Format:"" Descr:"The tenant's name"
    viewerSeats: int  # Format:"int32" Descr:"Number of Viewer seat licenses to allocate to the tenant"
    proSeats: int  # Format:"int32" Descr:"Number of Professional seat licenses to allocate to the tenant"
    showGroupFolder: Optional[bool]  # Format:"" Descr:"Boolean flag to show a tenant's group folders"
    

class NotificationIndicatorsResult(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/NotificationIndicatorsResult.htm
    """
    models: Optional[int]  # Format:"int32" Descr:"model notification count."
    subscriptions: Optional[int]  # Format:"int32" Descr:"subscription notification count."
    alerts: Optional[int]  # Format:"int32" Descr:"alert notification count."
    publications: Optional[int]  # Format:"int32" Descr:"publication notification count."
    conversations: Optional[int]  # Format:"int32" Descr:"conversation notification count."
    

class ProfilePermissionHolder(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ProfilePermissionHolder.htm
    """
    permissionBitIndexList: Optional[List[PermissionBitIndex]]  # Format:"" Descr:"A list of permission bit index switches [x,y,...]"
    numeric: Optional[int]  # Format:"int64" Descr:"The summation of all permission bit indexes result=(2^x)+(2^y)+..."
    

class PieApiObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PieApiObject.htm
    """
    rootFolderId: str  # Format:"" Descr:"The system ID of the root folder that will house the imported content"
    fileZippedData: str  # Format:"" Descr:"The PIE file contents (base64 data payload)"
    clashDefaultOption: Optional[ClashDefaultOption]  # Format:"" Descr:"The settings for how to handle content clashes on import. Default:REPLACE_FILE"
    rolesAssignmentType: Optional[RoleAssignmentType]  # Format:"" Descr:"The settings for how to set roles on imported content. Default:UseDefaultBehavior"
    roleIds: Optional[List[str]]  # Format:"" Descr:"The roles ID's to be applied to the imported content. Relevant only for 'RoleAssignmentType.ForceExternalRoles'"
    

class ProfileApiData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ProfileApiData.htm
    """
    profileId: Optional[str]  # Format:"" Descr:"The system ID of the profile. When adding a profile, the provided GUID will be used if supplied. Otherwise, the function will auto-create it."
    name: str  # Format:"" Descr:"Profile's name or caption"
    description: str  # Format:"" Descr:"Profile's description"
    permissions: ProfilePermissionHolder  # Format:"" Descr:"Profile's permissions (using either numeric switches or an array of switches)."
    tenantId: str  # Format:"" Descr:"The profile's tenant (ID)"
    

class ProfileRolesData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ProfileRolesData.htm
    """
    profileId: str  # Format:"" Descr:"The system ID of the profile"
    rolesToAdd: List[str]  # Format:"" Descr:"The a list of role ID's that the profile will be ADDEd to."
    rolesToRemove: List[str]  # Format:"" Descr:"The a list of role ID's that the profile will be REMOVED from."
    

class PyramidContentItem(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PyramidContentItem.htm
    """
    id: Optional[str]  # Format:"" Descr:"The content item's ID"
    parentId: Optional[str]  # Format:"" Descr:"The content item's parent ID"
    caption: Optional[str]  # Format:"" Descr:"The content item's caption"
    itemType: Optional[ItemType]  # Format:"" Descr:"The content item's type enumeration"
    createdBy: Optional[str]  # Format:"" Descr:"The creator's user ID"
    createdDate: Optional[str]  # Format:"date-time" Descr:"The create date of the item"
    version: Optional[str]  # Format:"" Descr:"The version of the item"
    modifiedDate: Optional[str]  # Format:"date-time" Descr:"The modified date if the item"
    description: Optional[str]  # Format:"" Descr:"The description of the item"
    tenantId: Optional[str]  # Format:"" Descr:"The content item's related tenant ID"
    contentType: Optional[ContentType]  # Format:"" Descr:"The content type enumeration"
    isDeleted: Optional[bool]  # Format:"" Descr:"is the item deleted"
    

class PyramidItemIdentifier(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PyramidItemIdentifier.htm
    """
    itemId: str  # Format:"" Descr:"The item's ID"
    itemTypeObject: ContentItemObject  # Format:"" Descr:"The item type"
    

class PyramidViewUserObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PyramidViewUserObject.htm
    """
    id: str  # Format:"uuid" Descr:"The user's system ID."
    userName: Optional[str]  # Format:"" Descr:"The login username for the user"
    firstName: Optional[str]  # Format:"" Descr:"The user's first name"
    lastName: Optional[str]  # Format:"" Descr:"The user's last name"
    email: Optional[str]  # Format:"" Descr:"The user's email"
    phone: Optional[str]  # Format:"" Descr:"The user's phone"
    proxyAccount: Optional[str]  # Format:"" Descr:"The user's proxy account needed for connecting to different data sources"
    adminType: Optional[AdminType]  # Format:"" Descr:"The user's administration level using the admin type enumeration"
    roleIds: Optional[List[str]]  # Format:"" Descr:"The user's list of roles"
    clientLicenseType: Optional[ClientLicenseType]  # Format:"" Descr:"The user's license type using the type enumeration"
    statusID: Optional[UserStatusID]  # Format:"" Descr:"The user's status using the status type enumeration"
    tenantId: Optional[str]  # Format:"" Descr:"The user's tenant ID"
    createdDate: Optional[int]  # Format:"int64" Descr:""
    lastLoginDate: Optional[int]  # Format:"int64" Descr:""
    adDomainName: Optional[str]  # Format:"" Descr:"The AD/LDAP domain name (relevant in case the user is authenticated using AD)"
    principalName: Optional[str]  # Format:"" Descr:"The user's SAML identifier (relevant in case the user is authenticated using SAML)"
    secondaryMobilePhone: Optional[str]  # Format:"" Descr:"The user's secondary mobile phone."
    

class QueryExportData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/QueryExportData.htm
    """
    itemId: str  # Format:"uuid" Descr:"Content item's ID that houses the query to execute"
    exportType: ApiResponseFormat  # Format:"" Descr:"Result format type using enumeration of export format types"
    exportOptions: ExportOptions  # Format:"" Descr:"Export Options and switches"
    externalParameters: ExternalParameters  # Format:"" Descr:"Export Parameters and switches"
    

class RenameItemApiData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RenameItemApiData.htm
    """
    itemId: str  # Format:"" Descr:"The system ID of the item to rename"
    newName: str  # Format:"" Descr:"The new name for the item"
    

class ResultsObjectData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ResultsObjectData.htm
    """
    result: Optional[dict]  # Format:"" Descr:"The resulting object"
    message: Optional[str]  # Format:"" Descr:"Result based messages"
    

class RoleAdGroupsModifyObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RoleAdGroupsModifyObject.htm
    """
    roleId: str  # Format:"" Descr:"The role's ID"
    groupsToAdd: Optional[List[LdapGroupIdentifier]]  # Format:"" Descr:"List of groups to add to the role"
    groupsToRemove: Optional[List[LdapGroupIdentifier]]  # Format:"" Descr:"List of groups to remove from the role"
    

class RoleData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RoleData.htm
    """
    roleId: Optional[str]  # Format:"uuid" Descr:"The role's system ID"
    roleName: str  # Format:"" Descr:"The role's name"
    roleSettings: Optional[str]  # Format:"" Descr:"The role's settings"
    isHidden: Optional[bool]  # Format:"" Descr:"Flag to indicate if the role is hidden"
    tenantId: str  # Format:"uuid" Descr:"The roles's tenant (ID)"
    

class RoleMinimalData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RoleMinimalData.htm
    """
    roleId: Optional[str]  # Format:"" Descr:"The role's system ID"
    roleName: str  # Format:"" Descr:"The role's name"
    tenantId: str  # Format:"" Descr:"The roles's tenant (ID)"
    

class RoleToItemApiData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RoleToItemApiData.htm
    """
    itemId: str  # Format:"" Descr:"The system ID of the content item"
    roleId: str  # Format:"" Descr:"The system ID of the role"
    accessType: Optional[AccessType]  # Format:"" Descr:"The access settings for the role on this item. Default:Read"
    propagateRoles: Optional[bool] = False # Format:"" Descr:"Boolean to determine whether the role settings to propagate to subordinate items. Default:false"
    

class RolesInItemRemovalObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RolesInItemRemovalObject.htm
    """
    itemId: str  # Format:"" Descr:"The system ID of the content item"
    roleIds: List[str]  # Format:"" Descr:"The system ID of the role"
    

class ScheduleSearchCriteria(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ScheduleSearchCriteria.htm
    """
    searchCriteria: Optional[SearchCriteria]  # Format:"" Descr:"Search criteria object for specifying schedule search conditions and strings"
    scheduleType: Optional[ScheduleType]  # Format:"" Descr:"Schedule type enumeration for narrowing the search"
    

class ScheduleViewObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ScheduleViewObject.htm
    """
    scheduleId: Optional[str]  # Format:"" Descr:"Schedule's system ID"
    name: Optional[str]  # Format:"" Descr:"Schedule's name or caption"
    description: Optional[str]  # Format:"" Descr:"Schedule's description"
    type: Optional[ScheduleType]  # Format:"" Descr:"Schedule's type"
    createdDate: Optional[str]  # Format:"date-time" Descr:"Schedule's create date"
    createdBy: Optional[str]  # Format:"" Descr:"Schedule's creator"
    startDate: Optional[str]  # Format:"date-time" Descr:"Schedule's start date"
    endDate: Optional[str]  # Format:"date-time" Descr:"Schedule's end date"
    scheduleDataType: Optional[ScheduleDataType]  # Format:"" Descr:"Schedule repetition type enumeration"
    status: Optional[ScheduleStatus]  # Format:"" Descr:"Schedule status enumeration"
    scheduleItemId: Optional[str]  # Format:"" Descr:"The content item (ID) that the schedule is attached to"
    scheduleItemName: Optional[str]  # Format:"" Descr:"The content item (Name) that the schedule is attached to"
    tenantId: Optional[str]  # Format:"" Descr:"The tenant id of the Schedule's creator"
    

class SearchAdGroupUsersData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SearchAdGroupUsersData.htm
    """
    domainNetBios: str  # Format:"" Descr:"The AD domain"
    groupNames: List[str]  # Format:"" Descr:"An array of AD group names to be used for searching"
    

class SearchAdUserGroupsData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SearchAdUserGroupsData.htm
    """
    domainNetBios: str  # Format:"" Descr:"The AD domain"
    userName: str  # Format:"" Descr:"The AD username to be used for searching"
    

class SearchCriteria(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SearchCriteria.htm
    """
    searchValue: str  # Format:"" Descr:"Search string"
    searchMatchType: Optional[SearchMatchType]  # Format:"" Descr:"Search match enumeration type. Default:Equals."
    

class ServerData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ServerData.htm
    """
    id: Optional[str]  # Format:"" Descr:"The data source's system ID"
    serverName: str  # Format:"" Descr:"The data source server's caption or name"
    serverType: ConnectionStringType  # Format:"" Descr:"The data source server's type enumeration"
    serverIp: str  # Format:"" Descr:"The data source server's IP address or FQDN"
    instanceName: Optional[str]  # Format:"" Descr:"The instance name of the data source (if relevant)"
    port: Optional[int]  # Format:"int32" Descr:"The data source server's port number"
    writeCapable: Optional[int]  # Format:"int32" Descr:"Read=0, Write=1, Default:Read"
    optionalParameters: Optional[str]  # Format:"" Descr:"Optional parameters for data source connection"
    securedByUser: Optional[bool]  # Format:"" Descr:"Boolean flag if the data source will be secured by each end-user"
    serverAuthenticationMethod: Optional[ServerAuthenticationMethod]  # Format:"" Descr:"Authentication method details when securing the connection."
    userName: Optional[str]  # Format:"" Descr:"User Id needed for connection"
    password: Optional[str]  # Format:"" Descr:"User password need for connection"
    tenantId: Optional[str]  # Format:"" Descr:"The tenant ID that the data source will be attached to"
    additionalServerProperties: Optional[AdditionalServerProperties]  # Format:"" Descr:"Additional connection properties and settings for the data source"
    useGlobalAccount: Optional[bool] = False # Format:"" Descr:"Boolean to flag if the global account should be sued for connecting. Default:false"
    pulseClient: Optional[str]  # Format:"" Descr:"The Pulse client ID if used with the data source"
    defaultDatabaseName: Optional[str]  # Format:"" Descr:"The default database to be used with the data source"
    overlayPyramidSecurity: Optional[bool]  # Format:"" Descr:"Boolean flag if the data source will use Pyramid's security and metadata overlays"
    modifiedDate: Optional[str]  # Format:"date-time" Descr:""
    serverIpAndInstanceName: Optional[str]  # Format:"" Descr:""
    

class TagData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TagData.htm
    """
    tagId: Optional[str]  # Format:"" Descr:"The tag ID. If provided, the GUID will be used. Otherwise, the function will auto-create it."
    tagDescription: Optional[str]  # Format:"" Descr:"The tag's description."
    tagType: TagType  # Format:"" Descr:"The tag's type based on the enumeration of types."
    

class TagUsageApiData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TagUsageApiData.htm
    """
    itemId: str  # Format:"" Descr:"The content item's system ID"
    tagId: str  # Format:"" Descr:"The tag's system ID"
    

class TaskUserApiData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TaskUserApiData.htm
    """
    taskId: str  # Format:"" Descr:"The task's ID"
    userId: Optional[str]  # Format:"" Descr:"The user's ID"
    

class TenantLicenseTypeData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TenantLicenseTypeData.htm
    """
    tenantId: str  # Format:"" Descr:"The tenant's system ID"
    licenseType: ClientLicenseType  # Format:"" Descr:"The licence type"
    

class TenantSettings(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TenantSettings.htm
    """
    showGroupFolder: Optional[bool]  # Format:"" Descr:"Boolean to show or hide the tenant's group folders"
    allowWebhookChannels: Optional[bool]  # Format:"" Descr:""
    firstWorkday: Optional[FirstWorkday]  # Format:"" Descr:"-"
    

class TenantUsersGetObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TenantUsersGetObject.htm
    """
    tenantId: str  # Format:"" Descr:"The user's tenant ID"
    clientLicenseType: ClientLicenseType  # Format:"" Descr:"The user's license type using the type enumeration"
    

class ThemeApiData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ThemeApiData.htm
    """
    themeData: str  # Format:"" Descr:"The encrypted data"
    isDefault: Optional[bool]  # Format:"" Descr:"Boolean of whether theme is default or not"
    

class ThemeApiObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ThemeApiObject.htm
    """
    themeId: Optional[str]  # Format:"" Descr:"The theme ID. If provided, the GUID will be used. Otherwise, the function will auto-create it."
    themeName: Optional[str]  # Format:"" Descr:"The theme name. If provided, the name will be used. Otherwise, the function will use the original theme name."
    themeData: str  # Format:"" Descr:"The encrypted theme data"
    isDefault: Optional[bool]  # Format:"" Descr:"Boolean of whether theme is default or not"
    

class ThemeListObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ThemeListObject.htm
    """
    themeId: Optional[str]  # Format:"" Descr:"The theme's system ID"
    themeName: Optional[str]  # Format:"" Descr:"The theme's name or caption"
    

class ToggleUserApiData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ToggleUserApiData.htm
    """
    userId: str  # Format:"" Descr:"A user's system ID"
    isEnable: bool  # Format:"" Descr:"Boolean flag for enabled or disabled"
    

class UpdateTenantSeatsObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UpdateTenantSeatsObject.htm
    """
    id: str  # Format:"" Descr:"The tenant ID."
    viewerSeats: Optional[int]  # Format:"int32" Descr:"Number of Viewer seat licenses to allocate to the tenant"
    proSeats: Optional[int]  # Format:"int32" Descr:"Number of Professional seat licenses to allocate to the tenant"
    

class UpdateUserAdObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UpdateUserAdObject.htm
    """
    id: str  # Format:"uuid" Descr:"The user's system ID."
    secondaryPhone: Optional[str]  # Format:"" Descr:"User's secondary phone - needed for automation and messaging"
    adminType: Optional[AdminType]  # Format:"" Descr:"The user's administration level using the admin type enumeration"
    roleIds: Optional[List[str]]  # Format:"" Descr:"The user's list of roles"
    clientLicenseType: Optional[ClientLicenseType]  # Format:"" Descr:"The user's license type using the type enumeration"
    statusID: Optional[UserStatusID]  # Format:"" Descr:"The user's status using the status type enumeration"
    tenantId: Optional[str]  # Format:"" Descr:"The user's tenant ID"
    profileId: Optional[str]  # Format:"" Descr:"The profile ID to be applied for this user"
    

class UpdateUserDbObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UpdateUserDbObject.htm
    """
    id: str  # Format:"uuid" Descr:"The user's system ID."
    userName: Optional[str]  # Format:"" Descr:"The login username for the user"
    firstName: Optional[str]  # Format:"" Descr:"The user's first name"
    lastName: Optional[str]  # Format:"" Descr:"The user's last name"
    email: Optional[str]  # Format:"" Descr:"The user's email"
    phone: Optional[str]  # Format:"" Descr:"The user's phone"
    proxyAccount: Optional[str]  # Format:"" Descr:"The user's proxy account needed for connecting to different data sources"
    adminType: Optional[AdminType]  # Format:"" Descr:"The user's administration level using the admin type enumeration"
    roleIds: Optional[List[str]]  # Format:"" Descr:"The user's list of roles"
    clientLicenseType: Optional[ClientLicenseType]  # Format:"" Descr:"The user's license type using the type enumeration"
    statusID: Optional[UserStatusID]  # Format:"" Descr:"The user's status using the status type enumeration"
    tenantId: Optional[str]  # Format:"" Descr:"The user's tenant ID"
    profileId: Optional[str]  # Format:"" Descr:"The profile ID to be applied for this user"
    password: Optional[str]  # Format:"" Descr:"The User's password"
    

class UpdateUserOpenIdObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UpdateUserOpenIdObject.htm
    """
    id: str  # Format:"uuid" Descr:"The user's system ID."
    userName: Optional[str]  # Format:"" Descr:"The login username for the user"
    firstName: Optional[str]  # Format:"" Descr:"The user's first name"
    lastName: Optional[str]  # Format:"" Descr:"The user's last name"
    email: Optional[str]  # Format:"" Descr:"The user's email"
    phone: Optional[str]  # Format:"" Descr:"The user's phone"
    proxyAccount: Optional[str]  # Format:"" Descr:"The user's proxy account needed for connecting to different data sources"
    adminType: Optional[AdminType]  # Format:"" Descr:"The user's administration level using the admin type enumeration"
    roleIds: Optional[List[str]]  # Format:"" Descr:"The user's list of roles"
    clientLicenseType: Optional[ClientLicenseType]  # Format:"" Descr:"The user's license type using the type enumeration"
    statusID: Optional[UserStatusID]  # Format:"" Descr:"The user's status using the status type enumeration"
    tenantId: Optional[str]  # Format:"" Descr:"The user's tenant ID"
    profileId: Optional[str]  # Format:"" Descr:"The profile ID to be applied for this user"
    principalName: Optional[str]  # Format:"" Descr:"The user's OpenID principal name identifier"
    password: Optional[str]  # Format:"" Descr:"User's password. relevant only for enterprise admin users"
    

class UpdateUserSamlObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UpdateUserSamlObject.htm
    """
    id: str  # Format:"uuid" Descr:"The user's system ID."
    userName: Optional[str]  # Format:"" Descr:"The login username for the user"
    firstName: Optional[str]  # Format:"" Descr:"The user's first name"
    lastName: Optional[str]  # Format:"" Descr:"The user's last name"
    email: Optional[str]  # Format:"" Descr:"The user's email"
    phone: Optional[str]  # Format:"" Descr:"The user's phone"
    proxyAccount: Optional[str]  # Format:"" Descr:"The user's proxy account needed for connecting to different data sources"
    adminType: Optional[AdminType]  # Format:"" Descr:"The user's administration level using the admin type enumeration"
    roleIds: Optional[List[str]]  # Format:"" Descr:"The user's list of roles"
    clientLicenseType: Optional[ClientLicenseType]  # Format:"" Descr:"The user's license type using the type enumeration"
    statusID: Optional[UserStatusID]  # Format:"" Descr:"The user's status using the status type enumeration"
    tenantId: Optional[str]  # Format:"" Descr:"The user's tenant ID"
    profileId: Optional[str]  # Format:"" Descr:"The profile ID to be applied for this user"
    principalName: Optional[str]  # Format:"" Descr:"The user's SAML identifier"
    password: Optional[str]  # Format:"" Descr:"User's password. relevant only for enterprise admin users"
    

class UserCredentials(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UserCredentials.htm
    """
    username: str  # Format:"" Descr:"The user's login identity The format depends on the authentication provider: Its 'username' for internal database authentication. For AD, its either UPN or 'domain\username'."
    password: str  # Format:"" Descr:"The user's password."
    domain: Optional[str]  # Format:"" Descr:"The URL web domain - needed only for embedded authentication."
    customData: Optional[str]  # Format:"" Descr:"Custom data input for usage within the product."
    

class UserData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UserData.htm
    """
    id: Optional[str]  # Format:"uuid" Descr:"The user's system ID"
    userName: Optional[str]  # Format:"" Descr:"The user's login name."
    password: Optional[str]  # Format:"" Descr:""
    firstName: Optional[str]  # Format:"" Descr:"The user's first name."
    lastName: Optional[str]  # Format:"" Descr:"The user's last name."
    email: Optional[str]  # Format:"" Descr:"The user's email."
    mobilePhone: Optional[str]  # Format:"" Descr:"The user's mobile phone."
    secondaryMobilePhone: Optional[str]  # Format:"" Descr:"The user's secondary mobile phone."
    adminType: Optional[AdminType]  # Format:"" Descr:"The user's administration type flag."
    roles: Optional[List[RoleData]]  # Format:"" Descr:"The role object contains meta-data for the role."
    userSettings: Optional[UserSettingsData]  # Format:"" Descr:"-"
    clientLicenseType: Optional[ClientLicenseType]  # Format:"" Descr:"The user's client license type."
    statusID: Optional[int]  # Format:"int32" Descr:"The user's system status."
    adDomain: Optional[str]  # Format:"" Descr:"The user's AD domain (if relevant)."
    adAccount: Optional[str]  # Format:"" Descr:"The user's AD username (if relevant)."
    adSid: Optional[str]  # Format:"" Descr:"The user's AD SID (if relevant)."
    proxyAccount: Optional[str]  # Format:"" Descr:""
    upgradeVersion: Optional[str]  # Format:"" Descr:""
    adGuid: Optional[str]  # Format:"" Descr:"The user's AD GUID (if relevant)."
    createdDate: Optional[int]  # Format:"int64" Descr:""
    modifiedDate: Optional[int]  # Format:"int64" Descr:""
    lastLoginDate: Optional[int]  # Format:"int64" Descr:""
    version: Optional[str]  # Format:"" Descr:""
    tenantId: Optional[str]  # Format:"" Descr:"The user's tenant (ID)."
    principalName: Optional[str]  # Format:"" Descr:"The user's principal name (UPN)."
    privateProfileId: Optional[str]  # Format:"" Descr:""
    tenantsInfo: Optional[List[TenantInfo]]  # Format:"" Descr:"-"
    newUserId: Optional[str]  # Format:"uuid" Descr:""
    migratedUser: Optional[bool]  # Format:"" Descr:""
    tenantName: Optional[str]  # Format:"" Descr:""
    userWorkspace: Optional[UserWorkspaceSettings]  # Format:"" Descr:"-"
    profilePicture: Optional[str]  # Format:"" Descr:""
    certification: Optional[str]  # Format:"" Descr:""
    

class UserOpenIdCredentials(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UserOpenIdCredentials.htm
    """
    parameterMap: str  # Format:"" Descr:"The OpenID auth parameter map serialized to String."
    domain: Optional[str]  # Format:"" Descr:"The URL web domain - needed only for embedded authentication."
    customData: Optional[str]  # Format:"" Descr:"Custom data input for usage within the product."
    

class UserRolesData(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UserRolesData.htm
    """
    userId: str  # Format:"" Descr:"The system ID of the user"
    rolesToAdd: Optional[List[str]]  # Format:"" Descr:"The a list of role ID's to ADD to the user"
    rolesToRemove: Optional[List[str]]  # Format:"" Descr:"The a list of role ID's to REMOVE from the user"
    

class UserSamlCredentials(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UserSamlCredentials.htm
    """
    token: str  # Format:"" Descr:"The SAML auth token."
    domain: Optional[str]  # Format:"" Descr:"The URL web domain - needed only for embedded authentication."
    customData: Optional[str]  # Format:"" Descr:"Custom data input for usage within the product."
    

class UserTokenCredentials(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UserTokenCredentials.htm
    """
    token: str  # Format:"" Descr:"The administrative authority token - generated by by an administrator using normal authentication methods first."
    userIdentity: str  # Format:"" Descr:"The user's login identity.  The format depends on the authentication provider: Its 'username' for internal database authentication. For AD, its either UPN or 'domain\\username'. For SAML its UPN."
    customData: Optional[str]  # Format:"" Descr:"Custom data input for usage within the product."
    

class MasterFlowValidationResult(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowValidationResult.htm
    """
    sources: Optional[List[MasterFlowSourceObject]]  # Format:"" Descr:"Validation results for sources objects"
    targets: Optional[List[MasterFlowTargetObject]]  # Format:"" Descr:"Validation results for targets objects"
    others: Optional[List[MasterFlowOtherObject]]  # Format:"" Descr:"Validation results for other objects"
    variables: Optional[List[MasterFlowVariableObject]]  # Format:"" Descr:"Validation results for variables objects"
    

class MasterFlowSourceObject(BaseModel):
    """
    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterFlowSourceObject.htm
    """
    masterFlowNodeId: Optional[str]  # Format:"" Descr:"Master Flow node id"
    masterFlowNodeName: Optional[str]  # Format:"" Descr:"Master Flow node name"
    dataFlowNodeId: Optional[str]  # Format:"" Descr:"Data Flow node id"
    description: Optional[str]  # Format:"" Descr:"Description of the data flow node"
    serverId: Optional[str]  # Format:"" Descr:"Server id"
    serverName: Optional[str]  # Format:"" Descr:"Server name"
    serverType: Optional[ConnectionStringType]  # Format:"" Descr:"Server Type - one of the ConnectionStringType enumeration"
    databaseName: Optional[str]  # Format:"" Descr:"Database name"
    validationMessage: Optional[str]  # Format:"" Descr:"Validation message"
    
