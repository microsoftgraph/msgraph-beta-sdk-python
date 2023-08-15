from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent

from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent

@dataclass
class AppleVppTokenTroubleshootingEvent(DeviceManagementTroubleshootingEvent):
    """
    Event representing an Apple Vpp Token Troubleshooting Event.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # Apple Volume Purchase Program Token Identifier.
    token_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleVppTokenTroubleshootingEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppleVppTokenTroubleshootingEvent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AppleVppTokenTroubleshootingEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent

        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent

        fields: Dict[str, Callable[[Any], None]] = {
            "tokenId": lambda n : setattr(self, 'token_id', n.get_str_value()),
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
        writer.write_str_value("tokenId", self.token_id)
    

