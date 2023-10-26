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
    from ...models.on_premises_publishing_profile import OnPremisesPublishingProfile
    from ...models.o_data_errors.o_data_error import ODataError
    from .agents.agents_request_builder import AgentsRequestBuilder
    from .agent_groups.agent_groups_request_builder import AgentGroupsRequestBuilder
    from .connectors.connectors_request_builder import ConnectorsRequestBuilder
    from .connector_groups.connector_groups_request_builder import ConnectorGroupsRequestBuilder
    from .published_resources.published_resources_request_builder import PublishedResourcesRequestBuilder

class OnPremisesPublishingProfileItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of onPremisesPublishingProfile entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OnPremisesPublishingProfileItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/onPremisesPublishingProfiles/{onPremisesPublishingProfile%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[OnPremisesPublishingProfileItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete entity from onPremisesPublishingProfiles
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
    
    async def get(self,request_configuration: Optional[OnPremisesPublishingProfileItemRequestBuilderGetRequestConfiguration] = None) -> Optional[OnPremisesPublishingProfile]:
        """
        Get entity from onPremisesPublishingProfiles by key
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnPremisesPublishingProfile]
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
        from ...models.on_premises_publishing_profile import OnPremisesPublishingProfile

        return await self.request_adapter.send_async(request_info, OnPremisesPublishingProfile, error_mapping)
    
    async def patch(self,body: Optional[OnPremisesPublishingProfile] = None, request_configuration: Optional[OnPremisesPublishingProfileItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[OnPremisesPublishingProfile]:
        """
        Update entity in onPremisesPublishingProfiles
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnPremisesPublishingProfile]
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
        from ...models.on_premises_publishing_profile import OnPremisesPublishingProfile

        return await self.request_adapter.send_async(request_info, OnPremisesPublishingProfile, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[OnPremisesPublishingProfileItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from onPremisesPublishingProfiles
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
        request_info.headers.try_add("Accept", "application/json, application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[OnPremisesPublishingProfileItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get entity from onPremisesPublishingProfiles by key
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
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def to_patch_request_information(self,body: Optional[OnPremisesPublishingProfile] = None, request_configuration: Optional[OnPremisesPublishingProfileItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in onPremisesPublishingProfiles
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
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> OnPremisesPublishingProfileItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OnPremisesPublishingProfileItemRequestBuilder
        """
        if not raw_url:
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
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class OnPremisesPublishingProfileItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class OnPremisesPublishingProfileItemRequestBuilderGetQueryParameters():
        """
        Get entity from onPremisesPublishingProfiles by key
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
    class OnPremisesPublishingProfileItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[OnPremisesPublishingProfileItemRequestBuilder.OnPremisesPublishingProfileItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class OnPremisesPublishingProfileItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

