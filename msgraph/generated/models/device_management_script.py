from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_script_assignment, device_management_script_device_state, device_management_script_group_assignment, device_management_script_run_summary, device_management_script_user_state, entity, run_as_account_type

from . import entity

@dataclass
class DeviceManagementScript(entity.Entity):
    """
    Intune will provide customer the ability to run their Powershell scripts on the enrolled windows 10 Azure Active Directory joined devices. The script can be run once or periodically.
    """
    # The list of group assignments for the device management script.
    assignments: Optional[List[device_management_script_assignment.DeviceManagementScriptAssignment]] = None
    # The date and time the device management script was created. This property is read-only.
    created_date_time: Optional[datetime] = None
    # Optional description for the device management script.
    description: Optional[str] = None
    # List of run states for this script across all devices.
    device_run_states: Optional[List[device_management_script_device_state.DeviceManagementScriptDeviceState]] = None
    # Name of the device management script.
    display_name: Optional[str] = None
    # Indicate whether the script signature needs be checked.
    enforce_signature_check: Optional[bool] = None
    # Script file name.
    file_name: Optional[str] = None
    # The list of group assignments for the device management script.
    group_assignments: Optional[List[device_management_script_group_assignment.DeviceManagementScriptGroupAssignment]] = None
    # The date and time the device management script was last modified. This property is read-only.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tag IDs for this PowerShellScript instance.
    role_scope_tag_ids: Optional[List[str]] = None
    # Indicates the type of execution context the app runs in.
    run_as_account: Optional[run_as_account_type.RunAsAccountType] = None
    # A value indicating whether the PowerShell script should run as 32-bit
    run_as32_bit: Optional[bool] = None
    # Run summary for device management script.
    run_summary: Optional[device_management_script_run_summary.DeviceManagementScriptRunSummary] = None
    # The script content.
    script_content: Optional[bytes] = None
    # List of run states for this script across all users.
    user_run_states: Optional[List[device_management_script_user_state.DeviceManagementScriptUserState]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementScript:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementScript
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementScript()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_script_assignment, device_management_script_device_state, device_management_script_group_assignment, device_management_script_run_summary, device_management_script_user_state, entity, run_as_account_type

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_management_script_assignment.DeviceManagementScriptAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceRunStates": lambda n : setattr(self, 'device_run_states', n.get_collection_of_object_values(device_management_script_device_state.DeviceManagementScriptDeviceState)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforceSignatureCheck": lambda n : setattr(self, 'enforce_signature_check', n.get_bool_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "groupAssignments": lambda n : setattr(self, 'group_assignments', n.get_collection_of_object_values(device_management_script_group_assignment.DeviceManagementScriptGroupAssignment)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "runAs32Bit": lambda n : setattr(self, 'run_as32_bit', n.get_bool_value()),
            "runAsAccount": lambda n : setattr(self, 'run_as_account', n.get_enum_value(run_as_account_type.RunAsAccountType)),
            "runSummary": lambda n : setattr(self, 'run_summary', n.get_object_value(device_management_script_run_summary.DeviceManagementScriptRunSummary)),
            "scriptContent": lambda n : setattr(self, 'script_content', n.get_bytes_value()),
            "userRunStates": lambda n : setattr(self, 'user_run_states', n.get_collection_of_object_values(device_management_script_user_state.DeviceManagementScriptUserState)),
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
        writer.write_collection_of_object_values("deviceRunStates", self.device_run_states)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enforceSignatureCheck", self.enforce_signature_check)
        writer.write_str_value("fileName", self.file_name)
        writer.write_collection_of_object_values("groupAssignments", self.group_assignments)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_bool_value("runAs32Bit", self.run_as32_bit)
        writer.write_enum_value("runAsAccount", self.run_as_account)
        writer.write_object_value("runSummary", self.run_summary)
        writer.write_object_value("scriptContent", self.script_content)
        writer.write_collection_of_object_values("userRunStates", self.user_run_states)
    

