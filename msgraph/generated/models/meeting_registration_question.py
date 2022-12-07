from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

answer_input_type = lazy_import('msgraph.generated.models.answer_input_type')
entity = lazy_import('msgraph.generated.models.entity')

class MeetingRegistrationQuestion(entity.Entity):
    """
    Provides operations to manage the commsApplication singleton.
    """
    @property
    def answer_input_type(self,) -> Optional[answer_input_type.AnswerInputType]:
        """
        Gets the answerInputType property value. Answer input type of the custom registration question.
        Returns: Optional[answer_input_type.AnswerInputType]
        """
        return self._answer_input_type
    
    @answer_input_type.setter
    def answer_input_type(self,value: Optional[answer_input_type.AnswerInputType] = None) -> None:
        """
        Sets the answerInputType property value. Answer input type of the custom registration question.
        Args:
            value: Value to set for the answerInputType property.
        """
        self._answer_input_type = value
    
    @property
    def answer_options(self,) -> Optional[List[str]]:
        """
        Gets the answerOptions property value. Answer options when answerInputType is radioButton.
        Returns: Optional[List[str]]
        """
        return self._answer_options
    
    @answer_options.setter
    def answer_options(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the answerOptions property value. Answer options when answerInputType is radioButton.
        Args:
            value: Value to set for the answerOptions property.
        """
        self._answer_options = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new meetingRegistrationQuestion and sets the default values.
        """
        super().__init__()
        # Answer input type of the custom registration question.
        self._answer_input_type: Optional[answer_input_type.AnswerInputType] = None
        # Answer options when answerInputType is radioButton.
        self._answer_options: Optional[List[str]] = None
        # Display name of the custom registration question.
        self._display_name: Optional[str] = None
        # Indicates whether the question is required. Default value is false.
        self._is_required: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingRegistrationQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingRegistrationQuestion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MeetingRegistrationQuestion()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the custom registration question.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the custom registration question.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "answer_input_type": lambda n : setattr(self, 'answer_input_type', n.get_enum_value(answer_input_type.AnswerInputType)),
            "answer_options": lambda n : setattr(self, 'answer_options', n.get_collection_of_primitive_values(str)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_required": lambda n : setattr(self, 'is_required', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_required(self,) -> Optional[bool]:
        """
        Gets the isRequired property value. Indicates whether the question is required. Default value is false.
        Returns: Optional[bool]
        """
        return self._is_required
    
    @is_required.setter
    def is_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRequired property value. Indicates whether the question is required. Default value is false.
        Args:
            value: Value to set for the isRequired property.
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
        writer.write_enum_value("answerInputType", self.answer_input_type)
        writer.write_collection_of_primitive_values("answerOptions", self.answer_options)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isRequired", self.is_required)
    

