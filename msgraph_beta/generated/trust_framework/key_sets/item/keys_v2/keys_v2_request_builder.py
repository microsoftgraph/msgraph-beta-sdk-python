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
    from .....models.o_data_errors.o_data_error import ODataError
    from .....models.trust_framework_key_v2_collection_response import TrustFrameworkKey_v2CollectionResponse
    from .count.count_request_builder import CountRequestBuilder
    from .item.trust_framework_key_v2_k_item_request_builder import TrustFrameworkKey_v2KItemRequestBuilder

class Keys_v2RequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the keys_v2 property of the microsoft.graph.trustFrameworkKeySet entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new Keys_v2RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/trustFramework/keySets/{trustFrameworkKeySet%2Did}/keys_v2{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_trust_framework_key_v2_kid(self,trust_framework_key_v2_kid: str) -> TrustFrameworkKey_v2KItemRequestBuilder:
        """
        Provides operations to manage the keys_v2 property of the microsoft.graph.trustFrameworkKeySet entity.
        param trust_framework_key_v2_kid: The unique identifier of trustFrameworkKey_v2
        Returns: TrustFrameworkKey_v2KItemRequestBuilder
        """
        if trust_framework_key_v2_kid is None:
            raise TypeError("trust_framework_key_v2_kid cannot be null.")
        from .item.trust_framework_key_v2_k_item_request_builder import TrustFrameworkKey_v2KItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["trustFrameworkKey_v2%2Dkid"] = trust_framework_key_v2_kid
        return TrustFrameworkKey_v2KItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[Keys_v2RequestBuilderGetQueryParameters]] = None) -> Optional[TrustFrameworkKey_v2CollectionResponse]:
        """
        Read the properties and relationships of a trustFrameworkKeyv2 object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TrustFrameworkKey_v2CollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.trust_framework_key_v2_collection_response import TrustFrameworkKey_v2CollectionResponse

        return await self.request_adapter.send_async(request_info, TrustFrameworkKey_v2CollectionResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[Keys_v2RequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read the properties and relationships of a trustFrameworkKeyv2 object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> Keys_v2RequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: Keys_v2RequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return Keys_v2RequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class Keys_v2RequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a trustFrameworkKeyv2 object.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
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

    
    @dataclass
    class Keys_v2RequestBuilderGetRequestConfiguration(RequestConfiguration[Keys_v2RequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

