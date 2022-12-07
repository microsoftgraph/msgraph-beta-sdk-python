from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

answer_state = lazy_import('msgraph.generated.models.search.answer_state')
search_answer = lazy_import('msgraph.generated.models.search.search_answer')

class Acronym(search_answer.SearchAnswer):
    def __init__(self,) -> None:
        """
        Instantiates a new Acronym and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # What the acronym stands for.
        self._stands_for: Optional[str] = None
        # The state property
        self._state: Optional[answer_state.AnswerState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Acronym:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Acronym
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Acronym()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "stands_for": lambda n : setattr(self, 'stands_for', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(answer_state.AnswerState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("standsFor", self.stands_for)
        writer.write_enum_value("state", self.state)
    
    @property
    def stands_for(self,) -> Optional[str]:
        """
        Gets the standsFor property value. What the acronym stands for.
        Returns: Optional[str]
        """
        return self._stands_for
    
    @stands_for.setter
    def stands_for(self,value: Optional[str] = None) -> None:
        """
        Sets the standsFor property value. What the acronym stands for.
        Args:
            value: Value to set for the standsFor property.
        """
        self._stands_for = value
    
    @property
    def state(self,) -> Optional[answer_state.AnswerState]:
        """
        Gets the state property value. The state property
        Returns: Optional[answer_state.AnswerState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[answer_state.AnswerState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

