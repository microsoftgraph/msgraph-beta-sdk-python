from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import email_type, item_facet

from . import item_facet

@dataclass
class ItemEmail(item_facet.ItemFacet):
    odata_type = "#microsoft.graph.itemEmail"
    # The email address itself.
    address: Optional[str] = None
    # The name or label a user has associated with a particular email address.
    display_name: Optional[str] = None
    # The type property
    type: Optional[email_type.EmailType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemEmail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemEmail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemEmail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import email_type, item_facet

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(email_type.EmailType)),
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
        writer.write_str_value("address", self.address)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("type", self.type)
    

