from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import classification_attribute

@dataclass
class DiscoveredSensitiveType(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The classificationAttributes property
    classification_attributes: Optional[List[classification_attribute.ClassificationAttribute]] = None
    # The confidence property
    confidence: Optional[int] = None
    # The count property
    count: Optional[int] = None
    # The id property
    id: Optional[UUID] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DiscoveredSensitiveType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DiscoveredSensitiveType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DiscoveredSensitiveType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import classification_attribute

        fields: Dict[str, Callable[[Any], None]] = {
            "classificationAttributes": lambda n : setattr(self, 'classification_attributes', n.get_collection_of_object_values(classification_attribute.ClassificationAttribute)),
            "confidence": lambda n : setattr(self, 'confidence', n.get_int_value()),
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("classificationAttributes", self.classification_attributes)
        writer.write_int_value("confidence", self.confidence)
        writer.write_int_value("count", self.count)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

