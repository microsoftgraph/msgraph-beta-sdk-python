from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import comms_operation, record_completion_reason

from . import comms_operation

class RecordOperation(comms_operation.CommsOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new RecordOperation and sets the default values.
        """
        super().__init__()
        # Possible values are: operationCanceled, stopToneDetected, maxRecordDurationReached, initialSilenceTimeout, maxSilenceTimeout, playPromptFailed, playBeepFailed, mediaReceiveTimeout, unspecifiedError, none.
        self._completion_reason: Optional[record_completion_reason.RecordCompletionReason] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The access token required to retrieve the recording.
        self._recording_access_token: Optional[str] = None
        # The location where the recording is located.
        self._recording_location: Optional[str] = None
    
    @property
    def completion_reason(self,) -> Optional[record_completion_reason.RecordCompletionReason]:
        """
        Gets the completionReason property value. Possible values are: operationCanceled, stopToneDetected, maxRecordDurationReached, initialSilenceTimeout, maxSilenceTimeout, playPromptFailed, playBeepFailed, mediaReceiveTimeout, unspecifiedError, none.
        Returns: Optional[record_completion_reason.RecordCompletionReason]
        """
        return self._completion_reason
    
    @completion_reason.setter
    def completion_reason(self,value: Optional[record_completion_reason.RecordCompletionReason] = None) -> None:
        """
        Sets the completionReason property value. Possible values are: operationCanceled, stopToneDetected, maxRecordDurationReached, initialSilenceTimeout, maxSilenceTimeout, playPromptFailed, playBeepFailed, mediaReceiveTimeout, unspecifiedError, none.
        Args:
            value: Value to set for the completion_reason property.
        """
        self._completion_reason = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecordOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecordOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RecordOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import comms_operation, record_completion_reason

        fields: Dict[str, Callable[[Any], None]] = {
            "completionReason": lambda n : setattr(self, 'completion_reason', n.get_enum_value(record_completion_reason.RecordCompletionReason)),
            "recordingAccessToken": lambda n : setattr(self, 'recording_access_token', n.get_str_value()),
            "recordingLocation": lambda n : setattr(self, 'recording_location', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def recording_access_token(self,) -> Optional[str]:
        """
        Gets the recordingAccessToken property value. The access token required to retrieve the recording.
        Returns: Optional[str]
        """
        return self._recording_access_token
    
    @recording_access_token.setter
    def recording_access_token(self,value: Optional[str] = None) -> None:
        """
        Sets the recordingAccessToken property value. The access token required to retrieve the recording.
        Args:
            value: Value to set for the recording_access_token property.
        """
        self._recording_access_token = value
    
    @property
    def recording_location(self,) -> Optional[str]:
        """
        Gets the recordingLocation property value. The location where the recording is located.
        Returns: Optional[str]
        """
        return self._recording_location
    
    @recording_location.setter
    def recording_location(self,value: Optional[str] = None) -> None:
        """
        Sets the recordingLocation property value. The location where the recording is located.
        Args:
            value: Value to set for the recording_location property.
        """
        self._recording_location = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("completionReason", self.completion_reason)
        writer.write_str_value("recordingAccessToken", self.recording_access_token)
        writer.write_str_value("recordingLocation", self.recording_location)
    

