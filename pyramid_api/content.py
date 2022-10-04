
from typing import (
    Any,
    Dict,
    List,
    Optional
)
from .objects import *
from .enum import *
from .api_interface import call_api

def addContentItemsToFavorites(data: ItemsForFavorites) -> ModifiedItemsResult:
    """
    Description:
        Add content items to user favorites
    
    Input:
        Name: data
        Object Type: ItemsForFavorites
        Description: The listing of favorite content items for a user.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/addContentItemsToFavorites.htm
    """
    data = { "data" : data }
    return call_api("/API2/content/addContentItemsToFavorites",
                data=data, 
                response_type=ModifiedItemsResult
           )



def addRoleToItem(roleToItemApiData: RoleToItemApiData) -> ModifiedItemsResult:
    """
    Description:
        Add role to a content Item
    
    Input:
        Name: roleToItemApiData
        Object Type: RoleToItemApiData
        Description: The role object with settings to be set for the chosen content item.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/addRoleToItem.htm
    """
    data = { "roleToItemApiData" : roleToItemApiData }
    return call_api("/API2/content/addRoleToItem",
                data=data, 
                response_type=ModifiedItemsResult
           )



def addTag(tagData: TagData) -> ModifiedItemsResult:
    """
    Description:
        Add a Tag to the content system
    
    Input:
        Name: tagData
        Object Type: TagData
        Description: The tag object used to capture a tag's settings.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/addTag.htm
    """
    data = { "tagData" : tagData }
    return call_api("/API2/content/addTag",
                data=data, 
                response_type=ModifiedItemsResult
           )



def addTagToItem(tagUsageApiData: TagUsageApiData) -> ModifiedItemsResult:
    """
    Description:
        Set a Tag to a content item
    
    Input:
        Name: tagUsageApiData
        Object Type: TagUsageApiData
        Description: The tag usage object used to set a tag for a given content item.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/addTagToItem.htm
    """
    data = { "tagUsageApiData" : tagUsageApiData }
    return call_api("/API2/content/addTagToItem",
                data=data, 
                response_type=ModifiedItemsResult
           )



def changeItemDescription(changeItemDescriptionData: ChangeItemDescriptionData) -> ModifiedItemsResult:
    """
    Description:
        Change Content Item's Description
    
    Input:
        Name: changeItemDescriptionData
        Object Type: ChangeItemDescriptionData
        Description: The change object used to set a description for a given content item.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/changeItemDescription.htm
    """
    data = { "changeItemDescriptionData" : changeItemDescriptionData }
    return call_api("/API2/content/changeItemDescription",
                data=data, 
                response_type=ModifiedItemsResult
           )



def changeItemFolder(itemParentApiData: ItemParentApiData) -> ModifiedItemsResult:
    """
    Description:
        Change the Parent Folder of a content item
    
    Input:
        Name: itemParentApiData
        Object Type: ItemParentApiData
        Description: The item-parent object used to set the content item's parent item ID.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/changeItemFolder.htm
    """
    data = { "itemParentApiData" : itemParentApiData }
    return call_api("/API2/content/changeItemFolder",
                data=data, 
                response_type=ModifiedItemsResult
           )



def copyItems(moveItemsObject: MoveItemsObject) -> ModifiedItemsResult:
    """
    Description:
        Copy Items
    
    Input:
        Name: moveItemsObject
        Object Type: MoveItemsObject
        Description: The move/copy items object with details of the selected content items and the destination folder.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/copyItems.htm
    """
    data = { "moveItemsObject" : moveItemsObject }
    return call_api("/API2/content/copyItems",
                data=data, 
                response_type=ModifiedItemsResult
           )



def createNewFolder(folderApiData: NewFolderApiData) -> ModifiedItemsResult:
    """
    Description:
        Add a New Folder
    
    Input:
        Name: folderApiData
        Object Type: NewFolderApiData
        Description: The listing of content items object.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/createNewFolder.htm
    """
    data = { "folderApiData" : folderApiData }
    return call_api("/API2/content/createNewFolder",
                data=data, 
                response_type=ModifiedItemsResult
           )



def deleteTag(tagId: str) -> ModifiedItemsResult:
    """
    Description:
        Delete a Tag
    
    Input:
        Name: tagId
        Type: string
        Description: The system tag ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: TagData
        Description of Response Type: The tag object used to capture a tag's settings.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/deleteTag.htm
    """
    
    data = {"tagId" : tagId,}
    return call_api("/API2/content/deleteTag",
                data=data, 
                response_type=ModifiedItemsResult
           )



def exportContent(itemIds: List[str]) -> None:
    """
    Description:
        Export Content to a PIE file
    
    Input:
        Name: itemIds
        Description: List of content item ID's to export
        
        
    
    Output:
        Successful Result Code: 200
        Description of Response Type: successful operation
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/exportContent.htm
    """
    
    data = {"itemIds" : itemIds,}
    return call_api("/API2/content/exportContent",
                data=data, 
                response_type=None
           )



def findContentItem(searchParams: ContentSearchParamsObject) -> List[PyramidContentItem]:
    """
    Description:
        Search for Content Items
    
    Input:
        Name: searchParams
        Object Type: ContentSearchParamsObject
        Description: The content search object for specifying search criteria to be used in content searches.
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidContentItem[]
        Description of Response Type: Pyramid Content item object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/findContentItem.htm
    """
    data = { "searchParams" : searchParams }
    return call_api("/API2/content/findContentItem",
                data=data, 
                response_type=List[PyramidContentItem]
           )



def findItemsByTagId(tag: str) -> List[ItemId]:
    """
    Description:
        Find Content Items By Tag ID
    
    Input:
        Name: tag
        Type: string
        Description: The tag ID to search
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: A generic object used to contain ID's of items. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/findItemsByTagId.htm
    """
    
    data = {"tag" : tag,}
    return call_api("/API2/content/findItemsByTagId",
                data=data, 
                response_type=List[ItemId]
           )



def findItemsByTagName(tag: str) -> List[ItemId]:
    """
    Description:
        Find Content Items By Tag Caption
    
    Input:
        Name: tag
        Type: string
        Description: The tag caption to search
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: A generic object used to contain ID's of items. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/findItemsByTagName.htm
    """
    
    data = {"tag" : tag,}
    return call_api("/API2/content/findItemsByTagName",
                data=data, 
                response_type=List[ItemId]
           )



def getAllItemTags(itemId: str) -> List[ItemId]:
    """
    Description:
        Gets all Item Tags
    
    Input:
        Name: itemId
        Type: string
        Description: The system item ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: A generic object used to contain ID's of items. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getAllItemTags.htm
    """
    
    data = {"itemId" : itemId,}
    return call_api("/API2/content/getAllItemTags",
                data=data, 
                response_type=List[ItemId]
           )



def getAllItemsCreatedByUser(userId: str) -> List[PyramidContentItem]:
    """
    Description:
        Get Items created by User
    
    Input:
        Name: userId
        Type: string
        Description: The system user ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidContentItem[]
        Description of Response Type: Pyramid Content item object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getAllItemsCreatedByUser.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getAllItemsCreatedByUser",
                data=data, 
                response_type=List[PyramidContentItem]
           )



def getAllTags() -> List[ItemId]:
    """
    Description:
        Gets all Tags
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: A generic object used to contain ID's of items. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getAllTags.htm
    """
    
    return call_api("/API2/content/getAllTags",
                data=None, 
                response_type=List[ItemId]
           )



def getAllUserContentItems(userId: str) -> List[PyramidContentItem]:
    """
    Description:
        Get a User's Content Items
    
    Input:
        Name: userId
        Type: string
        Description: The system user ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidContentItem[]
        Description of Response Type: Pyramid Content item object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getAllUserContentItems.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getAllUserContentItems",
                data=data, 
                response_type=List[PyramidContentItem]
           )



def getAutoRecommendedItems(userId: str) -> List[PyramidContentItem]:
    """
    Description:
        Get the Auto-Recommended item listing
    
    Input:
        Name: userId
        Type: string
        Description: The user's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidContentItem[]
        Description of Response Type: Pyramid Content item object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getAutoRecommendedItems.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getAutoRecommendedItems",
                data=data, 
                response_type=List[PyramidContentItem]
           )



def getContentItemMetaData(itemId: str) -> PyramidContentItem:
    """
    Description:
        Get a content item's metadata
    
    Input:
        Name: itemId
        Type: string
        Description: The system content item ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: PyramidContentItem
        Description of Response Type: Pyramid Content item object.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getContentItemMetaData.htm
    """
    
    data = {"itemId" : itemId,}
    return call_api("/API2/content/getContentItemMetaData",
                data=data, 
                response_type=PyramidContentItem
           )



def getContentItemSecurityRoles(contentItemId: str) -> List[RoleData]:
    """
    Description:
        Get Content Item's Roles
    
    Input:
        Name: contentItemId
        Type: string
        Description: The system content item ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: RoleData[]
        Description of Response Type: successful operation Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getContentItemSecurityRoles.htm
    """
    
    data = {"contentItemId" : contentItemId,}
    return call_api("/API2/content/getContentItemSecurityRoles",
                data=data, 
                response_type=List[RoleData]
           )



def getContentItemSecurityRolesID(contentItemId: str) -> List[ItemId]:
    """
    Description:
        Get Content Item's Roles
    
    Input:
        Name: contentItemId
        Type: string
        Description: The system content item ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: ItemId[]
        Description of Response Type: A generic object used to contain ID's of items. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getContentItemSecurityRolesID.htm
    """
    
    data = {"contentItemId" : contentItemId,}
    return call_api("/API2/content/getContentItemSecurityRolesID",
                data=data, 
                response_type=List[ItemId]
           )



def getFavoriteItems(userId: str) -> List[PyramidContentItem]:
    """
    Description:
        Get Favorite Items List for a user
    
    Input:
        Name: userId
        Type: string
        Description: The system user ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidContentItem[]
        Description of Response Type: Pyramid Content item object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getFavoriteItems.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getFavoriteItems",
                data=data, 
                response_type=List[PyramidContentItem]
           )



def getFolderChildrenOnlyFolders(folder: CmsTreeNodeMetadata) -> List[CmsTreeNodeMetadata]:
    """
    Description:
        Get Folder Items
    
    Input:
        Name: folder
        Object Type: CmsTreeNodeMetadata
        Description: The system folder
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: CmsTreeNodeMetadata[]
        Description of Response Type: successful operation Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getFolderChildrenOnlyFolders.htm
    """
    data = { "folder" : folder }
    return call_api("/API2/content/getFolderChildrenOnlyFolders",
                data=data, 
                response_type=List[CmsTreeNodeMetadata]
           )



def getFolderItems(folderId: str) -> List[PyramidContentItem]:
    """
    Description:
        Get Folder Items
    
    Input:
        Name: folderId
        Type: string
        Description: The system folder ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidContentItem[]
        Description of Response Type: Pyramid Content item object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getFolderItems.htm
    """
    
    data = {"folderId" : folderId,}
    return call_api("/API2/content/getFolderItems",
                data=data, 
                response_type=List[PyramidContentItem]
           )



def getMostUsedItems(userId: str) -> List[PyramidContentItem]:
    """
    Description:
        Get the Most Used item listing
    
    Input:
        Name: userId
        Type: string
        Description: The user's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidContentItem[]
        Description of Response Type: Pyramid Content item object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getMostUsedItems.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getMostUsedItems",
                data=data, 
                response_type=List[PyramidContentItem]
           )



def getPrivateFolderForUser(userId: str) -> PyramidContentItem:
    """
    Description:
        Get a User's Private Folder
    
    Input:
        Name: userId
        Type: string
        Description: The user folder ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: PyramidContentItem
        Description of Response Type: Pyramid Content item object.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getPrivateFolderForUser.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getPrivateFolderForUser",
                data=data, 
                response_type=PyramidContentItem
           )



def getPrivateRootFolder(userId: str) -> PyramidContentItem:
    """
    Description:
        Get user's Private folder
    
    Input:
        Name: userId
        Type: string
        Description: The user's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: PyramidContentItem
        Description of Response Type: Pyramid Content item object.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getPrivateRootFolder.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getPrivateRootFolder",
                data=data, 
                response_type=PyramidContentItem
           )



def getPublicOrGroupFolderByTenantId(folderTenantObject: FolderTenantObject) -> PyramidContentItem:
    """
    Description:
        Get a Tenant's Public Folders
    
    Input:
        Name: folderTenantObject
        Object Type: FolderTenantObject
        Description: The folder for a tenant object.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: PyramidContentItem
        Description of Response Type: Pyramid Content item object.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getPublicOrGroupFolderByTenantId.htm
    """
    data = { "folderTenantObject" : folderTenantObject }
    return call_api("/API2/content/getPublicOrGroupFolderByTenantId",
                data=data, 
                response_type=PyramidContentItem
           )



def getRecentItems(userId: str) -> List[PyramidContentItem]:
    """
    Description:
        Get Recent Items List
    
    Input:
        Name: userId
        Type: string
        Description: The system user ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidContentItem[]
        Description of Response Type: Pyramid Content item object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getRecentItems.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getRecentItems",
                data=data, 
                response_type=List[PyramidContentItem]
           )



def getRecommendedItems(userId: str) -> List[PyramidContentItem]:
    """
    Description:
        Get the Recommended item listing
    
    Input:
        Name: userId
        Type: string
        Description: The user's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidContentItem[]
        Description of Response Type: Pyramid Content item object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getRecommendedItems.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getRecommendedItems",
                data=data, 
                response_type=List[PyramidContentItem]
           )



def getTag(tagId: str) -> TagData:
    """
    Description:
        Gets tag data
    
    Input:
        Name: tagId
        Type: string
        Description: The system tag ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: TagData
        Description of Response Type: The tag object used to capture a tag's settings.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getTag.htm
    """
    
    data = {"tagId" : tagId,}
    return call_api("/API2/content/getTag",
                data=data, 
                response_type=TagData
           )



def getUserGroupFolders(userId: str) -> List[PyramidContentItem]:
    """
    Description:
        Get a user's first-tier group folders
    
    Input:
        Name: userId
        Type: string
        Description: The user's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidContentItem[]
        Description of Response Type: Pyramid Content item object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getUserGroupFolders.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getUserGroupFolders",
                data=data, 
                response_type=List[PyramidContentItem]
           )



def getUserGroupRootFolder(userId: str) -> PyramidContentItem:
    """
    Description:
        Get user's Group folder
    
    Input:
        Name: userId
        Type: string
        Description: The user's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: PyramidContentItem
        Description of Response Type: Pyramid Content item object.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getUserGroupRootFolder.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getUserGroupRootFolder",
                data=data, 
                response_type=PyramidContentItem
           )



def getUserPrivateFolder(userId: str) -> List[PyramidContentItem]:
    """
    Description:
        Get a user's first-tier private folders
    
    Input:
        Name: userId
        Type: string
        Description: The user's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidContentItem[]
        Description of Response Type: Pyramid Content item object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getUserPrivateFolder.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getUserPrivateFolder",
                data=data, 
                response_type=List[PyramidContentItem]
           )



def getUserPrivateRootFolder(userId: str) -> PyramidContentItem:
    """
    Description:
        Get user's Group folder
    
    Input:
        Name: userId
        Type: string
        Description: The user's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: PyramidContentItem
        Description of Response Type: Pyramid Content item object.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getUserPrivateRootFolder.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getUserPrivateRootFolder",
                data=data, 
                response_type=PyramidContentItem
           )



def getUserPublicFolders(userId: str) -> List[PyramidContentItem]:
    """
    Description:
        Get a user's first-tier public folders
    
    Input:
        Name: userId
        Type: string
        Description: The user's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response List Type: PyramidContentItem[]
        Description of Response Type: Pyramid Content item object. Note that the response is returned as a list of items of this object type.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getUserPublicFolders.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getUserPublicFolders",
                data=data, 
                response_type=List[PyramidContentItem]
           )



def getUserPublicRootFolder(userId: str) -> PyramidContentItem:
    """
    Description:
        Get user's Public folder
    
    Input:
        Name: userId
        Type: string
        Description: The user's system ID
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: PyramidContentItem
        Description of Response Type: Pyramid Content item object.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/getUserPublicRootFolder.htm
    """
    
    data = {"userId" : userId,}
    return call_api("/API2/content/getUserPublicRootFolder",
                data=data, 
                response_type=PyramidContentItem
           )



def importContent(pieApiObject: PieApiObject) -> ImportApiResultObject:
    """
    Description:
        Import Content from a PIE file
    
    Input:
        Name: pieApiObject
        Object Type: PieApiObject
        Description: The object representing the details for where to import a PIE file of content.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ImportApiResultObject
        Description of Response Type: The import content items result object from importing content into the system.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/importContent.htm
    """
    data = { "pieApiObject" : pieApiObject }
    return call_api("/API2/content/importContent",
                data=data, 
                response_type=ImportApiResultObject
           )



def moveItems(moveItemsObject: MoveItemsObject) -> ModifiedItemsResult:
    """
    Description:
        Move Items
    
    Input:
        Name: moveItemsObject
        Object Type: MoveItemsObject
        Description: The move/copy items object with details of the selected content items and the destination folder.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/moveItems.htm
    """
    data = { "moveItemsObject" : moveItemsObject }
    return call_api("/API2/content/moveItems",
                data=data, 
                response_type=ModifiedItemsResult
           )



def purgeContentItems(itemIds: List[str]) -> ModifiedItemsResult:
    """
    Description:
        Purge Content Items
    
    Input:
        Name: itemIds
        Description: A list of system content item IDs
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/purgeContentItems.htm
    """
    
    data = {"itemIds" : itemIds,}
    return call_api("/API2/content/purgeContentItems",
                data=data, 
                response_type=ModifiedItemsResult
           )



def removeContentItemsFromFavorites(data: ItemsForFavorites) -> ModifiedItemsResult:
    """
    Description:
        Remove content items from user favorites
    
    Input:
        Name: data
        Object Type: ItemsForFavorites
        Description: The listing of favorite content items for a user.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/removeContentItemsFromFavorites.htm
    """
    data = { "data" : data }
    return call_api("/API2/content/removeContentItemsFromFavorites",
                data=data, 
                response_type=ModifiedItemsResult
           )



def removeRolesFromItem(rolesInItemRemovalObject: RolesInItemRemovalObject) -> ModifiedItemsResult:
    """
    Description:
        Remove roles from a content Item
    
    Input:
        Name: rolesInItemRemovalObject
        Object Type: RolesInItemRemovalObject
        Description: The role object with settings to be set for the chosen content item.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/removeRolesFromItem.htm
    """
    data = { "rolesInItemRemovalObject" : rolesInItemRemovalObject }
    return call_api("/API2/content/removeRolesFromItem",
                data=data, 
                response_type=ModifiedItemsResult
           )



def removeTagFromItem(tagUsageApiData: TagUsageApiData) -> ModifiedItemsResult:
    """
    Description:
        Remove a content item's tag
    
    Input:
        Name: tagUsageApiData
        Object Type: TagUsageApiData
        Description: The tag usage object used to set a tag for a given content item.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/removeTagFromItem.htm
    """
    data = { "tagUsageApiData" : tagUsageApiData }
    return call_api("/API2/content/removeTagFromItem",
                data=data, 
                response_type=ModifiedItemsResult
           )



def renameItem(renameItemApiData: RenameItemApiData) -> ModifiedItemsResult:
    """
    Description:
        Rename a Content Item
    
    Input:
        Name: renameItemApiData
        Object Type: RenameItemApiData
        Description: The rename object for settings to rename content items.
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/renameItem.htm
    """
    data = { "renameItemApiData" : renameItemApiData }
    return call_api("/API2/content/renameItem",
                data=data, 
                response_type=ModifiedItemsResult
           )



def restoreSoftDeletedContentItems(itemIds: List[str]) -> ModifiedItemsResult:
    """
    Description:
        Restore Deleted Content Items
    
    Input:
        Name: itemIds
        Description: A list of system content item IDs
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/restoreSoftDeletedContentItems.htm
    """
    
    data = {"itemIds" : itemIds,}
    return call_api("/API2/content/restoreSoftDeletedContentItems",
                data=data, 
                response_type=ModifiedItemsResult
           )



def softDeleteContentItems(itemIds: List[str]) -> ModifiedItemsResult:
    """
    Description:
        Delete Content Items
    
    Input:
        Name: itemIds
        Description: A list of system content item IDs
        
        
    
    Output:
        Successful Result Code: 200
        Response Type: ModifiedItemsResult
        Description of Response Type: Generic API response object with success or failure flag and related messages.
        

    generated from https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/API2/content/softDeleteContentItems.htm
    """
    
    data = {"itemIds" : itemIds,}
    return call_api("/API2/content/softDeleteContentItems",
                data=data, 
                response_type=ModifiedItemsResult
           )


