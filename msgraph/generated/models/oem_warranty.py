from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import warranty_offer

@dataclass
class OemWarranty(AdditionalDataHolder, Parsable):
    """
    OEM Warranty information for a given device
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # List of additional warranty offers. This collection can contain a maximum of 100 elements.
    additional_warranties: Optional[List[warranty_offer.WarrantyOffer]] = None
    # List of base warranty offers. This collection can contain a maximum of 100 elements.
    base_warranties: Optional[List[warranty_offer.WarrantyOffer]] = None
    # Device configuration page URL
    device_configuration_url: Optional[str] = None
    # Device warranty page URL
    device_warranty_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OemWarranty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OemWarranty
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OemWarranty()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import warranty_offer

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalWarranties": lambda n : setattr(self, 'additional_warranties', n.get_collection_of_object_values(warranty_offer.WarrantyOffer)),
            "baseWarranties": lambda n : setattr(self, 'base_warranties', n.get_collection_of_object_values(warranty_offer.WarrantyOffer)),
            "deviceConfigurationUrl": lambda n : setattr(self, 'device_configuration_url', n.get_str_value()),
            "deviceWarrantyUrl": lambda n : setattr(self, 'device_warranty_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("additionalWarranties", self.additional_warranties)
        writer.write_collection_of_object_values("baseWarranties", self.base_warranties)
        writer.write_str_value("deviceConfigurationUrl", self.device_configuration_url)
        writer.write_str_value("deviceWarrantyUrl", self.device_warranty_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

