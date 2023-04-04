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
    from ........models import onenote_section
    from ........models.o_data_errors import o_data_error
    from .copy_to_notebook import copy_to_notebook_request_builder
    from .copy_to_section_group import copy_to_section_group_request_builder
    from .pages import pages_request_builder
    from .pages.item import onenote_page_item_request_builder
    from .parent_notebook import parent_notebook_request_builder
    from .parent_section_group import parent_section_group_request_builder

class OnenoteSectionItemRequestBuilder():
    """
    Provides operations to manage the sections property of the microsoft.graph.sectionGroup entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OnenoteSectionItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/onenote/sectionGroups/{sectionGroup%2Did}/sections/{onenoteSection%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[OnenoteSectionItemRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete navigation property sections for users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def get(self,request_configuration: Optional[OnenoteSectionItemRequestBuilderGetRequestConfiguration] = None) -> Optional[onenote_section.OnenoteSection]:
        """
        The sections in the section group. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[onenote_section.OnenoteSection]
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
        from ........models import onenote_section

        return await self.request_adapter.send_async(request_info, onenote_section.OnenoteSection, error_mapping)
    
    def pages_by_id(self,id: str) -> onenote_page_item_request_builder.OnenotePageItemRequestBuilder:
        """
        Provides operations to manage the pages property of the microsoft.graph.onenoteSection entity.
        Args:
            id: Unique identifier of the item
        Returns: onenote_page_item_request_builder.OnenotePageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .pages.item import onenote_page_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["onenotePage%2Did"] = id
        return onenote_page_item_request_builder.OnenotePageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[onenote_section.OnenoteSection] = None, request_configuration: Optional[OnenoteSectionItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[onenote_section.OnenoteSection]:
        """
        Update the navigation property sections in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[onenote_section.OnenoteSection]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models import onenote_section

        return await self.request_adapter.send_async(request_info, onenote_section.OnenoteSection, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[OnenoteSectionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property sections for users
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
    
    def to_get_request_information(self,request_configuration: Optional[OnenoteSectionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The sections in the section group. Read-only. Nullable.
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
    
    def to_patch_request_information(self,body: Optional[onenote_section.OnenoteSection] = None, request_configuration: Optional[OnenoteSectionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property sections in users
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
    def copy_to_notebook(self) -> copy_to_notebook_request_builder.CopyToNotebookRequestBuilder:
        """
        Provides operations to call the copyToNotebook method.
        """
        from .copy_to_notebook import copy_to_notebook_request_builder

        return copy_to_notebook_request_builder.CopyToNotebookRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def copy_to_section_group(self) -> copy_to_section_group_request_builder.CopyToSectionGroupRequestBuilder:
        """
        Provides operations to call the copyToSectionGroup method.
        """
        from .copy_to_section_group import copy_to_section_group_request_builder

        return copy_to_section_group_request_builder.CopyToSectionGroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pages(self) -> pages_request_builder.PagesRequestBuilder:
        """
        Provides operations to manage the pages property of the microsoft.graph.onenoteSection entity.
        """
        from .pages import pages_request_builder

        return pages_request_builder.PagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def parent_notebook(self) -> parent_notebook_request_builder.ParentNotebookRequestBuilder:
        """
        Provides operations to manage the parentNotebook property of the microsoft.graph.onenoteSection entity.
        """
        from .parent_notebook import parent_notebook_request_builder

        return parent_notebook_request_builder.ParentNotebookRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def parent_section_group(self) -> parent_section_group_request_builder.ParentSectionGroupRequestBuilder:
        """
        Provides operations to manage the parentSectionGroup property of the microsoft.graph.onenoteSection entity.
        """
        from .parent_section_group import parent_section_group_request_builder

        return parent_section_group_request_builder.ParentSectionGroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OnenoteSectionItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class OnenoteSectionItemRequestBuilderGetQueryParameters():
        """
        The sections in the section group. Read-only. Nullable.
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
    class OnenoteSectionItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[OnenoteSectionItemRequestBuilder.OnenoteSectionItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class OnenoteSectionItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

