from __future__ import annotations
import datetime
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
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.service_activity import ServiceActivity
    from .get_metrics_for_conditional_access_compliant_devices_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes.get_metrics_for_conditional_access_compliant_devices_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes_request_builder import GetMetricsForConditionalAccessCompliantDevicesSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder
    from .get_metrics_for_conditional_access_managed_devices_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes.get_metrics_for_conditional_access_managed_devices_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes_request_builder import GetMetricsForConditionalAccessManagedDevicesSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder
    from .get_metrics_for_mfa_sign_in_failure_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes.get_metrics_for_mfa_sign_in_failure_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes_request_builder import GetMetricsForMfaSignInFailureWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder
    from .get_metrics_for_mfa_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes.get_metrics_for_mfa_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes_request_builder import GetMetricsForMfaSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder
    from .get_metrics_for_saml_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes.get_metrics_for_saml_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes_request_builder import GetMetricsForSamlSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder

class ServiceActivityRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the serviceActivity property of the microsoft.graph.reportRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ServiceActivityRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/reports/serviceActivity{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[ServiceActivityRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property serviceActivity for reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ServiceActivityRequestBuilderGetRequestConfiguration] = None) -> Optional[ServiceActivity]:
        """
        A placeholder to the Microsoft Entra service activity.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ServiceActivity]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.service_activity import ServiceActivity

        return await self.request_adapter.send_async(request_info, ServiceActivity, error_mapping)
    
    def get_metrics_for_conditional_access_compliant_devices_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: Optional[datetime.datetime] = None, inclusive_interval_start_date_time: Optional[datetime.datetime] = None) -> GetMetricsForConditionalAccessCompliantDevicesSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder:
        """
        Provides operations to call the getMetricsForConditionalAccessCompliantDevicesSignInSuccess method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForConditionalAccessCompliantDevicesSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder
        """
        if not exclusive_interval_end_date_time:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if not inclusive_interval_start_date_time:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_conditional_access_compliant_devices_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes.get_metrics_for_conditional_access_compliant_devices_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes_request_builder import GetMetricsForConditionalAccessCompliantDevicesSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder

        return GetMetricsForConditionalAccessCompliantDevicesSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_conditional_access_managed_devices_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: Optional[datetime.datetime] = None, inclusive_interval_start_date_time: Optional[datetime.datetime] = None) -> GetMetricsForConditionalAccessManagedDevicesSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder:
        """
        Provides operations to call the getMetricsForConditionalAccessManagedDevicesSignInSuccess method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForConditionalAccessManagedDevicesSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder
        """
        if not exclusive_interval_end_date_time:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if not inclusive_interval_start_date_time:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_conditional_access_managed_devices_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes.get_metrics_for_conditional_access_managed_devices_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes_request_builder import GetMetricsForConditionalAccessManagedDevicesSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder

        return GetMetricsForConditionalAccessManagedDevicesSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_mfa_sign_in_failure_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: Optional[datetime.datetime] = None, inclusive_interval_start_date_time: Optional[datetime.datetime] = None) -> GetMetricsForMfaSignInFailureWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder:
        """
        Provides operations to call the getMetricsForMfaSignInFailure method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForMfaSignInFailureWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder
        """
        if not exclusive_interval_end_date_time:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if not inclusive_interval_start_date_time:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_mfa_sign_in_failure_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes.get_metrics_for_mfa_sign_in_failure_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes_request_builder import GetMetricsForMfaSignInFailureWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder

        return GetMetricsForMfaSignInFailureWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_mfa_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: Optional[datetime.datetime] = None, inclusive_interval_start_date_time: Optional[datetime.datetime] = None) -> GetMetricsForMfaSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder:
        """
        Provides operations to call the getMetricsForMfaSignInSuccess method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForMfaSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder
        """
        if not exclusive_interval_end_date_time:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if not inclusive_interval_start_date_time:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_mfa_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes.get_metrics_for_mfa_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes_request_builder import GetMetricsForMfaSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder

        return GetMetricsForMfaSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_saml_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: Optional[datetime.datetime] = None, inclusive_interval_start_date_time: Optional[datetime.datetime] = None) -> GetMetricsForSamlSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder:
        """
        Provides operations to call the getMetricsForSamlSignInSuccess method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForSamlSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder
        """
        if not exclusive_interval_end_date_time:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if not inclusive_interval_start_date_time:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_saml_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes.get_metrics_for_saml_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes_request_builder import GetMetricsForSamlSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder

        return GetMetricsForSamlSignInSuccessWithInclusiveIntervalStartDateTimeWithExclusiveIntervalEndDateTimeWithAggregationIntervalInMinutesRequestBuilder(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    async def patch(self,body: Optional[ServiceActivity] = None, request_configuration: Optional[ServiceActivityRequestBuilderPatchRequestConfiguration] = None) -> Optional[ServiceActivity]:
        """
        Update the navigation property serviceActivity in reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ServiceActivity]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.service_activity import ServiceActivity

        return await self.request_adapter.send_async(request_info, ServiceActivity, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ServiceActivityRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property serviceActivity for reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[ServiceActivityRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A placeholder to the Microsoft Entra service activity.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[ServiceActivity] = None, request_configuration: Optional[ServiceActivityRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property serviceActivity in reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ServiceActivityRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ServiceActivityRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ServiceActivityRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ServiceActivityRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class ServiceActivityRequestBuilderGetQueryParameters():
        """
        A placeholder to the Microsoft Entra service activity.
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
    class ServiceActivityRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ServiceActivityRequestBuilder.ServiceActivityRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ServiceActivityRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

