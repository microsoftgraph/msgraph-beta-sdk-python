from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_choice_setting_collection_definition, device_management_configuration_choice_setting_definition, device_management_configuration_control_type, device_management_configuration_redirect_setting_definition, device_management_configuration_referred_setting_information, device_management_configuration_setting_access_types, device_management_configuration_setting_applicability, device_management_configuration_setting_group_collection_definition, device_management_configuration_setting_group_definition, device_management_configuration_setting_occurrence, device_management_configuration_setting_usage, device_management_configuration_setting_visibility, device_management_configuration_simple_setting_collection_definition, device_management_configuration_simple_setting_definition, entity

from . import entity

@dataclass
class DeviceManagementConfigurationSettingDefinition(entity.Entity):
    # The accessTypes property
    access_types: Optional[device_management_configuration_setting_access_types.DeviceManagementConfigurationSettingAccessTypes] = None
    # Details which device setting is applicable on. Supports: $filters.
    applicability: Optional[device_management_configuration_setting_applicability.DeviceManagementConfigurationSettingApplicability] = None
    # Base CSP Path
    base_uri: Optional[str] = None
    # Specify category in which the setting is under. Support $filters.
    category_id: Optional[str] = None
    # Description of the setting.
    description: Optional[str] = None
    # Name of the setting. For example: Allow Toast.
    display_name: Optional[str] = None
    # Help text of the setting. Give more details of the setting.
    help_text: Optional[str] = None
    # List of links more info for the setting can be found at.
    info_urls: Optional[List[str]] = None
    # Tokens which to search settings on
    keywords: Optional[List[str]] = None
    # Name of the item
    name: Optional[str] = None
    # Indicates whether the setting is required or not
    occurrence: Optional[device_management_configuration_setting_occurrence.DeviceManagementConfigurationSettingOccurrence] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Offset CSP Path from Base
    offset_uri: Optional[str] = None
    # List of referred setting information.
    referred_setting_information_list: Optional[List[device_management_configuration_referred_setting_information.DeviceManagementConfigurationReferredSettingInformation]] = None
    # Root setting definition id if the setting is a child setting.
    root_definition_id: Optional[str] = None
    # Supported setting types
    setting_usage: Optional[device_management_configuration_setting_usage.DeviceManagementConfigurationSettingUsage] = None
    # Setting control type representation in the UX
    ux_behavior: Optional[device_management_configuration_control_type.DeviceManagementConfigurationControlType] = None
    # Item Version
    version: Optional[str] = None
    # Supported setting types
    visibility: Optional[device_management_configuration_setting_visibility.DeviceManagementConfigurationSettingVisibility] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionDefinition".casefold():
            from . import device_management_configuration_choice_setting_collection_definition

            return device_management_configuration_choice_setting_collection_definition.DeviceManagementConfigurationChoiceSettingCollectionDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingDefinition".casefold():
            from . import device_management_configuration_choice_setting_definition

            return device_management_configuration_choice_setting_definition.DeviceManagementConfigurationChoiceSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationRedirectSettingDefinition".casefold():
            from . import device_management_configuration_redirect_setting_definition

            return device_management_configuration_redirect_setting_definition.DeviceManagementConfigurationRedirectSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSettingGroupCollectionDefinition".casefold():
            from . import device_management_configuration_setting_group_collection_definition

            return device_management_configuration_setting_group_collection_definition.DeviceManagementConfigurationSettingGroupCollectionDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSettingGroupDefinition".casefold():
            from . import device_management_configuration_setting_group_definition

            return device_management_configuration_setting_group_definition.DeviceManagementConfigurationSettingGroupDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionDefinition".casefold():
            from . import device_management_configuration_simple_setting_collection_definition

            return device_management_configuration_simple_setting_collection_definition.DeviceManagementConfigurationSimpleSettingCollectionDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingDefinition".casefold():
            from . import device_management_configuration_simple_setting_definition

            return device_management_configuration_simple_setting_definition.DeviceManagementConfigurationSimpleSettingDefinition()
        return DeviceManagementConfigurationSettingDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_choice_setting_collection_definition, device_management_configuration_choice_setting_definition, device_management_configuration_control_type, device_management_configuration_redirect_setting_definition, device_management_configuration_referred_setting_information, device_management_configuration_setting_access_types, device_management_configuration_setting_applicability, device_management_configuration_setting_group_collection_definition, device_management_configuration_setting_group_definition, device_management_configuration_setting_occurrence, device_management_configuration_setting_usage, device_management_configuration_setting_visibility, device_management_configuration_simple_setting_collection_definition, device_management_configuration_simple_setting_definition, entity

        from . import device_management_configuration_choice_setting_collection_definition, device_management_configuration_choice_setting_definition, device_management_configuration_control_type, device_management_configuration_redirect_setting_definition, device_management_configuration_referred_setting_information, device_management_configuration_setting_access_types, device_management_configuration_setting_applicability, device_management_configuration_setting_group_collection_definition, device_management_configuration_setting_group_definition, device_management_configuration_setting_occurrence, device_management_configuration_setting_usage, device_management_configuration_setting_visibility, device_management_configuration_simple_setting_collection_definition, device_management_configuration_simple_setting_definition, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessTypes": lambda n : setattr(self, 'access_types', n.get_enum_value(device_management_configuration_setting_access_types.DeviceManagementConfigurationSettingAccessTypes)),
            "applicability": lambda n : setattr(self, 'applicability', n.get_object_value(device_management_configuration_setting_applicability.DeviceManagementConfigurationSettingApplicability)),
            "baseUri": lambda n : setattr(self, 'base_uri', n.get_str_value()),
            "categoryId": lambda n : setattr(self, 'category_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "helpText": lambda n : setattr(self, 'help_text', n.get_str_value()),
            "infoUrls": lambda n : setattr(self, 'info_urls', n.get_collection_of_primitive_values(str)),
            "keywords": lambda n : setattr(self, 'keywords', n.get_collection_of_primitive_values(str)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "occurrence": lambda n : setattr(self, 'occurrence', n.get_object_value(device_management_configuration_setting_occurrence.DeviceManagementConfigurationSettingOccurrence)),
            "offsetUri": lambda n : setattr(self, 'offset_uri', n.get_str_value()),
            "referredSettingInformationList": lambda n : setattr(self, 'referred_setting_information_list', n.get_collection_of_object_values(device_management_configuration_referred_setting_information.DeviceManagementConfigurationReferredSettingInformation)),
            "rootDefinitionId": lambda n : setattr(self, 'root_definition_id', n.get_str_value()),
            "settingUsage": lambda n : setattr(self, 'setting_usage', n.get_enum_value(device_management_configuration_setting_usage.DeviceManagementConfigurationSettingUsage)),
            "uxBehavior": lambda n : setattr(self, 'ux_behavior', n.get_enum_value(device_management_configuration_control_type.DeviceManagementConfigurationControlType)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_enum_value(device_management_configuration_setting_visibility.DeviceManagementConfigurationSettingVisibility)),
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
        writer.write_enum_value("accessTypes", self.access_types)
        writer.write_object_value("applicability", self.applicability)
        writer.write_str_value("baseUri", self.base_uri)
        writer.write_str_value("categoryId", self.category_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("helpText", self.help_text)
        writer.write_collection_of_primitive_values("infoUrls", self.info_urls)
        writer.write_collection_of_primitive_values("keywords", self.keywords)
        writer.write_str_value("name", self.name)
        writer.write_object_value("occurrence", self.occurrence)
        writer.write_str_value("offsetUri", self.offset_uri)
        writer.write_collection_of_object_values("referredSettingInformationList", self.referred_setting_information_list)
        writer.write_str_value("rootDefinitionId", self.root_definition_id)
        writer.write_enum_value("settingUsage", self.setting_usage)
        writer.write_enum_value("uxBehavior", self.ux_behavior)
        writer.write_str_value("version", self.version)
        writer.write_enum_value("visibility", self.visibility)
    

