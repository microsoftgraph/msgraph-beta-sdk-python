from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue
    from .device_management_configuration_group_setting_value import DeviceManagementConfigurationGroupSettingValue
    from .device_management_configuration_integer_setting_value import DeviceManagementConfigurationIntegerSettingValue
    from .device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue
    from .device_management_configuration_secret_setting_value import DeviceManagementConfigurationSecretSettingValue
    from .device_management_configuration_setting_value_template_reference import DeviceManagementConfigurationSettingValueTemplateReference
    from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue
    from .device_management_configuration_string_setting_value import DeviceManagementConfigurationStringSettingValue

@dataclass
class DeviceManagementConfigurationSettingValue(AdditionalDataHolder, BackedModel, Parsable):
    """
    Setting value
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Setting value template reference
    setting_value_template_reference: Optional[DeviceManagementConfigurationSettingValueTemplateReference] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingValue
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingValue".casefold():
            from .device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue

            return DeviceManagementConfigurationChoiceSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationGroupSettingValue".casefold():
            from .device_management_configuration_group_setting_value import DeviceManagementConfigurationGroupSettingValue

            return DeviceManagementConfigurationGroupSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationIntegerSettingValue".casefold():
            from .device_management_configuration_integer_setting_value import DeviceManagementConfigurationIntegerSettingValue

            return DeviceManagementConfigurationIntegerSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationReferenceSettingValue".casefold():
            from .device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue

            return DeviceManagementConfigurationReferenceSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSecretSettingValue".casefold():
            from .device_management_configuration_secret_setting_value import DeviceManagementConfigurationSecretSettingValue

            return DeviceManagementConfigurationSecretSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingValue".casefold():
            from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue

            return DeviceManagementConfigurationSimpleSettingValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationStringSettingValue".casefold():
            from .device_management_configuration_string_setting_value import DeviceManagementConfigurationStringSettingValue

            return DeviceManagementConfigurationStringSettingValue()
        return DeviceManagementConfigurationSettingValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue
        from .device_management_configuration_group_setting_value import DeviceManagementConfigurationGroupSettingValue
        from .device_management_configuration_integer_setting_value import DeviceManagementConfigurationIntegerSettingValue
        from .device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue
        from .device_management_configuration_secret_setting_value import DeviceManagementConfigurationSecretSettingValue
        from .device_management_configuration_setting_value_template_reference import DeviceManagementConfigurationSettingValueTemplateReference
        from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue
        from .device_management_configuration_string_setting_value import DeviceManagementConfigurationStringSettingValue

        from .device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue
        from .device_management_configuration_group_setting_value import DeviceManagementConfigurationGroupSettingValue
        from .device_management_configuration_integer_setting_value import DeviceManagementConfigurationIntegerSettingValue
        from .device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue
        from .device_management_configuration_secret_setting_value import DeviceManagementConfigurationSecretSettingValue
        from .device_management_configuration_setting_value_template_reference import DeviceManagementConfigurationSettingValueTemplateReference
        from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue
        from .device_management_configuration_string_setting_value import DeviceManagementConfigurationStringSettingValue

        fields: Dict[str, Callable[[Any], None]] = {
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "settingValueTemplateReference": lambda n : setattr(self, 'setting_value_template_reference', n.get_object_value(DeviceManagementConfigurationSettingValueTemplateReference)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_object_value("settingValueTemplateReference", self.setting_value_template_reference)
        writer.write_additional_data_value(self.additional_data)
    

