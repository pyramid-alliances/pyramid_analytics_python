
from typing import (
    Any,
    Dict,
    List,
    Optional
)
from .objects import *
from .enum import *
from .api_interface import call_api

def getNotificationIndicators(userId: str) -> NotificationIndicatorsResult:
    """
    Description:
        Get current notification indicator counts
    
    Input:
        Name: userId
        Type: string
        Description: The system user ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: NotificationIndicatorsResult
        Description of Response Type: List of notification indicator counts for unread items.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/notification/getNotificationIndicators.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/notification/getNotificationIndicators",
                data=data, 
                response_type=NotificationIndicatorsResult
           )


