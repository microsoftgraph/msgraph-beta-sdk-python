from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class CorsConfiguration_v2(entity.Entity):
    """
    Casts the previous resource to application.
    """
    @property
    def allowed_headers(self,) -> Optional[List[str]]:
        """
        Gets the allowedHeaders property value. The allowedHeaders property
        Returns: Optional[List[str]]
        """
        return self._allowed_headers
    
    @allowed_headers.setter
    def allowed_headers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedHeaders property value. The allowedHeaders property
        Args:
            value: Value to set for the allowedHeaders property.
        """
        self._allowed_headers = value
    
    @property
    def allowed_methods(self,) -> Optional[List[str]]:
        """
        Gets the allowedMethods property value. The allowedMethods property
        Returns: Optional[List[str]]
        """
        return self._allowed_methods
    
    @allowed_methods.setter
    def allowed_methods(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedMethods property value. The allowedMethods property
        Args:
            value: Value to set for the allowedMethods property.
        """
        self._allowed_methods = value
    
    @property
    def allowed_origins(self,) -> Optional[List[str]]:
        """
        Gets the allowedOrigins property value. The allowedOrigins property
        Returns: Optional[List[str]]
        """
        return self._allowed_origins
    
    @allowed_origins.setter
    def allowed_origins(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedOrigins property value. The allowedOrigins property
        Args:
            value: Value to set for the allowedOrigins property.
        """
        self._allowed_origins = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new corsConfiguration_v2 and sets the default values.
        """
        super().__init__()
        # The allowedHeaders property
        self._allowed_headers: Optional[List[str]] = None
        # The allowedMethods property
        self._allowed_methods: Optional[List[str]] = None
        # The allowedOrigins property
        self._allowed_origins: Optional[List[str]] = None
        # The maxAgeInSeconds property
        self._max_age_in_seconds: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The resource property
        self._resource: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CorsConfiguration_v2:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CorsConfiguration_v2
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CorsConfiguration_v2()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_headers": lambda n : setattr(self, 'allowed_headers', n.get_collection_of_primitive_values(str)),
            "allowed_methods": lambda n : setattr(self, 'allowed_methods', n.get_collection_of_primitive_values(str)),
            "allowed_origins": lambda n : setattr(self, 'allowed_origins', n.get_collection_of_primitive_values(str)),
            "max_age_in_seconds": lambda n : setattr(self, 'max_age_in_seconds', n.get_int_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def max_age_in_seconds(self,) -> Optional[int]:
        """
        Gets the maxAgeInSeconds property value. The maxAgeInSeconds property
        Returns: Optional[int]
        """
        return self._max_age_in_seconds
    
    @max_age_in_seconds.setter
    def max_age_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the maxAgeInSeconds property value. The maxAgeInSeconds property
        Args:
            value: Value to set for the maxAgeInSeconds property.
        """
        self._max_age_in_seconds = value
    
    @property
    def resource(self,) -> Optional[str]:
        """
        Gets the resource property value. The resource property
        Returns: Optional[str]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[str] = None) -> None:
        """
        Sets the resource property value. The resource property
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("allowedHeaders", self.allowed_headers)
        writer.write_collection_of_primitive_values("allowedMethods", self.allowed_methods)
        writer.write_collection_of_primitive_values("allowedOrigins", self.allowed_origins)
        writer.write_int_value("maxAgeInSeconds", self.max_age_in_seconds)
        writer.write_str_value("resource", self.resource)
    

