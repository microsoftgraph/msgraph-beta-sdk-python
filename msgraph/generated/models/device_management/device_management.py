from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import monitoring
    from .. import admin_consent, advanced_threat_protection_onboarding_state_summary, android_device_owner_enrollment_profile, android_for_work_app_configuration_schema, android_for_work_enrollment_profile, android_for_work_settings, android_managed_store_account_enterprise_settings, android_managed_store_app_configuration_schema, apple_push_notification_certificate, apple_user_initiated_enrollment_profile, audit_event, cart_to_class_association, certificate_connector_details, chrome_o_s_onboarding_settings, cloud_p_c_connectivity_issue, comanagement_eligible_device, compliance_management_partner, config_manager_collection, connector_status_details, data_processor_service_for_windows_features_onboarding, data_sharing_consent, dep_onboarding_setting, detected_app, device_and_app_management_assignment_filter, device_and_app_management_role_assignment, device_category, device_compliance_policy, device_compliance_policy_device_state_summary, device_compliance_policy_setting_state_summary, device_compliance_script, device_configuration, device_configuration_conflict_summary, device_configuration_device_state_summary, device_configuration_user_state_summary, device_custom_attribute_shell_script, device_enrollment_configuration, device_health_script, device_management_autopilot_event, device_management_compliance_policy, device_management_configuration_category, device_management_configuration_policy, device_management_configuration_policy_template, device_management_configuration_setting_definition, device_management_configuration_setting_template, device_management_derived_credential_settings, device_management_domain_join_connector, device_management_exchange_connector, device_management_exchange_on_premises_policy, device_management_intent, device_management_partner, device_management_reports, device_management_resource_access_profile_base, device_management_reusable_policy_setting, device_management_script, device_management_settings, device_management_setting_category, device_management_setting_definition, device_management_subscriptions, device_management_subscription_state, device_management_template, device_management_template_insights_definition, device_management_troubleshooting_event, device_protection_overview, device_shell_script, embedded_s_i_m_activation_code_pool, entity, group_policy_category, group_policy_configuration, group_policy_definition, group_policy_definition_file, group_policy_migration_report, group_policy_object_file, group_policy_uploaded_definition_file, imported_device_identity, imported_windows_autopilot_device_identity, intune_brand, intune_branding_profile, ios_update_device_status, mac_o_s_software_update_account_summary, managed_all_device_certificate_state, managed_device, managed_device_cleanup_settings, managed_device_encryption_state, managed_device_overview, microsoft_tunnel_configuration, microsoft_tunnel_health_threshold, microsoft_tunnel_server_log_collection_response, microsoft_tunnel_site, mobile_app_troubleshooting_event, mobile_threat_defense_connector, ndes_connector, notification_message_template, on_premises_conditional_access_settings, privilege_management_elevation, remote_action_audit, remote_assistance_partner, remote_assistance_settings, resource_operation, restricted_apps_violation, role_definition, role_scope_tag, service_now_connection, software_update_status_summary, telecom_expense_management_partner, tenant_attach_r_b_a_c, terms_and_conditions, user_experience_analytics_anomaly, user_experience_analytics_anomaly_correlation_group_overview, user_experience_analytics_anomaly_device, user_experience_analytics_anomaly_severity_overview, user_experience_analytics_app_health_application_performance, user_experience_analytics_app_health_app_performance_by_app_version, user_experience_analytics_app_health_app_performance_by_app_version_details, user_experience_analytics_app_health_app_performance_by_app_version_device_id, user_experience_analytics_app_health_app_performance_by_o_s_version, user_experience_analytics_app_health_device_model_performance, user_experience_analytics_app_health_device_performance, user_experience_analytics_app_health_device_performance_details, user_experience_analytics_app_health_o_s_version_performance, user_experience_analytics_baseline, user_experience_analytics_battery_health_app_impact, user_experience_analytics_battery_health_capacity_details, user_experience_analytics_battery_health_device_app_impact, user_experience_analytics_battery_health_device_performance, user_experience_analytics_battery_health_device_runtime_history, user_experience_analytics_battery_health_model_performance, user_experience_analytics_battery_health_os_performance, user_experience_analytics_battery_health_runtime_details, user_experience_analytics_category, user_experience_analytics_device_performance, user_experience_analytics_device_scope, user_experience_analytics_device_scores, user_experience_analytics_device_startup_history, user_experience_analytics_device_startup_process, user_experience_analytics_device_startup_process_performance, user_experience_analytics_device_timeline_event, user_experience_analytics_device_without_cloud_identity, user_experience_analytics_impacting_process, user_experience_analytics_metric_history, user_experience_analytics_model_scores, user_experience_analytics_not_autopilot_ready_device, user_experience_analytics_overview, user_experience_analytics_remote_connection, user_experience_analytics_resource_performance, user_experience_analytics_score_history, user_experience_analytics_settings, user_experience_analytics_work_from_anywhere_hardware_readiness_metric, user_experience_analytics_work_from_anywhere_metric, user_experience_analytics_work_from_anywhere_model_performance, user_p_f_x_certificate, virtual_endpoint, windows_autopilot_deployment_profile, windows_autopilot_device_identity, windows_autopilot_settings, windows_driver_update_profile, windows_feature_update_profile, windows_information_protection_app_learning_summary, windows_information_protection_network_learning_summary, windows_malware_information, windows_malware_overview, windows_quality_update_profile, windows_update_catalog_item, zebra_fota_artifact, zebra_fota_connector, zebra_fota_deployment

from .. import entity

@dataclass
class DeviceManagement(entity.Entity):
    # The date & time when tenant data moved between scaleunits.
    account_move_completion_date_time: Optional[datetime] = None
    # Admin consent information.
    admin_consent: Optional[admin_consent.AdminConsent] = None
    # The summary state of ATP onboarding state for this account.
    advanced_threat_protection_onboarding_state_summary: Optional[advanced_threat_protection_onboarding_state_summary.AdvancedThreatProtectionOnboardingStateSummary] = None
    # Android device owner enrollment profile entities.
    android_device_owner_enrollment_profiles: Optional[List[android_device_owner_enrollment_profile.AndroidDeviceOwnerEnrollmentProfile]] = None
    # Android for Work app configuration schema entities.
    android_for_work_app_configuration_schemas: Optional[List[android_for_work_app_configuration_schema.AndroidForWorkAppConfigurationSchema]] = None
    # Android for Work enrollment profile entities.
    android_for_work_enrollment_profiles: Optional[List[android_for_work_enrollment_profile.AndroidForWorkEnrollmentProfile]] = None
    # The singleton Android for Work settings entity.
    android_for_work_settings: Optional[android_for_work_settings.AndroidForWorkSettings] = None
    # The singleton Android managed store account enterprise settings entity.
    android_managed_store_account_enterprise_settings: Optional[android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings] = None
    # Android Enterprise app configuration schema entities.
    android_managed_store_app_configuration_schemas: Optional[List[android_managed_store_app_configuration_schema.AndroidManagedStoreAppConfigurationSchema]] = None
    # Apple push notification certificate.
    apple_push_notification_certificate: Optional[apple_push_notification_certificate.ApplePushNotificationCertificate] = None
    # Apple user initiated enrollment profiles
    apple_user_initiated_enrollment_profiles: Optional[List[apple_user_initiated_enrollment_profile.AppleUserInitiatedEnrollmentProfile]] = None
    # The list of assignment filters
    assignment_filters: Optional[List[device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter]] = None
    # The Audit Events
    audit_events: Optional[List[audit_event.AuditEvent]] = None
    # The list of autopilot events for the tenant.
    autopilot_events: Optional[List[device_management_autopilot_event.DeviceManagementAutopilotEvent]] = None
    # The Cart To Class Associations.
    cart_to_class_associations: Optional[List[cart_to_class_association.CartToClassAssociation]] = None
    # The available categories
    categories: Optional[List[device_management_setting_category.DeviceManagementSettingCategory]] = None
    # Collection of certificate connector details, each associated with a corresponding Intune Certificate Connector.
    certificate_connector_details: Optional[List[certificate_connector_details.CertificateConnectorDetails]] = None
    # Collection of ChromeOSOnboardingSettings settings associated with account.
    chrome_o_s_onboarding_settings: Optional[List[chrome_o_s_onboarding_settings.ChromeOSOnboardingSettings]] = None
    # The list of CloudPC Connectivity Issue.
    cloud_p_c_connectivity_issues: Optional[List[cloud_p_c_connectivity_issue.CloudPCConnectivityIssue]] = None
    # The list of co-managed devices report
    comanaged_devices: Optional[List[managed_device.ManagedDevice]] = None
    # The list of co-management eligible devices report
    comanagement_eligible_devices: Optional[List[comanagement_eligible_device.ComanagementEligibleDevice]] = None
    # List of all compliance categories
    compliance_categories: Optional[List[device_management_configuration_category.DeviceManagementConfigurationCategory]] = None
    # The list of Compliance Management Partners configured by the tenant.
    compliance_management_partners: Optional[List[compliance_management_partner.ComplianceManagementPartner]] = None
    # List of all compliance policies
    compliance_policies: Optional[List[device_management_compliance_policy.DeviceManagementCompliancePolicy]] = None
    # List of all ComplianceSettings
    compliance_settings: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None
    # The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
    conditional_access_settings: Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings] = None
    # A list of ConfigManagerCollection
    config_manager_collections: Optional[List[config_manager_collection.ConfigManagerCollection]] = None
    # List of all Configuration Categories
    configuration_categories: Optional[List[device_management_configuration_category.DeviceManagementConfigurationCategory]] = None
    # List of all Configuration policies
    configuration_policies: Optional[List[device_management_configuration_policy.DeviceManagementConfigurationPolicy]] = None
    # List of all templates
    configuration_policy_templates: Optional[List[device_management_configuration_policy_template.DeviceManagementConfigurationPolicyTemplate]] = None
    # List of all ConfigurationSettings
    configuration_settings: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None
    # The list of connector status for the tenant.
    connector_status: Optional[List[connector_status_details.ConnectorStatusDetails]] = None
    # A configuration entity for MEM features that utilize Data Processor Service for Windows (DPSW) data.
    data_processor_service_for_windows_features_onboarding: Optional[data_processor_service_for_windows_features_onboarding.DataProcessorServiceForWindowsFeaturesOnboarding] = None
    # Data sharing consents.
    data_sharing_consents: Optional[List[data_sharing_consent.DataSharingConsent]] = None
    # This collections of multiple DEP tokens per-tenant.
    dep_onboarding_settings: Optional[List[dep_onboarding_setting.DepOnboardingSetting]] = None
    # Collection of Derived credential settings associated with account.
    derived_credentials: Optional[List[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]] = None
    # The list of detected apps associated with a device.
    detected_apps: Optional[List[detected_app.DetectedApp]] = None
    # The list of device categories with the tenant.
    device_categories: Optional[List[device_category.DeviceCategory]] = None
    # The device compliance policies.
    device_compliance_policies: Optional[List[device_compliance_policy.DeviceCompliancePolicy]] = None
    # The device compliance state summary for this account.
    device_compliance_policy_device_state_summary: Optional[device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary] = None
    # The summary states of compliance policy settings for this account.
    device_compliance_policy_setting_state_summaries: Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]] = None
    # The last requested time of device compliance reporting for this account. This property is read-only.
    device_compliance_report_summarization_date_time: Optional[datetime] = None
    # The list of device compliance scripts associated with the tenant.
    device_compliance_scripts: Optional[List[device_compliance_script.DeviceComplianceScript]] = None
    # Summary of policies in conflict state for this account.
    device_configuration_conflict_summary: Optional[List[device_configuration_conflict_summary.DeviceConfigurationConflictSummary]] = None
    # The device configuration device state summary for this account.
    device_configuration_device_state_summaries: Optional[device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary] = None
    # Restricted apps violations for this account.
    device_configuration_restricted_apps_violations: Optional[List[restricted_apps_violation.RestrictedAppsViolation]] = None
    # The device configuration user state summary for this account.
    device_configuration_user_state_summaries: Optional[device_configuration_user_state_summary.DeviceConfigurationUserStateSummary] = None
    # The device configurations.
    device_configurations: Optional[List[device_configuration.DeviceConfiguration]] = None
    # Summary of all certificates for all devices.
    device_configurations_all_managed_device_certificate_states: Optional[List[managed_all_device_certificate_state.ManagedAllDeviceCertificateState]] = None
    # The list of device custom attribute shell scripts associated with the tenant.
    device_custom_attribute_shell_scripts: Optional[List[device_custom_attribute_shell_script.DeviceCustomAttributeShellScript]] = None
    # The list of device enrollment configurations
    device_enrollment_configurations: Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]] = None
    # The list of device health scripts associated with the tenant.
    device_health_scripts: Optional[List[device_health_script.DeviceHealthScript]] = None
    # The list of Device Management Partners configured by the tenant.
    device_management_partners: Optional[List[device_management_partner.DeviceManagementPartner]] = None
    # The list of device management scripts associated with the tenant.
    device_management_scripts: Optional[List[device_management_script.DeviceManagementScript]] = None
    # Device protection overview.
    device_protection_overview: Optional[device_protection_overview.DeviceProtectionOverview] = None
    # The list of device shell scripts associated with the tenant.
    device_shell_scripts: Optional[List[device_shell_script.DeviceShellScript]] = None
    # A list of connector objects.
    domain_join_connectors: Optional[List[device_management_domain_join_connector.DeviceManagementDomainJoinConnector]] = None
    # The embedded SIM activation code pools created by this account.
    embedded_s_i_m_activation_code_pools: Optional[List[embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool]] = None
    # The list of Exchange Connectors configured by the tenant.
    exchange_connectors: Optional[List[device_management_exchange_connector.DeviceManagementExchangeConnector]] = None
    # The list of Exchange On Premisis policies configured by the tenant.
    exchange_on_premises_policies: Optional[List[device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy]] = None
    # The policy which controls mobile device access to Exchange On Premises
    exchange_on_premises_policy: Optional[device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy] = None
    # The available group policy categories for this account.
    group_policy_categories: Optional[List[group_policy_category.GroupPolicyCategory]] = None
    # The group policy configurations created by this account.
    group_policy_configurations: Optional[List[group_policy_configuration.GroupPolicyConfiguration]] = None
    # The available group policy definition files for this account.
    group_policy_definition_files: Optional[List[group_policy_definition_file.GroupPolicyDefinitionFile]] = None
    # The available group policy definitions for this account.
    group_policy_definitions: Optional[List[group_policy_definition.GroupPolicyDefinition]] = None
    # A list of Group Policy migration reports.
    group_policy_migration_reports: Optional[List[group_policy_migration_report.GroupPolicyMigrationReport]] = None
    # A list of Group Policy Object files uploaded.
    group_policy_object_files: Optional[List[group_policy_object_file.GroupPolicyObjectFile]] = None
    # The available group policy uploaded definition files for this account.
    group_policy_uploaded_definition_files: Optional[List[group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile]] = None
    # The imported device identities.
    imported_device_identities: Optional[List[imported_device_identity.ImportedDeviceIdentity]] = None
    # Collection of imported Windows autopilot devices.
    imported_windows_autopilot_device_identities: Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]] = None
    # The device management intents
    intents: Optional[List[device_management_intent.DeviceManagementIntent]] = None
    # Intune Account ID for given tenant
    intune_account_id: Optional[UUID] = None
    # intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
    intune_brand: Optional[intune_brand.IntuneBrand] = None
    # Intune branding profiles targeted to AAD groups
    intune_branding_profiles: Optional[List[intune_branding_profile.IntuneBrandingProfile]] = None
    # The IOS software update installation statuses for this account.
    ios_update_statuses: Optional[List[ios_update_device_status.IosUpdateDeviceStatus]] = None
    # The last modified time of reporting for this account. This property is read-only.
    last_report_aggregation_date_time: Optional[datetime] = None
    # The property to enable Non-MDM managed legacy PC management for this account. This property is read-only.
    legacy_pc_manangement_enabled: Optional[bool] = None
    # The MacOS software update account summaries for this account.
    mac_o_s_software_update_account_summaries: Optional[List[mac_o_s_software_update_account_summary.MacOSSoftwareUpdateAccountSummary]] = None
    # Device cleanup rule
    managed_device_cleanup_settings: Optional[managed_device_cleanup_settings.ManagedDeviceCleanupSettings] = None
    # Encryption report for devices in this account
    managed_device_encryption_states: Optional[List[managed_device_encryption_state.ManagedDeviceEncryptionState]] = None
    # Device overview
    managed_device_overview: Optional[managed_device_overview.ManagedDeviceOverview] = None
    # The list of managed devices.
    managed_devices: Optional[List[managed_device.ManagedDevice]] = None
    # Maximum number of DEP tokens allowed per-tenant.
    maximum_dep_tokens: Optional[int] = None
    # Collection of MicrosoftTunnelConfiguration settings associated with account.
    microsoft_tunnel_configurations: Optional[List[microsoft_tunnel_configuration.MicrosoftTunnelConfiguration]] = None
    # Collection of MicrosoftTunnelHealthThreshold settings associated with account.
    microsoft_tunnel_health_thresholds: Optional[List[microsoft_tunnel_health_threshold.MicrosoftTunnelHealthThreshold]] = None
    # Collection of MicrosoftTunnelServerLogCollectionResponse settings associated with account.
    microsoft_tunnel_server_log_collection_responses: Optional[List[microsoft_tunnel_server_log_collection_response.MicrosoftTunnelServerLogCollectionResponse]] = None
    # Collection of MicrosoftTunnelSite settings associated with account.
    microsoft_tunnel_sites: Optional[List[microsoft_tunnel_site.MicrosoftTunnelSite]] = None
    # The collection property of MobileAppTroubleshootingEvent.
    mobile_app_troubleshooting_events: Optional[List[mobile_app_troubleshooting_event.MobileAppTroubleshootingEvent]] = None
    # The list of Mobile threat Defense connectors configured by the tenant.
    mobile_threat_defense_connectors: Optional[List[mobile_threat_defense_connector.MobileThreatDefenseConnector]] = None
    # The monitoring property
    monitoring: Optional[monitoring.Monitoring] = None
    # The collection of Ndes connectors for this account.
    ndes_connectors: Optional[List[ndes_connector.NdesConnector]] = None
    # The Notification Message Templates.
    notification_message_templates: Optional[List[notification_message_template.NotificationMessageTemplate]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The endpoint privilege management elevation event entity contains elevation details.
    privilege_management_elevations: Optional[List[privilege_management_elevation.PrivilegeManagementElevation]] = None
    # The list of device remote action audits with the tenant.
    remote_action_audits: Optional[List[remote_action_audit.RemoteActionAudit]] = None
    # The remote assist partners.
    remote_assistance_partners: Optional[List[remote_assistance_partner.RemoteAssistancePartner]] = None
    # The remote assistance settings singleton
    remote_assistance_settings: Optional[remote_assistance_settings.RemoteAssistanceSettings] = None
    # Reports singleton
    reports: Optional[device_management_reports.DeviceManagementReports] = None
    # Collection of resource access settings associated with account.
    resource_access_profiles: Optional[List[device_management_resource_access_profile_base.DeviceManagementResourceAccessProfileBase]] = None
    # The Resource Operations.
    resource_operations: Optional[List[resource_operation.ResourceOperation]] = None
    # List of all reusable settings that can be referred in a policy
    reusable_policy_settings: Optional[List[device_management_reusable_policy_setting.DeviceManagementReusablePolicySetting]] = None
    # List of all reusable settings
    reusable_settings: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None
    # The Role Assignments.
    role_assignments: Optional[List[device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment]] = None
    # The Role Definitions.
    role_definitions: Optional[List[role_definition.RoleDefinition]] = None
    # The Role Scope Tags.
    role_scope_tags: Optional[List[role_scope_tag.RoleScopeTag]] = None
    # A list of ServiceNowConnections
    service_now_connections: Optional[List[service_now_connection.ServiceNowConnection]] = None
    # The device management intent setting definitions
    setting_definitions: Optional[List[device_management_setting_definition.DeviceManagementSettingDefinition]] = None
    # Account level settings.
    settings: Optional[device_management_settings.DeviceManagementSettings] = None
    # The software update status summary.
    software_update_status_summary: Optional[software_update_status_summary.SoftwareUpdateStatusSummary] = None
    # Tenant mobile device management subscription state.
    subscription_state: Optional[device_management_subscription_state.DeviceManagementSubscriptionState] = None
    # Tenant mobile device management subscriptions.
    subscriptions: Optional[device_management_subscriptions.DeviceManagementSubscriptions] = None
    # The telecom expense management partners.
    telecom_expense_management_partners: Optional[List[telecom_expense_management_partner.TelecomExpenseManagementPartner]] = None
    # List of setting insights in a template
    template_insights: Optional[List[device_management_template_insights_definition.DeviceManagementTemplateInsightsDefinition]] = None
    # List of all TemplateSettings
    template_settings: Optional[List[device_management_configuration_setting_template.DeviceManagementConfigurationSettingTemplate]] = None
    # The available templates
    templates: Optional[List[device_management_template.DeviceManagementTemplate]] = None
    # TenantAttach RBAC Enablement
    tenant_attach_r_b_a_c: Optional[tenant_attach_r_b_a_c.TenantAttachRBAC] = None
    # The terms and conditions associated with device management of the company.
    terms_and_conditions: Optional[List[terms_and_conditions.TermsAndConditions]] = None
    # The list of troubleshooting events for the tenant.
    troubleshooting_events: Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]] = None
    # When enabled, users assigned as administrators via Role Assignment Memberships do not require an assigned Intune license. Prior to this, only Intune licensed users were granted permissions with an Intune role unless they were assigned a role via Azure Active Directory. You are limited to 350 unlicensed direct members for each AAD security group in a role assignment, but you can assign multiple AAD security groups to a role if you need to support more than 350 unlicensed administrators. Licensed administrators are unaffected, do not have to be direct members, nor does the 350 member limit apply. This property is read-only.
    unlicensed_adminstrators_enabled: Optional[bool] = None
    # The user experience analytics anomaly entity contains anomaly details.
    user_experience_analytics_anomaly: Optional[List[user_experience_analytics_anomaly.UserExperienceAnalyticsAnomaly]] = None
    # The user experience analytics anomaly correlation group overview entity contains the information for each correlation group of an anomaly.
    user_experience_analytics_anomaly_correlation_group_overview: Optional[List[user_experience_analytics_anomaly_correlation_group_overview.UserExperienceAnalyticsAnomalyCorrelationGroupOverview]] = None
    # The user experience analytics anomaly entity contains device details.
    user_experience_analytics_anomaly_device: Optional[List[user_experience_analytics_anomaly_device.UserExperienceAnalyticsAnomalyDevice]] = None
    # The user experience analytics anomaly severity overview entity contains the count information for each severity of anomaly.
    user_experience_analytics_anomaly_severity_overview: Optional[user_experience_analytics_anomaly_severity_overview.UserExperienceAnalyticsAnomalySeverityOverview] = None
    # User experience analytics appHealth Application Performance
    user_experience_analytics_app_health_application_performance: Optional[List[user_experience_analytics_app_health_application_performance.UserExperienceAnalyticsAppHealthApplicationPerformance]] = None
    # User experience analytics appHealth Application Performance by App Version
    user_experience_analytics_app_health_application_performance_by_app_version: Optional[List[user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion]] = None
    # User experience analytics appHealth Application Performance by App Version details
    user_experience_analytics_app_health_application_performance_by_app_version_details: Optional[List[user_experience_analytics_app_health_app_performance_by_app_version_details.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails]] = None
    # User experience analytics appHealth Application Performance by App Version Device Id
    user_experience_analytics_app_health_application_performance_by_app_version_device_id: Optional[List[user_experience_analytics_app_health_app_performance_by_app_version_device_id.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId]] = None
    # User experience analytics appHealth Application Performance by OS Version
    user_experience_analytics_app_health_application_performance_by_o_s_version: Optional[List[user_experience_analytics_app_health_app_performance_by_o_s_version.UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion]] = None
    # User experience analytics appHealth Model Performance
    user_experience_analytics_app_health_device_model_performance: Optional[List[user_experience_analytics_app_health_device_model_performance.UserExperienceAnalyticsAppHealthDeviceModelPerformance]] = None
    # User experience analytics appHealth Device Performance
    user_experience_analytics_app_health_device_performance: Optional[List[user_experience_analytics_app_health_device_performance.UserExperienceAnalyticsAppHealthDevicePerformance]] = None
    # User experience analytics device performance details
    user_experience_analytics_app_health_device_performance_details: Optional[List[user_experience_analytics_app_health_device_performance_details.UserExperienceAnalyticsAppHealthDevicePerformanceDetails]] = None
    # User experience analytics appHealth OS version Performance
    user_experience_analytics_app_health_o_s_version_performance: Optional[List[user_experience_analytics_app_health_o_s_version_performance.UserExperienceAnalyticsAppHealthOSVersionPerformance]] = None
    # User experience analytics appHealth overview
    user_experience_analytics_app_health_overview: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
    # User experience analytics baselines
    user_experience_analytics_baselines: Optional[List[user_experience_analytics_baseline.UserExperienceAnalyticsBaseline]] = None
    # User Experience Analytics Battery Health App Impact
    user_experience_analytics_battery_health_app_impact: Optional[List[user_experience_analytics_battery_health_app_impact.UserExperienceAnalyticsBatteryHealthAppImpact]] = None
    # User Experience Analytics Battery Health Capacity Details
    user_experience_analytics_battery_health_capacity_details: Optional[user_experience_analytics_battery_health_capacity_details.UserExperienceAnalyticsBatteryHealthCapacityDetails] = None
    # User Experience Analytics Battery Health Device App Impact
    user_experience_analytics_battery_health_device_app_impact: Optional[List[user_experience_analytics_battery_health_device_app_impact.UserExperienceAnalyticsBatteryHealthDeviceAppImpact]] = None
    # User Experience Analytics Battery Health Device Performance
    user_experience_analytics_battery_health_device_performance: Optional[List[user_experience_analytics_battery_health_device_performance.UserExperienceAnalyticsBatteryHealthDevicePerformance]] = None
    # User Experience Analytics Battery Health Device Runtime History
    user_experience_analytics_battery_health_device_runtime_history: Optional[List[user_experience_analytics_battery_health_device_runtime_history.UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory]] = None
    # User Experience Analytics Battery Health Model Performance
    user_experience_analytics_battery_health_model_performance: Optional[List[user_experience_analytics_battery_health_model_performance.UserExperienceAnalyticsBatteryHealthModelPerformance]] = None
    # User Experience Analytics Battery Health Os Performance
    user_experience_analytics_battery_health_os_performance: Optional[List[user_experience_analytics_battery_health_os_performance.UserExperienceAnalyticsBatteryHealthOsPerformance]] = None
    # User Experience Analytics Battery Health Runtime Details
    user_experience_analytics_battery_health_runtime_details: Optional[user_experience_analytics_battery_health_runtime_details.UserExperienceAnalyticsBatteryHealthRuntimeDetails] = None
    # User experience analytics categories
    user_experience_analytics_categories: Optional[List[user_experience_analytics_category.UserExperienceAnalyticsCategory]] = None
    # User experience analytics device metric history
    user_experience_analytics_device_metric_history: Optional[List[user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory]] = None
    # User experience analytics device performance
    user_experience_analytics_device_performance: Optional[List[user_experience_analytics_device_performance.UserExperienceAnalyticsDevicePerformance]] = None
    # The user experience analytics device scope entity endpoint to trigger on the service to either START or STOP computing metrics data based on a device scope configuration.
    user_experience_analytics_device_scope: Optional[user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope] = None
    # The user experience analytics device scope entity contains device scope configuration use to apply filtering on the endpoint analytics reports.
    user_experience_analytics_device_scopes: Optional[List[user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope]] = None
    # User experience analytics device scores
    user_experience_analytics_device_scores: Optional[List[user_experience_analytics_device_scores.UserExperienceAnalyticsDeviceScores]] = None
    # User experience analytics device Startup History
    user_experience_analytics_device_startup_history: Optional[List[user_experience_analytics_device_startup_history.UserExperienceAnalyticsDeviceStartupHistory]] = None
    # User experience analytics device Startup Process Performance
    user_experience_analytics_device_startup_process_performance: Optional[List[user_experience_analytics_device_startup_process_performance.UserExperienceAnalyticsDeviceStartupProcessPerformance]] = None
    # User experience analytics device Startup Processes
    user_experience_analytics_device_startup_processes: Optional[List[user_experience_analytics_device_startup_process.UserExperienceAnalyticsDeviceStartupProcess]] = None
    # The user experience analytics device events entity contains NRT device timeline event details.
    user_experience_analytics_device_timeline_event: Optional[List[user_experience_analytics_device_timeline_event.UserExperienceAnalyticsDeviceTimelineEvent]] = None
    # User experience analytics devices without cloud identity.
    user_experience_analytics_devices_without_cloud_identity: Optional[List[user_experience_analytics_device_without_cloud_identity.UserExperienceAnalyticsDeviceWithoutCloudIdentity]] = None
    # User experience analytics impacting process
    user_experience_analytics_impacting_process: Optional[List[user_experience_analytics_impacting_process.UserExperienceAnalyticsImpactingProcess]] = None
    # User experience analytics metric history
    user_experience_analytics_metric_history: Optional[List[user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory]] = None
    # User experience analytics model scores
    user_experience_analytics_model_scores: Optional[List[user_experience_analytics_model_scores.UserExperienceAnalyticsModelScores]] = None
    # User experience analytics devices not Windows Autopilot ready.
    user_experience_analytics_not_autopilot_ready_device: Optional[List[user_experience_analytics_not_autopilot_ready_device.UserExperienceAnalyticsNotAutopilotReadyDevice]] = None
    # User experience analytics overview
    user_experience_analytics_overview: Optional[user_experience_analytics_overview.UserExperienceAnalyticsOverview] = None
    # User experience analytics remote connection
    user_experience_analytics_remote_connection: Optional[List[user_experience_analytics_remote_connection.UserExperienceAnalyticsRemoteConnection]] = None
    # User experience analytics resource performance
    user_experience_analytics_resource_performance: Optional[List[user_experience_analytics_resource_performance.UserExperienceAnalyticsResourcePerformance]] = None
    # User experience analytics device Startup Score History
    user_experience_analytics_score_history: Optional[List[user_experience_analytics_score_history.UserExperienceAnalyticsScoreHistory]] = None
    # User experience analytics device settings
    user_experience_analytics_settings: Optional[user_experience_analytics_settings.UserExperienceAnalyticsSettings] = None
    # User experience analytics work from anywhere hardware readiness metrics.
    user_experience_analytics_work_from_anywhere_hardware_readiness_metric: Optional[user_experience_analytics_work_from_anywhere_hardware_readiness_metric.UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric] = None
    # User experience analytics work from anywhere metrics.
    user_experience_analytics_work_from_anywhere_metrics: Optional[List[user_experience_analytics_work_from_anywhere_metric.UserExperienceAnalyticsWorkFromAnywhereMetric]] = None
    # The user experience analytics work from anywhere model performance
    user_experience_analytics_work_from_anywhere_model_performance: Optional[List[user_experience_analytics_work_from_anywhere_model_performance.UserExperienceAnalyticsWorkFromAnywhereModelPerformance]] = None
    # Collection of PFX certificates associated with a user.
    user_pfx_certificates: Optional[List[user_p_f_x_certificate.UserPFXCertificate]] = None
    # The virtualEndpoint property
    virtual_endpoint: Optional[virtual_endpoint.VirtualEndpoint] = None
    # Windows auto pilot deployment profiles
    windows_autopilot_deployment_profiles: Optional[List[windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile]] = None
    # The Windows autopilot device identities contained collection.
    windows_autopilot_device_identities: Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]] = None
    # The Windows autopilot account settings.
    windows_autopilot_settings: Optional[windows_autopilot_settings.WindowsAutopilotSettings] = None
    # A collection of windows driver update profiles
    windows_driver_update_profiles: Optional[List[windows_driver_update_profile.WindowsDriverUpdateProfile]] = None
    # A collection of windows feature update profiles
    windows_feature_update_profiles: Optional[List[windows_feature_update_profile.WindowsFeatureUpdateProfile]] = None
    # The windows information protection app learning summaries.
    windows_information_protection_app_learning_summaries: Optional[List[windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary]] = None
    # The windows information protection network learning summaries.
    windows_information_protection_network_learning_summaries: Optional[List[windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary]] = None
    # The list of affected malware in the tenant.
    windows_malware_information: Optional[List[windows_malware_information.WindowsMalwareInformation]] = None
    # Malware overview for windows devices.
    windows_malware_overview: Optional[windows_malware_overview.WindowsMalwareOverview] = None
    # A collection of windows quality update profiles
    windows_quality_update_profiles: Optional[List[windows_quality_update_profile.WindowsQualityUpdateProfile]] = None
    # A collection of windows update catalog items (fetaure updates item , quality updates item)
    windows_update_catalog_items: Optional[List[windows_update_catalog_item.WindowsUpdateCatalogItem]] = None
    # The Collection of ZebraFotaArtifacts.
    zebra_fota_artifacts: Optional[List[zebra_fota_artifact.ZebraFotaArtifact]] = None
    # The singleton ZebraFotaConnector associated with account.
    zebra_fota_connector: Optional[zebra_fota_connector.ZebraFotaConnector] = None
    # Collection of ZebraFotaDeployments associated with account.
    zebra_fota_deployments: Optional[List[zebra_fota_deployment.ZebraFotaDeployment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagement
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import monitoring
        from .. import admin_consent, advanced_threat_protection_onboarding_state_summary, android_device_owner_enrollment_profile, android_for_work_app_configuration_schema, android_for_work_enrollment_profile, android_for_work_settings, android_managed_store_account_enterprise_settings, android_managed_store_app_configuration_schema, apple_push_notification_certificate, apple_user_initiated_enrollment_profile, audit_event, cart_to_class_association, certificate_connector_details, chrome_o_s_onboarding_settings, cloud_p_c_connectivity_issue, comanagement_eligible_device, compliance_management_partner, config_manager_collection, connector_status_details, data_processor_service_for_windows_features_onboarding, data_sharing_consent, dep_onboarding_setting, detected_app, device_and_app_management_assignment_filter, device_and_app_management_role_assignment, device_category, device_compliance_policy, device_compliance_policy_device_state_summary, device_compliance_policy_setting_state_summary, device_compliance_script, device_configuration, device_configuration_conflict_summary, device_configuration_device_state_summary, device_configuration_user_state_summary, device_custom_attribute_shell_script, device_enrollment_configuration, device_health_script, device_management_autopilot_event, device_management_compliance_policy, device_management_configuration_category, device_management_configuration_policy, device_management_configuration_policy_template, device_management_configuration_setting_definition, device_management_configuration_setting_template, device_management_derived_credential_settings, device_management_domain_join_connector, device_management_exchange_connector, device_management_exchange_on_premises_policy, device_management_intent, device_management_partner, device_management_reports, device_management_resource_access_profile_base, device_management_reusable_policy_setting, device_management_script, device_management_settings, device_management_setting_category, device_management_setting_definition, device_management_subscriptions, device_management_subscription_state, device_management_template, device_management_template_insights_definition, device_management_troubleshooting_event, device_protection_overview, device_shell_script, embedded_s_i_m_activation_code_pool, entity, group_policy_category, group_policy_configuration, group_policy_definition, group_policy_definition_file, group_policy_migration_report, group_policy_object_file, group_policy_uploaded_definition_file, imported_device_identity, imported_windows_autopilot_device_identity, intune_brand, intune_branding_profile, ios_update_device_status, mac_o_s_software_update_account_summary, managed_all_device_certificate_state, managed_device, managed_device_cleanup_settings, managed_device_encryption_state, managed_device_overview, microsoft_tunnel_configuration, microsoft_tunnel_health_threshold, microsoft_tunnel_server_log_collection_response, microsoft_tunnel_site, mobile_app_troubleshooting_event, mobile_threat_defense_connector, ndes_connector, notification_message_template, on_premises_conditional_access_settings, privilege_management_elevation, remote_action_audit, remote_assistance_partner, remote_assistance_settings, resource_operation, restricted_apps_violation, role_definition, role_scope_tag, service_now_connection, software_update_status_summary, telecom_expense_management_partner, tenant_attach_r_b_a_c, terms_and_conditions, user_experience_analytics_anomaly, user_experience_analytics_anomaly_correlation_group_overview, user_experience_analytics_anomaly_device, user_experience_analytics_anomaly_severity_overview, user_experience_analytics_app_health_application_performance, user_experience_analytics_app_health_app_performance_by_app_version, user_experience_analytics_app_health_app_performance_by_app_version_details, user_experience_analytics_app_health_app_performance_by_app_version_device_id, user_experience_analytics_app_health_app_performance_by_o_s_version, user_experience_analytics_app_health_device_model_performance, user_experience_analytics_app_health_device_performance, user_experience_analytics_app_health_device_performance_details, user_experience_analytics_app_health_o_s_version_performance, user_experience_analytics_baseline, user_experience_analytics_battery_health_app_impact, user_experience_analytics_battery_health_capacity_details, user_experience_analytics_battery_health_device_app_impact, user_experience_analytics_battery_health_device_performance, user_experience_analytics_battery_health_device_runtime_history, user_experience_analytics_battery_health_model_performance, user_experience_analytics_battery_health_os_performance, user_experience_analytics_battery_health_runtime_details, user_experience_analytics_category, user_experience_analytics_device_performance, user_experience_analytics_device_scope, user_experience_analytics_device_scores, user_experience_analytics_device_startup_history, user_experience_analytics_device_startup_process, user_experience_analytics_device_startup_process_performance, user_experience_analytics_device_timeline_event, user_experience_analytics_device_without_cloud_identity, user_experience_analytics_impacting_process, user_experience_analytics_metric_history, user_experience_analytics_model_scores, user_experience_analytics_not_autopilot_ready_device, user_experience_analytics_overview, user_experience_analytics_remote_connection, user_experience_analytics_resource_performance, user_experience_analytics_score_history, user_experience_analytics_settings, user_experience_analytics_work_from_anywhere_hardware_readiness_metric, user_experience_analytics_work_from_anywhere_metric, user_experience_analytics_work_from_anywhere_model_performance, user_p_f_x_certificate, virtual_endpoint, windows_autopilot_deployment_profile, windows_autopilot_device_identity, windows_autopilot_settings, windows_driver_update_profile, windows_feature_update_profile, windows_information_protection_app_learning_summary, windows_information_protection_network_learning_summary, windows_malware_information, windows_malware_overview, windows_quality_update_profile, windows_update_catalog_item, zebra_fota_artifact, zebra_fota_connector, zebra_fota_deployment

        from . import monitoring
        from .. import admin_consent, advanced_threat_protection_onboarding_state_summary, android_device_owner_enrollment_profile, android_for_work_app_configuration_schema, android_for_work_enrollment_profile, android_for_work_settings, android_managed_store_account_enterprise_settings, android_managed_store_app_configuration_schema, apple_push_notification_certificate, apple_user_initiated_enrollment_profile, audit_event, cart_to_class_association, certificate_connector_details, chrome_o_s_onboarding_settings, cloud_p_c_connectivity_issue, comanagement_eligible_device, compliance_management_partner, config_manager_collection, connector_status_details, data_processor_service_for_windows_features_onboarding, data_sharing_consent, dep_onboarding_setting, detected_app, device_and_app_management_assignment_filter, device_and_app_management_role_assignment, device_category, device_compliance_policy, device_compliance_policy_device_state_summary, device_compliance_policy_setting_state_summary, device_compliance_script, device_configuration, device_configuration_conflict_summary, device_configuration_device_state_summary, device_configuration_user_state_summary, device_custom_attribute_shell_script, device_enrollment_configuration, device_health_script, device_management_autopilot_event, device_management_compliance_policy, device_management_configuration_category, device_management_configuration_policy, device_management_configuration_policy_template, device_management_configuration_setting_definition, device_management_configuration_setting_template, device_management_derived_credential_settings, device_management_domain_join_connector, device_management_exchange_connector, device_management_exchange_on_premises_policy, device_management_intent, device_management_partner, device_management_reports, device_management_resource_access_profile_base, device_management_reusable_policy_setting, device_management_script, device_management_settings, device_management_setting_category, device_management_setting_definition, device_management_subscriptions, device_management_subscription_state, device_management_template, device_management_template_insights_definition, device_management_troubleshooting_event, device_protection_overview, device_shell_script, embedded_s_i_m_activation_code_pool, entity, group_policy_category, group_policy_configuration, group_policy_definition, group_policy_definition_file, group_policy_migration_report, group_policy_object_file, group_policy_uploaded_definition_file, imported_device_identity, imported_windows_autopilot_device_identity, intune_brand, intune_branding_profile, ios_update_device_status, mac_o_s_software_update_account_summary, managed_all_device_certificate_state, managed_device, managed_device_cleanup_settings, managed_device_encryption_state, managed_device_overview, microsoft_tunnel_configuration, microsoft_tunnel_health_threshold, microsoft_tunnel_server_log_collection_response, microsoft_tunnel_site, mobile_app_troubleshooting_event, mobile_threat_defense_connector, ndes_connector, notification_message_template, on_premises_conditional_access_settings, privilege_management_elevation, remote_action_audit, remote_assistance_partner, remote_assistance_settings, resource_operation, restricted_apps_violation, role_definition, role_scope_tag, service_now_connection, software_update_status_summary, telecom_expense_management_partner, tenant_attach_r_b_a_c, terms_and_conditions, user_experience_analytics_anomaly, user_experience_analytics_anomaly_correlation_group_overview, user_experience_analytics_anomaly_device, user_experience_analytics_anomaly_severity_overview, user_experience_analytics_app_health_application_performance, user_experience_analytics_app_health_app_performance_by_app_version, user_experience_analytics_app_health_app_performance_by_app_version_details, user_experience_analytics_app_health_app_performance_by_app_version_device_id, user_experience_analytics_app_health_app_performance_by_o_s_version, user_experience_analytics_app_health_device_model_performance, user_experience_analytics_app_health_device_performance, user_experience_analytics_app_health_device_performance_details, user_experience_analytics_app_health_o_s_version_performance, user_experience_analytics_baseline, user_experience_analytics_battery_health_app_impact, user_experience_analytics_battery_health_capacity_details, user_experience_analytics_battery_health_device_app_impact, user_experience_analytics_battery_health_device_performance, user_experience_analytics_battery_health_device_runtime_history, user_experience_analytics_battery_health_model_performance, user_experience_analytics_battery_health_os_performance, user_experience_analytics_battery_health_runtime_details, user_experience_analytics_category, user_experience_analytics_device_performance, user_experience_analytics_device_scope, user_experience_analytics_device_scores, user_experience_analytics_device_startup_history, user_experience_analytics_device_startup_process, user_experience_analytics_device_startup_process_performance, user_experience_analytics_device_timeline_event, user_experience_analytics_device_without_cloud_identity, user_experience_analytics_impacting_process, user_experience_analytics_metric_history, user_experience_analytics_model_scores, user_experience_analytics_not_autopilot_ready_device, user_experience_analytics_overview, user_experience_analytics_remote_connection, user_experience_analytics_resource_performance, user_experience_analytics_score_history, user_experience_analytics_settings, user_experience_analytics_work_from_anywhere_hardware_readiness_metric, user_experience_analytics_work_from_anywhere_metric, user_experience_analytics_work_from_anywhere_model_performance, user_p_f_x_certificate, virtual_endpoint, windows_autopilot_deployment_profile, windows_autopilot_device_identity, windows_autopilot_settings, windows_driver_update_profile, windows_feature_update_profile, windows_information_protection_app_learning_summary, windows_information_protection_network_learning_summary, windows_malware_information, windows_malware_overview, windows_quality_update_profile, windows_update_catalog_item, zebra_fota_artifact, zebra_fota_connector, zebra_fota_deployment

        fields: Dict[str, Callable[[Any], None]] = {
            "accountMoveCompletionDateTime": lambda n : setattr(self, 'account_move_completion_date_time', n.get_datetime_value()),
            "adminConsent": lambda n : setattr(self, 'admin_consent', n.get_object_value(admin_consent.AdminConsent)),
            "advancedThreatProtectionOnboardingStateSummary": lambda n : setattr(self, 'advanced_threat_protection_onboarding_state_summary', n.get_object_value(advanced_threat_protection_onboarding_state_summary.AdvancedThreatProtectionOnboardingStateSummary)),
            "androidDeviceOwnerEnrollmentProfiles": lambda n : setattr(self, 'android_device_owner_enrollment_profiles', n.get_collection_of_object_values(android_device_owner_enrollment_profile.AndroidDeviceOwnerEnrollmentProfile)),
            "androidForWorkAppConfigurationSchemas": lambda n : setattr(self, 'android_for_work_app_configuration_schemas', n.get_collection_of_object_values(android_for_work_app_configuration_schema.AndroidForWorkAppConfigurationSchema)),
            "androidForWorkEnrollmentProfiles": lambda n : setattr(self, 'android_for_work_enrollment_profiles', n.get_collection_of_object_values(android_for_work_enrollment_profile.AndroidForWorkEnrollmentProfile)),
            "androidForWorkSettings": lambda n : setattr(self, 'android_for_work_settings', n.get_object_value(android_for_work_settings.AndroidForWorkSettings)),
            "androidManagedStoreAccountEnterpriseSettings": lambda n : setattr(self, 'android_managed_store_account_enterprise_settings', n.get_object_value(android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings)),
            "androidManagedStoreAppConfigurationSchemas": lambda n : setattr(self, 'android_managed_store_app_configuration_schemas', n.get_collection_of_object_values(android_managed_store_app_configuration_schema.AndroidManagedStoreAppConfigurationSchema)),
            "applePushNotificationCertificate": lambda n : setattr(self, 'apple_push_notification_certificate', n.get_object_value(apple_push_notification_certificate.ApplePushNotificationCertificate)),
            "appleUserInitiatedEnrollmentProfiles": lambda n : setattr(self, 'apple_user_initiated_enrollment_profiles', n.get_collection_of_object_values(apple_user_initiated_enrollment_profile.AppleUserInitiatedEnrollmentProfile)),
            "assignmentFilters": lambda n : setattr(self, 'assignment_filters', n.get_collection_of_object_values(device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter)),
            "auditEvents": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(audit_event.AuditEvent)),
            "autopilotEvents": lambda n : setattr(self, 'autopilot_events', n.get_collection_of_object_values(device_management_autopilot_event.DeviceManagementAutopilotEvent)),
            "cartToClassAssociations": lambda n : setattr(self, 'cart_to_class_associations', n.get_collection_of_object_values(cart_to_class_association.CartToClassAssociation)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(device_management_setting_category.DeviceManagementSettingCategory)),
            "certificateConnectorDetails": lambda n : setattr(self, 'certificate_connector_details', n.get_collection_of_object_values(certificate_connector_details.CertificateConnectorDetails)),
            "chromeOSOnboardingSettings": lambda n : setattr(self, 'chrome_o_s_onboarding_settings', n.get_collection_of_object_values(chrome_o_s_onboarding_settings.ChromeOSOnboardingSettings)),
            "cloudPCConnectivityIssues": lambda n : setattr(self, 'cloud_p_c_connectivity_issues', n.get_collection_of_object_values(cloud_p_c_connectivity_issue.CloudPCConnectivityIssue)),
            "comanagedDevices": lambda n : setattr(self, 'comanaged_devices', n.get_collection_of_object_values(managed_device.ManagedDevice)),
            "comanagementEligibleDevices": lambda n : setattr(self, 'comanagement_eligible_devices', n.get_collection_of_object_values(comanagement_eligible_device.ComanagementEligibleDevice)),
            "complianceCategories": lambda n : setattr(self, 'compliance_categories', n.get_collection_of_object_values(device_management_configuration_category.DeviceManagementConfigurationCategory)),
            "complianceManagementPartners": lambda n : setattr(self, 'compliance_management_partners', n.get_collection_of_object_values(compliance_management_partner.ComplianceManagementPartner)),
            "compliancePolicies": lambda n : setattr(self, 'compliance_policies', n.get_collection_of_object_values(device_management_compliance_policy.DeviceManagementCompliancePolicy)),
            "complianceSettings": lambda n : setattr(self, 'compliance_settings', n.get_collection_of_object_values(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition)),
            "conditionalAccessSettings": lambda n : setattr(self, 'conditional_access_settings', n.get_object_value(on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings)),
            "configManagerCollections": lambda n : setattr(self, 'config_manager_collections', n.get_collection_of_object_values(config_manager_collection.ConfigManagerCollection)),
            "configurationCategories": lambda n : setattr(self, 'configuration_categories', n.get_collection_of_object_values(device_management_configuration_category.DeviceManagementConfigurationCategory)),
            "configurationPolicies": lambda n : setattr(self, 'configuration_policies', n.get_collection_of_object_values(device_management_configuration_policy.DeviceManagementConfigurationPolicy)),
            "configurationPolicyTemplates": lambda n : setattr(self, 'configuration_policy_templates', n.get_collection_of_object_values(device_management_configuration_policy_template.DeviceManagementConfigurationPolicyTemplate)),
            "configurationSettings": lambda n : setattr(self, 'configuration_settings', n.get_collection_of_object_values(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition)),
            "connectorStatus": lambda n : setattr(self, 'connector_status', n.get_collection_of_object_values(connector_status_details.ConnectorStatusDetails)),
            "dataProcessorServiceForWindowsFeaturesOnboarding": lambda n : setattr(self, 'data_processor_service_for_windows_features_onboarding', n.get_object_value(data_processor_service_for_windows_features_onboarding.DataProcessorServiceForWindowsFeaturesOnboarding)),
            "dataSharingConsents": lambda n : setattr(self, 'data_sharing_consents', n.get_collection_of_object_values(data_sharing_consent.DataSharingConsent)),
            "depOnboardingSettings": lambda n : setattr(self, 'dep_onboarding_settings', n.get_collection_of_object_values(dep_onboarding_setting.DepOnboardingSetting)),
            "derivedCredentials": lambda n : setattr(self, 'derived_credentials', n.get_collection_of_object_values(device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings)),
            "detectedApps": lambda n : setattr(self, 'detected_apps', n.get_collection_of_object_values(detected_app.DetectedApp)),
            "deviceCategories": lambda n : setattr(self, 'device_categories', n.get_collection_of_object_values(device_category.DeviceCategory)),
            "deviceCompliancePolicies": lambda n : setattr(self, 'device_compliance_policies', n.get_collection_of_object_values(device_compliance_policy.DeviceCompliancePolicy)),
            "deviceCompliancePolicyDeviceStateSummary": lambda n : setattr(self, 'device_compliance_policy_device_state_summary', n.get_object_value(device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary)),
            "deviceCompliancePolicySettingStateSummaries": lambda n : setattr(self, 'device_compliance_policy_setting_state_summaries', n.get_collection_of_object_values(device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary)),
            "deviceComplianceReportSummarizationDateTime": lambda n : setattr(self, 'device_compliance_report_summarization_date_time', n.get_datetime_value()),
            "deviceComplianceScripts": lambda n : setattr(self, 'device_compliance_scripts', n.get_collection_of_object_values(device_compliance_script.DeviceComplianceScript)),
            "deviceConfigurationConflictSummary": lambda n : setattr(self, 'device_configuration_conflict_summary', n.get_collection_of_object_values(device_configuration_conflict_summary.DeviceConfigurationConflictSummary)),
            "deviceConfigurationDeviceStateSummaries": lambda n : setattr(self, 'device_configuration_device_state_summaries', n.get_object_value(device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary)),
            "deviceConfigurationRestrictedAppsViolations": lambda n : setattr(self, 'device_configuration_restricted_apps_violations', n.get_collection_of_object_values(restricted_apps_violation.RestrictedAppsViolation)),
            "deviceConfigurationUserStateSummaries": lambda n : setattr(self, 'device_configuration_user_state_summaries', n.get_object_value(device_configuration_user_state_summary.DeviceConfigurationUserStateSummary)),
            "deviceConfigurations": lambda n : setattr(self, 'device_configurations', n.get_collection_of_object_values(device_configuration.DeviceConfiguration)),
            "deviceConfigurationsAllManagedDeviceCertificateStates": lambda n : setattr(self, 'device_configurations_all_managed_device_certificate_states', n.get_collection_of_object_values(managed_all_device_certificate_state.ManagedAllDeviceCertificateState)),
            "deviceCustomAttributeShellScripts": lambda n : setattr(self, 'device_custom_attribute_shell_scripts', n.get_collection_of_object_values(device_custom_attribute_shell_script.DeviceCustomAttributeShellScript)),
            "deviceEnrollmentConfigurations": lambda n : setattr(self, 'device_enrollment_configurations', n.get_collection_of_object_values(device_enrollment_configuration.DeviceEnrollmentConfiguration)),
            "deviceHealthScripts": lambda n : setattr(self, 'device_health_scripts', n.get_collection_of_object_values(device_health_script.DeviceHealthScript)),
            "deviceManagementPartners": lambda n : setattr(self, 'device_management_partners', n.get_collection_of_object_values(device_management_partner.DeviceManagementPartner)),
            "deviceManagementScripts": lambda n : setattr(self, 'device_management_scripts', n.get_collection_of_object_values(device_management_script.DeviceManagementScript)),
            "deviceProtectionOverview": lambda n : setattr(self, 'device_protection_overview', n.get_object_value(device_protection_overview.DeviceProtectionOverview)),
            "deviceShellScripts": lambda n : setattr(self, 'device_shell_scripts', n.get_collection_of_object_values(device_shell_script.DeviceShellScript)),
            "domainJoinConnectors": lambda n : setattr(self, 'domain_join_connectors', n.get_collection_of_object_values(device_management_domain_join_connector.DeviceManagementDomainJoinConnector)),
            "embeddedSIMActivationCodePools": lambda n : setattr(self, 'embedded_s_i_m_activation_code_pools', n.get_collection_of_object_values(embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool)),
            "exchangeConnectors": lambda n : setattr(self, 'exchange_connectors', n.get_collection_of_object_values(device_management_exchange_connector.DeviceManagementExchangeConnector)),
            "exchangeOnPremisesPolicies": lambda n : setattr(self, 'exchange_on_premises_policies', n.get_collection_of_object_values(device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy)),
            "exchangeOnPremisesPolicy": lambda n : setattr(self, 'exchange_on_premises_policy', n.get_object_value(device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy)),
            "groupPolicyCategories": lambda n : setattr(self, 'group_policy_categories', n.get_collection_of_object_values(group_policy_category.GroupPolicyCategory)),
            "groupPolicyConfigurations": lambda n : setattr(self, 'group_policy_configurations', n.get_collection_of_object_values(group_policy_configuration.GroupPolicyConfiguration)),
            "groupPolicyDefinitionFiles": lambda n : setattr(self, 'group_policy_definition_files', n.get_collection_of_object_values(group_policy_definition_file.GroupPolicyDefinitionFile)),
            "groupPolicyDefinitions": lambda n : setattr(self, 'group_policy_definitions', n.get_collection_of_object_values(group_policy_definition.GroupPolicyDefinition)),
            "groupPolicyMigrationReports": lambda n : setattr(self, 'group_policy_migration_reports', n.get_collection_of_object_values(group_policy_migration_report.GroupPolicyMigrationReport)),
            "groupPolicyObjectFiles": lambda n : setattr(self, 'group_policy_object_files', n.get_collection_of_object_values(group_policy_object_file.GroupPolicyObjectFile)),
            "groupPolicyUploadedDefinitionFiles": lambda n : setattr(self, 'group_policy_uploaded_definition_files', n.get_collection_of_object_values(group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile)),
            "importedDeviceIdentities": lambda n : setattr(self, 'imported_device_identities', n.get_collection_of_object_values(imported_device_identity.ImportedDeviceIdentity)),
            "importedWindowsAutopilotDeviceIdentities": lambda n : setattr(self, 'imported_windows_autopilot_device_identities', n.get_collection_of_object_values(imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity)),
            "intents": lambda n : setattr(self, 'intents', n.get_collection_of_object_values(device_management_intent.DeviceManagementIntent)),
            "intuneAccountId": lambda n : setattr(self, 'intune_account_id', n.get_uuid_value()),
            "intuneBrand": lambda n : setattr(self, 'intune_brand', n.get_object_value(intune_brand.IntuneBrand)),
            "intuneBrandingProfiles": lambda n : setattr(self, 'intune_branding_profiles', n.get_collection_of_object_values(intune_branding_profile.IntuneBrandingProfile)),
            "iosUpdateStatuses": lambda n : setattr(self, 'ios_update_statuses', n.get_collection_of_object_values(ios_update_device_status.IosUpdateDeviceStatus)),
            "lastReportAggregationDateTime": lambda n : setattr(self, 'last_report_aggregation_date_time', n.get_datetime_value()),
            "legacyPcManangementEnabled": lambda n : setattr(self, 'legacy_pc_manangement_enabled', n.get_bool_value()),
            "macOSSoftwareUpdateAccountSummaries": lambda n : setattr(self, 'mac_o_s_software_update_account_summaries', n.get_collection_of_object_values(mac_o_s_software_update_account_summary.MacOSSoftwareUpdateAccountSummary)),
            "managedDeviceCleanupSettings": lambda n : setattr(self, 'managed_device_cleanup_settings', n.get_object_value(managed_device_cleanup_settings.ManagedDeviceCleanupSettings)),
            "managedDeviceEncryptionStates": lambda n : setattr(self, 'managed_device_encryption_states', n.get_collection_of_object_values(managed_device_encryption_state.ManagedDeviceEncryptionState)),
            "managedDeviceOverview": lambda n : setattr(self, 'managed_device_overview', n.get_object_value(managed_device_overview.ManagedDeviceOverview)),
            "managedDevices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(managed_device.ManagedDevice)),
            "maximumDepTokens": lambda n : setattr(self, 'maximum_dep_tokens', n.get_int_value()),
            "microsoftTunnelConfigurations": lambda n : setattr(self, 'microsoft_tunnel_configurations', n.get_collection_of_object_values(microsoft_tunnel_configuration.MicrosoftTunnelConfiguration)),
            "microsoftTunnelHealthThresholds": lambda n : setattr(self, 'microsoft_tunnel_health_thresholds', n.get_collection_of_object_values(microsoft_tunnel_health_threshold.MicrosoftTunnelHealthThreshold)),
            "microsoftTunnelServerLogCollectionResponses": lambda n : setattr(self, 'microsoft_tunnel_server_log_collection_responses', n.get_collection_of_object_values(microsoft_tunnel_server_log_collection_response.MicrosoftTunnelServerLogCollectionResponse)),
            "microsoftTunnelSites": lambda n : setattr(self, 'microsoft_tunnel_sites', n.get_collection_of_object_values(microsoft_tunnel_site.MicrosoftTunnelSite)),
            "mobileAppTroubleshootingEvents": lambda n : setattr(self, 'mobile_app_troubleshooting_events', n.get_collection_of_object_values(mobile_app_troubleshooting_event.MobileAppTroubleshootingEvent)),
            "mobileThreatDefenseConnectors": lambda n : setattr(self, 'mobile_threat_defense_connectors', n.get_collection_of_object_values(mobile_threat_defense_connector.MobileThreatDefenseConnector)),
            "monitoring": lambda n : setattr(self, 'monitoring', n.get_object_value(monitoring.Monitoring)),
            "ndesConnectors": lambda n : setattr(self, 'ndes_connectors', n.get_collection_of_object_values(ndes_connector.NdesConnector)),
            "notificationMessageTemplates": lambda n : setattr(self, 'notification_message_templates', n.get_collection_of_object_values(notification_message_template.NotificationMessageTemplate)),
            "privilegeManagementElevations": lambda n : setattr(self, 'privilege_management_elevations', n.get_collection_of_object_values(privilege_management_elevation.PrivilegeManagementElevation)),
            "remoteActionAudits": lambda n : setattr(self, 'remote_action_audits', n.get_collection_of_object_values(remote_action_audit.RemoteActionAudit)),
            "remoteAssistancePartners": lambda n : setattr(self, 'remote_assistance_partners', n.get_collection_of_object_values(remote_assistance_partner.RemoteAssistancePartner)),
            "remoteAssistanceSettings": lambda n : setattr(self, 'remote_assistance_settings', n.get_object_value(remote_assistance_settings.RemoteAssistanceSettings)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(device_management_reports.DeviceManagementReports)),
            "resourceAccessProfiles": lambda n : setattr(self, 'resource_access_profiles', n.get_collection_of_object_values(device_management_resource_access_profile_base.DeviceManagementResourceAccessProfileBase)),
            "resourceOperations": lambda n : setattr(self, 'resource_operations', n.get_collection_of_object_values(resource_operation.ResourceOperation)),
            "reusablePolicySettings": lambda n : setattr(self, 'reusable_policy_settings', n.get_collection_of_object_values(device_management_reusable_policy_setting.DeviceManagementReusablePolicySetting)),
            "reusableSettings": lambda n : setattr(self, 'reusable_settings', n.get_collection_of_object_values(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(role_definition.RoleDefinition)),
            "roleScopeTags": lambda n : setattr(self, 'role_scope_tags', n.get_collection_of_object_values(role_scope_tag.RoleScopeTag)),
            "serviceNowConnections": lambda n : setattr(self, 'service_now_connections', n.get_collection_of_object_values(service_now_connection.ServiceNowConnection)),
            "settingDefinitions": lambda n : setattr(self, 'setting_definitions', n.get_collection_of_object_values(device_management_setting_definition.DeviceManagementSettingDefinition)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(device_management_settings.DeviceManagementSettings)),
            "softwareUpdateStatusSummary": lambda n : setattr(self, 'software_update_status_summary', n.get_object_value(software_update_status_summary.SoftwareUpdateStatusSummary)),
            "subscriptionState": lambda n : setattr(self, 'subscription_state', n.get_enum_value(device_management_subscription_state.DeviceManagementSubscriptionState)),
            "subscriptions": lambda n : setattr(self, 'subscriptions', n.get_enum_value(device_management_subscriptions.DeviceManagementSubscriptions)),
            "telecomExpenseManagementPartners": lambda n : setattr(self, 'telecom_expense_management_partners', n.get_collection_of_object_values(telecom_expense_management_partner.TelecomExpenseManagementPartner)),
            "templateInsights": lambda n : setattr(self, 'template_insights', n.get_collection_of_object_values(device_management_template_insights_definition.DeviceManagementTemplateInsightsDefinition)),
            "templateSettings": lambda n : setattr(self, 'template_settings', n.get_collection_of_object_values(device_management_configuration_setting_template.DeviceManagementConfigurationSettingTemplate)),
            "templates": lambda n : setattr(self, 'templates', n.get_collection_of_object_values(device_management_template.DeviceManagementTemplate)),
            "tenantAttachRBAC": lambda n : setattr(self, 'tenant_attach_r_b_a_c', n.get_object_value(tenant_attach_r_b_a_c.TenantAttachRBAC)),
            "termsAndConditions": lambda n : setattr(self, 'terms_and_conditions', n.get_collection_of_object_values(terms_and_conditions.TermsAndConditions)),
            "troubleshootingEvents": lambda n : setattr(self, 'troubleshooting_events', n.get_collection_of_object_values(device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent)),
            "unlicensedAdminstratorsEnabled": lambda n : setattr(self, 'unlicensed_adminstrators_enabled', n.get_bool_value()),
            "userExperienceAnalyticsAnomaly": lambda n : setattr(self, 'user_experience_analytics_anomaly', n.get_collection_of_object_values(user_experience_analytics_anomaly.UserExperienceAnalyticsAnomaly)),
            "userExperienceAnalyticsAnomalyCorrelationGroupOverview": lambda n : setattr(self, 'user_experience_analytics_anomaly_correlation_group_overview', n.get_collection_of_object_values(user_experience_analytics_anomaly_correlation_group_overview.UserExperienceAnalyticsAnomalyCorrelationGroupOverview)),
            "userExperienceAnalyticsAnomalyDevice": lambda n : setattr(self, 'user_experience_analytics_anomaly_device', n.get_collection_of_object_values(user_experience_analytics_anomaly_device.UserExperienceAnalyticsAnomalyDevice)),
            "userExperienceAnalyticsAnomalySeverityOverview": lambda n : setattr(self, 'user_experience_analytics_anomaly_severity_overview', n.get_object_value(user_experience_analytics_anomaly_severity_overview.UserExperienceAnalyticsAnomalySeverityOverview)),
            "userExperienceAnalyticsAppHealthApplicationPerformance": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance', n.get_collection_of_object_values(user_experience_analytics_app_health_application_performance.UserExperienceAnalyticsAppHealthApplicationPerformance)),
            "userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_app_version', n.get_collection_of_object_values(user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion)),
            "userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_app_version_details', n.get_collection_of_object_values(user_experience_analytics_app_health_app_performance_by_app_version_details.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails)),
            "userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_app_version_device_id', n.get_collection_of_object_values(user_experience_analytics_app_health_app_performance_by_app_version_device_id.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId)),
            "userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_o_s_version', n.get_collection_of_object_values(user_experience_analytics_app_health_app_performance_by_o_s_version.UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion)),
            "userExperienceAnalyticsAppHealthDeviceModelPerformance": lambda n : setattr(self, 'user_experience_analytics_app_health_device_model_performance', n.get_collection_of_object_values(user_experience_analytics_app_health_device_model_performance.UserExperienceAnalyticsAppHealthDeviceModelPerformance)),
            "userExperienceAnalyticsAppHealthDevicePerformance": lambda n : setattr(self, 'user_experience_analytics_app_health_device_performance', n.get_collection_of_object_values(user_experience_analytics_app_health_device_performance.UserExperienceAnalyticsAppHealthDevicePerformance)),
            "userExperienceAnalyticsAppHealthDevicePerformanceDetails": lambda n : setattr(self, 'user_experience_analytics_app_health_device_performance_details', n.get_collection_of_object_values(user_experience_analytics_app_health_device_performance_details.UserExperienceAnalyticsAppHealthDevicePerformanceDetails)),
            "userExperienceAnalyticsAppHealthOSVersionPerformance": lambda n : setattr(self, 'user_experience_analytics_app_health_o_s_version_performance', n.get_collection_of_object_values(user_experience_analytics_app_health_o_s_version_performance.UserExperienceAnalyticsAppHealthOSVersionPerformance)),
            "userExperienceAnalyticsAppHealthOverview": lambda n : setattr(self, 'user_experience_analytics_app_health_overview', n.get_object_value(user_experience_analytics_category.UserExperienceAnalyticsCategory)),
            "userExperienceAnalyticsBaselines": lambda n : setattr(self, 'user_experience_analytics_baselines', n.get_collection_of_object_values(user_experience_analytics_baseline.UserExperienceAnalyticsBaseline)),
            "userExperienceAnalyticsBatteryHealthAppImpact": lambda n : setattr(self, 'user_experience_analytics_battery_health_app_impact', n.get_collection_of_object_values(user_experience_analytics_battery_health_app_impact.UserExperienceAnalyticsBatteryHealthAppImpact)),
            "userExperienceAnalyticsBatteryHealthCapacityDetails": lambda n : setattr(self, 'user_experience_analytics_battery_health_capacity_details', n.get_object_value(user_experience_analytics_battery_health_capacity_details.UserExperienceAnalyticsBatteryHealthCapacityDetails)),
            "userExperienceAnalyticsBatteryHealthDeviceAppImpact": lambda n : setattr(self, 'user_experience_analytics_battery_health_device_app_impact', n.get_collection_of_object_values(user_experience_analytics_battery_health_device_app_impact.UserExperienceAnalyticsBatteryHealthDeviceAppImpact)),
            "userExperienceAnalyticsBatteryHealthDevicePerformance": lambda n : setattr(self, 'user_experience_analytics_battery_health_device_performance', n.get_collection_of_object_values(user_experience_analytics_battery_health_device_performance.UserExperienceAnalyticsBatteryHealthDevicePerformance)),
            "userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory": lambda n : setattr(self, 'user_experience_analytics_battery_health_device_runtime_history', n.get_collection_of_object_values(user_experience_analytics_battery_health_device_runtime_history.UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory)),
            "userExperienceAnalyticsBatteryHealthModelPerformance": lambda n : setattr(self, 'user_experience_analytics_battery_health_model_performance', n.get_collection_of_object_values(user_experience_analytics_battery_health_model_performance.UserExperienceAnalyticsBatteryHealthModelPerformance)),
            "userExperienceAnalyticsBatteryHealthOsPerformance": lambda n : setattr(self, 'user_experience_analytics_battery_health_os_performance', n.get_collection_of_object_values(user_experience_analytics_battery_health_os_performance.UserExperienceAnalyticsBatteryHealthOsPerformance)),
            "userExperienceAnalyticsBatteryHealthRuntimeDetails": lambda n : setattr(self, 'user_experience_analytics_battery_health_runtime_details', n.get_object_value(user_experience_analytics_battery_health_runtime_details.UserExperienceAnalyticsBatteryHealthRuntimeDetails)),
            "userExperienceAnalyticsCategories": lambda n : setattr(self, 'user_experience_analytics_categories', n.get_collection_of_object_values(user_experience_analytics_category.UserExperienceAnalyticsCategory)),
            "userExperienceAnalyticsDeviceMetricHistory": lambda n : setattr(self, 'user_experience_analytics_device_metric_history', n.get_collection_of_object_values(user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory)),
            "userExperienceAnalyticsDevicePerformance": lambda n : setattr(self, 'user_experience_analytics_device_performance', n.get_collection_of_object_values(user_experience_analytics_device_performance.UserExperienceAnalyticsDevicePerformance)),
            "userExperienceAnalyticsDeviceScope": lambda n : setattr(self, 'user_experience_analytics_device_scope', n.get_object_value(user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope)),
            "userExperienceAnalyticsDeviceScopes": lambda n : setattr(self, 'user_experience_analytics_device_scopes', n.get_collection_of_object_values(user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope)),
            "userExperienceAnalyticsDeviceScores": lambda n : setattr(self, 'user_experience_analytics_device_scores', n.get_collection_of_object_values(user_experience_analytics_device_scores.UserExperienceAnalyticsDeviceScores)),
            "userExperienceAnalyticsDeviceStartupHistory": lambda n : setattr(self, 'user_experience_analytics_device_startup_history', n.get_collection_of_object_values(user_experience_analytics_device_startup_history.UserExperienceAnalyticsDeviceStartupHistory)),
            "userExperienceAnalyticsDeviceStartupProcessPerformance": lambda n : setattr(self, 'user_experience_analytics_device_startup_process_performance', n.get_collection_of_object_values(user_experience_analytics_device_startup_process_performance.UserExperienceAnalyticsDeviceStartupProcessPerformance)),
            "userExperienceAnalyticsDeviceStartupProcesses": lambda n : setattr(self, 'user_experience_analytics_device_startup_processes', n.get_collection_of_object_values(user_experience_analytics_device_startup_process.UserExperienceAnalyticsDeviceStartupProcess)),
            "userExperienceAnalyticsDeviceTimelineEvent": lambda n : setattr(self, 'user_experience_analytics_device_timeline_event', n.get_collection_of_object_values(user_experience_analytics_device_timeline_event.UserExperienceAnalyticsDeviceTimelineEvent)),
            "userExperienceAnalyticsDevicesWithoutCloudIdentity": lambda n : setattr(self, 'user_experience_analytics_devices_without_cloud_identity', n.get_collection_of_object_values(user_experience_analytics_device_without_cloud_identity.UserExperienceAnalyticsDeviceWithoutCloudIdentity)),
            "userExperienceAnalyticsImpactingProcess": lambda n : setattr(self, 'user_experience_analytics_impacting_process', n.get_collection_of_object_values(user_experience_analytics_impacting_process.UserExperienceAnalyticsImpactingProcess)),
            "userExperienceAnalyticsMetricHistory": lambda n : setattr(self, 'user_experience_analytics_metric_history', n.get_collection_of_object_values(user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory)),
            "userExperienceAnalyticsModelScores": lambda n : setattr(self, 'user_experience_analytics_model_scores', n.get_collection_of_object_values(user_experience_analytics_model_scores.UserExperienceAnalyticsModelScores)),
            "userExperienceAnalyticsNotAutopilotReadyDevice": lambda n : setattr(self, 'user_experience_analytics_not_autopilot_ready_device', n.get_collection_of_object_values(user_experience_analytics_not_autopilot_ready_device.UserExperienceAnalyticsNotAutopilotReadyDevice)),
            "userExperienceAnalyticsOverview": lambda n : setattr(self, 'user_experience_analytics_overview', n.get_object_value(user_experience_analytics_overview.UserExperienceAnalyticsOverview)),
            "userExperienceAnalyticsRemoteConnection": lambda n : setattr(self, 'user_experience_analytics_remote_connection', n.get_collection_of_object_values(user_experience_analytics_remote_connection.UserExperienceAnalyticsRemoteConnection)),
            "userExperienceAnalyticsResourcePerformance": lambda n : setattr(self, 'user_experience_analytics_resource_performance', n.get_collection_of_object_values(user_experience_analytics_resource_performance.UserExperienceAnalyticsResourcePerformance)),
            "userExperienceAnalyticsScoreHistory": lambda n : setattr(self, 'user_experience_analytics_score_history', n.get_collection_of_object_values(user_experience_analytics_score_history.UserExperienceAnalyticsScoreHistory)),
            "userExperienceAnalyticsSettings": lambda n : setattr(self, 'user_experience_analytics_settings', n.get_object_value(user_experience_analytics_settings.UserExperienceAnalyticsSettings)),
            "userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_hardware_readiness_metric', n.get_object_value(user_experience_analytics_work_from_anywhere_hardware_readiness_metric.UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric)),
            "userExperienceAnalyticsWorkFromAnywhereMetrics": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_metrics', n.get_collection_of_object_values(user_experience_analytics_work_from_anywhere_metric.UserExperienceAnalyticsWorkFromAnywhereMetric)),
            "userExperienceAnalyticsWorkFromAnywhereModelPerformance": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_model_performance', n.get_collection_of_object_values(user_experience_analytics_work_from_anywhere_model_performance.UserExperienceAnalyticsWorkFromAnywhereModelPerformance)),
            "userPfxCertificates": lambda n : setattr(self, 'user_pfx_certificates', n.get_collection_of_object_values(user_p_f_x_certificate.UserPFXCertificate)),
            "virtualEndpoint": lambda n : setattr(self, 'virtual_endpoint', n.get_object_value(virtual_endpoint.VirtualEndpoint)),
            "windowsAutopilotDeploymentProfiles": lambda n : setattr(self, 'windows_autopilot_deployment_profiles', n.get_collection_of_object_values(windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile)),
            "windowsAutopilotDeviceIdentities": lambda n : setattr(self, 'windows_autopilot_device_identities', n.get_collection_of_object_values(windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity)),
            "windowsAutopilotSettings": lambda n : setattr(self, 'windows_autopilot_settings', n.get_object_value(windows_autopilot_settings.WindowsAutopilotSettings)),
            "windowsDriverUpdateProfiles": lambda n : setattr(self, 'windows_driver_update_profiles', n.get_collection_of_object_values(windows_driver_update_profile.WindowsDriverUpdateProfile)),
            "windowsFeatureUpdateProfiles": lambda n : setattr(self, 'windows_feature_update_profiles', n.get_collection_of_object_values(windows_feature_update_profile.WindowsFeatureUpdateProfile)),
            "windowsInformationProtectionAppLearningSummaries": lambda n : setattr(self, 'windows_information_protection_app_learning_summaries', n.get_collection_of_object_values(windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary)),
            "windowsInformationProtectionNetworkLearningSummaries": lambda n : setattr(self, 'windows_information_protection_network_learning_summaries', n.get_collection_of_object_values(windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary)),
            "windowsMalwareInformation": lambda n : setattr(self, 'windows_malware_information', n.get_collection_of_object_values(windows_malware_information.WindowsMalwareInformation)),
            "windowsMalwareOverview": lambda n : setattr(self, 'windows_malware_overview', n.get_object_value(windows_malware_overview.WindowsMalwareOverview)),
            "windowsQualityUpdateProfiles": lambda n : setattr(self, 'windows_quality_update_profiles', n.get_collection_of_object_values(windows_quality_update_profile.WindowsQualityUpdateProfile)),
            "windowsUpdateCatalogItems": lambda n : setattr(self, 'windows_update_catalog_items', n.get_collection_of_object_values(windows_update_catalog_item.WindowsUpdateCatalogItem)),
            "zebraFotaArtifacts": lambda n : setattr(self, 'zebra_fota_artifacts', n.get_collection_of_object_values(zebra_fota_artifact.ZebraFotaArtifact)),
            "zebraFotaConnector": lambda n : setattr(self, 'zebra_fota_connector', n.get_object_value(zebra_fota_connector.ZebraFotaConnector)),
            "zebraFotaDeployments": lambda n : setattr(self, 'zebra_fota_deployments', n.get_collection_of_object_values(zebra_fota_deployment.ZebraFotaDeployment)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("accountMoveCompletionDateTime", self.account_move_completion_date_time)
        writer.write_object_value("adminConsent", self.admin_consent)
        writer.write_object_value("advancedThreatProtectionOnboardingStateSummary", self.advanced_threat_protection_onboarding_state_summary)
        writer.write_collection_of_object_values("androidDeviceOwnerEnrollmentProfiles", self.android_device_owner_enrollment_profiles)
        writer.write_collection_of_object_values("androidForWorkAppConfigurationSchemas", self.android_for_work_app_configuration_schemas)
        writer.write_collection_of_object_values("androidForWorkEnrollmentProfiles", self.android_for_work_enrollment_profiles)
        writer.write_object_value("androidForWorkSettings", self.android_for_work_settings)
        writer.write_object_value("androidManagedStoreAccountEnterpriseSettings", self.android_managed_store_account_enterprise_settings)
        writer.write_collection_of_object_values("androidManagedStoreAppConfigurationSchemas", self.android_managed_store_app_configuration_schemas)
        writer.write_object_value("applePushNotificationCertificate", self.apple_push_notification_certificate)
        writer.write_collection_of_object_values("appleUserInitiatedEnrollmentProfiles", self.apple_user_initiated_enrollment_profiles)
        writer.write_collection_of_object_values("assignmentFilters", self.assignment_filters)
        writer.write_collection_of_object_values("auditEvents", self.audit_events)
        writer.write_collection_of_object_values("autopilotEvents", self.autopilot_events)
        writer.write_collection_of_object_values("cartToClassAssociations", self.cart_to_class_associations)
        writer.write_collection_of_object_values("categories", self.categories)
        writer.write_collection_of_object_values("certificateConnectorDetails", self.certificate_connector_details)
        writer.write_collection_of_object_values("chromeOSOnboardingSettings", self.chrome_o_s_onboarding_settings)
        writer.write_collection_of_object_values("cloudPCConnectivityIssues", self.cloud_p_c_connectivity_issues)
        writer.write_collection_of_object_values("comanagedDevices", self.comanaged_devices)
        writer.write_collection_of_object_values("comanagementEligibleDevices", self.comanagement_eligible_devices)
        writer.write_collection_of_object_values("complianceCategories", self.compliance_categories)
        writer.write_collection_of_object_values("complianceManagementPartners", self.compliance_management_partners)
        writer.write_collection_of_object_values("compliancePolicies", self.compliance_policies)
        writer.write_collection_of_object_values("complianceSettings", self.compliance_settings)
        writer.write_object_value("conditionalAccessSettings", self.conditional_access_settings)
        writer.write_collection_of_object_values("configManagerCollections", self.config_manager_collections)
        writer.write_collection_of_object_values("configurationCategories", self.configuration_categories)
        writer.write_collection_of_object_values("configurationPolicies", self.configuration_policies)
        writer.write_collection_of_object_values("configurationPolicyTemplates", self.configuration_policy_templates)
        writer.write_collection_of_object_values("configurationSettings", self.configuration_settings)
        writer.write_collection_of_object_values("connectorStatus", self.connector_status)
        writer.write_object_value("dataProcessorServiceForWindowsFeaturesOnboarding", self.data_processor_service_for_windows_features_onboarding)
        writer.write_collection_of_object_values("dataSharingConsents", self.data_sharing_consents)
        writer.write_collection_of_object_values("depOnboardingSettings", self.dep_onboarding_settings)
        writer.write_collection_of_object_values("derivedCredentials", self.derived_credentials)
        writer.write_collection_of_object_values("detectedApps", self.detected_apps)
        writer.write_collection_of_object_values("deviceCategories", self.device_categories)
        writer.write_collection_of_object_values("deviceCompliancePolicies", self.device_compliance_policies)
        writer.write_object_value("deviceCompliancePolicyDeviceStateSummary", self.device_compliance_policy_device_state_summary)
        writer.write_collection_of_object_values("deviceCompliancePolicySettingStateSummaries", self.device_compliance_policy_setting_state_summaries)
        writer.write_collection_of_object_values("deviceComplianceScripts", self.device_compliance_scripts)
        writer.write_collection_of_object_values("deviceConfigurationConflictSummary", self.device_configuration_conflict_summary)
        writer.write_object_value("deviceConfigurationDeviceStateSummaries", self.device_configuration_device_state_summaries)
        writer.write_collection_of_object_values("deviceConfigurationRestrictedAppsViolations", self.device_configuration_restricted_apps_violations)
        writer.write_object_value("deviceConfigurationUserStateSummaries", self.device_configuration_user_state_summaries)
        writer.write_collection_of_object_values("deviceConfigurations", self.device_configurations)
        writer.write_collection_of_object_values("deviceConfigurationsAllManagedDeviceCertificateStates", self.device_configurations_all_managed_device_certificate_states)
        writer.write_collection_of_object_values("deviceCustomAttributeShellScripts", self.device_custom_attribute_shell_scripts)
        writer.write_collection_of_object_values("deviceEnrollmentConfigurations", self.device_enrollment_configurations)
        writer.write_collection_of_object_values("deviceHealthScripts", self.device_health_scripts)
        writer.write_collection_of_object_values("deviceManagementPartners", self.device_management_partners)
        writer.write_collection_of_object_values("deviceManagementScripts", self.device_management_scripts)
        writer.write_object_value("deviceProtectionOverview", self.device_protection_overview)
        writer.write_collection_of_object_values("deviceShellScripts", self.device_shell_scripts)
        writer.write_collection_of_object_values("domainJoinConnectors", self.domain_join_connectors)
        writer.write_collection_of_object_values("embeddedSIMActivationCodePools", self.embedded_s_i_m_activation_code_pools)
        writer.write_collection_of_object_values("exchangeConnectors", self.exchange_connectors)
        writer.write_collection_of_object_values("exchangeOnPremisesPolicies", self.exchange_on_premises_policies)
        writer.write_object_value("exchangeOnPremisesPolicy", self.exchange_on_premises_policy)
        writer.write_collection_of_object_values("groupPolicyCategories", self.group_policy_categories)
        writer.write_collection_of_object_values("groupPolicyConfigurations", self.group_policy_configurations)
        writer.write_collection_of_object_values("groupPolicyDefinitionFiles", self.group_policy_definition_files)
        writer.write_collection_of_object_values("groupPolicyDefinitions", self.group_policy_definitions)
        writer.write_collection_of_object_values("groupPolicyMigrationReports", self.group_policy_migration_reports)
        writer.write_collection_of_object_values("groupPolicyObjectFiles", self.group_policy_object_files)
        writer.write_collection_of_object_values("groupPolicyUploadedDefinitionFiles", self.group_policy_uploaded_definition_files)
        writer.write_collection_of_object_values("importedDeviceIdentities", self.imported_device_identities)
        writer.write_collection_of_object_values("importedWindowsAutopilotDeviceIdentities", self.imported_windows_autopilot_device_identities)
        writer.write_collection_of_object_values("intents", self.intents)
        writer.write_uuid_value("intuneAccountId", self.intune_account_id)
        writer.write_object_value("intuneBrand", self.intune_brand)
        writer.write_collection_of_object_values("intuneBrandingProfiles", self.intune_branding_profiles)
        writer.write_collection_of_object_values("iosUpdateStatuses", self.ios_update_statuses)
        writer.write_collection_of_object_values("macOSSoftwareUpdateAccountSummaries", self.mac_o_s_software_update_account_summaries)
        writer.write_object_value("managedDeviceCleanupSettings", self.managed_device_cleanup_settings)
        writer.write_collection_of_object_values("managedDeviceEncryptionStates", self.managed_device_encryption_states)
        writer.write_object_value("managedDeviceOverview", self.managed_device_overview)
        writer.write_collection_of_object_values("managedDevices", self.managed_devices)
        writer.write_int_value("maximumDepTokens", self.maximum_dep_tokens)
        writer.write_collection_of_object_values("microsoftTunnelConfigurations", self.microsoft_tunnel_configurations)
        writer.write_collection_of_object_values("microsoftTunnelHealthThresholds", self.microsoft_tunnel_health_thresholds)
        writer.write_collection_of_object_values("microsoftTunnelServerLogCollectionResponses", self.microsoft_tunnel_server_log_collection_responses)
        writer.write_collection_of_object_values("microsoftTunnelSites", self.microsoft_tunnel_sites)
        writer.write_collection_of_object_values("mobileAppTroubleshootingEvents", self.mobile_app_troubleshooting_events)
        writer.write_collection_of_object_values("mobileThreatDefenseConnectors", self.mobile_threat_defense_connectors)
        writer.write_object_value("monitoring", self.monitoring)
        writer.write_collection_of_object_values("ndesConnectors", self.ndes_connectors)
        writer.write_collection_of_object_values("notificationMessageTemplates", self.notification_message_templates)
        writer.write_collection_of_object_values("privilegeManagementElevations", self.privilege_management_elevations)
        writer.write_collection_of_object_values("remoteActionAudits", self.remote_action_audits)
        writer.write_collection_of_object_values("remoteAssistancePartners", self.remote_assistance_partners)
        writer.write_object_value("remoteAssistanceSettings", self.remote_assistance_settings)
        writer.write_object_value("reports", self.reports)
        writer.write_collection_of_object_values("resourceAccessProfiles", self.resource_access_profiles)
        writer.write_collection_of_object_values("resourceOperations", self.resource_operations)
        writer.write_collection_of_object_values("reusablePolicySettings", self.reusable_policy_settings)
        writer.write_collection_of_object_values("reusableSettings", self.reusable_settings)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("roleScopeTags", self.role_scope_tags)
        writer.write_collection_of_object_values("serviceNowConnections", self.service_now_connections)
        writer.write_collection_of_object_values("settingDefinitions", self.setting_definitions)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("softwareUpdateStatusSummary", self.software_update_status_summary)
        writer.write_enum_value("subscriptionState", self.subscription_state)
        writer.write_enum_value("subscriptions", self.subscriptions)
        writer.write_collection_of_object_values("telecomExpenseManagementPartners", self.telecom_expense_management_partners)
        writer.write_collection_of_object_values("templateInsights", self.template_insights)
        writer.write_collection_of_object_values("templateSettings", self.template_settings)
        writer.write_collection_of_object_values("templates", self.templates)
        writer.write_object_value("tenantAttachRBAC", self.tenant_attach_r_b_a_c)
        writer.write_collection_of_object_values("termsAndConditions", self.terms_and_conditions)
        writer.write_collection_of_object_values("troubleshootingEvents", self.troubleshooting_events)
        writer.write_collection_of_object_values("userExperienceAnalyticsAnomaly", self.user_experience_analytics_anomaly)
        writer.write_collection_of_object_values("userExperienceAnalyticsAnomalyCorrelationGroupOverview", self.user_experience_analytics_anomaly_correlation_group_overview)
        writer.write_collection_of_object_values("userExperienceAnalyticsAnomalyDevice", self.user_experience_analytics_anomaly_device)
        writer.write_object_value("userExperienceAnalyticsAnomalySeverityOverview", self.user_experience_analytics_anomaly_severity_overview)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformance", self.user_experience_analytics_app_health_application_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion", self.user_experience_analytics_app_health_application_performance_by_app_version)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails", self.user_experience_analytics_app_health_application_performance_by_app_version_details)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId", self.user_experience_analytics_app_health_application_performance_by_app_version_device_id)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion", self.user_experience_analytics_app_health_application_performance_by_o_s_version)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthDeviceModelPerformance", self.user_experience_analytics_app_health_device_model_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthDevicePerformance", self.user_experience_analytics_app_health_device_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthDevicePerformanceDetails", self.user_experience_analytics_app_health_device_performance_details)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthOSVersionPerformance", self.user_experience_analytics_app_health_o_s_version_performance)
        writer.write_object_value("userExperienceAnalyticsAppHealthOverview", self.user_experience_analytics_app_health_overview)
        writer.write_collection_of_object_values("userExperienceAnalyticsBaselines", self.user_experience_analytics_baselines)
        writer.write_collection_of_object_values("userExperienceAnalyticsBatteryHealthAppImpact", self.user_experience_analytics_battery_health_app_impact)
        writer.write_object_value("userExperienceAnalyticsBatteryHealthCapacityDetails", self.user_experience_analytics_battery_health_capacity_details)
        writer.write_collection_of_object_values("userExperienceAnalyticsBatteryHealthDeviceAppImpact", self.user_experience_analytics_battery_health_device_app_impact)
        writer.write_collection_of_object_values("userExperienceAnalyticsBatteryHealthDevicePerformance", self.user_experience_analytics_battery_health_device_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory", self.user_experience_analytics_battery_health_device_runtime_history)
        writer.write_collection_of_object_values("userExperienceAnalyticsBatteryHealthModelPerformance", self.user_experience_analytics_battery_health_model_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsBatteryHealthOsPerformance", self.user_experience_analytics_battery_health_os_performance)
        writer.write_object_value("userExperienceAnalyticsBatteryHealthRuntimeDetails", self.user_experience_analytics_battery_health_runtime_details)
        writer.write_collection_of_object_values("userExperienceAnalyticsCategories", self.user_experience_analytics_categories)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceMetricHistory", self.user_experience_analytics_device_metric_history)
        writer.write_collection_of_object_values("userExperienceAnalyticsDevicePerformance", self.user_experience_analytics_device_performance)
        writer.write_object_value("userExperienceAnalyticsDeviceScope", self.user_experience_analytics_device_scope)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceScopes", self.user_experience_analytics_device_scopes)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceScores", self.user_experience_analytics_device_scores)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceStartupHistory", self.user_experience_analytics_device_startup_history)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceStartupProcessPerformance", self.user_experience_analytics_device_startup_process_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceStartupProcesses", self.user_experience_analytics_device_startup_processes)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceTimelineEvent", self.user_experience_analytics_device_timeline_event)
        writer.write_collection_of_object_values("userExperienceAnalyticsDevicesWithoutCloudIdentity", self.user_experience_analytics_devices_without_cloud_identity)
        writer.write_collection_of_object_values("userExperienceAnalyticsImpactingProcess", self.user_experience_analytics_impacting_process)
        writer.write_collection_of_object_values("userExperienceAnalyticsMetricHistory", self.user_experience_analytics_metric_history)
        writer.write_collection_of_object_values("userExperienceAnalyticsModelScores", self.user_experience_analytics_model_scores)
        writer.write_collection_of_object_values("userExperienceAnalyticsNotAutopilotReadyDevice", self.user_experience_analytics_not_autopilot_ready_device)
        writer.write_object_value("userExperienceAnalyticsOverview", self.user_experience_analytics_overview)
        writer.write_collection_of_object_values("userExperienceAnalyticsRemoteConnection", self.user_experience_analytics_remote_connection)
        writer.write_collection_of_object_values("userExperienceAnalyticsResourcePerformance", self.user_experience_analytics_resource_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsScoreHistory", self.user_experience_analytics_score_history)
        writer.write_object_value("userExperienceAnalyticsSettings", self.user_experience_analytics_settings)
        writer.write_object_value("userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric", self.user_experience_analytics_work_from_anywhere_hardware_readiness_metric)
        writer.write_collection_of_object_values("userExperienceAnalyticsWorkFromAnywhereMetrics", self.user_experience_analytics_work_from_anywhere_metrics)
        writer.write_collection_of_object_values("userExperienceAnalyticsWorkFromAnywhereModelPerformance", self.user_experience_analytics_work_from_anywhere_model_performance)
        writer.write_collection_of_object_values("userPfxCertificates", self.user_pfx_certificates)
        writer.write_object_value("virtualEndpoint", self.virtual_endpoint)
        writer.write_collection_of_object_values("windowsAutopilotDeploymentProfiles", self.windows_autopilot_deployment_profiles)
        writer.write_collection_of_object_values("windowsAutopilotDeviceIdentities", self.windows_autopilot_device_identities)
        writer.write_object_value("windowsAutopilotSettings", self.windows_autopilot_settings)
        writer.write_collection_of_object_values("windowsDriverUpdateProfiles", self.windows_driver_update_profiles)
        writer.write_collection_of_object_values("windowsFeatureUpdateProfiles", self.windows_feature_update_profiles)
        writer.write_collection_of_object_values("windowsInformationProtectionAppLearningSummaries", self.windows_information_protection_app_learning_summaries)
        writer.write_collection_of_object_values("windowsInformationProtectionNetworkLearningSummaries", self.windows_information_protection_network_learning_summaries)
        writer.write_collection_of_object_values("windowsMalwareInformation", self.windows_malware_information)
        writer.write_object_value("windowsMalwareOverview", self.windows_malware_overview)
        writer.write_collection_of_object_values("windowsQualityUpdateProfiles", self.windows_quality_update_profiles)
        writer.write_collection_of_object_values("windowsUpdateCatalogItems", self.windows_update_catalog_items)
        writer.write_collection_of_object_values("zebraFotaArtifacts", self.zebra_fota_artifacts)
        writer.write_object_value("zebraFotaConnector", self.zebra_fota_connector)
        writer.write_collection_of_object_values("zebraFotaDeployments", self.zebra_fota_deployments)
    

