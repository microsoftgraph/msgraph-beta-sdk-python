from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, participant

from . import entity

class DeltaParticipants(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new DeltaParticipants and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The participants property
        self._participants: Optional[List[participant.Participant]] = None
        # The sequenceNumber property
        self._sequence_number: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeltaParticipants:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeltaParticipants
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeltaParticipants()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, participant

        fields: Dict[str, Callable[[Any], None]] = {
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(participant.Participant)),
            "sequenceNumber": lambda n : setattr(self, 'sequence_number', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def participants(self,) -> Optional[List[participant.Participant]]:
        """
        Gets the participants property value. The participants property
        Returns: Optional[List[participant.Participant]]
        """
        return self._participants
    
    @participants.setter
    def participants(self,value: Optional[List[participant.Participant]] = None) -> None:
        """
        Sets the participants property value. The participants property
        Args:
            value: Value to set for the participants property.
        """
        self._participants = value
    
    @property
    def sequence_number(self,) -> Optional[int]:
        """
        Gets the sequenceNumber property value. The sequenceNumber property
        Returns: Optional[int]
        """
        return self._sequence_number
    
    @sequence_number.setter
    def sequence_number(self,value: Optional[int] = None) -> None:
        """
        Sets the sequenceNumber property value. The sequenceNumber property
        Args:
            value: Value to set for the sequence_number property.
        """
        self._sequence_number = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("participants", self.participants)
        writer.write_int_value("sequenceNumber", self.sequence_number)
    

