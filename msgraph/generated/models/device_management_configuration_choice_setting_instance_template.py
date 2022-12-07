from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_choice_setting_value_template = lazy_import('msgraph.generated.models.device_management_configuration_choice_setting_value_template')
device_management_configuration_setting_instance_template = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance_template')

class DeviceManagementConfigurationChoiceSettingInstanceTemplate(device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate):
    @property
    def choice_setting_value_template(self,) -> Optional[device_management_configuration_choice_setting_value_template.DeviceManagementConfigurationChoiceSettingValueTemplate]:
        """
        Gets the choiceSettingValueTemplate property value. Choice Setting Value Template
        Returns: Optional[device_management_configuration_choice_setting_value_template.DeviceManagementConfigurationChoiceSettingValueTemplate]
        """
        return self._choice_setting_value_template
    
    @choice_setting_value_template.setter
    def choice_setting_value_template(self,value: Optional[device_management_configuration_choice_setting_value_template.DeviceManagementConfigurationChoiceSettingValueTemplate] = None) -> None:
        """
        Sets the choiceSettingValueTemplate property value. Choice Setting Value Template
        Args:
            value: Value to set for the choiceSettingValueTemplate property.
        """
        self._choice_setting_value_template = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationChoiceSettingInstanceTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstanceTemplate"
        # Choice Setting Value Template
        self._choice_setting_value_template: Optional[device_management_configuration_choice_setting_value_template.DeviceManagementConfigurationChoiceSettingValueTemplate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationChoiceSettingInstanceTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingInstanceTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationChoiceSettingInstanceTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "choice_setting_value_template": lambda n : setattr(self, 'choice_setting_value_template', n.get_object_value(device_management_configuration_choice_setting_value_template.DeviceManagementConfigurationChoiceSettingValueTemplate)),
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
        writer.write_object_value("choiceSettingValueTemplate", self.choice_setting_value_template)
    

