from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_peripheral = lazy_import('msgraph.generated.models.teamwork_peripheral')

class TeamworkActivePeripherals(AdditionalDataHolder, Parsable):
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
    def communication_speaker(self,) -> Optional[teamwork_peripheral.TeamworkPeripheral]:
        """
        Gets the communicationSpeaker property value. The communicationSpeaker property
        Returns: Optional[teamwork_peripheral.TeamworkPeripheral]
        """
        return self._communication_speaker
    
    @communication_speaker.setter
    def communication_speaker(self,value: Optional[teamwork_peripheral.TeamworkPeripheral] = None) -> None:
        """
        Sets the communicationSpeaker property value. The communicationSpeaker property
        Args:
            value: Value to set for the communicationSpeaker property.
        """
        self._communication_speaker = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkActivePeripherals and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The communicationSpeaker property
        self._communication_speaker: Optional[teamwork_peripheral.TeamworkPeripheral] = None
        # The contentCamera property
        self._content_camera: Optional[teamwork_peripheral.TeamworkPeripheral] = None
        # The microphone property
        self._microphone: Optional[teamwork_peripheral.TeamworkPeripheral] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The roomCamera property
        self._room_camera: Optional[teamwork_peripheral.TeamworkPeripheral] = None
        # The speaker property
        self._speaker: Optional[teamwork_peripheral.TeamworkPeripheral] = None
    
    @property
    def content_camera(self,) -> Optional[teamwork_peripheral.TeamworkPeripheral]:
        """
        Gets the contentCamera property value. The contentCamera property
        Returns: Optional[teamwork_peripheral.TeamworkPeripheral]
        """
        return self._content_camera
    
    @content_camera.setter
    def content_camera(self,value: Optional[teamwork_peripheral.TeamworkPeripheral] = None) -> None:
        """
        Sets the contentCamera property value. The contentCamera property
        Args:
            value: Value to set for the contentCamera property.
        """
        self._content_camera = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkActivePeripherals:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkActivePeripherals
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkActivePeripherals()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "communication_speaker": lambda n : setattr(self, 'communication_speaker', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
            "content_camera": lambda n : setattr(self, 'content_camera', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
            "microphone": lambda n : setattr(self, 'microphone', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "room_camera": lambda n : setattr(self, 'room_camera', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
            "speaker": lambda n : setattr(self, 'speaker', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
        }
        return fields
    
    @property
    def microphone(self,) -> Optional[teamwork_peripheral.TeamworkPeripheral]:
        """
        Gets the microphone property value. The microphone property
        Returns: Optional[teamwork_peripheral.TeamworkPeripheral]
        """
        return self._microphone
    
    @microphone.setter
    def microphone(self,value: Optional[teamwork_peripheral.TeamworkPeripheral] = None) -> None:
        """
        Sets the microphone property value. The microphone property
        Args:
            value: Value to set for the microphone property.
        """
        self._microphone = value
    
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
    def room_camera(self,) -> Optional[teamwork_peripheral.TeamworkPeripheral]:
        """
        Gets the roomCamera property value. The roomCamera property
        Returns: Optional[teamwork_peripheral.TeamworkPeripheral]
        """
        return self._room_camera
    
    @room_camera.setter
    def room_camera(self,value: Optional[teamwork_peripheral.TeamworkPeripheral] = None) -> None:
        """
        Sets the roomCamera property value. The roomCamera property
        Args:
            value: Value to set for the roomCamera property.
        """
        self._room_camera = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("communicationSpeaker", self.communication_speaker)
        writer.write_object_value("contentCamera", self.content_camera)
        writer.write_object_value("microphone", self.microphone)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("roomCamera", self.room_camera)
        writer.write_object_value("speaker", self.speaker)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def speaker(self,) -> Optional[teamwork_peripheral.TeamworkPeripheral]:
        """
        Gets the speaker property value. The speaker property
        Returns: Optional[teamwork_peripheral.TeamworkPeripheral]
        """
        return self._speaker
    
    @speaker.setter
    def speaker(self,value: Optional[teamwork_peripheral.TeamworkPeripheral] = None) -> None:
        """
        Sets the speaker property value. The speaker property
        Args:
            value: Value to set for the speaker property.
        """
        self._speaker = value
    

