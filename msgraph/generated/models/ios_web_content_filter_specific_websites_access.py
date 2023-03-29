from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ios_bookmark, ios_web_content_filter_base

from . import ios_web_content_filter_base

class IosWebContentFilterSpecificWebsitesAccess(ios_web_content_filter_base.IosWebContentFilterBase):
    def __init__(self,) -> None:
        """
        Instantiates a new IosWebContentFilterSpecificWebsitesAccess and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosWebContentFilterSpecificWebsitesAccess"
        # URL bookmarks which will be installed into built-in browser and user is only allowed to access websites through bookmarks. This collection can contain a maximum of 500 elements.
        self._specific_websites_only: Optional[List[ios_bookmark.IosBookmark]] = None
        # URL bookmarks which will be installed into built-in browser and user is only allowed to access websites through bookmarks. This collection can contain a maximum of 500 elements.
        self._website_list: Optional[List[ios_bookmark.IosBookmark]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosWebContentFilterSpecificWebsitesAccess:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosWebContentFilterSpecificWebsitesAccess
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosWebContentFilterSpecificWebsitesAccess()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ios_bookmark, ios_web_content_filter_base

        fields: Dict[str, Callable[[Any], None]] = {
            "specificWebsitesOnly": lambda n : setattr(self, 'specific_websites_only', n.get_collection_of_object_values(ios_bookmark.IosBookmark)),
            "websiteList": lambda n : setattr(self, 'website_list', n.get_collection_of_object_values(ios_bookmark.IosBookmark)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("specificWebsitesOnly", self.specific_websites_only)
        writer.write_collection_of_object_values("websiteList", self.website_list)
    
    @property
    def specific_websites_only(self,) -> Optional[List[ios_bookmark.IosBookmark]]:
        """
        Gets the specificWebsitesOnly property value. URL bookmarks which will be installed into built-in browser and user is only allowed to access websites through bookmarks. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ios_bookmark.IosBookmark]]
        """
        return self._specific_websites_only
    
    @specific_websites_only.setter
    def specific_websites_only(self,value: Optional[List[ios_bookmark.IosBookmark]] = None) -> None:
        """
        Sets the specificWebsitesOnly property value. URL bookmarks which will be installed into built-in browser and user is only allowed to access websites through bookmarks. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the specific_websites_only property.
        """
        self._specific_websites_only = value
    
    @property
    def website_list(self,) -> Optional[List[ios_bookmark.IosBookmark]]:
        """
        Gets the websiteList property value. URL bookmarks which will be installed into built-in browser and user is only allowed to access websites through bookmarks. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ios_bookmark.IosBookmark]]
        """
        return self._website_list
    
    @website_list.setter
    def website_list(self,value: Optional[List[ios_bookmark.IosBookmark]] = None) -> None:
        """
        Sets the websiteList property value. URL bookmarks which will be installed into built-in browser and user is only allowed to access websites through bookmarks. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the website_list property.
        """
        self._website_list = value
    

