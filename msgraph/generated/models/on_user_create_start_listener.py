from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_event_listener, on_user_create_start_handler

from . import authentication_event_listener

@dataclass
class OnUserCreateStartListener(authentication_event_listener.AuthenticationEventListener):
    odata_type = "#microsoft.graph.onUserCreateStartListener"
    # Required. Configuration for what to invoke if the event resolves to this listener. This lets us define potential handler configurations per-event.
    handler: Optional[on_user_create_start_handler.OnUserCreateStartHandler] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnUserCreateStartListener:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnUserCreateStartListener
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnUserCreateStartListener()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_event_listener, on_user_create_start_handler

        from . import authentication_event_listener, on_user_create_start_handler

        fields: Dict[str, Callable[[Any], None]] = {
            "handler": lambda n : setattr(self, 'handler', n.get_object_value(on_user_create_start_handler.OnUserCreateStartHandler)),
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
        writer.write_object_value("handler", self.handler)
    

