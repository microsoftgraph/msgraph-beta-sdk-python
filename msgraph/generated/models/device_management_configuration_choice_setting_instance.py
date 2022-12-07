from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_choice_setting_value = lazy_import('msgraph.generated.models.device_management_configuration_choice_setting_value')
device_management_configuration_setting_instance = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance')

class DeviceManagementConfigurationChoiceSettingInstance(device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance):
    @property
    def choice_setting_value(self,) -> Optional[device_management_configuration_choice_setting_value.DeviceManagementConfigurationChoiceSettingValue]:
        """
        Gets the choiceSettingValue property value. The choiceSettingValue property
        Returns: Optional[device_management_configuration_choice_setting_value.DeviceManagementConfigurationChoiceSettingValue]
        """
        return self._choice_setting_value
    
    @choice_setting_value.setter
    def choice_setting_value(self,value: Optional[device_management_configuration_choice_setting_value.DeviceManagementConfigurationChoiceSettingValue] = None) -> None:
        """
        Sets the choiceSettingValue property value. The choiceSettingValue property
        Args:
            value: Value to set for the choiceSettingValue property.
        """
        self._choice_setting_value = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationChoiceSettingInstance and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstance"
        # The choiceSettingValue property
        self._choice_setting_value: Optional[device_management_configuration_choice_setting_value.DeviceManagementConfigurationChoiceSettingValue] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationChoiceSettingInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationChoiceSettingInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "choice_setting_value": lambda n : setattr(self, 'choice_setting_value', n.get_object_value(device_management_configuration_choice_setting_value.DeviceManagementConfigurationChoiceSettingValue)),
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
        writer.write_object_value("choiceSettingValue", self.choice_setting_value)
    

