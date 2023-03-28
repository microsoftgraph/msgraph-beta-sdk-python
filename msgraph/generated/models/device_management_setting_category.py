from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_intent_setting_category, device_management_setting_definition, device_management_template_setting_category, entity

from . import entity

class DeviceManagementSettingCategory(entity.Entity):
    """
    Entity representing a setting category
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementSettingCategory and sets the default values.
        """
        super().__init__()
        # The category name
        self._display_name: Optional[str] = None
        # The category contains top level required setting
        self._has_required_setting: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The setting definitions this category contains
        self._setting_definitions: Optional[List[device_management_setting_definition.DeviceManagementSettingDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingCategory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceManagementIntentSettingCategory":
                from . import device_management_intent_setting_category

                return device_management_intent_setting_category.DeviceManagementIntentSettingCategory()
            if mapping_value == "#microsoft.graph.deviceManagementTemplateSettingCategory":
                from . import device_management_template_setting_category

                return device_management_template_setting_category.DeviceManagementTemplateSettingCategory()
        return DeviceManagementSettingCategory()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The category name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The category name
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_intent_setting_category, device_management_setting_definition, device_management_template_setting_category, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "hasRequiredSetting": lambda n : setattr(self, 'has_required_setting', n.get_bool_value()),
            "settingDefinitions": lambda n : setattr(self, 'setting_definitions', n.get_collection_of_object_values(device_management_setting_definition.DeviceManagementSettingDefinition)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_required_setting(self,) -> Optional[bool]:
        """
        Gets the hasRequiredSetting property value. The category contains top level required setting
        Returns: Optional[bool]
        """
        return self._has_required_setting
    
    @has_required_setting.setter
    def has_required_setting(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasRequiredSetting property value. The category contains top level required setting
        Args:
            value: Value to set for the has_required_setting property.
        """
        self._has_required_setting = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("hasRequiredSetting", self.has_required_setting)
        writer.write_collection_of_object_values("settingDefinitions", self.setting_definitions)
    
    @property
    def setting_definitions(self,) -> Optional[List[device_management_setting_definition.DeviceManagementSettingDefinition]]:
        """
        Gets the settingDefinitions property value. The setting definitions this category contains
        Returns: Optional[List[device_management_setting_definition.DeviceManagementSettingDefinition]]
        """
        return self._setting_definitions
    
    @setting_definitions.setter
    def setting_definitions(self,value: Optional[List[device_management_setting_definition.DeviceManagementSettingDefinition]] = None) -> None:
        """
        Sets the settingDefinitions property value. The setting definitions this category contains
        Args:
            value: Value to set for the setting_definitions property.
        """
        self._setting_definitions = value
    

