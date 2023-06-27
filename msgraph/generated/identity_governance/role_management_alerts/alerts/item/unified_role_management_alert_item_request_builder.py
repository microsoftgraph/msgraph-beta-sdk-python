from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.o_data_errors.o_data_error import ODataError
    from .....models.unified_role_management_alert import UnifiedRoleManagementAlert
    from .alert_configuration.alert_configuration_request_builder import AlertConfigurationRequestBuilder
    from .alert_definition.alert_definition_request_builder import AlertDefinitionRequestBuilder
    from .alert_incidents.alert_incidents_request_builder import AlertIncidentsRequestBuilder
    from .refresh.refresh_request_builder import RefreshRequestBuilder

class UnifiedRoleManagementAlertItemRequestBuilder():
    """
    Provides operations to manage the alerts property of the microsoft.graph.roleManagementAlert entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UnifiedRoleManagementAlertItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/roleManagementAlerts/alerts/{unifiedRoleManagementAlert%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[UnifiedRoleManagementAlertItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property alerts for identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[UnifiedRoleManagementAlertItemRequestBuilderGetRequestConfiguration] = None) -> Optional[UnifiedRoleManagementAlert]:
        """
        Represents the alert entity.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnifiedRoleManagementAlert]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.unified_role_management_alert import UnifiedRoleManagementAlert

        return await self.request_adapter.send_async(request_info, UnifiedRoleManagementAlert, error_mapping)
    
    async def patch(self,body: Optional[UnifiedRoleManagementAlert] = None, request_configuration: Optional[UnifiedRoleManagementAlertItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[UnifiedRoleManagementAlert]:
        """
        Update the navigation property alerts in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnifiedRoleManagementAlert]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.unified_role_management_alert import UnifiedRoleManagementAlert

        return await self.request_adapter.send_async(request_info, UnifiedRoleManagementAlert, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[UnifiedRoleManagementAlertItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property alerts for identityGovernance
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
    
    def to_get_request_information(self,request_configuration: Optional[UnifiedRoleManagementAlertItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents the alert entity.
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
    
    def to_patch_request_information(self,body: Optional[UnifiedRoleManagementAlert] = None, request_configuration: Optional[UnifiedRoleManagementAlertItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property alerts in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
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
    class UnifiedRoleManagementAlertItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UnifiedRoleManagementAlertItemRequestBuilderGetQueryParameters():
        """
        Represents the alert entity.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
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

    
    @dataclass
    class UnifiedRoleManagementAlertItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UnifiedRoleManagementAlertItemRequestBuilder.UnifiedRoleManagementAlertItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UnifiedRoleManagementAlertItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

