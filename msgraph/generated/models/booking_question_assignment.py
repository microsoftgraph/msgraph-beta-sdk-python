from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class BookingQuestionAssignment(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new bookingQuestionAssignment and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether it is mandatory to answer the custom question.
        self._is_required: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # If it is mandatory to answer the custom question.
        self._question_id: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingQuestionAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingQuestionAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingQuestionAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "questionId": lambda n : setattr(self, 'question_id', n.get_str_value()),
        }
        return fields
    
    @property
    def is_required(self,) -> Optional[bool]:
        """
        Gets the isRequired property value. Indicates whether it is mandatory to answer the custom question.
        Returns: Optional[bool]
        """
        return self._is_required
    
    @is_required.setter
    def is_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRequired property value. Indicates whether it is mandatory to answer the custom question.
        Args:
            value: Value to set for the is_required property.
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def question_id(self,) -> Optional[str]:
        """
        Gets the questionId property value. If it is mandatory to answer the custom question.
        Returns: Optional[str]
        """
        return self._question_id
    
    @question_id.setter
    def question_id(self,value: Optional[str] = None) -> None:
        """
        Sets the questionId property value. If it is mandatory to answer the custom question.
        Args:
            value: Value to set for the question_id property.
        """
        self._question_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("questionId", self.question_id)
        writer.write_additional_data_value(self.additional_data)
    

