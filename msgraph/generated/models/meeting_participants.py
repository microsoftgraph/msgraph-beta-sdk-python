from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import meeting_participant_info

class MeetingParticipants(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new meetingParticipants and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Information of the meeting attendees.
        self._attendees: Optional[List[meeting_participant_info.MeetingParticipantInfo]] = None
        # The contributors property
        self._contributors: Optional[List[meeting_participant_info.MeetingParticipantInfo]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Information of the meeting organizer.
        self._organizer: Optional[meeting_participant_info.MeetingParticipantInfo] = None
        # The producers property
        self._producers: Optional[List[meeting_participant_info.MeetingParticipantInfo]] = None
    
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
    def attendees(self,) -> Optional[List[meeting_participant_info.MeetingParticipantInfo]]:
        """
        Gets the attendees property value. Information of the meeting attendees.
        Returns: Optional[List[meeting_participant_info.MeetingParticipantInfo]]
        """
        return self._attendees
    
    @attendees.setter
    def attendees(self,value: Optional[List[meeting_participant_info.MeetingParticipantInfo]] = None) -> None:
        """
        Sets the attendees property value. Information of the meeting attendees.
        Args:
            value: Value to set for the attendees property.
        """
        self._attendees = value
    
    @property
    def contributors(self,) -> Optional[List[meeting_participant_info.MeetingParticipantInfo]]:
        """
        Gets the contributors property value. The contributors property
        Returns: Optional[List[meeting_participant_info.MeetingParticipantInfo]]
        """
        return self._contributors
    
    @contributors.setter
    def contributors(self,value: Optional[List[meeting_participant_info.MeetingParticipantInfo]] = None) -> None:
        """
        Sets the contributors property value. The contributors property
        Args:
            value: Value to set for the contributors property.
        """
        self._contributors = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingParticipants:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingParticipants
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MeetingParticipants()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import meeting_participant_info

        fields: Dict[str, Callable[[Any], None]] = {
            "attendees": lambda n : setattr(self, 'attendees', n.get_collection_of_object_values(meeting_participant_info.MeetingParticipantInfo)),
            "contributors": lambda n : setattr(self, 'contributors', n.get_collection_of_object_values(meeting_participant_info.MeetingParticipantInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organizer": lambda n : setattr(self, 'organizer', n.get_object_value(meeting_participant_info.MeetingParticipantInfo)),
            "producers": lambda n : setattr(self, 'producers', n.get_collection_of_object_values(meeting_participant_info.MeetingParticipantInfo)),
        }
        return fields
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def organizer(self,) -> Optional[meeting_participant_info.MeetingParticipantInfo]:
        """
        Gets the organizer property value. Information of the meeting organizer.
        Returns: Optional[meeting_participant_info.MeetingParticipantInfo]
        """
        return self._organizer
    
    @organizer.setter
    def organizer(self,value: Optional[meeting_participant_info.MeetingParticipantInfo] = None) -> None:
        """
        Sets the organizer property value. Information of the meeting organizer.
        Args:
            value: Value to set for the organizer property.
        """
        self._organizer = value
    
    @property
    def producers(self,) -> Optional[List[meeting_participant_info.MeetingParticipantInfo]]:
        """
        Gets the producers property value. The producers property
        Returns: Optional[List[meeting_participant_info.MeetingParticipantInfo]]
        """
        return self._producers
    
    @producers.setter
    def producers(self,value: Optional[List[meeting_participant_info.MeetingParticipantInfo]] = None) -> None:
        """
        Sets the producers property value. The producers property
        Args:
            value: Value to set for the producers property.
        """
        self._producers = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("attendees", self.attendees)
        writer.write_collection_of_object_values("contributors", self.contributors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("organizer", self.organizer)
        writer.write_collection_of_object_values("producers", self.producers)
        writer.write_additional_data_value(self.additional_data)
    

