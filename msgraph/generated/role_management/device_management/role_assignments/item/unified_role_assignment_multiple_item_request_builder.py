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

unified_role_assignment_multiple = lazy_import('msgraph.generated.models.unified_role_assignment_multiple')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
app_scopes_request_builder = lazy_import('msgraph.generated.role_management.device_management.role_assignments.item.app_scopes.app_scopes_request_builder')
app_scope_item_request_builder = lazy_import('msgraph.generated.role_management.device_management.role_assignments.item.app_scopes.item.app_scope_item_request_builder')
directory_scopes_request_builder = lazy_import('msgraph.generated.role_management.device_management.role_assignments.item.directory_scopes.directory_scopes_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.role_management.device_management.role_assignments.item.directory_scopes.item.directory_object_item_request_builder')
principals_request_builder = lazy_import('msgraph.generated.role_management.device_management.role_assignments.item.principals.principals_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.role_management.device_management.role_assignments.item.principals.item.directory_object_item_request_builder')
role_definition_request_builder = lazy_import('msgraph.generated.role_management.device_management.role_assignments.item.role_definition.role_definition_request_builder')

class UnifiedRoleAssignmentMultipleItemRequestBuilder():
    """
    Provides operations to manage the roleAssignments property of the microsoft.graph.rbacApplicationMultiple entity.
    """
    @property
    def app_scopes(self) -> app_scopes_request_builder.AppScopesRequestBuilder:
        """
        Provides operations to manage the appScopes property of the microsoft.graph.unifiedRoleAssignmentMultiple entity.
        """
        return app_scopes_request_builder.AppScopesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_scopes(self) -> directory_scopes_request_builder.DirectoryScopesRequestBuilder:
        """
        Provides operations to manage the directoryScopes property of the microsoft.graph.unifiedRoleAssignmentMultiple entity.
        """
        return directory_scopes_request_builder.DirectoryScopesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def principals(self) -> principals_request_builder.PrincipalsRequestBuilder:
        """
        Provides operations to manage the principals property of the microsoft.graph.unifiedRoleAssignmentMultiple entity.
        """
        return principals_request_builder.PrincipalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definition(self) -> role_definition_request_builder.RoleDefinitionRequestBuilder:
        """
        Provides operations to manage the roleDefinition property of the microsoft.graph.unifiedRoleAssignmentMultiple entity.
        """
        return role_definition_request_builder.RoleDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    def app_scopes_by_id(self,id: str) -> app_scope_item_request_builder.AppScopeItemRequestBuilder:
        """
        Provides operations to manage the appScopes property of the microsoft.graph.unifiedRoleAssignmentMultiple entity.
        Args:
            id: Unique identifier of the item
        Returns: app_scope_item_request_builder.AppScopeItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["appScope%2Did"] = id
        return app_scope_item_request_builder.AppScopeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UnifiedRoleAssignmentMultipleItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/roleManagement/deviceManagement/roleAssignments/{unifiedRoleAssignmentMultiple%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[UnifiedRoleAssignmentMultipleItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property roleAssignments for roleManagement
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
    
    def create_get_request_information(self,request_configuration: Optional[UnifiedRoleAssignmentMultipleItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get roleAssignments from roleManagement
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
    
    def create_patch_request_information(self,body: Optional[unified_role_assignment_multiple.UnifiedRoleAssignmentMultiple] = None, request_configuration: Optional[UnifiedRoleAssignmentMultipleItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property roleAssignments in roleManagement
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
    
    async def delete(self,request_configuration: Optional[UnifiedRoleAssignmentMultipleItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property roleAssignments for roleManagement
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
    
    def directory_scopes_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the directoryScopes property of the microsoft.graph.unifiedRoleAssignmentMultiple entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[UnifiedRoleAssignmentMultipleItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[unified_role_assignment_multiple.UnifiedRoleAssignmentMultiple]:
        """
        Get roleAssignments from roleManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[unified_role_assignment_multiple.UnifiedRoleAssignmentMultiple]
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
        return await self.request_adapter.send_async(request_info, unified_role_assignment_multiple.UnifiedRoleAssignmentMultiple, response_handler, error_mapping)
    
    async def patch(self,body: Optional[unified_role_assignment_multiple.UnifiedRoleAssignmentMultiple] = None, request_configuration: Optional[UnifiedRoleAssignmentMultipleItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[unified_role_assignment_multiple.UnifiedRoleAssignmentMultiple]:
        """
        Update the navigation property roleAssignments in roleManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[unified_role_assignment_multiple.UnifiedRoleAssignmentMultiple]
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
        return await self.request_adapter.send_async(request_info, unified_role_assignment_multiple.UnifiedRoleAssignmentMultiple, response_handler, error_mapping)
    
    def principals_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the principals property of the microsoft.graph.unifiedRoleAssignmentMultiple entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class UnifiedRoleAssignmentMultipleItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UnifiedRoleAssignmentMultipleItemRequestBuilderGetQueryParameters():
        """
        Get roleAssignments from roleManagement
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
    class UnifiedRoleAssignmentMultipleItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UnifiedRoleAssignmentMultipleItemRequestBuilder.UnifiedRoleAssignmentMultipleItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UnifiedRoleAssignmentMultipleItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

