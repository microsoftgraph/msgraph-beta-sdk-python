from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_script_device_state = lazy_import('msgraph.generated.models.device_management_script_device_state')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementScriptUserState(entity.Entity):
    """
    Contains properties for user run state of the device management script.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementScriptUserState and sets the default values.
        """
        super().__init__()
        # List of run states for this script across all devices of specific user.
        self._device_run_states: Optional[List[device_management_script_device_state.DeviceManagementScriptDeviceState]] = None
        # Error device count for specific user.
        self._error_device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Success device count for specific user.
        self._success_device_count: Optional[int] = None
        # User principle name of specific user.
        self._user_principal_name: Optional[str] = None
    
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
    
    @property
    def device_run_states(self,) -> Optional[List[device_management_script_device_state.DeviceManagementScriptDeviceState]]:
        """
        Gets the deviceRunStates property value. List of run states for this script across all devices of specific user.
        Returns: Optional[List[device_management_script_device_state.DeviceManagementScriptDeviceState]]
        """
        return self._device_run_states
    
    @device_run_states.setter
    def device_run_states(self,value: Optional[List[device_management_script_device_state.DeviceManagementScriptDeviceState]] = None) -> None:
        """
        Sets the deviceRunStates property value. List of run states for this script across all devices of specific user.
        Args:
            value: Value to set for the deviceRunStates property.
        """
        self._device_run_states = value
    
    @property
    def error_device_count(self,) -> Optional[int]:
        """
        Gets the errorDeviceCount property value. Error device count for specific user.
        Returns: Optional[int]
        """
        return self._error_device_count
    
    @error_device_count.setter
    def error_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorDeviceCount property value. Error device count for specific user.
        Args:
            value: Value to set for the errorDeviceCount property.
        """
        self._error_device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_run_states": lambda n : setattr(self, 'device_run_states', n.get_collection_of_object_values(device_management_script_device_state.DeviceManagementScriptDeviceState)),
            "error_device_count": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "success_device_count": lambda n : setattr(self, 'success_device_count', n.get_int_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
    
    @property
    def success_device_count(self,) -> Optional[int]:
        """
        Gets the successDeviceCount property value. Success device count for specific user.
        Returns: Optional[int]
        """
        return self._success_device_count
    
    @success_device_count.setter
    def success_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the successDeviceCount property value. Success device count for specific user.
        Args:
            value: Value to set for the successDeviceCount property.
        """
        self._success_device_count = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User principle name of specific user.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User principle name of specific user.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

