from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audio_routing_group import AudioRoutingGroup
    from .call_direction import CallDirection
    from .call_media_state import CallMediaState
    from .call_options import CallOptions
    from .call_route import CallRoute
    from .call_state import CallState
    from .call_transcription_info import CallTranscriptionInfo
    from .chat_info import ChatInfo
    from .comms_operation import CommsOperation
    from .content_sharing_session import ContentSharingSession
    from .entity import Entity
    from .incoming_context import IncomingContext
    from .invitation_participant_info import InvitationParticipantInfo
    from .media_config import MediaConfig
    from .meeting_capability import MeetingCapability
    from .meeting_info import MeetingInfo
    from .modality import Modality
    from .participant import Participant
    from .participant_info import ParticipantInfo
    from .result_info import ResultInfo
    from .routing_policy import RoutingPolicy
    from .tone_info import ToneInfo

from .entity import Entity

@dataclass
class Call(Entity):
    # The list of active modalities. Possible values are: unknown, audio, video, videoBasedScreenSharing, data. Read-only.
    active_modalities: Optional[List[Modality]] = None
    # The participant that answered the call. Read-only.
    answered_by: Optional[ParticipantInfo] = None
    # The audioRoutingGroups property
    audio_routing_groups: Optional[List[AudioRoutingGroup]] = None
    # A unique identifier for all the participant calls in a conference or a unique identifier for two participant calls in a P2P call.  This needs to be copied over from Microsoft.Graph.Call.CallChainId.
    call_chain_id: Optional[str] = None
    # Contains the optional features for the call.
    call_options: Optional[CallOptions] = None
    # The routing information on how the call was retargeted. Read-only.
    call_routes: Optional[List[CallRoute]] = None
    # The callback URL on which callbacks will be delivered. Must be https.
    callback_uri: Optional[str] = None
    # The chat information. Required information for meeting scenarios.
    chat_info: Optional[ChatInfo] = None
    # The contentSharingSessions property
    content_sharing_sessions: Optional[List[ContentSharingSession]] = None
    # The direction of the call. The possible values are incoming or outgoing. Read-only.
    direction: Optional[CallDirection] = None
    # The context associated with an incoming call. Read-only. Server generated.
    incoming_context: Optional[IncomingContext] = None
    # The media configuration. Required information for creating peer to peer calls or joining meetings.
    media_config: Optional[MediaConfig] = None
    # Read-only. The call media state.
    media_state: Optional[CallMediaState] = None
    # Contains the capabilities of a meeting. Read-only.
    meeting_capability: Optional[MeetingCapability] = None
    # The meeting information. Required information for meeting scenarios.
    meeting_info: Optional[MeetingInfo] = None
    # The myParticipantId property
    my_participant_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operations property
    operations: Optional[List[CommsOperation]] = None
    # The participants property
    participants: Optional[List[Participant]] = None
    # The requestedModalities property
    requested_modalities: Optional[List[Modality]] = None
    # The resultInfo property
    result_info: Optional[ResultInfo] = None
    # The ringingTimeoutInSeconds property
    ringing_timeout_in_seconds: Optional[int] = None
    # The routingPolicies property
    routing_policies: Optional[List[RoutingPolicy]] = None
    # The source property
    source: Optional[ParticipantInfo] = None
    # The state property
    state: Optional[CallState] = None
    # The subject property
    subject: Optional[str] = None
    # The targets property
    targets: Optional[List[InvitationParticipantInfo]] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The terminationReason property
    termination_reason: Optional[str] = None
    # The toneInfo property
    tone_info: Optional[ToneInfo] = None
    # The transcription information for the call. Read-only.
    transcription: Optional[CallTranscriptionInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Call:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Call
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Call()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .audio_routing_group import AudioRoutingGroup
        from .call_direction import CallDirection
        from .call_media_state import CallMediaState
        from .call_options import CallOptions
        from .call_route import CallRoute
        from .call_state import CallState
        from .call_transcription_info import CallTranscriptionInfo
        from .chat_info import ChatInfo
        from .comms_operation import CommsOperation
        from .content_sharing_session import ContentSharingSession
        from .entity import Entity
        from .incoming_context import IncomingContext
        from .invitation_participant_info import InvitationParticipantInfo
        from .media_config import MediaConfig
        from .meeting_capability import MeetingCapability
        from .meeting_info import MeetingInfo
        from .modality import Modality
        from .participant import Participant
        from .participant_info import ParticipantInfo
        from .result_info import ResultInfo
        from .routing_policy import RoutingPolicy
        from .tone_info import ToneInfo

        from .audio_routing_group import AudioRoutingGroup
        from .call_direction import CallDirection
        from .call_media_state import CallMediaState
        from .call_options import CallOptions
        from .call_route import CallRoute
        from .call_state import CallState
        from .call_transcription_info import CallTranscriptionInfo
        from .chat_info import ChatInfo
        from .comms_operation import CommsOperation
        from .content_sharing_session import ContentSharingSession
        from .entity import Entity
        from .incoming_context import IncomingContext
        from .invitation_participant_info import InvitationParticipantInfo
        from .media_config import MediaConfig
        from .meeting_capability import MeetingCapability
        from .meeting_info import MeetingInfo
        from .modality import Modality
        from .participant import Participant
        from .participant_info import ParticipantInfo
        from .result_info import ResultInfo
        from .routing_policy import RoutingPolicy
        from .tone_info import ToneInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "activeModalities": lambda n : setattr(self, 'active_modalities', n.get_collection_of_enum_values(Modality)),
            "answeredBy": lambda n : setattr(self, 'answered_by', n.get_object_value(ParticipantInfo)),
            "audioRoutingGroups": lambda n : setattr(self, 'audio_routing_groups', n.get_collection_of_object_values(AudioRoutingGroup)),
            "callChainId": lambda n : setattr(self, 'call_chain_id', n.get_str_value()),
            "callOptions": lambda n : setattr(self, 'call_options', n.get_object_value(CallOptions)),
            "callRoutes": lambda n : setattr(self, 'call_routes', n.get_collection_of_object_values(CallRoute)),
            "callbackUri": lambda n : setattr(self, 'callback_uri', n.get_str_value()),
            "chatInfo": lambda n : setattr(self, 'chat_info', n.get_object_value(ChatInfo)),
            "contentSharingSessions": lambda n : setattr(self, 'content_sharing_sessions', n.get_collection_of_object_values(ContentSharingSession)),
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(CallDirection)),
            "incomingContext": lambda n : setattr(self, 'incoming_context', n.get_object_value(IncomingContext)),
            "mediaConfig": lambda n : setattr(self, 'media_config', n.get_object_value(MediaConfig)),
            "mediaState": lambda n : setattr(self, 'media_state', n.get_object_value(CallMediaState)),
            "meetingCapability": lambda n : setattr(self, 'meeting_capability', n.get_object_value(MeetingCapability)),
            "meetingInfo": lambda n : setattr(self, 'meeting_info', n.get_object_value(MeetingInfo)),
            "myParticipantId": lambda n : setattr(self, 'my_participant_id', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(CommsOperation)),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(Participant)),
            "requestedModalities": lambda n : setattr(self, 'requested_modalities', n.get_collection_of_enum_values(Modality)),
            "resultInfo": lambda n : setattr(self, 'result_info', n.get_object_value(ResultInfo)),
            "ringingTimeoutInSeconds": lambda n : setattr(self, 'ringing_timeout_in_seconds', n.get_int_value()),
            "routingPolicies": lambda n : setattr(self, 'routing_policies', n.get_collection_of_enum_values(RoutingPolicy)),
            "source": lambda n : setattr(self, 'source', n.get_object_value(ParticipantInfo)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(CallState)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(InvitationParticipantInfo)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "terminationReason": lambda n : setattr(self, 'termination_reason', n.get_str_value()),
            "toneInfo": lambda n : setattr(self, 'tone_info', n.get_object_value(ToneInfo)),
            "transcription": lambda n : setattr(self, 'transcription', n.get_object_value(CallTranscriptionInfo)),
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
        writer.write_collection_of_enum_values("activeModalities", self.active_modalities)
        writer.write_object_value("answeredBy", self.answered_by)
        writer.write_collection_of_object_values("audioRoutingGroups", self.audio_routing_groups)
        writer.write_str_value("callChainId", self.call_chain_id)
        writer.write_object_value("callOptions", self.call_options)
        writer.write_collection_of_object_values("callRoutes", self.call_routes)
        writer.write_str_value("callbackUri", self.callback_uri)
        writer.write_object_value("chatInfo", self.chat_info)
        writer.write_collection_of_object_values("contentSharingSessions", self.content_sharing_sessions)
        writer.write_enum_value("direction", self.direction)
        writer.write_object_value("incomingContext", self.incoming_context)
        writer.write_object_value("mediaConfig", self.media_config)
        writer.write_object_value("mediaState", self.media_state)
        writer.write_object_value("meetingCapability", self.meeting_capability)
        writer.write_object_value("meetingInfo", self.meeting_info)
        writer.write_str_value("myParticipantId", self.my_participant_id)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("participants", self.participants)
        writer.write_collection_of_enum_values("requestedModalities", self.requested_modalities)
        writer.write_object_value("resultInfo", self.result_info)
        writer.write_int_value("ringingTimeoutInSeconds", self.ringing_timeout_in_seconds)
        writer.write_collection_of_enum_values("routingPolicies", self.routing_policies)
        writer.write_object_value("source", self.source)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("subject", self.subject)
        writer.write_collection_of_object_values("targets", self.targets)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("terminationReason", self.termination_reason)
        writer.write_object_value("toneInfo", self.tone_info)
        writer.write_object_value("transcription", self.transcription)
    

