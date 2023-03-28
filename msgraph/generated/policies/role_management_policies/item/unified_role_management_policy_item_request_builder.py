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
    from ....models import unified_role_management_policy
    from ....models.o_data_errors import o_data_error
    from .effective_rules import effective_rules_request_builder
    from .effective_rules.item import unified_role_management_policy_rule_item_request_builder
    from .rules import rules_request_builder
    from .rules.item import unified_role_management_policy_rule_item_request_builder

class UnifiedRoleManagementPolicyItemRequestBuilder():
    """
    Provides operations to manage the roleManagementPolicies property of the microsoft.graph.policyRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UnifiedRoleManagementPolicyItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/policies/roleManagementPolicies/{unifiedRoleManagementPolicy%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[UnifiedRoleManagementPolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property roleManagementPolicies for policies
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
    
    def effective_rules_by_id(self,id: str) -> unified_role_management_policy_rule_item_request_builder.UnifiedRoleManagementPolicyRuleItemRequestBuilder:
        """
        Provides operations to manage the effectiveRules property of the microsoft.graph.unifiedRoleManagementPolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_management_policy_rule_item_request_builder.UnifiedRoleManagementPolicyRuleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .effective_rules.item import unified_role_management_policy_rule_item_request_builder
        from .rules.item import unified_role_management_policy_rule_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleManagementPolicyRule%2Did"] = id
        return unified_role_management_policy_rule_item_request_builder.UnifiedRoleManagementPolicyRuleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[UnifiedRoleManagementPolicyItemRequestBuilderGetRequestConfiguration] = None) -> Optional[unified_role_management_policy.UnifiedRoleManagementPolicy]:
        """
        Represents the role management policies.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[unified_role_management_policy.UnifiedRoleManagementPolicy]
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
        from ....models import unified_role_management_policy

        return await self.request_adapter.send_async(request_info, unified_role_management_policy.UnifiedRoleManagementPolicy, error_mapping)
    
    async def patch(self,body: Optional[unified_role_management_policy.UnifiedRoleManagementPolicy] = None, request_configuration: Optional[UnifiedRoleManagementPolicyItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[unified_role_management_policy.UnifiedRoleManagementPolicy]:
        """
        Update the navigation property roleManagementPolicies in policies
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[unified_role_management_policy.UnifiedRoleManagementPolicy]
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
        from ....models import unified_role_management_policy

        return await self.request_adapter.send_async(request_info, unified_role_management_policy.UnifiedRoleManagementPolicy, error_mapping)
    
    def rules_by_id(self,id: str) -> unified_role_management_policy_rule_item_request_builder.UnifiedRoleManagementPolicyRuleItemRequestBuilder:
        """
        Provides operations to manage the rules property of the microsoft.graph.unifiedRoleManagementPolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_management_policy_rule_item_request_builder.UnifiedRoleManagementPolicyRuleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .effective_rules.item import unified_role_management_policy_rule_item_request_builder
        from .rules.item import unified_role_management_policy_rule_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleManagementPolicyRule%2Did"] = id
        return unified_role_management_policy_rule_item_request_builder.UnifiedRoleManagementPolicyRuleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[UnifiedRoleManagementPolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property roleManagementPolicies for policies
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
    
    def to_get_request_information(self,request_configuration: Optional[UnifiedRoleManagementPolicyItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents the role management policies.
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
    
    def to_patch_request_information(self,body: Optional[unified_role_management_policy.UnifiedRoleManagementPolicy] = None, request_configuration: Optional[UnifiedRoleManagementPolicyItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property roleManagementPolicies in policies
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
    
    @property
    def effective_rules(self) -> effective_rules_request_builder.EffectiveRulesRequestBuilder:
        """
        Provides operations to manage the effectiveRules property of the microsoft.graph.unifiedRoleManagementPolicy entity.
        """
        from .effective_rules import effective_rules_request_builder

        return effective_rules_request_builder.EffectiveRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rules(self) -> rules_request_builder.RulesRequestBuilder:
        """
        Provides operations to manage the rules property of the microsoft.graph.unifiedRoleManagementPolicy entity.
        """
        from .rules import rules_request_builder

        return rules_request_builder.RulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class UnifiedRoleManagementPolicyItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UnifiedRoleManagementPolicyItemRequestBuilderGetQueryParameters():
        """
        Represents the role management policies.
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
    class UnifiedRoleManagementPolicyItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UnifiedRoleManagementPolicyItemRequestBuilder.UnifiedRoleManagementPolicyItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UnifiedRoleManagementPolicyItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

