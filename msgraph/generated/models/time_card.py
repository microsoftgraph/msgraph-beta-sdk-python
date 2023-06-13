from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import change_tracked_entity, confirmed_by, item_body, time_card_break, time_card_entry, time_card_event, time_card_state

from . import change_tracked_entity

@dataclass
class TimeCard(change_tracked_entity.ChangeTrackedEntity):
    odata_type = "#microsoft.graph.timeCard"
    # The list of breaks associated with the timeCard.
    breaks: Optional[List[time_card_break.TimeCardBreak]] = None
    # The clock-in event of the timeCard.
    clock_in_event: Optional[time_card_event.TimeCardEvent] = None
    # The clock-out event of the timeCard.
    clock_out_event: Optional[time_card_event.TimeCardEvent] = None
    # Indicates whether this timeCard entry is confirmed. Possible values are none, user, manager, unknownFutureValue.
    confirmed_by: Optional[confirmed_by.ConfirmedBy] = None
    # Notes about the timeCard.
    notes: Optional[item_body.ItemBody] = None
    # The original timeCardEntry of the timeCard, before user edits.
    original_entry: Optional[time_card_entry.TimeCardEntry] = None
    # The current state of the timeCard during its life cycle.Possible values are: clockedIn, onBreak, clockedOut, unknownFutureValue.
    state: Optional[time_card_state.TimeCardState] = None
    # User ID to which  the timeCard belongs.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeCard:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TimeCard
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TimeCard()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import change_tracked_entity, confirmed_by, item_body, time_card_break, time_card_entry, time_card_event, time_card_state

        fields: Dict[str, Callable[[Any], None]] = {
            "breaks": lambda n : setattr(self, 'breaks', n.get_collection_of_object_values(time_card_break.TimeCardBreak)),
            "clockInEvent": lambda n : setattr(self, 'clock_in_event', n.get_object_value(time_card_event.TimeCardEvent)),
            "clockOutEvent": lambda n : setattr(self, 'clock_out_event', n.get_object_value(time_card_event.TimeCardEvent)),
            "confirmedBy": lambda n : setattr(self, 'confirmed_by', n.get_enum_value(confirmed_by.ConfirmedBy)),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(item_body.ItemBody)),
            "originalEntry": lambda n : setattr(self, 'original_entry', n.get_object_value(time_card_entry.TimeCardEntry)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(time_card_state.TimeCardState)),
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
        writer.write_collection_of_object_values("breaks", self.breaks)
        writer.write_object_value("clockInEvent", self.clock_in_event)
        writer.write_object_value("clockOutEvent", self.clock_out_event)
        writer.write_enum_value("confirmedBy", self.confirmed_by)
        writer.write_object_value("notes", self.notes)
        writer.write_object_value("originalEntry", self.original_entry)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userId", self.user_id)
    

