from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

all_request_builder = lazy_import('msgraph.generated.me.planner.all.all_request_builder')
planner_delta_item_request_builder = lazy_import('msgraph.generated.me.planner.all.item.planner_delta_item_request_builder')
favorite_plans_request_builder = lazy_import('msgraph.generated.me.planner.favorite_plans.favorite_plans_request_builder')
planner_plan_item_request_builder = lazy_import('msgraph.generated.me.planner.favorite_plans.item.planner_plan_item_request_builder')
plans_request_builder = lazy_import('msgraph.generated.me.planner.plans.plans_request_builder')
planner_plan_item_request_builder = lazy_import('msgraph.generated.me.planner.plans.item.planner_plan_item_request_builder')
recent_plans_request_builder = lazy_import('msgraph.generated.me.planner.recent_plans.recent_plans_request_builder')
planner_plan_item_request_builder = lazy_import('msgraph.generated.me.planner.recent_plans.item.planner_plan_item_request_builder')
roster_plans_request_builder = lazy_import('msgraph.generated.me.planner.roster_plans.roster_plans_request_builder')
planner_plan_item_request_builder = lazy_import('msgraph.generated.me.planner.roster_plans.item.planner_plan_item_request_builder')
tasks_request_builder = lazy_import('msgraph.generated.me.planner.tasks.tasks_request_builder')
planner_task_item_request_builder = lazy_import('msgraph.generated.me.planner.tasks.item.planner_task_item_request_builder')
planner_user = lazy_import('msgraph.generated.models.planner_user')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class PlannerRequestBuilder():
    """
    Provides operations to manage the planner property of the microsoft.graph.user entity.
    """
    @property
    def all(self) -> all_request_builder.AllRequestBuilder:
        """
        Provides operations to manage the all property of the microsoft.graph.plannerUser entity.
        """
        return all_request_builder.AllRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def favorite_plans(self) -> favorite_plans_request_builder.FavoritePlansRequestBuilder:
        """
        Provides operations to manage the favoritePlans property of the microsoft.graph.plannerUser entity.
        """
        return favorite_plans_request_builder.FavoritePlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plans(self) -> plans_request_builder.PlansRequestBuilder:
        """
        Provides operations to manage the plans property of the microsoft.graph.plannerUser entity.
        """
        return plans_request_builder.PlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recent_plans(self) -> recent_plans_request_builder.RecentPlansRequestBuilder:
        """
        Provides operations to manage the recentPlans property of the microsoft.graph.plannerUser entity.
        """
        return recent_plans_request_builder.RecentPlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def roster_plans(self) -> roster_plans_request_builder.RosterPlansRequestBuilder:
        """
        Provides operations to manage the rosterPlans property of the microsoft.graph.plannerUser entity.
        """
        return roster_plans_request_builder.RosterPlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tasks(self) -> tasks_request_builder.TasksRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.plannerUser entity.
        """
        return tasks_request_builder.TasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    def all_by_id(self,id: str) -> planner_delta_item_request_builder.PlannerDeltaItemRequestBuilder:
        """
        Provides operations to manage the all property of the microsoft.graph.plannerUser entity.
        Args:
            id: Unique identifier of the item
        Returns: planner_delta_item_request_builder.PlannerDeltaItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["plannerDelta%2Did"] = id
        return planner_delta_item_request_builder.PlannerDeltaItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PlannerRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/planner{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[PlannerRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property planner for me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def favorite_plans_by_id(self,id: str) -> planner_plan_item_request_builder.PlannerPlanItemRequestBuilder:
        """
        Provides operations to manage the favoritePlans property of the microsoft.graph.plannerUser entity.
        Args:
            id: Unique identifier of the item
        Returns: planner_plan_item_request_builder.PlannerPlanItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["plannerPlan%2Did"] = id
        return planner_plan_item_request_builder.PlannerPlanItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[PlannerRequestBuilderGetRequestConfiguration] = None) -> Optional[planner_user.PlannerUser]:
        """
        Retrieve the properties and relationships of a plannerUser object. The returned properties include the user's favorite plans and recently viewed plans. 
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[planner_user.PlannerUser]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, planner_user.PlannerUser, error_mapping)
    
    async def patch(self,body: Optional[planner_user.PlannerUser] = None, request_configuration: Optional[PlannerRequestBuilderPatchRequestConfiguration] = None) -> Optional[planner_user.PlannerUser]:
        """
        Update the properties of a plannerUser object. You can use this operation to add or remove plans from a user's favorite plans list, and to indicate which plans the user has recently viewed.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[planner_user.PlannerUser]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, planner_user.PlannerUser, error_mapping)
    
    def plans_by_id(self,id: str) -> planner_plan_item_request_builder.PlannerPlanItemRequestBuilder:
        """
        Provides operations to manage the plans property of the microsoft.graph.plannerUser entity.
        Args:
            id: Unique identifier of the item
        Returns: planner_plan_item_request_builder.PlannerPlanItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["plannerPlan%2Did"] = id
        return planner_plan_item_request_builder.PlannerPlanItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def recent_plans_by_id(self,id: str) -> planner_plan_item_request_builder.PlannerPlanItemRequestBuilder:
        """
        Provides operations to manage the recentPlans property of the microsoft.graph.plannerUser entity.
        Args:
            id: Unique identifier of the item
        Returns: planner_plan_item_request_builder.PlannerPlanItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["plannerPlan%2Did"] = id
        return planner_plan_item_request_builder.PlannerPlanItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def roster_plans_by_id(self,id: str) -> planner_plan_item_request_builder.PlannerPlanItemRequestBuilder:
        """
        Provides operations to manage the rosterPlans property of the microsoft.graph.plannerUser entity.
        Args:
            id: Unique identifier of the item
        Returns: planner_plan_item_request_builder.PlannerPlanItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["plannerPlan%2Did"] = id
        return planner_plan_item_request_builder.PlannerPlanItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tasks_by_id(self,id: str) -> planner_task_item_request_builder.PlannerTaskItemRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.plannerUser entity.
        Args:
            id: Unique identifier of the item
        Returns: planner_task_item_request_builder.PlannerTaskItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["plannerTask%2Did"] = id
        return planner_task_item_request_builder.PlannerTaskItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[PlannerRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property planner for me
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
    
    def to_get_request_information(self,request_configuration: Optional[PlannerRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a plannerUser object. The returned properties include the user's favorite plans and recently viewed plans. 
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[planner_user.PlannerUser] = None, request_configuration: Optional[PlannerRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a plannerUser object. You can use this operation to add or remove plans from a user's favorite plans list, and to indicate which plans the user has recently viewed.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class PlannerRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PlannerRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a plannerUser object. The returned properties include the user's favorite plans and recently viewed plans. 
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class PlannerRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PlannerRequestBuilder.PlannerRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PlannerRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

