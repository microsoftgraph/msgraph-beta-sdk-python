from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .meeting_participant_info import MeetingParticipantInfo

@dataclass
class MeetingParticipants(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Information of the meeting attendees.
    attendees: Optional[List[MeetingParticipantInfo]] = None
    # The contributors property
    contributors: Optional[List[MeetingParticipantInfo]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Information of the meeting organizer.
    organizer: Optional[MeetingParticipantInfo] = None
    # The producers property
    producers: Optional[List[MeetingParticipantInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingParticipants:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingParticipants
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MeetingParticipants()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .meeting_participant_info import MeetingParticipantInfo

        from .meeting_participant_info import MeetingParticipantInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "attendees": lambda n : setattr(self, 'attendees', n.get_collection_of_object_values(MeetingParticipantInfo)),
            "contributors": lambda n : setattr(self, 'contributors', n.get_collection_of_object_values(MeetingParticipantInfo)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organizer": lambda n : setattr(self, 'organizer', n.get_object_value(MeetingParticipantInfo)),
            "producers": lambda n : setattr(self, 'producers', n.get_collection_of_object_values(MeetingParticipantInfo)),
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
        writer.write_collection_of_object_values("attendees", self.attendees)
        writer.write_collection_of_object_values("contributors", self.contributors)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_object_value("organizer", self.organizer)
        writer.write_collection_of_object_values("producers", self.producers)
        writer.write_additional_data_value(self.additional_data)
    

