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
    from ...models.device_management_reports import DeviceManagementReports
    from ...models.o_data_errors.o_data_error import ODataError
    from .cached_report_configurations.cached_report_configurations_request_builder import CachedReportConfigurationsRequestBuilder
    from .export_jobs.export_jobs_request_builder import ExportJobsRequestBuilder
    from .get_active_malware_report.get_active_malware_report_request_builder import GetActiveMalwareReportRequestBuilder
    from .get_active_malware_summary_report.get_active_malware_summary_report_request_builder import GetActiveMalwareSummaryReportRequestBuilder
    from .get_all_certificates_report.get_all_certificates_report_request_builder import GetAllCertificatesReportRequestBuilder
    from .get_apps_install_summary_report.get_apps_install_summary_report_request_builder import GetAppsInstallSummaryReportRequestBuilder
    from .get_app_status_overview_report.get_app_status_overview_report_request_builder import GetAppStatusOverviewReportRequestBuilder
    from .get_cached_report.get_cached_report_request_builder import GetCachedReportRequestBuilder
    from .get_certificates_report.get_certificates_report_request_builder import GetCertificatesReportRequestBuilder
    from .get_compliance_policies_report_for_device.get_compliance_policies_report_for_device_request_builder import GetCompliancePoliciesReportForDeviceRequestBuilder
    from .get_compliance_policy_devices_report.get_compliance_policy_devices_report_request_builder import GetCompliancePolicyDevicesReportRequestBuilder
    from .get_compliance_policy_device_summary_report.get_compliance_policy_device_summary_report_request_builder import GetCompliancePolicyDeviceSummaryReportRequestBuilder
    from .get_compliance_policy_non_compliance_report.get_compliance_policy_non_compliance_report_request_builder import GetCompliancePolicyNonComplianceReportRequestBuilder
    from .get_compliance_policy_non_compliance_summary_report.get_compliance_policy_non_compliance_summary_report_request_builder import GetCompliancePolicyNonComplianceSummaryReportRequestBuilder
    from .get_compliance_settings_report.get_compliance_settings_report_request_builder import GetComplianceSettingsReportRequestBuilder
    from .get_compliance_setting_details_report.get_compliance_setting_details_report_request_builder import GetComplianceSettingDetailsReportRequestBuilder
    from .get_compliance_setting_non_compliance_report.get_compliance_setting_non_compliance_report_request_builder import GetComplianceSettingNonComplianceReportRequestBuilder
    from .get_configuration_policies_report_for_device.get_configuration_policies_report_for_device_request_builder import GetConfigurationPoliciesReportForDeviceRequestBuilder
    from .get_configuration_policy_devices_report.get_configuration_policy_devices_report_request_builder import GetConfigurationPolicyDevicesReportRequestBuilder
    from .get_configuration_policy_device_summary_report.get_configuration_policy_device_summary_report_request_builder import GetConfigurationPolicyDeviceSummaryReportRequestBuilder
    from .get_configuration_policy_non_compliance_report.get_configuration_policy_non_compliance_report_request_builder import GetConfigurationPolicyNonComplianceReportRequestBuilder
    from .get_configuration_policy_non_compliance_summary_report.get_configuration_policy_non_compliance_summary_report_request_builder import GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder
    from .get_configuration_policy_settings_device_summary_report.get_configuration_policy_settings_device_summary_report_request_builder import GetConfigurationPolicySettingsDeviceSummaryReportRequestBuilder
    from .get_configuration_settings_report.get_configuration_settings_report_request_builder import GetConfigurationSettingsReportRequestBuilder
    from .get_configuration_setting_details_report.get_configuration_setting_details_report_request_builder import GetConfigurationSettingDetailsReportRequestBuilder
    from .get_configuration_setting_non_compliance_report.get_configuration_setting_non_compliance_report_request_builder import GetConfigurationSettingNonComplianceReportRequestBuilder
    from .get_config_manager_device_policy_status_report.get_config_manager_device_policy_status_report_request_builder import GetConfigManagerDevicePolicyStatusReportRequestBuilder
    from .get_devices_status_by_policy_platform_compliance_report.get_devices_status_by_policy_platform_compliance_report_request_builder import GetDevicesStatusByPolicyPlatformComplianceReportRequestBuilder
    from .get_devices_status_by_setting_report.get_devices_status_by_setting_report_request_builder import GetDevicesStatusBySettingReportRequestBuilder
    from .get_devices_without_compliance_policy_report.get_devices_without_compliance_policy_report_request_builder import GetDevicesWithoutCompliancePolicyReportRequestBuilder
    from .get_device_configuration_policy_settings_summary_report.get_device_configuration_policy_settings_summary_report_request_builder import GetDeviceConfigurationPolicySettingsSummaryReportRequestBuilder
    from .get_device_configuration_policy_status_summary.get_device_configuration_policy_status_summary_request_builder import GetDeviceConfigurationPolicyStatusSummaryRequestBuilder
    from .get_device_install_status_report.get_device_install_status_report_request_builder import GetDeviceInstallStatusReportRequestBuilder
    from .get_device_management_intent_per_setting_contributing_profiles.get_device_management_intent_per_setting_contributing_profiles_request_builder import GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder
    from .get_device_management_intent_settings_report.get_device_management_intent_settings_report_request_builder import GetDeviceManagementIntentSettingsReportRequestBuilder
    from .get_device_non_compliance_report.get_device_non_compliance_report_request_builder import GetDeviceNonComplianceReportRequestBuilder
    from .get_device_policies_compliance_report.get_device_policies_compliance_report_request_builder import GetDevicePoliciesComplianceReportRequestBuilder
    from .get_device_policy_settings_compliance_report.get_device_policy_settings_compliance_report_request_builder import GetDevicePolicySettingsComplianceReportRequestBuilder
    from .get_device_status_by_compliace_policy_report.get_device_status_by_compliace_policy_report_request_builder import GetDeviceStatusByCompliacePolicyReportRequestBuilder
    from .get_device_status_by_compliance_policy_setting_report.get_device_status_by_compliance_policy_setting_report_request_builder import GetDeviceStatusByCompliancePolicySettingReportRequestBuilder
    from .get_device_status_summary_by_compliace_policy_report.get_device_status_summary_by_compliace_policy_report_request_builder import GetDeviceStatusSummaryByCompliacePolicyReportRequestBuilder
    from .get_device_status_summary_by_compliance_policy_settings_report.get_device_status_summary_by_compliance_policy_settings_report_request_builder import GetDeviceStatusSummaryByCompliancePolicySettingsReportRequestBuilder
    from .get_encryption_report_for_devices.get_encryption_report_for_devices_request_builder import GetEncryptionReportForDevicesRequestBuilder
    from .get_enrollment_configuration_policies_by_device.get_enrollment_configuration_policies_by_device_request_builder import GetEnrollmentConfigurationPoliciesByDeviceRequestBuilder
    from .get_failed_mobile_apps_report.get_failed_mobile_apps_report_request_builder import GetFailedMobileAppsReportRequestBuilder
    from .get_failed_mobile_apps_summary_report.get_failed_mobile_apps_summary_report_request_builder import GetFailedMobileAppsSummaryReportRequestBuilder
    from .get_group_policy_settings_device_settings_report.get_group_policy_settings_device_settings_report_request_builder import GetGroupPolicySettingsDeviceSettingsReportRequestBuilder
    from .get_historical_report.get_historical_report_request_builder import GetHistoricalReportRequestBuilder
    from .get_malware_summary_report.get_malware_summary_report_request_builder import GetMalwareSummaryReportRequestBuilder
    from .get_mobile_application_management_app_configuration_report.get_mobile_application_management_app_configuration_report_request_builder import GetMobileApplicationManagementAppConfigurationReportRequestBuilder
    from .get_mobile_application_management_app_registration_summary_report.get_mobile_application_management_app_registration_summary_report_request_builder import GetMobileApplicationManagementAppRegistrationSummaryReportRequestBuilder
    from .get_noncompliant_devices_and_settings_report.get_noncompliant_devices_and_settings_report_request_builder import GetNoncompliantDevicesAndSettingsReportRequestBuilder
    from .get_policy_non_compliance_metadata.get_policy_non_compliance_metadata_request_builder import GetPolicyNonComplianceMetadataRequestBuilder
    from .get_policy_non_compliance_report.get_policy_non_compliance_report_request_builder import GetPolicyNonComplianceReportRequestBuilder
    from .get_policy_non_compliance_summary_report.get_policy_non_compliance_summary_report_request_builder import GetPolicyNonComplianceSummaryReportRequestBuilder
    from .get_quiet_time_policy_users_report.get_quiet_time_policy_users_report_request_builder import GetQuietTimePolicyUsersReportRequestBuilder
    from .get_quiet_time_policy_user_summary_report.get_quiet_time_policy_user_summary_report_request_builder import GetQuietTimePolicyUserSummaryReportRequestBuilder
    from .get_related_apps_status_report.get_related_apps_status_report_request_builder import GetRelatedAppsStatusReportRequestBuilder
    from .get_remote_assistance_sessions_report.get_remote_assistance_sessions_report_request_builder import GetRemoteAssistanceSessionsReportRequestBuilder
    from .get_report_filters.get_report_filters_request_builder import GetReportFiltersRequestBuilder
    from .get_setting_non_compliance_report.get_setting_non_compliance_report_request_builder import GetSettingNonComplianceReportRequestBuilder
    from .get_unhealthy_defender_agents_report.get_unhealthy_defender_agents_report_request_builder import GetUnhealthyDefenderAgentsReportRequestBuilder
    from .get_unhealthy_firewall_report.get_unhealthy_firewall_report_request_builder import GetUnhealthyFirewallReportRequestBuilder
    from .get_unhealthy_firewall_summary_report.get_unhealthy_firewall_summary_report_request_builder import GetUnhealthyFirewallSummaryReportRequestBuilder
    from .get_user_install_status_report.get_user_install_status_report_request_builder import GetUserInstallStatusReportRequestBuilder
    from .get_windows_driver_update_alerts_per_policy_per_device_report.get_windows_driver_update_alerts_per_policy_per_device_report_request_builder import GetWindowsDriverUpdateAlertsPerPolicyPerDeviceReportRequestBuilder
    from .get_windows_driver_update_alert_summary_report.get_windows_driver_update_alert_summary_report_request_builder import GetWindowsDriverUpdateAlertSummaryReportRequestBuilder
    from .get_windows_quality_update_alerts_per_policy_per_device_report.get_windows_quality_update_alerts_per_policy_per_device_report_request_builder import GetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequestBuilder
    from .get_windows_quality_update_alert_summary_report.get_windows_quality_update_alert_summary_report_request_builder import GetWindowsQualityUpdateAlertSummaryReportRequestBuilder
    from .get_windows_update_alerts_per_policy_per_device_report.get_windows_update_alerts_per_policy_per_device_report_request_builder import GetWindowsUpdateAlertsPerPolicyPerDeviceReportRequestBuilder
    from .get_windows_update_alert_summary_report.get_windows_update_alert_summary_report_request_builder import GetWindowsUpdateAlertSummaryReportRequestBuilder
    from .get_zebra_fota_deployment_report.get_zebra_fota_deployment_report_request_builder import GetZebraFotaDeploymentReportRequestBuilder
    from .retrieve_assigned_applications_report.retrieve_assigned_applications_report_request_builder import RetrieveAssignedApplicationsReportRequestBuilder
    from .retrieve_win32_catalog_apps_update_report.retrieve_win32_catalog_apps_update_report_request_builder import RetrieveWin32CatalogAppsUpdateReportRequestBuilder

class ReportsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the reports property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ReportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/reports{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property reports for deviceManagement
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ReportsRequestBuilderGetQueryParameters]] = None) -> Optional[DeviceManagementReports]:
        """
        Reports singleton
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagementReports]
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
        from ...models.device_management_reports import DeviceManagementReports

        return await self.request_adapter.send_async(request_info, DeviceManagementReports, error_mapping)
    
    async def patch(self,body: DeviceManagementReports, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeviceManagementReports]:
        """
        Update the navigation property reports in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagementReports]
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
        from ...models.device_management_reports import DeviceManagementReports

        return await self.request_adapter.send_async(request_info, DeviceManagementReports, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property reports for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ReportsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Reports singleton
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DeviceManagementReports, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property reports in deviceManagement
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
    
    def with_url(self,raw_url: str) -> ReportsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ReportsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ReportsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def cached_report_configurations(self) -> CachedReportConfigurationsRequestBuilder:
        """
        Provides operations to manage the cachedReportConfigurations property of the microsoft.graph.deviceManagementReports entity.
        """
        from .cached_report_configurations.cached_report_configurations_request_builder import CachedReportConfigurationsRequestBuilder

        return CachedReportConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def export_jobs(self) -> ExportJobsRequestBuilder:
        """
        Provides operations to manage the exportJobs property of the microsoft.graph.deviceManagementReports entity.
        """
        from .export_jobs.export_jobs_request_builder import ExportJobsRequestBuilder

        return ExportJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_active_malware_report(self) -> GetActiveMalwareReportRequestBuilder:
        """
        Provides operations to call the getActiveMalwareReport method.
        """
        from .get_active_malware_report.get_active_malware_report_request_builder import GetActiveMalwareReportRequestBuilder

        return GetActiveMalwareReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_active_malware_summary_report(self) -> GetActiveMalwareSummaryReportRequestBuilder:
        """
        Provides operations to call the getActiveMalwareSummaryReport method.
        """
        from .get_active_malware_summary_report.get_active_malware_summary_report_request_builder import GetActiveMalwareSummaryReportRequestBuilder

        return GetActiveMalwareSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_all_certificates_report(self) -> GetAllCertificatesReportRequestBuilder:
        """
        Provides operations to call the getAllCertificatesReport method.
        """
        from .get_all_certificates_report.get_all_certificates_report_request_builder import GetAllCertificatesReportRequestBuilder

        return GetAllCertificatesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_app_status_overview_report(self) -> GetAppStatusOverviewReportRequestBuilder:
        """
        Provides operations to call the getAppStatusOverviewReport method.
        """
        from .get_app_status_overview_report.get_app_status_overview_report_request_builder import GetAppStatusOverviewReportRequestBuilder

        return GetAppStatusOverviewReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_apps_install_summary_report(self) -> GetAppsInstallSummaryReportRequestBuilder:
        """
        Provides operations to call the getAppsInstallSummaryReport method.
        """
        from .get_apps_install_summary_report.get_apps_install_summary_report_request_builder import GetAppsInstallSummaryReportRequestBuilder

        return GetAppsInstallSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_cached_report(self) -> GetCachedReportRequestBuilder:
        """
        Provides operations to call the getCachedReport method.
        """
        from .get_cached_report.get_cached_report_request_builder import GetCachedReportRequestBuilder

        return GetCachedReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_certificates_report(self) -> GetCertificatesReportRequestBuilder:
        """
        Provides operations to call the getCertificatesReport method.
        """
        from .get_certificates_report.get_certificates_report_request_builder import GetCertificatesReportRequestBuilder

        return GetCertificatesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policies_report_for_device(self) -> GetCompliancePoliciesReportForDeviceRequestBuilder:
        """
        Provides operations to call the getCompliancePoliciesReportForDevice method.
        """
        from .get_compliance_policies_report_for_device.get_compliance_policies_report_for_device_request_builder import GetCompliancePoliciesReportForDeviceRequestBuilder

        return GetCompliancePoliciesReportForDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_device_summary_report(self) -> GetCompliancePolicyDeviceSummaryReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyDeviceSummaryReport method.
        """
        from .get_compliance_policy_device_summary_report.get_compliance_policy_device_summary_report_request_builder import GetCompliancePolicyDeviceSummaryReportRequestBuilder

        return GetCompliancePolicyDeviceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_devices_report(self) -> GetCompliancePolicyDevicesReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyDevicesReport method.
        """
        from .get_compliance_policy_devices_report.get_compliance_policy_devices_report_request_builder import GetCompliancePolicyDevicesReportRequestBuilder

        return GetCompliancePolicyDevicesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_non_compliance_report(self) -> GetCompliancePolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceReport method.
        """
        from .get_compliance_policy_non_compliance_report.get_compliance_policy_non_compliance_report_request_builder import GetCompliancePolicyNonComplianceReportRequestBuilder

        return GetCompliancePolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_non_compliance_summary_report(self) -> GetCompliancePolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceSummaryReport method.
        """
        from .get_compliance_policy_non_compliance_summary_report.get_compliance_policy_non_compliance_summary_report_request_builder import GetCompliancePolicyNonComplianceSummaryReportRequestBuilder

        return GetCompliancePolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_setting_details_report(self) -> GetComplianceSettingDetailsReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingDetailsReport method.
        """
        from .get_compliance_setting_details_report.get_compliance_setting_details_report_request_builder import GetComplianceSettingDetailsReportRequestBuilder

        return GetComplianceSettingDetailsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_setting_non_compliance_report(self) -> GetComplianceSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingNonComplianceReport method.
        """
        from .get_compliance_setting_non_compliance_report.get_compliance_setting_non_compliance_report_request_builder import GetComplianceSettingNonComplianceReportRequestBuilder

        return GetComplianceSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_settings_report(self) -> GetComplianceSettingsReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingsReport method.
        """
        from .get_compliance_settings_report.get_compliance_settings_report_request_builder import GetComplianceSettingsReportRequestBuilder

        return GetComplianceSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_config_manager_device_policy_status_report(self) -> GetConfigManagerDevicePolicyStatusReportRequestBuilder:
        """
        Provides operations to call the getConfigManagerDevicePolicyStatusReport method.
        """
        from .get_config_manager_device_policy_status_report.get_config_manager_device_policy_status_report_request_builder import GetConfigManagerDevicePolicyStatusReportRequestBuilder

        return GetConfigManagerDevicePolicyStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policies_report_for_device(self) -> GetConfigurationPoliciesReportForDeviceRequestBuilder:
        """
        Provides operations to call the getConfigurationPoliciesReportForDevice method.
        """
        from .get_configuration_policies_report_for_device.get_configuration_policies_report_for_device_request_builder import GetConfigurationPoliciesReportForDeviceRequestBuilder

        return GetConfigurationPoliciesReportForDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_device_summary_report(self) -> GetConfigurationPolicyDeviceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyDeviceSummaryReport method.
        """
        from .get_configuration_policy_device_summary_report.get_configuration_policy_device_summary_report_request_builder import GetConfigurationPolicyDeviceSummaryReportRequestBuilder

        return GetConfigurationPolicyDeviceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_devices_report(self) -> GetConfigurationPolicyDevicesReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyDevicesReport method.
        """
        from .get_configuration_policy_devices_report.get_configuration_policy_devices_report_request_builder import GetConfigurationPolicyDevicesReportRequestBuilder

        return GetConfigurationPolicyDevicesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_non_compliance_report(self) -> GetConfigurationPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceReport method.
        """
        from .get_configuration_policy_non_compliance_report.get_configuration_policy_non_compliance_report_request_builder import GetConfigurationPolicyNonComplianceReportRequestBuilder

        return GetConfigurationPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_non_compliance_summary_report(self) -> GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceSummaryReport method.
        """
        from .get_configuration_policy_non_compliance_summary_report.get_configuration_policy_non_compliance_summary_report_request_builder import GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder

        return GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_settings_device_summary_report(self) -> GetConfigurationPolicySettingsDeviceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicySettingsDeviceSummaryReport method.
        """
        from .get_configuration_policy_settings_device_summary_report.get_configuration_policy_settings_device_summary_report_request_builder import GetConfigurationPolicySettingsDeviceSummaryReportRequestBuilder

        return GetConfigurationPolicySettingsDeviceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_setting_details_report(self) -> GetConfigurationSettingDetailsReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingDetailsReport method.
        """
        from .get_configuration_setting_details_report.get_configuration_setting_details_report_request_builder import GetConfigurationSettingDetailsReportRequestBuilder

        return GetConfigurationSettingDetailsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_setting_non_compliance_report(self) -> GetConfigurationSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingNonComplianceReport method.
        """
        from .get_configuration_setting_non_compliance_report.get_configuration_setting_non_compliance_report_request_builder import GetConfigurationSettingNonComplianceReportRequestBuilder

        return GetConfigurationSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_settings_report(self) -> GetConfigurationSettingsReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingsReport method.
        """
        from .get_configuration_settings_report.get_configuration_settings_report_request_builder import GetConfigurationSettingsReportRequestBuilder

        return GetConfigurationSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_configuration_policy_settings_summary_report(self) -> GetDeviceConfigurationPolicySettingsSummaryReportRequestBuilder:
        """
        Provides operations to call the getDeviceConfigurationPolicySettingsSummaryReport method.
        """
        from .get_device_configuration_policy_settings_summary_report.get_device_configuration_policy_settings_summary_report_request_builder import GetDeviceConfigurationPolicySettingsSummaryReportRequestBuilder

        return GetDeviceConfigurationPolicySettingsSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_configuration_policy_status_summary(self) -> GetDeviceConfigurationPolicyStatusSummaryRequestBuilder:
        """
        Provides operations to call the getDeviceConfigurationPolicyStatusSummary method.
        """
        from .get_device_configuration_policy_status_summary.get_device_configuration_policy_status_summary_request_builder import GetDeviceConfigurationPolicyStatusSummaryRequestBuilder

        return GetDeviceConfigurationPolicyStatusSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_install_status_report(self) -> GetDeviceInstallStatusReportRequestBuilder:
        """
        Provides operations to call the getDeviceInstallStatusReport method.
        """
        from .get_device_install_status_report.get_device_install_status_report_request_builder import GetDeviceInstallStatusReportRequestBuilder

        return GetDeviceInstallStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_management_intent_per_setting_contributing_profiles(self) -> GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentPerSettingContributingProfiles method.
        """
        from .get_device_management_intent_per_setting_contributing_profiles.get_device_management_intent_per_setting_contributing_profiles_request_builder import GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder

        return GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_management_intent_settings_report(self) -> GetDeviceManagementIntentSettingsReportRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentSettingsReport method.
        """
        from .get_device_management_intent_settings_report.get_device_management_intent_settings_report_request_builder import GetDeviceManagementIntentSettingsReportRequestBuilder

        return GetDeviceManagementIntentSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_non_compliance_report(self) -> GetDeviceNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getDeviceNonComplianceReport method.
        """
        from .get_device_non_compliance_report.get_device_non_compliance_report_request_builder import GetDeviceNonComplianceReportRequestBuilder

        return GetDeviceNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_policies_compliance_report(self) -> GetDevicePoliciesComplianceReportRequestBuilder:
        """
        Provides operations to call the getDevicePoliciesComplianceReport method.
        """
        from .get_device_policies_compliance_report.get_device_policies_compliance_report_request_builder import GetDevicePoliciesComplianceReportRequestBuilder

        return GetDevicePoliciesComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_policy_settings_compliance_report(self) -> GetDevicePolicySettingsComplianceReportRequestBuilder:
        """
        Provides operations to call the getDevicePolicySettingsComplianceReport method.
        """
        from .get_device_policy_settings_compliance_report.get_device_policy_settings_compliance_report_request_builder import GetDevicePolicySettingsComplianceReportRequestBuilder

        return GetDevicePolicySettingsComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_status_by_compliace_policy_report(self) -> GetDeviceStatusByCompliacePolicyReportRequestBuilder:
        """
        Provides operations to call the getDeviceStatusByCompliacePolicyReport method.
        """
        from .get_device_status_by_compliace_policy_report.get_device_status_by_compliace_policy_report_request_builder import GetDeviceStatusByCompliacePolicyReportRequestBuilder

        return GetDeviceStatusByCompliacePolicyReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_status_by_compliance_policy_setting_report(self) -> GetDeviceStatusByCompliancePolicySettingReportRequestBuilder:
        """
        Provides operations to call the getDeviceStatusByCompliancePolicySettingReport method.
        """
        from .get_device_status_by_compliance_policy_setting_report.get_device_status_by_compliance_policy_setting_report_request_builder import GetDeviceStatusByCompliancePolicySettingReportRequestBuilder

        return GetDeviceStatusByCompliancePolicySettingReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_status_summary_by_compliace_policy_report(self) -> GetDeviceStatusSummaryByCompliacePolicyReportRequestBuilder:
        """
        Provides operations to call the getDeviceStatusSummaryByCompliacePolicyReport method.
        """
        from .get_device_status_summary_by_compliace_policy_report.get_device_status_summary_by_compliace_policy_report_request_builder import GetDeviceStatusSummaryByCompliacePolicyReportRequestBuilder

        return GetDeviceStatusSummaryByCompliacePolicyReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_status_summary_by_compliance_policy_settings_report(self) -> GetDeviceStatusSummaryByCompliancePolicySettingsReportRequestBuilder:
        """
        Provides operations to call the getDeviceStatusSummaryByCompliancePolicySettingsReport method.
        """
        from .get_device_status_summary_by_compliance_policy_settings_report.get_device_status_summary_by_compliance_policy_settings_report_request_builder import GetDeviceStatusSummaryByCompliancePolicySettingsReportRequestBuilder

        return GetDeviceStatusSummaryByCompliancePolicySettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_devices_status_by_policy_platform_compliance_report(self) -> GetDevicesStatusByPolicyPlatformComplianceReportRequestBuilder:
        """
        Provides operations to call the getDevicesStatusByPolicyPlatformComplianceReport method.
        """
        from .get_devices_status_by_policy_platform_compliance_report.get_devices_status_by_policy_platform_compliance_report_request_builder import GetDevicesStatusByPolicyPlatformComplianceReportRequestBuilder

        return GetDevicesStatusByPolicyPlatformComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_devices_status_by_setting_report(self) -> GetDevicesStatusBySettingReportRequestBuilder:
        """
        Provides operations to call the getDevicesStatusBySettingReport method.
        """
        from .get_devices_status_by_setting_report.get_devices_status_by_setting_report_request_builder import GetDevicesStatusBySettingReportRequestBuilder

        return GetDevicesStatusBySettingReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_devices_without_compliance_policy_report(self) -> GetDevicesWithoutCompliancePolicyReportRequestBuilder:
        """
        Provides operations to call the getDevicesWithoutCompliancePolicyReport method.
        """
        from .get_devices_without_compliance_policy_report.get_devices_without_compliance_policy_report_request_builder import GetDevicesWithoutCompliancePolicyReportRequestBuilder

        return GetDevicesWithoutCompliancePolicyReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_encryption_report_for_devices(self) -> GetEncryptionReportForDevicesRequestBuilder:
        """
        Provides operations to call the getEncryptionReportForDevices method.
        """
        from .get_encryption_report_for_devices.get_encryption_report_for_devices_request_builder import GetEncryptionReportForDevicesRequestBuilder

        return GetEncryptionReportForDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_enrollment_configuration_policies_by_device(self) -> GetEnrollmentConfigurationPoliciesByDeviceRequestBuilder:
        """
        Provides operations to call the getEnrollmentConfigurationPoliciesByDevice method.
        """
        from .get_enrollment_configuration_policies_by_device.get_enrollment_configuration_policies_by_device_request_builder import GetEnrollmentConfigurationPoliciesByDeviceRequestBuilder

        return GetEnrollmentConfigurationPoliciesByDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_failed_mobile_apps_report(self) -> GetFailedMobileAppsReportRequestBuilder:
        """
        Provides operations to call the getFailedMobileAppsReport method.
        """
        from .get_failed_mobile_apps_report.get_failed_mobile_apps_report_request_builder import GetFailedMobileAppsReportRequestBuilder

        return GetFailedMobileAppsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_failed_mobile_apps_summary_report(self) -> GetFailedMobileAppsSummaryReportRequestBuilder:
        """
        Provides operations to call the getFailedMobileAppsSummaryReport method.
        """
        from .get_failed_mobile_apps_summary_report.get_failed_mobile_apps_summary_report_request_builder import GetFailedMobileAppsSummaryReportRequestBuilder

        return GetFailedMobileAppsSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_group_policy_settings_device_settings_report(self) -> GetGroupPolicySettingsDeviceSettingsReportRequestBuilder:
        """
        Provides operations to call the getGroupPolicySettingsDeviceSettingsReport method.
        """
        from .get_group_policy_settings_device_settings_report.get_group_policy_settings_device_settings_report_request_builder import GetGroupPolicySettingsDeviceSettingsReportRequestBuilder

        return GetGroupPolicySettingsDeviceSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_historical_report(self) -> GetHistoricalReportRequestBuilder:
        """
        Provides operations to call the getHistoricalReport method.
        """
        from .get_historical_report.get_historical_report_request_builder import GetHistoricalReportRequestBuilder

        return GetHistoricalReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_malware_summary_report(self) -> GetMalwareSummaryReportRequestBuilder:
        """
        Provides operations to call the getMalwareSummaryReport method.
        """
        from .get_malware_summary_report.get_malware_summary_report_request_builder import GetMalwareSummaryReportRequestBuilder

        return GetMalwareSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_mobile_application_management_app_configuration_report(self) -> GetMobileApplicationManagementAppConfigurationReportRequestBuilder:
        """
        Provides operations to call the getMobileApplicationManagementAppConfigurationReport method.
        """
        from .get_mobile_application_management_app_configuration_report.get_mobile_application_management_app_configuration_report_request_builder import GetMobileApplicationManagementAppConfigurationReportRequestBuilder

        return GetMobileApplicationManagementAppConfigurationReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_mobile_application_management_app_registration_summary_report(self) -> GetMobileApplicationManagementAppRegistrationSummaryReportRequestBuilder:
        """
        Provides operations to call the getMobileApplicationManagementAppRegistrationSummaryReport method.
        """
        from .get_mobile_application_management_app_registration_summary_report.get_mobile_application_management_app_registration_summary_report_request_builder import GetMobileApplicationManagementAppRegistrationSummaryReportRequestBuilder

        return GetMobileApplicationManagementAppRegistrationSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_noncompliant_devices_and_settings_report(self) -> GetNoncompliantDevicesAndSettingsReportRequestBuilder:
        """
        Provides operations to call the getNoncompliantDevicesAndSettingsReport method.
        """
        from .get_noncompliant_devices_and_settings_report.get_noncompliant_devices_and_settings_report_request_builder import GetNoncompliantDevicesAndSettingsReportRequestBuilder

        return GetNoncompliantDevicesAndSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_metadata(self) -> GetPolicyNonComplianceMetadataRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceMetadata method.
        """
        from .get_policy_non_compliance_metadata.get_policy_non_compliance_metadata_request_builder import GetPolicyNonComplianceMetadataRequestBuilder

        return GetPolicyNonComplianceMetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_report(self) -> GetPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceReport method.
        """
        from .get_policy_non_compliance_report.get_policy_non_compliance_report_request_builder import GetPolicyNonComplianceReportRequestBuilder

        return GetPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_summary_report(self) -> GetPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceSummaryReport method.
        """
        from .get_policy_non_compliance_summary_report.get_policy_non_compliance_summary_report_request_builder import GetPolicyNonComplianceSummaryReportRequestBuilder

        return GetPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_quiet_time_policy_user_summary_report(self) -> GetQuietTimePolicyUserSummaryReportRequestBuilder:
        """
        Provides operations to call the getQuietTimePolicyUserSummaryReport method.
        """
        from .get_quiet_time_policy_user_summary_report.get_quiet_time_policy_user_summary_report_request_builder import GetQuietTimePolicyUserSummaryReportRequestBuilder

        return GetQuietTimePolicyUserSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_quiet_time_policy_users_report(self) -> GetQuietTimePolicyUsersReportRequestBuilder:
        """
        Provides operations to call the getQuietTimePolicyUsersReport method.
        """
        from .get_quiet_time_policy_users_report.get_quiet_time_policy_users_report_request_builder import GetQuietTimePolicyUsersReportRequestBuilder

        return GetQuietTimePolicyUsersReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_related_apps_status_report(self) -> GetRelatedAppsStatusReportRequestBuilder:
        """
        Provides operations to call the getRelatedAppsStatusReport method.
        """
        from .get_related_apps_status_report.get_related_apps_status_report_request_builder import GetRelatedAppsStatusReportRequestBuilder

        return GetRelatedAppsStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_remote_assistance_sessions_report(self) -> GetRemoteAssistanceSessionsReportRequestBuilder:
        """
        Provides operations to call the getRemoteAssistanceSessionsReport method.
        """
        from .get_remote_assistance_sessions_report.get_remote_assistance_sessions_report_request_builder import GetRemoteAssistanceSessionsReportRequestBuilder

        return GetRemoteAssistanceSessionsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_report_filters(self) -> GetReportFiltersRequestBuilder:
        """
        Provides operations to call the getReportFilters method.
        """
        from .get_report_filters.get_report_filters_request_builder import GetReportFiltersRequestBuilder

        return GetReportFiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_setting_non_compliance_report(self) -> GetSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getSettingNonComplianceReport method.
        """
        from .get_setting_non_compliance_report.get_setting_non_compliance_report_request_builder import GetSettingNonComplianceReportRequestBuilder

        return GetSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_unhealthy_defender_agents_report(self) -> GetUnhealthyDefenderAgentsReportRequestBuilder:
        """
        Provides operations to call the getUnhealthyDefenderAgentsReport method.
        """
        from .get_unhealthy_defender_agents_report.get_unhealthy_defender_agents_report_request_builder import GetUnhealthyDefenderAgentsReportRequestBuilder

        return GetUnhealthyDefenderAgentsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_unhealthy_firewall_report(self) -> GetUnhealthyFirewallReportRequestBuilder:
        """
        Provides operations to call the getUnhealthyFirewallReport method.
        """
        from .get_unhealthy_firewall_report.get_unhealthy_firewall_report_request_builder import GetUnhealthyFirewallReportRequestBuilder

        return GetUnhealthyFirewallReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_unhealthy_firewall_summary_report(self) -> GetUnhealthyFirewallSummaryReportRequestBuilder:
        """
        Provides operations to call the getUnhealthyFirewallSummaryReport method.
        """
        from .get_unhealthy_firewall_summary_report.get_unhealthy_firewall_summary_report_request_builder import GetUnhealthyFirewallSummaryReportRequestBuilder

        return GetUnhealthyFirewallSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_user_install_status_report(self) -> GetUserInstallStatusReportRequestBuilder:
        """
        Provides operations to call the getUserInstallStatusReport method.
        """
        from .get_user_install_status_report.get_user_install_status_report_request_builder import GetUserInstallStatusReportRequestBuilder

        return GetUserInstallStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_driver_update_alert_summary_report(self) -> GetWindowsDriverUpdateAlertSummaryReportRequestBuilder:
        """
        Provides operations to call the getWindowsDriverUpdateAlertSummaryReport method.
        """
        from .get_windows_driver_update_alert_summary_report.get_windows_driver_update_alert_summary_report_request_builder import GetWindowsDriverUpdateAlertSummaryReportRequestBuilder

        return GetWindowsDriverUpdateAlertSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_driver_update_alerts_per_policy_per_device_report(self) -> GetWindowsDriverUpdateAlertsPerPolicyPerDeviceReportRequestBuilder:
        """
        Provides operations to call the getWindowsDriverUpdateAlertsPerPolicyPerDeviceReport method.
        """
        from .get_windows_driver_update_alerts_per_policy_per_device_report.get_windows_driver_update_alerts_per_policy_per_device_report_request_builder import GetWindowsDriverUpdateAlertsPerPolicyPerDeviceReportRequestBuilder

        return GetWindowsDriverUpdateAlertsPerPolicyPerDeviceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_quality_update_alert_summary_report(self) -> GetWindowsQualityUpdateAlertSummaryReportRequestBuilder:
        """
        Provides operations to call the getWindowsQualityUpdateAlertSummaryReport method.
        """
        from .get_windows_quality_update_alert_summary_report.get_windows_quality_update_alert_summary_report_request_builder import GetWindowsQualityUpdateAlertSummaryReportRequestBuilder

        return GetWindowsQualityUpdateAlertSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_quality_update_alerts_per_policy_per_device_report(self) -> GetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequestBuilder:
        """
        Provides operations to call the getWindowsQualityUpdateAlertsPerPolicyPerDeviceReport method.
        """
        from .get_windows_quality_update_alerts_per_policy_per_device_report.get_windows_quality_update_alerts_per_policy_per_device_report_request_builder import GetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequestBuilder

        return GetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_update_alert_summary_report(self) -> GetWindowsUpdateAlertSummaryReportRequestBuilder:
        """
        Provides operations to call the getWindowsUpdateAlertSummaryReport method.
        """
        from .get_windows_update_alert_summary_report.get_windows_update_alert_summary_report_request_builder import GetWindowsUpdateAlertSummaryReportRequestBuilder

        return GetWindowsUpdateAlertSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_update_alerts_per_policy_per_device_report(self) -> GetWindowsUpdateAlertsPerPolicyPerDeviceReportRequestBuilder:
        """
        Provides operations to call the getWindowsUpdateAlertsPerPolicyPerDeviceReport method.
        """
        from .get_windows_update_alerts_per_policy_per_device_report.get_windows_update_alerts_per_policy_per_device_report_request_builder import GetWindowsUpdateAlertsPerPolicyPerDeviceReportRequestBuilder

        return GetWindowsUpdateAlertsPerPolicyPerDeviceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_zebra_fota_deployment_report(self) -> GetZebraFotaDeploymentReportRequestBuilder:
        """
        Provides operations to call the getZebraFotaDeploymentReport method.
        """
        from .get_zebra_fota_deployment_report.get_zebra_fota_deployment_report_request_builder import GetZebraFotaDeploymentReportRequestBuilder

        return GetZebraFotaDeploymentReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retrieve_assigned_applications_report(self) -> RetrieveAssignedApplicationsReportRequestBuilder:
        """
        Provides operations to call the retrieveAssignedApplicationsReport method.
        """
        from .retrieve_assigned_applications_report.retrieve_assigned_applications_report_request_builder import RetrieveAssignedApplicationsReportRequestBuilder

        return RetrieveAssignedApplicationsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retrieve_win32_catalog_apps_update_report(self) -> RetrieveWin32CatalogAppsUpdateReportRequestBuilder:
        """
        Provides operations to call the retrieveWin32CatalogAppsUpdateReport method.
        """
        from .retrieve_win32_catalog_apps_update_report.retrieve_win32_catalog_apps_update_report_request_builder import RetrieveWin32CatalogAppsUpdateReportRequestBuilder

        return RetrieveWin32CatalogAppsUpdateReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ReportsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Reports singleton
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
    class ReportsRequestBuilderGetRequestConfiguration(RequestConfiguration[ReportsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ReportsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

