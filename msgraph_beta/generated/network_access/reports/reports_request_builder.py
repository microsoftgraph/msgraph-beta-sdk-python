from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.networkaccess.reports import Reports
    from ...models.o_data_errors.o_data_error import ODataError
    from .microsoft_graph_networkaccess_cross_tenant_access_report_with_start_date_time_with_end_date_time.microsoft_graph_networkaccess_cross_tenant_access_report_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphNetworkaccessCrossTenantAccessReportWithStartDateTimeWithEndDateTimeRequestBuilder
    from .microsoft_graph_networkaccess_destination_report_with_start_date_time_with_end_date_time.microsoft_graph_networkaccess_destination_report_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphNetworkaccessDestinationReportWithStartDateTimeWithEndDateTimeRequestBuilder
    from .microsoft_graph_networkaccess_device_report_with_start_date_time_with_end_date_time.microsoft_graph_networkaccess_device_report_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphNetworkaccessDeviceReportWithStartDateTimeWithEndDateTimeRequestBuilder
    from .microsoft_graph_networkaccess_entities_summaries_with_start_date_time_with_end_date_time.microsoft_graph_networkaccess_entities_summaries_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphNetworkaccessEntitiesSummariesWithStartDateTimeWithEndDateTimeRequestBuilder
    from .microsoft_graph_networkaccess_get_cross_tenant_summary_with_start_date_time_with_end_date_time_with_discovery_pivot_date_time.microsoft_graph_networkaccess_get_cross_tenant_summary_with_start_date_time_with_end_date_time_with_discovery_pivot_date_time_request_builder import MicrosoftGraphNetworkaccessGetCrossTenantSummaryWithStartDateTimeWithEndDateTimeWithDiscoveryPivotDateTimeRequestBuilder
    from .microsoft_graph_networkaccess_get_destination_summaries_with_start_date_time_with_end_date_time_with_aggregated_by.microsoft_graph_networkaccess_get_destination_summaries_with_start_date_time_with_end_date_time_with_aggregated_by_request_builder import MicrosoftGraphNetworkaccessGetDestinationSummariesWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilder
    from .microsoft_graph_networkaccess_get_device_usage_summary_with_start_date_time_with_end_date_time_with_activity_pivot_date_time.microsoft_graph_networkaccess_get_device_usage_summary_with_start_date_time_with_end_date_time_with_activity_pivot_date_time_request_builder import MicrosoftGraphNetworkaccessGetDeviceUsageSummaryWithStartDateTimeWithEndDateTimeWithActivityPivotDateTimeRequestBuilder
    from .microsoft_graph_networkaccess_get_discovered_application_segment_report_with_start_date_time_with_end_date_timeuser_id_user_id.microsoft_graph_networkaccess_get_discovered_application_segment_report_with_start_date_time_with_end_date_timeuser_id_user_id_request_builder import MicrosoftGraphNetworkaccessGetDiscoveredApplicationSegmentReportWithStartDateTimeWithEndDateTimeuserIdUserIdRequestBuilder
    from .microsoft_graph_networkaccess_transaction_summaries_with_start_date_time_with_end_date_time.microsoft_graph_networkaccess_transaction_summaries_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphNetworkaccessTransactionSummariesWithStartDateTimeWithEndDateTimeRequestBuilder
    from .microsoft_graph_networkaccess_usage_profiling_with_start_date_time_with_end_date_time_with_aggregated_bydiscovered_application_segment_id_discovered_application_segment_id.microsoft_graph_networkaccess_usage_profiling_with_start_date_time_with_end_date_time_with_aggregated_bydiscovered_application_segment_id_discovered_application_segment_id_request_builder import MicrosoftGraphNetworkaccessUsageProfilingWithStartDateTimeWithEndDateTimeWithAggregatedBydiscoveredApplicationSegmentIdDiscoveredApplicationSegmentIdRequestBuilder
    from .microsoft_graph_networkaccess_user_report_with_start_date_time_with_end_date_timediscovered_application_segment_id_discovered_application_segment_id.microsoft_graph_networkaccess_user_report_with_start_date_time_with_end_date_timediscovered_application_segment_id_discovered_application_segment_id_request_builder import MicrosoftGraphNetworkaccessUserReportWithStartDateTimeWithEndDateTimediscoveredApplicationSegmentIdDiscoveredApplicationSegmentIdRequestBuilder
    from .microsoft_graph_networkaccess_web_category_report_with_start_date_time_with_end_date_time.microsoft_graph_networkaccess_web_category_report_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphNetworkaccessWebCategoryReportWithStartDateTimeWithEndDateTimeRequestBuilder

class ReportsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the reports property of the microsoft.graph.networkaccess.networkAccessRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ReportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/networkAccess/reports{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property reports for networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ReportsRequestBuilderGetQueryParameters]] = None) -> Optional[Reports]:
        """
        Represents the status of the Global Secure Access services for the tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Reports]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.networkaccess.reports import Reports

        return await self.request_adapter.send_async(request_info, Reports, error_mapping)
    
    def microsoft_graph_networkaccess_cross_tenant_access_report_with_start_date_time_with_end_date_time(self,end_date_time: datetime.datetime, start_date_time: datetime.datetime) -> MicrosoftGraphNetworkaccessCrossTenantAccessReportWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the crossTenantAccessReport method.
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: MicrosoftGraphNetworkaccessCrossTenantAccessReportWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_cross_tenant_access_report_with_start_date_time_with_end_date_time.microsoft_graph_networkaccess_cross_tenant_access_report_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphNetworkaccessCrossTenantAccessReportWithStartDateTimeWithEndDateTimeRequestBuilder

        return MicrosoftGraphNetworkaccessCrossTenantAccessReportWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_destination_report_with_start_date_time_with_end_date_time(self,end_date_time: datetime.datetime, start_date_time: datetime.datetime) -> MicrosoftGraphNetworkaccessDestinationReportWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the destinationReport method.
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: MicrosoftGraphNetworkaccessDestinationReportWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_destination_report_with_start_date_time_with_end_date_time.microsoft_graph_networkaccess_destination_report_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphNetworkaccessDestinationReportWithStartDateTimeWithEndDateTimeRequestBuilder

        return MicrosoftGraphNetworkaccessDestinationReportWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_device_report_with_start_date_time_with_end_date_time(self,end_date_time: datetime.datetime, start_date_time: datetime.datetime) -> MicrosoftGraphNetworkaccessDeviceReportWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the deviceReport method.
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: MicrosoftGraphNetworkaccessDeviceReportWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_device_report_with_start_date_time_with_end_date_time.microsoft_graph_networkaccess_device_report_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphNetworkaccessDeviceReportWithStartDateTimeWithEndDateTimeRequestBuilder

        return MicrosoftGraphNetworkaccessDeviceReportWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_entities_summaries_with_start_date_time_with_end_date_time(self,end_date_time: datetime.datetime, start_date_time: datetime.datetime) -> MicrosoftGraphNetworkaccessEntitiesSummariesWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the entitiesSummaries method.
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: MicrosoftGraphNetworkaccessEntitiesSummariesWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_entities_summaries_with_start_date_time_with_end_date_time.microsoft_graph_networkaccess_entities_summaries_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphNetworkaccessEntitiesSummariesWithStartDateTimeWithEndDateTimeRequestBuilder

        return MicrosoftGraphNetworkaccessEntitiesSummariesWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_get_cross_tenant_summary_with_start_date_time_with_end_date_time_with_discovery_pivot_date_time(self,discovery_pivot_date_time: datetime.datetime, end_date_time: datetime.datetime, start_date_time: datetime.datetime) -> MicrosoftGraphNetworkaccessGetCrossTenantSummaryWithStartDateTimeWithEndDateTimeWithDiscoveryPivotDateTimeRequestBuilder:
        """
        Provides operations to call the getCrossTenantSummary method.
        param discovery_pivot_date_time: Usage: discoveryPivotDateTime={discoveryPivotDateTime}
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: MicrosoftGraphNetworkaccessGetCrossTenantSummaryWithStartDateTimeWithEndDateTimeWithDiscoveryPivotDateTimeRequestBuilder
        """
        if discovery_pivot_date_time is None:
            raise TypeError("discovery_pivot_date_time cannot be null.")
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_get_cross_tenant_summary_with_start_date_time_with_end_date_time_with_discovery_pivot_date_time.microsoft_graph_networkaccess_get_cross_tenant_summary_with_start_date_time_with_end_date_time_with_discovery_pivot_date_time_request_builder import MicrosoftGraphNetworkaccessGetCrossTenantSummaryWithStartDateTimeWithEndDateTimeWithDiscoveryPivotDateTimeRequestBuilder

        return MicrosoftGraphNetworkaccessGetCrossTenantSummaryWithStartDateTimeWithEndDateTimeWithDiscoveryPivotDateTimeRequestBuilder(self.request_adapter, self.path_parameters, discovery_pivot_date_time, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_get_destination_summaries_with_start_date_time_with_end_date_time_with_aggregated_by(self,aggregated_by: str, end_date_time: datetime.datetime, start_date_time: datetime.datetime) -> MicrosoftGraphNetworkaccessGetDestinationSummariesWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilder:
        """
        Provides operations to call the getDestinationSummaries method.
        param aggregated_by: Usage: aggregatedBy='{aggregatedBy}'
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: MicrosoftGraphNetworkaccessGetDestinationSummariesWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilder
        """
        if aggregated_by is None:
            raise TypeError("aggregated_by cannot be null.")
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_get_destination_summaries_with_start_date_time_with_end_date_time_with_aggregated_by.microsoft_graph_networkaccess_get_destination_summaries_with_start_date_time_with_end_date_time_with_aggregated_by_request_builder import MicrosoftGraphNetworkaccessGetDestinationSummariesWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilder

        return MicrosoftGraphNetworkaccessGetDestinationSummariesWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilder(self.request_adapter, self.path_parameters, aggregated_by, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_get_device_usage_summary_with_start_date_time_with_end_date_time_with_activity_pivot_date_time(self,activity_pivot_date_time: datetime.datetime, end_date_time: datetime.datetime, start_date_time: datetime.datetime) -> MicrosoftGraphNetworkaccessGetDeviceUsageSummaryWithStartDateTimeWithEndDateTimeWithActivityPivotDateTimeRequestBuilder:
        """
        Provides operations to call the getDeviceUsageSummary method.
        param activity_pivot_date_time: Usage: activityPivotDateTime={activityPivotDateTime}
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: MicrosoftGraphNetworkaccessGetDeviceUsageSummaryWithStartDateTimeWithEndDateTimeWithActivityPivotDateTimeRequestBuilder
        """
        if activity_pivot_date_time is None:
            raise TypeError("activity_pivot_date_time cannot be null.")
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_get_device_usage_summary_with_start_date_time_with_end_date_time_with_activity_pivot_date_time.microsoft_graph_networkaccess_get_device_usage_summary_with_start_date_time_with_end_date_time_with_activity_pivot_date_time_request_builder import MicrosoftGraphNetworkaccessGetDeviceUsageSummaryWithStartDateTimeWithEndDateTimeWithActivityPivotDateTimeRequestBuilder

        return MicrosoftGraphNetworkaccessGetDeviceUsageSummaryWithStartDateTimeWithEndDateTimeWithActivityPivotDateTimeRequestBuilder(self.request_adapter, self.path_parameters, activity_pivot_date_time, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_get_discovered_application_segment_report_with_start_date_time_with_end_date_timeuser_id_user_id(self,end_date_time: datetime.datetime, start_date_time: datetime.datetime) -> MicrosoftGraphNetworkaccessGetDiscoveredApplicationSegmentReportWithStartDateTimeWithEndDateTimeuserIdUserIdRequestBuilder:
        """
        Provides operations to call the getDiscoveredApplicationSegmentReport method.
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: MicrosoftGraphNetworkaccessGetDiscoveredApplicationSegmentReportWithStartDateTimeWithEndDateTimeuserIdUserIdRequestBuilder
        """
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_get_discovered_application_segment_report_with_start_date_time_with_end_date_timeuser_id_user_id.microsoft_graph_networkaccess_get_discovered_application_segment_report_with_start_date_time_with_end_date_timeuser_id_user_id_request_builder import MicrosoftGraphNetworkaccessGetDiscoveredApplicationSegmentReportWithStartDateTimeWithEndDateTimeuserIdUserIdRequestBuilder

        return MicrosoftGraphNetworkaccessGetDiscoveredApplicationSegmentReportWithStartDateTimeWithEndDateTimeuserIdUserIdRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_transaction_summaries_with_start_date_time_with_end_date_time(self,end_date_time: datetime.datetime, start_date_time: datetime.datetime) -> MicrosoftGraphNetworkaccessTransactionSummariesWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the transactionSummaries method.
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: MicrosoftGraphNetworkaccessTransactionSummariesWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_transaction_summaries_with_start_date_time_with_end_date_time.microsoft_graph_networkaccess_transaction_summaries_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphNetworkaccessTransactionSummariesWithStartDateTimeWithEndDateTimeRequestBuilder

        return MicrosoftGraphNetworkaccessTransactionSummariesWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_usage_profiling_with_start_date_time_with_end_date_time_with_aggregated_bydiscovered_application_segment_id_discovered_application_segment_id(self,aggregated_by: str, end_date_time: datetime.datetime, start_date_time: datetime.datetime) -> MicrosoftGraphNetworkaccessUsageProfilingWithStartDateTimeWithEndDateTimeWithAggregatedBydiscoveredApplicationSegmentIdDiscoveredApplicationSegmentIdRequestBuilder:
        """
        Provides operations to call the usageProfiling method.
        param aggregated_by: Usage: aggregatedBy='{aggregatedBy}'
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: MicrosoftGraphNetworkaccessUsageProfilingWithStartDateTimeWithEndDateTimeWithAggregatedBydiscoveredApplicationSegmentIdDiscoveredApplicationSegmentIdRequestBuilder
        """
        if aggregated_by is None:
            raise TypeError("aggregated_by cannot be null.")
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_usage_profiling_with_start_date_time_with_end_date_time_with_aggregated_bydiscovered_application_segment_id_discovered_application_segment_id.microsoft_graph_networkaccess_usage_profiling_with_start_date_time_with_end_date_time_with_aggregated_bydiscovered_application_segment_id_discovered_application_segment_id_request_builder import MicrosoftGraphNetworkaccessUsageProfilingWithStartDateTimeWithEndDateTimeWithAggregatedBydiscoveredApplicationSegmentIdDiscoveredApplicationSegmentIdRequestBuilder

        return MicrosoftGraphNetworkaccessUsageProfilingWithStartDateTimeWithEndDateTimeWithAggregatedBydiscoveredApplicationSegmentIdDiscoveredApplicationSegmentIdRequestBuilder(self.request_adapter, self.path_parameters, aggregated_by, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_user_report_with_start_date_time_with_end_date_timediscovered_application_segment_id_discovered_application_segment_id(self,end_date_time: datetime.datetime, start_date_time: datetime.datetime) -> MicrosoftGraphNetworkaccessUserReportWithStartDateTimeWithEndDateTimediscoveredApplicationSegmentIdDiscoveredApplicationSegmentIdRequestBuilder:
        """
        Provides operations to call the userReport method.
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: MicrosoftGraphNetworkaccessUserReportWithStartDateTimeWithEndDateTimediscoveredApplicationSegmentIdDiscoveredApplicationSegmentIdRequestBuilder
        """
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_user_report_with_start_date_time_with_end_date_timediscovered_application_segment_id_discovered_application_segment_id.microsoft_graph_networkaccess_user_report_with_start_date_time_with_end_date_timediscovered_application_segment_id_discovered_application_segment_id_request_builder import MicrosoftGraphNetworkaccessUserReportWithStartDateTimeWithEndDateTimediscoveredApplicationSegmentIdDiscoveredApplicationSegmentIdRequestBuilder

        return MicrosoftGraphNetworkaccessUserReportWithStartDateTimeWithEndDateTimediscoveredApplicationSegmentIdDiscoveredApplicationSegmentIdRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_web_category_report_with_start_date_time_with_end_date_time(self,end_date_time: datetime.datetime, start_date_time: datetime.datetime) -> MicrosoftGraphNetworkaccessWebCategoryReportWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the webCategoryReport method.
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: MicrosoftGraphNetworkaccessWebCategoryReportWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_web_category_report_with_start_date_time_with_end_date_time.microsoft_graph_networkaccess_web_category_report_with_start_date_time_with_end_date_time_request_builder import MicrosoftGraphNetworkaccessWebCategoryReportWithStartDateTimeWithEndDateTimeRequestBuilder

        return MicrosoftGraphNetworkaccessWebCategoryReportWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time)
    
    async def patch(self,body: Reports, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Reports]:
        """
        Update the navigation property reports in networkAccess
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Reports]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.networkaccess.reports import Reports

        return await self.request_adapter.send_async(request_info, Reports, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property reports for networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ReportsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Represents the status of the Global Secure Access services for the tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Reports, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property reports in networkAccess
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ReportsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ReportsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ReportsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ReportsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Represents the status of the Global Secure Access services for the tenant.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class ReportsRequestBuilderGetRequestConfiguration(RequestConfiguration[ReportsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ReportsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

