from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_business import BookingBusiness
    from .booking_customer import BookingCustomer
    from .booking_person import BookingPerson
    from .booking_service import BookingService
    from .booking_staff_member import BookingStaffMember
    from .entity import Entity

from .entity import Entity

@dataclass
class BookingNamedEntity(Entity):
    """
    Booking entities that provide a display name.
    """
    # A name for the derived entity, which interfaces with customers.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingNamedEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingNamedEntity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingBusiness".casefold():
            from .booking_business import BookingBusiness

            return BookingBusiness()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCustomer".casefold():
            from .booking_customer import BookingCustomer

            return BookingCustomer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingPerson".casefold():
            from .booking_person import BookingPerson

            return BookingPerson()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingService".casefold():
            from .booking_service import BookingService

            return BookingService()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingStaffMember".casefold():
            from .booking_staff_member import BookingStaffMember

            return BookingStaffMember()
        return BookingNamedEntity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .booking_business import BookingBusiness
        from .booking_customer import BookingCustomer
        from .booking_person import BookingPerson
        from .booking_service import BookingService
        from .booking_staff_member import BookingStaffMember
        from .entity import Entity

        from .booking_business import BookingBusiness
        from .booking_customer import BookingCustomer
        from .booking_person import BookingPerson
        from .booking_service import BookingService
        from .booking_staff_member import BookingStaffMember
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
    

