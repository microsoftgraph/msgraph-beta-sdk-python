from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ......models.o_data_errors.o_data_error import ODataError
    from ......models.windows_updates.product import Product
    from .editions.editions_request_builder import EditionsRequestBuilder
    from .known_issues.known_issues_request_builder import KnownIssuesRequestBuilder
    from .microsoft_graph_windows_updates_get_known_issues_by_time_range_with_days_in_past_with_include_all_active.microsoft_graph_windows_updates_get_known_issues_by_time_range_with_days_in_past_with_include_all_active_request_builder import MicrosoftGraphWindowsUpdatesGetKnownIssuesByTimeRangeWithDaysInPastWithIncludeAllActiveRequestBuilder
    from .revisions.revisions_request_builder import RevisionsRequestBuilder

class ProductItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the products property of the microsoft.graph.adminWindowsUpdates entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ProductItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/admin/windows/updates/products/{product%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property products for admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ProductItemRequestBuilderGetQueryParameters]] = None) -> Optional[Product]:
        """
        A collection of Windows products.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Product]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.windows_updates.product import Product

        return await self.request_adapter.send_async(request_info, Product, error_mapping)
    
    def microsoft_graph_windows_updates_get_known_issues_by_time_range_with_days_in_past_with_include_all_active(self,days_in_past: int) -> MicrosoftGraphWindowsUpdatesGetKnownIssuesByTimeRangeWithDaysInPastWithIncludeAllActiveRequestBuilder:
        """
        Provides operations to call the getKnownIssuesByTimeRange method.
        param days_in_past: Usage: daysInPast={daysInPast}
        Returns: MicrosoftGraphWindowsUpdatesGetKnownIssuesByTimeRangeWithDaysInPastWithIncludeAllActiveRequestBuilder
        """
        if days_in_past is None:
            raise TypeError("days_in_past cannot be null.")
        from .microsoft_graph_windows_updates_get_known_issues_by_time_range_with_days_in_past_with_include_all_active.microsoft_graph_windows_updates_get_known_issues_by_time_range_with_days_in_past_with_include_all_active_request_builder import MicrosoftGraphWindowsUpdatesGetKnownIssuesByTimeRangeWithDaysInPastWithIncludeAllActiveRequestBuilder

        return MicrosoftGraphWindowsUpdatesGetKnownIssuesByTimeRangeWithDaysInPastWithIncludeAllActiveRequestBuilder(self.request_adapter, self.path_parameters, days_in_past)
    
    async def patch(self,body: Product, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Product]:
        """
        Update the navigation property products in admin
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Product]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.windows_updates.product import Product

        return await self.request_adapter.send_async(request_info, Product, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property products for admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ProductItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        A collection of Windows products.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Product, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property products in admin
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ProductItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ProductItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ProductItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def editions(self) -> EditionsRequestBuilder:
        """
        Provides operations to manage the editions property of the microsoft.graph.windowsUpdates.product entity.
        """
        from .editions.editions_request_builder import EditionsRequestBuilder

        return EditionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def known_issues(self) -> KnownIssuesRequestBuilder:
        """
        Provides operations to manage the knownIssues property of the microsoft.graph.windowsUpdates.product entity.
        """
        from .known_issues.known_issues_request_builder import KnownIssuesRequestBuilder

        return KnownIssuesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def revisions(self) -> RevisionsRequestBuilder:
        """
        Provides operations to manage the revisions property of the microsoft.graph.windowsUpdates.product entity.
        """
        from .revisions.revisions_request_builder import RevisionsRequestBuilder

        return RevisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ProductItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ProductItemRequestBuilderGetQueryParameters():
        """
        A collection of Windows products.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
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

    
    @dataclass
    class ProductItemRequestBuilderGetRequestConfiguration(RequestConfiguration[ProductItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ProductItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

