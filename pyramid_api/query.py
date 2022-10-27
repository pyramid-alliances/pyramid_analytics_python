
from typing import (
    Any,
    Dict,
    List,
    Optional
)
from .objects import *
from .enum import *
from .api_interface import call_api

def extractQueryResult(data: QueryExportData) -> None:
    """
    Description:
        Extract Query Results
    
    Input:
        Name: data
        Object Type: QueryExportData
        Description: The query export object used to specify how to extract query results.
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: successful operation
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/query/extractQueryResult.htm
    """
    data = { "data" : data }
    return call_api("/API2/query/extractQueryResult",
                data=data, 
                response_type=None
           )



def getParameterElements(parameterId: str) -> EnumerationOutput:
    """
    Description:
        Extract a Slicer / Parameter's members
    
    Input:
        Name: parameterId
        Type: string
        Description: The parameter's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: EnumerationOutput
        Description of Response Type: successful operation
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/query/getParameterElements.htm
    """
    
    data = {"parameterId" : parameterId,}
    return call_api("/API2/query/getParameterElements",
                data=data, 
                response_type=EnumerationOutput
           )


