from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_comanagement_authority_configuration, device_enrollment_configuration_type, device_enrollment_limit_configuration, device_enrollment_notification_configuration, device_enrollment_platform_restrictions_configuration, device_enrollment_platform_restriction_configuration, device_enrollment_windows_hello_for_business_configuration, enrollment_configuration_assignment, entity, windows10_enrollment_completion_page_configuration

from . import entity

@dataclass
class DeviceEnrollmentConfiguration(entity.Entity):
    """
    The Base Class of Device Enrollment Configuration
    """
    # The list of group assignments for the device configuration profile
    assignments: Optional[List[enrollment_configuration_assignment.EnrollmentConfigurationAssignment]] = None
    # Created date time in UTC of the device enrollment configuration
    created_date_time: Optional[datetime] = None
    # The description of the device enrollment configuration
    description: Optional[str] = None
    # Describes the TemplateFamily for the Template entity
    device_enrollment_configuration_type: Optional[device_enrollment_configuration_type.DeviceEnrollmentConfigurationType] = None
    # The display name of the device enrollment configuration
    display_name: Optional[str] = None
    # Last modified date time in UTC of the device enrollment configuration
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Priority is used when a user exists in multiple groups that are assigned enrollment configuration. Users are subject only to the configuration with the lowest priority value.
    priority: Optional[int] = None
    # Optional role scope tags for the enrollment restrictions.
    role_scope_tag_ids: Optional[List[str]] = None
    # The version of the device enrollment configuration
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceEnrollmentConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComanagementAuthorityConfiguration".casefold():
            from . import device_comanagement_authority_configuration

            return device_comanagement_authority_configuration.DeviceComanagementAuthorityConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentLimitConfiguration".casefold():
            from . import device_enrollment_limit_configuration

            return device_enrollment_limit_configuration.DeviceEnrollmentLimitConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentNotificationConfiguration".casefold():
            from . import device_enrollment_notification_configuration

            return device_enrollment_notification_configuration.DeviceEnrollmentNotificationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentPlatformRestrictionConfiguration".casefold():
            from . import device_enrollment_platform_restriction_configuration

            return device_enrollment_platform_restriction_configuration.DeviceEnrollmentPlatformRestrictionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration".casefold():
            from . import device_enrollment_platform_restrictions_configuration

            return device_enrollment_platform_restrictions_configuration.DeviceEnrollmentPlatformRestrictionsConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentWindowsHelloForBusinessConfiguration".casefold():
            from . import device_enrollment_windows_hello_for_business_configuration

            return device_enrollment_windows_hello_for_business_configuration.DeviceEnrollmentWindowsHelloForBusinessConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EnrollmentCompletionPageConfiguration".casefold():
            from . import windows10_enrollment_completion_page_configuration

            return windows10_enrollment_completion_page_configuration.Windows10EnrollmentCompletionPageConfiguration()
        return DeviceEnrollmentConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_comanagement_authority_configuration, device_enrollment_configuration_type, device_enrollment_limit_configuration, device_enrollment_notification_configuration, device_enrollment_platform_restrictions_configuration, device_enrollment_platform_restriction_configuration, device_enrollment_windows_hello_for_business_configuration, enrollment_configuration_assignment, entity, windows10_enrollment_completion_page_configuration

        from . import device_comanagement_authority_configuration, device_enrollment_configuration_type, device_enrollment_limit_configuration, device_enrollment_notification_configuration, device_enrollment_platform_restrictions_configuration, device_enrollment_platform_restriction_configuration, device_enrollment_windows_hello_for_business_configuration, enrollment_configuration_assignment, entity, windows10_enrollment_completion_page_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(enrollment_configuration_assignment.EnrollmentConfigurationAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceEnrollmentConfigurationType": lambda n : setattr(self, 'device_enrollment_configuration_type', n.get_enum_value(device_enrollment_configuration_type.DeviceEnrollmentConfigurationType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("deviceEnrollmentConfigurationType", self.device_enrollment_configuration_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_int_value("priority", self.priority)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_int_value("version", self.version)
    

