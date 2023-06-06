from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import change_tracked_entity, time_off_item

from . import change_tracked_entity

@dataclass
class TimeOff(change_tracked_entity.ChangeTrackedEntity):
    odata_type = "#microsoft.graph.timeOff"
    # The draft version of this timeOff that is viewable by managers. Required.
    draft_time_off: Optional[time_off_item.TimeOffItem] = None
    # The isStagedForDeletion property
    is_staged_for_deletion: Optional[bool] = None
    # The shared version of this timeOff that is viewable by both employees and managers. Required.
    shared_time_off: Optional[time_off_item.TimeOffItem] = None
    # ID of the user assigned to the timeOff. Required.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeOff:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TimeOff
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TimeOff()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import change_tracked_entity, time_off_item

        fields: Dict[str, Callable[[Any], None]] = {
            "draftTimeOff": lambda n : setattr(self, 'draft_time_off', n.get_object_value(time_off_item.TimeOffItem)),
            "isStagedForDeletion": lambda n : setattr(self, 'is_staged_for_deletion', n.get_bool_value()),
            "sharedTimeOff": lambda n : setattr(self, 'shared_time_off', n.get_object_value(time_off_item.TimeOffItem)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_object_value("draftTimeOff", self.draft_time_off)
        writer.write_bool_value("isStagedForDeletion", self.is_staged_for_deletion)
        writer.write_object_value("sharedTimeOff", self.shared_time_off)
        writer.write_str_value("userId", self.user_id)
    

