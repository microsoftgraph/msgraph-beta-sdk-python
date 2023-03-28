from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import date_time_time_zone, event_message, location

from . import event_message

class EventMessageRequest(event_message.EventMessage):
    def __init__(self,) -> None:
        """
        Instantiates a new EventMessageRequest and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.eventMessageRequest"
        # True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.
        self._allow_new_time_proposals: Optional[bool] = None
        # If the meeting update changes the meeting end time, this property specifies the previous meeting end time.
        self._previous_end_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # If the meeting update changes the meeting location, this property specifies the previous meeting location.
        self._previous_location: Optional[location.Location] = None
        # If the meeting update changes the meeting start time, this property specifies the previous meeting start time.
        self._previous_start_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # Set to true if the sender would like the invitee to send a response to the requested meeting.
        self._response_requested: Optional[bool] = None
    
    @property
    def allow_new_time_proposals(self,) -> Optional[bool]:
        """
        Gets the allowNewTimeProposals property value. True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.
        Returns: Optional[bool]
        """
        return self._allow_new_time_proposals
    
    @allow_new_time_proposals.setter
    def allow_new_time_proposals(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowNewTimeProposals property value. True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.
        Args:
            value: Value to set for the allow_new_time_proposals property.
        """
        self._allow_new_time_proposals = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EventMessageRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EventMessageRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EventMessageRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import date_time_time_zone, event_message, location

        fields: Dict[str, Callable[[Any], None]] = {
            "allowNewTimeProposals": lambda n : setattr(self, 'allow_new_time_proposals', n.get_bool_value()),
            "previousEndDateTime": lambda n : setattr(self, 'previous_end_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "previousLocation": lambda n : setattr(self, 'previous_location', n.get_object_value(location.Location)),
            "previousStartDateTime": lambda n : setattr(self, 'previous_start_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "responseRequested": lambda n : setattr(self, 'response_requested', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def previous_end_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the previousEndDateTime property value. If the meeting update changes the meeting end time, this property specifies the previous meeting end time.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._previous_end_date_time
    
    @previous_end_date_time.setter
    def previous_end_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the previousEndDateTime property value. If the meeting update changes the meeting end time, this property specifies the previous meeting end time.
        Args:
            value: Value to set for the previous_end_date_time property.
        """
        self._previous_end_date_time = value
    
    @property
    def previous_location(self,) -> Optional[location.Location]:
        """
        Gets the previousLocation property value. If the meeting update changes the meeting location, this property specifies the previous meeting location.
        Returns: Optional[location.Location]
        """
        return self._previous_location
    
    @previous_location.setter
    def previous_location(self,value: Optional[location.Location] = None) -> None:
        """
        Sets the previousLocation property value. If the meeting update changes the meeting location, this property specifies the previous meeting location.
        Args:
            value: Value to set for the previous_location property.
        """
        self._previous_location = value
    
    @property
    def previous_start_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the previousStartDateTime property value. If the meeting update changes the meeting start time, this property specifies the previous meeting start time.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._previous_start_date_time
    
    @previous_start_date_time.setter
    def previous_start_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the previousStartDateTime property value. If the meeting update changes the meeting start time, this property specifies the previous meeting start time.
        Args:
            value: Value to set for the previous_start_date_time property.
        """
        self._previous_start_date_time = value
    
    @property
    def response_requested(self,) -> Optional[bool]:
        """
        Gets the responseRequested property value. Set to true if the sender would like the invitee to send a response to the requested meeting.
        Returns: Optional[bool]
        """
        return self._response_requested
    
    @response_requested.setter
    def response_requested(self,value: Optional[bool] = None) -> None:
        """
        Sets the responseRequested property value. Set to true if the sender would like the invitee to send a response to the requested meeting.
        Args:
            value: Value to set for the response_requested property.
        """
        self._response_requested = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowNewTimeProposals", self.allow_new_time_proposals)
        writer.write_object_value("previousEndDateTime", self.previous_end_date_time)
        writer.write_object_value("previousLocation", self.previous_location)
        writer.write_object_value("previousStartDateTime", self.previous_start_date_time)
        writer.write_bool_value("responseRequested", self.response_requested)
    

