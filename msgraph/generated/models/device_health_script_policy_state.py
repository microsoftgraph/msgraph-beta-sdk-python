from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import remediation_state, run_state

class DeviceHealthScriptPolicyState(AdditionalDataHolder, Parsable):
    """
    Contains properties for policy run state of the device health script.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceHealthScriptPolicyState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A list of the assignment filter ids used for health script applicability evaluation
        self._assignment_filter_ids: Optional[List[str]] = None
        # Indicates the type of execution status of the device management script.
        self._detection_state: Optional[run_state.RunState] = None
        # The Intune device Id
        self._device_id: Optional[str] = None
        # Display name of the device
        self._device_name: Optional[str] = None
        # The next timestamp of when the device health script is expected to execute
        self._expected_state_update_date_time: Optional[datetime] = None
        # Key of the device health script policy state is a concatenation of the MT sideCar policy Id and Intune device Id
        self._id: Optional[str] = None
        # The last timestamp of when the device health script executed
        self._last_state_update_date_time: Optional[datetime] = None
        # The last time that Intune Managment Extension synced with Intune
        self._last_sync_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Value of the OS Version in string
        self._os_version: Optional[str] = None
        # The MT sideCar policy Id
        self._policy_id: Optional[str] = None
        # Display name of the device health script
        self._policy_name: Optional[str] = None
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
        # Name of the user whom ran the device health script
        self._user_name: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
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
            value: Value to set for the assignment_filter_ids property.
        """
        self._assignment_filter_ids = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptPolicyState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptPolicyState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceHealthScriptPolicyState()
    
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
            value: Value to set for the detection_state property.
        """
        self._detection_state = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The Intune device Id
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The Intune device Id
        Args:
            value: Value to set for the device_id property.
        """
        self._device_id = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Display name of the device
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Display name of the device
        Args:
            value: Value to set for the device_name property.
        """
        self._device_name = value
    
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
            value: Value to set for the expected_state_update_date_time property.
        """
        self._expected_state_update_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import remediation_state, run_state

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentFilterIds": lambda n : setattr(self, 'assignment_filter_ids', n.get_collection_of_primitive_values(str)),
            "detectionState": lambda n : setattr(self, 'detection_state', n.get_enum_value(run_state.RunState)),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "expectedStateUpdateDateTime": lambda n : setattr(self, 'expected_state_update_date_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastStateUpdateDateTime": lambda n : setattr(self, 'last_state_update_date_time', n.get_datetime_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "postRemediationDetectionScriptError": lambda n : setattr(self, 'post_remediation_detection_script_error', n.get_str_value()),
            "postRemediationDetectionScriptOutput": lambda n : setattr(self, 'post_remediation_detection_script_output', n.get_str_value()),
            "preRemediationDetectionScriptError": lambda n : setattr(self, 'pre_remediation_detection_script_error', n.get_str_value()),
            "preRemediationDetectionScriptOutput": lambda n : setattr(self, 'pre_remediation_detection_script_output', n.get_str_value()),
            "remediationScriptError": lambda n : setattr(self, 'remediation_script_error', n.get_str_value()),
            "remediationState": lambda n : setattr(self, 'remediation_state', n.get_enum_value(remediation_state.RemediationState)),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Key of the device health script policy state is a concatenation of the MT sideCar policy Id and Intune device Id
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Key of the device health script policy state is a concatenation of the MT sideCar policy Id and Intune device Id
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
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
            value: Value to set for the last_state_update_date_time property.
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
            value: Value to set for the last_sync_date_time property.
        """
        self._last_sync_date_time = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. Value of the OS Version in string
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. Value of the OS Version in string
        Args:
            value: Value to set for the os_version property.
        """
        self._os_version = value
    
    @property
    def policy_id(self,) -> Optional[str]:
        """
        Gets the policyId property value. The MT sideCar policy Id
        Returns: Optional[str]
        """
        return self._policy_id
    
    @policy_id.setter
    def policy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the policyId property value. The MT sideCar policy Id
        Args:
            value: Value to set for the policy_id property.
        """
        self._policy_id = value
    
    @property
    def policy_name(self,) -> Optional[str]:
        """
        Gets the policyName property value. Display name of the device health script
        Returns: Optional[str]
        """
        return self._policy_name
    
    @policy_name.setter
    def policy_name(self,value: Optional[str] = None) -> None:
        """
        Sets the policyName property value. Display name of the device health script
        Args:
            value: Value to set for the policy_name property.
        """
        self._policy_name = value
    
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
            value: Value to set for the post_remediation_detection_script_error property.
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
            value: Value to set for the post_remediation_detection_script_output property.
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
            value: Value to set for the pre_remediation_detection_script_error property.
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
            value: Value to set for the pre_remediation_detection_script_output property.
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
            value: Value to set for the remediation_script_error property.
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
            value: Value to set for the remediation_state property.
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
        writer.write_collection_of_primitive_values("assignmentFilterIds", self.assignment_filter_ids)
        writer.write_enum_value("detectionState", self.detection_state)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_datetime_value("expectedStateUpdateDateTime", self.expected_state_update_date_time)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("lastStateUpdateDateTime", self.last_state_update_date_time)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_str_value("postRemediationDetectionScriptError", self.post_remediation_detection_script_error)
        writer.write_str_value("postRemediationDetectionScriptOutput", self.post_remediation_detection_script_output)
        writer.write_str_value("preRemediationDetectionScriptError", self.pre_remediation_detection_script_error)
        writer.write_str_value("preRemediationDetectionScriptOutput", self.pre_remediation_detection_script_output)
        writer.write_str_value("remediationScriptError", self.remediation_script_error)
        writer.write_enum_value("remediationState", self.remediation_state)
        writer.write_str_value("userName", self.user_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. Name of the user whom ran the device health script
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. Name of the user whom ran the device health script
        Args:
            value: Value to set for the user_name property.
        """
        self._user_name = value
    

