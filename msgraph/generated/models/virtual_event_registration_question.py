from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .virtual_event_registration_question_answer_input_type import VirtualEventRegistrationQuestionAnswerInputType

from .entity import Entity

@dataclass
class VirtualEventRegistrationQuestion(Entity):
    # Answer choices when answerInputType is singleChoice or multiChoice.
    answer_choices: Optional[List[str]] = None
    # Input type of the registration question answer.
    answer_input_type: Optional[VirtualEventRegistrationQuestionAnswerInputType] = None
    # Display name of the registration question.
    display_name: Optional[str] = None
    # Indicates whether the question is required to answer. Default value is false.
    is_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventRegistrationQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistrationQuestion
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventRegistrationQuestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .virtual_event_registration_question_answer_input_type import VirtualEventRegistrationQuestionAnswerInputType

        from .entity import Entity
        from .virtual_event_registration_question_answer_input_type import VirtualEventRegistrationQuestionAnswerInputType

        fields: Dict[str, Callable[[Any], None]] = {
            "answerChoices": lambda n : setattr(self, 'answer_choices', n.get_collection_of_primitive_values(str)),
            "answerInputType": lambda n : setattr(self, 'answer_input_type', n.get_enum_value(VirtualEventRegistrationQuestionAnswerInputType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("answerChoices", self.answer_choices)
        writer.write_enum_value("answerInputType", self.answer_input_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isRequired", self.is_required)
    

