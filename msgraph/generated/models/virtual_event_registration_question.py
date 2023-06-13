from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, virtual_event_registration_question_answer_input_type

from . import entity

@dataclass
class VirtualEventRegistrationQuestion(entity.Entity):
    # Answer choices when answerInputType is singleChoice or multiChoice.
    answer_choices: Optional[List[str]] = None
    # Input type of the registration question answer.
    answer_input_type: Optional[virtual_event_registration_question_answer_input_type.VirtualEventRegistrationQuestionAnswerInputType] = None
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
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistrationQuestion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VirtualEventRegistrationQuestion()
    
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
    

