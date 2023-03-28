from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_setting_instance, device_management_configuration_simple_setting_value

from . import device_management_configuration_setting_instance

class DeviceManagementConfigurationSimpleSettingCollectionInstance(device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationSimpleSettingCollectionInstance and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstance"
        # Simple setting collection instance value
        self._simple_setting_collection_value: Optional[List[device_management_configuration_simple_setting_value.DeviceManagementConfigurationSimpleSettingValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSimpleSettingCollectionInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingCollectionInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSimpleSettingCollectionInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_setting_instance, device_management_configuration_simple_setting_value

        fields: Dict[str, Callable[[Any], None]] = {
            "simpleSettingCollectionValue": lambda n : setattr(self, 'simple_setting_collection_value', n.get_collection_of_object_values(device_management_configuration_simple_setting_value.DeviceManagementConfigurationSimpleSettingValue)),
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
        writer.write_collection_of_object_values("simpleSettingCollectionValue", self.simple_setting_collection_value)
    
    @property
    def simple_setting_collection_value(self,) -> Optional[List[device_management_configuration_simple_setting_value.DeviceManagementConfigurationSimpleSettingValue]]:
        """
        Gets the simpleSettingCollectionValue property value. Simple setting collection instance value
        Returns: Optional[List[device_management_configuration_simple_setting_value.DeviceManagementConfigurationSimpleSettingValue]]
        """
        return self._simple_setting_collection_value
    
    @simple_setting_collection_value.setter
    def simple_setting_collection_value(self,value: Optional[List[device_management_configuration_simple_setting_value.DeviceManagementConfigurationSimpleSettingValue]] = None) -> None:
        """
        Sets the simpleSettingCollectionValue property value. Simple setting collection instance value
        Args:
            value: Value to set for the simple_setting_collection_value property.
        """
        self._simple_setting_collection_value = value
    

