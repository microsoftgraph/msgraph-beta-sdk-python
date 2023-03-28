from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_integer_setting_value, device_management_configuration_reference_setting_value, device_management_configuration_secret_setting_value, device_management_configuration_setting_value, device_management_configuration_string_setting_value

from . import device_management_configuration_setting_value

class DeviceManagementConfigurationSimpleSettingValue(device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationSimpleSettingValue and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationSimpleSettingValue"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSimpleSettingValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingValue
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationIntegerSettingValue":
                from . import device_management_configuration_integer_setting_value

                return device_management_configuration_integer_setting_value.DeviceManagementConfigurationIntegerSettingValue()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationReferenceSettingValue":
                from . import device_management_configuration_reference_setting_value

                return device_management_configuration_reference_setting_value.DeviceManagementConfigurationReferenceSettingValue()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationSecretSettingValue":
                from . import device_management_configuration_secret_setting_value

                return device_management_configuration_secret_setting_value.DeviceManagementConfigurationSecretSettingValue()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationStringSettingValue":
                from . import device_management_configuration_string_setting_value

                return device_management_configuration_string_setting_value.DeviceManagementConfigurationStringSettingValue()
        return DeviceManagementConfigurationSimpleSettingValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
    

