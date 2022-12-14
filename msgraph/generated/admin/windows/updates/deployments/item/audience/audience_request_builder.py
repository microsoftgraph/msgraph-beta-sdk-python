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

exclusions_request_builder = lazy_import('msgraph.generated.admin.windows.updates.deployments.item.audience.exclusions.exclusions_request_builder')
updatable_asset_item_request_builder = lazy_import('msgraph.generated.admin.windows.updates.deployments.item.audience.exclusions.item.updatable_asset_item_request_builder')
members_request_builder = lazy_import('msgraph.generated.admin.windows.updates.deployments.item.audience.members.members_request_builder')
updatable_asset_item_request_builder = lazy_import('msgraph.generated.admin.windows.updates.deployments.item.audience.members.item.updatable_asset_item_request_builder')
update_audience_request_builder = lazy_import('msgraph.generated.admin.windows.updates.deployments.item.audience.update_audience.update_audience_request_builder')
update_audience_by_id_request_builder = lazy_import('msgraph.generated.admin.windows.updates.deployments.item.audience.update_audience_by_id.update_audience_by_id_request_builder')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
deployment_audience = lazy_import('msgraph.generated.models.windows_updates.deployment_audience')

class AudienceRequestBuilder():
    """
    Provides operations to manage the audience property of the microsoft.graph.windowsUpdates.deployment entity.
    """
    @property
    def exclusions(self) -> exclusions_request_builder.ExclusionsRequestBuilder:
        """
        Provides operations to manage the exclusions property of the microsoft.graph.windowsUpdates.deploymentAudience entity.
        """
        return exclusions_request_builder.ExclusionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> members_request_builder.MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.windowsUpdates.deploymentAudience entity.
        """
        return members_request_builder.MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_audience(self) -> update_audience_request_builder.UpdateAudienceRequestBuilder:
        """
        Provides operations to call the updateAudience method.
        """
        return update_audience_request_builder.UpdateAudienceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_audience_by_id(self) -> update_audience_by_id_request_builder.UpdateAudienceByIdRequestBuilder:
        """
        Provides operations to call the updateAudienceById method.
        """
        return update_audience_by_id_request_builder.UpdateAudienceByIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AudienceRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/admin/windows/updates/deployments/{deployment%2Did}/audience{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[AudienceRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property audience for admin
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
    
    def create_get_request_information(self,request_configuration: Optional[AudienceRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Specifies the audience to which content is deployed.
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
    
    def create_patch_request_information(self,body: Optional[deployment_audience.DeploymentAudience] = None, request_configuration: Optional[AudienceRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property audience in admin
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
    
    async def delete(self,request_configuration: Optional[AudienceRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property audience for admin
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
    
    def exclusions_by_id(self,id: str) -> updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder:
        """
        Provides operations to manage the exclusions property of the microsoft.graph.windowsUpdates.deploymentAudience entity.
        Args:
            id: Unique identifier of the item
        Returns: updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["updatableAsset%2Did"] = id
        return updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[AudienceRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[deployment_audience.DeploymentAudience]:
        """
        Specifies the audience to which content is deployed.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[deployment_audience.DeploymentAudience]
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
        return await self.request_adapter.send_async(request_info, deployment_audience.DeploymentAudience, response_handler, error_mapping)
    
    def members_by_id(self,id: str) -> updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.windowsUpdates.deploymentAudience entity.
        Args:
            id: Unique identifier of the item
        Returns: updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["updatableAsset%2Did"] = id
        return updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[deployment_audience.DeploymentAudience] = None, request_configuration: Optional[AudienceRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[deployment_audience.DeploymentAudience]:
        """
        Update the navigation property audience in admin
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[deployment_audience.DeploymentAudience]
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
        return await self.request_adapter.send_async(request_info, deployment_audience.DeploymentAudience, response_handler, error_mapping)
    
    @dataclass
    class AudienceRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AudienceRequestBuilderGetQueryParameters():
        """
        Specifies the audience to which content is deployed.
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
    class AudienceRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AudienceRequestBuilder.AudienceRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AudienceRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

