from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_platforms = lazy_import('msgraph.generated.models.device_management_configuration_platforms')
device_management_configuration_setting_usage = lazy_import('msgraph.generated.models.device_management_configuration_setting_usage')
device_management_configuration_technologies = lazy_import('msgraph.generated.models.device_management_configuration_technologies')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementConfigurationCategory(entity.Entity):
    """
    Device Management Configuration Policy
    """
    @property
    def category_description(self,) -> Optional[str]:
        """
        Gets the categoryDescription property value. Description of the category header
        Returns: Optional[str]
        """
        return self._category_description
    
    @category_description.setter
    def category_description(self,value: Optional[str] = None) -> None:
        """
        Sets the categoryDescription property value. Description of the category header
        Args:
            value: Value to set for the categoryDescription property.
        """
        self._category_description = value
    
    @property
    def child_category_ids(self,) -> Optional[List[str]]:
        """
        Gets the childCategoryIds property value. List of child ids of the category.
        Returns: Optional[List[str]]
        """
        return self._child_category_ids
    
    @child_category_ids.setter
    def child_category_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the childCategoryIds property value. List of child ids of the category.
        Args:
            value: Value to set for the childCategoryIds property.
        """
        self._child_category_ids = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationCategory and sets the default values.
        """
        super().__init__()
        # Description of the category header
        self._category_description: Optional[str] = None
        # List of child ids of the category.
        self._child_category_ids: Optional[List[str]] = None
        # Description of the item
        self._description: Optional[str] = None
        # Display name of the item
        self._display_name: Optional[str] = None
        # Help text of the item
        self._help_text: Optional[str] = None
        # Name of the item
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Parent id of the category.
        self._parent_category_id: Optional[str] = None
        # Supported platform types.
        self._platforms: Optional[device_management_configuration_platforms.DeviceManagementConfigurationPlatforms] = None
        # Root id of the category.
        self._root_category_id: Optional[str] = None
        # Supported setting types
        self._setting_usage: Optional[device_management_configuration_setting_usage.DeviceManagementConfigurationSettingUsage] = None
        # Describes which technology this setting can be deployed with
        self._technologies: Optional[device_management_configuration_technologies.DeviceManagementConfigurationTechnologies] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationCategory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationCategory()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the item
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the item
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the item
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the item
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
            "category_description": lambda n : setattr(self, 'category_description', n.get_str_value()),
            "child_category_ids": lambda n : setattr(self, 'child_category_ids', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "help_text": lambda n : setattr(self, 'help_text', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parent_category_id": lambda n : setattr(self, 'parent_category_id', n.get_str_value()),
            "platforms": lambda n : setattr(self, 'platforms', n.get_enum_value(device_management_configuration_platforms.DeviceManagementConfigurationPlatforms)),
            "root_category_id": lambda n : setattr(self, 'root_category_id', n.get_str_value()),
            "setting_usage": lambda n : setattr(self, 'setting_usage', n.get_enum_value(device_management_configuration_setting_usage.DeviceManagementConfigurationSettingUsage)),
            "technologies": lambda n : setattr(self, 'technologies', n.get_enum_value(device_management_configuration_technologies.DeviceManagementConfigurationTechnologies)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def help_text(self,) -> Optional[str]:
        """
        Gets the helpText property value. Help text of the item
        Returns: Optional[str]
        """
        return self._help_text
    
    @help_text.setter
    def help_text(self,value: Optional[str] = None) -> None:
        """
        Sets the helpText property value. Help text of the item
        Args:
            value: Value to set for the helpText property.
        """
        self._help_text = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the item
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the item
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def parent_category_id(self,) -> Optional[str]:
        """
        Gets the parentCategoryId property value. Parent id of the category.
        Returns: Optional[str]
        """
        return self._parent_category_id
    
    @parent_category_id.setter
    def parent_category_id(self,value: Optional[str] = None) -> None:
        """
        Sets the parentCategoryId property value. Parent id of the category.
        Args:
            value: Value to set for the parentCategoryId property.
        """
        self._parent_category_id = value
    
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
    def root_category_id(self,) -> Optional[str]:
        """
        Gets the rootCategoryId property value. Root id of the category.
        Returns: Optional[str]
        """
        return self._root_category_id
    
    @root_category_id.setter
    def root_category_id(self,value: Optional[str] = None) -> None:
        """
        Sets the rootCategoryId property value. Root id of the category.
        Args:
            value: Value to set for the rootCategoryId property.
        """
        self._root_category_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("categoryDescription", self.category_description)
        writer.write_collection_of_primitive_values("childCategoryIds", self.child_category_ids)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("helpText", self.help_text)
        writer.write_str_value("name", self.name)
        writer.write_str_value("parentCategoryId", self.parent_category_id)
        writer.write_enum_value("platforms", self.platforms)
        writer.write_str_value("rootCategoryId", self.root_category_id)
        writer.write_enum_value("settingUsage", self.setting_usage)
        writer.write_enum_value("technologies", self.technologies)
    
    @property
    def setting_usage(self,) -> Optional[device_management_configuration_setting_usage.DeviceManagementConfigurationSettingUsage]:
        """
        Gets the settingUsage property value. Supported setting types
        Returns: Optional[device_management_configuration_setting_usage.DeviceManagementConfigurationSettingUsage]
        """
        return self._setting_usage
    
    @setting_usage.setter
    def setting_usage(self,value: Optional[device_management_configuration_setting_usage.DeviceManagementConfigurationSettingUsage] = None) -> None:
        """
        Sets the settingUsage property value. Supported setting types
        Args:
            value: Value to set for the settingUsage property.
        """
        self._setting_usage = value
    
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
    

