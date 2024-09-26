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
    from ...models.on_premises_publishing_profile import OnPremisesPublishingProfile
    from ...models.o_data_errors.o_data_error import ODataError
    from .agents.agents_request_builder import AgentsRequestBuilder
    from .agent_groups.agent_groups_request_builder import AgentGroupsRequestBuilder
    from .application_segments.application_segments_request_builder import ApplicationSegmentsRequestBuilder
    from .connectors.connectors_request_builder import ConnectorsRequestBuilder
    from .connector_groups.connector_groups_request_builder import ConnectorGroupsRequestBuilder
    from .published_resources.published_resources_request_builder import PublishedResourcesRequestBuilder

class OnPremisesPublishingProfileItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of onPremisesPublishingProfile entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new OnPremisesPublishingProfileItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/onPremisesPublishingProfiles/{onPremisesPublishingProfile%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete entity from onPremisesPublishingProfiles
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[OnPremisesPublishingProfileItemRequestBuilderGetQueryParameters]] = None) -> Optional[OnPremisesPublishingProfile]:
        """
        Get entity from onPremisesPublishingProfiles by key
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnPremisesPublishingProfile]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.on_premises_publishing_profile import OnPremisesPublishingProfile

        return await self.request_adapter.send_async(request_info, OnPremisesPublishingProfile, error_mapping)
    
    async def patch(self,body: OnPremisesPublishingProfile, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[OnPremisesPublishingProfile]:
        """
        Update entity in onPremisesPublishingProfiles
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnPremisesPublishingProfile]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.on_premises_publishing_profile import OnPremisesPublishingProfile

        return await self.request_adapter.send_async(request_info, OnPremisesPublishingProfile, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete entity from onPremisesPublishingProfiles
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[OnPremisesPublishingProfileItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get entity from onPremisesPublishingProfiles by key
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: OnPremisesPublishingProfile, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update entity in onPremisesPublishingProfiles
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
    
    def with_url(self,raw_url: str) -> OnPremisesPublishingProfileItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OnPremisesPublishingProfileItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return OnPremisesPublishingProfileItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def agent_groups(self) -> AgentGroupsRequestBuilder:
        """
        Provides operations to manage the agentGroups property of the microsoft.graph.onPremisesPublishingProfile entity.
        """
        from .agent_groups.agent_groups_request_builder import AgentGroupsRequestBuilder

        return AgentGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agents(self) -> AgentsRequestBuilder:
        """
        Provides operations to manage the agents property of the microsoft.graph.onPremisesPublishingProfile entity.
        """
        from .agents.agents_request_builder import AgentsRequestBuilder

        return AgentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def application_segments(self) -> ApplicationSegmentsRequestBuilder:
        """
        Provides operations to manage the applicationSegments property of the microsoft.graph.onPremisesPublishingProfile entity.
        """
        from .application_segments.application_segments_request_builder import ApplicationSegmentsRequestBuilder

        return ApplicationSegmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def connector_groups(self) -> ConnectorGroupsRequestBuilder:
        """
        Provides operations to manage the connectorGroups property of the microsoft.graph.onPremisesPublishingProfile entity.
        """
        from .connector_groups.connector_groups_request_builder import ConnectorGroupsRequestBuilder

        return ConnectorGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def connectors(self) -> ConnectorsRequestBuilder:
        """
        Provides operations to manage the connectors property of the microsoft.graph.onPremisesPublishingProfile entity.
        """
        from .connectors.connectors_request_builder import ConnectorsRequestBuilder

        return ConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def published_resources(self) -> PublishedResourcesRequestBuilder:
        """
        Provides operations to manage the publishedResources property of the microsoft.graph.onPremisesPublishingProfile entity.
        """
        from .published_resources.published_resources_request_builder import PublishedResourcesRequestBuilder

        return PublishedResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OnPremisesPublishingProfileItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OnPremisesPublishingProfileItemRequestBuilderGetQueryParameters():
        """
        Get entity from onPremisesPublishingProfiles by key
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
    class OnPremisesPublishingProfileItemRequestBuilderGetRequestConfiguration(RequestConfiguration[OnPremisesPublishingProfileItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OnPremisesPublishingProfileItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

