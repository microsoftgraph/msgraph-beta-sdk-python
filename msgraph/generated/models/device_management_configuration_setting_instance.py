from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_choice_setting_collection_instance, device_management_configuration_choice_setting_instance, device_management_configuration_group_setting_collection_instance, device_management_configuration_group_setting_instance, device_management_configuration_setting_group_collection_instance, device_management_configuration_setting_group_instance, device_management_configuration_setting_instance_template_reference, device_management_configuration_simple_setting_collection_instance, device_management_configuration_simple_setting_instance

@dataclass
class DeviceManagementConfigurationSettingInstance(AdditionalDataHolder, Parsable):
    """
    Setting instance within policy
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Setting Definition Id
    setting_definition_id: Optional[str] = None
    # Setting Instance Template Reference
    setting_instance_template_reference: Optional[device_management_configuration_setting_instance_template_reference.DeviceManagementConfigurationSettingInstanceTemplateReference] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingInstance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionInstance".casefold():
            from . import device_management_configuration_choice_setting_collection_instance

            return device_management_configuration_choice_setting_collection_instance.DeviceManagementConfigurationChoiceSettingCollectionInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstance".casefold():
            from . import device_management_configuration_choice_setting_instance

            return device_management_configuration_choice_setting_instance.DeviceManagementConfigurationChoiceSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationGroupSettingCollectionInstance".casefold():
            from . import device_management_configuration_group_setting_collection_instance

            return device_management_configuration_group_setting_collection_instance.DeviceManagementConfigurationGroupSettingCollectionInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationGroupSettingInstance".casefold():
            from . import device_management_configuration_group_setting_instance

            return device_management_configuration_group_setting_instance.DeviceManagementConfigurationGroupSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSettingGroupCollectionInstance".casefold():
            from . import device_management_configuration_setting_group_collection_instance

            return device_management_configuration_setting_group_collection_instance.DeviceManagementConfigurationSettingGroupCollectionInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSettingGroupInstance".casefold():
            from . import device_management_configuration_setting_group_instance

            return device_management_configuration_setting_group_instance.DeviceManagementConfigurationSettingGroupInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstance".casefold():
            from . import device_management_configuration_simple_setting_collection_instance

            return device_management_configuration_simple_setting_collection_instance.DeviceManagementConfigurationSimpleSettingCollectionInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingInstance".casefold():
            from . import device_management_configuration_simple_setting_instance

            return device_management_configuration_simple_setting_instance.DeviceManagementConfigurationSimpleSettingInstance()
        return DeviceManagementConfigurationSettingInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_choice_setting_collection_instance, device_management_configuration_choice_setting_instance, device_management_configuration_group_setting_collection_instance, device_management_configuration_group_setting_instance, device_management_configuration_setting_group_collection_instance, device_management_configuration_setting_group_instance, device_management_configuration_setting_instance_template_reference, device_management_configuration_simple_setting_collection_instance, device_management_configuration_simple_setting_instance

        from . import device_management_configuration_choice_setting_collection_instance, device_management_configuration_choice_setting_instance, device_management_configuration_group_setting_collection_instance, device_management_configuration_group_setting_instance, device_management_configuration_setting_group_collection_instance, device_management_configuration_setting_group_instance, device_management_configuration_setting_instance_template_reference, device_management_configuration_simple_setting_collection_instance, device_management_configuration_simple_setting_instance

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "settingDefinitionId": lambda n : setattr(self, 'setting_definition_id', n.get_str_value()),
            "settingInstanceTemplateReference": lambda n : setattr(self, 'setting_instance_template_reference', n.get_object_value(device_management_configuration_setting_instance_template_reference.DeviceManagementConfigurationSettingInstanceTemplateReference)),
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
        writer.write_str_value("settingDefinitionId", self.setting_definition_id)
        writer.write_object_value("settingInstanceTemplateReference", self.setting_instance_template_reference)
        writer.write_additional_data_value(self.additional_data)
    

