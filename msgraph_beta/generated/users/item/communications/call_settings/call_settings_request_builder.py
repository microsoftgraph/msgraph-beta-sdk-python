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
    from .....models.call_settings import CallSettings
    from .....models.o_data_errors.o_data_error import ODataError
    from .delegates.delegates_request_builder import DelegatesRequestBuilder
    from .delegators.delegators_request_builder import DelegatorsRequestBuilder

class CallSettingsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the callSettings property of the microsoft.graph.userCloudCommunication entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CallSettingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/communications/callSettings{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property callSettings for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CallSettingsRequestBuilderGetQueryParameters]] = None) -> Optional[CallSettings]:
        """
        The call settings assigned to the user.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CallSettings]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.call_settings import CallSettings

        return await self.request_adapter.send_async(request_info, CallSettings, error_mapping)
    
    async def patch(self,body: CallSettings, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CallSettings]:
        """
        Update the navigation property callSettings in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CallSettings]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.call_settings import CallSettings

        return await self.request_adapter.send_async(request_info, CallSettings, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property callSettings for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CallSettingsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The call settings assigned to the user.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: CallSettings, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property callSettings in users
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
    
    def with_url(self,raw_url: str) -> CallSettingsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CallSettingsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CallSettingsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def delegates(self) -> DelegatesRequestBuilder:
        """
        Provides operations to manage the delegates property of the microsoft.graph.callSettings entity.
        """
        from .delegates.delegates_request_builder import DelegatesRequestBuilder

        return DelegatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delegators(self) -> DelegatorsRequestBuilder:
        """
        Provides operations to manage the delegators property of the microsoft.graph.callSettings entity.
        """
        from .delegators.delegators_request_builder import DelegatorsRequestBuilder

        return DelegatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CallSettingsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CallSettingsRequestBuilderGetQueryParameters():
        """
        The call settings assigned to the user.
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
    class CallSettingsRequestBuilderGetRequestConfiguration(RequestConfiguration[CallSettingsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CallSettingsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

