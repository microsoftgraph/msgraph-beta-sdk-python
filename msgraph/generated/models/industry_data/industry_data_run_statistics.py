from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import aggregated_inbound_statistics, industry_data_activity_statistics, industry_data_run_status

class IndustryDataRunStatistics(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new industryDataRunStatistics and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The collection of statistics for each activity included in this run.
        self._activity_statistics: Optional[List[industry_data_activity_statistics.IndustryDataActivityStatistics]] = None
        # The aggregate statistics for all inbound flows.
        self._inbound_totals: Optional[aggregated_inbound_statistics.AggregatedInboundStatistics] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The ID of the underlying run for the statistics.
        self._run_id: Optional[str] = None
        # The status property
        self._status: Optional[industry_data_run_status.IndustryDataRunStatus] = None
    
    @property
    def activity_statistics(self,) -> Optional[List[industry_data_activity_statistics.IndustryDataActivityStatistics]]:
        """
        Gets the activityStatistics property value. The collection of statistics for each activity included in this run.
        Returns: Optional[List[industry_data_activity_statistics.IndustryDataActivityStatistics]]
        """
        return self._activity_statistics
    
    @activity_statistics.setter
    def activity_statistics(self,value: Optional[List[industry_data_activity_statistics.IndustryDataActivityStatistics]] = None) -> None:
        """
        Sets the activityStatistics property value. The collection of statistics for each activity included in this run.
        Args:
            value: Value to set for the activity_statistics property.
        """
        self._activity_statistics = value
    
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
    
    @property
    def inbound_totals(self,) -> Optional[aggregated_inbound_statistics.AggregatedInboundStatistics]:
        """
        Gets the inboundTotals property value. The aggregate statistics for all inbound flows.
        Returns: Optional[aggregated_inbound_statistics.AggregatedInboundStatistics]
        """
        return self._inbound_totals
    
    @inbound_totals.setter
    def inbound_totals(self,value: Optional[aggregated_inbound_statistics.AggregatedInboundStatistics] = None) -> None:
        """
        Sets the inboundTotals property value. The aggregate statistics for all inbound flows.
        Args:
            value: Value to set for the inbound_totals property.
        """
        self._inbound_totals = value
    
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
    
    @property
    def run_id(self,) -> Optional[str]:
        """
        Gets the runId property value. The ID of the underlying run for the statistics.
        Returns: Optional[str]
        """
        return self._run_id
    
    @run_id.setter
    def run_id(self,value: Optional[str] = None) -> None:
        """
        Sets the runId property value. The ID of the underlying run for the statistics.
        Args:
            value: Value to set for the run_id property.
        """
        self._run_id = value
    
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
    
    @property
    def status(self,) -> Optional[industry_data_run_status.IndustryDataRunStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[industry_data_run_status.IndustryDataRunStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[industry_data_run_status.IndustryDataRunStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

