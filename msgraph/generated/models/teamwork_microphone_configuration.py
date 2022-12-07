from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_peripheral = lazy_import('msgraph.generated.models.teamwork_peripheral')

class TeamworkMicrophoneConfiguration(AdditionalDataHolder, Parsable):
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
        Instantiates a new teamworkMicrophoneConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The defaultMicrophone property
        self._default_microphone: Optional[teamwork_peripheral.TeamworkPeripheral] = None
        # True if the configured microphone is optional. False if the microphone is not optional and the health state of the device should be computed.
        self._is_microphone_optional: Optional[bool] = None
        # The microphones property
        self._microphones: Optional[List[teamwork_peripheral.TeamworkPeripheral]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkMicrophoneConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkMicrophoneConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkMicrophoneConfiguration()
    
    @property
    def default_microphone(self,) -> Optional[teamwork_peripheral.TeamworkPeripheral]:
        """
        Gets the defaultMicrophone property value. The defaultMicrophone property
        Returns: Optional[teamwork_peripheral.TeamworkPeripheral]
        """
        return self._default_microphone
    
    @default_microphone.setter
    def default_microphone(self,value: Optional[teamwork_peripheral.TeamworkPeripheral] = None) -> None:
        """
        Sets the defaultMicrophone property value. The defaultMicrophone property
        Args:
            value: Value to set for the defaultMicrophone property.
        """
        self._default_microphone = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_microphone": lambda n : setattr(self, 'default_microphone', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
            "is_microphone_optional": lambda n : setattr(self, 'is_microphone_optional', n.get_bool_value()),
            "microphones": lambda n : setattr(self, 'microphones', n.get_collection_of_object_values(teamwork_peripheral.TeamworkPeripheral)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_microphone_optional(self,) -> Optional[bool]:
        """
        Gets the isMicrophoneOptional property value. True if the configured microphone is optional. False if the microphone is not optional and the health state of the device should be computed.
        Returns: Optional[bool]
        """
        return self._is_microphone_optional
    
    @is_microphone_optional.setter
    def is_microphone_optional(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMicrophoneOptional property value. True if the configured microphone is optional. False if the microphone is not optional and the health state of the device should be computed.
        Args:
            value: Value to set for the isMicrophoneOptional property.
        """
        self._is_microphone_optional = value
    
    @property
    def microphones(self,) -> Optional[List[teamwork_peripheral.TeamworkPeripheral]]:
        """
        Gets the microphones property value. The microphones property
        Returns: Optional[List[teamwork_peripheral.TeamworkPeripheral]]
        """
        return self._microphones
    
    @microphones.setter
    def microphones(self,value: Optional[List[teamwork_peripheral.TeamworkPeripheral]] = None) -> None:
        """
        Sets the microphones property value. The microphones property
        Args:
            value: Value to set for the microphones property.
        """
        self._microphones = value
    
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
        writer.write_object_value("defaultMicrophone", self.default_microphone)
        writer.write_bool_value("isMicrophoneOptional", self.is_microphone_optional)
        writer.write_collection_of_object_values("microphones", self.microphones)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

