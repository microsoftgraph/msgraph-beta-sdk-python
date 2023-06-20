from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_choice_setting_value, device_management_configuration_group_setting_value, device_management_configuration_integer_setting_value, device_management_configuration_reference_setting_value, device_management_configuration_secret_setting_value, device_management_configuration_setting_value_template_reference, device_management_configuration_simple_setting_value, device_management_configuration_string_setting_value

@dataclass
class DeviceManagementConfigurationSettingValue(AdditionalDataHolder, Parsable):
    """
    Setting value
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Setting value template reference
    setting_value_template_reference: Optional[device_management_configuration_setting_value_template_reference.DeviceManagementConfigurationSettingValueTemplateReference] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingValue
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingValue".casefold():
            from . import device_management_configuration_choice_setting_value

            return device_management_configuration_choice_setting_value.DeviceManagementConfigurationChoiceSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationGroupSettingValue".casefold():
            from . import device_management_configuration_group_setting_value

            return device_management_configuration_group_setting_value.DeviceManagementConfigurationGroupSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationIntegerSettingValue".casefold():
            from . import device_management_configuration_integer_setting_value

            return device_management_configuration_integer_setting_value.DeviceManagementConfigurationIntegerSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationReferenceSettingValue".casefold():
            from . import device_management_configuration_reference_setting_value

            return device_management_configuration_reference_setting_value.DeviceManagementConfigurationReferenceSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSecretSettingValue".casefold():
            from . import device_management_configuration_secret_setting_value

            return device_management_configuration_secret_setting_value.DeviceManagementConfigurationSecretSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingValue".casefold():
            from . import device_management_configuration_simple_setting_value

            return device_management_configuration_simple_setting_value.DeviceManagementConfigurationSimpleSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationStringSettingValue".casefold():
            from . import device_management_configuration_string_setting_value

            return device_management_configuration_string_setting_value.DeviceManagementConfigurationStringSettingValue()
        return DeviceManagementConfigurationSettingValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_choice_setting_value, device_management_configuration_group_setting_value, device_management_configuration_integer_setting_value, device_management_configuration_reference_setting_value, device_management_configuration_secret_setting_value, device_management_configuration_setting_value_template_reference, device_management_configuration_simple_setting_value, device_management_configuration_string_setting_value

        from . import device_management_configuration_choice_setting_value, device_management_configuration_group_setting_value, device_management_configuration_integer_setting_value, device_management_configuration_reference_setting_value, device_management_configuration_secret_setting_value, device_management_configuration_setting_value_template_reference, device_management_configuration_simple_setting_value, device_management_configuration_string_setting_value

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "settingValueTemplateReference": lambda n : setattr(self, 'setting_value_template_reference', n.get_object_value(device_management_configuration_setting_value_template_reference.DeviceManagementConfigurationSettingValueTemplateReference)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("settingValueTemplateReference", self.setting_value_template_reference)
        writer.write_additional_data_value(self.additional_data)
    

