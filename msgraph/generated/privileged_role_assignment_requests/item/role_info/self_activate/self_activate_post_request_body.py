from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class SelfActivatePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the selfActivate method.
    """
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
        Instantiates a new selfActivatePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The duration property
        self._duration: Optional[str] = None
        # The reason property
        self._reason: Optional[str] = None
        # The ticketNumber property
        self._ticket_number: Optional[str] = None
        # The ticketSystem property
        self._ticket_system: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SelfActivatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SelfActivatePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SelfActivatePostRequestBody()
    
    @property
    def duration(self,) -> Optional[str]:
        """
        Gets the duration property value. The duration property
        Returns: Optional[str]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[str] = None) -> None:
        """
        Sets the duration property value. The duration property
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "duration": lambda n : setattr(self, 'duration', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "ticket_number": lambda n : setattr(self, 'ticket_number', n.get_str_value()),
            "ticket_system": lambda n : setattr(self, 'ticket_system', n.get_str_value()),
        }
        return fields
    
    @property
    def reason(self,) -> Optional[str]:
        """
        Gets the reason property value. The reason property
        Returns: Optional[str]
        """
        return self._reason
    
    @reason.setter
    def reason(self,value: Optional[str] = None) -> None:
        """
        Sets the reason property value. The reason property
        Args:
            value: Value to set for the reason property.
        """
        self._reason = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("duration", self.duration)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("ticketNumber", self.ticket_number)
        writer.write_str_value("ticketSystem", self.ticket_system)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def ticket_number(self,) -> Optional[str]:
        """
        Gets the ticketNumber property value. The ticketNumber property
        Returns: Optional[str]
        """
        return self._ticket_number
    
    @ticket_number.setter
    def ticket_number(self,value: Optional[str] = None) -> None:
        """
        Sets the ticketNumber property value. The ticketNumber property
        Args:
            value: Value to set for the ticketNumber property.
        """
        self._ticket_number = value
    
    @property
    def ticket_system(self,) -> Optional[str]:
        """
        Gets the ticketSystem property value. The ticketSystem property
        Returns: Optional[str]
        """
        return self._ticket_system
    
    @ticket_system.setter
    def ticket_system(self,value: Optional[str] = None) -> None:
        """
        Sets the ticketSystem property value. The ticketSystem property
        Args:
            value: Value to set for the ticketSystem property.
        """
        self._ticket_system = value
    

