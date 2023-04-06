from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, media_stream, online_meeting_restricted, participant_info, recording_info, removed_state

from . import entity

class Participant(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new participant and sets the default values.
        """
        super().__init__()
        # The info property
        self._info: Optional[participant_info.ParticipantInfo] = None
        # The isIdentityAnonymized property
        self._is_identity_anonymized: Optional[bool] = None
        # true if the participant is in lobby.
        self._is_in_lobby: Optional[bool] = None
        # true if the participant is muted (client or server muted).
        self._is_muted: Optional[bool] = None
        # The list of media streams.
        self._media_streams: Optional[List[media_stream.MediaStream]] = None
        # A blob of data provided by the participant in the roster.
        self._metadata: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Information on whether the participant has recording capability.
        self._recording_info: Optional[recording_info.RecordingInfo] = None
        # The removedState property
        self._removed_state: Optional[removed_state.RemovedState] = None
        # Indicates the reason or reasons why media content from this participant is restricted.
        self._restricted_experience: Optional[online_meeting_restricted.OnlineMeetingRestricted] = None
        # The rosterSequenceNumber property
        self._roster_sequence_number: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Participant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Participant
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Participant()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, media_stream, online_meeting_restricted, participant_info, recording_info, removed_state

        fields: Dict[str, Callable[[Any], None]] = {
            "info": lambda n : setattr(self, 'info', n.get_object_value(participant_info.ParticipantInfo)),
            "isIdentityAnonymized": lambda n : setattr(self, 'is_identity_anonymized', n.get_bool_value()),
            "isInLobby": lambda n : setattr(self, 'is_in_lobby', n.get_bool_value()),
            "isMuted": lambda n : setattr(self, 'is_muted', n.get_bool_value()),
            "mediaStreams": lambda n : setattr(self, 'media_streams', n.get_collection_of_object_values(media_stream.MediaStream)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_str_value()),
            "recordingInfo": lambda n : setattr(self, 'recording_info', n.get_object_value(recording_info.RecordingInfo)),
            "removedState": lambda n : setattr(self, 'removed_state', n.get_object_value(removed_state.RemovedState)),
            "restrictedExperience": lambda n : setattr(self, 'restricted_experience', n.get_object_value(online_meeting_restricted.OnlineMeetingRestricted)),
            "rosterSequenceNumber": lambda n : setattr(self, 'roster_sequence_number', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def info(self,) -> Optional[participant_info.ParticipantInfo]:
        """
        Gets the info property value. The info property
        Returns: Optional[participant_info.ParticipantInfo]
        """
        return self._info
    
    @info.setter
    def info(self,value: Optional[participant_info.ParticipantInfo] = None) -> None:
        """
        Sets the info property value. The info property
        Args:
            value: Value to set for the info property.
        """
        self._info = value
    
    @property
    def is_identity_anonymized(self,) -> Optional[bool]:
        """
        Gets the isIdentityAnonymized property value. The isIdentityAnonymized property
        Returns: Optional[bool]
        """
        return self._is_identity_anonymized
    
    @is_identity_anonymized.setter
    def is_identity_anonymized(self,value: Optional[bool] = None) -> None:
        """
        Sets the isIdentityAnonymized property value. The isIdentityAnonymized property
        Args:
            value: Value to set for the is_identity_anonymized property.
        """
        self._is_identity_anonymized = value
    
    @property
    def is_in_lobby(self,) -> Optional[bool]:
        """
        Gets the isInLobby property value. true if the participant is in lobby.
        Returns: Optional[bool]
        """
        return self._is_in_lobby
    
    @is_in_lobby.setter
    def is_in_lobby(self,value: Optional[bool] = None) -> None:
        """
        Sets the isInLobby property value. true if the participant is in lobby.
        Args:
            value: Value to set for the is_in_lobby property.
        """
        self._is_in_lobby = value
    
    @property
    def is_muted(self,) -> Optional[bool]:
        """
        Gets the isMuted property value. true if the participant is muted (client or server muted).
        Returns: Optional[bool]
        """
        return self._is_muted
    
    @is_muted.setter
    def is_muted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMuted property value. true if the participant is muted (client or server muted).
        Args:
            value: Value to set for the is_muted property.
        """
        self._is_muted = value
    
    @property
    def media_streams(self,) -> Optional[List[media_stream.MediaStream]]:
        """
        Gets the mediaStreams property value. The list of media streams.
        Returns: Optional[List[media_stream.MediaStream]]
        """
        return self._media_streams
    
    @media_streams.setter
    def media_streams(self,value: Optional[List[media_stream.MediaStream]] = None) -> None:
        """
        Sets the mediaStreams property value. The list of media streams.
        Args:
            value: Value to set for the media_streams property.
        """
        self._media_streams = value
    
    @property
    def metadata(self,) -> Optional[str]:
        """
        Gets the metadata property value. A blob of data provided by the participant in the roster.
        Returns: Optional[str]
        """
        return self._metadata
    
    @metadata.setter
    def metadata(self,value: Optional[str] = None) -> None:
        """
        Sets the metadata property value. A blob of data provided by the participant in the roster.
        Args:
            value: Value to set for the metadata property.
        """
        self._metadata = value
    
    @property
    def recording_info(self,) -> Optional[recording_info.RecordingInfo]:
        """
        Gets the recordingInfo property value. Information on whether the participant has recording capability.
        Returns: Optional[recording_info.RecordingInfo]
        """
        return self._recording_info
    
    @recording_info.setter
    def recording_info(self,value: Optional[recording_info.RecordingInfo] = None) -> None:
        """
        Sets the recordingInfo property value. Information on whether the participant has recording capability.
        Args:
            value: Value to set for the recording_info property.
        """
        self._recording_info = value
    
    @property
    def removed_state(self,) -> Optional[removed_state.RemovedState]:
        """
        Gets the removedState property value. The removedState property
        Returns: Optional[removed_state.RemovedState]
        """
        return self._removed_state
    
    @removed_state.setter
    def removed_state(self,value: Optional[removed_state.RemovedState] = None) -> None:
        """
        Sets the removedState property value. The removedState property
        Args:
            value: Value to set for the removed_state property.
        """
        self._removed_state = value
    
    @property
    def restricted_experience(self,) -> Optional[online_meeting_restricted.OnlineMeetingRestricted]:
        """
        Gets the restrictedExperience property value. Indicates the reason or reasons why media content from this participant is restricted.
        Returns: Optional[online_meeting_restricted.OnlineMeetingRestricted]
        """
        return self._restricted_experience
    
    @restricted_experience.setter
    def restricted_experience(self,value: Optional[online_meeting_restricted.OnlineMeetingRestricted] = None) -> None:
        """
        Sets the restrictedExperience property value. Indicates the reason or reasons why media content from this participant is restricted.
        Args:
            value: Value to set for the restricted_experience property.
        """
        self._restricted_experience = value
    
    @property
    def roster_sequence_number(self,) -> Optional[int]:
        """
        Gets the rosterSequenceNumber property value. The rosterSequenceNumber property
        Returns: Optional[int]
        """
        return self._roster_sequence_number
    
    @roster_sequence_number.setter
    def roster_sequence_number(self,value: Optional[int] = None) -> None:
        """
        Sets the rosterSequenceNumber property value. The rosterSequenceNumber property
        Args:
            value: Value to set for the roster_sequence_number property.
        """
        self._roster_sequence_number = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("info", self.info)
        writer.write_bool_value("isIdentityAnonymized", self.is_identity_anonymized)
        writer.write_bool_value("isInLobby", self.is_in_lobby)
        writer.write_bool_value("isMuted", self.is_muted)
        writer.write_collection_of_object_values("mediaStreams", self.media_streams)
        writer.write_str_value("metadata", self.metadata)
        writer.write_object_value("recordingInfo", self.recording_info)
        writer.write_object_value("removedState", self.removed_state)
        writer.write_object_value("restrictedExperience", self.restricted_experience)
        writer.write_int_value("rosterSequenceNumber", self.roster_sequence_number)
    

