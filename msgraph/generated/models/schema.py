from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
property_ = lazy_import('msgraph.generated.models.property_')

class Schema(entity.Entity):
    @property
    def base_type(self,) -> Optional[str]:
        """
        Gets the baseType property value. The baseType property
        Returns: Optional[str]
        """
        return self._base_type
    
    @base_type.setter
    def base_type(self,value: Optional[str] = None) -> None:
        """
        Sets the baseType property value. The baseType property
        Args:
            value: Value to set for the base_type property.
        """
        self._base_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new schema and sets the default values.
        """
        super().__init__()
        # The baseType property
        self._base_type: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The properties property
        self._properties: Optional[List[property_.Property_]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Schema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Schema
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Schema()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "baseType": lambda n : setattr(self, 'base_type', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(property_.Property_)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def properties(self,) -> Optional[List[property_.Property_]]:
        """
        Gets the properties property value. The properties property
        Returns: Optional[List[property_.Property_]]
        """
        return self._properties
    
    @properties.setter
    def properties(self,value: Optional[List[property_.Property_]] = None) -> None:
        """
        Sets the properties property value. The properties property
        Args:
            value: Value to set for the properties property.
        """
        self._properties = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("baseType", self.base_type)
        writer.write_collection_of_object_values("properties", self.properties)
    

