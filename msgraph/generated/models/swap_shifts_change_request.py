from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import offer_shift_request

from . import offer_shift_request

class SwapShiftsChangeRequest(offer_shift_request.OfferShiftRequest):
    def __init__(self,) -> None:
        """
        Instantiates a new SwapShiftsChangeRequest and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.swapShiftsChangeRequest"
        # Shift ID for the recipient user with whom the request is to swap.
        self._recipient_shift_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SwapShiftsChangeRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SwapShiftsChangeRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SwapShiftsChangeRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import offer_shift_request

        fields: Dict[str, Callable[[Any], None]] = {
            "recipientShiftId": lambda n : setattr(self, 'recipient_shift_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def recipient_shift_id(self,) -> Optional[str]:
        """
        Gets the recipientShiftId property value. Shift ID for the recipient user with whom the request is to swap.
        Returns: Optional[str]
        """
        return self._recipient_shift_id
    
    @recipient_shift_id.setter
    def recipient_shift_id(self,value: Optional[str] = None) -> None:
        """
        Sets the recipientShiftId property value. Shift ID for the recipient user with whom the request is to swap.
        Args:
            value: Value to set for the recipient_shift_id property.
        """
        self._recipient_shift_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("recipientShiftId", self.recipient_shift_id)
    

