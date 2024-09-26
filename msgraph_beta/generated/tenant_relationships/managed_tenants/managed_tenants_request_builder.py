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
    from ...models.managed_tenants.managed_tenant import ManagedTenant
    from ...models.o_data_errors.o_data_error import ODataError
    from .aggregated_policy_compliances.aggregated_policy_compliances_request_builder import AggregatedPolicyCompliancesRequestBuilder
    from .app_performances.app_performances_request_builder import AppPerformancesRequestBuilder
    from .audit_events.audit_events_request_builder import AuditEventsRequestBuilder
    from .cloud_pcs_overview.cloud_pcs_overview_request_builder import CloudPcsOverviewRequestBuilder
    from .cloud_pc_connections.cloud_pc_connections_request_builder import CloudPcConnectionsRequestBuilder
    from .cloud_pc_devices.cloud_pc_devices_request_builder import CloudPcDevicesRequestBuilder
    from .conditional_access_policy_coverages.conditional_access_policy_coverages_request_builder import ConditionalAccessPolicyCoveragesRequestBuilder
    from .credential_user_registrations_summaries.credential_user_registrations_summaries_request_builder import CredentialUserRegistrationsSummariesRequestBuilder
    from .device_app_performances.device_app_performances_request_builder import DeviceAppPerformancesRequestBuilder
    from .device_compliance_policy_setting_state_summaries.device_compliance_policy_setting_state_summaries_request_builder import DeviceCompliancePolicySettingStateSummariesRequestBuilder
    from .device_health_statuses.device_health_statuses_request_builder import DeviceHealthStatusesRequestBuilder
    from .managed_device_compliances.managed_device_compliances_request_builder import ManagedDeviceCompliancesRequestBuilder
    from .managed_device_compliance_trends.managed_device_compliance_trends_request_builder import ManagedDeviceComplianceTrendsRequestBuilder
    from .managed_tenant_alerts.managed_tenant_alerts_request_builder import ManagedTenantAlertsRequestBuilder
    from .managed_tenant_alert_logs.managed_tenant_alert_logs_request_builder import ManagedTenantAlertLogsRequestBuilder
    from .managed_tenant_alert_rules.managed_tenant_alert_rules_request_builder import ManagedTenantAlertRulesRequestBuilder
    from .managed_tenant_alert_rule_definitions.managed_tenant_alert_rule_definitions_request_builder import ManagedTenantAlertRuleDefinitionsRequestBuilder
    from .managed_tenant_api_notifications.managed_tenant_api_notifications_request_builder import ManagedTenantApiNotificationsRequestBuilder
    from .managed_tenant_email_notifications.managed_tenant_email_notifications_request_builder import ManagedTenantEmailNotificationsRequestBuilder
    from .managed_tenant_ticketing_endpoints.managed_tenant_ticketing_endpoints_request_builder import ManagedTenantTicketingEndpointsRequestBuilder
    from .management_actions.management_actions_request_builder import ManagementActionsRequestBuilder
    from .management_action_tenant_deployment_statuses.management_action_tenant_deployment_statuses_request_builder import ManagementActionTenantDeploymentStatusesRequestBuilder
    from .management_intents.management_intents_request_builder import ManagementIntentsRequestBuilder
    from .management_templates.management_templates_request_builder import ManagementTemplatesRequestBuilder
    from .management_template_collections.management_template_collections_request_builder import ManagementTemplateCollectionsRequestBuilder
    from .management_template_collection_tenant_summaries.management_template_collection_tenant_summaries_request_builder import ManagementTemplateCollectionTenantSummariesRequestBuilder
    from .management_template_steps.management_template_steps_request_builder import ManagementTemplateStepsRequestBuilder
    from .management_template_step_tenant_summaries.management_template_step_tenant_summaries_request_builder import ManagementTemplateStepTenantSummariesRequestBuilder
    from .management_template_step_versions.management_template_step_versions_request_builder import ManagementTemplateStepVersionsRequestBuilder
    from .my_roles.my_roles_request_builder import MyRolesRequestBuilder
    from .tenants.tenants_request_builder import TenantsRequestBuilder
    from .tenants_customized_information.tenants_customized_information_request_builder import TenantsCustomizedInformationRequestBuilder
    from .tenants_detailed_information.tenants_detailed_information_request_builder import TenantsDetailedInformationRequestBuilder
    from .tenant_groups.tenant_groups_request_builder import TenantGroupsRequestBuilder
    from .tenant_tags.tenant_tags_request_builder import TenantTagsRequestBuilder
    from .windows_device_malware_states.windows_device_malware_states_request_builder import WindowsDeviceMalwareStatesRequestBuilder
    from .windows_protection_states.windows_protection_states_request_builder import WindowsProtectionStatesRequestBuilder

class ManagedTenantsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the managedTenants property of the microsoft.graph.tenantRelationship entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ManagedTenantsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/tenantRelationships/managedTenants{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property managedTenants for tenantRelationships
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ManagedTenantsRequestBuilderGetQueryParameters]] = None) -> Optional[ManagedTenant]:
        """
        The operations available to interact with the multi-tenant management platform.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagedTenant]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.managed_tenants.managed_tenant import ManagedTenant

        return await self.request_adapter.send_async(request_info, ManagedTenant, error_mapping)
    
    async def patch(self,body: ManagedTenant, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManagedTenant]:
        """
        Update the navigation property managedTenants in tenantRelationships
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagedTenant]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.managed_tenants.managed_tenant import ManagedTenant

        return await self.request_adapter.send_async(request_info, ManagedTenant, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property managedTenants for tenantRelationships
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ManagedTenantsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The operations available to interact with the multi-tenant management platform.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ManagedTenant, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property managedTenants in tenantRelationships
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
    
    def with_url(self,raw_url: str) -> ManagedTenantsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ManagedTenantsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ManagedTenantsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def aggregated_policy_compliances(self) -> AggregatedPolicyCompliancesRequestBuilder:
        """
        Provides operations to manage the aggregatedPolicyCompliances property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .aggregated_policy_compliances.aggregated_policy_compliances_request_builder import AggregatedPolicyCompliancesRequestBuilder

        return AggregatedPolicyCompliancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_performances(self) -> AppPerformancesRequestBuilder:
        """
        Provides operations to manage the appPerformances property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .app_performances.app_performances_request_builder import AppPerformancesRequestBuilder

        return AppPerformancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def audit_events(self) -> AuditEventsRequestBuilder:
        """
        Provides operations to manage the auditEvents property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .audit_events.audit_events_request_builder import AuditEventsRequestBuilder

        return AuditEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_pc_connections(self) -> CloudPcConnectionsRequestBuilder:
        """
        Provides operations to manage the cloudPcConnections property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .cloud_pc_connections.cloud_pc_connections_request_builder import CloudPcConnectionsRequestBuilder

        return CloudPcConnectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_pc_devices(self) -> CloudPcDevicesRequestBuilder:
        """
        Provides operations to manage the cloudPcDevices property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .cloud_pc_devices.cloud_pc_devices_request_builder import CloudPcDevicesRequestBuilder

        return CloudPcDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_pcs_overview(self) -> CloudPcsOverviewRequestBuilder:
        """
        Provides operations to manage the cloudPcsOverview property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .cloud_pcs_overview.cloud_pcs_overview_request_builder import CloudPcsOverviewRequestBuilder

        return CloudPcsOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conditional_access_policy_coverages(self) -> ConditionalAccessPolicyCoveragesRequestBuilder:
        """
        Provides operations to manage the conditionalAccessPolicyCoverages property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .conditional_access_policy_coverages.conditional_access_policy_coverages_request_builder import ConditionalAccessPolicyCoveragesRequestBuilder

        return ConditionalAccessPolicyCoveragesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def credential_user_registrations_summaries(self) -> CredentialUserRegistrationsSummariesRequestBuilder:
        """
        Provides operations to manage the credentialUserRegistrationsSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .credential_user_registrations_summaries.credential_user_registrations_summaries_request_builder import CredentialUserRegistrationsSummariesRequestBuilder

        return CredentialUserRegistrationsSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_app_performances(self) -> DeviceAppPerformancesRequestBuilder:
        """
        Provides operations to manage the deviceAppPerformances property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .device_app_performances.device_app_performances_request_builder import DeviceAppPerformancesRequestBuilder

        return DeviceAppPerformancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_setting_state_summaries(self) -> DeviceCompliancePolicySettingStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicySettingStateSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .device_compliance_policy_setting_state_summaries.device_compliance_policy_setting_state_summaries_request_builder import DeviceCompliancePolicySettingStateSummariesRequestBuilder

        return DeviceCompliancePolicySettingStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_health_statuses(self) -> DeviceHealthStatusesRequestBuilder:
        """
        Provides operations to manage the deviceHealthStatuses property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .device_health_statuses.device_health_statuses_request_builder import DeviceHealthStatusesRequestBuilder

        return DeviceHealthStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_compliance_trends(self) -> ManagedDeviceComplianceTrendsRequestBuilder:
        """
        Provides operations to manage the managedDeviceComplianceTrends property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_device_compliance_trends.managed_device_compliance_trends_request_builder import ManagedDeviceComplianceTrendsRequestBuilder

        return ManagedDeviceComplianceTrendsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_compliances(self) -> ManagedDeviceCompliancesRequestBuilder:
        """
        Provides operations to manage the managedDeviceCompliances property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_device_compliances.managed_device_compliances_request_builder import ManagedDeviceCompliancesRequestBuilder

        return ManagedDeviceCompliancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_alert_logs(self) -> ManagedTenantAlertLogsRequestBuilder:
        """
        Provides operations to manage the managedTenantAlertLogs property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_alert_logs.managed_tenant_alert_logs_request_builder import ManagedTenantAlertLogsRequestBuilder

        return ManagedTenantAlertLogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_alert_rule_definitions(self) -> ManagedTenantAlertRuleDefinitionsRequestBuilder:
        """
        Provides operations to manage the managedTenantAlertRuleDefinitions property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_alert_rule_definitions.managed_tenant_alert_rule_definitions_request_builder import ManagedTenantAlertRuleDefinitionsRequestBuilder

        return ManagedTenantAlertRuleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_alert_rules(self) -> ManagedTenantAlertRulesRequestBuilder:
        """
        Provides operations to manage the managedTenantAlertRules property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_alert_rules.managed_tenant_alert_rules_request_builder import ManagedTenantAlertRulesRequestBuilder

        return ManagedTenantAlertRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_alerts(self) -> ManagedTenantAlertsRequestBuilder:
        """
        Provides operations to manage the managedTenantAlerts property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_alerts.managed_tenant_alerts_request_builder import ManagedTenantAlertsRequestBuilder

        return ManagedTenantAlertsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_api_notifications(self) -> ManagedTenantApiNotificationsRequestBuilder:
        """
        Provides operations to manage the managedTenantApiNotifications property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_api_notifications.managed_tenant_api_notifications_request_builder import ManagedTenantApiNotificationsRequestBuilder

        return ManagedTenantApiNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_email_notifications(self) -> ManagedTenantEmailNotificationsRequestBuilder:
        """
        Provides operations to manage the managedTenantEmailNotifications property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_email_notifications.managed_tenant_email_notifications_request_builder import ManagedTenantEmailNotificationsRequestBuilder

        return ManagedTenantEmailNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_tenant_ticketing_endpoints(self) -> ManagedTenantTicketingEndpointsRequestBuilder:
        """
        Provides operations to manage the managedTenantTicketingEndpoints property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .managed_tenant_ticketing_endpoints.managed_tenant_ticketing_endpoints_request_builder import ManagedTenantTicketingEndpointsRequestBuilder

        return ManagedTenantTicketingEndpointsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_action_tenant_deployment_statuses(self) -> ManagementActionTenantDeploymentStatusesRequestBuilder:
        """
        Provides operations to manage the managementActionTenantDeploymentStatuses property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_action_tenant_deployment_statuses.management_action_tenant_deployment_statuses_request_builder import ManagementActionTenantDeploymentStatusesRequestBuilder

        return ManagementActionTenantDeploymentStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_actions(self) -> ManagementActionsRequestBuilder:
        """
        Provides operations to manage the managementActions property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_actions.management_actions_request_builder import ManagementActionsRequestBuilder

        return ManagementActionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_intents(self) -> ManagementIntentsRequestBuilder:
        """
        Provides operations to manage the managementIntents property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_intents.management_intents_request_builder import ManagementIntentsRequestBuilder

        return ManagementIntentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_template_collection_tenant_summaries(self) -> ManagementTemplateCollectionTenantSummariesRequestBuilder:
        """
        Provides operations to manage the managementTemplateCollectionTenantSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_template_collection_tenant_summaries.management_template_collection_tenant_summaries_request_builder import ManagementTemplateCollectionTenantSummariesRequestBuilder

        return ManagementTemplateCollectionTenantSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_template_collections(self) -> ManagementTemplateCollectionsRequestBuilder:
        """
        Provides operations to manage the managementTemplateCollections property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_template_collections.management_template_collections_request_builder import ManagementTemplateCollectionsRequestBuilder

        return ManagementTemplateCollectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_template_step_tenant_summaries(self) -> ManagementTemplateStepTenantSummariesRequestBuilder:
        """
        Provides operations to manage the managementTemplateStepTenantSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_template_step_tenant_summaries.management_template_step_tenant_summaries_request_builder import ManagementTemplateStepTenantSummariesRequestBuilder

        return ManagementTemplateStepTenantSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_template_step_versions(self) -> ManagementTemplateStepVersionsRequestBuilder:
        """
        Provides operations to manage the managementTemplateStepVersions property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_template_step_versions.management_template_step_versions_request_builder import ManagementTemplateStepVersionsRequestBuilder

        return ManagementTemplateStepVersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_template_steps(self) -> ManagementTemplateStepsRequestBuilder:
        """
        Provides operations to manage the managementTemplateSteps property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_template_steps.management_template_steps_request_builder import ManagementTemplateStepsRequestBuilder

        return ManagementTemplateStepsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_templates(self) -> ManagementTemplatesRequestBuilder:
        """
        Provides operations to manage the managementTemplates property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .management_templates.management_templates_request_builder import ManagementTemplatesRequestBuilder

        return ManagementTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def my_roles(self) -> MyRolesRequestBuilder:
        """
        Provides operations to manage the myRoles property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .my_roles.my_roles_request_builder import MyRolesRequestBuilder

        return MyRolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenant_groups(self) -> TenantGroupsRequestBuilder:
        """
        Provides operations to manage the tenantGroups property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .tenant_groups.tenant_groups_request_builder import TenantGroupsRequestBuilder

        return TenantGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenant_tags(self) -> TenantTagsRequestBuilder:
        """
        Provides operations to manage the tenantTags property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .tenant_tags.tenant_tags_request_builder import TenantTagsRequestBuilder

        return TenantTagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenants(self) -> TenantsRequestBuilder:
        """
        Provides operations to manage the tenants property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .tenants.tenants_request_builder import TenantsRequestBuilder

        return TenantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenants_customized_information(self) -> TenantsCustomizedInformationRequestBuilder:
        """
        Provides operations to manage the tenantsCustomizedInformation property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .tenants_customized_information.tenants_customized_information_request_builder import TenantsCustomizedInformationRequestBuilder

        return TenantsCustomizedInformationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenants_detailed_information(self) -> TenantsDetailedInformationRequestBuilder:
        """
        Provides operations to manage the tenantsDetailedInformation property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .tenants_detailed_information.tenants_detailed_information_request_builder import TenantsDetailedInformationRequestBuilder

        return TenantsDetailedInformationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_device_malware_states(self) -> WindowsDeviceMalwareStatesRequestBuilder:
        """
        Provides operations to manage the windowsDeviceMalwareStates property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .windows_device_malware_states.windows_device_malware_states_request_builder import WindowsDeviceMalwareStatesRequestBuilder

        return WindowsDeviceMalwareStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_protection_states(self) -> WindowsProtectionStatesRequestBuilder:
        """
        Provides operations to manage the windowsProtectionStates property of the microsoft.graph.managedTenants.managedTenant entity.
        """
        from .windows_protection_states.windows_protection_states_request_builder import WindowsProtectionStatesRequestBuilder

        return WindowsProtectionStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ManagedTenantsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManagedTenantsRequestBuilderGetQueryParameters():
        """
        The operations available to interact with the multi-tenant management platform.
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
    class ManagedTenantsRequestBuilderGetRequestConfiguration(RequestConfiguration[ManagedTenantsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManagedTenantsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

