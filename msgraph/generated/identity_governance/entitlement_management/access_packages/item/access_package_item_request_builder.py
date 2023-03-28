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
    from .....models import access_package
    from .....models.o_data_errors import o_data_error
    from .access_package_assignment_policies import access_package_assignment_policies_request_builder
    from .access_package_assignment_policies.item import access_package_assignment_policy_item_request_builder
    from .access_package_catalog import access_package_catalog_request_builder
    from .access_package_resource_role_scopes import access_package_resource_role_scopes_request_builder
    from .access_package_resource_role_scopes.item import access_package_resource_role_scope_item_request_builder
    from .access_packages_incompatible_with import access_packages_incompatible_with_request_builder
    from .access_packages_incompatible_with.item import access_package_item_request_builder
    from .get_applicable_policy_requirements import get_applicable_policy_requirements_request_builder
    from .incompatible_access_packages import incompatible_access_packages_request_builder
    from .incompatible_access_packages.item import access_package_item_request_builder
    from .incompatible_groups import incompatible_groups_request_builder
    from .incompatible_groups.item import group_item_request_builder
    from .move_to_catalog import move_to_catalog_request_builder

class AccessPackageItemRequestBuilder():
    """
    Provides operations to manage the accessPackages property of the microsoft.graph.entitlementManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessPackageItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/entitlementManagement/accessPackages/{accessPackage%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def access_package_assignment_policies_by_id(self,id: str) -> access_package_assignment_policy_item_request_builder.AccessPackageAssignmentPolicyItemRequestBuilder:
        """
        Provides operations to manage the accessPackageAssignmentPolicies property of the microsoft.graph.accessPackage entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_assignment_policy_item_request_builder.AccessPackageAssignmentPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .access_package_assignment_policies.item import access_package_assignment_policy_item_request_builder

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
        from .access_package_resource_role_scopes.item import access_package_resource_role_scope_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageResourceRoleScope%2Did"] = id
        return access_package_resource_role_scope_item_request_builder.AccessPackageResourceRoleScopeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def access_packages_incompatible_with_by_id(self,id: str) -> AccessPackageItemRequestBuilder:
        """
        Provides operations to manage the accessPackagesIncompatibleWith property of the microsoft.graph.accessPackage entity.
        Args:
            id: Unique identifier of the item
        Returns: AccessPackageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .access_packages_incompatible_with.item import access_package_item_request_builder
        from .incompatible_access_packages.item import access_package_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackage%2Did1"] = id
        return AccessPackageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[AccessPackageItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property accessPackages for identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AccessPackageItemRequestBuilderGetRequestConfiguration] = None) -> Optional[access_package.AccessPackage]:
        """
        Represents access package objects.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[access_package.AccessPackage]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import access_package

        return await self.request_adapter.send_async(request_info, access_package.AccessPackage, error_mapping)
    
    def incompatible_access_packages_by_id(self,id: str) -> AccessPackageItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.identityGovernance.entitlementManagement.accessPackages.item.incompatibleAccessPackages.item collection
        Args:
            id: Unique identifier of the item
        Returns: AccessPackageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .access_packages_incompatible_with.item import access_package_item_request_builder
        from .incompatible_access_packages.item import access_package_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackage%2Did1"] = id
        return AccessPackageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def incompatible_groups_by_id(self,id: str) -> group_item_request_builder.GroupItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.identityGovernance.entitlementManagement.accessPackages.item.incompatibleGroups.item collection
        Args:
            id: Unique identifier of the item
        Returns: group_item_request_builder.GroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .incompatible_groups.item import group_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["group%2Did"] = id
        return group_item_request_builder.GroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[access_package.AccessPackage] = None, request_configuration: Optional[AccessPackageItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[access_package.AccessPackage]:
        """
        Update the navigation property accessPackages in identityGovernance
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
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import access_package

        return await self.request_adapter.send_async(request_info, access_package.AccessPackage, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessPackageItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property accessPackages for identityGovernance
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
    
    def to_get_request_information(self,request_configuration: Optional[AccessPackageItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents access package objects.
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
    
    def to_patch_request_information(self,body: Optional[access_package.AccessPackage] = None, request_configuration: Optional[AccessPackageItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property accessPackages in identityGovernance
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
    def access_package_assignment_policies(self) -> access_package_assignment_policies_request_builder.AccessPackageAssignmentPoliciesRequestBuilder:
        """
        Provides operations to manage the accessPackageAssignmentPolicies property of the microsoft.graph.accessPackage entity.
        """
        from .access_package_assignment_policies import access_package_assignment_policies_request_builder

        return access_package_assignment_policies_request_builder.AccessPackageAssignmentPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_package_catalog(self) -> access_package_catalog_request_builder.AccessPackageCatalogRequestBuilder:
        """
        Provides operations to manage the accessPackageCatalog property of the microsoft.graph.accessPackage entity.
        """
        from .access_package_catalog import access_package_catalog_request_builder

        return access_package_catalog_request_builder.AccessPackageCatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_package_resource_role_scopes(self) -> access_package_resource_role_scopes_request_builder.AccessPackageResourceRoleScopesRequestBuilder:
        """
        Provides operations to manage the accessPackageResourceRoleScopes property of the microsoft.graph.accessPackage entity.
        """
        from .access_package_resource_role_scopes import access_package_resource_role_scopes_request_builder

        return access_package_resource_role_scopes_request_builder.AccessPackageResourceRoleScopesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_packages_incompatible_with(self) -> access_packages_incompatible_with_request_builder.AccessPackagesIncompatibleWithRequestBuilder:
        """
        Provides operations to manage the accessPackagesIncompatibleWith property of the microsoft.graph.accessPackage entity.
        """
        from .access_packages_incompatible_with import access_packages_incompatible_with_request_builder

        return access_packages_incompatible_with_request_builder.AccessPackagesIncompatibleWithRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_applicable_policy_requirements(self) -> get_applicable_policy_requirements_request_builder.GetApplicablePolicyRequirementsRequestBuilder:
        """
        Provides operations to call the getApplicablePolicyRequirements method.
        """
        from .get_applicable_policy_requirements import get_applicable_policy_requirements_request_builder

        return get_applicable_policy_requirements_request_builder.GetApplicablePolicyRequirementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incompatible_access_packages(self) -> incompatible_access_packages_request_builder.IncompatibleAccessPackagesRequestBuilder:
        """
        Provides operations to manage the incompatibleAccessPackages property of the microsoft.graph.accessPackage entity.
        """
        from .incompatible_access_packages import incompatible_access_packages_request_builder

        return incompatible_access_packages_request_builder.IncompatibleAccessPackagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incompatible_groups(self) -> incompatible_groups_request_builder.IncompatibleGroupsRequestBuilder:
        """
        Provides operations to manage the incompatibleGroups property of the microsoft.graph.accessPackage entity.
        """
        from .incompatible_groups import incompatible_groups_request_builder

        return incompatible_groups_request_builder.IncompatibleGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def move_to_catalog(self) -> move_to_catalog_request_builder.MoveToCatalogRequestBuilder:
        """
        Provides operations to call the moveToCatalog method.
        """
        from .move_to_catalog import move_to_catalog_request_builder

        return move_to_catalog_request_builder.MoveToCatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AccessPackageItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AccessPackageItemRequestBuilderGetQueryParameters():
        """
        Represents access package objects.
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
    class AccessPackageItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AccessPackageItemRequestBuilder.AccessPackageItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AccessPackageItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

