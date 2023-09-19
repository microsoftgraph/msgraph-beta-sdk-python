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
    from .....models.add_large_gallery_view_operation import AddLargeGalleryViewOperation
    from .....models.o_data_errors.o_data_error import ODataError
    from .add_large_gallery_view_post_request_body import AddLargeGalleryViewPostRequestBody

class AddLargeGalleryViewRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the addLargeGalleryView method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AddLargeGalleryViewRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/communications/calls/{call%2Did}/addLargeGalleryView", path_parameters)
    
    async def post(self,body: Optional[AddLargeGalleryViewPostRequestBody] = None, request_configuration: Optional[AddLargeGalleryViewRequestBuilderPostRequestConfiguration] = None) -> Optional[AddLargeGalleryViewOperation]:
        """
        Add the large gallery view to a call.  For details about how to identify a large gallery view participant in a roster so that you can retrieve the relevant data to subscribe to the video feed, see Identify large gallery view participants in a roster.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AddLargeGalleryViewOperation]
        Find more info here: https://learn.microsoft.com/graph/api/call-addlargegalleryview?view=graph-rest-1.0
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
        from .....models.add_large_gallery_view_operation import AddLargeGalleryViewOperation

        return await self.request_adapter.send_async(request_info, AddLargeGalleryViewOperation, error_mapping)
    
    def to_post_request_information(self,body: Optional[AddLargeGalleryViewPostRequestBody] = None, request_configuration: Optional[AddLargeGalleryViewRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Add the large gallery view to a call.  For details about how to identify a large gallery view participant in a roster so that you can retrieve the relevant data to subscribe to the video feed, see Identify large gallery view participants in a roster.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> AddLargeGalleryViewRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AddLargeGalleryViewRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AddLargeGalleryViewRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AddLargeGalleryViewRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

