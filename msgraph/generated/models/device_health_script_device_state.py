from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
managed_device = lazy_import('msgraph.generated.models.managed_device')
remediation_state = lazy_import('msgraph.generated.models.remediation_state')
run_state = lazy_import('msgraph.generated.models.run_state')

class DeviceHealthScriptDeviceState(entity.Entity):
    """
    Contains properties for device run state of the device health script.
    """
    @property
    def assignment_filter_ids(self,) -> Optional[List[str]]:
        """
        Gets the assignmentFilterIds property value. A list of the assignment filter ids used for health script applicability evaluation
        Returns: Optional[List[str]]
        """
        return self._assignment_filter_ids
    
    @assignment_filter_ids.setter
    def assignment_filter_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the assignmentFilterIds property value. A list of the assignment filter ids used for health script applicability evaluation
        Args:
            value: Value to set for the assignmentFilterIds property.
        """
        self._assignment_filter_ids = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceHealthScriptDeviceState and sets the default values.
        """
        super().__init__()
        # A list of the assignment filter ids used for health script applicability evaluation
        self._assignment_filter_ids: Optional[List[str]] = None
        # Indicates the type of execution status of the device management script.
        self._detection_state: Optional[run_state.RunState] = None
        # The next timestamp of when the device health script is expected to execute
        self._expected_state_update_date_time: Optional[datetime] = None
        # The last timestamp of when the device health script executed
        self._last_state_update_date_time: Optional[datetime] = None
        # The last time that Intune Managment Extension synced with Intune
        self._last_sync_date_time: Optional[datetime] = None
        # The managed device on which the device health script executed
        self._managed_device: Optional[managed_device.ManagedDevice] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Error from the detection script after remediation
        self._post_remediation_detection_script_error: Optional[str] = None
        # Detection script output after remediation
        self._post_remediation_detection_script_output: Optional[str] = None
        # Error from the detection script before remediation
        self._pre_remediation_detection_script_error: Optional[str] = None
        # Output of the detection script before remediation
        self._pre_remediation_detection_script_output: Optional[str] = None
        # Error output of the remediation script
        self._remediation_script_error: Optional[str] = None
        # Indicates the type of execution status of the device management script.
        self._remediation_state: Optional[remediation_state.RemediationState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptDeviceState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptDeviceState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceHealthScriptDeviceState()
    
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
        Gets the expectedStateUpdateDateTime property value. The next timestamp of when the device health script is expected to execute
        Returns: Optional[datetime]
        """
        return self._expected_state_update_date_time
    
    @expected_state_update_date_time.setter
    def expected_state_update_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expectedStateUpdateDateTime property value. The next timestamp of when the device health script is expected to execute
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
            "assignment_filter_ids": lambda n : setattr(self, 'assignment_filter_ids', n.get_collection_of_primitive_values(str)),
            "detection_state": lambda n : setattr(self, 'detection_state', n.get_enum_value(run_state.RunState)),
            "expected_state_update_date_time": lambda n : setattr(self, 'expected_state_update_date_time', n.get_datetime_value()),
            "last_state_update_date_time": lambda n : setattr(self, 'last_state_update_date_time', n.get_datetime_value()),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "managed_device": lambda n : setattr(self, 'managed_device', n.get_object_value(managed_device.ManagedDevice)),
            "post_remediation_detection_script_error": lambda n : setattr(self, 'post_remediation_detection_script_error', n.get_str_value()),
            "post_remediation_detection_script_output": lambda n : setattr(self, 'post_remediation_detection_script_output', n.get_str_value()),
            "pre_remediation_detection_script_error": lambda n : setattr(self, 'pre_remediation_detection_script_error', n.get_str_value()),
            "pre_remediation_detection_script_output": lambda n : setattr(self, 'pre_remediation_detection_script_output', n.get_str_value()),
            "remediation_script_error": lambda n : setattr(self, 'remediation_script_error', n.get_str_value()),
            "remediation_state": lambda n : setattr(self, 'remediation_state', n.get_enum_value(remediation_state.RemediationState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_state_update_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastStateUpdateDateTime property value. The last timestamp of when the device health script executed
        Returns: Optional[datetime]
        """
        return self._last_state_update_date_time
    
    @last_state_update_date_time.setter
    def last_state_update_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastStateUpdateDateTime property value. The last timestamp of when the device health script executed
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
        Gets the managedDevice property value. The managed device on which the device health script executed
        Returns: Optional[managed_device.ManagedDevice]
        """
        return self._managed_device
    
    @managed_device.setter
    def managed_device(self,value: Optional[managed_device.ManagedDevice] = None) -> None:
        """
        Sets the managedDevice property value. The managed device on which the device health script executed
        Args:
            value: Value to set for the managedDevice property.
        """
        self._managed_device = value
    
    @property
    def post_remediation_detection_script_error(self,) -> Optional[str]:
        """
        Gets the postRemediationDetectionScriptError property value. Error from the detection script after remediation
        Returns: Optional[str]
        """
        return self._post_remediation_detection_script_error
    
    @post_remediation_detection_script_error.setter
    def post_remediation_detection_script_error(self,value: Optional[str] = None) -> None:
        """
        Sets the postRemediationDetectionScriptError property value. Error from the detection script after remediation
        Args:
            value: Value to set for the postRemediationDetectionScriptError property.
        """
        self._post_remediation_detection_script_error = value
    
    @property
    def post_remediation_detection_script_output(self,) -> Optional[str]:
        """
        Gets the postRemediationDetectionScriptOutput property value. Detection script output after remediation
        Returns: Optional[str]
        """
        return self._post_remediation_detection_script_output
    
    @post_remediation_detection_script_output.setter
    def post_remediation_detection_script_output(self,value: Optional[str] = None) -> None:
        """
        Sets the postRemediationDetectionScriptOutput property value. Detection script output after remediation
        Args:
            value: Value to set for the postRemediationDetectionScriptOutput property.
        """
        self._post_remediation_detection_script_output = value
    
    @property
    def pre_remediation_detection_script_error(self,) -> Optional[str]:
        """
        Gets the preRemediationDetectionScriptError property value. Error from the detection script before remediation
        Returns: Optional[str]
        """
        return self._pre_remediation_detection_script_error
    
    @pre_remediation_detection_script_error.setter
    def pre_remediation_detection_script_error(self,value: Optional[str] = None) -> None:
        """
        Sets the preRemediationDetectionScriptError property value. Error from the detection script before remediation
        Args:
            value: Value to set for the preRemediationDetectionScriptError property.
        """
        self._pre_remediation_detection_script_error = value
    
    @property
    def pre_remediation_detection_script_output(self,) -> Optional[str]:
        """
        Gets the preRemediationDetectionScriptOutput property value. Output of the detection script before remediation
        Returns: Optional[str]
        """
        return self._pre_remediation_detection_script_output
    
    @pre_remediation_detection_script_output.setter
    def pre_remediation_detection_script_output(self,value: Optional[str] = None) -> None:
        """
        Sets the preRemediationDetectionScriptOutput property value. Output of the detection script before remediation
        Args:
            value: Value to set for the preRemediationDetectionScriptOutput property.
        """
        self._pre_remediation_detection_script_output = value
    
    @property
    def remediation_script_error(self,) -> Optional[str]:
        """
        Gets the remediationScriptError property value. Error output of the remediation script
        Returns: Optional[str]
        """
        return self._remediation_script_error
    
    @remediation_script_error.setter
    def remediation_script_error(self,value: Optional[str] = None) -> None:
        """
        Sets the remediationScriptError property value. Error output of the remediation script
        Args:
            value: Value to set for the remediationScriptError property.
        """
        self._remediation_script_error = value
    
    @property
    def remediation_state(self,) -> Optional[remediation_state.RemediationState]:
        """
        Gets the remediationState property value. Indicates the type of execution status of the device management script.
        Returns: Optional[remediation_state.RemediationState]
        """
        return self._remediation_state
    
    @remediation_state.setter
    def remediation_state(self,value: Optional[remediation_state.RemediationState] = None) -> None:
        """
        Sets the remediationState property value. Indicates the type of execution status of the device management script.
        Args:
            value: Value to set for the remediationState property.
        """
        self._remediation_state = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("assignmentFilterIds", self.assignment_filter_ids)
        writer.write_enum_value("detectionState", self.detection_state)
        writer.write_datetime_value("expectedStateUpdateDateTime", self.expected_state_update_date_time)
        writer.write_datetime_value("lastStateUpdateDateTime", self.last_state_update_date_time)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_object_value("managedDevice", self.managed_device)
        writer.write_str_value("postRemediationDetectionScriptError", self.post_remediation_detection_script_error)
        writer.write_str_value("postRemediationDetectionScriptOutput", self.post_remediation_detection_script_output)
        writer.write_str_value("preRemediationDetectionScriptError", self.pre_remediation_detection_script_error)
        writer.write_str_value("preRemediationDetectionScriptOutput", self.pre_remediation_detection_script_output)
        writer.write_str_value("remediationScriptError", self.remediation_script_error)
        writer.write_enum_value("remediationState", self.remediation_state)
    

