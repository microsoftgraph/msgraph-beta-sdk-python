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
    from .....models.managed_tenants.managed_tenant_alert import ManagedTenantAlert
    from .....models.o_data_errors.o_data_error import ODataError
    from .alert_logs.alert_logs_request_builder import AlertLogsRequestBuilder
    from .alert_rule.alert_rule_request_builder import AlertRuleRequestBuilder
    from .api_notifications.api_notifications_request_builder import ApiNotificationsRequestBuilder
    from .email_notifications.email_notifications_request_builder import EmailNotificationsRequestBuilder
    from .microsoft_graph_managed_tenants_add_user_input_log.microsoft_graph_managed_tenants_add_user_input_log_request_builder import MicrosoftGraphManagedTenantsAddUserInputLogRequestBuilder

class ManagedTenantAlertItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the managedTenantAlerts property of the microsoft.graph.managedTenants.managedTenant entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ManagedTenantAlertItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/tenantRelationships/managedTenants/managedTenantAlerts/{managedTenantAlert%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property managedTenantAlerts for tenantRelationships
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ManagedTenantAlertItemRequestBuilderGetQueryParameters]] = None) -> Optional[ManagedTenantAlert]:
        """
        Get managedTenantAlerts from tenantRelationships
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagedTenantAlert]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.managed_tenants.managed_tenant_alert import ManagedTenantAlert

        return await self.request_adapter.send_async(request_info, ManagedTenantAlert, error_mapping)
    
    async def patch(self,body: ManagedTenantAlert, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManagedTenantAlert]:
        """
        Update the navigation property managedTenantAlerts in tenantRelationships
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagedTenantAlert]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.managed_tenants.managed_tenant_alert import ManagedTenantAlert

        return await self.request_adapter.send_async(request_info, ManagedTenantAlert, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property managedTenantAlerts for tenantRelationships
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ManagedTenantAlertItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get managedTenantAlerts from tenantRelationships
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ManagedTenantAlert, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property managedTenantAlerts in tenantRelationships
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
    
    def with_url(self,raw_url: str) -> ManagedTenantAlertItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ManagedTenantAlertItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ManagedTenantAlertItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def alert_logs(self) -> AlertLogsRequestBuilder:
        """
        Provides operations to manage the alertLogs property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        """
        from .alert_logs.alert_logs_request_builder import AlertLogsRequestBuilder

        return AlertLogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def alert_rule(self) -> AlertRuleRequestBuilder:
        """
        Provides operations to manage the alertRule property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        """
        from .alert_rule.alert_rule_request_builder import AlertRuleRequestBuilder

        return AlertRuleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def api_notifications(self) -> ApiNotificationsRequestBuilder:
        """
        Provides operations to manage the apiNotifications property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        """
        from .api_notifications.api_notifications_request_builder import ApiNotificationsRequestBuilder

        return ApiNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def email_notifications(self) -> EmailNotificationsRequestBuilder:
        """
        Provides operations to manage the emailNotifications property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        """
        from .email_notifications.email_notifications_request_builder import EmailNotificationsRequestBuilder

        return EmailNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_managed_tenants_add_user_input_log(self) -> MicrosoftGraphManagedTenantsAddUserInputLogRequestBuilder:
        """
        Provides operations to call the addUserInputLog method.
        """
        from .microsoft_graph_managed_tenants_add_user_input_log.microsoft_graph_managed_tenants_add_user_input_log_request_builder import MicrosoftGraphManagedTenantsAddUserInputLogRequestBuilder

        return MicrosoftGraphManagedTenantsAddUserInputLogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ManagedTenantAlertItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManagedTenantAlertItemRequestBuilderGetQueryParameters():
        """
        Get managedTenantAlerts from tenantRelationships
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
    class ManagedTenantAlertItemRequestBuilderGetRequestConfiguration(RequestConfiguration[ManagedTenantAlertItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManagedTenantAlertItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

