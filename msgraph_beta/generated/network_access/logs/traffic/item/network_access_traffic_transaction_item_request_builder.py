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
    from .....models.networkaccess.network_access_traffic import NetworkAccessTraffic
    from .....models.o_data_errors.o_data_error import ODataError

class NetworkAccessTrafficTransactionItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the traffic property of the microsoft.graph.networkaccess.logs entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new NetworkAccessTrafficTransactionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/networkAccess/logs/traffic/{networkAccessTraffic%2DtransactionId}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[NetworkAccessTrafficTransactionItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property traffic for networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[NetworkAccessTrafficTransactionItemRequestBuilderGetRequestConfiguration] = None) -> Optional[NetworkAccessTraffic]:
        """
        A network access traffic log entry that contains comprehensive information about network traffic events.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NetworkAccessTraffic]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.networkaccess.network_access_traffic import NetworkAccessTraffic

        return await self.request_adapter.send_async(request_info, NetworkAccessTraffic, error_mapping)
    
    async def patch(self,body: Optional[NetworkAccessTraffic] = None, request_configuration: Optional[NetworkAccessTrafficTransactionItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[NetworkAccessTraffic]:
        """
        Update the navigation property traffic in networkAccess
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NetworkAccessTraffic]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.networkaccess.network_access_traffic import NetworkAccessTraffic

        return await self.request_adapter.send_async(request_info, NetworkAccessTraffic, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[NetworkAccessTrafficTransactionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property traffic for networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/networkAccess/logs/traffic/{networkAccessTraffic%2DtransactionId}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[NetworkAccessTrafficTransactionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A network access traffic log entry that contains comprehensive information about network traffic events.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[NetworkAccessTraffic] = None, request_configuration: Optional[NetworkAccessTrafficTransactionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property traffic in networkAccess
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/networkAccess/logs/traffic/{networkAccessTraffic%2DtransactionId}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> NetworkAccessTrafficTransactionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NetworkAccessTrafficTransactionItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return NetworkAccessTrafficTransactionItemRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class NetworkAccessTrafficTransactionItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class NetworkAccessTrafficTransactionItemRequestBuilderGetQueryParameters():
        """
        A network access traffic log entry that contains comprehensive information about network traffic events.
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
    class NetworkAccessTrafficTransactionItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[NetworkAccessTrafficTransactionItemRequestBuilder.NetworkAccessTrafficTransactionItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class NetworkAccessTrafficTransactionItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

