from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import planner_roster
    from ....models.o_data_errors import o_data_error
    from .members import members_request_builder
    from .members.item import planner_roster_member_item_request_builder
    from .plans import plans_request_builder
    from .plans.item import planner_plan_item_request_builder

class PlannerRosterItemRequestBuilder():
    """
    Provides operations to manage the rosters property of the microsoft.graph.planner entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PlannerRosterItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/planner/rosters/{plannerRoster%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[PlannerRosterItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property rosters for planner
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[PlannerRosterItemRequestBuilderGetRequestConfiguration] = None) -> Optional[planner_roster.PlannerRoster]:
        """
        Read-only. Nullable. Returns a collection of the specified rosters
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[planner_roster.PlannerRoster]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import planner_roster

        return await self.request_adapter.send_async(request_info, planner_roster.PlannerRoster, error_mapping)
    
    def members_by_id(self,id: str) -> planner_roster_member_item_request_builder.PlannerRosterMemberItemRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.plannerRoster entity.
        Args:
            id: Unique identifier of the item
        Returns: planner_roster_member_item_request_builder.PlannerRosterMemberItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .members.item import planner_roster_member_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["plannerRosterMember%2Did"] = id
        return planner_roster_member_item_request_builder.PlannerRosterMemberItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[planner_roster.PlannerRoster] = None, request_configuration: Optional[PlannerRosterItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[planner_roster.PlannerRoster]:
        """
        Update the navigation property rosters in planner
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[planner_roster.PlannerRoster]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import planner_roster

        return await self.request_adapter.send_async(request_info, planner_roster.PlannerRoster, error_mapping)
    
    def plans_by_id(self,id: str) -> planner_plan_item_request_builder.PlannerPlanItemRequestBuilder:
        """
        Provides operations to manage the plans property of the microsoft.graph.plannerRoster entity.
        Args:
            id: Unique identifier of the item
        Returns: planner_plan_item_request_builder.PlannerPlanItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .plans.item import planner_plan_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["plannerPlan%2Did"] = id
        return planner_plan_item_request_builder.PlannerPlanItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[PlannerRosterItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property rosters for planner
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
    
    def to_get_request_information(self,request_configuration: Optional[PlannerRosterItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read-only. Nullable. Returns a collection of the specified rosters
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
    
    def to_patch_request_information(self,body: Optional[planner_roster.PlannerRoster] = None, request_configuration: Optional[PlannerRosterItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property rosters in planner
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def members(self) -> members_request_builder.MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.plannerRoster entity.
        """
        from .members import members_request_builder

        return members_request_builder.MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plans(self) -> plans_request_builder.PlansRequestBuilder:
        """
        Provides operations to manage the plans property of the microsoft.graph.plannerRoster entity.
        """
        from .plans import plans_request_builder

        return plans_request_builder.PlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PlannerRosterItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PlannerRosterItemRequestBuilderGetQueryParameters():
        """
        Read-only. Nullable. Returns a collection of the specified rosters
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class PlannerRosterItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PlannerRosterItemRequestBuilder.PlannerRosterItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PlannerRosterItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

