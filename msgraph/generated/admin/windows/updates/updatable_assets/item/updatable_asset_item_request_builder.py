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

add_members_request_builder = lazy_import('msgraph.generated.admin.windows.updates.updatable_assets.item.add_members.add_members_request_builder')
add_members_by_id_request_builder = lazy_import('msgraph.generated.admin.windows.updates.updatable_assets.item.add_members_by_id.add_members_by_id_request_builder')
remove_members_request_builder = lazy_import('msgraph.generated.admin.windows.updates.updatable_assets.item.remove_members.remove_members_request_builder')
remove_members_by_id_request_builder = lazy_import('msgraph.generated.admin.windows.updates.updatable_assets.item.remove_members_by_id.remove_members_by_id_request_builder')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
updatable_asset = lazy_import('msgraph.generated.models.windows_updates.updatable_asset')

class UpdatableAssetItemRequestBuilder():
    """
    Provides operations to manage the updatableAssets property of the microsoft.graph.windowsUpdates.updates entity.
    """
    @property
    def add_members(self) -> add_members_request_builder.AddMembersRequestBuilder:
        """
        Provides operations to call the addMembers method.
        """
        return add_members_request_builder.AddMembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_members_by_id(self) -> add_members_by_id_request_builder.AddMembersByIdRequestBuilder:
        """
        Provides operations to call the addMembersById method.
        """
        return add_members_by_id_request_builder.AddMembersByIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_members(self) -> remove_members_request_builder.RemoveMembersRequestBuilder:
        """
        Provides operations to call the removeMembers method.
        """
        return remove_members_request_builder.RemoveMembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_members_by_id(self) -> remove_members_by_id_request_builder.RemoveMembersByIdRequestBuilder:
        """
        Provides operations to call the removeMembersById method.
        """
        return remove_members_by_id_request_builder.RemoveMembersByIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UpdatableAssetItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/admin/windows/updates/updatableAssets/{updatableAsset%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[UpdatableAssetItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property updatableAssets for admin
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
    
    def create_get_request_information(self,request_configuration: Optional[UpdatableAssetItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Assets registered with the deployment service that can receive updates. Read-only.
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
    
    def create_patch_request_information(self,body: Optional[updatable_asset.UpdatableAsset] = None, request_configuration: Optional[UpdatableAssetItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property updatableAssets in admin
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
    
    async def delete(self,request_configuration: Optional[UpdatableAssetItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property updatableAssets for admin
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
    
    async def get(self,request_configuration: Optional[UpdatableAssetItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[updatable_asset.UpdatableAsset]:
        """
        Assets registered with the deployment service that can receive updates. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[updatable_asset.UpdatableAsset]
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
        return await self.request_adapter.send_async(request_info, updatable_asset.UpdatableAsset, response_handler, error_mapping)
    
    async def patch(self,body: Optional[updatable_asset.UpdatableAsset] = None, request_configuration: Optional[UpdatableAssetItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[updatable_asset.UpdatableAsset]:
        """
        Update the navigation property updatableAssets in admin
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[updatable_asset.UpdatableAsset]
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
        return await self.request_adapter.send_async(request_info, updatable_asset.UpdatableAsset, response_handler, error_mapping)
    
    @dataclass
    class UpdatableAssetItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UpdatableAssetItemRequestBuilderGetQueryParameters():
        """
        Assets registered with the deployment service that can receive updates. Read-only.
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
    class UpdatableAssetItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UpdatableAssetItemRequestBuilder.UpdatableAssetItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UpdatableAssetItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

