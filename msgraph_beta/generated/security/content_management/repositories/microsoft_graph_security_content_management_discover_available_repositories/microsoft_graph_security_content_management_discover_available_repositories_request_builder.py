from __future__ import annotations
from collections.abc import Callable
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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.o_data_errors.o_data_error import ODataError
    from .discover_available_repositories_post_request_body import DiscoverAvailableRepositoriesPostRequestBody
    from .discover_available_repositories_post_response import DiscoverAvailableRepositoriesPostResponse

class MicrosoftGraphSecurityContentManagementDiscoverAvailableRepositoriesRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the discoverAvailableRepositories method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MicrosoftGraphSecurityContentManagementDiscoverAvailableRepositoriesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/contentManagement/repositories/microsoft.graph.security.contentManagement.discoverAvailableRepositories", path_parameters)
    
    async def post(self,body: DiscoverAvailableRepositoriesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DiscoverAvailableRepositoriesPostResponse]:
        """
        Discover candidate repositories the caller can connect, using a supplied provider credential.Credential is passed in the request body and is never returned; only repository metadata is.Results are transient, non-addressable discovery records: the backend exposes no stable id fora candidate repository (confirmed in source), so they are modeled as value objects, not entities.The result is a bounded set: the action returns up to 200 candidate repositories accessible to thesupplied credential. It is not paged. Paging is not offered because the credential is a write-onlyrequest-body value and an OData `@odata.nextLink` continuation is a GET that cannot carry it; thebound keeps the response size predictable. Callers who need a specific repository connect it directly.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DiscoverAvailableRepositoriesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .discover_available_repositories_post_response import DiscoverAvailableRepositoriesPostResponse

        return await self.request_adapter.send_async(request_info, DiscoverAvailableRepositoriesPostResponse, error_mapping)
    
    def to_post_request_information(self,body: DiscoverAvailableRepositoriesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Discover candidate repositories the caller can connect, using a supplied provider credential.Credential is passed in the request body and is never returned; only repository metadata is.Results are transient, non-addressable discovery records: the backend exposes no stable id fora candidate repository (confirmed in source), so they are modeled as value objects, not entities.The result is a bounded set: the action returns up to 200 candidate repositories accessible to thesupplied credential. It is not paged. Paging is not offered because the credential is a write-onlyrequest-body value and an OData `@odata.nextLink` continuation is a GET that cannot carry it; thebound keeps the response size predictable. Callers who need a specific repository connect it directly.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> MicrosoftGraphSecurityContentManagementDiscoverAvailableRepositoriesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MicrosoftGraphSecurityContentManagementDiscoverAvailableRepositoriesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MicrosoftGraphSecurityContentManagementDiscoverAvailableRepositoriesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MicrosoftGraphSecurityContentManagementDiscoverAvailableRepositoriesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

