from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sensitive_content_evidence import SensitiveContentEvidence

@dataclass
class SensitiveContentLocation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The confidence property
    confidence: Optional[int] = None
    # The evidences property
    evidences: Optional[List[SensitiveContentEvidence]] = None
    # The idMatch property
    id_match: Optional[str] = None
    # The length property
    length: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The offset property
    offset: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SensitiveContentLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SensitiveContentLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SensitiveContentLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .sensitive_content_evidence import SensitiveContentEvidence

        from .sensitive_content_evidence import SensitiveContentEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "confidence": lambda n : setattr(self, 'confidence', n.get_int_value()),
            "evidences": lambda n : setattr(self, 'evidences', n.get_collection_of_object_values(SensitiveContentEvidence)),
            "idMatch": lambda n : setattr(self, 'id_match', n.get_str_value()),
            "length": lambda n : setattr(self, 'length', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_int_value()),
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
        writer.write_int_value("confidence", self.confidence)
        writer.write_collection_of_object_values("evidences", self.evidences)
        writer.write_str_value("idMatch", self.id_match)
        writer.write_int_value("length", self.length)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("offset", self.offset)
        writer.write_additional_data_value(self.additional_data)
    

