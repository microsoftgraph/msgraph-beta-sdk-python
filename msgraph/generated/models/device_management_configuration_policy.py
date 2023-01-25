from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_platforms = lazy_import('msgraph.generated.models.device_management_configuration_platforms')
device_management_configuration_policy_assignment = lazy_import('msgraph.generated.models.device_management_configuration_policy_assignment')
device_management_configuration_policy_template_reference = lazy_import('msgraph.generated.models.device_management_configuration_policy_template_reference')
device_management_configuration_setting = lazy_import('msgraph.generated.models.device_management_configuration_setting')
device_management_configuration_technologies = lazy_import('msgraph.generated.models.device_management_configuration_technologies')
device_management_priority_meta_data = lazy_import('msgraph.generated.models.device_management_priority_meta_data')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementConfigurationPolicy(entity.Entity):
    """
    Device Management Configuration Policy
    """
    @property
    def assignments(self,) -> Optional[List[device_management_configuration_policy_assignment.DeviceManagementConfigurationPolicyAssignment]]:
        """
        Gets the assignments property value. Policy assignments
        Returns: Optional[List[device_management_configuration_policy_assignment.DeviceManagementConfigurationPolicyAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[device_management_configuration_policy_assignment.DeviceManagementConfigurationPolicyAssignment]] = None) -> None:
        """
        Sets the assignments property value. Policy assignments
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationPolicy and sets the default values.
        """
        super().__init__()
        # Policy assignments
        self._assignments: Optional[List[device_management_configuration_policy_assignment.DeviceManagementConfigurationPolicyAssignment]] = None
        # Policy creation date and time
        self._created_date_time: Optional[datetime] = None
        # Policy creation source
        self._creation_source: Optional[str] = None
        # Policy description
        self._description: Optional[str] = None
        # Policy assignment status. This property is read-only.
        self._is_assigned: Optional[bool] = None
        # Policy last modification date and time
        self._last_modified_date_time: Optional[datetime] = None
        # Policy name
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Supported platform types.
        self._platforms: Optional[device_management_configuration_platforms.DeviceManagementConfigurationPlatforms] = None
        # Indicates the priority of each policies that are selected by the admin during enrollment process
        self._priority_meta_data: Optional[device_management_priority_meta_data.DeviceManagementPriorityMetaData] = None
        # List of Scope Tags for this Entity instance.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # Number of settings
        self._setting_count: Optional[int] = None
        # Policy settings
        self._settings: Optional[List[device_management_configuration_setting.DeviceManagementConfigurationSetting]] = None
        # Describes which technology this setting can be deployed with
        self._technologies: Optional[device_management_configuration_technologies.DeviceManagementConfigurationTechnologies] = None
        # Template reference information
        self._template_reference: Optional[device_management_configuration_policy_template_reference.DeviceManagementConfigurationPolicyTemplateReference] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Policy creation date and time
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Policy creation date and time
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationPolicy()
    
    @property
    def creation_source(self,) -> Optional[str]:
        """
        Gets the creationSource property value. Policy creation source
        Returns: Optional[str]
        """
        return self._creation_source
    
    @creation_source.setter
    def creation_source(self,value: Optional[str] = None) -> None:
        """
        Sets the creationSource property value. Policy creation source
        Args:
            value: Value to set for the creationSource property.
        """
        self._creation_source = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Policy description
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Policy description
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_management_configuration_policy_assignment.DeviceManagementConfigurationPolicyAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "creation_source": lambda n : setattr(self, 'creation_source', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "is_assigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "platforms": lambda n : setattr(self, 'platforms', n.get_enum_value(device_management_configuration_platforms.DeviceManagementConfigurationPlatforms)),
            "priority_meta_data": lambda n : setattr(self, 'priority_meta_data', n.get_object_value(device_management_priority_meta_data.DeviceManagementPriorityMetaData)),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "setting_count": lambda n : setattr(self, 'setting_count', n.get_int_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(device_management_configuration_setting.DeviceManagementConfigurationSetting)),
            "technologies": lambda n : setattr(self, 'technologies', n.get_enum_value(device_management_configuration_technologies.DeviceManagementConfigurationTechnologies)),
            "template_reference": lambda n : setattr(self, 'template_reference', n.get_object_value(device_management_configuration_policy_template_reference.DeviceManagementConfigurationPolicyTemplateReference)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_assigned(self,) -> Optional[bool]:
        """
        Gets the isAssigned property value. Policy assignment status. This property is read-only.
        Returns: Optional[bool]
        """
        return self._is_assigned
    
    @is_assigned.setter
    def is_assigned(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAssigned property value. Policy assignment status. This property is read-only.
        Args:
            value: Value to set for the isAssigned property.
        """
        self._is_assigned = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Policy last modification date and time
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Policy last modification date and time
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Policy name
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Policy name
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def platforms(self,) -> Optional[device_management_configuration_platforms.DeviceManagementConfigurationPlatforms]:
        """
        Gets the platforms property value. Supported platform types.
        Returns: Optional[device_management_configuration_platforms.DeviceManagementConfigurationPlatforms]
        """
        return self._platforms
    
    @platforms.setter
    def platforms(self,value: Optional[device_management_configuration_platforms.DeviceManagementConfigurationPlatforms] = None) -> None:
        """
        Sets the platforms property value. Supported platform types.
        Args:
            value: Value to set for the platforms property.
        """
        self._platforms = value
    
    @property
    def priority_meta_data(self,) -> Optional[device_management_priority_meta_data.DeviceManagementPriorityMetaData]:
        """
        Gets the priorityMetaData property value. Indicates the priority of each policies that are selected by the admin during enrollment process
        Returns: Optional[device_management_priority_meta_data.DeviceManagementPriorityMetaData]
        """
        return self._priority_meta_data
    
    @priority_meta_data.setter
    def priority_meta_data(self,value: Optional[device_management_priority_meta_data.DeviceManagementPriorityMetaData] = None) -> None:
        """
        Sets the priorityMetaData property value. Indicates the priority of each policies that are selected by the admin during enrollment process
        Args:
            value: Value to set for the priorityMetaData property.
        """
        self._priority_meta_data = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
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
    
    @property
    def setting_count(self,) -> Optional[int]:
        """
        Gets the settingCount property value. Number of settings
        Returns: Optional[int]
        """
        return self._setting_count
    
    @setting_count.setter
    def setting_count(self,value: Optional[int] = None) -> None:
        """
        Sets the settingCount property value. Number of settings
        Args:
            value: Value to set for the settingCount property.
        """
        self._setting_count = value
    
    @property
    def settings(self,) -> Optional[List[device_management_configuration_setting.DeviceManagementConfigurationSetting]]:
        """
        Gets the settings property value. Policy settings
        Returns: Optional[List[device_management_configuration_setting.DeviceManagementConfigurationSetting]]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[List[device_management_configuration_setting.DeviceManagementConfigurationSetting]] = None) -> None:
        """
        Sets the settings property value. Policy settings
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def technologies(self,) -> Optional[device_management_configuration_technologies.DeviceManagementConfigurationTechnologies]:
        """
        Gets the technologies property value. Describes which technology this setting can be deployed with
        Returns: Optional[device_management_configuration_technologies.DeviceManagementConfigurationTechnologies]
        """
        return self._technologies
    
    @technologies.setter
    def technologies(self,value: Optional[device_management_configuration_technologies.DeviceManagementConfigurationTechnologies] = None) -> None:
        """
        Sets the technologies property value. Describes which technology this setting can be deployed with
        Args:
            value: Value to set for the technologies property.
        """
        self._technologies = value
    
    @property
    def template_reference(self,) -> Optional[device_management_configuration_policy_template_reference.DeviceManagementConfigurationPolicyTemplateReference]:
        """
        Gets the templateReference property value. Template reference information
        Returns: Optional[device_management_configuration_policy_template_reference.DeviceManagementConfigurationPolicyTemplateReference]
        """
        return self._template_reference
    
    @template_reference.setter
    def template_reference(self,value: Optional[device_management_configuration_policy_template_reference.DeviceManagementConfigurationPolicyTemplateReference] = None) -> None:
        """
        Sets the templateReference property value. Template reference information
        Args:
            value: Value to set for the templateReference property.
        """
        self._template_reference = value
    

