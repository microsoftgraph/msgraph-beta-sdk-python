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
    from ....models.daily_user_insight_metrics_root import DailyUserInsightMetricsRoot
    from ....models.o_data_errors.o_data_error import ODataError
    from .active_users.active_users_request_builder import ActiveUsersRequestBuilder
    from .active_users_breakdown.active_users_breakdown_request_builder import ActiveUsersBreakdownRequestBuilder
    from .authentications.authentications_request_builder import AuthenticationsRequestBuilder
    from .inactive_users.inactive_users_request_builder import InactiveUsersRequestBuilder
    from .inactive_users_by_application.inactive_users_by_application_request_builder import InactiveUsersByApplicationRequestBuilder
    from .mfa_completions.mfa_completions_request_builder import MfaCompletionsRequestBuilder
    from .sign_ups.sign_ups_request_builder import SignUpsRequestBuilder
    from .summary.summary_request_builder import SummaryRequestBuilder
    from .user_count.user_count_request_builder import UserCountRequestBuilder

class DailyRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the daily property of the microsoft.graph.userInsightsRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DailyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/reports/userInsights/daily{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[DailyRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property daily for reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[DailyRequestBuilderGetRequestConfiguration] = None) -> Optional[DailyUserInsightMetricsRoot]:
        """
        Summaries of daily user activities on apps registered in your tenant that is configured for Microsoft Entra External ID for customers.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DailyUserInsightMetricsRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.daily_user_insight_metrics_root import DailyUserInsightMetricsRoot

        return await self.request_adapter.send_async(request_info, DailyUserInsightMetricsRoot, error_mapping)
    
    async def patch(self,body: Optional[DailyUserInsightMetricsRoot] = None, request_configuration: Optional[DailyRequestBuilderPatchRequestConfiguration] = None) -> Optional[DailyUserInsightMetricsRoot]:
        """
        Update the navigation property daily in reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DailyUserInsightMetricsRoot]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.daily_user_insight_metrics_root import DailyUserInsightMetricsRoot

        return await self.request_adapter.send_async(request_info, DailyUserInsightMetricsRoot, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[DailyRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property daily for reports
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
    
    def to_get_request_information(self,request_configuration: Optional[DailyRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Summaries of daily user activities on apps registered in your tenant that is configured for Microsoft Entra External ID for customers.
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
    
    def to_patch_request_information(self,body: Optional[DailyUserInsightMetricsRoot] = None, request_configuration: Optional[DailyRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property daily in reports
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
    
    def with_url(self,raw_url: Optional[str] = None) -> DailyRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DailyRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return DailyRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def active_users(self) -> ActiveUsersRequestBuilder:
        """
        Provides operations to manage the activeUsers property of the microsoft.graph.dailyUserInsightMetricsRoot entity.
        """
        from .active_users.active_users_request_builder import ActiveUsersRequestBuilder

        return ActiveUsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def active_users_breakdown(self) -> ActiveUsersBreakdownRequestBuilder:
        """
        Provides operations to manage the activeUsersBreakdown property of the microsoft.graph.dailyUserInsightMetricsRoot entity.
        """
        from .active_users_breakdown.active_users_breakdown_request_builder import ActiveUsersBreakdownRequestBuilder

        return ActiveUsersBreakdownRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentications(self) -> AuthenticationsRequestBuilder:
        """
        Provides operations to manage the authentications property of the microsoft.graph.dailyUserInsightMetricsRoot entity.
        """
        from .authentications.authentications_request_builder import AuthenticationsRequestBuilder

        return AuthenticationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inactive_users(self) -> InactiveUsersRequestBuilder:
        """
        Provides operations to manage the inactiveUsers property of the microsoft.graph.dailyUserInsightMetricsRoot entity.
        """
        from .inactive_users.inactive_users_request_builder import InactiveUsersRequestBuilder

        return InactiveUsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inactive_users_by_application(self) -> InactiveUsersByApplicationRequestBuilder:
        """
        Provides operations to manage the inactiveUsersByApplication property of the microsoft.graph.dailyUserInsightMetricsRoot entity.
        """
        from .inactive_users_by_application.inactive_users_by_application_request_builder import InactiveUsersByApplicationRequestBuilder

        return InactiveUsersByApplicationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mfa_completions(self) -> MfaCompletionsRequestBuilder:
        """
        Provides operations to manage the mfaCompletions property of the microsoft.graph.dailyUserInsightMetricsRoot entity.
        """
        from .mfa_completions.mfa_completions_request_builder import MfaCompletionsRequestBuilder

        return MfaCompletionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sign_ups(self) -> SignUpsRequestBuilder:
        """
        Provides operations to manage the signUps property of the microsoft.graph.dailyUserInsightMetricsRoot entity.
        """
        from .sign_ups.sign_ups_request_builder import SignUpsRequestBuilder

        return SignUpsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def summary(self) -> SummaryRequestBuilder:
        """
        Provides operations to manage the summary property of the microsoft.graph.dailyUserInsightMetricsRoot entity.
        """
        from .summary.summary_request_builder import SummaryRequestBuilder

        return SummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_count(self) -> UserCountRequestBuilder:
        """
        Provides operations to manage the userCount property of the microsoft.graph.dailyUserInsightMetricsRoot entity.
        """
        from .user_count.user_count_request_builder import UserCountRequestBuilder

        return UserCountRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DailyRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class DailyRequestBuilderGetQueryParameters():
        """
        Summaries of daily user activities on apps registered in your tenant that is configured for Microsoft Entra External ID for customers.
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
    class DailyRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[DailyRequestBuilder.DailyRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DailyRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

