from __future__ import annotations
from collections.abc import Callable
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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.security.data_discovery_report import DataDiscoveryReport
    from .uploaded_streams.uploaded_streams_request_builder import UploadedStreamsRequestBuilder

class CloudAppDiscoveryRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the cloudAppDiscovery property of the microsoft.graph.security.dataDiscoveryRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CloudAppDiscoveryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/dataDiscovery/cloudAppDiscovery{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property cloudAppDiscovery for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CloudAppDiscoveryRequestBuilderGetQueryParameters]] = None) -> Optional[DataDiscoveryReport]:
        """
        The available entities are IP addresses, devices, and users who access a cloud app.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DataDiscoveryReport]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.security.data_discovery_report import DataDiscoveryReport

        return await self.request_adapter.send_async(request_info, DataDiscoveryReport, error_mapping)
    
    async def patch(self,body: DataDiscoveryReport, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DataDiscoveryReport]:
        """
        Update the navigation property cloudAppDiscovery in security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DataDiscoveryReport]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.security.data_discovery_report import DataDiscoveryReport

        return await self.request_adapter.send_async(request_info, DataDiscoveryReport, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property cloudAppDiscovery for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CloudAppDiscoveryRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The available entities are IP addresses, devices, and users who access a cloud app.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DataDiscoveryReport, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property cloudAppDiscovery in security
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
    
    def with_url(self,raw_url: str) -> CloudAppDiscoveryRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CloudAppDiscoveryRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CloudAppDiscoveryRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def uploaded_streams(self) -> UploadedStreamsRequestBuilder:
        """
        Provides operations to manage the uploadedStreams property of the microsoft.graph.security.dataDiscoveryReport entity.
        """
        from .uploaded_streams.uploaded_streams_request_builder import UploadedStreamsRequestBuilder

        return UploadedStreamsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CloudAppDiscoveryRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CloudAppDiscoveryRequestBuilderGetQueryParameters():
        """
        The available entities are IP addresses, devices, and users who access a cloud app.
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
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class CloudAppDiscoveryRequestBuilderGetRequestConfiguration(RequestConfiguration[CloudAppDiscoveryRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CloudAppDiscoveryRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

