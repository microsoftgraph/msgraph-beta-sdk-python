from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .endpoint_type import EndpointType
    from .identity_set import IdentitySet

@dataclass
class InvitationParticipantInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The type of endpoint. Possible values are: default, voicemail, skypeForBusiness, skypeForBusinessVoipPhone and unknownFutureValue.
    endpoint_type: Optional[EndpointType] = None
    # Optional. Whether to hide the participant from the roster.
    hidden: Optional[bool] = None
    # The identity property
    identity: Optional[IdentitySet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Optional. The ID of the target participant.
    participant_id: Optional[str] = None
    # Optional. Whether to remove them from the main mixer.
    remove_from_default_audio_routing_group: Optional[bool] = None
    # Optional. The call which the target identity is currently a part of. For peer-to-peer case, the call will be dropped once the participant is added successfully.
    replaces_call_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InvitationParticipantInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvitationParticipantInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InvitationParticipantInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .endpoint_type import EndpointType
        from .identity_set import IdentitySet

        from .endpoint_type import EndpointType
        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "endpointType": lambda n : setattr(self, 'endpoint_type', n.get_enum_value(EndpointType)),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(IdentitySet)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "participantId": lambda n : setattr(self, 'participant_id', n.get_str_value()),
            "removeFromDefaultAudioRoutingGroup": lambda n : setattr(self, 'remove_from_default_audio_routing_group', n.get_bool_value()),
            "replacesCallId": lambda n : setattr(self, 'replaces_call_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("endpointType", self.endpoint_type)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_object_value("identity", self.identity)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("participantId", self.participant_id)
        writer.write_bool_value("removeFromDefaultAudioRoutingGroup", self.remove_from_default_audio_routing_group)
        writer.write_str_value("replacesCallId", self.replaces_call_id)
        writer.write_additional_data_value(self.additional_data)
    

