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
    from ......models.application import Application
    from ......models.o_data_errors.o_data_error import ODataError

class ApplicationsWithAppIdRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the applications property of the microsoft.graph.connectorGroup entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]], app_id: Optional[str] = None) -> None:
        """
        Instantiates a new ApplicationsWithAppIdRequestBuilder and sets the default values.
        param app_id: Alternate key of application
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['appId'] = str(app_id)
        super().__init__(request_adapter, "{+baseurl}/onPremisesPublishingProfiles/{onPremisesPublishingProfile%2Did}/connectorGroups/{connectorGroup%2Did}/applications(appId='{appId}'){?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[ApplicationsWithAppIdRequestBuilderGetRequestConfiguration] = None) -> Optional[Application]:
        """
        Get applications from onPremisesPublishingProfiles
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Application]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.application import Application

        return await self.request_adapter.send_async(request_info, Application, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[ApplicationsWithAppIdRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get applications from onPremisesPublishingProfiles
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ApplicationsWithAppIdRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ApplicationsWithAppIdRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ApplicationsWithAppIdRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ApplicationsWithAppIdRequestBuilderGetQueryParameters():
        """
        Get applications from onPremisesPublishingProfiles
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ApplicationsWithAppIdRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ApplicationsWithAppIdRequestBuilder.ApplicationsWithAppIdRequestBuilderGetQueryParameters] = None

    

