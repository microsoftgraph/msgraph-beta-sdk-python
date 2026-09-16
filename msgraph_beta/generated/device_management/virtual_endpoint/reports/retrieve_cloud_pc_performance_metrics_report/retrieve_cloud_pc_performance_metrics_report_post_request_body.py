from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.cloud_pc_performance_metric_names_type import CloudPcPerformanceMetricNamesType
    from .....models.cloud_pc_vm_performance_metrics_time_range import CloudPcVmPerformanceMetricsTimeRange

@dataclass
class RetrieveCloudPcPerformanceMetricsReportPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The cloudPcId property
    cloud_pc_id: Optional[str] = None
    # The endDateTime property
    end_date_time: Optional[datetime.datetime] = None
    # The metricNames property
    metric_names: Optional[CloudPcPerformanceMetricNamesType] = None
    # The startDateTime property
    start_date_time: Optional[datetime.datetime] = None
    # The timeRange property
    time_range: Optional[CloudPcVmPerformanceMetricsTimeRange] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RetrieveCloudPcPerformanceMetricsReportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RetrieveCloudPcPerformanceMetricsReportPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RetrieveCloudPcPerformanceMetricsReportPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.cloud_pc_performance_metric_names_type import CloudPcPerformanceMetricNamesType
        from .....models.cloud_pc_vm_performance_metrics_time_range import CloudPcVmPerformanceMetricsTimeRange

        from .....models.cloud_pc_performance_metric_names_type import CloudPcPerformanceMetricNamesType
        from .....models.cloud_pc_vm_performance_metrics_time_range import CloudPcVmPerformanceMetricsTimeRange

        fields: dict[str, Callable[[Any], None]] = {
            "cloudPcId": lambda n : setattr(self, 'cloud_pc_id', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "metricNames": lambda n : setattr(self, 'metric_names', n.get_collection_of_enum_values(CloudPcPerformanceMetricNamesType)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "timeRange": lambda n : setattr(self, 'time_range', n.get_enum_value(CloudPcVmPerformanceMetricsTimeRange)),
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
        writer.write_str_value("cloudPcId", self.cloud_pc_id)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_enum_value("metricNames", self.metric_names)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("timeRange", self.time_range)
        writer.write_additional_data_value(self.additional_data)
    

