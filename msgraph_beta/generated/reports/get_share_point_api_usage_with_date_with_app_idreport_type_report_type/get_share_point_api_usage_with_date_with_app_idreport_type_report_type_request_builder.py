from __future__ import annotations
import datetime
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

class GetSharePointApiUsageWithDateWithAppIdreportTypeReportTypeRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getSharePointApiUsage method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]], app_id: Optional[str] = None, date: Optional[datetime.datetime] = None) -> None:
        """
        Instantiates a new GetSharePointApiUsageWithDateWithAppIdreportTypeReportTypeRequestBuilder and sets the default values.
        param app_id: Usage: appId='{appId}'
        param date: Usage: date={date}
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['appId'] = app_id
            path_parameters['date'] = date
        super().__init__(request_adapter, "{+baseurl}/reports/getSharePointApiUsage(date={date},appId='{appId}',reportType='@reportType'){?reportType*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[GetSharePointApiUsageWithDateWithAppIdreportTypeReportTypeRequestBuilderGetQueryParameters]] = None) -> Optional[bytes]:
        """
        Get aggregated usage data for all applications in a tenant. Specify either a period or a date, but not both. Optionally filter the results by application ID. Data is returned in CSV format by default, or in JSON format when requested through the $format query parameter. Use the optional reportType parameter to choose which usage metrics to return: egressReport (default) includes usage (UsageMB in CSV, usageMB in JSON), and throttlingReport includes throttled request counts (ThrottledRequests in CSV, throttledRequests in JSON). Each report type must be enabled (onboarded) for the tenant before its data is available. Use enableApiUsageReport to enable a report metric, disableApiUsageReport to disable it, and List apiUsageReportMetrics to check the enablement status. If you request a report type that isn't enabled for the tenant, this method returns a 403 Forbidden response with the error code accessDenied and the message 'Tenant is not enabled for this report type.' CSV column headers use PascalCase (ThrottledRequests) while JSON properties use camelCase (throttledRequests) to maintain consistency with other Microsoft Graph reporting APIs.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        Find more info here: https://learn.microsoft.com/graph/api/reportroot-getsharepointapiusage?view=graph-rest-beta
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
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[GetSharePointApiUsageWithDateWithAppIdreportTypeReportTypeRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get aggregated usage data for all applications in a tenant. Specify either a period or a date, but not both. Optionally filter the results by application ID. Data is returned in CSV format by default, or in JSON format when requested through the $format query parameter. Use the optional reportType parameter to choose which usage metrics to return: egressReport (default) includes usage (UsageMB in CSV, usageMB in JSON), and throttlingReport includes throttled request counts (ThrottledRequests in CSV, throttledRequests in JSON). Each report type must be enabled (onboarded) for the tenant before its data is available. Use enableApiUsageReport to enable a report metric, disableApiUsageReport to disable it, and List apiUsageReportMetrics to check the enablement status. If you request a report type that isn't enabled for the tenant, this method returns a 403 Forbidden response with the error code accessDenied and the message 'Tenant is not enabled for this report type.' CSV column headers use PascalCase (ThrottledRequests) while JSON properties use camelCase (throttledRequests) to maintain consistency with other Microsoft Graph reporting APIs.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/octet-stream, application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> GetSharePointApiUsageWithDateWithAppIdreportTypeReportTypeRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GetSharePointApiUsageWithDateWithAppIdreportTypeReportTypeRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GetSharePointApiUsageWithDateWithAppIdreportTypeReportTypeRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class GetSharePointApiUsageWithDateWithAppIdreportTypeReportTypeRequestBuilderGetQueryParameters():
        """
        Get aggregated usage data for all applications in a tenant. Specify either a period or a date, but not both. Optionally filter the results by application ID. Data is returned in CSV format by default, or in JSON format when requested through the $format query parameter. Use the optional reportType parameter to choose which usage metrics to return: egressReport (default) includes usage (UsageMB in CSV, usageMB in JSON), and throttlingReport includes throttled request counts (ThrottledRequests in CSV, throttledRequests in JSON). Each report type must be enabled (onboarded) for the tenant before its data is available. Use enableApiUsageReport to enable a report metric, disableApiUsageReport to disable it, and List apiUsageReportMetrics to check the enablement status. If you request a report type that isn't enabled for the tenant, this method returns a 403 Forbidden response with the error code accessDenied and the message 'Tenant is not enabled for this report type.' CSV column headers use PascalCase (ThrottledRequests) while JSON properties use camelCase (throttledRequests) to maintain consistency with other Microsoft Graph reporting APIs.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "report_type":
                return "reportType"
            return original_name
        
        # Usage: reportType='@reportType'
        report_type: Optional[str] = None

    
    @dataclass
    class GetSharePointApiUsageWithDateWithAppIdreportTypeReportTypeRequestBuilderGetRequestConfiguration(RequestConfiguration[GetSharePointApiUsageWithDateWithAppIdreportTypeReportTypeRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

