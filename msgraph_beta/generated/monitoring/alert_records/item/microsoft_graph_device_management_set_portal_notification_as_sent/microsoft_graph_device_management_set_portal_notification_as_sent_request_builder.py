from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.o_data_errors.o_data_error import ODataError

class MicrosoftGraphDeviceManagementSetPortalNotificationAsSentRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the setPortalNotificationAsSent method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new MicrosoftGraphDeviceManagementSetPortalNotificationAsSentRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/monitoring/alertRecords/{alertRecord%2Did}/microsoft.graph.deviceManagement.setPortalNotificationAsSent", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Set the status of the notification associated with the specified alertRecord on the Microsoft EndPoint Manager admin center as sent, by setting the isPortalNotificationSent property of the portal notification to true.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/devicemanagement-alertrecord-setportalnotificationassent?view=graph-rest-1.0
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Set the status of the notification associated with the specified alertRecord on the Microsoft EndPoint Manager admin center as sent, by setting the isPortalNotificationSent property of the portal notification to true.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> MicrosoftGraphDeviceManagementSetPortalNotificationAsSentRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MicrosoftGraphDeviceManagementSetPortalNotificationAsSentRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return MicrosoftGraphDeviceManagementSetPortalNotificationAsSentRequestBuilder(self.request_adapter, raw_url)
    

