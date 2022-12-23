from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class TeamworkPeripheral(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkPeripheral and sets the default values.
        """
        super().__init__()
        # Display name for the peripheral.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The product ID of the device. Each product from a vendor has its own ID.
        self._product_id: Optional[str] = None
        # The unique identifier for the vendor of the device. Each vendor has a unique ID.
        self._vendor_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkPeripheral:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkPeripheral
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkPeripheral()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name for the peripheral.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name for the peripheral.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "product_id": lambda n : setattr(self, 'product_id', n.get_str_value()),
            "vendor_id": lambda n : setattr(self, 'vendor_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def product_id(self,) -> Optional[str]:
        """
        Gets the productId property value. The product ID of the device. Each product from a vendor has its own ID.
        Returns: Optional[str]
        """
        return self._product_id
    
    @product_id.setter
    def product_id(self,value: Optional[str] = None) -> None:
        """
        Sets the productId property value. The product ID of the device. Each product from a vendor has its own ID.
        Args:
            value: Value to set for the productId property.
        """
        self._product_id = value
    
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
        writer.write_str_value("productId", self.product_id)
        writer.write_str_value("vendorId", self.vendor_id)
    
    @property
    def vendor_id(self,) -> Optional[str]:
        """
        Gets the vendorId property value. The unique identifier for the vendor of the device. Each vendor has a unique ID.
        Returns: Optional[str]
        """
        return self._vendor_id
    
    @vendor_id.setter
    def vendor_id(self,value: Optional[str] = None) -> None:
        """
        Sets the vendorId property value. The unique identifier for the vendor of the device. Each vendor has a unique ID.
        Args:
            value: Value to set for the vendorId property.
        """
        self._vendor_id = value
    

