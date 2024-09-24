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
    from ..models.device_management.device_management import DeviceManagement
    from ..models.o_data_errors.o_data_error import ODataError
    from .advanced_threat_protection_onboarding_state_summary.advanced_threat_protection_onboarding_state_summary_request_builder import AdvancedThreatProtectionOnboardingStateSummaryRequestBuilder
    from .android_device_owner_enrollment_profiles.android_device_owner_enrollment_profiles_request_builder import AndroidDeviceOwnerEnrollmentProfilesRequestBuilder
    from .android_for_work_app_configuration_schemas.android_for_work_app_configuration_schemas_request_builder import AndroidForWorkAppConfigurationSchemasRequestBuilder
    from .android_for_work_enrollment_profiles.android_for_work_enrollment_profiles_request_builder import AndroidForWorkEnrollmentProfilesRequestBuilder
    from .android_for_work_settings.android_for_work_settings_request_builder import AndroidForWorkSettingsRequestBuilder
    from .android_managed_store_account_enterprise_settings.android_managed_store_account_enterprise_settings_request_builder import AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder
    from .android_managed_store_app_configuration_schemas.android_managed_store_app_configuration_schemas_request_builder import AndroidManagedStoreAppConfigurationSchemasRequestBuilder
    from .apple_push_notification_certificate.apple_push_notification_certificate_request_builder import ApplePushNotificationCertificateRequestBuilder
    from .apple_user_initiated_enrollment_profiles.apple_user_initiated_enrollment_profiles_request_builder import AppleUserInitiatedEnrollmentProfilesRequestBuilder
    from .assignment_filters.assignment_filters_request_builder import AssignmentFiltersRequestBuilder
    from .audit_events.audit_events_request_builder import AuditEventsRequestBuilder
    from .autopilot_events.autopilot_events_request_builder import AutopilotEventsRequestBuilder
    from .cart_to_class_associations.cart_to_class_associations_request_builder import CartToClassAssociationsRequestBuilder
    from .categories.categories_request_builder import CategoriesRequestBuilder
    from .certificate_connector_details.certificate_connector_details_request_builder import CertificateConnectorDetailsRequestBuilder
    from .chrome_o_s_onboarding_settings.chrome_o_s_onboarding_settings_request_builder import ChromeOSOnboardingSettingsRequestBuilder
    from .cloud_p_c_connectivity_issues.cloud_p_c_connectivity_issues_request_builder import CloudPCConnectivityIssuesRequestBuilder
    from .comanaged_devices.comanaged_devices_request_builder import ComanagedDevicesRequestBuilder
    from .comanagement_eligible_devices.comanagement_eligible_devices_request_builder import ComanagementEligibleDevicesRequestBuilder
    from .compliance_categories.compliance_categories_request_builder import ComplianceCategoriesRequestBuilder
    from .compliance_management_partners.compliance_management_partners_request_builder import ComplianceManagementPartnersRequestBuilder
    from .compliance_policies.compliance_policies_request_builder import CompliancePoliciesRequestBuilder
    from .compliance_settings.compliance_settings_request_builder import ComplianceSettingsRequestBuilder
    from .conditional_access_settings.conditional_access_settings_request_builder import ConditionalAccessSettingsRequestBuilder
    from .configuration_categories.configuration_categories_request_builder import ConfigurationCategoriesRequestBuilder
    from .configuration_policies.configuration_policies_request_builder import ConfigurationPoliciesRequestBuilder
    from .configuration_policy_templates.configuration_policy_templates_request_builder import ConfigurationPolicyTemplatesRequestBuilder
    from .configuration_settings.configuration_settings_request_builder import ConfigurationSettingsRequestBuilder
    from .config_manager_collections.config_manager_collections_request_builder import ConfigManagerCollectionsRequestBuilder
    from .data_sharing_consents.data_sharing_consents_request_builder import DataSharingConsentsRequestBuilder
    from .dep_onboarding_settings.dep_onboarding_settings_request_builder import DepOnboardingSettingsRequestBuilder
    from .derived_credentials.derived_credentials_request_builder import DerivedCredentialsRequestBuilder
    from .detected_apps.detected_apps_request_builder import DetectedAppsRequestBuilder
    from .device_categories.device_categories_request_builder import DeviceCategoriesRequestBuilder
    from .device_compliance_policies.device_compliance_policies_request_builder import DeviceCompliancePoliciesRequestBuilder
    from .device_compliance_policy_device_state_summary.device_compliance_policy_device_state_summary_request_builder import DeviceCompliancePolicyDeviceStateSummaryRequestBuilder
    from .device_compliance_policy_setting_state_summaries.device_compliance_policy_setting_state_summaries_request_builder import DeviceCompliancePolicySettingStateSummariesRequestBuilder
    from .device_compliance_scripts.device_compliance_scripts_request_builder import DeviceComplianceScriptsRequestBuilder
    from .device_configurations.device_configurations_request_builder import DeviceConfigurationsRequestBuilder
    from .device_configurations_all_managed_device_certificate_states.device_configurations_all_managed_device_certificate_states_request_builder import DeviceConfigurationsAllManagedDeviceCertificateStatesRequestBuilder
    from .device_configuration_conflict_summary.device_configuration_conflict_summary_request_builder import DeviceConfigurationConflictSummaryRequestBuilder
    from .device_configuration_device_state_summaries.device_configuration_device_state_summaries_request_builder import DeviceConfigurationDeviceStateSummariesRequestBuilder
    from .device_configuration_profiles.device_configuration_profiles_request_builder import DeviceConfigurationProfilesRequestBuilder
    from .device_configuration_restricted_apps_violations.device_configuration_restricted_apps_violations_request_builder import DeviceConfigurationRestrictedAppsViolationsRequestBuilder
    from .device_configuration_user_state_summaries.device_configuration_user_state_summaries_request_builder import DeviceConfigurationUserStateSummariesRequestBuilder
    from .device_custom_attribute_shell_scripts.device_custom_attribute_shell_scripts_request_builder import DeviceCustomAttributeShellScriptsRequestBuilder
    from .device_enrollment_configurations.device_enrollment_configurations_request_builder import DeviceEnrollmentConfigurationsRequestBuilder
    from .device_health_scripts.device_health_scripts_request_builder import DeviceHealthScriptsRequestBuilder
    from .device_management_partners.device_management_partners_request_builder import DeviceManagementPartnersRequestBuilder
    from .device_management_scripts.device_management_scripts_request_builder import DeviceManagementScriptsRequestBuilder
    from .device_shell_scripts.device_shell_scripts_request_builder import DeviceShellScriptsRequestBuilder
    from .domain_join_connectors.domain_join_connectors_request_builder import DomainJoinConnectorsRequestBuilder
    from .elevation_requests.elevation_requests_request_builder import ElevationRequestsRequestBuilder
    from .embedded_s_i_m_activation_code_pools.embedded_s_i_m_activation_code_pools_request_builder import EmbeddedSIMActivationCodePoolsRequestBuilder
    from .enable_android_device_administrator_enrollment.enable_android_device_administrator_enrollment_request_builder import EnableAndroidDeviceAdministratorEnrollmentRequestBuilder
    from .enable_endpoint_privilege_management.enable_endpoint_privilege_management_request_builder import EnableEndpointPrivilegeManagementRequestBuilder
    from .enable_legacy_pc_management.enable_legacy_pc_management_request_builder import EnableLegacyPcManagementRequestBuilder
    from .enable_unlicensed_adminstrators.enable_unlicensed_adminstrators_request_builder import EnableUnlicensedAdminstratorsRequestBuilder
    from .endpoint_privilege_management_provisioning_status.endpoint_privilege_management_provisioning_status_request_builder import EndpointPrivilegeManagementProvisioningStatusRequestBuilder
    from .evaluate_assignment_filter.evaluate_assignment_filter_request_builder import EvaluateAssignmentFilterRequestBuilder
    from .exchange_connectors.exchange_connectors_request_builder import ExchangeConnectorsRequestBuilder
    from .exchange_on_premises_policies.exchange_on_premises_policies_request_builder import ExchangeOnPremisesPoliciesRequestBuilder
    from .exchange_on_premises_policy.exchange_on_premises_policy_request_builder import ExchangeOnPremisesPolicyRequestBuilder
    from .get_assigned_role_details.get_assigned_role_details_request_builder import GetAssignedRoleDetailsRequestBuilder
    from .get_assignment_filters_status_details.get_assignment_filters_status_details_request_builder import GetAssignmentFiltersStatusDetailsRequestBuilder
    from .get_comanaged_devices_summary.get_comanaged_devices_summary_request_builder import GetComanagedDevicesSummaryRequestBuilder
    from .get_comanagement_eligible_devices_summary.get_comanagement_eligible_devices_summary_request_builder import GetComanagementEligibleDevicesSummaryRequestBuilder
    from .get_effective_permissions.get_effective_permissions_request_builder import GetEffectivePermissionsRequestBuilder
    from .get_effective_permissions_with_scope.get_effective_permissions_with_scope_request_builder import GetEffectivePermissionsWithScopeRequestBuilder
    from .get_role_scope_tags_by_ids_with_ids.get_role_scope_tags_by_ids_with_ids_request_builder import GetRoleScopeTagsByIdsWithIdsRequestBuilder
    from .get_role_scope_tags_by_resource_with_resource.get_role_scope_tags_by_resource_with_resource_request_builder import GetRoleScopeTagsByResourceWithResourceRequestBuilder
    from .get_suggested_enrollment_limit_with_enrollment_type.get_suggested_enrollment_limit_with_enrollment_type_request_builder import GetSuggestedEnrollmentLimitWithEnrollmentTypeRequestBuilder
    from .group_policy_categories.group_policy_categories_request_builder import GroupPolicyCategoriesRequestBuilder
    from .group_policy_configurations.group_policy_configurations_request_builder import GroupPolicyConfigurationsRequestBuilder
    from .group_policy_definitions.group_policy_definitions_request_builder import GroupPolicyDefinitionsRequestBuilder
    from .group_policy_definition_files.group_policy_definition_files_request_builder import GroupPolicyDefinitionFilesRequestBuilder
    from .group_policy_migration_reports.group_policy_migration_reports_request_builder import GroupPolicyMigrationReportsRequestBuilder
    from .group_policy_object_files.group_policy_object_files_request_builder import GroupPolicyObjectFilesRequestBuilder
    from .group_policy_uploaded_definition_files.group_policy_uploaded_definition_files_request_builder import GroupPolicyUploadedDefinitionFilesRequestBuilder
    from .hardware_configurations.hardware_configurations_request_builder import HardwareConfigurationsRequestBuilder
    from .hardware_password_details.hardware_password_details_request_builder import HardwarePasswordDetailsRequestBuilder
    from .hardware_password_info.hardware_password_info_request_builder import HardwarePasswordInfoRequestBuilder
    from .imported_device_identities.imported_device_identities_request_builder import ImportedDeviceIdentitiesRequestBuilder
    from .imported_windows_autopilot_device_identities.imported_windows_autopilot_device_identities_request_builder import ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder
    from .intents.intents_request_builder import IntentsRequestBuilder
    from .intune_branding_profiles.intune_branding_profiles_request_builder import IntuneBrandingProfilesRequestBuilder
    from .ios_update_statuses.ios_update_statuses_request_builder import IosUpdateStatusesRequestBuilder
    from .mac_o_s_software_update_account_summaries.mac_o_s_software_update_account_summaries_request_builder import MacOSSoftwareUpdateAccountSummariesRequestBuilder
    from .managed_devices.managed_devices_request_builder import ManagedDevicesRequestBuilder
    from .managed_device_cleanup_rules.managed_device_cleanup_rules_request_builder import ManagedDeviceCleanupRulesRequestBuilder
    from .managed_device_encryption_states.managed_device_encryption_states_request_builder import ManagedDeviceEncryptionStatesRequestBuilder
    from .managed_device_overview.managed_device_overview_request_builder import ManagedDeviceOverviewRequestBuilder
    from .managed_device_windows_o_s_images.managed_device_windows_o_s_images_request_builder import ManagedDeviceWindowsOSImagesRequestBuilder
    from .microsoft_tunnel_configurations.microsoft_tunnel_configurations_request_builder import MicrosoftTunnelConfigurationsRequestBuilder
    from .microsoft_tunnel_health_thresholds.microsoft_tunnel_health_thresholds_request_builder import MicrosoftTunnelHealthThresholdsRequestBuilder
    from .microsoft_tunnel_server_log_collection_responses.microsoft_tunnel_server_log_collection_responses_request_builder import MicrosoftTunnelServerLogCollectionResponsesRequestBuilder
    from .microsoft_tunnel_sites.microsoft_tunnel_sites_request_builder import MicrosoftTunnelSitesRequestBuilder
    from .mobile_app_troubleshooting_events.mobile_app_troubleshooting_events_request_builder import MobileAppTroubleshootingEventsRequestBuilder
    from .mobile_threat_defense_connectors.mobile_threat_defense_connectors_request_builder import MobileThreatDefenseConnectorsRequestBuilder
    from .monitoring.monitoring_request_builder import MonitoringRequestBuilder
    from .ndes_connectors.ndes_connectors_request_builder import NdesConnectorsRequestBuilder
    from .notification_message_templates.notification_message_templates_request_builder import NotificationMessageTemplatesRequestBuilder
    from .operation_approval_policies.operation_approval_policies_request_builder import OperationApprovalPoliciesRequestBuilder
    from .operation_approval_requests.operation_approval_requests_request_builder import OperationApprovalRequestsRequestBuilder
    from .privilege_management_elevations.privilege_management_elevations_request_builder import PrivilegeManagementElevationsRequestBuilder
    from .remote_action_audits.remote_action_audits_request_builder import RemoteActionAuditsRequestBuilder
    from .remote_assistance_partners.remote_assistance_partners_request_builder import RemoteAssistancePartnersRequestBuilder
    from .remote_assistance_settings.remote_assistance_settings_request_builder import RemoteAssistanceSettingsRequestBuilder
    from .reports.reports_request_builder import ReportsRequestBuilder
    from .resource_access_profiles.resource_access_profiles_request_builder import ResourceAccessProfilesRequestBuilder
    from .resource_operations.resource_operations_request_builder import ResourceOperationsRequestBuilder
    from .reusable_policy_settings.reusable_policy_settings_request_builder import ReusablePolicySettingsRequestBuilder
    from .reusable_settings.reusable_settings_request_builder import ReusableSettingsRequestBuilder
    from .role_assignments.role_assignments_request_builder import RoleAssignmentsRequestBuilder
    from .role_definitions.role_definitions_request_builder import RoleDefinitionsRequestBuilder
    from .role_scope_tags.role_scope_tags_request_builder import RoleScopeTagsRequestBuilder
    from .scoped_for_resource_with_resource.scoped_for_resource_with_resource_request_builder import ScopedForResourceWithResourceRequestBuilder
    from .send_custom_notification_to_company_portal.send_custom_notification_to_company_portal_request_builder import SendCustomNotificationToCompanyPortalRequestBuilder
    from .service_now_connections.service_now_connections_request_builder import ServiceNowConnectionsRequestBuilder
    from .setting_definitions.setting_definitions_request_builder import SettingDefinitionsRequestBuilder
    from .software_update_status_summary.software_update_status_summary_request_builder import SoftwareUpdateStatusSummaryRequestBuilder
    from .telecom_expense_management_partners.telecom_expense_management_partners_request_builder import TelecomExpenseManagementPartnersRequestBuilder
    from .templates.templates_request_builder import TemplatesRequestBuilder
    from .template_insights.template_insights_request_builder import TemplateInsightsRequestBuilder
    from .template_settings.template_settings_request_builder import TemplateSettingsRequestBuilder
    from .tenant_attach_r_b_a_c.tenant_attach_r_b_a_c_request_builder import TenantAttachRBACRequestBuilder
    from .terms_and_conditions.terms_and_conditions_request_builder import TermsAndConditionsRequestBuilder
    from .troubleshooting_events.troubleshooting_events_request_builder import TroubleshootingEventsRequestBuilder
    from .user_experience_analytics_anomaly.user_experience_analytics_anomaly_request_builder import UserExperienceAnalyticsAnomalyRequestBuilder
    from .user_experience_analytics_anomaly_correlation_group_overview.user_experience_analytics_anomaly_correlation_group_overview_request_builder import UserExperienceAnalyticsAnomalyCorrelationGroupOverviewRequestBuilder
    from .user_experience_analytics_anomaly_device.user_experience_analytics_anomaly_device_request_builder import UserExperienceAnalyticsAnomalyDeviceRequestBuilder
    from .user_experience_analytics_app_health_application_performance.user_experience_analytics_app_health_application_performance_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceRequestBuilder
    from .user_experience_analytics_app_health_application_performance_by_app_version.user_experience_analytics_app_health_application_performance_by_app_version_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionRequestBuilder
    from .user_experience_analytics_app_health_application_performance_by_app_version_details.user_experience_analytics_app_health_application_performance_by_app_version_details_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilder
    from .user_experience_analytics_app_health_application_performance_by_app_version_device_id.user_experience_analytics_app_health_application_performance_by_app_version_device_id_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequestBuilder
    from .user_experience_analytics_app_health_application_performance_by_o_s_version.user_experience_analytics_app_health_application_performance_by_o_s_version_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequestBuilder
    from .user_experience_analytics_app_health_device_model_performance.user_experience_analytics_app_health_device_model_performance_request_builder import UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequestBuilder
    from .user_experience_analytics_app_health_device_performance.user_experience_analytics_app_health_device_performance_request_builder import UserExperienceAnalyticsAppHealthDevicePerformanceRequestBuilder
    from .user_experience_analytics_app_health_device_performance_details.user_experience_analytics_app_health_device_performance_details_request_builder import UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequestBuilder
    from .user_experience_analytics_app_health_overview.user_experience_analytics_app_health_overview_request_builder import UserExperienceAnalyticsAppHealthOverviewRequestBuilder
    from .user_experience_analytics_app_health_o_s_version_performance.user_experience_analytics_app_health_o_s_version_performance_request_builder import UserExperienceAnalyticsAppHealthOSVersionPerformanceRequestBuilder
    from .user_experience_analytics_baselines.user_experience_analytics_baselines_request_builder import UserExperienceAnalyticsBaselinesRequestBuilder
    from .user_experience_analytics_battery_health_app_impact.user_experience_analytics_battery_health_app_impact_request_builder import UserExperienceAnalyticsBatteryHealthAppImpactRequestBuilder
    from .user_experience_analytics_battery_health_capacity_details.user_experience_analytics_battery_health_capacity_details_request_builder import UserExperienceAnalyticsBatteryHealthCapacityDetailsRequestBuilder
    from .user_experience_analytics_battery_health_device_app_impact.user_experience_analytics_battery_health_device_app_impact_request_builder import UserExperienceAnalyticsBatteryHealthDeviceAppImpactRequestBuilder
    from .user_experience_analytics_battery_health_device_performance.user_experience_analytics_battery_health_device_performance_request_builder import UserExperienceAnalyticsBatteryHealthDevicePerformanceRequestBuilder
    from .user_experience_analytics_battery_health_device_runtime_history.user_experience_analytics_battery_health_device_runtime_history_request_builder import UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistoryRequestBuilder
    from .user_experience_analytics_battery_health_model_performance.user_experience_analytics_battery_health_model_performance_request_builder import UserExperienceAnalyticsBatteryHealthModelPerformanceRequestBuilder
    from .user_experience_analytics_battery_health_os_performance.user_experience_analytics_battery_health_os_performance_request_builder import UserExperienceAnalyticsBatteryHealthOsPerformanceRequestBuilder
    from .user_experience_analytics_battery_health_runtime_details.user_experience_analytics_battery_health_runtime_details_request_builder import UserExperienceAnalyticsBatteryHealthRuntimeDetailsRequestBuilder
    from .user_experience_analytics_categories.user_experience_analytics_categories_request_builder import UserExperienceAnalyticsCategoriesRequestBuilder
    from .user_experience_analytics_devices_without_cloud_identity.user_experience_analytics_devices_without_cloud_identity_request_builder import UserExperienceAnalyticsDevicesWithoutCloudIdentityRequestBuilder
    from .user_experience_analytics_device_metric_history.user_experience_analytics_device_metric_history_request_builder import UserExperienceAnalyticsDeviceMetricHistoryRequestBuilder
    from .user_experience_analytics_device_performance.user_experience_analytics_device_performance_request_builder import UserExperienceAnalyticsDevicePerformanceRequestBuilder
    from .user_experience_analytics_device_scope.user_experience_analytics_device_scope_request_builder import UserExperienceAnalyticsDeviceScopeRequestBuilder
    from .user_experience_analytics_device_scopes.user_experience_analytics_device_scopes_request_builder import UserExperienceAnalyticsDeviceScopesRequestBuilder
    from .user_experience_analytics_device_scores.user_experience_analytics_device_scores_request_builder import UserExperienceAnalyticsDeviceScoresRequestBuilder
    from .user_experience_analytics_device_startup_history.user_experience_analytics_device_startup_history_request_builder import UserExperienceAnalyticsDeviceStartupHistoryRequestBuilder
    from .user_experience_analytics_device_startup_processes.user_experience_analytics_device_startup_processes_request_builder import UserExperienceAnalyticsDeviceStartupProcessesRequestBuilder
    from .user_experience_analytics_device_startup_process_performance.user_experience_analytics_device_startup_process_performance_request_builder import UserExperienceAnalyticsDeviceStartupProcessPerformanceRequestBuilder
    from .user_experience_analytics_device_timeline_event.user_experience_analytics_device_timeline_event_request_builder import UserExperienceAnalyticsDeviceTimelineEventRequestBuilder
    from .user_experience_analytics_impacting_process.user_experience_analytics_impacting_process_request_builder import UserExperienceAnalyticsImpactingProcessRequestBuilder
    from .user_experience_analytics_metric_history.user_experience_analytics_metric_history_request_builder import UserExperienceAnalyticsMetricHistoryRequestBuilder
    from .user_experience_analytics_model_scores.user_experience_analytics_model_scores_request_builder import UserExperienceAnalyticsModelScoresRequestBuilder
    from .user_experience_analytics_not_autopilot_ready_device.user_experience_analytics_not_autopilot_ready_device_request_builder import UserExperienceAnalyticsNotAutopilotReadyDeviceRequestBuilder
    from .user_experience_analytics_overview.user_experience_analytics_overview_request_builder import UserExperienceAnalyticsOverviewRequestBuilder
    from .user_experience_analytics_remote_connection.user_experience_analytics_remote_connection_request_builder import UserExperienceAnalyticsRemoteConnectionRequestBuilder
    from .user_experience_analytics_resource_performance.user_experience_analytics_resource_performance_request_builder import UserExperienceAnalyticsResourcePerformanceRequestBuilder
    from .user_experience_analytics_score_history.user_experience_analytics_score_history_request_builder import UserExperienceAnalyticsScoreHistoryRequestBuilder
    from .user_experience_analytics_summarized_device_scopes.user_experience_analytics_summarized_device_scopes_request_builder import UserExperienceAnalyticsSummarizedDeviceScopesRequestBuilder
    from .user_experience_analytics_summarize_work_from_anywhere_devices.user_experience_analytics_summarize_work_from_anywhere_devices_request_builder import UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequestBuilder
    from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric.user_experience_analytics_work_from_anywhere_hardware_readiness_metric_request_builder import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequestBuilder
    from .user_experience_analytics_work_from_anywhere_metrics.user_experience_analytics_work_from_anywhere_metrics_request_builder import UserExperienceAnalyticsWorkFromAnywhereMetricsRequestBuilder
    from .user_experience_analytics_work_from_anywhere_model_performance.user_experience_analytics_work_from_anywhere_model_performance_request_builder import UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequestBuilder
    from .user_pfx_certificates.user_pfx_certificates_request_builder import UserPfxCertificatesRequestBuilder
    from .verify_windows_enrollment_auto_discovery_with_domain_name.verify_windows_enrollment_auto_discovery_with_domain_name_request_builder import VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder
    from .virtual_endpoint.virtual_endpoint_request_builder import VirtualEndpointRequestBuilder
    from .windows_autopilot_deployment_profiles.windows_autopilot_deployment_profiles_request_builder import WindowsAutopilotDeploymentProfilesRequestBuilder
    from .windows_autopilot_device_identities.windows_autopilot_device_identities_request_builder import WindowsAutopilotDeviceIdentitiesRequestBuilder
    from .windows_autopilot_settings.windows_autopilot_settings_request_builder import WindowsAutopilotSettingsRequestBuilder
    from .windows_driver_update_profiles.windows_driver_update_profiles_request_builder import WindowsDriverUpdateProfilesRequestBuilder
    from .windows_feature_update_profiles.windows_feature_update_profiles_request_builder import WindowsFeatureUpdateProfilesRequestBuilder
    from .windows_information_protection_app_learning_summaries.windows_information_protection_app_learning_summaries_request_builder import WindowsInformationProtectionAppLearningSummariesRequestBuilder
    from .windows_information_protection_network_learning_summaries.windows_information_protection_network_learning_summaries_request_builder import WindowsInformationProtectionNetworkLearningSummariesRequestBuilder
    from .windows_malware_information.windows_malware_information_request_builder import WindowsMalwareInformationRequestBuilder
    from .windows_quality_update_policies.windows_quality_update_policies_request_builder import WindowsQualityUpdatePoliciesRequestBuilder
    from .windows_quality_update_profiles.windows_quality_update_profiles_request_builder import WindowsQualityUpdateProfilesRequestBuilder
    from .windows_update_catalog_items.windows_update_catalog_items_request_builder import WindowsUpdateCatalogItemsRequestBuilder
    from .zebra_fota_artifacts.zebra_fota_artifacts_request_builder import ZebraFotaArtifactsRequestBuilder
    from .zebra_fota_connector.zebra_fota_connector_request_builder import ZebraFotaConnectorRequestBuilder
    from .zebra_fota_deployments.zebra_fota_deployments_request_builder import ZebraFotaDeploymentsRequestBuilder

class DeviceManagementRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the deviceManagement singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new DeviceManagementRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DeviceManagementRequestBuilderGetQueryParameters]] = None) -> Optional[DeviceManagement]:
        """
        Get deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagement]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.device_management.device_management import DeviceManagement

        return await self.request_adapter.send_async(request_info, DeviceManagement, error_mapping)
    
    def get_effective_permissions_with_scope(self,scope: str) -> GetEffectivePermissionsWithScopeRequestBuilder:
        """
        Provides operations to call the getEffectivePermissions method.
        param scope: Usage: scope='{scope}'
        Returns: GetEffectivePermissionsWithScopeRequestBuilder
        """
        if scope is None:
            raise TypeError("scope cannot be null.")
        from .get_effective_permissions_with_scope.get_effective_permissions_with_scope_request_builder import GetEffectivePermissionsWithScopeRequestBuilder

        return GetEffectivePermissionsWithScopeRequestBuilder(self.request_adapter, self.path_parameters, scope)
    
    def get_role_scope_tags_by_ids_with_ids(self,ids: str) -> GetRoleScopeTagsByIdsWithIdsRequestBuilder:
        """
        Provides operations to call the getRoleScopeTagsByIds method.
        param ids: Usage: ids={ids}
        Returns: GetRoleScopeTagsByIdsWithIdsRequestBuilder
        """
        if ids is None:
            raise TypeError("ids cannot be null.")
        from .get_role_scope_tags_by_ids_with_ids.get_role_scope_tags_by_ids_with_ids_request_builder import GetRoleScopeTagsByIdsWithIdsRequestBuilder

        return GetRoleScopeTagsByIdsWithIdsRequestBuilder(self.request_adapter, self.path_parameters, ids)
    
    def get_role_scope_tags_by_resource_with_resource(self,resource: str) -> GetRoleScopeTagsByResourceWithResourceRequestBuilder:
        """
        Provides operations to call the getRoleScopeTagsByResource method.
        param resource: Usage: resource='{resource}'
        Returns: GetRoleScopeTagsByResourceWithResourceRequestBuilder
        """
        if resource is None:
            raise TypeError("resource cannot be null.")
        from .get_role_scope_tags_by_resource_with_resource.get_role_scope_tags_by_resource_with_resource_request_builder import GetRoleScopeTagsByResourceWithResourceRequestBuilder

        return GetRoleScopeTagsByResourceWithResourceRequestBuilder(self.request_adapter, self.path_parameters, resource)
    
    def get_suggested_enrollment_limit_with_enrollment_type(self,enrollment_type: str) -> GetSuggestedEnrollmentLimitWithEnrollmentTypeRequestBuilder:
        """
        Provides operations to call the getSuggestedEnrollmentLimit method.
        param enrollment_type: Usage: enrollmentType='{enrollmentType}'
        Returns: GetSuggestedEnrollmentLimitWithEnrollmentTypeRequestBuilder
        """
        if enrollment_type is None:
            raise TypeError("enrollment_type cannot be null.")
        from .get_suggested_enrollment_limit_with_enrollment_type.get_suggested_enrollment_limit_with_enrollment_type_request_builder import GetSuggestedEnrollmentLimitWithEnrollmentTypeRequestBuilder

        return GetSuggestedEnrollmentLimitWithEnrollmentTypeRequestBuilder(self.request_adapter, self.path_parameters, enrollment_type)
    
    async def patch(self,body: DeviceManagement, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeviceManagement]:
        """
        Update deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagement]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.device_management.device_management import DeviceManagement

        return await self.request_adapter.send_async(request_info, DeviceManagement, error_mapping)
    
    def scoped_for_resource_with_resource(self,resource: str) -> ScopedForResourceWithResourceRequestBuilder:
        """
        Provides operations to call the scopedForResource method.
        param resource: Usage: resource='{resource}'
        Returns: ScopedForResourceWithResourceRequestBuilder
        """
        if resource is None:
            raise TypeError("resource cannot be null.")
        from .scoped_for_resource_with_resource.scoped_for_resource_with_resource_request_builder import ScopedForResourceWithResourceRequestBuilder

        return ScopedForResourceWithResourceRequestBuilder(self.request_adapter, self.path_parameters, resource)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DeviceManagementRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DeviceManagement, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update deviceManagement
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
    
    def verify_windows_enrollment_auto_discovery_with_domain_name(self,domain_name: str) -> VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder:
        """
        Provides operations to call the verifyWindowsEnrollmentAutoDiscovery method.
        param domain_name: Usage: domainName='{domainName}'
        Returns: VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder
        """
        if domain_name is None:
            raise TypeError("domain_name cannot be null.")
        from .verify_windows_enrollment_auto_discovery_with_domain_name.verify_windows_enrollment_auto_discovery_with_domain_name_request_builder import VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder

        return VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder(self.request_adapter, self.path_parameters, domain_name)
    
    def with_url(self,raw_url: str) -> DeviceManagementRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeviceManagementRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DeviceManagementRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def advanced_threat_protection_onboarding_state_summary(self) -> AdvancedThreatProtectionOnboardingStateSummaryRequestBuilder:
        """
        Provides operations to manage the advancedThreatProtectionOnboardingStateSummary property of the microsoft.graph.deviceManagement entity.
        """
        from .advanced_threat_protection_onboarding_state_summary.advanced_threat_protection_onboarding_state_summary_request_builder import AdvancedThreatProtectionOnboardingStateSummaryRequestBuilder

        return AdvancedThreatProtectionOnboardingStateSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def android_device_owner_enrollment_profiles(self) -> AndroidDeviceOwnerEnrollmentProfilesRequestBuilder:
        """
        Provides operations to manage the androidDeviceOwnerEnrollmentProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .android_device_owner_enrollment_profiles.android_device_owner_enrollment_profiles_request_builder import AndroidDeviceOwnerEnrollmentProfilesRequestBuilder

        return AndroidDeviceOwnerEnrollmentProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def android_for_work_app_configuration_schemas(self) -> AndroidForWorkAppConfigurationSchemasRequestBuilder:
        """
        Provides operations to manage the androidForWorkAppConfigurationSchemas property of the microsoft.graph.deviceManagement entity.
        """
        from .android_for_work_app_configuration_schemas.android_for_work_app_configuration_schemas_request_builder import AndroidForWorkAppConfigurationSchemasRequestBuilder

        return AndroidForWorkAppConfigurationSchemasRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def android_for_work_enrollment_profiles(self) -> AndroidForWorkEnrollmentProfilesRequestBuilder:
        """
        Provides operations to manage the androidForWorkEnrollmentProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .android_for_work_enrollment_profiles.android_for_work_enrollment_profiles_request_builder import AndroidForWorkEnrollmentProfilesRequestBuilder

        return AndroidForWorkEnrollmentProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def android_for_work_settings(self) -> AndroidForWorkSettingsRequestBuilder:
        """
        Provides operations to manage the androidForWorkSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .android_for_work_settings.android_for_work_settings_request_builder import AndroidForWorkSettingsRequestBuilder

        return AndroidForWorkSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def android_managed_store_account_enterprise_settings(self) -> AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder:
        """
        Provides operations to manage the androidManagedStoreAccountEnterpriseSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .android_managed_store_account_enterprise_settings.android_managed_store_account_enterprise_settings_request_builder import AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder

        return AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def android_managed_store_app_configuration_schemas(self) -> AndroidManagedStoreAppConfigurationSchemasRequestBuilder:
        """
        Provides operations to manage the androidManagedStoreAppConfigurationSchemas property of the microsoft.graph.deviceManagement entity.
        """
        from .android_managed_store_app_configuration_schemas.android_managed_store_app_configuration_schemas_request_builder import AndroidManagedStoreAppConfigurationSchemasRequestBuilder

        return AndroidManagedStoreAppConfigurationSchemasRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apple_push_notification_certificate(self) -> ApplePushNotificationCertificateRequestBuilder:
        """
        Provides operations to manage the applePushNotificationCertificate property of the microsoft.graph.deviceManagement entity.
        """
        from .apple_push_notification_certificate.apple_push_notification_certificate_request_builder import ApplePushNotificationCertificateRequestBuilder

        return ApplePushNotificationCertificateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apple_user_initiated_enrollment_profiles(self) -> AppleUserInitiatedEnrollmentProfilesRequestBuilder:
        """
        Provides operations to manage the appleUserInitiatedEnrollmentProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .apple_user_initiated_enrollment_profiles.apple_user_initiated_enrollment_profiles_request_builder import AppleUserInitiatedEnrollmentProfilesRequestBuilder

        return AppleUserInitiatedEnrollmentProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_filters(self) -> AssignmentFiltersRequestBuilder:
        """
        Provides operations to manage the assignmentFilters property of the microsoft.graph.deviceManagement entity.
        """
        from .assignment_filters.assignment_filters_request_builder import AssignmentFiltersRequestBuilder

        return AssignmentFiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def audit_events(self) -> AuditEventsRequestBuilder:
        """
        Provides operations to manage the auditEvents property of the microsoft.graph.deviceManagement entity.
        """
        from .audit_events.audit_events_request_builder import AuditEventsRequestBuilder

        return AuditEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def autopilot_events(self) -> AutopilotEventsRequestBuilder:
        """
        Provides operations to manage the autopilotEvents property of the microsoft.graph.deviceManagement entity.
        """
        from .autopilot_events.autopilot_events_request_builder import AutopilotEventsRequestBuilder

        return AutopilotEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cart_to_class_associations(self) -> CartToClassAssociationsRequestBuilder:
        """
        Provides operations to manage the cartToClassAssociations property of the microsoft.graph.deviceManagement entity.
        """
        from .cart_to_class_associations.cart_to_class_associations_request_builder import CartToClassAssociationsRequestBuilder

        return CartToClassAssociationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def categories(self) -> CategoriesRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.deviceManagement entity.
        """
        from .categories.categories_request_builder import CategoriesRequestBuilder

        return CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def certificate_connector_details(self) -> CertificateConnectorDetailsRequestBuilder:
        """
        Provides operations to manage the certificateConnectorDetails property of the microsoft.graph.deviceManagement entity.
        """
        from .certificate_connector_details.certificate_connector_details_request_builder import CertificateConnectorDetailsRequestBuilder

        return CertificateConnectorDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chrome_o_s_onboarding_settings(self) -> ChromeOSOnboardingSettingsRequestBuilder:
        """
        Provides operations to manage the chromeOSOnboardingSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .chrome_o_s_onboarding_settings.chrome_o_s_onboarding_settings_request_builder import ChromeOSOnboardingSettingsRequestBuilder

        return ChromeOSOnboardingSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_p_c_connectivity_issues(self) -> CloudPCConnectivityIssuesRequestBuilder:
        """
        Provides operations to manage the cloudPCConnectivityIssues property of the microsoft.graph.deviceManagement entity.
        """
        from .cloud_p_c_connectivity_issues.cloud_p_c_connectivity_issues_request_builder import CloudPCConnectivityIssuesRequestBuilder

        return CloudPCConnectivityIssuesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def comanaged_devices(self) -> ComanagedDevicesRequestBuilder:
        """
        Provides operations to manage the comanagedDevices property of the microsoft.graph.deviceManagement entity.
        """
        from .comanaged_devices.comanaged_devices_request_builder import ComanagedDevicesRequestBuilder

        return ComanagedDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def comanagement_eligible_devices(self) -> ComanagementEligibleDevicesRequestBuilder:
        """
        Provides operations to manage the comanagementEligibleDevices property of the microsoft.graph.deviceManagement entity.
        """
        from .comanagement_eligible_devices.comanagement_eligible_devices_request_builder import ComanagementEligibleDevicesRequestBuilder

        return ComanagementEligibleDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance_categories(self) -> ComplianceCategoriesRequestBuilder:
        """
        Provides operations to manage the complianceCategories property of the microsoft.graph.deviceManagement entity.
        """
        from .compliance_categories.compliance_categories_request_builder import ComplianceCategoriesRequestBuilder

        return ComplianceCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance_management_partners(self) -> ComplianceManagementPartnersRequestBuilder:
        """
        Provides operations to manage the complianceManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        from .compliance_management_partners.compliance_management_partners_request_builder import ComplianceManagementPartnersRequestBuilder

        return ComplianceManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance_policies(self) -> CompliancePoliciesRequestBuilder:
        """
        Provides operations to manage the compliancePolicies property of the microsoft.graph.deviceManagement entity.
        """
        from .compliance_policies.compliance_policies_request_builder import CompliancePoliciesRequestBuilder

        return CompliancePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance_settings(self) -> ComplianceSettingsRequestBuilder:
        """
        Provides operations to manage the complianceSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .compliance_settings.compliance_settings_request_builder import ComplianceSettingsRequestBuilder

        return ComplianceSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conditional_access_settings(self) -> ConditionalAccessSettingsRequestBuilder:
        """
        Provides operations to manage the conditionalAccessSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .conditional_access_settings.conditional_access_settings_request_builder import ConditionalAccessSettingsRequestBuilder

        return ConditionalAccessSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def config_manager_collections(self) -> ConfigManagerCollectionsRequestBuilder:
        """
        Provides operations to manage the configManagerCollections property of the microsoft.graph.deviceManagement entity.
        """
        from .config_manager_collections.config_manager_collections_request_builder import ConfigManagerCollectionsRequestBuilder

        return ConfigManagerCollectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration_categories(self) -> ConfigurationCategoriesRequestBuilder:
        """
        Provides operations to manage the configurationCategories property of the microsoft.graph.deviceManagement entity.
        """
        from .configuration_categories.configuration_categories_request_builder import ConfigurationCategoriesRequestBuilder

        return ConfigurationCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration_policies(self) -> ConfigurationPoliciesRequestBuilder:
        """
        Provides operations to manage the configurationPolicies property of the microsoft.graph.deviceManagement entity.
        """
        from .configuration_policies.configuration_policies_request_builder import ConfigurationPoliciesRequestBuilder

        return ConfigurationPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration_policy_templates(self) -> ConfigurationPolicyTemplatesRequestBuilder:
        """
        Provides operations to manage the configurationPolicyTemplates property of the microsoft.graph.deviceManagement entity.
        """
        from .configuration_policy_templates.configuration_policy_templates_request_builder import ConfigurationPolicyTemplatesRequestBuilder

        return ConfigurationPolicyTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration_settings(self) -> ConfigurationSettingsRequestBuilder:
        """
        Provides operations to manage the configurationSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .configuration_settings.configuration_settings_request_builder import ConfigurationSettingsRequestBuilder

        return ConfigurationSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_sharing_consents(self) -> DataSharingConsentsRequestBuilder:
        """
        Provides operations to manage the dataSharingConsents property of the microsoft.graph.deviceManagement entity.
        """
        from .data_sharing_consents.data_sharing_consents_request_builder import DataSharingConsentsRequestBuilder

        return DataSharingConsentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dep_onboarding_settings(self) -> DepOnboardingSettingsRequestBuilder:
        """
        Provides operations to manage the depOnboardingSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .dep_onboarding_settings.dep_onboarding_settings_request_builder import DepOnboardingSettingsRequestBuilder

        return DepOnboardingSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def derived_credentials(self) -> DerivedCredentialsRequestBuilder:
        """
        Provides operations to manage the derivedCredentials property of the microsoft.graph.deviceManagement entity.
        """
        from .derived_credentials.derived_credentials_request_builder import DerivedCredentialsRequestBuilder

        return DerivedCredentialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def detected_apps(self) -> DetectedAppsRequestBuilder:
        """
        Provides operations to manage the detectedApps property of the microsoft.graph.deviceManagement entity.
        """
        from .detected_apps.detected_apps_request_builder import DetectedAppsRequestBuilder

        return DetectedAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_categories(self) -> DeviceCategoriesRequestBuilder:
        """
        Provides operations to manage the deviceCategories property of the microsoft.graph.deviceManagement entity.
        """
        from .device_categories.device_categories_request_builder import DeviceCategoriesRequestBuilder

        return DeviceCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policies(self) -> DeviceCompliancePoliciesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicies property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_policies.device_compliance_policies_request_builder import DeviceCompliancePoliciesRequestBuilder

        return DeviceCompliancePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_device_state_summary(self) -> DeviceCompliancePolicyDeviceStateSummaryRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicyDeviceStateSummary property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_policy_device_state_summary.device_compliance_policy_device_state_summary_request_builder import DeviceCompliancePolicyDeviceStateSummaryRequestBuilder

        return DeviceCompliancePolicyDeviceStateSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_setting_state_summaries(self) -> DeviceCompliancePolicySettingStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicySettingStateSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_policy_setting_state_summaries.device_compliance_policy_setting_state_summaries_request_builder import DeviceCompliancePolicySettingStateSummariesRequestBuilder

        return DeviceCompliancePolicySettingStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_scripts(self) -> DeviceComplianceScriptsRequestBuilder:
        """
        Provides operations to manage the deviceComplianceScripts property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_scripts.device_compliance_scripts_request_builder import DeviceComplianceScriptsRequestBuilder

        return DeviceComplianceScriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_conflict_summary(self) -> DeviceConfigurationConflictSummaryRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationConflictSummary property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configuration_conflict_summary.device_configuration_conflict_summary_request_builder import DeviceConfigurationConflictSummaryRequestBuilder

        return DeviceConfigurationConflictSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_device_state_summaries(self) -> DeviceConfigurationDeviceStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationDeviceStateSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configuration_device_state_summaries.device_configuration_device_state_summaries_request_builder import DeviceConfigurationDeviceStateSummariesRequestBuilder

        return DeviceConfigurationDeviceStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_profiles(self) -> DeviceConfigurationProfilesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configuration_profiles.device_configuration_profiles_request_builder import DeviceConfigurationProfilesRequestBuilder

        return DeviceConfigurationProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_restricted_apps_violations(self) -> DeviceConfigurationRestrictedAppsViolationsRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationRestrictedAppsViolations property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configuration_restricted_apps_violations.device_configuration_restricted_apps_violations_request_builder import DeviceConfigurationRestrictedAppsViolationsRequestBuilder

        return DeviceConfigurationRestrictedAppsViolationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_user_state_summaries(self) -> DeviceConfigurationUserStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationUserStateSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configuration_user_state_summaries.device_configuration_user_state_summaries_request_builder import DeviceConfigurationUserStateSummariesRequestBuilder

        return DeviceConfigurationUserStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configurations(self) -> DeviceConfigurationsRequestBuilder:
        """
        Provides operations to manage the deviceConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configurations.device_configurations_request_builder import DeviceConfigurationsRequestBuilder

        return DeviceConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configurations_all_managed_device_certificate_states(self) -> DeviceConfigurationsAllManagedDeviceCertificateStatesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationsAllManagedDeviceCertificateStates property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configurations_all_managed_device_certificate_states.device_configurations_all_managed_device_certificate_states_request_builder import DeviceConfigurationsAllManagedDeviceCertificateStatesRequestBuilder

        return DeviceConfigurationsAllManagedDeviceCertificateStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_custom_attribute_shell_scripts(self) -> DeviceCustomAttributeShellScriptsRequestBuilder:
        """
        Provides operations to manage the deviceCustomAttributeShellScripts property of the microsoft.graph.deviceManagement entity.
        """
        from .device_custom_attribute_shell_scripts.device_custom_attribute_shell_scripts_request_builder import DeviceCustomAttributeShellScriptsRequestBuilder

        return DeviceCustomAttributeShellScriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_enrollment_configurations(self) -> DeviceEnrollmentConfigurationsRequestBuilder:
        """
        Provides operations to manage the deviceEnrollmentConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        from .device_enrollment_configurations.device_enrollment_configurations_request_builder import DeviceEnrollmentConfigurationsRequestBuilder

        return DeviceEnrollmentConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_health_scripts(self) -> DeviceHealthScriptsRequestBuilder:
        """
        Provides operations to manage the deviceHealthScripts property of the microsoft.graph.deviceManagement entity.
        """
        from .device_health_scripts.device_health_scripts_request_builder import DeviceHealthScriptsRequestBuilder

        return DeviceHealthScriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management_partners(self) -> DeviceManagementPartnersRequestBuilder:
        """
        Provides operations to manage the deviceManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        from .device_management_partners.device_management_partners_request_builder import DeviceManagementPartnersRequestBuilder

        return DeviceManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management_scripts(self) -> DeviceManagementScriptsRequestBuilder:
        """
        Provides operations to manage the deviceManagementScripts property of the microsoft.graph.deviceManagement entity.
        """
        from .device_management_scripts.device_management_scripts_request_builder import DeviceManagementScriptsRequestBuilder

        return DeviceManagementScriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_shell_scripts(self) -> DeviceShellScriptsRequestBuilder:
        """
        Provides operations to manage the deviceShellScripts property of the microsoft.graph.deviceManagement entity.
        """
        from .device_shell_scripts.device_shell_scripts_request_builder import DeviceShellScriptsRequestBuilder

        return DeviceShellScriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def domain_join_connectors(self) -> DomainJoinConnectorsRequestBuilder:
        """
        Provides operations to manage the domainJoinConnectors property of the microsoft.graph.deviceManagement entity.
        """
        from .domain_join_connectors.domain_join_connectors_request_builder import DomainJoinConnectorsRequestBuilder

        return DomainJoinConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def elevation_requests(self) -> ElevationRequestsRequestBuilder:
        """
        Provides operations to manage the elevationRequests property of the microsoft.graph.deviceManagement entity.
        """
        from .elevation_requests.elevation_requests_request_builder import ElevationRequestsRequestBuilder

        return ElevationRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def embedded_s_i_m_activation_code_pools(self) -> EmbeddedSIMActivationCodePoolsRequestBuilder:
        """
        Provides operations to manage the embeddedSIMActivationCodePools property of the microsoft.graph.deviceManagement entity.
        """
        from .embedded_s_i_m_activation_code_pools.embedded_s_i_m_activation_code_pools_request_builder import EmbeddedSIMActivationCodePoolsRequestBuilder

        return EmbeddedSIMActivationCodePoolsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable_android_device_administrator_enrollment(self) -> EnableAndroidDeviceAdministratorEnrollmentRequestBuilder:
        """
        Provides operations to call the enableAndroidDeviceAdministratorEnrollment method.
        """
        from .enable_android_device_administrator_enrollment.enable_android_device_administrator_enrollment_request_builder import EnableAndroidDeviceAdministratorEnrollmentRequestBuilder

        return EnableAndroidDeviceAdministratorEnrollmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable_endpoint_privilege_management(self) -> EnableEndpointPrivilegeManagementRequestBuilder:
        """
        Provides operations to call the enableEndpointPrivilegeManagement method.
        """
        from .enable_endpoint_privilege_management.enable_endpoint_privilege_management_request_builder import EnableEndpointPrivilegeManagementRequestBuilder

        return EnableEndpointPrivilegeManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable_legacy_pc_management(self) -> EnableLegacyPcManagementRequestBuilder:
        """
        Provides operations to call the enableLegacyPcManagement method.
        """
        from .enable_legacy_pc_management.enable_legacy_pc_management_request_builder import EnableLegacyPcManagementRequestBuilder

        return EnableLegacyPcManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable_unlicensed_adminstrators(self) -> EnableUnlicensedAdminstratorsRequestBuilder:
        """
        Provides operations to call the enableUnlicensedAdminstrators method.
        """
        from .enable_unlicensed_adminstrators.enable_unlicensed_adminstrators_request_builder import EnableUnlicensedAdminstratorsRequestBuilder

        return EnableUnlicensedAdminstratorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def endpoint_privilege_management_provisioning_status(self) -> EndpointPrivilegeManagementProvisioningStatusRequestBuilder:
        """
        Provides operations to manage the endpointPrivilegeManagementProvisioningStatus property of the microsoft.graph.deviceManagement entity.
        """
        from .endpoint_privilege_management_provisioning_status.endpoint_privilege_management_provisioning_status_request_builder import EndpointPrivilegeManagementProvisioningStatusRequestBuilder

        return EndpointPrivilegeManagementProvisioningStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def evaluate_assignment_filter(self) -> EvaluateAssignmentFilterRequestBuilder:
        """
        Provides operations to call the evaluateAssignmentFilter method.
        """
        from .evaluate_assignment_filter.evaluate_assignment_filter_request_builder import EvaluateAssignmentFilterRequestBuilder

        return EvaluateAssignmentFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange_connectors(self) -> ExchangeConnectorsRequestBuilder:
        """
        Provides operations to manage the exchangeConnectors property of the microsoft.graph.deviceManagement entity.
        """
        from .exchange_connectors.exchange_connectors_request_builder import ExchangeConnectorsRequestBuilder

        return ExchangeConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange_on_premises_policies(self) -> ExchangeOnPremisesPoliciesRequestBuilder:
        """
        Provides operations to manage the exchangeOnPremisesPolicies property of the microsoft.graph.deviceManagement entity.
        """
        from .exchange_on_premises_policies.exchange_on_premises_policies_request_builder import ExchangeOnPremisesPoliciesRequestBuilder

        return ExchangeOnPremisesPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange_on_premises_policy(self) -> ExchangeOnPremisesPolicyRequestBuilder:
        """
        Provides operations to manage the exchangeOnPremisesPolicy property of the microsoft.graph.deviceManagement entity.
        """
        from .exchange_on_premises_policy.exchange_on_premises_policy_request_builder import ExchangeOnPremisesPolicyRequestBuilder

        return ExchangeOnPremisesPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_assigned_role_details(self) -> GetAssignedRoleDetailsRequestBuilder:
        """
        Provides operations to call the getAssignedRoleDetails method.
        """
        from .get_assigned_role_details.get_assigned_role_details_request_builder import GetAssignedRoleDetailsRequestBuilder

        return GetAssignedRoleDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_assignment_filters_status_details(self) -> GetAssignmentFiltersStatusDetailsRequestBuilder:
        """
        Provides operations to call the getAssignmentFiltersStatusDetails method.
        """
        from .get_assignment_filters_status_details.get_assignment_filters_status_details_request_builder import GetAssignmentFiltersStatusDetailsRequestBuilder

        return GetAssignmentFiltersStatusDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_comanaged_devices_summary(self) -> GetComanagedDevicesSummaryRequestBuilder:
        """
        Provides operations to call the getComanagedDevicesSummary method.
        """
        from .get_comanaged_devices_summary.get_comanaged_devices_summary_request_builder import GetComanagedDevicesSummaryRequestBuilder

        return GetComanagedDevicesSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_comanagement_eligible_devices_summary(self) -> GetComanagementEligibleDevicesSummaryRequestBuilder:
        """
        Provides operations to call the getComanagementEligibleDevicesSummary method.
        """
        from .get_comanagement_eligible_devices_summary.get_comanagement_eligible_devices_summary_request_builder import GetComanagementEligibleDevicesSummaryRequestBuilder

        return GetComanagementEligibleDevicesSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_effective_permissions(self) -> GetEffectivePermissionsRequestBuilder:
        """
        Provides operations to call the getEffectivePermissions method.
        """
        from .get_effective_permissions.get_effective_permissions_request_builder import GetEffectivePermissionsRequestBuilder

        return GetEffectivePermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_categories(self) -> GroupPolicyCategoriesRequestBuilder:
        """
        Provides operations to manage the groupPolicyCategories property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_categories.group_policy_categories_request_builder import GroupPolicyCategoriesRequestBuilder

        return GroupPolicyCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_configurations(self) -> GroupPolicyConfigurationsRequestBuilder:
        """
        Provides operations to manage the groupPolicyConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_configurations.group_policy_configurations_request_builder import GroupPolicyConfigurationsRequestBuilder

        return GroupPolicyConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_definition_files(self) -> GroupPolicyDefinitionFilesRequestBuilder:
        """
        Provides operations to manage the groupPolicyDefinitionFiles property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_definition_files.group_policy_definition_files_request_builder import GroupPolicyDefinitionFilesRequestBuilder

        return GroupPolicyDefinitionFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_definitions(self) -> GroupPolicyDefinitionsRequestBuilder:
        """
        Provides operations to manage the groupPolicyDefinitions property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_definitions.group_policy_definitions_request_builder import GroupPolicyDefinitionsRequestBuilder

        return GroupPolicyDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_migration_reports(self) -> GroupPolicyMigrationReportsRequestBuilder:
        """
        Provides operations to manage the groupPolicyMigrationReports property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_migration_reports.group_policy_migration_reports_request_builder import GroupPolicyMigrationReportsRequestBuilder

        return GroupPolicyMigrationReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_object_files(self) -> GroupPolicyObjectFilesRequestBuilder:
        """
        Provides operations to manage the groupPolicyObjectFiles property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_object_files.group_policy_object_files_request_builder import GroupPolicyObjectFilesRequestBuilder

        return GroupPolicyObjectFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_uploaded_definition_files(self) -> GroupPolicyUploadedDefinitionFilesRequestBuilder:
        """
        Provides operations to manage the groupPolicyUploadedDefinitionFiles property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_uploaded_definition_files.group_policy_uploaded_definition_files_request_builder import GroupPolicyUploadedDefinitionFilesRequestBuilder

        return GroupPolicyUploadedDefinitionFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hardware_configurations(self) -> HardwareConfigurationsRequestBuilder:
        """
        Provides operations to manage the hardwareConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        from .hardware_configurations.hardware_configurations_request_builder import HardwareConfigurationsRequestBuilder

        return HardwareConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hardware_password_details(self) -> HardwarePasswordDetailsRequestBuilder:
        """
        Provides operations to manage the hardwarePasswordDetails property of the microsoft.graph.deviceManagement entity.
        """
        from .hardware_password_details.hardware_password_details_request_builder import HardwarePasswordDetailsRequestBuilder

        return HardwarePasswordDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hardware_password_info(self) -> HardwarePasswordInfoRequestBuilder:
        """
        Provides operations to manage the hardwarePasswordInfo property of the microsoft.graph.deviceManagement entity.
        """
        from .hardware_password_info.hardware_password_info_request_builder import HardwarePasswordInfoRequestBuilder

        return HardwarePasswordInfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def imported_device_identities(self) -> ImportedDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the importedDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        """
        from .imported_device_identities.imported_device_identities_request_builder import ImportedDeviceIdentitiesRequestBuilder

        return ImportedDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def imported_windows_autopilot_device_identities(self) -> ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the importedWindowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        """
        from .imported_windows_autopilot_device_identities.imported_windows_autopilot_device_identities_request_builder import ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder

        return ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intents(self) -> IntentsRequestBuilder:
        """
        Provides operations to manage the intents property of the microsoft.graph.deviceManagement entity.
        """
        from .intents.intents_request_builder import IntentsRequestBuilder

        return IntentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intune_branding_profiles(self) -> IntuneBrandingProfilesRequestBuilder:
        """
        Provides operations to manage the intuneBrandingProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .intune_branding_profiles.intune_branding_profiles_request_builder import IntuneBrandingProfilesRequestBuilder

        return IntuneBrandingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ios_update_statuses(self) -> IosUpdateStatusesRequestBuilder:
        """
        Provides operations to manage the iosUpdateStatuses property of the microsoft.graph.deviceManagement entity.
        """
        from .ios_update_statuses.ios_update_statuses_request_builder import IosUpdateStatusesRequestBuilder

        return IosUpdateStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mac_o_s_software_update_account_summaries(self) -> MacOSSoftwareUpdateAccountSummariesRequestBuilder:
        """
        Provides operations to manage the macOSSoftwareUpdateAccountSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .mac_o_s_software_update_account_summaries.mac_o_s_software_update_account_summaries_request_builder import MacOSSoftwareUpdateAccountSummariesRequestBuilder

        return MacOSSoftwareUpdateAccountSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_cleanup_rules(self) -> ManagedDeviceCleanupRulesRequestBuilder:
        """
        Provides operations to manage the managedDeviceCleanupRules property of the microsoft.graph.deviceManagement entity.
        """
        from .managed_device_cleanup_rules.managed_device_cleanup_rules_request_builder import ManagedDeviceCleanupRulesRequestBuilder

        return ManagedDeviceCleanupRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_encryption_states(self) -> ManagedDeviceEncryptionStatesRequestBuilder:
        """
        Provides operations to manage the managedDeviceEncryptionStates property of the microsoft.graph.deviceManagement entity.
        """
        from .managed_device_encryption_states.managed_device_encryption_states_request_builder import ManagedDeviceEncryptionStatesRequestBuilder

        return ManagedDeviceEncryptionStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_overview(self) -> ManagedDeviceOverviewRequestBuilder:
        """
        Provides operations to manage the managedDeviceOverview property of the microsoft.graph.deviceManagement entity.
        """
        from .managed_device_overview.managed_device_overview_request_builder import ManagedDeviceOverviewRequestBuilder

        return ManagedDeviceOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_windows_o_s_images(self) -> ManagedDeviceWindowsOSImagesRequestBuilder:
        """
        Provides operations to manage the managedDeviceWindowsOSImages property of the microsoft.graph.deviceManagement entity.
        """
        from .managed_device_windows_o_s_images.managed_device_windows_o_s_images_request_builder import ManagedDeviceWindowsOSImagesRequestBuilder

        return ManagedDeviceWindowsOSImagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_devices(self) -> ManagedDevicesRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.deviceManagement entity.
        """
        from .managed_devices.managed_devices_request_builder import ManagedDevicesRequestBuilder

        return ManagedDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_tunnel_configurations(self) -> MicrosoftTunnelConfigurationsRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        from .microsoft_tunnel_configurations.microsoft_tunnel_configurations_request_builder import MicrosoftTunnelConfigurationsRequestBuilder

        return MicrosoftTunnelConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_tunnel_health_thresholds(self) -> MicrosoftTunnelHealthThresholdsRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelHealthThresholds property of the microsoft.graph.deviceManagement entity.
        """
        from .microsoft_tunnel_health_thresholds.microsoft_tunnel_health_thresholds_request_builder import MicrosoftTunnelHealthThresholdsRequestBuilder

        return MicrosoftTunnelHealthThresholdsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_tunnel_server_log_collection_responses(self) -> MicrosoftTunnelServerLogCollectionResponsesRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelServerLogCollectionResponses property of the microsoft.graph.deviceManagement entity.
        """
        from .microsoft_tunnel_server_log_collection_responses.microsoft_tunnel_server_log_collection_responses_request_builder import MicrosoftTunnelServerLogCollectionResponsesRequestBuilder

        return MicrosoftTunnelServerLogCollectionResponsesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_tunnel_sites(self) -> MicrosoftTunnelSitesRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelSites property of the microsoft.graph.deviceManagement entity.
        """
        from .microsoft_tunnel_sites.microsoft_tunnel_sites_request_builder import MicrosoftTunnelSitesRequestBuilder

        return MicrosoftTunnelSitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_troubleshooting_events(self) -> MobileAppTroubleshootingEventsRequestBuilder:
        """
        Provides operations to manage the mobileAppTroubleshootingEvents property of the microsoft.graph.deviceManagement entity.
        """
        from .mobile_app_troubleshooting_events.mobile_app_troubleshooting_events_request_builder import MobileAppTroubleshootingEventsRequestBuilder

        return MobileAppTroubleshootingEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_threat_defense_connectors(self) -> MobileThreatDefenseConnectorsRequestBuilder:
        """
        Provides operations to manage the mobileThreatDefenseConnectors property of the microsoft.graph.deviceManagement entity.
        """
        from .mobile_threat_defense_connectors.mobile_threat_defense_connectors_request_builder import MobileThreatDefenseConnectorsRequestBuilder

        return MobileThreatDefenseConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monitoring(self) -> MonitoringRequestBuilder:
        """
        Provides operations to manage the monitoring property of the microsoft.graph.deviceManagement entity.
        """
        from .monitoring.monitoring_request_builder import MonitoringRequestBuilder

        return MonitoringRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ndes_connectors(self) -> NdesConnectorsRequestBuilder:
        """
        Provides operations to manage the ndesConnectors property of the microsoft.graph.deviceManagement entity.
        """
        from .ndes_connectors.ndes_connectors_request_builder import NdesConnectorsRequestBuilder

        return NdesConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notification_message_templates(self) -> NotificationMessageTemplatesRequestBuilder:
        """
        Provides operations to manage the notificationMessageTemplates property of the microsoft.graph.deviceManagement entity.
        """
        from .notification_message_templates.notification_message_templates_request_builder import NotificationMessageTemplatesRequestBuilder

        return NotificationMessageTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operation_approval_policies(self) -> OperationApprovalPoliciesRequestBuilder:
        """
        Provides operations to manage the operationApprovalPolicies property of the microsoft.graph.deviceManagement entity.
        """
        from .operation_approval_policies.operation_approval_policies_request_builder import OperationApprovalPoliciesRequestBuilder

        return OperationApprovalPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operation_approval_requests(self) -> OperationApprovalRequestsRequestBuilder:
        """
        Provides operations to manage the operationApprovalRequests property of the microsoft.graph.deviceManagement entity.
        """
        from .operation_approval_requests.operation_approval_requests_request_builder import OperationApprovalRequestsRequestBuilder

        return OperationApprovalRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privilege_management_elevations(self) -> PrivilegeManagementElevationsRequestBuilder:
        """
        Provides operations to manage the privilegeManagementElevations property of the microsoft.graph.deviceManagement entity.
        """
        from .privilege_management_elevations.privilege_management_elevations_request_builder import PrivilegeManagementElevationsRequestBuilder

        return PrivilegeManagementElevationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_action_audits(self) -> RemoteActionAuditsRequestBuilder:
        """
        Provides operations to manage the remoteActionAudits property of the microsoft.graph.deviceManagement entity.
        """
        from .remote_action_audits.remote_action_audits_request_builder import RemoteActionAuditsRequestBuilder

        return RemoteActionAuditsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_assistance_partners(self) -> RemoteAssistancePartnersRequestBuilder:
        """
        Provides operations to manage the remoteAssistancePartners property of the microsoft.graph.deviceManagement entity.
        """
        from .remote_assistance_partners.remote_assistance_partners_request_builder import RemoteAssistancePartnersRequestBuilder

        return RemoteAssistancePartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_assistance_settings(self) -> RemoteAssistanceSettingsRequestBuilder:
        """
        Provides operations to manage the remoteAssistanceSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .remote_assistance_settings.remote_assistance_settings_request_builder import RemoteAssistanceSettingsRequestBuilder

        return RemoteAssistanceSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reports(self) -> ReportsRequestBuilder:
        """
        Provides operations to manage the reports property of the microsoft.graph.deviceManagement entity.
        """
        from .reports.reports_request_builder import ReportsRequestBuilder

        return ReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_access_profiles(self) -> ResourceAccessProfilesRequestBuilder:
        """
        Provides operations to manage the resourceAccessProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .resource_access_profiles.resource_access_profiles_request_builder import ResourceAccessProfilesRequestBuilder

        return ResourceAccessProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_operations(self) -> ResourceOperationsRequestBuilder:
        """
        Provides operations to manage the resourceOperations property of the microsoft.graph.deviceManagement entity.
        """
        from .resource_operations.resource_operations_request_builder import ResourceOperationsRequestBuilder

        return ResourceOperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reusable_policy_settings(self) -> ReusablePolicySettingsRequestBuilder:
        """
        Provides operations to manage the reusablePolicySettings property of the microsoft.graph.deviceManagement entity.
        """
        from .reusable_policy_settings.reusable_policy_settings_request_builder import ReusablePolicySettingsRequestBuilder

        return ReusablePolicySettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reusable_settings(self) -> ReusableSettingsRequestBuilder:
        """
        Provides operations to manage the reusableSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .reusable_settings.reusable_settings_request_builder import ReusableSettingsRequestBuilder

        return ReusableSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignments(self) -> RoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.deviceManagement entity.
        """
        from .role_assignments.role_assignments_request_builder import RoleAssignmentsRequestBuilder

        return RoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definitions(self) -> RoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.deviceManagement entity.
        """
        from .role_definitions.role_definitions_request_builder import RoleDefinitionsRequestBuilder

        return RoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_scope_tags(self) -> RoleScopeTagsRequestBuilder:
        """
        Provides operations to manage the roleScopeTags property of the microsoft.graph.deviceManagement entity.
        """
        from .role_scope_tags.role_scope_tags_request_builder import RoleScopeTagsRequestBuilder

        return RoleScopeTagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_custom_notification_to_company_portal(self) -> SendCustomNotificationToCompanyPortalRequestBuilder:
        """
        Provides operations to call the sendCustomNotificationToCompanyPortal method.
        """
        from .send_custom_notification_to_company_portal.send_custom_notification_to_company_portal_request_builder import SendCustomNotificationToCompanyPortalRequestBuilder

        return SendCustomNotificationToCompanyPortalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_now_connections(self) -> ServiceNowConnectionsRequestBuilder:
        """
        Provides operations to manage the serviceNowConnections property of the microsoft.graph.deviceManagement entity.
        """
        from .service_now_connections.service_now_connections_request_builder import ServiceNowConnectionsRequestBuilder

        return ServiceNowConnectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def setting_definitions(self) -> SettingDefinitionsRequestBuilder:
        """
        Provides operations to manage the settingDefinitions property of the microsoft.graph.deviceManagement entity.
        """
        from .setting_definitions.setting_definitions_request_builder import SettingDefinitionsRequestBuilder

        return SettingDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def software_update_status_summary(self) -> SoftwareUpdateStatusSummaryRequestBuilder:
        """
        Provides operations to manage the softwareUpdateStatusSummary property of the microsoft.graph.deviceManagement entity.
        """
        from .software_update_status_summary.software_update_status_summary_request_builder import SoftwareUpdateStatusSummaryRequestBuilder

        return SoftwareUpdateStatusSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def telecom_expense_management_partners(self) -> TelecomExpenseManagementPartnersRequestBuilder:
        """
        Provides operations to manage the telecomExpenseManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        from .telecom_expense_management_partners.telecom_expense_management_partners_request_builder import TelecomExpenseManagementPartnersRequestBuilder

        return TelecomExpenseManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def template_insights(self) -> TemplateInsightsRequestBuilder:
        """
        Provides operations to manage the templateInsights property of the microsoft.graph.deviceManagement entity.
        """
        from .template_insights.template_insights_request_builder import TemplateInsightsRequestBuilder

        return TemplateInsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def template_settings(self) -> TemplateSettingsRequestBuilder:
        """
        Provides operations to manage the templateSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .template_settings.template_settings_request_builder import TemplateSettingsRequestBuilder

        return TemplateSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def templates(self) -> TemplatesRequestBuilder:
        """
        Provides operations to manage the templates property of the microsoft.graph.deviceManagement entity.
        """
        from .templates.templates_request_builder import TemplatesRequestBuilder

        return TemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenant_attach_r_b_a_c(self) -> TenantAttachRBACRequestBuilder:
        """
        Provides operations to manage the tenantAttachRBAC property of the microsoft.graph.deviceManagement entity.
        """
        from .tenant_attach_r_b_a_c.tenant_attach_r_b_a_c_request_builder import TenantAttachRBACRequestBuilder

        return TenantAttachRBACRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def terms_and_conditions(self) -> TermsAndConditionsRequestBuilder:
        """
        Provides operations to manage the termsAndConditions property of the microsoft.graph.deviceManagement entity.
        """
        from .terms_and_conditions.terms_and_conditions_request_builder import TermsAndConditionsRequestBuilder

        return TermsAndConditionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def troubleshooting_events(self) -> TroubleshootingEventsRequestBuilder:
        """
        Provides operations to manage the troubleshootingEvents property of the microsoft.graph.deviceManagement entity.
        """
        from .troubleshooting_events.troubleshooting_events_request_builder import TroubleshootingEventsRequestBuilder

        return TroubleshootingEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_anomaly(self) -> UserExperienceAnalyticsAnomalyRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAnomaly property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_anomaly.user_experience_analytics_anomaly_request_builder import UserExperienceAnalyticsAnomalyRequestBuilder

        return UserExperienceAnalyticsAnomalyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_anomaly_correlation_group_overview(self) -> UserExperienceAnalyticsAnomalyCorrelationGroupOverviewRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAnomalyCorrelationGroupOverview property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_anomaly_correlation_group_overview.user_experience_analytics_anomaly_correlation_group_overview_request_builder import UserExperienceAnalyticsAnomalyCorrelationGroupOverviewRequestBuilder

        return UserExperienceAnalyticsAnomalyCorrelationGroupOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_anomaly_device(self) -> UserExperienceAnalyticsAnomalyDeviceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAnomalyDevice property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_anomaly_device.user_experience_analytics_anomaly_device_request_builder import UserExperienceAnalyticsAnomalyDeviceRequestBuilder

        return UserExperienceAnalyticsAnomalyDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_application_performance(self) -> UserExperienceAnalyticsAppHealthApplicationPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance.user_experience_analytics_app_health_application_performance_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceRequestBuilder

        return UserExperienceAnalyticsAppHealthApplicationPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_application_performance_by_app_version(self) -> UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance_by_app_version.user_experience_analytics_app_health_application_performance_by_app_version_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionRequestBuilder

        return UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_application_performance_by_app_version_details(self) -> UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance_by_app_version_details.user_experience_analytics_app_health_application_performance_by_app_version_details_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilder

        return UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_application_performance_by_app_version_device_id(self) -> UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance_by_app_version_device_id.user_experience_analytics_app_health_application_performance_by_app_version_device_id_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequestBuilder

        return UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_application_performance_by_o_s_version(self) -> UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance_by_o_s_version.user_experience_analytics_app_health_application_performance_by_o_s_version_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequestBuilder

        return UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_device_model_performance(self) -> UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthDeviceModelPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_device_model_performance.user_experience_analytics_app_health_device_model_performance_request_builder import UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequestBuilder

        return UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_device_performance(self) -> UserExperienceAnalyticsAppHealthDevicePerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthDevicePerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_device_performance.user_experience_analytics_app_health_device_performance_request_builder import UserExperienceAnalyticsAppHealthDevicePerformanceRequestBuilder

        return UserExperienceAnalyticsAppHealthDevicePerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_device_performance_details(self) -> UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthDevicePerformanceDetails property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_device_performance_details.user_experience_analytics_app_health_device_performance_details_request_builder import UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequestBuilder

        return UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_o_s_version_performance(self) -> UserExperienceAnalyticsAppHealthOSVersionPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthOSVersionPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_o_s_version_performance.user_experience_analytics_app_health_o_s_version_performance_request_builder import UserExperienceAnalyticsAppHealthOSVersionPerformanceRequestBuilder

        return UserExperienceAnalyticsAppHealthOSVersionPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_overview(self) -> UserExperienceAnalyticsAppHealthOverviewRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthOverview property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_overview.user_experience_analytics_app_health_overview_request_builder import UserExperienceAnalyticsAppHealthOverviewRequestBuilder

        return UserExperienceAnalyticsAppHealthOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_baselines(self) -> UserExperienceAnalyticsBaselinesRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBaselines property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_baselines.user_experience_analytics_baselines_request_builder import UserExperienceAnalyticsBaselinesRequestBuilder

        return UserExperienceAnalyticsBaselinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_app_impact(self) -> UserExperienceAnalyticsBatteryHealthAppImpactRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthAppImpact property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_app_impact.user_experience_analytics_battery_health_app_impact_request_builder import UserExperienceAnalyticsBatteryHealthAppImpactRequestBuilder

        return UserExperienceAnalyticsBatteryHealthAppImpactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_capacity_details(self) -> UserExperienceAnalyticsBatteryHealthCapacityDetailsRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthCapacityDetails property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_capacity_details.user_experience_analytics_battery_health_capacity_details_request_builder import UserExperienceAnalyticsBatteryHealthCapacityDetailsRequestBuilder

        return UserExperienceAnalyticsBatteryHealthCapacityDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_device_app_impact(self) -> UserExperienceAnalyticsBatteryHealthDeviceAppImpactRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthDeviceAppImpact property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_device_app_impact.user_experience_analytics_battery_health_device_app_impact_request_builder import UserExperienceAnalyticsBatteryHealthDeviceAppImpactRequestBuilder

        return UserExperienceAnalyticsBatteryHealthDeviceAppImpactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_device_performance(self) -> UserExperienceAnalyticsBatteryHealthDevicePerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthDevicePerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_device_performance.user_experience_analytics_battery_health_device_performance_request_builder import UserExperienceAnalyticsBatteryHealthDevicePerformanceRequestBuilder

        return UserExperienceAnalyticsBatteryHealthDevicePerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_device_runtime_history(self) -> UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistoryRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_device_runtime_history.user_experience_analytics_battery_health_device_runtime_history_request_builder import UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistoryRequestBuilder

        return UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_model_performance(self) -> UserExperienceAnalyticsBatteryHealthModelPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthModelPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_model_performance.user_experience_analytics_battery_health_model_performance_request_builder import UserExperienceAnalyticsBatteryHealthModelPerformanceRequestBuilder

        return UserExperienceAnalyticsBatteryHealthModelPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_os_performance(self) -> UserExperienceAnalyticsBatteryHealthOsPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthOsPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_os_performance.user_experience_analytics_battery_health_os_performance_request_builder import UserExperienceAnalyticsBatteryHealthOsPerformanceRequestBuilder

        return UserExperienceAnalyticsBatteryHealthOsPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_runtime_details(self) -> UserExperienceAnalyticsBatteryHealthRuntimeDetailsRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthRuntimeDetails property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_runtime_details.user_experience_analytics_battery_health_runtime_details_request_builder import UserExperienceAnalyticsBatteryHealthRuntimeDetailsRequestBuilder

        return UserExperienceAnalyticsBatteryHealthRuntimeDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_categories(self) -> UserExperienceAnalyticsCategoriesRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsCategories property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_categories.user_experience_analytics_categories_request_builder import UserExperienceAnalyticsCategoriesRequestBuilder

        return UserExperienceAnalyticsCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_metric_history(self) -> UserExperienceAnalyticsDeviceMetricHistoryRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceMetricHistory property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_metric_history.user_experience_analytics_device_metric_history_request_builder import UserExperienceAnalyticsDeviceMetricHistoryRequestBuilder

        return UserExperienceAnalyticsDeviceMetricHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_performance(self) -> UserExperienceAnalyticsDevicePerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDevicePerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_performance.user_experience_analytics_device_performance_request_builder import UserExperienceAnalyticsDevicePerformanceRequestBuilder

        return UserExperienceAnalyticsDevicePerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_scope(self) -> UserExperienceAnalyticsDeviceScopeRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceScope property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_scope.user_experience_analytics_device_scope_request_builder import UserExperienceAnalyticsDeviceScopeRequestBuilder

        return UserExperienceAnalyticsDeviceScopeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_scopes(self) -> UserExperienceAnalyticsDeviceScopesRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceScopes property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_scopes.user_experience_analytics_device_scopes_request_builder import UserExperienceAnalyticsDeviceScopesRequestBuilder

        return UserExperienceAnalyticsDeviceScopesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_scores(self) -> UserExperienceAnalyticsDeviceScoresRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceScores property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_scores.user_experience_analytics_device_scores_request_builder import UserExperienceAnalyticsDeviceScoresRequestBuilder

        return UserExperienceAnalyticsDeviceScoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_startup_history(self) -> UserExperienceAnalyticsDeviceStartupHistoryRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceStartupHistory property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_startup_history.user_experience_analytics_device_startup_history_request_builder import UserExperienceAnalyticsDeviceStartupHistoryRequestBuilder

        return UserExperienceAnalyticsDeviceStartupHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_startup_process_performance(self) -> UserExperienceAnalyticsDeviceStartupProcessPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceStartupProcessPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_startup_process_performance.user_experience_analytics_device_startup_process_performance_request_builder import UserExperienceAnalyticsDeviceStartupProcessPerformanceRequestBuilder

        return UserExperienceAnalyticsDeviceStartupProcessPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_startup_processes(self) -> UserExperienceAnalyticsDeviceStartupProcessesRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceStartupProcesses property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_startup_processes.user_experience_analytics_device_startup_processes_request_builder import UserExperienceAnalyticsDeviceStartupProcessesRequestBuilder

        return UserExperienceAnalyticsDeviceStartupProcessesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_timeline_event(self) -> UserExperienceAnalyticsDeviceTimelineEventRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceTimelineEvent property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_timeline_event.user_experience_analytics_device_timeline_event_request_builder import UserExperienceAnalyticsDeviceTimelineEventRequestBuilder

        return UserExperienceAnalyticsDeviceTimelineEventRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_devices_without_cloud_identity(self) -> UserExperienceAnalyticsDevicesWithoutCloudIdentityRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDevicesWithoutCloudIdentity property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_devices_without_cloud_identity.user_experience_analytics_devices_without_cloud_identity_request_builder import UserExperienceAnalyticsDevicesWithoutCloudIdentityRequestBuilder

        return UserExperienceAnalyticsDevicesWithoutCloudIdentityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_impacting_process(self) -> UserExperienceAnalyticsImpactingProcessRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsImpactingProcess property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_impacting_process.user_experience_analytics_impacting_process_request_builder import UserExperienceAnalyticsImpactingProcessRequestBuilder

        return UserExperienceAnalyticsImpactingProcessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_metric_history(self) -> UserExperienceAnalyticsMetricHistoryRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsMetricHistory property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_metric_history.user_experience_analytics_metric_history_request_builder import UserExperienceAnalyticsMetricHistoryRequestBuilder

        return UserExperienceAnalyticsMetricHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_model_scores(self) -> UserExperienceAnalyticsModelScoresRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsModelScores property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_model_scores.user_experience_analytics_model_scores_request_builder import UserExperienceAnalyticsModelScoresRequestBuilder

        return UserExperienceAnalyticsModelScoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_not_autopilot_ready_device(self) -> UserExperienceAnalyticsNotAutopilotReadyDeviceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsNotAutopilotReadyDevice property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_not_autopilot_ready_device.user_experience_analytics_not_autopilot_ready_device_request_builder import UserExperienceAnalyticsNotAutopilotReadyDeviceRequestBuilder

        return UserExperienceAnalyticsNotAutopilotReadyDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_overview(self) -> UserExperienceAnalyticsOverviewRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsOverview property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_overview.user_experience_analytics_overview_request_builder import UserExperienceAnalyticsOverviewRequestBuilder

        return UserExperienceAnalyticsOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_remote_connection(self) -> UserExperienceAnalyticsRemoteConnectionRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsRemoteConnection property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_remote_connection.user_experience_analytics_remote_connection_request_builder import UserExperienceAnalyticsRemoteConnectionRequestBuilder

        return UserExperienceAnalyticsRemoteConnectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_resource_performance(self) -> UserExperienceAnalyticsResourcePerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsResourcePerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_resource_performance.user_experience_analytics_resource_performance_request_builder import UserExperienceAnalyticsResourcePerformanceRequestBuilder

        return UserExperienceAnalyticsResourcePerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_score_history(self) -> UserExperienceAnalyticsScoreHistoryRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsScoreHistory property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_score_history.user_experience_analytics_score_history_request_builder import UserExperienceAnalyticsScoreHistoryRequestBuilder

        return UserExperienceAnalyticsScoreHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_summarize_work_from_anywhere_devices(self) -> UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequestBuilder:
        """
        Provides operations to call the userExperienceAnalyticsSummarizeWorkFromAnywhereDevices method.
        """
        from .user_experience_analytics_summarize_work_from_anywhere_devices.user_experience_analytics_summarize_work_from_anywhere_devices_request_builder import UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequestBuilder

        return UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_summarized_device_scopes(self) -> UserExperienceAnalyticsSummarizedDeviceScopesRequestBuilder:
        """
        Provides operations to call the userExperienceAnalyticsSummarizedDeviceScopes method.
        """
        from .user_experience_analytics_summarized_device_scopes.user_experience_analytics_summarized_device_scopes_request_builder import UserExperienceAnalyticsSummarizedDeviceScopesRequestBuilder

        return UserExperienceAnalyticsSummarizedDeviceScopesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_work_from_anywhere_hardware_readiness_metric(self) -> UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric.user_experience_analytics_work_from_anywhere_hardware_readiness_metric_request_builder import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequestBuilder

        return UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_work_from_anywhere_metrics(self) -> UserExperienceAnalyticsWorkFromAnywhereMetricsRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsWorkFromAnywhereMetrics property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_work_from_anywhere_metrics.user_experience_analytics_work_from_anywhere_metrics_request_builder import UserExperienceAnalyticsWorkFromAnywhereMetricsRequestBuilder

        return UserExperienceAnalyticsWorkFromAnywhereMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_work_from_anywhere_model_performance(self) -> UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsWorkFromAnywhereModelPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_work_from_anywhere_model_performance.user_experience_analytics_work_from_anywhere_model_performance_request_builder import UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequestBuilder

        return UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_pfx_certificates(self) -> UserPfxCertificatesRequestBuilder:
        """
        Provides operations to manage the userPfxCertificates property of the microsoft.graph.deviceManagement entity.
        """
        from .user_pfx_certificates.user_pfx_certificates_request_builder import UserPfxCertificatesRequestBuilder

        return UserPfxCertificatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def virtual_endpoint(self) -> VirtualEndpointRequestBuilder:
        """
        Provides operations to manage the virtualEndpoint property of the microsoft.graph.deviceManagement entity.
        """
        from .virtual_endpoint.virtual_endpoint_request_builder import VirtualEndpointRequestBuilder

        return VirtualEndpointRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_autopilot_deployment_profiles(self) -> WindowsAutopilotDeploymentProfilesRequestBuilder:
        """
        Provides operations to manage the windowsAutopilotDeploymentProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_autopilot_deployment_profiles.windows_autopilot_deployment_profiles_request_builder import WindowsAutopilotDeploymentProfilesRequestBuilder

        return WindowsAutopilotDeploymentProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_autopilot_device_identities(self) -> WindowsAutopilotDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the windowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_autopilot_device_identities.windows_autopilot_device_identities_request_builder import WindowsAutopilotDeviceIdentitiesRequestBuilder

        return WindowsAutopilotDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_autopilot_settings(self) -> WindowsAutopilotSettingsRequestBuilder:
        """
        Provides operations to manage the windowsAutopilotSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_autopilot_settings.windows_autopilot_settings_request_builder import WindowsAutopilotSettingsRequestBuilder

        return WindowsAutopilotSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_driver_update_profiles(self) -> WindowsDriverUpdateProfilesRequestBuilder:
        """
        Provides operations to manage the windowsDriverUpdateProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_driver_update_profiles.windows_driver_update_profiles_request_builder import WindowsDriverUpdateProfilesRequestBuilder

        return WindowsDriverUpdateProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_feature_update_profiles(self) -> WindowsFeatureUpdateProfilesRequestBuilder:
        """
        Provides operations to manage the windowsFeatureUpdateProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_feature_update_profiles.windows_feature_update_profiles_request_builder import WindowsFeatureUpdateProfilesRequestBuilder

        return WindowsFeatureUpdateProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_app_learning_summaries(self) -> WindowsInformationProtectionAppLearningSummariesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionAppLearningSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_information_protection_app_learning_summaries.windows_information_protection_app_learning_summaries_request_builder import WindowsInformationProtectionAppLearningSummariesRequestBuilder

        return WindowsInformationProtectionAppLearningSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_network_learning_summaries(self) -> WindowsInformationProtectionNetworkLearningSummariesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionNetworkLearningSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_information_protection_network_learning_summaries.windows_information_protection_network_learning_summaries_request_builder import WindowsInformationProtectionNetworkLearningSummariesRequestBuilder

        return WindowsInformationProtectionNetworkLearningSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_malware_information(self) -> WindowsMalwareInformationRequestBuilder:
        """
        Provides operations to manage the windowsMalwareInformation property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_malware_information.windows_malware_information_request_builder import WindowsMalwareInformationRequestBuilder

        return WindowsMalwareInformationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_quality_update_policies(self) -> WindowsQualityUpdatePoliciesRequestBuilder:
        """
        Provides operations to manage the windowsQualityUpdatePolicies property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_quality_update_policies.windows_quality_update_policies_request_builder import WindowsQualityUpdatePoliciesRequestBuilder

        return WindowsQualityUpdatePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_quality_update_profiles(self) -> WindowsQualityUpdateProfilesRequestBuilder:
        """
        Provides operations to manage the windowsQualityUpdateProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_quality_update_profiles.windows_quality_update_profiles_request_builder import WindowsQualityUpdateProfilesRequestBuilder

        return WindowsQualityUpdateProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_update_catalog_items(self) -> WindowsUpdateCatalogItemsRequestBuilder:
        """
        Provides operations to manage the windowsUpdateCatalogItems property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_update_catalog_items.windows_update_catalog_items_request_builder import WindowsUpdateCatalogItemsRequestBuilder

        return WindowsUpdateCatalogItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def zebra_fota_artifacts(self) -> ZebraFotaArtifactsRequestBuilder:
        """
        Provides operations to manage the zebraFotaArtifacts property of the microsoft.graph.deviceManagement entity.
        """
        from .zebra_fota_artifacts.zebra_fota_artifacts_request_builder import ZebraFotaArtifactsRequestBuilder

        return ZebraFotaArtifactsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def zebra_fota_connector(self) -> ZebraFotaConnectorRequestBuilder:
        """
        Provides operations to manage the zebraFotaConnector property of the microsoft.graph.deviceManagement entity.
        """
        from .zebra_fota_connector.zebra_fota_connector_request_builder import ZebraFotaConnectorRequestBuilder

        return ZebraFotaConnectorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def zebra_fota_deployments(self) -> ZebraFotaDeploymentsRequestBuilder:
        """
        Provides operations to manage the zebraFotaDeployments property of the microsoft.graph.deviceManagement entity.
        """
        from .zebra_fota_deployments.zebra_fota_deployments_request_builder import ZebraFotaDeploymentsRequestBuilder

        return ZebraFotaDeploymentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceManagementRequestBuilderGetQueryParameters():
        """
        Get deviceManagement
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
    class DeviceManagementRequestBuilderGetRequestConfiguration(RequestConfiguration[DeviceManagementRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DeviceManagementRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

