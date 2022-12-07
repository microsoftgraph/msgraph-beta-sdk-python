from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_setting_group_definition = lazy_import('msgraph.generated.models.device_management_configuration_setting_group_definition')

class DeviceManagementConfigurationSettingGroupCollectionDefinition(device_management_configuration_setting_group_definition.DeviceManagementConfigurationSettingGroupDefinition):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationSettingGroupCollectionDefinition and sets the default values.
        """
        super().__init__()
        # Maximum number of setting group count in the collection. Valid values 1 to 100
        self._maximum_count: Optional[int] = None
        # Minimum number of setting group count in the collection. Valid values 1 to 100
        self._minimum_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingGroupCollectionDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingGroupCollectionDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSettingGroupCollectionDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "maximum_count": lambda n : setattr(self, 'maximum_count', n.get_int_value()),
            "minimum_count": lambda n : setattr(self, 'minimum_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def maximum_count(self,) -> Optional[int]:
        """
        Gets the maximumCount property value. Maximum number of setting group count in the collection. Valid values 1 to 100
        Returns: Optional[int]
        """
        return self._maximum_count
    
    @maximum_count.setter
    def maximum_count(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumCount property value. Maximum number of setting group count in the collection. Valid values 1 to 100
        Args:
            value: Value to set for the maximumCount property.
        """
        self._maximum_count = value
    
    @property
    def minimum_count(self,) -> Optional[int]:
        """
        Gets the minimumCount property value. Minimum number of setting group count in the collection. Valid values 1 to 100
        Returns: Optional[int]
        """
        return self._minimum_count
    
    @minimum_count.setter
    def minimum_count(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumCount property value. Minimum number of setting group count in the collection. Valid values 1 to 100
        Args:
            value: Value to set for the minimumCount property.
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
    

