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

publish_request_builder = lazy_import('msgraph.generated.admin.edge.internet_explorer_mode.site_lists.item.publish.publish_request_builder')
shared_cookies_request_builder = lazy_import('msgraph.generated.admin.edge.internet_explorer_mode.site_lists.item.shared_cookies.shared_cookies_request_builder')
browser_shared_cookie_item_request_builder = lazy_import('msgraph.generated.admin.edge.internet_explorer_mode.site_lists.item.shared_cookies.item.browser_shared_cookie_item_request_builder')
sites_request_builder = lazy_import('msgraph.generated.admin.edge.internet_explorer_mode.site_lists.item.sites.sites_request_builder')
browser_site_item_request_builder = lazy_import('msgraph.generated.admin.edge.internet_explorer_mode.site_lists.item.sites.item.browser_site_item_request_builder')
browser_site_list = lazy_import('msgraph.generated.models.browser_site_list')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class BrowserSiteListItemRequestBuilder():
    """
    Provides operations to manage the siteLists property of the microsoft.graph.internetExplorerMode entity.
    """
    @property
    def publish(self) -> publish_request_builder.PublishRequestBuilder:
        """
        Provides operations to call the publish method.
        """
        return publish_request_builder.PublishRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shared_cookies(self) -> shared_cookies_request_builder.SharedCookiesRequestBuilder:
        """
        Provides operations to manage the sharedCookies property of the microsoft.graph.browserSiteList entity.
        """
        return shared_cookies_request_builder.SharedCookiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sites(self) -> sites_request_builder.SitesRequestBuilder:
        """
        Provides operations to manage the sites property of the microsoft.graph.browserSiteList entity.
        """
        return sites_request_builder.SitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new BrowserSiteListItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/admin/edge/internetExplorerMode/siteLists/{browserSiteList%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[BrowserSiteListItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property siteLists for admin
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
    
    def create_get_request_information(self,request_configuration: Optional[BrowserSiteListItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A collection of site lists to support Internet Explorer mode.
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
    
    def create_patch_request_information(self,body: Optional[browser_site_list.BrowserSiteList] = None, request_configuration: Optional[BrowserSiteListItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property siteLists in admin
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
    
    async def delete(self,request_configuration: Optional[BrowserSiteListItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property siteLists for admin
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
    
    async def get(self,request_configuration: Optional[BrowserSiteListItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[browser_site_list.BrowserSiteList]:
        """
        A collection of site lists to support Internet Explorer mode.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[browser_site_list.BrowserSiteList]
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
        return await self.request_adapter.send_async(request_info, browser_site_list.BrowserSiteList, response_handler, error_mapping)
    
    async def patch(self,body: Optional[browser_site_list.BrowserSiteList] = None, request_configuration: Optional[BrowserSiteListItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[browser_site_list.BrowserSiteList]:
        """
        Update the navigation property siteLists in admin
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[browser_site_list.BrowserSiteList]
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
        return await self.request_adapter.send_async(request_info, browser_site_list.BrowserSiteList, response_handler, error_mapping)
    
    def shared_cookies_by_id(self,id: str) -> browser_shared_cookie_item_request_builder.BrowserSharedCookieItemRequestBuilder:
        """
        Provides operations to manage the sharedCookies property of the microsoft.graph.browserSiteList entity.
        Args:
            id: Unique identifier of the item
        Returns: browser_shared_cookie_item_request_builder.BrowserSharedCookieItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["browserSharedCookie%2Did"] = id
        return browser_shared_cookie_item_request_builder.BrowserSharedCookieItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sites_by_id(self,id: str) -> browser_site_item_request_builder.BrowserSiteItemRequestBuilder:
        """
        Provides operations to manage the sites property of the microsoft.graph.browserSiteList entity.
        Args:
            id: Unique identifier of the item
        Returns: browser_site_item_request_builder.BrowserSiteItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["browserSite%2Did"] = id
        return browser_site_item_request_builder.BrowserSiteItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class BrowserSiteListItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class BrowserSiteListItemRequestBuilderGetQueryParameters():
        """
        A collection of site lists to support Internet Explorer mode.
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
    class BrowserSiteListItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[BrowserSiteListItemRequestBuilder.BrowserSiteListItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class BrowserSiteListItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

