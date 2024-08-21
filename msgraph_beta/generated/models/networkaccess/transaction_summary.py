from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .traffic_type import TrafficType

@dataclass
class TransactionSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The number of transactions that were blocked.
    blocked_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The total number of transactions.
    total_count: Optional[int] = None
    # The trafficType property
    traffic_type: Optional[TrafficType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TransactionSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TransactionSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TransactionSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .traffic_type import TrafficType

        from .traffic_type import TrafficType

        fields: Dict[str, Callable[[Any], None]] = {
            "blockedCount": lambda n : setattr(self, 'blocked_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "totalCount": lambda n : setattr(self, 'total_count', n.get_int_value()),
            "trafficType": lambda n : setattr(self, 'traffic_type', n.get_enum_value(TrafficType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("blockedCount", self.blocked_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("totalCount", self.total_count)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_additional_data_value(self.additional_data)
    

