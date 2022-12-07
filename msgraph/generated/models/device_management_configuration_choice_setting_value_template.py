from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_choice_setting_value_default_template = lazy_import('msgraph.generated.models.device_management_configuration_choice_setting_value_default_template')
device_management_configuration_choice_setting_value_definition_template = lazy_import('msgraph.generated.models.device_management_configuration_choice_setting_value_definition_template')

class DeviceManagementConfigurationChoiceSettingValueTemplate(AdditionalDataHolder, Parsable):
    """
    Choice Setting Value Template
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationChoiceSettingValueTemplate and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Choice Setting Value Default Template.
        self._default_value: Optional[device_management_configuration_choice_setting_value_default_template.DeviceManagementConfigurationChoiceSettingValueDefaultTemplate] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Recommended definition override.
        self._recommended_value_definition: Optional[device_management_configuration_choice_setting_value_definition_template.DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate] = None
        # Required definition override.
        self._required_value_definition: Optional[device_management_configuration_choice_setting_value_definition_template.DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate] = None
        # Setting Value Template Id
        self._setting_value_template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationChoiceSettingValueTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingValueTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationChoiceSettingValueTemplate()
    
    @property
    def default_value(self,) -> Optional[device_management_configuration_choice_setting_value_default_template.DeviceManagementConfigurationChoiceSettingValueDefaultTemplate]:
        """
        Gets the defaultValue property value. Choice Setting Value Default Template.
        Returns: Optional[device_management_configuration_choice_setting_value_default_template.DeviceManagementConfigurationChoiceSettingValueDefaultTemplate]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[device_management_configuration_choice_setting_value_default_template.DeviceManagementConfigurationChoiceSettingValueDefaultTemplate] = None) -> None:
        """
        Sets the defaultValue property value. Choice Setting Value Default Template.
        Args:
            value: Value to set for the defaultValue property.
        """
        self._default_value = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_value": lambda n : setattr(self, 'default_value', n.get_object_value(device_management_configuration_choice_setting_value_default_template.DeviceManagementConfigurationChoiceSettingValueDefaultTemplate)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommended_value_definition": lambda n : setattr(self, 'recommended_value_definition', n.get_object_value(device_management_configuration_choice_setting_value_definition_template.DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate)),
            "required_value_definition": lambda n : setattr(self, 'required_value_definition', n.get_object_value(device_management_configuration_choice_setting_value_definition_template.DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate)),
            "setting_value_template_id": lambda n : setattr(self, 'setting_value_template_id', n.get_str_value()),
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def recommended_value_definition(self,) -> Optional[device_management_configuration_choice_setting_value_definition_template.DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate]:
        """
        Gets the recommendedValueDefinition property value. Recommended definition override.
        Returns: Optional[device_management_configuration_choice_setting_value_definition_template.DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate]
        """
        return self._recommended_value_definition
    
    @recommended_value_definition.setter
    def recommended_value_definition(self,value: Optional[device_management_configuration_choice_setting_value_definition_template.DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate] = None) -> None:
        """
        Sets the recommendedValueDefinition property value. Recommended definition override.
        Args:
            value: Value to set for the recommendedValueDefinition property.
        """
        self._recommended_value_definition = value
    
    @property
    def required_value_definition(self,) -> Optional[device_management_configuration_choice_setting_value_definition_template.DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate]:
        """
        Gets the requiredValueDefinition property value. Required definition override.
        Returns: Optional[device_management_configuration_choice_setting_value_definition_template.DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate]
        """
        return self._required_value_definition
    
    @required_value_definition.setter
    def required_value_definition(self,value: Optional[device_management_configuration_choice_setting_value_definition_template.DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate] = None) -> None:
        """
        Sets the requiredValueDefinition property value. Required definition override.
        Args:
            value: Value to set for the requiredValueDefinition property.
        """
        self._required_value_definition = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("defaultValue", self.default_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("recommendedValueDefinition", self.recommended_value_definition)
        writer.write_object_value("requiredValueDefinition", self.required_value_definition)
        writer.write_str_value("settingValueTemplateId", self.setting_value_template_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def setting_value_template_id(self,) -> Optional[str]:
        """
        Gets the settingValueTemplateId property value. Setting Value Template Id
        Returns: Optional[str]
        """
        return self._setting_value_template_id
    
    @setting_value_template_id.setter
    def setting_value_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the settingValueTemplateId property value. Setting Value Template Id
        Args:
            value: Value to set for the settingValueTemplateId property.
        """
        self._setting_value_template_id = value
    

