from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_configurations_request_builder = lazy_import('msgraph.generated.identity_governance.role_management_alerts.alert_configurations.alert_configurations_request_builder')
unified_role_management_alert_configuration_item_request_builder = lazy_import('msgraph.generated.identity_governance.role_management_alerts.alert_configurations.item.unified_role_management_alert_configuration_item_request_builder')
alert_definitions_request_builder = lazy_import('msgraph.generated.identity_governance.role_management_alerts.alert_definitions.alert_definitions_request_builder')
unified_role_management_alert_definition_item_request_builder = lazy_import('msgraph.generated.identity_governance.role_management_alerts.alert_definitions.item.unified_role_management_alert_definition_item_request_builder')
alerts_request_builder = lazy_import('msgraph.generated.identity_governance.role_management_alerts.alerts.alerts_request_builder')
unified_role_management_alert_item_request_builder = lazy_import('msgraph.generated.identity_governance.role_management_alerts.alerts.item.unified_role_management_alert_item_request_builder')
operations_request_builder = lazy_import('msgraph.generated.identity_governance.role_management_alerts.operations.operations_request_builder')
long_running_operation_item_request_builder = lazy_import('msgraph.generated.identity_governance.role_management_alerts.operations.item.long_running_operation_item_request_builder')
role_management_alert = lazy_import('msgraph.generated.models.role_management_alert')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class RoleManagementAlertsRequestBuilder():
    """
    Provides operations to manage the roleManagementAlerts property of the microsoft.graph.identityGovernance entity.
    """
    @property
    def alert_configurations(self) -> alert_configurations_request_builder.AlertConfigurationsRequestBuilder:
        """
        Provides operations to manage the alertConfigurations property of the microsoft.graph.roleManagementAlert entity.
        """
        return alert_configurations_request_builder.AlertConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def alert_definitions(self) -> alert_definitions_request_builder.AlertDefinitionsRequestBuilder:
        """
        Provides operations to manage the alertDefinitions property of the microsoft.graph.roleManagementAlert entity.
        """
        return alert_definitions_request_builder.AlertDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def alerts(self) -> alerts_request_builder.AlertsRequestBuilder:
        """
        Provides operations to manage the alerts property of the microsoft.graph.roleManagementAlert entity.
        """
        return alerts_request_builder.AlertsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.roleManagementAlert entity.
        """
        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def alert_configurations_by_id(self,id: str) -> unified_role_management_alert_configuration_item_request_builder.UnifiedRoleManagementAlertConfigurationItemRequestBuilder:
        """
        Provides operations to manage the alertConfigurations property of the microsoft.graph.roleManagementAlert entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_management_alert_configuration_item_request_builder.UnifiedRoleManagementAlertConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleManagementAlertConfiguration%2Did"] = id
        return unified_role_management_alert_configuration_item_request_builder.UnifiedRoleManagementAlertConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def alert_definitions_by_id(self,id: str) -> unified_role_management_alert_definition_item_request_builder.UnifiedRoleManagementAlertDefinitionItemRequestBuilder:
        """
        Provides operations to manage the alertDefinitions property of the microsoft.graph.roleManagementAlert entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_management_alert_definition_item_request_builder.UnifiedRoleManagementAlertDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleManagementAlertDefinition%2Did"] = id
        return unified_role_management_alert_definition_item_request_builder.UnifiedRoleManagementAlertDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def alerts_by_id(self,id: str) -> unified_role_management_alert_item_request_builder.UnifiedRoleManagementAlertItemRequestBuilder:
        """
        Provides operations to manage the alerts property of the microsoft.graph.roleManagementAlert entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_management_alert_item_request_builder.UnifiedRoleManagementAlertItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleManagementAlert%2Did"] = id
        return unified_role_management_alert_item_request_builder.UnifiedRoleManagementAlertItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new RoleManagementAlertsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/roleManagementAlerts{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[RoleManagementAlertsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property roleManagementAlerts for identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RoleManagementAlertsRequestBuilderGetRequestConfiguration] = None) -> Optional[role_management_alert.RoleManagementAlert]:
        """
        Get roleManagementAlerts from identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[role_management_alert.RoleManagementAlert]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, role_management_alert.RoleManagementAlert, error_mapping)
    
    def operations_by_id(self,id: str) -> long_running_operation_item_request_builder.LongRunningOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.roleManagementAlert entity.
        Args:
            id: Unique identifier of the item
        Returns: long_running_operation_item_request_builder.LongRunningOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["longRunningOperation%2Did"] = id
        return long_running_operation_item_request_builder.LongRunningOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[role_management_alert.RoleManagementAlert] = None, request_configuration: Optional[RoleManagementAlertsRequestBuilderPatchRequestConfiguration] = None) -> Optional[role_management_alert.RoleManagementAlert]:
        """
        Update the navigation property roleManagementAlerts in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[role_management_alert.RoleManagementAlert]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, role_management_alert.RoleManagementAlert, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RoleManagementAlertsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property roleManagementAlerts for identityGovernance
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
    
    def to_get_request_information(self,request_configuration: Optional[RoleManagementAlertsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get roleManagementAlerts from identityGovernance
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
    
    def to_patch_request_information(self,body: Optional[role_management_alert.RoleManagementAlert] = None, request_configuration: Optional[RoleManagementAlertsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property roleManagementAlerts in identityGovernance
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
    
    @dataclass
    class RoleManagementAlertsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class RoleManagementAlertsRequestBuilderGetQueryParameters():
        """
        Get roleManagementAlerts from identityGovernance
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class RoleManagementAlertsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[RoleManagementAlertsRequestBuilder.RoleManagementAlertsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class RoleManagementAlertsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

