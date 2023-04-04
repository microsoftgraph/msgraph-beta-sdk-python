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
    from ...models.managed_tenants import managed_tenant
    from ...models.o_data_errors import o_data_error
    from .aggregated_policy_compliances import aggregated_policy_compliances_request_builder
    from .aggregated_policy_compliances.item import aggregated_policy_compliance_item_request_builder
    from .app_performances import app_performances_request_builder
    from .app_performances.item import app_performance_item_request_builder
    from .audit_events import audit_events_request_builder
    from .audit_events.item import audit_event_item_request_builder
    from .cloud_pc_connections import cloud_pc_connections_request_builder
    from .cloud_pc_connections.item import cloud_pc_connection_item_request_builder
    from .cloud_pc_devices import cloud_pc_devices_request_builder
    from .cloud_pc_devices.item import cloud_pc_device_item_request_builder
    from .cloud_pcs_overview import cloud_pcs_overview_request_builder
    from .cloud_pcs_overview.item import cloud_pc_overview_tenant_item_request_builder
    from .conditional_access_policy_coverages import conditional_access_policy_coverages_request_builder
    from .conditional_access_policy_coverages.item import conditional_access_policy_coverage_item_request_builder
    from .credential_user_registrations_summaries import credential_user_registrations_summaries_request_builder
    from .credential_user_registrations_summaries.item import credential_user_registrations_summary_item_request_builder
    from .device_app_performances import device_app_performances_request_builder
    from .device_app_performances.item import device_app_performance_item_request_builder
    from .device_compliance_policy_setting_state_summaries import device_compliance_policy_setting_state_summaries_request_builder
    from .device_compliance_policy_setting_state_summaries.item import device_compliance_policy_setting_state_summary_item_request_builder
    from .device_health_statuses import device_health_statuses_request_builder
    from .device_health_statuses.item import device_health_status_item_request_builder
    from .managed_device_compliances import managed_device_compliances_request_builder
    from .managed_device_compliances.item import managed_device_compliance_item_request_builder
    from .managed_device_compliance_trends import managed_device_compliance_trends_request_builder
    from .managed_device_compliance_trends.item import managed_device_compliance_trend_item_request_builder
    from .managed_tenant_alert_logs import managed_tenant_alert_logs_request_builder
    from .managed_tenant_alert_logs.item import managed_tenant_alert_log_item_request_builder
    from .managed_tenant_alert_rule_definitions import managed_tenant_alert_rule_definitions_request_builder
    from .managed_tenant_alert_rule_definitions.item import managed_tenant_alert_rule_definition_item_request_builder
    from .managed_tenant_alert_rules import managed_tenant_alert_rules_request_builder
    from .managed_tenant_alert_rules.item import managed_tenant_alert_rule_item_request_builder
    from .managed_tenant_alerts import managed_tenant_alerts_request_builder
    from .managed_tenant_alerts.item import managed_tenant_alert_item_request_builder
    from .managed_tenant_api_notifications import managed_tenant_api_notifications_request_builder
    from .managed_tenant_api_notifications.item import managed_tenant_api_notification_item_request_builder
    from .managed_tenant_email_notifications import managed_tenant_email_notifications_request_builder
    from .managed_tenant_email_notifications.item import managed_tenant_email_notification_item_request_builder
    from .managed_tenant_ticketing_endpoints import managed_tenant_ticketing_endpoints_request_builder
    from .managed_tenant_ticketing_endpoints.item import managed_tenant_ticketing_endpoint_item_request_builder
    from .management_actions import management_actions_request_builder
    from .management_actions.item import management_action_item_request_builder
    from .management_action_tenant_deployment_statuses import management_action_tenant_deployment_statuses_request_builder
    from .management_action_tenant_deployment_statuses.item import management_action_tenant_deployment_status_item_request_builder
    from .management_intents import management_intents_request_builder
    from .management_intents.item import management_intent_item_request_builder
    from .management_template_collections import management_template_collections_request_builder
    from .management_template_collections.item import management_template_collection_item_request_builder
    from .management_template_collection_tenant_summaries import management_template_collection_tenant_summaries_request_builder
    from .management_template_collection_tenant_summaries.item import management_template_collection_tenant_summary_item_request_builder
    from .management_templates import management_templates_request_builder
    from .management_templates.item import management_template_item_request_builder
    from .management_template_steps import management_template_steps_request_builder
    from .management_template_steps.item import management_template_step_item_request_builder
    from .management_template_step_tenant_summaries import management_template_step_tenant_summaries_request_builder
    from .management_template_step_tenant_summaries.item import management_template_step_tenant_summary_item_request_builder
    from .management_template_step_versions import management_template_step_versions_request_builder
    from .management_template_step_versions.item import management_template_step_version_item_request_builder
    from .my_roles import my_roles_request_builder
    from .my_roles.item import my_role_tenant_item_request_builder
    from .tenant_groups import tenant_groups_request_builder
    from .tenant_groups.item import tenant_group_item_request_builder
    from .tenants import tenants_request_builder
    from .tenants.item import tenant_item_request_builder
    from .tenants_customized_information import tenants_customized_information_request_builder
    from .tenants_customized_information.item import tenant_customized_information_item_request_builder
    from .tenants_detailed_information import tenants_detailed_information_request_builder
    from .tenants_detailed_information.item import tenant_detailed_information_item_request_builder
    from .tenant_tags import tenant_tags_request_builder
    from .tenant_tags.item import tenant_tag_item_request_builder
    from .windows_device_malware_states import windows_device_malware_states_request_builder
    from .windows_device_malware_states.item import windows_device_malware_state_item_request_builder
    from .windows_protection_states import windows_protection_states_request_builder
    from .windows_protection_states.item import windows_protection_state_item_request_builder

class ManagedTenantsRequestBuilder():
    """
    Provides operations to manage the managedTenants property of the microsoft.graph.tenantRelationship entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ManagedTenantsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/tenantRelationships/managedTenants{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def aggregated_policy_compliances_by_id(self,id: str) -> aggregated_policy_compliance_item_request_builder.AggregatedPolicyComplianceItemRequestBuilder:
        """
        Provides operations to manage the aggregatedPolicyCompliances property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: aggregated_policy_compliance_item_request_builder.AggregatedPolicyComplianceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .aggregated_policy_compliances.item import aggregated_policy_compliance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["aggregatedPolicyCompliance%2Did"] = id
        return aggregated_policy_compliance_item_request_builder.AggregatedPolicyComplianceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def app_performances_by_id(self,id: str) -> app_performance_item_request_builder.AppPerformanceItemRequestBuilder:
        """
        Provides operations to manage the appPerformances property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: app_performance_item_request_builder.AppPerformanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .app_performances.item import app_performance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["appPerformance%2Did"] = id
        return app_performance_item_request_builder.AppPerformanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def audit_events_by_id(self,id: str) -> audit_event_item_request_builder.AuditEventItemRequestBuilder:
        """
        Provides operations to manage the auditEvents property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: audit_event_item_request_builder.AuditEventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .audit_events.item import audit_event_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["auditEvent%2Did"] = id
        return audit_event_item_request_builder.AuditEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def cloud_pc_connections_by_id(self,id: str) -> cloud_pc_connection_item_request_builder.CloudPcConnectionItemRequestBuilder:
        """
        Provides operations to manage the cloudPcConnections property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_connection_item_request_builder.CloudPcConnectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .cloud_pc_connections.item import cloud_pc_connection_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcConnection%2Did"] = id
        return cloud_pc_connection_item_request_builder.CloudPcConnectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def cloud_pc_devices_by_id(self,id: str) -> cloud_pc_device_item_request_builder.CloudPcDeviceItemRequestBuilder:
        """
        Provides operations to manage the cloudPcDevices property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_device_item_request_builder.CloudPcDeviceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .cloud_pc_devices.item import cloud_pc_device_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcDevice%2Did"] = id
        return cloud_pc_device_item_request_builder.CloudPcDeviceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def cloud_pcs_overview_by_id(self,id: str) -> cloud_pc_overview_tenant_item_request_builder.CloudPcOverviewTenantItemRequestBuilder:
        """
        Provides operations to manage the cloudPcsOverview property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_overview_tenant_item_request_builder.CloudPcOverviewTenantItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .cloud_pcs_overview.item import cloud_pc_overview_tenant_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcOverview%2DtenantId"] = id
        return cloud_pc_overview_tenant_item_request_builder.CloudPcOverviewTenantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def conditional_access_policy_coverages_by_id(self,id: str) -> conditional_access_policy_coverage_item_request_builder.ConditionalAccessPolicyCoverageItemRequestBuilder:
        """
        Provides operations to manage the conditionalAccessPolicyCoverages property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: conditional_access_policy_coverage_item_request_builder.ConditionalAccessPolicyCoverageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .conditional_access_policy_coverages.item import conditional_access_policy_coverage_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["conditionalAccessPolicyCoverage%2Did"] = id
        return conditional_access_policy_coverage_item_request_builder.ConditionalAccessPolicyCoverageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def credential_user_registrations_summaries_by_id(self,id: str) -> credential_user_registrations_summary_item_request_builder.CredentialUserRegistrationsSummaryItemRequestBuilder:
        """
        Provides operations to manage the credentialUserRegistrationsSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: credential_user_registrations_summary_item_request_builder.CredentialUserRegistrationsSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .credential_user_registrations_summaries.item import credential_user_registrations_summary_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["credentialUserRegistrationsSummary%2Did"] = id
        return credential_user_registrations_summary_item_request_builder.CredentialUserRegistrationsSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[ManagedTenantsRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete navigation property managedTenants for tenantRelationships
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
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
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def device_app_performances_by_id(self,id: str) -> device_app_performance_item_request_builder.DeviceAppPerformanceItemRequestBuilder:
        """
        Provides operations to manage the deviceAppPerformances property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: device_app_performance_item_request_builder.DeviceAppPerformanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_app_performances.item import device_app_performance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceAppPerformance%2Did"] = id
        return device_app_performance_item_request_builder.DeviceAppPerformanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_compliance_policy_setting_state_summaries_by_id(self,id: str) -> device_compliance_policy_setting_state_summary_item_request_builder.DeviceCompliancePolicySettingStateSummaryItemRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicySettingStateSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: device_compliance_policy_setting_state_summary_item_request_builder.DeviceCompliancePolicySettingStateSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_compliance_policy_setting_state_summaries.item import device_compliance_policy_setting_state_summary_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceCompliancePolicySettingStateSummary%2Did"] = id
        return device_compliance_policy_setting_state_summary_item_request_builder.DeviceCompliancePolicySettingStateSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_health_statuses_by_id(self,id: str) -> device_health_status_item_request_builder.DeviceHealthStatusItemRequestBuilder:
        """
        Provides operations to manage the deviceHealthStatuses property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: device_health_status_item_request_builder.DeviceHealthStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_health_statuses.item import device_health_status_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceHealthStatus%2Did"] = id
        return device_health_status_item_request_builder.DeviceHealthStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ManagedTenantsRequestBuilderGetRequestConfiguration] = None) -> Optional[managed_tenant.ManagedTenant]:
        """
        The operations available to interact with the multi-tenant management platform.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_tenant.ManagedTenant]
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
        from ...models.managed_tenants import managed_tenant

        return await self.request_adapter.send_async(request_info, managed_tenant.ManagedTenant, error_mapping)
    
    def managed_device_compliances_by_id(self,id: str) -> managed_device_compliance_item_request_builder.ManagedDeviceComplianceItemRequestBuilder:
        """
        Provides operations to manage the managedDeviceCompliances property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_device_compliance_item_request_builder.ManagedDeviceComplianceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .managed_device_compliances.item import managed_device_compliance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDeviceCompliance%2Did"] = id
        return managed_device_compliance_item_request_builder.ManagedDeviceComplianceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_device_compliance_trends_by_id(self,id: str) -> managed_device_compliance_trend_item_request_builder.ManagedDeviceComplianceTrendItemRequestBuilder:
        """
        Provides operations to manage the managedDeviceComplianceTrends property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_device_compliance_trend_item_request_builder.ManagedDeviceComplianceTrendItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .managed_device_compliance_trends.item import managed_device_compliance_trend_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDeviceComplianceTrend%2Did"] = id
        return managed_device_compliance_trend_item_request_builder.ManagedDeviceComplianceTrendItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_tenant_alert_logs_by_id(self,id: str) -> managed_tenant_alert_log_item_request_builder.ManagedTenantAlertLogItemRequestBuilder:
        """
        Provides operations to manage the managedTenantAlertLogs property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_tenant_alert_log_item_request_builder.ManagedTenantAlertLogItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .managed_tenant_alert_logs.item import managed_tenant_alert_log_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedTenantAlertLog%2Did"] = id
        return managed_tenant_alert_log_item_request_builder.ManagedTenantAlertLogItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_tenant_alert_rule_definitions_by_id(self,id: str) -> managed_tenant_alert_rule_definition_item_request_builder.ManagedTenantAlertRuleDefinitionItemRequestBuilder:
        """
        Provides operations to manage the managedTenantAlertRuleDefinitions property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_tenant_alert_rule_definition_item_request_builder.ManagedTenantAlertRuleDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .managed_tenant_alert_rule_definitions.item import managed_tenant_alert_rule_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedTenantAlertRuleDefinition%2Did"] = id
        return managed_tenant_alert_rule_definition_item_request_builder.ManagedTenantAlertRuleDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_tenant_alert_rules_by_id(self,id: str) -> managed_tenant_alert_rule_item_request_builder.ManagedTenantAlertRuleItemRequestBuilder:
        """
        Provides operations to manage the managedTenantAlertRules property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_tenant_alert_rule_item_request_builder.ManagedTenantAlertRuleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .managed_tenant_alert_rules.item import managed_tenant_alert_rule_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedTenantAlertRule%2Did"] = id
        return managed_tenant_alert_rule_item_request_builder.ManagedTenantAlertRuleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_tenant_alerts_by_id(self,id: str) -> managed_tenant_alert_item_request_builder.ManagedTenantAlertItemRequestBuilder:
        """
        Provides operations to manage the managedTenantAlerts property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_tenant_alert_item_request_builder.ManagedTenantAlertItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .managed_tenant_alerts.item import managed_tenant_alert_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedTenantAlert%2Did"] = id
        return managed_tenant_alert_item_request_builder.ManagedTenantAlertItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_tenant_api_notifications_by_id(self,id: str) -> managed_tenant_api_notification_item_request_builder.ManagedTenantApiNotificationItemRequestBuilder:
        """
        Provides operations to manage the managedTenantApiNotifications property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_tenant_api_notification_item_request_builder.ManagedTenantApiNotificationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .managed_tenant_api_notifications.item import managed_tenant_api_notification_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedTenantApiNotification%2Did"] = id
        return managed_tenant_api_notification_item_request_builder.ManagedTenantApiNotificationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_tenant_email_notifications_by_id(self,id: str) -> managed_tenant_email_notification_item_request_builder.ManagedTenantEmailNotificationItemRequestBuilder:
        """
        Provides operations to manage the managedTenantEmailNotifications property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_tenant_email_notification_item_request_builder.ManagedTenantEmailNotificationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .managed_tenant_email_notifications.item import managed_tenant_email_notification_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedTenantEmailNotification%2Did"] = id
        return managed_tenant_email_notification_item_request_builder.ManagedTenantEmailNotificationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_tenant_ticketing_endpoints_by_id(self,id: str) -> managed_tenant_ticketing_endpoint_item_request_builder.ManagedTenantTicketingEndpointItemRequestBuilder:
        """
        Provides operations to manage the managedTenantTicketingEndpoints property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_tenant_ticketing_endpoint_item_request_builder.ManagedTenantTicketingEndpointItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .managed_tenant_ticketing_endpoints.item import managed_tenant_ticketing_endpoint_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedTenantTicketingEndpoint%2Did"] = id
        return managed_tenant_ticketing_endpoint_item_request_builder.ManagedTenantTicketingEndpointItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def management_actions_by_id(self,id: str) -> management_action_item_request_builder.ManagementActionItemRequestBuilder:
        """
        Provides operations to manage the managementActions property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: management_action_item_request_builder.ManagementActionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .management_actions.item import management_action_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managementAction%2Did"] = id
        return management_action_item_request_builder.ManagementActionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def management_action_tenant_deployment_statuses_by_id(self,id: str) -> management_action_tenant_deployment_status_item_request_builder.ManagementActionTenantDeploymentStatusItemRequestBuilder:
        """
        Provides operations to manage the managementActionTenantDeploymentStatuses property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: management_action_tenant_deployment_status_item_request_builder.ManagementActionTenantDeploymentStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .management_action_tenant_deployment_statuses.item import management_action_tenant_deployment_status_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managementActionTenantDeploymentStatus%2Did"] = id
        return management_action_tenant_deployment_status_item_request_builder.ManagementActionTenantDeploymentStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def management_intents_by_id(self,id: str) -> management_intent_item_request_builder.ManagementIntentItemRequestBuilder:
        """
        Provides operations to manage the managementIntents property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: management_intent_item_request_builder.ManagementIntentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .management_intents.item import management_intent_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managementIntent%2Did"] = id
        return management_intent_item_request_builder.ManagementIntentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def management_template_collections_by_id(self,id: str) -> management_template_collection_item_request_builder.ManagementTemplateCollectionItemRequestBuilder:
        """
        Provides operations to manage the managementTemplateCollections property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: management_template_collection_item_request_builder.ManagementTemplateCollectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .management_template_collections.item import management_template_collection_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managementTemplateCollection%2Did"] = id
        return management_template_collection_item_request_builder.ManagementTemplateCollectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def management_template_collection_tenant_summaries_by_id(self,id: str) -> management_template_collection_tenant_summary_item_request_builder.ManagementTemplateCollectionTenantSummaryItemRequestBuilder:
        """
        Provides operations to manage the managementTemplateCollectionTenantSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: management_template_collection_tenant_summary_item_request_builder.ManagementTemplateCollectionTenantSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .management_template_collection_tenant_summaries.item import management_template_collection_tenant_summary_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managementTemplateCollectionTenantSummary%2Did"] = id
        return management_template_collection_tenant_summary_item_request_builder.ManagementTemplateCollectionTenantSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def management_templates_by_id(self,id: str) -> management_template_item_request_builder.ManagementTemplateItemRequestBuilder:
        """
        Provides operations to manage the managementTemplates property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: management_template_item_request_builder.ManagementTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .management_templates.item import management_template_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managementTemplate%2Did"] = id
        return management_template_item_request_builder.ManagementTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def management_template_steps_by_id(self,id: str) -> management_template_step_item_request_builder.ManagementTemplateStepItemRequestBuilder:
        """
        Provides operations to manage the managementTemplateSteps property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: management_template_step_item_request_builder.ManagementTemplateStepItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .management_template_steps.item import management_template_step_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managementTemplateStep%2Did"] = id
        return management_template_step_item_request_builder.ManagementTemplateStepItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def management_template_step_tenant_summaries_by_id(self,id: str) -> management_template_step_tenant_summary_item_request_builder.ManagementTemplateStepTenantSummaryItemRequestBuilder:
        """
        Provides operations to manage the managementTemplateStepTenantSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: management_template_step_tenant_summary_item_request_builder.ManagementTemplateStepTenantSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .management_template_step_tenant_summaries.item import management_template_step_tenant_summary_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managementTemplateStepTenantSummary%2Did"] = id
        return management_template_step_tenant_summary_item_request_builder.ManagementTemplateStepTenantSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def management_template_step_versions_by_id(self,id: str) -> management_template_step_version_item_request_builder.ManagementTemplateStepVersionItemRequestBuilder:
        """
        Provides operations to manage the managementTemplateStepVersions property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: management_template_step_version_item_request_builder.ManagementTemplateStepVersionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .management_template_step_versions.item import management_template_step_version_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managementTemplateStepVersion%2Did"] = id
        return management_template_step_version_item_request_builder.ManagementTemplateStepVersionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def my_roles_by_id(self,id: str) -> my_role_tenant_item_request_builder.MyRoleTenantItemRequestBuilder:
        """
        Provides operations to manage the myRoles property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: my_role_tenant_item_request_builder.MyRoleTenantItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .my_roles.item import my_role_tenant_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["myRole%2DtenantId"] = id
        return my_role_tenant_item_request_builder.MyRoleTenantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[managed_tenant.ManagedTenant] = None, request_configuration: Optional[ManagedTenantsRequestBuilderPatchRequestConfiguration] = None) -> Optional[managed_tenant.ManagedTenant]:
        """
        Update the navigation property managedTenants in tenantRelationships
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_tenant.ManagedTenant]
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
        from ...models.managed_tenants import managed_tenant

        return await self.request_adapter.send_async(request_info, managed_tenant.ManagedTenant, error_mapping)
    
    def tenant_groups_by_id(self,id: str) -> tenant_group_item_request_builder.TenantGroupItemRequestBuilder:
        """
        Provides operations to manage the tenantGroups property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: tenant_group_item_request_builder.TenantGroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .tenant_groups.item import tenant_group_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tenantGroup%2Did"] = id
        return tenant_group_item_request_builder.TenantGroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tenants_by_id(self,id: str) -> tenant_item_request_builder.TenantItemRequestBuilder:
        """
        Provides operations to manage the tenants property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: tenant_item_request_builder.TenantItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .tenants.item import tenant_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tenant%2Did"] = id
        return tenant_item_request_builder.TenantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tenants_customized_information_by_id(self,id: str) -> tenant_customized_information_item_request_builder.TenantCustomizedInformationItemRequestBuilder:
        """
        Provides operations to manage the tenantsCustomizedInformation property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: tenant_customized_information_item_request_builder.TenantCustomizedInformationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .tenants_customized_information.item import tenant_customized_information_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tenantCustomizedInformation%2Did"] = id
        return tenant_customized_information_item_request_builder.TenantCustomizedInformationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tenants_detailed_information_by_id(self,id: str) -> tenant_detailed_information_item_request_builder.TenantDetailedInformationItemRequestBuilder:
        """
        Provides operations to manage the tenantsDetailedInformation property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: tenant_detailed_information_item_request_builder.TenantDetailedInformationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .tenants_detailed_information.item import tenant_detailed_information_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tenantDetailedInformation%2Did"] = id
        return tenant_detailed_information_item_request_builder.TenantDetailedInformationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tenant_tags_by_id(self,id: str) -> tenant_tag_item_request_builder.TenantTagItemRequestBuilder:
        """
        Provides operations to manage the tenantTags property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: tenant_tag_item_request_builder.TenantTagItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .tenant_tags.item import tenant_tag_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tenantTag%2Did"] = id
        return tenant_tag_item_request_builder.TenantTagItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[ManagedTenantsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property managedTenants for tenantRelationships
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
    
    def to_get_request_information(self,request_configuration: Optional[ManagedTenantsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The operations available to interact with the multi-tenant management platform.
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
    
    def to_patch_request_information(self,body: Optional[managed_tenant.ManagedTenant] = None, request_configuration: Optional[ManagedTenantsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property managedTenants in tenantRelationships
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
    
    def windows_device_malware_states_by_id(self,id: str) -> windows_device_malware_state_item_request_builder.WindowsDeviceMalwareStateItemRequestBuilder:
        """
        Provides operations to manage the windowsDeviceMalwareStates property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_device_malware_state_item_request_builder.WindowsDeviceMalwareStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .windows_device_malware_states.item import windows_device_malware_state_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsDeviceMalwareState%2Did"] = id
        return windows_device_malware_state_item_request_builder.WindowsDeviceMalwareStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_protection_states_by_id(self,id: str) -> windows_protection_state_item_request_builder.WindowsProtectionStateItemRequestBuilder:
        """
        Provides operations to manage the windowsProtectionStates property of the microsoft.graph.managedTenants.managedTenant entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_protection_state_item_request_builder.WindowsProtectionStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .windows_protection_states.item import windows_protection_state_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsProtectionState%2Did"] = id
        return windows_protection_state_item_request_builder.WindowsProtectionStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def aggregated_policy_compliances(self) -> aggregated_policy_compliances_request_builder.AggregatedPolicyCompliancesRequestBuilder:
        """
        Provides operations to manage the aggregatedPolicyCompliances property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .aggregated_policy_compliances import aggregated_policy_compliances_request_builder

        return aggregated_policy_compliances_request_builder.AggregatedPolicyCompliancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_performances(self) -> app_performances_request_builder.AppPerformancesRequestBuilder:
        """
        Provides operations to manage the appPerformances property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .app_performances import app_performances_request_builder

        return app_performances_request_builder.AppPerformancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def audit_events(self) -> audit_events_request_builder.AuditEventsRequestBuilder:
        """
        Provides operations to manage the auditEvents property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .audit_events import audit_events_request_builder

        return audit_events_request_builder.AuditEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_pc_connections(self) -> cloud_pc_connections_request_builder.CloudPcConnectionsRequestBuilder:
        """
        Provides operations to manage the cloudPcConnections property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .cloud_pc_connections import cloud_pc_connections_request_builder

        return cloud_pc_connections_request_builder.CloudPcConnectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_pc_devices(self) -> cloud_pc_devices_request_builder.CloudPcDevicesRequestBuilder:
        """
        Provides operations to manage the cloudPcDevices property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .cloud_pc_devices import cloud_pc_devices_request_builder

        return cloud_pc_devices_request_builder.CloudPcDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_pcs_overview(self) -> cloud_pcs_overview_request_builder.CloudPcsOverviewRequestBuilder:
        """
        Provides operations to manage the cloudPcsOverview property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .cloud_pcs_overview import cloud_pcs_overview_request_builder

        return cloud_pcs_overview_request_builder.CloudPcsOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conditional_access_policy_coverages(self) -> conditional_access_policy_coverages_request_builder.ConditionalAccessPolicyCoveragesRequestBuilder:
        """
        Provides operations to manage the conditionalAccessPolicyCoverages property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .conditional_access_policy_coverages import conditional_access_policy_coverages_request_builder

        return conditional_access_policy_coverages_request_builder.ConditionalAccessPolicyCoveragesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def credential_user_registrations_summaries(self) -> credential_user_registrations_summaries_request_builder.CredentialUserRegistrationsSummariesRequestBuilder:
        """
        Provides operations to manage the credentialUserRegistrationsSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .credential_user_registrations_summaries import credential_user_registrations_summaries_request_builder

        return credential_user_registrations_summaries_request_builder.CredentialUserRegistrationsSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_app_performances(self) -> device_app_performances_request_builder.DeviceAppPerformancesRequestBuilder:
        """
        Provides operations to manage the deviceAppPerformances property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .device_app_performances import device_app_performances_request_builder

        return device_app_performances_request_builder.DeviceAppPerformancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_setting_state_summaries(self) -> device_compliance_policy_setting_state_summaries_request_builder.DeviceCompliancePolicySettingStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicySettingStateSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .device_compliance_policy_setting_state_summaries import device_compliance_policy_setting_state_summaries_request_builder

        return device_compliance_policy_setting_state_summaries_request_builder.DeviceCompliancePolicySettingStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_health_statuses(self) -> device_health_statuses_request_builder.DeviceHealthStatusesRequestBuilder:
        """
        Provides operations to manage the deviceHealthStatuses property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .device_health_statuses import device_health_statuses_request_builder

        return device_health_statuses_request_builder.DeviceHealthStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_compliances(self) -> managed_device_compliances_request_builder.ManagedDeviceCompliancesRequestBuilder:
        """
        Provides operations to manage the managedDeviceCompliances property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_device_compliances import managed_device_compliances_request_builder

        return managed_device_compliances_request_builder.ManagedDeviceCompliancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_compliance_trends(self) -> managed_device_compliance_trends_request_builder.ManagedDeviceComplianceTrendsRequestBuilder:
        """
        Provides operations to manage the managedDeviceComplianceTrends property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_device_compliance_trends import managed_device_compliance_trends_request_builder

        return managed_device_compliance_trends_request_builder.ManagedDeviceComplianceTrendsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_alert_logs(self) -> managed_tenant_alert_logs_request_builder.ManagedTenantAlertLogsRequestBuilder:
        """
        Provides operations to manage the managedTenantAlertLogs property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_alert_logs import managed_tenant_alert_logs_request_builder

        return managed_tenant_alert_logs_request_builder.ManagedTenantAlertLogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_alert_rule_definitions(self) -> managed_tenant_alert_rule_definitions_request_builder.ManagedTenantAlertRuleDefinitionsRequestBuilder:
        """
        Provides operations to manage the managedTenantAlertRuleDefinitions property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_alert_rule_definitions import managed_tenant_alert_rule_definitions_request_builder

        return managed_tenant_alert_rule_definitions_request_builder.ManagedTenantAlertRuleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_alert_rules(self) -> managed_tenant_alert_rules_request_builder.ManagedTenantAlertRulesRequestBuilder:
        """
        Provides operations to manage the managedTenantAlertRules property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_alert_rules import managed_tenant_alert_rules_request_builder

        return managed_tenant_alert_rules_request_builder.ManagedTenantAlertRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_alerts(self) -> managed_tenant_alerts_request_builder.ManagedTenantAlertsRequestBuilder:
        """
        Provides operations to manage the managedTenantAlerts property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_alerts import managed_tenant_alerts_request_builder

        return managed_tenant_alerts_request_builder.ManagedTenantAlertsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_api_notifications(self) -> managed_tenant_api_notifications_request_builder.ManagedTenantApiNotificationsRequestBuilder:
        """
        Provides operations to manage the managedTenantApiNotifications property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_api_notifications import managed_tenant_api_notifications_request_builder

        return managed_tenant_api_notifications_request_builder.ManagedTenantApiNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_email_notifications(self) -> managed_tenant_email_notifications_request_builder.ManagedTenantEmailNotificationsRequestBuilder:
        """
        Provides operations to manage the managedTenantEmailNotifications property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_email_notifications import managed_tenant_email_notifications_request_builder

        return managed_tenant_email_notifications_request_builder.ManagedTenantEmailNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_ticketing_endpoints(self) -> managed_tenant_ticketing_endpoints_request_builder.ManagedTenantTicketingEndpointsRequestBuilder:
        """
        Provides operations to manage the managedTenantTicketingEndpoints property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_ticketing_endpoints import managed_tenant_ticketing_endpoints_request_builder

        return managed_tenant_ticketing_endpoints_request_builder.ManagedTenantTicketingEndpointsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_actions(self) -> management_actions_request_builder.ManagementActionsRequestBuilder:
        """
        Provides operations to manage the managementActions property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_actions import management_actions_request_builder

        return management_actions_request_builder.ManagementActionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_action_tenant_deployment_statuses(self) -> management_action_tenant_deployment_statuses_request_builder.ManagementActionTenantDeploymentStatusesRequestBuilder:
        """
        Provides operations to manage the managementActionTenantDeploymentStatuses property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_action_tenant_deployment_statuses import management_action_tenant_deployment_statuses_request_builder

        return management_action_tenant_deployment_statuses_request_builder.ManagementActionTenantDeploymentStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_intents(self) -> management_intents_request_builder.ManagementIntentsRequestBuilder:
        """
        Provides operations to manage the managementIntents property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_intents import management_intents_request_builder

        return management_intents_request_builder.ManagementIntentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_template_collections(self) -> management_template_collections_request_builder.ManagementTemplateCollectionsRequestBuilder:
        """
        Provides operations to manage the managementTemplateCollections property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_template_collections import management_template_collections_request_builder

        return management_template_collections_request_builder.ManagementTemplateCollectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_template_collection_tenant_summaries(self) -> management_template_collection_tenant_summaries_request_builder.ManagementTemplateCollectionTenantSummariesRequestBuilder:
        """
        Provides operations to manage the managementTemplateCollectionTenantSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_template_collection_tenant_summaries import management_template_collection_tenant_summaries_request_builder

        return management_template_collection_tenant_summaries_request_builder.ManagementTemplateCollectionTenantSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_templates(self) -> management_templates_request_builder.ManagementTemplatesRequestBuilder:
        """
        Provides operations to manage the managementTemplates property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_templates import management_templates_request_builder

        return management_templates_request_builder.ManagementTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_template_steps(self) -> management_template_steps_request_builder.ManagementTemplateStepsRequestBuilder:
        """
        Provides operations to manage the managementTemplateSteps property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_template_steps import management_template_steps_request_builder

        return management_template_steps_request_builder.ManagementTemplateStepsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_template_step_tenant_summaries(self) -> management_template_step_tenant_summaries_request_builder.ManagementTemplateStepTenantSummariesRequestBuilder:
        """
        Provides operations to manage the managementTemplateStepTenantSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_template_step_tenant_summaries import management_template_step_tenant_summaries_request_builder

        return management_template_step_tenant_summaries_request_builder.ManagementTemplateStepTenantSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_template_step_versions(self) -> management_template_step_versions_request_builder.ManagementTemplateStepVersionsRequestBuilder:
        """
        Provides operations to manage the managementTemplateStepVersions property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_template_step_versions import management_template_step_versions_request_builder

        return management_template_step_versions_request_builder.ManagementTemplateStepVersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def my_roles(self) -> my_roles_request_builder.MyRolesRequestBuilder:
        """
        Provides operations to manage the myRoles property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .my_roles import my_roles_request_builder

        return my_roles_request_builder.MyRolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenant_groups(self) -> tenant_groups_request_builder.TenantGroupsRequestBuilder:
        """
        Provides operations to manage the tenantGroups property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .tenant_groups import tenant_groups_request_builder

        return tenant_groups_request_builder.TenantGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenants(self) -> tenants_request_builder.TenantsRequestBuilder:
        """
        Provides operations to manage the tenants property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .tenants import tenants_request_builder

        return tenants_request_builder.TenantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenants_customized_information(self) -> tenants_customized_information_request_builder.TenantsCustomizedInformationRequestBuilder:
        """
        Provides operations to manage the tenantsCustomizedInformation property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .tenants_customized_information import tenants_customized_information_request_builder

        return tenants_customized_information_request_builder.TenantsCustomizedInformationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenants_detailed_information(self) -> tenants_detailed_information_request_builder.TenantsDetailedInformationRequestBuilder:
        """
        Provides operations to manage the tenantsDetailedInformation property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .tenants_detailed_information import tenants_detailed_information_request_builder

        return tenants_detailed_information_request_builder.TenantsDetailedInformationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenant_tags(self) -> tenant_tags_request_builder.TenantTagsRequestBuilder:
        """
        Provides operations to manage the tenantTags property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .tenant_tags import tenant_tags_request_builder

        return tenant_tags_request_builder.TenantTagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_device_malware_states(self) -> windows_device_malware_states_request_builder.WindowsDeviceMalwareStatesRequestBuilder:
        """
        Provides operations to manage the windowsDeviceMalwareStates property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .windows_device_malware_states import windows_device_malware_states_request_builder

        return windows_device_malware_states_request_builder.WindowsDeviceMalwareStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_protection_states(self) -> windows_protection_states_request_builder.WindowsProtectionStatesRequestBuilder:
        """
        Provides operations to manage the windowsProtectionStates property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .windows_protection_states import windows_protection_states_request_builder

        return windows_protection_states_request_builder.WindowsProtectionStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ManagedTenantsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ManagedTenantsRequestBuilderGetQueryParameters():
        """
        The operations available to interact with the multi-tenant management platform.
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
    class ManagedTenantsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ManagedTenantsRequestBuilder.ManagedTenantsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ManagedTenantsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

