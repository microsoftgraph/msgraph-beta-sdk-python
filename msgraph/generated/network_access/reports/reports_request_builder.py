from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.networkaccess import reports
    from ...models.o_data_errors import o_data_error
    from .microsoft_graph_networkaccess_entities_summaries_with_start_date_time_with_end_date_time import microsoft_graph_networkaccess_entities_summaries_with_start_date_time_with_end_date_time_request_builder
    from .microsoft_graph_networkaccess_get_cross_tenant_summary_with_start_date_time_with_end_date_time_with_discovery_pivot_date_time import microsoft_graph_networkaccess_get_cross_tenant_summary_with_start_date_time_with_end_date_time_with_discovery_pivot_date_time_request_builder
    from .microsoft_graph_networkaccess_get_destination_summaries_with_start_date_time_with_end_date_time_with_aggregated_by import microsoft_graph_networkaccess_get_destination_summaries_with_start_date_time_with_end_date_time_with_aggregated_by_request_builder
    from .microsoft_graph_networkaccess_get_device_usage_summary_with_start_date_time_with_end_date_time_with_activity_pivot_date_time import microsoft_graph_networkaccess_get_device_usage_summary_with_start_date_time_with_end_date_time_with_activity_pivot_date_time_request_builder
    from .microsoft_graph_networkaccess_transaction_summaries_with_start_date_time_with_end_date_time import microsoft_graph_networkaccess_transaction_summaries_with_start_date_time_with_end_date_time_request_builder

class ReportsRequestBuilder():
    """
    Provides operations to manage the reports property of the microsoft.graph.networkaccess.networkAccessRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ReportsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/networkAccess/reports{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property reports for networkAccess
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> Optional[reports.Reports]:
        """
        Get reports from networkAccess
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[reports.Reports]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.networkaccess import reports

        return await self.request_adapter.send_async(request_info, reports.Reports, error_mapping)
    
    def microsoft_graph_networkaccess_entities_summaries_with_start_date_time_with_end_date_time(self,end_date_time: Optional[datetime] = None, start_date_time: Optional[datetime] = None) -> microsoft_graph_networkaccess_entities_summaries_with_start_date_time_with_end_date_time_request_builder.MicrosoftGraphNetworkaccessEntitiesSummariesWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the entitiesSummaries method.
        Args:
            endDateTime: Usage: endDateTime={endDateTime}
            startDateTime: Usage: startDateTime={startDateTime}
        Returns: microsoft_graph_networkaccess_entities_summaries_with_start_date_time_with_end_date_time_request_builder.MicrosoftGraphNetworkaccessEntitiesSummariesWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if not end_date_time:
            raise TypeError("end_date_time cannot be null.")
        if not start_date_time:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_entities_summaries_with_start_date_time_with_end_date_time import microsoft_graph_networkaccess_entities_summaries_with_start_date_time_with_end_date_time_request_builder

        return microsoft_graph_networkaccess_entities_summaries_with_start_date_time_with_end_date_time_request_builder.MicrosoftGraphNetworkaccessEntitiesSummariesWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_get_cross_tenant_summary_with_start_date_time_with_end_date_time_with_discovery_pivot_date_time(self,discovery_pivot_date_time: Optional[datetime] = None, end_date_time: Optional[datetime] = None, start_date_time: Optional[datetime] = None) -> microsoft_graph_networkaccess_get_cross_tenant_summary_with_start_date_time_with_end_date_time_with_discovery_pivot_date_time_request_builder.MicrosoftGraphNetworkaccessGetCrossTenantSummaryWithStartDateTimeWithEndDateTimeWithDiscoveryPivotDateTimeRequestBuilder:
        """
        Provides operations to call the getCrossTenantSummary method.
        Args:
            discoveryPivotDateTime: Usage: discoveryPivotDateTime={discoveryPivotDateTime}
            endDateTime: Usage: endDateTime={endDateTime}
            startDateTime: Usage: startDateTime={startDateTime}
        Returns: microsoft_graph_networkaccess_get_cross_tenant_summary_with_start_date_time_with_end_date_time_with_discovery_pivot_date_time_request_builder.MicrosoftGraphNetworkaccessGetCrossTenantSummaryWithStartDateTimeWithEndDateTimeWithDiscoveryPivotDateTimeRequestBuilder
        """
        if not discovery_pivot_date_time:
            raise TypeError("discovery_pivot_date_time cannot be null.")
        if not end_date_time:
            raise TypeError("end_date_time cannot be null.")
        if not start_date_time:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_get_cross_tenant_summary_with_start_date_time_with_end_date_time_with_discovery_pivot_date_time import microsoft_graph_networkaccess_get_cross_tenant_summary_with_start_date_time_with_end_date_time_with_discovery_pivot_date_time_request_builder

        return microsoft_graph_networkaccess_get_cross_tenant_summary_with_start_date_time_with_end_date_time_with_discovery_pivot_date_time_request_builder.MicrosoftGraphNetworkaccessGetCrossTenantSummaryWithStartDateTimeWithEndDateTimeWithDiscoveryPivotDateTimeRequestBuilder(self.request_adapter, self.path_parameters, discovery_pivot_date_time, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_get_destination_summaries_with_start_date_time_with_end_date_time_with_aggregated_by(self,aggregated_by: Optional[str] = None, end_date_time: Optional[datetime] = None, start_date_time: Optional[datetime] = None) -> microsoft_graph_networkaccess_get_destination_summaries_with_start_date_time_with_end_date_time_with_aggregated_by_request_builder.MicrosoftGraphNetworkaccessGetDestinationSummariesWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilder:
        """
        Provides operations to call the getDestinationSummaries method.
        Args:
            aggregatedBy: Usage: aggregatedBy='{aggregatedBy}'
            endDateTime: Usage: endDateTime={endDateTime}
            startDateTime: Usage: startDateTime={startDateTime}
        Returns: microsoft_graph_networkaccess_get_destination_summaries_with_start_date_time_with_end_date_time_with_aggregated_by_request_builder.MicrosoftGraphNetworkaccessGetDestinationSummariesWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilder
        """
        if not aggregated_by:
            raise TypeError("aggregated_by cannot be null.")
        if not end_date_time:
            raise TypeError("end_date_time cannot be null.")
        if not start_date_time:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_get_destination_summaries_with_start_date_time_with_end_date_time_with_aggregated_by import microsoft_graph_networkaccess_get_destination_summaries_with_start_date_time_with_end_date_time_with_aggregated_by_request_builder

        return microsoft_graph_networkaccess_get_destination_summaries_with_start_date_time_with_end_date_time_with_aggregated_by_request_builder.MicrosoftGraphNetworkaccessGetDestinationSummariesWithStartDateTimeWithEndDateTimeWithAggregatedByRequestBuilder(self.request_adapter, self.path_parameters, aggregated_by, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_get_device_usage_summary_with_start_date_time_with_end_date_time_with_activity_pivot_date_time(self,activity_pivot_date_time: Optional[datetime] = None, end_date_time: Optional[datetime] = None, start_date_time: Optional[datetime] = None) -> microsoft_graph_networkaccess_get_device_usage_summary_with_start_date_time_with_end_date_time_with_activity_pivot_date_time_request_builder.MicrosoftGraphNetworkaccessGetDeviceUsageSummaryWithStartDateTimeWithEndDateTimeWithActivityPivotDateTimeRequestBuilder:
        """
        Provides operations to call the getDeviceUsageSummary method.
        Args:
            activityPivotDateTime: Usage: activityPivotDateTime={activityPivotDateTime}
            endDateTime: Usage: endDateTime={endDateTime}
            startDateTime: Usage: startDateTime={startDateTime}
        Returns: microsoft_graph_networkaccess_get_device_usage_summary_with_start_date_time_with_end_date_time_with_activity_pivot_date_time_request_builder.MicrosoftGraphNetworkaccessGetDeviceUsageSummaryWithStartDateTimeWithEndDateTimeWithActivityPivotDateTimeRequestBuilder
        """
        if not activity_pivot_date_time:
            raise TypeError("activity_pivot_date_time cannot be null.")
        if not end_date_time:
            raise TypeError("end_date_time cannot be null.")
        if not start_date_time:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_get_device_usage_summary_with_start_date_time_with_end_date_time_with_activity_pivot_date_time import microsoft_graph_networkaccess_get_device_usage_summary_with_start_date_time_with_end_date_time_with_activity_pivot_date_time_request_builder

        return microsoft_graph_networkaccess_get_device_usage_summary_with_start_date_time_with_end_date_time_with_activity_pivot_date_time_request_builder.MicrosoftGraphNetworkaccessGetDeviceUsageSummaryWithStartDateTimeWithEndDateTimeWithActivityPivotDateTimeRequestBuilder(self.request_adapter, self.path_parameters, activity_pivot_date_time, end_date_time, start_date_time)
    
    def microsoft_graph_networkaccess_transaction_summaries_with_start_date_time_with_end_date_time(self,end_date_time: Optional[datetime] = None, start_date_time: Optional[datetime] = None) -> microsoft_graph_networkaccess_transaction_summaries_with_start_date_time_with_end_date_time_request_builder.MicrosoftGraphNetworkaccessTransactionSummariesWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the transactionSummaries method.
        Args:
            endDateTime: Usage: endDateTime={endDateTime}
            startDateTime: Usage: startDateTime={startDateTime}
        Returns: microsoft_graph_networkaccess_transaction_summaries_with_start_date_time_with_end_date_time_request_builder.MicrosoftGraphNetworkaccessTransactionSummariesWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if not end_date_time:
            raise TypeError("end_date_time cannot be null.")
        if not start_date_time:
            raise TypeError("start_date_time cannot be null.")
        from .microsoft_graph_networkaccess_transaction_summaries_with_start_date_time_with_end_date_time import microsoft_graph_networkaccess_transaction_summaries_with_start_date_time_with_end_date_time_request_builder

        return microsoft_graph_networkaccess_transaction_summaries_with_start_date_time_with_end_date_time_request_builder.MicrosoftGraphNetworkaccessTransactionSummariesWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time)
    
    async def patch(self,body: Optional[reports.Reports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> Optional[reports.Reports]:
        """
        Update the navigation property reports in networkAccess
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[reports.Reports]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.networkaccess import reports

        return await self.request_adapter.send_async(request_info, reports.Reports, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property reports for networkAccess
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get reports from networkAccess
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[reports.Reports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property reports in networkAccess
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class ReportsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Get reports from networkAccess
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
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

    
    @dataclass
    class ReportsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ReportsRequestBuilder.ReportsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ReportsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

