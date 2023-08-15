from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_answer_choice import AccessPackageAnswerChoice
    from .access_package_question import AccessPackageQuestion

from .access_package_question import AccessPackageQuestion

@dataclass
class AccessPackageMultipleChoiceQuestion(AccessPackageQuestion):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessPackageMultipleChoiceQuestion"
    # Indicates whether requestor can select multiple choices as their answer.
    allows_multiple_selection: Optional[bool] = None
    # List of answer choices.
    choices: Optional[List[AccessPackageAnswerChoice]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageMultipleChoiceQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
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
        from .access_package_answer_choice import AccessPackageAnswerChoice
        from .access_package_question import AccessPackageQuestion

        from .access_package_answer_choice import AccessPackageAnswerChoice
        from .access_package_question import AccessPackageQuestion

        fields: Dict[str, Callable[[Any], None]] = {
            "allowsMultipleSelection": lambda n : setattr(self, 'allows_multiple_selection', n.get_bool_value()),
            "choices": lambda n : setattr(self, 'choices', n.get_collection_of_object_values(AccessPackageAnswerChoice)),
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
        writer.write_bool_value("allowsMultipleSelection", self.allows_multiple_selection)
        writer.write_collection_of_object_values("choices", self.choices)
    

