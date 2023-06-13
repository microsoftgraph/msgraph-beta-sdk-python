from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, remote_assistance_state

from . import entity

@dataclass
class RemoteAssistanceSettings(entity.Entity):
    # Indicates if sessions to unenrolled devices are allowed for the account. This setting is configurable by the admin. Default value is false.
    allow_sessions_to_unenrolled_devices: Optional[bool] = None
    # Indicates if sessions to block chat function. This setting is configurable by the admin. Default value is false.
    block_chat: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # State of remote assistance for the account
    remote_assistance_state: Optional[remote_assistance_state.RemoteAssistanceState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoteAssistanceSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RemoteAssistanceSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RemoteAssistanceSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, remote_assistance_state

        fields: Dict[str, Callable[[Any], None]] = {
            "allowSessionsToUnenrolledDevices": lambda n : setattr(self, 'allow_sessions_to_unenrolled_devices', n.get_bool_value()),
            "blockChat": lambda n : setattr(self, 'block_chat', n.get_bool_value()),
            "remoteAssistanceState": lambda n : setattr(self, 'remote_assistance_state', n.get_enum_value(remote_assistance_state.RemoteAssistanceState)),
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
        writer.write_bool_value("allowSessionsToUnenrolledDevices", self.allow_sessions_to_unenrolled_devices)
        writer.write_bool_value("blockChat", self.block_chat)
        writer.write_enum_value("remoteAssistanceState", self.remote_assistance_state)
    

