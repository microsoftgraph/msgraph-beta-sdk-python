from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import aggregated_inbound_statistics, industry_data_activity_statistics, industry_data_run_status

@dataclass
class IndustryDataRunStatistics(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The collection of statistics for each activity included in this run.
    activity_statistics: Optional[List[industry_data_activity_statistics.IndustryDataActivityStatistics]] = None
    # The aggregate statistics for all inbound flows.
    inbound_totals: Optional[aggregated_inbound_statistics.AggregatedInboundStatistics] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the underlying run for the statistics.
    run_id: Optional[str] = None
    # The status property
    status: Optional[industry_data_run_status.IndustryDataRunStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IndustryDataRunStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataRunStatistics
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IndustryDataRunStatistics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import aggregated_inbound_statistics, industry_data_activity_statistics, industry_data_run_status

        fields: Dict[str, Callable[[Any], None]] = {
            "activityStatistics": lambda n : setattr(self, 'activity_statistics', n.get_collection_of_object_values(industry_data_activity_statistics.IndustryDataActivityStatistics)),
            "inboundTotals": lambda n : setattr(self, 'inbound_totals', n.get_object_value(aggregated_inbound_statistics.AggregatedInboundStatistics)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "runId": lambda n : setattr(self, 'run_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(industry_data_run_status.IndustryDataRunStatus)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

