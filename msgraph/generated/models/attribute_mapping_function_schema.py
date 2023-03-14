from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attribute_mapping_parameter_schema = lazy_import('msgraph.generated.models.attribute_mapping_parameter_schema')
entity = lazy_import('msgraph.generated.models.entity')

class AttributeMappingFunctionSchema(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new attributeMappingFunctionSchema and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Collection of function parameters.
        self._parameters: Optional[List[attribute_mapping_parameter_schema.AttributeMappingParameterSchema]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttributeMappingFunctionSchema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttributeMappingFunctionSchema
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttributeMappingFunctionSchema()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "parameters": lambda n : setattr(self, 'parameters', n.get_collection_of_object_values(attribute_mapping_parameter_schema.AttributeMappingParameterSchema)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def parameters(self,) -> Optional[List[attribute_mapping_parameter_schema.AttributeMappingParameterSchema]]:
        """
        Gets the parameters property value. Collection of function parameters.
        Returns: Optional[List[attribute_mapping_parameter_schema.AttributeMappingParameterSchema]]
        """
        return self._parameters
    
    @parameters.setter
    def parameters(self,value: Optional[List[attribute_mapping_parameter_schema.AttributeMappingParameterSchema]] = None) -> None:
        """
        Sets the parameters property value. Collection of function parameters.
        Args:
            value: Value to set for the parameters property.
        """
        self._parameters = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("parameters", self.parameters)
    

