from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import microsoft_edge_channel, mobile_app

from . import mobile_app

@dataclass
class MacOSMicrosoftEdgeApp(mobile_app.MobileApp):
    odata_type = "#microsoft.graph.macOSMicrosoftEdgeApp"
    # The enum to specify the channels for Microsoft Edge apps.
    channel: Optional[microsoft_edge_channel.MicrosoftEdgeChannel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSMicrosoftEdgeApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSMicrosoftEdgeApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MacOSMicrosoftEdgeApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import microsoft_edge_channel, mobile_app

        from . import microsoft_edge_channel, mobile_app

        fields: Dict[str, Callable[[Any], None]] = {
            "channel": lambda n : setattr(self, 'channel', n.get_enum_value(microsoft_edge_channel.MicrosoftEdgeChannel)),
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
        writer.write_enum_value("channel", self.channel)
    

