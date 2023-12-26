from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.access_package import AccessPackage
    from .....models.o_data_errors.o_data_error import ODataError
    from .access_packages_incompatible_with.access_packages_incompatible_with_request_builder import AccessPackagesIncompatibleWithRequestBuilder
    from .access_package_assignment_policies.access_package_assignment_policies_request_builder import AccessPackageAssignmentPoliciesRequestBuilder
    from .access_package_catalog.access_package_catalog_request_builder import AccessPackageCatalogRequestBuilder
    from .access_package_resource_role_scopes.access_package_resource_role_scopes_request_builder import AccessPackageResourceRoleScopesRequestBuilder
    from .get_applicable_policy_requirements.get_applicable_policy_requirements_request_builder import GetApplicablePolicyRequirementsRequestBuilder
    from .incompatible_access_packages.incompatible_access_packages_request_builder import IncompatibleAccessPackagesRequestBuilder
    from .incompatible_groups.incompatible_groups_request_builder import IncompatibleGroupsRequestBuilder
    from .move_to_catalog.move_to_catalog_request_builder import MoveToCatalogRequestBuilder

class AccessPackageItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the accessPackages property of the microsoft.graph.entitlementManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessPackageItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackages/{accessPackage%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[AccessPackageItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete an accessPackage object. You can't delete an access package if it has any accessPackageAssignment. To delete the access package, first query if there are any assignments with a filter to indicate the specific access package, such as: $filter=accessPackage/id eq 'a914b616-e04e-476b-aa37-91038f0b165b'. For more information on how to remove assignments that are still in the delivered state, see Remove an assignment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/accesspackage-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AccessPackageItemRequestBuilderGetRequestConfiguration] = None) -> Optional[AccessPackage]:
        """
        Retrieve an access package with a list of accessPackageResourceRoleScope objects. These objects represent the resource roles that an access package assigns to each subject. Each object links to an accessPackageResourceRole and an accessPackageResourceScope.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackage]
        Find more info here: https://learn.microsoft.com/graph/api/accesspackage-list-accesspackageresourcerolescopes?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package import AccessPackage

        return await self.request_adapter.send_async(request_info, AccessPackage, error_mapping)
    
    async def patch(self,body: Optional[AccessPackage] = None, request_configuration: Optional[AccessPackageItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[AccessPackage]:
        """
        Update an existing accessPackage object to change one or more of its properties, such as the display name or description.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackage]
        Find more info here: https://learn.microsoft.com/graph/api/accesspackage-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package import AccessPackage

        return await self.request_adapter.send_async(request_info, AccessPackage, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessPackageItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete an accessPackage object. You can't delete an access package if it has any accessPackageAssignment. To delete the access package, first query if there are any assignments with a filter to indicate the specific access package, such as: $filter=accessPackage/id eq 'a914b616-e04e-476b-aa37-91038f0b165b'. For more information on how to remove assignments that are still in the delivered state, see Remove an assignment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[AccessPackageItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve an access package with a list of accessPackageResourceRoleScope objects. These objects represent the resource roles that an access package assigns to each subject. Each object links to an accessPackageResourceRole and an accessPackageResourceScope.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[AccessPackage] = None, request_configuration: Optional[AccessPackageItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update an existing accessPackage object to change one or more of its properties, such as the display name or description.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> AccessPackageItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AccessPackageItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AccessPackageItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def access_package_assignment_policies(self) -> AccessPackageAssignmentPoliciesRequestBuilder:
        """
        Provides operations to manage the accessPackageAssignmentPolicies property of the microsoft.graph.accessPackage entity.
        """
        from .access_package_assignment_policies.access_package_assignment_policies_request_builder import AccessPackageAssignmentPoliciesRequestBuilder

        return AccessPackageAssignmentPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_package_catalog(self) -> AccessPackageCatalogRequestBuilder:
        """
        Provides operations to manage the accessPackageCatalog property of the microsoft.graph.accessPackage entity.
        """
        from .access_package_catalog.access_package_catalog_request_builder import AccessPackageCatalogRequestBuilder

        return AccessPackageCatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_package_resource_role_scopes(self) -> AccessPackageResourceRoleScopesRequestBuilder:
        """
        Provides operations to manage the accessPackageResourceRoleScopes property of the microsoft.graph.accessPackage entity.
        """
        from .access_package_resource_role_scopes.access_package_resource_role_scopes_request_builder import AccessPackageResourceRoleScopesRequestBuilder

        return AccessPackageResourceRoleScopesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_packages_incompatible_with(self) -> AccessPackagesIncompatibleWithRequestBuilder:
        """
        Provides operations to manage the accessPackagesIncompatibleWith property of the microsoft.graph.accessPackage entity.
        """
        from .access_packages_incompatible_with.access_packages_incompatible_with_request_builder import AccessPackagesIncompatibleWithRequestBuilder

        return AccessPackagesIncompatibleWithRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_applicable_policy_requirements(self) -> GetApplicablePolicyRequirementsRequestBuilder:
        """
        Provides operations to call the getApplicablePolicyRequirements method.
        """
        from .get_applicable_policy_requirements.get_applicable_policy_requirements_request_builder import GetApplicablePolicyRequirementsRequestBuilder

        return GetApplicablePolicyRequirementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incompatible_access_packages(self) -> IncompatibleAccessPackagesRequestBuilder:
        """
        Provides operations to manage the incompatibleAccessPackages property of the microsoft.graph.accessPackage entity.
        """
        from .incompatible_access_packages.incompatible_access_packages_request_builder import IncompatibleAccessPackagesRequestBuilder

        return IncompatibleAccessPackagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incompatible_groups(self) -> IncompatibleGroupsRequestBuilder:
        """
        Provides operations to manage the incompatibleGroups property of the microsoft.graph.accessPackage entity.
        """
        from .incompatible_groups.incompatible_groups_request_builder import IncompatibleGroupsRequestBuilder

        return IncompatibleGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def move_to_catalog(self) -> MoveToCatalogRequestBuilder:
        """
        Provides operations to call the moveToCatalog method.
        """
        from .move_to_catalog.move_to_catalog_request_builder import MoveToCatalogRequestBuilder

        return MoveToCatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessPackageItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class AccessPackageItemRequestBuilderGetQueryParameters():
        """
        Retrieve an access package with a list of accessPackageResourceRoleScope objects. These objects represent the resource roles that an access package assigns to each subject. Each object links to an accessPackageResourceRole and an accessPackageResourceScope.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessPackageItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AccessPackageItemRequestBuilder.AccessPackageItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessPackageItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

