from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audio_conferencing import AudioConferencing
    from .chat_info import ChatInfo
    from .chat_restrictions import ChatRestrictions
    from .entity import Entity
    from .item_body import ItemBody
    from .join_meeting_id_settings import JoinMeetingIdSettings
    from .lobby_bypass_settings import LobbyBypassSettings
    from .meeting_attendance_report import MeetingAttendanceReport
    from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
    from .meeting_chat_mode import MeetingChatMode
    from .online_meeting import OnlineMeeting
    from .online_meeting_presenters import OnlineMeetingPresenters
    from .online_meeting_role import OnlineMeetingRole
    from .virtual_event_session import VirtualEventSession
    from .watermark_protection_values import WatermarkProtectionValues

from .entity import Entity

@dataclass
class OnlineMeetingBase(Entity):
    # The allowAttendeeToEnableCamera property
    allow_attendee_to_enable_camera: Optional[bool] = None
    # The allowAttendeeToEnableMic property
    allow_attendee_to_enable_mic: Optional[bool] = None
    # The allowMeetingChat property
    allow_meeting_chat: Optional[MeetingChatMode] = None
    # The allowParticipantsToChangeName property
    allow_participants_to_change_name: Optional[bool] = None
    # The allowRecording property
    allow_recording: Optional[bool] = None
    # The allowTeamworkReactions property
    allow_teamwork_reactions: Optional[bool] = None
    # The allowTranscription property
    allow_transcription: Optional[bool] = None
    # The allowedPresenters property
    allowed_presenters: Optional[OnlineMeetingPresenters] = None
    # The anonymizeIdentityForRoles property
    anonymize_identity_for_roles: Optional[List[OnlineMeetingRole]] = None
    # The attendanceReports property
    attendance_reports: Optional[List[MeetingAttendanceReport]] = None
    # The audioConferencing property
    audio_conferencing: Optional[AudioConferencing] = None
    # The chatInfo property
    chat_info: Optional[ChatInfo] = None
    # The chatRestrictions property
    chat_restrictions: Optional[ChatRestrictions] = None
    # The isEndToEndEncryptionEnabled property
    is_end_to_end_encryption_enabled: Optional[bool] = None
    # The isEntryExitAnnounced property
    is_entry_exit_announced: Optional[bool] = None
    # The joinInformation property
    join_information: Optional[ItemBody] = None
    # The joinMeetingIdSettings property
    join_meeting_id_settings: Optional[JoinMeetingIdSettings] = None
    # The joinWebUrl property
    join_web_url: Optional[str] = None
    # The lobbyBypassSettings property
    lobby_bypass_settings: Optional[LobbyBypassSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recordAutomatically property
    record_automatically: Optional[bool] = None
    # The shareMeetingChatHistoryDefault property
    share_meeting_chat_history_default: Optional[MeetingChatHistoryDefaultMode] = None
    # The subject property
    subject: Optional[str] = None
    # The videoTeleconferenceId property
    video_teleconference_id: Optional[str] = None
    # The watermarkProtection property
    watermark_protection: Optional[WatermarkProtectionValues] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnlineMeetingBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeetingBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onlineMeeting".casefold():
            from .online_meeting import OnlineMeeting

            return OnlineMeeting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventSession".casefold():
            from .virtual_event_session import VirtualEventSession

            return VirtualEventSession()
        return OnlineMeetingBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .audio_conferencing import AudioConferencing
        from .chat_info import ChatInfo
        from .chat_restrictions import ChatRestrictions
        from .entity import Entity
        from .item_body import ItemBody
        from .join_meeting_id_settings import JoinMeetingIdSettings
        from .lobby_bypass_settings import LobbyBypassSettings
        from .meeting_attendance_report import MeetingAttendanceReport
        from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
        from .meeting_chat_mode import MeetingChatMode
        from .online_meeting import OnlineMeeting
        from .online_meeting_presenters import OnlineMeetingPresenters
        from .online_meeting_role import OnlineMeetingRole
        from .virtual_event_session import VirtualEventSession
        from .watermark_protection_values import WatermarkProtectionValues

        from .audio_conferencing import AudioConferencing
        from .chat_info import ChatInfo
        from .chat_restrictions import ChatRestrictions
        from .entity import Entity
        from .item_body import ItemBody
        from .join_meeting_id_settings import JoinMeetingIdSettings
        from .lobby_bypass_settings import LobbyBypassSettings
        from .meeting_attendance_report import MeetingAttendanceReport
        from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
        from .meeting_chat_mode import MeetingChatMode
        from .online_meeting import OnlineMeeting
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
            "anonymizeIdentityForRoles": lambda n : setattr(self, 'anonymize_identity_for_roles', n.get_collection_of_enum_values(OnlineMeetingRole)),
            "attendanceReports": lambda n : setattr(self, 'attendance_reports', n.get_collection_of_object_values(MeetingAttendanceReport)),
            "audioConferencing": lambda n : setattr(self, 'audio_conferencing', n.get_object_value(AudioConferencing)),
            "chatInfo": lambda n : setattr(self, 'chat_info', n.get_object_value(ChatInfo)),
            "chatRestrictions": lambda n : setattr(self, 'chat_restrictions', n.get_object_value(ChatRestrictions)),
            "isEndToEndEncryptionEnabled": lambda n : setattr(self, 'is_end_to_end_encryption_enabled', n.get_bool_value()),
            "isEntryExitAnnounced": lambda n : setattr(self, 'is_entry_exit_announced', n.get_bool_value()),
            "joinInformation": lambda n : setattr(self, 'join_information', n.get_object_value(ItemBody)),
            "joinMeetingIdSettings": lambda n : setattr(self, 'join_meeting_id_settings', n.get_object_value(JoinMeetingIdSettings)),
            "joinWebUrl": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
            "lobbyBypassSettings": lambda n : setattr(self, 'lobby_bypass_settings', n.get_object_value(LobbyBypassSettings)),
            "recordAutomatically": lambda n : setattr(self, 'record_automatically', n.get_bool_value()),
            "shareMeetingChatHistoryDefault": lambda n : setattr(self, 'share_meeting_chat_history_default', n.get_enum_value(MeetingChatHistoryDefaultMode)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
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
        writer.write_collection_of_enum_values("anonymizeIdentityForRoles", self.anonymize_identity_for_roles)
        writer.write_collection_of_object_values("attendanceReports", self.attendance_reports)
        writer.write_object_value("audioConferencing", self.audio_conferencing)
        writer.write_object_value("chatInfo", self.chat_info)
        writer.write_object_value("chatRestrictions", self.chat_restrictions)
        writer.write_bool_value("isEndToEndEncryptionEnabled", self.is_end_to_end_encryption_enabled)
        writer.write_bool_value("isEntryExitAnnounced", self.is_entry_exit_announced)
        writer.write_object_value("joinInformation", self.join_information)
        writer.write_object_value("joinMeetingIdSettings", self.join_meeting_id_settings)
        writer.write_str_value("joinWebUrl", self.join_web_url)
        writer.write_object_value("lobbyBypassSettings", self.lobby_bypass_settings)
        writer.write_bool_value("recordAutomatically", self.record_automatically)
        writer.write_enum_value("shareMeetingChatHistoryDefault", self.share_meeting_chat_history_default)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("videoTeleconferenceId", self.video_teleconference_id)
        writer.write_object_value("watermarkProtection", self.watermark_protection)
    

