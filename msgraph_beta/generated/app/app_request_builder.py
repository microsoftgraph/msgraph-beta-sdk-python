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
    from ..models.comms_application import CommsApplication
    from ..models.o_data_errors.o_data_error import ODataError
    from .calls.calls_request_builder import CallsRequestBuilder
    from .online_meetings.online_meetings_request_builder import OnlineMeetingsRequestBuilder
    from .online_meetings_with_join_web_url.online_meetings_with_join_web_url_request_builder import OnlineMeetingsWithJoinWebUrlRequestBuilder

class AppRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the commsApplication singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AppRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/app{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AppRequestBuilderGetQueryParameters]] = None) -> Optional[CommsApplication]:
        """
        Get app
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CommsApplication]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.comms_application import CommsApplication

        return await self.request_adapter.send_async(request_info, CommsApplication, error_mapping)
    
    def online_meetings_with_join_web_url(self,join_web_url: str) -> OnlineMeetingsWithJoinWebUrlRequestBuilder:
        """
        Provides operations to manage the onlineMeetings property of the microsoft.graph.commsApplication entity.
        param join_web_url: Alternate key of onlineMeeting
        Returns: OnlineMeetingsWithJoinWebUrlRequestBuilder
        """
        if join_web_url is None:
            raise TypeError("join_web_url cannot be null.")
        from .online_meetings_with_join_web_url.online_meetings_with_join_web_url_request_builder import OnlineMeetingsWithJoinWebUrlRequestBuilder

        return OnlineMeetingsWithJoinWebUrlRequestBuilder(self.request_adapter, self.path_parameters, join_web_url)
    
    async def patch(self,body: CommsApplication, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CommsApplication]:
        """
        Update app
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CommsApplication]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.comms_application import CommsApplication

        return await self.request_adapter.send_async(request_info, CommsApplication, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AppRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get app
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: CommsApplication, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update app
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
    
    def with_url(self,raw_url: str) -> AppRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AppRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AppRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def calls(self) -> CallsRequestBuilder:
        """
        Provides operations to manage the calls property of the microsoft.graph.commsApplication entity.
        """
        from .calls.calls_request_builder import CallsRequestBuilder

        return CallsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def online_meetings(self) -> OnlineMeetingsRequestBuilder:
        """
        Provides operations to manage the onlineMeetings property of the microsoft.graph.commsApplication entity.
        """
        from .online_meetings.online_meetings_request_builder import OnlineMeetingsRequestBuilder

        return OnlineMeetingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AppRequestBuilderGetQueryParameters():
        """
        Get app
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
    class AppRequestBuilderGetRequestConfiguration(RequestConfiguration[AppRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AppRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

