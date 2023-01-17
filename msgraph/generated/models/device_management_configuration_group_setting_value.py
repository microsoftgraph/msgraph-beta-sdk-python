from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_setting_instance = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance')
device_management_configuration_setting_value = lazy_import('msgraph.generated.models.device_management_configuration_setting_value')

class DeviceManagementConfigurationGroupSettingValue(device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue):
    """
    Value of the GroupSetting
    """
    @property
    def children(self,) -> Optional[List[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance]]:
        """
        Gets the children property value. Collection of child setting instances contained within this GroupSetting
        Returns: Optional[List[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance]]
        """
        return self._children
    
    @children.setter
    def children(self,value: Optional[List[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance]] = None) -> None:
        """
        Sets the children property value. Collection of child setting instances contained within this GroupSetting
        Args:
            value: Value to set for the children property.
        """
        self._children = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationGroupSettingValue and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationGroupSettingValue"
        # Collection of child setting instances contained within this GroupSetting
        self._children: Optional[List[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationGroupSettingValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationGroupSettingValue
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationGroupSettingValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance)),
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
    

