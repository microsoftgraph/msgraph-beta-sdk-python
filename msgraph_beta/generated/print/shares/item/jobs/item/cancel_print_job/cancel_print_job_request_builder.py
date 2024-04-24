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
from warnings import warn

if TYPE_CHECKING:
    from .......models.o_data_errors.o_data_error import ODataError

class CancelPrintJobRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the cancelPrintJob method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CancelPrintJobRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/print/shares/{printerShare%2Did}/jobs/{printJob%2Did}/cancelPrintJob", path_parameters)
    
    async def post(self,request_configuration: Optional[CancelPrintJobRequestBuilderPostRequestConfiguration] = None) -> None:
        """
        Invoke action cancelPrintJob
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        warn("The cancelPrintJob API is deprecated and will stop returning data on July 31, 2023. Please use the cancel API instead of this. as of 2023-06/Tasks_And_Plans", DeprecationWarning)
        request_info = self.to_post_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[CancelPrintJobRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Invoke action cancelPrintJob
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The cancelPrintJob API is deprecated and will stop returning data on July 31, 2023. Please use the cancel API instead of this. as of 2023-06/Tasks_And_Plans", DeprecationWarning)
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CancelPrintJobRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CancelPrintJobRequestBuilder
        """
        warn("The cancelPrintJob API is deprecated and will stop returning data on July 31, 2023. Please use the cancel API instead of this. as of 2023-06/Tasks_And_Plans", DeprecationWarning)
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CancelPrintJobRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CancelPrintJobRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

