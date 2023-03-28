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
    from ...models import on_premises_publishing_profile
    from ...models.o_data_errors import o_data_error
    from .agent_groups import agent_groups_request_builder
    from .agent_groups.item import on_premises_agent_group_item_request_builder
    from .agents import agents_request_builder
    from .agents.item import on_premises_agent_item_request_builder
    from .connector_groups import connector_groups_request_builder
    from .connector_groups.item import connector_group_item_request_builder
    from .connectors import connectors_request_builder
    from .connectors.item import connector_item_request_builder
    from .published_resources import published_resources_request_builder
    from .published_resources.item import published_resource_item_request_builder

class OnPremisesPublishingProfileItemRequestBuilder():
    """
    Provides operations to manage the collection of onPremisesPublishingProfile entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OnPremisesPublishingProfileItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/onPremisesPublishingProfiles/{onPremisesPublishingProfile%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def agent_groups_by_id(self,id: str) -> on_premises_agent_group_item_request_builder.OnPremisesAgentGroupItemRequestBuilder:
        """
        Provides operations to manage the agentGroups property of the microsoft.graph.onPremisesPublishingProfile entity.
        Args:
            id: Unique identifier of the item
        Returns: on_premises_agent_group_item_request_builder.OnPremisesAgentGroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .agent_groups.item import on_premises_agent_group_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["onPremisesAgentGroup%2Did"] = id
        return on_premises_agent_group_item_request_builder.OnPremisesAgentGroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def agents_by_id(self,id: str) -> on_premises_agent_item_request_builder.OnPremisesAgentItemRequestBuilder:
        """
        Provides operations to manage the agents property of the microsoft.graph.onPremisesPublishingProfile entity.
        Args:
            id: Unique identifier of the item
        Returns: on_premises_agent_item_request_builder.OnPremisesAgentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .agents.item import on_premises_agent_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["onPremisesAgent%2Did"] = id
        return on_premises_agent_item_request_builder.OnPremisesAgentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def connector_groups_by_id(self,id: str) -> connector_group_item_request_builder.ConnectorGroupItemRequestBuilder:
        """
        Provides operations to manage the connectorGroups property of the microsoft.graph.onPremisesPublishingProfile entity.
        Args:
            id: Unique identifier of the item
        Returns: connector_group_item_request_builder.ConnectorGroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .connector_groups.item import connector_group_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["connectorGroup%2Did"] = id
        return connector_group_item_request_builder.ConnectorGroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def connectors_by_id(self,id: str) -> connector_item_request_builder.ConnectorItemRequestBuilder:
        """
        Provides operations to manage the connectors property of the microsoft.graph.onPremisesPublishingProfile entity.
        Args:
            id: Unique identifier of the item
        Returns: connector_item_request_builder.ConnectorItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .connectors.item import connector_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["connector%2Did"] = id
        return connector_item_request_builder.ConnectorItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[OnPremisesPublishingProfileItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete entity from onPremisesPublishingProfiles
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[OnPremisesPublishingProfileItemRequestBuilderGetRequestConfiguration] = None) -> Optional[on_premises_publishing_profile.OnPremisesPublishingProfile]:
        """
        Get entity from onPremisesPublishingProfiles by key
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[on_premises_publishing_profile.OnPremisesPublishingProfile]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import on_premises_publishing_profile

        return await self.request_adapter.send_async(request_info, on_premises_publishing_profile.OnPremisesPublishingProfile, error_mapping)
    
    async def patch(self,body: Optional[on_premises_publishing_profile.OnPremisesPublishingProfile] = None, request_configuration: Optional[OnPremisesPublishingProfileItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[on_premises_publishing_profile.OnPremisesPublishingProfile]:
        """
        Update entity in onPremisesPublishingProfiles
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[on_premises_publishing_profile.OnPremisesPublishingProfile]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import on_premises_publishing_profile

        return await self.request_adapter.send_async(request_info, on_premises_publishing_profile.OnPremisesPublishingProfile, error_mapping)
    
    def published_resources_by_id(self,id: str) -> published_resource_item_request_builder.PublishedResourceItemRequestBuilder:
        """
        Provides operations to manage the publishedResources property of the microsoft.graph.onPremisesPublishingProfile entity.
        Args:
            id: Unique identifier of the item
        Returns: published_resource_item_request_builder.PublishedResourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .published_resources.item import published_resource_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["publishedResource%2Did"] = id
        return published_resource_item_request_builder.PublishedResourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[OnPremisesPublishingProfileItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from onPremisesPublishingProfiles
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
    
    def to_get_request_information(self,request_configuration: Optional[OnPremisesPublishingProfileItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get entity from onPremisesPublishingProfiles by key
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
    
    def to_patch_request_information(self,body: Optional[on_premises_publishing_profile.OnPremisesPublishingProfile] = None, request_configuration: Optional[OnPremisesPublishingProfileItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in onPremisesPublishingProfiles
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
    def agent_groups(self) -> agent_groups_request_builder.AgentGroupsRequestBuilder:
        """
        Provides operations to manage the agentGroups property of the microsoft.graph.onPremisesPublishingProfile entity.
        """
        from .agent_groups import agent_groups_request_builder

        return agent_groups_request_builder.AgentGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agents(self) -> agents_request_builder.AgentsRequestBuilder:
        """
        Provides operations to manage the agents property of the microsoft.graph.onPremisesPublishingProfile entity.
        """
        from .agents import agents_request_builder

        return agents_request_builder.AgentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def connector_groups(self) -> connector_groups_request_builder.ConnectorGroupsRequestBuilder:
        """
        Provides operations to manage the connectorGroups property of the microsoft.graph.onPremisesPublishingProfile entity.
        """
        from .connector_groups import connector_groups_request_builder

        return connector_groups_request_builder.ConnectorGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def connectors(self) -> connectors_request_builder.ConnectorsRequestBuilder:
        """
        Provides operations to manage the connectors property of the microsoft.graph.onPremisesPublishingProfile entity.
        """
        from .connectors import connectors_request_builder

        return connectors_request_builder.ConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def published_resources(self) -> published_resources_request_builder.PublishedResourcesRequestBuilder:
        """
        Provides operations to manage the publishedResources property of the microsoft.graph.onPremisesPublishingProfile entity.
        """
        from .published_resources import published_resources_request_builder

        return published_resources_request_builder.PublishedResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OnPremisesPublishingProfileItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class OnPremisesPublishingProfileItemRequestBuilderGetQueryParameters():
        """
        Get entity from onPremisesPublishingProfiles by key
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
    class OnPremisesPublishingProfileItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[OnPremisesPublishingProfileItemRequestBuilder.OnPremisesPublishingProfileItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class OnPremisesPublishingProfileItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

