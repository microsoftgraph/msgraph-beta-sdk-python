from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_choice_setting_collection_instance, device_management_configuration_choice_setting_instance, device_management_configuration_group_setting_collection_instance, device_management_configuration_group_setting_instance, device_management_configuration_setting_group_collection_instance, device_management_configuration_setting_group_instance, device_management_configuration_setting_instance_template_reference, device_management_configuration_simple_setting_collection_instance, device_management_configuration_simple_setting_instance

class DeviceManagementConfigurationSettingInstance(AdditionalDataHolder, Parsable):
    """
    Setting instance within policy
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationSettingInstance and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Setting Definition Id
        self._setting_definition_id: Optional[str] = None
        # Setting Instance Template Reference
        self._setting_instance_template_reference: Optional[device_management_configuration_setting_instance_template_reference.DeviceManagementConfigurationSettingInstanceTemplateReference] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionInstance":
                from . import device_management_configuration_choice_setting_collection_instance

                return device_management_configuration_choice_setting_collection_instance.DeviceManagementConfigurationChoiceSettingCollectionInstance()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstance":
                from . import device_management_configuration_choice_setting_instance

                return device_management_configuration_choice_setting_instance.DeviceManagementConfigurationChoiceSettingInstance()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationGroupSettingCollectionInstance":
                from . import device_management_configuration_group_setting_collection_instance

                return device_management_configuration_group_setting_collection_instance.DeviceManagementConfigurationGroupSettingCollectionInstance()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationGroupSettingInstance":
                from . import device_management_configuration_group_setting_instance

                return device_management_configuration_group_setting_instance.DeviceManagementConfigurationGroupSettingInstance()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationSettingGroupCollectionInstance":
                from . import device_management_configuration_setting_group_collection_instance

                return device_management_configuration_setting_group_collection_instance.DeviceManagementConfigurationSettingGroupCollectionInstance()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationSettingGroupInstance":
                from . import device_management_configuration_setting_group_instance

                return device_management_configuration_setting_group_instance.DeviceManagementConfigurationSettingGroupInstance()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstance":
                from . import device_management_configuration_simple_setting_collection_instance

                return device_management_configuration_simple_setting_collection_instance.DeviceManagementConfigurationSimpleSettingCollectionInstance()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationSimpleSettingInstance":
                from . import device_management_configuration_simple_setting_instance

                return device_management_configuration_simple_setting_instance.DeviceManagementConfigurationSimpleSettingInstance()
        return DeviceManagementConfigurationSettingInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_choice_setting_collection_instance, device_management_configuration_choice_setting_instance, device_management_configuration_group_setting_collection_instance, device_management_configuration_group_setting_instance, device_management_configuration_setting_group_collection_instance, device_management_configuration_setting_group_instance, device_management_configuration_setting_instance_template_reference, device_management_configuration_simple_setting_collection_instance, device_management_configuration_simple_setting_instance

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "settingDefinitionId": lambda n : setattr(self, 'setting_definition_id', n.get_str_value()),
            "settingInstanceTemplateReference": lambda n : setattr(self, 'setting_instance_template_reference', n.get_object_value(device_management_configuration_setting_instance_template_reference.DeviceManagementConfigurationSettingInstanceTemplateReference)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("settingDefinitionId", self.setting_definition_id)
        writer.write_object_value("settingInstanceTemplateReference", self.setting_instance_template_reference)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def setting_definition_id(self,) -> Optional[str]:
        """
        Gets the settingDefinitionId property value. Setting Definition Id
        Returns: Optional[str]
        """
        return self._setting_definition_id
    
    @setting_definition_id.setter
    def setting_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the settingDefinitionId property value. Setting Definition Id
        Args:
            value: Value to set for the setting_definition_id property.
        """
        self._setting_definition_id = value
    
    @property
    def setting_instance_template_reference(self,) -> Optional[device_management_configuration_setting_instance_template_reference.DeviceManagementConfigurationSettingInstanceTemplateReference]:
        """
        Gets the settingInstanceTemplateReference property value. Setting Instance Template Reference
        Returns: Optional[device_management_configuration_setting_instance_template_reference.DeviceManagementConfigurationSettingInstanceTemplateReference]
        """
        return self._setting_instance_template_reference
    
    @setting_instance_template_reference.setter
    def setting_instance_template_reference(self,value: Optional[device_management_configuration_setting_instance_template_reference.DeviceManagementConfigurationSettingInstanceTemplateReference] = None) -> None:
        """
        Sets the settingInstanceTemplateReference property value. Setting Instance Template Reference
        Args:
            value: Value to set for the setting_instance_template_reference property.
        """
        self._setting_instance_template_reference = value
    

