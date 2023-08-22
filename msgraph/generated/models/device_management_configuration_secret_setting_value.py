from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_secret_setting_value_state import DeviceManagementConfigurationSecretSettingValueState
    from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue

from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue

@dataclass
class DeviceManagementConfigurationSecretSettingValue(DeviceManagementConfigurationSimpleSettingValue):
    """
    Graph model for a secret setting value
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationSecretSettingValue"
    # Value of the secret setting.
    value: Optional[str] = None
    # type tracking the encryption state of a secret setting value
    value_state: Optional[DeviceManagementConfigurationSecretSettingValueState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSecretSettingValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSecretSettingValue
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationSecretSettingValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_secret_setting_value_state import DeviceManagementConfigurationSecretSettingValueState
        from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue

        from .device_management_configuration_secret_setting_value_state import DeviceManagementConfigurationSecretSettingValueState
        from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
            "valueState": lambda n : setattr(self, 'value_state', n.get_enum_value(DeviceManagementConfigurationSecretSettingValueState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("value", self.value)
        writer.write_enum_value("valueState", self.value_state)
    

