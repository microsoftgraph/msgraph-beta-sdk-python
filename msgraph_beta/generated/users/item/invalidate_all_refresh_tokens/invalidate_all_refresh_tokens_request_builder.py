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
    from .invalidate_all_refresh_tokens_post_response import InvalidateAllRefreshTokensPostResponse

class InvalidateAllRefreshTokensRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the invalidateAllRefreshTokens method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new InvalidateAllRefreshTokensRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/invalidateAllRefreshTokens", path_parameters)
    
    async def post(self,request_configuration: Optional[InvalidateAllRefreshTokensRequestBuilderPostRequestConfiguration] = None) -> Optional[InvalidateAllRefreshTokensPostResponse]:
        """
        Invalidates all of the user's refresh tokens issued to applications (as well as session cookies in a user's browser), by resetting the refreshTokensValidFromDateTime user property to the current date-time. Typically, this operation is performed (by the user or an administrator) if the user has a lost or stolen device.  This operation would prevent access to any of the organization's data accessed through applications on the device without the user first being required to sign in again. In fact, this operation would force the user to sign in again for all applications that they have previously consented to, independent of device. For developers, if the application attempts to redeem a delegated access token for this user by using an invalidated refresh token, the application will get an error. If this happens, the application will need to acquire a new refresh token by making a request to the authorize endpoint, which will force the user to sign in. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InvalidateAllRefreshTokensPostResponse]
        Find more info here: https://learn.microsoft.com/graph/api/user-invalidateallrefreshtokens?view=graph-rest-1.0
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .invalidate_all_refresh_tokens_post_response import InvalidateAllRefreshTokensPostResponse

        return await self.request_adapter.send_async(request_info, InvalidateAllRefreshTokensPostResponse, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[InvalidateAllRefreshTokensRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Invalidates all of the user's refresh tokens issued to applications (as well as session cookies in a user's browser), by resetting the refreshTokensValidFromDateTime user property to the current date-time. Typically, this operation is performed (by the user or an administrator) if the user has a lost or stolen device.  This operation would prevent access to any of the organization's data accessed through applications on the device without the user first being required to sign in again. In fact, this operation would force the user to sign in again for all applications that they have previously consented to, independent of device. For developers, if the application attempts to redeem a delegated access token for this user by using an invalidated refresh token, the application will get an error. If this happens, the application will need to acquire a new refresh token by making a request to the authorize endpoint, which will force the user to sign in. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> InvalidateAllRefreshTokensRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InvalidateAllRefreshTokensRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return InvalidateAllRefreshTokensRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class InvalidateAllRefreshTokensRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

