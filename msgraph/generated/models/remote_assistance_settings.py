from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
remote_assistance_state = lazy_import('msgraph.generated.models.remote_assistance_state')

class RemoteAssistanceSettings(entity.Entity):
    @property
    def allow_sessions_to_unenrolled_devices(self,) -> Optional[bool]:
        """
        Gets the allowSessionsToUnenrolledDevices property value. Indicates if sessions to unenrolled devices are allowed for the account. This setting is configurable by the admin. Default value is false.
        Returns: Optional[bool]
        """
        return self._allow_sessions_to_unenrolled_devices
    
    @allow_sessions_to_unenrolled_devices.setter
    def allow_sessions_to_unenrolled_devices(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowSessionsToUnenrolledDevices property value. Indicates if sessions to unenrolled devices are allowed for the account. This setting is configurable by the admin. Default value is false.
        Args:
            value: Value to set for the allowSessionsToUnenrolledDevices property.
        """
        self._allow_sessions_to_unenrolled_devices = value
    
    @property
    def block_chat(self,) -> Optional[bool]:
        """
        Gets the blockChat property value. Indicates if sessions to block chat function. This setting is configurable by the admin. Default value is false.
        Returns: Optional[bool]
        """
        return self._block_chat
    
    @block_chat.setter
    def block_chat(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockChat property value. Indicates if sessions to block chat function. This setting is configurable by the admin. Default value is false.
        Args:
            value: Value to set for the blockChat property.
        """
        self._block_chat = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new remoteAssistanceSettings and sets the default values.
        """
        super().__init__()
        # Indicates if sessions to unenrolled devices are allowed for the account. This setting is configurable by the admin. Default value is false.
        self._allow_sessions_to_unenrolled_devices: Optional[bool] = None
        # Indicates if sessions to block chat function. This setting is configurable by the admin. Default value is false.
        self._block_chat: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # State of remote assistance for the account
        self._remote_assistance_state: Optional[remote_assistance_state.RemoteAssistanceState] = None
    
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
        fields = {
            "allow_sessions_to_unenrolled_devices": lambda n : setattr(self, 'allow_sessions_to_unenrolled_devices', n.get_bool_value()),
            "block_chat": lambda n : setattr(self, 'block_chat', n.get_bool_value()),
            "remote_assistance_state": lambda n : setattr(self, 'remote_assistance_state', n.get_enum_value(remote_assistance_state.RemoteAssistanceState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def remote_assistance_state(self,) -> Optional[remote_assistance_state.RemoteAssistanceState]:
        """
        Gets the remoteAssistanceState property value. State of remote assistance for the account
        Returns: Optional[remote_assistance_state.RemoteAssistanceState]
        """
        return self._remote_assistance_state
    
    @remote_assistance_state.setter
    def remote_assistance_state(self,value: Optional[remote_assistance_state.RemoteAssistanceState] = None) -> None:
        """
        Sets the remoteAssistanceState property value. State of remote assistance for the account
        Args:
            value: Value to set for the remoteAssistanceState property.
        """
        self._remote_assistance_state = value
    
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
    

