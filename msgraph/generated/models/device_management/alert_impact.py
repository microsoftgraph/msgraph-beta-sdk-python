from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..key_value_pair import KeyValuePair
    from .aggregation_type import AggregationType

@dataclass
class AlertImpact(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The aggregation type of the impact. The possible values are: count, percentage, affectedCloudPcCount, affectedCloudPcPercentage, unknownFutureValue.
    aggregation_type: Optional[AggregationType] = None
    # The detail information of the impact. For example, if the Frontline Cloud PCs near concurrency limit alert is triggered, the details contain the impacted Frontline license SKU name, such as Windows 365 Frontline 2 vCPU/8GB/128GB, and the corresponding impacted value.
    alert_impact_details: Optional[List[KeyValuePair]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number value of the impact. For the aggregation types of count and affectedCloudPcCount, the value indicates the number of affected instances. For example, 6 affectedCloudPcCount means that six Cloud PCs are affected. For the aggregation types of percentage and affectedCloudPcPercentage, the value indicates the percent of affected instances. For example, 12 affectedCloudPcPercentage means that 12% of Cloud PCs are affected.
    value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlertImpact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AlertImpact
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AlertImpact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..key_value_pair import KeyValuePair
        from .aggregation_type import AggregationType

        from ..key_value_pair import KeyValuePair
        from .aggregation_type import AggregationType

        fields: Dict[str, Callable[[Any], None]] = {
            "aggregationType": lambda n : setattr(self, 'aggregation_type', n.get_enum_value(AggregationType)),
            "alertImpactDetails": lambda n : setattr(self, 'alert_impact_details', n.get_collection_of_object_values(KeyValuePair)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("aggregationType", self.aggregation_type)
        writer.write_collection_of_object_values("alertImpactDetails", self.alert_impact_details)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

