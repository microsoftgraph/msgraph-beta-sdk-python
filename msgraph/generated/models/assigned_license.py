from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class AssignedLicense(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # A collection of the unique identifiers for plans that have been disabled.
    disabled_plans: Optional[List[UUID]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier for the SKU.
    sku_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignedLicense:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignedLicense
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AssignedLicense()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "disabledPlans": lambda n : setattr(self, 'disabled_plans', n.get_collection_of_primitive_values(UUID)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "skuId": lambda n : setattr(self, 'sku_id', n.get_uuid_value()),
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
        writer.write_collection_of_primitive_values("disabledPlans", self.disabled_plans)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_uuid_value("skuId", self.sku_id)
        writer.write_additional_data_value(self.additional_data)
    

