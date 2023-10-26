from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .call_direction import CallDirection
    from .call_event_type import CallEventType
    from .entity import Entity

from .entity import Entity

@dataclass
class CallEvent(Entity):
    # The callEventType property
    call_event_type: Optional[CallEventType] = None
    # The direction property
    direction: Optional[CallDirection] = None
    # The joinCallUrl property
    join_call_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallEvent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CallEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .call_direction import CallDirection
        from .call_event_type import CallEventType
        from .entity import Entity

        from .call_direction import CallDirection
        from .call_event_type import CallEventType
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "callEventType": lambda n : setattr(self, 'call_event_type', n.get_enum_value(CallEventType)),
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(CallDirection)),
            "joinCallUrl": lambda n : setattr(self, 'join_call_url', n.get_str_value()),
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
        writer.write_enum_value("callEventType", self.call_event_type)
        writer.write_enum_value("direction", self.direction)
        writer.write_str_value("joinCallUrl", self.join_call_url)
    

