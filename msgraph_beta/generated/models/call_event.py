from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .call_event_type import CallEventType
    from .emergency_call_event import EmergencyCallEvent
    from .entity import Entity
    from .participant import Participant

from .entity import Entity

@dataclass
class CallEvent(Entity):
    # The callEventType property
    call_event_type: Optional[CallEventType] = None
    # The eventDateTime property
    event_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The participants property
    participants: Optional[List[Participant]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CallEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emergencyCallEvent".casefold():
            from .emergency_call_event import EmergencyCallEvent

            return EmergencyCallEvent()
        return CallEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .call_event_type import CallEventType
        from .emergency_call_event import EmergencyCallEvent
        from .entity import Entity
        from .participant import Participant

        from .call_event_type import CallEventType
        from .emergency_call_event import EmergencyCallEvent
        from .entity import Entity
        from .participant import Participant

        fields: Dict[str, Callable[[Any], None]] = {
            "callEventType": lambda n : setattr(self, 'call_event_type', n.get_enum_value(CallEventType)),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(Participant)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("callEventType", self.call_event_type)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_collection_of_object_values("participants", self.participants)
    

