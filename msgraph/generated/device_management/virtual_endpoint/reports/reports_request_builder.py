from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import cloud_pc_reports
    from ....models.o_data_errors import o_data_error
    from .export_jobs import export_jobs_request_builder
    from .get_daily_aggregated_remote_connection_reports import get_daily_aggregated_remote_connection_reports_request_builder
    from .get_real_time_remote_connection_latency_with_cloud_pc_id import get_real_time_remote_connection_latency_with_cloud_pc_id_request_builder
    from .get_real_time_remote_connection_status_with_cloud_pc_id import get_real_time_remote_connection_status_with_cloud_pc_id_request_builder
    from .get_remote_connection_historical_reports import get_remote_connection_historical_reports_request_builder
    from .get_shared_use_license_usage_report import get_shared_use_license_usage_report_request_builder
    from .get_total_aggregated_remote_connection_reports import get_total_aggregated_remote_connection_reports_request_builder

class ReportsRequestBuilder():
    """
    Provides operations to manage the reports property of the microsoft.graph.virtualEndpoint entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ReportsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/virtualEndpoint/reports{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property reports for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> Optional[cloud_pc_reports.CloudPcReports]:
        """
        Cloud PC related reports.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[cloud_pc_reports.CloudPcReports]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import cloud_pc_reports

        return await self.request_adapter.send_async(request_info, cloud_pc_reports.CloudPcReports, error_mapping)
    
    def get_real_time_remote_connection_latency_with_cloud_pc_id(self,cloud_pc_id: Optional[str] = None) -> get_real_time_remote_connection_latency_with_cloud_pc_id_request_builder.GetRealTimeRemoteConnectionLatencyWithCloudPcIdRequestBuilder:
        """
        Provides operations to call the getRealTimeRemoteConnectionLatency method.
        Args:
            cloudPcId: Usage: cloudPcId='{cloudPcId}'
        Returns: get_real_time_remote_connection_latency_with_cloud_pc_id_request_builder.GetRealTimeRemoteConnectionLatencyWithCloudPcIdRequestBuilder
        """
        if cloud_pc_id is None:
            raise Exception("cloud_pc_id cannot be undefined")
        from .get_real_time_remote_connection_latency_with_cloud_pc_id import get_real_time_remote_connection_latency_with_cloud_pc_id_request_builder

        return get_real_time_remote_connection_latency_with_cloud_pc_id_request_builder.GetRealTimeRemoteConnectionLatencyWithCloudPcIdRequestBuilder(self.request_adapter, self.path_parameters, cloud_pc_id)
    
    def get_real_time_remote_connection_status_with_cloud_pc_id(self,cloud_pc_id: Optional[str] = None) -> get_real_time_remote_connection_status_with_cloud_pc_id_request_builder.GetRealTimeRemoteConnectionStatusWithCloudPcIdRequestBuilder:
        """
        Provides operations to call the getRealTimeRemoteConnectionStatus method.
        Args:
            cloudPcId: Usage: cloudPcId='{cloudPcId}'
        Returns: get_real_time_remote_connection_status_with_cloud_pc_id_request_builder.GetRealTimeRemoteConnectionStatusWithCloudPcIdRequestBuilder
        """
        if cloud_pc_id is None:
            raise Exception("cloud_pc_id cannot be undefined")
        from .get_real_time_remote_connection_status_with_cloud_pc_id import get_real_time_remote_connection_status_with_cloud_pc_id_request_builder

        return get_real_time_remote_connection_status_with_cloud_pc_id_request_builder.GetRealTimeRemoteConnectionStatusWithCloudPcIdRequestBuilder(self.request_adapter, self.path_parameters, cloud_pc_id)
    
    async def patch(self,body: Optional[cloud_pc_reports.CloudPcReports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> Optional[cloud_pc_reports.CloudPcReports]:
        """
        Update the navigation property reports in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[cloud_pc_reports.CloudPcReports]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import cloud_pc_reports

        return await self.request_adapter.send_async(request_info, cloud_pc_reports.CloudPcReports, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property reports for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Cloud PC related reports.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[cloud_pc_reports.CloudPcReports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property reports in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def export_jobs(self) -> export_jobs_request_builder.ExportJobsRequestBuilder:
        """
        Provides operations to manage the exportJobs property of the microsoft.graph.cloudPcReports entity.
        """
        from .export_jobs import export_jobs_request_builder

        return export_jobs_request_builder.ExportJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_daily_aggregated_remote_connection_reports(self) -> get_daily_aggregated_remote_connection_reports_request_builder.GetDailyAggregatedRemoteConnectionReportsRequestBuilder:
        """
        Provides operations to call the getDailyAggregatedRemoteConnectionReports method.
        """
        from .get_daily_aggregated_remote_connection_reports import get_daily_aggregated_remote_connection_reports_request_builder

        return get_daily_aggregated_remote_connection_reports_request_builder.GetDailyAggregatedRemoteConnectionReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_remote_connection_historical_reports(self) -> get_remote_connection_historical_reports_request_builder.GetRemoteConnectionHistoricalReportsRequestBuilder:
        """
        Provides operations to call the getRemoteConnectionHistoricalReports method.
        """
        from .get_remote_connection_historical_reports import get_remote_connection_historical_reports_request_builder

        return get_remote_connection_historical_reports_request_builder.GetRemoteConnectionHistoricalReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_shared_use_license_usage_report(self) -> get_shared_use_license_usage_report_request_builder.GetSharedUseLicenseUsageReportRequestBuilder:
        """
        Provides operations to call the getSharedUseLicenseUsageReport method.
        """
        from .get_shared_use_license_usage_report import get_shared_use_license_usage_report_request_builder

        return get_shared_use_license_usage_report_request_builder.GetSharedUseLicenseUsageReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_total_aggregated_remote_connection_reports(self) -> get_total_aggregated_remote_connection_reports_request_builder.GetTotalAggregatedRemoteConnectionReportsRequestBuilder:
        """
        Provides operations to call the getTotalAggregatedRemoteConnectionReports method.
        """
        from .get_total_aggregated_remote_connection_reports import get_total_aggregated_remote_connection_reports_request_builder

        return get_total_aggregated_remote_connection_reports_request_builder.GetTotalAggregatedRemoteConnectionReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ReportsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Cloud PC related reports.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
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
    class ReportsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ReportsRequestBuilder.ReportsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ReportsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

