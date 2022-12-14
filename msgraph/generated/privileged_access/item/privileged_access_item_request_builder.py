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

privileged_access = lazy_import('msgraph.generated.models.privileged_access')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
resources_request_builder = lazy_import('msgraph.generated.privileged_access.item.resources.resources_request_builder')
governance_resource_item_request_builder = lazy_import('msgraph.generated.privileged_access.item.resources.item.governance_resource_item_request_builder')
role_assignment_requests_request_builder = lazy_import('msgraph.generated.privileged_access.item.role_assignment_requests.role_assignment_requests_request_builder')
governance_role_assignment_request_item_request_builder = lazy_import('msgraph.generated.privileged_access.item.role_assignment_requests.item.governance_role_assignment_request_item_request_builder')
role_assignments_request_builder = lazy_import('msgraph.generated.privileged_access.item.role_assignments.role_assignments_request_builder')
governance_role_assignment_item_request_builder = lazy_import('msgraph.generated.privileged_access.item.role_assignments.item.governance_role_assignment_item_request_builder')
role_definitions_request_builder = lazy_import('msgraph.generated.privileged_access.item.role_definitions.role_definitions_request_builder')
governance_role_definition_item_request_builder = lazy_import('msgraph.generated.privileged_access.item.role_definitions.item.governance_role_definition_item_request_builder')
role_settings_request_builder = lazy_import('msgraph.generated.privileged_access.item.role_settings.role_settings_request_builder')
governance_role_setting_item_request_builder = lazy_import('msgraph.generated.privileged_access.item.role_settings.item.governance_role_setting_item_request_builder')

class PrivilegedAccessItemRequestBuilder():
    """
    Provides operations to manage the collection of privilegedAccess entities.
    """
    @property
    def resources(self) -> resources_request_builder.ResourcesRequestBuilder:
        """
        Provides operations to manage the resources property of the microsoft.graph.privilegedAccess entity.
        """
        return resources_request_builder.ResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignment_requests(self) -> role_assignment_requests_request_builder.RoleAssignmentRequestsRequestBuilder:
        """
        Provides operations to manage the roleAssignmentRequests property of the microsoft.graph.privilegedAccess entity.
        """
        return role_assignment_requests_request_builder.RoleAssignmentRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignments(self) -> role_assignments_request_builder.RoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.privilegedAccess entity.
        """
        return role_assignments_request_builder.RoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definitions(self) -> role_definitions_request_builder.RoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.privilegedAccess entity.
        """
        return role_definitions_request_builder.RoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_settings(self) -> role_settings_request_builder.RoleSettingsRequestBuilder:
        """
        Provides operations to manage the roleSettings property of the microsoft.graph.privilegedAccess entity.
        """
        return role_settings_request_builder.RoleSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PrivilegedAccessItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/privilegedAccess/{privilegedAccess%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[PrivilegedAccessItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from privilegedAccess
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
    
    def create_get_request_information(self,request_configuration: Optional[PrivilegedAccessItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get entity from privilegedAccess by key
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
    
    def create_patch_request_information(self,body: Optional[privileged_access.PrivilegedAccess] = None, request_configuration: Optional[PrivilegedAccessItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in privilegedAccess
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
    
    async def delete(self,request_configuration: Optional[PrivilegedAccessItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete entity from privilegedAccess
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
    
    async def get(self,request_configuration: Optional[PrivilegedAccessItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[privileged_access.PrivilegedAccess]:
        """
        Get entity from privilegedAccess by key
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[privileged_access.PrivilegedAccess]
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
        return await self.request_adapter.send_async(request_info, privileged_access.PrivilegedAccess, response_handler, error_mapping)
    
    async def patch(self,body: Optional[privileged_access.PrivilegedAccess] = None, request_configuration: Optional[PrivilegedAccessItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[privileged_access.PrivilegedAccess]:
        """
        Update entity in privilegedAccess
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[privileged_access.PrivilegedAccess]
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
        return await self.request_adapter.send_async(request_info, privileged_access.PrivilegedAccess, response_handler, error_mapping)
    
    def resources_by_id(self,id: str) -> governance_resource_item_request_builder.GovernanceResourceItemRequestBuilder:
        """
        Provides operations to manage the resources property of the microsoft.graph.privilegedAccess entity.
        Args:
            id: Unique identifier of the item
        Returns: governance_resource_item_request_builder.GovernanceResourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["governanceResource%2Did"] = id
        return governance_resource_item_request_builder.GovernanceResourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_assignment_requests_by_id(self,id: str) -> governance_role_assignment_request_item_request_builder.GovernanceRoleAssignmentRequestItemRequestBuilder:
        """
        Provides operations to manage the roleAssignmentRequests property of the microsoft.graph.privilegedAccess entity.
        Args:
            id: Unique identifier of the item
        Returns: governance_role_assignment_request_item_request_builder.GovernanceRoleAssignmentRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["governanceRoleAssignmentRequest%2Did"] = id
        return governance_role_assignment_request_item_request_builder.GovernanceRoleAssignmentRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_assignments_by_id(self,id: str) -> governance_role_assignment_item_request_builder.GovernanceRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.privilegedAccess entity.
        Args:
            id: Unique identifier of the item
        Returns: governance_role_assignment_item_request_builder.GovernanceRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["governanceRoleAssignment%2Did"] = id
        return governance_role_assignment_item_request_builder.GovernanceRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_definitions_by_id(self,id: str) -> governance_role_definition_item_request_builder.GovernanceRoleDefinitionItemRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.privilegedAccess entity.
        Args:
            id: Unique identifier of the item
        Returns: governance_role_definition_item_request_builder.GovernanceRoleDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["governanceRoleDefinition%2Did"] = id
        return governance_role_definition_item_request_builder.GovernanceRoleDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_settings_by_id(self,id: str) -> governance_role_setting_item_request_builder.GovernanceRoleSettingItemRequestBuilder:
        """
        Provides operations to manage the roleSettings property of the microsoft.graph.privilegedAccess entity.
        Args:
            id: Unique identifier of the item
        Returns: governance_role_setting_item_request_builder.GovernanceRoleSettingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["governanceRoleSetting%2Did"] = id
        return governance_role_setting_item_request_builder.GovernanceRoleSettingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class PrivilegedAccessItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PrivilegedAccessItemRequestBuilderGetQueryParameters():
        """
        Get entity from privilegedAccess by key
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
    class PrivilegedAccessItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PrivilegedAccessItemRequestBuilder.PrivilegedAccessItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PrivilegedAccessItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

