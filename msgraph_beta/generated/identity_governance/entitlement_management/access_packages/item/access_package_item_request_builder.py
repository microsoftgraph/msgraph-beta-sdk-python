from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.access_package import AccessPackage
    from .....models.o_data_errors.o_data_error import ODataError
    from .access_packages_incompatible_with.access_packages_incompatible_with_request_builder import AccessPackagesIncompatibleWithRequestBuilder
    from .access_packages_incompatible_with_with_unique_name.access_packages_incompatible_with_with_unique_name_request_builder import AccessPackagesIncompatibleWithWithUniqueNameRequestBuilder
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
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AccessPackageItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackages/{accessPackage%2Did}{?%24expand,%24select}", path_parameters)
    
    def access_packages_incompatible_with_with_unique_name(self,unique_name: str) -> AccessPackagesIncompatibleWithWithUniqueNameRequestBuilder:
        """
        Provides operations to manage the accessPackagesIncompatibleWith property of the microsoft.graph.accessPackage entity.
        param unique_name: Alternate key of accessPackage
        Returns: AccessPackagesIncompatibleWithWithUniqueNameRequestBuilder
        """
        if unique_name is None:
            raise TypeError("unique_name cannot be null.")
        from .access_packages_incompatible_with_with_unique_name.access_packages_incompatible_with_with_unique_name_request_builder import AccessPackagesIncompatibleWithWithUniqueNameRequestBuilder

        return AccessPackagesIncompatibleWithWithUniqueNameRequestBuilder(self.request_adapter, self.path_parameters, unique_name)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete an accessPackage object. You can't delete an access package if it has any accessPackageAssignment. To delete the access package, first query if there are any assignments with a filter to indicate the specific access package, such as: $filter=accessPackage/id eq 'a914b616-e04e-476b-aa37-91038f0b165b'. For more information on how to remove assignments that are still in the delivered state, see Remove an assignment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/accesspackage-delete?view=graph-rest-beta
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AccessPackageItemRequestBuilderGetQueryParameters]] = None) -> Optional[AccessPackage]:
        """
        Retrieve the properties and relationships of an accessPackage object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackage]
        Find more info here: https://learn.microsoft.com/graph/api/accesspackage-get?view=graph-rest-beta
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package import AccessPackage

        return await self.request_adapter.send_async(request_info, AccessPackage, error_mapping)
    
    async def patch(self,body: AccessPackage, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AccessPackage]:
        """
        Update an existing accessPackage object to change one or more of its properties, such as the display name or description.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackage]
        Find more info here: https://learn.microsoft.com/graph/api/accesspackage-update?view=graph-rest-beta
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package import AccessPackage

        return await self.request_adapter.send_async(request_info, AccessPackage, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete an accessPackage object. You can't delete an access package if it has any accessPackageAssignment. To delete the access package, first query if there are any assignments with a filter to indicate the specific access package, such as: $filter=accessPackage/id eq 'a914b616-e04e-476b-aa37-91038f0b165b'. For more information on how to remove assignments that are still in the delivered state, see Remove an assignment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AccessPackageItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of an accessPackage object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: AccessPackage, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update an existing accessPackage object to change one or more of its properties, such as the display name or description.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> AccessPackageItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AccessPackageItemRequestBuilder
        """
        if raw_url is None:
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
    
    @dataclass
    class AccessPackageItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AccessPackageItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of an accessPackage object.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class AccessPackageItemRequestBuilderGetRequestConfiguration(RequestConfiguration[AccessPackageItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AccessPackageItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

