from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_dependent_on, device_management_configuration_setting_definition, device_management_configuration_setting_depended_on_by, device_management_configuration_setting_value, device_management_configuration_setting_value_definition, device_management_configuration_simple_setting_collection_definition

from . import device_management_configuration_setting_definition

@dataclass
class DeviceManagementConfigurationSimpleSettingDefinition(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition):
    # Default setting value for this setting.
    default_value: Optional[device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue] = None
    # list of child settings that depend on this setting.
    depended_on_by: Optional[List[device_management_configuration_setting_depended_on_by.DeviceManagementConfigurationSettingDependedOnBy]] = None
    # list of parent settings this setting is dependent on.
    dependent_on: Optional[List[device_management_configuration_dependent_on.DeviceManagementConfigurationDependentOn]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Definition of the value for this setting.
    value_definition: Optional[device_management_configuration_setting_value_definition.DeviceManagementConfigurationSettingValueDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSimpleSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionDefinition":
                from . import device_management_configuration_simple_setting_collection_definition

                return device_management_configuration_simple_setting_collection_definition.DeviceManagementConfigurationSimpleSettingCollectionDefinition()
        return DeviceManagementConfigurationSimpleSettingDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_dependent_on, device_management_configuration_setting_definition, device_management_configuration_setting_depended_on_by, device_management_configuration_setting_value, device_management_configuration_setting_value_definition, device_management_configuration_simple_setting_collection_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_object_value(device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue)),
            "dependedOnBy": lambda n : setattr(self, 'depended_on_by', n.get_collection_of_object_values(device_management_configuration_setting_depended_on_by.DeviceManagementConfigurationSettingDependedOnBy)),
            "dependentOn": lambda n : setattr(self, 'dependent_on', n.get_collection_of_object_values(device_management_configuration_dependent_on.DeviceManagementConfigurationDependentOn)),
            "valueDefinition": lambda n : setattr(self, 'value_definition', n.get_object_value(device_management_configuration_setting_value_definition.DeviceManagementConfigurationSettingValueDefinition)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("defaultValue", self.default_value)
        writer.write_collection_of_object_values("dependedOnBy", self.depended_on_by)
        writer.write_collection_of_object_values("dependentOn", self.dependent_on)
        writer.write_object_value("valueDefinition", self.value_definition)
    

