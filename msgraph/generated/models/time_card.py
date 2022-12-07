from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

change_tracked_entity = lazy_import('msgraph.generated.models.change_tracked_entity')
confirmed_by = lazy_import('msgraph.generated.models.confirmed_by')
item_body = lazy_import('msgraph.generated.models.item_body')
time_card_break = lazy_import('msgraph.generated.models.time_card_break')
time_card_entry = lazy_import('msgraph.generated.models.time_card_entry')
time_card_event = lazy_import('msgraph.generated.models.time_card_event')
time_card_state = lazy_import('msgraph.generated.models.time_card_state')

class TimeCard(change_tracked_entity.ChangeTrackedEntity):
    @property
    def breaks(self,) -> Optional[List[time_card_break.TimeCardBreak]]:
        """
        Gets the breaks property value. The list of breaks associated with the timeCard.
        Returns: Optional[List[time_card_break.TimeCardBreak]]
        """
        return self._breaks
    
    @breaks.setter
    def breaks(self,value: Optional[List[time_card_break.TimeCardBreak]] = None) -> None:
        """
        Sets the breaks property value. The list of breaks associated with the timeCard.
        Args:
            value: Value to set for the breaks property.
        """
        self._breaks = value
    
    @property
    def clock_in_event(self,) -> Optional[time_card_event.TimeCardEvent]:
        """
        Gets the clockInEvent property value. The clock-in event of the timeCard.
        Returns: Optional[time_card_event.TimeCardEvent]
        """
        return self._clock_in_event
    
    @clock_in_event.setter
    def clock_in_event(self,value: Optional[time_card_event.TimeCardEvent] = None) -> None:
        """
        Sets the clockInEvent property value. The clock-in event of the timeCard.
        Args:
            value: Value to set for the clockInEvent property.
        """
        self._clock_in_event = value
    
    @property
    def clock_out_event(self,) -> Optional[time_card_event.TimeCardEvent]:
        """
        Gets the clockOutEvent property value. The clock-out event of the timeCard.
        Returns: Optional[time_card_event.TimeCardEvent]
        """
        return self._clock_out_event
    
    @clock_out_event.setter
    def clock_out_event(self,value: Optional[time_card_event.TimeCardEvent] = None) -> None:
        """
        Sets the clockOutEvent property value. The clock-out event of the timeCard.
        Args:
            value: Value to set for the clockOutEvent property.
        """
        self._clock_out_event = value
    
    @property
    def confirmed_by(self,) -> Optional[confirmed_by.ConfirmedBy]:
        """
        Gets the confirmedBy property value. Indicate if this timeCard entry is confirmed. Possible values are none, user, manager, unknownFutureValue.
        Returns: Optional[confirmed_by.ConfirmedBy]
        """
        return self._confirmed_by
    
    @confirmed_by.setter
    def confirmed_by(self,value: Optional[confirmed_by.ConfirmedBy] = None) -> None:
        """
        Sets the confirmedBy property value. Indicate if this timeCard entry is confirmed. Possible values are none, user, manager, unknownFutureValue.
        Args:
            value: Value to set for the confirmedBy property.
        """
        self._confirmed_by = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new TimeCard and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.timeCard"
        # The list of breaks associated with the timeCard.
        self._breaks: Optional[List[time_card_break.TimeCardBreak]] = None
        # The clock-in event of the timeCard.
        self._clock_in_event: Optional[time_card_event.TimeCardEvent] = None
        # The clock-out event of the timeCard.
        self._clock_out_event: Optional[time_card_event.TimeCardEvent] = None
        # Indicate if this timeCard entry is confirmed. Possible values are none, user, manager, unknownFutureValue.
        self._confirmed_by: Optional[confirmed_by.ConfirmedBy] = None
        # Notes about the timeCard.
        self._notes: Optional[item_body.ItemBody] = None
        # The original timeCardEntry of the timeCard, before user edits.
        self._original_entry: Optional[time_card_entry.TimeCardEntry] = None
        # The current state of the timeCard during its life cycle.Possible values are: clockedIn, onBreak, clockedOut, unknownFutureValue.
        self._state: Optional[time_card_state.TimeCardState] = None
        # User ID to which  the timeCard belongs.
        self._user_id: Optional[str] = None
    
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
        fields = {
            "breaks": lambda n : setattr(self, 'breaks', n.get_collection_of_object_values(time_card_break.TimeCardBreak)),
            "clock_in_event": lambda n : setattr(self, 'clock_in_event', n.get_object_value(time_card_event.TimeCardEvent)),
            "clock_out_event": lambda n : setattr(self, 'clock_out_event', n.get_object_value(time_card_event.TimeCardEvent)),
            "confirmed_by": lambda n : setattr(self, 'confirmed_by', n.get_enum_value(confirmed_by.ConfirmedBy)),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(item_body.ItemBody)),
            "original_entry": lambda n : setattr(self, 'original_entry', n.get_object_value(time_card_entry.TimeCardEntry)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(time_card_state.TimeCardState)),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def notes(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the notes property value. Notes about the timeCard.
        Returns: Optional[item_body.ItemBody]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the notes property value. Notes about the timeCard.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def original_entry(self,) -> Optional[time_card_entry.TimeCardEntry]:
        """
        Gets the originalEntry property value. The original timeCardEntry of the timeCard, before user edits.
        Returns: Optional[time_card_entry.TimeCardEntry]
        """
        return self._original_entry
    
    @original_entry.setter
    def original_entry(self,value: Optional[time_card_entry.TimeCardEntry] = None) -> None:
        """
        Sets the originalEntry property value. The original timeCardEntry of the timeCard, before user edits.
        Args:
            value: Value to set for the originalEntry property.
        """
        self._original_entry = value
    
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
    
    @property
    def state(self,) -> Optional[time_card_state.TimeCardState]:
        """
        Gets the state property value. The current state of the timeCard during its life cycle.Possible values are: clockedIn, onBreak, clockedOut, unknownFutureValue.
        Returns: Optional[time_card_state.TimeCardState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[time_card_state.TimeCardState] = None) -> None:
        """
        Sets the state property value. The current state of the timeCard during its life cycle.Possible values are: clockedIn, onBreak, clockedOut, unknownFutureValue.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. User ID to which  the timeCard belongs.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. User ID to which  the timeCard belongs.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

