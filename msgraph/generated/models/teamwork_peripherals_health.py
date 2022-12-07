from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_peripheral_health = lazy_import('msgraph.generated.models.teamwork_peripheral_health')

class TeamworkPeripheralsHealth(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def communication_speaker_health(self,) -> Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]:
        """
        Gets the communicationSpeakerHealth property value. The health details about the communication speaker.
        Returns: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]
        """
        return self._communication_speaker_health
    
    @communication_speaker_health.setter
    def communication_speaker_health(self,value: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None) -> None:
        """
        Sets the communicationSpeakerHealth property value. The health details about the communication speaker.
        Args:
            value: Value to set for the communicationSpeakerHealth property.
        """
        self._communication_speaker_health = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkPeripheralsHealth and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The health details about the communication speaker.
        self._communication_speaker_health: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None
        # The health details about the content camera.
        self._content_camera_health: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None
        # The health details about displays.
        self._display_health_collection: Optional[List[teamwork_peripheral_health.TeamworkPeripheralHealth]] = None
        # The health details about the microphone.
        self._microphone_health: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The health details about the room camera.
        self._room_camera_health: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None
        # The health details about the speaker.
        self._speaker_health: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None
    
    @property
    def content_camera_health(self,) -> Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]:
        """
        Gets the contentCameraHealth property value. The health details about the content camera.
        Returns: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]
        """
        return self._content_camera_health
    
    @content_camera_health.setter
    def content_camera_health(self,value: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None) -> None:
        """
        Sets the contentCameraHealth property value. The health details about the content camera.
        Args:
            value: Value to set for the contentCameraHealth property.
        """
        self._content_camera_health = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkPeripheralsHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkPeripheralsHealth
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkPeripheralsHealth()
    
    @property
    def display_health_collection(self,) -> Optional[List[teamwork_peripheral_health.TeamworkPeripheralHealth]]:
        """
        Gets the displayHealthCollection property value. The health details about displays.
        Returns: Optional[List[teamwork_peripheral_health.TeamworkPeripheralHealth]]
        """
        return self._display_health_collection
    
    @display_health_collection.setter
    def display_health_collection(self,value: Optional[List[teamwork_peripheral_health.TeamworkPeripheralHealth]] = None) -> None:
        """
        Sets the displayHealthCollection property value. The health details about displays.
        Args:
            value: Value to set for the displayHealthCollection property.
        """
        self._display_health_collection = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "communication_speaker_health": lambda n : setattr(self, 'communication_speaker_health', n.get_object_value(teamwork_peripheral_health.TeamworkPeripheralHealth)),
            "content_camera_health": lambda n : setattr(self, 'content_camera_health', n.get_object_value(teamwork_peripheral_health.TeamworkPeripheralHealth)),
            "display_health_collection": lambda n : setattr(self, 'display_health_collection', n.get_collection_of_object_values(teamwork_peripheral_health.TeamworkPeripheralHealth)),
            "microphone_health": lambda n : setattr(self, 'microphone_health', n.get_object_value(teamwork_peripheral_health.TeamworkPeripheralHealth)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "room_camera_health": lambda n : setattr(self, 'room_camera_health', n.get_object_value(teamwork_peripheral_health.TeamworkPeripheralHealth)),
            "speaker_health": lambda n : setattr(self, 'speaker_health', n.get_object_value(teamwork_peripheral_health.TeamworkPeripheralHealth)),
        }
        return fields
    
    @property
    def microphone_health(self,) -> Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]:
        """
        Gets the microphoneHealth property value. The health details about the microphone.
        Returns: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]
        """
        return self._microphone_health
    
    @microphone_health.setter
    def microphone_health(self,value: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None) -> None:
        """
        Sets the microphoneHealth property value. The health details about the microphone.
        Args:
            value: Value to set for the microphoneHealth property.
        """
        self._microphone_health = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def room_camera_health(self,) -> Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]:
        """
        Gets the roomCameraHealth property value. The health details about the room camera.
        Returns: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]
        """
        return self._room_camera_health
    
    @room_camera_health.setter
    def room_camera_health(self,value: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None) -> None:
        """
        Sets the roomCameraHealth property value. The health details about the room camera.
        Args:
            value: Value to set for the roomCameraHealth property.
        """
        self._room_camera_health = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("communicationSpeakerHealth", self.communication_speaker_health)
        writer.write_object_value("contentCameraHealth", self.content_camera_health)
        writer.write_collection_of_object_values("displayHealthCollection", self.display_health_collection)
        writer.write_object_value("microphoneHealth", self.microphone_health)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("roomCameraHealth", self.room_camera_health)
        writer.write_object_value("speakerHealth", self.speaker_health)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def speaker_health(self,) -> Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]:
        """
        Gets the speakerHealth property value. The health details about the speaker.
        Returns: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]
        """
        return self._speaker_health
    
    @speaker_health.setter
    def speaker_health(self,value: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None) -> None:
        """
        Sets the speakerHealth property value. The health details about the speaker.
        Args:
            value: Value to set for the speakerHealth property.
        """
        self._speaker_health = value
    

