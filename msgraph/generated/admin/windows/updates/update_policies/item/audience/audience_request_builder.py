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
    from .......models.o_data_errors import o_data_error
    from .......models.windows_updates import deployment_audience
    from .exclusions import exclusions_request_builder
    from .exclusions.item import updatable_asset_item_request_builder
    from .members import members_request_builder
    from .members.item import updatable_asset_item_request_builder
    from .windows_updates_update_audience import windows_updates_update_audience_request_builder
    from .windows_updates_update_audience_by_id import windows_updates_update_audience_by_id_request_builder

class AudienceRequestBuilder():
    """
    Provides operations to manage the audience property of the microsoft.graph.windowsUpdates.updatePolicy entity.
    """
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
        self.url_template: str = "{+baseurl}/admin/windows/updates/updatePolicies/{updatePolicy%2Did}/audience{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[AudienceRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property audience for admin
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def exclusions_by_id(self,id: str) -> updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder:
        """
        Provides operations to manage the exclusions property of the microsoft.graph.windowsUpdates.deploymentAudience entity.
        Args:
            id: Unique identifier of the item
        Returns: updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .exclusions.item import updatable_asset_item_request_builder
        from .members.item import updatable_asset_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["updatableAsset%2Did"] = id
        return updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[AudienceRequestBuilderGetRequestConfiguration] = None) -> Optional[deployment_audience.DeploymentAudience]:
        """
        Specifies the audience to target.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[deployment_audience.DeploymentAudience]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.windows_updates import deployment_audience

        return await self.request_adapter.send_async(request_info, deployment_audience.DeploymentAudience, error_mapping)
    
    def members_by_id(self,id: str) -> updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.windowsUpdates.deploymentAudience entity.
        Args:
            id: Unique identifier of the item
        Returns: updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .exclusions.item import updatable_asset_item_request_builder
        from .members.item import updatable_asset_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["updatableAsset%2Did"] = id
        return updatable_asset_item_request_builder.UpdatableAssetItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[deployment_audience.DeploymentAudience] = None, request_configuration: Optional[AudienceRequestBuilderPatchRequestConfiguration] = None) -> Optional[deployment_audience.DeploymentAudience]:
        """
        Update the navigation property audience in admin
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[deployment_audience.DeploymentAudience]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.windows_updates import deployment_audience

        return await self.request_adapter.send_async(request_info, deployment_audience.DeploymentAudience, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AudienceRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
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
    
    def to_get_request_information(self,request_configuration: Optional[AudienceRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Specifies the audience to target.
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
    
    def to_patch_request_information(self,body: Optional[deployment_audience.DeploymentAudience] = None, request_configuration: Optional[AudienceRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def exclusions(self) -> exclusions_request_builder.ExclusionsRequestBuilder:
        """
        Provides operations to manage the exclusions property of the microsoft.graph.windowsUpdates.deploymentAudience entity.
        """
        from .exclusions import exclusions_request_builder

        return exclusions_request_builder.ExclusionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> members_request_builder.MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.windowsUpdates.deploymentAudience entity.
        """
        from .members import members_request_builder

        return members_request_builder.MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_updates_update_audience(self) -> windows_updates_update_audience_request_builder.WindowsUpdatesUpdateAudienceRequestBuilder:
        """
        Provides operations to call the updateAudience method.
        """
        from .windows_updates_update_audience import windows_updates_update_audience_request_builder

        return windows_updates_update_audience_request_builder.WindowsUpdatesUpdateAudienceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_updates_update_audience_by_id(self) -> windows_updates_update_audience_by_id_request_builder.WindowsUpdatesUpdateAudienceByIdRequestBuilder:
        """
        Provides operations to call the updateAudienceById method.
        """
        from .windows_updates_update_audience_by_id import windows_updates_update_audience_by_id_request_builder

        return windows_updates_update_audience_by_id_request_builder.WindowsUpdatesUpdateAudienceByIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AudienceRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AudienceRequestBuilderGetQueryParameters():
        """
        Specifies the audience to target.
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
    class AudienceRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

