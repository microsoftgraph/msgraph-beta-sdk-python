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
    from ....models.directory_setting import DirectorySetting
    from ....models.directory_setting_collection_response import DirectorySettingCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.directory_setting_item_request_builder import DirectorySettingItemRequestBuilder

class SettingsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the settings property of the microsoft.graph.group entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SettingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/settings{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_directory_setting_id(self,directory_setting_id: str) -> DirectorySettingItemRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.group entity.
        param directory_setting_id: The unique identifier of directorySetting
        Returns: DirectorySettingItemRequestBuilder
        """
        if not directory_setting_id:
            raise TypeError("directory_setting_id cannot be null.")
        from .item.directory_setting_item_request_builder import DirectorySettingItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directorySetting%2Did"] = directory_setting_id
        return DirectorySettingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[SettingsRequestBuilderGetRequestConfiguration] = None) -> Optional[DirectorySettingCollectionResponse]:
        """
        Settings that can govern this group's behavior, like whether members can invite guest users to the group. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DirectorySettingCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.directory_setting_collection_response import DirectorySettingCollectionResponse

        return await self.request_adapter.send_async(request_info, DirectorySettingCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[DirectorySetting] = None, request_configuration: Optional[SettingsRequestBuilderPostRequestConfiguration] = None) -> Optional[DirectorySetting]:
        """
        Create a new setting based on the templates available in directorySettingTemplates. These settings can be at the tenant-level or at the group level. Group settings apply to only Microsoft 365 groups. The template named Group.Unified can be used to configure tenant-wide Microsoft 365 group settings, while the template named Group.Unified.Guest can be used to configure group-specific settings.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DirectorySetting]
        Find more info here: https://learn.microsoft.com/graph/api/group-post-settings?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.directory_setting import DirectorySetting

        return await self.request_adapter.send_async(request_info, DirectorySetting, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[SettingsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Settings that can govern this group's behavior, like whether members can invite guest users to the group. Nullable.
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
    
    def to_post_request_information(self,body: Optional[DirectorySetting] = None, request_configuration: Optional[SettingsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create a new setting based on the templates available in directorySettingTemplates. These settings can be at the tenant-level or at the group level. Group settings apply to only Microsoft 365 groups. The template named Group.Unified can be used to configure tenant-wide Microsoft 365 group settings, while the template named Group.Unified.Guest can be used to configure group-specific settings.
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
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> SettingsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SettingsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return SettingsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SettingsRequestBuilderGetQueryParameters():
        """
        Settings that can govern this group's behavior, like whether members can invite guest users to the group. Nullable.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SettingsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[SettingsRequestBuilder.SettingsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SettingsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

