from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_item import BaseItem
    from .recycle_bin_item import RecycleBinItem

from .base_item import BaseItem

@dataclass
class RecycleBin(BaseItem):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.recycleBin"
    # List of the recycleBinItems deleted by a user.
    items: Optional[List[RecycleBinItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecycleBin:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecycleBin
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RecycleBin()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_item import BaseItem
        from .recycle_bin_item import RecycleBinItem

        from .base_item import BaseItem
        from .recycle_bin_item import RecycleBinItem

        fields: Dict[str, Callable[[Any], None]] = {
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(RecycleBinItem)),
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
        writer.write_collection_of_object_values("items", self.items)
    

