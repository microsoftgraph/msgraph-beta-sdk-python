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
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.bookingBusiness":
                from . import booking_business

                return booking_business.BookingBusiness()
            if mapping_value == "#microsoft.graph.bookingCustomer":
                from . import booking_customer

                return booking_customer.BookingCustomer()
            if mapping_value == "#microsoft.graph.bookingPerson":
                from . import booking_person

                return booking_person.BookingPerson()
            if mapping_value == "#microsoft.graph.bookingService":
                from . import booking_service

                return booking_service.BookingService()
            if mapping_value == "#microsoft.graph.bookingStaffMember":
                from . import booking_staff_member

                return booking_staff_member.BookingStaffMember()
        return BookingNamedEntity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
    

