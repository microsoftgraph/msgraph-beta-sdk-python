from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_localized_content = lazy_import('msgraph.generated.models.access_package_localized_content')

class AccessPackageQuestion(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageQuestion and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # ID of the question.
        self._id: Optional[str] = None
        # Specifies whether the requestor is allowed to edit answers to questions.
        self._is_answer_editable: Optional[bool] = None
        # Whether the requestor is required to supply an answer or not.
        self._is_required: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Relative position of this question when displaying a list of questions to the requestor.
        self._sequence: Optional[int] = None
        # The text of the question to show to the requestor.
        self._text: Optional[access_package_localized_content.AccessPackageLocalizedContent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageQuestion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageQuestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "is_answer_editable": lambda n : setattr(self, 'is_answer_editable', n.get_bool_value()),
            "is_required": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sequence": lambda n : setattr(self, 'sequence', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_object_value(access_package_localized_content.AccessPackageLocalizedContent)),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. ID of the question.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. ID of the question.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def is_answer_editable(self,) -> Optional[bool]:
        """
        Gets the isAnswerEditable property value. Specifies whether the requestor is allowed to edit answers to questions.
        Returns: Optional[bool]
        """
        return self._is_answer_editable
    
    @is_answer_editable.setter
    def is_answer_editable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAnswerEditable property value. Specifies whether the requestor is allowed to edit answers to questions.
        Args:
            value: Value to set for the isAnswerEditable property.
        """
        self._is_answer_editable = value
    
    @property
    def is_required(self,) -> Optional[bool]:
        """
        Gets the isRequired property value. Whether the requestor is required to supply an answer or not.
        Returns: Optional[bool]
        """
        return self._is_required
    
    @is_required.setter
    def is_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRequired property value. Whether the requestor is required to supply an answer or not.
        Args:
            value: Value to set for the isRequired property.
        """
        self._is_required = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def sequence(self,) -> Optional[int]:
        """
        Gets the sequence property value. Relative position of this question when displaying a list of questions to the requestor.
        Returns: Optional[int]
        """
        return self._sequence
    
    @sequence.setter
    def sequence(self,value: Optional[int] = None) -> None:
        """
        Sets the sequence property value. Relative position of this question when displaying a list of questions to the requestor.
        Args:
            value: Value to set for the sequence property.
        """
        self._sequence = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isAnswerEditable", self.is_answer_editable)
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("sequence", self.sequence)
        writer.write_object_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def text(self,) -> Optional[access_package_localized_content.AccessPackageLocalizedContent]:
        """
        Gets the text property value. The text of the question to show to the requestor.
        Returns: Optional[access_package_localized_content.AccessPackageLocalizedContent]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[access_package_localized_content.AccessPackageLocalizedContent] = None) -> None:
        """
        Sets the text property value. The text of the question to show to the requestor.
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    

