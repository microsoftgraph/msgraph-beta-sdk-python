from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import booking_customer, booking_named_entity, booking_staff_member

from . import booking_named_entity

class BookingPerson(booking_named_entity.BookingNamedEntity):
    """
    Represents a booking customer or staff member.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new bookingPerson and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.bookingPerson"
        # The email address of the person.
        self._email_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingPerson:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingPerson
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.bookingCustomer":
                from . import booking_customer

                return booking_customer.BookingCustomer()
            if mapping_value == "#microsoft.graph.bookingStaffMember":
                from . import booking_staff_member

                return booking_staff_member.BookingStaffMember()
        return BookingPerson()
    
    @property
    def email_address(self,) -> Optional[str]:
        """
        Gets the emailAddress property value. The email address of the person.
        Returns: Optional[str]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailAddress property value. The email address of the person.
        Args:
            value: Value to set for the email_address property.
        """
        self._email_address = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import booking_customer, booking_named_entity, booking_staff_member

        fields: Dict[str, Callable[[Any], None]] = {
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
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
        writer.write_str_value("emailAddress", self.email_address)
    

