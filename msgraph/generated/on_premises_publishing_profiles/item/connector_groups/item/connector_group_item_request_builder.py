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
    from .....models import connector_group
    from .....models.o_data_errors import o_data_error
    from .applications import applications_request_builder
    from .applications.item import application_item_request_builder
    from .members import members_request_builder
    from .members.item import connector_item_request_builder

class ConnectorGroupItemRequestBuilder():
    """
    Provides operations to manage the connectorGroups property of the microsoft.graph.onPremisesPublishingProfile entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ConnectorGroupItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/onPremisesPublishingProfiles/{onPremisesPublishingProfile%2Did}/connectorGroups/{connectorGroup%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def applications_by_id(self,id: str) -> application_item_request_builder.ApplicationItemRequestBuilder:
        """
        Provides operations to manage the applications property of the microsoft.graph.connectorGroup entity.
        Args:
            id: Unique identifier of the item
        Returns: application_item_request_builder.ApplicationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .applications.item import application_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["application%2Did"] = id
        return application_item_request_builder.ApplicationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[ConnectorGroupItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property connectorGroups for onPremisesPublishingProfiles
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ConnectorGroupItemRequestBuilderGetRequestConfiguration] = None) -> Optional[connector_group.ConnectorGroup]:
        """
        List of existing connectorGroup objects for applications published through Application Proxy. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[connector_group.ConnectorGroup]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import connector_group

        return await self.request_adapter.send_async(request_info, connector_group.ConnectorGroup, error_mapping)
    
    def members_by_id(self,id: str) -> connector_item_request_builder.ConnectorItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.onPremisesPublishingProfiles.item.connectorGroups.item.members.item collection
        Args:
            id: Unique identifier of the item
        Returns: connector_item_request_builder.ConnectorItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .members.item import connector_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["connector%2Did"] = id
        return connector_item_request_builder.ConnectorItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[connector_group.ConnectorGroup] = None, request_configuration: Optional[ConnectorGroupItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[connector_group.ConnectorGroup]:
        """
        Update the navigation property connectorGroups in onPremisesPublishingProfiles
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[connector_group.ConnectorGroup]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import connector_group

        return await self.request_adapter.send_async(request_info, connector_group.ConnectorGroup, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ConnectorGroupItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property connectorGroups for onPremisesPublishingProfiles
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
    
    def to_get_request_information(self,request_configuration: Optional[ConnectorGroupItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        List of existing connectorGroup objects for applications published through Application Proxy. Read-only. Nullable.
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
    
    def to_patch_request_information(self,body: Optional[connector_group.ConnectorGroup] = None, request_configuration: Optional[ConnectorGroupItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property connectorGroups in onPremisesPublishingProfiles
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
    def applications(self) -> applications_request_builder.ApplicationsRequestBuilder:
        """
        Provides operations to manage the applications property of the microsoft.graph.connectorGroup entity.
        """
        from .applications import applications_request_builder

        return applications_request_builder.ApplicationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> members_request_builder.MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.connectorGroup entity.
        """
        from .members import members_request_builder

        return members_request_builder.MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ConnectorGroupItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ConnectorGroupItemRequestBuilderGetQueryParameters():
        """
        List of existing connectorGroup objects for applications published through Application Proxy. Read-only. Nullable.
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
    class ConnectorGroupItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ConnectorGroupItemRequestBuilder.ConnectorGroupItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ConnectorGroupItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

