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
    from ......models.microsoft_tunnel_server import MicrosoftTunnelServer
    from ......models.o_data_errors.o_data_error import ODataError
    from .create_server_log_collection_request.create_server_log_collection_request_request_builder import CreateServerLogCollectionRequestRequestBuilder
    from .generate_server_log_collection_request.generate_server_log_collection_request_request_builder import GenerateServerLogCollectionRequestRequestBuilder
    from .get_health_metrics.get_health_metrics_request_builder import GetHealthMetricsRequestBuilder
    from .get_health_metric_time_series.get_health_metric_time_series_request_builder import GetHealthMetricTimeSeriesRequestBuilder

class MicrosoftTunnelServerItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the microsoftTunnelServers property of the microsoft.graph.microsoftTunnelSite entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new MicrosoftTunnelServerItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/microsoftTunnelSites/{microsoftTunnelSite%2Did}/microsoftTunnelServers/{microsoftTunnelServer%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[MicrosoftTunnelServerItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property microsoftTunnelServers for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[MicrosoftTunnelServerItemRequestBuilderGetRequestConfiguration] = None) -> Optional[MicrosoftTunnelServer]:
        """
        A list of MicrosoftTunnelServers that are registered to this MicrosoftTunnelSite
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MicrosoftTunnelServer]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.microsoft_tunnel_server import MicrosoftTunnelServer

        return await self.request_adapter.send_async(request_info, MicrosoftTunnelServer, error_mapping)
    
    async def patch(self,body: Optional[MicrosoftTunnelServer] = None, request_configuration: Optional[MicrosoftTunnelServerItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[MicrosoftTunnelServer]:
        """
        Update the navigation property microsoftTunnelServers in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MicrosoftTunnelServer]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.microsoft_tunnel_server import MicrosoftTunnelServer

        return await self.request_adapter.send_async(request_info, MicrosoftTunnelServer, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[MicrosoftTunnelServerItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property microsoftTunnelServers for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[MicrosoftTunnelServerItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A list of MicrosoftTunnelServers that are registered to this MicrosoftTunnelSite
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[MicrosoftTunnelServer] = None, request_configuration: Optional[MicrosoftTunnelServerItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property microsoftTunnelServers in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> MicrosoftTunnelServerItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MicrosoftTunnelServerItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return MicrosoftTunnelServerItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def create_server_log_collection_request(self) -> CreateServerLogCollectionRequestRequestBuilder:
        """
        Provides operations to call the createServerLogCollectionRequest method.
        """
        from .create_server_log_collection_request.create_server_log_collection_request_request_builder import CreateServerLogCollectionRequestRequestBuilder

        return CreateServerLogCollectionRequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def generate_server_log_collection_request(self) -> GenerateServerLogCollectionRequestRequestBuilder:
        """
        Provides operations to call the generateServerLogCollectionRequest method.
        """
        from .generate_server_log_collection_request.generate_server_log_collection_request_request_builder import GenerateServerLogCollectionRequestRequestBuilder

        return GenerateServerLogCollectionRequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_health_metric_time_series(self) -> GetHealthMetricTimeSeriesRequestBuilder:
        """
        Provides operations to call the getHealthMetricTimeSeries method.
        """
        from .get_health_metric_time_series.get_health_metric_time_series_request_builder import GetHealthMetricTimeSeriesRequestBuilder

        return GetHealthMetricTimeSeriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_health_metrics(self) -> GetHealthMetricsRequestBuilder:
        """
        Provides operations to call the getHealthMetrics method.
        """
        from .get_health_metrics.get_health_metrics_request_builder import GetHealthMetricsRequestBuilder

        return GetHealthMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class MicrosoftTunnelServerItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class MicrosoftTunnelServerItemRequestBuilderGetQueryParameters():
        """
        A list of MicrosoftTunnelServers that are registered to this MicrosoftTunnelSite
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
    class MicrosoftTunnelServerItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[MicrosoftTunnelServerItemRequestBuilder.MicrosoftTunnelServerItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class MicrosoftTunnelServerItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

