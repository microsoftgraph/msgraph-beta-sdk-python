from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import availability_item

class StaffAvailabilityItem(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new staffAvailabilityItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Each item in this collection indicates a slot and the status of the staff member.
        self._availability_items: Optional[List[availability_item.AvailabilityItem]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The ID of the staff member.
        self._staff_id: Optional[str] = None
    
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
    
    @property
    def availability_items(self,) -> Optional[List[availability_item.AvailabilityItem]]:
        """
        Gets the availabilityItems property value. Each item in this collection indicates a slot and the status of the staff member.
        Returns: Optional[List[availability_item.AvailabilityItem]]
        """
        return self._availability_items
    
    @availability_items.setter
    def availability_items(self,value: Optional[List[availability_item.AvailabilityItem]] = None) -> None:
        """
        Sets the availabilityItems property value. Each item in this collection indicates a slot and the status of the staff member.
        Args:
            value: Value to set for the availability_items property.
        """
        self._availability_items = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StaffAvailabilityItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: StaffAvailabilityItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return StaffAvailabilityItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import availability_item

        fields: Dict[str, Callable[[Any], None]] = {
            "availabilityItems": lambda n : setattr(self, 'availability_items', n.get_collection_of_object_values(availability_item.AvailabilityItem)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "staffId": lambda n : setattr(self, 'staff_id', n.get_str_value()),
        }
        return fields
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("availabilityItems", self.availability_items)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("staffId", self.staff_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def staff_id(self,) -> Optional[str]:
        """
        Gets the staffId property value. The ID of the staff member.
        Returns: Optional[str]
        """
        return self._staff_id
    
    @staff_id.setter
    def staff_id(self,value: Optional[str] = None) -> None:
        """
        Sets the staffId property value. The ID of the staff member.
        Args:
            value: Value to set for the staff_id property.
        """
        self._staff_id = value
    

