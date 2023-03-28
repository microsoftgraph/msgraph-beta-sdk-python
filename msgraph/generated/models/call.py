from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import audio_routing_group, call_direction, call_media_state, call_options, call_route, call_state, call_transcription_info, chat_info, comms_operation, content_sharing_session, entity, incoming_context, invitation_participant_info, media_config, meeting_capability, meeting_info, modality, participant, participant_info, result_info, routing_policy, tone_info

from . import entity

class Call(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new call and sets the default values.
        """
        super().__init__()
        # The list of active modalities. Possible values are: unknown, audio, video, videoBasedScreenSharing, data. Read-only.
        self._active_modalities: Optional[List[modality.Modality]] = None
        # The participant that answered the call. Read-only.
        self._answered_by: Optional[participant_info.ParticipantInfo] = None
        # The audioRoutingGroups property
        self._audio_routing_groups: Optional[List[audio_routing_group.AudioRoutingGroup]] = None
        # A unique identifier for all the participant calls in a conference or a unique identifier for two participant calls in a P2P call.  This needs to be copied over from Microsoft.Graph.Call.CallChainId.
        self._call_chain_id: Optional[str] = None
        # Contains the optional features for the call.
        self._call_options: Optional[call_options.CallOptions] = None
        # The routing information on how the call was retargeted. Read-only.
        self._call_routes: Optional[List[call_route.CallRoute]] = None
        # The callback URL on which callbacks will be delivered. Must be https.
        self._callback_uri: Optional[str] = None
        # The chat information. Required information for meeting scenarios.
        self._chat_info: Optional[chat_info.ChatInfo] = None
        # The contentSharingSessions property
        self._content_sharing_sessions: Optional[List[content_sharing_session.ContentSharingSession]] = None
        # The direction of the call. The possible value are incoming or outgoing. Read-only.
        self._direction: Optional[call_direction.CallDirection] = None
        # The context associated with an incoming call. Read-only. Server generated.
        self._incoming_context: Optional[incoming_context.IncomingContext] = None
        # The media configuration. Required information for creating peer to peer calls or joining meetings.
        self._media_config: Optional[media_config.MediaConfig] = None
        # Read-only. The call media state.
        self._media_state: Optional[call_media_state.CallMediaState] = None
        # Contains the capabilities of a meeting. Read-only.
        self._meeting_capability: Optional[meeting_capability.MeetingCapability] = None
        # The meeting information. Required information for meeting scenarios.
        self._meeting_info: Optional[meeting_info.MeetingInfo] = None
        # The myParticipantId property
        self._my_participant_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The operations property
        self._operations: Optional[List[comms_operation.CommsOperation]] = None
        # The participants property
        self._participants: Optional[List[participant.Participant]] = None
        # The requestedModalities property
        self._requested_modalities: Optional[List[modality.Modality]] = None
        # The resultInfo property
        self._result_info: Optional[result_info.ResultInfo] = None
        # The ringingTimeoutInSeconds property
        self._ringing_timeout_in_seconds: Optional[int] = None
        # The routingPolicies property
        self._routing_policies: Optional[List[routing_policy.RoutingPolicy]] = None
        # The source property
        self._source: Optional[participant_info.ParticipantInfo] = None
        # The state property
        self._state: Optional[call_state.CallState] = None
        # The subject property
        self._subject: Optional[str] = None
        # The targets property
        self._targets: Optional[List[invitation_participant_info.InvitationParticipantInfo]] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
        # The terminationReason property
        self._termination_reason: Optional[str] = None
        # The toneInfo property
        self._tone_info: Optional[tone_info.ToneInfo] = None
        # The transcription information for the call. Read-only.
        self._transcription: Optional[call_transcription_info.CallTranscriptionInfo] = None
    
    @property
    def active_modalities(self,) -> Optional[List[modality.Modality]]:
        """
        Gets the activeModalities property value. The list of active modalities. Possible values are: unknown, audio, video, videoBasedScreenSharing, data. Read-only.
        Returns: Optional[List[modality.Modality]]
        """
        return self._active_modalities
    
    @active_modalities.setter
    def active_modalities(self,value: Optional[List[modality.Modality]] = None) -> None:
        """
        Sets the activeModalities property value. The list of active modalities. Possible values are: unknown, audio, video, videoBasedScreenSharing, data. Read-only.
        Args:
            value: Value to set for the active_modalities property.
        """
        self._active_modalities = value
    
    @property
    def answered_by(self,) -> Optional[participant_info.ParticipantInfo]:
        """
        Gets the answeredBy property value. The participant that answered the call. Read-only.
        Returns: Optional[participant_info.ParticipantInfo]
        """
        return self._answered_by
    
    @answered_by.setter
    def answered_by(self,value: Optional[participant_info.ParticipantInfo] = None) -> None:
        """
        Sets the answeredBy property value. The participant that answered the call. Read-only.
        Args:
            value: Value to set for the answered_by property.
        """
        self._answered_by = value
    
    @property
    def audio_routing_groups(self,) -> Optional[List[audio_routing_group.AudioRoutingGroup]]:
        """
        Gets the audioRoutingGroups property value. The audioRoutingGroups property
        Returns: Optional[List[audio_routing_group.AudioRoutingGroup]]
        """
        return self._audio_routing_groups
    
    @audio_routing_groups.setter
    def audio_routing_groups(self,value: Optional[List[audio_routing_group.AudioRoutingGroup]] = None) -> None:
        """
        Sets the audioRoutingGroups property value. The audioRoutingGroups property
        Args:
            value: Value to set for the audio_routing_groups property.
        """
        self._audio_routing_groups = value
    
    @property
    def call_chain_id(self,) -> Optional[str]:
        """
        Gets the callChainId property value. A unique identifier for all the participant calls in a conference or a unique identifier for two participant calls in a P2P call.  This needs to be copied over from Microsoft.Graph.Call.CallChainId.
        Returns: Optional[str]
        """
        return self._call_chain_id
    
    @call_chain_id.setter
    def call_chain_id(self,value: Optional[str] = None) -> None:
        """
        Sets the callChainId property value. A unique identifier for all the participant calls in a conference or a unique identifier for two participant calls in a P2P call.  This needs to be copied over from Microsoft.Graph.Call.CallChainId.
        Args:
            value: Value to set for the call_chain_id property.
        """
        self._call_chain_id = value
    
    @property
    def call_options(self,) -> Optional[call_options.CallOptions]:
        """
        Gets the callOptions property value. Contains the optional features for the call.
        Returns: Optional[call_options.CallOptions]
        """
        return self._call_options
    
    @call_options.setter
    def call_options(self,value: Optional[call_options.CallOptions] = None) -> None:
        """
        Sets the callOptions property value. Contains the optional features for the call.
        Args:
            value: Value to set for the call_options property.
        """
        self._call_options = value
    
    @property
    def call_routes(self,) -> Optional[List[call_route.CallRoute]]:
        """
        Gets the callRoutes property value. The routing information on how the call was retargeted. Read-only.
        Returns: Optional[List[call_route.CallRoute]]
        """
        return self._call_routes
    
    @call_routes.setter
    def call_routes(self,value: Optional[List[call_route.CallRoute]] = None) -> None:
        """
        Sets the callRoutes property value. The routing information on how the call was retargeted. Read-only.
        Args:
            value: Value to set for the call_routes property.
        """
        self._call_routes = value
    
    @property
    def callback_uri(self,) -> Optional[str]:
        """
        Gets the callbackUri property value. The callback URL on which callbacks will be delivered. Must be https.
        Returns: Optional[str]
        """
        return self._callback_uri
    
    @callback_uri.setter
    def callback_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the callbackUri property value. The callback URL on which callbacks will be delivered. Must be https.
        Args:
            value: Value to set for the callback_uri property.
        """
        self._callback_uri = value
    
    @property
    def chat_info(self,) -> Optional[chat_info.ChatInfo]:
        """
        Gets the chatInfo property value. The chat information. Required information for meeting scenarios.
        Returns: Optional[chat_info.ChatInfo]
        """
        return self._chat_info
    
    @chat_info.setter
    def chat_info(self,value: Optional[chat_info.ChatInfo] = None) -> None:
        """
        Sets the chatInfo property value. The chat information. Required information for meeting scenarios.
        Args:
            value: Value to set for the chat_info property.
        """
        self._chat_info = value
    
    @property
    def content_sharing_sessions(self,) -> Optional[List[content_sharing_session.ContentSharingSession]]:
        """
        Gets the contentSharingSessions property value. The contentSharingSessions property
        Returns: Optional[List[content_sharing_session.ContentSharingSession]]
        """
        return self._content_sharing_sessions
    
    @content_sharing_sessions.setter
    def content_sharing_sessions(self,value: Optional[List[content_sharing_session.ContentSharingSession]] = None) -> None:
        """
        Sets the contentSharingSessions property value. The contentSharingSessions property
        Args:
            value: Value to set for the content_sharing_sessions property.
        """
        self._content_sharing_sessions = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Call:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Call
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Call()
    
    @property
    def direction(self,) -> Optional[call_direction.CallDirection]:
        """
        Gets the direction property value. The direction of the call. The possible value are incoming or outgoing. Read-only.
        Returns: Optional[call_direction.CallDirection]
        """
        return self._direction
    
    @direction.setter
    def direction(self,value: Optional[call_direction.CallDirection] = None) -> None:
        """
        Sets the direction property value. The direction of the call. The possible value are incoming or outgoing. Read-only.
        Args:
            value: Value to set for the direction property.
        """
        self._direction = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import audio_routing_group, call_direction, call_media_state, call_options, call_route, call_state, call_transcription_info, chat_info, comms_operation, content_sharing_session, entity, incoming_context, invitation_participant_info, media_config, meeting_capability, meeting_info, modality, participant, participant_info, result_info, routing_policy, tone_info

        fields: Dict[str, Callable[[Any], None]] = {
            "activeModalities": lambda n : setattr(self, 'active_modalities', n.get_collection_of_enum_values(modality.Modality)),
            "answeredBy": lambda n : setattr(self, 'answered_by', n.get_object_value(participant_info.ParticipantInfo)),
            "audioRoutingGroups": lambda n : setattr(self, 'audio_routing_groups', n.get_collection_of_object_values(audio_routing_group.AudioRoutingGroup)),
            "callbackUri": lambda n : setattr(self, 'callback_uri', n.get_str_value()),
            "callChainId": lambda n : setattr(self, 'call_chain_id', n.get_str_value()),
            "callOptions": lambda n : setattr(self, 'call_options', n.get_object_value(call_options.CallOptions)),
            "callRoutes": lambda n : setattr(self, 'call_routes', n.get_collection_of_object_values(call_route.CallRoute)),
            "chatInfo": lambda n : setattr(self, 'chat_info', n.get_object_value(chat_info.ChatInfo)),
            "contentSharingSessions": lambda n : setattr(self, 'content_sharing_sessions', n.get_collection_of_object_values(content_sharing_session.ContentSharingSession)),
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(call_direction.CallDirection)),
            "incomingContext": lambda n : setattr(self, 'incoming_context', n.get_object_value(incoming_context.IncomingContext)),
            "mediaConfig": lambda n : setattr(self, 'media_config', n.get_object_value(media_config.MediaConfig)),
            "mediaState": lambda n : setattr(self, 'media_state', n.get_object_value(call_media_state.CallMediaState)),
            "meetingCapability": lambda n : setattr(self, 'meeting_capability', n.get_object_value(meeting_capability.MeetingCapability)),
            "meetingInfo": lambda n : setattr(self, 'meeting_info', n.get_object_value(meeting_info.MeetingInfo)),
            "myParticipantId": lambda n : setattr(self, 'my_participant_id', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(comms_operation.CommsOperation)),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(participant.Participant)),
            "requestedModalities": lambda n : setattr(self, 'requested_modalities', n.get_collection_of_enum_values(modality.Modality)),
            "resultInfo": lambda n : setattr(self, 'result_info', n.get_object_value(result_info.ResultInfo)),
            "ringingTimeoutInSeconds": lambda n : setattr(self, 'ringing_timeout_in_seconds', n.get_int_value()),
            "routingPolicies": lambda n : setattr(self, 'routing_policies', n.get_collection_of_enum_values(routing_policy.RoutingPolicy)),
            "source": lambda n : setattr(self, 'source', n.get_object_value(participant_info.ParticipantInfo)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(call_state.CallState)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(invitation_participant_info.InvitationParticipantInfo)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "terminationReason": lambda n : setattr(self, 'termination_reason', n.get_str_value()),
            "toneInfo": lambda n : setattr(self, 'tone_info', n.get_object_value(tone_info.ToneInfo)),
            "transcription": lambda n : setattr(self, 'transcription', n.get_object_value(call_transcription_info.CallTranscriptionInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def incoming_context(self,) -> Optional[incoming_context.IncomingContext]:
        """
        Gets the incomingContext property value. The context associated with an incoming call. Read-only. Server generated.
        Returns: Optional[incoming_context.IncomingContext]
        """
        return self._incoming_context
    
    @incoming_context.setter
    def incoming_context(self,value: Optional[incoming_context.IncomingContext] = None) -> None:
        """
        Sets the incomingContext property value. The context associated with an incoming call. Read-only. Server generated.
        Args:
            value: Value to set for the incoming_context property.
        """
        self._incoming_context = value
    
    @property
    def media_config(self,) -> Optional[media_config.MediaConfig]:
        """
        Gets the mediaConfig property value. The media configuration. Required information for creating peer to peer calls or joining meetings.
        Returns: Optional[media_config.MediaConfig]
        """
        return self._media_config
    
    @media_config.setter
    def media_config(self,value: Optional[media_config.MediaConfig] = None) -> None:
        """
        Sets the mediaConfig property value. The media configuration. Required information for creating peer to peer calls or joining meetings.
        Args:
            value: Value to set for the media_config property.
        """
        self._media_config = value
    
    @property
    def media_state(self,) -> Optional[call_media_state.CallMediaState]:
        """
        Gets the mediaState property value. Read-only. The call media state.
        Returns: Optional[call_media_state.CallMediaState]
        """
        return self._media_state
    
    @media_state.setter
    def media_state(self,value: Optional[call_media_state.CallMediaState] = None) -> None:
        """
        Sets the mediaState property value. Read-only. The call media state.
        Args:
            value: Value to set for the media_state property.
        """
        self._media_state = value
    
    @property
    def meeting_capability(self,) -> Optional[meeting_capability.MeetingCapability]:
        """
        Gets the meetingCapability property value. Contains the capabilities of a meeting. Read-only.
        Returns: Optional[meeting_capability.MeetingCapability]
        """
        return self._meeting_capability
    
    @meeting_capability.setter
    def meeting_capability(self,value: Optional[meeting_capability.MeetingCapability] = None) -> None:
        """
        Sets the meetingCapability property value. Contains the capabilities of a meeting. Read-only.
        Args:
            value: Value to set for the meeting_capability property.
        """
        self._meeting_capability = value
    
    @property
    def meeting_info(self,) -> Optional[meeting_info.MeetingInfo]:
        """
        Gets the meetingInfo property value. The meeting information. Required information for meeting scenarios.
        Returns: Optional[meeting_info.MeetingInfo]
        """
        return self._meeting_info
    
    @meeting_info.setter
    def meeting_info(self,value: Optional[meeting_info.MeetingInfo] = None) -> None:
        """
        Sets the meetingInfo property value. The meeting information. Required information for meeting scenarios.
        Args:
            value: Value to set for the meeting_info property.
        """
        self._meeting_info = value
    
    @property
    def my_participant_id(self,) -> Optional[str]:
        """
        Gets the myParticipantId property value. The myParticipantId property
        Returns: Optional[str]
        """
        return self._my_participant_id
    
    @my_participant_id.setter
    def my_participant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the myParticipantId property value. The myParticipantId property
        Args:
            value: Value to set for the my_participant_id property.
        """
        self._my_participant_id = value
    
    @property
    def operations(self,) -> Optional[List[comms_operation.CommsOperation]]:
        """
        Gets the operations property value. The operations property
        Returns: Optional[List[comms_operation.CommsOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[comms_operation.CommsOperation]] = None) -> None:
        """
        Sets the operations property value. The operations property
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def participants(self,) -> Optional[List[participant.Participant]]:
        """
        Gets the participants property value. The participants property
        Returns: Optional[List[participant.Participant]]
        """
        return self._participants
    
    @participants.setter
    def participants(self,value: Optional[List[participant.Participant]] = None) -> None:
        """
        Sets the participants property value. The participants property
        Args:
            value: Value to set for the participants property.
        """
        self._participants = value
    
    @property
    def requested_modalities(self,) -> Optional[List[modality.Modality]]:
        """
        Gets the requestedModalities property value. The requestedModalities property
        Returns: Optional[List[modality.Modality]]
        """
        return self._requested_modalities
    
    @requested_modalities.setter
    def requested_modalities(self,value: Optional[List[modality.Modality]] = None) -> None:
        """
        Sets the requestedModalities property value. The requestedModalities property
        Args:
            value: Value to set for the requested_modalities property.
        """
        self._requested_modalities = value
    
    @property
    def result_info(self,) -> Optional[result_info.ResultInfo]:
        """
        Gets the resultInfo property value. The resultInfo property
        Returns: Optional[result_info.ResultInfo]
        """
        return self._result_info
    
    @result_info.setter
    def result_info(self,value: Optional[result_info.ResultInfo] = None) -> None:
        """
        Sets the resultInfo property value. The resultInfo property
        Args:
            value: Value to set for the result_info property.
        """
        self._result_info = value
    
    @property
    def ringing_timeout_in_seconds(self,) -> Optional[int]:
        """
        Gets the ringingTimeoutInSeconds property value. The ringingTimeoutInSeconds property
        Returns: Optional[int]
        """
        return self._ringing_timeout_in_seconds
    
    @ringing_timeout_in_seconds.setter
    def ringing_timeout_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the ringingTimeoutInSeconds property value. The ringingTimeoutInSeconds property
        Args:
            value: Value to set for the ringing_timeout_in_seconds property.
        """
        self._ringing_timeout_in_seconds = value
    
    @property
    def routing_policies(self,) -> Optional[List[routing_policy.RoutingPolicy]]:
        """
        Gets the routingPolicies property value. The routingPolicies property
        Returns: Optional[List[routing_policy.RoutingPolicy]]
        """
        return self._routing_policies
    
    @routing_policies.setter
    def routing_policies(self,value: Optional[List[routing_policy.RoutingPolicy]] = None) -> None:
        """
        Sets the routingPolicies property value. The routingPolicies property
        Args:
            value: Value to set for the routing_policies property.
        """
        self._routing_policies = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("activeModalities", self.active_modalities)
        writer.write_object_value("answeredBy", self.answered_by)
        writer.write_collection_of_object_values("audioRoutingGroups", self.audio_routing_groups)
        writer.write_str_value("callbackUri", self.callback_uri)
        writer.write_str_value("callChainId", self.call_chain_id)
        writer.write_object_value("callOptions", self.call_options)
        writer.write_collection_of_object_values("callRoutes", self.call_routes)
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
        writer.write_enum_value("requestedModalities", self.requested_modalities)
        writer.write_object_value("resultInfo", self.result_info)
        writer.write_int_value("ringingTimeoutInSeconds", self.ringing_timeout_in_seconds)
        writer.write_enum_value("routingPolicies", self.routing_policies)
        writer.write_object_value("source", self.source)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("subject", self.subject)
        writer.write_collection_of_object_values("targets", self.targets)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("terminationReason", self.termination_reason)
        writer.write_object_value("toneInfo", self.tone_info)
        writer.write_object_value("transcription", self.transcription)
    
    @property
    def source(self,) -> Optional[participant_info.ParticipantInfo]:
        """
        Gets the source property value. The source property
        Returns: Optional[participant_info.ParticipantInfo]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[participant_info.ParticipantInfo] = None) -> None:
        """
        Sets the source property value. The source property
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    
    @property
    def state(self,) -> Optional[call_state.CallState]:
        """
        Gets the state property value. The state property
        Returns: Optional[call_state.CallState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[call_state.CallState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The subject property
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The subject property
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    
    @property
    def targets(self,) -> Optional[List[invitation_participant_info.InvitationParticipantInfo]]:
        """
        Gets the targets property value. The targets property
        Returns: Optional[List[invitation_participant_info.InvitationParticipantInfo]]
        """
        return self._targets
    
    @targets.setter
    def targets(self,value: Optional[List[invitation_participant_info.InvitationParticipantInfo]] = None) -> None:
        """
        Sets the targets property value. The targets property
        Args:
            value: Value to set for the targets property.
        """
        self._targets = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    
    @property
    def termination_reason(self,) -> Optional[str]:
        """
        Gets the terminationReason property value. The terminationReason property
        Returns: Optional[str]
        """
        return self._termination_reason
    
    @termination_reason.setter
    def termination_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the terminationReason property value. The terminationReason property
        Args:
            value: Value to set for the termination_reason property.
        """
        self._termination_reason = value
    
    @property
    def tone_info(self,) -> Optional[tone_info.ToneInfo]:
        """
        Gets the toneInfo property value. The toneInfo property
        Returns: Optional[tone_info.ToneInfo]
        """
        return self._tone_info
    
    @tone_info.setter
    def tone_info(self,value: Optional[tone_info.ToneInfo] = None) -> None:
        """
        Sets the toneInfo property value. The toneInfo property
        Args:
            value: Value to set for the tone_info property.
        """
        self._tone_info = value
    
    @property
    def transcription(self,) -> Optional[call_transcription_info.CallTranscriptionInfo]:
        """
        Gets the transcription property value. The transcription information for the call. Read-only.
        Returns: Optional[call_transcription_info.CallTranscriptionInfo]
        """
        return self._transcription
    
    @transcription.setter
    def transcription(self,value: Optional[call_transcription_info.CallTranscriptionInfo] = None) -> None:
        """
        Sets the transcription property value. The transcription information for the call. Read-only.
        Args:
            value: Value to set for the transcription property.
        """
        self._transcription = value
    

