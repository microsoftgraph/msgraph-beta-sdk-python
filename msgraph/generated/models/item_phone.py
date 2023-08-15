from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_facet import ItemFacet
    from .phone_type import PhoneType

from .item_facet import ItemFacet

@dataclass
class ItemPhone(ItemFacet):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.itemPhone"
    # Friendly name the user has assigned this phone number.
    display_name: Optional[str] = None
    # Phone number provided by the user.
    number: Optional[str] = None
    # The type property
    type: Optional[PhoneType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemPhone:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemPhone
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ItemPhone()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .item_facet import ItemFacet
        from .phone_type import PhoneType

        from .item_facet import ItemFacet
        from .phone_type import PhoneType

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PhoneType)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("number", self.number)
        writer.write_enum_value("type", self.type)
    

