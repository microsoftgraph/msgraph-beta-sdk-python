from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audio_conferencing import AudioConferencing
    from .broadcast_meeting_settings import BroadcastMeetingSettings
    from .call_recording import CallRecording
    from .call_transcript import CallTranscript
    from .chat_info import ChatInfo
    from .chat_restrictions import ChatRestrictions
    from .entity import Entity
    from .item_body import ItemBody
    from .join_meeting_id_settings import JoinMeetingIdSettings
    from .lobby_bypass_settings import LobbyBypassSettings
    from .meeting_attendance_report import MeetingAttendanceReport
    from .meeting_capabilities import MeetingCapabilities
    from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
    from .meeting_chat_mode import MeetingChatMode
    from .meeting_participants import MeetingParticipants
    from .meeting_registration import MeetingRegistration
    from .online_meeting_presenters import OnlineMeetingPresenters
    from .online_meeting_role import OnlineMeetingRole
    from .virtual_event_session import VirtualEventSession
    from .watermark_protection_values import WatermarkProtectionValues

from .entity import Entity

@dataclass
class OnlineMeeting(Entity):
    # Indicates whether attendees can turn on their camera.
    allow_attendee_to_enable_camera: Optional[bool] = None
    # Indicates whether attendees can turn on their microphone.
    allow_attendee_to_enable_mic: Optional[bool] = None
    # Specifies the mode of meeting chat.
    allow_meeting_chat: Optional[MeetingChatMode] = None
    # Specifies if participants are allowed to rename themselves in an instance of the meeting.
    allow_participants_to_change_name: Optional[bool] = None
    # Indicates whether recording is enabled for the meeting.
    allow_recording: Optional[bool] = None
    # Indicates if Teams reactions are enabled for the meeting.
    allow_teamwork_reactions: Optional[bool] = None
    # Indicates whether transcription is enabled for the meeting.
    allow_transcription: Optional[bool] = None
    # Specifies who can be a presenter in a meeting.
    allowed_presenters: Optional[OnlineMeetingPresenters] = None
    # The alternativeRecording property
    alternative_recording: Optional[bytes] = None
    # Specifies whose identity will be anonymized in the meeting. Possible values are: attendee. The attendee value cannot be removed through a PATCH operation once added.
    anonymize_identity_for_roles: Optional[List[OnlineMeetingRole]] = None
    # The attendance reports of an online meeting. Read-only.
    attendance_reports: Optional[List[MeetingAttendanceReport]] = None
    # The attendeeReport property
    attendee_report: Optional[bytes] = None
    # The phone access (dial-in) information for an online meeting. Read-only.
    audio_conferencing: Optional[AudioConferencing] = None
    # The broadcastRecording property
    broadcast_recording: Optional[bytes] = None
    # The broadcastSettings property
    broadcast_settings: Optional[BroadcastMeetingSettings] = None
    # The capabilities property
    capabilities: Optional[List[MeetingCapabilities]] = None
    # The chat information associated with this online meeting.
    chat_info: Optional[ChatInfo] = None
    # The chatRestrictions property
    chat_restrictions: Optional[ChatRestrictions] = None
    # The meeting creation time in UTC. Read-only.
    creation_date_time: Optional[datetime.datetime] = None
    # The meeting end time in UTC.
    end_date_time: Optional[datetime.datetime] = None
    # The external ID. A custom ID. Optional.
    external_id: Optional[str] = None
    # The isBroadcast property
    is_broadcast: Optional[bool] = None
    # The isEndToEndEncryptionEnabled property
    is_end_to_end_encryption_enabled: Optional[bool] = None
    # Indicates whether to announce when callers join or leave.
    is_entry_exit_announced: Optional[bool] = None
    # The join information in the language and locale variant specified in 'Accept-Language' request HTTP header. Read-only.
    join_information: Optional[ItemBody] = None
    # Specifies the joinMeetingId, the meeting passcode, and the requirement for the passcode. Once an onlineMeeting is created, the joinMeetingIdSettings cannot be modified. To make any changes to this property, the meeting needs to be canceled and a new one needs to be created.
    join_meeting_id_settings: Optional[JoinMeetingIdSettings] = None
    # The joinUrl property
    join_url: Optional[str] = None
    # The join URL of the online meeting. Read-only.
    join_web_url: Optional[str] = None
    # Specifies which participants can bypass the meeting lobby.
    lobby_bypass_settings: Optional[LobbyBypassSettings] = None
    # The meetingAttendanceReport property
    meeting_attendance_report: Optional[MeetingAttendanceReport] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The participants associated with the online meeting. This includes the organizer and the attendees.
    participants: Optional[MeetingParticipants] = None
    # Indicates whether to record the meeting automatically.
    record_automatically: Optional[bool] = None
    # The recording property
    recording: Optional[bytes] = None
    # The recordings of an online meeting. Read-only.
    recordings: Optional[List[CallRecording]] = None
    # The registration that has been enabled for an online meeting. One online meeting can only have one registration enabled.
    registration: Optional[MeetingRegistration] = None
    # Specifies whether meeting chat history is shared with participants.  Possible values are: all, none, unknownFutureValue.
    share_meeting_chat_history_default: Optional[MeetingChatHistoryDefaultMode] = None
    # The meeting start time in UTC.
    start_date_time: Optional[datetime.datetime] = None
    # The subject of the online meeting.
    subject: Optional[str] = None
    # The transcripts of an online meeting. Read-only.
    transcripts: Optional[List[CallTranscript]] = None
    # The video teleconferencing ID. Read-only.
    video_teleconference_id: Optional[str] = None
    # Specifies whether a watermark should be applied to a content type by the client application.
    watermark_protection: Optional[WatermarkProtectionValues] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnlineMeeting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeeting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventSession".casefold():
            from .virtual_event_session import VirtualEventSession

            return VirtualEventSession()
        return OnlineMeeting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .audio_conferencing import AudioConferencing
        from .broadcast_meeting_settings import BroadcastMeetingSettings
        from .call_recording import CallRecording
        from .call_transcript import CallTranscript
        from .chat_info import ChatInfo
        from .chat_restrictions import ChatRestrictions
        from .entity import Entity
        from .item_body import ItemBody
        from .join_meeting_id_settings import JoinMeetingIdSettings
        from .lobby_bypass_settings import LobbyBypassSettings
        from .meeting_attendance_report import MeetingAttendanceReport
        from .meeting_capabilities import MeetingCapabilities
        from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
        from .meeting_chat_mode import MeetingChatMode
        from .meeting_participants import MeetingParticipants
        from .meeting_registration import MeetingRegistration
        from .online_meeting_presenters import OnlineMeetingPresenters
        from .online_meeting_role import OnlineMeetingRole
        from .virtual_event_session import VirtualEventSession
        from .watermark_protection_values import WatermarkProtectionValues

        from .audio_conferencing import AudioConferencing
        from .broadcast_meeting_settings import BroadcastMeetingSettings
        from .call_recording import CallRecording
        from .call_transcript import CallTranscript
        from .chat_info import ChatInfo
        from .chat_restrictions import ChatRestrictions
        from .entity import Entity
        from .item_body import ItemBody
        from .join_meeting_id_settings import JoinMeetingIdSettings
        from .lobby_bypass_settings import LobbyBypassSettings
        from .meeting_attendance_report import MeetingAttendanceReport
        from .meeting_capabilities import MeetingCapabilities
        from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
        from .meeting_chat_mode import MeetingChatMode
        from .meeting_participants import MeetingParticipants
        from .meeting_registration import MeetingRegistration
        from .online_meeting_presenters import OnlineMeetingPresenters
        from .online_meeting_role import OnlineMeetingRole
        from .virtual_event_session import VirtualEventSession
        from .watermark_protection_values import WatermarkProtectionValues

        fields: Dict[str, Callable[[Any], None]] = {
            "allowAttendeeToEnableCamera": lambda n : setattr(self, 'allow_attendee_to_enable_camera', n.get_bool_value()),
            "allowAttendeeToEnableMic": lambda n : setattr(self, 'allow_attendee_to_enable_mic', n.get_bool_value()),
            "allowMeetingChat": lambda n : setattr(self, 'allow_meeting_chat', n.get_enum_value(MeetingChatMode)),
            "allowParticipantsToChangeName": lambda n : setattr(self, 'allow_participants_to_change_name', n.get_bool_value()),
            "allowRecording": lambda n : setattr(self, 'allow_recording', n.get_bool_value()),
            "allowTeamworkReactions": lambda n : setattr(self, 'allow_teamwork_reactions', n.get_bool_value()),
            "allowTranscription": lambda n : setattr(self, 'allow_transcription', n.get_bool_value()),
            "allowedPresenters": lambda n : setattr(self, 'allowed_presenters', n.get_enum_value(OnlineMeetingPresenters)),
            "alternativeRecording": lambda n : setattr(self, 'alternative_recording', n.get_bytes_value()),
            "anonymizeIdentityForRoles": lambda n : setattr(self, 'anonymize_identity_for_roles', n.get_collection_of_enum_values(OnlineMeetingRole)),
            "attendanceReports": lambda n : setattr(self, 'attendance_reports', n.get_collection_of_object_values(MeetingAttendanceReport)),
            "attendeeReport": lambda n : setattr(self, 'attendee_report', n.get_bytes_value()),
            "audioConferencing": lambda n : setattr(self, 'audio_conferencing', n.get_object_value(AudioConferencing)),
            "broadcastRecording": lambda n : setattr(self, 'broadcast_recording', n.get_bytes_value()),
            "broadcastSettings": lambda n : setattr(self, 'broadcast_settings', n.get_object_value(BroadcastMeetingSettings)),
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_collection_of_enum_values(MeetingCapabilities)),
            "chatInfo": lambda n : setattr(self, 'chat_info', n.get_object_value(ChatInfo)),
            "chatRestrictions": lambda n : setattr(self, 'chat_restrictions', n.get_object_value(ChatRestrictions)),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "isBroadcast": lambda n : setattr(self, 'is_broadcast', n.get_bool_value()),
            "isEndToEndEncryptionEnabled": lambda n : setattr(self, 'is_end_to_end_encryption_enabled', n.get_bool_value()),
            "isEntryExitAnnounced": lambda n : setattr(self, 'is_entry_exit_announced', n.get_bool_value()),
            "joinInformation": lambda n : setattr(self, 'join_information', n.get_object_value(ItemBody)),
            "joinMeetingIdSettings": lambda n : setattr(self, 'join_meeting_id_settings', n.get_object_value(JoinMeetingIdSettings)),
            "joinUrl": lambda n : setattr(self, 'join_url', n.get_str_value()),
            "joinWebUrl": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
            "lobbyBypassSettings": lambda n : setattr(self, 'lobby_bypass_settings', n.get_object_value(LobbyBypassSettings)),
            "meetingAttendanceReport": lambda n : setattr(self, 'meeting_attendance_report', n.get_object_value(MeetingAttendanceReport)),
            "participants": lambda n : setattr(self, 'participants', n.get_object_value(MeetingParticipants)),
            "recordAutomatically": lambda n : setattr(self, 'record_automatically', n.get_bool_value()),
            "recording": lambda n : setattr(self, 'recording', n.get_bytes_value()),
            "recordings": lambda n : setattr(self, 'recordings', n.get_collection_of_object_values(CallRecording)),
            "registration": lambda n : setattr(self, 'registration', n.get_object_value(MeetingRegistration)),
            "shareMeetingChatHistoryDefault": lambda n : setattr(self, 'share_meeting_chat_history_default', n.get_enum_value(MeetingChatHistoryDefaultMode)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "transcripts": lambda n : setattr(self, 'transcripts', n.get_collection_of_object_values(CallTranscript)),
            "videoTeleconferenceId": lambda n : setattr(self, 'video_teleconference_id', n.get_str_value()),
            "watermarkProtection": lambda n : setattr(self, 'watermark_protection', n.get_object_value(WatermarkProtectionValues)),
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
        writer.write_bool_value("allowAttendeeToEnableCamera", self.allow_attendee_to_enable_camera)
        writer.write_bool_value("allowAttendeeToEnableMic", self.allow_attendee_to_enable_mic)
        writer.write_enum_value("allowMeetingChat", self.allow_meeting_chat)
        writer.write_bool_value("allowParticipantsToChangeName", self.allow_participants_to_change_name)
        writer.write_bool_value("allowRecording", self.allow_recording)
        writer.write_bool_value("allowTeamworkReactions", self.allow_teamwork_reactions)
        writer.write_bool_value("allowTranscription", self.allow_transcription)
        writer.write_enum_value("allowedPresenters", self.allowed_presenters)
        writer.write_bytes_value("alternativeRecording", self.alternative_recording)
        writer.write_collection_of_enum_values("anonymizeIdentityForRoles", self.anonymize_identity_for_roles)
        writer.write_collection_of_object_values("attendanceReports", self.attendance_reports)
        writer.write_bytes_value("attendeeReport", self.attendee_report)
        writer.write_object_value("audioConferencing", self.audio_conferencing)
        writer.write_bytes_value("broadcastRecording", self.broadcast_recording)
        writer.write_object_value("broadcastSettings", self.broadcast_settings)
        writer.write_collection_of_enum_values("capabilities", self.capabilities)
        writer.write_object_value("chatInfo", self.chat_info)
        writer.write_object_value("chatRestrictions", self.chat_restrictions)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("externalId", self.external_id)
        writer.write_bool_value("isBroadcast", self.is_broadcast)
        writer.write_bool_value("isEndToEndEncryptionEnabled", self.is_end_to_end_encryption_enabled)
        writer.write_bool_value("isEntryExitAnnounced", self.is_entry_exit_announced)
        writer.write_object_value("joinInformation", self.join_information)
        writer.write_object_value("joinMeetingIdSettings", self.join_meeting_id_settings)
        writer.write_str_value("joinUrl", self.join_url)
        writer.write_str_value("joinWebUrl", self.join_web_url)
        writer.write_object_value("lobbyBypassSettings", self.lobby_bypass_settings)
        writer.write_object_value("meetingAttendanceReport", self.meeting_attendance_report)
        writer.write_object_value("participants", self.participants)
        writer.write_bool_value("recordAutomatically", self.record_automatically)
        writer.write_bytes_value("recording", self.recording)
        writer.write_collection_of_object_values("recordings", self.recordings)
        writer.write_object_value("registration", self.registration)
        writer.write_enum_value("shareMeetingChatHistoryDefault", self.share_meeting_chat_history_default)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("subject", self.subject)
        writer.write_collection_of_object_values("transcripts", self.transcripts)
        writer.write_str_value("videoTeleconferenceId", self.video_teleconference_id)
        writer.write_object_value("watermarkProtection", self.watermark_protection)
    

