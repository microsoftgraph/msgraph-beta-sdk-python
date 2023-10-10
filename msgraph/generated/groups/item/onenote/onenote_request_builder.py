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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.onenote import Onenote
    from .notebooks.notebooks_request_builder import NotebooksRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .pages.pages_request_builder import PagesRequestBuilder
    from .resources.resources_request_builder import ResourcesRequestBuilder
    from .section_groups.section_groups_request_builder import SectionGroupsRequestBuilder
    from .sections.sections_request_builder import SectionsRequestBuilder

class OnenoteRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the onenote property of the microsoft.graph.group entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OnenoteRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/onenote{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[OnenoteRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property onenote for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[OnenoteRequestBuilderGetRequestConfiguration] = None) -> Optional[Onenote]:
        """
        Get onenote from groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Onenote]
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
        from ....models.onenote import Onenote

        return await self.request_adapter.send_async(request_info, Onenote, error_mapping)
    
    async def patch(self,body: Optional[Onenote] = None, request_configuration: Optional[OnenoteRequestBuilderPatchRequestConfiguration] = None) -> Optional[Onenote]:
        """
        Update the navigation property onenote in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Onenote]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.onenote import Onenote

        return await self.request_adapter.send_async(request_info, Onenote, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[OnenoteRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property onenote for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_get_request_information(self,request_configuration: Optional[OnenoteRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get onenote from groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_patch_request_information(self,body: Optional[Onenote] = None, request_configuration: Optional[OnenoteRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property onenote in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
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
    
    def with_url(self,raw_url: Optional[str] = None) -> OnenoteRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OnenoteRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return OnenoteRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def notebooks(self) -> NotebooksRequestBuilder:
        """
        Provides operations to manage the notebooks property of the microsoft.graph.onenote entity.
        """
        from .notebooks.notebooks_request_builder import NotebooksRequestBuilder

        return NotebooksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.onenote entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pages(self) -> PagesRequestBuilder:
        """
        Provides operations to manage the pages property of the microsoft.graph.onenote entity.
        """
        from .pages.pages_request_builder import PagesRequestBuilder

        return PagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resources(self) -> ResourcesRequestBuilder:
        """
        Provides operations to manage the resources property of the microsoft.graph.onenote entity.
        """
        from .resources.resources_request_builder import ResourcesRequestBuilder

        return ResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def section_groups(self) -> SectionGroupsRequestBuilder:
        """
        Provides operations to manage the sectionGroups property of the microsoft.graph.onenote entity.
        """
        from .section_groups.section_groups_request_builder import SectionGroupsRequestBuilder

        return SectionGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sections(self) -> SectionsRequestBuilder:
        """
        Provides operations to manage the sections property of the microsoft.graph.onenote entity.
        """
        from .sections.sections_request_builder import SectionsRequestBuilder

        return SectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class OnenoteRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class OnenoteRequestBuilderGetQueryParameters():
        """
        Get onenote from groups
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class OnenoteRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[OnenoteRequestBuilder.OnenoteRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class OnenoteRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

