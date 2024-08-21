from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .match_location import MatchLocation

@dataclass
class ContentClassification(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The confidence property
    confidence: Optional[int] = None
    # The matches property
    matches: Optional[List[MatchLocation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The sensitiveTypeId property
    sensitive_type_id: Optional[str] = None
    # The uniqueCount property
    unique_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentClassification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentClassification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentClassification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .match_location import MatchLocation

        from .match_location import MatchLocation

        fields: Dict[str, Callable[[Any], None]] = {
            "confidence": lambda n : setattr(self, 'confidence', n.get_int_value()),
            "matches": lambda n : setattr(self, 'matches', n.get_collection_of_object_values(MatchLocation)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sensitiveTypeId": lambda n : setattr(self, 'sensitive_type_id', n.get_str_value()),
            "uniqueCount": lambda n : setattr(self, 'unique_count', n.get_int_value()),
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
        writer.write_collection_of_object_values("matches", self.matches)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sensitiveTypeId", self.sensitive_type_id)
        writer.write_int_value("uniqueCount", self.unique_count)
        writer.write_additional_data_value(self.additional_data)
    

