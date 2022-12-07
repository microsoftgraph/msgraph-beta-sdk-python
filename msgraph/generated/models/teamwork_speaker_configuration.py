from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_peripheral = lazy_import('msgraph.generated.models.teamwork_peripheral')

class TeamworkSpeakerConfiguration(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkSpeakerConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The defaultCommunicationSpeaker property
        self._default_communication_speaker: Optional[teamwork_peripheral.TeamworkPeripheral] = None
        # The defaultSpeaker property
        self._default_speaker: Optional[teamwork_peripheral.TeamworkPeripheral] = None
        # True if the communication speaker is optional. Used to compute the health state if the communication speaker is not optional.
        self._is_communication_speaker_optional: Optional[bool] = None
        # True if the configured speaker is optional. Used to compute the health state if the speaker is not optional.
        self._is_speaker_optional: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The speakers property
        self._speakers: Optional[List[teamwork_peripheral.TeamworkPeripheral]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkSpeakerConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkSpeakerConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkSpeakerConfiguration()
    
    @property
    def default_communication_speaker(self,) -> Optional[teamwork_peripheral.TeamworkPeripheral]:
        """
        Gets the defaultCommunicationSpeaker property value. The defaultCommunicationSpeaker property
        Returns: Optional[teamwork_peripheral.TeamworkPeripheral]
        """
        return self._default_communication_speaker
    
    @default_communication_speaker.setter
    def default_communication_speaker(self,value: Optional[teamwork_peripheral.TeamworkPeripheral] = None) -> None:
        """
        Sets the defaultCommunicationSpeaker property value. The defaultCommunicationSpeaker property
        Args:
            value: Value to set for the defaultCommunicationSpeaker property.
        """
        self._default_communication_speaker = value
    
    @property
    def default_speaker(self,) -> Optional[teamwork_peripheral.TeamworkPeripheral]:
        """
        Gets the defaultSpeaker property value. The defaultSpeaker property
        Returns: Optional[teamwork_peripheral.TeamworkPeripheral]
        """
        return self._default_speaker
    
    @default_speaker.setter
    def default_speaker(self,value: Optional[teamwork_peripheral.TeamworkPeripheral] = None) -> None:
        """
        Sets the defaultSpeaker property value. The defaultSpeaker property
        Args:
            value: Value to set for the defaultSpeaker property.
        """
        self._default_speaker = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_communication_speaker": lambda n : setattr(self, 'default_communication_speaker', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
            "default_speaker": lambda n : setattr(self, 'default_speaker', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
            "is_communication_speaker_optional": lambda n : setattr(self, 'is_communication_speaker_optional', n.get_bool_value()),
            "is_speaker_optional": lambda n : setattr(self, 'is_speaker_optional', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "speakers": lambda n : setattr(self, 'speakers', n.get_collection_of_object_values(teamwork_peripheral.TeamworkPeripheral)),
        }
        return fields
    
    @property
    def is_communication_speaker_optional(self,) -> Optional[bool]:
        """
        Gets the isCommunicationSpeakerOptional property value. True if the communication speaker is optional. Used to compute the health state if the communication speaker is not optional.
        Returns: Optional[bool]
        """
        return self._is_communication_speaker_optional
    
    @is_communication_speaker_optional.setter
    def is_communication_speaker_optional(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCommunicationSpeakerOptional property value. True if the communication speaker is optional. Used to compute the health state if the communication speaker is not optional.
        Args:
            value: Value to set for the isCommunicationSpeakerOptional property.
        """
        self._is_communication_speaker_optional = value
    
    @property
    def is_speaker_optional(self,) -> Optional[bool]:
        """
        Gets the isSpeakerOptional property value. True if the configured speaker is optional. Used to compute the health state if the speaker is not optional.
        Returns: Optional[bool]
        """
        return self._is_speaker_optional
    
    @is_speaker_optional.setter
    def is_speaker_optional(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSpeakerOptional property value. True if the configured speaker is optional. Used to compute the health state if the speaker is not optional.
        Args:
            value: Value to set for the isSpeakerOptional property.
        """
        self._is_speaker_optional = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("defaultCommunicationSpeaker", self.default_communication_speaker)
        writer.write_object_value("defaultSpeaker", self.default_speaker)
        writer.write_bool_value("isCommunicationSpeakerOptional", self.is_communication_speaker_optional)
        writer.write_bool_value("isSpeakerOptional", self.is_speaker_optional)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("speakers", self.speakers)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def speakers(self,) -> Optional[List[teamwork_peripheral.TeamworkPeripheral]]:
        """
        Gets the speakers property value. The speakers property
        Returns: Optional[List[teamwork_peripheral.TeamworkPeripheral]]
        """
        return self._speakers
    
    @speakers.setter
    def speakers(self,value: Optional[List[teamwork_peripheral.TeamworkPeripheral]] = None) -> None:
        """
        Sets the speakers property value. The speakers property
        Args:
            value: Value to set for the speakers property.
        """
        self._speakers = value
    

