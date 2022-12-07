from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_setting_instance = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance')
device_management_configuration_setting_value = lazy_import('msgraph.generated.models.device_management_configuration_setting_value')

class DeviceManagementConfigurationChoiceSettingValue(device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue):
    @property
    def children(self,) -> Optional[List[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance]]:
        """
        Gets the children property value. Child settings.
        Returns: Optional[List[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance]]
        """
        return self._children
    
    @children.setter
    def children(self,value: Optional[List[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance]] = None) -> None:
        """
        Sets the children property value. Child settings.
        Args:
            value: Value to set for the children property.
        """
        self._children = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationChoiceSettingValue and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationChoiceSettingValue"
        # Child settings.
        self._children: Optional[List[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance]] = None
        # Choice setting value: an OptionDefinition ItemId.
        self._value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationChoiceSettingValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingValue
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationChoiceSettingValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance)),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_collection_of_object_values("children", self.children)
        writer.write_str_value("value", self.value)
    
    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. Choice setting value: an OptionDefinition ItemId.
        Returns: Optional[str]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. Choice setting value: an OptionDefinition ItemId.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

