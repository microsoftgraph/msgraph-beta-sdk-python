from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CorsConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The request headers that the origin domain may specify on the CORS request. The wildcard character * indicates that any header beginning with the specified prefix is allowed.
    allowed_headers: Optional[List[str]] = None
    # The HTTP request methods that the origin domain may use for a CORS request.
    allowed_methods: Optional[List[str]] = None
    # The origin domains that are permitted to make a request against the service via CORS. The origin domain is the domain from which the request originates. The origin must be an exact case-sensitive match with the origin that the user age sends to the service.
    allowed_origins: Optional[List[str]] = None
    # The maximum amount of time that a browser should cache the response to the preflight OPTIONS request.
    max_age_in_seconds: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Resource within the application segment for which CORS permissions are granted. / grants permission for whole app segment.
    resource: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CorsConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CorsConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CorsConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "allowedHeaders": lambda n : setattr(self, 'allowed_headers', n.get_collection_of_primitive_values(str)),
            "allowedMethods": lambda n : setattr(self, 'allowed_methods', n.get_collection_of_primitive_values(str)),
            "allowedOrigins": lambda n : setattr(self, 'allowed_origins', n.get_collection_of_primitive_values(str)),
            "maxAgeInSeconds": lambda n : setattr(self, 'max_age_in_seconds', n.get_int_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("allowedHeaders", self.allowed_headers)
        writer.write_collection_of_primitive_values("allowedMethods", self.allowed_methods)
        writer.write_collection_of_primitive_values("allowedOrigins", self.allowed_origins)
        writer.write_int_value("maxAgeInSeconds", self.max_age_in_seconds)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("resource", self.resource)
        writer.write_additional_data_value(self.additional_data)
    

