from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_answer_choice, access_package_question

from . import access_package_question

@dataclass
class AccessPackageMultipleChoiceQuestion(access_package_question.AccessPackageQuestion):
    odata_type = "#microsoft.graph.accessPackageMultipleChoiceQuestion"
    # Indicates whether requestor can select multiple choices as their answer.
    allows_multiple_selection: Optional[bool] = None
    # List of answer choices.
    choices: Optional[List[access_package_answer_choice.AccessPackageAnswerChoice]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageMultipleChoiceQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageMultipleChoiceQuestion
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageMultipleChoiceQuestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_answer_choice, access_package_question

        from . import access_package_answer_choice, access_package_question

        fields: Dict[str, Callable[[Any], None]] = {
            "allowsMultipleSelection": lambda n : setattr(self, 'allows_multiple_selection', n.get_bool_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("allowsMultipleSelection", self.allows_multiple_selection)
        writer.write_collection_of_object_values("choices", self.choices)
    

