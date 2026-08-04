from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .content_modality import ContentModality
    from .media_segment import MediaSegment

@dataclass
class SyntheticMediaDetectionDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The confidence property
    confidence: Optional[float] = None
    # The modality property
    modality: Optional[ContentModality] = None
    # The modelName property
    model_name: Optional[str] = None
    # The modelTasks property
    model_tasks: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The segment property
    segment: Optional[MediaSegment] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SyntheticMediaDetectionDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SyntheticMediaDetectionDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SyntheticMediaDetectionDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .content_modality import ContentModality
        from .media_segment import MediaSegment

        from .content_modality import ContentModality
        from .media_segment import MediaSegment

        fields: dict[str, Callable[[Any], None]] = {
            "confidence": lambda n : setattr(self, 'confidence', n.get_float_value()),
            "modality": lambda n : setattr(self, 'modality', n.get_enum_value(ContentModality)),
            "modelName": lambda n : setattr(self, 'model_name', n.get_str_value()),
            "modelTasks": lambda n : setattr(self, 'model_tasks', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "segment": lambda n : setattr(self, 'segment', n.get_object_value(MediaSegment)),
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
        writer.write_float_value("confidence", self.confidence)
        writer.write_enum_value("modality", self.modality)
        writer.write_str_value("modelName", self.model_name)
        writer.write_collection_of_primitive_values("modelTasks", self.model_tasks)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("segment", self.segment)
        writer.write_additional_data_value(self.additional_data)
    

