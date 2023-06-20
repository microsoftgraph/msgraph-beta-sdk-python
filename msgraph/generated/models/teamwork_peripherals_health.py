from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teamwork_peripheral_health

@dataclass
class TeamworkPeripheralsHealth(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The health details about the communication speaker.
    communication_speaker_health: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None
    # The health details about the content camera.
    content_camera_health: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None
    # The health details about displays.
    display_health_collection: Optional[List[teamwork_peripheral_health.TeamworkPeripheralHealth]] = None
    # The health details about the microphone.
    microphone_health: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The health details about the room camera.
    room_camera_health: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None
    # The health details about the speaker.
    speaker_health: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkPeripheralsHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkPeripheralsHealth
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkPeripheralsHealth()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teamwork_peripheral_health

        from . import teamwork_peripheral_health

        fields: Dict[str, Callable[[Any], None]] = {
            "communicationSpeakerHealth": lambda n : setattr(self, 'communication_speaker_health', n.get_object_value(teamwork_peripheral_health.TeamworkPeripheralHealth)),
            "contentCameraHealth": lambda n : setattr(self, 'content_camera_health', n.get_object_value(teamwork_peripheral_health.TeamworkPeripheralHealth)),
            "displayHealthCollection": lambda n : setattr(self, 'display_health_collection', n.get_collection_of_object_values(teamwork_peripheral_health.TeamworkPeripheralHealth)),
            "microphoneHealth": lambda n : setattr(self, 'microphone_health', n.get_object_value(teamwork_peripheral_health.TeamworkPeripheralHealth)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "roomCameraHealth": lambda n : setattr(self, 'room_camera_health', n.get_object_value(teamwork_peripheral_health.TeamworkPeripheralHealth)),
            "speakerHealth": lambda n : setattr(self, 'speaker_health', n.get_object_value(teamwork_peripheral_health.TeamworkPeripheralHealth)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("communicationSpeakerHealth", self.communication_speaker_health)
        writer.write_object_value("contentCameraHealth", self.content_camera_health)
        writer.write_collection_of_object_values("displayHealthCollection", self.display_health_collection)
        writer.write_object_value("microphoneHealth", self.microphone_health)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("roomCameraHealth", self.room_camera_health)
        writer.write_object_value("speakerHealth", self.speaker_health)
        writer.write_additional_data_value(self.additional_data)
    

