from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import aggregated_policy_compliance, app_performance, audit_event, cloud_pc_connection, cloud_pc_device, cloud_pc_overview, conditional_access_policy_coverage, credential_user_registrations_summary, device_app_performance, device_compliance_policy_setting_state_summary, device_health_status, managed_device_compliance, managed_device_compliance_trend, managed_tenant_alert, managed_tenant_alert_log, managed_tenant_alert_rule, managed_tenant_alert_rule_definition, managed_tenant_api_notification, managed_tenant_email_notification, managed_tenant_ticketing_endpoint, management_action, management_action_tenant_deployment_status, management_intent, management_template, management_template_collection, management_template_collection_tenant_summary, management_template_step, management_template_step_tenant_summary, management_template_step_version, my_role, tenant, tenant_customized_information, tenant_detailed_information, tenant_group, tenant_tag, windows_device_malware_state, windows_protection_state
    from .. import entity

from .. import entity

class ManagedTenant(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new ManagedTenant and sets the default values.
        """
        super().__init__()
        # Aggregate view of device compliance policies across managed tenants.
        self._aggregated_policy_compliances: Optional[List[aggregated_policy_compliance.AggregatedPolicyCompliance]] = None
        # The appPerformances property
        self._app_performances: Optional[List[app_performance.AppPerformance]] = None
        # The collection of audit events across managed tenants.
        self._audit_events: Optional[List[audit_event.AuditEvent]] = None
        # The collection of cloud PC connections across managed tenants.
        self._cloud_pc_connections: Optional[List[cloud_pc_connection.CloudPcConnection]] = None
        # The collection of cloud PC devices across managed tenants.
        self._cloud_pc_devices: Optional[List[cloud_pc_device.CloudPcDevice]] = None
        # Overview of cloud PC information across managed tenants.
        self._cloud_pcs_overview: Optional[List[cloud_pc_overview.CloudPcOverview]] = None
        # Aggregate view of conditional access policy coverage across managed tenants.
        self._conditional_access_policy_coverages: Optional[List[conditional_access_policy_coverage.ConditionalAccessPolicyCoverage]] = None
        # Summary information for user registration for multi-factor authentication and self service password reset across managed tenants.
        self._credential_user_registrations_summaries: Optional[List[credential_user_registrations_summary.CredentialUserRegistrationsSummary]] = None
        # The deviceAppPerformances property
        self._device_app_performances: Optional[List[device_app_performance.DeviceAppPerformance]] = None
        # Summary information for device compliance policy setting states across managed tenants.
        self._device_compliance_policy_setting_state_summaries: Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]] = None
        # The deviceHealthStatuses property
        self._device_health_statuses: Optional[List[device_health_status.DeviceHealthStatus]] = None
        # Trend insights for device compliance across managed tenants.
        self._managed_device_compliance_trends: Optional[List[managed_device_compliance_trend.ManagedDeviceComplianceTrend]] = None
        # The collection of compliance for managed devices across managed tenants.
        self._managed_device_compliances: Optional[List[managed_device_compliance.ManagedDeviceCompliance]] = None
        # The managedTenantAlertLogs property
        self._managed_tenant_alert_logs: Optional[List[managed_tenant_alert_log.ManagedTenantAlertLog]] = None
        # The managedTenantAlertRuleDefinitions property
        self._managed_tenant_alert_rule_definitions: Optional[List[managed_tenant_alert_rule_definition.ManagedTenantAlertRuleDefinition]] = None
        # The managedTenantAlertRules property
        self._managed_tenant_alert_rules: Optional[List[managed_tenant_alert_rule.ManagedTenantAlertRule]] = None
        # The managedTenantAlerts property
        self._managed_tenant_alerts: Optional[List[managed_tenant_alert.ManagedTenantAlert]] = None
        # The managedTenantApiNotifications property
        self._managed_tenant_api_notifications: Optional[List[managed_tenant_api_notification.ManagedTenantApiNotification]] = None
        # The managedTenantEmailNotifications property
        self._managed_tenant_email_notifications: Optional[List[managed_tenant_email_notification.ManagedTenantEmailNotification]] = None
        # The managedTenantTicketingEndpoints property
        self._managed_tenant_ticketing_endpoints: Optional[List[managed_tenant_ticketing_endpoint.ManagedTenantTicketingEndpoint]] = None
        # The tenant level status of management actions across managed tenants.
        self._management_action_tenant_deployment_statuses: Optional[List[management_action_tenant_deployment_status.ManagementActionTenantDeploymentStatus]] = None
        # The collection of baseline management actions across managed tenants.
        self._management_actions: Optional[List[management_action.ManagementAction]] = None
        # The collection of baseline management intents across managed tenants.
        self._management_intents: Optional[List[management_intent.ManagementIntent]] = None
        # The managementTemplateCollectionTenantSummaries property
        self._management_template_collection_tenant_summaries: Optional[List[management_template_collection_tenant_summary.ManagementTemplateCollectionTenantSummary]] = None
        # The managementTemplateCollections property
        self._management_template_collections: Optional[List[management_template_collection.ManagementTemplateCollection]] = None
        # The managementTemplateStepTenantSummaries property
        self._management_template_step_tenant_summaries: Optional[List[management_template_step_tenant_summary.ManagementTemplateStepTenantSummary]] = None
        # The managementTemplateStepVersions property
        self._management_template_step_versions: Optional[List[management_template_step_version.ManagementTemplateStepVersion]] = None
        # The managementTemplateSteps property
        self._management_template_steps: Optional[List[management_template_step.ManagementTemplateStep]] = None
        # The collection of baseline management templates across managed tenants.
        self._management_templates: Optional[List[management_template.ManagementTemplate]] = None
        # The collection of role assignments to a signed-in user for a managed tenant.
        self._my_roles: Optional[List[my_role.MyRole]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The collection of a logical grouping of managed tenants used by the multi-tenant management platform.
        self._tenant_groups: Optional[List[tenant_group.TenantGroup]] = None
        # The collection of tenant tags across managed tenants.
        self._tenant_tags: Optional[List[tenant_tag.TenantTag]] = None
        # The collection of tenants associated with the managing entity.
        self._tenants: Optional[List[tenant.Tenant]] = None
        # The collection of tenant level customized information across managed tenants.
        self._tenants_customized_information: Optional[List[tenant_customized_information.TenantCustomizedInformation]] = None
        # The collection tenant level detailed information across managed tenants.
        self._tenants_detailed_information: Optional[List[tenant_detailed_information.TenantDetailedInformation]] = None
        # The state of malware for Windows devices, registered with Microsoft Endpoint Manager, across managed tenants.
        self._windows_device_malware_states: Optional[List[windows_device_malware_state.WindowsDeviceMalwareState]] = None
        # The protection state for Windows devices, registered with Microsoft Endpoint Manager, across managed tenants.
        self._windows_protection_states: Optional[List[windows_protection_state.WindowsProtectionState]] = None
    
    @property
    def aggregated_policy_compliances(self,) -> Optional[List[aggregated_policy_compliance.AggregatedPolicyCompliance]]:
        """
        Gets the aggregatedPolicyCompliances property value. Aggregate view of device compliance policies across managed tenants.
        Returns: Optional[List[aggregated_policy_compliance.AggregatedPolicyCompliance]]
        """
        return self._aggregated_policy_compliances
    
    @aggregated_policy_compliances.setter
    def aggregated_policy_compliances(self,value: Optional[List[aggregated_policy_compliance.AggregatedPolicyCompliance]] = None) -> None:
        """
        Sets the aggregatedPolicyCompliances property value. Aggregate view of device compliance policies across managed tenants.
        Args:
            value: Value to set for the aggregated_policy_compliances property.
        """
        self._aggregated_policy_compliances = value
    
    @property
    def app_performances(self,) -> Optional[List[app_performance.AppPerformance]]:
        """
        Gets the appPerformances property value. The appPerformances property
        Returns: Optional[List[app_performance.AppPerformance]]
        """
        return self._app_performances
    
    @app_performances.setter
    def app_performances(self,value: Optional[List[app_performance.AppPerformance]] = None) -> None:
        """
        Sets the appPerformances property value. The appPerformances property
        Args:
            value: Value to set for the app_performances property.
        """
        self._app_performances = value
    
    @property
    def audit_events(self,) -> Optional[List[audit_event.AuditEvent]]:
        """
        Gets the auditEvents property value. The collection of audit events across managed tenants.
        Returns: Optional[List[audit_event.AuditEvent]]
        """
        return self._audit_events
    
    @audit_events.setter
    def audit_events(self,value: Optional[List[audit_event.AuditEvent]] = None) -> None:
        """
        Sets the auditEvents property value. The collection of audit events across managed tenants.
        Args:
            value: Value to set for the audit_events property.
        """
        self._audit_events = value
    
    @property
    def cloud_pc_connections(self,) -> Optional[List[cloud_pc_connection.CloudPcConnection]]:
        """
        Gets the cloudPcConnections property value. The collection of cloud PC connections across managed tenants.
        Returns: Optional[List[cloud_pc_connection.CloudPcConnection]]
        """
        return self._cloud_pc_connections
    
    @cloud_pc_connections.setter
    def cloud_pc_connections(self,value: Optional[List[cloud_pc_connection.CloudPcConnection]] = None) -> None:
        """
        Sets the cloudPcConnections property value. The collection of cloud PC connections across managed tenants.
        Args:
            value: Value to set for the cloud_pc_connections property.
        """
        self._cloud_pc_connections = value
    
    @property
    def cloud_pc_devices(self,) -> Optional[List[cloud_pc_device.CloudPcDevice]]:
        """
        Gets the cloudPcDevices property value. The collection of cloud PC devices across managed tenants.
        Returns: Optional[List[cloud_pc_device.CloudPcDevice]]
        """
        return self._cloud_pc_devices
    
    @cloud_pc_devices.setter
    def cloud_pc_devices(self,value: Optional[List[cloud_pc_device.CloudPcDevice]] = None) -> None:
        """
        Sets the cloudPcDevices property value. The collection of cloud PC devices across managed tenants.
        Args:
            value: Value to set for the cloud_pc_devices property.
        """
        self._cloud_pc_devices = value
    
    @property
    def cloud_pcs_overview(self,) -> Optional[List[cloud_pc_overview.CloudPcOverview]]:
        """
        Gets the cloudPcsOverview property value. Overview of cloud PC information across managed tenants.
        Returns: Optional[List[cloud_pc_overview.CloudPcOverview]]
        """
        return self._cloud_pcs_overview
    
    @cloud_pcs_overview.setter
    def cloud_pcs_overview(self,value: Optional[List[cloud_pc_overview.CloudPcOverview]] = None) -> None:
        """
        Sets the cloudPcsOverview property value. Overview of cloud PC information across managed tenants.
        Args:
            value: Value to set for the cloud_pcs_overview property.
        """
        self._cloud_pcs_overview = value
    
    @property
    def conditional_access_policy_coverages(self,) -> Optional[List[conditional_access_policy_coverage.ConditionalAccessPolicyCoverage]]:
        """
        Gets the conditionalAccessPolicyCoverages property value. Aggregate view of conditional access policy coverage across managed tenants.
        Returns: Optional[List[conditional_access_policy_coverage.ConditionalAccessPolicyCoverage]]
        """
        return self._conditional_access_policy_coverages
    
    @conditional_access_policy_coverages.setter
    def conditional_access_policy_coverages(self,value: Optional[List[conditional_access_policy_coverage.ConditionalAccessPolicyCoverage]] = None) -> None:
        """
        Sets the conditionalAccessPolicyCoverages property value. Aggregate view of conditional access policy coverage across managed tenants.
        Args:
            value: Value to set for the conditional_access_policy_coverages property.
        """
        self._conditional_access_policy_coverages = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedTenant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedTenant
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedTenant()
    
    @property
    def credential_user_registrations_summaries(self,) -> Optional[List[credential_user_registrations_summary.CredentialUserRegistrationsSummary]]:
        """
        Gets the credentialUserRegistrationsSummaries property value. Summary information for user registration for multi-factor authentication and self service password reset across managed tenants.
        Returns: Optional[List[credential_user_registrations_summary.CredentialUserRegistrationsSummary]]
        """
        return self._credential_user_registrations_summaries
    
    @credential_user_registrations_summaries.setter
    def credential_user_registrations_summaries(self,value: Optional[List[credential_user_registrations_summary.CredentialUserRegistrationsSummary]] = None) -> None:
        """
        Sets the credentialUserRegistrationsSummaries property value. Summary information for user registration for multi-factor authentication and self service password reset across managed tenants.
        Args:
            value: Value to set for the credential_user_registrations_summaries property.
        """
        self._credential_user_registrations_summaries = value
    
    @property
    def device_app_performances(self,) -> Optional[List[device_app_performance.DeviceAppPerformance]]:
        """
        Gets the deviceAppPerformances property value. The deviceAppPerformances property
        Returns: Optional[List[device_app_performance.DeviceAppPerformance]]
        """
        return self._device_app_performances
    
    @device_app_performances.setter
    def device_app_performances(self,value: Optional[List[device_app_performance.DeviceAppPerformance]] = None) -> None:
        """
        Sets the deviceAppPerformances property value. The deviceAppPerformances property
        Args:
            value: Value to set for the device_app_performances property.
        """
        self._device_app_performances = value
    
    @property
    def device_compliance_policy_setting_state_summaries(self,) -> Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]]:
        """
        Gets the deviceCompliancePolicySettingStateSummaries property value. Summary information for device compliance policy setting states across managed tenants.
        Returns: Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]]
        """
        return self._device_compliance_policy_setting_state_summaries
    
    @device_compliance_policy_setting_state_summaries.setter
    def device_compliance_policy_setting_state_summaries(self,value: Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]] = None) -> None:
        """
        Sets the deviceCompliancePolicySettingStateSummaries property value. Summary information for device compliance policy setting states across managed tenants.
        Args:
            value: Value to set for the device_compliance_policy_setting_state_summaries property.
        """
        self._device_compliance_policy_setting_state_summaries = value
    
    @property
    def device_health_statuses(self,) -> Optional[List[device_health_status.DeviceHealthStatus]]:
        """
        Gets the deviceHealthStatuses property value. The deviceHealthStatuses property
        Returns: Optional[List[device_health_status.DeviceHealthStatus]]
        """
        return self._device_health_statuses
    
    @device_health_statuses.setter
    def device_health_statuses(self,value: Optional[List[device_health_status.DeviceHealthStatus]] = None) -> None:
        """
        Sets the deviceHealthStatuses property value. The deviceHealthStatuses property
        Args:
            value: Value to set for the device_health_statuses property.
        """
        self._device_health_statuses = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import aggregated_policy_compliance, app_performance, audit_event, cloud_pc_connection, cloud_pc_device, cloud_pc_overview, conditional_access_policy_coverage, credential_user_registrations_summary, device_app_performance, device_compliance_policy_setting_state_summary, device_health_status, managed_device_compliance, managed_device_compliance_trend, managed_tenant_alert, managed_tenant_alert_log, managed_tenant_alert_rule, managed_tenant_alert_rule_definition, managed_tenant_api_notification, managed_tenant_email_notification, managed_tenant_ticketing_endpoint, management_action, management_action_tenant_deployment_status, management_intent, management_template, management_template_collection, management_template_collection_tenant_summary, management_template_step, management_template_step_tenant_summary, management_template_step_version, my_role, tenant, tenant_customized_information, tenant_detailed_information, tenant_group, tenant_tag, windows_device_malware_state, windows_protection_state
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "aggregatedPolicyCompliances": lambda n : setattr(self, 'aggregated_policy_compliances', n.get_collection_of_object_values(aggregated_policy_compliance.AggregatedPolicyCompliance)),
            "appPerformances": lambda n : setattr(self, 'app_performances', n.get_collection_of_object_values(app_performance.AppPerformance)),
            "auditEvents": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(audit_event.AuditEvent)),
            "cloudPcsOverview": lambda n : setattr(self, 'cloud_pcs_overview', n.get_collection_of_object_values(cloud_pc_overview.CloudPcOverview)),
            "cloudPcConnections": lambda n : setattr(self, 'cloud_pc_connections', n.get_collection_of_object_values(cloud_pc_connection.CloudPcConnection)),
            "cloudPcDevices": lambda n : setattr(self, 'cloud_pc_devices', n.get_collection_of_object_values(cloud_pc_device.CloudPcDevice)),
            "conditionalAccessPolicyCoverages": lambda n : setattr(self, 'conditional_access_policy_coverages', n.get_collection_of_object_values(conditional_access_policy_coverage.ConditionalAccessPolicyCoverage)),
            "credentialUserRegistrationsSummaries": lambda n : setattr(self, 'credential_user_registrations_summaries', n.get_collection_of_object_values(credential_user_registrations_summary.CredentialUserRegistrationsSummary)),
            "deviceAppPerformances": lambda n : setattr(self, 'device_app_performances', n.get_collection_of_object_values(device_app_performance.DeviceAppPerformance)),
            "deviceCompliancePolicySettingStateSummaries": lambda n : setattr(self, 'device_compliance_policy_setting_state_summaries', n.get_collection_of_object_values(device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary)),
            "deviceHealthStatuses": lambda n : setattr(self, 'device_health_statuses', n.get_collection_of_object_values(device_health_status.DeviceHealthStatus)),
            "managedDeviceCompliances": lambda n : setattr(self, 'managed_device_compliances', n.get_collection_of_object_values(managed_device_compliance.ManagedDeviceCompliance)),
            "managedDeviceComplianceTrends": lambda n : setattr(self, 'managed_device_compliance_trends', n.get_collection_of_object_values(managed_device_compliance_trend.ManagedDeviceComplianceTrend)),
            "managedTenantAlerts": lambda n : setattr(self, 'managed_tenant_alerts', n.get_collection_of_object_values(managed_tenant_alert.ManagedTenantAlert)),
            "managedTenantAlertLogs": lambda n : setattr(self, 'managed_tenant_alert_logs', n.get_collection_of_object_values(managed_tenant_alert_log.ManagedTenantAlertLog)),
            "managedTenantAlertRules": lambda n : setattr(self, 'managed_tenant_alert_rules', n.get_collection_of_object_values(managed_tenant_alert_rule.ManagedTenantAlertRule)),
            "managedTenantAlertRuleDefinitions": lambda n : setattr(self, 'managed_tenant_alert_rule_definitions', n.get_collection_of_object_values(managed_tenant_alert_rule_definition.ManagedTenantAlertRuleDefinition)),
            "managedTenantApiNotifications": lambda n : setattr(self, 'managed_tenant_api_notifications', n.get_collection_of_object_values(managed_tenant_api_notification.ManagedTenantApiNotification)),
            "managedTenantEmailNotifications": lambda n : setattr(self, 'managed_tenant_email_notifications', n.get_collection_of_object_values(managed_tenant_email_notification.ManagedTenantEmailNotification)),
            "managedTenantTicketingEndpoints": lambda n : setattr(self, 'managed_tenant_ticketing_endpoints', n.get_collection_of_object_values(managed_tenant_ticketing_endpoint.ManagedTenantTicketingEndpoint)),
            "managementActions": lambda n : setattr(self, 'management_actions', n.get_collection_of_object_values(management_action.ManagementAction)),
            "managementActionTenantDeploymentStatuses": lambda n : setattr(self, 'management_action_tenant_deployment_statuses', n.get_collection_of_object_values(management_action_tenant_deployment_status.ManagementActionTenantDeploymentStatus)),
            "managementIntents": lambda n : setattr(self, 'management_intents', n.get_collection_of_object_values(management_intent.ManagementIntent)),
            "managementTemplates": lambda n : setattr(self, 'management_templates', n.get_collection_of_object_values(management_template.ManagementTemplate)),
            "managementTemplateCollections": lambda n : setattr(self, 'management_template_collections', n.get_collection_of_object_values(management_template_collection.ManagementTemplateCollection)),
            "managementTemplateCollectionTenantSummaries": lambda n : setattr(self, 'management_template_collection_tenant_summaries', n.get_collection_of_object_values(management_template_collection_tenant_summary.ManagementTemplateCollectionTenantSummary)),
            "managementTemplateSteps": lambda n : setattr(self, 'management_template_steps', n.get_collection_of_object_values(management_template_step.ManagementTemplateStep)),
            "managementTemplateStepTenantSummaries": lambda n : setattr(self, 'management_template_step_tenant_summaries', n.get_collection_of_object_values(management_template_step_tenant_summary.ManagementTemplateStepTenantSummary)),
            "managementTemplateStepVersions": lambda n : setattr(self, 'management_template_step_versions', n.get_collection_of_object_values(management_template_step_version.ManagementTemplateStepVersion)),
            "myRoles": lambda n : setattr(self, 'my_roles', n.get_collection_of_object_values(my_role.MyRole)),
            "tenants": lambda n : setattr(self, 'tenants', n.get_collection_of_object_values(tenant.Tenant)),
            "tenantsCustomizedInformation": lambda n : setattr(self, 'tenants_customized_information', n.get_collection_of_object_values(tenant_customized_information.TenantCustomizedInformation)),
            "tenantsDetailedInformation": lambda n : setattr(self, 'tenants_detailed_information', n.get_collection_of_object_values(tenant_detailed_information.TenantDetailedInformation)),
            "tenantGroups": lambda n : setattr(self, 'tenant_groups', n.get_collection_of_object_values(tenant_group.TenantGroup)),
            "tenantTags": lambda n : setattr(self, 'tenant_tags', n.get_collection_of_object_values(tenant_tag.TenantTag)),
            "windowsDeviceMalwareStates": lambda n : setattr(self, 'windows_device_malware_states', n.get_collection_of_object_values(windows_device_malware_state.WindowsDeviceMalwareState)),
            "windowsProtectionStates": lambda n : setattr(self, 'windows_protection_states', n.get_collection_of_object_values(windows_protection_state.WindowsProtectionState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_device_compliance_trends(self,) -> Optional[List[managed_device_compliance_trend.ManagedDeviceComplianceTrend]]:
        """
        Gets the managedDeviceComplianceTrends property value. Trend insights for device compliance across managed tenants.
        Returns: Optional[List[managed_device_compliance_trend.ManagedDeviceComplianceTrend]]
        """
        return self._managed_device_compliance_trends
    
    @managed_device_compliance_trends.setter
    def managed_device_compliance_trends(self,value: Optional[List[managed_device_compliance_trend.ManagedDeviceComplianceTrend]] = None) -> None:
        """
        Sets the managedDeviceComplianceTrends property value. Trend insights for device compliance across managed tenants.
        Args:
            value: Value to set for the managed_device_compliance_trends property.
        """
        self._managed_device_compliance_trends = value
    
    @property
    def managed_device_compliances(self,) -> Optional[List[managed_device_compliance.ManagedDeviceCompliance]]:
        """
        Gets the managedDeviceCompliances property value. The collection of compliance for managed devices across managed tenants.
        Returns: Optional[List[managed_device_compliance.ManagedDeviceCompliance]]
        """
        return self._managed_device_compliances
    
    @managed_device_compliances.setter
    def managed_device_compliances(self,value: Optional[List[managed_device_compliance.ManagedDeviceCompliance]] = None) -> None:
        """
        Sets the managedDeviceCompliances property value. The collection of compliance for managed devices across managed tenants.
        Args:
            value: Value to set for the managed_device_compliances property.
        """
        self._managed_device_compliances = value
    
    @property
    def managed_tenant_alert_logs(self,) -> Optional[List[managed_tenant_alert_log.ManagedTenantAlertLog]]:
        """
        Gets the managedTenantAlertLogs property value. The managedTenantAlertLogs property
        Returns: Optional[List[managed_tenant_alert_log.ManagedTenantAlertLog]]
        """
        return self._managed_tenant_alert_logs
    
    @managed_tenant_alert_logs.setter
    def managed_tenant_alert_logs(self,value: Optional[List[managed_tenant_alert_log.ManagedTenantAlertLog]] = None) -> None:
        """
        Sets the managedTenantAlertLogs property value. The managedTenantAlertLogs property
        Args:
            value: Value to set for the managed_tenant_alert_logs property.
        """
        self._managed_tenant_alert_logs = value
    
    @property
    def managed_tenant_alert_rule_definitions(self,) -> Optional[List[managed_tenant_alert_rule_definition.ManagedTenantAlertRuleDefinition]]:
        """
        Gets the managedTenantAlertRuleDefinitions property value. The managedTenantAlertRuleDefinitions property
        Returns: Optional[List[managed_tenant_alert_rule_definition.ManagedTenantAlertRuleDefinition]]
        """
        return self._managed_tenant_alert_rule_definitions
    
    @managed_tenant_alert_rule_definitions.setter
    def managed_tenant_alert_rule_definitions(self,value: Optional[List[managed_tenant_alert_rule_definition.ManagedTenantAlertRuleDefinition]] = None) -> None:
        """
        Sets the managedTenantAlertRuleDefinitions property value. The managedTenantAlertRuleDefinitions property
        Args:
            value: Value to set for the managed_tenant_alert_rule_definitions property.
        """
        self._managed_tenant_alert_rule_definitions = value
    
    @property
    def managed_tenant_alert_rules(self,) -> Optional[List[managed_tenant_alert_rule.ManagedTenantAlertRule]]:
        """
        Gets the managedTenantAlertRules property value. The managedTenantAlertRules property
        Returns: Optional[List[managed_tenant_alert_rule.ManagedTenantAlertRule]]
        """
        return self._managed_tenant_alert_rules
    
    @managed_tenant_alert_rules.setter
    def managed_tenant_alert_rules(self,value: Optional[List[managed_tenant_alert_rule.ManagedTenantAlertRule]] = None) -> None:
        """
        Sets the managedTenantAlertRules property value. The managedTenantAlertRules property
        Args:
            value: Value to set for the managed_tenant_alert_rules property.
        """
        self._managed_tenant_alert_rules = value
    
    @property
    def managed_tenant_alerts(self,) -> Optional[List[managed_tenant_alert.ManagedTenantAlert]]:
        """
        Gets the managedTenantAlerts property value. The managedTenantAlerts property
        Returns: Optional[List[managed_tenant_alert.ManagedTenantAlert]]
        """
        return self._managed_tenant_alerts
    
    @managed_tenant_alerts.setter
    def managed_tenant_alerts(self,value: Optional[List[managed_tenant_alert.ManagedTenantAlert]] = None) -> None:
        """
        Sets the managedTenantAlerts property value. The managedTenantAlerts property
        Args:
            value: Value to set for the managed_tenant_alerts property.
        """
        self._managed_tenant_alerts = value
    
    @property
    def managed_tenant_api_notifications(self,) -> Optional[List[managed_tenant_api_notification.ManagedTenantApiNotification]]:
        """
        Gets the managedTenantApiNotifications property value. The managedTenantApiNotifications property
        Returns: Optional[List[managed_tenant_api_notification.ManagedTenantApiNotification]]
        """
        return self._managed_tenant_api_notifications
    
    @managed_tenant_api_notifications.setter
    def managed_tenant_api_notifications(self,value: Optional[List[managed_tenant_api_notification.ManagedTenantApiNotification]] = None) -> None:
        """
        Sets the managedTenantApiNotifications property value. The managedTenantApiNotifications property
        Args:
            value: Value to set for the managed_tenant_api_notifications property.
        """
        self._managed_tenant_api_notifications = value
    
    @property
    def managed_tenant_email_notifications(self,) -> Optional[List[managed_tenant_email_notification.ManagedTenantEmailNotification]]:
        """
        Gets the managedTenantEmailNotifications property value. The managedTenantEmailNotifications property
        Returns: Optional[List[managed_tenant_email_notification.ManagedTenantEmailNotification]]
        """
        return self._managed_tenant_email_notifications
    
    @managed_tenant_email_notifications.setter
    def managed_tenant_email_notifications(self,value: Optional[List[managed_tenant_email_notification.ManagedTenantEmailNotification]] = None) -> None:
        """
        Sets the managedTenantEmailNotifications property value. The managedTenantEmailNotifications property
        Args:
            value: Value to set for the managed_tenant_email_notifications property.
        """
        self._managed_tenant_email_notifications = value
    
    @property
    def managed_tenant_ticketing_endpoints(self,) -> Optional[List[managed_tenant_ticketing_endpoint.ManagedTenantTicketingEndpoint]]:
        """
        Gets the managedTenantTicketingEndpoints property value. The managedTenantTicketingEndpoints property
        Returns: Optional[List[managed_tenant_ticketing_endpoint.ManagedTenantTicketingEndpoint]]
        """
        return self._managed_tenant_ticketing_endpoints
    
    @managed_tenant_ticketing_endpoints.setter
    def managed_tenant_ticketing_endpoints(self,value: Optional[List[managed_tenant_ticketing_endpoint.ManagedTenantTicketingEndpoint]] = None) -> None:
        """
        Sets the managedTenantTicketingEndpoints property value. The managedTenantTicketingEndpoints property
        Args:
            value: Value to set for the managed_tenant_ticketing_endpoints property.
        """
        self._managed_tenant_ticketing_endpoints = value
    
    @property
    def management_action_tenant_deployment_statuses(self,) -> Optional[List[management_action_tenant_deployment_status.ManagementActionTenantDeploymentStatus]]:
        """
        Gets the managementActionTenantDeploymentStatuses property value. The tenant level status of management actions across managed tenants.
        Returns: Optional[List[management_action_tenant_deployment_status.ManagementActionTenantDeploymentStatus]]
        """
        return self._management_action_tenant_deployment_statuses
    
    @management_action_tenant_deployment_statuses.setter
    def management_action_tenant_deployment_statuses(self,value: Optional[List[management_action_tenant_deployment_status.ManagementActionTenantDeploymentStatus]] = None) -> None:
        """
        Sets the managementActionTenantDeploymentStatuses property value. The tenant level status of management actions across managed tenants.
        Args:
            value: Value to set for the management_action_tenant_deployment_statuses property.
        """
        self._management_action_tenant_deployment_statuses = value
    
    @property
    def management_actions(self,) -> Optional[List[management_action.ManagementAction]]:
        """
        Gets the managementActions property value. The collection of baseline management actions across managed tenants.
        Returns: Optional[List[management_action.ManagementAction]]
        """
        return self._management_actions
    
    @management_actions.setter
    def management_actions(self,value: Optional[List[management_action.ManagementAction]] = None) -> None:
        """
        Sets the managementActions property value. The collection of baseline management actions across managed tenants.
        Args:
            value: Value to set for the management_actions property.
        """
        self._management_actions = value
    
    @property
    def management_intents(self,) -> Optional[List[management_intent.ManagementIntent]]:
        """
        Gets the managementIntents property value. The collection of baseline management intents across managed tenants.
        Returns: Optional[List[management_intent.ManagementIntent]]
        """
        return self._management_intents
    
    @management_intents.setter
    def management_intents(self,value: Optional[List[management_intent.ManagementIntent]] = None) -> None:
        """
        Sets the managementIntents property value. The collection of baseline management intents across managed tenants.
        Args:
            value: Value to set for the management_intents property.
        """
        self._management_intents = value
    
    @property
    def management_template_collection_tenant_summaries(self,) -> Optional[List[management_template_collection_tenant_summary.ManagementTemplateCollectionTenantSummary]]:
        """
        Gets the managementTemplateCollectionTenantSummaries property value. The managementTemplateCollectionTenantSummaries property
        Returns: Optional[List[management_template_collection_tenant_summary.ManagementTemplateCollectionTenantSummary]]
        """
        return self._management_template_collection_tenant_summaries
    
    @management_template_collection_tenant_summaries.setter
    def management_template_collection_tenant_summaries(self,value: Optional[List[management_template_collection_tenant_summary.ManagementTemplateCollectionTenantSummary]] = None) -> None:
        """
        Sets the managementTemplateCollectionTenantSummaries property value. The managementTemplateCollectionTenantSummaries property
        Args:
            value: Value to set for the management_template_collection_tenant_summaries property.
        """
        self._management_template_collection_tenant_summaries = value
    
    @property
    def management_template_collections(self,) -> Optional[List[management_template_collection.ManagementTemplateCollection]]:
        """
        Gets the managementTemplateCollections property value. The managementTemplateCollections property
        Returns: Optional[List[management_template_collection.ManagementTemplateCollection]]
        """
        return self._management_template_collections
    
    @management_template_collections.setter
    def management_template_collections(self,value: Optional[List[management_template_collection.ManagementTemplateCollection]] = None) -> None:
        """
        Sets the managementTemplateCollections property value. The managementTemplateCollections property
        Args:
            value: Value to set for the management_template_collections property.
        """
        self._management_template_collections = value
    
    @property
    def management_template_step_tenant_summaries(self,) -> Optional[List[management_template_step_tenant_summary.ManagementTemplateStepTenantSummary]]:
        """
        Gets the managementTemplateStepTenantSummaries property value. The managementTemplateStepTenantSummaries property
        Returns: Optional[List[management_template_step_tenant_summary.ManagementTemplateStepTenantSummary]]
        """
        return self._management_template_step_tenant_summaries
    
    @management_template_step_tenant_summaries.setter
    def management_template_step_tenant_summaries(self,value: Optional[List[management_template_step_tenant_summary.ManagementTemplateStepTenantSummary]] = None) -> None:
        """
        Sets the managementTemplateStepTenantSummaries property value. The managementTemplateStepTenantSummaries property
        Args:
            value: Value to set for the management_template_step_tenant_summaries property.
        """
        self._management_template_step_tenant_summaries = value
    
    @property
    def management_template_step_versions(self,) -> Optional[List[management_template_step_version.ManagementTemplateStepVersion]]:
        """
        Gets the managementTemplateStepVersions property value. The managementTemplateStepVersions property
        Returns: Optional[List[management_template_step_version.ManagementTemplateStepVersion]]
        """
        return self._management_template_step_versions
    
    @management_template_step_versions.setter
    def management_template_step_versions(self,value: Optional[List[management_template_step_version.ManagementTemplateStepVersion]] = None) -> None:
        """
        Sets the managementTemplateStepVersions property value. The managementTemplateStepVersions property
        Args:
            value: Value to set for the management_template_step_versions property.
        """
        self._management_template_step_versions = value
    
    @property
    def management_template_steps(self,) -> Optional[List[management_template_step.ManagementTemplateStep]]:
        """
        Gets the managementTemplateSteps property value. The managementTemplateSteps property
        Returns: Optional[List[management_template_step.ManagementTemplateStep]]
        """
        return self._management_template_steps
    
    @management_template_steps.setter
    def management_template_steps(self,value: Optional[List[management_template_step.ManagementTemplateStep]] = None) -> None:
        """
        Sets the managementTemplateSteps property value. The managementTemplateSteps property
        Args:
            value: Value to set for the management_template_steps property.
        """
        self._management_template_steps = value
    
    @property
    def management_templates(self,) -> Optional[List[management_template.ManagementTemplate]]:
        """
        Gets the managementTemplates property value. The collection of baseline management templates across managed tenants.
        Returns: Optional[List[management_template.ManagementTemplate]]
        """
        return self._management_templates
    
    @management_templates.setter
    def management_templates(self,value: Optional[List[management_template.ManagementTemplate]] = None) -> None:
        """
        Sets the managementTemplates property value. The collection of baseline management templates across managed tenants.
        Args:
            value: Value to set for the management_templates property.
        """
        self._management_templates = value
    
    @property
    def my_roles(self,) -> Optional[List[my_role.MyRole]]:
        """
        Gets the myRoles property value. The collection of role assignments to a signed-in user for a managed tenant.
        Returns: Optional[List[my_role.MyRole]]
        """
        return self._my_roles
    
    @my_roles.setter
    def my_roles(self,value: Optional[List[my_role.MyRole]] = None) -> None:
        """
        Sets the myRoles property value. The collection of role assignments to a signed-in user for a managed tenant.
        Args:
            value: Value to set for the my_roles property.
        """
        self._my_roles = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("aggregatedPolicyCompliances", self.aggregated_policy_compliances)
        writer.write_collection_of_object_values("appPerformances", self.app_performances)
        writer.write_collection_of_object_values("auditEvents", self.audit_events)
        writer.write_collection_of_object_values("cloudPcsOverview", self.cloud_pcs_overview)
        writer.write_collection_of_object_values("cloudPcConnections", self.cloud_pc_connections)
        writer.write_collection_of_object_values("cloudPcDevices", self.cloud_pc_devices)
        writer.write_collection_of_object_values("conditionalAccessPolicyCoverages", self.conditional_access_policy_coverages)
        writer.write_collection_of_object_values("credentialUserRegistrationsSummaries", self.credential_user_registrations_summaries)
        writer.write_collection_of_object_values("deviceAppPerformances", self.device_app_performances)
        writer.write_collection_of_object_values("deviceCompliancePolicySettingStateSummaries", self.device_compliance_policy_setting_state_summaries)
        writer.write_collection_of_object_values("deviceHealthStatuses", self.device_health_statuses)
        writer.write_collection_of_object_values("managedDeviceCompliances", self.managed_device_compliances)
        writer.write_collection_of_object_values("managedDeviceComplianceTrends", self.managed_device_compliance_trends)
        writer.write_collection_of_object_values("managedTenantAlerts", self.managed_tenant_alerts)
        writer.write_collection_of_object_values("managedTenantAlertLogs", self.managed_tenant_alert_logs)
        writer.write_collection_of_object_values("managedTenantAlertRules", self.managed_tenant_alert_rules)
        writer.write_collection_of_object_values("managedTenantAlertRuleDefinitions", self.managed_tenant_alert_rule_definitions)
        writer.write_collection_of_object_values("managedTenantApiNotifications", self.managed_tenant_api_notifications)
        writer.write_collection_of_object_values("managedTenantEmailNotifications", self.managed_tenant_email_notifications)
        writer.write_collection_of_object_values("managedTenantTicketingEndpoints", self.managed_tenant_ticketing_endpoints)
        writer.write_collection_of_object_values("managementActions", self.management_actions)
        writer.write_collection_of_object_values("managementActionTenantDeploymentStatuses", self.management_action_tenant_deployment_statuses)
        writer.write_collection_of_object_values("managementIntents", self.management_intents)
        writer.write_collection_of_object_values("managementTemplates", self.management_templates)
        writer.write_collection_of_object_values("managementTemplateCollections", self.management_template_collections)
        writer.write_collection_of_object_values("managementTemplateCollectionTenantSummaries", self.management_template_collection_tenant_summaries)
        writer.write_collection_of_object_values("managementTemplateSteps", self.management_template_steps)
        writer.write_collection_of_object_values("managementTemplateStepTenantSummaries", self.management_template_step_tenant_summaries)
        writer.write_collection_of_object_values("managementTemplateStepVersions", self.management_template_step_versions)
        writer.write_collection_of_object_values("myRoles", self.my_roles)
        writer.write_collection_of_object_values("tenants", self.tenants)
        writer.write_collection_of_object_values("tenantsCustomizedInformation", self.tenants_customized_information)
        writer.write_collection_of_object_values("tenantsDetailedInformation", self.tenants_detailed_information)
        writer.write_collection_of_object_values("tenantGroups", self.tenant_groups)
        writer.write_collection_of_object_values("tenantTags", self.tenant_tags)
        writer.write_collection_of_object_values("windowsDeviceMalwareStates", self.windows_device_malware_states)
        writer.write_collection_of_object_values("windowsProtectionStates", self.windows_protection_states)
    
    @property
    def tenant_groups(self,) -> Optional[List[tenant_group.TenantGroup]]:
        """
        Gets the tenantGroups property value. The collection of a logical grouping of managed tenants used by the multi-tenant management platform.
        Returns: Optional[List[tenant_group.TenantGroup]]
        """
        return self._tenant_groups
    
    @tenant_groups.setter
    def tenant_groups(self,value: Optional[List[tenant_group.TenantGroup]] = None) -> None:
        """
        Sets the tenantGroups property value. The collection of a logical grouping of managed tenants used by the multi-tenant management platform.
        Args:
            value: Value to set for the tenant_groups property.
        """
        self._tenant_groups = value
    
    @property
    def tenant_tags(self,) -> Optional[List[tenant_tag.TenantTag]]:
        """
        Gets the tenantTags property value. The collection of tenant tags across managed tenants.
        Returns: Optional[List[tenant_tag.TenantTag]]
        """
        return self._tenant_tags
    
    @tenant_tags.setter
    def tenant_tags(self,value: Optional[List[tenant_tag.TenantTag]] = None) -> None:
        """
        Sets the tenantTags property value. The collection of tenant tags across managed tenants.
        Args:
            value: Value to set for the tenant_tags property.
        """
        self._tenant_tags = value
    
    @property
    def tenants(self,) -> Optional[List[tenant.Tenant]]:
        """
        Gets the tenants property value. The collection of tenants associated with the managing entity.
        Returns: Optional[List[tenant.Tenant]]
        """
        return self._tenants
    
    @tenants.setter
    def tenants(self,value: Optional[List[tenant.Tenant]] = None) -> None:
        """
        Sets the tenants property value. The collection of tenants associated with the managing entity.
        Args:
            value: Value to set for the tenants property.
        """
        self._tenants = value
    
    @property
    def tenants_customized_information(self,) -> Optional[List[tenant_customized_information.TenantCustomizedInformation]]:
        """
        Gets the tenantsCustomizedInformation property value. The collection of tenant level customized information across managed tenants.
        Returns: Optional[List[tenant_customized_information.TenantCustomizedInformation]]
        """
        return self._tenants_customized_information
    
    @tenants_customized_information.setter
    def tenants_customized_information(self,value: Optional[List[tenant_customized_information.TenantCustomizedInformation]] = None) -> None:
        """
        Sets the tenantsCustomizedInformation property value. The collection of tenant level customized information across managed tenants.
        Args:
            value: Value to set for the tenants_customized_information property.
        """
        self._tenants_customized_information = value
    
    @property
    def tenants_detailed_information(self,) -> Optional[List[tenant_detailed_information.TenantDetailedInformation]]:
        """
        Gets the tenantsDetailedInformation property value. The collection tenant level detailed information across managed tenants.
        Returns: Optional[List[tenant_detailed_information.TenantDetailedInformation]]
        """
        return self._tenants_detailed_information
    
    @tenants_detailed_information.setter
    def tenants_detailed_information(self,value: Optional[List[tenant_detailed_information.TenantDetailedInformation]] = None) -> None:
        """
        Sets the tenantsDetailedInformation property value. The collection tenant level detailed information across managed tenants.
        Args:
            value: Value to set for the tenants_detailed_information property.
        """
        self._tenants_detailed_information = value
    
    @property
    def windows_device_malware_states(self,) -> Optional[List[windows_device_malware_state.WindowsDeviceMalwareState]]:
        """
        Gets the windowsDeviceMalwareStates property value. The state of malware for Windows devices, registered with Microsoft Endpoint Manager, across managed tenants.
        Returns: Optional[List[windows_device_malware_state.WindowsDeviceMalwareState]]
        """
        return self._windows_device_malware_states
    
    @windows_device_malware_states.setter
    def windows_device_malware_states(self,value: Optional[List[windows_device_malware_state.WindowsDeviceMalwareState]] = None) -> None:
        """
        Sets the windowsDeviceMalwareStates property value. The state of malware for Windows devices, registered with Microsoft Endpoint Manager, across managed tenants.
        Args:
            value: Value to set for the windows_device_malware_states property.
        """
        self._windows_device_malware_states = value
    
    @property
    def windows_protection_states(self,) -> Optional[List[windows_protection_state.WindowsProtectionState]]:
        """
        Gets the windowsProtectionStates property value. The protection state for Windows devices, registered with Microsoft Endpoint Manager, across managed tenants.
        Returns: Optional[List[windows_protection_state.WindowsProtectionState]]
        """
        return self._windows_protection_states
    
    @windows_protection_states.setter
    def windows_protection_states(self,value: Optional[List[windows_protection_state.WindowsProtectionState]] = None) -> None:
        """
        Sets the windowsProtectionStates property value. The protection state for Windows devices, registered with Microsoft Endpoint Manager, across managed tenants.
        Args:
            value: Value to set for the windows_protection_states property.
        """
        self._windows_protection_states = value
    

