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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.planner_user import PlannerUser
    from .all.all_request_builder import AllRequestBuilder
    from .favorite_plans.favorite_plans_request_builder import FavoritePlansRequestBuilder
    from .my_day_tasks.my_day_tasks_request_builder import MyDayTasksRequestBuilder
    from .plans.plans_request_builder import PlansRequestBuilder
    from .recent_plans.recent_plans_request_builder import RecentPlansRequestBuilder
    from .roster_plans.roster_plans_request_builder import RosterPlansRequestBuilder
    from .tasks.tasks_request_builder import TasksRequestBuilder

class PlannerRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the planner property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PlannerRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/planner{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property planner for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PlannerRequestBuilderGetQueryParameters]] = None) -> Optional[PlannerUser]:
        """
        Selective Planner services available to the user. Read-only. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PlannerUser]
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.planner_user import PlannerUser

        return await self.request_adapter.send_async(request_info, PlannerUser, error_mapping)
    
    async def patch(self,body: PlannerUser, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PlannerUser]:
        """
        Update the navigation property planner in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PlannerUser]
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
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
        from ....models.planner_user import PlannerUser

        return await self.request_adapter.send_async(request_info, PlannerUser, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property planner for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PlannerRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Selective Planner services available to the user. Read-only. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: PlannerUser, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property planner in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> PlannerRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlannerRequestBuilder
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PlannerRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def all(self) -> AllRequestBuilder:
        """
        Provides operations to manage the all property of the microsoft.graph.plannerUser entity.
        """
        from .all.all_request_builder import AllRequestBuilder

        return AllRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def favorite_plans(self) -> FavoritePlansRequestBuilder:
        """
        Provides operations to manage the favoritePlans property of the microsoft.graph.plannerUser entity.
        """
        from .favorite_plans.favorite_plans_request_builder import FavoritePlansRequestBuilder

        return FavoritePlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def my_day_tasks(self) -> MyDayTasksRequestBuilder:
        """
        Provides operations to manage the myDayTasks property of the microsoft.graph.plannerUser entity.
        """
        from .my_day_tasks.my_day_tasks_request_builder import MyDayTasksRequestBuilder

        return MyDayTasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plans(self) -> PlansRequestBuilder:
        """
        Provides operations to manage the plans property of the microsoft.graph.plannerUser entity.
        """
        from .plans.plans_request_builder import PlansRequestBuilder

        return PlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recent_plans(self) -> RecentPlansRequestBuilder:
        """
        Provides operations to manage the recentPlans property of the microsoft.graph.plannerUser entity.
        """
        from .recent_plans.recent_plans_request_builder import RecentPlansRequestBuilder

        return RecentPlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def roster_plans(self) -> RosterPlansRequestBuilder:
        """
        Provides operations to manage the rosterPlans property of the microsoft.graph.plannerUser entity.
        """
        from .roster_plans.roster_plans_request_builder import RosterPlansRequestBuilder

        return RosterPlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tasks(self) -> TasksRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.plannerUser entity.
        """
        from .tasks.tasks_request_builder import TasksRequestBuilder

        return TasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PlannerRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PlannerRequestBuilderGetQueryParameters():
        """
        Selective Planner services available to the user. Read-only. Nullable.
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
    class PlannerRequestBuilderGetRequestConfiguration(RequestConfiguration[PlannerRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PlannerRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

