from __future__ import annotations

import copy
from enum import IntEnum
from operator import truediv

from dataclasses_json import DataClassJsonMixin


from dataclasses import (
    dataclass,
    field
)
from typing import (
    Any,
    Dict,
    List,
    Optional
)


def default_field(obj):
    return field(default_factory=lambda: copy.copy(obj))


class ClientLicenseType(IntEnum):
    none = 0
    viewer = 100
    professional = 200    


class AdminType(IntEnum):
    none = 0
    domainadmin = 1
    enterpriseadmin = 2


class UserStatusID(IntEnum):
    disabled = 0
    enabled = 1


class ServerType(IntEnum):
    none = 0
    ms_olap = 1
    ms_olap_tabular = 2
    powerpivot = 3
    in_memory = 4
    sqlserver = 5
    mysql = 6
    monetdb = 7
    postgresql = 8
    oracle = 9
    db2 = 10
    teradata = 11
    drill = 12
    pa_imdb = 13
    redshift = 14
    presto = 15
    athena = 16
    bigquery = 17
    hive = 18
    salesforce = 19
    sap_hana = 20
    googleanalytics = 21
    mongodbbicx = 22
    sqlserverazure = 23
    snowflake = 24
    sybase = 25
    firebird = 26
    facebook = 27
    vertica = 28
    twitter = 29
    odbcserver = 30
    sharepoint = 31
    sap_bw = 32
    azureblobstorage = 33
    amazons3storage = 34
    greenplum = 35
    exasol = 36
    memsql = 37
    mariadb = 38
    netezza = 39
    glue = 40
    impala = 41
    azuresynapse = 42
    odbcdirectquery = 43
    as400 = 44


class ServerAuthenticationMethod(IntEnum):
    userpassword = 0
    globalactivedirectory = 1
    specificactivedirectory = 2
    serviceaccount = 3
    enduser = 4
    defaultawscredentialsproviderchain = 5
    keytab = 6
    snc = 7
    sap_logon_ticket = 8
    saml = 9


class AccessType(IntEnum):
    none = 0
    read = 1
    write = 2
    view = 3
    admin = 4


class SearchRootFolderType(IntEnum):
    private = 0
    public = 1
    group = 2
    oneoff = 3
    deletedcontent = 4
    crosstenant = 5
    recent = 6
    favorite = 7


class SearchMatchType(IntEnum):
    contains = 0
    notcontains = 1
    equals = 2
    startswith = 3
    endswith = 4


class ContentType(IntEnum):
    none = 0
    asset = 1
    calculation = 2
    datadiscovery = 3
    etlflow = 4
    folder = 5
    publisher = 6
    server = 7
    storyboard = 8
    document = 9
    component = 10
    theme = 11
    prom = 12
    contentview = 13
    # there is no 14!
    kpibandscontainer = 15
    datasource = 16

class ContentItemType(IntEnum):
    none = 0
    asset =1
    server = 2
    document = 3
    container = 4
    folder = 5
    calculation = 6
    prom = 7
    etlflow = 8
    customvisual = 9

# NOT THE SAME AS ABOVE!?!?!?!?
class ContentItemObjectType(IntEnum):
    asset = 0
    publisher = 1
    storyboard = 2
    calculation = 3
    datadiscovery = 4

class MaterializedItemType(IntEnum):
    none = 0
    database = 1
    modelingmodel = 2
    server = 3
    machinelearningmodel = 4
    schedule = 5
    model = 6
    output = 7


class RoleAssignmentType(IntEnum):
    usedefaultbehavior = 0
    forcepackageroles = 1
    forceexternalroles = 2
    forceparentroles = 3


# subclassing enums only works in 3.8+ so we'll be redundant
class MaterializedRoleAssignmentType(IntEnum):
    usedefaultbehavior = 0
    forcepackageroles = 1
    forceexternalroles = 2
    forceparentroles = 3


class ValidRootFolderType(IntEnum):
    private = 0
    public = 1
    group = 2


class ApiResponseFormat(IntEnum):
    json = 0
    xml = 1
    csv = 2
    odata = 3
    odata_metadata = 4
    odata_db_level = 5

class SyntaxType(IntEnum):
    pql = 0
    ms = 1
    bw = 2

class WriteCapability(IntEnum):
    Read = 0
    Write = 1

class ClashDefaultOption(IntEnum):
    REPLACE_FILE = 1
    # Need:
    # NEW
    # SKIP

class RootFolderType(IntEnum):
    private = 0
    public = 1
    group = 2
    oneoff = 3
    privatedummy = 4
    tenantsrootfolderdummy = 5
    tenantdummy = 6
    deletedcontent = 7
    crosstenant = 8
    recent = 9
    favorites = 10

@dataclass
class ItemId(DataClassJsonMixin):
    id: str
    name: str = None


@dataclass
class Role(DataClassJsonMixin):
    tenantId: str
    roleName: str
    roleId: str = None
    roleSettings: str = None
    isHidden: bool = False
    isPrivate: bool = False
    isGroupRole: bool = False
    createdBy: str = None
    
@dataclass
class ItemRolePair(DataClassJsonMixin):
    roleId: str
    accessType: AccessType = AccessType.none

@dataclass
class User(DataClassJsonMixin):
    tenantId: str
    userName: str
    roleIds: List[str] = default_field([])
    clientLicenseType: ClientLicenseType = ClientLicenseType.none
    id: str = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    proxyAccount: Optional[str] = None
    adminType: AdminType = 0
    statusID: int = 1
    createdDate: Optional[int] = 0
    lastLoginDate: Optional[int] = 0
    # optional
    adDomainName: Optional[str] = None
    principalName: Optional[str] = None
    # missing from official spec
    inheritanceType: Optional[str] = None
    secondaryMobilePhone: Optional[str] = None

@dataclass
class Server(DataClassJsonMixin):
    port: int
    serverName: str
    id: Optional[str] = None
    serverType: ServerType = ServerType.none
    serverIp: Optional[str] = None
    instanceName: Optional[str] = None
    writeCapable: Optional[WriteCapability] = WriteCapability.Read
    optionalParameters: Optional[str] = None
    securedByUser: bool = False
    serverAuthenticationMethod: Optional[ServerAuthenticationMethod] = ServerAuthenticationMethod.userpassword
    userName: Optional[str] = None
    password: Optional[str] = None
    tenantId: Optional[str] = None
    additionalServerProperties: Dict = default_field({})
    useGlobalAccount: bool = False
    pulseClient: Optional[str] = None
    defaultDatabaseName: Optional[str] = None
    overlayPyramidSecurity: Optional[bool] = False
    serverIpAndInstanceName: Optional[str] = None


@dataclass
class ServerDetails(Server):
    inheritanceType: Optional[str] = 'ServerData'


@dataclass
class TenantSettings(DataClassJsonMixin):
    showGroupFolder: Optional[bool] = None
    allowWebhookChannels: Optional[bool] = None


@dataclass
class TenantData(DataClassJsonMixin):
    id: Optional[str]
    name: Optional[str]
    viewerSeats: Optional[int] = 0
    usedViewerSeats: Optional[int] = 0
    proSeats: Optional[int] = 0
    usedProSeats: Optional[int] = 0
    tenantSettings: Optional[TenantSettings] = None
    pulseKey: Optional[str] = None
    selectedUserDefaultsId: Optional[str] = None
    selectedUserDefaultsName: Optional[str] = None
    defaultThemeId: Optional[str] = None
    defaultAiServer: Optional[str] = None
    userDefaultsOverridable: Optional[bool] = None


@dataclass
class NewTenant(DataClassJsonMixin):
    id: str
    name: str
    viewerSeats: int = 0
    proSeats: int = 0
    showGroupFolder: bool = False


@dataclass
class NotificationIndicatorsResult(DataClassJsonMixin):
    models: Optional[int]
    subscriptions: Optional[int]
    alerts: Optional[int]
    publications: Optional[int]
    conversations: Optional[int]


@dataclass
class NewFolder(DataClassJsonMixin):
    parentFolderId: str
    folderName: str
    folderId: Optional[str] = None


@dataclass
class SearchParams(DataClassJsonMixin):
    searchString: str
    filterTypes: List[ContentType]
    searchMatchType: SearchMatchType = SearchMatchType.contains
    searchRootFolderType: SearchRootFolderType = SearchRootFolderType.public
    startCreatedDate: Optional[str] = None
    endCreatedDate: Optional[str] = None
    startModifiedDate: Optional[str] = None
    endModifiedDate: Optional[str] = None
    server: Optional[str] = None
    model: Optional[str] = None
    dataBase: Optional[str] = None
    isAdvancedSearch: bool = False
    folderPathToSearch: Optional[str] = None


@dataclass
class ConnectionStringProperties(DataClassJsonMixin):
    id: Optional[str] = None
    modelId: Optional[str] = None
    modelName: Optional[str] = None
    serverId: Optional[str] = None
    serverName: Optional[str] = None
    dataBaseId: Optional[str] = None
    dataBaseName: Optional[str] = None
    connectionStringType: Optional[ServerType] = ServerType.none
    isDynamicModel: Optional[bool] = False
    modelParamsStatus: Optional[str] = None
    securityHash: Optional[str] = None


@dataclass
class ContentItem(DataClassJsonMixin):
    id: Optional[str]
    parentId: Optional[str]
    caption: Optional[str]
    itemType: Optional[ContentItemType]
    createdBy: Optional[str] = None
    createdDate: Optional[int] = None
    version: Optional[str] = None
    modifiedDate: Optional[str] = None
    description: Optional[str] = None
    tenantId: Optional[str] = None
    contentType: Optional[ContentType] = None
    isDeleted: bool = False

@dataclass
class ModifiedItemsResult(DataClassJsonMixin):
    success: bool
    modifiedList: List[ItemId] = default_field([])
    errorMessage: str = None


@dataclass
class MaterializedItemObject(DataClassJsonMixin):
    itemId: str
    itemCaption: str = None
    itemType: MaterializedItemType = MaterializedItemType.none


@dataclass
class PieApiObject(DataClassJsonMixin):
    rootFolderId: str
    fileZippedData: str # base64 encoded string of the file
    clashDefaultOption: int = ClashDefaultOption.REPLACE_FILE
    rolesAssignmentType: RoleAssignmentType = RoleAssignmentType.forceparentroles
    roleIds: List[str] = None  # only relevent to RoleAssignmentType.ForceExternalRoles

    @staticmethod
    def dataFromPath(path_: str):
        with open(path_, 'rb') as f:
            bytes_ =  f.read()
            return bytes_.decode('ascii') 


@dataclass
class ConnectionStringData(DataClassJsonMixin):
    serverId: Optional[str] = None
    dataBaseName: Optional[str] = None
    model: Optional[str] = None
    serverName: Optional[str] = None
    dynamicModel: Optional[bool] = False
    uniqueKey: Optional[str] = None


@dataclass 
class ImportDscMapItem(DataClassJsonMixin):
    connectionStringProperties: ConnectionStringProperties
    needsToPerformDsc: bool = True

@dataclass
class RelatedItemData(DataClassJsonMixin):
    name: str
    itemId: str
    contentType: Optional[ContentType] = ContentType.none
    children: List[RelatedItemData] = default_field([])
    rootFolderType: Optional[RootFolderType] = RootFolderType.privatedummy
    hasWriteAccess: Optional[bool] = False
    numberOfUsages: Optional[int] = 0
    sourceItemId: Optional[str] = None
    level: int = 0
    createdDate: Optional[int] = None
    createdBy: Optional[str] = None
    dataSourceProperties: ConnectionStringData = default_field({})
    folderPath: Optional[str] = None
    tenantId: Optional[str] = None
    securityHash: Optional[str] = None
    folderId: Optional[str] = None
    lockedByUser: Optional[str] = None
    itemIdAsString: Optional[str] = None

    def __post_init__(self):
        self.dataSourceProperties = ConnectionStringData(**self.dataSourceProperties)
        self.children = [RelatedItemData(**i) for i in self.children]

@dataclass
class ImportApiResultObject(DataClassJsonMixin):
    importDscMap: Dict[str, List[ImportDscMapItem]] = default_field({})
    failedItems: List[RelatedItemData] = default_field([])
    itemsIds: Dict[str, str] = default_field({})

    def __post_init__(self):
        result = {}

        for k, v in self.importDscMap.items():
            result[k] = [ImportDscMapItem(**i) for i in v]

        self.importDscMap = result
        self.failedItems = [RelatedItemData(**i) for i in self.failedItems]

@dataclass
class ExportOptions(DataClassJsonMixin):
    showUniqueName: bool = True
    columnHeaderAsCaption: bool = True

@dataclass
class FilterParameter(DataClassJsonMixin):
    value: str

@dataclass
class TargetParameter(DataClassJsonMixin):
    name: str
    filters: List[FilterParameter] = default_field([])
    syntaxType: Optional[SyntaxType] = SyntaxType.pql

    def __post_init__(self):
        self.filters = [FilterParameter(**i) for i in self.filters]

@dataclass
class ExternalParameters(DataClassJsonMixin):
    reportFilters: List[FilterParameter] = default_field([])
    targets: List[TargetParameter] = default_field([])
    slideNumber: Optional[int] = 0

    def __post_init__(self):
        self.reportFilters = [FilterParameter(**i) for i in self.reportFilters]
        self.targets = [TargetParameter(**i) for i in self.targets]

@dataclass
class QueryExportData(DataClassJsonMixin):
    itemId: str
    exportType: ApiResponseFormat
    exportOptions: Optional[ExportOptions] = None
    externalParameters: Optional[ExternalParameters] = None

@dataclass
class MasterFlowSourceObject(DataClassJsonMixin):
    masterFlowNodeId: str
    masterFlowNodeName: str
    dataFlowNodeId: str
    description: str
    serverId: str
    serverName: str
    serverType: ServerType
    databaseName: str
    validationMessage: str

@dataclass
class MasterFlowTargetObject(DataClassJsonMixin):
    masterFlowNodeId: str
    masterFlowNodeName: str
    dataFlowNodeId: str
    description: str
    serverId: str
    serverName: str
    serverType: ServerType
    createNewDb: bool
    databaseName: str
    validationMessage: str

@dataclass
class MasterFlowOtherObject(DataClassJsonMixin):
    masterFlowNodeId: str
    masterFlowNodeName: str
    dataFlowNodeId: str
    dataFlowNodeType: str
    dataFlowNodeName: str
    description: str
    validationMessage: str

@dataclass
class MasterFlowVariableObject(DataClassJsonMixin):
    masterFlowNodeId: str
    masterFlowNodeName: str
    dataFlowNodeId: str
    description: str
    serverId: str
    serverName: str
    serverType: ServerType
    databaseName: str
    validationMessage: str
    variableCurrentValue: str
    variableDataType: str
    variableType: str

@dataclass
class MasterFlowValidationResult(DataClassJsonMixin):
    sources: List[MasterFlowSourceObject]
    targets: List[MasterFlowTargetObject]
    others: List[MasterFlowOtherObject]
    variables: List[MasterFlowVariableObject]

    def __post_init__(self):
        self.sources = [MasterFlowSourceObject(**i) for i in self.sources]
        self.targets = [MasterFlowTargetObject(**i) for i in self.targets]
        self.others = [MasterFlowOtherObject(**i) for i in self.others]
        self.variables = [MasterFlowVariableObject(**i) for i in self.variables]


