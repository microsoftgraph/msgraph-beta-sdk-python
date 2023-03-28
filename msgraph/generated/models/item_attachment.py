from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attachment, outlook_item

from . import attachment

class ItemAttachment(attachment.Attachment):
    def __init__(self,) -> None:
        """
        Instantiates a new ItemAttachment and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.itemAttachment"
        # The attached contact, message or event. Navigation property.
        self._item: Optional[outlook_item.OutlookItem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemAttachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemAttachment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemAttachment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attachment, outlook_item

        fields: Dict[str, Callable[[Any], None]] = {
            "item": lambda n : setattr(self, 'item', n.get_object_value(outlook_item.OutlookItem)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def item(self,) -> Optional[outlook_item.OutlookItem]:
        """
        Gets the item property value. The attached contact, message or event. Navigation property.
        Returns: Optional[outlook_item.OutlookItem]
        """
        return self._item
    
    @item.setter
    def item(self,value: Optional[outlook_item.OutlookItem] = None) -> None:
        """
        Sets the item property value. The attached contact, message or event. Navigation property.
        Args:
            value: Value to set for the item property.
        """
        self._item = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("item", self.item)
    

