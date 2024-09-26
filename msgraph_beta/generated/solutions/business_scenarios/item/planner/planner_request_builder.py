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
    from .....models.business_scenario_planner import BusinessScenarioPlanner
    from .....models.o_data_errors.o_data_error import ODataError
    from .get_plan.get_plan_request_builder import GetPlanRequestBuilder
    from .plan_configuration.plan_configuration_request_builder import PlanConfigurationRequestBuilder
    from .tasks.tasks_request_builder import TasksRequestBuilder
    from .task_configuration.task_configuration_request_builder import TaskConfigurationRequestBuilder

class PlannerRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the planner property of the microsoft.graph.businessScenario entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PlannerRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/solutions/businessScenarios/{businessScenario%2Did}/planner{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property planner for solutions
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PlannerRequestBuilderGetQueryParameters]] = None) -> Optional[BusinessScenarioPlanner]:
        """
        Read the properties and relationships of a businessScenarioPlanner object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BusinessScenarioPlanner]
        Find more info here: https://learn.microsoft.com/graph/api/businessscenarioplanner-get?view=graph-rest-beta
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.business_scenario_planner import BusinessScenarioPlanner

        return await self.request_adapter.send_async(request_info, BusinessScenarioPlanner, error_mapping)
    
    async def patch(self,body: BusinessScenarioPlanner, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[BusinessScenarioPlanner]:
        """
        Update the navigation property planner in solutions
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BusinessScenarioPlanner]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.business_scenario_planner import BusinessScenarioPlanner

        return await self.request_adapter.send_async(request_info, BusinessScenarioPlanner, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property planner for solutions
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PlannerRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read the properties and relationships of a businessScenarioPlanner object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: BusinessScenarioPlanner, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property planner in solutions
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
    
    def with_url(self,raw_url: str) -> PlannerRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlannerRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PlannerRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def get_plan(self) -> GetPlanRequestBuilder:
        """
        Provides operations to call the getPlan method.
        """
        from .get_plan.get_plan_request_builder import GetPlanRequestBuilder

        return GetPlanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plan_configuration(self) -> PlanConfigurationRequestBuilder:
        """
        Provides operations to manage the planConfiguration property of the microsoft.graph.businessScenarioPlanner entity.
        """
        from .plan_configuration.plan_configuration_request_builder import PlanConfigurationRequestBuilder

        return PlanConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_configuration(self) -> TaskConfigurationRequestBuilder:
        """
        Provides operations to manage the taskConfiguration property of the microsoft.graph.businessScenarioPlanner entity.
        """
        from .task_configuration.task_configuration_request_builder import TaskConfigurationRequestBuilder

        return TaskConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tasks(self) -> TasksRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.businessScenarioPlanner entity.
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
        Read the properties and relationships of a businessScenarioPlanner object.
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
    

