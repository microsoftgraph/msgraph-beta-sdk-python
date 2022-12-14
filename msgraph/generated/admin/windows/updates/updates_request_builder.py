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

catalog_request_builder = lazy_import('msgraph.generated.admin.windows.updates.catalog.catalog_request_builder')
deployments_request_builder = lazy_import('msgraph.generated.admin.windows.updates.deployments.deployments_request_builder')
deployment_item_request_builder = lazy_import('msgraph.generated.admin.windows.updates.deployments.item.deployment_item_request_builder')
resource_connections_request_builder = lazy_import('msgraph.generated.admin.windows.updates.resource_connections.resource_connections_request_builder')
resource_connection_item_request_builder = lazy_import('msgraph.generated.admin.windows.updates.resource_connections.item.resource_connection_item_request_builder')
updatable_assets_request_builder = lazy_import('msgraph.generated.admin.windows.updates.updatable_assets.updatable_assets_request_builder')
updatable_asset_item_request_builder = lazy_import('msgraph.generated.admin.windows.updates.updatable_assets.item.updatable_asset_item_request_builder')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
updates = lazy_import('msgraph.generated.models.windows_updates.updates')

class UpdatesRequestBuilder():
    """
    Provides operations to manage the updates property of the microsoft.graph.windowsUpdates.windows entity.
    """
    @property
    def catalog(self) -> catalog_request_builder.CatalogRequestBuilder:
        """
        Provides operations to manage the catalog property of the microsoft.graph.windowsUpdates.updates entity.
        """
        return catalog_request_builder.CatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deployments(self) -> deployments_request_builder.DeploymentsRequestBuilder:
        """
        Provides operations to manage the deployments property of the microsoft.graph.windowsUpdates.updates entity.
        """
        return deployments_request_builder.DeploymentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_connections(self) -> resource_connections_request_builder.ResourceConnectionsRequestBuilder:
        """
        Provides operations to manage the resourceConnections property of the microsoft.graph.windowsUpdates.updates entity.
        """
        return resource_connections_request_builder.ResourceConnectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def updatable_assets(self) -> updatable_assets_request_builder.UpdatableAssetsRequestBuilder:
        """
        Provides operations to manage the updatableAssets property of the microsoft.graph.windowsUpdates.updates entity.
        """
        return updatable_assets_request_builder.UpdatableAssetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UpdatesRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/admin/windows/updates{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[UpdatesRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property updates for admin
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
    
    def create_get_request_information(self,request_configuration: Optional[UpdatesRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Entity that acts as a container for the functionality of the Windows Update for Business deployment service. Read-only.
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
    
    def create_patch_request_information(self,body: Optional[updates.Updates] = None, request_configuration: Optional[UpdatesRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property updates in admin
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
    
    async def delete(self,request_configuration: Optional[UpdatesRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property updates for admin
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
    
    def deployments_by_id(self,id: str) -> deployment_item_request_builder.DeploymentItemRequestBuilder:
        """
        Provides operations to manage the deployments property of the microsoft.graph.windowsUpdates.updates entity.
        Args:
            id: Unique identifier of the item
        Returns: deployment_item_request_builder.DeploymentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deployment%2Did"] = id
        return deployment_item_request_builder.DeploymentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[UpdatesRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[updates.Updates]:
        """
        Entity that acts as a container for the functionality of the Windows Update for Business deployment service. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[updates.Updates]
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
        return await self.request_adapter.send_async(request_info, updates.Updates, response_handler, error_mapping)
    
    async def patch(self,body: Optional[updates.Updates] = None, request_configuration: Optional[UpdatesRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[updates.Updates]:
        """
        Update the navigation property updates in admin
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[updates.Updates]
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
        return await self.request_adapter.send_async(request_info, updates.Updates, response_handler, error_mapping)
    
    def resource_connections_by_id(self,id: str) -> resource_connection_item_request_builder.ResourceConnectionItemRequestBuilder:
        """
        Provides operations to manage the resourceConnections property of the microsoft.graph.windowsUpdates.updates entity.
        Args:
            id: Unique identifier of the item
        Returns: resource_connection_item_request_builder.ResourceConnectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["resourceConnection%2Did"] = id
        return resource_connection_item_request_builder.ResourceConnectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def updatable_assets_by_id(self,id: str) -> updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder:
        """
        Provides operations to manage the updatableAssets property of the microsoft.graph.windowsUpdates.updates entity.
        Args:
            id: Unique identifier of the item
        Returns: updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["updatableAsset%2Did"] = id
        return updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class UpdatesRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UpdatesRequestBuilderGetQueryParameters():
        """
        Entity that acts as a container for the functionality of the Windows Update for Business deployment service. Read-only.
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
    class UpdatesRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UpdatesRequestBuilder.UpdatesRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UpdatesRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

