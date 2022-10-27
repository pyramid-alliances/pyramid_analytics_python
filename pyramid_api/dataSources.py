
from typing import (
    Any,
    Dict,
    List,
    Optional
)
from .objects import *
from .enum import *
from .api_interface import call_api

def addHierarchySecurityToModel(hierarchyMeasureSecurityApiObject: HierarchyMeasureSecurityApiObject) -> ModifiedItemsResult:
    """
    Description:
        Applies data security to model attribute hierarchies
    
    Input:
        Name: hierarchyMeasureSecurityApiObject
        Object Type: HierarchyMeasureSecurityApiObject
        Description: Details of the security settings to be applied to a data model's hierarchies or measures.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/addHierarchySecurityToModel.htm
    """
    data = { "hierarchyMeasureSecurityApiObject" : hierarchyMeasureSecurityApiObject }
    return call_api("/API2/dataSources/addHierarchySecurityToModel",
                data=data, 
                response_type=ModifiedItemsResult
           )



def addMeasureSecurityToModel(hierarchyMeasureSecurityApiObject: HierarchyMeasureSecurityApiObject) -> ModifiedItemsResult:
    """
    Description:
        Applies data security to model measures
    
    Input:
        Name: hierarchyMeasureSecurityApiObject
        Object Type: HierarchyMeasureSecurityApiObject
        Description: Details of the security settings to be applied to a data model's hierarchies or measures.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/addMeasureSecurityToModel.htm
    """
    data = { "hierarchyMeasureSecurityApiObject" : hierarchyMeasureSecurityApiObject }
    return call_api("/API2/dataSources/addMeasureSecurityToModel",
                data=data, 
                response_type=ModifiedItemsResult
           )



def addMembersSecurityToModel(membersSecurityObject: MembersSecurityApiObject) -> ModifiedItemsResult:
    """
    Description:
        Applies data security to hierarchy members
    
    Input:
        Name: membersSecurityObject
        Object Type: MembersSecurityApiObject
        Description: Details of the security settings to be applied to a data model hierarchy's member elements.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/addMembersSecurityToModel.htm
    """
    data = { "membersSecurityObject" : membersSecurityObject }
    return call_api("/API2/dataSources/addMembersSecurityToModel",
                data=data, 
                response_type=ModifiedItemsResult
           )



def addRolesToDataBase(itemRoles: ItemRolesToBeAdded) -> ModifiedItemsResult:
    """
    Description:
        Add Roles to a Data Source Database
    
    Input:
        Name: itemRoles
        Object Type: ItemRolesToBeAdded
        Description: Object with roles and items to be added.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/addRolesToDataBase.htm
    """
    data = { "itemRoles" : itemRoles }
    return call_api("/API2/dataSources/addRolesToDataBase",
                data=data, 
                response_type=ModifiedItemsResult
           )



def addRolesToItemAndBubbleUp(itemRoles: ItemRolesToBeAdded) -> ModifiedItemsResult:
    """
    Description:
        Add roles to a data source item with bubble up.
    
    Input:
        Name: itemRoles
        Object Type: ItemRolesToBeAdded
        Description: Object with roles and items to be added.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/addRolesToItemAndBubbleUp.htm
    """
    data = { "itemRoles" : itemRoles }
    return call_api("/API2/dataSources/addRolesToItemAndBubbleUp",
                data=data, 
                response_type=ModifiedItemsResult
           )



def addRolesToItemAndPropagate(itemRoles: ItemRolesToBeAdded) -> ModifiedItemsResult:
    """
    Description:
        Add roles to a data source item with propagate down.
    
    Input:
        Name: itemRoles
        Object Type: ItemRolesToBeAdded
        Description: Object with roles and items to be added.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/addRolesToItemAndPropagate.htm
    """
    data = { "itemRoles" : itemRoles }
    return call_api("/API2/dataSources/addRolesToItemAndPropagate",
                data=data, 
                response_type=ModifiedItemsResult
           )



def addRolesToModel(itemRoles: ItemRolesToBeAdded) -> ModifiedItemsResult:
    """
    Description:
        Add Roles to a Materialized Model
    
    Input:
        Name: itemRoles
        Object Type: ItemRolesToBeAdded
        Description: Object with roles and items to be added.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/addRolesToModel.htm
    """
    data = { "itemRoles" : itemRoles }
    return call_api("/API2/dataSources/addRolesToModel",
                data=data, 
                response_type=ModifiedItemsResult
           )



def addRolesToServer(itemRoles: ItemRolesToBeAdded) -> ModifiedItemsResult:
    """
    Description:
        Add Roles to a Data Source Server
    
    Input:
        Name: itemRoles
        Object Type: ItemRolesToBeAdded
        Description: Object with roles and items to be added.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/addRolesToServer.htm
    """
    data = { "itemRoles" : itemRoles }
    return call_api("/API2/dataSources/addRolesToServer",
                data=data, 
                response_type=ModifiedItemsResult
           )



def changeDataSource(dscApiData: DscApiData) -> ModifiedItemsResult:
    """
    Description:
        Change an Item's Data Source
    
    Input:
        Name: dscApiData
        Object Type: DscApiData
        Description: The data source changer settings object.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/changeDataSource.htm
    """
    data = { "dscApiData" : dscApiData }
    return call_api("/API2/dataSources/changeDataSource",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createDataServer(serverData: ServerData) -> ModifiedItemsResult:
    """
    Description:
        Create a new Data Source
    
    Input:
        Name: serverData
        Object Type: ServerData
        Description: 
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/createDataServer.htm
    """
    data = { "serverData" : serverData }
    return call_api("/API2/dataSources/createDataServer",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createDataServers(serverData: List[ServerData]) -> ModifiedItemsResult:
    """
    Description:
        Create Multiple Data Sources from a List
    
    Input:
        Name: serverData
        Object Type: ServerData[]
        Description: 
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/createDataServers.htm
    """
    data = { "serverData" : serverData }
    return call_api("/API2/dataSources/createDataServers",
                data=data, 
                response_type=ModifiedItemsResult
           )



def deleteDataBase(databaseId: str) -> ModifiedItemsResult:
    """
    Description:
        Delete an Existing Database
    
    Input:
        Name: databaseId
        Type: string
        Description: The database's ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/deleteDataBase.htm
    """
    
    data = {"databaseId" : databaseId,}
    return call_api("/API2/dataSources/deleteDataBase",
                data=data, 
                response_type=ModifiedItemsResult
           )



def deleteDataSource(sourceId: str) -> ModifiedItemsResult:
    """
    Description:
        Delete a Data Source
    
    Input:
        Name: sourceId
        Type: string
        Description: The data source's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/deleteDataSource.htm
    """
    
    data = {"sourceId" : sourceId,}
    return call_api("/API2/dataSources/deleteDataSource",
                data=data, 
                response_type=ModifiedItemsResult
           )



def deleteMaterializedModel(modelId: str) -> ModifiedItemsResult:
    """
    Description:
        Delete a Materialized Model
    
    Input:
        Name: modelId
        Type: string
        Description: The item's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/deleteMaterializedModel.htm
    """
    
    data = {"modelId" : modelId,}
    return call_api("/API2/dataSources/deleteMaterializedModel",
                data=data, 
                response_type=ModifiedItemsResult
           )



def deleteRolesFromDatabase(itemRoles: ItemRolesForRemoval) -> ModifiedItemsResult:
    """
    Description:
        Delete Roles from a Data Source Database
    
    Input:
        Name: itemRoles
        Object Type: ItemRolesForRemoval
        Description: Object with roles and items to be removed.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/deleteRolesFromDatabase.htm
    """
    data = { "itemRoles" : itemRoles }
    return call_api("/API2/dataSources/deleteRolesFromDatabase",
                data=data, 
                response_type=ModifiedItemsResult
           )



def deleteRolesFromModel(itemRoles: ItemRolesForRemoval) -> ModifiedItemsResult:
    """
    Description:
        Delete Roles from a Materialized Model
    
    Input:
        Name: itemRoles
        Object Type: ItemRolesForRemoval
        Description: Object with roles and items to be removed.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/deleteRolesFromModel.htm
    """
    data = { "itemRoles" : itemRoles }
    return call_api("/API2/dataSources/deleteRolesFromModel",
                data=data, 
                response_type=ModifiedItemsResult
           )



def deleteRolesFromServer(itemRoles: ItemRolesForRemoval) -> ModifiedItemsResult:
    """
    Description:
        Delete Roles from a Data Source Server
    
    Input:
        Name: itemRoles
        Object Type: ItemRolesForRemoval
        Description: Object with roles and items to be removed.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/deleteRolesFromServer.htm
    """
    data = { "itemRoles" : itemRoles }
    return call_api("/API2/dataSources/deleteRolesFromServer",
                data=data, 
                response_type=ModifiedItemsResult
           )



def executeMasterFlow(executeMasterFlowObject: ExecuteMasterFlowObject) -> ExecuteMasterFlowResult:
    """
    Description:
        Executes a Master Flow
    
    Input:
        Name: executeMasterFlowObject
        Object Type: ExecuteMasterFlowObject
        Description: Input parameters needed to execute a Master Flow
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ExecuteMasterFlowResult
        Description of Response Type: Execute master flow result
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/executeMasterFlow.htm
    """
    data = { "executeMasterFlowObject" : executeMasterFlowObject }
    return call_api("/API2/dataSources/executeMasterFlow",
                data=data, 
                response_type=ExecuteMasterFlowResult
           )



def exportModel(materializedModelId: str) -> ExportData:
    """
    Description:
        Export a PIE file
    
    Input:
        Name: materializedModelId
        Type: string
        Description: The system ID of the materialized model
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ExportData
        Description of Response Type: The object representing the exported PIE file.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/exportModel.htm
    """
    
    data = {"materializedModelId" : materializedModelId,}
    return call_api("/API2/dataSources/exportModel",
                data=data, 
                response_type=ExportData
           )



def findDatabaseByName(searchCriteria: ConnectedItemsSearchCriteria) -> List[MaterializedItemObject]:
    """
    Description:
        Find a Data Source Database
    
    Input:
        Name: searchCriteria
        Object Type: ConnectedItemsSearchCriteria
        Description: The search criteria for finding materialized data elements.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: MaterializedItemObject[]
        Description of Response Type: The search results object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/findDatabaseByName.htm
    """
    data = { "searchCriteria" : searchCriteria }
    return call_api("/API2/dataSources/findDatabaseByName",
                data=data, 
                response_type=List[MaterializedItemObject]
           )



def findModelByName(searchCriteria: ConnectedItemsSearchCriteria) -> List[MaterializedItemObject]:
    """
    Description:
        Find a Materialized model
    
    Input:
        Name: searchCriteria
        Object Type: ConnectedItemsSearchCriteria
        Description: The search criteria for finding materialized data elements.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: MaterializedItemObject[]
        Description of Response Type: The search results object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/findModelByName.htm
    """
    data = { "searchCriteria" : searchCriteria }
    return call_api("/API2/dataSources/findModelByName",
                data=data, 
                response_type=List[MaterializedItemObject]
           )



def findServerByName(searchCriteria: SearchCriteria) -> List[MaterializedItemObject]:
    """
    Description:
        Find a Data Source Server
    
    Input:
        Name: searchCriteria
        Object Type: SearchCriteria
        Description: The search criteria for finding materialized data elements.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: MaterializedItemObject[]
        Description of Response Type: The search results object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/findServerByName.htm
    """
    data = { "searchCriteria" : searchCriteria }
    return call_api("/API2/dataSources/findServerByName",
                data=data, 
                response_type=List[MaterializedItemObject]
           )



def getAllConnectionStrings() -> List[ConnectionStringProperties]:
    """
    Description:
        Get all Data Connections
    
    Output:
        Successful Result Code: 200
        Response List Type: ConnectionStringProperties[]
        Description of Response Type: The connection object representing the details of the data sources. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getAllConnectionStrings.htm
    """
    
    return call_api("/API2/dataSources/getAllConnectionStrings",
                data=None, 
                response_type=List[ConnectionStringProperties]
           )



def getDataModelStructure(modelId: str) -> ModelingModel:
    """
    Description:
        Extract the structure of a data model
    
    Input:
        Name: modelId
        Type: string
        Description: The model's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModelingModel
        Description of Response Type: The model definition that contains details of tables, their relationships and joins, and measures.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getDataModelStructure.htm
    """
    
    data = {"modelId" : modelId,}
    return call_api("/API2/dataSources/getDataModelStructure",
                data=data, 
                response_type=ModelingModel
           )



def getDataSourcesByTenant(tenantId: str) -> List[MaterializedItemObject]:
    """
    Description:
        Get all Datasources for a Tenant.
    
    Input:
        Name: tenantId
        Type: string
        Description: The tenant's ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: MaterializedItemObject[]
        Description of Response Type: Result object with success or failure flag and related messages. Also includes the servers found Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getDataSourcesByTenant.htm
    """
    
    data = {"tenantId" : tenantId,}
    return call_api("/API2/dataSources/getDataSourcesByTenant",
                data=data, 
                response_type=List[MaterializedItemObject]
           )



def getDataSourcesByUserId(userId: str) -> ModifiedItemsResult:
    """
    Description:
        Get an Tenant's Data Sources
    
    Input:
        Name: userId
        Type: string
        Description: The tenant's ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getDataSourcesByUserId.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/dataSources/getDataSourcesByUserId",
                data=data, 
                response_type=ModifiedItemsResult
           )



def getDatasourceUsedTables(findDataSourceObject: MasterFlowFindDataSourceObject) -> DataSourceUsedTablesResult:
    """
    Description:
        Get data source used tables.
    
    Input:
        Name: findDataSourceObject
        Object Type: MasterFlowFindDataSourceObject
        Description: Use this object to find a specific data source
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: DataSourceUsedTablesResult
        Description of Response Type: List of used tables of a data source node within a data flow.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getDatasourceUsedTables.htm
    """
    data = { "findDataSourceObject" : findDataSourceObject }
    return call_api("/API2/dataSources/getDatasourceUsedTables",
                data=data, 
                response_type=DataSourceUsedTablesResult
           )



def getItemConnectionString(pyramidItemIdentifier: PyramidItemIdentifier) -> List[ConnectionStringProperties]:
    """
    Description:
        Get an Item's Data Source Details
    
    Input:
        Name: pyramidItemIdentifier
        Object Type: PyramidItemIdentifier
        Description: The item idenifier object.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ConnectionStringProperties[]
        Description of Response Type: The connection object representing the details of the data sources. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getItemConnectionString.htm
    """
    data = { "pyramidItemIdentifier" : pyramidItemIdentifier }
    return call_api("/API2/dataSources/getItemConnectionString",
                data=data, 
                response_type=List[ConnectionStringProperties]
           )



def getMasterFlowProgressUpdate(scheduleId: str) -> MasterFlowProgressResult:
    """
    Description:
        Get Master Flow Execution Progress
    
    Input:
        Name: scheduleId
        Type: string
        Description: The schedule's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: MasterFlowProgressResult
        Description of Response Type: The master flow progress update
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getMasterFlowProgressUpdate.htm
    """
    
    data = {"scheduleId" : scheduleId,}
    return call_api("/API2/dataSources/getMasterFlowProgressUpdate",
                data=data, 
                response_type=MasterFlowProgressResult
           )



def getMasterFlowVariables(itemId: str) -> MasterFlowVariablesResult:
    """
    Description:
        Get all variables in a Master Flow
    
    Input:
        Name: itemId
        Type: string
        Description: The item's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: MasterFlowVariablesResult
        Description of Response Type: List of variables based on a query with all their connection details
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getMasterFlowVariables.htm
    """
    
    data = {"itemId" : itemId,}
    return call_api("/API2/dataSources/getMasterFlowVariables",
                data=data, 
                response_type=MasterFlowVariablesResult
           )



def getRolesByDataBase(dataBaseId: str) -> List[ItemRolePair]:
    """
    Description:
        Get Data Source Database Roles
    
    Input:
        Name: dataBaseId
        Type: string
        Description: The database's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemRolePair[]
        Description of Response Type: Object with role and role access types. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getRolesByDataBase.htm
    """
    
    data = {"dataBaseId" : dataBaseId,}
    return call_api("/API2/dataSources/getRolesByDataBase",
                data=data, 
                response_type=List[ItemRolePair]
           )



def getRolesByModel(modelId: str) -> List[ItemRolePair]:
    """
    Description:
        Get Materialized Model Roles
    
    Input:
        Name: modelId
        Type: string
        Description: The materialized model's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemRolePair[]
        Description of Response Type: Object with role and role access types. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getRolesByModel.htm
    """
    
    data = {"modelId" : modelId,}
    return call_api("/API2/dataSources/getRolesByModel",
                data=data, 
                response_type=List[ItemRolePair]
           )



def getRolesByServer(serverId: str) -> List[ItemRolePair]:
    """
    Description:
        Get Data Source Server Roles
    
    Input:
        Name: serverId
        Type: string
        Description: The server's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemRolePair[]
        Description of Response Type: Object with role and role access types. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getRolesByServer.htm
    """
    
    data = {"serverId" : serverId,}
    return call_api("/API2/dataSources/getRolesByServer",
                data=data, 
                response_type=List[ItemRolePair]
           )



def getServerDataById(dataServerId: str) -> ServerData:
    """
    Description:
        Get a Server's Data Details
    
    Input:
        Name: dataServerId
        Type: string
        Description: The dataServer's ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ServerData
        Description of Response Type: Result object with success or failure flag and related messages. Also includes the data source's ID
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getServerDataById.htm
    """
    
    data = {"dataServerId" : dataServerId,}
    return call_api("/API2/dataSources/getServerDataById",
                data=data, 
                response_type=ServerData
           )



def getSourceByNodeId(findDataSourceObject: MasterFlowFindDataSourceObject) -> MasterFlowSourceObject:
    """
    Description:
        Get a specific Data Source by Data Flow Node ID
    
    Input:
        Name: findDataSourceObject
        Object Type: MasterFlowFindDataSourceObject
        Description: Use this object to find a specific data source
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: MasterFlowSourceObject
        Description of Response Type: The master flow data source object contains information about the connection of a specific source ETL node or master flow sql script node and the validation message result
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getSourceByNodeId.htm
    """
    data = { "findDataSourceObject" : findDataSourceObject }
    return call_api("/API2/dataSources/getSourceByNodeId",
                data=data, 
                response_type=MasterFlowSourceObject
           )



def getTargetByNodeId(findDataSourceObject: MasterFlowFindDataSourceObject) -> MasterFlowTargetObject:
    """
    Description:
        Get a specific Data Target by Data Flow Node ID
    
    Input:
        Name: findDataSourceObject
        Object Type: MasterFlowFindDataSourceObject
        Description: Use this object to find a specific data source
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: MasterFlowTargetObject
        Description of Response Type: The master flow target object contains information about the connection of a specific target ETL node and the validation message result
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/getTargetByNodeId.htm
    """
    data = { "findDataSourceObject" : findDataSourceObject }
    return call_api("/API2/dataSources/getTargetByNodeId",
                data=data, 
                response_type=MasterFlowTargetObject
           )



def importModel(modelApiObject: MaterializedApiObject) -> None:
    """
    Description:
        Import a Data Model
    
    Input:
        Name: modelApiObject
        Object Type: MaterializedApiObject
        Description: The object representing the details for where to import a model PIE file.
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: successful operation
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/importModel.htm
    """
    data = { "modelApiObject" : modelApiObject }
    return call_api("/API2/dataSources/importModel",
                data=data, 
                response_type=None
           )



def recognizeDataBase(dataBaseRecognitionObject: DataBaseRecognitionObject) -> ModifiedItemsResult:
    """
    Description:
        Recognize a Database
    
    Input:
        Name: dataBaseRecognitionObject
        Object Type: DataBaseRecognitionObject
        Description: The database and its details object.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/recognizeDataBase.htm
    """
    data = { "dataBaseRecognitionObject" : dataBaseRecognitionObject }
    return call_api("/API2/dataSources/recognizeDataBase",
                data=data, 
                response_type=ModifiedItemsResult
           )



def recognizeModel(modelRecognitionObject: ModelRecognitionObject) -> ModifiedItemsResult:
    """
    Description:
        Recognize an existing Data Model
    
    Input:
        Name: modelRecognitionObject
        Object Type: ModelRecognitionObject
        Description: The model and its details.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/recognizeModel.htm
    """
    data = { "modelRecognitionObject" : modelRecognitionObject }
    return call_api("/API2/dataSources/recognizeModel",
                data=data, 
                response_type=ModifiedItemsResult
           )



def updateDataFlowNodeSchemas(schemasObject: MasterFlowSchemasObject) -> ApiModifierResult:
    """
    Description:
        Update data source used schemas.
    
    Input:
        Name: schemasObject
        Object Type: MasterFlowSchemasObject
        Description: Use this object to update the database schemas used in the data flow.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ApiModifierResult
        Description of Response Type: successful operation
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/updateDataFlowNodeSchemas.htm
    """
    data = { "schemasObject" : schemasObject }
    return call_api("/API2/dataSources/updateDataFlowNodeSchemas",
                data=data, 
                response_type=ApiModifierResult
           )



def updateModelName(modelNameObject: MasterFlowModelNameObject) -> MasterFlowUpdatedVariableResult:
    """
    Description:
        Update model name.
    
    Input:
        Name: modelNameObject
        Object Type: MasterFlowModelNameObject
        Description: Use this object to update model name.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: MasterFlowUpdatedVariableResult
        Description of Response Type: The master flow updated list of variables result
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/updateModelName.htm
    """
    data = { "modelNameObject" : modelNameObject }
    return call_api("/API2/dataSources/updateModelName",
                data=data, 
                response_type=MasterFlowUpdatedVariableResult
           )



def updateSourceNodeConnection(connectionObject: MasterFlowSourceConnectionObject) -> ModifiedItemsResult:
    """
    Description:
        Update the Connection for a Data Source
    
    Input:
        Name: connectionObject
        Object Type: MasterFlowSourceConnectionObject
        Description: Use this object to modify the data source server and/or the database in a data flow.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/updateSourceNodeConnection.htm
    """
    data = { "connectionObject" : connectionObject }
    return call_api("/API2/dataSources/updateSourceNodeConnection",
                data=data, 
                response_type=ModifiedItemsResult
           )



def updateTargetNodeConnection(connectionObject: MasterFlowTargetConnectionObject) -> ModifiedItemsResult:
    """
    Description:
        Update the Connection for a Data Target
    
    Input:
        Name: connectionObject
        Object Type: MasterFlowTargetConnectionObject
        Description: Use this object to modify the data target server and/or the database in a data flow.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/updateTargetNodeConnection.htm
    """
    data = { "connectionObject" : connectionObject }
    return call_api("/API2/dataSources/updateTargetNodeConnection",
                data=data, 
                response_type=ModifiedItemsResult
           )



def updateVariableConnection(connectionObject: MasterFlowVariableConnectionObject) -> ModifiedItemsResult:
    """
    Description:
        Update the Connection for a Variable
    
    Input:
        Name: connectionObject
        Object Type: MasterFlowVariableConnectionObject
        Description: Use this object to modify the data source server ID or/and database name used in the variable connection.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/updateVariableConnection.htm
    """
    data = { "connectionObject" : connectionObject }
    return call_api("/API2/dataSources/updateVariableConnection",
                data=data, 
                response_type=ModifiedItemsResult
           )



def updateVariableValue(variablesValueObject: MasterFlowVariablesValueObject) -> MasterFlowUpdatedVariableResult:
    """
    Description:
        Sets the values of a list of variables
    
    Input:
        Name: variablesValueObject
        Object Type: MasterFlowVariablesValueObject
        Description: Use this object to modify the values of a list of variables used in a Master Flow.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: MasterFlowUpdatedVariableResult
        Description of Response Type: The master flow updated list of variables result
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/updateVariableValue.htm
    """
    data = { "variablesValueObject" : variablesValueObject }
    return call_api("/API2/dataSources/updateVariableValue",
                data=data, 
                response_type=MasterFlowUpdatedVariableResult
           )



def validateMasterFlow(validateMasterFlowObject: ExecuteMasterFlowObject) -> MasterFlowValidationResult:
    """
    Description:
        Validates a Master Flow
    
    Input:
        Name: validateMasterFlowObject
        Object Type: ExecuteMasterFlowObject
        Description: Input parameters needed to execute a Master Flow
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: MasterFlowValidationResult
        Description of Response Type: Validation result, includes list for each validation type object
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/dataSources/validateMasterFlow.htm
    """
    data = { "validateMasterFlowObject" : validateMasterFlowObject }
    return call_api("/API2/dataSources/validateMasterFlow",
                data=data, 
                response_type=MasterFlowValidationResult
           )


