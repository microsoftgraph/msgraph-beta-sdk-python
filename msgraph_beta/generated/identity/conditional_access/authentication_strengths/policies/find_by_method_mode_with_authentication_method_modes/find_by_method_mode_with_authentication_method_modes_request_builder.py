from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
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
    from .find_by_method_mode_with_authentication_method_modes_get_response import FindByMethodModeWithAuthenticationMethodModesGetResponse

class FindByMethodModeWithAuthenticationMethodModesRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the findByMethodMode method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]], authentication_method_modes: Optional[str] = None) -> None:
        """
        Instantiates a new FindByMethodModeWithAuthenticationMethodModesRequestBuilder and sets the default values.
        param authentication_method_modes: Usage: authenticationMethodModes={authenticationMethodModes}
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['authenticationMethodModes'] = str(authentication_method_modes)
        super().__init__(request_adapter, "{+baseurl}/identity/conditionalAccess/authenticationStrengths/policies/findByMethodMode(authenticationMethodModes={authenticationMethodModes}){?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[FindByMethodModeWithAuthenticationMethodModesGetResponse]:
        """
        Invoke function findByMethodMode
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FindByMethodModeWithAuthenticationMethodModesGetResponse]
        """
        warn("The &apos;authenticationStrengths&apos; segment is deprecated. Please use &apos;authenticationStrength&apos; instead. as of 2023-02/AuthenticationStrengthsRemove", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .find_by_method_mode_with_authentication_method_modes_get_response import FindByMethodModeWithAuthenticationMethodModesGetResponse

        return await self.request_adapter.send_async(request_info, FindByMethodModeWithAuthenticationMethodModesGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Invoke function findByMethodMode
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The &apos;authenticationStrengths&apos; segment is deprecated. Please use &apos;authenticationStrength&apos; instead. as of 2023-02/AuthenticationStrengthsRemove", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> FindByMethodModeWithAuthenticationMethodModesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FindByMethodModeWithAuthenticationMethodModesRequestBuilder
        """
        warn("The &apos;authenticationStrengths&apos; segment is deprecated. Please use &apos;authenticationStrength&apos; instead. as of 2023-02/AuthenticationStrengthsRemove", DeprecationWarning)
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return FindByMethodModeWithAuthenticationMethodModesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class FindByMethodModeWithAuthenticationMethodModesRequestBuilderGetQueryParameters():
        """
        Invoke function findByMethodMode
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    

