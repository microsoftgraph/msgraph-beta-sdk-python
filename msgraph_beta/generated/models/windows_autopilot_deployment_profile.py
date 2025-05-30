from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .active_directory_windows_autopilot_deployment_profile import ActiveDirectoryWindowsAutopilotDeploymentProfile
    from .azure_a_d_windows_autopilot_deployment_profile import AzureADWindowsAutopilotDeploymentProfile
    from .entity import Entity
    from .out_of_box_experience_setting import OutOfBoxExperienceSetting
    from .out_of_box_experience_settings import OutOfBoxExperienceSettings
    from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment
    from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
    from .windows_autopilot_device_type import WindowsAutopilotDeviceType
    from .windows_enrollment_status_screen_settings import WindowsEnrollmentStatusScreenSettings

from .entity import Entity

@dataclass
class WindowsAutopilotDeploymentProfile(Entity, Parsable):
    """
    Windows Autopilot Deployment Profile
    """
    # The list of assigned devices for the profile.
    assigned_devices: Optional[list[WindowsAutopilotDeviceIdentity]] = None
    # The list of group assignments for the profile.
    assignments: Optional[list[WindowsAutopilotDeploymentProfileAssignment]] = None
    # The date and time of when the deployment profile was created. The value cannot be modified and is automatically populated when the profile was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Supports: $select, $top, $skip. $Search, $orderBy and $filter are not supported. Read-Only.
    created_date_time: Optional[datetime.datetime] = None
    # A description of the deployment profile. Max allowed length is 1500 chars. Supports: $select, $top, $skip, $orderBy. $Search and $filter are not supported.
    description: Optional[str] = None
    # The template used to name the Autopilot device. This can be a custom text and can also contain either the serial number of the device, or a randomly generated number. The total length of the text generated by the template can be no more than 15 characters. Supports: $select, $top, $skip. $Search, $orderBy and $filter are not supported.
    device_name_template: Optional[str] = None
    # The deviceType property
    device_type: Optional[WindowsAutopilotDeviceType] = None
    # The display name of the deployment profile. Max allowed length is 200 chars. Returned by default. Supports: $select, $top, $skip, $orderby. $Search and $filter are not supported.
    display_name: Optional[str] = None
    # Indicates whether the user is allowed to use Windows Autopilot for pre-provisioned deployment mode during Out of Box experience (OOBE). When TRUE, indicates that Windows Autopilot for pre-provisioned deployment mode is allowed. When false, Windows Autopilot for pre-provisioned deployment mode is not allowed. The default is FALSE. Read-Only. Starting from May 2024 this property will no longer be supported and will be marked as deprecated. Use preprovisioningAllowed instead.
    enable_white_glove: Optional[bool] = None
    # Enrollment status screen setting
    enrollment_status_screen_settings: Optional[WindowsEnrollmentStatusScreenSettings] = None
    # Indicates whether the profile supports the extraction of hardware hash values and registration of the device into Windows Autopilot. When TRUE, indicates if hardware extraction and Windows Autopilot registration will happen on the next successful check-in. When FALSE, hardware hash extraction and Windows Autopilot registration will not happen. Default value is FALSE. Supports: $select, $top, $skip. $Search, $orderBy and $filter are not supported. Read-Only. Starting from May 2024 this property will no longer be supported and will be marked as deprecated. Use hardwareHashExtractionEnabled instead.
    extract_hardware_hash: Optional[bool] = None
    # Indicates whether the profile supports the extraction of hardware hash values and registration of the device into Windows Autopilot. When TRUE, indicates if hardware extraction and Windows Autopilot registration will happen on the next successful check-in. When FALSE, hardware hash extraction and Windows Autopilot registration will not happen. Default value is FALSE. Supports: $select, $top, $skip. $Search, $orderBy and $filter are not supported.
    hardware_hash_extraction_enabled: Optional[bool] = None
    # The language code to be used when configuring the device. E.g. en-US. The default value is os-default. Supports: $select, $top, $skip. $Search, $orderBy and $filter are not supported. Read-Only. Starting from May 2024 this property will no longer be supported and will be marked as deprecated. Use locale instead.
    language: Optional[str] = None
    # The date and time of when the deployment profile was last modified. The value cannot be updated manually and is automatically populated when any changes are made to the profile. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Supports: $select, $top, $skip. $Search, $orderBy and $filter are not supported Read-Only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The locale (language) to be used when configuring the device. E.g. en-US. The default value is os-default. Supports: $select, $top, $skip. $Search, $orderBy and $filter are not supported.
    locale: Optional[str] = None
    # The Entra management service App ID which gets used during client device-based enrollment discovery. Supports: $select, $top, $skip. $Search, $orderBy and $filter are not supported.
    management_service_app_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Windows Autopilot Deployment Profile settings used by the device for the out-of-box experience. Supports: $select, $top, $skip. $Search, $orderBy and $filter are not supported.
    out_of_box_experience_setting: Optional[OutOfBoxExperienceSetting] = None
    # The Windows Autopilot Deployment Profile settings used by the Autopilot device for out-of-box experience. Supports: $select, $top, $skip. $Search, $orderBy and $filter are not supported. Read-Only. Starting from May 2024 this property will no longer be supported and will be marked as deprecated. Use outOfBoxExperienceSetting instead.
    out_of_box_experience_settings: Optional[OutOfBoxExperienceSettings] = None
    # Indicates whether the user is allowed to use Windows Autopilot for pre-provisioned deployment mode during Out of Box experience (OOBE). When TRUE, indicates that Windows Autopilot for pre-provisioned deployment mode for OOBE is allowed to be used. When false, Windows Autopilot for pre-provisioned deployment mode for OOBE is not allowed. The default is FALSE.
    preprovisioning_allowed: Optional[bool] = None
    # List of role scope tags for the deployment profile.
    role_scope_tag_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsAutopilotDeploymentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAutopilotDeploymentProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activeDirectoryWindowsAutopilotDeploymentProfile".casefold():
            from .active_directory_windows_autopilot_deployment_profile import ActiveDirectoryWindowsAutopilotDeploymentProfile

            return ActiveDirectoryWindowsAutopilotDeploymentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureADWindowsAutopilotDeploymentProfile".casefold():
            from .azure_a_d_windows_autopilot_deployment_profile import AzureADWindowsAutopilotDeploymentProfile

            return AzureADWindowsAutopilotDeploymentProfile()
        return WindowsAutopilotDeploymentProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .active_directory_windows_autopilot_deployment_profile import ActiveDirectoryWindowsAutopilotDeploymentProfile
        from .azure_a_d_windows_autopilot_deployment_profile import AzureADWindowsAutopilotDeploymentProfile
        from .entity import Entity
        from .out_of_box_experience_setting import OutOfBoxExperienceSetting
        from .out_of_box_experience_settings import OutOfBoxExperienceSettings
        from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment
        from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
        from .windows_autopilot_device_type import WindowsAutopilotDeviceType
        from .windows_enrollment_status_screen_settings import WindowsEnrollmentStatusScreenSettings

        from .active_directory_windows_autopilot_deployment_profile import ActiveDirectoryWindowsAutopilotDeploymentProfile
        from .azure_a_d_windows_autopilot_deployment_profile import AzureADWindowsAutopilotDeploymentProfile
        from .entity import Entity
        from .out_of_box_experience_setting import OutOfBoxExperienceSetting
        from .out_of_box_experience_settings import OutOfBoxExperienceSettings
        from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment
        from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
        from .windows_autopilot_device_type import WindowsAutopilotDeviceType
        from .windows_enrollment_status_screen_settings import WindowsEnrollmentStatusScreenSettings

        fields: dict[str, Callable[[Any], None]] = {
            "assignedDevices": lambda n : setattr(self, 'assigned_devices', n.get_collection_of_object_values(WindowsAutopilotDeviceIdentity)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(WindowsAutopilotDeploymentProfileAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceNameTemplate": lambda n : setattr(self, 'device_name_template', n.get_str_value()),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_enum_value(WindowsAutopilotDeviceType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enableWhiteGlove": lambda n : setattr(self, 'enable_white_glove', n.get_bool_value()),
            "enrollmentStatusScreenSettings": lambda n : setattr(self, 'enrollment_status_screen_settings', n.get_object_value(WindowsEnrollmentStatusScreenSettings)),
            "extractHardwareHash": lambda n : setattr(self, 'extract_hardware_hash', n.get_bool_value()),
            "hardwareHashExtractionEnabled": lambda n : setattr(self, 'hardware_hash_extraction_enabled', n.get_bool_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "managementServiceAppId": lambda n : setattr(self, 'management_service_app_id', n.get_str_value()),
            "outOfBoxExperienceSetting": lambda n : setattr(self, 'out_of_box_experience_setting', n.get_object_value(OutOfBoxExperienceSetting)),
            "outOfBoxExperienceSettings": lambda n : setattr(self, 'out_of_box_experience_settings', n.get_object_value(OutOfBoxExperienceSettings)),
            "preprovisioningAllowed": lambda n : setattr(self, 'preprovisioning_allowed', n.get_bool_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignedDevices", self.assigned_devices)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("deviceNameTemplate", self.device_name_template)
        writer.write_enum_value("deviceType", self.device_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enableWhiteGlove", self.enable_white_glove)
        writer.write_object_value("enrollmentStatusScreenSettings", self.enrollment_status_screen_settings)
        writer.write_bool_value("extractHardwareHash", self.extract_hardware_hash)
        writer.write_bool_value("hardwareHashExtractionEnabled", self.hardware_hash_extraction_enabled)
        writer.write_str_value("language", self.language)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("locale", self.locale)
        writer.write_str_value("managementServiceAppId", self.management_service_app_id)
        writer.write_object_value("outOfBoxExperienceSetting", self.out_of_box_experience_setting)
        writer.write_object_value("outOfBoxExperienceSettings", self.out_of_box_experience_settings)
        writer.write_bool_value("preprovisioningAllowed", self.preprovisioning_allowed)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

