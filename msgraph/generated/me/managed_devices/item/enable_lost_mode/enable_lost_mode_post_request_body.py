from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class EnableLostModePostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new enableLostModePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The footer property
        self._footer: Optional[str] = None
        # The message property
        self._message: Optional[str] = None
        # The phoneNumber property
        self._phone_number: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EnableLostModePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EnableLostModePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EnableLostModePostRequestBody()
    
    @property
    def footer(self,) -> Optional[str]:
        """
        Gets the footer property value. The footer property
        Returns: Optional[str]
        """
        return self._footer
    
    @footer.setter
    def footer(self,value: Optional[str] = None) -> None:
        """
        Sets the footer property value. The footer property
        Args:
            value: Value to set for the footer property.
        """
        self._footer = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "footer": lambda n : setattr(self, 'footer', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
        }
        return fields
    
    @property
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. The message property
        Returns: Optional[str]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. The message property
        Args:
            value: Value to set for the message property.
        """
        self._message = value
    
    @property
    def phone_number(self,) -> Optional[str]:
        """
        Gets the phoneNumber property value. The phoneNumber property
        Returns: Optional[str]
        """
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the phoneNumber property value. The phoneNumber property
        Args:
            value: Value to set for the phone_number property.
        """
        self._phone_number = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("footer", self.footer)
        writer.write_str_value("message", self.message)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_additional_data_value(self.additional_data)
    

