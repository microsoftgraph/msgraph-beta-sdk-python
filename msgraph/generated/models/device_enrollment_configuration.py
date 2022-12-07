from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_enrollment_configuration_type = lazy_import('msgraph.generated.models.device_enrollment_configuration_type')
enrollment_configuration_assignment = lazy_import('msgraph.generated.models.enrollment_configuration_assignment')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceEnrollmentConfiguration(entity.Entity):
    """
    The Base Class of Device Enrollment Configuration
    """
    @property
    def assignments(self,) -> Optional[List[enrollment_configuration_assignment.EnrollmentConfigurationAssignment]]:
        """
        Gets the assignments property value. The list of group assignments for the device configuration profile
        Returns: Optional[List[enrollment_configuration_assignment.EnrollmentConfigurationAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[enrollment_configuration_assignment.EnrollmentConfigurationAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of group assignments for the device configuration profile
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceEnrollmentConfiguration and sets the default values.
        """
        super().__init__()
        # The list of group assignments for the device configuration profile
        self._assignments: Optional[List[enrollment_configuration_assignment.EnrollmentConfigurationAssignment]] = None
        # Created date time in UTC of the device enrollment configuration
        self._created_date_time: Optional[datetime] = None
        # The description of the device enrollment configuration
        self._description: Optional[str] = None
        # Describes the TemplateFamily for the Template entity
        self._device_enrollment_configuration_type: Optional[device_enrollment_configuration_type.DeviceEnrollmentConfigurationType] = None
        # The display name of the device enrollment configuration
        self._display_name: Optional[str] = None
        # Last modified date time in UTC of the device enrollment configuration
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Priority is used when a user exists in multiple groups that are assigned enrollment configuration. Users are subject only to the configuration with the lowest priority value.
        self._priority: Optional[int] = None
        # Optional role scope tags for the enrollment restrictions.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # The version of the device enrollment configuration
        self._version: Optional[int] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Created date time in UTC of the device enrollment configuration
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Created date time in UTC of the device enrollment configuration
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceEnrollmentConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceEnrollmentConfiguration()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the device enrollment configuration
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the device enrollment configuration
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_enrollment_configuration_type(self,) -> Optional[device_enrollment_configuration_type.DeviceEnrollmentConfigurationType]:
        """
        Gets the deviceEnrollmentConfigurationType property value. Describes the TemplateFamily for the Template entity
        Returns: Optional[device_enrollment_configuration_type.DeviceEnrollmentConfigurationType]
        """
        return self._device_enrollment_configuration_type
    
    @device_enrollment_configuration_type.setter
    def device_enrollment_configuration_type(self,value: Optional[device_enrollment_configuration_type.DeviceEnrollmentConfigurationType] = None) -> None:
        """
        Sets the deviceEnrollmentConfigurationType property value. Describes the TemplateFamily for the Template entity
        Args:
            value: Value to set for the deviceEnrollmentConfigurationType property.
        """
        self._device_enrollment_configuration_type = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the device enrollment configuration
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the device enrollment configuration
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(enrollment_configuration_assignment.EnrollmentConfigurationAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "device_enrollment_configuration_type": lambda n : setattr(self, 'device_enrollment_configuration_type', n.get_enum_value(device_enrollment_configuration_type.DeviceEnrollmentConfigurationType)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Last modified date time in UTC of the device enrollment configuration
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Last modified date time in UTC of the device enrollment configuration
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. Priority is used when a user exists in multiple groups that are assigned enrollment configuration. Users are subject only to the configuration with the lowest priority value.
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. Priority is used when a user exists in multiple groups that are assigned enrollment configuration. Users are subject only to the configuration with the lowest priority value.
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. Optional role scope tags for the enrollment restrictions.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. Optional role scope tags for the enrollment restrictions.
        Args:
            value: Value to set for the roleScopeTagIds property.
        """
        self._role_scope_tag_ids = value
    
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("deviceEnrollmentConfigurationType", self.device_enrollment_configuration_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_int_value("priority", self.priority)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_int_value("version", self.version)
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. The version of the device enrollment configuration
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. The version of the device enrollment configuration
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

