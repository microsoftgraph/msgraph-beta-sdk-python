from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

comms_operation = lazy_import('msgraph.generated.models.comms_operation')

class MuteParticipantsOperation(comms_operation.CommsOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new MuteParticipantsOperation and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The participants property
        self._participants: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MuteParticipantsOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MuteParticipantsOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MuteParticipantsOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def participants(self,) -> Optional[List[str]]:
        """
        Gets the participants property value. The participants property
        Returns: Optional[List[str]]
        """
        return self._participants
    
    @participants.setter
    def participants(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the participants property value. The participants property
        Args:
            value: Value to set for the participants property.
        """
        self._participants = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("participants", self.participants)
    

