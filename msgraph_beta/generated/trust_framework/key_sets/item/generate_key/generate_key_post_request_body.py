from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class GenerateKeyPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The exp property
    exp: Optional[int] = None
    # The kty property
    kty: Optional[str] = None
    # The nbf property
    nbf: Optional[int] = None
    # The use property
    use: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GenerateKeyPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GenerateKeyPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GenerateKeyPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "exp": lambda n : setattr(self, 'exp', n.get_int_value()),
            "kty": lambda n : setattr(self, 'kty', n.get_str_value()),
            "nbf": lambda n : setattr(self, 'nbf', n.get_int_value()),
            "use": lambda n : setattr(self, 'use', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("exp", self.exp)
        writer.write_str_value("kty", self.kty)
        writer.write_int_value("nbf", self.nbf)
        writer.write_str_value("use", self.use)
        writer.write_additional_data_value(self.additional_data)
    

