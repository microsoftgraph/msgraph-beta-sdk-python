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
    from ..models import search_entity
    from ..models.o_data_errors import o_data_error
    from .acronyms import acronyms_request_builder
    from .acronyms.item import acronym_item_request_builder
    from .bookmarks import bookmarks_request_builder
    from .bookmarks.item import bookmark_item_request_builder
    from .qnas import qnas_request_builder
    from .qnas.item import qna_item_request_builder
    from .query import query_request_builder

class SearchRequestBuilder():
    """
    Provides operations to manage the searchEntity singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SearchRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/search{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def acronyms_by_id(self,id: str) -> acronym_item_request_builder.AcronymItemRequestBuilder:
        """
        Provides operations to manage the acronyms property of the microsoft.graph.searchEntity entity.
        Args:
            id: Unique identifier of the item
        Returns: acronym_item_request_builder.AcronymItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .acronyms.item import acronym_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["acronym%2Did"] = id
        return acronym_item_request_builder.AcronymItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def bookmarks_by_id(self,id: str) -> bookmark_item_request_builder.BookmarkItemRequestBuilder:
        """
        Provides operations to manage the bookmarks property of the microsoft.graph.searchEntity entity.
        Args:
            id: Unique identifier of the item
        Returns: bookmark_item_request_builder.BookmarkItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .bookmarks.item import bookmark_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["bookmark%2Did"] = id
        return bookmark_item_request_builder.BookmarkItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[SearchRequestBuilderGetRequestConfiguration] = None) -> Optional[search_entity.SearchEntity]:
        """
        Get search
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[search_entity.SearchEntity]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import search_entity

        return await self.request_adapter.send_async(request_info, search_entity.SearchEntity, error_mapping)
    
    async def patch(self,body: Optional[search_entity.SearchEntity] = None, request_configuration: Optional[SearchRequestBuilderPatchRequestConfiguration] = None) -> Optional[search_entity.SearchEntity]:
        """
        Update search
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[search_entity.SearchEntity]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import search_entity

        return await self.request_adapter.send_async(request_info, search_entity.SearchEntity, error_mapping)
    
    def qnas_by_id(self,id: str) -> qna_item_request_builder.QnaItemRequestBuilder:
        """
        Provides operations to manage the qnas property of the microsoft.graph.searchEntity entity.
        Args:
            id: Unique identifier of the item
        Returns: qna_item_request_builder.QnaItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .qnas.item import qna_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["qna%2Did"] = id
        return qna_item_request_builder.QnaItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[SearchRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get search
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
    
    def to_patch_request_information(self,body: Optional[search_entity.SearchEntity] = None, request_configuration: Optional[SearchRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update search
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
    def acronyms(self) -> acronyms_request_builder.AcronymsRequestBuilder:
        """
        Provides operations to manage the acronyms property of the microsoft.graph.searchEntity entity.
        """
        from .acronyms import acronyms_request_builder

        return acronyms_request_builder.AcronymsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bookmarks(self) -> bookmarks_request_builder.BookmarksRequestBuilder:
        """
        Provides operations to manage the bookmarks property of the microsoft.graph.searchEntity entity.
        """
        from .bookmarks import bookmarks_request_builder

        return bookmarks_request_builder.BookmarksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def qnas(self) -> qnas_request_builder.QnasRequestBuilder:
        """
        Provides operations to manage the qnas property of the microsoft.graph.searchEntity entity.
        """
        from .qnas import qnas_request_builder

        return qnas_request_builder.QnasRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def query(self) -> query_request_builder.QueryRequestBuilder:
        """
        Provides operations to call the query method.
        """
        from .query import query_request_builder

        return query_request_builder.QueryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SearchRequestBuilderGetQueryParameters():
        """
        Get search
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
    class SearchRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SearchRequestBuilder.SearchRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SearchRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

