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
    from ...models import device_management_reports
    from ...models.o_data_errors import o_data_error
    from .cached_report_configurations import cached_report_configurations_request_builder
    from .export_jobs import export_jobs_request_builder
    from .get_active_malware_report import get_active_malware_report_request_builder
    from .get_active_malware_summary_report import get_active_malware_summary_report_request_builder
    from .get_all_certificates_report import get_all_certificates_report_request_builder
    from .get_apps_install_summary_report import get_apps_install_summary_report_request_builder
    from .get_app_status_overview_report import get_app_status_overview_report_request_builder
    from .get_cached_report import get_cached_report_request_builder
    from .get_certificates_report import get_certificates_report_request_builder
    from .get_compliance_policies_report_for_device import get_compliance_policies_report_for_device_request_builder
    from .get_compliance_policy_devices_report import get_compliance_policy_devices_report_request_builder
    from .get_compliance_policy_device_summary_report import get_compliance_policy_device_summary_report_request_builder
    from .get_compliance_policy_non_compliance_report import get_compliance_policy_non_compliance_report_request_builder
    from .get_compliance_policy_non_compliance_summary_report import get_compliance_policy_non_compliance_summary_report_request_builder
    from .get_compliance_setting_details_report import get_compliance_setting_details_report_request_builder
    from .get_compliance_setting_non_compliance_report import get_compliance_setting_non_compliance_report_request_builder
    from .get_compliance_settings_report import get_compliance_settings_report_request_builder
    from .get_config_manager_device_policy_status_report import get_config_manager_device_policy_status_report_request_builder
    from .get_configuration_policies_report_for_device import get_configuration_policies_report_for_device_request_builder
    from .get_configuration_policy_devices_report import get_configuration_policy_devices_report_request_builder
    from .get_configuration_policy_device_summary_report import get_configuration_policy_device_summary_report_request_builder
    from .get_configuration_policy_non_compliance_report import get_configuration_policy_non_compliance_report_request_builder
    from .get_configuration_policy_non_compliance_summary_report import get_configuration_policy_non_compliance_summary_report_request_builder
    from .get_configuration_policy_settings_device_summary_report import get_configuration_policy_settings_device_summary_report_request_builder
    from .get_configuration_setting_details_report import get_configuration_setting_details_report_request_builder
    from .get_configuration_setting_non_compliance_report import get_configuration_setting_non_compliance_report_request_builder
    from .get_configuration_settings_report import get_configuration_settings_report_request_builder
    from .get_device_configuration_policy_settings_summary_report import get_device_configuration_policy_settings_summary_report_request_builder
    from .get_device_configuration_policy_status_summary import get_device_configuration_policy_status_summary_request_builder
    from .get_device_install_status_report import get_device_install_status_report_request_builder
    from .get_device_management_intent_per_setting_contributing_profiles import get_device_management_intent_per_setting_contributing_profiles_request_builder
    from .get_device_management_intent_settings_report import get_device_management_intent_settings_report_request_builder
    from .get_device_non_compliance_report import get_device_non_compliance_report_request_builder
    from .get_device_policies_compliance_report import get_device_policies_compliance_report_request_builder
    from .get_device_policy_settings_compliance_report import get_device_policy_settings_compliance_report_request_builder
    from .get_devices_status_by_policy_platform_compliance_report import get_devices_status_by_policy_platform_compliance_report_request_builder
    from .get_devices_status_by_setting_report import get_devices_status_by_setting_report_request_builder
    from .get_device_status_by_compliace_policy_report import get_device_status_by_compliace_policy_report_request_builder
    from .get_device_status_by_compliance_policy_setting_report import get_device_status_by_compliance_policy_setting_report_request_builder
    from .get_device_status_summary_by_compliace_policy_report import get_device_status_summary_by_compliace_policy_report_request_builder
    from .get_device_status_summary_by_compliance_policy_settings_report import get_device_status_summary_by_compliance_policy_settings_report_request_builder
    from .get_devices_without_compliance_policy_report import get_devices_without_compliance_policy_report_request_builder
    from .get_encryption_report_for_devices import get_encryption_report_for_devices_request_builder
    from .get_enrollment_configuration_policies_by_device import get_enrollment_configuration_policies_by_device_request_builder
    from .get_failed_mobile_apps_report import get_failed_mobile_apps_report_request_builder
    from .get_failed_mobile_apps_summary_report import get_failed_mobile_apps_summary_report_request_builder
    from .get_group_policy_settings_device_settings_report import get_group_policy_settings_device_settings_report_request_builder
    from .get_historical_report import get_historical_report_request_builder
    from .get_malware_summary_report import get_malware_summary_report_request_builder
    from .get_mobile_application_management_app_configuration_report import get_mobile_application_management_app_configuration_report_request_builder
    from .get_mobile_application_management_app_registration_summary_report import get_mobile_application_management_app_registration_summary_report_request_builder
    from .get_noncompliant_devices_and_settings_report import get_noncompliant_devices_and_settings_report_request_builder
    from .get_policy_non_compliance_metadata import get_policy_non_compliance_metadata_request_builder
    from .get_policy_non_compliance_report import get_policy_non_compliance_report_request_builder
    from .get_policy_non_compliance_summary_report import get_policy_non_compliance_summary_report_request_builder
    from .get_quiet_time_policy_users_report import get_quiet_time_policy_users_report_request_builder
    from .get_quiet_time_policy_user_summary_report import get_quiet_time_policy_user_summary_report_request_builder
    from .get_related_apps_status_report import get_related_apps_status_report_request_builder
    from .get_remote_assistance_sessions_report import get_remote_assistance_sessions_report_request_builder
    from .get_report_filters import get_report_filters_request_builder
    from .get_setting_non_compliance_report import get_setting_non_compliance_report_request_builder
    from .get_unhealthy_defender_agents_report import get_unhealthy_defender_agents_report_request_builder
    from .get_unhealthy_firewall_report import get_unhealthy_firewall_report_request_builder
    from .get_unhealthy_firewall_summary_report import get_unhealthy_firewall_summary_report_request_builder
    from .get_user_install_status_report import get_user_install_status_report_request_builder
    from .get_windows_quality_update_alerts_per_policy_per_device_report import get_windows_quality_update_alerts_per_policy_per_device_report_request_builder
    from .get_windows_quality_update_alert_summary_report import get_windows_quality_update_alert_summary_report_request_builder
    from .get_windows_update_alerts_per_policy_per_device_report import get_windows_update_alerts_per_policy_per_device_report_request_builder
    from .get_windows_update_alert_summary_report import get_windows_update_alert_summary_report_request_builder
    from .get_zebra_fota_deployment_report import get_zebra_fota_deployment_report_request_builder

class ReportsRequestBuilder():
    """
    Provides operations to manage the reports property of the microsoft.graph.deviceManagement entity.
    """
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
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
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
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import device_management_reports

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
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import device_management_reports

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
        request_info.headers["Accept"] = ["application/json"]
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def cached_report_configurations(self) -> cached_report_configurations_request_builder.CachedReportConfigurationsRequestBuilder:
        """
        Provides operations to manage the cachedReportConfigurations property of the microsoft.graph.deviceManagementReports entity.
        """
        from .cached_report_configurations import cached_report_configurations_request_builder

        return cached_report_configurations_request_builder.CachedReportConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def export_jobs(self) -> export_jobs_request_builder.ExportJobsRequestBuilder:
        """
        Provides operations to manage the exportJobs property of the microsoft.graph.deviceManagementReports entity.
        """
        from .export_jobs import export_jobs_request_builder

        return export_jobs_request_builder.ExportJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_active_malware_report(self) -> get_active_malware_report_request_builder.GetActiveMalwareReportRequestBuilder:
        """
        Provides operations to call the getActiveMalwareReport method.
        """
        from .get_active_malware_report import get_active_malware_report_request_builder

        return get_active_malware_report_request_builder.GetActiveMalwareReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_active_malware_summary_report(self) -> get_active_malware_summary_report_request_builder.GetActiveMalwareSummaryReportRequestBuilder:
        """
        Provides operations to call the getActiveMalwareSummaryReport method.
        """
        from .get_active_malware_summary_report import get_active_malware_summary_report_request_builder

        return get_active_malware_summary_report_request_builder.GetActiveMalwareSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_all_certificates_report(self) -> get_all_certificates_report_request_builder.GetAllCertificatesReportRequestBuilder:
        """
        Provides operations to call the getAllCertificatesReport method.
        """
        from .get_all_certificates_report import get_all_certificates_report_request_builder

        return get_all_certificates_report_request_builder.GetAllCertificatesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_apps_install_summary_report(self) -> get_apps_install_summary_report_request_builder.GetAppsInstallSummaryReportRequestBuilder:
        """
        Provides operations to call the getAppsInstallSummaryReport method.
        """
        from .get_apps_install_summary_report import get_apps_install_summary_report_request_builder

        return get_apps_install_summary_report_request_builder.GetAppsInstallSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_app_status_overview_report(self) -> get_app_status_overview_report_request_builder.GetAppStatusOverviewReportRequestBuilder:
        """
        Provides operations to call the getAppStatusOverviewReport method.
        """
        from .get_app_status_overview_report import get_app_status_overview_report_request_builder

        return get_app_status_overview_report_request_builder.GetAppStatusOverviewReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_cached_report(self) -> get_cached_report_request_builder.GetCachedReportRequestBuilder:
        """
        Provides operations to call the getCachedReport method.
        """
        from .get_cached_report import get_cached_report_request_builder

        return get_cached_report_request_builder.GetCachedReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_certificates_report(self) -> get_certificates_report_request_builder.GetCertificatesReportRequestBuilder:
        """
        Provides operations to call the getCertificatesReport method.
        """
        from .get_certificates_report import get_certificates_report_request_builder

        return get_certificates_report_request_builder.GetCertificatesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policies_report_for_device(self) -> get_compliance_policies_report_for_device_request_builder.GetCompliancePoliciesReportForDeviceRequestBuilder:
        """
        Provides operations to call the getCompliancePoliciesReportForDevice method.
        """
        from .get_compliance_policies_report_for_device import get_compliance_policies_report_for_device_request_builder

        return get_compliance_policies_report_for_device_request_builder.GetCompliancePoliciesReportForDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_devices_report(self) -> get_compliance_policy_devices_report_request_builder.GetCompliancePolicyDevicesReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyDevicesReport method.
        """
        from .get_compliance_policy_devices_report import get_compliance_policy_devices_report_request_builder

        return get_compliance_policy_devices_report_request_builder.GetCompliancePolicyDevicesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_device_summary_report(self) -> get_compliance_policy_device_summary_report_request_builder.GetCompliancePolicyDeviceSummaryReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyDeviceSummaryReport method.
        """
        from .get_compliance_policy_device_summary_report import get_compliance_policy_device_summary_report_request_builder

        return get_compliance_policy_device_summary_report_request_builder.GetCompliancePolicyDeviceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_non_compliance_report(self) -> get_compliance_policy_non_compliance_report_request_builder.GetCompliancePolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceReport method.
        """
        from .get_compliance_policy_non_compliance_report import get_compliance_policy_non_compliance_report_request_builder

        return get_compliance_policy_non_compliance_report_request_builder.GetCompliancePolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_non_compliance_summary_report(self) -> get_compliance_policy_non_compliance_summary_report_request_builder.GetCompliancePolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceSummaryReport method.
        """
        from .get_compliance_policy_non_compliance_summary_report import get_compliance_policy_non_compliance_summary_report_request_builder

        return get_compliance_policy_non_compliance_summary_report_request_builder.GetCompliancePolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_setting_details_report(self) -> get_compliance_setting_details_report_request_builder.GetComplianceSettingDetailsReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingDetailsReport method.
        """
        from .get_compliance_setting_details_report import get_compliance_setting_details_report_request_builder

        return get_compliance_setting_details_report_request_builder.GetComplianceSettingDetailsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_setting_non_compliance_report(self) -> get_compliance_setting_non_compliance_report_request_builder.GetComplianceSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingNonComplianceReport method.
        """
        from .get_compliance_setting_non_compliance_report import get_compliance_setting_non_compliance_report_request_builder

        return get_compliance_setting_non_compliance_report_request_builder.GetComplianceSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_settings_report(self) -> get_compliance_settings_report_request_builder.GetComplianceSettingsReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingsReport method.
        """
        from .get_compliance_settings_report import get_compliance_settings_report_request_builder

        return get_compliance_settings_report_request_builder.GetComplianceSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_config_manager_device_policy_status_report(self) -> get_config_manager_device_policy_status_report_request_builder.GetConfigManagerDevicePolicyStatusReportRequestBuilder:
        """
        Provides operations to call the getConfigManagerDevicePolicyStatusReport method.
        """
        from .get_config_manager_device_policy_status_report import get_config_manager_device_policy_status_report_request_builder

        return get_config_manager_device_policy_status_report_request_builder.GetConfigManagerDevicePolicyStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policies_report_for_device(self) -> get_configuration_policies_report_for_device_request_builder.GetConfigurationPoliciesReportForDeviceRequestBuilder:
        """
        Provides operations to call the getConfigurationPoliciesReportForDevice method.
        """
        from .get_configuration_policies_report_for_device import get_configuration_policies_report_for_device_request_builder

        return get_configuration_policies_report_for_device_request_builder.GetConfigurationPoliciesReportForDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_devices_report(self) -> get_configuration_policy_devices_report_request_builder.GetConfigurationPolicyDevicesReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyDevicesReport method.
        """
        from .get_configuration_policy_devices_report import get_configuration_policy_devices_report_request_builder

        return get_configuration_policy_devices_report_request_builder.GetConfigurationPolicyDevicesReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_device_summary_report(self) -> get_configuration_policy_device_summary_report_request_builder.GetConfigurationPolicyDeviceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyDeviceSummaryReport method.
        """
        from .get_configuration_policy_device_summary_report import get_configuration_policy_device_summary_report_request_builder

        return get_configuration_policy_device_summary_report_request_builder.GetConfigurationPolicyDeviceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_non_compliance_report(self) -> get_configuration_policy_non_compliance_report_request_builder.GetConfigurationPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceReport method.
        """
        from .get_configuration_policy_non_compliance_report import get_configuration_policy_non_compliance_report_request_builder

        return get_configuration_policy_non_compliance_report_request_builder.GetConfigurationPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_non_compliance_summary_report(self) -> get_configuration_policy_non_compliance_summary_report_request_builder.GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceSummaryReport method.
        """
        from .get_configuration_policy_non_compliance_summary_report import get_configuration_policy_non_compliance_summary_report_request_builder

        return get_configuration_policy_non_compliance_summary_report_request_builder.GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_settings_device_summary_report(self) -> get_configuration_policy_settings_device_summary_report_request_builder.GetConfigurationPolicySettingsDeviceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicySettingsDeviceSummaryReport method.
        """
        from .get_configuration_policy_settings_device_summary_report import get_configuration_policy_settings_device_summary_report_request_builder

        return get_configuration_policy_settings_device_summary_report_request_builder.GetConfigurationPolicySettingsDeviceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_setting_details_report(self) -> get_configuration_setting_details_report_request_builder.GetConfigurationSettingDetailsReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingDetailsReport method.
        """
        from .get_configuration_setting_details_report import get_configuration_setting_details_report_request_builder

        return get_configuration_setting_details_report_request_builder.GetConfigurationSettingDetailsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_setting_non_compliance_report(self) -> get_configuration_setting_non_compliance_report_request_builder.GetConfigurationSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingNonComplianceReport method.
        """
        from .get_configuration_setting_non_compliance_report import get_configuration_setting_non_compliance_report_request_builder

        return get_configuration_setting_non_compliance_report_request_builder.GetConfigurationSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_settings_report(self) -> get_configuration_settings_report_request_builder.GetConfigurationSettingsReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingsReport method.
        """
        from .get_configuration_settings_report import get_configuration_settings_report_request_builder

        return get_configuration_settings_report_request_builder.GetConfigurationSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_configuration_policy_settings_summary_report(self) -> get_device_configuration_policy_settings_summary_report_request_builder.GetDeviceConfigurationPolicySettingsSummaryReportRequestBuilder:
        """
        Provides operations to call the getDeviceConfigurationPolicySettingsSummaryReport method.
        """
        from .get_device_configuration_policy_settings_summary_report import get_device_configuration_policy_settings_summary_report_request_builder

        return get_device_configuration_policy_settings_summary_report_request_builder.GetDeviceConfigurationPolicySettingsSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_configuration_policy_status_summary(self) -> get_device_configuration_policy_status_summary_request_builder.GetDeviceConfigurationPolicyStatusSummaryRequestBuilder:
        """
        Provides operations to call the getDeviceConfigurationPolicyStatusSummary method.
        """
        from .get_device_configuration_policy_status_summary import get_device_configuration_policy_status_summary_request_builder

        return get_device_configuration_policy_status_summary_request_builder.GetDeviceConfigurationPolicyStatusSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_install_status_report(self) -> get_device_install_status_report_request_builder.GetDeviceInstallStatusReportRequestBuilder:
        """
        Provides operations to call the getDeviceInstallStatusReport method.
        """
        from .get_device_install_status_report import get_device_install_status_report_request_builder

        return get_device_install_status_report_request_builder.GetDeviceInstallStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_management_intent_per_setting_contributing_profiles(self) -> get_device_management_intent_per_setting_contributing_profiles_request_builder.GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentPerSettingContributingProfiles method.
        """
        from .get_device_management_intent_per_setting_contributing_profiles import get_device_management_intent_per_setting_contributing_profiles_request_builder

        return get_device_management_intent_per_setting_contributing_profiles_request_builder.GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_management_intent_settings_report(self) -> get_device_management_intent_settings_report_request_builder.GetDeviceManagementIntentSettingsReportRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentSettingsReport method.
        """
        from .get_device_management_intent_settings_report import get_device_management_intent_settings_report_request_builder

        return get_device_management_intent_settings_report_request_builder.GetDeviceManagementIntentSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_non_compliance_report(self) -> get_device_non_compliance_report_request_builder.GetDeviceNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getDeviceNonComplianceReport method.
        """
        from .get_device_non_compliance_report import get_device_non_compliance_report_request_builder

        return get_device_non_compliance_report_request_builder.GetDeviceNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_policies_compliance_report(self) -> get_device_policies_compliance_report_request_builder.GetDevicePoliciesComplianceReportRequestBuilder:
        """
        Provides operations to call the getDevicePoliciesComplianceReport method.
        """
        from .get_device_policies_compliance_report import get_device_policies_compliance_report_request_builder

        return get_device_policies_compliance_report_request_builder.GetDevicePoliciesComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_policy_settings_compliance_report(self) -> get_device_policy_settings_compliance_report_request_builder.GetDevicePolicySettingsComplianceReportRequestBuilder:
        """
        Provides operations to call the getDevicePolicySettingsComplianceReport method.
        """
        from .get_device_policy_settings_compliance_report import get_device_policy_settings_compliance_report_request_builder

        return get_device_policy_settings_compliance_report_request_builder.GetDevicePolicySettingsComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_devices_status_by_policy_platform_compliance_report(self) -> get_devices_status_by_policy_platform_compliance_report_request_builder.GetDevicesStatusByPolicyPlatformComplianceReportRequestBuilder:
        """
        Provides operations to call the getDevicesStatusByPolicyPlatformComplianceReport method.
        """
        from .get_devices_status_by_policy_platform_compliance_report import get_devices_status_by_policy_platform_compliance_report_request_builder

        return get_devices_status_by_policy_platform_compliance_report_request_builder.GetDevicesStatusByPolicyPlatformComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_devices_status_by_setting_report(self) -> get_devices_status_by_setting_report_request_builder.GetDevicesStatusBySettingReportRequestBuilder:
        """
        Provides operations to call the getDevicesStatusBySettingReport method.
        """
        from .get_devices_status_by_setting_report import get_devices_status_by_setting_report_request_builder

        return get_devices_status_by_setting_report_request_builder.GetDevicesStatusBySettingReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_status_by_compliace_policy_report(self) -> get_device_status_by_compliace_policy_report_request_builder.GetDeviceStatusByCompliacePolicyReportRequestBuilder:
        """
        Provides operations to call the getDeviceStatusByCompliacePolicyReport method.
        """
        from .get_device_status_by_compliace_policy_report import get_device_status_by_compliace_policy_report_request_builder

        return get_device_status_by_compliace_policy_report_request_builder.GetDeviceStatusByCompliacePolicyReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_status_by_compliance_policy_setting_report(self) -> get_device_status_by_compliance_policy_setting_report_request_builder.GetDeviceStatusByCompliancePolicySettingReportRequestBuilder:
        """
        Provides operations to call the getDeviceStatusByCompliancePolicySettingReport method.
        """
        from .get_device_status_by_compliance_policy_setting_report import get_device_status_by_compliance_policy_setting_report_request_builder

        return get_device_status_by_compliance_policy_setting_report_request_builder.GetDeviceStatusByCompliancePolicySettingReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_status_summary_by_compliace_policy_report(self) -> get_device_status_summary_by_compliace_policy_report_request_builder.GetDeviceStatusSummaryByCompliacePolicyReportRequestBuilder:
        """
        Provides operations to call the getDeviceStatusSummaryByCompliacePolicyReport method.
        """
        from .get_device_status_summary_by_compliace_policy_report import get_device_status_summary_by_compliace_policy_report_request_builder

        return get_device_status_summary_by_compliace_policy_report_request_builder.GetDeviceStatusSummaryByCompliacePolicyReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_status_summary_by_compliance_policy_settings_report(self) -> get_device_status_summary_by_compliance_policy_settings_report_request_builder.GetDeviceStatusSummaryByCompliancePolicySettingsReportRequestBuilder:
        """
        Provides operations to call the getDeviceStatusSummaryByCompliancePolicySettingsReport method.
        """
        from .get_device_status_summary_by_compliance_policy_settings_report import get_device_status_summary_by_compliance_policy_settings_report_request_builder

        return get_device_status_summary_by_compliance_policy_settings_report_request_builder.GetDeviceStatusSummaryByCompliancePolicySettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_devices_without_compliance_policy_report(self) -> get_devices_without_compliance_policy_report_request_builder.GetDevicesWithoutCompliancePolicyReportRequestBuilder:
        """
        Provides operations to call the getDevicesWithoutCompliancePolicyReport method.
        """
        from .get_devices_without_compliance_policy_report import get_devices_without_compliance_policy_report_request_builder

        return get_devices_without_compliance_policy_report_request_builder.GetDevicesWithoutCompliancePolicyReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_encryption_report_for_devices(self) -> get_encryption_report_for_devices_request_builder.GetEncryptionReportForDevicesRequestBuilder:
        """
        Provides operations to call the getEncryptionReportForDevices method.
        """
        from .get_encryption_report_for_devices import get_encryption_report_for_devices_request_builder

        return get_encryption_report_for_devices_request_builder.GetEncryptionReportForDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_enrollment_configuration_policies_by_device(self) -> get_enrollment_configuration_policies_by_device_request_builder.GetEnrollmentConfigurationPoliciesByDeviceRequestBuilder:
        """
        Provides operations to call the getEnrollmentConfigurationPoliciesByDevice method.
        """
        from .get_enrollment_configuration_policies_by_device import get_enrollment_configuration_policies_by_device_request_builder

        return get_enrollment_configuration_policies_by_device_request_builder.GetEnrollmentConfigurationPoliciesByDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_failed_mobile_apps_report(self) -> get_failed_mobile_apps_report_request_builder.GetFailedMobileAppsReportRequestBuilder:
        """
        Provides operations to call the getFailedMobileAppsReport method.
        """
        from .get_failed_mobile_apps_report import get_failed_mobile_apps_report_request_builder

        return get_failed_mobile_apps_report_request_builder.GetFailedMobileAppsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_failed_mobile_apps_summary_report(self) -> get_failed_mobile_apps_summary_report_request_builder.GetFailedMobileAppsSummaryReportRequestBuilder:
        """
        Provides operations to call the getFailedMobileAppsSummaryReport method.
        """
        from .get_failed_mobile_apps_summary_report import get_failed_mobile_apps_summary_report_request_builder

        return get_failed_mobile_apps_summary_report_request_builder.GetFailedMobileAppsSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_group_policy_settings_device_settings_report(self) -> get_group_policy_settings_device_settings_report_request_builder.GetGroupPolicySettingsDeviceSettingsReportRequestBuilder:
        """
        Provides operations to call the getGroupPolicySettingsDeviceSettingsReport method.
        """
        from .get_group_policy_settings_device_settings_report import get_group_policy_settings_device_settings_report_request_builder

        return get_group_policy_settings_device_settings_report_request_builder.GetGroupPolicySettingsDeviceSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_historical_report(self) -> get_historical_report_request_builder.GetHistoricalReportRequestBuilder:
        """
        Provides operations to call the getHistoricalReport method.
        """
        from .get_historical_report import get_historical_report_request_builder

        return get_historical_report_request_builder.GetHistoricalReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_malware_summary_report(self) -> get_malware_summary_report_request_builder.GetMalwareSummaryReportRequestBuilder:
        """
        Provides operations to call the getMalwareSummaryReport method.
        """
        from .get_malware_summary_report import get_malware_summary_report_request_builder

        return get_malware_summary_report_request_builder.GetMalwareSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_mobile_application_management_app_configuration_report(self) -> get_mobile_application_management_app_configuration_report_request_builder.GetMobileApplicationManagementAppConfigurationReportRequestBuilder:
        """
        Provides operations to call the getMobileApplicationManagementAppConfigurationReport method.
        """
        from .get_mobile_application_management_app_configuration_report import get_mobile_application_management_app_configuration_report_request_builder

        return get_mobile_application_management_app_configuration_report_request_builder.GetMobileApplicationManagementAppConfigurationReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_mobile_application_management_app_registration_summary_report(self) -> get_mobile_application_management_app_registration_summary_report_request_builder.GetMobileApplicationManagementAppRegistrationSummaryReportRequestBuilder:
        """
        Provides operations to call the getMobileApplicationManagementAppRegistrationSummaryReport method.
        """
        from .get_mobile_application_management_app_registration_summary_report import get_mobile_application_management_app_registration_summary_report_request_builder

        return get_mobile_application_management_app_registration_summary_report_request_builder.GetMobileApplicationManagementAppRegistrationSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_noncompliant_devices_and_settings_report(self) -> get_noncompliant_devices_and_settings_report_request_builder.GetNoncompliantDevicesAndSettingsReportRequestBuilder:
        """
        Provides operations to call the getNoncompliantDevicesAndSettingsReport method.
        """
        from .get_noncompliant_devices_and_settings_report import get_noncompliant_devices_and_settings_report_request_builder

        return get_noncompliant_devices_and_settings_report_request_builder.GetNoncompliantDevicesAndSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_metadata(self) -> get_policy_non_compliance_metadata_request_builder.GetPolicyNonComplianceMetadataRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceMetadata method.
        """
        from .get_policy_non_compliance_metadata import get_policy_non_compliance_metadata_request_builder

        return get_policy_non_compliance_metadata_request_builder.GetPolicyNonComplianceMetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_report(self) -> get_policy_non_compliance_report_request_builder.GetPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceReport method.
        """
        from .get_policy_non_compliance_report import get_policy_non_compliance_report_request_builder

        return get_policy_non_compliance_report_request_builder.GetPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_summary_report(self) -> get_policy_non_compliance_summary_report_request_builder.GetPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceSummaryReport method.
        """
        from .get_policy_non_compliance_summary_report import get_policy_non_compliance_summary_report_request_builder

        return get_policy_non_compliance_summary_report_request_builder.GetPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_quiet_time_policy_users_report(self) -> get_quiet_time_policy_users_report_request_builder.GetQuietTimePolicyUsersReportRequestBuilder:
        """
        Provides operations to call the getQuietTimePolicyUsersReport method.
        """
        from .get_quiet_time_policy_users_report import get_quiet_time_policy_users_report_request_builder

        return get_quiet_time_policy_users_report_request_builder.GetQuietTimePolicyUsersReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_quiet_time_policy_user_summary_report(self) -> get_quiet_time_policy_user_summary_report_request_builder.GetQuietTimePolicyUserSummaryReportRequestBuilder:
        """
        Provides operations to call the getQuietTimePolicyUserSummaryReport method.
        """
        from .get_quiet_time_policy_user_summary_report import get_quiet_time_policy_user_summary_report_request_builder

        return get_quiet_time_policy_user_summary_report_request_builder.GetQuietTimePolicyUserSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_related_apps_status_report(self) -> get_related_apps_status_report_request_builder.GetRelatedAppsStatusReportRequestBuilder:
        """
        Provides operations to call the getRelatedAppsStatusReport method.
        """
        from .get_related_apps_status_report import get_related_apps_status_report_request_builder

        return get_related_apps_status_report_request_builder.GetRelatedAppsStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_remote_assistance_sessions_report(self) -> get_remote_assistance_sessions_report_request_builder.GetRemoteAssistanceSessionsReportRequestBuilder:
        """
        Provides operations to call the getRemoteAssistanceSessionsReport method.
        """
        from .get_remote_assistance_sessions_report import get_remote_assistance_sessions_report_request_builder

        return get_remote_assistance_sessions_report_request_builder.GetRemoteAssistanceSessionsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_report_filters(self) -> get_report_filters_request_builder.GetReportFiltersRequestBuilder:
        """
        Provides operations to call the getReportFilters method.
        """
        from .get_report_filters import get_report_filters_request_builder

        return get_report_filters_request_builder.GetReportFiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_setting_non_compliance_report(self) -> get_setting_non_compliance_report_request_builder.GetSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getSettingNonComplianceReport method.
        """
        from .get_setting_non_compliance_report import get_setting_non_compliance_report_request_builder

        return get_setting_non_compliance_report_request_builder.GetSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_unhealthy_defender_agents_report(self) -> get_unhealthy_defender_agents_report_request_builder.GetUnhealthyDefenderAgentsReportRequestBuilder:
        """
        Provides operations to call the getUnhealthyDefenderAgentsReport method.
        """
        from .get_unhealthy_defender_agents_report import get_unhealthy_defender_agents_report_request_builder

        return get_unhealthy_defender_agents_report_request_builder.GetUnhealthyDefenderAgentsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_unhealthy_firewall_report(self) -> get_unhealthy_firewall_report_request_builder.GetUnhealthyFirewallReportRequestBuilder:
        """
        Provides operations to call the getUnhealthyFirewallReport method.
        """
        from .get_unhealthy_firewall_report import get_unhealthy_firewall_report_request_builder

        return get_unhealthy_firewall_report_request_builder.GetUnhealthyFirewallReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_unhealthy_firewall_summary_report(self) -> get_unhealthy_firewall_summary_report_request_builder.GetUnhealthyFirewallSummaryReportRequestBuilder:
        """
        Provides operations to call the getUnhealthyFirewallSummaryReport method.
        """
        from .get_unhealthy_firewall_summary_report import get_unhealthy_firewall_summary_report_request_builder

        return get_unhealthy_firewall_summary_report_request_builder.GetUnhealthyFirewallSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_user_install_status_report(self) -> get_user_install_status_report_request_builder.GetUserInstallStatusReportRequestBuilder:
        """
        Provides operations to call the getUserInstallStatusReport method.
        """
        from .get_user_install_status_report import get_user_install_status_report_request_builder

        return get_user_install_status_report_request_builder.GetUserInstallStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_quality_update_alerts_per_policy_per_device_report(self) -> get_windows_quality_update_alerts_per_policy_per_device_report_request_builder.GetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequestBuilder:
        """
        Provides operations to call the getWindowsQualityUpdateAlertsPerPolicyPerDeviceReport method.
        """
        from .get_windows_quality_update_alerts_per_policy_per_device_report import get_windows_quality_update_alerts_per_policy_per_device_report_request_builder

        return get_windows_quality_update_alerts_per_policy_per_device_report_request_builder.GetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_quality_update_alert_summary_report(self) -> get_windows_quality_update_alert_summary_report_request_builder.GetWindowsQualityUpdateAlertSummaryReportRequestBuilder:
        """
        Provides operations to call the getWindowsQualityUpdateAlertSummaryReport method.
        """
        from .get_windows_quality_update_alert_summary_report import get_windows_quality_update_alert_summary_report_request_builder

        return get_windows_quality_update_alert_summary_report_request_builder.GetWindowsQualityUpdateAlertSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_update_alerts_per_policy_per_device_report(self) -> get_windows_update_alerts_per_policy_per_device_report_request_builder.GetWindowsUpdateAlertsPerPolicyPerDeviceReportRequestBuilder:
        """
        Provides operations to call the getWindowsUpdateAlertsPerPolicyPerDeviceReport method.
        """
        from .get_windows_update_alerts_per_policy_per_device_report import get_windows_update_alerts_per_policy_per_device_report_request_builder

        return get_windows_update_alerts_per_policy_per_device_report_request_builder.GetWindowsUpdateAlertsPerPolicyPerDeviceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_windows_update_alert_summary_report(self) -> get_windows_update_alert_summary_report_request_builder.GetWindowsUpdateAlertSummaryReportRequestBuilder:
        """
        Provides operations to call the getWindowsUpdateAlertSummaryReport method.
        """
        from .get_windows_update_alert_summary_report import get_windows_update_alert_summary_report_request_builder

        return get_windows_update_alert_summary_report_request_builder.GetWindowsUpdateAlertSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_zebra_fota_deployment_report(self) -> get_zebra_fota_deployment_report_request_builder.GetZebraFotaDeploymentReportRequestBuilder:
        """
        Provides operations to call the getZebraFotaDeploymentReport method.
        """
        from .get_zebra_fota_deployment_report import get_zebra_fota_deployment_report_request_builder

        return get_zebra_fota_deployment_report_request_builder.GetZebraFotaDeploymentReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ReportsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Reports singleton
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
    class ReportsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

