
from typing import (
    Any,
    Dict,
    List,
    Optional
)
from .objects import *
from .enum import *
from .api_interface import call_api

def authenticateUser(userCredentials: UserCredentials) -> str:
    """
    Description:
        Authenticate User
    
    Input:
        Name: userCredentials
        Object Type: UserCredentials
        Description: The user credential object used to set a user's login settings.
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: The response is the security token as a base64 string. It is usually stored in a cookie.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/auth/authenticateUser.htm
    """
    data = { "userCredentials" : userCredentials }
    return call_api("/API2/auth/authenticateUser",
                data=data,
                response_type=str
           )



def authenticateUserByToken(userTokenCredentials: UserTokenCredentials) -> str:
    """
    Description:
        Authenticate User using Tokens
    
    Input:
        Name: userTokenCredentials
        Object Type: UserTokenCredentials
        Description: The user credentials for authentication by token.
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: The response is the security token as a base64 string. It is usually stored in a cookie.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/auth/authenticateUserByToken.htm
    """
    data = { "userTokenCredentials" : userTokenCredentials }
    return call_api("/API2/auth/authenticateUserByToken",
                data=data,
                response_type=str
           )



def authenticateUserEmbed(userCredentials: UserCredentials) -> str:
    """
    Description:
        Authenticate User for Embedding
    
    Input:
        Name: userCredentials
        Object Type: UserCredentials
        Description: The user credential object used to set a user's login settings.
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: The response is the security token as a base64 string. It is usually stored in a cookie.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/auth/authenticateUserEmbed.htm
    """
    data = { "userCredentials" : userCredentials }
    return call_api("/API2/auth/authenticateUserEmbed",
                data=data,
                response_type=str
           )



def authenticateUserEmbedByToken(userTokenCredentials: UserTokenCredentials) -> str:
    """
    Description:
        Authenticate User for Embedding using Tokens
    
    Input:
        Name: userTokenCredentials
        Object Type: UserTokenCredentials
        Description: The user credentials for authentication by token.
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: The response is the security token as a base64 string. It is usually stored in a cookie.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/auth/authenticateUserEmbedByToken.htm
    """
    data = { "userTokenCredentials" : userTokenCredentials }
    return call_api("/API2/auth/authenticateUserEmbedByToken",
                data=data,
                response_type=str
           )



def authenticateUserEmbedOPENID(userOpenIdCredentials: UserOpenIdCredentials) -> str:
    """
    Description:
        Authenticate User for Embedding with OpenID Authentication
    
    Input:
        Name: userOpenIdCredentials
        Object Type: UserOpenIdCredentials
        Description: The user credentials for authentication by OpenID parameter map.
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: The response is the security token as a base64 string. It is usually stored in a cookie.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/auth/authenticateUserEmbedOPENID.htm
    """
    data = { "userOpenIdCredentials" : userOpenIdCredentials }
    return call_api("/API2/auth/authenticateUserEmbedOPENID",
                data=data,
                response_type=str
           )



def authenticateUserEmbedSAML(userSamlCredentials: UserSamlCredentials) -> str:
    """
    Description:
        Authenticate User for Embedding with SAML Authentication
    
    Input:
        Name: userSamlCredentials
        Object Type: UserSamlCredentials
        Description: The user credentials for authentication by SAML token.
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: The response is the security token as a base64 string. It is usually stored in a cookie.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/auth/authenticateUserEmbedSAML.htm
    """
    data = { "userSamlCredentials" : userSamlCredentials }
    return call_api("/API2/auth/authenticateUserEmbedSAML",
                data=data,
                response_type=str
           )



def authenticateUserEmbedWindows(domain: str) -> str:
    """
    Description:
        Authenticate User for Embedding with Window Authentication
    
    Input:
        Name: domain
        Type: string
        Description: The URL web domain - needed only for embedded authentication.
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: The response is the security token as a base64 string. It is usually stored in a cookie.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/auth/authenticateUserEmbedWindows.htm
    """
    
    data = {"domain" : domain,}
    return call_api("/API2/auth/authenticateUserEmbedWindows",
                data=data,
                response_type=str
           )



def authenticateUserOPENID(parameterMap: str) -> str:
    """
    Description:
        Authenticate User with OpenID Authentication
    
    Input:
        Name: parameterMap
        Type: string
        Description: The OpenID parameter map serialized to String representation
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: The response is the security token as a base64 string. It is usually stored in a cookie.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/auth/authenticateUserOPENID.htm
    """
    
    data = {"parameterMap" : parameterMap,}
    return call_api("/API2/auth/authenticateUserOPENID",
                data=data,
                response_type=str
           )



def authenticateUserOPENIDAlt(userOpenIdCredentials: UserOpenIdCredentials) -> str:
    """
    Description:
        Authenticate User with OpenID Authentication
    
    Input:
        Name: userOpenIdCredentials
        Object Type: UserOpenIdCredentials
        Description: The user credentials for authentication by OpenID parameter map.
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: The response is the security token as a base64 string. It is usually stored in a cookie.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/auth/authenticateUserOPENIDAlt.htm
    """
    data = { "userOpenIdCredentials" : userOpenIdCredentials }
    return call_api("/API2/auth/authenticateUserOPENIDAlt",
                data=data,
                response_type=str
           )



def authenticateUserSAML(token: str) -> str:
    """
    Description:
        Authenticate User with SAML Authentication
    
    Input:
        Name: token
        Type: string
        Description: The SAML assertion token
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: The response is the security token as a base64 string. It is usually stored in a cookie.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/auth/authenticateUserSAML.htm
    """
    
    data = {"token" : token,}
    return call_api("/API2/auth/authenticateUserSAML",
                data=data,
                response_type=str
           )



def authenticateUserSAMLAlt(userSamlCredentials: UserSamlCredentials) -> str:
    """
    Description:
        Authenticate User with SAML Authentication
    
    Input:
        Name: userSamlCredentials
        Object Type: UserSamlCredentials
        Description: The user credentials for authentication by SAML token.
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: The response is the security token as a base64 string. It is usually stored in a cookie.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/auth/authenticateUserSAMLAlt.htm
    """
    data = { "userSamlCredentials" : userSamlCredentials }
    return call_api("/API2/auth/authenticateUserSAMLAlt",
                data=data,
                response_type=str
           )



def authenticateUserWindows() -> str:
    """
    Description:
        Authenticate User with Window Authentication
    
    Output:
        Successful Result Code: 200
        Description of Response Type: The response is the security token as a base64 string. It is usually stored in a cookie.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/auth/authenticateUserWindows.htm
    """
    
    return call_api("/API2/auth/authenticateUserWindows",
                data=None,
                response_type=str
           )


