from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_localized_content import AccessPackageLocalizedContent
    from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
    from .access_package_text_input_question import AccessPackageTextInputQuestion

@dataclass
class AccessPackageQuestion(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # ID of the question.
    id: Optional[str] = None
    # Specifies whether the requestor is allowed to edit answers to questions.
    is_answer_editable: Optional[bool] = None
    # Whether the requestor is required to supply an answer or not.
    is_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Relative position of this question when displaying a list of questions to the requestor.
    sequence: Optional[int] = None
    # The text of the question to show to the requestor.
    text: Optional[AccessPackageLocalizedContent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageQuestion
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageMultipleChoiceQuestion".casefold():
            from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion

            return AccessPackageMultipleChoiceQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageTextInputQuestion".casefold():
            from .access_package_text_input_question import AccessPackageTextInputQuestion

            return AccessPackageTextInputQuestion()
        return AccessPackageQuestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_localized_content import AccessPackageLocalizedContent
        from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
        from .access_package_text_input_question import AccessPackageTextInputQuestion

        from .access_package_localized_content import AccessPackageLocalizedContent
        from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
        from .access_package_text_input_question import AccessPackageTextInputQuestion

        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isAnswerEditable": lambda n : setattr(self, 'is_answer_editable', n.get_bool_value()),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sequence": lambda n : setattr(self, 'sequence', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_object_value(AccessPackageLocalizedContent)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isAnswerEditable", self.is_answer_editable)
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_int_value("sequence", self.sequence)
        writer.write_object_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    

