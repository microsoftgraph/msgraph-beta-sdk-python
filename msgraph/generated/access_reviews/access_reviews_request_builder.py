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
    from ..models.access_review import AccessReview
    from ..models.access_review_collection_response import AccessReviewCollectionResponse
    from ..models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.access_review_item_request_builder import AccessReviewItemRequestBuilder

class AccessReviewsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessReviewsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/accessReviews{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_access_review_id(self,access_review_id: str) -> AccessReviewItemRequestBuilder:
        """
        Provides operations to manage the collection of accessReview entities.
        param access_review_id: The unique identifier of accessReview
        Returns: AccessReviewItemRequestBuilder
        """
        if not access_review_id:
            raise TypeError("access_review_id cannot be null.")
        from .item.access_review_item_request_builder import AccessReviewItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReview%2Did"] = access_review_id
        return AccessReviewItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[AccessReviewsRequestBuilderGetRequestConfiguration] = None) -> Optional[AccessReviewCollectionResponse]:
        """
        Retrieve the accessReview objects for a particular businessFlowTemplate. A list of zero or more accessReview objects are returned, for each one-time and recurring access review that was created with that business flow template.  Note that business flow template IDs are case sensitive. If many access reviews match the filter, to improve efficiency and avoid timeouts, retrieve the result set in pages, by including both the $top query parameter with a page size, for example 100, and the $skip=0 query parameter in the request. These parameters can be included even when you do not anticipate that the request will span multiple pages. When a result set spans multiple pages, Microsoft Graph returns that page with an @odata.nextLink property in the response that contains a URL to the next page of results. If that property is present, continue making additional requests with the @odata.nextLink URL in each response, until all the results are returned, as described in paging Microsoft Graph data in your app. The accessReview objects returned by this API will not include nested structure properties such as settings, or relationships.  To retrieve an access review settings or relationships, use the get accessReview API. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessReviewCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/accessreview-list?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.access_review_collection_response import AccessReviewCollectionResponse

        return await self.request_adapter.send_async(request_info, AccessReviewCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[AccessReview] = None, request_configuration: Optional[AccessReviewsRequestBuilderPostRequestConfiguration] = None) -> Optional[AccessReview]:
        """
        In the Microsoft Entra access reviews feature, create a new accessReview object. Before making this request, the caller must have previously retrieved the list of business flow templates, to have the value of businessFlowTemplateId to include in the request. After making this request, the caller should create a programControl, to link the access review to a program.   This API is available in the following national cloud deployments.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessReview]
        Find more info here: https://learn.microsoft.com/graph/api/accessreview-create?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.access_review import AccessReview

        return await self.request_adapter.send_async(request_info, AccessReview, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[AccessReviewsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the accessReview objects for a particular businessFlowTemplate. A list of zero or more accessReview objects are returned, for each one-time and recurring access review that was created with that business flow template.  Note that business flow template IDs are case sensitive. If many access reviews match the filter, to improve efficiency and avoid timeouts, retrieve the result set in pages, by including both the $top query parameter with a page size, for example 100, and the $skip=0 query parameter in the request. These parameters can be included even when you do not anticipate that the request will span multiple pages. When a result set spans multiple pages, Microsoft Graph returns that page with an @odata.nextLink property in the response that contains a URL to the next page of results. If that property is present, continue making additional requests with the @odata.nextLink URL in each response, until all the results are returned, as described in paging Microsoft Graph data in your app. The accessReview objects returned by this API will not include nested structure properties such as settings, or relationships.  To retrieve an access review settings or relationships, use the get accessReview API. This API is available in the following national cloud deployments.
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
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def to_post_request_information(self,body: Optional[AccessReview] = None, request_configuration: Optional[AccessReviewsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        In the Microsoft Entra access reviews feature, create a new accessReview object. Before making this request, the caller must have previously retrieved the list of business flow templates, to have the value of businessFlowTemplateId to include in the request. After making this request, the caller should create a programControl, to link the access review to a program.   This API is available in the following national cloud deployments.
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
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> AccessReviewsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AccessReviewsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AccessReviewsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AccessReviewsRequestBuilderGetQueryParameters():
        """
        Retrieve the accessReview objects for a particular businessFlowTemplate. A list of zero or more accessReview objects are returned, for each one-time and recurring access review that was created with that business flow template.  Note that business flow template IDs are case sensitive. If many access reviews match the filter, to improve efficiency and avoid timeouts, retrieve the result set in pages, by including both the $top query parameter with a page size, for example 100, and the $skip=0 query parameter in the request. These parameters can be included even when you do not anticipate that the request will span multiple pages. When a result set spans multiple pages, Microsoft Graph returns that page with an @odata.nextLink property in the response that contains a URL to the next page of results. If that property is present, continue making additional requests with the @odata.nextLink URL in each response, until all the results are returned, as described in paging Microsoft Graph data in your app. The accessReview objects returned by this API will not include nested structure properties such as settings, or relationships.  To retrieve an access review settings or relationships, use the get accessReview API. This API is available in the following national cloud deployments.
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
    class AccessReviewsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AccessReviewsRequestBuilder.AccessReviewsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessReviewsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

