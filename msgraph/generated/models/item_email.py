from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_type import EmailType
    from .item_facet import ItemFacet

from .item_facet import ItemFacet

@dataclass
class ItemEmail(ItemFacet):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.itemEmail"
    # The email address itself.
    address: Optional[str] = None
    # The name or label a user has associated with a particular email address.
    display_name: Optional[str] = None
    # The type property
    type: Optional[EmailType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemEmail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemEmail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ItemEmail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .email_type import EmailType
        from .item_facet import ItemFacet

        from .email_type import EmailType
        from .item_facet import ItemFacet

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(EmailType)),
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
        writer.write_str_value("address", self.address)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("type", self.type)
    

