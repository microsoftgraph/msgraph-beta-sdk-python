from __future__ import annotations
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
    from ....models.plan import Plan
    from .buckets.buckets_request_builder import BucketsRequestBuilder
    from .contexts.contexts_request_builder import ContextsRequestBuilder
    from .custom_field_definitions.custom_field_definitions_request_builder import CustomFieldDefinitionsRequestBuilder
    from .dependencies.dependencies_request_builder import DependenciesRequestBuilder
    from .goals.goals_request_builder import GoalsRequestBuilder
    from .history_items.history_items_request_builder import HistoryItemsRequestBuilder
    from .links.links_request_builder import LinksRequestBuilder
    from .tasks.tasks_request_builder import TasksRequestBuilder

class PlanItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the plans_v2 property of the microsoft.graph.planner entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PlanItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/planner/plans_v2/{plan%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete a plan object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/planneruser-delete-v2?view=graph-rest-beta
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PlanItemRequestBuilderGetQueryParameters]] = None) -> Optional[Plan]:
        """
        Read the properties and relationships of plan object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Plan]
        Find more info here: https://learn.microsoft.com/graph/api/plan-get?view=graph-rest-beta
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
        from ....models.plan import Plan

        return await self.request_adapter.send_async(request_info, Plan, error_mapping)
    
    async def patch(self,body: Plan, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Plan]:
        """
        Update the properties of a plan object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Plan]
        Find more info here: https://learn.microsoft.com/graph/api/plan-update?view=graph-rest-beta
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.plan import Plan

        return await self.request_adapter.send_async(request_info, Plan, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete a plan object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PlanItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read the properties and relationships of plan object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Plan, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of a plan object.
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
    
    def with_url(self,raw_url: str) -> PlanItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlanItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PlanItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def buckets(self) -> BucketsRequestBuilder:
        """
        Provides operations to manage the buckets property of the microsoft.graph.plan entity.
        """
        from .buckets.buckets_request_builder import BucketsRequestBuilder

        return BucketsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contexts(self) -> ContextsRequestBuilder:
        """
        Provides operations to manage the contexts property of the microsoft.graph.plan entity.
        """
        from .contexts.contexts_request_builder import ContextsRequestBuilder

        return ContextsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_field_definitions(self) -> CustomFieldDefinitionsRequestBuilder:
        """
        Provides operations to manage the customFieldDefinitions property of the microsoft.graph.plan entity.
        """
        from .custom_field_definitions.custom_field_definitions_request_builder import CustomFieldDefinitionsRequestBuilder

        return CustomFieldDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dependencies(self) -> DependenciesRequestBuilder:
        """
        Provides operations to manage the dependencies property of the microsoft.graph.plan entity.
        """
        from .dependencies.dependencies_request_builder import DependenciesRequestBuilder

        return DependenciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def goals(self) -> GoalsRequestBuilder:
        """
        Provides operations to manage the goals property of the microsoft.graph.plan entity.
        """
        from .goals.goals_request_builder import GoalsRequestBuilder

        return GoalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def history_items(self) -> HistoryItemsRequestBuilder:
        """
        Provides operations to manage the historyItems property of the microsoft.graph.plan entity.
        """
        from .history_items.history_items_request_builder import HistoryItemsRequestBuilder

        return HistoryItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def links(self) -> LinksRequestBuilder:
        """
        Provides operations to manage the links property of the microsoft.graph.plan entity.
        """
        from .links.links_request_builder import LinksRequestBuilder

        return LinksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tasks(self) -> TasksRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.plan entity.
        """
        from .tasks.tasks_request_builder import TasksRequestBuilder

        return TasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PlanItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PlanItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of plan object.
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
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class PlanItemRequestBuilderGetRequestConfiguration(RequestConfiguration[PlanItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PlanItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

