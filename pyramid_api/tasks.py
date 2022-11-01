
from typing import (
    Any,
    Dict,
    List,
    Optional
)
from .objects import *
from .enum import *
from .api_interface import call_api

def deleteSchedule(scheduleId: str) -> ModifiedItemsResult:
    """
    Description:
        Delete a Schedule
    
    Input:
        Name: scheduleId
        Type: string
        Description: The schedule's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/deleteSchedule.htm
    """
    
    data = {"scheduleId" : scheduleId,}
    return call_api("/API2/tasks/deleteSchedule",
                data=data,
                response_type=ModifiedItemsResult
           )



def findSchedule(searchCriteria: ScheduleSearchCriteria) -> List[ScheduleViewObject]:
    """
    Description:
        Find a Schedule
    
    Input:
        Name: searchCriteria
        Object Type: ScheduleSearchCriteria
        Description: The search criteria object for finding a schedule.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ScheduleViewObject[]
        Description of Response Type: The schedule listing object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/findSchedule.htm
    """
    data = { "searchCriteria" : searchCriteria }
    return call_api("/API2/tasks/findSchedule",
                data=data,
                response_type=List[ScheduleViewObject]
           )



def getExecutions(scheduleId: str) -> List[ExecutionViewData]:
    """
    Description:
        Get schedule's Executions
    
    Input:
        Name: scheduleId
        Type: string
        Description: The schedule's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ExecutionViewData[]
        Description of Response Type: The execution object contains all the details of scheduled execution instance. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/getExecutions.htm
    """
    
    data = {"scheduleId" : scheduleId,}
    return call_api("/API2/tasks/getExecutions",
                data=data,
                response_type=List[ExecutionViewData]
           )



def getScheduleExecutionStatus(executionId: str) -> ApiResultTaskStatus:
    """
    Description:
        Get a Schedule's Execution Status
    
    Input:
        Name: executionId
        Type: string
        Description: The execution's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ApiResultTaskStatus
        Description of Response Type: Returns the task status indicator
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/getScheduleExecutionStatus.htm
    """
    
    data = {"executionId" : executionId,}
    return call_api("/API2/tasks/getScheduleExecutionStatus",
                data=data,
                response_type=ApiResultTaskStatus
           )



def getSchedulesForUser(userId: str) -> List[ScheduleViewObject]:
    """
    Description:
        Gets a Userâs Schedules
    
    Input:
        Name: userId
        Type: string
        Description: The system user ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ScheduleViewObject[]
        Description of Response Type: The schedule listing object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/getSchedulesForUser.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/tasks/getSchedulesForUser",
                data=data,
                response_type=List[ScheduleViewObject]
           )



def getTaskData(taskId: str) -> TaskViewData:
    """
    Description:
        Get task's Data
    
    Input:
        Name: taskId
        Type: string
        Description: The task's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: TaskViewData
        Description of Response Type: Execution Tasks object with details of a scheduled job task.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/getTaskData.htm
    """
    
    data = {"taskId" : taskId,}
    return call_api("/API2/tasks/getTaskData",
                data=data,
                response_type=TaskViewData
           )



def getTaskOutputs(taskId: str) -> List[ItemId]:
    """
    Description:
        Get schedule task's Outputs
    
    Input:
        Name: taskId
        Type: string
        Description: The task's ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: A generic object used to contain ID's of items. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/getTaskOutputs.htm
    """
    
    data = {"taskId" : taskId,}
    return call_api("/API2/tasks/getTaskOutputs",
                data=data,
                response_type=List[ItemId]
           )



def getTaskOutputsForUser(taskUserApiData: TaskUserApiData) -> List[ItemId]:
    """
    Description:
        Get task's Outputs for a user
    
    Input:
        Name: taskUserApiData
        Object Type: TaskUserApiData
        Description: An object specifying the requested task id and user id .
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: A generic object used to contain ID's of items. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/getTaskOutputsForUser.htm
    """
    data = { "taskUserApiData" : taskUserApiData }
    return call_api("/API2/tasks/getTaskOutputsForUser",
                data=data,
                response_type=List[ItemId]
           )



def getTasks(executionsId: str) -> List[TaskViewData]:
    """
    Description:
        Get schedule execution's Tasks
    
    Input:
        Name: executionsId
        Type: string
        Description: The execution's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: TaskViewData[]
        Description of Response Type: Execution Tasks object with details of a scheduled job task. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/getTasks.htm
    """
    
    data = {"executionsId" : executionsId,}
    return call_api("/API2/tasks/getTasks",
                data=data,
                response_type=List[TaskViewData]
           )



def getTasksIds(executionsId: str) -> List[ItemId]:
    """
    Description:
        Get schedule execution's Tasks
    
    Input:
        Name: executionsId
        Type: string
        Description: The execution's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: A generic object used to contain ID's of items. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/getTasksIds.htm
    """
    
    data = {"executionsId" : executionsId,}
    return call_api("/API2/tasks/getTasksIds",
                data=data,
                response_type=List[ItemId]
           )



def reRunTask(taskId: str) -> ModifiedItemsResult:
    """
    Description:
        Run an Existing Schedule
    
    Input:
        Name: taskId
        Type: string
        Description: The task's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/reRunTask.htm
    """
    
    data = {"taskId" : taskId,}
    return call_api("/API2/tasks/reRunTask",
                data=data,
                response_type=ModifiedItemsResult
           )



def resumeSchedule(scheduleId: str) -> ModifiedItemsResult:
    """
    Description:
        Resume a Paused Schedule
    
    Input:
        Name: scheduleId
        Type: string
        Description: The schedule's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/resumeSchedule.htm
    """
    
    data = {"scheduleId" : scheduleId,}
    return call_api("/API2/tasks/resumeSchedule",
                data=data,
                response_type=ModifiedItemsResult
           )



def runSchedule(ExecuteScheduleApiData: ExecuteScheduleApiData) -> None:
    """
    Description:
        Run a Schedule
    
    Input:
        Name: ExecuteScheduleApiData
        Object Type: ExecuteScheduleApiData
        Description: An object for settings the execution parameters of a schedule.
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: Returns the executionId for the created execution
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/runSchedule.htm
    """
    data = { "ExecuteScheduleApiData" : ExecuteScheduleApiData }
    return call_api("/API2/tasks/runSchedule",
                data=data,
                response_type=None
           )



def suspendSchedule(scheduleId: str) -> ModifiedItemsResult:
    """
    Description:
        Pause an Active Schedule
    
    Input:
        Name: scheduleId
        Type: string
        Description: The schedule's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/tasks/suspendSchedule.htm
    """
    
    data = {"scheduleId" : scheduleId,}
    return call_api("/API2/tasks/suspendSchedule",
                data=data,
                response_type=ModifiedItemsResult
           )


