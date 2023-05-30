from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_simple_setting_definition

from . import device_management_configuration_simple_setting_definition

class DeviceManagementConfigurationSimpleSettingCollectionDefinition(device_management_configuration_simple_setting_definition.DeviceManagementConfigurationSimpleSettingDefinition):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationSimpleSettingCollectionDefinition and sets the default values.
        """
        super().__init__()
        # Maximum number of simple settings in the collection. Valid values 1 to 100
        self._maximum_count: Optional[int] = None
        # Minimum number of simple settings in the collection. Valid values 1 to 100
        self._minimum_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSimpleSettingCollectionDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingCollectionDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSimpleSettingCollectionDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_simple_setting_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "maximumCount": lambda n : setattr(self, 'maximum_count', n.get_int_value()),
            "minimumCount": lambda n : setattr(self, 'minimum_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def maximum_count(self,) -> Optional[int]:
        """
        Gets the maximumCount property value. Maximum number of simple settings in the collection. Valid values 1 to 100
        Returns: Optional[int]
        """
        return self._maximum_count
    
    @maximum_count.setter
    def maximum_count(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumCount property value. Maximum number of simple settings in the collection. Valid values 1 to 100
        Args:
            value: Value to set for the maximum_count property.
        """
        self._maximum_count = value
    
    @property
    def minimum_count(self,) -> Optional[int]:
        """
        Gets the minimumCount property value. Minimum number of simple settings in the collection. Valid values 1 to 100
        Returns: Optional[int]
        """
        return self._minimum_count
    
    @minimum_count.setter
    def minimum_count(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumCount property value. Minimum number of simple settings in the collection. Valid values 1 to 100
        Args:
            value: Value to set for the minimum_count property.
        """
        self._minimum_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("maximumCount", self.maximum_count)
        writer.write_int_value("minimumCount", self.minimum_count)
    

