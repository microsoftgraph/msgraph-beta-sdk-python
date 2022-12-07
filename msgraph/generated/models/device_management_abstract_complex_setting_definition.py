from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_setting_definition = lazy_import('msgraph.generated.models.device_management_setting_definition')

class DeviceManagementAbstractComplexSettingDefinition(device_management_setting_definition.DeviceManagementSettingDefinition):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementAbstractComplexSettingDefinition and sets the default values.
        """
        super().__init__()
        # List of definition IDs for all possible implementations of this abstract complex setting
        self._implementations: Optional[List[str]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementAbstractComplexSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementAbstractComplexSettingDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementAbstractComplexSettingDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "implementations": lambda n : setattr(self, 'implementations', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def implementations(self,) -> Optional[List[str]]:
        """
        Gets the implementations property value. List of definition IDs for all possible implementations of this abstract complex setting
        Returns: Optional[List[str]]
        """
        return self._implementations
    
    @implementations.setter
    def implementations(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the implementations property value. List of definition IDs for all possible implementations of this abstract complex setting
        Args:
            value: Value to set for the implementations property.
        """
        self._implementations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("implementations", self.implementations)
    

