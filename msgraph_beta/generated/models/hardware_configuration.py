from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .hardware_configuration_assignment import HardwareConfigurationAssignment
    from .hardware_configuration_device_state import HardwareConfigurationDeviceState
    from .hardware_configuration_format import HardwareConfigurationFormat
    from .hardware_configuration_run_summary import HardwareConfigurationRunSummary
    from .hardware_configuration_user_state import HardwareConfigurationUserState

from .entity import Entity

@dataclass
class HardwareConfiguration(Entity):
    """
    BIOS configuration and other settings provides customers the ability to configure hardware/bios settings on the enrolled Windows 10/11 Entra ID joined devices by uploading a configuration file generated with their OEM tool (e.g. Dell Command tool). A BIOS configuration policy can be assigned to multiple devices, allowing admins to remotely control a device's hardware properties (e.g. enable Secure Boot) from the Intune Portal.
    """
    # List of the Azure AD user group ids that hardware configuration will be applied to. Only security groups and Office 365 Groups are supported.
    assignments: Optional[List[HardwareConfigurationAssignment]] = None
    # File content of the hardware configuration
    configuration_file_content: Optional[bytes] = None
    # Timestamp of when the hardware configuration was created. This property is read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Description of the hardware configuration
    description: Optional[str] = None
    # List of run states for the hardware configuration across all devices
    device_run_states: Optional[List[HardwareConfigurationDeviceState]] = None
    # Name of the hardware configuration
    display_name: Optional[str] = None
    # File name of the hardware configuration
    file_name: Optional[str] = None
    # Indicates the supported oems of hardware configuration
    hardware_configuration_format: Optional[HardwareConfigurationFormat] = None
    # Timestamp of when the hardware configuration was modified. This property is read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A value indicating whether per devcive pasword disabled
    per_device_password_disabled: Optional[bool] = None
    # List of Scope Tag IDs for the hardware configuration
    role_scope_tag_ids: Optional[List[str]] = None
    # A summary of the results from an attempt to configure hardware settings
    run_summary: Optional[HardwareConfigurationRunSummary] = None
    # List of run states for the hardware configuration across all users
    user_run_states: Optional[List[HardwareConfigurationUserState]] = None
    # Version of the hardware configuration (E.g. 1, 2, 3 ...)
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HardwareConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HardwareConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HardwareConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .hardware_configuration_assignment import HardwareConfigurationAssignment
        from .hardware_configuration_device_state import HardwareConfigurationDeviceState
        from .hardware_configuration_format import HardwareConfigurationFormat
        from .hardware_configuration_run_summary import HardwareConfigurationRunSummary
        from .hardware_configuration_user_state import HardwareConfigurationUserState

        from .entity import Entity
        from .hardware_configuration_assignment import HardwareConfigurationAssignment
        from .hardware_configuration_device_state import HardwareConfigurationDeviceState
        from .hardware_configuration_format import HardwareConfigurationFormat
        from .hardware_configuration_run_summary import HardwareConfigurationRunSummary
        from .hardware_configuration_user_state import HardwareConfigurationUserState

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(HardwareConfigurationAssignment)),
            "configurationFileContent": lambda n : setattr(self, 'configuration_file_content', n.get_bytes_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceRunStates": lambda n : setattr(self, 'device_run_states', n.get_collection_of_object_values(HardwareConfigurationDeviceState)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "hardwareConfigurationFormat": lambda n : setattr(self, 'hardware_configuration_format', n.get_enum_value(HardwareConfigurationFormat)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "perDevicePasswordDisabled": lambda n : setattr(self, 'per_device_password_disabled', n.get_bool_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "runSummary": lambda n : setattr(self, 'run_summary', n.get_object_value(HardwareConfigurationRunSummary)),
            "userRunStates": lambda n : setattr(self, 'user_run_states', n.get_collection_of_object_values(HardwareConfigurationUserState)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_bytes_value("configurationFileContent", self.configuration_file_content)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("deviceRunStates", self.device_run_states)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("fileName", self.file_name)
        writer.write_enum_value("hardwareConfigurationFormat", self.hardware_configuration_format)
        writer.write_bool_value("perDevicePasswordDisabled", self.per_device_password_disabled)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_object_value("runSummary", self.run_summary)
        writer.write_collection_of_object_values("userRunStates", self.user_run_states)
        writer.write_int_value("version", self.version)
    

