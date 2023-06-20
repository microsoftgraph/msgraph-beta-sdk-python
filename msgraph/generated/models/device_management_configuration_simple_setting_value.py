from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_integer_setting_value, device_management_configuration_reference_setting_value, device_management_configuration_secret_setting_value, device_management_configuration_setting_value, device_management_configuration_string_setting_value

from . import device_management_configuration_setting_value

@dataclass
class DeviceManagementConfigurationSimpleSettingValue(device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue):
    odata_type = "#microsoft.graph.deviceManagementConfigurationSimpleSettingValue"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSimpleSettingValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingValue
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationIntegerSettingValue".casefold():
            from . import device_management_configuration_integer_setting_value

            return device_management_configuration_integer_setting_value.DeviceManagementConfigurationIntegerSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationReferenceSettingValue".casefold():
            from . import device_management_configuration_reference_setting_value

            return device_management_configuration_reference_setting_value.DeviceManagementConfigurationReferenceSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSecretSettingValue".casefold():
            from . import device_management_configuration_secret_setting_value

            return device_management_configuration_secret_setting_value.DeviceManagementConfigurationSecretSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationStringSettingValue".casefold():
            from . import device_management_configuration_string_setting_value

            return device_management_configuration_string_setting_value.DeviceManagementConfigurationStringSettingValue()
        return DeviceManagementConfigurationSimpleSettingValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_integer_setting_value, device_management_configuration_reference_setting_value, device_management_configuration_secret_setting_value, device_management_configuration_setting_value, device_management_configuration_string_setting_value

        from . import device_management_configuration_integer_setting_value, device_management_configuration_reference_setting_value, device_management_configuration_secret_setting_value, device_management_configuration_setting_value, device_management_configuration_string_setting_value

        fields: Dict[str, Callable[[Any], None]] = {
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
    

