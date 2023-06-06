from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import audio_conferencing, broadcast_meeting_settings, call_recording, call_transcript, chat_info, entity, item_body, join_meeting_id_settings, lobby_bypass_settings, meeting_attendance_report, meeting_capabilities, meeting_chat_history_default_mode, meeting_chat_mode, meeting_participants, meeting_registration, online_meeting_presenters, online_meeting_role, virtual_appointment, virtual_event_session, watermark_protection_values

from . import entity

@dataclass
class OnlineMeeting(entity.Entity):
    # Indicates whether attendees can turn on their camera.
    allow_attendee_to_enable_camera: Optional[bool] = None
    # Indicates whether attendees can turn on their microphone.
    allow_attendee_to_enable_mic: Optional[bool] = None
    # Specifies the mode of meeting chat.
    allow_meeting_chat: Optional[meeting_chat_mode.MeetingChatMode] = None
    # Specifies if participants are allowed to rename themselves in an instance of the meeting.
    allow_participants_to_change_name: Optional[bool] = None
    # The allowRecording property
    allow_recording: Optional[bool] = None
    # Indicates if Teams reactions are enabled for the meeting.
    allow_teamwork_reactions: Optional[bool] = None
    # The allowTranscription property
    allow_transcription: Optional[bool] = None
    # Specifies who can be a presenter in a meeting.
    allowed_presenters: Optional[online_meeting_presenters.OnlineMeetingPresenters] = None
    # The content stream of the alternative recording of a Microsoft Teams live event. Read-only.
    alternative_recording: Optional[bytes] = None
    # The anonymizeIdentityForRoles property
    anonymize_identity_for_roles: Optional[List[online_meeting_role.OnlineMeetingRole]] = None
    # The attendance reports of an online meeting. Read-only.
    attendance_reports: Optional[List[meeting_attendance_report.MeetingAttendanceReport]] = None
    # The content stream of the attendee report of a Teams live event. Read-only.
    attendee_report: Optional[bytes] = None
    # The phone access (dial-in) information for an online meeting. Read-only.
    audio_conferencing: Optional[audio_conferencing.AudioConferencing] = None
    # The broadcastRecording property
    broadcast_recording: Optional[bytes] = None
    # Settings related to a live event.
    broadcast_settings: Optional[broadcast_meeting_settings.BroadcastMeetingSettings] = None
    # The capabilities property
    capabilities: Optional[List[meeting_capabilities.MeetingCapabilities]] = None
    # The chat information associated with this online meeting.
    chat_info: Optional[chat_info.ChatInfo] = None
    # The meeting creation time in UTC. Read-only.
    creation_date_time: Optional[datetime] = None
    # The meeting end time in UTC.
    end_date_time: Optional[datetime] = None
    # The external ID. A custom ID. Optional.
    external_id: Optional[str] = None
    # Indicates whether this is a Teams live event.
    is_broadcast: Optional[bool] = None
    # Indicates whether to announce when callers join or leave.
    is_entry_exit_announced: Optional[bool] = None
    # The join information in the language and locale variant specified in 'Accept-Language' request HTTP header. Read-only.
    join_information: Optional[item_body.ItemBody] = None
    # Specifies the joinMeetingId, the meeting passcode, and the requirement for the passcode. Once an onlineMeeting is created, the joinMeetingIdSettings cannot be modified. To make any changes to this property, the meeting needs to be canceled and a new one needs to be created.
    join_meeting_id_settings: Optional[join_meeting_id_settings.JoinMeetingIdSettings] = None
    # The joinUrl property
    join_url: Optional[str] = None
    # The join URL of the online meeting. Read-only.
    join_web_url: Optional[str] = None
    # Specifies which participants can bypass the meeting lobby.
    lobby_bypass_settings: Optional[lobby_bypass_settings.LobbyBypassSettings] = None
    # The meetingAttendanceReport property
    meeting_attendance_report: Optional[meeting_attendance_report.MeetingAttendanceReport] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The participants associated with the online meeting. This includes the organizer and the attendees.
    participants: Optional[meeting_participants.MeetingParticipants] = None
    # Indicates whether to record the meeting automatically.
    record_automatically: Optional[bool] = None
    # The content stream of the recording of a Teams live event. Read-only.
    recording: Optional[bytes] = None
    # The recordings property
    recordings: Optional[List[call_recording.CallRecording]] = None
    # The registration that has been enabled for an online meeting. One online meeting can only have one registration enabled.
    registration: Optional[meeting_registration.MeetingRegistration] = None
    # Specifies whether meeting chat history is shared with participants.  Possible values are: all, none, unknownFutureValue.
    share_meeting_chat_history_default: Optional[meeting_chat_history_default_mode.MeetingChatHistoryDefaultMode] = None
    # The meeting start time in UTC.
    start_date_time: Optional[datetime] = None
    # The subject of the online meeting.
    subject: Optional[str] = None
    # The transcripts of an online meeting. Read-only.
    transcripts: Optional[List[call_transcript.CallTranscript]] = None
    # The video teleconferencing ID. Read-only.
    video_teleconference_id: Optional[str] = None
    # The virtualAppointment property
    virtual_appointment: Optional[virtual_appointment.VirtualAppointment] = None
    # Specifies whether a watermark should be applied to a content type by the client application.
    watermark_protection: Optional[watermark_protection_values.WatermarkProtectionValues] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnlineMeeting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeeting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.virtualEventSession":
                from . import virtual_event_session

                return virtual_event_session.VirtualEventSession()
        return OnlineMeeting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import audio_conferencing, broadcast_meeting_settings, call_recording, call_transcript, chat_info, entity, item_body, join_meeting_id_settings, lobby_bypass_settings, meeting_attendance_report, meeting_capabilities, meeting_chat_history_default_mode, meeting_chat_mode, meeting_participants, meeting_registration, online_meeting_presenters, online_meeting_role, virtual_appointment, virtual_event_session, watermark_protection_values

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedPresenters": lambda n : setattr(self, 'allowed_presenters', n.get_enum_value(online_meeting_presenters.OnlineMeetingPresenters)),
            "allowAttendeeToEnableCamera": lambda n : setattr(self, 'allow_attendee_to_enable_camera', n.get_bool_value()),
            "allowAttendeeToEnableMic": lambda n : setattr(self, 'allow_attendee_to_enable_mic', n.get_bool_value()),
            "allowMeetingChat": lambda n : setattr(self, 'allow_meeting_chat', n.get_enum_value(meeting_chat_mode.MeetingChatMode)),
            "allowParticipantsToChangeName": lambda n : setattr(self, 'allow_participants_to_change_name', n.get_bool_value()),
            "allowRecording": lambda n : setattr(self, 'allow_recording', n.get_bool_value()),
            "allowTeamworkReactions": lambda n : setattr(self, 'allow_teamwork_reactions', n.get_bool_value()),
            "allowTranscription": lambda n : setattr(self, 'allow_transcription', n.get_bool_value()),
            "alternativeRecording": lambda n : setattr(self, 'alternative_recording', n.get_bytes_value()),
            "anonymizeIdentityForRoles": lambda n : setattr(self, 'anonymize_identity_for_roles', n.get_collection_of_enum_values(online_meeting_role.OnlineMeetingRole)),
            "attendanceReports": lambda n : setattr(self, 'attendance_reports', n.get_collection_of_object_values(meeting_attendance_report.MeetingAttendanceReport)),
            "attendeeReport": lambda n : setattr(self, 'attendee_report', n.get_bytes_value()),
            "audioConferencing": lambda n : setattr(self, 'audio_conferencing', n.get_object_value(audio_conferencing.AudioConferencing)),
            "broadcastRecording": lambda n : setattr(self, 'broadcast_recording', n.get_bytes_value()),
            "broadcastSettings": lambda n : setattr(self, 'broadcast_settings', n.get_object_value(broadcast_meeting_settings.BroadcastMeetingSettings)),
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_collection_of_enum_values(meeting_capabilities.MeetingCapabilities)),
            "chatInfo": lambda n : setattr(self, 'chat_info', n.get_object_value(chat_info.ChatInfo)),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "isBroadcast": lambda n : setattr(self, 'is_broadcast', n.get_bool_value()),
            "isEntryExitAnnounced": lambda n : setattr(self, 'is_entry_exit_announced', n.get_bool_value()),
            "joinInformation": lambda n : setattr(self, 'join_information', n.get_object_value(item_body.ItemBody)),
            "joinMeetingIdSettings": lambda n : setattr(self, 'join_meeting_id_settings', n.get_object_value(join_meeting_id_settings.JoinMeetingIdSettings)),
            "joinUrl": lambda n : setattr(self, 'join_url', n.get_str_value()),
            "joinWebUrl": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
            "lobbyBypassSettings": lambda n : setattr(self, 'lobby_bypass_settings', n.get_object_value(lobby_bypass_settings.LobbyBypassSettings)),
            "meetingAttendanceReport": lambda n : setattr(self, 'meeting_attendance_report', n.get_object_value(meeting_attendance_report.MeetingAttendanceReport)),
            "participants": lambda n : setattr(self, 'participants', n.get_object_value(meeting_participants.MeetingParticipants)),
            "recording": lambda n : setattr(self, 'recording', n.get_bytes_value()),
            "recordings": lambda n : setattr(self, 'recordings', n.get_collection_of_object_values(call_recording.CallRecording)),
            "recordAutomatically": lambda n : setattr(self, 'record_automatically', n.get_bool_value()),
            "registration": lambda n : setattr(self, 'registration', n.get_object_value(meeting_registration.MeetingRegistration)),
            "shareMeetingChatHistoryDefault": lambda n : setattr(self, 'share_meeting_chat_history_default', n.get_enum_value(meeting_chat_history_default_mode.MeetingChatHistoryDefaultMode)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "transcripts": lambda n : setattr(self, 'transcripts', n.get_collection_of_object_values(call_transcript.CallTranscript)),
            "videoTeleconferenceId": lambda n : setattr(self, 'video_teleconference_id', n.get_str_value()),
            "virtualAppointment": lambda n : setattr(self, 'virtual_appointment', n.get_object_value(virtual_appointment.VirtualAppointment)),
            "watermarkProtection": lambda n : setattr(self, 'watermark_protection', n.get_object_value(watermark_protection_values.WatermarkProtectionValues)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("allowedPresenters", self.allowed_presenters)
        writer.write_bool_value("allowAttendeeToEnableCamera", self.allow_attendee_to_enable_camera)
        writer.write_bool_value("allowAttendeeToEnableMic", self.allow_attendee_to_enable_mic)
        writer.write_enum_value("allowMeetingChat", self.allow_meeting_chat)
        writer.write_bool_value("allowParticipantsToChangeName", self.allow_participants_to_change_name)
        writer.write_bool_value("allowRecording", self.allow_recording)
        writer.write_bool_value("allowTeamworkReactions", self.allow_teamwork_reactions)
        writer.write_bool_value("allowTranscription", self.allow_transcription)
        writer.write_object_value("alternativeRecording", self.alternative_recording)
        writer.write_enum_value("anonymizeIdentityForRoles", self.anonymize_identity_for_roles)
        writer.write_collection_of_object_values("attendanceReports", self.attendance_reports)
        writer.write_object_value("attendeeReport", self.attendee_report)
        writer.write_object_value("audioConferencing", self.audio_conferencing)
        writer.write_object_value("broadcastRecording", self.broadcast_recording)
        writer.write_object_value("broadcastSettings", self.broadcast_settings)
        writer.write_enum_value("capabilities", self.capabilities)
        writer.write_object_value("chatInfo", self.chat_info)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("externalId", self.external_id)
        writer.write_bool_value("isBroadcast", self.is_broadcast)
        writer.write_bool_value("isEntryExitAnnounced", self.is_entry_exit_announced)
        writer.write_object_value("joinInformation", self.join_information)
        writer.write_object_value("joinMeetingIdSettings", self.join_meeting_id_settings)
        writer.write_str_value("joinUrl", self.join_url)
        writer.write_str_value("joinWebUrl", self.join_web_url)
        writer.write_object_value("lobbyBypassSettings", self.lobby_bypass_settings)
        writer.write_object_value("meetingAttendanceReport", self.meeting_attendance_report)
        writer.write_object_value("participants", self.participants)
        writer.write_object_value("recording", self.recording)
        writer.write_collection_of_object_values("recordings", self.recordings)
        writer.write_bool_value("recordAutomatically", self.record_automatically)
        writer.write_object_value("registration", self.registration)
        writer.write_enum_value("shareMeetingChatHistoryDefault", self.share_meeting_chat_history_default)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("subject", self.subject)
        writer.write_collection_of_object_values("transcripts", self.transcripts)
        writer.write_str_value("videoTeleconferenceId", self.video_teleconference_id)
        writer.write_object_value("virtualAppointment", self.virtual_appointment)
        writer.write_object_value("watermarkProtection", self.watermark_protection)
    

