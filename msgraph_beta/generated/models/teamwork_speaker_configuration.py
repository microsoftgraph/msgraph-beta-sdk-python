from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_peripheral import TeamworkPeripheral

@dataclass
class TeamworkSpeakerConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The defaultCommunicationSpeaker property
    default_communication_speaker: Optional[TeamworkPeripheral] = None
    # The defaultSpeaker property
    default_speaker: Optional[TeamworkPeripheral] = None
    # True if the communication speaker is optional. Used to compute the health state if the communication speaker is not optional.
    is_communication_speaker_optional: Optional[bool] = None
    # True if the configured speaker is optional. Used to compute the health state if the speaker is not optional.
    is_speaker_optional: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The speakers property
    speakers: Optional[List[TeamworkPeripheral]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkSpeakerConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkSpeakerConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkSpeakerConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_peripheral import TeamworkPeripheral

        from .teamwork_peripheral import TeamworkPeripheral

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultCommunicationSpeaker": lambda n : setattr(self, 'default_communication_speaker', n.get_object_value(TeamworkPeripheral)),
            "defaultSpeaker": lambda n : setattr(self, 'default_speaker', n.get_object_value(TeamworkPeripheral)),
            "isCommunicationSpeakerOptional": lambda n : setattr(self, 'is_communication_speaker_optional', n.get_bool_value()),
            "isSpeakerOptional": lambda n : setattr(self, 'is_speaker_optional', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "speakers": lambda n : setattr(self, 'speakers', n.get_collection_of_object_values(TeamworkPeripheral)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("defaultCommunicationSpeaker", self.default_communication_speaker)
        writer.write_object_value("defaultSpeaker", self.default_speaker)
        writer.write_bool_value("isCommunicationSpeakerOptional", self.is_communication_speaker_optional)
        writer.write_bool_value("isSpeakerOptional", self.is_speaker_optional)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("speakers", self.speakers)
        writer.write_additional_data_value(self.additional_data)
    

