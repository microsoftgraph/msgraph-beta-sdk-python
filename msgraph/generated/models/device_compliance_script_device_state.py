from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
managed_device = lazy_import('msgraph.generated.models.managed_device')
run_state = lazy_import('msgraph.generated.models.run_state')

class DeviceComplianceScriptDeviceState(entity.Entity):
    """
    Contains properties for device run state of the device compliance script.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceComplianceScriptDeviceState and sets the default values.
        """
        super().__init__()
        # Indicates the type of execution status of the device management script.
        self._detection_state: Optional[run_state.RunState] = None
        # The next timestamp of when the device compliance script is expected to execute
        self._expected_state_update_date_time: Optional[datetime] = None
        # The last timestamp of when the device compliance script executed
        self._last_state_update_date_time: Optional[datetime] = None
        # The last time that Intune Managment Extension synced with Intune
        self._last_sync_date_time: Optional[datetime] = None
        # The managed device on which the device compliance script executed
        self._managed_device: Optional[managed_device.ManagedDevice] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Error from the detection script
        self._script_error: Optional[str] = None
        # Output of the detection script
        self._script_output: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComplianceScriptDeviceState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScriptDeviceState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceComplianceScriptDeviceState()
    
    @property
    def detection_state(self,) -> Optional[run_state.RunState]:
        """
        Gets the detectionState property value. Indicates the type of execution status of the device management script.
        Returns: Optional[run_state.RunState]
        """
        return self._detection_state
    
    @detection_state.setter
    def detection_state(self,value: Optional[run_state.RunState] = None) -> None:
        """
        Sets the detectionState property value. Indicates the type of execution status of the device management script.
        Args:
            value: Value to set for the detectionState property.
        """
        self._detection_state = value
    
    @property
    def expected_state_update_date_time(self,) -> Optional[datetime]:
        """
        Gets the expectedStateUpdateDateTime property value. The next timestamp of when the device compliance script is expected to execute
        Returns: Optional[datetime]
        """
        return self._expected_state_update_date_time
    
    @expected_state_update_date_time.setter
    def expected_state_update_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expectedStateUpdateDateTime property value. The next timestamp of when the device compliance script is expected to execute
        Args:
            value: Value to set for the expectedStateUpdateDateTime property.
        """
        self._expected_state_update_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "detection_state": lambda n : setattr(self, 'detection_state', n.get_enum_value(run_state.RunState)),
            "expected_state_update_date_time": lambda n : setattr(self, 'expected_state_update_date_time', n.get_datetime_value()),
            "last_state_update_date_time": lambda n : setattr(self, 'last_state_update_date_time', n.get_datetime_value()),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "managed_device": lambda n : setattr(self, 'managed_device', n.get_object_value(managed_device.ManagedDevice)),
            "script_error": lambda n : setattr(self, 'script_error', n.get_str_value()),
            "script_output": lambda n : setattr(self, 'script_output', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_state_update_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastStateUpdateDateTime property value. The last timestamp of when the device compliance script executed
        Returns: Optional[datetime]
        """
        return self._last_state_update_date_time
    
    @last_state_update_date_time.setter
    def last_state_update_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastStateUpdateDateTime property value. The last timestamp of when the device compliance script executed
        Args:
            value: Value to set for the lastStateUpdateDateTime property.
        """
        self._last_state_update_date_time = value
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. The last time that Intune Managment Extension synced with Intune
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. The last time that Intune Managment Extension synced with Intune
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    @property
    def managed_device(self,) -> Optional[managed_device.ManagedDevice]:
        """
        Gets the managedDevice property value. The managed device on which the device compliance script executed
        Returns: Optional[managed_device.ManagedDevice]
        """
        return self._managed_device
    
    @managed_device.setter
    def managed_device(self,value: Optional[managed_device.ManagedDevice] = None) -> None:
        """
        Sets the managedDevice property value. The managed device on which the device compliance script executed
        Args:
            value: Value to set for the managedDevice property.
        """
        self._managed_device = value
    
    @property
    def script_error(self,) -> Optional[str]:
        """
        Gets the scriptError property value. Error from the detection script
        Returns: Optional[str]
        """
        return self._script_error
    
    @script_error.setter
    def script_error(self,value: Optional[str] = None) -> None:
        """
        Sets the scriptError property value. Error from the detection script
        Args:
            value: Value to set for the scriptError property.
        """
        self._script_error = value
    
    @property
    def script_output(self,) -> Optional[str]:
        """
        Gets the scriptOutput property value. Output of the detection script
        Returns: Optional[str]
        """
        return self._script_output
    
    @script_output.setter
    def script_output(self,value: Optional[str] = None) -> None:
        """
        Sets the scriptOutput property value. Output of the detection script
        Args:
            value: Value to set for the scriptOutput property.
        """
        self._script_output = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("detectionState", self.detection_state)
        writer.write_datetime_value("expectedStateUpdateDateTime", self.expected_state_update_date_time)
        writer.write_datetime_value("lastStateUpdateDateTime", self.last_state_update_date_time)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_object_value("managedDevice", self.managed_device)
        writer.write_str_value("scriptError", self.script_error)
        writer.write_str_value("scriptOutput", self.script_output)
    

