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
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.unified_rbac_application import UnifiedRbacApplication
    from .custom_app_scopes.custom_app_scopes_request_builder import CustomAppScopesRequestBuilder
    from .resource_namespaces.resource_namespaces_request_builder import ResourceNamespacesRequestBuilder
    from .role_assignments.role_assignments_request_builder import RoleAssignmentsRequestBuilder
    from .role_definitions.role_definitions_request_builder import RoleDefinitionsRequestBuilder
    from .transitive_role_assignments.transitive_role_assignments_request_builder import TransitiveRoleAssignmentsRequestBuilder

class ExchangeRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the exchange property of the microsoft.graph.roleManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ExchangeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/roleManagement/exchange{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property exchange for roleManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ExchangeRequestBuilderGetQueryParameters]] = None) -> Optional[UnifiedRbacApplication]:
        """
        Get exchange from roleManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnifiedRbacApplication]
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.unified_rbac_application import UnifiedRbacApplication

        return await self.request_adapter.send_async(request_info, UnifiedRbacApplication, error_mapping)
    
    async def patch(self,body: UnifiedRbacApplication, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[UnifiedRbacApplication]:
        """
        Update the navigation property exchange in roleManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnifiedRbacApplication]
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.unified_rbac_application import UnifiedRbacApplication

        return await self.request_adapter.send_async(request_info, UnifiedRbacApplication, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property exchange for roleManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ExchangeRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get exchange from roleManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: UnifiedRbacApplication, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property exchange in roleManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ExchangeRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ExchangeRequestBuilder
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ExchangeRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def custom_app_scopes(self) -> CustomAppScopesRequestBuilder:
        """
        Provides operations to manage the customAppScopes property of the microsoft.graph.unifiedRbacApplication entity.
        """
        from .custom_app_scopes.custom_app_scopes_request_builder import CustomAppScopesRequestBuilder

        return CustomAppScopesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_namespaces(self) -> ResourceNamespacesRequestBuilder:
        """
        Provides operations to manage the resourceNamespaces property of the microsoft.graph.unifiedRbacApplication entity.
        """
        from .resource_namespaces.resource_namespaces_request_builder import ResourceNamespacesRequestBuilder

        return ResourceNamespacesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignments(self) -> RoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.unifiedRbacApplication entity.
        """
        from .role_assignments.role_assignments_request_builder import RoleAssignmentsRequestBuilder

        return RoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definitions(self) -> RoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.unifiedRbacApplication entity.
        """
        from .role_definitions.role_definitions_request_builder import RoleDefinitionsRequestBuilder

        return RoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_role_assignments(self) -> TransitiveRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the transitiveRoleAssignments property of the microsoft.graph.unifiedRbacApplication entity.
        """
        from .transitive_role_assignments.transitive_role_assignments_request_builder import TransitiveRoleAssignmentsRequestBuilder

        return TransitiveRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ExchangeRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ExchangeRequestBuilderGetQueryParameters():
        """
        Get exchange from roleManagement
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
    class ExchangeRequestBuilderGetRequestConfiguration(RequestConfiguration[ExchangeRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ExchangeRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

