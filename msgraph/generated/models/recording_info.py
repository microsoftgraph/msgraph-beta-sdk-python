from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_set, participant_info, recording_status

@dataclass
class RecordingInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The participant who initiated the recording.
    initiated_by: Optional[participant_info.ParticipantInfo] = None
    # The identities of recording initiator.
    initiator: Optional[identity_set.IdentitySet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recordingStatus property
    recording_status: Optional[recording_status.RecordingStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecordingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecordingInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RecordingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_set, participant_info, recording_status

        from . import identity_set, participant_info, recording_status

        fields: Dict[str, Callable[[Any], None]] = {
            "initiatedBy": lambda n : setattr(self, 'initiated_by', n.get_object_value(participant_info.ParticipantInfo)),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recordingStatus": lambda n : setattr(self, 'recording_status', n.get_enum_value(recording_status.RecordingStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("initiatedBy", self.initiated_by)
        writer.write_object_value("initiator", self.initiator)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("recordingStatus", self.recording_status)
        writer.write_additional_data_value(self.additional_data)
    

