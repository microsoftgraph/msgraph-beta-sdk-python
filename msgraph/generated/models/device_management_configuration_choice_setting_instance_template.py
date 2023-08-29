from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_choice_setting_value_template import DeviceManagementConfigurationChoiceSettingValueTemplate
    from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

@dataclass
class DeviceManagementConfigurationChoiceSettingInstanceTemplate(DeviceManagementConfigurationSettingInstanceTemplate):
    """
    Choice Setting Instance Template
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstanceTemplate"
    # Choice Setting Value Template
    choice_setting_value_template: Optional[DeviceManagementConfigurationChoiceSettingValueTemplate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationChoiceSettingInstanceTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingInstanceTemplate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationChoiceSettingInstanceTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_choice_setting_value_template import DeviceManagementConfigurationChoiceSettingValueTemplate
        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

        from .device_management_configuration_choice_setting_value_template import DeviceManagementConfigurationChoiceSettingValueTemplate
        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

        fields: Dict[str, Callable[[Any], None]] = {
            "choiceSettingValueTemplate": lambda n : setattr(self, 'choice_setting_value_template', n.get_object_value(DeviceManagementConfigurationChoiceSettingValueTemplate)),
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
        writer.write_object_value("choiceSettingValueTemplate", self.choice_setting_value_template)
    

