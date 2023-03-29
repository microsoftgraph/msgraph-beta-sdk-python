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
    from .....models import unified_role_management_alert_configuration
    from .....models.o_data_errors import o_data_error
    from .alert_definition import alert_definition_request_builder

class UnifiedRoleManagementAlertConfigurationItemRequestBuilder():
    """
    Provides operations to manage the alertConfigurations property of the microsoft.graph.roleManagementAlert entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UnifiedRoleManagementAlertConfigurationItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/roleManagementAlerts/alertConfigurations/{unifiedRoleManagementAlertConfiguration%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[UnifiedRoleManagementAlertConfigurationItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property alertConfigurations for identityGovernance
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
    
    async def get(self,request_configuration: Optional[UnifiedRoleManagementAlertConfigurationItemRequestBuilderGetRequestConfiguration] = None) -> Optional[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration]:
        """
        Get alertConfigurations from identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration]
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
        from .....models import unified_role_management_alert_configuration

        return await self.request_adapter.send_async(request_info, unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration, error_mapping)
    
    async def patch(self,body: Optional[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration] = None, request_configuration: Optional[UnifiedRoleManagementAlertConfigurationItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration]:
        """
        Update the navigation property alertConfigurations in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration]
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
        from .....models import unified_role_management_alert_configuration

        return await self.request_adapter.send_async(request_info, unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[UnifiedRoleManagementAlertConfigurationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property alertConfigurations for identityGovernance
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
    
    def to_get_request_information(self,request_configuration: Optional[UnifiedRoleManagementAlertConfigurationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get alertConfigurations from identityGovernance
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
    
    def to_patch_request_information(self,body: Optional[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration] = None, request_configuration: Optional[UnifiedRoleManagementAlertConfigurationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property alertConfigurations in identityGovernance
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
    def alert_definition(self) -> alert_definition_request_builder.AlertDefinitionRequestBuilder:
        """
        Provides operations to manage the alertDefinition property of the microsoft.graph.unifiedRoleManagementAlertConfiguration entity.
        """
        from .alert_definition import alert_definition_request_builder

        return alert_definition_request_builder.AlertDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class UnifiedRoleManagementAlertConfigurationItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UnifiedRoleManagementAlertConfigurationItemRequestBuilderGetQueryParameters():
        """
        Get alertConfigurations from identityGovernance
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
    class UnifiedRoleManagementAlertConfigurationItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UnifiedRoleManagementAlertConfigurationItemRequestBuilder.UnifiedRoleManagementAlertConfigurationItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UnifiedRoleManagementAlertConfigurationItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

