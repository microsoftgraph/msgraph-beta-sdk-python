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
    from ......models.on_authentication_method_load_start_handler import OnAuthenticationMethodLoadStartHandler
    from ......models.o_data_errors.o_data_error import ODataError
    from .graph_on_authentication_method_load_start_external_users_self_service_sign_up.graph_on_authentication_method_load_start_external_users_self_service_sign_up_request_builder import GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilder

class OnAuthenticationMethodLoadStartRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /identity/authenticationEventsFlows/{authenticationEventsFlow-id}/graph.externalUsersSelfServiceSignUpEventsFlow/onAuthenticationMethodLoadStart
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OnAuthenticationMethodLoadStartRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow%2Did}/graph.externalUsersSelfServiceSignUpEventsFlow/onAuthenticationMethodLoadStart{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[OnAuthenticationMethodLoadStartRequestBuilderGetRequestConfiguration] = None) -> Optional[OnAuthenticationMethodLoadStartHandler]:
        """
        Required. The configuration for what to invoke when authentication methods are ready to be presented to the user. Must have at least one identity provider linked.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnAuthenticationMethodLoadStartHandler]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.on_authentication_method_load_start_handler import OnAuthenticationMethodLoadStartHandler

        return await self.request_adapter.send_async(request_info, OnAuthenticationMethodLoadStartHandler, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[OnAuthenticationMethodLoadStartRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Required. The configuration for what to invoke when authentication methods are ready to be presented to the user. Must have at least one identity provider linked.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> OnAuthenticationMethodLoadStartRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OnAuthenticationMethodLoadStartRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return OnAuthenticationMethodLoadStartRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def graph_on_authentication_method_load_start_external_users_self_service_sign_up(self) -> GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilder:
        """
        Casts the previous resource to onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp.
        """
        from .graph_on_authentication_method_load_start_external_users_self_service_sign_up.graph_on_authentication_method_load_start_external_users_self_service_sign_up_request_builder import GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilder

        return GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OnAuthenticationMethodLoadStartRequestBuilderGetQueryParameters():
        """
        Required. The configuration for what to invoke when authentication methods are ready to be presented to the user. Must have at least one identity provider linked.
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
    class OnAuthenticationMethodLoadStartRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[OnAuthenticationMethodLoadStartRequestBuilder.OnAuthenticationMethodLoadStartRequestBuilderGetQueryParameters] = None

    

