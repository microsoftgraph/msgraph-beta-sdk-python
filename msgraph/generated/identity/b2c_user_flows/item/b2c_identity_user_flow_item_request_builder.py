from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import b2c_identity_user_flow
    from ....models.o_data_errors import o_data_error
    from .identity_providers import identity_providers_request_builder
    from .identity_providers.item import identity_provider_item_request_builder
    from .languages import languages_request_builder
    from .languages.item import user_flow_language_configuration_item_request_builder
    from .user_attribute_assignments import user_attribute_assignments_request_builder
    from .user_attribute_assignments.item import identity_user_flow_attribute_assignment_item_request_builder
    from .user_flow_identity_providers import user_flow_identity_providers_request_builder
    from .user_flow_identity_providers.item import identity_provider_base_item_request_builder

class B2cIdentityUserFlowItemRequestBuilder():
    """
    Provides operations to manage the b2cUserFlows property of the microsoft.graph.identityContainer entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new B2cIdentityUserFlowItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identity/b2cUserFlows/{b2cIdentityUserFlow%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[B2cIdentityUserFlowItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property b2cUserFlows for identity
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[B2cIdentityUserFlowItemRequestBuilderGetRequestConfiguration] = None) -> Optional[b2c_identity_user_flow.B2cIdentityUserFlow]:
        """
        Represents entry point for B2C identity userflows.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[b2c_identity_user_flow.B2cIdentityUserFlow]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import b2c_identity_user_flow

        return await self.request_adapter.send_async(request_info, b2c_identity_user_flow.B2cIdentityUserFlow, error_mapping)
    
    def identity_providers_by_id(self,id: str) -> identity_provider_item_request_builder.IdentityProviderItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.identity.b2cUserFlows.item.identityProviders.item collection
        Args:
            id: Unique identifier of the item
        Returns: identity_provider_item_request_builder.IdentityProviderItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .identity_providers.item import identity_provider_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["identityProvider%2Did"] = id
        return identity_provider_item_request_builder.IdentityProviderItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def languages_by_id(self,id: str) -> user_flow_language_configuration_item_request_builder.UserFlowLanguageConfigurationItemRequestBuilder:
        """
        Provides operations to manage the languages property of the microsoft.graph.b2cIdentityUserFlow entity.
        Args:
            id: Unique identifier of the item
        Returns: user_flow_language_configuration_item_request_builder.UserFlowLanguageConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .languages.item import user_flow_language_configuration_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userFlowLanguageConfiguration%2Did"] = id
        return user_flow_language_configuration_item_request_builder.UserFlowLanguageConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[b2c_identity_user_flow.B2cIdentityUserFlow] = None, request_configuration: Optional[B2cIdentityUserFlowItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[b2c_identity_user_flow.B2cIdentityUserFlow]:
        """
        Update the navigation property b2cUserFlows in identity
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[b2c_identity_user_flow.B2cIdentityUserFlow]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import b2c_identity_user_flow

        return await self.request_adapter.send_async(request_info, b2c_identity_user_flow.B2cIdentityUserFlow, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[B2cIdentityUserFlowItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property b2cUserFlows for identity
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[B2cIdentityUserFlowItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents entry point for B2C identity userflows.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[b2c_identity_user_flow.B2cIdentityUserFlow] = None, request_configuration: Optional[B2cIdentityUserFlowItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property b2cUserFlows in identity
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def user_attribute_assignments_by_id(self,id: str) -> identity_user_flow_attribute_assignment_item_request_builder.IdentityUserFlowAttributeAssignmentItemRequestBuilder:
        """
        Provides operations to manage the userAttributeAssignments property of the microsoft.graph.b2cIdentityUserFlow entity.
        Args:
            id: Unique identifier of the item
        Returns: identity_user_flow_attribute_assignment_item_request_builder.IdentityUserFlowAttributeAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_attribute_assignments.item import identity_user_flow_attribute_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["identityUserFlowAttributeAssignment%2Did"] = id
        return identity_user_flow_attribute_assignment_item_request_builder.IdentityUserFlowAttributeAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_flow_identity_providers_by_id(self,id: str) -> identity_provider_base_item_request_builder.IdentityProviderBaseItemRequestBuilder:
        """
        Provides operations to manage the userFlowIdentityProviders property of the microsoft.graph.b2cIdentityUserFlow entity.
        Args:
            id: Unique identifier of the item
        Returns: identity_provider_base_item_request_builder.IdentityProviderBaseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_flow_identity_providers.item import identity_provider_base_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["identityProviderBase%2Did"] = id
        return identity_provider_base_item_request_builder.IdentityProviderBaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def identity_providers(self) -> identity_providers_request_builder.IdentityProvidersRequestBuilder:
        """
        Provides operations to manage the identityProviders property of the microsoft.graph.b2cIdentityUserFlow entity.
        """
        from .identity_providers import identity_providers_request_builder

        return identity_providers_request_builder.IdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def languages(self) -> languages_request_builder.LanguagesRequestBuilder:
        """
        Provides operations to manage the languages property of the microsoft.graph.b2cIdentityUserFlow entity.
        """
        from .languages import languages_request_builder

        return languages_request_builder.LanguagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_attribute_assignments(self) -> user_attribute_assignments_request_builder.UserAttributeAssignmentsRequestBuilder:
        """
        Provides operations to manage the userAttributeAssignments property of the microsoft.graph.b2cIdentityUserFlow entity.
        """
        from .user_attribute_assignments import user_attribute_assignments_request_builder

        return user_attribute_assignments_request_builder.UserAttributeAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_flow_identity_providers(self) -> user_flow_identity_providers_request_builder.UserFlowIdentityProvidersRequestBuilder:
        """
        Provides operations to manage the userFlowIdentityProviders property of the microsoft.graph.b2cIdentityUserFlow entity.
        """
        from .user_flow_identity_providers import user_flow_identity_providers_request_builder

        return user_flow_identity_providers_request_builder.UserFlowIdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class B2cIdentityUserFlowItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class B2cIdentityUserFlowItemRequestBuilderGetQueryParameters():
        """
        Represents entry point for B2C identity userflows.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
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
    class B2cIdentityUserFlowItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[B2cIdentityUserFlowItemRequestBuilder.B2cIdentityUserFlowItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class B2cIdentityUserFlowItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

