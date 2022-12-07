from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_constraint = lazy_import('msgraph.generated.models.device_management_constraint')

class DeviceManagementSettingProfileConstraint(device_management_constraint.DeviceManagementConstraint):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementSettingProfileConstraint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementSettingProfileConstraint"
        # The source of the entity
        self._source: Optional[str] = None
        # A collection of types this entity carries
        self._types: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingProfileConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingProfileConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingProfileConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "types": lambda n : setattr(self, 'types', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("source", self.source)
        writer.write_collection_of_primitive_values("types", self.types)
    
    @property
    def source(self,) -> Optional[str]:
        """
        Gets the source property value. The source of the entity
        Returns: Optional[str]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[str] = None) -> None:
        """
        Sets the source property value. The source of the entity
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    
    @property
    def types(self,) -> Optional[List[str]]:
        """
        Gets the types property value. A collection of types this entity carries
        Returns: Optional[List[str]]
        """
        return self._types
    
    @types.setter
    def types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the types property value. A collection of types this entity carries
        Args:
            value: Value to set for the types property.
        """
        self._types = value
    

