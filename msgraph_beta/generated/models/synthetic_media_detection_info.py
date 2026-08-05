from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class SyntheticMediaDetectionInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The detectionId property
    detection_id: Optional[UUID] = None
    # The detectorBot property
    detector_bot: Optional[str] = None
    # The isParticipantTrusted property
    is_participant_trusted: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The syntheticConfidence property
    synthetic_confidence: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SyntheticMediaDetectionInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SyntheticMediaDetectionInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SyntheticMediaDetectionInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "detectionId": lambda n : setattr(self, 'detection_id', n.get_uuid_value()),
            "detectorBot": lambda n : setattr(self, 'detector_bot', n.get_str_value()),
            "isParticipantTrusted": lambda n : setattr(self, 'is_participant_trusted', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "syntheticConfidence": lambda n : setattr(self, 'synthetic_confidence', n.get_float_value()),
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
        writer.write_uuid_value("detectionId", self.detection_id)
        writer.write_str_value("detectorBot", self.detector_bot)
        writer.write_bool_value("isParticipantTrusted", self.is_participant_trusted)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("syntheticConfidence", self.synthetic_confidence)
        writer.write_additional_data_value(self.additional_data)
    

