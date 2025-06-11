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
    from ...models.o_data_errors.o_data_error import ODataError

class GetApiUsageserviceAreaServiceAreaPeriodPeriodAppIdAppIdRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getApiUsage method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new GetApiUsageserviceAreaServiceAreaPeriodPeriodAppIdAppIdRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/reports/getApiUsage(serviceArea='@serviceArea',period='@period',appId='@appId'){?appId*,period*,serviceArea*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[GetApiUsageserviceAreaServiceAreaPeriodPeriodAppIdAppIdRequestBuilderGetQueryParameters]] = None) -> Optional[bytes]:
        """
        Get the tenant and app API usage for Microsoft Graph services.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[GetApiUsageserviceAreaServiceAreaPeriodPeriodAppIdAppIdRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get the tenant and app API usage for Microsoft Graph services.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/octet-stream, application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> GetApiUsageserviceAreaServiceAreaPeriodPeriodAppIdAppIdRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GetApiUsageserviceAreaServiceAreaPeriodPeriodAppIdAppIdRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GetApiUsageserviceAreaServiceAreaPeriodPeriodAppIdAppIdRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class GetApiUsageserviceAreaServiceAreaPeriodPeriodAppIdAppIdRequestBuilderGetQueryParameters():
        """
        Get the tenant and app API usage for Microsoft Graph services.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "app_id":
                return "appId"
            if original_name == "service_area":
                return "serviceArea"
            if original_name == "period":
                return "period"
            return original_name
        
        # Usage: appId='@appId'
        app_id: Optional[str] = None

        # Usage: period='@period'
        period: Optional[str] = None

        # Usage: serviceArea='@serviceArea'
        service_area: Optional[str] = None

    
    @dataclass
    class GetApiUsageserviceAreaServiceAreaPeriodPeriodAppIdAppIdRequestBuilderGetRequestConfiguration(RequestConfiguration[GetApiUsageserviceAreaServiceAreaPeriodPeriodAppIdAppIdRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

