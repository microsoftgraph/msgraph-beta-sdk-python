from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_compliance_script_device_state import DeviceComplianceScriptDeviceState
    from .device_compliance_script_run_summary import DeviceComplianceScriptRunSummary
    from .device_health_script_assignment import DeviceHealthScriptAssignment
    from .entity import Entity
    from .run_as_account_type import RunAsAccountType

from .entity import Entity

@dataclass
class DeviceComplianceScript(Entity):
    """
    Intune will provide customer the ability to run their Powershell Compliance scripts (detection) on the enrolled windows 10 Azure Active Directory joined devices.
    """
    # The list of group assignments for the device compliance script
    assignments: Optional[List[DeviceHealthScriptAssignment]] = None
    # The timestamp of when the device compliance script was created. This property is read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Description of the device compliance script
    description: Optional[str] = None
    # The entire content of the detection powershell script
    detection_script_content: Optional[bytes] = None
    # List of run states for the device compliance script across all devices
    device_run_states: Optional[List[DeviceComplianceScriptDeviceState]] = None
    # Name of the device compliance script
    display_name: Optional[str] = None
    # Indicate whether the script signature needs be checked
    enforce_signature_check: Optional[bool] = None
    # The timestamp of when the device compliance script was modified. This property is read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the device compliance script publisher
    publisher: Optional[str] = None
    # List of Scope Tag IDs for the device compliance script
    role_scope_tag_ids: Optional[List[str]] = None
    # Indicates the type of execution context the app runs in.
    run_as_account: Optional[RunAsAccountType] = None
    # Indicate whether PowerShell script(s) should run as 32-bit
    run_as32_bit: Optional[bool] = None
    # High level run summary for device compliance script.
    run_summary: Optional[DeviceComplianceScriptRunSummary] = None
    # Version of the device compliance script
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComplianceScript:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScript
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceComplianceScript()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_compliance_script_device_state import DeviceComplianceScriptDeviceState
        from .device_compliance_script_run_summary import DeviceComplianceScriptRunSummary
        from .device_health_script_assignment import DeviceHealthScriptAssignment
        from .entity import Entity
        from .run_as_account_type import RunAsAccountType

        from .device_compliance_script_device_state import DeviceComplianceScriptDeviceState
        from .device_compliance_script_run_summary import DeviceComplianceScriptRunSummary
        from .device_health_script_assignment import DeviceHealthScriptAssignment
        from .entity import Entity
        from .run_as_account_type import RunAsAccountType

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(DeviceHealthScriptAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detectionScriptContent": lambda n : setattr(self, 'detection_script_content', n.get_bytes_value()),
            "deviceRunStates": lambda n : setattr(self, 'device_run_states', n.get_collection_of_object_values(DeviceComplianceScriptDeviceState)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforceSignatureCheck": lambda n : setattr(self, 'enforce_signature_check', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "runAsAccount": lambda n : setattr(self, 'run_as_account', n.get_enum_value(RunAsAccountType)),
            "runAs32Bit": lambda n : setattr(self, 'run_as32_bit', n.get_bool_value()),
            "runSummary": lambda n : setattr(self, 'run_summary', n.get_object_value(DeviceComplianceScriptRunSummary)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("description", self.description)
        writer.write_bytes_value("detectionScriptContent", self.detection_script_content)
        writer.write_collection_of_object_values("deviceRunStates", self.device_run_states)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enforceSignatureCheck", self.enforce_signature_check)
        writer.write_str_value("publisher", self.publisher)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_enum_value("runAsAccount", self.run_as_account)
        writer.write_bool_value("runAs32Bit", self.run_as32_bit)
        writer.write_object_value("runSummary", self.run_summary)
        writer.write_str_value("version", self.version)
    

