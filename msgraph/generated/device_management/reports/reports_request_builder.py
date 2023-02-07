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
microsoft_graph_get_active_malware_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_active_malware_report.microsoft_graph_get_active_malware_report_request_builder')
microsoft_graph_get_active_malware_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_active_malware_summary_report.microsoft_graph_get_active_malware_summary_report_request_builder')
microsoft_graph_get_all_certificates_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_all_certificates_report.microsoft_graph_get_all_certificates_report_request_builder')
microsoft_graph_get_apps_install_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_apps_install_summary_report.microsoft_graph_get_apps_install_summary_report_request_builder')
microsoft_graph_get_app_status_overview_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_app_status_overview_report.microsoft_graph_get_app_status_overview_report_request_builder')
microsoft_graph_get_cached_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_cached_report.microsoft_graph_get_cached_report_request_builder')
microsoft_graph_get_certificates_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_certificates_report.microsoft_graph_get_certificates_report_request_builder')
microsoft_graph_get_compliance_policies_report_for_device_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_compliance_policies_report_for_device.microsoft_graph_get_compliance_policies_report_for_device_request_builder')
microsoft_graph_get_compliance_policy_devices_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_compliance_policy_devices_report.microsoft_graph_get_compliance_policy_devices_report_request_builder')
microsoft_graph_get_compliance_policy_device_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_compliance_policy_device_summary_report.microsoft_graph_get_compliance_policy_device_summary_report_request_builder')
microsoft_graph_get_compliance_policy_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_compliance_policy_non_compliance_report.microsoft_graph_get_compliance_policy_non_compliance_report_request_builder')
microsoft_graph_get_compliance_policy_non_compliance_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_compliance_policy_non_compliance_summary_report.microsoft_graph_get_compliance_policy_non_compliance_summary_report_request_builder')
microsoft_graph_get_compliance_setting_details_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_compliance_setting_details_report.microsoft_graph_get_compliance_setting_details_report_request_builder')
microsoft_graph_get_compliance_setting_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_compliance_setting_non_compliance_report.microsoft_graph_get_compliance_setting_non_compliance_report_request_builder')
microsoft_graph_get_compliance_settings_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_compliance_settings_report.microsoft_graph_get_compliance_settings_report_request_builder')
microsoft_graph_get_config_manager_device_policy_status_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_config_manager_device_policy_status_report.microsoft_graph_get_config_manager_device_policy_status_report_request_builder')
microsoft_graph_get_configuration_policies_report_for_device_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_configuration_policies_report_for_device.microsoft_graph_get_configuration_policies_report_for_device_request_builder')
microsoft_graph_get_configuration_policy_devices_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_configuration_policy_devices_report.microsoft_graph_get_configuration_policy_devices_report_request_builder')
microsoft_graph_get_configuration_policy_device_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_configuration_policy_device_summary_report.microsoft_graph_get_configuration_policy_device_summary_report_request_builder')
microsoft_graph_get_configuration_policy_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_configuration_policy_non_compliance_report.microsoft_graph_get_configuration_policy_non_compliance_report_request_builder')
microsoft_graph_get_configuration_policy_non_compliance_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_configuration_policy_non_compliance_summary_report.microsoft_graph_get_configuration_policy_non_compliance_summary_report_request_builder')
microsoft_graph_get_configuration_policy_settings_device_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_configuration_policy_settings_device_summary_report.microsoft_graph_get_configuration_policy_settings_device_summary_report_request_builder')
microsoft_graph_get_configuration_setting_details_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_configuration_setting_details_report.microsoft_graph_get_configuration_setting_details_report_request_builder')
microsoft_graph_get_configuration_setting_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_configuration_setting_non_compliance_report.microsoft_graph_get_configuration_setting_non_compliance_report_request_builder')
microsoft_graph_get_configuration_settings_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_configuration_settings_report.microsoft_graph_get_configuration_settings_report_request_builder')
microsoft_graph_get_device_configuration_policy_settings_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_device_configuration_policy_settings_summary_report.microsoft_graph_get_device_configuration_policy_settings_summary_report_request_builder')
microsoft_graph_get_device_configuration_policy_status_summary_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_device_configuration_policy_status_summary.microsoft_graph_get_device_configuration_policy_status_summary_request_builder')
microsoft_graph_get_device_install_status_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_device_install_status_report.microsoft_graph_get_device_install_status_report_request_builder')
microsoft_graph_get_device_management_intent_per_setting_contributing_profiles_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_device_management_intent_per_setting_contributing_profiles.microsoft_graph_get_device_management_intent_per_setting_contributing_profiles_request_builder')
microsoft_graph_get_device_management_intent_settings_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_device_management_intent_settings_report.microsoft_graph_get_device_management_intent_settings_report_request_builder')
microsoft_graph_get_device_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_device_non_compliance_report.microsoft_graph_get_device_non_compliance_report_request_builder')
microsoft_graph_get_devices_without_compliance_policy_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_devices_without_compliance_policy_report.microsoft_graph_get_devices_without_compliance_policy_report_request_builder')
microsoft_graph_get_encryption_report_for_devices_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_encryption_report_for_devices.microsoft_graph_get_encryption_report_for_devices_request_builder')
microsoft_graph_get_enrollment_configuration_policies_by_device_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_enrollment_configuration_policies_by_device.microsoft_graph_get_enrollment_configuration_policies_by_device_request_builder')
microsoft_graph_get_failed_mobile_apps_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_failed_mobile_apps_report.microsoft_graph_get_failed_mobile_apps_report_request_builder')
microsoft_graph_get_failed_mobile_apps_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_failed_mobile_apps_summary_report.microsoft_graph_get_failed_mobile_apps_summary_report_request_builder')
microsoft_graph_get_group_policy_settings_device_settings_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_group_policy_settings_device_settings_report.microsoft_graph_get_group_policy_settings_device_settings_report_request_builder')
microsoft_graph_get_historical_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_historical_report.microsoft_graph_get_historical_report_request_builder')
microsoft_graph_get_malware_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_malware_summary_report.microsoft_graph_get_malware_summary_report_request_builder')
microsoft_graph_get_mobile_application_management_app_configuration_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_mobile_application_management_app_configuration_report.microsoft_graph_get_mobile_application_management_app_configuration_report_request_builder')
microsoft_graph_get_mobile_application_management_app_registration_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_mobile_application_management_app_registration_summary_report.microsoft_graph_get_mobile_application_management_app_registration_summary_report_request_builder')
microsoft_graph_get_noncompliant_devices_and_settings_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_noncompliant_devices_and_settings_report.microsoft_graph_get_noncompliant_devices_and_settings_report_request_builder')
microsoft_graph_get_policy_non_compliance_metadata_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_policy_non_compliance_metadata.microsoft_graph_get_policy_non_compliance_metadata_request_builder')
microsoft_graph_get_policy_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_policy_non_compliance_report.microsoft_graph_get_policy_non_compliance_report_request_builder')
microsoft_graph_get_policy_non_compliance_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_policy_non_compliance_summary_report.microsoft_graph_get_policy_non_compliance_summary_report_request_builder')
microsoft_graph_get_quiet_time_policy_users_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_quiet_time_policy_users_report.microsoft_graph_get_quiet_time_policy_users_report_request_builder')
microsoft_graph_get_quiet_time_policy_user_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_quiet_time_policy_user_summary_report.microsoft_graph_get_quiet_time_policy_user_summary_report_request_builder')
microsoft_graph_get_related_apps_status_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_related_apps_status_report.microsoft_graph_get_related_apps_status_report_request_builder')
microsoft_graph_get_remote_assistance_sessions_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_remote_assistance_sessions_report.microsoft_graph_get_remote_assistance_sessions_report_request_builder')
microsoft_graph_get_report_filters_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_report_filters.microsoft_graph_get_report_filters_request_builder')
microsoft_graph_get_setting_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_setting_non_compliance_report.microsoft_graph_get_setting_non_compliance_report_request_builder')
microsoft_graph_get_unhealthy_defender_agents_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_unhealthy_defender_agents_report.microsoft_graph_get_unhealthy_defender_agents_report_request_builder')
microsoft_graph_get_unhealthy_firewall_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_unhealthy_firewall_report.microsoft_graph_get_unhealthy_firewall_report_request_builder')
microsoft_graph_get_unhealthy_firewall_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_unhealthy_firewall_summary_report.microsoft_graph_get_unhealthy_firewall_summary_report_request_builder')
microsoft_graph_get_user_install_status_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_user_install_status_report.microsoft_graph_get_user_install_status_report_request_builder')
microsoft_graph_get_windows_quality_update_alerts_per_policy_per_device_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_windows_quality_update_alerts_per_policy_per_device_report.microsoft_graph_get_windows_quality_update_alerts_per_policy_per_device_report_request_builder')
microsoft_graph_get_windows_quality_update_alert_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_windows_quality_update_alert_summary_report.microsoft_graph_get_windows_quality_update_alert_summary_report_request_builder')
microsoft_graph_get_windows_update_alerts_per_policy_per_device_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_windows_update_alerts_per_policy_per_device_report.microsoft_graph_get_windows_update_alerts_per_policy_per_device_report_request_builder')
microsoft_graph_get_windows_update_alert_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_windows_update_alert_summary_report.microsoft_graph_get_windows_update_alert_summary_report_request_builder')
microsoft_graph_get_zebra_fota_deployment_report_request_builder = lazy_import('msgraph.generated.device_management.reports.microsoft_graph_get_zebra_fota_deployment_report.microsoft_graph_get_zebra_fota_deployment_report_request_builder')
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
    def microsoft_graph_get_active_malware_report(self) -> microsoft_graph_get_active_malware_report_request_builder.MicrosoftGraphGetActiveMalwareReportRequestBuilder:
        """
        Provides operations to call the getActiveMalwareReport method.
        """
        return microsoft_graph_get_active_malware_report_request_builder.MicrosoftGraphGetActiveMalwareReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_active_malware_summary_report(self) -> microsoft_graph_get_active_malware_summary_report_request_builder.MicrosoftGraphGetActiveMalwareSummaryReportRequestBuilder:
        """
        Provides operations to call the getActiveMalwareSummaryReport method.
        """
        return microsoft_graph_get_active_malware_summary_report_request_builder.MicrosoftGraphGetActiveMalwareSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_all_certificates_report(self) -> microsoft_graph_get_all_certificates_report_request_builder.MicrosoftGraphGetAllCertificatesReportRequestBuilder:
        """
        Provides operations to call the getAllCertificatesReport method.
        """
        return microsoft_graph_get_all_certificates_report_request_builder.MicrosoftGraphGetAllCertificatesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_apps_install_summary_report(self) -> microsoft_graph_get_apps_install_summary_report_request_builder.MicrosoftGraphGetAppsInstallSummaryReportRequestBuilder:
        """
        Provides operations to call the getAppsInstallSummaryReport method.
        """
        return microsoft_graph_get_apps_install_summary_report_request_builder.MicrosoftGraphGetAppsInstallSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_app_status_overview_report(self) -> microsoft_graph_get_app_status_overview_report_request_builder.MicrosoftGraphGetAppStatusOverviewReportRequestBuilder:
        """
        Provides operations to call the getAppStatusOverviewReport method.
        """
        return microsoft_graph_get_app_status_overview_report_request_builder.MicrosoftGraphGetAppStatusOverviewReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_cached_report(self) -> microsoft_graph_get_cached_report_request_builder.MicrosoftGraphGetCachedReportRequestBuilder:
        """
        Provides operations to call the getCachedReport method.
        """
        return microsoft_graph_get_cached_report_request_builder.MicrosoftGraphGetCachedReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_certificates_report(self) -> microsoft_graph_get_certificates_report_request_builder.MicrosoftGraphGetCertificatesReportRequestBuilder:
        """
        Provides operations to call the getCertificatesReport method.
        """
        return microsoft_graph_get_certificates_report_request_builder.MicrosoftGraphGetCertificatesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_compliance_policies_report_for_device(self) -> microsoft_graph_get_compliance_policies_report_for_device_request_builder.MicrosoftGraphGetCompliancePoliciesReportForDeviceRequestBuilder:
        """
        Provides operations to call the getCompliancePoliciesReportForDevice method.
        """
        return microsoft_graph_get_compliance_policies_report_for_device_request_builder.MicrosoftGraphGetCompliancePoliciesReportForDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_compliance_policy_devices_report(self) -> microsoft_graph_get_compliance_policy_devices_report_request_builder.MicrosoftGraphGetCompliancePolicyDevicesReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyDevicesReport method.
        """
        return microsoft_graph_get_compliance_policy_devices_report_request_builder.MicrosoftGraphGetCompliancePolicyDevicesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_compliance_policy_device_summary_report(self) -> microsoft_graph_get_compliance_policy_device_summary_report_request_builder.MicrosoftGraphGetCompliancePolicyDeviceSummaryReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyDeviceSummaryReport method.
        """
        return microsoft_graph_get_compliance_policy_device_summary_report_request_builder.MicrosoftGraphGetCompliancePolicyDeviceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_compliance_policy_non_compliance_report(self) -> microsoft_graph_get_compliance_policy_non_compliance_report_request_builder.MicrosoftGraphGetCompliancePolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceReport method.
        """
        return microsoft_graph_get_compliance_policy_non_compliance_report_request_builder.MicrosoftGraphGetCompliancePolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_compliance_policy_non_compliance_summary_report(self) -> microsoft_graph_get_compliance_policy_non_compliance_summary_report_request_builder.MicrosoftGraphGetCompliancePolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceSummaryReport method.
        """
        return microsoft_graph_get_compliance_policy_non_compliance_summary_report_request_builder.MicrosoftGraphGetCompliancePolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_compliance_setting_details_report(self) -> microsoft_graph_get_compliance_setting_details_report_request_builder.MicrosoftGraphGetComplianceSettingDetailsReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingDetailsReport method.
        """
        return microsoft_graph_get_compliance_setting_details_report_request_builder.MicrosoftGraphGetComplianceSettingDetailsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_compliance_setting_non_compliance_report(self) -> microsoft_graph_get_compliance_setting_non_compliance_report_request_builder.MicrosoftGraphGetComplianceSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingNonComplianceReport method.
        """
        return microsoft_graph_get_compliance_setting_non_compliance_report_request_builder.MicrosoftGraphGetComplianceSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_compliance_settings_report(self) -> microsoft_graph_get_compliance_settings_report_request_builder.MicrosoftGraphGetComplianceSettingsReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingsReport method.
        """
        return microsoft_graph_get_compliance_settings_report_request_builder.MicrosoftGraphGetComplianceSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_config_manager_device_policy_status_report(self) -> microsoft_graph_get_config_manager_device_policy_status_report_request_builder.MicrosoftGraphGetConfigManagerDevicePolicyStatusReportRequestBuilder:
        """
        Provides operations to call the getConfigManagerDevicePolicyStatusReport method.
        """
        return microsoft_graph_get_config_manager_device_policy_status_report_request_builder.MicrosoftGraphGetConfigManagerDevicePolicyStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_configuration_policies_report_for_device(self) -> microsoft_graph_get_configuration_policies_report_for_device_request_builder.MicrosoftGraphGetConfigurationPoliciesReportForDeviceRequestBuilder:
        """
        Provides operations to call the getConfigurationPoliciesReportForDevice method.
        """
        return microsoft_graph_get_configuration_policies_report_for_device_request_builder.MicrosoftGraphGetConfigurationPoliciesReportForDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_configuration_policy_devices_report(self) -> microsoft_graph_get_configuration_policy_devices_report_request_builder.MicrosoftGraphGetConfigurationPolicyDevicesReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyDevicesReport method.
        """
        return microsoft_graph_get_configuration_policy_devices_report_request_builder.MicrosoftGraphGetConfigurationPolicyDevicesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_configuration_policy_device_summary_report(self) -> microsoft_graph_get_configuration_policy_device_summary_report_request_builder.MicrosoftGraphGetConfigurationPolicyDeviceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyDeviceSummaryReport method.
        """
        return microsoft_graph_get_configuration_policy_device_summary_report_request_builder.MicrosoftGraphGetConfigurationPolicyDeviceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_configuration_policy_non_compliance_report(self) -> microsoft_graph_get_configuration_policy_non_compliance_report_request_builder.MicrosoftGraphGetConfigurationPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceReport method.
        """
        return microsoft_graph_get_configuration_policy_non_compliance_report_request_builder.MicrosoftGraphGetConfigurationPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_configuration_policy_non_compliance_summary_report(self) -> microsoft_graph_get_configuration_policy_non_compliance_summary_report_request_builder.MicrosoftGraphGetConfigurationPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceSummaryReport method.
        """
        return microsoft_graph_get_configuration_policy_non_compliance_summary_report_request_builder.MicrosoftGraphGetConfigurationPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_configuration_policy_settings_device_summary_report(self) -> microsoft_graph_get_configuration_policy_settings_device_summary_report_request_builder.MicrosoftGraphGetConfigurationPolicySettingsDeviceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicySettingsDeviceSummaryReport method.
        """
        return microsoft_graph_get_configuration_policy_settings_device_summary_report_request_builder.MicrosoftGraphGetConfigurationPolicySettingsDeviceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_configuration_setting_details_report(self) -> microsoft_graph_get_configuration_setting_details_report_request_builder.MicrosoftGraphGetConfigurationSettingDetailsReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingDetailsReport method.
        """
        return microsoft_graph_get_configuration_setting_details_report_request_builder.MicrosoftGraphGetConfigurationSettingDetailsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_configuration_setting_non_compliance_report(self) -> microsoft_graph_get_configuration_setting_non_compliance_report_request_builder.MicrosoftGraphGetConfigurationSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingNonComplianceReport method.
        """
        return microsoft_graph_get_configuration_setting_non_compliance_report_request_builder.MicrosoftGraphGetConfigurationSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_configuration_settings_report(self) -> microsoft_graph_get_configuration_settings_report_request_builder.MicrosoftGraphGetConfigurationSettingsReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingsReport method.
        """
        return microsoft_graph_get_configuration_settings_report_request_builder.MicrosoftGraphGetConfigurationSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_device_configuration_policy_settings_summary_report(self) -> microsoft_graph_get_device_configuration_policy_settings_summary_report_request_builder.MicrosoftGraphGetDeviceConfigurationPolicySettingsSummaryReportRequestBuilder:
        """
        Provides operations to call the getDeviceConfigurationPolicySettingsSummaryReport method.
        """
        return microsoft_graph_get_device_configuration_policy_settings_summary_report_request_builder.MicrosoftGraphGetDeviceConfigurationPolicySettingsSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_device_configuration_policy_status_summary(self) -> microsoft_graph_get_device_configuration_policy_status_summary_request_builder.MicrosoftGraphGetDeviceConfigurationPolicyStatusSummaryRequestBuilder:
        """
        Provides operations to call the getDeviceConfigurationPolicyStatusSummary method.
        """
        return microsoft_graph_get_device_configuration_policy_status_summary_request_builder.MicrosoftGraphGetDeviceConfigurationPolicyStatusSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_device_install_status_report(self) -> microsoft_graph_get_device_install_status_report_request_builder.MicrosoftGraphGetDeviceInstallStatusReportRequestBuilder:
        """
        Provides operations to call the getDeviceInstallStatusReport method.
        """
        return microsoft_graph_get_device_install_status_report_request_builder.MicrosoftGraphGetDeviceInstallStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_device_management_intent_per_setting_contributing_profiles(self) -> microsoft_graph_get_device_management_intent_per_setting_contributing_profiles_request_builder.MicrosoftGraphGetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentPerSettingContributingProfiles method.
        """
        return microsoft_graph_get_device_management_intent_per_setting_contributing_profiles_request_builder.MicrosoftGraphGetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_device_management_intent_settings_report(self) -> microsoft_graph_get_device_management_intent_settings_report_request_builder.MicrosoftGraphGetDeviceManagementIntentSettingsReportRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentSettingsReport method.
        """
        return microsoft_graph_get_device_management_intent_settings_report_request_builder.MicrosoftGraphGetDeviceManagementIntentSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_device_non_compliance_report(self) -> microsoft_graph_get_device_non_compliance_report_request_builder.MicrosoftGraphGetDeviceNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getDeviceNonComplianceReport method.
        """
        return microsoft_graph_get_device_non_compliance_report_request_builder.MicrosoftGraphGetDeviceNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_devices_without_compliance_policy_report(self) -> microsoft_graph_get_devices_without_compliance_policy_report_request_builder.MicrosoftGraphGetDevicesWithoutCompliancePolicyReportRequestBuilder:
        """
        Provides operations to call the getDevicesWithoutCompliancePolicyReport method.
        """
        return microsoft_graph_get_devices_without_compliance_policy_report_request_builder.MicrosoftGraphGetDevicesWithoutCompliancePolicyReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_encryption_report_for_devices(self) -> microsoft_graph_get_encryption_report_for_devices_request_builder.MicrosoftGraphGetEncryptionReportForDevicesRequestBuilder:
        """
        Provides operations to call the getEncryptionReportForDevices method.
        """
        return microsoft_graph_get_encryption_report_for_devices_request_builder.MicrosoftGraphGetEncryptionReportForDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_enrollment_configuration_policies_by_device(self) -> microsoft_graph_get_enrollment_configuration_policies_by_device_request_builder.MicrosoftGraphGetEnrollmentConfigurationPoliciesByDeviceRequestBuilder:
        """
        Provides operations to call the getEnrollmentConfigurationPoliciesByDevice method.
        """
        return microsoft_graph_get_enrollment_configuration_policies_by_device_request_builder.MicrosoftGraphGetEnrollmentConfigurationPoliciesByDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_failed_mobile_apps_report(self) -> microsoft_graph_get_failed_mobile_apps_report_request_builder.MicrosoftGraphGetFailedMobileAppsReportRequestBuilder:
        """
        Provides operations to call the getFailedMobileAppsReport method.
        """
        return microsoft_graph_get_failed_mobile_apps_report_request_builder.MicrosoftGraphGetFailedMobileAppsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_failed_mobile_apps_summary_report(self) -> microsoft_graph_get_failed_mobile_apps_summary_report_request_builder.MicrosoftGraphGetFailedMobileAppsSummaryReportRequestBuilder:
        """
        Provides operations to call the getFailedMobileAppsSummaryReport method.
        """
        return microsoft_graph_get_failed_mobile_apps_summary_report_request_builder.MicrosoftGraphGetFailedMobileAppsSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_group_policy_settings_device_settings_report(self) -> microsoft_graph_get_group_policy_settings_device_settings_report_request_builder.MicrosoftGraphGetGroupPolicySettingsDeviceSettingsReportRequestBuilder:
        """
        Provides operations to call the getGroupPolicySettingsDeviceSettingsReport method.
        """
        return microsoft_graph_get_group_policy_settings_device_settings_report_request_builder.MicrosoftGraphGetGroupPolicySettingsDeviceSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_historical_report(self) -> microsoft_graph_get_historical_report_request_builder.MicrosoftGraphGetHistoricalReportRequestBuilder:
        """
        Provides operations to call the getHistoricalReport method.
        """
        return microsoft_graph_get_historical_report_request_builder.MicrosoftGraphGetHistoricalReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_malware_summary_report(self) -> microsoft_graph_get_malware_summary_report_request_builder.MicrosoftGraphGetMalwareSummaryReportRequestBuilder:
        """
        Provides operations to call the getMalwareSummaryReport method.
        """
        return microsoft_graph_get_malware_summary_report_request_builder.MicrosoftGraphGetMalwareSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_mobile_application_management_app_configuration_report(self) -> microsoft_graph_get_mobile_application_management_app_configuration_report_request_builder.MicrosoftGraphGetMobileApplicationManagementAppConfigurationReportRequestBuilder:
        """
        Provides operations to call the getMobileApplicationManagementAppConfigurationReport method.
        """
        return microsoft_graph_get_mobile_application_management_app_configuration_report_request_builder.MicrosoftGraphGetMobileApplicationManagementAppConfigurationReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_mobile_application_management_app_registration_summary_report(self) -> microsoft_graph_get_mobile_application_management_app_registration_summary_report_request_builder.MicrosoftGraphGetMobileApplicationManagementAppRegistrationSummaryReportRequestBuilder:
        """
        Provides operations to call the getMobileApplicationManagementAppRegistrationSummaryReport method.
        """
        return microsoft_graph_get_mobile_application_management_app_registration_summary_report_request_builder.MicrosoftGraphGetMobileApplicationManagementAppRegistrationSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_noncompliant_devices_and_settings_report(self) -> microsoft_graph_get_noncompliant_devices_and_settings_report_request_builder.MicrosoftGraphGetNoncompliantDevicesAndSettingsReportRequestBuilder:
        """
        Provides operations to call the getNoncompliantDevicesAndSettingsReport method.
        """
        return microsoft_graph_get_noncompliant_devices_and_settings_report_request_builder.MicrosoftGraphGetNoncompliantDevicesAndSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_policy_non_compliance_metadata(self) -> microsoft_graph_get_policy_non_compliance_metadata_request_builder.MicrosoftGraphGetPolicyNonComplianceMetadataRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceMetadata method.
        """
        return microsoft_graph_get_policy_non_compliance_metadata_request_builder.MicrosoftGraphGetPolicyNonComplianceMetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_policy_non_compliance_report(self) -> microsoft_graph_get_policy_non_compliance_report_request_builder.MicrosoftGraphGetPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceReport method.
        """
        return microsoft_graph_get_policy_non_compliance_report_request_builder.MicrosoftGraphGetPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_policy_non_compliance_summary_report(self) -> microsoft_graph_get_policy_non_compliance_summary_report_request_builder.MicrosoftGraphGetPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceSummaryReport method.
        """
        return microsoft_graph_get_policy_non_compliance_summary_report_request_builder.MicrosoftGraphGetPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_quiet_time_policy_users_report(self) -> microsoft_graph_get_quiet_time_policy_users_report_request_builder.MicrosoftGraphGetQuietTimePolicyUsersReportRequestBuilder:
        """
        Provides operations to call the getQuietTimePolicyUsersReport method.
        """
        return microsoft_graph_get_quiet_time_policy_users_report_request_builder.MicrosoftGraphGetQuietTimePolicyUsersReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_quiet_time_policy_user_summary_report(self) -> microsoft_graph_get_quiet_time_policy_user_summary_report_request_builder.MicrosoftGraphGetQuietTimePolicyUserSummaryReportRequestBuilder:
        """
        Provides operations to call the getQuietTimePolicyUserSummaryReport method.
        """
        return microsoft_graph_get_quiet_time_policy_user_summary_report_request_builder.MicrosoftGraphGetQuietTimePolicyUserSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_related_apps_status_report(self) -> microsoft_graph_get_related_apps_status_report_request_builder.MicrosoftGraphGetRelatedAppsStatusReportRequestBuilder:
        """
        Provides operations to call the getRelatedAppsStatusReport method.
        """
        return microsoft_graph_get_related_apps_status_report_request_builder.MicrosoftGraphGetRelatedAppsStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_remote_assistance_sessions_report(self) -> microsoft_graph_get_remote_assistance_sessions_report_request_builder.MicrosoftGraphGetRemoteAssistanceSessionsReportRequestBuilder:
        """
        Provides operations to call the getRemoteAssistanceSessionsReport method.
        """
        return microsoft_graph_get_remote_assistance_sessions_report_request_builder.MicrosoftGraphGetRemoteAssistanceSessionsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_report_filters(self) -> microsoft_graph_get_report_filters_request_builder.MicrosoftGraphGetReportFiltersRequestBuilder:
        """
        Provides operations to call the getReportFilters method.
        """
        return microsoft_graph_get_report_filters_request_builder.MicrosoftGraphGetReportFiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_setting_non_compliance_report(self) -> microsoft_graph_get_setting_non_compliance_report_request_builder.MicrosoftGraphGetSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getSettingNonComplianceReport method.
        """
        return microsoft_graph_get_setting_non_compliance_report_request_builder.MicrosoftGraphGetSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_unhealthy_defender_agents_report(self) -> microsoft_graph_get_unhealthy_defender_agents_report_request_builder.MicrosoftGraphGetUnhealthyDefenderAgentsReportRequestBuilder:
        """
        Provides operations to call the getUnhealthyDefenderAgentsReport method.
        """
        return microsoft_graph_get_unhealthy_defender_agents_report_request_builder.MicrosoftGraphGetUnhealthyDefenderAgentsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_unhealthy_firewall_report(self) -> microsoft_graph_get_unhealthy_firewall_report_request_builder.MicrosoftGraphGetUnhealthyFirewallReportRequestBuilder:
        """
        Provides operations to call the getUnhealthyFirewallReport method.
        """
        return microsoft_graph_get_unhealthy_firewall_report_request_builder.MicrosoftGraphGetUnhealthyFirewallReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_unhealthy_firewall_summary_report(self) -> microsoft_graph_get_unhealthy_firewall_summary_report_request_builder.MicrosoftGraphGetUnhealthyFirewallSummaryReportRequestBuilder:
        """
        Provides operations to call the getUnhealthyFirewallSummaryReport method.
        """
        return microsoft_graph_get_unhealthy_firewall_summary_report_request_builder.MicrosoftGraphGetUnhealthyFirewallSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_user_install_status_report(self) -> microsoft_graph_get_user_install_status_report_request_builder.MicrosoftGraphGetUserInstallStatusReportRequestBuilder:
        """
        Provides operations to call the getUserInstallStatusReport method.
        """
        return microsoft_graph_get_user_install_status_report_request_builder.MicrosoftGraphGetUserInstallStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_windows_quality_update_alerts_per_policy_per_device_report(self) -> microsoft_graph_get_windows_quality_update_alerts_per_policy_per_device_report_request_builder.MicrosoftGraphGetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequestBuilder:
        """
        Provides operations to call the getWindowsQualityUpdateAlertsPerPolicyPerDeviceReport method.
        """
        return microsoft_graph_get_windows_quality_update_alerts_per_policy_per_device_report_request_builder.MicrosoftGraphGetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_windows_quality_update_alert_summary_report(self) -> microsoft_graph_get_windows_quality_update_alert_summary_report_request_builder.MicrosoftGraphGetWindowsQualityUpdateAlertSummaryReportRequestBuilder:
        """
        Provides operations to call the getWindowsQualityUpdateAlertSummaryReport method.
        """
        return microsoft_graph_get_windows_quality_update_alert_summary_report_request_builder.MicrosoftGraphGetWindowsQualityUpdateAlertSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_windows_update_alerts_per_policy_per_device_report(self) -> microsoft_graph_get_windows_update_alerts_per_policy_per_device_report_request_builder.MicrosoftGraphGetWindowsUpdateAlertsPerPolicyPerDeviceReportRequestBuilder:
        """
        Provides operations to call the getWindowsUpdateAlertsPerPolicyPerDeviceReport method.
        """
        return microsoft_graph_get_windows_update_alerts_per_policy_per_device_report_request_builder.MicrosoftGraphGetWindowsUpdateAlertsPerPolicyPerDeviceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_windows_update_alert_summary_report(self) -> microsoft_graph_get_windows_update_alert_summary_report_request_builder.MicrosoftGraphGetWindowsUpdateAlertSummaryReportRequestBuilder:
        """
        Provides operations to call the getWindowsUpdateAlertSummaryReport method.
        """
        return microsoft_graph_get_windows_update_alert_summary_report_request_builder.MicrosoftGraphGetWindowsUpdateAlertSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_zebra_fota_deployment_report(self) -> microsoft_graph_get_zebra_fota_deployment_report_request_builder.MicrosoftGraphGetZebraFotaDeploymentReportRequestBuilder:
        """
        Provides operations to call the getZebraFotaDeploymentReport method.
        """
        return microsoft_graph_get_zebra_fota_deployment_report_request_builder.MicrosoftGraphGetZebraFotaDeploymentReportRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    
    async def delete(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property reports for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
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
    
    async def get(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> Optional[device_management_reports.DeviceManagementReports]:
        """
        Reports singleton
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management_reports.DeviceManagementReports]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, device_management_reports.DeviceManagementReports, error_mapping)
    
    async def patch(self,body: Optional[device_management_reports.DeviceManagementReports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> Optional[device_management_reports.DeviceManagementReports]:
        """
        Update the navigation property reports in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management_reports.DeviceManagementReports]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, device_management_reports.DeviceManagementReports, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
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
    
    def to_get_request_information(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
    
    def to_patch_request_information(self,body: Optional[device_management_reports.DeviceManagementReports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
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

    

