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

rbac_application_multiple = lazy_import('msgraph.generated.models.rbac_application_multiple')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
resource_namespaces_request_builder = lazy_import('msgraph.generated.role_management.cloud_p_c.resource_namespaces.resource_namespaces_request_builder')
unified_rbac_resource_namespace_item_request_builder = lazy_import('msgraph.generated.role_management.cloud_p_c.resource_namespaces.item.unified_rbac_resource_namespace_item_request_builder')
role_assignments_request_builder = lazy_import('msgraph.generated.role_management.cloud_p_c.role_assignments.role_assignments_request_builder')
unified_role_assignment_multiple_item_request_builder = lazy_import('msgraph.generated.role_management.cloud_p_c.role_assignments.item.unified_role_assignment_multiple_item_request_builder')
role_definitions_request_builder = lazy_import('msgraph.generated.role_management.cloud_p_c.role_definitions.role_definitions_request_builder')
unified_role_definition_item_request_builder = lazy_import('msgraph.generated.role_management.cloud_p_c.role_definitions.item.unified_role_definition_item_request_builder')

class CloudPCRequestBuilder():
    """
    Provides operations to manage the cloudPC property of the microsoft.graph.roleManagement entity.
    """
    @property
    def resource_namespaces(self) -> resource_namespaces_request_builder.ResourceNamespacesRequestBuilder:
        """
        Provides operations to manage the resourceNamespaces property of the microsoft.graph.rbacApplicationMultiple entity.
        """
        return resource_namespaces_request_builder.ResourceNamespacesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignments(self) -> role_assignments_request_builder.RoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.rbacApplicationMultiple entity.
        """
        return role_assignments_request_builder.RoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definitions(self) -> role_definitions_request_builder.RoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.rbacApplicationMultiple entity.
        """
        return role_definitions_request_builder.RoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CloudPCRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/roleManagement/cloudPC{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[CloudPCRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property cloudPC for roleManagement
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
    
    async def get(self,request_configuration: Optional[CloudPCRequestBuilderGetRequestConfiguration] = None) -> Optional[rbac_application_multiple.RbacApplicationMultiple]:
        """
        Get cloudPC from roleManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[rbac_application_multiple.RbacApplicationMultiple]
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
        return await self.request_adapter.send_async(request_info, rbac_application_multiple.RbacApplicationMultiple, error_mapping)
    
    async def patch(self,body: Optional[rbac_application_multiple.RbacApplicationMultiple] = None, request_configuration: Optional[CloudPCRequestBuilderPatchRequestConfiguration] = None) -> Optional[rbac_application_multiple.RbacApplicationMultiple]:
        """
        Update the navigation property cloudPC in roleManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[rbac_application_multiple.RbacApplicationMultiple]
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
        return await self.request_adapter.send_async(request_info, rbac_application_multiple.RbacApplicationMultiple, error_mapping)
    
    def resource_namespaces_by_id(self,id: str) -> unified_rbac_resource_namespace_item_request_builder.UnifiedRbacResourceNamespaceItemRequestBuilder:
        """
        Provides operations to manage the resourceNamespaces property of the microsoft.graph.rbacApplicationMultiple entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_rbac_resource_namespace_item_request_builder.UnifiedRbacResourceNamespaceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRbacResourceNamespace%2Did"] = id
        return unified_rbac_resource_namespace_item_request_builder.UnifiedRbacResourceNamespaceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_assignments_by_id(self,id: str) -> unified_role_assignment_multiple_item_request_builder.UnifiedRoleAssignmentMultipleItemRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.rbacApplicationMultiple entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_assignment_multiple_item_request_builder.UnifiedRoleAssignmentMultipleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleAssignmentMultiple%2Did"] = id
        return unified_role_assignment_multiple_item_request_builder.UnifiedRoleAssignmentMultipleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_definitions_by_id(self,id: str) -> unified_role_definition_item_request_builder.UnifiedRoleDefinitionItemRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.rbacApplicationMultiple entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_definition_item_request_builder.UnifiedRoleDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleDefinition%2Did"] = id
        return unified_role_definition_item_request_builder.UnifiedRoleDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[CloudPCRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property cloudPC for roleManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[CloudPCRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get cloudPC from roleManagement
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
    
    def to_patch_request_information(self,body: Optional[rbac_application_multiple.RbacApplicationMultiple] = None, request_configuration: Optional[CloudPCRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property cloudPC in roleManagement
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
    class CloudPCRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class CloudPCRequestBuilderGetQueryParameters():
        """
        Get cloudPC from roleManagement
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
    class CloudPCRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CloudPCRequestBuilder.CloudPCRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class CloudPCRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

