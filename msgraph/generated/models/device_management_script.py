from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_script_assignment, device_management_script_device_state, device_management_script_group_assignment, device_management_script_run_summary, device_management_script_user_state, entity, run_as_account_type

from . import entity

class DeviceManagementScript(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementScript and sets the default values.
        """
        super().__init__()
        # The list of group assignments for the device management script.
        self._assignments: Optional[List[device_management_script_assignment.DeviceManagementScriptAssignment]] = None
        # The date and time the device management script was created. This property is read-only.
        self._created_date_time: Optional[datetime] = None
        # Optional description for the device management script.
        self._description: Optional[str] = None
        # List of run states for this script across all devices.
        self._device_run_states: Optional[List[device_management_script_device_state.DeviceManagementScriptDeviceState]] = None
        # Name of the device management script.
        self._display_name: Optional[str] = None
        # Indicate whether the script signature needs be checked.
        self._enforce_signature_check: Optional[bool] = None
        # Script file name.
        self._file_name: Optional[str] = None
        # The list of group assignments for the device management script.
        self._group_assignments: Optional[List[device_management_script_group_assignment.DeviceManagementScriptGroupAssignment]] = None
        # The date and time the device management script was last modified. This property is read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of Scope Tag IDs for this PowerShellScript instance.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # Indicates the type of execution context the app runs in.
        self._run_as_account: Optional[run_as_account_type.RunAsAccountType] = None
        # A value indicating whether the PowerShell script should run as 32-bit
        self._run_as32_bit: Optional[bool] = None
        # Run summary for device management script.
        self._run_summary: Optional[device_management_script_run_summary.DeviceManagementScriptRunSummary] = None
        # The script content.
        self._script_content: Optional[bytes] = None
        # List of run states for this script across all users.
        self._user_run_states: Optional[List[device_management_script_user_state.DeviceManagementScriptUserState]] = None
    
    @property
    def assignments(self,) -> Optional[List[device_management_script_assignment.DeviceManagementScriptAssignment]]:
        """
        Gets the assignments property value. The list of group assignments for the device management script.
        Returns: Optional[List[device_management_script_assignment.DeviceManagementScriptAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[device_management_script_assignment.DeviceManagementScriptAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of group assignments for the device management script.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the device management script was created. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the device management script was created. This property is read-only.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
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
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Optional description for the device management script.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Optional description for the device management script.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_run_states(self,) -> Optional[List[device_management_script_device_state.DeviceManagementScriptDeviceState]]:
        """
        Gets the deviceRunStates property value. List of run states for this script across all devices.
        Returns: Optional[List[device_management_script_device_state.DeviceManagementScriptDeviceState]]
        """
        return self._device_run_states
    
    @device_run_states.setter
    def device_run_states(self,value: Optional[List[device_management_script_device_state.DeviceManagementScriptDeviceState]] = None) -> None:
        """
        Sets the deviceRunStates property value. List of run states for this script across all devices.
        Args:
            value: Value to set for the device_run_states property.
        """
        self._device_run_states = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the device management script.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the device management script.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def enforce_signature_check(self,) -> Optional[bool]:
        """
        Gets the enforceSignatureCheck property value. Indicate whether the script signature needs be checked.
        Returns: Optional[bool]
        """
        return self._enforce_signature_check
    
    @enforce_signature_check.setter
    def enforce_signature_check(self,value: Optional[bool] = None) -> None:
        """
        Sets the enforceSignatureCheck property value. Indicate whether the script signature needs be checked.
        Args:
            value: Value to set for the enforce_signature_check property.
        """
        self._enforce_signature_check = value
    
    @property
    def file_name(self,) -> Optional[str]:
        """
        Gets the fileName property value. Script file name.
        Returns: Optional[str]
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileName property value. Script file name.
        Args:
            value: Value to set for the file_name property.
        """
        self._file_name = value
    
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
    
    @property
    def group_assignments(self,) -> Optional[List[device_management_script_group_assignment.DeviceManagementScriptGroupAssignment]]:
        """
        Gets the groupAssignments property value. The list of group assignments for the device management script.
        Returns: Optional[List[device_management_script_group_assignment.DeviceManagementScriptGroupAssignment]]
        """
        return self._group_assignments
    
    @group_assignments.setter
    def group_assignments(self,value: Optional[List[device_management_script_group_assignment.DeviceManagementScriptGroupAssignment]] = None) -> None:
        """
        Sets the groupAssignments property value. The list of group assignments for the device management script.
        Args:
            value: Value to set for the group_assignments property.
        """
        self._group_assignments = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the device management script was last modified. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the device management script was last modified. This property is read-only.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tag IDs for this PowerShellScript instance.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tag IDs for this PowerShellScript instance.
        Args:
            value: Value to set for the role_scope_tag_ids property.
        """
        self._role_scope_tag_ids = value
    
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
            value: Value to set for the run_as_account property.
        """
        self._run_as_account = value
    
    @property
    def run_as32_bit(self,) -> Optional[bool]:
        """
        Gets the runAs32Bit property value. A value indicating whether the PowerShell script should run as 32-bit
        Returns: Optional[bool]
        """
        return self._run_as32_bit
    
    @run_as32_bit.setter
    def run_as32_bit(self,value: Optional[bool] = None) -> None:
        """
        Sets the runAs32Bit property value. A value indicating whether the PowerShell script should run as 32-bit
        Args:
            value: Value to set for the run_as32_bit property.
        """
        self._run_as32_bit = value
    
    @property
    def run_summary(self,) -> Optional[device_management_script_run_summary.DeviceManagementScriptRunSummary]:
        """
        Gets the runSummary property value. Run summary for device management script.
        Returns: Optional[device_management_script_run_summary.DeviceManagementScriptRunSummary]
        """
        return self._run_summary
    
    @run_summary.setter
    def run_summary(self,value: Optional[device_management_script_run_summary.DeviceManagementScriptRunSummary] = None) -> None:
        """
        Sets the runSummary property value. Run summary for device management script.
        Args:
            value: Value to set for the run_summary property.
        """
        self._run_summary = value
    
    @property
    def script_content(self,) -> Optional[bytes]:
        """
        Gets the scriptContent property value. The script content.
        Returns: Optional[bytes]
        """
        return self._script_content
    
    @script_content.setter
    def script_content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the scriptContent property value. The script content.
        Args:
            value: Value to set for the script_content property.
        """
        self._script_content = value
    
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
    
    @property
    def user_run_states(self,) -> Optional[List[device_management_script_user_state.DeviceManagementScriptUserState]]:
        """
        Gets the userRunStates property value. List of run states for this script across all users.
        Returns: Optional[List[device_management_script_user_state.DeviceManagementScriptUserState]]
        """
        return self._user_run_states
    
    @user_run_states.setter
    def user_run_states(self,value: Optional[List[device_management_script_user_state.DeviceManagementScriptUserState]] = None) -> None:
        """
        Sets the userRunStates property value. List of run states for this script across all users.
        Args:
            value: Value to set for the user_run_states property.
        """
        self._user_run_states = value
    

