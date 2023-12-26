from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .broadcast_meeting_settings import BroadcastMeetingSettings
    from .call_recording import CallRecording
    from .call_transcript import CallTranscript
    from .meeting_attendance_report import MeetingAttendanceReport
    from .meeting_capabilities import MeetingCapabilities
    from .meeting_participants import MeetingParticipants
    from .meeting_registration import MeetingRegistration
    from .online_meeting_base import OnlineMeetingBase

from .online_meeting_base import OnlineMeetingBase

@dataclass
class OnlineMeeting(OnlineMeetingBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onlineMeeting"
    # The alternativeRecording property
    alternative_recording: Optional[bytes] = None
    # The attendeeReport property
    attendee_report: Optional[bytes] = None
    # The broadcastRecording property
    broadcast_recording: Optional[bytes] = None
    # The broadcastSettings property
    broadcast_settings: Optional[BroadcastMeetingSettings] = None
    # The capabilities property
    capabilities: Optional[List[MeetingCapabilities]] = None
    # The meeting creation time in UTC. Read-only.
    creation_date_time: Optional[datetime.datetime] = None
    # The meeting end time in UTC.
    end_date_time: Optional[datetime.datetime] = None
    # The external ID. A custom ID. Optional.
    external_id: Optional[str] = None
    # The isBroadcast property
    is_broadcast: Optional[bool] = None
    # The joinUrl property
    join_url: Optional[str] = None
    # The meetingAttendanceReport property
    meeting_attendance_report: Optional[MeetingAttendanceReport] = None
    # The participants associated with the online meeting, including the organizer and the attendees.
    participants: Optional[MeetingParticipants] = None
    # The recording property
    recording: Optional[bytes] = None
    # The recordings of an online meeting. Read-only.
    recordings: Optional[List[CallRecording]] = None
    # The registration that is enabled for an online meeting. One online meeting can only have one registration enabled.
    registration: Optional[MeetingRegistration] = None
    # The meeting start time in UTC.
    start_date_time: Optional[datetime.datetime] = None
    # The transcripts of an online meeting. Read-only.
    transcripts: Optional[List[CallTranscript]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnlineMeeting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeeting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnlineMeeting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .broadcast_meeting_settings import BroadcastMeetingSettings
        from .call_recording import CallRecording
        from .call_transcript import CallTranscript
        from .meeting_attendance_report import MeetingAttendanceReport
        from .meeting_capabilities import MeetingCapabilities
        from .meeting_participants import MeetingParticipants
        from .meeting_registration import MeetingRegistration
        from .online_meeting_base import OnlineMeetingBase

        from .broadcast_meeting_settings import BroadcastMeetingSettings
        from .call_recording import CallRecording
        from .call_transcript import CallTranscript
        from .meeting_attendance_report import MeetingAttendanceReport
        from .meeting_capabilities import MeetingCapabilities
        from .meeting_participants import MeetingParticipants
        from .meeting_registration import MeetingRegistration
        from .online_meeting_base import OnlineMeetingBase

        fields: Dict[str, Callable[[Any], None]] = {
            "alternativeRecording": lambda n : setattr(self, 'alternative_recording', n.get_bytes_value()),
            "attendeeReport": lambda n : setattr(self, 'attendee_report', n.get_bytes_value()),
            "broadcastRecording": lambda n : setattr(self, 'broadcast_recording', n.get_bytes_value()),
            "broadcastSettings": lambda n : setattr(self, 'broadcast_settings', n.get_object_value(BroadcastMeetingSettings)),
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_collection_of_enum_values(MeetingCapabilities)),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "isBroadcast": lambda n : setattr(self, 'is_broadcast', n.get_bool_value()),
            "joinUrl": lambda n : setattr(self, 'join_url', n.get_str_value()),
            "meetingAttendanceReport": lambda n : setattr(self, 'meeting_attendance_report', n.get_object_value(MeetingAttendanceReport)),
            "participants": lambda n : setattr(self, 'participants', n.get_object_value(MeetingParticipants)),
            "recording": lambda n : setattr(self, 'recording', n.get_bytes_value()),
            "recordings": lambda n : setattr(self, 'recordings', n.get_collection_of_object_values(CallRecording)),
            "registration": lambda n : setattr(self, 'registration', n.get_object_value(MeetingRegistration)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "transcripts": lambda n : setattr(self, 'transcripts', n.get_collection_of_object_values(CallTranscript)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bytes_value("alternativeRecording", self.alternative_recording)
        writer.write_bytes_value("attendeeReport", self.attendee_report)
        writer.write_bytes_value("broadcastRecording", self.broadcast_recording)
        writer.write_object_value("broadcastSettings", self.broadcast_settings)
        writer.write_collection_of_enum_values("capabilities", self.capabilities)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("externalId", self.external_id)
        writer.write_bool_value("isBroadcast", self.is_broadcast)
        writer.write_str_value("joinUrl", self.join_url)
        writer.write_object_value("meetingAttendanceReport", self.meeting_attendance_report)
        writer.write_object_value("participants", self.participants)
        writer.write_bytes_value("recording", self.recording)
        writer.write_collection_of_object_values("recordings", self.recordings)
        writer.write_object_value("registration", self.registration)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_collection_of_object_values("transcripts", self.transcripts)
    

