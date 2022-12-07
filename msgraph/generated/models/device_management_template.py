from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_setting_instance = lazy_import('msgraph.generated.models.device_management_setting_instance')
device_management_template_setting_category = lazy_import('msgraph.generated.models.device_management_template_setting_category')
device_management_template_subtype = lazy_import('msgraph.generated.models.device_management_template_subtype')
device_management_template_type = lazy_import('msgraph.generated.models.device_management_template_type')
entity = lazy_import('msgraph.generated.models.entity')
policy_platform_type = lazy_import('msgraph.generated.models.policy_platform_type')

class DeviceManagementTemplate(entity.Entity):
    """
    Entity that represents a defined collection of device settings
    """
    @property
    def categories(self,) -> Optional[List[device_management_template_setting_category.DeviceManagementTemplateSettingCategory]]:
        """
        Gets the categories property value. Collection of setting categories within the template
        Returns: Optional[List[device_management_template_setting_category.DeviceManagementTemplateSettingCategory]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[device_management_template_setting_category.DeviceManagementTemplateSettingCategory]] = None) -> None:
        """
        Sets the categories property value. Collection of setting categories within the template
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementTemplate and sets the default values.
        """
        super().__init__()
        # Collection of setting categories within the template
        self._categories: Optional[List[device_management_template_setting_category.DeviceManagementTemplateSettingCategory]] = None
        # The template's description
        self._description: Optional[str] = None
        # The template's display name
        self._display_name: Optional[str] = None
        # Number of Intents created from this template.
        self._intent_count: Optional[int] = None
        # The template is deprecated or not. Intents cannot be created from a deprecated template.
        self._is_deprecated: Optional[bool] = None
        # Collection of templates this template can migrate to
        self._migratable_to: Optional[List[DeviceManagementTemplate]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Supported platform types for policies.
        self._platform_type: Optional[policy_platform_type.PolicyPlatformType] = None
        # When the template was published
        self._published_date_time: Optional[datetime] = None
        # Collection of all settings this template has
        self._settings: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None
        # Template subtype
        self._template_subtype: Optional[device_management_template_subtype.DeviceManagementTemplateSubtype] = None
        # Template type
        self._template_type: Optional[device_management_template_type.DeviceManagementTemplateType] = None
        # The template's version information
        self._version_info: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementTemplate()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The template's description
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The template's description
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The template's display name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The template's display name
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
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(device_management_template_setting_category.DeviceManagementTemplateSettingCategory)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "intent_count": lambda n : setattr(self, 'intent_count', n.get_int_value()),
            "is_deprecated": lambda n : setattr(self, 'is_deprecated', n.get_bool_value()),
            "migratable_to": lambda n : setattr(self, 'migratable_to', n.get_collection_of_object_values(DeviceManagementTemplate)),
            "platform_type": lambda n : setattr(self, 'platform_type', n.get_enum_value(policy_platform_type.PolicyPlatformType)),
            "published_date_time": lambda n : setattr(self, 'published_date_time', n.get_datetime_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(device_management_setting_instance.DeviceManagementSettingInstance)),
            "template_subtype": lambda n : setattr(self, 'template_subtype', n.get_enum_value(device_management_template_subtype.DeviceManagementTemplateSubtype)),
            "template_type": lambda n : setattr(self, 'template_type', n.get_enum_value(device_management_template_type.DeviceManagementTemplateType)),
            "version_info": lambda n : setattr(self, 'version_info', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def intent_count(self,) -> Optional[int]:
        """
        Gets the intentCount property value. Number of Intents created from this template.
        Returns: Optional[int]
        """
        return self._intent_count
    
    @intent_count.setter
    def intent_count(self,value: Optional[int] = None) -> None:
        """
        Sets the intentCount property value. Number of Intents created from this template.
        Args:
            value: Value to set for the intentCount property.
        """
        self._intent_count = value
    
    @property
    def is_deprecated(self,) -> Optional[bool]:
        """
        Gets the isDeprecated property value. The template is deprecated or not. Intents cannot be created from a deprecated template.
        Returns: Optional[bool]
        """
        return self._is_deprecated
    
    @is_deprecated.setter
    def is_deprecated(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDeprecated property value. The template is deprecated or not. Intents cannot be created from a deprecated template.
        Args:
            value: Value to set for the isDeprecated property.
        """
        self._is_deprecated = value
    
    @property
    def migratable_to(self,) -> Optional[List[DeviceManagementTemplate]]:
        """
        Gets the migratableTo property value. Collection of templates this template can migrate to
        Returns: Optional[List[DeviceManagementTemplate]]
        """
        return self._migratable_to
    
    @migratable_to.setter
    def migratable_to(self,value: Optional[List[DeviceManagementTemplate]] = None) -> None:
        """
        Sets the migratableTo property value. Collection of templates this template can migrate to
        Args:
            value: Value to set for the migratableTo property.
        """
        self._migratable_to = value
    
    @property
    def platform_type(self,) -> Optional[policy_platform_type.PolicyPlatformType]:
        """
        Gets the platformType property value. Supported platform types for policies.
        Returns: Optional[policy_platform_type.PolicyPlatformType]
        """
        return self._platform_type
    
    @platform_type.setter
    def platform_type(self,value: Optional[policy_platform_type.PolicyPlatformType] = None) -> None:
        """
        Sets the platformType property value. Supported platform types for policies.
        Args:
            value: Value to set for the platformType property.
        """
        self._platform_type = value
    
    @property
    def published_date_time(self,) -> Optional[datetime]:
        """
        Gets the publishedDateTime property value. When the template was published
        Returns: Optional[datetime]
        """
        return self._published_date_time
    
    @published_date_time.setter
    def published_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the publishedDateTime property value. When the template was published
        Args:
            value: Value to set for the publishedDateTime property.
        """
        self._published_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("categories", self.categories)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("intentCount", self.intent_count)
        writer.write_bool_value("isDeprecated", self.is_deprecated)
        writer.write_collection_of_object_values("migratableTo", self.migratable_to)
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_datetime_value("publishedDateTime", self.published_date_time)
        writer.write_collection_of_object_values("settings", self.settings)
        writer.write_enum_value("templateSubtype", self.template_subtype)
        writer.write_enum_value("templateType", self.template_type)
        writer.write_str_value("versionInfo", self.version_info)
    
    @property
    def settings(self,) -> Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]]:
        """
        Gets the settings property value. Collection of all settings this template has
        Returns: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None) -> None:
        """
        Sets the settings property value. Collection of all settings this template has
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def template_subtype(self,) -> Optional[device_management_template_subtype.DeviceManagementTemplateSubtype]:
        """
        Gets the templateSubtype property value. Template subtype
        Returns: Optional[device_management_template_subtype.DeviceManagementTemplateSubtype]
        """
        return self._template_subtype
    
    @template_subtype.setter
    def template_subtype(self,value: Optional[device_management_template_subtype.DeviceManagementTemplateSubtype] = None) -> None:
        """
        Sets the templateSubtype property value. Template subtype
        Args:
            value: Value to set for the templateSubtype property.
        """
        self._template_subtype = value
    
    @property
    def template_type(self,) -> Optional[device_management_template_type.DeviceManagementTemplateType]:
        """
        Gets the templateType property value. Template type
        Returns: Optional[device_management_template_type.DeviceManagementTemplateType]
        """
        return self._template_type
    
    @template_type.setter
    def template_type(self,value: Optional[device_management_template_type.DeviceManagementTemplateType] = None) -> None:
        """
        Sets the templateType property value. Template type
        Args:
            value: Value to set for the templateType property.
        """
        self._template_type = value
    
    @property
    def version_info(self,) -> Optional[str]:
        """
        Gets the versionInfo property value. The template's version information
        Returns: Optional[str]
        """
        return self._version_info
    
    @version_info.setter
    def version_info(self,value: Optional[str] = None) -> None:
        """
        Sets the versionInfo property value. The template's version information
        Args:
            value: Value to set for the versionInfo property.
        """
        self._version_info = value
    

