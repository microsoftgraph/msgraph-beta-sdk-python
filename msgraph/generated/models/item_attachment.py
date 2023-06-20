from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attachment, outlook_item

from . import attachment

@dataclass
class ItemAttachment(attachment.Attachment):
    odata_type = "#microsoft.graph.itemAttachment"
    # The attached contact, message or event. Navigation property.
    item: Optional[outlook_item.OutlookItem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemAttachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemAttachment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ItemAttachment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attachment, outlook_item

        from . import attachment, outlook_item

        fields: Dict[str, Callable[[Any], None]] = {
            "item": lambda n : setattr(self, 'item', n.get_object_value(outlook_item.OutlookItem)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("item", self.item)
    

