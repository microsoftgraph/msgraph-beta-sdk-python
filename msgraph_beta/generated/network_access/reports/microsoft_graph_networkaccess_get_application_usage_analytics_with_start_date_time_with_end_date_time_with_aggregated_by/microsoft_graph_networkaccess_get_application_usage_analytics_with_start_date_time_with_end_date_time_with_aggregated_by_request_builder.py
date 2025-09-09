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
    from ....models.o_data_errors.o_data_error import ODataError
    from .get_application_usage_analytics_with_start_date_time_with_end_date_time_with_aggregated_by_get_response import GetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByGetResponse

class MicrosoftGraphNetworkaccessGetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getApplicationUsageAnalytics method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]], aggregated_by: Optional[str] = None, end_date_time: Optional[datetime.datetime] = None, start_date_time: Optional[datetime.datetime] = None) -> None:
        """
        Instantiates a new MicrosoftGraphNetworkaccessGetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilder and sets the default values.
        param aggregated_by: Usage: aggregatedBy='{aggregatedBy}'
        param end_date_time: Usage: endDateTime={endDateTime}
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['aggregatedBy'] = aggregated_by
            path_parameters['endDateTime'] = end_date_time
            path_parameters['startDateTime'] = start_date_time
        super().__init__(request_adapter, "{+baseurl}/networkAccess/reports/microsoft.graph.networkaccess.getApplicationUsageAnalytics(startDateTime={startDateTime},endDateTime={endDateTime},aggregatedBy='{aggregatedBy}'){?%24count,%24filter,%24search,%24skip,%24top}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MicrosoftGraphNetworkaccessGetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilderGetQueryParameters]] = None) -> Optional[GetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByGetResponse]:
        """
        Get a collection of application usage analytics data points based on aggregated traffic logs for a specified time period, providing daily breakdown of usage between cloud and enterprise applications in Global Secure Access.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByGetResponse]
        Find more info here: https://learn.microsoft.com/graph/api/networkaccess-reports-getapplicationusageanalytics?view=graph-rest-beta
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .get_application_usage_analytics_with_start_date_time_with_end_date_time_with_aggregated_by_get_response import GetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByGetResponse

        return await self.request_adapter.send_async(request_info, GetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MicrosoftGraphNetworkaccessGetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get a collection of application usage analytics data points based on aggregated traffic logs for a specified time period, providing daily breakdown of usage between cloud and enterprise applications in Global Secure Access.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MicrosoftGraphNetworkaccessGetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MicrosoftGraphNetworkaccessGetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MicrosoftGraphNetworkaccessGetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MicrosoftGraphNetworkaccessGetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilderGetQueryParameters():
        """
        Get a collection of application usage analytics data points based on aggregated traffic logs for a specified time period, providing daily breakdown of usage between cloud and enterprise applications in Global Secure Access.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "filter":
                return "%24filter"
            if original_name == "search":
                return "%24search"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class MicrosoftGraphNetworkaccessGetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilderGetRequestConfiguration(RequestConfiguration[MicrosoftGraphNetworkaccessGetApplicationUsageAnalyticsWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

