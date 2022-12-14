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

access_package_resource_environment_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.access_package_resource_role_scopes.item.access_package_resource_role.access_package_resource.access_package_resource_environment.access_package_resource_environment_request_builder')
access_package_resource_roles_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.access_package_resource_role_scopes.item.access_package_resource_role.access_package_resource.access_package_resource_roles.access_package_resource_roles_request_builder')
access_package_resource_role_item_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.access_package_resource_role_scopes.item.access_package_resource_role.access_package_resource.access_package_resource_roles.item.access_package_resource_role_item_request_builder')
access_package_resource_scopes_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.access_package_resource_role_scopes.item.access_package_resource_role.access_package_resource.access_package_resource_scopes.access_package_resource_scopes_request_builder')
access_package_resource_scope_item_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.access_package_resource_role_scopes.item.access_package_resource_role.access_package_resource.access_package_resource_scopes.item.access_package_resource_scope_item_request_builder')
access_package_resource = lazy_import('msgraph.generated.models.access_package_resource')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class AccessPackageResourceRequestBuilder():
    """
    Provides operations to manage the accessPackageResource property of the microsoft.graph.accessPackageResourceRole entity.
    """
    @property
    def access_package_resource_environment(self) -> access_package_resource_environment_request_builder.AccessPackageResourceEnvironmentRequestBuilder:
        """
        Provides operations to manage the accessPackageResourceEnvironment property of the microsoft.graph.accessPackageResource entity.
        """
        return access_package_resource_environment_request_builder.AccessPackageResourceEnvironmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_package_resource_roles(self) -> access_package_resource_roles_request_builder.AccessPackageResourceRolesRequestBuilder:
        """
        Provides operations to manage the accessPackageResourceRoles property of the microsoft.graph.accessPackageResource entity.
        """
        return access_package_resource_roles_request_builder.AccessPackageResourceRolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_package_resource_scopes(self) -> access_package_resource_scopes_request_builder.AccessPackageResourceScopesRequestBuilder:
        """
        Provides operations to manage the accessPackageResourceScopes property of the microsoft.graph.accessPackageResource entity.
        """
        return access_package_resource_scopes_request_builder.AccessPackageResourceScopesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def access_package_resource_roles_by_id(self,id: str) -> access_package_resource_role_item_request_builder.AccessPackageResourceRoleItemRequestBuilder:
        """
        Provides operations to manage the accessPackageResourceRoles property of the microsoft.graph.accessPackageResource entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_resource_role_item_request_builder.AccessPackageResourceRoleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageResourceRole%2Did"] = id
        return access_package_resource_role_item_request_builder.AccessPackageResourceRoleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def access_package_resource_scopes_by_id(self,id: str) -> access_package_resource_scope_item_request_builder.AccessPackageResourceScopeItemRequestBuilder:
        """
        Provides operations to manage the accessPackageResourceScopes property of the microsoft.graph.accessPackageResource entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_resource_scope_item_request_builder.AccessPackageResourceScopeItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageResourceScope%2Did"] = id
        return access_package_resource_scope_item_request_builder.AccessPackageResourceScopeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessPackageResourceRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/entitlementManagement/accessPackageAssignments/{accessPackageAssignment%2Did}/accessPackage/accessPackageResourceRoleScopes/{accessPackageResourceRoleScope%2Did}/accessPackageResourceRole/accessPackageResource{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[AccessPackageResourceRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property accessPackageResource for identityGovernance
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
    
    def create_get_request_information(self,request_configuration: Optional[AccessPackageResourceRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get accessPackageResource from identityGovernance
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
    
    def create_patch_request_information(self,body: Optional[access_package_resource.AccessPackageResource] = None, request_configuration: Optional[AccessPackageResourceRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property accessPackageResource in identityGovernance
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
    
    async def delete(self,request_configuration: Optional[AccessPackageResourceRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property accessPackageResource for identityGovernance
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
    
    async def get(self,request_configuration: Optional[AccessPackageResourceRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[access_package_resource.AccessPackageResource]:
        """
        Get accessPackageResource from identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[access_package_resource.AccessPackageResource]
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
        return await self.request_adapter.send_async(request_info, access_package_resource.AccessPackageResource, response_handler, error_mapping)
    
    async def patch(self,body: Optional[access_package_resource.AccessPackageResource] = None, request_configuration: Optional[AccessPackageResourceRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[access_package_resource.AccessPackageResource]:
        """
        Update the navigation property accessPackageResource in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[access_package_resource.AccessPackageResource]
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
        return await self.request_adapter.send_async(request_info, access_package_resource.AccessPackageResource, response_handler, error_mapping)
    
    @dataclass
    class AccessPackageResourceRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AccessPackageResourceRequestBuilderGetQueryParameters():
        """
        Get accessPackageResource from identityGovernance
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
    class AccessPackageResourceRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AccessPackageResourceRequestBuilder.AccessPackageResourceRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AccessPackageResourceRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

