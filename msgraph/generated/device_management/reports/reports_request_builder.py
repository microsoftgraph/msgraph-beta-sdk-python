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

cached_report_configurations_request_builder = lazy_import('msgraph.generated.device_management.reports.cached_report_configurations.cached_report_configurations_request_builder')
device_management_cached_report_configuration_item_request_builder = lazy_import('msgraph.generated.device_management.reports.cached_report_configurations.item.device_management_cached_report_configuration_item_request_builder')
export_jobs_request_builder = lazy_import('msgraph.generated.device_management.reports.export_jobs.export_jobs_request_builder')
device_management_export_job_item_request_builder = lazy_import('msgraph.generated.device_management.reports.export_jobs.item.device_management_export_job_item_request_builder')
get_active_malware_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_active_malware_report.get_active_malware_report_request_builder')
get_active_malware_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_active_malware_summary_report.get_active_malware_summary_report_request_builder')
get_all_certificates_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_all_certificates_report.get_all_certificates_report_request_builder')
get_apps_install_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_apps_install_summary_report.get_apps_install_summary_report_request_builder')
get_app_status_overview_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_app_status_overview_report.get_app_status_overview_report_request_builder')
get_cached_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_cached_report.get_cached_report_request_builder')
get_certificates_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_certificates_report.get_certificates_report_request_builder')
get_compliance_policies_report_for_device_request_builder = lazy_import('msgraph.generated.device_management.reports.get_compliance_policies_report_for_device.get_compliance_policies_report_for_device_request_builder')
get_compliance_policy_devices_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_compliance_policy_devices_report.get_compliance_policy_devices_report_request_builder')
get_compliance_policy_device_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_compliance_policy_device_summary_report.get_compliance_policy_device_summary_report_request_builder')
get_compliance_policy_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_compliance_policy_non_compliance_report.get_compliance_policy_non_compliance_report_request_builder')
get_compliance_policy_non_compliance_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_compliance_policy_non_compliance_summary_report.get_compliance_policy_non_compliance_summary_report_request_builder')
get_compliance_setting_details_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_compliance_setting_details_report.get_compliance_setting_details_report_request_builder')
get_compliance_setting_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_compliance_setting_non_compliance_report.get_compliance_setting_non_compliance_report_request_builder')
get_compliance_settings_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_compliance_settings_report.get_compliance_settings_report_request_builder')
get_config_manager_device_policy_status_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_config_manager_device_policy_status_report.get_config_manager_device_policy_status_report_request_builder')
get_configuration_policies_report_for_device_request_builder = lazy_import('msgraph.generated.device_management.reports.get_configuration_policies_report_for_device.get_configuration_policies_report_for_device_request_builder')
get_configuration_policy_devices_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_configuration_policy_devices_report.get_configuration_policy_devices_report_request_builder')
get_configuration_policy_device_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_configuration_policy_device_summary_report.get_configuration_policy_device_summary_report_request_builder')
get_configuration_policy_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_configuration_policy_non_compliance_report.get_configuration_policy_non_compliance_report_request_builder')
get_configuration_policy_non_compliance_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_configuration_policy_non_compliance_summary_report.get_configuration_policy_non_compliance_summary_report_request_builder')
get_configuration_policy_settings_device_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_configuration_policy_settings_device_summary_report.get_configuration_policy_settings_device_summary_report_request_builder')
get_configuration_setting_details_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_configuration_setting_details_report.get_configuration_setting_details_report_request_builder')
get_configuration_setting_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_configuration_setting_non_compliance_report.get_configuration_setting_non_compliance_report_request_builder')
get_configuration_settings_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_configuration_settings_report.get_configuration_settings_report_request_builder')
get_device_configuration_policy_settings_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_device_configuration_policy_settings_summary_report.get_device_configuration_policy_settings_summary_report_request_builder')
get_device_configuration_policy_status_summary_request_builder = lazy_import('msgraph.generated.device_management.reports.get_device_configuration_policy_status_summary.get_device_configuration_policy_status_summary_request_builder')
get_device_install_status_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_device_install_status_report.get_device_install_status_report_request_builder')
get_device_management_intent_per_setting_contributing_profiles_request_builder = lazy_import('msgraph.generated.device_management.reports.get_device_management_intent_per_setting_contributing_profiles.get_device_management_intent_per_setting_contributing_profiles_request_builder')
get_device_management_intent_settings_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_device_management_intent_settings_report.get_device_management_intent_settings_report_request_builder')
get_device_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_device_non_compliance_report.get_device_non_compliance_report_request_builder')
get_encryption_report_for_devices_request_builder = lazy_import('msgraph.generated.device_management.reports.get_encryption_report_for_devices.get_encryption_report_for_devices_request_builder')
get_enrollment_configuration_policies_by_device_request_builder = lazy_import('msgraph.generated.device_management.reports.get_enrollment_configuration_policies_by_device.get_enrollment_configuration_policies_by_device_request_builder')
get_failed_mobile_apps_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_failed_mobile_apps_report.get_failed_mobile_apps_report_request_builder')
get_failed_mobile_apps_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_failed_mobile_apps_summary_report.get_failed_mobile_apps_summary_report_request_builder')
get_group_policy_settings_device_settings_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_group_policy_settings_device_settings_report.get_group_policy_settings_device_settings_report_request_builder')
get_historical_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_historical_report.get_historical_report_request_builder')
get_malware_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_malware_summary_report.get_malware_summary_report_request_builder')
get_mobile_application_management_app_configuration_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_mobile_application_management_app_configuration_report.get_mobile_application_management_app_configuration_report_request_builder')
get_mobile_application_management_app_registration_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_mobile_application_management_app_registration_summary_report.get_mobile_application_management_app_registration_summary_report_request_builder')
get_noncompliant_devices_and_settings_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_noncompliant_devices_and_settings_report.get_noncompliant_devices_and_settings_report_request_builder')
get_policy_non_compliance_metadata_request_builder = lazy_import('msgraph.generated.device_management.reports.get_policy_non_compliance_metadata.get_policy_non_compliance_metadata_request_builder')
get_policy_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_policy_non_compliance_report.get_policy_non_compliance_report_request_builder')
get_policy_non_compliance_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_policy_non_compliance_summary_report.get_policy_non_compliance_summary_report_request_builder')
get_quiet_time_policy_users_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_quiet_time_policy_users_report.get_quiet_time_policy_users_report_request_builder')
get_quiet_time_policy_user_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_quiet_time_policy_user_summary_report.get_quiet_time_policy_user_summary_report_request_builder')
get_related_apps_status_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_related_apps_status_report.get_related_apps_status_report_request_builder')
get_remote_assistance_sessions_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_remote_assistance_sessions_report.get_remote_assistance_sessions_report_request_builder')
get_report_filters_request_builder = lazy_import('msgraph.generated.device_management.reports.get_report_filters.get_report_filters_request_builder')
get_setting_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_setting_non_compliance_report.get_setting_non_compliance_report_request_builder')
get_unhealthy_defender_agents_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_unhealthy_defender_agents_report.get_unhealthy_defender_agents_report_request_builder')
get_unhealthy_firewall_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_unhealthy_firewall_report.get_unhealthy_firewall_report_request_builder')
get_unhealthy_firewall_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_unhealthy_firewall_summary_report.get_unhealthy_firewall_summary_report_request_builder')
get_user_install_status_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_user_install_status_report.get_user_install_status_report_request_builder')
get_windows_quality_update_alerts_per_policy_per_device_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_windows_quality_update_alerts_per_policy_per_device_report.get_windows_quality_update_alerts_per_policy_per_device_report_request_builder')
get_windows_quality_update_alert_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_windows_quality_update_alert_summary_report.get_windows_quality_update_alert_summary_report_request_builder')
get_windows_update_alerts_per_policy_per_device_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_windows_update_alerts_per_policy_per_device_report.get_windows_update_alerts_per_policy_per_device_report_request_builder')
get_windows_update_alert_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_windows_update_alert_summary_report.get_windows_update_alert_summary_report_request_builder')
get_zebra_fota_deployment_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_zebra_fota_deployment_report.get_zebra_fota_deployment_report_request_builder')
device_management_reports = lazy_import('msgraph.generated.models.device_management_reports')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class ReportsRequestBuilder():
    """
    Provides operations to manage the reports property of the microsoft.graph.deviceManagement entity.
    """
    @property
    def cached_report_configurations(self) -> cached_report_configurations_request_builder.CachedReportConfigurationsRequestBuilder:
        """
        Provides operations to manage the cachedReportConfigurations property of the microsoft.graph.deviceManagementReports entity.
        """
        return cached_report_configurations_request_builder.CachedReportConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def export_jobs(self) -> export_jobs_request_builder.ExportJobsRequestBuilder:
        """
        Provides operations to manage the exportJobs property of the microsoft.graph.deviceManagementReports entity.
        """
        return export_jobs_request_builder.ExportJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_active_malware_report(self) -> get_active_malware_report_request_builder.GetActiveMalwareReportRequestBuilder:
        """
        Provides operations to call the getActiveMalwareReport method.
        """
        return get_active_malware_report_request_builder.GetActiveMalwareReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_active_malware_summary_report(self) -> get_active_malware_summary_report_request_builder.GetActiveMalwareSummaryReportRequestBuilder:
        """
        Provides operations to call the getActiveMalwareSummaryReport method.
        """
        return get_active_malware_summary_report_request_builder.GetActiveMalwareSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_all_certificates_report(self) -> get_all_certificates_report_request_builder.GetAllCertificatesReportRequestBuilder:
        """
        Provides operations to call the getAllCertificatesReport method.
        """
        return get_all_certificates_report_request_builder.GetAllCertificatesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_apps_install_summary_report(self) -> get_apps_install_summary_report_request_builder.GetAppsInstallSummaryReportRequestBuilder:
        """
        Provides operations to call the getAppsInstallSummaryReport method.
        """
        return get_apps_install_summary_report_request_builder.GetAppsInstallSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_app_status_overview_report(self) -> get_app_status_overview_report_request_builder.GetAppStatusOverviewReportRequestBuilder:
        """
        Provides operations to call the getAppStatusOverviewReport method.
        """
        return get_app_status_overview_report_request_builder.GetAppStatusOverviewReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_cached_report(self) -> get_cached_report_request_builder.GetCachedReportRequestBuilder:
        """
        Provides operations to call the getCachedReport method.
        """
        return get_cached_report_request_builder.GetCachedReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_certificates_report(self) -> get_certificates_report_request_builder.GetCertificatesReportRequestBuilder:
        """
        Provides operations to call the getCertificatesReport method.
        """
        return get_certificates_report_request_builder.GetCertificatesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policies_report_for_device(self) -> get_compliance_policies_report_for_device_request_builder.GetCompliancePoliciesReportForDeviceRequestBuilder:
        """
        Provides operations to call the getCompliancePoliciesReportForDevice method.
        """
        return get_compliance_policies_report_for_device_request_builder.GetCompliancePoliciesReportForDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_devices_report(self) -> get_compliance_policy_devices_report_request_builder.GetCompliancePolicyDevicesReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyDevicesReport method.
        """
        return get_compliance_policy_devices_report_request_builder.GetCompliancePolicyDevicesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_device_summary_report(self) -> get_compliance_policy_device_summary_report_request_builder.GetCompliancePolicyDeviceSummaryReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyDeviceSummaryReport method.
        """
        return get_compliance_policy_device_summary_report_request_builder.GetCompliancePolicyDeviceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_non_compliance_report(self) -> get_compliance_policy_non_compliance_report_request_builder.GetCompliancePolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceReport method.
        """
        return get_compliance_policy_non_compliance_report_request_builder.GetCompliancePolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_non_compliance_summary_report(self) -> get_compliance_policy_non_compliance_summary_report_request_builder.GetCompliancePolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceSummaryReport method.
        """
        return get_compliance_policy_non_compliance_summary_report_request_builder.GetCompliancePolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_setting_details_report(self) -> get_compliance_setting_details_report_request_builder.GetComplianceSettingDetailsReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingDetailsReport method.
        """
        return get_compliance_setting_details_report_request_builder.GetComplianceSettingDetailsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_setting_non_compliance_report(self) -> get_compliance_setting_non_compliance_report_request_builder.GetComplianceSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingNonComplianceReport method.
        """
        return get_compliance_setting_non_compliance_report_request_builder.GetComplianceSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_settings_report(self) -> get_compliance_settings_report_request_builder.GetComplianceSettingsReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingsReport method.
        """
        return get_compliance_settings_report_request_builder.GetComplianceSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_config_manager_device_policy_status_report(self) -> get_config_manager_device_policy_status_report_request_builder.GetConfigManagerDevicePolicyStatusReportRequestBuilder:
        """
        Provides operations to call the getConfigManagerDevicePolicyStatusReport method.
        """
        return get_config_manager_device_policy_status_report_request_builder.GetConfigManagerDevicePolicyStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policies_report_for_device(self) -> get_configuration_policies_report_for_device_request_builder.GetConfigurationPoliciesReportForDeviceRequestBuilder:
        """
        Provides operations to call the getConfigurationPoliciesReportForDevice method.
        """
        return get_configuration_policies_report_for_device_request_builder.GetConfigurationPoliciesReportForDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_devices_report(self) -> get_configuration_policy_devices_report_request_builder.GetConfigurationPolicyDevicesReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyDevicesReport method.
        """
        return get_configuration_policy_devices_report_request_builder.GetConfigurationPolicyDevicesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_device_summary_report(self) -> get_configuration_policy_device_summary_report_request_builder.GetConfigurationPolicyDeviceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyDeviceSummaryReport method.
        """
        return get_configuration_policy_device_summary_report_request_builder.GetConfigurationPolicyDeviceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_non_compliance_report(self) -> get_configuration_policy_non_compliance_report_request_builder.GetConfigurationPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceReport method.
        """
        return get_configuration_policy_non_compliance_report_request_builder.GetConfigurationPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_non_compliance_summary_report(self) -> get_configuration_policy_non_compliance_summary_report_request_builder.GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceSummaryReport method.
        """
        return get_configuration_policy_non_compliance_summary_report_request_builder.GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_settings_device_summary_report(self) -> get_configuration_policy_settings_device_summary_report_request_builder.GetConfigurationPolicySettingsDeviceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicySettingsDeviceSummaryReport method.
        """
        return get_configuration_policy_settings_device_summary_report_request_builder.GetConfigurationPolicySettingsDeviceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_setting_details_report(self) -> get_configuration_setting_details_report_request_builder.GetConfigurationSettingDetailsReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingDetailsReport method.
        """
        return get_configuration_setting_details_report_request_builder.GetConfigurationSettingDetailsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_setting_non_compliance_report(self) -> get_configuration_setting_non_compliance_report_request_builder.GetConfigurationSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingNonComplianceReport method.
        """
        return get_configuration_setting_non_compliance_report_request_builder.GetConfigurationSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_settings_report(self) -> get_configuration_settings_report_request_builder.GetConfigurationSettingsReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingsReport method.
        """
        return get_configuration_settings_report_request_builder.GetConfigurationSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_configuration_policy_settings_summary_report(self) -> get_device_configuration_policy_settings_summary_report_request_builder.GetDeviceConfigurationPolicySettingsSummaryReportRequestBuilder:
        """
        Provides operations to call the getDeviceConfigurationPolicySettingsSummaryReport method.
        """
        return get_device_configuration_policy_settings_summary_report_request_builder.GetDeviceConfigurationPolicySettingsSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_configuration_policy_status_summary(self) -> get_device_configuration_policy_status_summary_request_builder.GetDeviceConfigurationPolicyStatusSummaryRequestBuilder:
        """
        Provides operations to call the getDeviceConfigurationPolicyStatusSummary method.
        """
        return get_device_configuration_policy_status_summary_request_builder.GetDeviceConfigurationPolicyStatusSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_install_status_report(self) -> get_device_install_status_report_request_builder.GetDeviceInstallStatusReportRequestBuilder:
        """
        Provides operations to call the getDeviceInstallStatusReport method.
        """
        return get_device_install_status_report_request_builder.GetDeviceInstallStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_management_intent_per_setting_contributing_profiles(self) -> get_device_management_intent_per_setting_contributing_profiles_request_builder.GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentPerSettingContributingProfiles method.
        """
        return get_device_management_intent_per_setting_contributing_profiles_request_builder.GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_management_intent_settings_report(self) -> get_device_management_intent_settings_report_request_builder.GetDeviceManagementIntentSettingsReportRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentSettingsReport method.
        """
        return get_device_management_intent_settings_report_request_builder.GetDeviceManagementIntentSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_non_compliance_report(self) -> get_device_non_compliance_report_request_builder.GetDeviceNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getDeviceNonComplianceReport method.
        """
        return get_device_non_compliance_report_request_builder.GetDeviceNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_encryption_report_for_devices(self) -> get_encryption_report_for_devices_request_builder.GetEncryptionReportForDevicesRequestBuilder:
        """
        Provides operations to call the getEncryptionReportForDevices method.
        """
        return get_encryption_report_for_devices_request_builder.GetEncryptionReportForDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_enrollment_configuration_policies_by_device(self) -> get_enrollment_configuration_policies_by_device_request_builder.GetEnrollmentConfigurationPoliciesByDeviceRequestBuilder:
        """
        Provides operations to call the getEnrollmentConfigurationPoliciesByDevice method.
        """
        return get_enrollment_configuration_policies_by_device_request_builder.GetEnrollmentConfigurationPoliciesByDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_failed_mobile_apps_report(self) -> get_failed_mobile_apps_report_request_builder.GetFailedMobileAppsReportRequestBuilder:
        """
        Provides operations to call the getFailedMobileAppsReport method.
        """
        return get_failed_mobile_apps_report_request_builder.GetFailedMobileAppsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_failed_mobile_apps_summary_report(self) -> get_failed_mobile_apps_summary_report_request_builder.GetFailedMobileAppsSummaryReportRequestBuilder:
        """
        Provides operations to call the getFailedMobileAppsSummaryReport method.
        """
        return get_failed_mobile_apps_summary_report_request_builder.GetFailedMobileAppsSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_group_policy_settings_device_settings_report(self) -> get_group_policy_settings_device_settings_report_request_builder.GetGroupPolicySettingsDeviceSettingsReportRequestBuilder:
        """
        Provides operations to call the getGroupPolicySettingsDeviceSettingsReport method.
        """
        return get_group_policy_settings_device_settings_report_request_builder.GetGroupPolicySettingsDeviceSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_historical_report(self) -> get_historical_report_request_builder.GetHistoricalReportRequestBuilder:
        """
        Provides operations to call the getHistoricalReport method.
        """
        return get_historical_report_request_builder.GetHistoricalReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_malware_summary_report(self) -> get_malware_summary_report_request_builder.GetMalwareSummaryReportRequestBuilder:
        """
        Provides operations to call the getMalwareSummaryReport method.
        """
        return get_malware_summary_report_request_builder.GetMalwareSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_mobile_application_management_app_configuration_report(self) -> get_mobile_application_management_app_configuration_report_request_builder.GetMobileApplicationManagementAppConfigurationReportRequestBuilder:
        """
        Provides operations to call the getMobileApplicationManagementAppConfigurationReport method.
        """
        return get_mobile_application_management_app_configuration_report_request_builder.GetMobileApplicationManagementAppConfigurationReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_mobile_application_management_app_registration_summary_report(self) -> get_mobile_application_management_app_registration_summary_report_request_builder.GetMobileApplicationManagementAppRegistrationSummaryReportRequestBuilder:
        """
        Provides operations to call the getMobileApplicationManagementAppRegistrationSummaryReport method.
        """
        return get_mobile_application_management_app_registration_summary_report_request_builder.GetMobileApplicationManagementAppRegistrationSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_noncompliant_devices_and_settings_report(self) -> get_noncompliant_devices_and_settings_report_request_builder.GetNoncompliantDevicesAndSettingsReportRequestBuilder:
        """
        Provides operations to call the getNoncompliantDevicesAndSettingsReport method.
        """
        return get_noncompliant_devices_and_settings_report_request_builder.GetNoncompliantDevicesAndSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_metadata(self) -> get_policy_non_compliance_metadata_request_builder.GetPolicyNonComplianceMetadataRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceMetadata method.
        """
        return get_policy_non_compliance_metadata_request_builder.GetPolicyNonComplianceMetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_report(self) -> get_policy_non_compliance_report_request_builder.GetPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceReport method.
        """
        return get_policy_non_compliance_report_request_builder.GetPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_summary_report(self) -> get_policy_non_compliance_summary_report_request_builder.GetPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceSummaryReport method.
        """
        return get_policy_non_compliance_summary_report_request_builder.GetPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_quiet_time_policy_users_report(self) -> get_quiet_time_policy_users_report_request_builder.GetQuietTimePolicyUsersReportRequestBuilder:
        """
        Provides operations to call the getQuietTimePolicyUsersReport method.
        """
        return get_quiet_time_policy_users_report_request_builder.GetQuietTimePolicyUsersReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_quiet_time_policy_user_summary_report(self) -> get_quiet_time_policy_user_summary_report_request_builder.GetQuietTimePolicyUserSummaryReportRequestBuilder:
        """
        Provides operations to call the getQuietTimePolicyUserSummaryReport method.
        """
        return get_quiet_time_policy_user_summary_report_request_builder.GetQuietTimePolicyUserSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_related_apps_status_report(self) -> get_related_apps_status_report_request_builder.GetRelatedAppsStatusReportRequestBuilder:
        """
        Provides operations to call the getRelatedAppsStatusReport method.
        """
        return get_related_apps_status_report_request_builder.GetRelatedAppsStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_remote_assistance_sessions_report(self) -> get_remote_assistance_sessions_report_request_builder.GetRemoteAssistanceSessionsReportRequestBuilder:
        """
        Provides operations to call the getRemoteAssistanceSessionsReport method.
        """
        return get_remote_assistance_sessions_report_request_builder.GetRemoteAssistanceSessionsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_report_filters(self) -> get_report_filters_request_builder.GetReportFiltersRequestBuilder:
        """
        Provides operations to call the getReportFilters method.
        """
        return get_report_filters_request_builder.GetReportFiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_setting_non_compliance_report(self) -> get_setting_non_compliance_report_request_builder.GetSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getSettingNonComplianceReport method.
        """
        return get_setting_non_compliance_report_request_builder.GetSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_unhealthy_defender_agents_report(self) -> get_unhealthy_defender_agents_report_request_builder.GetUnhealthyDefenderAgentsReportRequestBuilder:
        """
        Provides operations to call the getUnhealthyDefenderAgentsReport method.
        """
        return get_unhealthy_defender_agents_report_request_builder.GetUnhealthyDefenderAgentsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_unhealthy_firewall_report(self) -> get_unhealthy_firewall_report_request_builder.GetUnhealthyFirewallReportRequestBuilder:
        """
        Provides operations to call the getUnhealthyFirewallReport method.
        """
        return get_unhealthy_firewall_report_request_builder.GetUnhealthyFirewallReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_unhealthy_firewall_summary_report(self) -> get_unhealthy_firewall_summary_report_request_builder.GetUnhealthyFirewallSummaryReportRequestBuilder:
        """
        Provides operations to call the getUnhealthyFirewallSummaryReport method.
        """
        return get_unhealthy_firewall_summary_report_request_builder.GetUnhealthyFirewallSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_user_install_status_report(self) -> get_user_install_status_report_request_builder.GetUserInstallStatusReportRequestBuilder:
        """
        Provides operations to call the getUserInstallStatusReport method.
        """
        return get_user_install_status_report_request_builder.GetUserInstallStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_quality_update_alerts_per_policy_per_device_report(self) -> get_windows_quality_update_alerts_per_policy_per_device_report_request_builder.GetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequestBuilder:
        """
        Provides operations to call the getWindowsQualityUpdateAlertsPerPolicyPerDeviceReport method.
        """
        return get_windows_quality_update_alerts_per_policy_per_device_report_request_builder.GetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_quality_update_alert_summary_report(self) -> get_windows_quality_update_alert_summary_report_request_builder.GetWindowsQualityUpdateAlertSummaryReportRequestBuilder:
        """
        Provides operations to call the getWindowsQualityUpdateAlertSummaryReport method.
        """
        return get_windows_quality_update_alert_summary_report_request_builder.GetWindowsQualityUpdateAlertSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_update_alerts_per_policy_per_device_report(self) -> get_windows_update_alerts_per_policy_per_device_report_request_builder.GetWindowsUpdateAlertsPerPolicyPerDeviceReportRequestBuilder:
        """
        Provides operations to call the getWindowsUpdateAlertsPerPolicyPerDeviceReport method.
        """
        return get_windows_update_alerts_per_policy_per_device_report_request_builder.GetWindowsUpdateAlertsPerPolicyPerDeviceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_update_alert_summary_report(self) -> get_windows_update_alert_summary_report_request_builder.GetWindowsUpdateAlertSummaryReportRequestBuilder:
        """
        Provides operations to call the getWindowsUpdateAlertSummaryReport method.
        """
        return get_windows_update_alert_summary_report_request_builder.GetWindowsUpdateAlertSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_zebra_fota_deployment_report(self) -> get_zebra_fota_deployment_report_request_builder.GetZebraFotaDeploymentReportRequestBuilder:
        """
        Provides operations to call the getZebraFotaDeploymentReport method.
        """
        return get_zebra_fota_deployment_report_request_builder.GetZebraFotaDeploymentReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def cached_report_configurations_by_id(self,id: str) -> device_management_cached_report_configuration_item_request_builder.DeviceManagementCachedReportConfigurationItemRequestBuilder:
        """
        Provides operations to manage the cachedReportConfigurations property of the microsoft.graph.deviceManagementReports entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_cached_report_configuration_item_request_builder.DeviceManagementCachedReportConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementCachedReportConfiguration%2Did"] = id
        return device_management_cached_report_configuration_item_request_builder.DeviceManagementCachedReportConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ReportsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/reports{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property reports for deviceManagement
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
    
    def create_get_request_information(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Reports singleton
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
    
    def create_patch_request_information(self,body: Optional[device_management_reports.DeviceManagementReports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property reports in deviceManagement
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
    
    async def delete(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property reports for deviceManagement
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
    
    def export_jobs_by_id(self,id: str) -> device_management_export_job_item_request_builder.DeviceManagementExportJobItemRequestBuilder:
        """
        Provides operations to manage the exportJobs property of the microsoft.graph.deviceManagementReports entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_export_job_item_request_builder.DeviceManagementExportJobItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementExportJob%2Did"] = id
        return device_management_export_job_item_request_builder.DeviceManagementExportJobItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_management_reports.DeviceManagementReports]:
        """
        Reports singleton
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_management_reports.DeviceManagementReports]
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
        return await self.request_adapter.send_async(request_info, device_management_reports.DeviceManagementReports, response_handler, error_mapping)
    
    async def patch(self,body: Optional[device_management_reports.DeviceManagementReports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_management_reports.DeviceManagementReports]:
        """
        Update the navigation property reports in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_management_reports.DeviceManagementReports]
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
        return await self.request_adapter.send_async(request_info, device_management_reports.DeviceManagementReports, response_handler, error_mapping)
    
    @dataclass
    class ReportsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Reports singleton
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
    class ReportsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ReportsRequestBuilder.ReportsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ReportsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

