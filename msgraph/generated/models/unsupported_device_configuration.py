from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
unsupported_device_configuration_detail = lazy_import('msgraph.generated.models.unsupported_device_configuration_detail')

class UnsupportedDeviceConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new UnsupportedDeviceConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.unsupportedDeviceConfiguration"
        # Details describing why the entity is unsupported. This collection can contain a maximum of 1000 elements.
        self._details: Optional[List[unsupported_device_configuration_detail.UnsupportedDeviceConfigurationDetail]] = None
        # The type of entity that would be returned otherwise.
        self._original_entity_type_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnsupportedDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnsupportedDeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnsupportedDeviceConfiguration()
    
    @property
    def details(self,) -> Optional[List[unsupported_device_configuration_detail.UnsupportedDeviceConfigurationDetail]]:
        """
        Gets the details property value. Details describing why the entity is unsupported. This collection can contain a maximum of 1000 elements.
        Returns: Optional[List[unsupported_device_configuration_detail.UnsupportedDeviceConfigurationDetail]]
        """
        return self._details
    
    @details.setter
    def details(self,value: Optional[List[unsupported_device_configuration_detail.UnsupportedDeviceConfigurationDetail]] = None) -> None:
        """
        Sets the details property value. Details describing why the entity is unsupported. This collection can contain a maximum of 1000 elements.
        Args:
            value: Value to set for the details property.
        """
        self._details = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(unsupported_device_configuration_detail.UnsupportedDeviceConfigurationDetail)),
            "original_entity_type_name": lambda n : setattr(self, 'original_entity_type_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def original_entity_type_name(self,) -> Optional[str]:
        """
        Gets the originalEntityTypeName property value. The type of entity that would be returned otherwise.
        Returns: Optional[str]
        """
        return self._original_entity_type_name
    
    @original_entity_type_name.setter
    def original_entity_type_name(self,value: Optional[str] = None) -> None:
        """
        Sets the originalEntityTypeName property value. The type of entity that would be returned otherwise.
        Args:
            value: Value to set for the originalEntityTypeName property.
        """
        self._original_entity_type_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("details", self.details)
        writer.write_str_value("originalEntityTypeName", self.original_entity_type_name)
    

