from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import booking_business, booking_customer, booking_person, booking_service, booking_staff_member, entity

from . import entity

@dataclass
class BookingNamedEntity(entity.Entity):
    # A name for the derived entity, which interfaces with customers.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingNamedEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingNamedEntity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingBusiness".casefold():
            from . import booking_business

            return booking_business.BookingBusiness()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCustomer".casefold():
            from . import booking_customer

            return booking_customer.BookingCustomer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingPerson".casefold():
            from . import booking_person

            return booking_person.BookingPerson()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingService".casefold():
            from . import booking_service

            return booking_service.BookingService()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingStaffMember".casefold():
            from . import booking_staff_member

            return booking_staff_member.BookingStaffMember()
        return BookingNamedEntity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import booking_business, booking_customer, booking_person, booking_service, booking_staff_member, entity

        from . import booking_business, booking_customer, booking_person, booking_service, booking_staff_member, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
    

