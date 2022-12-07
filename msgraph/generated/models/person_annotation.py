from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_body = lazy_import('msgraph.generated.models.item_body')
item_facet = lazy_import('msgraph.generated.models.item_facet')

class PersonAnnotation(item_facet.ItemFacet):
    def __init__(self,) -> None:
        """
        Instantiates a new PersonAnnotation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.personAnnotation"
        # Contains the detail of the note itself.
        self._detail: Optional[item_body.ItemBody] = None
        # Contains a friendly name for the note.
        self._display_name: Optional[str] = None
        # The thumbnailUrl property
        self._thumbnail_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PersonAnnotation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PersonAnnotation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PersonAnnotation()
    
    @property
    def detail(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the detail property value. Contains the detail of the note itself.
        Returns: Optional[item_body.ItemBody]
        """
        return self._detail
    
    @detail.setter
    def detail(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the detail property value. Contains the detail of the note itself.
        Args:
            value: Value to set for the detail property.
        """
        self._detail = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Contains a friendly name for the note.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Contains a friendly name for the note.
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
            "detail": lambda n : setattr(self, 'detail', n.get_object_value(item_body.ItemBody)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "thumbnail_url": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
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
        writer.write_object_value("detail", self.detail)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
    
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
    

