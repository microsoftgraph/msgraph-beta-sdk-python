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
    from .....models.o_data_errors.o_data_error import ODataError
    from .set_user_preferred_presence_post_request_body import SetUserPreferredPresencePostRequestBody

class SetUserPreferredPresenceRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the setUserPreferredPresence method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SetUserPreferredPresenceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/communications/presences/{presence%2Did}/setUserPreferredPresence", path_parameters)
    
    async def post(self,body: Optional[SetUserPreferredPresencePostRequestBody] = None, request_configuration: Optional[SetUserPreferredPresenceRequestBuilderPostRequestConfiguration] = None) -> None:
        """
        Set the preferred availability and activity status for a user. If the preferred presence of a user is set, the user's presence is the preferred presence. Preferred presence takes effect only when there is at least one presence session of the user. Otherwise, the user's presence stays as Offline. A presence session can be created as a result of a successful setPresence operation, or if the user is signed in on a Teams client.  Read more about presence sessions and their time-out and expiration. 
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/presence-setuserpreferredpresence?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_post_request_information(self,body: Optional[SetUserPreferredPresencePostRequestBody] = None, request_configuration: Optional[SetUserPreferredPresenceRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Set the preferred availability and activity status for a user. If the preferred presence of a user is set, the user's presence is the preferred presence. Preferred presence takes effect only when there is at least one presence session of the user. Otherwise, the user's presence stays as Offline. A presence session can be created as a result of a successful setPresence operation, or if the user is signed in on a Teams client.  Read more about presence sessions and their time-out and expiration. 
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
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> SetUserPreferredPresenceRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SetUserPreferredPresenceRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return SetUserPreferredPresenceRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SetUserPreferredPresenceRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

