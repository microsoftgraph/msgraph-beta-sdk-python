from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.cloud_pc_reports import CloudPcReports
    from ....models.o_data_errors.o_data_error import ODataError
    from .export_jobs.export_jobs_request_builder import ExportJobsRequestBuilder
    from .get_connection_quality_reports.get_connection_quality_reports_request_builder import GetConnectionQualityReportsRequestBuilder
    from .get_daily_aggregated_remote_connection_reports.get_daily_aggregated_remote_connection_reports_request_builder import GetDailyAggregatedRemoteConnectionReportsRequestBuilder
    from .get_frontline_report.get_frontline_report_request_builder import GetFrontlineReportRequestBuilder
    from .get_inaccessible_cloud_pc_reports.get_inaccessible_cloud_pc_reports_request_builder import GetInaccessibleCloudPcReportsRequestBuilder
    from .get_raw_remote_connection_reports.get_raw_remote_connection_reports_request_builder import GetRawRemoteConnectionReportsRequestBuilder
    from .get_real_time_remote_connection_latency_with_cloud_pc_id.get_real_time_remote_connection_latency_with_cloud_pc_id_request_builder import GetRealTimeRemoteConnectionLatencyWithCloudPcIdRequestBuilder
    from .get_real_time_remote_connection_status_with_cloud_pc_id.get_real_time_remote_connection_status_with_cloud_pc_id_request_builder import GetRealTimeRemoteConnectionStatusWithCloudPcIdRequestBuilder
    from .get_remote_connection_historical_reports.get_remote_connection_historical_reports_request_builder import GetRemoteConnectionHistoricalReportsRequestBuilder
    from .get_shared_use_license_usage_report.get_shared_use_license_usage_report_request_builder import GetSharedUseLicenseUsageReportRequestBuilder
    from .get_total_aggregated_remote_connection_reports.get_total_aggregated_remote_connection_reports_request_builder import GetTotalAggregatedRemoteConnectionReportsRequestBuilder

class ReportsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the reports property of the microsoft.graph.virtualEndpoint entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ReportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/reports{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property reports for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> Optional[CloudPcReports]:
        """
        Cloud PC related reports.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPcReports]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.cloud_pc_reports import CloudPcReports

        return await self.request_adapter.send_async(request_info, CloudPcReports, error_mapping)
    
    def get_real_time_remote_connection_latency_with_cloud_pc_id(self,cloud_pc_id: Optional[str] = None) -> GetRealTimeRemoteConnectionLatencyWithCloudPcIdRequestBuilder:
        """
        Provides operations to call the getRealTimeRemoteConnectionLatency method.
        param cloud_pc_id: Usage: cloudPcId='{cloudPcId}'
        Returns: GetRealTimeRemoteConnectionLatencyWithCloudPcIdRequestBuilder
        """
        if not cloud_pc_id:
            raise TypeError("cloud_pc_id cannot be null.")
        from .get_real_time_remote_connection_latency_with_cloud_pc_id.get_real_time_remote_connection_latency_with_cloud_pc_id_request_builder import GetRealTimeRemoteConnectionLatencyWithCloudPcIdRequestBuilder

        return GetRealTimeRemoteConnectionLatencyWithCloudPcIdRequestBuilder(self.request_adapter, self.path_parameters, cloud_pc_id)
    
    def get_real_time_remote_connection_status_with_cloud_pc_id(self,cloud_pc_id: Optional[str] = None) -> GetRealTimeRemoteConnectionStatusWithCloudPcIdRequestBuilder:
        """
        Provides operations to call the getRealTimeRemoteConnectionStatus method.
        param cloud_pc_id: Usage: cloudPcId='{cloudPcId}'
        Returns: GetRealTimeRemoteConnectionStatusWithCloudPcIdRequestBuilder
        """
        if not cloud_pc_id:
            raise TypeError("cloud_pc_id cannot be null.")
        from .get_real_time_remote_connection_status_with_cloud_pc_id.get_real_time_remote_connection_status_with_cloud_pc_id_request_builder import GetRealTimeRemoteConnectionStatusWithCloudPcIdRequestBuilder

        return GetRealTimeRemoteConnectionStatusWithCloudPcIdRequestBuilder(self.request_adapter, self.path_parameters, cloud_pc_id)
    
    async def patch(self,body: Optional[CloudPcReports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> Optional[CloudPcReports]:
        """
        Update the navigation property reports in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPcReports]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.cloud_pc_reports import CloudPcReports

        return await self.request_adapter.send_async(request_info, CloudPcReports, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property reports for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json, application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Cloud PC related reports.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def to_patch_request_information(self,body: Optional[CloudPcReports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property reports in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ReportsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ReportsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ReportsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def export_jobs(self) -> ExportJobsRequestBuilder:
        """
        Provides operations to manage the exportJobs property of the microsoft.graph.cloudPcReports entity.
        """
        from .export_jobs.export_jobs_request_builder import ExportJobsRequestBuilder

        return ExportJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_connection_quality_reports(self) -> GetConnectionQualityReportsRequestBuilder:
        """
        Provides operations to call the getConnectionQualityReports method.
        """
        from .get_connection_quality_reports.get_connection_quality_reports_request_builder import GetConnectionQualityReportsRequestBuilder

        return GetConnectionQualityReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_daily_aggregated_remote_connection_reports(self) -> GetDailyAggregatedRemoteConnectionReportsRequestBuilder:
        """
        Provides operations to call the getDailyAggregatedRemoteConnectionReports method.
        """
        from .get_daily_aggregated_remote_connection_reports.get_daily_aggregated_remote_connection_reports_request_builder import GetDailyAggregatedRemoteConnectionReportsRequestBuilder

        return GetDailyAggregatedRemoteConnectionReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_frontline_report(self) -> GetFrontlineReportRequestBuilder:
        """
        Provides operations to call the getFrontlineReport method.
        """
        from .get_frontline_report.get_frontline_report_request_builder import GetFrontlineReportRequestBuilder

        return GetFrontlineReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_inaccessible_cloud_pc_reports(self) -> GetInaccessibleCloudPcReportsRequestBuilder:
        """
        Provides operations to call the getInaccessibleCloudPcReports method.
        """
        from .get_inaccessible_cloud_pc_reports.get_inaccessible_cloud_pc_reports_request_builder import GetInaccessibleCloudPcReportsRequestBuilder

        return GetInaccessibleCloudPcReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_raw_remote_connection_reports(self) -> GetRawRemoteConnectionReportsRequestBuilder:
        """
        Provides operations to call the getRawRemoteConnectionReports method.
        """
        from .get_raw_remote_connection_reports.get_raw_remote_connection_reports_request_builder import GetRawRemoteConnectionReportsRequestBuilder

        return GetRawRemoteConnectionReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_remote_connection_historical_reports(self) -> GetRemoteConnectionHistoricalReportsRequestBuilder:
        """
        Provides operations to call the getRemoteConnectionHistoricalReports method.
        """
        from .get_remote_connection_historical_reports.get_remote_connection_historical_reports_request_builder import GetRemoteConnectionHistoricalReportsRequestBuilder

        return GetRemoteConnectionHistoricalReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_shared_use_license_usage_report(self) -> GetSharedUseLicenseUsageReportRequestBuilder:
        """
        Provides operations to call the getSharedUseLicenseUsageReport method.
        """
        from .get_shared_use_license_usage_report.get_shared_use_license_usage_report_request_builder import GetSharedUseLicenseUsageReportRequestBuilder

        return GetSharedUseLicenseUsageReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_total_aggregated_remote_connection_reports(self) -> GetTotalAggregatedRemoteConnectionReportsRequestBuilder:
        """
        Provides operations to call the getTotalAggregatedRemoteConnectionReports method.
        """
        from .get_total_aggregated_remote_connection_reports.get_total_aggregated_remote_connection_reports_request_builder import GetTotalAggregatedRemoteConnectionReportsRequestBuilder

        return GetTotalAggregatedRemoteConnectionReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ReportsRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Cloud PC related reports.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ReportsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ReportsRequestBuilder.ReportsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ReportsRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

