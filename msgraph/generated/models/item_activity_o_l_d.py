from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import drive_item, entity, identity_set, item_action_set, item_activity_time_set, list_item

from . import entity

@dataclass
class ItemActivityOLD(entity.Entity):
    # The action property
    action: Optional[item_action_set.ItemActionSet] = None
    # The actor property
    actor: Optional[identity_set.IdentitySet] = None
    # The driveItem property
    drive_item: Optional[drive_item.DriveItem] = None
    # The listItem property
    list_item: Optional[list_item.ListItem] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The times property
    times: Optional[item_activity_time_set.ItemActivityTimeSet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemActivityOLD:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemActivityOLD
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ItemActivityOLD()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import drive_item, entity, identity_set, item_action_set, item_activity_time_set, list_item

        from . import drive_item, entity, identity_set, item_action_set, item_activity_time_set, list_item

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_object_value(item_action_set.ItemActionSet)),
            "actor": lambda n : setattr(self, 'actor', n.get_object_value(identity_set.IdentitySet)),
            "driveItem": lambda n : setattr(self, 'drive_item', n.get_object_value(drive_item.DriveItem)),
            "listItem": lambda n : setattr(self, 'list_item', n.get_object_value(list_item.ListItem)),
            "times": lambda n : setattr(self, 'times', n.get_object_value(item_activity_time_set.ItemActivityTimeSet)),
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
        writer.write_object_value("action", self.action)
        writer.write_object_value("actor", self.actor)
        writer.write_object_value("driveItem", self.drive_item)
        writer.write_object_value("listItem", self.list_item)
        writer.write_object_value("times", self.times)
    

