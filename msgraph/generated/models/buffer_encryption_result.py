from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class BufferEncryptionResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The encryptedBuffer property
    encrypted_buffer: Optional[bytes] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The publishingLicense property
    publishing_license: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BufferEncryptionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BufferEncryptionResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BufferEncryptionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "encryptedBuffer": lambda n : setattr(self, 'encrypted_buffer', n.get_bytes_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "publishingLicense": lambda n : setattr(self, 'publishing_license', n.get_bytes_value()),
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
        writer.write_bytes_value("encryptedBuffer", self.encrypted_buffer)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_bytes_value("publishingLicense", self.publishing_license)
        writer.write_additional_data_value(self.additional_data)
    

