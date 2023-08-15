from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_customer import BookingCustomer
    from .booking_named_entity import BookingNamedEntity
    from .booking_staff_member import BookingStaffMember

from .booking_named_entity import BookingNamedEntity

@dataclass
class BookingPerson(BookingNamedEntity):
    """
    Represents a booking customer or staff member.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.bookingPerson"
    # The email address of the person.
    email_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingPerson:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingPerson
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCustomer".casefold():
            from .booking_customer import BookingCustomer

            return BookingCustomer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingStaffMember".casefold():
            from .booking_staff_member import BookingStaffMember

            return BookingStaffMember()
        return BookingPerson()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .booking_customer import BookingCustomer
        from .booking_named_entity import BookingNamedEntity
        from .booking_staff_member import BookingStaffMember

        from .booking_customer import BookingCustomer
        from .booking_named_entity import BookingNamedEntity
        from .booking_staff_member import BookingStaffMember

        fields: Dict[str, Callable[[Any], None]] = {
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
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
        writer.write_str_value("emailAddress", self.email_address)
    

