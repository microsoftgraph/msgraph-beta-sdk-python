from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_intent_setting_category, device_management_setting_definition, device_management_template_setting_category, entity

from . import entity

@dataclass
class DeviceManagementSettingCategory(entity.Entity):
    """
    Entity representing a setting category
    """
    # The category name
    display_name: Optional[str] = None
    # The category contains top level required setting
    has_required_setting: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The setting definitions this category contains
    setting_definitions: Optional[List[device_management_setting_definition.DeviceManagementSettingDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingCategory
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntentSettingCategory".casefold():
            from . import device_management_intent_setting_category

            return device_management_intent_setting_category.DeviceManagementIntentSettingCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementTemplateSettingCategory".casefold():
            from . import device_management_template_setting_category

            return device_management_template_setting_category.DeviceManagementTemplateSettingCategory()
        return DeviceManagementSettingCategory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_intent_setting_category, device_management_setting_definition, device_management_template_setting_category, entity

        from . import device_management_intent_setting_category, device_management_setting_definition, device_management_template_setting_category, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "hasRequiredSetting": lambda n : setattr(self, 'has_required_setting', n.get_bool_value()),
            "settingDefinitions": lambda n : setattr(self, 'setting_definitions', n.get_collection_of_object_values(device_management_setting_definition.DeviceManagementSettingDefinition)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("hasRequiredSetting", self.has_required_setting)
        writer.write_collection_of_object_values("settingDefinitions", self.setting_definitions)
    

