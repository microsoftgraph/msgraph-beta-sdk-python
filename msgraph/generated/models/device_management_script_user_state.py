from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_script_device_state, entity

from . import entity

@dataclass
class DeviceManagementScriptUserState(entity.Entity):
    """
    Contains properties for user run state of the device management script.
    """
    # List of run states for this script across all devices of specific user.
    device_run_states: Optional[List[device_management_script_device_state.DeviceManagementScriptDeviceState]] = None
    # Error device count for specific user.
    error_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Success device count for specific user.
    success_device_count: Optional[int] = None
    # User principle name of specific user.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementScriptUserState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementScriptUserState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementScriptUserState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_script_device_state, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceRunStates": lambda n : setattr(self, 'device_run_states', n.get_collection_of_object_values(device_management_script_device_state.DeviceManagementScriptDeviceState)),
            "errorDeviceCount": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "successDeviceCount": lambda n : setattr(self, 'success_device_count', n.get_int_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("deviceRunStates", self.device_run_states)
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("successDeviceCount", self.success_device_count)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

