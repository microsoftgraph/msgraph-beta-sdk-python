from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .acl import Acl
    from .entity import Entity
    from .external_item_content import ExternalItemContent
    from .properties import Properties

from .entity import Entity

@dataclass
class ExternalItem(Entity):
    # The acl property
    acl: Optional[List[Acl]] = None
    # The content property
    content: Optional[ExternalItemContent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The properties property
    properties: Optional[Properties] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalItem
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ExternalItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .acl import Acl
        from .entity import Entity
        from .external_item_content import ExternalItemContent
        from .properties import Properties

        from .acl import Acl
        from .entity import Entity
        from .external_item_content import ExternalItemContent
        from .properties import Properties

        fields: Dict[str, Callable[[Any], None]] = {
            "acl": lambda n : setattr(self, 'acl', n.get_collection_of_object_values(Acl)),
            "content": lambda n : setattr(self, 'content', n.get_object_value(ExternalItemContent)),
            "properties": lambda n : setattr(self, 'properties', n.get_object_value(Properties)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("acl", self.acl)
        writer.write_object_value("content", self.content)
        writer.write_object_value("properties", self.properties)
    

