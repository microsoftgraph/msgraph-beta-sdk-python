from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, virtual_event_registration_question_answer_input_type

from . import entity

class VirtualEventRegistrationQuestion(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new virtualEventRegistrationQuestion and sets the default values.
        """
        super().__init__()
        # The answerChoices property
        self._answer_choices: Optional[List[str]] = None
        # The answerInputType property
        self._answer_input_type: Optional[virtual_event_registration_question_answer_input_type.VirtualEventRegistrationQuestionAnswerInputType] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The isRequired property
        self._is_required: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def answer_choices(self,) -> Optional[List[str]]:
        """
        Gets the answerChoices property value. The answerChoices property
        Returns: Optional[List[str]]
        """
        return self._answer_choices
    
    @answer_choices.setter
    def answer_choices(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the answerChoices property value. The answerChoices property
        Args:
            value: Value to set for the answer_choices property.
        """
        self._answer_choices = value
    
    @property
    def answer_input_type(self,) -> Optional[virtual_event_registration_question_answer_input_type.VirtualEventRegistrationQuestionAnswerInputType]:
        """
        Gets the answerInputType property value. The answerInputType property
        Returns: Optional[virtual_event_registration_question_answer_input_type.VirtualEventRegistrationQuestionAnswerInputType]
        """
        return self._answer_input_type
    
    @answer_input_type.setter
    def answer_input_type(self,value: Optional[virtual_event_registration_question_answer_input_type.VirtualEventRegistrationQuestionAnswerInputType] = None) -> None:
        """
        Sets the answerInputType property value. The answerInputType property
        Args:
            value: Value to set for the answer_input_type property.
        """
        self._answer_input_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventRegistrationQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistrationQuestion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VirtualEventRegistrationQuestion()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, virtual_event_registration_question_answer_input_type

        fields: Dict[str, Callable[[Any], None]] = {
            "answerChoices": lambda n : setattr(self, 'answer_choices', n.get_collection_of_primitive_values(str)),
            "answerInputType": lambda n : setattr(self, 'answer_input_type', n.get_enum_value(virtual_event_registration_question_answer_input_type.VirtualEventRegistrationQuestionAnswerInputType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_required(self,) -> Optional[bool]:
        """
        Gets the isRequired property value. The isRequired property
        Returns: Optional[bool]
        """
        return self._is_required
    
    @is_required.setter
    def is_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRequired property value. The isRequired property
        Args:
            value: Value to set for the is_required property.
        """
        self._is_required = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("answerChoices", self.answer_choices)
        writer.write_enum_value("answerInputType", self.answer_input_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isRequired", self.is_required)
    

