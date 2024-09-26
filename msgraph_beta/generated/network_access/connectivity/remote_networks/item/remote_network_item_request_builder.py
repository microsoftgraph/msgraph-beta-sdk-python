from __future__ import annotations
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
    from .....models.networkaccess.remote_network import RemoteNetwork
    from .....models.o_data_errors.o_data_error import ODataError
    from .connectivity_configuration.connectivity_configuration_request_builder import ConnectivityConfigurationRequestBuilder
    from .device_links.device_links_request_builder import DeviceLinksRequestBuilder
    from .forwarding_profiles.forwarding_profiles_request_builder import ForwardingProfilesRequestBuilder

class RemoteNetworkItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the remoteNetworks property of the microsoft.graph.networkaccess.connectivity entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new RemoteNetworkItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/networkAccess/connectivity/remoteNetworks/{remoteNetwork%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property remoteNetworks for networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[RemoteNetworkItemRequestBuilderGetQueryParameters]] = None) -> Optional[RemoteNetwork]:
        """
        Represent locations, such as branches, that are connected to Global Secure Access services through an IPsec tunnel.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RemoteNetwork]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.networkaccess.remote_network import RemoteNetwork

        return await self.request_adapter.send_async(request_info, RemoteNetwork, error_mapping)
    
    async def patch(self,body: RemoteNetwork, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[RemoteNetwork]:
        """
        Update the navigation property remoteNetworks in networkAccess
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RemoteNetwork]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.networkaccess.remote_network import RemoteNetwork

        return await self.request_adapter.send_async(request_info, RemoteNetwork, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property remoteNetworks for networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[RemoteNetworkItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Represent locations, such as branches, that are connected to Global Secure Access services through an IPsec tunnel.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: RemoteNetwork, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property remoteNetworks in networkAccess
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
    
    def with_url(self,raw_url: str) -> RemoteNetworkItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RemoteNetworkItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RemoteNetworkItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def connectivity_configuration(self) -> ConnectivityConfigurationRequestBuilder:
        """
        Provides operations to manage the connectivityConfiguration property of the microsoft.graph.networkaccess.remoteNetwork entity.
        """
        from .connectivity_configuration.connectivity_configuration_request_builder import ConnectivityConfigurationRequestBuilder

        return ConnectivityConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_links(self) -> DeviceLinksRequestBuilder:
        """
        Provides operations to manage the deviceLinks property of the microsoft.graph.networkaccess.remoteNetwork entity.
        """
        from .device_links.device_links_request_builder import DeviceLinksRequestBuilder

        return DeviceLinksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forwarding_profiles(self) -> ForwardingProfilesRequestBuilder:
        """
        Provides operations to manage the forwardingProfiles property of the microsoft.graph.networkaccess.remoteNetwork entity.
        """
        from .forwarding_profiles.forwarding_profiles_request_builder import ForwardingProfilesRequestBuilder

        return ForwardingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RemoteNetworkItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class RemoteNetworkItemRequestBuilderGetQueryParameters():
        """
        Represent locations, such as branches, that are connected to Global Secure Access services through an IPsec tunnel.
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
    class RemoteNetworkItemRequestBuilderGetRequestConfiguration(RequestConfiguration[RemoteNetworkItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class RemoteNetworkItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

