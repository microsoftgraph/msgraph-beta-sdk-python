from __future__ import annotations
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
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.admin_windows_updates import AdminWindowsUpdates
    from ....models.o_data_errors.o_data_error import ODataError
    from .catalog.catalog_request_builder import CatalogRequestBuilder
    from .deployments.deployments_request_builder import DeploymentsRequestBuilder
    from .deployment_audiences.deployment_audiences_request_builder import DeploymentAudiencesRequestBuilder
    from .products.products_request_builder import ProductsRequestBuilder
    from .resource_connections.resource_connections_request_builder import ResourceConnectionsRequestBuilder
    from .updatable_assets.updatable_assets_request_builder import UpdatableAssetsRequestBuilder
    from .update_policies.update_policies_request_builder import UpdatePoliciesRequestBuilder

class UpdatesRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the updates property of the microsoft.graph.adminWindows entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new UpdatesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/admin/windows/updates{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property updates for admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[UpdatesRequestBuilderGetQueryParameters]] = None) -> Optional[AdminWindowsUpdates]:
        """
        Entity that acts as a container for all Windows Update for Business deployment service functionalities. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AdminWindowsUpdates]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.admin_windows_updates import AdminWindowsUpdates

        return await self.request_adapter.send_async(request_info, AdminWindowsUpdates, error_mapping)
    
    async def patch(self,body: AdminWindowsUpdates, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AdminWindowsUpdates]:
        """
        Update the navigation property updates in admin
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AdminWindowsUpdates]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.admin_windows_updates import AdminWindowsUpdates

        return await self.request_adapter.send_async(request_info, AdminWindowsUpdates, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property updates for admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[UpdatesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Entity that acts as a container for all Windows Update for Business deployment service functionalities. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: AdminWindowsUpdates, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property updates in admin
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
    
    def with_url(self,raw_url: str) -> UpdatesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UpdatesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return UpdatesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def catalog(self) -> CatalogRequestBuilder:
        """
        Provides operations to manage the catalog property of the microsoft.graph.adminWindowsUpdates entity.
        """
        from .catalog.catalog_request_builder import CatalogRequestBuilder

        return CatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deployment_audiences(self) -> DeploymentAudiencesRequestBuilder:
        """
        Provides operations to manage the deploymentAudiences property of the microsoft.graph.adminWindowsUpdates entity.
        """
        from .deployment_audiences.deployment_audiences_request_builder import DeploymentAudiencesRequestBuilder

        return DeploymentAudiencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deployments(self) -> DeploymentsRequestBuilder:
        """
        Provides operations to manage the deployments property of the microsoft.graph.adminWindowsUpdates entity.
        """
        from .deployments.deployments_request_builder import DeploymentsRequestBuilder

        return DeploymentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def products(self) -> ProductsRequestBuilder:
        """
        Provides operations to manage the products property of the microsoft.graph.adminWindowsUpdates entity.
        """
        from .products.products_request_builder import ProductsRequestBuilder

        return ProductsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_connections(self) -> ResourceConnectionsRequestBuilder:
        """
        Provides operations to manage the resourceConnections property of the microsoft.graph.adminWindowsUpdates entity.
        """
        from .resource_connections.resource_connections_request_builder import ResourceConnectionsRequestBuilder

        return ResourceConnectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def updatable_assets(self) -> UpdatableAssetsRequestBuilder:
        """
        Provides operations to manage the updatableAssets property of the microsoft.graph.adminWindowsUpdates entity.
        """
        from .updatable_assets.updatable_assets_request_builder import UpdatableAssetsRequestBuilder

        return UpdatableAssetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_policies(self) -> UpdatePoliciesRequestBuilder:
        """
        Provides operations to manage the updatePolicies property of the microsoft.graph.adminWindowsUpdates entity.
        """
        from .update_policies.update_policies_request_builder import UpdatePoliciesRequestBuilder

        return UpdatePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class UpdatesRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class UpdatesRequestBuilderGetQueryParameters():
        """
        Entity that acts as a container for all Windows Update for Business deployment service functionalities. Read-only.
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
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class UpdatesRequestBuilderGetRequestConfiguration(RequestConfiguration[UpdatesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class UpdatesRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

