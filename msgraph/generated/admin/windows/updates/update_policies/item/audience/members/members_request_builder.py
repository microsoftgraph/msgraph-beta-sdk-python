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
    from ........models.o_data_errors import o_data_error
    from ........models.windows_updates import updatable_asset, updatable_asset_collection_response
    from .count import count_request_builder
    from .windows_updates_enroll_assets import windows_updates_enroll_assets_request_builder
    from .windows_updates_enroll_assets_by_id import windows_updates_enroll_assets_by_id_request_builder
    from .windows_updates_unenroll_assets import windows_updates_unenroll_assets_request_builder
    from .windows_updates_unenroll_assets_by_id import windows_updates_unenroll_assets_by_id_request_builder

class MembersRequestBuilder():
    """
    Provides operations to manage the members property of the microsoft.graph.windowsUpdates.deploymentAudience entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MembersRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/admin/windows/updates/updatePolicies/{updatePolicy%2Did}/audience/members{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[MembersRequestBuilderGetRequestConfiguration] = None) -> Optional[updatable_asset_collection_response.UpdatableAssetCollectionResponse]:
        """
        List the updatableAsset resources that are members of a deploymentAudience.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[updatable_asset_collection_response.UpdatableAssetCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.windows_updates import updatable_asset_collection_response

        return await self.request_adapter.send_async(request_info, updatable_asset_collection_response.UpdatableAssetCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[updatable_asset.UpdatableAsset] = None, request_configuration: Optional[MembersRequestBuilderPostRequestConfiguration] = None) -> Optional[updatable_asset.UpdatableAsset]:
        """
        Create new navigation property to members for admin
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[updatable_asset.UpdatableAsset]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.windows_updates import updatable_asset

        return await self.request_adapter.send_async(request_info, updatable_asset.UpdatableAsset, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[MembersRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        List the updatableAsset resources that are members of a deploymentAudience.
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
    
    def to_post_request_information(self,body: Optional[updatable_asset.UpdatableAsset] = None, request_configuration: Optional[MembersRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to members for admin
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
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count import count_request_builder

        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_updates_enroll_assets(self) -> windows_updates_enroll_assets_request_builder.WindowsUpdatesEnrollAssetsRequestBuilder:
        """
        Provides operations to call the enrollAssets method.
        """
        from .windows_updates_enroll_assets import windows_updates_enroll_assets_request_builder

        return windows_updates_enroll_assets_request_builder.WindowsUpdatesEnrollAssetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_updates_enroll_assets_by_id(self) -> windows_updates_enroll_assets_by_id_request_builder.WindowsUpdatesEnrollAssetsByIdRequestBuilder:
        """
        Provides operations to call the enrollAssetsById method.
        """
        from .windows_updates_enroll_assets_by_id import windows_updates_enroll_assets_by_id_request_builder

        return windows_updates_enroll_assets_by_id_request_builder.WindowsUpdatesEnrollAssetsByIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_updates_unenroll_assets(self) -> windows_updates_unenroll_assets_request_builder.WindowsUpdatesUnenrollAssetsRequestBuilder:
        """
        Provides operations to call the unenrollAssets method.
        """
        from .windows_updates_unenroll_assets import windows_updates_unenroll_assets_request_builder

        return windows_updates_unenroll_assets_request_builder.WindowsUpdatesUnenrollAssetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_updates_unenroll_assets_by_id(self) -> windows_updates_unenroll_assets_by_id_request_builder.WindowsUpdatesUnenrollAssetsByIdRequestBuilder:
        """
        Provides operations to call the unenrollAssetsById method.
        """
        from .windows_updates_unenroll_assets_by_id import windows_updates_unenroll_assets_by_id_request_builder

        return windows_updates_unenroll_assets_by_id_request_builder.WindowsUpdatesUnenrollAssetsByIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MembersRequestBuilderGetQueryParameters():
        """
        List the updatableAsset resources that are members of a deploymentAudience.
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
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class MembersRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[MembersRequestBuilder.MembersRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class MembersRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

