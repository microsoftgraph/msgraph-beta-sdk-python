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
    from ......models.o_data_errors.o_data_error import ODataError

class ApplyDecisionsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the applyDecisions method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ApplyDecisionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/accessReviews/{accessReview%2Did}/instances/{accessReview%2Did1}/applyDecisions", path_parameters)
    
    async def post(self,request_configuration: Optional[ApplyDecisionsRequestBuilderPostRequestConfiguration] = None) -> None:
        """
        In the Microsoft Entra access reviews feature, apply the decisions of a completed accessReview.  The target object can be either a one-time access review, or an instance of a recurring access review.   After an access review is finished, either because it reached the end date or an administrator stopped it manually, and auto-apply wasn't configured for the review, you can call Apply to apply the changes. Until apply occurs, the decisions to remove access rights do not appear on the source resource, the users for instance retain their group memberships. By calling apply, the outcome of the review is implemented by updating the group or application. If a user's access was denied in the review, when an administrator calls this API, Microsoft Entra ID removes their membership or application assignment.  After an access review is finished, and auto-apply was configured, then the status of the review will change from Completed through intermediate states and finally will change to state Applied. You should expect to see denied users, if any, being removed from the resource group membership or app assignment in a few minutes. A configured auto applying review, or selecting Apply doesn't have an effect on a group that originates in an on-premises directory or a dynamic group. If you want to change a group that originates on-premises, download the results and apply those changes to the representation of the group in that directory.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/accessreview-apply?view=graph-rest-1.0
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[ApplyDecisionsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        In the Microsoft Entra access reviews feature, apply the decisions of a completed accessReview.  The target object can be either a one-time access review, or an instance of a recurring access review.   After an access review is finished, either because it reached the end date or an administrator stopped it manually, and auto-apply wasn't configured for the review, you can call Apply to apply the changes. Until apply occurs, the decisions to remove access rights do not appear on the source resource, the users for instance retain their group memberships. By calling apply, the outcome of the review is implemented by updating the group or application. If a user's access was denied in the review, when an administrator calls this API, Microsoft Entra ID removes their membership or application assignment.  After an access review is finished, and auto-apply was configured, then the status of the review will change from Completed through intermediate states and finally will change to state Applied. You should expect to see denied users, if any, being removed from the resource group membership or app assignment in a few minutes. A configured auto applying review, or selecting Apply doesn't have an effect on a group that originates in an on-premises directory or a dynamic group. If you want to change a group that originates on-premises, download the results and apply those changes to the representation of the group in that directory.
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
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ApplyDecisionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ApplyDecisionsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ApplyDecisionsRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ApplyDecisionsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

