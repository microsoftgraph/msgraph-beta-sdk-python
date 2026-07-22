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
    from ......models.lock_info import LockInfo
    from ......models.o_data_errors.o_data_error import ODataError
    from .lock_post_request_body import LockPostRequestBody

class LockRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the lock method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LockRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/lock", path_parameters)
    
    async def post(self,body: LockPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LockInfo]:
        """
        Acquire an exclusive lock on a file represented by a driveItem, or extend an existing lock you already hold. While the lock is held, other users are prevented from acquiring a lock on the same file. The lock automatically expires after the duration specified in the request elapses. A single endpoint handles both initial acquisition and refresh. The server determines which behavior applies based on the file's current lock state and the caller's identity. The caller doesn't need to track whether they previously locked the file, and doesn't need to manage a lock identifier. Only exclusive locks are currently supported.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LockInfo]
        Find more info here: https://learn.microsoft.com/graph/api/driveitem-lock?view=graph-rest-beta
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.lock_info import LockInfo

        return await self.request_adapter.send_async(request_info, LockInfo, error_mapping)
    
    def to_post_request_information(self,body: LockPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Acquire an exclusive lock on a file represented by a driveItem, or extend an existing lock you already hold. While the lock is held, other users are prevented from acquiring a lock on the same file. The lock automatically expires after the duration specified in the request elapses. A single endpoint handles both initial acquisition and refresh. The server determines which behavior applies based on the file's current lock state and the caller's identity. The caller doesn't need to track whether they previously locked the file, and doesn't need to manage a lock identifier. Only exclusive locks are currently supported.
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
    
    def with_url(self,raw_url: str) -> LockRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LockRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LockRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class LockRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

