from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_set, participant_info, recording_status

class RecordingInfo(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new recordingInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The participant who initiated the recording.
        self._initiated_by: Optional[participant_info.ParticipantInfo] = None
        # The identities of recording initiator.
        self._initiator: Optional[identity_set.IdentitySet] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The recordingStatus property
        self._recording_status: Optional[recording_status.RecordingStatus] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecordingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecordingInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RecordingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_set, participant_info, recording_status

        fields: Dict[str, Callable[[Any], None]] = {
            "initiatedBy": lambda n : setattr(self, 'initiated_by', n.get_object_value(participant_info.ParticipantInfo)),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recordingStatus": lambda n : setattr(self, 'recording_status', n.get_enum_value(recording_status.RecordingStatus)),
        }
        return fields
    
    @property
    def initiated_by(self,) -> Optional[participant_info.ParticipantInfo]:
        """
        Gets the initiatedBy property value. The participant who initiated the recording.
        Returns: Optional[participant_info.ParticipantInfo]
        """
        return self._initiated_by
    
    @initiated_by.setter
    def initiated_by(self,value: Optional[participant_info.ParticipantInfo] = None) -> None:
        """
        Sets the initiatedBy property value. The participant who initiated the recording.
        Args:
            value: Value to set for the initiated_by property.
        """
        self._initiated_by = value
    
    @property
    def initiator(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the initiator property value. The identities of recording initiator.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._initiator
    
    @initiator.setter
    def initiator(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the initiator property value. The identities of recording initiator.
        Args:
            value: Value to set for the initiator property.
        """
        self._initiator = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def recording_status(self,) -> Optional[recording_status.RecordingStatus]:
        """
        Gets the recordingStatus property value. The recordingStatus property
        Returns: Optional[recording_status.RecordingStatus]
        """
        return self._recording_status
    
    @recording_status.setter
    def recording_status(self,value: Optional[recording_status.RecordingStatus] = None) -> None:
        """
        Sets the recordingStatus property value. The recordingStatus property
        Args:
            value: Value to set for the recording_status property.
        """
        self._recording_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("initiatedBy", self.initiated_by)
        writer.write_object_value("initiator", self.initiator)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("recordingStatus", self.recording_status)
        writer.write_additional_data_value(self.additional_data)
    

