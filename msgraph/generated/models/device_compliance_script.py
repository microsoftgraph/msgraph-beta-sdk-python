from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_compliance_script_device_state, device_compliance_script_run_summary, device_health_script_assignment, entity, run_as_account_type

from . import entity

@dataclass
class DeviceComplianceScript(entity.Entity):
    """
    Intune will provide customer the ability to run their Powershell Compliance scripts (detection) on the enrolled windows 10 Azure Active Directory joined devices.
    """
    # The list of group assignments for the device compliance script
    assignments: Optional[List[device_health_script_assignment.DeviceHealthScriptAssignment]] = None
    # The timestamp of when the device compliance script was created. This property is read-only.
    created_date_time: Optional[datetime] = None
    # Description of the device compliance script
    description: Optional[str] = None
    # The entire content of the detection powershell script
    detection_script_content: Optional[bytes] = None
    # List of run states for the device compliance script across all devices
    device_run_states: Optional[List[device_compliance_script_device_state.DeviceComplianceScriptDeviceState]] = None
    # Name of the device compliance script
    display_name: Optional[str] = None
    # Indicate whether the script signature needs be checked
    enforce_signature_check: Optional[bool] = None
    # The timestamp of when the device compliance script was modified. This property is read-only.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the device compliance script publisher
    publisher: Optional[str] = None
    # List of Scope Tag IDs for the device compliance script
    role_scope_tag_ids: Optional[List[str]] = None
    # Indicates the type of execution context the app runs in.
    run_as_account: Optional[run_as_account_type.RunAsAccountType] = None
    # Indicate whether PowerShell script(s) should run as 32-bit
    run_as32_bit: Optional[bool] = None
    # High level run summary for device compliance script.
    run_summary: Optional[device_compliance_script_run_summary.DeviceComplianceScriptRunSummary] = None
    # Version of the device compliance script
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComplianceScript:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScript
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceComplianceScript()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_compliance_script_device_state, device_compliance_script_run_summary, device_health_script_assignment, entity, run_as_account_type

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_health_script_assignment.DeviceHealthScriptAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detectionScriptContent": lambda n : setattr(self, 'detection_script_content', n.get_bytes_value()),
            "deviceRunStates": lambda n : setattr(self, 'device_run_states', n.get_collection_of_object_values(device_compliance_script_device_state.DeviceComplianceScriptDeviceState)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforceSignatureCheck": lambda n : setattr(self, 'enforce_signature_check', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "runAs32Bit": lambda n : setattr(self, 'run_as32_bit', n.get_bool_value()),
            "runAsAccount": lambda n : setattr(self, 'run_as_account', n.get_enum_value(run_as_account_type.RunAsAccountType)),
            "runSummary": lambda n : setattr(self, 'run_summary', n.get_object_value(device_compliance_script_run_summary.DeviceComplianceScriptRunSummary)),
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
        writer.write_collection_of_object_values("deviceRunStates", self.device_run_states)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enforceSignatureCheck", self.enforce_signature_check)
        writer.write_str_value("publisher", self.publisher)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_bool_value("runAs32Bit", self.run_as32_bit)
        writer.write_enum_value("runAsAccount", self.run_as_account)
        writer.write_object_value("runSummary", self.run_summary)
        writer.write_str_value("version", self.version)
    

