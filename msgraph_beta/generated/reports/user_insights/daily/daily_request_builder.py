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
    from ....models.daily_user_insight_metrics_root import DailyUserInsightMetricsRoot
    from ....models.o_data_errors.o_data_error import ODataError
    from .active_users.active_users_request_builder import ActiveUsersRequestBuilder
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
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new DailyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/reports/userInsights/daily{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property daily for reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DailyRequestBuilderGetQueryParameters]] = None) -> Optional[DailyUserInsightMetricsRoot]:
        """
        Summaries of daily user activities on apps registered in your tenant that is configured for Microsoft Entra External ID for customers.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DailyUserInsightMetricsRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.daily_user_insight_metrics_root import DailyUserInsightMetricsRoot

        return await self.request_adapter.send_async(request_info, DailyUserInsightMetricsRoot, error_mapping)
    
    async def patch(self,body: DailyUserInsightMetricsRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DailyUserInsightMetricsRoot]:
        """
        Update the navigation property daily in reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DailyUserInsightMetricsRoot]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.daily_user_insight_metrics_root import DailyUserInsightMetricsRoot

        return await self.request_adapter.send_async(request_info, DailyUserInsightMetricsRoot, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property daily for reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DailyRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Summaries of daily user activities on apps registered in your tenant that is configured for Microsoft Entra External ID for customers.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DailyUserInsightMetricsRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property daily in reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> DailyRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DailyRequestBuilder
        """
        if raw_url is None:
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
    
    @dataclass
    class DailyRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DailyRequestBuilderGetQueryParameters():
        """
        Summaries of daily user activities on apps registered in your tenant that is configured for Microsoft Entra External ID for customers.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
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
    class DailyRequestBuilderGetRequestConfiguration(RequestConfiguration[DailyRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DailyRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

