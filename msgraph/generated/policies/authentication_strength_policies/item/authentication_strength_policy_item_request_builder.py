from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_strength_policy = lazy_import('msgraph.generated.models.authentication_strength_policy')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
combination_configurations_request_builder = lazy_import('msgraph.generated.policies.authentication_strength_policies.item.combination_configurations.combination_configurations_request_builder')
authentication_combination_configuration_item_request_builder = lazy_import('msgraph.generated.policies.authentication_strength_policies.item.combination_configurations.item.authentication_combination_configuration_item_request_builder')
update_allowed_combinations_request_builder = lazy_import('msgraph.generated.policies.authentication_strength_policies.item.update_allowed_combinations.update_allowed_combinations_request_builder')
usage_request_builder = lazy_import('msgraph.generated.policies.authentication_strength_policies.item.usage.usage_request_builder')

class AuthenticationStrengthPolicyItemRequestBuilder():
    """
    Provides operations to manage the authenticationStrengthPolicies property of the microsoft.graph.policyRoot entity.
    """
    @property
    def combination_configurations(self) -> combination_configurations_request_builder.CombinationConfigurationsRequestBuilder:
        """
        Provides operations to manage the combinationConfigurations property of the microsoft.graph.authenticationStrengthPolicy entity.
        """
        return combination_configurations_request_builder.CombinationConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_allowed_combinations(self) -> update_allowed_combinations_request_builder.UpdateAllowedCombinationsRequestBuilder:
        """
        Provides operations to call the updateAllowedCombinations method.
        """
        return update_allowed_combinations_request_builder.UpdateAllowedCombinationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def combination_configurations_by_id(self,id: str) -> authentication_combination_configuration_item_request_builder.AuthenticationCombinationConfigurationItemRequestBuilder:
        """
        Provides operations to manage the combinationConfigurations property of the microsoft.graph.authenticationStrengthPolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: authentication_combination_configuration_item_request_builder.AuthenticationCombinationConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["authenticationCombinationConfiguration%2Did"] = id
        return authentication_combination_configuration_item_request_builder.AuthenticationCombinationConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AuthenticationStrengthPolicyItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/policies/authenticationStrengthPolicies/{authenticationStrengthPolicy%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[AuthenticationStrengthPolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property authenticationStrengthPolicies for policies
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
    
    def create_get_request_information(self,request_configuration: Optional[AuthenticationStrengthPolicyItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The authentication method combinations that are to be used in scenarios defined by Azure AD Conditional Access.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[authentication_strength_policy.AuthenticationStrengthPolicy] = None, request_configuration: Optional[AuthenticationStrengthPolicyItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property authenticationStrengthPolicies in policies
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[AuthenticationStrengthPolicyItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property authenticationStrengthPolicies for policies
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[AuthenticationStrengthPolicyItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[authentication_strength_policy.AuthenticationStrengthPolicy]:
        """
        The authentication method combinations that are to be used in scenarios defined by Azure AD Conditional Access.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[authentication_strength_policy.AuthenticationStrengthPolicy]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, authentication_strength_policy.AuthenticationStrengthPolicy, response_handler, error_mapping)
    
    async def patch(self,body: Optional[authentication_strength_policy.AuthenticationStrengthPolicy] = None, request_configuration: Optional[AuthenticationStrengthPolicyItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[authentication_strength_policy.AuthenticationStrengthPolicy]:
        """
        Update the navigation property authenticationStrengthPolicies in policies
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[authentication_strength_policy.AuthenticationStrengthPolicy]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, authentication_strength_policy.AuthenticationStrengthPolicy, response_handler, error_mapping)
    
    def usage(self,) -> usage_request_builder.UsageRequestBuilder:
        """
        Provides operations to call the usage method.
        Returns: usage_request_builder.UsageRequestBuilder
        """
        return usage_request_builder.UsageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AuthenticationStrengthPolicyItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AuthenticationStrengthPolicyItemRequestBuilderGetQueryParameters():
        """
        The authentication method combinations that are to be used in scenarios defined by Azure AD Conditional Access.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class AuthenticationStrengthPolicyItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AuthenticationStrengthPolicyItemRequestBuilder.AuthenticationStrengthPolicyItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AuthenticationStrengthPolicyItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

