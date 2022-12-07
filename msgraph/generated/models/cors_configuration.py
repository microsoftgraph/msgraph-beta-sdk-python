from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class CorsConfiguration(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def allowed_headers(self,) -> Optional[List[str]]:
        """
        Gets the allowedHeaders property value. The request headers that the origin domain may specify on the CORS request. The wildcard character * indicates that any header beginning with the specified prefix is allowed.
        Returns: Optional[List[str]]
        """
        return self._allowed_headers
    
    @allowed_headers.setter
    def allowed_headers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedHeaders property value. The request headers that the origin domain may specify on the CORS request. The wildcard character * indicates that any header beginning with the specified prefix is allowed.
        Args:
            value: Value to set for the allowedHeaders property.
        """
        self._allowed_headers = value
    
    @property
    def allowed_methods(self,) -> Optional[List[str]]:
        """
        Gets the allowedMethods property value. The HTTP request methods that the origin domain may use for a CORS request.
        Returns: Optional[List[str]]
        """
        return self._allowed_methods
    
    @allowed_methods.setter
    def allowed_methods(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedMethods property value. The HTTP request methods that the origin domain may use for a CORS request.
        Args:
            value: Value to set for the allowedMethods property.
        """
        self._allowed_methods = value
    
    @property
    def allowed_origins(self,) -> Optional[List[str]]:
        """
        Gets the allowedOrigins property value. The origin domains that are permitted to make a request against the service via CORS. The origin domain is the domain from which the request originates. The origin must be an exact case-sensitive match with the origin that the user age sends to the service.
        Returns: Optional[List[str]]
        """
        return self._allowed_origins
    
    @allowed_origins.setter
    def allowed_origins(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedOrigins property value. The origin domains that are permitted to make a request against the service via CORS. The origin domain is the domain from which the request originates. The origin must be an exact case-sensitive match with the origin that the user age sends to the service.
        Args:
            value: Value to set for the allowedOrigins property.
        """
        self._allowed_origins = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new corsConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The request headers that the origin domain may specify on the CORS request. The wildcard character * indicates that any header beginning with the specified prefix is allowed.
        self._allowed_headers: Optional[List[str]] = None
        # The HTTP request methods that the origin domain may use for a CORS request.
        self._allowed_methods: Optional[List[str]] = None
        # The origin domains that are permitted to make a request against the service via CORS. The origin domain is the domain from which the request originates. The origin must be an exact case-sensitive match with the origin that the user age sends to the service.
        self._allowed_origins: Optional[List[str]] = None
        # The maximum amount of time that a browser should cache the response to the preflight OPTIONS request.
        self._max_age_in_seconds: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Resource within the application segment for which CORS permissions are granted. / grants permission for whole app segment.
        self._resource: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CorsConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CorsConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CorsConfiguration()
    
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
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_str_value()),
        }
        return fields
    
    @property
    def max_age_in_seconds(self,) -> Optional[int]:
        """
        Gets the maxAgeInSeconds property value. The maximum amount of time that a browser should cache the response to the preflight OPTIONS request.
        Returns: Optional[int]
        """
        return self._max_age_in_seconds
    
    @max_age_in_seconds.setter
    def max_age_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the maxAgeInSeconds property value. The maximum amount of time that a browser should cache the response to the preflight OPTIONS request.
        Args:
            value: Value to set for the maxAgeInSeconds property.
        """
        self._max_age_in_seconds = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def resource(self,) -> Optional[str]:
        """
        Gets the resource property value. Resource within the application segment for which CORS permissions are granted. / grants permission for whole app segment.
        Returns: Optional[str]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[str] = None) -> None:
        """
        Sets the resource property value. Resource within the application segment for which CORS permissions are granted. / grants permission for whole app segment.
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
        writer.write_collection_of_primitive_values("allowedHeaders", self.allowed_headers)
        writer.write_collection_of_primitive_values("allowedMethods", self.allowed_methods)
        writer.write_collection_of_primitive_values("allowedOrigins", self.allowed_origins)
        writer.write_int_value("maxAgeInSeconds", self.max_age_in_seconds)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resource", self.resource)
        writer.write_additional_data_value(self.additional_data)
    

