from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_health_script_assignment = lazy_import('msgraph.generated.models.device_health_script_assignment')
device_health_script_device_state = lazy_import('msgraph.generated.models.device_health_script_device_state')
device_health_script_parameter = lazy_import('msgraph.generated.models.device_health_script_parameter')
device_health_script_run_summary = lazy_import('msgraph.generated.models.device_health_script_run_summary')
entity = lazy_import('msgraph.generated.models.entity')
run_as_account_type = lazy_import('msgraph.generated.models.run_as_account_type')

class DeviceHealthScript(entity.Entity):
    """
    Intune will provide customer the ability to run their Powershell Health scripts (remediation + detection) on the enrolled windows 10 Azure Active Directory joined devices.
    """
    @property
    def assignments(self,) -> Optional[List[device_health_script_assignment.DeviceHealthScriptAssignment]]:
        """
        Gets the assignments property value. The list of group assignments for the device health script
        Returns: Optional[List[device_health_script_assignment.DeviceHealthScriptAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[device_health_script_assignment.DeviceHealthScriptAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of group assignments for the device health script
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceHealthScript and sets the default values.
        """
        super().__init__()
        # The list of group assignments for the device health script
        self._assignments: Optional[List[device_health_script_assignment.DeviceHealthScriptAssignment]] = None
        # The timestamp of when the device health script was created. This property is read-only.
        self._created_date_time: Optional[datetime] = None
        # Description of the device health script
        self._description: Optional[str] = None
        # The entire content of the detection powershell script
        self._detection_script_content: Optional[bytes] = None
        # List of ComplexType DetectionScriptParameters objects.
        self._detection_script_parameters: Optional[List[device_health_script_parameter.DeviceHealthScriptParameter]] = None
        # List of run states for the device health script across all devices
        self._device_run_states: Optional[List[device_health_script_device_state.DeviceHealthScriptDeviceState]] = None
        # Name of the device health script
        self._display_name: Optional[str] = None
        # Indicate whether the script signature needs be checked
        self._enforce_signature_check: Optional[bool] = None
        # Highest available version for a Microsoft Proprietary script
        self._highest_available_version: Optional[str] = None
        # Determines if this is Microsoft Proprietary Script. Proprietary scripts are read-only
        self._is_global_script: Optional[bool] = None
        # The timestamp of when the device health script was modified. This property is read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Name of the device health script publisher
        self._publisher: Optional[str] = None
        # The entire content of the remediation powershell script
        self._remediation_script_content: Optional[bytes] = None
        # List of ComplexType RemediationScriptParameters objects.
        self._remediation_script_parameters: Optional[List[device_health_script_parameter.DeviceHealthScriptParameter]] = None
        # List of Scope Tag IDs for the device health script
        self._role_scope_tag_ids: Optional[List[str]] = None
        # Indicate whether PowerShell script(s) should run as 32-bit
        self._run_as32_bit: Optional[bool] = None
        # Indicates the type of execution context the app runs in.
        self._run_as_account: Optional[run_as_account_type.RunAsAccountType] = None
        # High level run summary for device health script.
        self._run_summary: Optional[device_health_script_run_summary.DeviceHealthScriptRunSummary] = None
        # Version of the device health script
        self._version: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The timestamp of when the device health script was created. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The timestamp of when the device health script was created. This property is read-only.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScript:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScript
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceHealthScript()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the device health script
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the device health script
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def detection_script_content(self,) -> Optional[bytes]:
        """
        Gets the detectionScriptContent property value. The entire content of the detection powershell script
        Returns: Optional[bytes]
        """
        return self._detection_script_content
    
    @detection_script_content.setter
    def detection_script_content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the detectionScriptContent property value. The entire content of the detection powershell script
        Args:
            value: Value to set for the detectionScriptContent property.
        """
        self._detection_script_content = value
    
    @property
    def detection_script_parameters(self,) -> Optional[List[device_health_script_parameter.DeviceHealthScriptParameter]]:
        """
        Gets the detectionScriptParameters property value. List of ComplexType DetectionScriptParameters objects.
        Returns: Optional[List[device_health_script_parameter.DeviceHealthScriptParameter]]
        """
        return self._detection_script_parameters
    
    @detection_script_parameters.setter
    def detection_script_parameters(self,value: Optional[List[device_health_script_parameter.DeviceHealthScriptParameter]] = None) -> None:
        """
        Sets the detectionScriptParameters property value. List of ComplexType DetectionScriptParameters objects.
        Args:
            value: Value to set for the detectionScriptParameters property.
        """
        self._detection_script_parameters = value
    
    @property
    def device_run_states(self,) -> Optional[List[device_health_script_device_state.DeviceHealthScriptDeviceState]]:
        """
        Gets the deviceRunStates property value. List of run states for the device health script across all devices
        Returns: Optional[List[device_health_script_device_state.DeviceHealthScriptDeviceState]]
        """
        return self._device_run_states
    
    @device_run_states.setter
    def device_run_states(self,value: Optional[List[device_health_script_device_state.DeviceHealthScriptDeviceState]] = None) -> None:
        """
        Sets the deviceRunStates property value. List of run states for the device health script across all devices
        Args:
            value: Value to set for the deviceRunStates property.
        """
        self._device_run_states = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the device health script
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the device health script
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def enforce_signature_check(self,) -> Optional[bool]:
        """
        Gets the enforceSignatureCheck property value. Indicate whether the script signature needs be checked
        Returns: Optional[bool]
        """
        return self._enforce_signature_check
    
    @enforce_signature_check.setter
    def enforce_signature_check(self,value: Optional[bool] = None) -> None:
        """
        Sets the enforceSignatureCheck property value. Indicate whether the script signature needs be checked
        Args:
            value: Value to set for the enforceSignatureCheck property.
        """
        self._enforce_signature_check = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_health_script_assignment.DeviceHealthScriptAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detection_script_content": lambda n : setattr(self, 'detection_script_content', n.get_bytes_value()),
            "detection_script_parameters": lambda n : setattr(self, 'detection_script_parameters', n.get_collection_of_object_values(device_health_script_parameter.DeviceHealthScriptParameter)),
            "device_run_states": lambda n : setattr(self, 'device_run_states', n.get_collection_of_object_values(device_health_script_device_state.DeviceHealthScriptDeviceState)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforce_signature_check": lambda n : setattr(self, 'enforce_signature_check', n.get_bool_value()),
            "highest_available_version": lambda n : setattr(self, 'highest_available_version', n.get_str_value()),
            "is_global_script": lambda n : setattr(self, 'is_global_script', n.get_bool_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "remediation_script_content": lambda n : setattr(self, 'remediation_script_content', n.get_bytes_value()),
            "remediation_script_parameters": lambda n : setattr(self, 'remediation_script_parameters', n.get_collection_of_object_values(device_health_script_parameter.DeviceHealthScriptParameter)),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "run_as32_bit": lambda n : setattr(self, 'run_as32_bit', n.get_bool_value()),
            "run_as_account": lambda n : setattr(self, 'run_as_account', n.get_enum_value(run_as_account_type.RunAsAccountType)),
            "run_summary": lambda n : setattr(self, 'run_summary', n.get_object_value(device_health_script_run_summary.DeviceHealthScriptRunSummary)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def highest_available_version(self,) -> Optional[str]:
        """
        Gets the highestAvailableVersion property value. Highest available version for a Microsoft Proprietary script
        Returns: Optional[str]
        """
        return self._highest_available_version
    
    @highest_available_version.setter
    def highest_available_version(self,value: Optional[str] = None) -> None:
        """
        Sets the highestAvailableVersion property value. Highest available version for a Microsoft Proprietary script
        Args:
            value: Value to set for the highestAvailableVersion property.
        """
        self._highest_available_version = value
    
    @property
    def is_global_script(self,) -> Optional[bool]:
        """
        Gets the isGlobalScript property value. Determines if this is Microsoft Proprietary Script. Proprietary scripts are read-only
        Returns: Optional[bool]
        """
        return self._is_global_script
    
    @is_global_script.setter
    def is_global_script(self,value: Optional[bool] = None) -> None:
        """
        Sets the isGlobalScript property value. Determines if this is Microsoft Proprietary Script. Proprietary scripts are read-only
        Args:
            value: Value to set for the isGlobalScript property.
        """
        self._is_global_script = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The timestamp of when the device health script was modified. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The timestamp of when the device health script was modified. This property is read-only.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. Name of the device health script publisher
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. Name of the device health script publisher
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    @property
    def remediation_script_content(self,) -> Optional[bytes]:
        """
        Gets the remediationScriptContent property value. The entire content of the remediation powershell script
        Returns: Optional[bytes]
        """
        return self._remediation_script_content
    
    @remediation_script_content.setter
    def remediation_script_content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the remediationScriptContent property value. The entire content of the remediation powershell script
        Args:
            value: Value to set for the remediationScriptContent property.
        """
        self._remediation_script_content = value
    
    @property
    def remediation_script_parameters(self,) -> Optional[List[device_health_script_parameter.DeviceHealthScriptParameter]]:
        """
        Gets the remediationScriptParameters property value. List of ComplexType RemediationScriptParameters objects.
        Returns: Optional[List[device_health_script_parameter.DeviceHealthScriptParameter]]
        """
        return self._remediation_script_parameters
    
    @remediation_script_parameters.setter
    def remediation_script_parameters(self,value: Optional[List[device_health_script_parameter.DeviceHealthScriptParameter]] = None) -> None:
        """
        Sets the remediationScriptParameters property value. List of ComplexType RemediationScriptParameters objects.
        Args:
            value: Value to set for the remediationScriptParameters property.
        """
        self._remediation_script_parameters = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tag IDs for the device health script
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tag IDs for the device health script
        Args:
            value: Value to set for the roleScopeTagIds property.
        """
        self._role_scope_tag_ids = value
    
    @property
    def run_as32_bit(self,) -> Optional[bool]:
        """
        Gets the runAs32Bit property value. Indicate whether PowerShell script(s) should run as 32-bit
        Returns: Optional[bool]
        """
        return self._run_as32_bit
    
    @run_as32_bit.setter
    def run_as32_bit(self,value: Optional[bool] = None) -> None:
        """
        Sets the runAs32Bit property value. Indicate whether PowerShell script(s) should run as 32-bit
        Args:
            value: Value to set for the runAs32Bit property.
        """
        self._run_as32_bit = value
    
    @property
    def run_as_account(self,) -> Optional[run_as_account_type.RunAsAccountType]:
        """
        Gets the runAsAccount property value. Indicates the type of execution context the app runs in.
        Returns: Optional[run_as_account_type.RunAsAccountType]
        """
        return self._run_as_account
    
    @run_as_account.setter
    def run_as_account(self,value: Optional[run_as_account_type.RunAsAccountType] = None) -> None:
        """
        Sets the runAsAccount property value. Indicates the type of execution context the app runs in.
        Args:
            value: Value to set for the runAsAccount property.
        """
        self._run_as_account = value
    
    @property
    def run_summary(self,) -> Optional[device_health_script_run_summary.DeviceHealthScriptRunSummary]:
        """
        Gets the runSummary property value. High level run summary for device health script.
        Returns: Optional[device_health_script_run_summary.DeviceHealthScriptRunSummary]
        """
        return self._run_summary
    
    @run_summary.setter
    def run_summary(self,value: Optional[device_health_script_run_summary.DeviceHealthScriptRunSummary] = None) -> None:
        """
        Sets the runSummary property value. High level run summary for device health script.
        Args:
            value: Value to set for the runSummary property.
        """
        self._run_summary = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("description", self.description)
        writer.write_object_value("detectionScriptContent", self.detection_script_content)
        writer.write_collection_of_object_values("detectionScriptParameters", self.detection_script_parameters)
        writer.write_collection_of_object_values("deviceRunStates", self.device_run_states)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enforceSignatureCheck", self.enforce_signature_check)
        writer.write_str_value("highestAvailableVersion", self.highest_available_version)
        writer.write_bool_value("isGlobalScript", self.is_global_script)
        writer.write_str_value("publisher", self.publisher)
        writer.write_object_value("remediationScriptContent", self.remediation_script_content)
        writer.write_collection_of_object_values("remediationScriptParameters", self.remediation_script_parameters)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_bool_value("runAs32Bit", self.run_as32_bit)
        writer.write_enum_value("runAsAccount", self.run_as_account)
        writer.write_object_value("runSummary", self.run_summary)
        writer.write_str_value("version", self.version)
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. Version of the device health script
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. Version of the device health script
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

