from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .availability_item import AvailabilityItem

@dataclass
class StaffAvailabilityItem(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Each item in this collection indicates a slot and the status of the staff member.
    availability_items: Optional[List[AvailabilityItem]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the staff member.
    staff_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StaffAvailabilityItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StaffAvailabilityItem
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return StaffAvailabilityItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .availability_item import AvailabilityItem

        from .availability_item import AvailabilityItem

        fields: Dict[str, Callable[[Any], None]] = {
            "availabilityItems": lambda n : setattr(self, 'availability_items', n.get_collection_of_object_values(AvailabilityItem)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "staffId": lambda n : setattr(self, 'staff_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("availabilityItems", self.availability_items)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("staffId", self.staff_id)
        writer.write_additional_data_value(self.additional_data)
    

