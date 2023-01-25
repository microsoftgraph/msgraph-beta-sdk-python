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

access_package_assignment_policies_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.access_package_assignment_policies.access_package_assignment_policies_request_builder')
access_package_assignment_policy_item_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.access_package_assignment_policies.item.access_package_assignment_policy_item_request_builder')
access_package_catalog_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.access_package_catalog.access_package_catalog_request_builder')
access_package_resource_role_scopes_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.access_package_resource_role_scopes.access_package_resource_role_scopes_request_builder')
access_package_resource_role_scope_item_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.access_package_resource_role_scopes.item.access_package_resource_role_scope_item_request_builder')
access_packages_incompatible_with_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.access_packages_incompatible_with.access_packages_incompatible_with_request_builder')
access_package_item_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.access_packages_incompatible_with.item.access_package_item_request_builder')
get_applicable_policy_requirements_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.get_applicable_policy_requirements.get_applicable_policy_requirements_request_builder')
incompatible_access_packages_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.incompatible_access_packages.incompatible_access_packages_request_builder')
access_package_item_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.incompatible_access_packages.item.access_package_item_request_builder')
incompatible_groups_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.incompatible_groups.incompatible_groups_request_builder')
group_item_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.incompatible_groups.item.group_item_request_builder')
move_to_catalog_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_package_assignments.item.access_package.move_to_catalog.move_to_catalog_request_builder')
access_package = lazy_import('msgraph.generated.models.access_package')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class AccessPackageRequestBuilder():
    """
    Provides operations to manage the accessPackage property of the microsoft.graph.accessPackageAssignment entity.
    """
    @property
    def access_package_assignment_policies(self) -> access_package_assignment_policies_request_builder.AccessPackageAssignmentPoliciesRequestBuilder:
        """
        Provides operations to manage the accessPackageAssignmentPolicies property of the microsoft.graph.accessPackage entity.
        """
        return access_package_assignment_policies_request_builder.AccessPackageAssignmentPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_package_catalog(self) -> access_package_catalog_request_builder.AccessPackageCatalogRequestBuilder:
        """
        Provides operations to manage the accessPackageCatalog property of the microsoft.graph.accessPackage entity.
        """
        return access_package_catalog_request_builder.AccessPackageCatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_package_resource_role_scopes(self) -> access_package_resource_role_scopes_request_builder.AccessPackageResourceRoleScopesRequestBuilder:
        """
        Provides operations to manage the accessPackageResourceRoleScopes property of the microsoft.graph.accessPackage entity.
        """
        return access_package_resource_role_scopes_request_builder.AccessPackageResourceRoleScopesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_packages_incompatible_with(self) -> access_packages_incompatible_with_request_builder.AccessPackagesIncompatibleWithRequestBuilder:
        """
        Provides operations to manage the accessPackagesIncompatibleWith property of the microsoft.graph.accessPackage entity.
        """
        return access_packages_incompatible_with_request_builder.AccessPackagesIncompatibleWithRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_applicable_policy_requirements(self) -> get_applicable_policy_requirements_request_builder.GetApplicablePolicyRequirementsRequestBuilder:
        """
        Provides operations to call the getApplicablePolicyRequirements method.
        """
        return get_applicable_policy_requirements_request_builder.GetApplicablePolicyRequirementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incompatible_access_packages(self) -> incompatible_access_packages_request_builder.IncompatibleAccessPackagesRequestBuilder:
        """
        Provides operations to manage the incompatibleAccessPackages property of the microsoft.graph.accessPackage entity.
        """
        return incompatible_access_packages_request_builder.IncompatibleAccessPackagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incompatible_groups(self) -> incompatible_groups_request_builder.IncompatibleGroupsRequestBuilder:
        """
        Provides operations to manage the incompatibleGroups property of the microsoft.graph.accessPackage entity.
        """
        return incompatible_groups_request_builder.IncompatibleGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def move_to_catalog(self) -> move_to_catalog_request_builder.MoveToCatalogRequestBuilder:
        """
        Provides operations to call the moveToCatalog method.
        """
        return move_to_catalog_request_builder.MoveToCatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    def access_package_assignment_policies_by_id(self,id: str) -> access_package_assignment_policy_item_request_builder.AccessPackageAssignmentPolicyItemRequestBuilder:
        """
        Provides operations to manage the accessPackageAssignmentPolicies property of the microsoft.graph.accessPackage entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_assignment_policy_item_request_builder.AccessPackageAssignmentPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageAssignmentPolicy%2Did"] = id
        return access_package_assignment_policy_item_request_builder.AccessPackageAssignmentPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def access_package_resource_role_scopes_by_id(self,id: str) -> access_package_resource_role_scope_item_request_builder.AccessPackageResourceRoleScopeItemRequestBuilder:
        """
        Provides operations to manage the accessPackageResourceRoleScopes property of the microsoft.graph.accessPackage entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_resource_role_scope_item_request_builder.AccessPackageResourceRoleScopeItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageResourceRoleScope%2Did"] = id
        return access_package_resource_role_scope_item_request_builder.AccessPackageResourceRoleScopeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def access_packages_incompatible_with_by_id(self,id: str) -> access_package_item_request_builder.AccessPackageItemRequestBuilder:
        """
        Provides operations to manage the accessPackagesIncompatibleWith property of the microsoft.graph.accessPackage entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_item_request_builder.AccessPackageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackage%2Did"] = id
        return access_package_item_request_builder.AccessPackageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessPackageRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/entitlementManagement/accessPackageAssignments/{accessPackageAssignment%2Did}/accessPackage{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[AccessPackageRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property accessPackage for identityGovernance
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
    
    async def get(self,request_configuration: Optional[AccessPackageRequestBuilderGetRequestConfiguration] = None) -> Optional[access_package.AccessPackage]:
        """
        Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[access_package.AccessPackage]
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
        return await self.request_adapter.send_async(request_info, access_package.AccessPackage, error_mapping)
    
    def incompatible_access_packages_by_id(self,id: str) -> access_package_item_request_builder.AccessPackageItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.identityGovernance.entitlementManagement.accessPackageAssignments.item.accessPackage.incompatibleAccessPackages.item collection
        Args:
            id: Unique identifier of the item
        Returns: access_package_item_request_builder.AccessPackageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackage%2Did"] = id
        return access_package_item_request_builder.AccessPackageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def incompatible_groups_by_id(self,id: str) -> group_item_request_builder.GroupItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.identityGovernance.entitlementManagement.accessPackageAssignments.item.accessPackage.incompatibleGroups.item collection
        Args:
            id: Unique identifier of the item
        Returns: group_item_request_builder.GroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["group%2Did"] = id
        return group_item_request_builder.GroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[access_package.AccessPackage] = None, request_configuration: Optional[AccessPackageRequestBuilderPatchRequestConfiguration] = None) -> Optional[access_package.AccessPackage]:
        """
        Update the navigation property accessPackage in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[access_package.AccessPackage]
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
        return await self.request_adapter.send_async(request_info, access_package.AccessPackage, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessPackageRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property accessPackage for identityGovernance
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
    
    def to_get_request_information(self,request_configuration: Optional[AccessPackageRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.
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
    
    def to_patch_request_information(self,body: Optional[access_package.AccessPackage] = None, request_configuration: Optional[AccessPackageRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property accessPackage in identityGovernance
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
    class AccessPackageRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AccessPackageRequestBuilderGetQueryParameters():
        """
        Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.
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
    class AccessPackageRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AccessPackageRequestBuilder.AccessPackageRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AccessPackageRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

