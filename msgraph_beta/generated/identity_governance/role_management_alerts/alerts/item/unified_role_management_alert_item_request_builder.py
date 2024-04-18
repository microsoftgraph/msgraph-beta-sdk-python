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
    from .....models.o_data_errors.o_data_error import ODataError
    from .....models.unified_role_management_alert import UnifiedRoleManagementAlert
    from .alert_configuration.alert_configuration_request_builder import AlertConfigurationRequestBuilder
    from .alert_definition.alert_definition_request_builder import AlertDefinitionRequestBuilder
    from .alert_incidents.alert_incidents_request_builder import AlertIncidentsRequestBuilder
    from .refresh.refresh_request_builder import RefreshRequestBuilder

class UnifiedRoleManagementAlertItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the alerts property of the microsoft.graph.roleManagementAlert entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new UnifiedRoleManagementAlertItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/roleManagementAlerts/alerts/{unifiedRoleManagementAlert%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete navigation property alerts for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[UnifiedRoleManagementAlert]:
        """
        Represents the alert entity.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnifiedRoleManagementAlert]
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
        from .....models.unified_role_management_alert import UnifiedRoleManagementAlert

        return await self.request_adapter.send_async(request_info, UnifiedRoleManagementAlert, error_mapping)
    
    async def patch(self,body: Optional[UnifiedRoleManagementAlert] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[UnifiedRoleManagementAlert]:
        """
        Update the navigation property alerts in identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnifiedRoleManagementAlert]
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
        from .....models.unified_role_management_alert import UnifiedRoleManagementAlert

        return await self.request_adapter.send_async(request_info, UnifiedRoleManagementAlert, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property alerts for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Represents the alert entity.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[UnifiedRoleManagementAlert] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property alerts in identityGovernance
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
    
    def with_url(self,raw_url: Optional[str] = None) -> UnifiedRoleManagementAlertItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UnifiedRoleManagementAlertItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return UnifiedRoleManagementAlertItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def alert_configuration(self) -> AlertConfigurationRequestBuilder:
        """
        Provides operations to manage the alertConfiguration property of the microsoft.graph.unifiedRoleManagementAlert entity.
        """
        from .alert_configuration.alert_configuration_request_builder import AlertConfigurationRequestBuilder

        return AlertConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def alert_definition(self) -> AlertDefinitionRequestBuilder:
        """
        Provides operations to manage the alertDefinition property of the microsoft.graph.unifiedRoleManagementAlert entity.
        """
        from .alert_definition.alert_definition_request_builder import AlertDefinitionRequestBuilder

        return AlertDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def alert_incidents(self) -> AlertIncidentsRequestBuilder:
        """
        Provides operations to manage the alertIncidents property of the microsoft.graph.unifiedRoleManagementAlert entity.
        """
        from .alert_incidents.alert_incidents_request_builder import AlertIncidentsRequestBuilder

        return AlertIncidentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def refresh(self) -> RefreshRequestBuilder:
        """
        Provides operations to call the refresh method.
        """
        from .refresh.refresh_request_builder import RefreshRequestBuilder

        return RefreshRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class UnifiedRoleManagementAlertItemRequestBuilderGetQueryParameters():
        """
        Represents the alert entity.
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

    

