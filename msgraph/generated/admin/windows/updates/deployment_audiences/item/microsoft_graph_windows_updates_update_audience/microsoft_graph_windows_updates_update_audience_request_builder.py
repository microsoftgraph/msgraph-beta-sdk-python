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
    from .update_audience_post_request_body import UpdateAudiencePostRequestBody

class MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the updateAudience method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/admin/windows/updates/deploymentAudiences/{deploymentAudience%2Did}/microsoft.graph.windowsUpdates.updateAudience", path_parameters)
    
    async def post(self,body: Optional[UpdateAudiencePostRequestBody] = None, request_configuration: Optional[MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilderPostRequestConfiguration] = None) -> None:
        """
        Update the members and exclusions collections of a deploymentAudience. Adding an azureADDevice to the members or exclusions collections of a deployment audience automatically creates an Azure AD device object, if it does not already exist. If the same updatableAsset gets included in the exclusions and members collections of a deploymentAudience, deployment will not apply to that asset. If all updatableAsset objects are the same type, you can also use the method updateAudienceById to update the deploymentAudience.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/windowsupdates-deploymentaudience-updateaudience?view=graph-rest-1.0
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
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_post_request_information(self,body: Optional[UpdateAudiencePostRequestBody] = None, request_configuration: Optional[MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Update the members and exclusions collections of a deploymentAudience. Adding an azureADDevice to the members or exclusions collections of a deployment audience automatically creates an Azure AD device object, if it does not already exist. If the same updatableAsset gets included in the exclusions and members collections of a deploymentAudience, deployment will not apply to that asset. If all updatableAsset objects are the same type, you can also use the method updateAudienceById to update the deploymentAudience.
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
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

