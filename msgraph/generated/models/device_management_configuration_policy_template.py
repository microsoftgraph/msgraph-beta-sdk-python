from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_platforms = lazy_import('msgraph.generated.models.device_management_configuration_platforms')
device_management_configuration_setting_template = lazy_import('msgraph.generated.models.device_management_configuration_setting_template')
device_management_configuration_technologies = lazy_import('msgraph.generated.models.device_management_configuration_technologies')
device_management_configuration_template_family = lazy_import('msgraph.generated.models.device_management_configuration_template_family')
device_management_template_lifecycle_state = lazy_import('msgraph.generated.models.device_management_template_lifecycle_state')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementConfigurationPolicyTemplate(entity.Entity):
    """
    Device Management Configuration Policy Template
    """
    @property
    def allow_unmanaged_settings(self,) -> Optional[bool]:
        """
        Gets the allowUnmanagedSettings property value. Allow unmanaged setting templates
        Returns: Optional[bool]
        """
        return self._allow_unmanaged_settings
    
    @allow_unmanaged_settings.setter
    def allow_unmanaged_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowUnmanagedSettings property value. Allow unmanaged setting templates
        Args:
            value: Value to set for the allowUnmanagedSettings property.
        """
        self._allow_unmanaged_settings = value
    
    @property
    def base_id(self,) -> Optional[str]:
        """
        Gets the baseId property value. Template base identifier
        Returns: Optional[str]
        """
        return self._base_id
    
    @base_id.setter
    def base_id(self,value: Optional[str] = None) -> None:
        """
        Sets the baseId property value. Template base identifier
        Args:
            value: Value to set for the baseId property.
        """
        self._base_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationPolicyTemplate and sets the default values.
        """
        super().__init__()
        # Allow unmanaged setting templates
        self._allow_unmanaged_settings: Optional[bool] = None
        # Template base identifier
        self._base_id: Optional[str] = None
        # Template description
        self._description: Optional[str] = None
        # Template display name
        self._display_name: Optional[str] = None
        # Description of template version
        self._display_version: Optional[str] = None
        # Describes current lifecycle state of a template
        self._lifecycle_state: Optional[device_management_template_lifecycle_state.DeviceManagementTemplateLifecycleState] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Supported platform types.
        self._platforms: Optional[device_management_configuration_platforms.DeviceManagementConfigurationPlatforms] = None
        # Number of setting templates. Valid values 0 to 2147483647. This property is read-only.
        self._setting_template_count: Optional[int] = None
        # Setting templates
        self._setting_templates: Optional[List[device_management_configuration_setting_template.DeviceManagementConfigurationSettingTemplate]] = None
        # Describes which technology this setting can be deployed with
        self._technologies: Optional[device_management_configuration_technologies.DeviceManagementConfigurationTechnologies] = None
        # Describes the TemplateFamily for the Template entity
        self._template_family: Optional[device_management_configuration_template_family.DeviceManagementConfigurationTemplateFamily] = None
        # Template version. Valid values 1 to 2147483647. This property is read-only.
        self._version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationPolicyTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationPolicyTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationPolicyTemplate()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Template description
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Template description
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Template display name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Template display name
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def display_version(self,) -> Optional[str]:
        """
        Gets the displayVersion property value. Description of template version
        Returns: Optional[str]
        """
        return self._display_version
    
    @display_version.setter
    def display_version(self,value: Optional[str] = None) -> None:
        """
        Sets the displayVersion property value. Description of template version
        Args:
            value: Value to set for the displayVersion property.
        """
        self._display_version = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_unmanaged_settings": lambda n : setattr(self, 'allow_unmanaged_settings', n.get_bool_value()),
            "base_id": lambda n : setattr(self, 'base_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "display_version": lambda n : setattr(self, 'display_version', n.get_str_value()),
            "lifecycle_state": lambda n : setattr(self, 'lifecycle_state', n.get_enum_value(device_management_template_lifecycle_state.DeviceManagementTemplateLifecycleState)),
            "platforms": lambda n : setattr(self, 'platforms', n.get_enum_value(device_management_configuration_platforms.DeviceManagementConfigurationPlatforms)),
            "setting_template_count": lambda n : setattr(self, 'setting_template_count', n.get_int_value()),
            "setting_templates": lambda n : setattr(self, 'setting_templates', n.get_collection_of_object_values(device_management_configuration_setting_template.DeviceManagementConfigurationSettingTemplate)),
            "technologies": lambda n : setattr(self, 'technologies', n.get_enum_value(device_management_configuration_technologies.DeviceManagementConfigurationTechnologies)),
            "template_family": lambda n : setattr(self, 'template_family', n.get_enum_value(device_management_configuration_template_family.DeviceManagementConfigurationTemplateFamily)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def lifecycle_state(self,) -> Optional[device_management_template_lifecycle_state.DeviceManagementTemplateLifecycleState]:
        """
        Gets the lifecycleState property value. Describes current lifecycle state of a template
        Returns: Optional[device_management_template_lifecycle_state.DeviceManagementTemplateLifecycleState]
        """
        return self._lifecycle_state
    
    @lifecycle_state.setter
    def lifecycle_state(self,value: Optional[device_management_template_lifecycle_state.DeviceManagementTemplateLifecycleState] = None) -> None:
        """
        Sets the lifecycleState property value. Describes current lifecycle state of a template
        Args:
            value: Value to set for the lifecycleState property.
        """
        self._lifecycle_state = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowUnmanagedSettings", self.allow_unmanaged_settings)
        writer.write_str_value("baseId", self.base_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("displayVersion", self.display_version)
        writer.write_enum_value("lifecycleState", self.lifecycle_state)
        writer.write_enum_value("platforms", self.platforms)
        writer.write_collection_of_object_values("settingTemplates", self.setting_templates)
        writer.write_enum_value("technologies", self.technologies)
        writer.write_enum_value("templateFamily", self.template_family)
    
    @property
    def setting_template_count(self,) -> Optional[int]:
        """
        Gets the settingTemplateCount property value. Number of setting templates. Valid values 0 to 2147483647. This property is read-only.
        Returns: Optional[int]
        """
        return self._setting_template_count
    
    @setting_template_count.setter
    def setting_template_count(self,value: Optional[int] = None) -> None:
        """
        Sets the settingTemplateCount property value. Number of setting templates. Valid values 0 to 2147483647. This property is read-only.
        Args:
            value: Value to set for the settingTemplateCount property.
        """
        self._setting_template_count = value
    
    @property
    def setting_templates(self,) -> Optional[List[device_management_configuration_setting_template.DeviceManagementConfigurationSettingTemplate]]:
        """
        Gets the settingTemplates property value. Setting templates
        Returns: Optional[List[device_management_configuration_setting_template.DeviceManagementConfigurationSettingTemplate]]
        """
        return self._setting_templates
    
    @setting_templates.setter
    def setting_templates(self,value: Optional[List[device_management_configuration_setting_template.DeviceManagementConfigurationSettingTemplate]] = None) -> None:
        """
        Sets the settingTemplates property value. Setting templates
        Args:
            value: Value to set for the settingTemplates property.
        """
        self._setting_templates = value
    
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
    def template_family(self,) -> Optional[device_management_configuration_template_family.DeviceManagementConfigurationTemplateFamily]:
        """
        Gets the templateFamily property value. Describes the TemplateFamily for the Template entity
        Returns: Optional[device_management_configuration_template_family.DeviceManagementConfigurationTemplateFamily]
        """
        return self._template_family
    
    @template_family.setter
    def template_family(self,value: Optional[device_management_configuration_template_family.DeviceManagementConfigurationTemplateFamily] = None) -> None:
        """
        Sets the templateFamily property value. Describes the TemplateFamily for the Template entity
        Args:
            value: Value to set for the templateFamily property.
        """
        self._template_family = value
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. Template version. Valid values 1 to 2147483647. This property is read-only.
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. Template version. Valid values 1 to 2147483647. This property is read-only.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

