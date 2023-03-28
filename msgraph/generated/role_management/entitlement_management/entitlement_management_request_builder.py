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
    from ...models import rbac_application
    from ...models.o_data_errors import o_data_error
    from .resource_namespaces import resource_namespaces_request_builder
    from .resource_namespaces.item import unified_rbac_resource_namespace_item_request_builder
    from .role_assignment_approvals import role_assignment_approvals_request_builder
    from .role_assignment_approvals.item import approval_item_request_builder
    from .role_assignments import role_assignments_request_builder
    from .role_assignments.item import unified_role_assignment_item_request_builder
    from .role_assignment_schedule_instances import role_assignment_schedule_instances_request_builder
    from .role_assignment_schedule_instances.item import unified_role_assignment_schedule_instance_item_request_builder
    from .role_assignment_schedule_requests import role_assignment_schedule_requests_request_builder
    from .role_assignment_schedule_requests.item import unified_role_assignment_schedule_request_item_request_builder
    from .role_assignment_schedules import role_assignment_schedules_request_builder
    from .role_assignment_schedules.item import unified_role_assignment_schedule_item_request_builder
    from .role_definitions import role_definitions_request_builder
    from .role_definitions.item import unified_role_definition_item_request_builder
    from .role_eligibility_schedule_instances import role_eligibility_schedule_instances_request_builder
    from .role_eligibility_schedule_instances.item import unified_role_eligibility_schedule_instance_item_request_builder
    from .role_eligibility_schedule_requests import role_eligibility_schedule_requests_request_builder
    from .role_eligibility_schedule_requests.item import unified_role_eligibility_schedule_request_item_request_builder
    from .role_eligibility_schedules import role_eligibility_schedules_request_builder
    from .role_eligibility_schedules.item import unified_role_eligibility_schedule_item_request_builder
    from .role_schedule_instancesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id import role_schedule_instancesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id_request_builder
    from .role_schedulesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id import role_schedulesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id_request_builder
    from .transitive_role_assignments import transitive_role_assignments_request_builder
    from .transitive_role_assignments.item import unified_role_assignment_item_request_builder

class EntitlementManagementRequestBuilder():
    """
    Provides operations to manage the entitlementManagement property of the microsoft.graph.roleManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EntitlementManagementRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/roleManagement/entitlementManagement{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[EntitlementManagementRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property entitlementManagement for roleManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[EntitlementManagementRequestBuilderGetRequestConfiguration] = None) -> Optional[rbac_application.RbacApplication]:
        """
        The RbacApplication for Entitlement Management
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[rbac_application.RbacApplication]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import rbac_application

        return await self.request_adapter.send_async(request_info, rbac_application.RbacApplication, error_mapping)
    
    async def patch(self,body: Optional[rbac_application.RbacApplication] = None, request_configuration: Optional[EntitlementManagementRequestBuilderPatchRequestConfiguration] = None) -> Optional[rbac_application.RbacApplication]:
        """
        Update the navigation property entitlementManagement in roleManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[rbac_application.RbacApplication]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import rbac_application

        return await self.request_adapter.send_async(request_info, rbac_application.RbacApplication, error_mapping)
    
    def resource_namespaces_by_id(self,id: str) -> unified_rbac_resource_namespace_item_request_builder.UnifiedRbacResourceNamespaceItemRequestBuilder:
        """
        Provides operations to manage the resourceNamespaces property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_rbac_resource_namespace_item_request_builder.UnifiedRbacResourceNamespaceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .resource_namespaces.item import unified_rbac_resource_namespace_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRbacResourceNamespace%2Did"] = id
        return unified_rbac_resource_namespace_item_request_builder.UnifiedRbacResourceNamespaceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_assignment_approvals_by_id(self,id: str) -> approval_item_request_builder.ApprovalItemRequestBuilder:
        """
        Provides operations to manage the roleAssignmentApprovals property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: approval_item_request_builder.ApprovalItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_assignment_approvals.item import approval_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["approval%2Did"] = id
        return approval_item_request_builder.ApprovalItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_assignments_by_id(self,id: str) -> unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_assignments.item import unified_role_assignment_item_request_builder
        from .transitive_role_assignments.item import unified_role_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleAssignment%2Did"] = id
        return unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_assignment_schedule_instances_by_id(self,id: str) -> unified_role_assignment_schedule_instance_item_request_builder.UnifiedRoleAssignmentScheduleInstanceItemRequestBuilder:
        """
        Provides operations to manage the roleAssignmentScheduleInstances property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_assignment_schedule_instance_item_request_builder.UnifiedRoleAssignmentScheduleInstanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_assignment_schedule_instances.item import unified_role_assignment_schedule_instance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleAssignmentScheduleInstance%2Did"] = id
        return unified_role_assignment_schedule_instance_item_request_builder.UnifiedRoleAssignmentScheduleInstanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_assignment_schedule_requests_by_id(self,id: str) -> unified_role_assignment_schedule_request_item_request_builder.UnifiedRoleAssignmentScheduleRequestItemRequestBuilder:
        """
        Provides operations to manage the roleAssignmentScheduleRequests property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_assignment_schedule_request_item_request_builder.UnifiedRoleAssignmentScheduleRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_assignment_schedule_requests.item import unified_role_assignment_schedule_request_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleAssignmentScheduleRequest%2Did"] = id
        return unified_role_assignment_schedule_request_item_request_builder.UnifiedRoleAssignmentScheduleRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_assignment_schedules_by_id(self,id: str) -> unified_role_assignment_schedule_item_request_builder.UnifiedRoleAssignmentScheduleItemRequestBuilder:
        """
        Provides operations to manage the roleAssignmentSchedules property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_assignment_schedule_item_request_builder.UnifiedRoleAssignmentScheduleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_assignment_schedules.item import unified_role_assignment_schedule_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleAssignmentSchedule%2Did"] = id
        return unified_role_assignment_schedule_item_request_builder.UnifiedRoleAssignmentScheduleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_definitions_by_id(self,id: str) -> unified_role_definition_item_request_builder.UnifiedRoleDefinitionItemRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_definition_item_request_builder.UnifiedRoleDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_definitions.item import unified_role_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleDefinition%2Did"] = id
        return unified_role_definition_item_request_builder.UnifiedRoleDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_eligibility_schedule_instances_by_id(self,id: str) -> unified_role_eligibility_schedule_instance_item_request_builder.UnifiedRoleEligibilityScheduleInstanceItemRequestBuilder:
        """
        Provides operations to manage the roleEligibilityScheduleInstances property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_eligibility_schedule_instance_item_request_builder.UnifiedRoleEligibilityScheduleInstanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_eligibility_schedule_instances.item import unified_role_eligibility_schedule_instance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleEligibilityScheduleInstance%2Did"] = id
        return unified_role_eligibility_schedule_instance_item_request_builder.UnifiedRoleEligibilityScheduleInstanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_eligibility_schedule_requests_by_id(self,id: str) -> unified_role_eligibility_schedule_request_item_request_builder.UnifiedRoleEligibilityScheduleRequestItemRequestBuilder:
        """
        Provides operations to manage the roleEligibilityScheduleRequests property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_eligibility_schedule_request_item_request_builder.UnifiedRoleEligibilityScheduleRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_eligibility_schedule_requests.item import unified_role_eligibility_schedule_request_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleEligibilityScheduleRequest%2Did"] = id
        return unified_role_eligibility_schedule_request_item_request_builder.UnifiedRoleEligibilityScheduleRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_eligibility_schedules_by_id(self,id: str) -> unified_role_eligibility_schedule_item_request_builder.UnifiedRoleEligibilityScheduleItemRequestBuilder:
        """
        Provides operations to manage the roleEligibilitySchedules property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_eligibility_schedule_item_request_builder.UnifiedRoleEligibilityScheduleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_eligibility_schedules.item import unified_role_eligibility_schedule_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleEligibilitySchedule%2Did"] = id
        return unified_role_eligibility_schedule_item_request_builder.UnifiedRoleEligibilityScheduleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[EntitlementManagementRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property entitlementManagement for roleManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[EntitlementManagementRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The RbacApplication for Entitlement Management
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
    
    def to_patch_request_information(self,body: Optional[rbac_application.RbacApplication] = None, request_configuration: Optional[EntitlementManagementRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property entitlementManagement in roleManagement
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
    
    def transitive_role_assignments_by_id(self,id: str) -> unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the transitiveRoleAssignments property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_assignments.item import unified_role_assignment_item_request_builder
        from .transitive_role_assignments.item import unified_role_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleAssignment%2Did"] = id
        return unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def resource_namespaces(self) -> resource_namespaces_request_builder.ResourceNamespacesRequestBuilder:
        """
        Provides operations to manage the resourceNamespaces property of the microsoft.graph.rbacApplication entity.
        """
        from .resource_namespaces import resource_namespaces_request_builder

        return resource_namespaces_request_builder.ResourceNamespacesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignment_approvals(self) -> role_assignment_approvals_request_builder.RoleAssignmentApprovalsRequestBuilder:
        """
        Provides operations to manage the roleAssignmentApprovals property of the microsoft.graph.rbacApplication entity.
        """
        from .role_assignment_approvals import role_assignment_approvals_request_builder

        return role_assignment_approvals_request_builder.RoleAssignmentApprovalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignments(self) -> role_assignments_request_builder.RoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.rbacApplication entity.
        """
        from .role_assignments import role_assignments_request_builder

        return role_assignments_request_builder.RoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignment_schedule_instances(self) -> role_assignment_schedule_instances_request_builder.RoleAssignmentScheduleInstancesRequestBuilder:
        """
        Provides operations to manage the roleAssignmentScheduleInstances property of the microsoft.graph.rbacApplication entity.
        """
        from .role_assignment_schedule_instances import role_assignment_schedule_instances_request_builder

        return role_assignment_schedule_instances_request_builder.RoleAssignmentScheduleInstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignment_schedule_requests(self) -> role_assignment_schedule_requests_request_builder.RoleAssignmentScheduleRequestsRequestBuilder:
        """
        Provides operations to manage the roleAssignmentScheduleRequests property of the microsoft.graph.rbacApplication entity.
        """
        from .role_assignment_schedule_requests import role_assignment_schedule_requests_request_builder

        return role_assignment_schedule_requests_request_builder.RoleAssignmentScheduleRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignment_schedules(self) -> role_assignment_schedules_request_builder.RoleAssignmentSchedulesRequestBuilder:
        """
        Provides operations to manage the roleAssignmentSchedules property of the microsoft.graph.rbacApplication entity.
        """
        from .role_assignment_schedules import role_assignment_schedules_request_builder

        return role_assignment_schedules_request_builder.RoleAssignmentSchedulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definitions(self) -> role_definitions_request_builder.RoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.rbacApplication entity.
        """
        from .role_definitions import role_definitions_request_builder

        return role_definitions_request_builder.RoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_eligibility_schedule_instances(self) -> role_eligibility_schedule_instances_request_builder.RoleEligibilityScheduleInstancesRequestBuilder:
        """
        Provides operations to manage the roleEligibilityScheduleInstances property of the microsoft.graph.rbacApplication entity.
        """
        from .role_eligibility_schedule_instances import role_eligibility_schedule_instances_request_builder

        return role_eligibility_schedule_instances_request_builder.RoleEligibilityScheduleInstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_eligibility_schedule_requests(self) -> role_eligibility_schedule_requests_request_builder.RoleEligibilityScheduleRequestsRequestBuilder:
        """
        Provides operations to manage the roleEligibilityScheduleRequests property of the microsoft.graph.rbacApplication entity.
        """
        from .role_eligibility_schedule_requests import role_eligibility_schedule_requests_request_builder

        return role_eligibility_schedule_requests_request_builder.RoleEligibilityScheduleRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_eligibility_schedules(self) -> role_eligibility_schedules_request_builder.RoleEligibilitySchedulesRequestBuilder:
        """
        Provides operations to manage the roleEligibilitySchedules property of the microsoft.graph.rbacApplication entity.
        """
        from .role_eligibility_schedules import role_eligibility_schedules_request_builder

        return role_eligibility_schedules_request_builder.RoleEligibilitySchedulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_schedule_instancesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id(self) -> role_schedule_instancesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id_request_builder.RoleScheduleInstancesdirectoryScopeIdDirectoryScopeIdAppScopeIdAppScopeIdPrincipalIdPrincipalIdRoleDefinitionIdRoleDefinitionIdRequestBuilder:
        """
        Provides operations to call the roleScheduleInstances method.
        """
        from .role_schedule_instancesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id import role_schedule_instancesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id_request_builder

        return role_schedule_instancesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id_request_builder.RoleScheduleInstancesdirectoryScopeIdDirectoryScopeIdAppScopeIdAppScopeIdPrincipalIdPrincipalIdRoleDefinitionIdRoleDefinitionIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_schedulesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id(self) -> role_schedulesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id_request_builder.RoleSchedulesdirectoryScopeIdDirectoryScopeIdAppScopeIdAppScopeIdPrincipalIdPrincipalIdRoleDefinitionIdRoleDefinitionIdRequestBuilder:
        """
        Provides operations to call the roleSchedules method.
        """
        from .role_schedulesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id import role_schedulesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id_request_builder

        return role_schedulesdirectory_scope_id_directory_scope_id_app_scope_id_app_scope_id_principal_id_principal_id_role_definition_id_role_definition_id_request_builder.RoleSchedulesdirectoryScopeIdDirectoryScopeIdAppScopeIdAppScopeIdPrincipalIdPrincipalIdRoleDefinitionIdRoleDefinitionIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_role_assignments(self) -> transitive_role_assignments_request_builder.TransitiveRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the transitiveRoleAssignments property of the microsoft.graph.rbacApplication entity.
        """
        from .transitive_role_assignments import transitive_role_assignments_request_builder

        return transitive_role_assignments_request_builder.TransitiveRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EntitlementManagementRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EntitlementManagementRequestBuilderGetQueryParameters():
        """
        The RbacApplication for Entitlement Management
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
    class EntitlementManagementRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EntitlementManagementRequestBuilder.EntitlementManagementRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EntitlementManagementRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

