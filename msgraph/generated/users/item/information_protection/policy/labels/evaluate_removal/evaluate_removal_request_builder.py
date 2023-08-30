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
    from .......models.o_data_errors.o_data_error import ODataError
    from .evaluate_removal_post_request_body import EvaluateRemovalPostRequestBody
    from .evaluate_removal_response import EvaluateRemovalResponse

class EvaluateRemovalRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the evaluateRemoval method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EvaluateRemovalRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/informationProtection/policy/labels/evaluateRemoval", path_parameters)
    
    async def post(self,body: Optional[EvaluateRemovalPostRequestBody] = None, request_configuration: Optional[EvaluateRemovalRequestBuilderPostRequestConfiguration] = None) -> Optional[EvaluateRemovalResponse]:
        """
        Indicate to the consuming application what actions it should take to remove the label information. Given contentInfo as an input, which includes existing content metadata key/value pairs, the API returns an informationProtectionAction that contains some combination of one of more of the following: 
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EvaluateRemovalResponse]
        Find more info here: https://learn.microsoft.com/graph/api/informationprotectionlabel-evaluateremoval?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .evaluate_removal_response import EvaluateRemovalResponse

        return await self.request_adapter.send_async(request_info, EvaluateRemovalResponse, error_mapping)
    
    def to_post_request_information(self,body: Optional[EvaluateRemovalPostRequestBody] = None, request_configuration: Optional[EvaluateRemovalRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Indicate to the consuming application what actions it should take to remove the label information. Given contentInfo as an input, which includes existing content metadata key/value pairs, the API returns an informationProtectionAction that contains some combination of one of more of the following: 
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
    
    def with_url(self,raw_url: Optional[str] = None) -> EvaluateRemovalRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EvaluateRemovalRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return EvaluateRemovalRequestBuilder(raw_url, self.request_adapter)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EvaluateRemovalRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

