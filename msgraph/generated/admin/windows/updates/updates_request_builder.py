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
    from ....models import admin_windows_updates
    from ....models.o_data_errors import o_data_error
    from .catalog import catalog_request_builder
    from .deployment_audiences import deployment_audiences_request_builder
    from .deployment_audiences.item import deployment_audience_item_request_builder
    from .deployments import deployments_request_builder
    from .deployments.item import deployment_item_request_builder
    from .resource_connections import resource_connections_request_builder
    from .resource_connections.item import resource_connection_item_request_builder
    from .updatable_assets import updatable_assets_request_builder
    from .updatable_assets.item import updatable_asset_item_request_builder
    from .update_policies import update_policies_request_builder
    from .update_policies.item import update_policy_item_request_builder

class UpdatesRequestBuilder():
    """
    Provides operations to manage the updates property of the microsoft.graph.adminWindows entity.
    """
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
    
    async def delete(self,request_configuration: Optional[UpdatesRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property updates for admin
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def deployment_audiences_by_id(self,id: str) -> deployment_audience_item_request_builder.DeploymentAudienceItemRequestBuilder:
        """
        Provides operations to manage the deploymentAudiences property of the microsoft.graph.adminWindowsUpdates entity.
        Args:
            id: Unique identifier of the item
        Returns: deployment_audience_item_request_builder.DeploymentAudienceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .deployment_audiences.item import deployment_audience_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deploymentAudience%2Did"] = id
        return deployment_audience_item_request_builder.DeploymentAudienceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def deployments_by_id(self,id: str) -> deployment_item_request_builder.DeploymentItemRequestBuilder:
        """
        Provides operations to manage the deployments property of the microsoft.graph.adminWindowsUpdates entity.
        Args:
            id: Unique identifier of the item
        Returns: deployment_item_request_builder.DeploymentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .deployments.item import deployment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deployment%2Did"] = id
        return deployment_item_request_builder.DeploymentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[UpdatesRequestBuilderGetRequestConfiguration] = None) -> Optional[admin_windows_updates.AdminWindowsUpdates]:
        """
        Entity that acts as a container for all Windows Update for Business deployment service functionalities. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[admin_windows_updates.AdminWindowsUpdates]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import admin_windows_updates

        return await self.request_adapter.send_async(request_info, admin_windows_updates.AdminWindowsUpdates, error_mapping)
    
    async def patch(self,body: Optional[admin_windows_updates.AdminWindowsUpdates] = None, request_configuration: Optional[UpdatesRequestBuilderPatchRequestConfiguration] = None) -> Optional[admin_windows_updates.AdminWindowsUpdates]:
        """
        Update the navigation property updates in admin
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[admin_windows_updates.AdminWindowsUpdates]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import admin_windows_updates

        return await self.request_adapter.send_async(request_info, admin_windows_updates.AdminWindowsUpdates, error_mapping)
    
    def resource_connections_by_id(self,id: str) -> resource_connection_item_request_builder.ResourceConnectionItemRequestBuilder:
        """
        Provides operations to manage the resourceConnections property of the microsoft.graph.adminWindowsUpdates entity.
        Args:
            id: Unique identifier of the item
        Returns: resource_connection_item_request_builder.ResourceConnectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .resource_connections.item import resource_connection_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["resourceConnection%2Did"] = id
        return resource_connection_item_request_builder.ResourceConnectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[UpdatesRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
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
    
    def to_get_request_information(self,request_configuration: Optional[UpdatesRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Entity that acts as a container for all Windows Update for Business deployment service functionalities. Read-only.
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
    
    def to_patch_request_information(self,body: Optional[admin_windows_updates.AdminWindowsUpdates] = None, request_configuration: Optional[UpdatesRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def updatable_assets_by_id(self,id: str) -> updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder:
        """
        Provides operations to manage the updatableAssets property of the microsoft.graph.adminWindowsUpdates entity.
        Args:
            id: Unique identifier of the item
        Returns: updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .updatable_assets.item import updatable_asset_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["updatableAsset%2Did"] = id
        return updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def update_policies_by_id(self,id: str) -> update_policy_item_request_builder.UpdatePolicyItemRequestBuilder:
        """
        Provides operations to manage the updatePolicies property of the microsoft.graph.adminWindowsUpdates entity.
        Args:
            id: Unique identifier of the item
        Returns: update_policy_item_request_builder.UpdatePolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .update_policies.item import update_policy_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["updatePolicy%2Did"] = id
        return update_policy_item_request_builder.UpdatePolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def catalog(self) -> catalog_request_builder.CatalogRequestBuilder:
        """
        Provides operations to manage the catalog property of the microsoft.graph.adminWindowsUpdates entity.
        """
        from .catalog import catalog_request_builder

        return catalog_request_builder.CatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deployment_audiences(self) -> deployment_audiences_request_builder.DeploymentAudiencesRequestBuilder:
        """
        Provides operations to manage the deploymentAudiences property of the microsoft.graph.adminWindowsUpdates entity.
        """
        from .deployment_audiences import deployment_audiences_request_builder

        return deployment_audiences_request_builder.DeploymentAudiencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deployments(self) -> deployments_request_builder.DeploymentsRequestBuilder:
        """
        Provides operations to manage the deployments property of the microsoft.graph.adminWindowsUpdates entity.
        """
        from .deployments import deployments_request_builder

        return deployments_request_builder.DeploymentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_connections(self) -> resource_connections_request_builder.ResourceConnectionsRequestBuilder:
        """
        Provides operations to manage the resourceConnections property of the microsoft.graph.adminWindowsUpdates entity.
        """
        from .resource_connections import resource_connections_request_builder

        return resource_connections_request_builder.ResourceConnectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def updatable_assets(self) -> updatable_assets_request_builder.UpdatableAssetsRequestBuilder:
        """
        Provides operations to manage the updatableAssets property of the microsoft.graph.adminWindowsUpdates entity.
        """
        from .updatable_assets import updatable_assets_request_builder

        return updatable_assets_request_builder.UpdatableAssetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_policies(self) -> update_policies_request_builder.UpdatePoliciesRequestBuilder:
        """
        Provides operations to manage the updatePolicies property of the microsoft.graph.adminWindowsUpdates entity.
        """
        from .update_policies import update_policies_request_builder

        return update_policies_request_builder.UpdatePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class UpdatesRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UpdatesRequestBuilderGetQueryParameters():
        """
        Entity that acts as a container for all Windows Update for Business deployment service functionalities. Read-only.
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
    class UpdatesRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

