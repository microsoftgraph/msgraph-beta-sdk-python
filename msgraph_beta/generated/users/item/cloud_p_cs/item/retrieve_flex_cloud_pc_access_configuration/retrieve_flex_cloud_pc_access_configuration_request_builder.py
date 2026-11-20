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
    from ......models.cloud_pc_flex_access_configuration import CloudPcFlexAccessConfiguration
    from ......models.o_data_errors.o_data_error import ODataError

class RetrieveFlexCloudPcAccessConfigurationRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the retrieveFlexCloudPcAccessConfiguration method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RetrieveFlexCloudPcAccessConfigurationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/cloudPCs/{cloudPC%2Did}/retrieveFlexCloudPcAccessConfiguration()", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CloudPcFlexAccessConfiguration]:
        """
        Get the current access configuration of a Windows 365 Flex (formerly Windows 365 Frontline) Cloud PC. The cloudPcFlexAccessConfiguration response contains the live accessState of the Cloud PC. Use the /me endpoint to retrieve the access configuration of a Cloud PC that belongs to the signed-in user. An administrator or application can use the /deviceManagement/virtualEndpoint endpoint to retrieve the access configuration of a targeted Cloud PC.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPcFlexAccessConfiguration]
        Find more info here: https://learn.microsoft.com/graph/api/cloudpc-retrieveflexcloudpcaccessconfiguration?view=graph-rest-beta
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.cloud_pc_flex_access_configuration import CloudPcFlexAccessConfiguration

        return await self.request_adapter.send_async(request_info, CloudPcFlexAccessConfiguration, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Get the current access configuration of a Windows 365 Flex (formerly Windows 365 Frontline) Cloud PC. The cloudPcFlexAccessConfiguration response contains the live accessState of the Cloud PC. Use the /me endpoint to retrieve the access configuration of a Cloud PC that belongs to the signed-in user. An administrator or application can use the /deviceManagement/virtualEndpoint endpoint to retrieve the access configuration of a targeted Cloud PC.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> RetrieveFlexCloudPcAccessConfigurationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RetrieveFlexCloudPcAccessConfigurationRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RetrieveFlexCloudPcAccessConfigurationRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class RetrieveFlexCloudPcAccessConfigurationRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

