from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.connector_group import ConnectorGroup
    from .....models.o_data_errors.o_data_error import ODataError
    from .applications.applications_request_builder import ApplicationsRequestBuilder
    from .applications_with_app_id.applications_with_app_id_request_builder import ApplicationsWithAppIdRequestBuilder
    from .applications_with_unique_name.applications_with_unique_name_request_builder import ApplicationsWithUniqueNameRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder

class ConnectorGroupItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the connectorGroups property of the microsoft.graph.onPremisesPublishingProfile entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ConnectorGroupItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/onPremisesPublishingProfiles/{onPremisesPublishingProfile%2Did}/connectorGroups/{connectorGroup%2Did}{?%24expand,%24select}", path_parameters)
    
    def applications_with_app_id(self,app_id: Optional[str] = None) -> ApplicationsWithAppIdRequestBuilder:
        """
        Provides operations to manage the applications property of the microsoft.graph.connectorGroup entity.
        param app_id: Alternate key of application
        Returns: ApplicationsWithAppIdRequestBuilder
        """
        if not app_id:
            raise TypeError("app_id cannot be null.")
        from .applications_with_app_id.applications_with_app_id_request_builder import ApplicationsWithAppIdRequestBuilder

        return ApplicationsWithAppIdRequestBuilder(self.request_adapter, self.path_parameters, app_id)
    
    def applications_with_unique_name(self,unique_name: Optional[str] = None) -> ApplicationsWithUniqueNameRequestBuilder:
        """
        Provides operations to manage the applications property of the microsoft.graph.connectorGroup entity.
        param unique_name: Alternate key of application
        Returns: ApplicationsWithUniqueNameRequestBuilder
        """
        if not unique_name:
            raise TypeError("unique_name cannot be null.")
        from .applications_with_unique_name.applications_with_unique_name_request_builder import ApplicationsWithUniqueNameRequestBuilder

        return ApplicationsWithUniqueNameRequestBuilder(self.request_adapter, self.path_parameters, unique_name)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete a connectorGroup. All connectors and applications must be removed from the connector group before a connector group can be deleted.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/connectorgroup-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[ConnectorGroup]:
        """
        Retrieve the properties of a connectorGroup.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConnectorGroup]
        Find more info here: https://learn.microsoft.com/graph/api/connectorgroup-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.connector_group import ConnectorGroup

        return await self.request_adapter.send_async(request_info, ConnectorGroup, error_mapping)
    
    async def patch(self,body: Optional[ConnectorGroup] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[ConnectorGroup]:
        """
        Update the properties of a connectorGroup object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConnectorGroup]
        Find more info here: https://learn.microsoft.com/graph/api/connectorgroup-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.connector_group import ConnectorGroup

        return await self.request_adapter.send_async(request_info, ConnectorGroup, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete a connectorGroup. All connectors and applications must be removed from the connector group before a connector group can be deleted.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties of a connectorGroup.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[ConnectorGroup] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a connectorGroup object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ConnectorGroupItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ConnectorGroupItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ConnectorGroupItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def applications(self) -> ApplicationsRequestBuilder:
        """
        Provides operations to manage the applications property of the microsoft.graph.connectorGroup entity.
        """
        from .applications.applications_request_builder import ApplicationsRequestBuilder

        return ApplicationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.connectorGroup entity.
        """
        from .members.members_request_builder import MembersRequestBuilder

        return MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ConnectorGroupItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties of a connectorGroup.
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

    

