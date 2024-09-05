from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .traffic_type import TrafficType

@dataclass
class DestinationSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The number of the destinationSummary objects, aggregated by Global Secure Access service.
    count: Optional[int] = None
    # The IP address or FQDN of the destination.
    destination: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The traffic classification. The allowed values are internet, private, microsoft365, all, and unknownFutureValue.
    traffic_type: Optional[TrafficType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DestinationSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DestinationSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DestinationSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .traffic_type import TrafficType

        from .traffic_type import TrafficType

        fields: Dict[str, Callable[[Any], None]] = {
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "destination": lambda n : setattr(self, 'destination', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_int_value("count", self.count)
        writer.write_str_value("destination", self.destination)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_additional_data_value(self.additional_data)
    

