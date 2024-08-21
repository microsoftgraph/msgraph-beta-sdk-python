from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aggregated_inbound_statistics import AggregatedInboundStatistics
    from .industry_data_activity_statistics import IndustryDataActivityStatistics
    from .industry_data_run_status import IndustryDataRunStatus

@dataclass
class IndustryDataRunStatistics(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The collection of statistics for each activity included in this run.
    activity_statistics: Optional[List[IndustryDataActivityStatistics]] = None
    # The aggregate statistics for all inbound flows.
    inbound_totals: Optional[AggregatedInboundStatistics] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the underlying run for the statistics.
    run_id: Optional[str] = None
    # The status property
    status: Optional[IndustryDataRunStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IndustryDataRunStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataRunStatistics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IndustryDataRunStatistics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .aggregated_inbound_statistics import AggregatedInboundStatistics
        from .industry_data_activity_statistics import IndustryDataActivityStatistics
        from .industry_data_run_status import IndustryDataRunStatus

        from .aggregated_inbound_statistics import AggregatedInboundStatistics
        from .industry_data_activity_statistics import IndustryDataActivityStatistics
        from .industry_data_run_status import IndustryDataRunStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "activityStatistics": lambda n : setattr(self, 'activity_statistics', n.get_collection_of_object_values(IndustryDataActivityStatistics)),
            "inboundTotals": lambda n : setattr(self, 'inbound_totals', n.get_object_value(AggregatedInboundStatistics)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "runId": lambda n : setattr(self, 'run_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(IndustryDataRunStatus)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

