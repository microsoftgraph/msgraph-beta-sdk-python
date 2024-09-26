from __future__ import annotations
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
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ......models.frontline_cloud_pc_access_state import FrontlineCloudPcAccessState
    from ......models.o_data_errors.o_data_error import ODataError

class GetFrontlineCloudPcAccessStateRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getFrontlineCloudPcAccessState method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new GetFrontlineCloudPcAccessStateRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/cloudPCs/{cloudPC%2Did}/getFrontlineCloudPcAccessState()", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[frontlineCloudPcAccessState]:
        """
        Get the frontlineCloudPcAccessState of a frontline Cloud PC.  This API only supports shared-use licenses. For more information, see cloudPcProvisioningPolicy. Shared-use licenses allow three users per license, with one user signed in at a time. Callers can get the latest frontline Cloud PC accessState and determine whether the frontline Cloud PC is accessible to a user.  If a web client needs to connect to a frontline Cloud PC, the sharedCloudPcAccessState validates the bookmark scenario. If sharedCloudPcAccessState isn't active/activating/standbyMode, the web client shows a bad bookmark.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[frontlineCloudPcAccessState]
        Find more info here: https://learn.microsoft.com/graph/api/cloudpc-getfrontlinecloudpcaccessstate?view=graph-rest-beta
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.frontline_cloud_pc_access_state import FrontlineCloudPcAccessState

        return await self.request_adapter.send_async(request_info, frontlineCloudPcAccessState, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Get the frontlineCloudPcAccessState of a frontline Cloud PC.  This API only supports shared-use licenses. For more information, see cloudPcProvisioningPolicy. Shared-use licenses allow three users per license, with one user signed in at a time. Callers can get the latest frontline Cloud PC accessState and determine whether the frontline Cloud PC is accessible to a user.  If a web client needs to connect to a frontline Cloud PC, the sharedCloudPcAccessState validates the bookmark scenario. If sharedCloudPcAccessState isn't active/activating/standbyMode, the web client shows a bad bookmark.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> GetFrontlineCloudPcAccessStateRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GetFrontlineCloudPcAccessStateRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GetFrontlineCloudPcAccessStateRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class GetFrontlineCloudPcAccessStateRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

