from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_choice_setting_collection_instance_template import DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate
    from .device_management_configuration_choice_setting_instance_template import DeviceManagementConfigurationChoiceSettingInstanceTemplate
    from .device_management_configuration_group_setting_collection_instance_template import DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate
    from .device_management_configuration_group_setting_instance_template import DeviceManagementConfigurationGroupSettingInstanceTemplate
    from .device_management_configuration_simple_setting_collection_instance_template import DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate
    from .device_management_configuration_simple_setting_instance_template import DeviceManagementConfigurationSimpleSettingInstanceTemplate

@dataclass
class DeviceManagementConfigurationSettingInstanceTemplate(AdditionalDataHolder, BackedModel, Parsable):
    """
    Setting Instance Template
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates if a policy must specify this setting.
    is_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Setting Definition Id
    setting_definition_id: Optional[str] = None
    # Setting Instance Template Id
    setting_instance_template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingInstanceTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingInstanceTemplate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionInstanceTemplate".casefold():
            from .device_management_configuration_choice_setting_collection_instance_template import DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate

            return DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstanceTemplate".casefold():
            from .device_management_configuration_choice_setting_instance_template import DeviceManagementConfigurationChoiceSettingInstanceTemplate

            return DeviceManagementConfigurationChoiceSettingInstanceTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationGroupSettingCollectionInstanceTemplate".casefold():
            from .device_management_configuration_group_setting_collection_instance_template import DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate

            return DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationGroupSettingInstanceTemplate".casefold():
            from .device_management_configuration_group_setting_instance_template import DeviceManagementConfigurationGroupSettingInstanceTemplate

            return DeviceManagementConfigurationGroupSettingInstanceTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstanceTemplate".casefold():
            from .device_management_configuration_simple_setting_collection_instance_template import DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate

            return DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingInstanceTemplate".casefold():
            from .device_management_configuration_simple_setting_instance_template import DeviceManagementConfigurationSimpleSettingInstanceTemplate

            return DeviceManagementConfigurationSimpleSettingInstanceTemplate()
        return DeviceManagementConfigurationSettingInstanceTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_choice_setting_collection_instance_template import DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate
        from .device_management_configuration_choice_setting_instance_template import DeviceManagementConfigurationChoiceSettingInstanceTemplate
        from .device_management_configuration_group_setting_collection_instance_template import DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate
        from .device_management_configuration_group_setting_instance_template import DeviceManagementConfigurationGroupSettingInstanceTemplate
        from .device_management_configuration_simple_setting_collection_instance_template import DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate
        from .device_management_configuration_simple_setting_instance_template import DeviceManagementConfigurationSimpleSettingInstanceTemplate

        from .device_management_configuration_choice_setting_collection_instance_template import DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate
        from .device_management_configuration_choice_setting_instance_template import DeviceManagementConfigurationChoiceSettingInstanceTemplate
        from .device_management_configuration_group_setting_collection_instance_template import DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate
        from .device_management_configuration_group_setting_instance_template import DeviceManagementConfigurationGroupSettingInstanceTemplate
        from .device_management_configuration_simple_setting_collection_instance_template import DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate
        from .device_management_configuration_simple_setting_instance_template import DeviceManagementConfigurationSimpleSettingInstanceTemplate

        fields: Dict[str, Callable[[Any], None]] = {
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "settingDefinitionId": lambda n : setattr(self, 'setting_definition_id', n.get_str_value()),
            "settingInstanceTemplateId": lambda n : setattr(self, 'setting_instance_template_id', n.get_str_value()),
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
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("settingDefinitionId", self.setting_definition_id)
        writer.write_str_value("settingInstanceTemplateId", self.setting_instance_template_id)
        writer.write_additional_data_value(self.additional_data)
    

