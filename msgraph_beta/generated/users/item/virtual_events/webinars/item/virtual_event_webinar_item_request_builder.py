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
    from ......models.o_data_errors.o_data_error import ODataError
    from ......models.virtual_event_webinar import VirtualEventWebinar

class VirtualEventWebinarItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the webinars property of the microsoft.graph.userVirtualEventsRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new VirtualEventWebinarItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/virtualEvents/webinars/{virtualEventWebinar%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[VirtualEventWebinarItemRequestBuilderGetQueryParameters]] = None) -> Optional[VirtualEventWebinar]:
        """
        Get webinars from users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VirtualEventWebinar]
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.virtual_event_webinar import VirtualEventWebinar

        return await self.request_adapter.send_async(request_info, VirtualEventWebinar, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[VirtualEventWebinarItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get webinars from users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> VirtualEventWebinarItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VirtualEventWebinarItemRequestBuilder
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return VirtualEventWebinarItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class VirtualEventWebinarItemRequestBuilderGetQueryParameters():
        """
        Get webinars from users
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
    class VirtualEventWebinarItemRequestBuilderGetRequestConfiguration(RequestConfiguration[VirtualEventWebinarItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

