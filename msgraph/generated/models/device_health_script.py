from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_health_script_assignment, device_health_script_device_state, device_health_script_parameter, device_health_script_run_summary, device_health_script_type, entity, run_as_account_type

from . import entity

@dataclass
class DeviceHealthScript(entity.Entity):
    """
    Intune will provide customer the ability to run their Powershell Health scripts (remediation + detection) on the enrolled windows 10 Azure Active Directory joined devices.
    """
    # The list of group assignments for the device health script
    assignments: Optional[List[device_health_script_assignment.DeviceHealthScriptAssignment]] = None
    # The timestamp of when the device health script was created. This property is read-only.
    created_date_time: Optional[datetime] = None
    # Description of the device health script
    description: Optional[str] = None
    # The entire content of the detection powershell script
    detection_script_content: Optional[bytes] = None
    # List of ComplexType DetectionScriptParameters objects.
    detection_script_parameters: Optional[List[device_health_script_parameter.DeviceHealthScriptParameter]] = None
    # Indicates the type of device script.
    device_health_script_type: Optional[device_health_script_type.DeviceHealthScriptType] = None
    # List of run states for the device health script across all devices
    device_run_states: Optional[List[device_health_script_device_state.DeviceHealthScriptDeviceState]] = None
    # Name of the device health script
    display_name: Optional[str] = None
    # Indicate whether the script signature needs be checked
    enforce_signature_check: Optional[bool] = None
    # Highest available version for a Microsoft Proprietary script
    highest_available_version: Optional[str] = None
    # Determines if this is Microsoft Proprietary Script. Proprietary scripts are read-only
    is_global_script: Optional[bool] = None
    # The timestamp of when the device health script was modified. This property is read-only.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the device health script publisher
    publisher: Optional[str] = None
    # The entire content of the remediation powershell script
    remediation_script_content: Optional[bytes] = None
    # List of ComplexType RemediationScriptParameters objects.
    remediation_script_parameters: Optional[List[device_health_script_parameter.DeviceHealthScriptParameter]] = None
    # List of Scope Tag IDs for the device health script
    role_scope_tag_ids: Optional[List[str]] = None
    # Indicates the type of execution context the app runs in.
    run_as_account: Optional[run_as_account_type.RunAsAccountType] = None
    # Indicate whether PowerShell script(s) should run as 32-bit
    run_as32_bit: Optional[bool] = None
    # High level run summary for device health script.
    run_summary: Optional[device_health_script_run_summary.DeviceHealthScriptRunSummary] = None
    # Version of the device health script
    version: Optional[str] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_health_script_assignment, device_health_script_device_state, device_health_script_parameter, device_health_script_run_summary, device_health_script_type, entity, run_as_account_type

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_health_script_assignment.DeviceHealthScriptAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detectionScriptContent": lambda n : setattr(self, 'detection_script_content', n.get_bytes_value()),
            "detectionScriptParameters": lambda n : setattr(self, 'detection_script_parameters', n.get_collection_of_object_values(device_health_script_parameter.DeviceHealthScriptParameter)),
            "deviceHealthScriptType": lambda n : setattr(self, 'device_health_script_type', n.get_enum_value(device_health_script_type.DeviceHealthScriptType)),
            "deviceRunStates": lambda n : setattr(self, 'device_run_states', n.get_collection_of_object_values(device_health_script_device_state.DeviceHealthScriptDeviceState)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforceSignatureCheck": lambda n : setattr(self, 'enforce_signature_check', n.get_bool_value()),
            "highestAvailableVersion": lambda n : setattr(self, 'highest_available_version', n.get_str_value()),
            "isGlobalScript": lambda n : setattr(self, 'is_global_script', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "remediationScriptContent": lambda n : setattr(self, 'remediation_script_content', n.get_bytes_value()),
            "remediationScriptParameters": lambda n : setattr(self, 'remediation_script_parameters', n.get_collection_of_object_values(device_health_script_parameter.DeviceHealthScriptParameter)),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "runAs32Bit": lambda n : setattr(self, 'run_as32_bit', n.get_bool_value()),
            "runAsAccount": lambda n : setattr(self, 'run_as_account', n.get_enum_value(run_as_account_type.RunAsAccountType)),
            "runSummary": lambda n : setattr(self, 'run_summary', n.get_object_value(device_health_script_run_summary.DeviceHealthScriptRunSummary)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("description", self.description)
        writer.write_object_value("detectionScriptContent", self.detection_script_content)
        writer.write_collection_of_object_values("detectionScriptParameters", self.detection_script_parameters)
        writer.write_enum_value("deviceHealthScriptType", self.device_health_script_type)
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
    

