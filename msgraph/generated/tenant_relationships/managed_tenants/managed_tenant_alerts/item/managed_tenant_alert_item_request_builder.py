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

managed_tenant_alert = lazy_import('msgraph.generated.models.managed_tenants.managed_tenant_alert')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
add_user_input_log_request_builder = lazy_import('msgraph.generated.tenant_relationships.managed_tenants.managed_tenant_alerts.item.add_user_input_log.add_user_input_log_request_builder')
alert_logs_request_builder = lazy_import('msgraph.generated.tenant_relationships.managed_tenants.managed_tenant_alerts.item.alert_logs.alert_logs_request_builder')
managed_tenant_alert_log_item_request_builder = lazy_import('msgraph.generated.tenant_relationships.managed_tenants.managed_tenant_alerts.item.alert_logs.item.managed_tenant_alert_log_item_request_builder')
alert_rule_request_builder = lazy_import('msgraph.generated.tenant_relationships.managed_tenants.managed_tenant_alerts.item.alert_rule.alert_rule_request_builder')
api_notifications_request_builder = lazy_import('msgraph.generated.tenant_relationships.managed_tenants.managed_tenant_alerts.item.api_notifications.api_notifications_request_builder')
managed_tenant_api_notification_item_request_builder = lazy_import('msgraph.generated.tenant_relationships.managed_tenants.managed_tenant_alerts.item.api_notifications.item.managed_tenant_api_notification_item_request_builder')
email_notifications_request_builder = lazy_import('msgraph.generated.tenant_relationships.managed_tenants.managed_tenant_alerts.item.email_notifications.email_notifications_request_builder')
managed_tenant_email_notification_item_request_builder = lazy_import('msgraph.generated.tenant_relationships.managed_tenants.managed_tenant_alerts.item.email_notifications.item.managed_tenant_email_notification_item_request_builder')

class ManagedTenantAlertItemRequestBuilder():
    """
    Provides operations to manage the managedTenantAlerts property of the microsoft.graph.managedTenants.managedTenant entity.
    """
    @property
    def add_user_input_log(self) -> add_user_input_log_request_builder.AddUserInputLogRequestBuilder:
        """
        Provides operations to call the addUserInputLog method.
        """
        return add_user_input_log_request_builder.AddUserInputLogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def alert_logs(self) -> alert_logs_request_builder.AlertLogsRequestBuilder:
        """
        Provides operations to manage the alertLogs property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        """
        return alert_logs_request_builder.AlertLogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def alert_rule(self) -> alert_rule_request_builder.AlertRuleRequestBuilder:
        """
        Provides operations to manage the alertRule property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        """
        return alert_rule_request_builder.AlertRuleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def api_notifications(self) -> api_notifications_request_builder.ApiNotificationsRequestBuilder:
        """
        Provides operations to manage the apiNotifications property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        """
        return api_notifications_request_builder.ApiNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def email_notifications(self) -> email_notifications_request_builder.EmailNotificationsRequestBuilder:
        """
        Provides operations to manage the emailNotifications property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        """
        return email_notifications_request_builder.EmailNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def alert_logs_by_id(self,id: str) -> managed_tenant_alert_log_item_request_builder.ManagedTenantAlertLogItemRequestBuilder:
        """
        Provides operations to manage the alertLogs property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_tenant_alert_log_item_request_builder.ManagedTenantAlertLogItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedTenantAlertLog%2Did"] = id
        return managed_tenant_alert_log_item_request_builder.ManagedTenantAlertLogItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def api_notifications_by_id(self,id: str) -> managed_tenant_api_notification_item_request_builder.ManagedTenantApiNotificationItemRequestBuilder:
        """
        Provides operations to manage the apiNotifications property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_tenant_api_notification_item_request_builder.ManagedTenantApiNotificationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedTenantApiNotification%2Did"] = id
        return managed_tenant_api_notification_item_request_builder.ManagedTenantApiNotificationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ManagedTenantAlertItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/tenantRelationships/managedTenants/managedTenantAlerts/{managedTenantAlert%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[ManagedTenantAlertItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property managedTenantAlerts for tenantRelationships
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
    
    def create_get_request_information(self,request_configuration: Optional[ManagedTenantAlertItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get managedTenantAlerts from tenantRelationships
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[managed_tenant_alert.ManagedTenantAlert] = None, request_configuration: Optional[ManagedTenantAlertItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property managedTenantAlerts in tenantRelationships
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[ManagedTenantAlertItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property managedTenantAlerts for tenantRelationships
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    def email_notifications_by_id(self,id: str) -> managed_tenant_email_notification_item_request_builder.ManagedTenantEmailNotificationItemRequestBuilder:
        """
        Provides operations to manage the emailNotifications property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_tenant_email_notification_item_request_builder.ManagedTenantEmailNotificationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedTenantEmailNotification%2Did"] = id
        return managed_tenant_email_notification_item_request_builder.ManagedTenantEmailNotificationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ManagedTenantAlertItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[managed_tenant_alert.ManagedTenantAlert]:
        """
        Get managedTenantAlerts from tenantRelationships
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[managed_tenant_alert.ManagedTenantAlert]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, managed_tenant_alert.ManagedTenantAlert, response_handler, error_mapping)
    
    async def patch(self,body: Optional[managed_tenant_alert.ManagedTenantAlert] = None, request_configuration: Optional[ManagedTenantAlertItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[managed_tenant_alert.ManagedTenantAlert]:
        """
        Update the navigation property managedTenantAlerts in tenantRelationships
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[managed_tenant_alert.ManagedTenantAlert]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, managed_tenant_alert.ManagedTenantAlert, response_handler, error_mapping)
    
    @dataclass
    class ManagedTenantAlertItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ManagedTenantAlertItemRequestBuilderGetQueryParameters():
        """
        Get managedTenantAlerts from tenantRelationships
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
    class ManagedTenantAlertItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ManagedTenantAlertItemRequestBuilder.ManagedTenantAlertItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ManagedTenantAlertItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

