from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_facet = lazy_import('msgraph.generated.models.item_facet')

class ItemPublication(item_facet.ItemFacet):
    def __init__(self,) -> None:
        """
        Instantiates a new ItemPublication and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.itemPublication"
        # Description of the publication.
        self._description: Optional[str] = None
        # Title of the publication.
        self._display_name: Optional[str] = None
        # The date that the publication was published.
        self._published_date: Optional[Date] = None
        # Publication or publisher for the publication.
        self._publisher: Optional[str] = None
        # URL referencing a thumbnail of the publication.
        self._thumbnail_url: Optional[str] = None
        # URL referencing the publication.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemPublication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemPublication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemPublication()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the publication.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the publication.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Title of the publication.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Title of the publication.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "published_date": lambda n : setattr(self, 'published_date', n.get_object_value(Date)),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "thumbnail_url": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def published_date(self,) -> Optional[Date]:
        """
        Gets the publishedDate property value. The date that the publication was published.
        Returns: Optional[Date]
        """
        return self._published_date
    
    @published_date.setter
    def published_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the publishedDate property value. The date that the publication was published.
        Args:
            value: Value to set for the publishedDate property.
        """
        self._published_date = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. Publication or publisher for the publication.
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. Publication or publisher for the publication.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("publishedDate", self.published_date)
        writer.write_str_value("publisher", self.publisher)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def thumbnail_url(self,) -> Optional[str]:
        """
        Gets the thumbnailUrl property value. URL referencing a thumbnail of the publication.
        Returns: Optional[str]
        """
        return self._thumbnail_url
    
    @thumbnail_url.setter
    def thumbnail_url(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbnailUrl property value. URL referencing a thumbnail of the publication.
        Args:
            value: Value to set for the thumbnailUrl property.
        """
        self._thumbnail_url = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. URL referencing the publication.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. URL referencing the publication.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

