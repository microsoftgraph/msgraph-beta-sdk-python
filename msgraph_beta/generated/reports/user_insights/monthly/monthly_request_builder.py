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
    from ....models.monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot
    from ....models.o_data_errors.o_data_error import ODataError
    from .active_users.active_users_request_builder import ActiveUsersRequestBuilder
    from .authentications.authentications_request_builder import AuthenticationsRequestBuilder
    from .inactive_users.inactive_users_request_builder import InactiveUsersRequestBuilder
    from .inactive_users_by_application.inactive_users_by_application_request_builder import InactiveUsersByApplicationRequestBuilder
    from .mfa_completions.mfa_completions_request_builder import MfaCompletionsRequestBuilder
    from .requests.requests_request_builder import RequestsRequestBuilder
    from .sign_ups.sign_ups_request_builder import SignUpsRequestBuilder
    from .summary.summary_request_builder import SummaryRequestBuilder

class MonthlyRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the monthly property of the microsoft.graph.userInsightsRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new MonthlyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/reports/userInsights/monthly{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property monthly for reports
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MonthlyRequestBuilderGetQueryParameters]] = None) -> Optional[MonthlyUserInsightMetricsRoot]:
        """
        Summaries of monthly user activities on apps registered in your tenant that is configured for Microsoft Entra External ID for customers.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MonthlyUserInsightMetricsRoot]
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
        from ....models.monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot

        return await self.request_adapter.send_async(request_info, MonthlyUserInsightMetricsRoot, error_mapping)
    
    async def patch(self,body: MonthlyUserInsightMetricsRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MonthlyUserInsightMetricsRoot]:
        """
        Update the navigation property monthly in reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MonthlyUserInsightMetricsRoot]
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
        from ....models.monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot

        return await self.request_adapter.send_async(request_info, MonthlyUserInsightMetricsRoot, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property monthly for reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MonthlyRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Summaries of monthly user activities on apps registered in your tenant that is configured for Microsoft Entra External ID for customers.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: MonthlyUserInsightMetricsRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property monthly in reports
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
    
    def with_url(self,raw_url: str) -> MonthlyRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MonthlyRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MonthlyRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def active_users(self) -> ActiveUsersRequestBuilder:
        """
        Provides operations to manage the activeUsers property of the microsoft.graph.monthlyUserInsightMetricsRoot entity.
        """
        from .active_users.active_users_request_builder import ActiveUsersRequestBuilder

        return ActiveUsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentications(self) -> AuthenticationsRequestBuilder:
        """
        Provides operations to manage the authentications property of the microsoft.graph.monthlyUserInsightMetricsRoot entity.
        """
        from .authentications.authentications_request_builder import AuthenticationsRequestBuilder

        return AuthenticationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inactive_users(self) -> InactiveUsersRequestBuilder:
        """
        Provides operations to manage the inactiveUsers property of the microsoft.graph.monthlyUserInsightMetricsRoot entity.
        """
        from .inactive_users.inactive_users_request_builder import InactiveUsersRequestBuilder

        return InactiveUsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inactive_users_by_application(self) -> InactiveUsersByApplicationRequestBuilder:
        """
        Provides operations to manage the inactiveUsersByApplication property of the microsoft.graph.monthlyUserInsightMetricsRoot entity.
        """
        from .inactive_users_by_application.inactive_users_by_application_request_builder import InactiveUsersByApplicationRequestBuilder

        return InactiveUsersByApplicationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mfa_completions(self) -> MfaCompletionsRequestBuilder:
        """
        Provides operations to manage the mfaCompletions property of the microsoft.graph.monthlyUserInsightMetricsRoot entity.
        """
        from .mfa_completions.mfa_completions_request_builder import MfaCompletionsRequestBuilder

        return MfaCompletionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def requests(self) -> RequestsRequestBuilder:
        """
        Provides operations to manage the requests property of the microsoft.graph.monthlyUserInsightMetricsRoot entity.
        """
        from .requests.requests_request_builder import RequestsRequestBuilder

        return RequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sign_ups(self) -> SignUpsRequestBuilder:
        """
        Provides operations to manage the signUps property of the microsoft.graph.monthlyUserInsightMetricsRoot entity.
        """
        from .sign_ups.sign_ups_request_builder import SignUpsRequestBuilder

        return SignUpsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def summary(self) -> SummaryRequestBuilder:
        """
        Provides operations to manage the summary property of the microsoft.graph.monthlyUserInsightMetricsRoot entity.
        """
        from .summary.summary_request_builder import SummaryRequestBuilder

        return SummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MonthlyRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MonthlyRequestBuilderGetQueryParameters():
        """
        Summaries of monthly user activities on apps registered in your tenant that is configured for Microsoft Entra External ID for customers.
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
    class MonthlyRequestBuilderGetRequestConfiguration(RequestConfiguration[MonthlyRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MonthlyRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

