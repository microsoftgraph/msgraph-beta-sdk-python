from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

admin_consent = lazy_import('msgraph.generated.models.admin_consent')
advanced_threat_protection_onboarding_state_summary = lazy_import('msgraph.generated.models.advanced_threat_protection_onboarding_state_summary')
android_device_owner_enrollment_profile = lazy_import('msgraph.generated.models.android_device_owner_enrollment_profile')
android_for_work_app_configuration_schema = lazy_import('msgraph.generated.models.android_for_work_app_configuration_schema')
android_for_work_enrollment_profile = lazy_import('msgraph.generated.models.android_for_work_enrollment_profile')
android_for_work_settings = lazy_import('msgraph.generated.models.android_for_work_settings')
android_managed_store_account_enterprise_settings = lazy_import('msgraph.generated.models.android_managed_store_account_enterprise_settings')
android_managed_store_app_configuration_schema = lazy_import('msgraph.generated.models.android_managed_store_app_configuration_schema')
apple_push_notification_certificate = lazy_import('msgraph.generated.models.apple_push_notification_certificate')
apple_user_initiated_enrollment_profile = lazy_import('msgraph.generated.models.apple_user_initiated_enrollment_profile')
audit_event = lazy_import('msgraph.generated.models.audit_event')
cart_to_class_association = lazy_import('msgraph.generated.models.cart_to_class_association')
certificate_connector_details = lazy_import('msgraph.generated.models.certificate_connector_details')
chrome_o_s_onboarding_settings = lazy_import('msgraph.generated.models.chrome_o_s_onboarding_settings')
cloud_p_c_connectivity_issue = lazy_import('msgraph.generated.models.cloud_p_c_connectivity_issue')
comanagement_eligible_device = lazy_import('msgraph.generated.models.comanagement_eligible_device')
compliance_management_partner = lazy_import('msgraph.generated.models.compliance_management_partner')
config_manager_collection = lazy_import('msgraph.generated.models.config_manager_collection')
data_processor_service_for_windows_features_onboarding = lazy_import('msgraph.generated.models.data_processor_service_for_windows_features_onboarding')
data_sharing_consent = lazy_import('msgraph.generated.models.data_sharing_consent')
dep_onboarding_setting = lazy_import('msgraph.generated.models.dep_onboarding_setting')
detected_app = lazy_import('msgraph.generated.models.detected_app')
device_and_app_management_assignment_filter = lazy_import('msgraph.generated.models.device_and_app_management_assignment_filter')
device_and_app_management_role_assignment = lazy_import('msgraph.generated.models.device_and_app_management_role_assignment')
device_category = lazy_import('msgraph.generated.models.device_category')
device_compliance_policy = lazy_import('msgraph.generated.models.device_compliance_policy')
device_compliance_policy_device_state_summary = lazy_import('msgraph.generated.models.device_compliance_policy_device_state_summary')
device_compliance_policy_setting_state_summary = lazy_import('msgraph.generated.models.device_compliance_policy_setting_state_summary')
device_compliance_script = lazy_import('msgraph.generated.models.device_compliance_script')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
device_configuration_conflict_summary = lazy_import('msgraph.generated.models.device_configuration_conflict_summary')
device_configuration_device_state_summary = lazy_import('msgraph.generated.models.device_configuration_device_state_summary')
device_configuration_user_state_summary = lazy_import('msgraph.generated.models.device_configuration_user_state_summary')
device_custom_attribute_shell_script = lazy_import('msgraph.generated.models.device_custom_attribute_shell_script')
device_enrollment_configuration = lazy_import('msgraph.generated.models.device_enrollment_configuration')
device_health_script = lazy_import('msgraph.generated.models.device_health_script')
device_management_autopilot_event = lazy_import('msgraph.generated.models.device_management_autopilot_event')
device_management_compliance_policy = lazy_import('msgraph.generated.models.device_management_compliance_policy')
device_management_configuration_category = lazy_import('msgraph.generated.models.device_management_configuration_category')
device_management_configuration_policy = lazy_import('msgraph.generated.models.device_management_configuration_policy')
device_management_configuration_policy_template = lazy_import('msgraph.generated.models.device_management_configuration_policy_template')
device_management_configuration_setting_definition = lazy_import('msgraph.generated.models.device_management_configuration_setting_definition')
device_management_configuration_setting_template = lazy_import('msgraph.generated.models.device_management_configuration_setting_template')
device_management_derived_credential_settings = lazy_import('msgraph.generated.models.device_management_derived_credential_settings')
device_management_domain_join_connector = lazy_import('msgraph.generated.models.device_management_domain_join_connector')
device_management_exchange_connector = lazy_import('msgraph.generated.models.device_management_exchange_connector')
device_management_exchange_on_premises_policy = lazy_import('msgraph.generated.models.device_management_exchange_on_premises_policy')
device_management_intent = lazy_import('msgraph.generated.models.device_management_intent')
device_management_partner = lazy_import('msgraph.generated.models.device_management_partner')
device_management_reports = lazy_import('msgraph.generated.models.device_management_reports')
device_management_resource_access_profile_base = lazy_import('msgraph.generated.models.device_management_resource_access_profile_base')
device_management_reusable_policy_setting = lazy_import('msgraph.generated.models.device_management_reusable_policy_setting')
device_management_script = lazy_import('msgraph.generated.models.device_management_script')
device_management_setting_category = lazy_import('msgraph.generated.models.device_management_setting_category')
device_management_setting_definition = lazy_import('msgraph.generated.models.device_management_setting_definition')
device_management_settings = lazy_import('msgraph.generated.models.device_management_settings')
device_management_subscription_state = lazy_import('msgraph.generated.models.device_management_subscription_state')
device_management_subscriptions = lazy_import('msgraph.generated.models.device_management_subscriptions')
device_management_template = lazy_import('msgraph.generated.models.device_management_template')
device_management_troubleshooting_event = lazy_import('msgraph.generated.models.device_management_troubleshooting_event')
device_protection_overview = lazy_import('msgraph.generated.models.device_protection_overview')
device_shell_script = lazy_import('msgraph.generated.models.device_shell_script')
embedded_s_i_m_activation_code_pool = lazy_import('msgraph.generated.models.embedded_s_i_m_activation_code_pool')
entity = lazy_import('msgraph.generated.models.entity')
group_policy_category = lazy_import('msgraph.generated.models.group_policy_category')
group_policy_configuration = lazy_import('msgraph.generated.models.group_policy_configuration')
group_policy_definition = lazy_import('msgraph.generated.models.group_policy_definition')
group_policy_definition_file = lazy_import('msgraph.generated.models.group_policy_definition_file')
group_policy_migration_report = lazy_import('msgraph.generated.models.group_policy_migration_report')
group_policy_object_file = lazy_import('msgraph.generated.models.group_policy_object_file')
group_policy_uploaded_definition_file = lazy_import('msgraph.generated.models.group_policy_uploaded_definition_file')
imported_device_identity = lazy_import('msgraph.generated.models.imported_device_identity')
imported_windows_autopilot_device_identity = lazy_import('msgraph.generated.models.imported_windows_autopilot_device_identity')
intune_brand = lazy_import('msgraph.generated.models.intune_brand')
intune_branding_profile = lazy_import('msgraph.generated.models.intune_branding_profile')
ios_update_device_status = lazy_import('msgraph.generated.models.ios_update_device_status')
mac_o_s_software_update_account_summary = lazy_import('msgraph.generated.models.mac_o_s_software_update_account_summary')
managed_all_device_certificate_state = lazy_import('msgraph.generated.models.managed_all_device_certificate_state')
managed_device = lazy_import('msgraph.generated.models.managed_device')
managed_device_cleanup_settings = lazy_import('msgraph.generated.models.managed_device_cleanup_settings')
managed_device_encryption_state = lazy_import('msgraph.generated.models.managed_device_encryption_state')
managed_device_overview = lazy_import('msgraph.generated.models.managed_device_overview')
microsoft_tunnel_configuration = lazy_import('msgraph.generated.models.microsoft_tunnel_configuration')
microsoft_tunnel_health_threshold = lazy_import('msgraph.generated.models.microsoft_tunnel_health_threshold')
microsoft_tunnel_server_log_collection_response = lazy_import('msgraph.generated.models.microsoft_tunnel_server_log_collection_response')
microsoft_tunnel_site = lazy_import('msgraph.generated.models.microsoft_tunnel_site')
mobile_app_troubleshooting_event = lazy_import('msgraph.generated.models.mobile_app_troubleshooting_event')
mobile_threat_defense_connector = lazy_import('msgraph.generated.models.mobile_threat_defense_connector')
ndes_connector = lazy_import('msgraph.generated.models.ndes_connector')
notification_message_template = lazy_import('msgraph.generated.models.notification_message_template')
oem_warranty_information_onboarding = lazy_import('msgraph.generated.models.oem_warranty_information_onboarding')
on_premises_conditional_access_settings = lazy_import('msgraph.generated.models.on_premises_conditional_access_settings')
remote_action_audit = lazy_import('msgraph.generated.models.remote_action_audit')
remote_assistance_partner = lazy_import('msgraph.generated.models.remote_assistance_partner')
remote_assistance_settings = lazy_import('msgraph.generated.models.remote_assistance_settings')
resource_operation = lazy_import('msgraph.generated.models.resource_operation')
restricted_apps_violation = lazy_import('msgraph.generated.models.restricted_apps_violation')
role_definition = lazy_import('msgraph.generated.models.role_definition')
role_scope_tag = lazy_import('msgraph.generated.models.role_scope_tag')
software_update_status_summary = lazy_import('msgraph.generated.models.software_update_status_summary')
telecom_expense_management_partner = lazy_import('msgraph.generated.models.telecom_expense_management_partner')
tenant_attach_r_b_a_c = lazy_import('msgraph.generated.models.tenant_attach_r_b_a_c')
terms_and_conditions = lazy_import('msgraph.generated.models.terms_and_conditions')
user_experience_analytics_anomaly = lazy_import('msgraph.generated.models.user_experience_analytics_anomaly')
user_experience_analytics_anomaly_device = lazy_import('msgraph.generated.models.user_experience_analytics_anomaly_device')
user_experience_analytics_anomaly_severity_overview = lazy_import('msgraph.generated.models.user_experience_analytics_anomaly_severity_overview')
user_experience_analytics_app_health_app_performance_by_app_version = lazy_import('msgraph.generated.models.user_experience_analytics_app_health_app_performance_by_app_version')
user_experience_analytics_app_health_app_performance_by_app_version_details = lazy_import('msgraph.generated.models.user_experience_analytics_app_health_app_performance_by_app_version_details')
user_experience_analytics_app_health_app_performance_by_app_version_device_id = lazy_import('msgraph.generated.models.user_experience_analytics_app_health_app_performance_by_app_version_device_id')
user_experience_analytics_app_health_app_performance_by_o_s_version = lazy_import('msgraph.generated.models.user_experience_analytics_app_health_app_performance_by_o_s_version')
user_experience_analytics_app_health_application_performance = lazy_import('msgraph.generated.models.user_experience_analytics_app_health_application_performance')
user_experience_analytics_app_health_device_model_performance = lazy_import('msgraph.generated.models.user_experience_analytics_app_health_device_model_performance')
user_experience_analytics_app_health_device_performance = lazy_import('msgraph.generated.models.user_experience_analytics_app_health_device_performance')
user_experience_analytics_app_health_device_performance_details = lazy_import('msgraph.generated.models.user_experience_analytics_app_health_device_performance_details')
user_experience_analytics_app_health_o_s_version_performance = lazy_import('msgraph.generated.models.user_experience_analytics_app_health_o_s_version_performance')
user_experience_analytics_baseline = lazy_import('msgraph.generated.models.user_experience_analytics_baseline')
user_experience_analytics_battery_health_app_impact = lazy_import('msgraph.generated.models.user_experience_analytics_battery_health_app_impact')
user_experience_analytics_battery_health_capacity_details = lazy_import('msgraph.generated.models.user_experience_analytics_battery_health_capacity_details')
user_experience_analytics_battery_health_device_app_impact = lazy_import('msgraph.generated.models.user_experience_analytics_battery_health_device_app_impact')
user_experience_analytics_battery_health_device_performance = lazy_import('msgraph.generated.models.user_experience_analytics_battery_health_device_performance')
user_experience_analytics_battery_health_device_runtime_history = lazy_import('msgraph.generated.models.user_experience_analytics_battery_health_device_runtime_history')
user_experience_analytics_battery_health_model_performance = lazy_import('msgraph.generated.models.user_experience_analytics_battery_health_model_performance')
user_experience_analytics_battery_health_os_performance = lazy_import('msgraph.generated.models.user_experience_analytics_battery_health_os_performance')
user_experience_analytics_battery_health_runtime_details = lazy_import('msgraph.generated.models.user_experience_analytics_battery_health_runtime_details')
user_experience_analytics_category = lazy_import('msgraph.generated.models.user_experience_analytics_category')
user_experience_analytics_device_performance = lazy_import('msgraph.generated.models.user_experience_analytics_device_performance')
user_experience_analytics_device_scope = lazy_import('msgraph.generated.models.user_experience_analytics_device_scope')
user_experience_analytics_device_scores = lazy_import('msgraph.generated.models.user_experience_analytics_device_scores')
user_experience_analytics_device_startup_history = lazy_import('msgraph.generated.models.user_experience_analytics_device_startup_history')
user_experience_analytics_device_startup_process = lazy_import('msgraph.generated.models.user_experience_analytics_device_startup_process')
user_experience_analytics_device_startup_process_performance = lazy_import('msgraph.generated.models.user_experience_analytics_device_startup_process_performance')
user_experience_analytics_device_without_cloud_identity = lazy_import('msgraph.generated.models.user_experience_analytics_device_without_cloud_identity')
user_experience_analytics_impacting_process = lazy_import('msgraph.generated.models.user_experience_analytics_impacting_process')
user_experience_analytics_metric_history = lazy_import('msgraph.generated.models.user_experience_analytics_metric_history')
user_experience_analytics_model_scores = lazy_import('msgraph.generated.models.user_experience_analytics_model_scores')
user_experience_analytics_not_autopilot_ready_device = lazy_import('msgraph.generated.models.user_experience_analytics_not_autopilot_ready_device')
user_experience_analytics_overview = lazy_import('msgraph.generated.models.user_experience_analytics_overview')
user_experience_analytics_remote_connection = lazy_import('msgraph.generated.models.user_experience_analytics_remote_connection')
user_experience_analytics_resource_performance = lazy_import('msgraph.generated.models.user_experience_analytics_resource_performance')
user_experience_analytics_score_history = lazy_import('msgraph.generated.models.user_experience_analytics_score_history')
user_experience_analytics_settings = lazy_import('msgraph.generated.models.user_experience_analytics_settings')
user_experience_analytics_work_from_anywhere_hardware_readiness_metric = lazy_import('msgraph.generated.models.user_experience_analytics_work_from_anywhere_hardware_readiness_metric')
user_experience_analytics_work_from_anywhere_metric = lazy_import('msgraph.generated.models.user_experience_analytics_work_from_anywhere_metric')
user_experience_analytics_work_from_anywhere_model_performance = lazy_import('msgraph.generated.models.user_experience_analytics_work_from_anywhere_model_performance')
user_p_f_x_certificate = lazy_import('msgraph.generated.models.user_p_f_x_certificate')
virtual_endpoint = lazy_import('msgraph.generated.models.virtual_endpoint')
windows_autopilot_deployment_profile = lazy_import('msgraph.generated.models.windows_autopilot_deployment_profile')
windows_autopilot_device_identity = lazy_import('msgraph.generated.models.windows_autopilot_device_identity')
windows_autopilot_settings = lazy_import('msgraph.generated.models.windows_autopilot_settings')
windows_driver_update_profile = lazy_import('msgraph.generated.models.windows_driver_update_profile')
windows_feature_update_profile = lazy_import('msgraph.generated.models.windows_feature_update_profile')
windows_information_protection_app_learning_summary = lazy_import('msgraph.generated.models.windows_information_protection_app_learning_summary')
windows_information_protection_network_learning_summary = lazy_import('msgraph.generated.models.windows_information_protection_network_learning_summary')
windows_malware_information = lazy_import('msgraph.generated.models.windows_malware_information')
windows_malware_overview = lazy_import('msgraph.generated.models.windows_malware_overview')
windows_quality_update_profile = lazy_import('msgraph.generated.models.windows_quality_update_profile')
windows_update_catalog_item = lazy_import('msgraph.generated.models.windows_update_catalog_item')
zebra_fota_artifact = lazy_import('msgraph.generated.models.zebra_fota_artifact')
zebra_fota_connector = lazy_import('msgraph.generated.models.zebra_fota_connector')
zebra_fota_deployment = lazy_import('msgraph.generated.models.zebra_fota_deployment')
monitoring = lazy_import('msgraph.generated.models.device_management.monitoring')

class DeviceManagement(entity.Entity):
    @property
    def account_move_completion_date_time(self,) -> Optional[datetime]:
        """
        Gets the accountMoveCompletionDateTime property value. The date & time when tenant data moved between scaleunits.
        Returns: Optional[datetime]
        """
        return self._account_move_completion_date_time
    
    @account_move_completion_date_time.setter
    def account_move_completion_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the accountMoveCompletionDateTime property value. The date & time when tenant data moved between scaleunits.
        Args:
            value: Value to set for the accountMoveCompletionDateTime property.
        """
        self._account_move_completion_date_time = value
    
    @property
    def admin_consent(self,) -> Optional[admin_consent.AdminConsent]:
        """
        Gets the adminConsent property value. Admin consent information.
        Returns: Optional[admin_consent.AdminConsent]
        """
        return self._admin_consent
    
    @admin_consent.setter
    def admin_consent(self,value: Optional[admin_consent.AdminConsent] = None) -> None:
        """
        Sets the adminConsent property value. Admin consent information.
        Args:
            value: Value to set for the adminConsent property.
        """
        self._admin_consent = value
    
    @property
    def advanced_threat_protection_onboarding_state_summary(self,) -> Optional[advanced_threat_protection_onboarding_state_summary.AdvancedThreatProtectionOnboardingStateSummary]:
        """
        Gets the advancedThreatProtectionOnboardingStateSummary property value. The summary state of ATP onboarding state for this account.
        Returns: Optional[advanced_threat_protection_onboarding_state_summary.AdvancedThreatProtectionOnboardingStateSummary]
        """
        return self._advanced_threat_protection_onboarding_state_summary
    
    @advanced_threat_protection_onboarding_state_summary.setter
    def advanced_threat_protection_onboarding_state_summary(self,value: Optional[advanced_threat_protection_onboarding_state_summary.AdvancedThreatProtectionOnboardingStateSummary] = None) -> None:
        """
        Sets the advancedThreatProtectionOnboardingStateSummary property value. The summary state of ATP onboarding state for this account.
        Args:
            value: Value to set for the advancedThreatProtectionOnboardingStateSummary property.
        """
        self._advanced_threat_protection_onboarding_state_summary = value
    
    @property
    def android_device_owner_enrollment_profiles(self,) -> Optional[List[android_device_owner_enrollment_profile.AndroidDeviceOwnerEnrollmentProfile]]:
        """
        Gets the androidDeviceOwnerEnrollmentProfiles property value. Android device owner enrollment profile entities.
        Returns: Optional[List[android_device_owner_enrollment_profile.AndroidDeviceOwnerEnrollmentProfile]]
        """
        return self._android_device_owner_enrollment_profiles
    
    @android_device_owner_enrollment_profiles.setter
    def android_device_owner_enrollment_profiles(self,value: Optional[List[android_device_owner_enrollment_profile.AndroidDeviceOwnerEnrollmentProfile]] = None) -> None:
        """
        Sets the androidDeviceOwnerEnrollmentProfiles property value. Android device owner enrollment profile entities.
        Args:
            value: Value to set for the androidDeviceOwnerEnrollmentProfiles property.
        """
        self._android_device_owner_enrollment_profiles = value
    
    @property
    def android_for_work_app_configuration_schemas(self,) -> Optional[List[android_for_work_app_configuration_schema.AndroidForWorkAppConfigurationSchema]]:
        """
        Gets the androidForWorkAppConfigurationSchemas property value. Android for Work app configuration schema entities.
        Returns: Optional[List[android_for_work_app_configuration_schema.AndroidForWorkAppConfigurationSchema]]
        """
        return self._android_for_work_app_configuration_schemas
    
    @android_for_work_app_configuration_schemas.setter
    def android_for_work_app_configuration_schemas(self,value: Optional[List[android_for_work_app_configuration_schema.AndroidForWorkAppConfigurationSchema]] = None) -> None:
        """
        Sets the androidForWorkAppConfigurationSchemas property value. Android for Work app configuration schema entities.
        Args:
            value: Value to set for the androidForWorkAppConfigurationSchemas property.
        """
        self._android_for_work_app_configuration_schemas = value
    
    @property
    def android_for_work_enrollment_profiles(self,) -> Optional[List[android_for_work_enrollment_profile.AndroidForWorkEnrollmentProfile]]:
        """
        Gets the androidForWorkEnrollmentProfiles property value. Android for Work enrollment profile entities.
        Returns: Optional[List[android_for_work_enrollment_profile.AndroidForWorkEnrollmentProfile]]
        """
        return self._android_for_work_enrollment_profiles
    
    @android_for_work_enrollment_profiles.setter
    def android_for_work_enrollment_profiles(self,value: Optional[List[android_for_work_enrollment_profile.AndroidForWorkEnrollmentProfile]] = None) -> None:
        """
        Sets the androidForWorkEnrollmentProfiles property value. Android for Work enrollment profile entities.
        Args:
            value: Value to set for the androidForWorkEnrollmentProfiles property.
        """
        self._android_for_work_enrollment_profiles = value
    
    @property
    def android_for_work_settings(self,) -> Optional[android_for_work_settings.AndroidForWorkSettings]:
        """
        Gets the androidForWorkSettings property value. The singleton Android for Work settings entity.
        Returns: Optional[android_for_work_settings.AndroidForWorkSettings]
        """
        return self._android_for_work_settings
    
    @android_for_work_settings.setter
    def android_for_work_settings(self,value: Optional[android_for_work_settings.AndroidForWorkSettings] = None) -> None:
        """
        Sets the androidForWorkSettings property value. The singleton Android for Work settings entity.
        Args:
            value: Value to set for the androidForWorkSettings property.
        """
        self._android_for_work_settings = value
    
    @property
    def android_managed_store_account_enterprise_settings(self,) -> Optional[android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings]:
        """
        Gets the androidManagedStoreAccountEnterpriseSettings property value. The singleton Android managed store account enterprise settings entity.
        Returns: Optional[android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings]
        """
        return self._android_managed_store_account_enterprise_settings
    
    @android_managed_store_account_enterprise_settings.setter
    def android_managed_store_account_enterprise_settings(self,value: Optional[android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings] = None) -> None:
        """
        Sets the androidManagedStoreAccountEnterpriseSettings property value. The singleton Android managed store account enterprise settings entity.
        Args:
            value: Value to set for the androidManagedStoreAccountEnterpriseSettings property.
        """
        self._android_managed_store_account_enterprise_settings = value
    
    @property
    def android_managed_store_app_configuration_schemas(self,) -> Optional[List[android_managed_store_app_configuration_schema.AndroidManagedStoreAppConfigurationSchema]]:
        """
        Gets the androidManagedStoreAppConfigurationSchemas property value. Android Enterprise app configuration schema entities.
        Returns: Optional[List[android_managed_store_app_configuration_schema.AndroidManagedStoreAppConfigurationSchema]]
        """
        return self._android_managed_store_app_configuration_schemas
    
    @android_managed_store_app_configuration_schemas.setter
    def android_managed_store_app_configuration_schemas(self,value: Optional[List[android_managed_store_app_configuration_schema.AndroidManagedStoreAppConfigurationSchema]] = None) -> None:
        """
        Sets the androidManagedStoreAppConfigurationSchemas property value. Android Enterprise app configuration schema entities.
        Args:
            value: Value to set for the androidManagedStoreAppConfigurationSchemas property.
        """
        self._android_managed_store_app_configuration_schemas = value
    
    @property
    def apple_push_notification_certificate(self,) -> Optional[apple_push_notification_certificate.ApplePushNotificationCertificate]:
        """
        Gets the applePushNotificationCertificate property value. Apple push notification certificate.
        Returns: Optional[apple_push_notification_certificate.ApplePushNotificationCertificate]
        """
        return self._apple_push_notification_certificate
    
    @apple_push_notification_certificate.setter
    def apple_push_notification_certificate(self,value: Optional[apple_push_notification_certificate.ApplePushNotificationCertificate] = None) -> None:
        """
        Sets the applePushNotificationCertificate property value. Apple push notification certificate.
        Args:
            value: Value to set for the applePushNotificationCertificate property.
        """
        self._apple_push_notification_certificate = value
    
    @property
    def apple_user_initiated_enrollment_profiles(self,) -> Optional[List[apple_user_initiated_enrollment_profile.AppleUserInitiatedEnrollmentProfile]]:
        """
        Gets the appleUserInitiatedEnrollmentProfiles property value. Apple user initiated enrollment profiles
        Returns: Optional[List[apple_user_initiated_enrollment_profile.AppleUserInitiatedEnrollmentProfile]]
        """
        return self._apple_user_initiated_enrollment_profiles
    
    @apple_user_initiated_enrollment_profiles.setter
    def apple_user_initiated_enrollment_profiles(self,value: Optional[List[apple_user_initiated_enrollment_profile.AppleUserInitiatedEnrollmentProfile]] = None) -> None:
        """
        Sets the appleUserInitiatedEnrollmentProfiles property value. Apple user initiated enrollment profiles
        Args:
            value: Value to set for the appleUserInitiatedEnrollmentProfiles property.
        """
        self._apple_user_initiated_enrollment_profiles = value
    
    @property
    def assignment_filters(self,) -> Optional[List[device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter]]:
        """
        Gets the assignmentFilters property value. The list of assignment filters
        Returns: Optional[List[device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter]]
        """
        return self._assignment_filters
    
    @assignment_filters.setter
    def assignment_filters(self,value: Optional[List[device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter]] = None) -> None:
        """
        Sets the assignmentFilters property value. The list of assignment filters
        Args:
            value: Value to set for the assignmentFilters property.
        """
        self._assignment_filters = value
    
    @property
    def audit_events(self,) -> Optional[List[audit_event.AuditEvent]]:
        """
        Gets the auditEvents property value. The Audit Events
        Returns: Optional[List[audit_event.AuditEvent]]
        """
        return self._audit_events
    
    @audit_events.setter
    def audit_events(self,value: Optional[List[audit_event.AuditEvent]] = None) -> None:
        """
        Sets the auditEvents property value. The Audit Events
        Args:
            value: Value to set for the auditEvents property.
        """
        self._audit_events = value
    
    @property
    def autopilot_events(self,) -> Optional[List[device_management_autopilot_event.DeviceManagementAutopilotEvent]]:
        """
        Gets the autopilotEvents property value. The list of autopilot events for the tenant.
        Returns: Optional[List[device_management_autopilot_event.DeviceManagementAutopilotEvent]]
        """
        return self._autopilot_events
    
    @autopilot_events.setter
    def autopilot_events(self,value: Optional[List[device_management_autopilot_event.DeviceManagementAutopilotEvent]] = None) -> None:
        """
        Sets the autopilotEvents property value. The list of autopilot events for the tenant.
        Args:
            value: Value to set for the autopilotEvents property.
        """
        self._autopilot_events = value
    
    @property
    def cart_to_class_associations(self,) -> Optional[List[cart_to_class_association.CartToClassAssociation]]:
        """
        Gets the cartToClassAssociations property value. The Cart To Class Associations.
        Returns: Optional[List[cart_to_class_association.CartToClassAssociation]]
        """
        return self._cart_to_class_associations
    
    @cart_to_class_associations.setter
    def cart_to_class_associations(self,value: Optional[List[cart_to_class_association.CartToClassAssociation]] = None) -> None:
        """
        Sets the cartToClassAssociations property value. The Cart To Class Associations.
        Args:
            value: Value to set for the cartToClassAssociations property.
        """
        self._cart_to_class_associations = value
    
    @property
    def categories(self,) -> Optional[List[device_management_setting_category.DeviceManagementSettingCategory]]:
        """
        Gets the categories property value. The available categories
        Returns: Optional[List[device_management_setting_category.DeviceManagementSettingCategory]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[device_management_setting_category.DeviceManagementSettingCategory]] = None) -> None:
        """
        Sets the categories property value. The available categories
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    @property
    def certificate_connector_details(self,) -> Optional[List[certificate_connector_details.CertificateConnectorDetails]]:
        """
        Gets the certificateConnectorDetails property value. Collection of certificate connector details, each associated with a corresponding Intune Certificate Connector.
        Returns: Optional[List[certificate_connector_details.CertificateConnectorDetails]]
        """
        return self._certificate_connector_details
    
    @certificate_connector_details.setter
    def certificate_connector_details(self,value: Optional[List[certificate_connector_details.CertificateConnectorDetails]] = None) -> None:
        """
        Sets the certificateConnectorDetails property value. Collection of certificate connector details, each associated with a corresponding Intune Certificate Connector.
        Args:
            value: Value to set for the certificateConnectorDetails property.
        """
        self._certificate_connector_details = value
    
    @property
    def chrome_o_s_onboarding_settings(self,) -> Optional[List[chrome_o_s_onboarding_settings.ChromeOSOnboardingSettings]]:
        """
        Gets the chromeOSOnboardingSettings property value. Collection of ChromeOSOnboardingSettings settings associated with account.
        Returns: Optional[List[chrome_o_s_onboarding_settings.ChromeOSOnboardingSettings]]
        """
        return self._chrome_o_s_onboarding_settings
    
    @chrome_o_s_onboarding_settings.setter
    def chrome_o_s_onboarding_settings(self,value: Optional[List[chrome_o_s_onboarding_settings.ChromeOSOnboardingSettings]] = None) -> None:
        """
        Sets the chromeOSOnboardingSettings property value. Collection of ChromeOSOnboardingSettings settings associated with account.
        Args:
            value: Value to set for the chromeOSOnboardingSettings property.
        """
        self._chrome_o_s_onboarding_settings = value
    
    @property
    def cloud_p_c_connectivity_issues(self,) -> Optional[List[cloud_p_c_connectivity_issue.CloudPCConnectivityIssue]]:
        """
        Gets the cloudPCConnectivityIssues property value. The list of CloudPC Connectivity Issue.
        Returns: Optional[List[cloud_p_c_connectivity_issue.CloudPCConnectivityIssue]]
        """
        return self._cloud_p_c_connectivity_issues
    
    @cloud_p_c_connectivity_issues.setter
    def cloud_p_c_connectivity_issues(self,value: Optional[List[cloud_p_c_connectivity_issue.CloudPCConnectivityIssue]] = None) -> None:
        """
        Sets the cloudPCConnectivityIssues property value. The list of CloudPC Connectivity Issue.
        Args:
            value: Value to set for the cloudPCConnectivityIssues property.
        """
        self._cloud_p_c_connectivity_issues = value
    
    @property
    def comanaged_devices(self,) -> Optional[List[managed_device.ManagedDevice]]:
        """
        Gets the comanagedDevices property value. The list of co-managed devices report
        Returns: Optional[List[managed_device.ManagedDevice]]
        """
        return self._comanaged_devices
    
    @comanaged_devices.setter
    def comanaged_devices(self,value: Optional[List[managed_device.ManagedDevice]] = None) -> None:
        """
        Sets the comanagedDevices property value. The list of co-managed devices report
        Args:
            value: Value to set for the comanagedDevices property.
        """
        self._comanaged_devices = value
    
    @property
    def comanagement_eligible_devices(self,) -> Optional[List[comanagement_eligible_device.ComanagementEligibleDevice]]:
        """
        Gets the comanagementEligibleDevices property value. The list of co-management eligible devices report
        Returns: Optional[List[comanagement_eligible_device.ComanagementEligibleDevice]]
        """
        return self._comanagement_eligible_devices
    
    @comanagement_eligible_devices.setter
    def comanagement_eligible_devices(self,value: Optional[List[comanagement_eligible_device.ComanagementEligibleDevice]] = None) -> None:
        """
        Sets the comanagementEligibleDevices property value. The list of co-management eligible devices report
        Args:
            value: Value to set for the comanagementEligibleDevices property.
        """
        self._comanagement_eligible_devices = value
    
    @property
    def compliance_categories(self,) -> Optional[List[device_management_configuration_category.DeviceManagementConfigurationCategory]]:
        """
        Gets the complianceCategories property value. List of all compliance categories
        Returns: Optional[List[device_management_configuration_category.DeviceManagementConfigurationCategory]]
        """
        return self._compliance_categories
    
    @compliance_categories.setter
    def compliance_categories(self,value: Optional[List[device_management_configuration_category.DeviceManagementConfigurationCategory]] = None) -> None:
        """
        Sets the complianceCategories property value. List of all compliance categories
        Args:
            value: Value to set for the complianceCategories property.
        """
        self._compliance_categories = value
    
    @property
    def compliance_management_partners(self,) -> Optional[List[compliance_management_partner.ComplianceManagementPartner]]:
        """
        Gets the complianceManagementPartners property value. The list of Compliance Management Partners configured by the tenant.
        Returns: Optional[List[compliance_management_partner.ComplianceManagementPartner]]
        """
        return self._compliance_management_partners
    
    @compliance_management_partners.setter
    def compliance_management_partners(self,value: Optional[List[compliance_management_partner.ComplianceManagementPartner]] = None) -> None:
        """
        Sets the complianceManagementPartners property value. The list of Compliance Management Partners configured by the tenant.
        Args:
            value: Value to set for the complianceManagementPartners property.
        """
        self._compliance_management_partners = value
    
    @property
    def compliance_policies(self,) -> Optional[List[device_management_compliance_policy.DeviceManagementCompliancePolicy]]:
        """
        Gets the compliancePolicies property value. List of all compliance policies
        Returns: Optional[List[device_management_compliance_policy.DeviceManagementCompliancePolicy]]
        """
        return self._compliance_policies
    
    @compliance_policies.setter
    def compliance_policies(self,value: Optional[List[device_management_compliance_policy.DeviceManagementCompliancePolicy]] = None) -> None:
        """
        Sets the compliancePolicies property value. List of all compliance policies
        Args:
            value: Value to set for the compliancePolicies property.
        """
        self._compliance_policies = value
    
    @property
    def compliance_settings(self,) -> Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]]:
        """
        Gets the complianceSettings property value. List of all ComplianceSettings
        Returns: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]]
        """
        return self._compliance_settings
    
    @compliance_settings.setter
    def compliance_settings(self,value: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None) -> None:
        """
        Sets the complianceSettings property value. List of all ComplianceSettings
        Args:
            value: Value to set for the complianceSettings property.
        """
        self._compliance_settings = value
    
    @property
    def conditional_access_settings(self,) -> Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings]:
        """
        Gets the conditionalAccessSettings property value. The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
        Returns: Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings]
        """
        return self._conditional_access_settings
    
    @conditional_access_settings.setter
    def conditional_access_settings(self,value: Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings] = None) -> None:
        """
        Sets the conditionalAccessSettings property value. The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
        Args:
            value: Value to set for the conditionalAccessSettings property.
        """
        self._conditional_access_settings = value
    
    @property
    def config_manager_collections(self,) -> Optional[List[config_manager_collection.ConfigManagerCollection]]:
        """
        Gets the configManagerCollections property value. A list of ConfigManagerCollection
        Returns: Optional[List[config_manager_collection.ConfigManagerCollection]]
        """
        return self._config_manager_collections
    
    @config_manager_collections.setter
    def config_manager_collections(self,value: Optional[List[config_manager_collection.ConfigManagerCollection]] = None) -> None:
        """
        Sets the configManagerCollections property value. A list of ConfigManagerCollection
        Args:
            value: Value to set for the configManagerCollections property.
        """
        self._config_manager_collections = value
    
    @property
    def configuration_categories(self,) -> Optional[List[device_management_configuration_category.DeviceManagementConfigurationCategory]]:
        """
        Gets the configurationCategories property value. List of all Configuration Categories
        Returns: Optional[List[device_management_configuration_category.DeviceManagementConfigurationCategory]]
        """
        return self._configuration_categories
    
    @configuration_categories.setter
    def configuration_categories(self,value: Optional[List[device_management_configuration_category.DeviceManagementConfigurationCategory]] = None) -> None:
        """
        Sets the configurationCategories property value. List of all Configuration Categories
        Args:
            value: Value to set for the configurationCategories property.
        """
        self._configuration_categories = value
    
    @property
    def configuration_policies(self,) -> Optional[List[device_management_configuration_policy.DeviceManagementConfigurationPolicy]]:
        """
        Gets the configurationPolicies property value. List of all Configuration policies
        Returns: Optional[List[device_management_configuration_policy.DeviceManagementConfigurationPolicy]]
        """
        return self._configuration_policies
    
    @configuration_policies.setter
    def configuration_policies(self,value: Optional[List[device_management_configuration_policy.DeviceManagementConfigurationPolicy]] = None) -> None:
        """
        Sets the configurationPolicies property value. List of all Configuration policies
        Args:
            value: Value to set for the configurationPolicies property.
        """
        self._configuration_policies = value
    
    @property
    def configuration_policy_templates(self,) -> Optional[List[device_management_configuration_policy_template.DeviceManagementConfigurationPolicyTemplate]]:
        """
        Gets the configurationPolicyTemplates property value. List of all templates
        Returns: Optional[List[device_management_configuration_policy_template.DeviceManagementConfigurationPolicyTemplate]]
        """
        return self._configuration_policy_templates
    
    @configuration_policy_templates.setter
    def configuration_policy_templates(self,value: Optional[List[device_management_configuration_policy_template.DeviceManagementConfigurationPolicyTemplate]] = None) -> None:
        """
        Sets the configurationPolicyTemplates property value. List of all templates
        Args:
            value: Value to set for the configurationPolicyTemplates property.
        """
        self._configuration_policy_templates = value
    
    @property
    def configuration_settings(self,) -> Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]]:
        """
        Gets the configurationSettings property value. List of all ConfigurationSettings
        Returns: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]]
        """
        return self._configuration_settings
    
    @configuration_settings.setter
    def configuration_settings(self,value: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None) -> None:
        """
        Sets the configurationSettings property value. List of all ConfigurationSettings
        Args:
            value: Value to set for the configurationSettings property.
        """
        self._configuration_settings = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagement and sets the default values.
        """
        super().__init__()
        # The date & time when tenant data moved between scaleunits.
        self._account_move_completion_date_time: Optional[datetime] = None
        # Admin consent information.
        self._admin_consent: Optional[admin_consent.AdminConsent] = None
        # The summary state of ATP onboarding state for this account.
        self._advanced_threat_protection_onboarding_state_summary: Optional[advanced_threat_protection_onboarding_state_summary.AdvancedThreatProtectionOnboardingStateSummary] = None
        # Android device owner enrollment profile entities.
        self._android_device_owner_enrollment_profiles: Optional[List[android_device_owner_enrollment_profile.AndroidDeviceOwnerEnrollmentProfile]] = None
        # Android for Work app configuration schema entities.
        self._android_for_work_app_configuration_schemas: Optional[List[android_for_work_app_configuration_schema.AndroidForWorkAppConfigurationSchema]] = None
        # Android for Work enrollment profile entities.
        self._android_for_work_enrollment_profiles: Optional[List[android_for_work_enrollment_profile.AndroidForWorkEnrollmentProfile]] = None
        # The singleton Android for Work settings entity.
        self._android_for_work_settings: Optional[android_for_work_settings.AndroidForWorkSettings] = None
        # The singleton Android managed store account enterprise settings entity.
        self._android_managed_store_account_enterprise_settings: Optional[android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings] = None
        # Android Enterprise app configuration schema entities.
        self._android_managed_store_app_configuration_schemas: Optional[List[android_managed_store_app_configuration_schema.AndroidManagedStoreAppConfigurationSchema]] = None
        # Apple push notification certificate.
        self._apple_push_notification_certificate: Optional[apple_push_notification_certificate.ApplePushNotificationCertificate] = None
        # Apple user initiated enrollment profiles
        self._apple_user_initiated_enrollment_profiles: Optional[List[apple_user_initiated_enrollment_profile.AppleUserInitiatedEnrollmentProfile]] = None
        # The list of assignment filters
        self._assignment_filters: Optional[List[device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter]] = None
        # The Audit Events
        self._audit_events: Optional[List[audit_event.AuditEvent]] = None
        # The list of autopilot events for the tenant.
        self._autopilot_events: Optional[List[device_management_autopilot_event.DeviceManagementAutopilotEvent]] = None
        # The Cart To Class Associations.
        self._cart_to_class_associations: Optional[List[cart_to_class_association.CartToClassAssociation]] = None
        # The available categories
        self._categories: Optional[List[device_management_setting_category.DeviceManagementSettingCategory]] = None
        # Collection of certificate connector details, each associated with a corresponding Intune Certificate Connector.
        self._certificate_connector_details: Optional[List[certificate_connector_details.CertificateConnectorDetails]] = None
        # Collection of ChromeOSOnboardingSettings settings associated with account.
        self._chrome_o_s_onboarding_settings: Optional[List[chrome_o_s_onboarding_settings.ChromeOSOnboardingSettings]] = None
        # The list of CloudPC Connectivity Issue.
        self._cloud_p_c_connectivity_issues: Optional[List[cloud_p_c_connectivity_issue.CloudPCConnectivityIssue]] = None
        # The list of co-managed devices report
        self._comanaged_devices: Optional[List[managed_device.ManagedDevice]] = None
        # The list of co-management eligible devices report
        self._comanagement_eligible_devices: Optional[List[comanagement_eligible_device.ComanagementEligibleDevice]] = None
        # List of all compliance categories
        self._compliance_categories: Optional[List[device_management_configuration_category.DeviceManagementConfigurationCategory]] = None
        # The list of Compliance Management Partners configured by the tenant.
        self._compliance_management_partners: Optional[List[compliance_management_partner.ComplianceManagementPartner]] = None
        # List of all compliance policies
        self._compliance_policies: Optional[List[device_management_compliance_policy.DeviceManagementCompliancePolicy]] = None
        # List of all ComplianceSettings
        self._compliance_settings: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None
        # The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
        self._conditional_access_settings: Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings] = None
        # A list of ConfigManagerCollection
        self._config_manager_collections: Optional[List[config_manager_collection.ConfigManagerCollection]] = None
        # List of all Configuration Categories
        self._configuration_categories: Optional[List[device_management_configuration_category.DeviceManagementConfigurationCategory]] = None
        # List of all Configuration policies
        self._configuration_policies: Optional[List[device_management_configuration_policy.DeviceManagementConfigurationPolicy]] = None
        # List of all templates
        self._configuration_policy_templates: Optional[List[device_management_configuration_policy_template.DeviceManagementConfigurationPolicyTemplate]] = None
        # List of all ConfigurationSettings
        self._configuration_settings: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None
        # A configuration entity for MEM features that utilize Data Processor Service for Windows (DPSW) data.
        self._data_processor_service_for_windows_features_onboarding: Optional[data_processor_service_for_windows_features_onboarding.DataProcessorServiceForWindowsFeaturesOnboarding] = None
        # Data sharing consents.
        self._data_sharing_consents: Optional[List[data_sharing_consent.DataSharingConsent]] = None
        # This collections of multiple DEP tokens per-tenant.
        self._dep_onboarding_settings: Optional[List[dep_onboarding_setting.DepOnboardingSetting]] = None
        # Collection of Derived credential settings associated with account.
        self._derived_credentials: Optional[List[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]] = None
        # The list of detected apps associated with a device.
        self._detected_apps: Optional[List[detected_app.DetectedApp]] = None
        # The list of device categories with the tenant.
        self._device_categories: Optional[List[device_category.DeviceCategory]] = None
        # The device compliance policies.
        self._device_compliance_policies: Optional[List[device_compliance_policy.DeviceCompliancePolicy]] = None
        # The device compliance state summary for this account.
        self._device_compliance_policy_device_state_summary: Optional[device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary] = None
        # The summary states of compliance policy settings for this account.
        self._device_compliance_policy_setting_state_summaries: Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]] = None
        # The last requested time of device compliance reporting for this account. This property is read-only.
        self._device_compliance_report_summarization_date_time: Optional[datetime] = None
        # The list of device compliance scripts associated with the tenant.
        self._device_compliance_scripts: Optional[List[device_compliance_script.DeviceComplianceScript]] = None
        # Summary of policies in conflict state for this account.
        self._device_configuration_conflict_summary: Optional[List[device_configuration_conflict_summary.DeviceConfigurationConflictSummary]] = None
        # The device configuration device state summary for this account.
        self._device_configuration_device_state_summaries: Optional[device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary] = None
        # Restricted apps violations for this account.
        self._device_configuration_restricted_apps_violations: Optional[List[restricted_apps_violation.RestrictedAppsViolation]] = None
        # The device configurations.
        self._device_configurations: Optional[List[device_configuration.DeviceConfiguration]] = None
        # Summary of all certificates for all devices.
        self._device_configurations_all_managed_device_certificate_states: Optional[List[managed_all_device_certificate_state.ManagedAllDeviceCertificateState]] = None
        # The device configuration user state summary for this account.
        self._device_configuration_user_state_summaries: Optional[device_configuration_user_state_summary.DeviceConfigurationUserStateSummary] = None
        # The list of device custom attribute shell scripts associated with the tenant.
        self._device_custom_attribute_shell_scripts: Optional[List[device_custom_attribute_shell_script.DeviceCustomAttributeShellScript]] = None
        # The list of device enrollment configurations
        self._device_enrollment_configurations: Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]] = None
        # The list of device health scripts associated with the tenant.
        self._device_health_scripts: Optional[List[device_health_script.DeviceHealthScript]] = None
        # The list of Device Management Partners configured by the tenant.
        self._device_management_partners: Optional[List[device_management_partner.DeviceManagementPartner]] = None
        # The list of device management scripts associated with the tenant.
        self._device_management_scripts: Optional[List[device_management_script.DeviceManagementScript]] = None
        # Device protection overview.
        self._device_protection_overview: Optional[device_protection_overview.DeviceProtectionOverview] = None
        # The list of device shell scripts associated with the tenant.
        self._device_shell_scripts: Optional[List[device_shell_script.DeviceShellScript]] = None
        # A list of connector objects.
        self._domain_join_connectors: Optional[List[device_management_domain_join_connector.DeviceManagementDomainJoinConnector]] = None
        # The embedded SIM activation code pools created by this account.
        self._embedded_s_i_m_activation_code_pools: Optional[List[embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool]] = None
        # The list of Exchange Connectors configured by the tenant.
        self._exchange_connectors: Optional[List[device_management_exchange_connector.DeviceManagementExchangeConnector]] = None
        # The list of Exchange On Premisis policies configured by the tenant.
        self._exchange_on_premises_policies: Optional[List[device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy]] = None
        # The policy which controls mobile device access to Exchange On Premises
        self._exchange_on_premises_policy: Optional[device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy] = None
        # The available group policy categories for this account.
        self._group_policy_categories: Optional[List[group_policy_category.GroupPolicyCategory]] = None
        # The group policy configurations created by this account.
        self._group_policy_configurations: Optional[List[group_policy_configuration.GroupPolicyConfiguration]] = None
        # The available group policy definition files for this account.
        self._group_policy_definition_files: Optional[List[group_policy_definition_file.GroupPolicyDefinitionFile]] = None
        # The available group policy definitions for this account.
        self._group_policy_definitions: Optional[List[group_policy_definition.GroupPolicyDefinition]] = None
        # A list of Group Policy migration reports.
        self._group_policy_migration_reports: Optional[List[group_policy_migration_report.GroupPolicyMigrationReport]] = None
        # A list of Group Policy Object files uploaded.
        self._group_policy_object_files: Optional[List[group_policy_object_file.GroupPolicyObjectFile]] = None
        # The available group policy uploaded definition files for this account.
        self._group_policy_uploaded_definition_files: Optional[List[group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile]] = None
        # The imported device identities.
        self._imported_device_identities: Optional[List[imported_device_identity.ImportedDeviceIdentity]] = None
        # Collection of imported Windows autopilot devices.
        self._imported_windows_autopilot_device_identities: Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]] = None
        # The device management intents
        self._intents: Optional[List[device_management_intent.DeviceManagementIntent]] = None
        # Intune Account ID for given tenant
        self._intune_account_id: Optional[Guid] = None
        # intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
        self._intune_brand: Optional[intune_brand.IntuneBrand] = None
        # Intune branding profiles targeted to AAD groups
        self._intune_branding_profiles: Optional[List[intune_branding_profile.IntuneBrandingProfile]] = None
        # The IOS software update installation statuses for this account.
        self._ios_update_statuses: Optional[List[ios_update_device_status.IosUpdateDeviceStatus]] = None
        # The last modified time of reporting for this account. This property is read-only.
        self._last_report_aggregation_date_time: Optional[datetime] = None
        # The property to enable Non-MDM managed legacy PC management for this account. This property is read-only.
        self._legacy_pc_manangement_enabled: Optional[bool] = None
        # The MacOS software update account summaries for this account.
        self._mac_o_s_software_update_account_summaries: Optional[List[mac_o_s_software_update_account_summary.MacOSSoftwareUpdateAccountSummary]] = None
        # Device cleanup rule
        self._managed_device_cleanup_settings: Optional[managed_device_cleanup_settings.ManagedDeviceCleanupSettings] = None
        # Encryption report for devices in this account
        self._managed_device_encryption_states: Optional[List[managed_device_encryption_state.ManagedDeviceEncryptionState]] = None
        # Device overview
        self._managed_device_overview: Optional[managed_device_overview.ManagedDeviceOverview] = None
        # The list of managed devices.
        self._managed_devices: Optional[List[managed_device.ManagedDevice]] = None
        # Maximum number of DEP tokens allowed per-tenant.
        self._maximum_dep_tokens: Optional[int] = None
        # Collection of MicrosoftTunnelConfiguration settings associated with account.
        self._microsoft_tunnel_configurations: Optional[List[microsoft_tunnel_configuration.MicrosoftTunnelConfiguration]] = None
        # Collection of MicrosoftTunnelHealthThreshold settings associated with account.
        self._microsoft_tunnel_health_thresholds: Optional[List[microsoft_tunnel_health_threshold.MicrosoftTunnelHealthThreshold]] = None
        # Collection of MicrosoftTunnelServerLogCollectionResponse settings associated with account.
        self._microsoft_tunnel_server_log_collection_responses: Optional[List[microsoft_tunnel_server_log_collection_response.MicrosoftTunnelServerLogCollectionResponse]] = None
        # Collection of MicrosoftTunnelSite settings associated with account.
        self._microsoft_tunnel_sites: Optional[List[microsoft_tunnel_site.MicrosoftTunnelSite]] = None
        # The collection property of MobileAppTroubleshootingEvent.
        self._mobile_app_troubleshooting_events: Optional[List[mobile_app_troubleshooting_event.MobileAppTroubleshootingEvent]] = None
        # The list of Mobile threat Defense connectors configured by the tenant.
        self._mobile_threat_defense_connectors: Optional[List[mobile_threat_defense_connector.MobileThreatDefenseConnector]] = None
        # The monitoring property
        self._monitoring: Optional[monitoring.Monitoring] = None
        # The collection of Ndes connectors for this account.
        self._ndes_connectors: Optional[List[ndes_connector.NdesConnector]] = None
        # The Notification Message Templates.
        self._notification_message_templates: Optional[List[notification_message_template.NotificationMessageTemplate]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of OEM Warranty Statuses
        self._oem_warranty_information_onboarding: Optional[List[oem_warranty_information_onboarding.OemWarrantyInformationOnboarding]] = None
        # The list of device remote action audits with the tenant.
        self._remote_action_audits: Optional[List[remote_action_audit.RemoteActionAudit]] = None
        # The remote assist partners.
        self._remote_assistance_partners: Optional[List[remote_assistance_partner.RemoteAssistancePartner]] = None
        # The remote assistance settings singleton
        self._remote_assistance_settings: Optional[remote_assistance_settings.RemoteAssistanceSettings] = None
        # Reports singleton
        self._reports: Optional[device_management_reports.DeviceManagementReports] = None
        # Collection of resource access settings associated with account.
        self._resource_access_profiles: Optional[List[device_management_resource_access_profile_base.DeviceManagementResourceAccessProfileBase]] = None
        # The Resource Operations.
        self._resource_operations: Optional[List[resource_operation.ResourceOperation]] = None
        # List of all reusable settings that can be referred in a policy
        self._reusable_policy_settings: Optional[List[device_management_reusable_policy_setting.DeviceManagementReusablePolicySetting]] = None
        # List of all reusable settings
        self._reusable_settings: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None
        # The Role Assignments.
        self._role_assignments: Optional[List[device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment]] = None
        # The Role Definitions.
        self._role_definitions: Optional[List[role_definition.RoleDefinition]] = None
        # The Role Scope Tags.
        self._role_scope_tags: Optional[List[role_scope_tag.RoleScopeTag]] = None
        # The device management intent setting definitions
        self._setting_definitions: Optional[List[device_management_setting_definition.DeviceManagementSettingDefinition]] = None
        # Account level settings.
        self._settings: Optional[device_management_settings.DeviceManagementSettings] = None
        # The software update status summary.
        self._software_update_status_summary: Optional[software_update_status_summary.SoftwareUpdateStatusSummary] = None
        # Tenant mobile device management subscriptions.
        self._subscriptions: Optional[device_management_subscriptions.DeviceManagementSubscriptions] = None
        # Tenant mobile device management subscription state.
        self._subscription_state: Optional[device_management_subscription_state.DeviceManagementSubscriptionState] = None
        # The telecom expense management partners.
        self._telecom_expense_management_partners: Optional[List[telecom_expense_management_partner.TelecomExpenseManagementPartner]] = None
        # The available templates
        self._templates: Optional[List[device_management_template.DeviceManagementTemplate]] = None
        # List of all TemplateSettings
        self._template_settings: Optional[List[device_management_configuration_setting_template.DeviceManagementConfigurationSettingTemplate]] = None
        # TenantAttach RBAC Enablement
        self._tenant_attach_r_b_a_c: Optional[tenant_attach_r_b_a_c.TenantAttachRBAC] = None
        # The terms and conditions associated with device management of the company.
        self._terms_and_conditions: Optional[List[terms_and_conditions.TermsAndConditions]] = None
        # The list of troubleshooting events for the tenant.
        self._troubleshooting_events: Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]] = None
        # When enabled, users assigned as administrators via Role Assignment Memberships do not require an assigned Intune license. Prior to this, only Intune licensed users were granted permissions with an Intune role unless they were assigned a role via Azure Active Directory. You are limited to 350 unlicensed direct members for each AAD security group in a role assignment, but you can assign multiple AAD security groups to a role if you need to support more than 350 unlicensed administrators. Licensed administrators are unaffected, do not have to be direct members, nor does the 350 member limit apply. This property is read-only.
        self._unlicensed_adminstrators_enabled: Optional[bool] = None
        # The user experience analytics anomaly entity contains anomaly details.
        self._user_experience_analytics_anomaly: Optional[List[user_experience_analytics_anomaly.UserExperienceAnalyticsAnomaly]] = None
        # The user experience analytics anomaly entity contains device details.
        self._user_experience_analytics_anomaly_device: Optional[List[user_experience_analytics_anomaly_device.UserExperienceAnalyticsAnomalyDevice]] = None
        # The user experience analytics anomaly severity overview entity contains the count information for each severity of anomaly.
        self._user_experience_analytics_anomaly_severity_overview: Optional[user_experience_analytics_anomaly_severity_overview.UserExperienceAnalyticsAnomalySeverityOverview] = None
        # User experience analytics appHealth Application Performance
        self._user_experience_analytics_app_health_application_performance: Optional[List[user_experience_analytics_app_health_application_performance.UserExperienceAnalyticsAppHealthApplicationPerformance]] = None
        # User experience analytics appHealth Application Performance by App Version
        self._user_experience_analytics_app_health_application_performance_by_app_version: Optional[List[user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion]] = None
        # User experience analytics appHealth Application Performance by App Version details
        self._user_experience_analytics_app_health_application_performance_by_app_version_details: Optional[List[user_experience_analytics_app_health_app_performance_by_app_version_details.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails]] = None
        # User experience analytics appHealth Application Performance by App Version Device Id
        self._user_experience_analytics_app_health_application_performance_by_app_version_device_id: Optional[List[user_experience_analytics_app_health_app_performance_by_app_version_device_id.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId]] = None
        # User experience analytics appHealth Application Performance by OS Version
        self._user_experience_analytics_app_health_application_performance_by_o_s_version: Optional[List[user_experience_analytics_app_health_app_performance_by_o_s_version.UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion]] = None
        # User experience analytics appHealth Model Performance
        self._user_experience_analytics_app_health_device_model_performance: Optional[List[user_experience_analytics_app_health_device_model_performance.UserExperienceAnalyticsAppHealthDeviceModelPerformance]] = None
        # User experience analytics appHealth Device Performance
        self._user_experience_analytics_app_health_device_performance: Optional[List[user_experience_analytics_app_health_device_performance.UserExperienceAnalyticsAppHealthDevicePerformance]] = None
        # User experience analytics device performance details
        self._user_experience_analytics_app_health_device_performance_details: Optional[List[user_experience_analytics_app_health_device_performance_details.UserExperienceAnalyticsAppHealthDevicePerformanceDetails]] = None
        # User experience analytics appHealth OS version Performance
        self._user_experience_analytics_app_health_o_s_version_performance: Optional[List[user_experience_analytics_app_health_o_s_version_performance.UserExperienceAnalyticsAppHealthOSVersionPerformance]] = None
        # User experience analytics appHealth overview
        self._user_experience_analytics_app_health_overview: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
        # User experience analytics baselines
        self._user_experience_analytics_baselines: Optional[List[user_experience_analytics_baseline.UserExperienceAnalyticsBaseline]] = None
        # User Experience Analytics Battery Health App Impact
        self._user_experience_analytics_battery_health_app_impact: Optional[List[user_experience_analytics_battery_health_app_impact.UserExperienceAnalyticsBatteryHealthAppImpact]] = None
        # User Experience Analytics Battery Health Capacity Details
        self._user_experience_analytics_battery_health_capacity_details: Optional[user_experience_analytics_battery_health_capacity_details.UserExperienceAnalyticsBatteryHealthCapacityDetails] = None
        # User Experience Analytics Battery Health Device App Impact
        self._user_experience_analytics_battery_health_device_app_impact: Optional[List[user_experience_analytics_battery_health_device_app_impact.UserExperienceAnalyticsBatteryHealthDeviceAppImpact]] = None
        # User Experience Analytics Battery Health Device Performance
        self._user_experience_analytics_battery_health_device_performance: Optional[List[user_experience_analytics_battery_health_device_performance.UserExperienceAnalyticsBatteryHealthDevicePerformance]] = None
        # User Experience Analytics Battery Health Device Runtime History
        self._user_experience_analytics_battery_health_device_runtime_history: Optional[List[user_experience_analytics_battery_health_device_runtime_history.UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory]] = None
        # User Experience Analytics Battery Health Model Performance
        self._user_experience_analytics_battery_health_model_performance: Optional[List[user_experience_analytics_battery_health_model_performance.UserExperienceAnalyticsBatteryHealthModelPerformance]] = None
        # User Experience Analytics Battery Health Os Performance
        self._user_experience_analytics_battery_health_os_performance: Optional[List[user_experience_analytics_battery_health_os_performance.UserExperienceAnalyticsBatteryHealthOsPerformance]] = None
        # User Experience Analytics Battery Health Runtime Details
        self._user_experience_analytics_battery_health_runtime_details: Optional[user_experience_analytics_battery_health_runtime_details.UserExperienceAnalyticsBatteryHealthRuntimeDetails] = None
        # User experience analytics categories
        self._user_experience_analytics_categories: Optional[List[user_experience_analytics_category.UserExperienceAnalyticsCategory]] = None
        # User experience analytics device metric history
        self._user_experience_analytics_device_metric_history: Optional[List[user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory]] = None
        # User experience analytics device performance
        self._user_experience_analytics_device_performance: Optional[List[user_experience_analytics_device_performance.UserExperienceAnalyticsDevicePerformance]] = None
        # The user experience analytics device scope entity endpoint to trigger on the service to either START or STOP computing metrics data based on a device scope configuration.
        self._user_experience_analytics_device_scope: Optional[user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope] = None
        # The user experience analytics device scope entity contains device scope configuration use to apply filtering on the endpoint analytics reports.
        self._user_experience_analytics_device_scopes: Optional[List[user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope]] = None
        # User experience analytics device scores
        self._user_experience_analytics_device_scores: Optional[List[user_experience_analytics_device_scores.UserExperienceAnalyticsDeviceScores]] = None
        # User experience analytics device Startup History
        self._user_experience_analytics_device_startup_history: Optional[List[user_experience_analytics_device_startup_history.UserExperienceAnalyticsDeviceStartupHistory]] = None
        # User experience analytics device Startup Processes
        self._user_experience_analytics_device_startup_processes: Optional[List[user_experience_analytics_device_startup_process.UserExperienceAnalyticsDeviceStartupProcess]] = None
        # User experience analytics device Startup Process Performance
        self._user_experience_analytics_device_startup_process_performance: Optional[List[user_experience_analytics_device_startup_process_performance.UserExperienceAnalyticsDeviceStartupProcessPerformance]] = None
        # User experience analytics devices without cloud identity.
        self._user_experience_analytics_devices_without_cloud_identity: Optional[List[user_experience_analytics_device_without_cloud_identity.UserExperienceAnalyticsDeviceWithoutCloudIdentity]] = None
        # User experience analytics impacting process
        self._user_experience_analytics_impacting_process: Optional[List[user_experience_analytics_impacting_process.UserExperienceAnalyticsImpactingProcess]] = None
        # User experience analytics metric history
        self._user_experience_analytics_metric_history: Optional[List[user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory]] = None
        # User experience analytics model scores
        self._user_experience_analytics_model_scores: Optional[List[user_experience_analytics_model_scores.UserExperienceAnalyticsModelScores]] = None
        # User experience analytics devices not Windows Autopilot ready.
        self._user_experience_analytics_not_autopilot_ready_device: Optional[List[user_experience_analytics_not_autopilot_ready_device.UserExperienceAnalyticsNotAutopilotReadyDevice]] = None
        # User experience analytics overview
        self._user_experience_analytics_overview: Optional[user_experience_analytics_overview.UserExperienceAnalyticsOverview] = None
        # User experience analytics remote connection
        self._user_experience_analytics_remote_connection: Optional[List[user_experience_analytics_remote_connection.UserExperienceAnalyticsRemoteConnection]] = None
        # User experience analytics resource performance
        self._user_experience_analytics_resource_performance: Optional[List[user_experience_analytics_resource_performance.UserExperienceAnalyticsResourcePerformance]] = None
        # User experience analytics device Startup Score History
        self._user_experience_analytics_score_history: Optional[List[user_experience_analytics_score_history.UserExperienceAnalyticsScoreHistory]] = None
        # User experience analytics device settings
        self._user_experience_analytics_settings: Optional[user_experience_analytics_settings.UserExperienceAnalyticsSettings] = None
        # User experience analytics work from anywhere hardware readiness metrics.
        self._user_experience_analytics_work_from_anywhere_hardware_readiness_metric: Optional[user_experience_analytics_work_from_anywhere_hardware_readiness_metric.UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric] = None
        # User experience analytics work from anywhere metrics.
        self._user_experience_analytics_work_from_anywhere_metrics: Optional[List[user_experience_analytics_work_from_anywhere_metric.UserExperienceAnalyticsWorkFromAnywhereMetric]] = None
        # The user experience analytics work from anywhere model performance
        self._user_experience_analytics_work_from_anywhere_model_performance: Optional[List[user_experience_analytics_work_from_anywhere_model_performance.UserExperienceAnalyticsWorkFromAnywhereModelPerformance]] = None
        # Collection of PFX certificates associated with a user.
        self._user_pfx_certificates: Optional[List[user_p_f_x_certificate.UserPFXCertificate]] = None
        # The virtualEndpoint property
        self._virtual_endpoint: Optional[virtual_endpoint.VirtualEndpoint] = None
        # Windows auto pilot deployment profiles
        self._windows_autopilot_deployment_profiles: Optional[List[windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile]] = None
        # The Windows autopilot device identities contained collection.
        self._windows_autopilot_device_identities: Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]] = None
        # The Windows autopilot account settings.
        self._windows_autopilot_settings: Optional[windows_autopilot_settings.WindowsAutopilotSettings] = None
        # A collection of windows driver update profiles
        self._windows_driver_update_profiles: Optional[List[windows_driver_update_profile.WindowsDriverUpdateProfile]] = None
        # A collection of windows feature update profiles
        self._windows_feature_update_profiles: Optional[List[windows_feature_update_profile.WindowsFeatureUpdateProfile]] = None
        # The windows information protection app learning summaries.
        self._windows_information_protection_app_learning_summaries: Optional[List[windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary]] = None
        # The windows information protection network learning summaries.
        self._windows_information_protection_network_learning_summaries: Optional[List[windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary]] = None
        # The list of affected malware in the tenant.
        self._windows_malware_information: Optional[List[windows_malware_information.WindowsMalwareInformation]] = None
        # Malware overview for windows devices.
        self._windows_malware_overview: Optional[windows_malware_overview.WindowsMalwareOverview] = None
        # A collection of windows quality update profiles
        self._windows_quality_update_profiles: Optional[List[windows_quality_update_profile.WindowsQualityUpdateProfile]] = None
        # A collection of windows update catalog items (fetaure updates item , quality updates item)
        self._windows_update_catalog_items: Optional[List[windows_update_catalog_item.WindowsUpdateCatalogItem]] = None
        # The Collection of ZebraFotaArtifacts.
        self._zebra_fota_artifacts: Optional[List[zebra_fota_artifact.ZebraFotaArtifact]] = None
        # The singleton ZebraFotaConnector associated with account.
        self._zebra_fota_connector: Optional[zebra_fota_connector.ZebraFotaConnector] = None
        # Collection of ZebraFotaDeployments associated with account.
        self._zebra_fota_deployments: Optional[List[zebra_fota_deployment.ZebraFotaDeployment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagement
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagement()
    
    @property
    def data_processor_service_for_windows_features_onboarding(self,) -> Optional[data_processor_service_for_windows_features_onboarding.DataProcessorServiceForWindowsFeaturesOnboarding]:
        """
        Gets the dataProcessorServiceForWindowsFeaturesOnboarding property value. A configuration entity for MEM features that utilize Data Processor Service for Windows (DPSW) data.
        Returns: Optional[data_processor_service_for_windows_features_onboarding.DataProcessorServiceForWindowsFeaturesOnboarding]
        """
        return self._data_processor_service_for_windows_features_onboarding
    
    @data_processor_service_for_windows_features_onboarding.setter
    def data_processor_service_for_windows_features_onboarding(self,value: Optional[data_processor_service_for_windows_features_onboarding.DataProcessorServiceForWindowsFeaturesOnboarding] = None) -> None:
        """
        Sets the dataProcessorServiceForWindowsFeaturesOnboarding property value. A configuration entity for MEM features that utilize Data Processor Service for Windows (DPSW) data.
        Args:
            value: Value to set for the dataProcessorServiceForWindowsFeaturesOnboarding property.
        """
        self._data_processor_service_for_windows_features_onboarding = value
    
    @property
    def data_sharing_consents(self,) -> Optional[List[data_sharing_consent.DataSharingConsent]]:
        """
        Gets the dataSharingConsents property value. Data sharing consents.
        Returns: Optional[List[data_sharing_consent.DataSharingConsent]]
        """
        return self._data_sharing_consents
    
    @data_sharing_consents.setter
    def data_sharing_consents(self,value: Optional[List[data_sharing_consent.DataSharingConsent]] = None) -> None:
        """
        Sets the dataSharingConsents property value. Data sharing consents.
        Args:
            value: Value to set for the dataSharingConsents property.
        """
        self._data_sharing_consents = value
    
    @property
    def dep_onboarding_settings(self,) -> Optional[List[dep_onboarding_setting.DepOnboardingSetting]]:
        """
        Gets the depOnboardingSettings property value. This collections of multiple DEP tokens per-tenant.
        Returns: Optional[List[dep_onboarding_setting.DepOnboardingSetting]]
        """
        return self._dep_onboarding_settings
    
    @dep_onboarding_settings.setter
    def dep_onboarding_settings(self,value: Optional[List[dep_onboarding_setting.DepOnboardingSetting]] = None) -> None:
        """
        Sets the depOnboardingSettings property value. This collections of multiple DEP tokens per-tenant.
        Args:
            value: Value to set for the depOnboardingSettings property.
        """
        self._dep_onboarding_settings = value
    
    @property
    def derived_credentials(self,) -> Optional[List[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]]:
        """
        Gets the derivedCredentials property value. Collection of Derived credential settings associated with account.
        Returns: Optional[List[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]]
        """
        return self._derived_credentials
    
    @derived_credentials.setter
    def derived_credentials(self,value: Optional[List[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]] = None) -> None:
        """
        Sets the derivedCredentials property value. Collection of Derived credential settings associated with account.
        Args:
            value: Value to set for the derivedCredentials property.
        """
        self._derived_credentials = value
    
    @property
    def detected_apps(self,) -> Optional[List[detected_app.DetectedApp]]:
        """
        Gets the detectedApps property value. The list of detected apps associated with a device.
        Returns: Optional[List[detected_app.DetectedApp]]
        """
        return self._detected_apps
    
    @detected_apps.setter
    def detected_apps(self,value: Optional[List[detected_app.DetectedApp]] = None) -> None:
        """
        Sets the detectedApps property value. The list of detected apps associated with a device.
        Args:
            value: Value to set for the detectedApps property.
        """
        self._detected_apps = value
    
    @property
    def device_categories(self,) -> Optional[List[device_category.DeviceCategory]]:
        """
        Gets the deviceCategories property value. The list of device categories with the tenant.
        Returns: Optional[List[device_category.DeviceCategory]]
        """
        return self._device_categories
    
    @device_categories.setter
    def device_categories(self,value: Optional[List[device_category.DeviceCategory]] = None) -> None:
        """
        Sets the deviceCategories property value. The list of device categories with the tenant.
        Args:
            value: Value to set for the deviceCategories property.
        """
        self._device_categories = value
    
    @property
    def device_compliance_policies(self,) -> Optional[List[device_compliance_policy.DeviceCompliancePolicy]]:
        """
        Gets the deviceCompliancePolicies property value. The device compliance policies.
        Returns: Optional[List[device_compliance_policy.DeviceCompliancePolicy]]
        """
        return self._device_compliance_policies
    
    @device_compliance_policies.setter
    def device_compliance_policies(self,value: Optional[List[device_compliance_policy.DeviceCompliancePolicy]] = None) -> None:
        """
        Sets the deviceCompliancePolicies property value. The device compliance policies.
        Args:
            value: Value to set for the deviceCompliancePolicies property.
        """
        self._device_compliance_policies = value
    
    @property
    def device_compliance_policy_device_state_summary(self,) -> Optional[device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary]:
        """
        Gets the deviceCompliancePolicyDeviceStateSummary property value. The device compliance state summary for this account.
        Returns: Optional[device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary]
        """
        return self._device_compliance_policy_device_state_summary
    
    @device_compliance_policy_device_state_summary.setter
    def device_compliance_policy_device_state_summary(self,value: Optional[device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary] = None) -> None:
        """
        Sets the deviceCompliancePolicyDeviceStateSummary property value. The device compliance state summary for this account.
        Args:
            value: Value to set for the deviceCompliancePolicyDeviceStateSummary property.
        """
        self._device_compliance_policy_device_state_summary = value
    
    @property
    def device_compliance_policy_setting_state_summaries(self,) -> Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]]:
        """
        Gets the deviceCompliancePolicySettingStateSummaries property value. The summary states of compliance policy settings for this account.
        Returns: Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]]
        """
        return self._device_compliance_policy_setting_state_summaries
    
    @device_compliance_policy_setting_state_summaries.setter
    def device_compliance_policy_setting_state_summaries(self,value: Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]] = None) -> None:
        """
        Sets the deviceCompliancePolicySettingStateSummaries property value. The summary states of compliance policy settings for this account.
        Args:
            value: Value to set for the deviceCompliancePolicySettingStateSummaries property.
        """
        self._device_compliance_policy_setting_state_summaries = value
    
    @property
    def device_compliance_report_summarization_date_time(self,) -> Optional[datetime]:
        """
        Gets the deviceComplianceReportSummarizationDateTime property value. The last requested time of device compliance reporting for this account. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._device_compliance_report_summarization_date_time
    
    @device_compliance_report_summarization_date_time.setter
    def device_compliance_report_summarization_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deviceComplianceReportSummarizationDateTime property value. The last requested time of device compliance reporting for this account. This property is read-only.
        Args:
            value: Value to set for the deviceComplianceReportSummarizationDateTime property.
        """
        self._device_compliance_report_summarization_date_time = value
    
    @property
    def device_compliance_scripts(self,) -> Optional[List[device_compliance_script.DeviceComplianceScript]]:
        """
        Gets the deviceComplianceScripts property value. The list of device compliance scripts associated with the tenant.
        Returns: Optional[List[device_compliance_script.DeviceComplianceScript]]
        """
        return self._device_compliance_scripts
    
    @device_compliance_scripts.setter
    def device_compliance_scripts(self,value: Optional[List[device_compliance_script.DeviceComplianceScript]] = None) -> None:
        """
        Sets the deviceComplianceScripts property value. The list of device compliance scripts associated with the tenant.
        Args:
            value: Value to set for the deviceComplianceScripts property.
        """
        self._device_compliance_scripts = value
    
    @property
    def device_configuration_conflict_summary(self,) -> Optional[List[device_configuration_conflict_summary.DeviceConfigurationConflictSummary]]:
        """
        Gets the deviceConfigurationConflictSummary property value. Summary of policies in conflict state for this account.
        Returns: Optional[List[device_configuration_conflict_summary.DeviceConfigurationConflictSummary]]
        """
        return self._device_configuration_conflict_summary
    
    @device_configuration_conflict_summary.setter
    def device_configuration_conflict_summary(self,value: Optional[List[device_configuration_conflict_summary.DeviceConfigurationConflictSummary]] = None) -> None:
        """
        Sets the deviceConfigurationConflictSummary property value. Summary of policies in conflict state for this account.
        Args:
            value: Value to set for the deviceConfigurationConflictSummary property.
        """
        self._device_configuration_conflict_summary = value
    
    @property
    def device_configuration_device_state_summaries(self,) -> Optional[device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary]:
        """
        Gets the deviceConfigurationDeviceStateSummaries property value. The device configuration device state summary for this account.
        Returns: Optional[device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary]
        """
        return self._device_configuration_device_state_summaries
    
    @device_configuration_device_state_summaries.setter
    def device_configuration_device_state_summaries(self,value: Optional[device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary] = None) -> None:
        """
        Sets the deviceConfigurationDeviceStateSummaries property value. The device configuration device state summary for this account.
        Args:
            value: Value to set for the deviceConfigurationDeviceStateSummaries property.
        """
        self._device_configuration_device_state_summaries = value
    
    @property
    def device_configuration_restricted_apps_violations(self,) -> Optional[List[restricted_apps_violation.RestrictedAppsViolation]]:
        """
        Gets the deviceConfigurationRestrictedAppsViolations property value. Restricted apps violations for this account.
        Returns: Optional[List[restricted_apps_violation.RestrictedAppsViolation]]
        """
        return self._device_configuration_restricted_apps_violations
    
    @device_configuration_restricted_apps_violations.setter
    def device_configuration_restricted_apps_violations(self,value: Optional[List[restricted_apps_violation.RestrictedAppsViolation]] = None) -> None:
        """
        Sets the deviceConfigurationRestrictedAppsViolations property value. Restricted apps violations for this account.
        Args:
            value: Value to set for the deviceConfigurationRestrictedAppsViolations property.
        """
        self._device_configuration_restricted_apps_violations = value
    
    @property
    def device_configurations(self,) -> Optional[List[device_configuration.DeviceConfiguration]]:
        """
        Gets the deviceConfigurations property value. The device configurations.
        Returns: Optional[List[device_configuration.DeviceConfiguration]]
        """
        return self._device_configurations
    
    @device_configurations.setter
    def device_configurations(self,value: Optional[List[device_configuration.DeviceConfiguration]] = None) -> None:
        """
        Sets the deviceConfigurations property value. The device configurations.
        Args:
            value: Value to set for the deviceConfigurations property.
        """
        self._device_configurations = value
    
    @property
    def device_configurations_all_managed_device_certificate_states(self,) -> Optional[List[managed_all_device_certificate_state.ManagedAllDeviceCertificateState]]:
        """
        Gets the deviceConfigurationsAllManagedDeviceCertificateStates property value. Summary of all certificates for all devices.
        Returns: Optional[List[managed_all_device_certificate_state.ManagedAllDeviceCertificateState]]
        """
        return self._device_configurations_all_managed_device_certificate_states
    
    @device_configurations_all_managed_device_certificate_states.setter
    def device_configurations_all_managed_device_certificate_states(self,value: Optional[List[managed_all_device_certificate_state.ManagedAllDeviceCertificateState]] = None) -> None:
        """
        Sets the deviceConfigurationsAllManagedDeviceCertificateStates property value. Summary of all certificates for all devices.
        Args:
            value: Value to set for the deviceConfigurationsAllManagedDeviceCertificateStates property.
        """
        self._device_configurations_all_managed_device_certificate_states = value
    
    @property
    def device_configuration_user_state_summaries(self,) -> Optional[device_configuration_user_state_summary.DeviceConfigurationUserStateSummary]:
        """
        Gets the deviceConfigurationUserStateSummaries property value. The device configuration user state summary for this account.
        Returns: Optional[device_configuration_user_state_summary.DeviceConfigurationUserStateSummary]
        """
        return self._device_configuration_user_state_summaries
    
    @device_configuration_user_state_summaries.setter
    def device_configuration_user_state_summaries(self,value: Optional[device_configuration_user_state_summary.DeviceConfigurationUserStateSummary] = None) -> None:
        """
        Sets the deviceConfigurationUserStateSummaries property value. The device configuration user state summary for this account.
        Args:
            value: Value to set for the deviceConfigurationUserStateSummaries property.
        """
        self._device_configuration_user_state_summaries = value
    
    @property
    def device_custom_attribute_shell_scripts(self,) -> Optional[List[device_custom_attribute_shell_script.DeviceCustomAttributeShellScript]]:
        """
        Gets the deviceCustomAttributeShellScripts property value. The list of device custom attribute shell scripts associated with the tenant.
        Returns: Optional[List[device_custom_attribute_shell_script.DeviceCustomAttributeShellScript]]
        """
        return self._device_custom_attribute_shell_scripts
    
    @device_custom_attribute_shell_scripts.setter
    def device_custom_attribute_shell_scripts(self,value: Optional[List[device_custom_attribute_shell_script.DeviceCustomAttributeShellScript]] = None) -> None:
        """
        Sets the deviceCustomAttributeShellScripts property value. The list of device custom attribute shell scripts associated with the tenant.
        Args:
            value: Value to set for the deviceCustomAttributeShellScripts property.
        """
        self._device_custom_attribute_shell_scripts = value
    
    @property
    def device_enrollment_configurations(self,) -> Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]]:
        """
        Gets the deviceEnrollmentConfigurations property value. The list of device enrollment configurations
        Returns: Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]]
        """
        return self._device_enrollment_configurations
    
    @device_enrollment_configurations.setter
    def device_enrollment_configurations(self,value: Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]] = None) -> None:
        """
        Sets the deviceEnrollmentConfigurations property value. The list of device enrollment configurations
        Args:
            value: Value to set for the deviceEnrollmentConfigurations property.
        """
        self._device_enrollment_configurations = value
    
    @property
    def device_health_scripts(self,) -> Optional[List[device_health_script.DeviceHealthScript]]:
        """
        Gets the deviceHealthScripts property value. The list of device health scripts associated with the tenant.
        Returns: Optional[List[device_health_script.DeviceHealthScript]]
        """
        return self._device_health_scripts
    
    @device_health_scripts.setter
    def device_health_scripts(self,value: Optional[List[device_health_script.DeviceHealthScript]] = None) -> None:
        """
        Sets the deviceHealthScripts property value. The list of device health scripts associated with the tenant.
        Args:
            value: Value to set for the deviceHealthScripts property.
        """
        self._device_health_scripts = value
    
    @property
    def device_management_partners(self,) -> Optional[List[device_management_partner.DeviceManagementPartner]]:
        """
        Gets the deviceManagementPartners property value. The list of Device Management Partners configured by the tenant.
        Returns: Optional[List[device_management_partner.DeviceManagementPartner]]
        """
        return self._device_management_partners
    
    @device_management_partners.setter
    def device_management_partners(self,value: Optional[List[device_management_partner.DeviceManagementPartner]] = None) -> None:
        """
        Sets the deviceManagementPartners property value. The list of Device Management Partners configured by the tenant.
        Args:
            value: Value to set for the deviceManagementPartners property.
        """
        self._device_management_partners = value
    
    @property
    def device_management_scripts(self,) -> Optional[List[device_management_script.DeviceManagementScript]]:
        """
        Gets the deviceManagementScripts property value. The list of device management scripts associated with the tenant.
        Returns: Optional[List[device_management_script.DeviceManagementScript]]
        """
        return self._device_management_scripts
    
    @device_management_scripts.setter
    def device_management_scripts(self,value: Optional[List[device_management_script.DeviceManagementScript]] = None) -> None:
        """
        Sets the deviceManagementScripts property value. The list of device management scripts associated with the tenant.
        Args:
            value: Value to set for the deviceManagementScripts property.
        """
        self._device_management_scripts = value
    
    @property
    def device_protection_overview(self,) -> Optional[device_protection_overview.DeviceProtectionOverview]:
        """
        Gets the deviceProtectionOverview property value. Device protection overview.
        Returns: Optional[device_protection_overview.DeviceProtectionOverview]
        """
        return self._device_protection_overview
    
    @device_protection_overview.setter
    def device_protection_overview(self,value: Optional[device_protection_overview.DeviceProtectionOverview] = None) -> None:
        """
        Sets the deviceProtectionOverview property value. Device protection overview.
        Args:
            value: Value to set for the deviceProtectionOverview property.
        """
        self._device_protection_overview = value
    
    @property
    def device_shell_scripts(self,) -> Optional[List[device_shell_script.DeviceShellScript]]:
        """
        Gets the deviceShellScripts property value. The list of device shell scripts associated with the tenant.
        Returns: Optional[List[device_shell_script.DeviceShellScript]]
        """
        return self._device_shell_scripts
    
    @device_shell_scripts.setter
    def device_shell_scripts(self,value: Optional[List[device_shell_script.DeviceShellScript]] = None) -> None:
        """
        Sets the deviceShellScripts property value. The list of device shell scripts associated with the tenant.
        Args:
            value: Value to set for the deviceShellScripts property.
        """
        self._device_shell_scripts = value
    
    @property
    def domain_join_connectors(self,) -> Optional[List[device_management_domain_join_connector.DeviceManagementDomainJoinConnector]]:
        """
        Gets the domainJoinConnectors property value. A list of connector objects.
        Returns: Optional[List[device_management_domain_join_connector.DeviceManagementDomainJoinConnector]]
        """
        return self._domain_join_connectors
    
    @domain_join_connectors.setter
    def domain_join_connectors(self,value: Optional[List[device_management_domain_join_connector.DeviceManagementDomainJoinConnector]] = None) -> None:
        """
        Sets the domainJoinConnectors property value. A list of connector objects.
        Args:
            value: Value to set for the domainJoinConnectors property.
        """
        self._domain_join_connectors = value
    
    @property
    def embedded_s_i_m_activation_code_pools(self,) -> Optional[List[embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool]]:
        """
        Gets the embeddedSIMActivationCodePools property value. The embedded SIM activation code pools created by this account.
        Returns: Optional[List[embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool]]
        """
        return self._embedded_s_i_m_activation_code_pools
    
    @embedded_s_i_m_activation_code_pools.setter
    def embedded_s_i_m_activation_code_pools(self,value: Optional[List[embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool]] = None) -> None:
        """
        Sets the embeddedSIMActivationCodePools property value. The embedded SIM activation code pools created by this account.
        Args:
            value: Value to set for the embeddedSIMActivationCodePools property.
        """
        self._embedded_s_i_m_activation_code_pools = value
    
    @property
    def exchange_connectors(self,) -> Optional[List[device_management_exchange_connector.DeviceManagementExchangeConnector]]:
        """
        Gets the exchangeConnectors property value. The list of Exchange Connectors configured by the tenant.
        Returns: Optional[List[device_management_exchange_connector.DeviceManagementExchangeConnector]]
        """
        return self._exchange_connectors
    
    @exchange_connectors.setter
    def exchange_connectors(self,value: Optional[List[device_management_exchange_connector.DeviceManagementExchangeConnector]] = None) -> None:
        """
        Sets the exchangeConnectors property value. The list of Exchange Connectors configured by the tenant.
        Args:
            value: Value to set for the exchangeConnectors property.
        """
        self._exchange_connectors = value
    
    @property
    def exchange_on_premises_policies(self,) -> Optional[List[device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy]]:
        """
        Gets the exchangeOnPremisesPolicies property value. The list of Exchange On Premisis policies configured by the tenant.
        Returns: Optional[List[device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy]]
        """
        return self._exchange_on_premises_policies
    
    @exchange_on_premises_policies.setter
    def exchange_on_premises_policies(self,value: Optional[List[device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy]] = None) -> None:
        """
        Sets the exchangeOnPremisesPolicies property value. The list of Exchange On Premisis policies configured by the tenant.
        Args:
            value: Value to set for the exchangeOnPremisesPolicies property.
        """
        self._exchange_on_premises_policies = value
    
    @property
    def exchange_on_premises_policy(self,) -> Optional[device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy]:
        """
        Gets the exchangeOnPremisesPolicy property value. The policy which controls mobile device access to Exchange On Premises
        Returns: Optional[device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy]
        """
        return self._exchange_on_premises_policy
    
    @exchange_on_premises_policy.setter
    def exchange_on_premises_policy(self,value: Optional[device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy] = None) -> None:
        """
        Sets the exchangeOnPremisesPolicy property value. The policy which controls mobile device access to Exchange On Premises
        Args:
            value: Value to set for the exchangeOnPremisesPolicy property.
        """
        self._exchange_on_premises_policy = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_move_completion_date_time": lambda n : setattr(self, 'account_move_completion_date_time', n.get_datetime_value()),
            "admin_consent": lambda n : setattr(self, 'admin_consent', n.get_object_value(admin_consent.AdminConsent)),
            "advanced_threat_protection_onboarding_state_summary": lambda n : setattr(self, 'advanced_threat_protection_onboarding_state_summary', n.get_object_value(advanced_threat_protection_onboarding_state_summary.AdvancedThreatProtectionOnboardingStateSummary)),
            "android_device_owner_enrollment_profiles": lambda n : setattr(self, 'android_device_owner_enrollment_profiles', n.get_collection_of_object_values(android_device_owner_enrollment_profile.AndroidDeviceOwnerEnrollmentProfile)),
            "android_for_work_app_configuration_schemas": lambda n : setattr(self, 'android_for_work_app_configuration_schemas', n.get_collection_of_object_values(android_for_work_app_configuration_schema.AndroidForWorkAppConfigurationSchema)),
            "android_for_work_enrollment_profiles": lambda n : setattr(self, 'android_for_work_enrollment_profiles', n.get_collection_of_object_values(android_for_work_enrollment_profile.AndroidForWorkEnrollmentProfile)),
            "android_for_work_settings": lambda n : setattr(self, 'android_for_work_settings', n.get_object_value(android_for_work_settings.AndroidForWorkSettings)),
            "android_managed_store_account_enterprise_settings": lambda n : setattr(self, 'android_managed_store_account_enterprise_settings', n.get_object_value(android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings)),
            "android_managed_store_app_configuration_schemas": lambda n : setattr(self, 'android_managed_store_app_configuration_schemas', n.get_collection_of_object_values(android_managed_store_app_configuration_schema.AndroidManagedStoreAppConfigurationSchema)),
            "apple_push_notification_certificate": lambda n : setattr(self, 'apple_push_notification_certificate', n.get_object_value(apple_push_notification_certificate.ApplePushNotificationCertificate)),
            "apple_user_initiated_enrollment_profiles": lambda n : setattr(self, 'apple_user_initiated_enrollment_profiles', n.get_collection_of_object_values(apple_user_initiated_enrollment_profile.AppleUserInitiatedEnrollmentProfile)),
            "assignment_filters": lambda n : setattr(self, 'assignment_filters', n.get_collection_of_object_values(device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter)),
            "audit_events": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(audit_event.AuditEvent)),
            "autopilot_events": lambda n : setattr(self, 'autopilot_events', n.get_collection_of_object_values(device_management_autopilot_event.DeviceManagementAutopilotEvent)),
            "cart_to_class_associations": lambda n : setattr(self, 'cart_to_class_associations', n.get_collection_of_object_values(cart_to_class_association.CartToClassAssociation)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(device_management_setting_category.DeviceManagementSettingCategory)),
            "certificate_connector_details": lambda n : setattr(self, 'certificate_connector_details', n.get_collection_of_object_values(certificate_connector_details.CertificateConnectorDetails)),
            "chrome_o_s_onboarding_settings": lambda n : setattr(self, 'chrome_o_s_onboarding_settings', n.get_collection_of_object_values(chrome_o_s_onboarding_settings.ChromeOSOnboardingSettings)),
            "cloud_p_c_connectivity_issues": lambda n : setattr(self, 'cloud_p_c_connectivity_issues', n.get_collection_of_object_values(cloud_p_c_connectivity_issue.CloudPCConnectivityIssue)),
            "comanaged_devices": lambda n : setattr(self, 'comanaged_devices', n.get_collection_of_object_values(managed_device.ManagedDevice)),
            "comanagement_eligible_devices": lambda n : setattr(self, 'comanagement_eligible_devices', n.get_collection_of_object_values(comanagement_eligible_device.ComanagementEligibleDevice)),
            "compliance_categories": lambda n : setattr(self, 'compliance_categories', n.get_collection_of_object_values(device_management_configuration_category.DeviceManagementConfigurationCategory)),
            "compliance_management_partners": lambda n : setattr(self, 'compliance_management_partners', n.get_collection_of_object_values(compliance_management_partner.ComplianceManagementPartner)),
            "compliance_policies": lambda n : setattr(self, 'compliance_policies', n.get_collection_of_object_values(device_management_compliance_policy.DeviceManagementCompliancePolicy)),
            "compliance_settings": lambda n : setattr(self, 'compliance_settings', n.get_collection_of_object_values(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition)),
            "conditional_access_settings": lambda n : setattr(self, 'conditional_access_settings', n.get_object_value(on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings)),
            "config_manager_collections": lambda n : setattr(self, 'config_manager_collections', n.get_collection_of_object_values(config_manager_collection.ConfigManagerCollection)),
            "configuration_categories": lambda n : setattr(self, 'configuration_categories', n.get_collection_of_object_values(device_management_configuration_category.DeviceManagementConfigurationCategory)),
            "configuration_policies": lambda n : setattr(self, 'configuration_policies', n.get_collection_of_object_values(device_management_configuration_policy.DeviceManagementConfigurationPolicy)),
            "configuration_policy_templates": lambda n : setattr(self, 'configuration_policy_templates', n.get_collection_of_object_values(device_management_configuration_policy_template.DeviceManagementConfigurationPolicyTemplate)),
            "configuration_settings": lambda n : setattr(self, 'configuration_settings', n.get_collection_of_object_values(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition)),
            "data_processor_service_for_windows_features_onboarding": lambda n : setattr(self, 'data_processor_service_for_windows_features_onboarding', n.get_object_value(data_processor_service_for_windows_features_onboarding.DataProcessorServiceForWindowsFeaturesOnboarding)),
            "data_sharing_consents": lambda n : setattr(self, 'data_sharing_consents', n.get_collection_of_object_values(data_sharing_consent.DataSharingConsent)),
            "dep_onboarding_settings": lambda n : setattr(self, 'dep_onboarding_settings', n.get_collection_of_object_values(dep_onboarding_setting.DepOnboardingSetting)),
            "derived_credentials": lambda n : setattr(self, 'derived_credentials', n.get_collection_of_object_values(device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings)),
            "detected_apps": lambda n : setattr(self, 'detected_apps', n.get_collection_of_object_values(detected_app.DetectedApp)),
            "device_categories": lambda n : setattr(self, 'device_categories', n.get_collection_of_object_values(device_category.DeviceCategory)),
            "device_compliance_policies": lambda n : setattr(self, 'device_compliance_policies', n.get_collection_of_object_values(device_compliance_policy.DeviceCompliancePolicy)),
            "device_compliance_policy_device_state_summary": lambda n : setattr(self, 'device_compliance_policy_device_state_summary', n.get_object_value(device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary)),
            "device_compliance_policy_setting_state_summaries": lambda n : setattr(self, 'device_compliance_policy_setting_state_summaries', n.get_collection_of_object_values(device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary)),
            "device_compliance_report_summarization_date_time": lambda n : setattr(self, 'device_compliance_report_summarization_date_time', n.get_datetime_value()),
            "device_compliance_scripts": lambda n : setattr(self, 'device_compliance_scripts', n.get_collection_of_object_values(device_compliance_script.DeviceComplianceScript)),
            "device_configuration_conflict_summary": lambda n : setattr(self, 'device_configuration_conflict_summary', n.get_collection_of_object_values(device_configuration_conflict_summary.DeviceConfigurationConflictSummary)),
            "device_configuration_device_state_summaries": lambda n : setattr(self, 'device_configuration_device_state_summaries', n.get_object_value(device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary)),
            "device_configuration_restricted_apps_violations": lambda n : setattr(self, 'device_configuration_restricted_apps_violations', n.get_collection_of_object_values(restricted_apps_violation.RestrictedAppsViolation)),
            "device_configurations": lambda n : setattr(self, 'device_configurations', n.get_collection_of_object_values(device_configuration.DeviceConfiguration)),
            "device_configurations_all_managed_device_certificate_states": lambda n : setattr(self, 'device_configurations_all_managed_device_certificate_states', n.get_collection_of_object_values(managed_all_device_certificate_state.ManagedAllDeviceCertificateState)),
            "device_configuration_user_state_summaries": lambda n : setattr(self, 'device_configuration_user_state_summaries', n.get_object_value(device_configuration_user_state_summary.DeviceConfigurationUserStateSummary)),
            "device_custom_attribute_shell_scripts": lambda n : setattr(self, 'device_custom_attribute_shell_scripts', n.get_collection_of_object_values(device_custom_attribute_shell_script.DeviceCustomAttributeShellScript)),
            "device_enrollment_configurations": lambda n : setattr(self, 'device_enrollment_configurations', n.get_collection_of_object_values(device_enrollment_configuration.DeviceEnrollmentConfiguration)),
            "device_health_scripts": lambda n : setattr(self, 'device_health_scripts', n.get_collection_of_object_values(device_health_script.DeviceHealthScript)),
            "device_management_partners": lambda n : setattr(self, 'device_management_partners', n.get_collection_of_object_values(device_management_partner.DeviceManagementPartner)),
            "device_management_scripts": lambda n : setattr(self, 'device_management_scripts', n.get_collection_of_object_values(device_management_script.DeviceManagementScript)),
            "device_protection_overview": lambda n : setattr(self, 'device_protection_overview', n.get_object_value(device_protection_overview.DeviceProtectionOverview)),
            "device_shell_scripts": lambda n : setattr(self, 'device_shell_scripts', n.get_collection_of_object_values(device_shell_script.DeviceShellScript)),
            "domain_join_connectors": lambda n : setattr(self, 'domain_join_connectors', n.get_collection_of_object_values(device_management_domain_join_connector.DeviceManagementDomainJoinConnector)),
            "embedded_s_i_m_activation_code_pools": lambda n : setattr(self, 'embedded_s_i_m_activation_code_pools', n.get_collection_of_object_values(embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool)),
            "exchange_connectors": lambda n : setattr(self, 'exchange_connectors', n.get_collection_of_object_values(device_management_exchange_connector.DeviceManagementExchangeConnector)),
            "exchange_on_premises_policies": lambda n : setattr(self, 'exchange_on_premises_policies', n.get_collection_of_object_values(device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy)),
            "exchange_on_premises_policy": lambda n : setattr(self, 'exchange_on_premises_policy', n.get_object_value(device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy)),
            "group_policy_categories": lambda n : setattr(self, 'group_policy_categories', n.get_collection_of_object_values(group_policy_category.GroupPolicyCategory)),
            "group_policy_configurations": lambda n : setattr(self, 'group_policy_configurations', n.get_collection_of_object_values(group_policy_configuration.GroupPolicyConfiguration)),
            "group_policy_definition_files": lambda n : setattr(self, 'group_policy_definition_files', n.get_collection_of_object_values(group_policy_definition_file.GroupPolicyDefinitionFile)),
            "group_policy_definitions": lambda n : setattr(self, 'group_policy_definitions', n.get_collection_of_object_values(group_policy_definition.GroupPolicyDefinition)),
            "group_policy_migration_reports": lambda n : setattr(self, 'group_policy_migration_reports', n.get_collection_of_object_values(group_policy_migration_report.GroupPolicyMigrationReport)),
            "group_policy_object_files": lambda n : setattr(self, 'group_policy_object_files', n.get_collection_of_object_values(group_policy_object_file.GroupPolicyObjectFile)),
            "group_policy_uploaded_definition_files": lambda n : setattr(self, 'group_policy_uploaded_definition_files', n.get_collection_of_object_values(group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile)),
            "imported_device_identities": lambda n : setattr(self, 'imported_device_identities', n.get_collection_of_object_values(imported_device_identity.ImportedDeviceIdentity)),
            "imported_windows_autopilot_device_identities": lambda n : setattr(self, 'imported_windows_autopilot_device_identities', n.get_collection_of_object_values(imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity)),
            "intents": lambda n : setattr(self, 'intents', n.get_collection_of_object_values(device_management_intent.DeviceManagementIntent)),
            "intune_account_id": lambda n : setattr(self, 'intune_account_id', n.get_object_value(Guid)),
            "intune_brand": lambda n : setattr(self, 'intune_brand', n.get_object_value(intune_brand.IntuneBrand)),
            "intune_branding_profiles": lambda n : setattr(self, 'intune_branding_profiles', n.get_collection_of_object_values(intune_branding_profile.IntuneBrandingProfile)),
            "ios_update_statuses": lambda n : setattr(self, 'ios_update_statuses', n.get_collection_of_object_values(ios_update_device_status.IosUpdateDeviceStatus)),
            "last_report_aggregation_date_time": lambda n : setattr(self, 'last_report_aggregation_date_time', n.get_datetime_value()),
            "legacy_pc_manangement_enabled": lambda n : setattr(self, 'legacy_pc_manangement_enabled', n.get_bool_value()),
            "mac_o_s_software_update_account_summaries": lambda n : setattr(self, 'mac_o_s_software_update_account_summaries', n.get_collection_of_object_values(mac_o_s_software_update_account_summary.MacOSSoftwareUpdateAccountSummary)),
            "managed_device_cleanup_settings": lambda n : setattr(self, 'managed_device_cleanup_settings', n.get_object_value(managed_device_cleanup_settings.ManagedDeviceCleanupSettings)),
            "managed_device_encryption_states": lambda n : setattr(self, 'managed_device_encryption_states', n.get_collection_of_object_values(managed_device_encryption_state.ManagedDeviceEncryptionState)),
            "managed_device_overview": lambda n : setattr(self, 'managed_device_overview', n.get_object_value(managed_device_overview.ManagedDeviceOverview)),
            "managed_devices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(managed_device.ManagedDevice)),
            "maximum_dep_tokens": lambda n : setattr(self, 'maximum_dep_tokens', n.get_int_value()),
            "microsoft_tunnel_configurations": lambda n : setattr(self, 'microsoft_tunnel_configurations', n.get_collection_of_object_values(microsoft_tunnel_configuration.MicrosoftTunnelConfiguration)),
            "microsoft_tunnel_health_thresholds": lambda n : setattr(self, 'microsoft_tunnel_health_thresholds', n.get_collection_of_object_values(microsoft_tunnel_health_threshold.MicrosoftTunnelHealthThreshold)),
            "microsoft_tunnel_server_log_collection_responses": lambda n : setattr(self, 'microsoft_tunnel_server_log_collection_responses', n.get_collection_of_object_values(microsoft_tunnel_server_log_collection_response.MicrosoftTunnelServerLogCollectionResponse)),
            "microsoft_tunnel_sites": lambda n : setattr(self, 'microsoft_tunnel_sites', n.get_collection_of_object_values(microsoft_tunnel_site.MicrosoftTunnelSite)),
            "mobile_app_troubleshooting_events": lambda n : setattr(self, 'mobile_app_troubleshooting_events', n.get_collection_of_object_values(mobile_app_troubleshooting_event.MobileAppTroubleshootingEvent)),
            "mobile_threat_defense_connectors": lambda n : setattr(self, 'mobile_threat_defense_connectors', n.get_collection_of_object_values(mobile_threat_defense_connector.MobileThreatDefenseConnector)),
            "monitoring": lambda n : setattr(self, 'monitoring', n.get_object_value(monitoring.Monitoring)),
            "ndes_connectors": lambda n : setattr(self, 'ndes_connectors', n.get_collection_of_object_values(ndes_connector.NdesConnector)),
            "notification_message_templates": lambda n : setattr(self, 'notification_message_templates', n.get_collection_of_object_values(notification_message_template.NotificationMessageTemplate)),
            "oem_warranty_information_onboarding": lambda n : setattr(self, 'oem_warranty_information_onboarding', n.get_collection_of_object_values(oem_warranty_information_onboarding.OemWarrantyInformationOnboarding)),
            "remote_action_audits": lambda n : setattr(self, 'remote_action_audits', n.get_collection_of_object_values(remote_action_audit.RemoteActionAudit)),
            "remote_assistance_partners": lambda n : setattr(self, 'remote_assistance_partners', n.get_collection_of_object_values(remote_assistance_partner.RemoteAssistancePartner)),
            "remote_assistance_settings": lambda n : setattr(self, 'remote_assistance_settings', n.get_object_value(remote_assistance_settings.RemoteAssistanceSettings)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(device_management_reports.DeviceManagementReports)),
            "resource_access_profiles": lambda n : setattr(self, 'resource_access_profiles', n.get_collection_of_object_values(device_management_resource_access_profile_base.DeviceManagementResourceAccessProfileBase)),
            "resource_operations": lambda n : setattr(self, 'resource_operations', n.get_collection_of_object_values(resource_operation.ResourceOperation)),
            "reusable_policy_settings": lambda n : setattr(self, 'reusable_policy_settings', n.get_collection_of_object_values(device_management_reusable_policy_setting.DeviceManagementReusablePolicySetting)),
            "reusable_settings": lambda n : setattr(self, 'reusable_settings', n.get_collection_of_object_values(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition)),
            "role_assignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment)),
            "role_definitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(role_definition.RoleDefinition)),
            "role_scope_tags": lambda n : setattr(self, 'role_scope_tags', n.get_collection_of_object_values(role_scope_tag.RoleScopeTag)),
            "setting_definitions": lambda n : setattr(self, 'setting_definitions', n.get_collection_of_object_values(device_management_setting_definition.DeviceManagementSettingDefinition)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(device_management_settings.DeviceManagementSettings)),
            "software_update_status_summary": lambda n : setattr(self, 'software_update_status_summary', n.get_object_value(software_update_status_summary.SoftwareUpdateStatusSummary)),
            "subscriptions": lambda n : setattr(self, 'subscriptions', n.get_enum_value(device_management_subscriptions.DeviceManagementSubscriptions)),
            "subscription_state": lambda n : setattr(self, 'subscription_state', n.get_enum_value(device_management_subscription_state.DeviceManagementSubscriptionState)),
            "telecom_expense_management_partners": lambda n : setattr(self, 'telecom_expense_management_partners', n.get_collection_of_object_values(telecom_expense_management_partner.TelecomExpenseManagementPartner)),
            "templates": lambda n : setattr(self, 'templates', n.get_collection_of_object_values(device_management_template.DeviceManagementTemplate)),
            "template_settings": lambda n : setattr(self, 'template_settings', n.get_collection_of_object_values(device_management_configuration_setting_template.DeviceManagementConfigurationSettingTemplate)),
            "tenant_attach_r_b_a_c": lambda n : setattr(self, 'tenant_attach_r_b_a_c', n.get_object_value(tenant_attach_r_b_a_c.TenantAttachRBAC)),
            "terms_and_conditions": lambda n : setattr(self, 'terms_and_conditions', n.get_collection_of_object_values(terms_and_conditions.TermsAndConditions)),
            "troubleshooting_events": lambda n : setattr(self, 'troubleshooting_events', n.get_collection_of_object_values(device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent)),
            "unlicensed_adminstrators_enabled": lambda n : setattr(self, 'unlicensed_adminstrators_enabled', n.get_bool_value()),
            "user_experience_analytics_anomaly": lambda n : setattr(self, 'user_experience_analytics_anomaly', n.get_collection_of_object_values(user_experience_analytics_anomaly.UserExperienceAnalyticsAnomaly)),
            "user_experience_analytics_anomaly_device": lambda n : setattr(self, 'user_experience_analytics_anomaly_device', n.get_collection_of_object_values(user_experience_analytics_anomaly_device.UserExperienceAnalyticsAnomalyDevice)),
            "user_experience_analytics_anomaly_severity_overview": lambda n : setattr(self, 'user_experience_analytics_anomaly_severity_overview', n.get_object_value(user_experience_analytics_anomaly_severity_overview.UserExperienceAnalyticsAnomalySeverityOverview)),
            "user_experience_analytics_app_health_application_performance": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance', n.get_collection_of_object_values(user_experience_analytics_app_health_application_performance.UserExperienceAnalyticsAppHealthApplicationPerformance)),
            "user_experience_analytics_app_health_application_performance_by_app_version": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_app_version', n.get_collection_of_object_values(user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion)),
            "user_experience_analytics_app_health_application_performance_by_app_version_details": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_app_version_details', n.get_collection_of_object_values(user_experience_analytics_app_health_app_performance_by_app_version_details.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails)),
            "user_experience_analytics_app_health_application_performance_by_app_version_device_id": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_app_version_device_id', n.get_collection_of_object_values(user_experience_analytics_app_health_app_performance_by_app_version_device_id.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId)),
            "user_experience_analytics_app_health_application_performance_by_o_s_version": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_o_s_version', n.get_collection_of_object_values(user_experience_analytics_app_health_app_performance_by_o_s_version.UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion)),
            "user_experience_analytics_app_health_device_model_performance": lambda n : setattr(self, 'user_experience_analytics_app_health_device_model_performance', n.get_collection_of_object_values(user_experience_analytics_app_health_device_model_performance.UserExperienceAnalyticsAppHealthDeviceModelPerformance)),
            "user_experience_analytics_app_health_device_performance": lambda n : setattr(self, 'user_experience_analytics_app_health_device_performance', n.get_collection_of_object_values(user_experience_analytics_app_health_device_performance.UserExperienceAnalyticsAppHealthDevicePerformance)),
            "user_experience_analytics_app_health_device_performance_details": lambda n : setattr(self, 'user_experience_analytics_app_health_device_performance_details', n.get_collection_of_object_values(user_experience_analytics_app_health_device_performance_details.UserExperienceAnalyticsAppHealthDevicePerformanceDetails)),
            "user_experience_analytics_app_health_o_s_version_performance": lambda n : setattr(self, 'user_experience_analytics_app_health_o_s_version_performance', n.get_collection_of_object_values(user_experience_analytics_app_health_o_s_version_performance.UserExperienceAnalyticsAppHealthOSVersionPerformance)),
            "user_experience_analytics_app_health_overview": lambda n : setattr(self, 'user_experience_analytics_app_health_overview', n.get_object_value(user_experience_analytics_category.UserExperienceAnalyticsCategory)),
            "user_experience_analytics_baselines": lambda n : setattr(self, 'user_experience_analytics_baselines', n.get_collection_of_object_values(user_experience_analytics_baseline.UserExperienceAnalyticsBaseline)),
            "user_experience_analytics_battery_health_app_impact": lambda n : setattr(self, 'user_experience_analytics_battery_health_app_impact', n.get_collection_of_object_values(user_experience_analytics_battery_health_app_impact.UserExperienceAnalyticsBatteryHealthAppImpact)),
            "user_experience_analytics_battery_health_capacity_details": lambda n : setattr(self, 'user_experience_analytics_battery_health_capacity_details', n.get_object_value(user_experience_analytics_battery_health_capacity_details.UserExperienceAnalyticsBatteryHealthCapacityDetails)),
            "user_experience_analytics_battery_health_device_app_impact": lambda n : setattr(self, 'user_experience_analytics_battery_health_device_app_impact', n.get_collection_of_object_values(user_experience_analytics_battery_health_device_app_impact.UserExperienceAnalyticsBatteryHealthDeviceAppImpact)),
            "user_experience_analytics_battery_health_device_performance": lambda n : setattr(self, 'user_experience_analytics_battery_health_device_performance', n.get_collection_of_object_values(user_experience_analytics_battery_health_device_performance.UserExperienceAnalyticsBatteryHealthDevicePerformance)),
            "user_experience_analytics_battery_health_device_runtime_history": lambda n : setattr(self, 'user_experience_analytics_battery_health_device_runtime_history', n.get_collection_of_object_values(user_experience_analytics_battery_health_device_runtime_history.UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory)),
            "user_experience_analytics_battery_health_model_performance": lambda n : setattr(self, 'user_experience_analytics_battery_health_model_performance', n.get_collection_of_object_values(user_experience_analytics_battery_health_model_performance.UserExperienceAnalyticsBatteryHealthModelPerformance)),
            "user_experience_analytics_battery_health_os_performance": lambda n : setattr(self, 'user_experience_analytics_battery_health_os_performance', n.get_collection_of_object_values(user_experience_analytics_battery_health_os_performance.UserExperienceAnalyticsBatteryHealthOsPerformance)),
            "user_experience_analytics_battery_health_runtime_details": lambda n : setattr(self, 'user_experience_analytics_battery_health_runtime_details', n.get_object_value(user_experience_analytics_battery_health_runtime_details.UserExperienceAnalyticsBatteryHealthRuntimeDetails)),
            "user_experience_analytics_categories": lambda n : setattr(self, 'user_experience_analytics_categories', n.get_collection_of_object_values(user_experience_analytics_category.UserExperienceAnalyticsCategory)),
            "user_experience_analytics_device_metric_history": lambda n : setattr(self, 'user_experience_analytics_device_metric_history', n.get_collection_of_object_values(user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory)),
            "user_experience_analytics_device_performance": lambda n : setattr(self, 'user_experience_analytics_device_performance', n.get_collection_of_object_values(user_experience_analytics_device_performance.UserExperienceAnalyticsDevicePerformance)),
            "user_experience_analytics_device_scope": lambda n : setattr(self, 'user_experience_analytics_device_scope', n.get_object_value(user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope)),
            "user_experience_analytics_device_scopes": lambda n : setattr(self, 'user_experience_analytics_device_scopes', n.get_collection_of_object_values(user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope)),
            "user_experience_analytics_device_scores": lambda n : setattr(self, 'user_experience_analytics_device_scores', n.get_collection_of_object_values(user_experience_analytics_device_scores.UserExperienceAnalyticsDeviceScores)),
            "user_experience_analytics_device_startup_history": lambda n : setattr(self, 'user_experience_analytics_device_startup_history', n.get_collection_of_object_values(user_experience_analytics_device_startup_history.UserExperienceAnalyticsDeviceStartupHistory)),
            "user_experience_analytics_device_startup_processes": lambda n : setattr(self, 'user_experience_analytics_device_startup_processes', n.get_collection_of_object_values(user_experience_analytics_device_startup_process.UserExperienceAnalyticsDeviceStartupProcess)),
            "user_experience_analytics_device_startup_process_performance": lambda n : setattr(self, 'user_experience_analytics_device_startup_process_performance', n.get_collection_of_object_values(user_experience_analytics_device_startup_process_performance.UserExperienceAnalyticsDeviceStartupProcessPerformance)),
            "user_experience_analytics_devices_without_cloud_identity": lambda n : setattr(self, 'user_experience_analytics_devices_without_cloud_identity', n.get_collection_of_object_values(user_experience_analytics_device_without_cloud_identity.UserExperienceAnalyticsDeviceWithoutCloudIdentity)),
            "user_experience_analytics_impacting_process": lambda n : setattr(self, 'user_experience_analytics_impacting_process', n.get_collection_of_object_values(user_experience_analytics_impacting_process.UserExperienceAnalyticsImpactingProcess)),
            "user_experience_analytics_metric_history": lambda n : setattr(self, 'user_experience_analytics_metric_history', n.get_collection_of_object_values(user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory)),
            "user_experience_analytics_model_scores": lambda n : setattr(self, 'user_experience_analytics_model_scores', n.get_collection_of_object_values(user_experience_analytics_model_scores.UserExperienceAnalyticsModelScores)),
            "user_experience_analytics_not_autopilot_ready_device": lambda n : setattr(self, 'user_experience_analytics_not_autopilot_ready_device', n.get_collection_of_object_values(user_experience_analytics_not_autopilot_ready_device.UserExperienceAnalyticsNotAutopilotReadyDevice)),
            "user_experience_analytics_overview": lambda n : setattr(self, 'user_experience_analytics_overview', n.get_object_value(user_experience_analytics_overview.UserExperienceAnalyticsOverview)),
            "user_experience_analytics_remote_connection": lambda n : setattr(self, 'user_experience_analytics_remote_connection', n.get_collection_of_object_values(user_experience_analytics_remote_connection.UserExperienceAnalyticsRemoteConnection)),
            "user_experience_analytics_resource_performance": lambda n : setattr(self, 'user_experience_analytics_resource_performance', n.get_collection_of_object_values(user_experience_analytics_resource_performance.UserExperienceAnalyticsResourcePerformance)),
            "user_experience_analytics_score_history": lambda n : setattr(self, 'user_experience_analytics_score_history', n.get_collection_of_object_values(user_experience_analytics_score_history.UserExperienceAnalyticsScoreHistory)),
            "user_experience_analytics_settings": lambda n : setattr(self, 'user_experience_analytics_settings', n.get_object_value(user_experience_analytics_settings.UserExperienceAnalyticsSettings)),
            "user_experience_analytics_work_from_anywhere_hardware_readiness_metric": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_hardware_readiness_metric', n.get_object_value(user_experience_analytics_work_from_anywhere_hardware_readiness_metric.UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric)),
            "user_experience_analytics_work_from_anywhere_metrics": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_metrics', n.get_collection_of_object_values(user_experience_analytics_work_from_anywhere_metric.UserExperienceAnalyticsWorkFromAnywhereMetric)),
            "user_experience_analytics_work_from_anywhere_model_performance": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_model_performance', n.get_collection_of_object_values(user_experience_analytics_work_from_anywhere_model_performance.UserExperienceAnalyticsWorkFromAnywhereModelPerformance)),
            "user_pfx_certificates": lambda n : setattr(self, 'user_pfx_certificates', n.get_collection_of_object_values(user_p_f_x_certificate.UserPFXCertificate)),
            "virtual_endpoint": lambda n : setattr(self, 'virtual_endpoint', n.get_object_value(virtual_endpoint.VirtualEndpoint)),
            "windows_autopilot_deployment_profiles": lambda n : setattr(self, 'windows_autopilot_deployment_profiles', n.get_collection_of_object_values(windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile)),
            "windows_autopilot_device_identities": lambda n : setattr(self, 'windows_autopilot_device_identities', n.get_collection_of_object_values(windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity)),
            "windows_autopilot_settings": lambda n : setattr(self, 'windows_autopilot_settings', n.get_object_value(windows_autopilot_settings.WindowsAutopilotSettings)),
            "windows_driver_update_profiles": lambda n : setattr(self, 'windows_driver_update_profiles', n.get_collection_of_object_values(windows_driver_update_profile.WindowsDriverUpdateProfile)),
            "windows_feature_update_profiles": lambda n : setattr(self, 'windows_feature_update_profiles', n.get_collection_of_object_values(windows_feature_update_profile.WindowsFeatureUpdateProfile)),
            "windows_information_protection_app_learning_summaries": lambda n : setattr(self, 'windows_information_protection_app_learning_summaries', n.get_collection_of_object_values(windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary)),
            "windows_information_protection_network_learning_summaries": lambda n : setattr(self, 'windows_information_protection_network_learning_summaries', n.get_collection_of_object_values(windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary)),
            "windows_malware_information": lambda n : setattr(self, 'windows_malware_information', n.get_collection_of_object_values(windows_malware_information.WindowsMalwareInformation)),
            "windows_malware_overview": lambda n : setattr(self, 'windows_malware_overview', n.get_object_value(windows_malware_overview.WindowsMalwareOverview)),
            "windows_quality_update_profiles": lambda n : setattr(self, 'windows_quality_update_profiles', n.get_collection_of_object_values(windows_quality_update_profile.WindowsQualityUpdateProfile)),
            "windows_update_catalog_items": lambda n : setattr(self, 'windows_update_catalog_items', n.get_collection_of_object_values(windows_update_catalog_item.WindowsUpdateCatalogItem)),
            "zebra_fota_artifacts": lambda n : setattr(self, 'zebra_fota_artifacts', n.get_collection_of_object_values(zebra_fota_artifact.ZebraFotaArtifact)),
            "zebra_fota_connector": lambda n : setattr(self, 'zebra_fota_connector', n.get_object_value(zebra_fota_connector.ZebraFotaConnector)),
            "zebra_fota_deployments": lambda n : setattr(self, 'zebra_fota_deployments', n.get_collection_of_object_values(zebra_fota_deployment.ZebraFotaDeployment)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_policy_categories(self,) -> Optional[List[group_policy_category.GroupPolicyCategory]]:
        """
        Gets the groupPolicyCategories property value. The available group policy categories for this account.
        Returns: Optional[List[group_policy_category.GroupPolicyCategory]]
        """
        return self._group_policy_categories
    
    @group_policy_categories.setter
    def group_policy_categories(self,value: Optional[List[group_policy_category.GroupPolicyCategory]] = None) -> None:
        """
        Sets the groupPolicyCategories property value. The available group policy categories for this account.
        Args:
            value: Value to set for the groupPolicyCategories property.
        """
        self._group_policy_categories = value
    
    @property
    def group_policy_configurations(self,) -> Optional[List[group_policy_configuration.GroupPolicyConfiguration]]:
        """
        Gets the groupPolicyConfigurations property value. The group policy configurations created by this account.
        Returns: Optional[List[group_policy_configuration.GroupPolicyConfiguration]]
        """
        return self._group_policy_configurations
    
    @group_policy_configurations.setter
    def group_policy_configurations(self,value: Optional[List[group_policy_configuration.GroupPolicyConfiguration]] = None) -> None:
        """
        Sets the groupPolicyConfigurations property value. The group policy configurations created by this account.
        Args:
            value: Value to set for the groupPolicyConfigurations property.
        """
        self._group_policy_configurations = value
    
    @property
    def group_policy_definition_files(self,) -> Optional[List[group_policy_definition_file.GroupPolicyDefinitionFile]]:
        """
        Gets the groupPolicyDefinitionFiles property value. The available group policy definition files for this account.
        Returns: Optional[List[group_policy_definition_file.GroupPolicyDefinitionFile]]
        """
        return self._group_policy_definition_files
    
    @group_policy_definition_files.setter
    def group_policy_definition_files(self,value: Optional[List[group_policy_definition_file.GroupPolicyDefinitionFile]] = None) -> None:
        """
        Sets the groupPolicyDefinitionFiles property value. The available group policy definition files for this account.
        Args:
            value: Value to set for the groupPolicyDefinitionFiles property.
        """
        self._group_policy_definition_files = value
    
    @property
    def group_policy_definitions(self,) -> Optional[List[group_policy_definition.GroupPolicyDefinition]]:
        """
        Gets the groupPolicyDefinitions property value. The available group policy definitions for this account.
        Returns: Optional[List[group_policy_definition.GroupPolicyDefinition]]
        """
        return self._group_policy_definitions
    
    @group_policy_definitions.setter
    def group_policy_definitions(self,value: Optional[List[group_policy_definition.GroupPolicyDefinition]] = None) -> None:
        """
        Sets the groupPolicyDefinitions property value. The available group policy definitions for this account.
        Args:
            value: Value to set for the groupPolicyDefinitions property.
        """
        self._group_policy_definitions = value
    
    @property
    def group_policy_migration_reports(self,) -> Optional[List[group_policy_migration_report.GroupPolicyMigrationReport]]:
        """
        Gets the groupPolicyMigrationReports property value. A list of Group Policy migration reports.
        Returns: Optional[List[group_policy_migration_report.GroupPolicyMigrationReport]]
        """
        return self._group_policy_migration_reports
    
    @group_policy_migration_reports.setter
    def group_policy_migration_reports(self,value: Optional[List[group_policy_migration_report.GroupPolicyMigrationReport]] = None) -> None:
        """
        Sets the groupPolicyMigrationReports property value. A list of Group Policy migration reports.
        Args:
            value: Value to set for the groupPolicyMigrationReports property.
        """
        self._group_policy_migration_reports = value
    
    @property
    def group_policy_object_files(self,) -> Optional[List[group_policy_object_file.GroupPolicyObjectFile]]:
        """
        Gets the groupPolicyObjectFiles property value. A list of Group Policy Object files uploaded.
        Returns: Optional[List[group_policy_object_file.GroupPolicyObjectFile]]
        """
        return self._group_policy_object_files
    
    @group_policy_object_files.setter
    def group_policy_object_files(self,value: Optional[List[group_policy_object_file.GroupPolicyObjectFile]] = None) -> None:
        """
        Sets the groupPolicyObjectFiles property value. A list of Group Policy Object files uploaded.
        Args:
            value: Value to set for the groupPolicyObjectFiles property.
        """
        self._group_policy_object_files = value
    
    @property
    def group_policy_uploaded_definition_files(self,) -> Optional[List[group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile]]:
        """
        Gets the groupPolicyUploadedDefinitionFiles property value. The available group policy uploaded definition files for this account.
        Returns: Optional[List[group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile]]
        """
        return self._group_policy_uploaded_definition_files
    
    @group_policy_uploaded_definition_files.setter
    def group_policy_uploaded_definition_files(self,value: Optional[List[group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile]] = None) -> None:
        """
        Sets the groupPolicyUploadedDefinitionFiles property value. The available group policy uploaded definition files for this account.
        Args:
            value: Value to set for the groupPolicyUploadedDefinitionFiles property.
        """
        self._group_policy_uploaded_definition_files = value
    
    @property
    def imported_device_identities(self,) -> Optional[List[imported_device_identity.ImportedDeviceIdentity]]:
        """
        Gets the importedDeviceIdentities property value. The imported device identities.
        Returns: Optional[List[imported_device_identity.ImportedDeviceIdentity]]
        """
        return self._imported_device_identities
    
    @imported_device_identities.setter
    def imported_device_identities(self,value: Optional[List[imported_device_identity.ImportedDeviceIdentity]] = None) -> None:
        """
        Sets the importedDeviceIdentities property value. The imported device identities.
        Args:
            value: Value to set for the importedDeviceIdentities property.
        """
        self._imported_device_identities = value
    
    @property
    def imported_windows_autopilot_device_identities(self,) -> Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]]:
        """
        Gets the importedWindowsAutopilotDeviceIdentities property value. Collection of imported Windows autopilot devices.
        Returns: Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]]
        """
        return self._imported_windows_autopilot_device_identities
    
    @imported_windows_autopilot_device_identities.setter
    def imported_windows_autopilot_device_identities(self,value: Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]] = None) -> None:
        """
        Sets the importedWindowsAutopilotDeviceIdentities property value. Collection of imported Windows autopilot devices.
        Args:
            value: Value to set for the importedWindowsAutopilotDeviceIdentities property.
        """
        self._imported_windows_autopilot_device_identities = value
    
    @property
    def intents(self,) -> Optional[List[device_management_intent.DeviceManagementIntent]]:
        """
        Gets the intents property value. The device management intents
        Returns: Optional[List[device_management_intent.DeviceManagementIntent]]
        """
        return self._intents
    
    @intents.setter
    def intents(self,value: Optional[List[device_management_intent.DeviceManagementIntent]] = None) -> None:
        """
        Sets the intents property value. The device management intents
        Args:
            value: Value to set for the intents property.
        """
        self._intents = value
    
    @property
    def intune_account_id(self,) -> Optional[Guid]:
        """
        Gets the intuneAccountId property value. Intune Account ID for given tenant
        Returns: Optional[Guid]
        """
        return self._intune_account_id
    
    @intune_account_id.setter
    def intune_account_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the intuneAccountId property value. Intune Account ID for given tenant
        Args:
            value: Value to set for the intuneAccountId property.
        """
        self._intune_account_id = value
    
    @property
    def intune_brand(self,) -> Optional[intune_brand.IntuneBrand]:
        """
        Gets the intuneBrand property value. intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
        Returns: Optional[intune_brand.IntuneBrand]
        """
        return self._intune_brand
    
    @intune_brand.setter
    def intune_brand(self,value: Optional[intune_brand.IntuneBrand] = None) -> None:
        """
        Sets the intuneBrand property value. intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
        Args:
            value: Value to set for the intuneBrand property.
        """
        self._intune_brand = value
    
    @property
    def intune_branding_profiles(self,) -> Optional[List[intune_branding_profile.IntuneBrandingProfile]]:
        """
        Gets the intuneBrandingProfiles property value. Intune branding profiles targeted to AAD groups
        Returns: Optional[List[intune_branding_profile.IntuneBrandingProfile]]
        """
        return self._intune_branding_profiles
    
    @intune_branding_profiles.setter
    def intune_branding_profiles(self,value: Optional[List[intune_branding_profile.IntuneBrandingProfile]] = None) -> None:
        """
        Sets the intuneBrandingProfiles property value. Intune branding profiles targeted to AAD groups
        Args:
            value: Value to set for the intuneBrandingProfiles property.
        """
        self._intune_branding_profiles = value
    
    @property
    def ios_update_statuses(self,) -> Optional[List[ios_update_device_status.IosUpdateDeviceStatus]]:
        """
        Gets the iosUpdateStatuses property value. The IOS software update installation statuses for this account.
        Returns: Optional[List[ios_update_device_status.IosUpdateDeviceStatus]]
        """
        return self._ios_update_statuses
    
    @ios_update_statuses.setter
    def ios_update_statuses(self,value: Optional[List[ios_update_device_status.IosUpdateDeviceStatus]] = None) -> None:
        """
        Sets the iosUpdateStatuses property value. The IOS software update installation statuses for this account.
        Args:
            value: Value to set for the iosUpdateStatuses property.
        """
        self._ios_update_statuses = value
    
    @property
    def last_report_aggregation_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastReportAggregationDateTime property value. The last modified time of reporting for this account. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._last_report_aggregation_date_time
    
    @last_report_aggregation_date_time.setter
    def last_report_aggregation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastReportAggregationDateTime property value. The last modified time of reporting for this account. This property is read-only.
        Args:
            value: Value to set for the lastReportAggregationDateTime property.
        """
        self._last_report_aggregation_date_time = value
    
    @property
    def legacy_pc_manangement_enabled(self,) -> Optional[bool]:
        """
        Gets the legacyPcManangementEnabled property value. The property to enable Non-MDM managed legacy PC management for this account. This property is read-only.
        Returns: Optional[bool]
        """
        return self._legacy_pc_manangement_enabled
    
    @legacy_pc_manangement_enabled.setter
    def legacy_pc_manangement_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the legacyPcManangementEnabled property value. The property to enable Non-MDM managed legacy PC management for this account. This property is read-only.
        Args:
            value: Value to set for the legacyPcManangementEnabled property.
        """
        self._legacy_pc_manangement_enabled = value
    
    @property
    def mac_o_s_software_update_account_summaries(self,) -> Optional[List[mac_o_s_software_update_account_summary.MacOSSoftwareUpdateAccountSummary]]:
        """
        Gets the macOSSoftwareUpdateAccountSummaries property value. The MacOS software update account summaries for this account.
        Returns: Optional[List[mac_o_s_software_update_account_summary.MacOSSoftwareUpdateAccountSummary]]
        """
        return self._mac_o_s_software_update_account_summaries
    
    @mac_o_s_software_update_account_summaries.setter
    def mac_o_s_software_update_account_summaries(self,value: Optional[List[mac_o_s_software_update_account_summary.MacOSSoftwareUpdateAccountSummary]] = None) -> None:
        """
        Sets the macOSSoftwareUpdateAccountSummaries property value. The MacOS software update account summaries for this account.
        Args:
            value: Value to set for the macOSSoftwareUpdateAccountSummaries property.
        """
        self._mac_o_s_software_update_account_summaries = value
    
    @property
    def managed_device_cleanup_settings(self,) -> Optional[managed_device_cleanup_settings.ManagedDeviceCleanupSettings]:
        """
        Gets the managedDeviceCleanupSettings property value. Device cleanup rule
        Returns: Optional[managed_device_cleanup_settings.ManagedDeviceCleanupSettings]
        """
        return self._managed_device_cleanup_settings
    
    @managed_device_cleanup_settings.setter
    def managed_device_cleanup_settings(self,value: Optional[managed_device_cleanup_settings.ManagedDeviceCleanupSettings] = None) -> None:
        """
        Sets the managedDeviceCleanupSettings property value. Device cleanup rule
        Args:
            value: Value to set for the managedDeviceCleanupSettings property.
        """
        self._managed_device_cleanup_settings = value
    
    @property
    def managed_device_encryption_states(self,) -> Optional[List[managed_device_encryption_state.ManagedDeviceEncryptionState]]:
        """
        Gets the managedDeviceEncryptionStates property value. Encryption report for devices in this account
        Returns: Optional[List[managed_device_encryption_state.ManagedDeviceEncryptionState]]
        """
        return self._managed_device_encryption_states
    
    @managed_device_encryption_states.setter
    def managed_device_encryption_states(self,value: Optional[List[managed_device_encryption_state.ManagedDeviceEncryptionState]] = None) -> None:
        """
        Sets the managedDeviceEncryptionStates property value. Encryption report for devices in this account
        Args:
            value: Value to set for the managedDeviceEncryptionStates property.
        """
        self._managed_device_encryption_states = value
    
    @property
    def managed_device_overview(self,) -> Optional[managed_device_overview.ManagedDeviceOverview]:
        """
        Gets the managedDeviceOverview property value. Device overview
        Returns: Optional[managed_device_overview.ManagedDeviceOverview]
        """
        return self._managed_device_overview
    
    @managed_device_overview.setter
    def managed_device_overview(self,value: Optional[managed_device_overview.ManagedDeviceOverview] = None) -> None:
        """
        Sets the managedDeviceOverview property value. Device overview
        Args:
            value: Value to set for the managedDeviceOverview property.
        """
        self._managed_device_overview = value
    
    @property
    def managed_devices(self,) -> Optional[List[managed_device.ManagedDevice]]:
        """
        Gets the managedDevices property value. The list of managed devices.
        Returns: Optional[List[managed_device.ManagedDevice]]
        """
        return self._managed_devices
    
    @managed_devices.setter
    def managed_devices(self,value: Optional[List[managed_device.ManagedDevice]] = None) -> None:
        """
        Sets the managedDevices property value. The list of managed devices.
        Args:
            value: Value to set for the managedDevices property.
        """
        self._managed_devices = value
    
    @property
    def maximum_dep_tokens(self,) -> Optional[int]:
        """
        Gets the maximumDepTokens property value. Maximum number of DEP tokens allowed per-tenant.
        Returns: Optional[int]
        """
        return self._maximum_dep_tokens
    
    @maximum_dep_tokens.setter
    def maximum_dep_tokens(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumDepTokens property value. Maximum number of DEP tokens allowed per-tenant.
        Args:
            value: Value to set for the maximumDepTokens property.
        """
        self._maximum_dep_tokens = value
    
    @property
    def microsoft_tunnel_configurations(self,) -> Optional[List[microsoft_tunnel_configuration.MicrosoftTunnelConfiguration]]:
        """
        Gets the microsoftTunnelConfigurations property value. Collection of MicrosoftTunnelConfiguration settings associated with account.
        Returns: Optional[List[microsoft_tunnel_configuration.MicrosoftTunnelConfiguration]]
        """
        return self._microsoft_tunnel_configurations
    
    @microsoft_tunnel_configurations.setter
    def microsoft_tunnel_configurations(self,value: Optional[List[microsoft_tunnel_configuration.MicrosoftTunnelConfiguration]] = None) -> None:
        """
        Sets the microsoftTunnelConfigurations property value. Collection of MicrosoftTunnelConfiguration settings associated with account.
        Args:
            value: Value to set for the microsoftTunnelConfigurations property.
        """
        self._microsoft_tunnel_configurations = value
    
    @property
    def microsoft_tunnel_health_thresholds(self,) -> Optional[List[microsoft_tunnel_health_threshold.MicrosoftTunnelHealthThreshold]]:
        """
        Gets the microsoftTunnelHealthThresholds property value. Collection of MicrosoftTunnelHealthThreshold settings associated with account.
        Returns: Optional[List[microsoft_tunnel_health_threshold.MicrosoftTunnelHealthThreshold]]
        """
        return self._microsoft_tunnel_health_thresholds
    
    @microsoft_tunnel_health_thresholds.setter
    def microsoft_tunnel_health_thresholds(self,value: Optional[List[microsoft_tunnel_health_threshold.MicrosoftTunnelHealthThreshold]] = None) -> None:
        """
        Sets the microsoftTunnelHealthThresholds property value. Collection of MicrosoftTunnelHealthThreshold settings associated with account.
        Args:
            value: Value to set for the microsoftTunnelHealthThresholds property.
        """
        self._microsoft_tunnel_health_thresholds = value
    
    @property
    def microsoft_tunnel_server_log_collection_responses(self,) -> Optional[List[microsoft_tunnel_server_log_collection_response.MicrosoftTunnelServerLogCollectionResponse]]:
        """
        Gets the microsoftTunnelServerLogCollectionResponses property value. Collection of MicrosoftTunnelServerLogCollectionResponse settings associated with account.
        Returns: Optional[List[microsoft_tunnel_server_log_collection_response.MicrosoftTunnelServerLogCollectionResponse]]
        """
        return self._microsoft_tunnel_server_log_collection_responses
    
    @microsoft_tunnel_server_log_collection_responses.setter
    def microsoft_tunnel_server_log_collection_responses(self,value: Optional[List[microsoft_tunnel_server_log_collection_response.MicrosoftTunnelServerLogCollectionResponse]] = None) -> None:
        """
        Sets the microsoftTunnelServerLogCollectionResponses property value. Collection of MicrosoftTunnelServerLogCollectionResponse settings associated with account.
        Args:
            value: Value to set for the microsoftTunnelServerLogCollectionResponses property.
        """
        self._microsoft_tunnel_server_log_collection_responses = value
    
    @property
    def microsoft_tunnel_sites(self,) -> Optional[List[microsoft_tunnel_site.MicrosoftTunnelSite]]:
        """
        Gets the microsoftTunnelSites property value. Collection of MicrosoftTunnelSite settings associated with account.
        Returns: Optional[List[microsoft_tunnel_site.MicrosoftTunnelSite]]
        """
        return self._microsoft_tunnel_sites
    
    @microsoft_tunnel_sites.setter
    def microsoft_tunnel_sites(self,value: Optional[List[microsoft_tunnel_site.MicrosoftTunnelSite]] = None) -> None:
        """
        Sets the microsoftTunnelSites property value. Collection of MicrosoftTunnelSite settings associated with account.
        Args:
            value: Value to set for the microsoftTunnelSites property.
        """
        self._microsoft_tunnel_sites = value
    
    @property
    def mobile_app_troubleshooting_events(self,) -> Optional[List[mobile_app_troubleshooting_event.MobileAppTroubleshootingEvent]]:
        """
        Gets the mobileAppTroubleshootingEvents property value. The collection property of MobileAppTroubleshootingEvent.
        Returns: Optional[List[mobile_app_troubleshooting_event.MobileAppTroubleshootingEvent]]
        """
        return self._mobile_app_troubleshooting_events
    
    @mobile_app_troubleshooting_events.setter
    def mobile_app_troubleshooting_events(self,value: Optional[List[mobile_app_troubleshooting_event.MobileAppTroubleshootingEvent]] = None) -> None:
        """
        Sets the mobileAppTroubleshootingEvents property value. The collection property of MobileAppTroubleshootingEvent.
        Args:
            value: Value to set for the mobileAppTroubleshootingEvents property.
        """
        self._mobile_app_troubleshooting_events = value
    
    @property
    def mobile_threat_defense_connectors(self,) -> Optional[List[mobile_threat_defense_connector.MobileThreatDefenseConnector]]:
        """
        Gets the mobileThreatDefenseConnectors property value. The list of Mobile threat Defense connectors configured by the tenant.
        Returns: Optional[List[mobile_threat_defense_connector.MobileThreatDefenseConnector]]
        """
        return self._mobile_threat_defense_connectors
    
    @mobile_threat_defense_connectors.setter
    def mobile_threat_defense_connectors(self,value: Optional[List[mobile_threat_defense_connector.MobileThreatDefenseConnector]] = None) -> None:
        """
        Sets the mobileThreatDefenseConnectors property value. The list of Mobile threat Defense connectors configured by the tenant.
        Args:
            value: Value to set for the mobileThreatDefenseConnectors property.
        """
        self._mobile_threat_defense_connectors = value
    
    @property
    def monitoring(self,) -> Optional[monitoring.Monitoring]:
        """
        Gets the monitoring property value. The monitoring property
        Returns: Optional[monitoring.Monitoring]
        """
        return self._monitoring
    
    @monitoring.setter
    def monitoring(self,value: Optional[monitoring.Monitoring] = None) -> None:
        """
        Sets the monitoring property value. The monitoring property
        Args:
            value: Value to set for the monitoring property.
        """
        self._monitoring = value
    
    @property
    def ndes_connectors(self,) -> Optional[List[ndes_connector.NdesConnector]]:
        """
        Gets the ndesConnectors property value. The collection of Ndes connectors for this account.
        Returns: Optional[List[ndes_connector.NdesConnector]]
        """
        return self._ndes_connectors
    
    @ndes_connectors.setter
    def ndes_connectors(self,value: Optional[List[ndes_connector.NdesConnector]] = None) -> None:
        """
        Sets the ndesConnectors property value. The collection of Ndes connectors for this account.
        Args:
            value: Value to set for the ndesConnectors property.
        """
        self._ndes_connectors = value
    
    @property
    def notification_message_templates(self,) -> Optional[List[notification_message_template.NotificationMessageTemplate]]:
        """
        Gets the notificationMessageTemplates property value. The Notification Message Templates.
        Returns: Optional[List[notification_message_template.NotificationMessageTemplate]]
        """
        return self._notification_message_templates
    
    @notification_message_templates.setter
    def notification_message_templates(self,value: Optional[List[notification_message_template.NotificationMessageTemplate]] = None) -> None:
        """
        Sets the notificationMessageTemplates property value. The Notification Message Templates.
        Args:
            value: Value to set for the notificationMessageTemplates property.
        """
        self._notification_message_templates = value
    
    @property
    def oem_warranty_information_onboarding(self,) -> Optional[List[oem_warranty_information_onboarding.OemWarrantyInformationOnboarding]]:
        """
        Gets the oemWarrantyInformationOnboarding property value. List of OEM Warranty Statuses
        Returns: Optional[List[oem_warranty_information_onboarding.OemWarrantyInformationOnboarding]]
        """
        return self._oem_warranty_information_onboarding
    
    @oem_warranty_information_onboarding.setter
    def oem_warranty_information_onboarding(self,value: Optional[List[oem_warranty_information_onboarding.OemWarrantyInformationOnboarding]] = None) -> None:
        """
        Sets the oemWarrantyInformationOnboarding property value. List of OEM Warranty Statuses
        Args:
            value: Value to set for the oemWarrantyInformationOnboarding property.
        """
        self._oem_warranty_information_onboarding = value
    
    @property
    def remote_action_audits(self,) -> Optional[List[remote_action_audit.RemoteActionAudit]]:
        """
        Gets the remoteActionAudits property value. The list of device remote action audits with the tenant.
        Returns: Optional[List[remote_action_audit.RemoteActionAudit]]
        """
        return self._remote_action_audits
    
    @remote_action_audits.setter
    def remote_action_audits(self,value: Optional[List[remote_action_audit.RemoteActionAudit]] = None) -> None:
        """
        Sets the remoteActionAudits property value. The list of device remote action audits with the tenant.
        Args:
            value: Value to set for the remoteActionAudits property.
        """
        self._remote_action_audits = value
    
    @property
    def remote_assistance_partners(self,) -> Optional[List[remote_assistance_partner.RemoteAssistancePartner]]:
        """
        Gets the remoteAssistancePartners property value. The remote assist partners.
        Returns: Optional[List[remote_assistance_partner.RemoteAssistancePartner]]
        """
        return self._remote_assistance_partners
    
    @remote_assistance_partners.setter
    def remote_assistance_partners(self,value: Optional[List[remote_assistance_partner.RemoteAssistancePartner]] = None) -> None:
        """
        Sets the remoteAssistancePartners property value. The remote assist partners.
        Args:
            value: Value to set for the remoteAssistancePartners property.
        """
        self._remote_assistance_partners = value
    
    @property
    def remote_assistance_settings(self,) -> Optional[remote_assistance_settings.RemoteAssistanceSettings]:
        """
        Gets the remoteAssistanceSettings property value. The remote assistance settings singleton
        Returns: Optional[remote_assistance_settings.RemoteAssistanceSettings]
        """
        return self._remote_assistance_settings
    
    @remote_assistance_settings.setter
    def remote_assistance_settings(self,value: Optional[remote_assistance_settings.RemoteAssistanceSettings] = None) -> None:
        """
        Sets the remoteAssistanceSettings property value. The remote assistance settings singleton
        Args:
            value: Value to set for the remoteAssistanceSettings property.
        """
        self._remote_assistance_settings = value
    
    @property
    def reports(self,) -> Optional[device_management_reports.DeviceManagementReports]:
        """
        Gets the reports property value. Reports singleton
        Returns: Optional[device_management_reports.DeviceManagementReports]
        """
        return self._reports
    
    @reports.setter
    def reports(self,value: Optional[device_management_reports.DeviceManagementReports] = None) -> None:
        """
        Sets the reports property value. Reports singleton
        Args:
            value: Value to set for the reports property.
        """
        self._reports = value
    
    @property
    def resource_access_profiles(self,) -> Optional[List[device_management_resource_access_profile_base.DeviceManagementResourceAccessProfileBase]]:
        """
        Gets the resourceAccessProfiles property value. Collection of resource access settings associated with account.
        Returns: Optional[List[device_management_resource_access_profile_base.DeviceManagementResourceAccessProfileBase]]
        """
        return self._resource_access_profiles
    
    @resource_access_profiles.setter
    def resource_access_profiles(self,value: Optional[List[device_management_resource_access_profile_base.DeviceManagementResourceAccessProfileBase]] = None) -> None:
        """
        Sets the resourceAccessProfiles property value. Collection of resource access settings associated with account.
        Args:
            value: Value to set for the resourceAccessProfiles property.
        """
        self._resource_access_profiles = value
    
    @property
    def resource_operations(self,) -> Optional[List[resource_operation.ResourceOperation]]:
        """
        Gets the resourceOperations property value. The Resource Operations.
        Returns: Optional[List[resource_operation.ResourceOperation]]
        """
        return self._resource_operations
    
    @resource_operations.setter
    def resource_operations(self,value: Optional[List[resource_operation.ResourceOperation]] = None) -> None:
        """
        Sets the resourceOperations property value. The Resource Operations.
        Args:
            value: Value to set for the resourceOperations property.
        """
        self._resource_operations = value
    
    @property
    def reusable_policy_settings(self,) -> Optional[List[device_management_reusable_policy_setting.DeviceManagementReusablePolicySetting]]:
        """
        Gets the reusablePolicySettings property value. List of all reusable settings that can be referred in a policy
        Returns: Optional[List[device_management_reusable_policy_setting.DeviceManagementReusablePolicySetting]]
        """
        return self._reusable_policy_settings
    
    @reusable_policy_settings.setter
    def reusable_policy_settings(self,value: Optional[List[device_management_reusable_policy_setting.DeviceManagementReusablePolicySetting]] = None) -> None:
        """
        Sets the reusablePolicySettings property value. List of all reusable settings that can be referred in a policy
        Args:
            value: Value to set for the reusablePolicySettings property.
        """
        self._reusable_policy_settings = value
    
    @property
    def reusable_settings(self,) -> Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]]:
        """
        Gets the reusableSettings property value. List of all reusable settings
        Returns: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]]
        """
        return self._reusable_settings
    
    @reusable_settings.setter
    def reusable_settings(self,value: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None) -> None:
        """
        Sets the reusableSettings property value. List of all reusable settings
        Args:
            value: Value to set for the reusableSettings property.
        """
        self._reusable_settings = value
    
    @property
    def role_assignments(self,) -> Optional[List[device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment]]:
        """
        Gets the roleAssignments property value. The Role Assignments.
        Returns: Optional[List[device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment]]
        """
        return self._role_assignments
    
    @role_assignments.setter
    def role_assignments(self,value: Optional[List[device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment]] = None) -> None:
        """
        Sets the roleAssignments property value. The Role Assignments.
        Args:
            value: Value to set for the roleAssignments property.
        """
        self._role_assignments = value
    
    @property
    def role_definitions(self,) -> Optional[List[role_definition.RoleDefinition]]:
        """
        Gets the roleDefinitions property value. The Role Definitions.
        Returns: Optional[List[role_definition.RoleDefinition]]
        """
        return self._role_definitions
    
    @role_definitions.setter
    def role_definitions(self,value: Optional[List[role_definition.RoleDefinition]] = None) -> None:
        """
        Sets the roleDefinitions property value. The Role Definitions.
        Args:
            value: Value to set for the roleDefinitions property.
        """
        self._role_definitions = value
    
    @property
    def role_scope_tags(self,) -> Optional[List[role_scope_tag.RoleScopeTag]]:
        """
        Gets the roleScopeTags property value. The Role Scope Tags.
        Returns: Optional[List[role_scope_tag.RoleScopeTag]]
        """
        return self._role_scope_tags
    
    @role_scope_tags.setter
    def role_scope_tags(self,value: Optional[List[role_scope_tag.RoleScopeTag]] = None) -> None:
        """
        Sets the roleScopeTags property value. The Role Scope Tags.
        Args:
            value: Value to set for the roleScopeTags property.
        """
        self._role_scope_tags = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
        writer.write_collection_of_object_values("deviceConfigurations", self.device_configurations)
        writer.write_collection_of_object_values("deviceConfigurationsAllManagedDeviceCertificateStates", self.device_configurations_all_managed_device_certificate_states)
        writer.write_object_value("deviceConfigurationUserStateSummaries", self.device_configuration_user_state_summaries)
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
        writer.write_object_value("intuneAccountId", self.intune_account_id)
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
        writer.write_collection_of_object_values("oemWarrantyInformationOnboarding", self.oem_warranty_information_onboarding)
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
        writer.write_collection_of_object_values("settingDefinitions", self.setting_definitions)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("softwareUpdateStatusSummary", self.software_update_status_summary)
        writer.write_enum_value("subscriptions", self.subscriptions)
        writer.write_enum_value("subscriptionState", self.subscription_state)
        writer.write_collection_of_object_values("telecomExpenseManagementPartners", self.telecom_expense_management_partners)
        writer.write_collection_of_object_values("templates", self.templates)
        writer.write_collection_of_object_values("templateSettings", self.template_settings)
        writer.write_object_value("tenantAttachRBAC", self.tenant_attach_r_b_a_c)
        writer.write_collection_of_object_values("termsAndConditions", self.terms_and_conditions)
        writer.write_collection_of_object_values("troubleshootingEvents", self.troubleshooting_events)
        writer.write_collection_of_object_values("userExperienceAnalyticsAnomaly", self.user_experience_analytics_anomaly)
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
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceStartupProcesses", self.user_experience_analytics_device_startup_processes)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceStartupProcessPerformance", self.user_experience_analytics_device_startup_process_performance)
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
    
    @property
    def setting_definitions(self,) -> Optional[List[device_management_setting_definition.DeviceManagementSettingDefinition]]:
        """
        Gets the settingDefinitions property value. The device management intent setting definitions
        Returns: Optional[List[device_management_setting_definition.DeviceManagementSettingDefinition]]
        """
        return self._setting_definitions
    
    @setting_definitions.setter
    def setting_definitions(self,value: Optional[List[device_management_setting_definition.DeviceManagementSettingDefinition]] = None) -> None:
        """
        Sets the settingDefinitions property value. The device management intent setting definitions
        Args:
            value: Value to set for the settingDefinitions property.
        """
        self._setting_definitions = value
    
    @property
    def settings(self,) -> Optional[device_management_settings.DeviceManagementSettings]:
        """
        Gets the settings property value. Account level settings.
        Returns: Optional[device_management_settings.DeviceManagementSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[device_management_settings.DeviceManagementSettings] = None) -> None:
        """
        Sets the settings property value. Account level settings.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def software_update_status_summary(self,) -> Optional[software_update_status_summary.SoftwareUpdateStatusSummary]:
        """
        Gets the softwareUpdateStatusSummary property value. The software update status summary.
        Returns: Optional[software_update_status_summary.SoftwareUpdateStatusSummary]
        """
        return self._software_update_status_summary
    
    @software_update_status_summary.setter
    def software_update_status_summary(self,value: Optional[software_update_status_summary.SoftwareUpdateStatusSummary] = None) -> None:
        """
        Sets the softwareUpdateStatusSummary property value. The software update status summary.
        Args:
            value: Value to set for the softwareUpdateStatusSummary property.
        """
        self._software_update_status_summary = value
    
    @property
    def subscriptions(self,) -> Optional[device_management_subscriptions.DeviceManagementSubscriptions]:
        """
        Gets the subscriptions property value. Tenant mobile device management subscriptions.
        Returns: Optional[device_management_subscriptions.DeviceManagementSubscriptions]
        """
        return self._subscriptions
    
    @subscriptions.setter
    def subscriptions(self,value: Optional[device_management_subscriptions.DeviceManagementSubscriptions] = None) -> None:
        """
        Sets the subscriptions property value. Tenant mobile device management subscriptions.
        Args:
            value: Value to set for the subscriptions property.
        """
        self._subscriptions = value
    
    @property
    def subscription_state(self,) -> Optional[device_management_subscription_state.DeviceManagementSubscriptionState]:
        """
        Gets the subscriptionState property value. Tenant mobile device management subscription state.
        Returns: Optional[device_management_subscription_state.DeviceManagementSubscriptionState]
        """
        return self._subscription_state
    
    @subscription_state.setter
    def subscription_state(self,value: Optional[device_management_subscription_state.DeviceManagementSubscriptionState] = None) -> None:
        """
        Sets the subscriptionState property value. Tenant mobile device management subscription state.
        Args:
            value: Value to set for the subscriptionState property.
        """
        self._subscription_state = value
    
    @property
    def telecom_expense_management_partners(self,) -> Optional[List[telecom_expense_management_partner.TelecomExpenseManagementPartner]]:
        """
        Gets the telecomExpenseManagementPartners property value. The telecom expense management partners.
        Returns: Optional[List[telecom_expense_management_partner.TelecomExpenseManagementPartner]]
        """
        return self._telecom_expense_management_partners
    
    @telecom_expense_management_partners.setter
    def telecom_expense_management_partners(self,value: Optional[List[telecom_expense_management_partner.TelecomExpenseManagementPartner]] = None) -> None:
        """
        Sets the telecomExpenseManagementPartners property value. The telecom expense management partners.
        Args:
            value: Value to set for the telecomExpenseManagementPartners property.
        """
        self._telecom_expense_management_partners = value
    
    @property
    def templates(self,) -> Optional[List[device_management_template.DeviceManagementTemplate]]:
        """
        Gets the templates property value. The available templates
        Returns: Optional[List[device_management_template.DeviceManagementTemplate]]
        """
        return self._templates
    
    @templates.setter
    def templates(self,value: Optional[List[device_management_template.DeviceManagementTemplate]] = None) -> None:
        """
        Sets the templates property value. The available templates
        Args:
            value: Value to set for the templates property.
        """
        self._templates = value
    
    @property
    def template_settings(self,) -> Optional[List[device_management_configuration_setting_template.DeviceManagementConfigurationSettingTemplate]]:
        """
        Gets the templateSettings property value. List of all TemplateSettings
        Returns: Optional[List[device_management_configuration_setting_template.DeviceManagementConfigurationSettingTemplate]]
        """
        return self._template_settings
    
    @template_settings.setter
    def template_settings(self,value: Optional[List[device_management_configuration_setting_template.DeviceManagementConfigurationSettingTemplate]] = None) -> None:
        """
        Sets the templateSettings property value. List of all TemplateSettings
        Args:
            value: Value to set for the templateSettings property.
        """
        self._template_settings = value
    
    @property
    def tenant_attach_r_b_a_c(self,) -> Optional[tenant_attach_r_b_a_c.TenantAttachRBAC]:
        """
        Gets the tenantAttachRBAC property value. TenantAttach RBAC Enablement
        Returns: Optional[tenant_attach_r_b_a_c.TenantAttachRBAC]
        """
        return self._tenant_attach_r_b_a_c
    
    @tenant_attach_r_b_a_c.setter
    def tenant_attach_r_b_a_c(self,value: Optional[tenant_attach_r_b_a_c.TenantAttachRBAC] = None) -> None:
        """
        Sets the tenantAttachRBAC property value. TenantAttach RBAC Enablement
        Args:
            value: Value to set for the tenantAttachRBAC property.
        """
        self._tenant_attach_r_b_a_c = value
    
    @property
    def terms_and_conditions(self,) -> Optional[List[terms_and_conditions.TermsAndConditions]]:
        """
        Gets the termsAndConditions property value. The terms and conditions associated with device management of the company.
        Returns: Optional[List[terms_and_conditions.TermsAndConditions]]
        """
        return self._terms_and_conditions
    
    @terms_and_conditions.setter
    def terms_and_conditions(self,value: Optional[List[terms_and_conditions.TermsAndConditions]] = None) -> None:
        """
        Sets the termsAndConditions property value. The terms and conditions associated with device management of the company.
        Args:
            value: Value to set for the termsAndConditions property.
        """
        self._terms_and_conditions = value
    
    @property
    def troubleshooting_events(self,) -> Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]]:
        """
        Gets the troubleshootingEvents property value. The list of troubleshooting events for the tenant.
        Returns: Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]]
        """
        return self._troubleshooting_events
    
    @troubleshooting_events.setter
    def troubleshooting_events(self,value: Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]] = None) -> None:
        """
        Sets the troubleshootingEvents property value. The list of troubleshooting events for the tenant.
        Args:
            value: Value to set for the troubleshootingEvents property.
        """
        self._troubleshooting_events = value
    
    @property
    def unlicensed_adminstrators_enabled(self,) -> Optional[bool]:
        """
        Gets the unlicensedAdminstratorsEnabled property value. When enabled, users assigned as administrators via Role Assignment Memberships do not require an assigned Intune license. Prior to this, only Intune licensed users were granted permissions with an Intune role unless they were assigned a role via Azure Active Directory. You are limited to 350 unlicensed direct members for each AAD security group in a role assignment, but you can assign multiple AAD security groups to a role if you need to support more than 350 unlicensed administrators. Licensed administrators are unaffected, do not have to be direct members, nor does the 350 member limit apply. This property is read-only.
        Returns: Optional[bool]
        """
        return self._unlicensed_adminstrators_enabled
    
    @unlicensed_adminstrators_enabled.setter
    def unlicensed_adminstrators_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the unlicensedAdminstratorsEnabled property value. When enabled, users assigned as administrators via Role Assignment Memberships do not require an assigned Intune license. Prior to this, only Intune licensed users were granted permissions with an Intune role unless they were assigned a role via Azure Active Directory. You are limited to 350 unlicensed direct members for each AAD security group in a role assignment, but you can assign multiple AAD security groups to a role if you need to support more than 350 unlicensed administrators. Licensed administrators are unaffected, do not have to be direct members, nor does the 350 member limit apply. This property is read-only.
        Args:
            value: Value to set for the unlicensedAdminstratorsEnabled property.
        """
        self._unlicensed_adminstrators_enabled = value
    
    @property
    def user_experience_analytics_anomaly(self,) -> Optional[List[user_experience_analytics_anomaly.UserExperienceAnalyticsAnomaly]]:
        """
        Gets the userExperienceAnalyticsAnomaly property value. The user experience analytics anomaly entity contains anomaly details.
        Returns: Optional[List[user_experience_analytics_anomaly.UserExperienceAnalyticsAnomaly]]
        """
        return self._user_experience_analytics_anomaly
    
    @user_experience_analytics_anomaly.setter
    def user_experience_analytics_anomaly(self,value: Optional[List[user_experience_analytics_anomaly.UserExperienceAnalyticsAnomaly]] = None) -> None:
        """
        Sets the userExperienceAnalyticsAnomaly property value. The user experience analytics anomaly entity contains anomaly details.
        Args:
            value: Value to set for the userExperienceAnalyticsAnomaly property.
        """
        self._user_experience_analytics_anomaly = value
    
    @property
    def user_experience_analytics_anomaly_device(self,) -> Optional[List[user_experience_analytics_anomaly_device.UserExperienceAnalyticsAnomalyDevice]]:
        """
        Gets the userExperienceAnalyticsAnomalyDevice property value. The user experience analytics anomaly entity contains device details.
        Returns: Optional[List[user_experience_analytics_anomaly_device.UserExperienceAnalyticsAnomalyDevice]]
        """
        return self._user_experience_analytics_anomaly_device
    
    @user_experience_analytics_anomaly_device.setter
    def user_experience_analytics_anomaly_device(self,value: Optional[List[user_experience_analytics_anomaly_device.UserExperienceAnalyticsAnomalyDevice]] = None) -> None:
        """
        Sets the userExperienceAnalyticsAnomalyDevice property value. The user experience analytics anomaly entity contains device details.
        Args:
            value: Value to set for the userExperienceAnalyticsAnomalyDevice property.
        """
        self._user_experience_analytics_anomaly_device = value
    
    @property
    def user_experience_analytics_anomaly_severity_overview(self,) -> Optional[user_experience_analytics_anomaly_severity_overview.UserExperienceAnalyticsAnomalySeverityOverview]:
        """
        Gets the userExperienceAnalyticsAnomalySeverityOverview property value. The user experience analytics anomaly severity overview entity contains the count information for each severity of anomaly.
        Returns: Optional[user_experience_analytics_anomaly_severity_overview.UserExperienceAnalyticsAnomalySeverityOverview]
        """
        return self._user_experience_analytics_anomaly_severity_overview
    
    @user_experience_analytics_anomaly_severity_overview.setter
    def user_experience_analytics_anomaly_severity_overview(self,value: Optional[user_experience_analytics_anomaly_severity_overview.UserExperienceAnalyticsAnomalySeverityOverview] = None) -> None:
        """
        Sets the userExperienceAnalyticsAnomalySeverityOverview property value. The user experience analytics anomaly severity overview entity contains the count information for each severity of anomaly.
        Args:
            value: Value to set for the userExperienceAnalyticsAnomalySeverityOverview property.
        """
        self._user_experience_analytics_anomaly_severity_overview = value
    
    @property
    def user_experience_analytics_app_health_application_performance(self,) -> Optional[List[user_experience_analytics_app_health_application_performance.UserExperienceAnalyticsAppHealthApplicationPerformance]]:
        """
        Gets the userExperienceAnalyticsAppHealthApplicationPerformance property value. User experience analytics appHealth Application Performance
        Returns: Optional[List[user_experience_analytics_app_health_application_performance.UserExperienceAnalyticsAppHealthApplicationPerformance]]
        """
        return self._user_experience_analytics_app_health_application_performance
    
    @user_experience_analytics_app_health_application_performance.setter
    def user_experience_analytics_app_health_application_performance(self,value: Optional[List[user_experience_analytics_app_health_application_performance.UserExperienceAnalyticsAppHealthApplicationPerformance]] = None) -> None:
        """
        Sets the userExperienceAnalyticsAppHealthApplicationPerformance property value. User experience analytics appHealth Application Performance
        Args:
            value: Value to set for the userExperienceAnalyticsAppHealthApplicationPerformance property.
        """
        self._user_experience_analytics_app_health_application_performance = value
    
    @property
    def user_experience_analytics_app_health_application_performance_by_app_version(self,) -> Optional[List[user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion]]:
        """
        Gets the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion property value. User experience analytics appHealth Application Performance by App Version
        Returns: Optional[List[user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion]]
        """
        return self._user_experience_analytics_app_health_application_performance_by_app_version
    
    @user_experience_analytics_app_health_application_performance_by_app_version.setter
    def user_experience_analytics_app_health_application_performance_by_app_version(self,value: Optional[List[user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion]] = None) -> None:
        """
        Sets the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion property value. User experience analytics appHealth Application Performance by App Version
        Args:
            value: Value to set for the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion property.
        """
        self._user_experience_analytics_app_health_application_performance_by_app_version = value
    
    @property
    def user_experience_analytics_app_health_application_performance_by_app_version_details(self,) -> Optional[List[user_experience_analytics_app_health_app_performance_by_app_version_details.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails]]:
        """
        Gets the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails property value. User experience analytics appHealth Application Performance by App Version details
        Returns: Optional[List[user_experience_analytics_app_health_app_performance_by_app_version_details.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails]]
        """
        return self._user_experience_analytics_app_health_application_performance_by_app_version_details
    
    @user_experience_analytics_app_health_application_performance_by_app_version_details.setter
    def user_experience_analytics_app_health_application_performance_by_app_version_details(self,value: Optional[List[user_experience_analytics_app_health_app_performance_by_app_version_details.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails]] = None) -> None:
        """
        Sets the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails property value. User experience analytics appHealth Application Performance by App Version details
        Args:
            value: Value to set for the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails property.
        """
        self._user_experience_analytics_app_health_application_performance_by_app_version_details = value
    
    @property
    def user_experience_analytics_app_health_application_performance_by_app_version_device_id(self,) -> Optional[List[user_experience_analytics_app_health_app_performance_by_app_version_device_id.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId]]:
        """
        Gets the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId property value. User experience analytics appHealth Application Performance by App Version Device Id
        Returns: Optional[List[user_experience_analytics_app_health_app_performance_by_app_version_device_id.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId]]
        """
        return self._user_experience_analytics_app_health_application_performance_by_app_version_device_id
    
    @user_experience_analytics_app_health_application_performance_by_app_version_device_id.setter
    def user_experience_analytics_app_health_application_performance_by_app_version_device_id(self,value: Optional[List[user_experience_analytics_app_health_app_performance_by_app_version_device_id.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId]] = None) -> None:
        """
        Sets the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId property value. User experience analytics appHealth Application Performance by App Version Device Id
        Args:
            value: Value to set for the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId property.
        """
        self._user_experience_analytics_app_health_application_performance_by_app_version_device_id = value
    
    @property
    def user_experience_analytics_app_health_application_performance_by_o_s_version(self,) -> Optional[List[user_experience_analytics_app_health_app_performance_by_o_s_version.UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion]]:
        """
        Gets the userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion property value. User experience analytics appHealth Application Performance by OS Version
        Returns: Optional[List[user_experience_analytics_app_health_app_performance_by_o_s_version.UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion]]
        """
        return self._user_experience_analytics_app_health_application_performance_by_o_s_version
    
    @user_experience_analytics_app_health_application_performance_by_o_s_version.setter
    def user_experience_analytics_app_health_application_performance_by_o_s_version(self,value: Optional[List[user_experience_analytics_app_health_app_performance_by_o_s_version.UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion]] = None) -> None:
        """
        Sets the userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion property value. User experience analytics appHealth Application Performance by OS Version
        Args:
            value: Value to set for the userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion property.
        """
        self._user_experience_analytics_app_health_application_performance_by_o_s_version = value
    
    @property
    def user_experience_analytics_app_health_device_model_performance(self,) -> Optional[List[user_experience_analytics_app_health_device_model_performance.UserExperienceAnalyticsAppHealthDeviceModelPerformance]]:
        """
        Gets the userExperienceAnalyticsAppHealthDeviceModelPerformance property value. User experience analytics appHealth Model Performance
        Returns: Optional[List[user_experience_analytics_app_health_device_model_performance.UserExperienceAnalyticsAppHealthDeviceModelPerformance]]
        """
        return self._user_experience_analytics_app_health_device_model_performance
    
    @user_experience_analytics_app_health_device_model_performance.setter
    def user_experience_analytics_app_health_device_model_performance(self,value: Optional[List[user_experience_analytics_app_health_device_model_performance.UserExperienceAnalyticsAppHealthDeviceModelPerformance]] = None) -> None:
        """
        Sets the userExperienceAnalyticsAppHealthDeviceModelPerformance property value. User experience analytics appHealth Model Performance
        Args:
            value: Value to set for the userExperienceAnalyticsAppHealthDeviceModelPerformance property.
        """
        self._user_experience_analytics_app_health_device_model_performance = value
    
    @property
    def user_experience_analytics_app_health_device_performance(self,) -> Optional[List[user_experience_analytics_app_health_device_performance.UserExperienceAnalyticsAppHealthDevicePerformance]]:
        """
        Gets the userExperienceAnalyticsAppHealthDevicePerformance property value. User experience analytics appHealth Device Performance
        Returns: Optional[List[user_experience_analytics_app_health_device_performance.UserExperienceAnalyticsAppHealthDevicePerformance]]
        """
        return self._user_experience_analytics_app_health_device_performance
    
    @user_experience_analytics_app_health_device_performance.setter
    def user_experience_analytics_app_health_device_performance(self,value: Optional[List[user_experience_analytics_app_health_device_performance.UserExperienceAnalyticsAppHealthDevicePerformance]] = None) -> None:
        """
        Sets the userExperienceAnalyticsAppHealthDevicePerformance property value. User experience analytics appHealth Device Performance
        Args:
            value: Value to set for the userExperienceAnalyticsAppHealthDevicePerformance property.
        """
        self._user_experience_analytics_app_health_device_performance = value
    
    @property
    def user_experience_analytics_app_health_device_performance_details(self,) -> Optional[List[user_experience_analytics_app_health_device_performance_details.UserExperienceAnalyticsAppHealthDevicePerformanceDetails]]:
        """
        Gets the userExperienceAnalyticsAppHealthDevicePerformanceDetails property value. User experience analytics device performance details
        Returns: Optional[List[user_experience_analytics_app_health_device_performance_details.UserExperienceAnalyticsAppHealthDevicePerformanceDetails]]
        """
        return self._user_experience_analytics_app_health_device_performance_details
    
    @user_experience_analytics_app_health_device_performance_details.setter
    def user_experience_analytics_app_health_device_performance_details(self,value: Optional[List[user_experience_analytics_app_health_device_performance_details.UserExperienceAnalyticsAppHealthDevicePerformanceDetails]] = None) -> None:
        """
        Sets the userExperienceAnalyticsAppHealthDevicePerformanceDetails property value. User experience analytics device performance details
        Args:
            value: Value to set for the userExperienceAnalyticsAppHealthDevicePerformanceDetails property.
        """
        self._user_experience_analytics_app_health_device_performance_details = value
    
    @property
    def user_experience_analytics_app_health_o_s_version_performance(self,) -> Optional[List[user_experience_analytics_app_health_o_s_version_performance.UserExperienceAnalyticsAppHealthOSVersionPerformance]]:
        """
        Gets the userExperienceAnalyticsAppHealthOSVersionPerformance property value. User experience analytics appHealth OS version Performance
        Returns: Optional[List[user_experience_analytics_app_health_o_s_version_performance.UserExperienceAnalyticsAppHealthOSVersionPerformance]]
        """
        return self._user_experience_analytics_app_health_o_s_version_performance
    
    @user_experience_analytics_app_health_o_s_version_performance.setter
    def user_experience_analytics_app_health_o_s_version_performance(self,value: Optional[List[user_experience_analytics_app_health_o_s_version_performance.UserExperienceAnalyticsAppHealthOSVersionPerformance]] = None) -> None:
        """
        Sets the userExperienceAnalyticsAppHealthOSVersionPerformance property value. User experience analytics appHealth OS version Performance
        Args:
            value: Value to set for the userExperienceAnalyticsAppHealthOSVersionPerformance property.
        """
        self._user_experience_analytics_app_health_o_s_version_performance = value
    
    @property
    def user_experience_analytics_app_health_overview(self,) -> Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]:
        """
        Gets the userExperienceAnalyticsAppHealthOverview property value. User experience analytics appHealth overview
        Returns: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]
        """
        return self._user_experience_analytics_app_health_overview
    
    @user_experience_analytics_app_health_overview.setter
    def user_experience_analytics_app_health_overview(self,value: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None) -> None:
        """
        Sets the userExperienceAnalyticsAppHealthOverview property value. User experience analytics appHealth overview
        Args:
            value: Value to set for the userExperienceAnalyticsAppHealthOverview property.
        """
        self._user_experience_analytics_app_health_overview = value
    
    @property
    def user_experience_analytics_baselines(self,) -> Optional[List[user_experience_analytics_baseline.UserExperienceAnalyticsBaseline]]:
        """
        Gets the userExperienceAnalyticsBaselines property value. User experience analytics baselines
        Returns: Optional[List[user_experience_analytics_baseline.UserExperienceAnalyticsBaseline]]
        """
        return self._user_experience_analytics_baselines
    
    @user_experience_analytics_baselines.setter
    def user_experience_analytics_baselines(self,value: Optional[List[user_experience_analytics_baseline.UserExperienceAnalyticsBaseline]] = None) -> None:
        """
        Sets the userExperienceAnalyticsBaselines property value. User experience analytics baselines
        Args:
            value: Value to set for the userExperienceAnalyticsBaselines property.
        """
        self._user_experience_analytics_baselines = value
    
    @property
    def user_experience_analytics_battery_health_app_impact(self,) -> Optional[List[user_experience_analytics_battery_health_app_impact.UserExperienceAnalyticsBatteryHealthAppImpact]]:
        """
        Gets the userExperienceAnalyticsBatteryHealthAppImpact property value. User Experience Analytics Battery Health App Impact
        Returns: Optional[List[user_experience_analytics_battery_health_app_impact.UserExperienceAnalyticsBatteryHealthAppImpact]]
        """
        return self._user_experience_analytics_battery_health_app_impact
    
    @user_experience_analytics_battery_health_app_impact.setter
    def user_experience_analytics_battery_health_app_impact(self,value: Optional[List[user_experience_analytics_battery_health_app_impact.UserExperienceAnalyticsBatteryHealthAppImpact]] = None) -> None:
        """
        Sets the userExperienceAnalyticsBatteryHealthAppImpact property value. User Experience Analytics Battery Health App Impact
        Args:
            value: Value to set for the userExperienceAnalyticsBatteryHealthAppImpact property.
        """
        self._user_experience_analytics_battery_health_app_impact = value
    
    @property
    def user_experience_analytics_battery_health_capacity_details(self,) -> Optional[user_experience_analytics_battery_health_capacity_details.UserExperienceAnalyticsBatteryHealthCapacityDetails]:
        """
        Gets the userExperienceAnalyticsBatteryHealthCapacityDetails property value. User Experience Analytics Battery Health Capacity Details
        Returns: Optional[user_experience_analytics_battery_health_capacity_details.UserExperienceAnalyticsBatteryHealthCapacityDetails]
        """
        return self._user_experience_analytics_battery_health_capacity_details
    
    @user_experience_analytics_battery_health_capacity_details.setter
    def user_experience_analytics_battery_health_capacity_details(self,value: Optional[user_experience_analytics_battery_health_capacity_details.UserExperienceAnalyticsBatteryHealthCapacityDetails] = None) -> None:
        """
        Sets the userExperienceAnalyticsBatteryHealthCapacityDetails property value. User Experience Analytics Battery Health Capacity Details
        Args:
            value: Value to set for the userExperienceAnalyticsBatteryHealthCapacityDetails property.
        """
        self._user_experience_analytics_battery_health_capacity_details = value
    
    @property
    def user_experience_analytics_battery_health_device_app_impact(self,) -> Optional[List[user_experience_analytics_battery_health_device_app_impact.UserExperienceAnalyticsBatteryHealthDeviceAppImpact]]:
        """
        Gets the userExperienceAnalyticsBatteryHealthDeviceAppImpact property value. User Experience Analytics Battery Health Device App Impact
        Returns: Optional[List[user_experience_analytics_battery_health_device_app_impact.UserExperienceAnalyticsBatteryHealthDeviceAppImpact]]
        """
        return self._user_experience_analytics_battery_health_device_app_impact
    
    @user_experience_analytics_battery_health_device_app_impact.setter
    def user_experience_analytics_battery_health_device_app_impact(self,value: Optional[List[user_experience_analytics_battery_health_device_app_impact.UserExperienceAnalyticsBatteryHealthDeviceAppImpact]] = None) -> None:
        """
        Sets the userExperienceAnalyticsBatteryHealthDeviceAppImpact property value. User Experience Analytics Battery Health Device App Impact
        Args:
            value: Value to set for the userExperienceAnalyticsBatteryHealthDeviceAppImpact property.
        """
        self._user_experience_analytics_battery_health_device_app_impact = value
    
    @property
    def user_experience_analytics_battery_health_device_performance(self,) -> Optional[List[user_experience_analytics_battery_health_device_performance.UserExperienceAnalyticsBatteryHealthDevicePerformance]]:
        """
        Gets the userExperienceAnalyticsBatteryHealthDevicePerformance property value. User Experience Analytics Battery Health Device Performance
        Returns: Optional[List[user_experience_analytics_battery_health_device_performance.UserExperienceAnalyticsBatteryHealthDevicePerformance]]
        """
        return self._user_experience_analytics_battery_health_device_performance
    
    @user_experience_analytics_battery_health_device_performance.setter
    def user_experience_analytics_battery_health_device_performance(self,value: Optional[List[user_experience_analytics_battery_health_device_performance.UserExperienceAnalyticsBatteryHealthDevicePerformance]] = None) -> None:
        """
        Sets the userExperienceAnalyticsBatteryHealthDevicePerformance property value. User Experience Analytics Battery Health Device Performance
        Args:
            value: Value to set for the userExperienceAnalyticsBatteryHealthDevicePerformance property.
        """
        self._user_experience_analytics_battery_health_device_performance = value
    
    @property
    def user_experience_analytics_battery_health_device_runtime_history(self,) -> Optional[List[user_experience_analytics_battery_health_device_runtime_history.UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory]]:
        """
        Gets the userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory property value. User Experience Analytics Battery Health Device Runtime History
        Returns: Optional[List[user_experience_analytics_battery_health_device_runtime_history.UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory]]
        """
        return self._user_experience_analytics_battery_health_device_runtime_history
    
    @user_experience_analytics_battery_health_device_runtime_history.setter
    def user_experience_analytics_battery_health_device_runtime_history(self,value: Optional[List[user_experience_analytics_battery_health_device_runtime_history.UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory]] = None) -> None:
        """
        Sets the userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory property value. User Experience Analytics Battery Health Device Runtime History
        Args:
            value: Value to set for the userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory property.
        """
        self._user_experience_analytics_battery_health_device_runtime_history = value
    
    @property
    def user_experience_analytics_battery_health_model_performance(self,) -> Optional[List[user_experience_analytics_battery_health_model_performance.UserExperienceAnalyticsBatteryHealthModelPerformance]]:
        """
        Gets the userExperienceAnalyticsBatteryHealthModelPerformance property value. User Experience Analytics Battery Health Model Performance
        Returns: Optional[List[user_experience_analytics_battery_health_model_performance.UserExperienceAnalyticsBatteryHealthModelPerformance]]
        """
        return self._user_experience_analytics_battery_health_model_performance
    
    @user_experience_analytics_battery_health_model_performance.setter
    def user_experience_analytics_battery_health_model_performance(self,value: Optional[List[user_experience_analytics_battery_health_model_performance.UserExperienceAnalyticsBatteryHealthModelPerformance]] = None) -> None:
        """
        Sets the userExperienceAnalyticsBatteryHealthModelPerformance property value. User Experience Analytics Battery Health Model Performance
        Args:
            value: Value to set for the userExperienceAnalyticsBatteryHealthModelPerformance property.
        """
        self._user_experience_analytics_battery_health_model_performance = value
    
    @property
    def user_experience_analytics_battery_health_os_performance(self,) -> Optional[List[user_experience_analytics_battery_health_os_performance.UserExperienceAnalyticsBatteryHealthOsPerformance]]:
        """
        Gets the userExperienceAnalyticsBatteryHealthOsPerformance property value. User Experience Analytics Battery Health Os Performance
        Returns: Optional[List[user_experience_analytics_battery_health_os_performance.UserExperienceAnalyticsBatteryHealthOsPerformance]]
        """
        return self._user_experience_analytics_battery_health_os_performance
    
    @user_experience_analytics_battery_health_os_performance.setter
    def user_experience_analytics_battery_health_os_performance(self,value: Optional[List[user_experience_analytics_battery_health_os_performance.UserExperienceAnalyticsBatteryHealthOsPerformance]] = None) -> None:
        """
        Sets the userExperienceAnalyticsBatteryHealthOsPerformance property value. User Experience Analytics Battery Health Os Performance
        Args:
            value: Value to set for the userExperienceAnalyticsBatteryHealthOsPerformance property.
        """
        self._user_experience_analytics_battery_health_os_performance = value
    
    @property
    def user_experience_analytics_battery_health_runtime_details(self,) -> Optional[user_experience_analytics_battery_health_runtime_details.UserExperienceAnalyticsBatteryHealthRuntimeDetails]:
        """
        Gets the userExperienceAnalyticsBatteryHealthRuntimeDetails property value. User Experience Analytics Battery Health Runtime Details
        Returns: Optional[user_experience_analytics_battery_health_runtime_details.UserExperienceAnalyticsBatteryHealthRuntimeDetails]
        """
        return self._user_experience_analytics_battery_health_runtime_details
    
    @user_experience_analytics_battery_health_runtime_details.setter
    def user_experience_analytics_battery_health_runtime_details(self,value: Optional[user_experience_analytics_battery_health_runtime_details.UserExperienceAnalyticsBatteryHealthRuntimeDetails] = None) -> None:
        """
        Sets the userExperienceAnalyticsBatteryHealthRuntimeDetails property value. User Experience Analytics Battery Health Runtime Details
        Args:
            value: Value to set for the userExperienceAnalyticsBatteryHealthRuntimeDetails property.
        """
        self._user_experience_analytics_battery_health_runtime_details = value
    
    @property
    def user_experience_analytics_categories(self,) -> Optional[List[user_experience_analytics_category.UserExperienceAnalyticsCategory]]:
        """
        Gets the userExperienceAnalyticsCategories property value. User experience analytics categories
        Returns: Optional[List[user_experience_analytics_category.UserExperienceAnalyticsCategory]]
        """
        return self._user_experience_analytics_categories
    
    @user_experience_analytics_categories.setter
    def user_experience_analytics_categories(self,value: Optional[List[user_experience_analytics_category.UserExperienceAnalyticsCategory]] = None) -> None:
        """
        Sets the userExperienceAnalyticsCategories property value. User experience analytics categories
        Args:
            value: Value to set for the userExperienceAnalyticsCategories property.
        """
        self._user_experience_analytics_categories = value
    
    @property
    def user_experience_analytics_device_metric_history(self,) -> Optional[List[user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory]]:
        """
        Gets the userExperienceAnalyticsDeviceMetricHistory property value. User experience analytics device metric history
        Returns: Optional[List[user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory]]
        """
        return self._user_experience_analytics_device_metric_history
    
    @user_experience_analytics_device_metric_history.setter
    def user_experience_analytics_device_metric_history(self,value: Optional[List[user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory]] = None) -> None:
        """
        Sets the userExperienceAnalyticsDeviceMetricHistory property value. User experience analytics device metric history
        Args:
            value: Value to set for the userExperienceAnalyticsDeviceMetricHistory property.
        """
        self._user_experience_analytics_device_metric_history = value
    
    @property
    def user_experience_analytics_device_performance(self,) -> Optional[List[user_experience_analytics_device_performance.UserExperienceAnalyticsDevicePerformance]]:
        """
        Gets the userExperienceAnalyticsDevicePerformance property value. User experience analytics device performance
        Returns: Optional[List[user_experience_analytics_device_performance.UserExperienceAnalyticsDevicePerformance]]
        """
        return self._user_experience_analytics_device_performance
    
    @user_experience_analytics_device_performance.setter
    def user_experience_analytics_device_performance(self,value: Optional[List[user_experience_analytics_device_performance.UserExperienceAnalyticsDevicePerformance]] = None) -> None:
        """
        Sets the userExperienceAnalyticsDevicePerformance property value. User experience analytics device performance
        Args:
            value: Value to set for the userExperienceAnalyticsDevicePerformance property.
        """
        self._user_experience_analytics_device_performance = value
    
    @property
    def user_experience_analytics_device_scope(self,) -> Optional[user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope]:
        """
        Gets the userExperienceAnalyticsDeviceScope property value. The user experience analytics device scope entity endpoint to trigger on the service to either START or STOP computing metrics data based on a device scope configuration.
        Returns: Optional[user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope]
        """
        return self._user_experience_analytics_device_scope
    
    @user_experience_analytics_device_scope.setter
    def user_experience_analytics_device_scope(self,value: Optional[user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope] = None) -> None:
        """
        Sets the userExperienceAnalyticsDeviceScope property value. The user experience analytics device scope entity endpoint to trigger on the service to either START or STOP computing metrics data based on a device scope configuration.
        Args:
            value: Value to set for the userExperienceAnalyticsDeviceScope property.
        """
        self._user_experience_analytics_device_scope = value
    
    @property
    def user_experience_analytics_device_scopes(self,) -> Optional[List[user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope]]:
        """
        Gets the userExperienceAnalyticsDeviceScopes property value. The user experience analytics device scope entity contains device scope configuration use to apply filtering on the endpoint analytics reports.
        Returns: Optional[List[user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope]]
        """
        return self._user_experience_analytics_device_scopes
    
    @user_experience_analytics_device_scopes.setter
    def user_experience_analytics_device_scopes(self,value: Optional[List[user_experience_analytics_device_scope.UserExperienceAnalyticsDeviceScope]] = None) -> None:
        """
        Sets the userExperienceAnalyticsDeviceScopes property value. The user experience analytics device scope entity contains device scope configuration use to apply filtering on the endpoint analytics reports.
        Args:
            value: Value to set for the userExperienceAnalyticsDeviceScopes property.
        """
        self._user_experience_analytics_device_scopes = value
    
    @property
    def user_experience_analytics_device_scores(self,) -> Optional[List[user_experience_analytics_device_scores.UserExperienceAnalyticsDeviceScores]]:
        """
        Gets the userExperienceAnalyticsDeviceScores property value. User experience analytics device scores
        Returns: Optional[List[user_experience_analytics_device_scores.UserExperienceAnalyticsDeviceScores]]
        """
        return self._user_experience_analytics_device_scores
    
    @user_experience_analytics_device_scores.setter
    def user_experience_analytics_device_scores(self,value: Optional[List[user_experience_analytics_device_scores.UserExperienceAnalyticsDeviceScores]] = None) -> None:
        """
        Sets the userExperienceAnalyticsDeviceScores property value. User experience analytics device scores
        Args:
            value: Value to set for the userExperienceAnalyticsDeviceScores property.
        """
        self._user_experience_analytics_device_scores = value
    
    @property
    def user_experience_analytics_device_startup_history(self,) -> Optional[List[user_experience_analytics_device_startup_history.UserExperienceAnalyticsDeviceStartupHistory]]:
        """
        Gets the userExperienceAnalyticsDeviceStartupHistory property value. User experience analytics device Startup History
        Returns: Optional[List[user_experience_analytics_device_startup_history.UserExperienceAnalyticsDeviceStartupHistory]]
        """
        return self._user_experience_analytics_device_startup_history
    
    @user_experience_analytics_device_startup_history.setter
    def user_experience_analytics_device_startup_history(self,value: Optional[List[user_experience_analytics_device_startup_history.UserExperienceAnalyticsDeviceStartupHistory]] = None) -> None:
        """
        Sets the userExperienceAnalyticsDeviceStartupHistory property value. User experience analytics device Startup History
        Args:
            value: Value to set for the userExperienceAnalyticsDeviceStartupHistory property.
        """
        self._user_experience_analytics_device_startup_history = value
    
    @property
    def user_experience_analytics_device_startup_processes(self,) -> Optional[List[user_experience_analytics_device_startup_process.UserExperienceAnalyticsDeviceStartupProcess]]:
        """
        Gets the userExperienceAnalyticsDeviceStartupProcesses property value. User experience analytics device Startup Processes
        Returns: Optional[List[user_experience_analytics_device_startup_process.UserExperienceAnalyticsDeviceStartupProcess]]
        """
        return self._user_experience_analytics_device_startup_processes
    
    @user_experience_analytics_device_startup_processes.setter
    def user_experience_analytics_device_startup_processes(self,value: Optional[List[user_experience_analytics_device_startup_process.UserExperienceAnalyticsDeviceStartupProcess]] = None) -> None:
        """
        Sets the userExperienceAnalyticsDeviceStartupProcesses property value. User experience analytics device Startup Processes
        Args:
            value: Value to set for the userExperienceAnalyticsDeviceStartupProcesses property.
        """
        self._user_experience_analytics_device_startup_processes = value
    
    @property
    def user_experience_analytics_device_startup_process_performance(self,) -> Optional[List[user_experience_analytics_device_startup_process_performance.UserExperienceAnalyticsDeviceStartupProcessPerformance]]:
        """
        Gets the userExperienceAnalyticsDeviceStartupProcessPerformance property value. User experience analytics device Startup Process Performance
        Returns: Optional[List[user_experience_analytics_device_startup_process_performance.UserExperienceAnalyticsDeviceStartupProcessPerformance]]
        """
        return self._user_experience_analytics_device_startup_process_performance
    
    @user_experience_analytics_device_startup_process_performance.setter
    def user_experience_analytics_device_startup_process_performance(self,value: Optional[List[user_experience_analytics_device_startup_process_performance.UserExperienceAnalyticsDeviceStartupProcessPerformance]] = None) -> None:
        """
        Sets the userExperienceAnalyticsDeviceStartupProcessPerformance property value. User experience analytics device Startup Process Performance
        Args:
            value: Value to set for the userExperienceAnalyticsDeviceStartupProcessPerformance property.
        """
        self._user_experience_analytics_device_startup_process_performance = value
    
    @property
    def user_experience_analytics_devices_without_cloud_identity(self,) -> Optional[List[user_experience_analytics_device_without_cloud_identity.UserExperienceAnalyticsDeviceWithoutCloudIdentity]]:
        """
        Gets the userExperienceAnalyticsDevicesWithoutCloudIdentity property value. User experience analytics devices without cloud identity.
        Returns: Optional[List[user_experience_analytics_device_without_cloud_identity.UserExperienceAnalyticsDeviceWithoutCloudIdentity]]
        """
        return self._user_experience_analytics_devices_without_cloud_identity
    
    @user_experience_analytics_devices_without_cloud_identity.setter
    def user_experience_analytics_devices_without_cloud_identity(self,value: Optional[List[user_experience_analytics_device_without_cloud_identity.UserExperienceAnalyticsDeviceWithoutCloudIdentity]] = None) -> None:
        """
        Sets the userExperienceAnalyticsDevicesWithoutCloudIdentity property value. User experience analytics devices without cloud identity.
        Args:
            value: Value to set for the userExperienceAnalyticsDevicesWithoutCloudIdentity property.
        """
        self._user_experience_analytics_devices_without_cloud_identity = value
    
    @property
    def user_experience_analytics_impacting_process(self,) -> Optional[List[user_experience_analytics_impacting_process.UserExperienceAnalyticsImpactingProcess]]:
        """
        Gets the userExperienceAnalyticsImpactingProcess property value. User experience analytics impacting process
        Returns: Optional[List[user_experience_analytics_impacting_process.UserExperienceAnalyticsImpactingProcess]]
        """
        return self._user_experience_analytics_impacting_process
    
    @user_experience_analytics_impacting_process.setter
    def user_experience_analytics_impacting_process(self,value: Optional[List[user_experience_analytics_impacting_process.UserExperienceAnalyticsImpactingProcess]] = None) -> None:
        """
        Sets the userExperienceAnalyticsImpactingProcess property value. User experience analytics impacting process
        Args:
            value: Value to set for the userExperienceAnalyticsImpactingProcess property.
        """
        self._user_experience_analytics_impacting_process = value
    
    @property
    def user_experience_analytics_metric_history(self,) -> Optional[List[user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory]]:
        """
        Gets the userExperienceAnalyticsMetricHistory property value. User experience analytics metric history
        Returns: Optional[List[user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory]]
        """
        return self._user_experience_analytics_metric_history
    
    @user_experience_analytics_metric_history.setter
    def user_experience_analytics_metric_history(self,value: Optional[List[user_experience_analytics_metric_history.UserExperienceAnalyticsMetricHistory]] = None) -> None:
        """
        Sets the userExperienceAnalyticsMetricHistory property value. User experience analytics metric history
        Args:
            value: Value to set for the userExperienceAnalyticsMetricHistory property.
        """
        self._user_experience_analytics_metric_history = value
    
    @property
    def user_experience_analytics_model_scores(self,) -> Optional[List[user_experience_analytics_model_scores.UserExperienceAnalyticsModelScores]]:
        """
        Gets the userExperienceAnalyticsModelScores property value. User experience analytics model scores
        Returns: Optional[List[user_experience_analytics_model_scores.UserExperienceAnalyticsModelScores]]
        """
        return self._user_experience_analytics_model_scores
    
    @user_experience_analytics_model_scores.setter
    def user_experience_analytics_model_scores(self,value: Optional[List[user_experience_analytics_model_scores.UserExperienceAnalyticsModelScores]] = None) -> None:
        """
        Sets the userExperienceAnalyticsModelScores property value. User experience analytics model scores
        Args:
            value: Value to set for the userExperienceAnalyticsModelScores property.
        """
        self._user_experience_analytics_model_scores = value
    
    @property
    def user_experience_analytics_not_autopilot_ready_device(self,) -> Optional[List[user_experience_analytics_not_autopilot_ready_device.UserExperienceAnalyticsNotAutopilotReadyDevice]]:
        """
        Gets the userExperienceAnalyticsNotAutopilotReadyDevice property value. User experience analytics devices not Windows Autopilot ready.
        Returns: Optional[List[user_experience_analytics_not_autopilot_ready_device.UserExperienceAnalyticsNotAutopilotReadyDevice]]
        """
        return self._user_experience_analytics_not_autopilot_ready_device
    
    @user_experience_analytics_not_autopilot_ready_device.setter
    def user_experience_analytics_not_autopilot_ready_device(self,value: Optional[List[user_experience_analytics_not_autopilot_ready_device.UserExperienceAnalyticsNotAutopilotReadyDevice]] = None) -> None:
        """
        Sets the userExperienceAnalyticsNotAutopilotReadyDevice property value. User experience analytics devices not Windows Autopilot ready.
        Args:
            value: Value to set for the userExperienceAnalyticsNotAutopilotReadyDevice property.
        """
        self._user_experience_analytics_not_autopilot_ready_device = value
    
    @property
    def user_experience_analytics_overview(self,) -> Optional[user_experience_analytics_overview.UserExperienceAnalyticsOverview]:
        """
        Gets the userExperienceAnalyticsOverview property value. User experience analytics overview
        Returns: Optional[user_experience_analytics_overview.UserExperienceAnalyticsOverview]
        """
        return self._user_experience_analytics_overview
    
    @user_experience_analytics_overview.setter
    def user_experience_analytics_overview(self,value: Optional[user_experience_analytics_overview.UserExperienceAnalyticsOverview] = None) -> None:
        """
        Sets the userExperienceAnalyticsOverview property value. User experience analytics overview
        Args:
            value: Value to set for the userExperienceAnalyticsOverview property.
        """
        self._user_experience_analytics_overview = value
    
    @property
    def user_experience_analytics_remote_connection(self,) -> Optional[List[user_experience_analytics_remote_connection.UserExperienceAnalyticsRemoteConnection]]:
        """
        Gets the userExperienceAnalyticsRemoteConnection property value. User experience analytics remote connection
        Returns: Optional[List[user_experience_analytics_remote_connection.UserExperienceAnalyticsRemoteConnection]]
        """
        return self._user_experience_analytics_remote_connection
    
    @user_experience_analytics_remote_connection.setter
    def user_experience_analytics_remote_connection(self,value: Optional[List[user_experience_analytics_remote_connection.UserExperienceAnalyticsRemoteConnection]] = None) -> None:
        """
        Sets the userExperienceAnalyticsRemoteConnection property value. User experience analytics remote connection
        Args:
            value: Value to set for the userExperienceAnalyticsRemoteConnection property.
        """
        self._user_experience_analytics_remote_connection = value
    
    @property
    def user_experience_analytics_resource_performance(self,) -> Optional[List[user_experience_analytics_resource_performance.UserExperienceAnalyticsResourcePerformance]]:
        """
        Gets the userExperienceAnalyticsResourcePerformance property value. User experience analytics resource performance
        Returns: Optional[List[user_experience_analytics_resource_performance.UserExperienceAnalyticsResourcePerformance]]
        """
        return self._user_experience_analytics_resource_performance
    
    @user_experience_analytics_resource_performance.setter
    def user_experience_analytics_resource_performance(self,value: Optional[List[user_experience_analytics_resource_performance.UserExperienceAnalyticsResourcePerformance]] = None) -> None:
        """
        Sets the userExperienceAnalyticsResourcePerformance property value. User experience analytics resource performance
        Args:
            value: Value to set for the userExperienceAnalyticsResourcePerformance property.
        """
        self._user_experience_analytics_resource_performance = value
    
    @property
    def user_experience_analytics_score_history(self,) -> Optional[List[user_experience_analytics_score_history.UserExperienceAnalyticsScoreHistory]]:
        """
        Gets the userExperienceAnalyticsScoreHistory property value. User experience analytics device Startup Score History
        Returns: Optional[List[user_experience_analytics_score_history.UserExperienceAnalyticsScoreHistory]]
        """
        return self._user_experience_analytics_score_history
    
    @user_experience_analytics_score_history.setter
    def user_experience_analytics_score_history(self,value: Optional[List[user_experience_analytics_score_history.UserExperienceAnalyticsScoreHistory]] = None) -> None:
        """
        Sets the userExperienceAnalyticsScoreHistory property value. User experience analytics device Startup Score History
        Args:
            value: Value to set for the userExperienceAnalyticsScoreHistory property.
        """
        self._user_experience_analytics_score_history = value
    
    @property
    def user_experience_analytics_settings(self,) -> Optional[user_experience_analytics_settings.UserExperienceAnalyticsSettings]:
        """
        Gets the userExperienceAnalyticsSettings property value. User experience analytics device settings
        Returns: Optional[user_experience_analytics_settings.UserExperienceAnalyticsSettings]
        """
        return self._user_experience_analytics_settings
    
    @user_experience_analytics_settings.setter
    def user_experience_analytics_settings(self,value: Optional[user_experience_analytics_settings.UserExperienceAnalyticsSettings] = None) -> None:
        """
        Sets the userExperienceAnalyticsSettings property value. User experience analytics device settings
        Args:
            value: Value to set for the userExperienceAnalyticsSettings property.
        """
        self._user_experience_analytics_settings = value
    
    @property
    def user_experience_analytics_work_from_anywhere_hardware_readiness_metric(self,) -> Optional[user_experience_analytics_work_from_anywhere_hardware_readiness_metric.UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric]:
        """
        Gets the userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric property value. User experience analytics work from anywhere hardware readiness metrics.
        Returns: Optional[user_experience_analytics_work_from_anywhere_hardware_readiness_metric.UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric]
        """
        return self._user_experience_analytics_work_from_anywhere_hardware_readiness_metric
    
    @user_experience_analytics_work_from_anywhere_hardware_readiness_metric.setter
    def user_experience_analytics_work_from_anywhere_hardware_readiness_metric(self,value: Optional[user_experience_analytics_work_from_anywhere_hardware_readiness_metric.UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric] = None) -> None:
        """
        Sets the userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric property value. User experience analytics work from anywhere hardware readiness metrics.
        Args:
            value: Value to set for the userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric property.
        """
        self._user_experience_analytics_work_from_anywhere_hardware_readiness_metric = value
    
    @property
    def user_experience_analytics_work_from_anywhere_metrics(self,) -> Optional[List[user_experience_analytics_work_from_anywhere_metric.UserExperienceAnalyticsWorkFromAnywhereMetric]]:
        """
        Gets the userExperienceAnalyticsWorkFromAnywhereMetrics property value. User experience analytics work from anywhere metrics.
        Returns: Optional[List[user_experience_analytics_work_from_anywhere_metric.UserExperienceAnalyticsWorkFromAnywhereMetric]]
        """
        return self._user_experience_analytics_work_from_anywhere_metrics
    
    @user_experience_analytics_work_from_anywhere_metrics.setter
    def user_experience_analytics_work_from_anywhere_metrics(self,value: Optional[List[user_experience_analytics_work_from_anywhere_metric.UserExperienceAnalyticsWorkFromAnywhereMetric]] = None) -> None:
        """
        Sets the userExperienceAnalyticsWorkFromAnywhereMetrics property value. User experience analytics work from anywhere metrics.
        Args:
            value: Value to set for the userExperienceAnalyticsWorkFromAnywhereMetrics property.
        """
        self._user_experience_analytics_work_from_anywhere_metrics = value
    
    @property
    def user_experience_analytics_work_from_anywhere_model_performance(self,) -> Optional[List[user_experience_analytics_work_from_anywhere_model_performance.UserExperienceAnalyticsWorkFromAnywhereModelPerformance]]:
        """
        Gets the userExperienceAnalyticsWorkFromAnywhereModelPerformance property value. The user experience analytics work from anywhere model performance
        Returns: Optional[List[user_experience_analytics_work_from_anywhere_model_performance.UserExperienceAnalyticsWorkFromAnywhereModelPerformance]]
        """
        return self._user_experience_analytics_work_from_anywhere_model_performance
    
    @user_experience_analytics_work_from_anywhere_model_performance.setter
    def user_experience_analytics_work_from_anywhere_model_performance(self,value: Optional[List[user_experience_analytics_work_from_anywhere_model_performance.UserExperienceAnalyticsWorkFromAnywhereModelPerformance]] = None) -> None:
        """
        Sets the userExperienceAnalyticsWorkFromAnywhereModelPerformance property value. The user experience analytics work from anywhere model performance
        Args:
            value: Value to set for the userExperienceAnalyticsWorkFromAnywhereModelPerformance property.
        """
        self._user_experience_analytics_work_from_anywhere_model_performance = value
    
    @property
    def user_pfx_certificates(self,) -> Optional[List[user_p_f_x_certificate.UserPFXCertificate]]:
        """
        Gets the userPfxCertificates property value. Collection of PFX certificates associated with a user.
        Returns: Optional[List[user_p_f_x_certificate.UserPFXCertificate]]
        """
        return self._user_pfx_certificates
    
    @user_pfx_certificates.setter
    def user_pfx_certificates(self,value: Optional[List[user_p_f_x_certificate.UserPFXCertificate]] = None) -> None:
        """
        Sets the userPfxCertificates property value. Collection of PFX certificates associated with a user.
        Args:
            value: Value to set for the userPfxCertificates property.
        """
        self._user_pfx_certificates = value
    
    @property
    def virtual_endpoint(self,) -> Optional[virtual_endpoint.VirtualEndpoint]:
        """
        Gets the virtualEndpoint property value. The virtualEndpoint property
        Returns: Optional[virtual_endpoint.VirtualEndpoint]
        """
        return self._virtual_endpoint
    
    @virtual_endpoint.setter
    def virtual_endpoint(self,value: Optional[virtual_endpoint.VirtualEndpoint] = None) -> None:
        """
        Sets the virtualEndpoint property value. The virtualEndpoint property
        Args:
            value: Value to set for the virtualEndpoint property.
        """
        self._virtual_endpoint = value
    
    @property
    def windows_autopilot_deployment_profiles(self,) -> Optional[List[windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile]]:
        """
        Gets the windowsAutopilotDeploymentProfiles property value. Windows auto pilot deployment profiles
        Returns: Optional[List[windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile]]
        """
        return self._windows_autopilot_deployment_profiles
    
    @windows_autopilot_deployment_profiles.setter
    def windows_autopilot_deployment_profiles(self,value: Optional[List[windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile]] = None) -> None:
        """
        Sets the windowsAutopilotDeploymentProfiles property value. Windows auto pilot deployment profiles
        Args:
            value: Value to set for the windowsAutopilotDeploymentProfiles property.
        """
        self._windows_autopilot_deployment_profiles = value
    
    @property
    def windows_autopilot_device_identities(self,) -> Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]]:
        """
        Gets the windowsAutopilotDeviceIdentities property value. The Windows autopilot device identities contained collection.
        Returns: Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]]
        """
        return self._windows_autopilot_device_identities
    
    @windows_autopilot_device_identities.setter
    def windows_autopilot_device_identities(self,value: Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]] = None) -> None:
        """
        Sets the windowsAutopilotDeviceIdentities property value. The Windows autopilot device identities contained collection.
        Args:
            value: Value to set for the windowsAutopilotDeviceIdentities property.
        """
        self._windows_autopilot_device_identities = value
    
    @property
    def windows_autopilot_settings(self,) -> Optional[windows_autopilot_settings.WindowsAutopilotSettings]:
        """
        Gets the windowsAutopilotSettings property value. The Windows autopilot account settings.
        Returns: Optional[windows_autopilot_settings.WindowsAutopilotSettings]
        """
        return self._windows_autopilot_settings
    
    @windows_autopilot_settings.setter
    def windows_autopilot_settings(self,value: Optional[windows_autopilot_settings.WindowsAutopilotSettings] = None) -> None:
        """
        Sets the windowsAutopilotSettings property value. The Windows autopilot account settings.
        Args:
            value: Value to set for the windowsAutopilotSettings property.
        """
        self._windows_autopilot_settings = value
    
    @property
    def windows_driver_update_profiles(self,) -> Optional[List[windows_driver_update_profile.WindowsDriverUpdateProfile]]:
        """
        Gets the windowsDriverUpdateProfiles property value. A collection of windows driver update profiles
        Returns: Optional[List[windows_driver_update_profile.WindowsDriverUpdateProfile]]
        """
        return self._windows_driver_update_profiles
    
    @windows_driver_update_profiles.setter
    def windows_driver_update_profiles(self,value: Optional[List[windows_driver_update_profile.WindowsDriverUpdateProfile]] = None) -> None:
        """
        Sets the windowsDriverUpdateProfiles property value. A collection of windows driver update profiles
        Args:
            value: Value to set for the windowsDriverUpdateProfiles property.
        """
        self._windows_driver_update_profiles = value
    
    @property
    def windows_feature_update_profiles(self,) -> Optional[List[windows_feature_update_profile.WindowsFeatureUpdateProfile]]:
        """
        Gets the windowsFeatureUpdateProfiles property value. A collection of windows feature update profiles
        Returns: Optional[List[windows_feature_update_profile.WindowsFeatureUpdateProfile]]
        """
        return self._windows_feature_update_profiles
    
    @windows_feature_update_profiles.setter
    def windows_feature_update_profiles(self,value: Optional[List[windows_feature_update_profile.WindowsFeatureUpdateProfile]] = None) -> None:
        """
        Sets the windowsFeatureUpdateProfiles property value. A collection of windows feature update profiles
        Args:
            value: Value to set for the windowsFeatureUpdateProfiles property.
        """
        self._windows_feature_update_profiles = value
    
    @property
    def windows_information_protection_app_learning_summaries(self,) -> Optional[List[windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary]]:
        """
        Gets the windowsInformationProtectionAppLearningSummaries property value. The windows information protection app learning summaries.
        Returns: Optional[List[windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary]]
        """
        return self._windows_information_protection_app_learning_summaries
    
    @windows_information_protection_app_learning_summaries.setter
    def windows_information_protection_app_learning_summaries(self,value: Optional[List[windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary]] = None) -> None:
        """
        Sets the windowsInformationProtectionAppLearningSummaries property value. The windows information protection app learning summaries.
        Args:
            value: Value to set for the windowsInformationProtectionAppLearningSummaries property.
        """
        self._windows_information_protection_app_learning_summaries = value
    
    @property
    def windows_information_protection_network_learning_summaries(self,) -> Optional[List[windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary]]:
        """
        Gets the windowsInformationProtectionNetworkLearningSummaries property value. The windows information protection network learning summaries.
        Returns: Optional[List[windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary]]
        """
        return self._windows_information_protection_network_learning_summaries
    
    @windows_information_protection_network_learning_summaries.setter
    def windows_information_protection_network_learning_summaries(self,value: Optional[List[windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary]] = None) -> None:
        """
        Sets the windowsInformationProtectionNetworkLearningSummaries property value. The windows information protection network learning summaries.
        Args:
            value: Value to set for the windowsInformationProtectionNetworkLearningSummaries property.
        """
        self._windows_information_protection_network_learning_summaries = value
    
    @property
    def windows_malware_information(self,) -> Optional[List[windows_malware_information.WindowsMalwareInformation]]:
        """
        Gets the windowsMalwareInformation property value. The list of affected malware in the tenant.
        Returns: Optional[List[windows_malware_information.WindowsMalwareInformation]]
        """
        return self._windows_malware_information
    
    @windows_malware_information.setter
    def windows_malware_information(self,value: Optional[List[windows_malware_information.WindowsMalwareInformation]] = None) -> None:
        """
        Sets the windowsMalwareInformation property value. The list of affected malware in the tenant.
        Args:
            value: Value to set for the windowsMalwareInformation property.
        """
        self._windows_malware_information = value
    
    @property
    def windows_malware_overview(self,) -> Optional[windows_malware_overview.WindowsMalwareOverview]:
        """
        Gets the windowsMalwareOverview property value. Malware overview for windows devices.
        Returns: Optional[windows_malware_overview.WindowsMalwareOverview]
        """
        return self._windows_malware_overview
    
    @windows_malware_overview.setter
    def windows_malware_overview(self,value: Optional[windows_malware_overview.WindowsMalwareOverview] = None) -> None:
        """
        Sets the windowsMalwareOverview property value. Malware overview for windows devices.
        Args:
            value: Value to set for the windowsMalwareOverview property.
        """
        self._windows_malware_overview = value
    
    @property
    def windows_quality_update_profiles(self,) -> Optional[List[windows_quality_update_profile.WindowsQualityUpdateProfile]]:
        """
        Gets the windowsQualityUpdateProfiles property value. A collection of windows quality update profiles
        Returns: Optional[List[windows_quality_update_profile.WindowsQualityUpdateProfile]]
        """
        return self._windows_quality_update_profiles
    
    @windows_quality_update_profiles.setter
    def windows_quality_update_profiles(self,value: Optional[List[windows_quality_update_profile.WindowsQualityUpdateProfile]] = None) -> None:
        """
        Sets the windowsQualityUpdateProfiles property value. A collection of windows quality update profiles
        Args:
            value: Value to set for the windowsQualityUpdateProfiles property.
        """
        self._windows_quality_update_profiles = value
    
    @property
    def windows_update_catalog_items(self,) -> Optional[List[windows_update_catalog_item.WindowsUpdateCatalogItem]]:
        """
        Gets the windowsUpdateCatalogItems property value. A collection of windows update catalog items (fetaure updates item , quality updates item)
        Returns: Optional[List[windows_update_catalog_item.WindowsUpdateCatalogItem]]
        """
        return self._windows_update_catalog_items
    
    @windows_update_catalog_items.setter
    def windows_update_catalog_items(self,value: Optional[List[windows_update_catalog_item.WindowsUpdateCatalogItem]] = None) -> None:
        """
        Sets the windowsUpdateCatalogItems property value. A collection of windows update catalog items (fetaure updates item , quality updates item)
        Args:
            value: Value to set for the windowsUpdateCatalogItems property.
        """
        self._windows_update_catalog_items = value
    
    @property
    def zebra_fota_artifacts(self,) -> Optional[List[zebra_fota_artifact.ZebraFotaArtifact]]:
        """
        Gets the zebraFotaArtifacts property value. The Collection of ZebraFotaArtifacts.
        Returns: Optional[List[zebra_fota_artifact.ZebraFotaArtifact]]
        """
        return self._zebra_fota_artifacts
    
    @zebra_fota_artifacts.setter
    def zebra_fota_artifacts(self,value: Optional[List[zebra_fota_artifact.ZebraFotaArtifact]] = None) -> None:
        """
        Sets the zebraFotaArtifacts property value. The Collection of ZebraFotaArtifacts.
        Args:
            value: Value to set for the zebraFotaArtifacts property.
        """
        self._zebra_fota_artifacts = value
    
    @property
    def zebra_fota_connector(self,) -> Optional[zebra_fota_connector.ZebraFotaConnector]:
        """
        Gets the zebraFotaConnector property value. The singleton ZebraFotaConnector associated with account.
        Returns: Optional[zebra_fota_connector.ZebraFotaConnector]
        """
        return self._zebra_fota_connector
    
    @zebra_fota_connector.setter
    def zebra_fota_connector(self,value: Optional[zebra_fota_connector.ZebraFotaConnector] = None) -> None:
        """
        Sets the zebraFotaConnector property value. The singleton ZebraFotaConnector associated with account.
        Args:
            value: Value to set for the zebraFotaConnector property.
        """
        self._zebra_fota_connector = value
    
    @property
    def zebra_fota_deployments(self,) -> Optional[List[zebra_fota_deployment.ZebraFotaDeployment]]:
        """
        Gets the zebraFotaDeployments property value. Collection of ZebraFotaDeployments associated with account.
        Returns: Optional[List[zebra_fota_deployment.ZebraFotaDeployment]]
        """
        return self._zebra_fota_deployments
    
    @zebra_fota_deployments.setter
    def zebra_fota_deployments(self,value: Optional[List[zebra_fota_deployment.ZebraFotaDeployment]] = None) -> None:
        """
        Sets the zebraFotaDeployments property value. Collection of ZebraFotaDeployments associated with account.
        Args:
            value: Value to set for the zebraFotaDeployments property.
        """
        self._zebra_fota_deployments = value
    

