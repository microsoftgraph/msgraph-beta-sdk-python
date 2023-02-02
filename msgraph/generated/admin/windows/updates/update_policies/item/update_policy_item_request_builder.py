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

audience_request_builder = lazy_import('msgraph.generated.admin.windows.updates.update_policies.item.audience.audience_request_builder')
compliance_changes_request_builder = lazy_import('msgraph.generated.admin.windows.updates.update_policies.item.compliance_changes.compliance_changes_request_builder')
compliance_change_item_request_builder = lazy_import('msgraph.generated.admin.windows.updates.update_policies.item.compliance_changes.item.compliance_change_item_request_builder')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
update_policy = lazy_import('msgraph.generated.models.windows_updates.update_policy')

class UpdatePolicyItemRequestBuilder():
    """
    Provides operations to manage the updatePolicies property of the microsoft.graph.adminWindowsUpdates entity.
    """
    @property
    def audience(self) -> audience_request_builder.AudienceRequestBuilder:
        """
        Provides operations to manage the audience property of the microsoft.graph.windowsUpdates.updatePolicy entity.
        """
        return audience_request_builder.AudienceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance_changes(self) -> compliance_changes_request_builder.ComplianceChangesRequestBuilder:
        """
        Provides operations to manage the complianceChanges property of the microsoft.graph.windowsUpdates.updatePolicy entity.
        """
        return compliance_changes_request_builder.ComplianceChangesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def compliance_changes_by_id(self,id: str) -> compliance_change_item_request_builder.ComplianceChangeItemRequestBuilder:
        """
        Provides operations to manage the complianceChanges property of the microsoft.graph.windowsUpdates.updatePolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: compliance_change_item_request_builder.ComplianceChangeItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["complianceChange%2Did"] = id
        return compliance_change_item_request_builder.ComplianceChangeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, update_policy_id: Optional[str] = None) -> None:
        """
        Instantiates a new UpdatePolicyItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
            updatePolicyId: key: id of updatePolicy
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/admin/windows/updates/updatePolicies/{updatePolicy%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params["updatePolicy%2Did"] = updatePolicyId
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[UpdatePolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property updatePolicies for admin
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[UpdatePolicyItemRequestBuilderGetRequestConfiguration] = None) -> Optional[update_policy.UpdatePolicy]:
        """
        Get updatePolicies from admin
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[update_policy.UpdatePolicy]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, update_policy.UpdatePolicy, error_mapping)
    
    async def patch(self,body: Optional[update_policy.UpdatePolicy] = None, request_configuration: Optional[UpdatePolicyItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[update_policy.UpdatePolicy]:
        """
        Update the navigation property updatePolicies in admin
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[update_policy.UpdatePolicy]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, update_policy.UpdatePolicy, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[UpdatePolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property updatePolicies for admin
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
    
    def to_get_request_information(self,request_configuration: Optional[UpdatePolicyItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get updatePolicies from admin
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
    
    def to_patch_request_information(self,body: Optional[update_policy.UpdatePolicy] = None, request_configuration: Optional[UpdatePolicyItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property updatePolicies in admin
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
    
    @dataclass
    class UpdatePolicyItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UpdatePolicyItemRequestBuilderGetQueryParameters():
        """
        Get updatePolicies from admin
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
    class UpdatePolicyItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UpdatePolicyItemRequestBuilder.UpdatePolicyItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UpdatePolicyItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

