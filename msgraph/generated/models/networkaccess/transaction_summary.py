from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import traffic_type

@dataclass
class TransactionSummary(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The blockedCount property
    blocked_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The totalCount property
    total_count: Optional[int] = None
    # The trafficType property
    traffic_type: Optional[traffic_type.TrafficType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TransactionSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TransactionSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TransactionSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import traffic_type

        from . import traffic_type

        fields: Dict[str, Callable[[Any], None]] = {
            "blockedCount": lambda n : setattr(self, 'blocked_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "totalCount": lambda n : setattr(self, 'total_count', n.get_int_value()),
            "trafficType": lambda n : setattr(self, 'traffic_type', n.get_enum_value(traffic_type.TrafficType)),
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
        writer.write_int_value("blockedCount", self.blocked_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("totalCount", self.total_count)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_additional_data_value(self.additional_data)
    

