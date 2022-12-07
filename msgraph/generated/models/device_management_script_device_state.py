from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
managed_device = lazy_import('msgraph.generated.models.managed_device')
run_state = lazy_import('msgraph.generated.models.run_state')

class DeviceManagementScriptDeviceState(entity.Entity):
    """
    Contains properties for device run state of the device management script.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementScriptDeviceState and sets the default values.
        """
        super().__init__()
        # Error code corresponding to erroneous execution of the device management script.
        self._error_code: Optional[int] = None
        # Error description corresponding to erroneous execution of the device management script.
        self._error_description: Optional[str] = None
        # Latest time the device management script executes.
        self._last_state_update_date_time: Optional[datetime] = None
        # The managed devices that executes the device management script.
        self._managed_device: Optional[managed_device.ManagedDevice] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Details of execution output.
        self._result_message: Optional[str] = None
        # Indicates the type of execution status of the device management script.
        self._run_state: Optional[run_state.RunState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementScriptDeviceState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementScriptDeviceState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementScriptDeviceState()
    
    @property
    def error_code(self,) -> Optional[int]:
        """
        Gets the errorCode property value. Error code corresponding to erroneous execution of the device management script.
        Returns: Optional[int]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCode property value. Error code corresponding to erroneous execution of the device management script.
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    @property
    def error_description(self,) -> Optional[str]:
        """
        Gets the errorDescription property value. Error description corresponding to erroneous execution of the device management script.
        Returns: Optional[str]
        """
        return self._error_description
    
    @error_description.setter
    def error_description(self,value: Optional[str] = None) -> None:
        """
        Sets the errorDescription property value. Error description corresponding to erroneous execution of the device management script.
        Args:
            value: Value to set for the errorDescription property.
        """
        self._error_description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "error_code": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "error_description": lambda n : setattr(self, 'error_description', n.get_str_value()),
            "last_state_update_date_time": lambda n : setattr(self, 'last_state_update_date_time', n.get_datetime_value()),
            "managed_device": lambda n : setattr(self, 'managed_device', n.get_object_value(managed_device.ManagedDevice)),
            "result_message": lambda n : setattr(self, 'result_message', n.get_str_value()),
            "run_state": lambda n : setattr(self, 'run_state', n.get_enum_value(run_state.RunState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_state_update_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastStateUpdateDateTime property value. Latest time the device management script executes.
        Returns: Optional[datetime]
        """
        return self._last_state_update_date_time
    
    @last_state_update_date_time.setter
    def last_state_update_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastStateUpdateDateTime property value. Latest time the device management script executes.
        Args:
            value: Value to set for the lastStateUpdateDateTime property.
        """
        self._last_state_update_date_time = value
    
    @property
    def managed_device(self,) -> Optional[managed_device.ManagedDevice]:
        """
        Gets the managedDevice property value. The managed devices that executes the device management script.
        Returns: Optional[managed_device.ManagedDevice]
        """
        return self._managed_device
    
    @managed_device.setter
    def managed_device(self,value: Optional[managed_device.ManagedDevice] = None) -> None:
        """
        Sets the managedDevice property value. The managed devices that executes the device management script.
        Args:
            value: Value to set for the managedDevice property.
        """
        self._managed_device = value
    
    @property
    def result_message(self,) -> Optional[str]:
        """
        Gets the resultMessage property value. Details of execution output.
        Returns: Optional[str]
        """
        return self._result_message
    
    @result_message.setter
    def result_message(self,value: Optional[str] = None) -> None:
        """
        Sets the resultMessage property value. Details of execution output.
        Args:
            value: Value to set for the resultMessage property.
        """
        self._result_message = value
    
    @property
    def run_state(self,) -> Optional[run_state.RunState]:
        """
        Gets the runState property value. Indicates the type of execution status of the device management script.
        Returns: Optional[run_state.RunState]
        """
        return self._run_state
    
    @run_state.setter
    def run_state(self,value: Optional[run_state.RunState] = None) -> None:
        """
        Sets the runState property value. Indicates the type of execution status of the device management script.
        Args:
            value: Value to set for the runState property.
        """
        self._run_state = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_str_value("errorDescription", self.error_description)
        writer.write_datetime_value("lastStateUpdateDateTime", self.last_state_update_date_time)
        writer.write_object_value("managedDevice", self.managed_device)
        writer.write_str_value("resultMessage", self.result_message)
        writer.write_enum_value("runState", self.run_state)
    

