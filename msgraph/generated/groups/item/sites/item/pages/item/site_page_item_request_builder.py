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

canvas_layout_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.pages.item.canvas_layout.canvas_layout_request_builder')
get_web_parts_by_position_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.pages.item.get_web_parts_by_position.get_web_parts_by_position_request_builder')
publish_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.pages.item.publish.publish_request_builder')
web_parts_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.pages.item.web_parts.web_parts_request_builder')
web_part_item_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.pages.item.web_parts.item.web_part_item_request_builder')
site_page = lazy_import('msgraph.generated.models.site_page')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class SitePageItemRequestBuilder():
    """
    Provides operations to manage the pages property of the microsoft.graph.site entity.
    """
    @property
    def canvas_layout(self) -> canvas_layout_request_builder.CanvasLayoutRequestBuilder:
        """
        Provides operations to manage the canvasLayout property of the microsoft.graph.sitePage entity.
        """
        return canvas_layout_request_builder.CanvasLayoutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_web_parts_by_position(self) -> get_web_parts_by_position_request_builder.GetWebPartsByPositionRequestBuilder:
        """
        Provides operations to call the getWebPartsByPosition method.
        """
        return get_web_parts_by_position_request_builder.GetWebPartsByPositionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def publish(self) -> publish_request_builder.PublishRequestBuilder:
        """
        Provides operations to call the publish method.
        """
        return publish_request_builder.PublishRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def web_parts(self) -> web_parts_request_builder.WebPartsRequestBuilder:
        """
        Provides operations to manage the webParts property of the microsoft.graph.sitePage entity.
        """
        return web_parts_request_builder.WebPartsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SitePageItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/pages/{sitePage%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[SitePageItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property pages for groups
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
    
    def create_get_request_information(self,request_configuration: Optional[SitePageItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The collection of pages in the SitePages list in this site.
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
    
    def create_patch_request_information(self,body: Optional[site_page.SitePage] = None, request_configuration: Optional[SitePageItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property pages in groups
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
    
    async def delete(self,request_configuration: Optional[SitePageItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property pages for groups
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
    
    async def get(self,request_configuration: Optional[SitePageItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[site_page.SitePage]:
        """
        The collection of pages in the SitePages list in this site.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[site_page.SitePage]
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
        return await self.request_adapter.send_async(request_info, site_page.SitePage, response_handler, error_mapping)
    
    async def patch(self,body: Optional[site_page.SitePage] = None, request_configuration: Optional[SitePageItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[site_page.SitePage]:
        """
        Update the navigation property pages in groups
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[site_page.SitePage]
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
        return await self.request_adapter.send_async(request_info, site_page.SitePage, response_handler, error_mapping)
    
    def web_parts_by_id(self,id: str) -> web_part_item_request_builder.WebPartItemRequestBuilder:
        """
        Provides operations to manage the webParts property of the microsoft.graph.sitePage entity.
        Args:
            id: Unique identifier of the item
        Returns: web_part_item_request_builder.WebPartItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["webPart%2Did"] = id
        return web_part_item_request_builder.WebPartItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class SitePageItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SitePageItemRequestBuilderGetQueryParameters():
        """
        The collection of pages in the SitePages list in this site.
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
    class SitePageItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SitePageItemRequestBuilder.SitePageItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SitePageItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

