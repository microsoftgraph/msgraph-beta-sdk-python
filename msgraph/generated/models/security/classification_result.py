from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ClassificationResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The confidence level, 0 to 100, of the result.
    confidence_level: Optional[int] = None
    # The number of instances of the specific information type in the input.
    count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The GUID of the discovered sensitive information type.
    sensitive_type_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ClassificationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClassificationResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ClassificationResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "confidenceLevel": lambda n : setattr(self, 'confidence_level', n.get_int_value()),
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sensitiveTypeId": lambda n : setattr(self, 'sensitive_type_id', n.get_str_value()),
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
        writer.write_int_value("confidenceLevel", self.confidence_level)
        writer.write_int_value("count", self.count)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("sensitiveTypeId", self.sensitive_type_id)
        writer.write_additional_data_value(self.additional_data)
    

