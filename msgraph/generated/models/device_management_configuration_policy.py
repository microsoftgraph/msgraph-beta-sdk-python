from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_platforms, device_management_configuration_policy_assignment, device_management_configuration_policy_template_reference, device_management_configuration_setting, device_management_configuration_technologies, device_management_priority_meta_data, entity

from . import entity

@dataclass
class DeviceManagementConfigurationPolicy(entity.Entity):
    """
    Device Management Configuration Policy
    """
    # Policy assignments
    assignments: Optional[List[device_management_configuration_policy_assignment.DeviceManagementConfigurationPolicyAssignment]] = None
    # Policy creation date and time
    created_date_time: Optional[datetime] = None
    # Policy creation source
    creation_source: Optional[str] = None
    # Policy description
    description: Optional[str] = None
    # Policy assignment status. This property is read-only.
    is_assigned: Optional[bool] = None
    # Policy last modification date and time
    last_modified_date_time: Optional[datetime] = None
    # Policy name
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types.
    platforms: Optional[device_management_configuration_platforms.DeviceManagementConfigurationPlatforms] = None
    # Indicates the priority of each policies that are selected by the admin during enrollment process
    priority_meta_data: Optional[device_management_priority_meta_data.DeviceManagementPriorityMetaData] = None
    # List of Scope Tags for this Entity instance.
    role_scope_tag_ids: Optional[List[str]] = None
    # Number of settings
    setting_count: Optional[int] = None
    # Policy settings
    settings: Optional[List[device_management_configuration_setting.DeviceManagementConfigurationSetting]] = None
    # Describes which technology this setting can be deployed with
    technologies: Optional[device_management_configuration_technologies.DeviceManagementConfigurationTechnologies] = None
    # Template reference information
    template_reference: Optional[device_management_configuration_policy_template_reference.DeviceManagementConfigurationPolicyTemplateReference] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_platforms, device_management_configuration_policy_assignment, device_management_configuration_policy_template_reference, device_management_configuration_setting, device_management_configuration_technologies, device_management_priority_meta_data, entity

        from . import device_management_configuration_platforms, device_management_configuration_policy_assignment, device_management_configuration_policy_template_reference, device_management_configuration_setting, device_management_configuration_technologies, device_management_priority_meta_data, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_management_configuration_policy_assignment.DeviceManagementConfigurationPolicyAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "creationSource": lambda n : setattr(self, 'creation_source', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "isAssigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "platforms": lambda n : setattr(self, 'platforms', n.get_enum_value(device_management_configuration_platforms.DeviceManagementConfigurationPlatforms)),
            "priorityMetaData": lambda n : setattr(self, 'priority_meta_data', n.get_object_value(device_management_priority_meta_data.DeviceManagementPriorityMetaData)),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "settingCount": lambda n : setattr(self, 'setting_count', n.get_int_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(device_management_configuration_setting.DeviceManagementConfigurationSetting)),
            "technologies": lambda n : setattr(self, 'technologies', n.get_enum_value(device_management_configuration_technologies.DeviceManagementConfigurationTechnologies)),
            "templateReference": lambda n : setattr(self, 'template_reference', n.get_object_value(device_management_configuration_policy_template_reference.DeviceManagementConfigurationPolicyTemplateReference)),
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
        writer.write_str_value("creationSource", self.creation_source)
        writer.write_str_value("description", self.description)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("platforms", self.platforms)
        writer.write_object_value("priorityMetaData", self.priority_meta_data)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_int_value("settingCount", self.setting_count)
        writer.write_collection_of_object_values("settings", self.settings)
        writer.write_enum_value("technologies", self.technologies)
        writer.write_object_value("templateReference", self.template_reference)
    

