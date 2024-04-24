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
    from ....models.b2c_identity_user_flow import B2cIdentityUserFlow
    from ....models.o_data_errors.o_data_error import ODataError
    from .identity_providers.identity_providers_request_builder import IdentityProvidersRequestBuilder
    from .languages.languages_request_builder import LanguagesRequestBuilder
    from .user_attribute_assignments.user_attribute_assignments_request_builder import UserAttributeAssignmentsRequestBuilder
    from .user_flow_identity_providers.user_flow_identity_providers_request_builder import UserFlowIdentityProvidersRequestBuilder

class B2cIdentityUserFlowItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the b2cUserFlows property of the microsoft.graph.identityContainer entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new B2cIdentityUserFlowItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/b2cUserFlows/{b2cIdentityUserFlow%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[B2cIdentityUserFlowItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property b2cUserFlows for identity
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[B2cIdentityUserFlowItemRequestBuilderGetRequestConfiguration] = None) -> Optional[B2cIdentityUserFlow]:
        """
        Represents entry point for B2C identity userflows.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[B2cIdentityUserFlow]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.b2c_identity_user_flow import B2cIdentityUserFlow

        return await self.request_adapter.send_async(request_info, B2cIdentityUserFlow, error_mapping)
    
    async def patch(self,body: Optional[B2cIdentityUserFlow] = None, request_configuration: Optional[B2cIdentityUserFlowItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[B2cIdentityUserFlow]:
        """
        Update the navigation property b2cUserFlows in identity
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[B2cIdentityUserFlow]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.b2c_identity_user_flow import B2cIdentityUserFlow

        return await self.request_adapter.send_async(request_info, B2cIdentityUserFlow, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[B2cIdentityUserFlowItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property b2cUserFlows for identity
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[B2cIdentityUserFlowItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents entry point for B2C identity userflows.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[B2cIdentityUserFlow] = None, request_configuration: Optional[B2cIdentityUserFlowItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property b2cUserFlows in identity
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
    
    def with_url(self,raw_url: Optional[str] = None) -> B2cIdentityUserFlowItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: B2cIdentityUserFlowItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return B2cIdentityUserFlowItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def identity_providers(self) -> IdentityProvidersRequestBuilder:
        """
        Provides operations to manage the identityProviders property of the microsoft.graph.b2cIdentityUserFlow entity.
        """
        from .identity_providers.identity_providers_request_builder import IdentityProvidersRequestBuilder

        return IdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def languages(self) -> LanguagesRequestBuilder:
        """
        Provides operations to manage the languages property of the microsoft.graph.b2cIdentityUserFlow entity.
        """
        from .languages.languages_request_builder import LanguagesRequestBuilder

        return LanguagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_attribute_assignments(self) -> UserAttributeAssignmentsRequestBuilder:
        """
        Provides operations to manage the userAttributeAssignments property of the microsoft.graph.b2cIdentityUserFlow entity.
        """
        from .user_attribute_assignments.user_attribute_assignments_request_builder import UserAttributeAssignmentsRequestBuilder

        return UserAttributeAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_flow_identity_providers(self) -> UserFlowIdentityProvidersRequestBuilder:
        """
        Provides operations to manage the userFlowIdentityProviders property of the microsoft.graph.b2cIdentityUserFlow entity.
        """
        from .user_flow_identity_providers.user_flow_identity_providers_request_builder import UserFlowIdentityProvidersRequestBuilder

        return UserFlowIdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class B2cIdentityUserFlowItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class B2cIdentityUserFlowItemRequestBuilderGetQueryParameters():
        """
        Represents entry point for B2C identity userflows.
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
    class B2cIdentityUserFlowItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[B2cIdentityUserFlowItemRequestBuilder.B2cIdentityUserFlowItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class B2cIdentityUserFlowItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

