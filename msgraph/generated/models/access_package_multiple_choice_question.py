from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_answer_choice = lazy_import('msgraph.generated.models.access_package_answer_choice')
access_package_question = lazy_import('msgraph.generated.models.access_package_question')

class AccessPackageMultipleChoiceQuestion(access_package_question.AccessPackageQuestion):
    @property
    def allows_multiple_selection(self,) -> Optional[bool]:
        """
        Gets the allowsMultipleSelection property value. Indicates whether requestor can select multiple choices as their answer.
        Returns: Optional[bool]
        """
        return self._allows_multiple_selection
    
    @allows_multiple_selection.setter
    def allows_multiple_selection(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowsMultipleSelection property value. Indicates whether requestor can select multiple choices as their answer.
        Args:
            value: Value to set for the allowsMultipleSelection property.
        """
        self._allows_multiple_selection = value
    
    @property
    def choices(self,) -> Optional[List[access_package_answer_choice.AccessPackageAnswerChoice]]:
        """
        Gets the choices property value. List of answer choices.
        Returns: Optional[List[access_package_answer_choice.AccessPackageAnswerChoice]]
        """
        return self._choices
    
    @choices.setter
    def choices(self,value: Optional[List[access_package_answer_choice.AccessPackageAnswerChoice]] = None) -> None:
        """
        Sets the choices property value. List of answer choices.
        Args:
            value: Value to set for the choices property.
        """
        self._choices = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AccessPackageMultipleChoiceQuestion and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.accessPackageMultipleChoiceQuestion"
        # Indicates whether requestor can select multiple choices as their answer.
        self._allows_multiple_selection: Optional[bool] = None
        # List of answer choices.
        self._choices: Optional[List[access_package_answer_choice.AccessPackageAnswerChoice]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageMultipleChoiceQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageMultipleChoiceQuestion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageMultipleChoiceQuestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allows_multiple_selection": lambda n : setattr(self, 'allows_multiple_selection', n.get_bool_value()),
            "choices": lambda n : setattr(self, 'choices', n.get_collection_of_object_values(access_package_answer_choice.AccessPackageAnswerChoice)),
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
        writer.write_bool_value("allowsMultipleSelection", self.allows_multiple_selection)
        writer.write_collection_of_object_values("choices", self.choices)
    

