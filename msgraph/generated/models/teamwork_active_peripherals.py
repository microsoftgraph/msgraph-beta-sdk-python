from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_peripheral import TeamworkPeripheral

@dataclass
class TeamworkActivePeripherals(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The communicationSpeaker property
    communication_speaker: Optional[TeamworkPeripheral] = None
    # The contentCamera property
    content_camera: Optional[TeamworkPeripheral] = None
    # The microphone property
    microphone: Optional[TeamworkPeripheral] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The roomCamera property
    room_camera: Optional[TeamworkPeripheral] = None
    # The speaker property
    speaker: Optional[TeamworkPeripheral] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkActivePeripherals:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkActivePeripherals
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkActivePeripherals()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_peripheral import TeamworkPeripheral

        from .teamwork_peripheral import TeamworkPeripheral

        fields: Dict[str, Callable[[Any], None]] = {
            "communicationSpeaker": lambda n : setattr(self, 'communication_speaker', n.get_object_value(TeamworkPeripheral)),
            "contentCamera": lambda n : setattr(self, 'content_camera', n.get_object_value(TeamworkPeripheral)),
            "microphone": lambda n : setattr(self, 'microphone', n.get_object_value(TeamworkPeripheral)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "roomCamera": lambda n : setattr(self, 'room_camera', n.get_object_value(TeamworkPeripheral)),
            "speaker": lambda n : setattr(self, 'speaker', n.get_object_value(TeamworkPeripheral)),
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
        writer.write_object_value("communicationSpeaker", self.communication_speaker)
        writer.write_object_value("contentCamera", self.content_camera)
        writer.write_object_value("microphone", self.microphone)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_object_value("roomCamera", self.room_camera)
        writer.write_object_value("speaker", self.speaker)
        writer.write_additional_data_value(self.additional_data)
    

