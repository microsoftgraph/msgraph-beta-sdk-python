from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_facet = lazy_import('msgraph.generated.models.item_facet')

class PersonWebsite(item_facet.ItemFacet):
    @property
    def categories(self,) -> Optional[List[str]]:
        """
        Gets the categories property value. Contains categories a user has associated with the website (for example, personal, recipes).
        Returns: Optional[List[str]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the categories property value. Contains categories a user has associated with the website (for example, personal, recipes).
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new PersonWebsite and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.personWebsite"
        # Contains categories a user has associated with the website (for example, personal, recipes).
        self._categories: Optional[List[str]] = None
        # Contains a description of the website.
        self._description: Optional[str] = None
        # Contains a friendly name for the website.
        self._display_name: Optional[str] = None
        # The thumbnailUrl property
        self._thumbnail_url: Optional[str] = None
        # Contains a link to the website itself.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PersonWebsite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PersonWebsite
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PersonWebsite()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Contains a description of the website.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Contains a description of the website.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Contains a friendly name for the website.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Contains a friendly name for the website.
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
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "thumbnail_url": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def thumbnail_url(self,) -> Optional[str]:
        """
        Gets the thumbnailUrl property value. The thumbnailUrl property
        Returns: Optional[str]
        """
        return self._thumbnail_url
    
    @thumbnail_url.setter
    def thumbnail_url(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbnailUrl property value. The thumbnailUrl property
        Args:
            value: Value to set for the thumbnailUrl property.
        """
        self._thumbnail_url = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. Contains a link to the website itself.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. Contains a link to the website itself.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

