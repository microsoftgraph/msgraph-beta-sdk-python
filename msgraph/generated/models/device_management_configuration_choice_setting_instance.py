from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_choice_setting_value, device_management_configuration_setting_instance

from . import device_management_configuration_setting_instance

@dataclass
class DeviceManagementConfigurationChoiceSettingInstance(device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance):
    odata_type = "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstance"
    # The choiceSettingValue property
    choice_setting_value: Optional[device_management_configuration_choice_setting_value.DeviceManagementConfigurationChoiceSettingValue] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationChoiceSettingInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingInstance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationChoiceSettingInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_choice_setting_value, device_management_configuration_setting_instance

        from . import device_management_configuration_choice_setting_value, device_management_configuration_setting_instance

        fields: Dict[str, Callable[[Any], None]] = {
            "choiceSettingValue": lambda n : setattr(self, 'choice_setting_value', n.get_object_value(device_management_configuration_choice_setting_value.DeviceManagementConfigurationChoiceSettingValue)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("choiceSettingValue", self.choice_setting_value)
    

