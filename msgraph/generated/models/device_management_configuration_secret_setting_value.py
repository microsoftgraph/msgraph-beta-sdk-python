from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_secret_setting_value_state = lazy_import('msgraph.generated.models.device_management_configuration_secret_setting_value_state')
device_management_configuration_simple_setting_value = lazy_import('msgraph.generated.models.device_management_configuration_simple_setting_value')

class DeviceManagementConfigurationSecretSettingValue(device_management_configuration_simple_setting_value.DeviceManagementConfigurationSimpleSettingValue):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationSecretSettingValue and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationSecretSettingValue"
        # Value of the secret setting.
        self._value: Optional[str] = None
        # type tracking the encryption state of a secret setting value
        self._value_state: Optional[device_management_configuration_secret_setting_value_state.DeviceManagementConfigurationSecretSettingValueState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSecretSettingValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSecretSettingValue
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSecretSettingValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
            "value_state": lambda n : setattr(self, 'value_state', n.get_enum_value(device_management_configuration_secret_setting_value_state.DeviceManagementConfigurationSecretSettingValueState)),
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
        writer.write_str_value("value", self.value)
        writer.write_enum_value("valueState", self.value_state)
    
    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. Value of the secret setting.
        Returns: Optional[str]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. Value of the secret setting.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    
    @property
    def value_state(self,) -> Optional[device_management_configuration_secret_setting_value_state.DeviceManagementConfigurationSecretSettingValueState]:
        """
        Gets the valueState property value. type tracking the encryption state of a secret setting value
        Returns: Optional[device_management_configuration_secret_setting_value_state.DeviceManagementConfigurationSecretSettingValueState]
        """
        return self._value_state
    
    @value_state.setter
    def value_state(self,value: Optional[device_management_configuration_secret_setting_value_state.DeviceManagementConfigurationSecretSettingValueState] = None) -> None:
        """
        Sets the valueState property value. type tracking the encryption state of a secret setting value
        Args:
            value: Value to set for the valueState property.
        """
        self._value_state = value
    

