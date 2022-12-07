from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_group_setting_value = lazy_import('msgraph.generated.models.device_management_configuration_group_setting_value')
device_management_configuration_setting_instance = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance')

class DeviceManagementConfigurationGroupSettingCollectionInstance(device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationGroupSettingCollectionInstance and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationGroupSettingCollectionInstance"
        # A collection of GroupSetting values
        self._group_setting_collection_value: Optional[List[device_management_configuration_group_setting_value.DeviceManagementConfigurationGroupSettingValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationGroupSettingCollectionInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationGroupSettingCollectionInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationGroupSettingCollectionInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "group_setting_collection_value": lambda n : setattr(self, 'group_setting_collection_value', n.get_collection_of_object_values(device_management_configuration_group_setting_value.DeviceManagementConfigurationGroupSettingValue)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_setting_collection_value(self,) -> Optional[List[device_management_configuration_group_setting_value.DeviceManagementConfigurationGroupSettingValue]]:
        """
        Gets the groupSettingCollectionValue property value. A collection of GroupSetting values
        Returns: Optional[List[device_management_configuration_group_setting_value.DeviceManagementConfigurationGroupSettingValue]]
        """
        return self._group_setting_collection_value
    
    @group_setting_collection_value.setter
    def group_setting_collection_value(self,value: Optional[List[device_management_configuration_group_setting_value.DeviceManagementConfigurationGroupSettingValue]] = None) -> None:
        """
        Sets the groupSettingCollectionValue property value. A collection of GroupSetting values
        Args:
            value: Value to set for the groupSettingCollectionValue property.
        """
        self._group_setting_collection_value = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("groupSettingCollectionValue", self.group_setting_collection_value)
    

