from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .......models.detection_severity import DetectionSeverity
    from .......models.media_metadata import MediaMetadata
    from .......models.synthetic_media_detection_detail import SyntheticMediaDetectionDetail

@dataclass
class ReportSyntheticMediaPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The isMalicious property
    is_malicious: Optional[bool] = False
    # The contentMetadata property
    content_metadata: Optional[MediaMetadata] = None
    # The detectionDateTime property
    detection_date_time: Optional[datetime.datetime] = None
    # The detections property
    detections: Optional[list[SyntheticMediaDetectionDetail]] = None
    # The id property
    id: Optional[UUID] = None
    # The overallConfidence property
    overall_confidence: Optional[float] = None
    # The severity property
    severity: Optional[DetectionSeverity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ReportSyntheticMediaPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReportSyntheticMediaPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ReportSyntheticMediaPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .......models.detection_severity import DetectionSeverity
        from .......models.media_metadata import MediaMetadata
        from .......models.synthetic_media_detection_detail import SyntheticMediaDetectionDetail

        from .......models.detection_severity import DetectionSeverity
        from .......models.media_metadata import MediaMetadata
        from .......models.synthetic_media_detection_detail import SyntheticMediaDetectionDetail

        fields: dict[str, Callable[[Any], None]] = {
            "contentMetadata": lambda n : setattr(self, 'content_metadata', n.get_object_value(MediaMetadata)),
            "detectionDateTime": lambda n : setattr(self, 'detection_date_time', n.get_datetime_value()),
            "detections": lambda n : setattr(self, 'detections', n.get_collection_of_object_values(SyntheticMediaDetectionDetail)),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "isMalicious": lambda n : setattr(self, 'is_malicious', n.get_bool_value()),
            "overallConfidence": lambda n : setattr(self, 'overall_confidence', n.get_float_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(DetectionSeverity)),
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
        writer.write_object_value("contentMetadata", self.content_metadata)
        writer.write_datetime_value("detectionDateTime", self.detection_date_time)
        writer.write_collection_of_object_values("detections", self.detections)
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("isMalicious", self.is_malicious)
        writer.write_float_value("overallConfidence", self.overall_confidence)
        writer.write_enum_value("severity", self.severity)
        writer.write_additional_data_value(self.additional_data)
    

