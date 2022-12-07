from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ios_web_content_filter_base = lazy_import('msgraph.generated.models.ios_web_content_filter_base')

class IosWebContentFilterAutoFilter(ios_web_content_filter_base.IosWebContentFilterBase):
    @property
    def allowed_urls(self,) -> Optional[List[str]]:
        """
        Gets the allowedUrls property value. Additional URLs allowed for access
        Returns: Optional[List[str]]
        """
        return self._allowed_urls
    
    @allowed_urls.setter
    def allowed_urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedUrls property value. Additional URLs allowed for access
        Args:
            value: Value to set for the allowedUrls property.
        """
        self._allowed_urls = value
    
    @property
    def blocked_urls(self,) -> Optional[List[str]]:
        """
        Gets the blockedUrls property value. Additional URLs blocked for access
        Returns: Optional[List[str]]
        """
        return self._blocked_urls
    
    @blocked_urls.setter
    def blocked_urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the blockedUrls property value. Additional URLs blocked for access
        Args:
            value: Value to set for the blockedUrls property.
        """
        self._blocked_urls = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosWebContentFilterAutoFilter and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosWebContentFilterAutoFilter"
        # Additional URLs allowed for access
        self._allowed_urls: Optional[List[str]] = None
        # Additional URLs blocked for access
        self._blocked_urls: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosWebContentFilterAutoFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosWebContentFilterAutoFilter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosWebContentFilterAutoFilter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_urls": lambda n : setattr(self, 'allowed_urls', n.get_collection_of_primitive_values(str)),
            "blocked_urls": lambda n : setattr(self, 'blocked_urls', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("allowedUrls", self.allowed_urls)
        writer.write_collection_of_primitive_values("blockedUrls", self.blocked_urls)
    

