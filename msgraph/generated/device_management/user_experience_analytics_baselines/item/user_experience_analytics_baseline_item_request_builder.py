from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_health_metrics_request_builder = lazy_import('msgraph.generated.device_management.user_experience_analytics_baselines.item.app_health_metrics.app_health_metrics_request_builder')
battery_health_metrics_request_builder = lazy_import('msgraph.generated.device_management.user_experience_analytics_baselines.item.battery_health_metrics.battery_health_metrics_request_builder')
best_practices_metrics_request_builder = lazy_import('msgraph.generated.device_management.user_experience_analytics_baselines.item.best_practices_metrics.best_practices_metrics_request_builder')
device_boot_performance_metrics_request_builder = lazy_import('msgraph.generated.device_management.user_experience_analytics_baselines.item.device_boot_performance_metrics.device_boot_performance_metrics_request_builder')
reboot_analytics_metrics_request_builder = lazy_import('msgraph.generated.device_management.user_experience_analytics_baselines.item.reboot_analytics_metrics.reboot_analytics_metrics_request_builder')
resource_performance_metrics_request_builder = lazy_import('msgraph.generated.device_management.user_experience_analytics_baselines.item.resource_performance_metrics.resource_performance_metrics_request_builder')
work_from_anywhere_metrics_request_builder = lazy_import('msgraph.generated.device_management.user_experience_analytics_baselines.item.work_from_anywhere_metrics.work_from_anywhere_metrics_request_builder')
user_experience_analytics_baseline = lazy_import('msgraph.generated.models.user_experience_analytics_baseline')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class UserExperienceAnalyticsBaselineItemRequestBuilder():
    """
    Provides operations to manage the userExperienceAnalyticsBaselines property of the microsoft.graph.deviceManagement entity.
    """
    @property
    def app_health_metrics(self) -> app_health_metrics_request_builder.AppHealthMetricsRequestBuilder:
        """
        Provides operations to manage the appHealthMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        return app_health_metrics_request_builder.AppHealthMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def battery_health_metrics(self) -> battery_health_metrics_request_builder.BatteryHealthMetricsRequestBuilder:
        """
        Provides operations to manage the batteryHealthMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        return battery_health_metrics_request_builder.BatteryHealthMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def best_practices_metrics(self) -> best_practices_metrics_request_builder.BestPracticesMetricsRequestBuilder:
        """
        Provides operations to manage the bestPracticesMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        return best_practices_metrics_request_builder.BestPracticesMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_boot_performance_metrics(self) -> device_boot_performance_metrics_request_builder.DeviceBootPerformanceMetricsRequestBuilder:
        """
        Provides operations to manage the deviceBootPerformanceMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        return device_boot_performance_metrics_request_builder.DeviceBootPerformanceMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reboot_analytics_metrics(self) -> reboot_analytics_metrics_request_builder.RebootAnalyticsMetricsRequestBuilder:
        """
        Provides operations to manage the rebootAnalyticsMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        return reboot_analytics_metrics_request_builder.RebootAnalyticsMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_performance_metrics(self) -> resource_performance_metrics_request_builder.ResourcePerformanceMetricsRequestBuilder:
        """
        Provides operations to manage the resourcePerformanceMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        return resource_performance_metrics_request_builder.ResourcePerformanceMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def work_from_anywhere_metrics(self) -> work_from_anywhere_metrics_request_builder.WorkFromAnywhereMetricsRequestBuilder:
        """
        Provides operations to manage the workFromAnywhereMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        return work_from_anywhere_metrics_request_builder.WorkFromAnywhereMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UserExperienceAnalyticsBaselineItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/userExperienceAnalyticsBaselines/{userExperienceAnalyticsBaseline%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[UserExperienceAnalyticsBaselineItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property userExperienceAnalyticsBaselines for deviceManagement
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
    
    def create_get_request_information(self,request_configuration: Optional[UserExperienceAnalyticsBaselineItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        User experience analytics baselines
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[user_experience_analytics_baseline.UserExperienceAnalyticsBaseline] = None, request_configuration: Optional[UserExperienceAnalyticsBaselineItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property userExperienceAnalyticsBaselines in deviceManagement
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[UserExperienceAnalyticsBaselineItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property userExperienceAnalyticsBaselines for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[UserExperienceAnalyticsBaselineItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[user_experience_analytics_baseline.UserExperienceAnalyticsBaseline]:
        """
        User experience analytics baselines
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[user_experience_analytics_baseline.UserExperienceAnalyticsBaseline]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, user_experience_analytics_baseline.UserExperienceAnalyticsBaseline, response_handler, error_mapping)
    
    async def patch(self,body: Optional[user_experience_analytics_baseline.UserExperienceAnalyticsBaseline] = None, request_configuration: Optional[UserExperienceAnalyticsBaselineItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[user_experience_analytics_baseline.UserExperienceAnalyticsBaseline]:
        """
        Update the navigation property userExperienceAnalyticsBaselines in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[user_experience_analytics_baseline.UserExperienceAnalyticsBaseline]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, user_experience_analytics_baseline.UserExperienceAnalyticsBaseline, response_handler, error_mapping)
    
    @dataclass
    class UserExperienceAnalyticsBaselineItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UserExperienceAnalyticsBaselineItemRequestBuilderGetQueryParameters():
        """
        User experience analytics baselines
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class UserExperienceAnalyticsBaselineItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UserExperienceAnalyticsBaselineItemRequestBuilder.UserExperienceAnalyticsBaselineItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UserExperienceAnalyticsBaselineItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

