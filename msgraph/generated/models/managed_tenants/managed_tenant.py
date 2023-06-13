from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import aggregated_policy_compliance, app_performance, audit_event, cloud_pc_connection, cloud_pc_device, cloud_pc_overview, conditional_access_policy_coverage, credential_user_registrations_summary, device_app_performance, device_compliance_policy_setting_state_summary, device_health_status, managed_device_compliance, managed_device_compliance_trend, managed_tenant_alert, managed_tenant_alert_log, managed_tenant_alert_rule, managed_tenant_alert_rule_definition, managed_tenant_api_notification, managed_tenant_email_notification, managed_tenant_ticketing_endpoint, management_action, management_action_tenant_deployment_status, management_intent, management_template, management_template_collection, management_template_collection_tenant_summary, management_template_step, management_template_step_tenant_summary, management_template_step_version, my_role, tenant, tenant_customized_information, tenant_detailed_information, tenant_group, tenant_tag, windows_device_malware_state, windows_protection_state
    from .. import entity

from .. import entity

@dataclass
class ManagedTenant(entity.Entity):
    # Aggregate view of device compliance policies across managed tenants.
    aggregated_policy_compliances: Optional[List[aggregated_policy_compliance.AggregatedPolicyCompliance]] = None
    # The appPerformances property
    app_performances: Optional[List[app_performance.AppPerformance]] = None
    # The collection of audit events across managed tenants.
    audit_events: Optional[List[audit_event.AuditEvent]] = None
    # The collection of cloud PC connections across managed tenants.
    cloud_pc_connections: Optional[List[cloud_pc_connection.CloudPcConnection]] = None
    # The collection of cloud PC devices across managed tenants.
    cloud_pc_devices: Optional[List[cloud_pc_device.CloudPcDevice]] = None
    # Overview of cloud PC information across managed tenants.
    cloud_pcs_overview: Optional[List[cloud_pc_overview.CloudPcOverview]] = None
    # Aggregate view of conditional access policy coverage across managed tenants.
    conditional_access_policy_coverages: Optional[List[conditional_access_policy_coverage.ConditionalAccessPolicyCoverage]] = None
    # Summary information for user registration for multi-factor authentication and self service password reset across managed tenants.
    credential_user_registrations_summaries: Optional[List[credential_user_registrations_summary.CredentialUserRegistrationsSummary]] = None
    # The deviceAppPerformances property
    device_app_performances: Optional[List[device_app_performance.DeviceAppPerformance]] = None
    # Summary information for device compliance policy setting states across managed tenants.
    device_compliance_policy_setting_state_summaries: Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]] = None
    # The deviceHealthStatuses property
    device_health_statuses: Optional[List[device_health_status.DeviceHealthStatus]] = None
    # Trend insights for device compliance across managed tenants.
    managed_device_compliance_trends: Optional[List[managed_device_compliance_trend.ManagedDeviceComplianceTrend]] = None
    # The collection of compliance for managed devices across managed tenants.
    managed_device_compliances: Optional[List[managed_device_compliance.ManagedDeviceCompliance]] = None
    # The managedTenantAlertLogs property
    managed_tenant_alert_logs: Optional[List[managed_tenant_alert_log.ManagedTenantAlertLog]] = None
    # The managedTenantAlertRuleDefinitions property
    managed_tenant_alert_rule_definitions: Optional[List[managed_tenant_alert_rule_definition.ManagedTenantAlertRuleDefinition]] = None
    # The managedTenantAlertRules property
    managed_tenant_alert_rules: Optional[List[managed_tenant_alert_rule.ManagedTenantAlertRule]] = None
    # The managedTenantAlerts property
    managed_tenant_alerts: Optional[List[managed_tenant_alert.ManagedTenantAlert]] = None
    # The managedTenantApiNotifications property
    managed_tenant_api_notifications: Optional[List[managed_tenant_api_notification.ManagedTenantApiNotification]] = None
    # The managedTenantEmailNotifications property
    managed_tenant_email_notifications: Optional[List[managed_tenant_email_notification.ManagedTenantEmailNotification]] = None
    # The managedTenantTicketingEndpoints property
    managed_tenant_ticketing_endpoints: Optional[List[managed_tenant_ticketing_endpoint.ManagedTenantTicketingEndpoint]] = None
    # The tenant level status of management actions across managed tenants.
    management_action_tenant_deployment_statuses: Optional[List[management_action_tenant_deployment_status.ManagementActionTenantDeploymentStatus]] = None
    # The collection of baseline management actions across managed tenants.
    management_actions: Optional[List[management_action.ManagementAction]] = None
    # The collection of baseline management intents across managed tenants.
    management_intents: Optional[List[management_intent.ManagementIntent]] = None
    # The managementTemplateCollectionTenantSummaries property
    management_template_collection_tenant_summaries: Optional[List[management_template_collection_tenant_summary.ManagementTemplateCollectionTenantSummary]] = None
    # The managementTemplateCollections property
    management_template_collections: Optional[List[management_template_collection.ManagementTemplateCollection]] = None
    # The managementTemplateStepTenantSummaries property
    management_template_step_tenant_summaries: Optional[List[management_template_step_tenant_summary.ManagementTemplateStepTenantSummary]] = None
    # The managementTemplateStepVersions property
    management_template_step_versions: Optional[List[management_template_step_version.ManagementTemplateStepVersion]] = None
    # The managementTemplateSteps property
    management_template_steps: Optional[List[management_template_step.ManagementTemplateStep]] = None
    # The collection of baseline management templates across managed tenants.
    management_templates: Optional[List[management_template.ManagementTemplate]] = None
    # The collection of role assignments to a signed-in user for a managed tenant.
    my_roles: Optional[List[my_role.MyRole]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of a logical grouping of managed tenants used by the multi-tenant management platform.
    tenant_groups: Optional[List[tenant_group.TenantGroup]] = None
    # The collection of tenant tags across managed tenants.
    tenant_tags: Optional[List[tenant_tag.TenantTag]] = None
    # The collection of tenants associated with the managing entity.
    tenants: Optional[List[tenant.Tenant]] = None
    # The collection of tenant level customized information across managed tenants.
    tenants_customized_information: Optional[List[tenant_customized_information.TenantCustomizedInformation]] = None
    # The collection tenant level detailed information across managed tenants.
    tenants_detailed_information: Optional[List[tenant_detailed_information.TenantDetailedInformation]] = None
    # The state of malware for Windows devices, registered with Microsoft Endpoint Manager, across managed tenants.
    windows_device_malware_states: Optional[List[windows_device_malware_state.WindowsDeviceMalwareState]] = None
    # The protection state for Windows devices, registered with Microsoft Endpoint Manager, across managed tenants.
    windows_protection_states: Optional[List[windows_protection_state.WindowsProtectionState]] = None
    
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
    

