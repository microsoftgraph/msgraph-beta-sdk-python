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
    from .....models.managed_tenants import managed_tenant_alert
    from .....models.o_data_errors import o_data_error
    from .alert_logs import alert_logs_request_builder
    from .alert_rule import alert_rule_request_builder
    from .api_notifications import api_notifications_request_builder
    from .email_notifications import email_notifications_request_builder
    from .managed_tenants_add_user_input_log import managed_tenants_add_user_input_log_request_builder

class ManagedTenantAlertItemRequestBuilder():
    """
    Provides operations to manage the managedTenantAlerts property of the microsoft.graph.managedTenants.managedTenant entity.
    """
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
    
    async def delete(self,request_configuration: Optional[ManagedTenantAlertItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property managedTenantAlerts for tenantRelationships
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
    
    async def get(self,request_configuration: Optional[ManagedTenantAlertItemRequestBuilderGetRequestConfiguration] = None) -> Optional[managed_tenant_alert.ManagedTenantAlert]:
        """
        Get managedTenantAlerts from tenantRelationships
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_tenant_alert.ManagedTenantAlert]
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
        from .....models.managed_tenants import managed_tenant_alert

        return await self.request_adapter.send_async(request_info, managed_tenant_alert.ManagedTenantAlert, error_mapping)
    
    async def patch(self,body: Optional[managed_tenant_alert.ManagedTenantAlert] = None, request_configuration: Optional[ManagedTenantAlertItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[managed_tenant_alert.ManagedTenantAlert]:
        """
        Update the navigation property managedTenantAlerts in tenantRelationships
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_tenant_alert.ManagedTenantAlert]
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
        from .....models.managed_tenants import managed_tenant_alert

        return await self.request_adapter.send_async(request_info, managed_tenant_alert.ManagedTenantAlert, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ManagedTenantAlertItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
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
    
    def to_get_request_information(self,request_configuration: Optional[ManagedTenantAlertItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[managed_tenant_alert.ManagedTenantAlert] = None, request_configuration: Optional[ManagedTenantAlertItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def alert_logs(self) -> alert_logs_request_builder.AlertLogsRequestBuilder:
        """
        Provides operations to manage the alertLogs property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        """
        from .alert_logs import alert_logs_request_builder

        return alert_logs_request_builder.AlertLogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def alert_rule(self) -> alert_rule_request_builder.AlertRuleRequestBuilder:
        """
        Provides operations to manage the alertRule property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        """
        from .alert_rule import alert_rule_request_builder

        return alert_rule_request_builder.AlertRuleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def api_notifications(self) -> api_notifications_request_builder.ApiNotificationsRequestBuilder:
        """
        Provides operations to manage the apiNotifications property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        """
        from .api_notifications import api_notifications_request_builder

        return api_notifications_request_builder.ApiNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def email_notifications(self) -> email_notifications_request_builder.EmailNotificationsRequestBuilder:
        """
        Provides operations to manage the emailNotifications property of the microsoft.graph.managedTenants.managedTenantAlert entity.
        """
        from .email_notifications import email_notifications_request_builder

        return email_notifications_request_builder.EmailNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenants_add_user_input_log(self) -> managed_tenants_add_user_input_log_request_builder.ManagedTenantsAddUserInputLogRequestBuilder:
        """
        Provides operations to call the addUserInputLog method.
        """
        from .managed_tenants_add_user_input_log import managed_tenants_add_user_input_log_request_builder

        return managed_tenants_add_user_input_log_request_builder.ManagedTenantsAddUserInputLogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ManagedTenantAlertItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ManagedTenantAlertItemRequestBuilderGetQueryParameters():
        """
        Get managedTenantAlerts from tenantRelationships
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
    class ManagedTenantAlertItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

