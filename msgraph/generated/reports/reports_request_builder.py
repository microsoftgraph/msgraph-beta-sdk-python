from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models import report_root
    from ..models.o_data_errors import o_data_error
    from .application_sign_in_detailed_summary import application_sign_in_detailed_summary_request_builder
    from .authentication_methods import authentication_methods_request_builder
    from .credential_user_registration_details import credential_user_registration_details_request_builder
    from .daily_print_usage import daily_print_usage_request_builder
    from .daily_print_usage_by_printer import daily_print_usage_by_printer_request_builder
    from .daily_print_usage_by_user import daily_print_usage_by_user_request_builder
    from .daily_print_usage_summaries_by_printer import daily_print_usage_summaries_by_printer_request_builder
    from .daily_print_usage_summaries_by_user import daily_print_usage_summaries_by_user_request_builder
    from .device_configuration_device_activity import device_configuration_device_activity_request_builder
    from .device_configuration_user_activity import device_configuration_user_activity_request_builder
    from .get_attack_simulation_repeat_offenders import get_attack_simulation_repeat_offenders_request_builder
    from .get_attack_simulation_simulation_user_coverage import get_attack_simulation_simulation_user_coverage_request_builder
    from .get_attack_simulation_training_user_coverage import get_attack_simulation_training_user_coverage_request_builder
    from .get_azure_a_d_application_sign_in_summary_with_period import get_azure_a_d_application_sign_in_summary_with_period_request_builder
    from .get_browser_distribution_user_counts_with_period import get_browser_distribution_user_counts_with_period_request_builder
    from .get_browser_user_counts_with_period import get_browser_user_counts_with_period_request_builder
    from .get_browser_user_detail_with_period import get_browser_user_detail_with_period_request_builder
    from .get_credential_usage_summary_with_period import get_credential_usage_summary_with_period_request_builder
    from .get_credential_user_registration_count import get_credential_user_registration_count_request_builder
    from .get_email_activity_counts_with_period import get_email_activity_counts_with_period_request_builder
    from .get_email_activity_user_counts_with_period import get_email_activity_user_counts_with_period_request_builder
    from .get_email_activity_user_detail_with_date import get_email_activity_user_detail_with_date_request_builder
    from .get_email_activity_user_detail_with_period import get_email_activity_user_detail_with_period_request_builder
    from .get_email_app_usage_apps_user_counts_with_period import get_email_app_usage_apps_user_counts_with_period_request_builder
    from .get_email_app_usage_user_counts_with_period import get_email_app_usage_user_counts_with_period_request_builder
    from .get_email_app_usage_user_detail_with_date import get_email_app_usage_user_detail_with_date_request_builder
    from .get_email_app_usage_user_detail_with_period import get_email_app_usage_user_detail_with_period_request_builder
    from .get_email_app_usage_versions_user_counts_with_period import get_email_app_usage_versions_user_counts_with_period_request_builder
    from .get_forms_user_activity_counts_with_period import get_forms_user_activity_counts_with_period_request_builder
    from .get_forms_user_activity_user_counts_with_period import get_forms_user_activity_user_counts_with_period_request_builder
    from .get_forms_user_activity_user_detail_with_date import get_forms_user_activity_user_detail_with_date_request_builder
    from .get_forms_user_activity_user_detail_with_period import get_forms_user_activity_user_detail_with_period_request_builder
    from .get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time import get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time_request_builder
    from .get_m365_app_platform_user_counts_with_period import get_m365_app_platform_user_counts_with_period_request_builder
    from .get_m365_app_user_counts_with_period import get_m365_app_user_counts_with_period_request_builder
    from .get_m365_app_user_detail_with_date import get_m365_app_user_detail_with_date_request_builder
    from .get_m365_app_user_detail_with_period import get_m365_app_user_detail_with_period_request_builder
    from .get_mailbox_usage_detail_with_period import get_mailbox_usage_detail_with_period_request_builder
    from .get_mailbox_usage_mailbox_counts_with_period import get_mailbox_usage_mailbox_counts_with_period_request_builder
    from .get_mailbox_usage_quota_status_mailbox_counts_with_period import get_mailbox_usage_quota_status_mailbox_counts_with_period_request_builder
    from .get_mailbox_usage_storage_with_period import get_mailbox_usage_storage_with_period_request_builder
    from .get_office365_activation_counts import get_office365_activation_counts_request_builder
    from .get_office365_activations_user_counts import get_office365_activations_user_counts_request_builder
    from .get_office365_activations_user_detail import get_office365_activations_user_detail_request_builder
    from .get_office365_active_user_counts_with_period import get_office365_active_user_counts_with_period_request_builder
    from .get_office365_active_user_detail_with_date import get_office365_active_user_detail_with_date_request_builder
    from .get_office365_active_user_detail_with_period import get_office365_active_user_detail_with_period_request_builder
    from .get_office365_groups_activity_counts_with_period import get_office365_groups_activity_counts_with_period_request_builder
    from .get_office365_groups_activity_detail_with_date import get_office365_groups_activity_detail_with_date_request_builder
    from .get_office365_groups_activity_detail_with_period import get_office365_groups_activity_detail_with_period_request_builder
    from .get_office365_groups_activity_file_counts_with_period import get_office365_groups_activity_file_counts_with_period_request_builder
    from .get_office365_groups_activity_group_counts_with_period import get_office365_groups_activity_group_counts_with_period_request_builder
    from .get_office365_groups_activity_storage_with_period import get_office365_groups_activity_storage_with_period_request_builder
    from .get_office365_services_user_counts_with_period import get_office365_services_user_counts_with_period_request_builder
    from .get_one_drive_activity_file_counts_with_period import get_one_drive_activity_file_counts_with_period_request_builder
    from .get_one_drive_activity_user_counts_with_period import get_one_drive_activity_user_counts_with_period_request_builder
    from .get_one_drive_activity_user_detail_with_date import get_one_drive_activity_user_detail_with_date_request_builder
    from .get_one_drive_activity_user_detail_with_period import get_one_drive_activity_user_detail_with_period_request_builder
    from .get_one_drive_usage_account_counts_with_period import get_one_drive_usage_account_counts_with_period_request_builder
    from .get_one_drive_usage_account_detail_with_date import get_one_drive_usage_account_detail_with_date_request_builder
    from .get_one_drive_usage_account_detail_with_period import get_one_drive_usage_account_detail_with_period_request_builder
    from .get_one_drive_usage_file_counts_with_period import get_one_drive_usage_file_counts_with_period_request_builder
    from .get_one_drive_usage_storage_with_period import get_one_drive_usage_storage_with_period_request_builder
    from .get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time import get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time_request_builder
    from .get_relying_party_detailed_summary_with_period import get_relying_party_detailed_summary_with_period_request_builder
    from .get_share_point_activity_file_counts_with_period import get_share_point_activity_file_counts_with_period_request_builder
    from .get_share_point_activity_pages_with_period import get_share_point_activity_pages_with_period_request_builder
    from .get_share_point_activity_user_counts_with_period import get_share_point_activity_user_counts_with_period_request_builder
    from .get_share_point_activity_user_detail_with_date import get_share_point_activity_user_detail_with_date_request_builder
    from .get_share_point_activity_user_detail_with_period import get_share_point_activity_user_detail_with_period_request_builder
    from .get_share_point_site_usage_detail_with_date import get_share_point_site_usage_detail_with_date_request_builder
    from .get_share_point_site_usage_detail_with_period import get_share_point_site_usage_detail_with_period_request_builder
    from .get_share_point_site_usage_file_counts_with_period import get_share_point_site_usage_file_counts_with_period_request_builder
    from .get_share_point_site_usage_pages_with_period import get_share_point_site_usage_pages_with_period_request_builder
    from .get_share_point_site_usage_site_counts_with_period import get_share_point_site_usage_site_counts_with_period_request_builder
    from .get_share_point_site_usage_storage_with_period import get_share_point_site_usage_storage_with_period_request_builder
    from .get_skype_for_business_activity_counts_with_period import get_skype_for_business_activity_counts_with_period_request_builder
    from .get_skype_for_business_activity_user_counts_with_period import get_skype_for_business_activity_user_counts_with_period_request_builder
    from .get_skype_for_business_activity_user_detail_with_date import get_skype_for_business_activity_user_detail_with_date_request_builder
    from .get_skype_for_business_activity_user_detail_with_period import get_skype_for_business_activity_user_detail_with_period_request_builder
    from .get_skype_for_business_device_usage_distribution_user_counts_with_period import get_skype_for_business_device_usage_distribution_user_counts_with_period_request_builder
    from .get_skype_for_business_device_usage_user_counts_with_period import get_skype_for_business_device_usage_user_counts_with_period_request_builder
    from .get_skype_for_business_device_usage_user_detail_with_date import get_skype_for_business_device_usage_user_detail_with_date_request_builder
    from .get_skype_for_business_device_usage_user_detail_with_period import get_skype_for_business_device_usage_user_detail_with_period_request_builder
    from .get_skype_for_business_organizer_activity_counts_with_period import get_skype_for_business_organizer_activity_counts_with_period_request_builder
    from .get_skype_for_business_organizer_activity_minute_counts_with_period import get_skype_for_business_organizer_activity_minute_counts_with_period_request_builder
    from .get_skype_for_business_organizer_activity_user_counts_with_period import get_skype_for_business_organizer_activity_user_counts_with_period_request_builder
    from .get_skype_for_business_participant_activity_counts_with_period import get_skype_for_business_participant_activity_counts_with_period_request_builder
    from .get_skype_for_business_participant_activity_minute_counts_with_period import get_skype_for_business_participant_activity_minute_counts_with_period_request_builder
    from .get_skype_for_business_participant_activity_user_counts_with_period import get_skype_for_business_participant_activity_user_counts_with_period_request_builder
    from .get_skype_for_business_peer_to_peer_activity_counts_with_period import get_skype_for_business_peer_to_peer_activity_counts_with_period_request_builder
    from .get_skype_for_business_peer_to_peer_activity_minute_counts_with_period import get_skype_for_business_peer_to_peer_activity_minute_counts_with_period_request_builder
    from .get_skype_for_business_peer_to_peer_activity_user_counts_with_period import get_skype_for_business_peer_to_peer_activity_user_counts_with_period_request_builder
    from .get_teams_device_usage_distribution_total_user_counts_with_period import get_teams_device_usage_distribution_total_user_counts_with_period_request_builder
    from .get_teams_device_usage_distribution_user_counts_with_period import get_teams_device_usage_distribution_user_counts_with_period_request_builder
    from .get_teams_device_usage_total_user_counts_with_period import get_teams_device_usage_total_user_counts_with_period_request_builder
    from .get_teams_device_usage_user_counts_with_period import get_teams_device_usage_user_counts_with_period_request_builder
    from .get_teams_device_usage_user_detail_with_date import get_teams_device_usage_user_detail_with_date_request_builder
    from .get_teams_device_usage_user_detail_with_period import get_teams_device_usage_user_detail_with_period_request_builder
    from .get_teams_team_activity_counts_with_period import get_teams_team_activity_counts_with_period_request_builder
    from .get_teams_team_activity_detail_with_date import get_teams_team_activity_detail_with_date_request_builder
    from .get_teams_team_activity_detail_with_period import get_teams_team_activity_detail_with_period_request_builder
    from .get_teams_team_activity_distribution_counts_with_period import get_teams_team_activity_distribution_counts_with_period_request_builder
    from .get_teams_team_counts_with_period import get_teams_team_counts_with_period_request_builder
    from .get_teams_user_activity_counts_with_period import get_teams_user_activity_counts_with_period_request_builder
    from .get_teams_user_activity_distribution_total_user_counts_with_period import get_teams_user_activity_distribution_total_user_counts_with_period_request_builder
    from .get_teams_user_activity_distribution_user_counts_with_period import get_teams_user_activity_distribution_user_counts_with_period_request_builder
    from .get_teams_user_activity_total_counts_with_period import get_teams_user_activity_total_counts_with_period_request_builder
    from .get_teams_user_activity_total_distribution_counts_with_period import get_teams_user_activity_total_distribution_counts_with_period_request_builder
    from .get_teams_user_activity_total_user_counts_with_period import get_teams_user_activity_total_user_counts_with_period_request_builder
    from .get_teams_user_activity_user_counts_with_period import get_teams_user_activity_user_counts_with_period_request_builder
    from .get_teams_user_activity_user_detail_with_date import get_teams_user_activity_user_detail_with_date_request_builder
    from .get_teams_user_activity_user_detail_with_period import get_teams_user_activity_user_detail_with_period_request_builder
    from .get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time import get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time_request_builder
    from .get_yammer_activity_counts_with_period import get_yammer_activity_counts_with_period_request_builder
    from .get_yammer_activity_user_counts_with_period import get_yammer_activity_user_counts_with_period_request_builder
    from .get_yammer_activity_user_detail_with_date import get_yammer_activity_user_detail_with_date_request_builder
    from .get_yammer_activity_user_detail_with_period import get_yammer_activity_user_detail_with_period_request_builder
    from .get_yammer_device_usage_distribution_user_counts_with_period import get_yammer_device_usage_distribution_user_counts_with_period_request_builder
    from .get_yammer_device_usage_user_counts_with_period import get_yammer_device_usage_user_counts_with_period_request_builder
    from .get_yammer_device_usage_user_detail_with_date import get_yammer_device_usage_user_detail_with_date_request_builder
    from .get_yammer_device_usage_user_detail_with_period import get_yammer_device_usage_user_detail_with_period_request_builder
    from .get_yammer_groups_activity_counts_with_period import get_yammer_groups_activity_counts_with_period_request_builder
    from .get_yammer_groups_activity_detail_with_date import get_yammer_groups_activity_detail_with_date_request_builder
    from .get_yammer_groups_activity_detail_with_period import get_yammer_groups_activity_detail_with_period_request_builder
    from .get_yammer_groups_activity_group_counts_with_period import get_yammer_groups_activity_group_counts_with_period_request_builder
    from .managed_device_enrollment_abandonment_details_with_skip_with_top_with_filter_with_skip_token import managed_device_enrollment_abandonment_details_with_skip_with_top_with_filter_with_skip_token_request_builder
    from .managed_device_enrollment_abandonment_summary_with_skip_with_top_with_filter_with_skip_token import managed_device_enrollment_abandonment_summary_with_skip_with_top_with_filter_with_skip_token_request_builder
    from .managed_device_enrollment_failure_details import managed_device_enrollment_failure_details_request_builder
    from .managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token import managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token_request_builder
    from .managed_device_enrollment_failure_trends import managed_device_enrollment_failure_trends_request_builder
    from .managed_device_enrollment_top_failures import managed_device_enrollment_top_failures_request_builder
    from .managed_device_enrollment_top_failures_with_period import managed_device_enrollment_top_failures_with_period_request_builder
    from .monthly_print_usage_by_printer import monthly_print_usage_by_printer_request_builder
    from .monthly_print_usage_by_user import monthly_print_usage_by_user_request_builder
    from .monthly_print_usage_summaries_by_printer import monthly_print_usage_summaries_by_printer_request_builder
    from .monthly_print_usage_summaries_by_user import monthly_print_usage_summaries_by_user_request_builder
    from .security import security_request_builder
    from .user_credential_usage_details import user_credential_usage_details_request_builder

class ReportsRequestBuilder():
    """
    Provides operations to manage the reportRoot singleton.
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
        self.url_template: str = "{+baseurl}/reports{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> Optional[report_root.ReportRoot]:
        """
        Get reports
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[report_root.ReportRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import report_root

        return await self.request_adapter.send_async(request_info, report_root.ReportRoot, error_mapping)
    
    def get_azure_a_d_application_sign_in_summary_with_period(self,period: Optional[str] = None) -> get_azure_a_d_application_sign_in_summary_with_period_request_builder.GetAzureADApplicationSignInSummaryWithPeriodRequestBuilder:
        """
        Provides operations to call the getAzureADApplicationSignInSummary method.
        Args:
            period: Usage: period='{period}'
        Returns: get_azure_a_d_application_sign_in_summary_with_period_request_builder.GetAzureADApplicationSignInSummaryWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_azure_a_d_application_sign_in_summary_with_period import get_azure_a_d_application_sign_in_summary_with_period_request_builder

        return get_azure_a_d_application_sign_in_summary_with_period_request_builder.GetAzureADApplicationSignInSummaryWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_browser_distribution_user_counts_with_period(self,period: Optional[str] = None) -> get_browser_distribution_user_counts_with_period_request_builder.GetBrowserDistributionUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getBrowserDistributionUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_browser_distribution_user_counts_with_period_request_builder.GetBrowserDistributionUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_browser_distribution_user_counts_with_period import get_browser_distribution_user_counts_with_period_request_builder

        return get_browser_distribution_user_counts_with_period_request_builder.GetBrowserDistributionUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_browser_user_counts_with_period(self,period: Optional[str] = None) -> get_browser_user_counts_with_period_request_builder.GetBrowserUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getBrowserUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_browser_user_counts_with_period_request_builder.GetBrowserUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_browser_user_counts_with_period import get_browser_user_counts_with_period_request_builder

        return get_browser_user_counts_with_period_request_builder.GetBrowserUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_browser_user_detail_with_period(self,period: Optional[str] = None) -> get_browser_user_detail_with_period_request_builder.GetBrowserUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getBrowserUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_browser_user_detail_with_period_request_builder.GetBrowserUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_browser_user_detail_with_period import get_browser_user_detail_with_period_request_builder

        return get_browser_user_detail_with_period_request_builder.GetBrowserUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_credential_usage_summary_with_period(self,period: Optional[str] = None) -> get_credential_usage_summary_with_period_request_builder.GetCredentialUsageSummaryWithPeriodRequestBuilder:
        """
        Provides operations to call the getCredentialUsageSummary method.
        Args:
            period: Usage: period='{period}'
        Returns: get_credential_usage_summary_with_period_request_builder.GetCredentialUsageSummaryWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_credential_usage_summary_with_period import get_credential_usage_summary_with_period_request_builder

        return get_credential_usage_summary_with_period_request_builder.GetCredentialUsageSummaryWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_activity_counts_with_period(self,period: Optional[str] = None) -> get_email_activity_counts_with_period_request_builder.GetEmailActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_email_activity_counts_with_period_request_builder.GetEmailActivityCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_email_activity_counts_with_period import get_email_activity_counts_with_period_request_builder

        return get_email_activity_counts_with_period_request_builder.GetEmailActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_activity_user_counts_with_period(self,period: Optional[str] = None) -> get_email_activity_user_counts_with_period_request_builder.GetEmailActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_email_activity_user_counts_with_period_request_builder.GetEmailActivityUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_email_activity_user_counts_with_period import get_email_activity_user_counts_with_period_request_builder

        return get_email_activity_user_counts_with_period_request_builder.GetEmailActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_activity_user_detail_with_date(self,date: Optional[date] = None) -> get_email_activity_user_detail_with_date_request_builder.GetEmailActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getEmailActivityUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_email_activity_user_detail_with_date_request_builder.GetEmailActivityUserDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_email_activity_user_detail_with_date import get_email_activity_user_detail_with_date_request_builder

        return get_email_activity_user_detail_with_date_request_builder.GetEmailActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_email_activity_user_detail_with_period(self,period: Optional[str] = None) -> get_email_activity_user_detail_with_period_request_builder.GetEmailActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailActivityUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_email_activity_user_detail_with_period_request_builder.GetEmailActivityUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_email_activity_user_detail_with_period import get_email_activity_user_detail_with_period_request_builder

        return get_email_activity_user_detail_with_period_request_builder.GetEmailActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_app_usage_apps_user_counts_with_period(self,period: Optional[str] = None) -> get_email_app_usage_apps_user_counts_with_period_request_builder.GetEmailAppUsageAppsUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageAppsUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_email_app_usage_apps_user_counts_with_period_request_builder.GetEmailAppUsageAppsUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_email_app_usage_apps_user_counts_with_period import get_email_app_usage_apps_user_counts_with_period_request_builder

        return get_email_app_usage_apps_user_counts_with_period_request_builder.GetEmailAppUsageAppsUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_app_usage_user_counts_with_period(self,period: Optional[str] = None) -> get_email_app_usage_user_counts_with_period_request_builder.GetEmailAppUsageUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_email_app_usage_user_counts_with_period_request_builder.GetEmailAppUsageUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_email_app_usage_user_counts_with_period import get_email_app_usage_user_counts_with_period_request_builder

        return get_email_app_usage_user_counts_with_period_request_builder.GetEmailAppUsageUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_app_usage_user_detail_with_date(self,date: Optional[date] = None) -> get_email_app_usage_user_detail_with_date_request_builder.GetEmailAppUsageUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_email_app_usage_user_detail_with_date_request_builder.GetEmailAppUsageUserDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_email_app_usage_user_detail_with_date import get_email_app_usage_user_detail_with_date_request_builder

        return get_email_app_usage_user_detail_with_date_request_builder.GetEmailAppUsageUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_email_app_usage_user_detail_with_period(self,period: Optional[str] = None) -> get_email_app_usage_user_detail_with_period_request_builder.GetEmailAppUsageUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_email_app_usage_user_detail_with_period_request_builder.GetEmailAppUsageUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_email_app_usage_user_detail_with_period import get_email_app_usage_user_detail_with_period_request_builder

        return get_email_app_usage_user_detail_with_period_request_builder.GetEmailAppUsageUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_app_usage_versions_user_counts_with_period(self,period: Optional[str] = None) -> get_email_app_usage_versions_user_counts_with_period_request_builder.GetEmailAppUsageVersionsUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageVersionsUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_email_app_usage_versions_user_counts_with_period_request_builder.GetEmailAppUsageVersionsUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_email_app_usage_versions_user_counts_with_period import get_email_app_usage_versions_user_counts_with_period_request_builder

        return get_email_app_usage_versions_user_counts_with_period_request_builder.GetEmailAppUsageVersionsUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_forms_user_activity_counts_with_period(self,period: Optional[str] = None) -> get_forms_user_activity_counts_with_period_request_builder.GetFormsUserActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getFormsUserActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_forms_user_activity_counts_with_period_request_builder.GetFormsUserActivityCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_forms_user_activity_counts_with_period import get_forms_user_activity_counts_with_period_request_builder

        return get_forms_user_activity_counts_with_period_request_builder.GetFormsUserActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_forms_user_activity_user_counts_with_period(self,period: Optional[str] = None) -> get_forms_user_activity_user_counts_with_period_request_builder.GetFormsUserActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getFormsUserActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_forms_user_activity_user_counts_with_period_request_builder.GetFormsUserActivityUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_forms_user_activity_user_counts_with_period import get_forms_user_activity_user_counts_with_period_request_builder

        return get_forms_user_activity_user_counts_with_period_request_builder.GetFormsUserActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_forms_user_activity_user_detail_with_date(self,date: Optional[date] = None) -> get_forms_user_activity_user_detail_with_date_request_builder.GetFormsUserActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getFormsUserActivityUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_forms_user_activity_user_detail_with_date_request_builder.GetFormsUserActivityUserDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_forms_user_activity_user_detail_with_date import get_forms_user_activity_user_detail_with_date_request_builder

        return get_forms_user_activity_user_detail_with_date_request_builder.GetFormsUserActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_forms_user_activity_user_detail_with_period(self,period: Optional[str] = None) -> get_forms_user_activity_user_detail_with_period_request_builder.GetFormsUserActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getFormsUserActivityUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_forms_user_activity_user_detail_with_period_request_builder.GetFormsUserActivityUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_forms_user_activity_user_detail_with_period import get_forms_user_activity_user_detail_with_period_request_builder

        return get_forms_user_activity_user_detail_with_period_request_builder.GetFormsUserActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time(self,end_date_time: Optional[datetime] = None, group_id: Optional[str] = None, start_date_time: Optional[datetime] = None) -> get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time_request_builder.GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the getGroupArchivedPrintJobs method.
        Args:
            endDateTime: Usage: endDateTime={endDateTime}
            groupId: Usage: groupId='{groupId}'
            startDateTime: Usage: startDateTime={startDateTime}
        Returns: get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time_request_builder.GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if end_date_time is None:
            raise Exception("end_date_time cannot be undefined")
        if group_id is None:
            raise Exception("group_id cannot be undefined")
        if start_date_time is None:
            raise Exception("start_date_time cannot be undefined")
        from .get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time import get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time_request_builder

        return get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time_request_builder.GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, group_id, start_date_time)
    
    def get_m365_app_platform_user_counts_with_period(self,period: Optional[str] = None) -> get_m365_app_platform_user_counts_with_period_request_builder.GetM365AppPlatformUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getM365AppPlatformUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_m365_app_platform_user_counts_with_period_request_builder.GetM365AppPlatformUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_m365_app_platform_user_counts_with_period import get_m365_app_platform_user_counts_with_period_request_builder

        return get_m365_app_platform_user_counts_with_period_request_builder.GetM365AppPlatformUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_m365_app_user_counts_with_period(self,period: Optional[str] = None) -> get_m365_app_user_counts_with_period_request_builder.GetM365AppUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getM365AppUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_m365_app_user_counts_with_period_request_builder.GetM365AppUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_m365_app_user_counts_with_period import get_m365_app_user_counts_with_period_request_builder

        return get_m365_app_user_counts_with_period_request_builder.GetM365AppUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_m365_app_user_detail_with_date(self,date: Optional[date] = None) -> get_m365_app_user_detail_with_date_request_builder.GetM365AppUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getM365AppUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_m365_app_user_detail_with_date_request_builder.GetM365AppUserDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_m365_app_user_detail_with_date import get_m365_app_user_detail_with_date_request_builder

        return get_m365_app_user_detail_with_date_request_builder.GetM365AppUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_m365_app_user_detail_with_period(self,period: Optional[str] = None) -> get_m365_app_user_detail_with_period_request_builder.GetM365AppUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getM365AppUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_m365_app_user_detail_with_period_request_builder.GetM365AppUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_m365_app_user_detail_with_period import get_m365_app_user_detail_with_period_request_builder

        return get_m365_app_user_detail_with_period_request_builder.GetM365AppUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_mailbox_usage_detail_with_period(self,period: Optional[str] = None) -> get_mailbox_usage_detail_with_period_request_builder.GetMailboxUsageDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getMailboxUsageDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_mailbox_usage_detail_with_period_request_builder.GetMailboxUsageDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_mailbox_usage_detail_with_period import get_mailbox_usage_detail_with_period_request_builder

        return get_mailbox_usage_detail_with_period_request_builder.GetMailboxUsageDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_mailbox_usage_mailbox_counts_with_period(self,period: Optional[str] = None) -> get_mailbox_usage_mailbox_counts_with_period_request_builder.GetMailboxUsageMailboxCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getMailboxUsageMailboxCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_mailbox_usage_mailbox_counts_with_period_request_builder.GetMailboxUsageMailboxCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_mailbox_usage_mailbox_counts_with_period import get_mailbox_usage_mailbox_counts_with_period_request_builder

        return get_mailbox_usage_mailbox_counts_with_period_request_builder.GetMailboxUsageMailboxCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_mailbox_usage_quota_status_mailbox_counts_with_period(self,period: Optional[str] = None) -> get_mailbox_usage_quota_status_mailbox_counts_with_period_request_builder.GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getMailboxUsageQuotaStatusMailboxCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_mailbox_usage_quota_status_mailbox_counts_with_period_request_builder.GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_mailbox_usage_quota_status_mailbox_counts_with_period import get_mailbox_usage_quota_status_mailbox_counts_with_period_request_builder

        return get_mailbox_usage_quota_status_mailbox_counts_with_period_request_builder.GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_mailbox_usage_storage_with_period(self,period: Optional[str] = None) -> get_mailbox_usage_storage_with_period_request_builder.GetMailboxUsageStorageWithPeriodRequestBuilder:
        """
        Provides operations to call the getMailboxUsageStorage method.
        Args:
            period: Usage: period='{period}'
        Returns: get_mailbox_usage_storage_with_period_request_builder.GetMailboxUsageStorageWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_mailbox_usage_storage_with_period import get_mailbox_usage_storage_with_period_request_builder

        return get_mailbox_usage_storage_with_period_request_builder.GetMailboxUsageStorageWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_active_user_counts_with_period(self,period: Optional[str] = None) -> get_office365_active_user_counts_with_period_request_builder.GetOffice365ActiveUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365ActiveUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_office365_active_user_counts_with_period_request_builder.GetOffice365ActiveUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_office365_active_user_counts_with_period import get_office365_active_user_counts_with_period_request_builder

        return get_office365_active_user_counts_with_period_request_builder.GetOffice365ActiveUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_active_user_detail_with_date(self,date: Optional[date] = None) -> get_office365_active_user_detail_with_date_request_builder.GetOffice365ActiveUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getOffice365ActiveUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_office365_active_user_detail_with_date_request_builder.GetOffice365ActiveUserDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_office365_active_user_detail_with_date import get_office365_active_user_detail_with_date_request_builder

        return get_office365_active_user_detail_with_date_request_builder.GetOffice365ActiveUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_office365_active_user_detail_with_period(self,period: Optional[str] = None) -> get_office365_active_user_detail_with_period_request_builder.GetOffice365ActiveUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365ActiveUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_office365_active_user_detail_with_period_request_builder.GetOffice365ActiveUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_office365_active_user_detail_with_period import get_office365_active_user_detail_with_period_request_builder

        return get_office365_active_user_detail_with_period_request_builder.GetOffice365ActiveUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_counts_with_period(self,period: Optional[str] = None) -> get_office365_groups_activity_counts_with_period_request_builder.GetOffice365GroupsActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_office365_groups_activity_counts_with_period_request_builder.GetOffice365GroupsActivityCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_office365_groups_activity_counts_with_period import get_office365_groups_activity_counts_with_period_request_builder

        return get_office365_groups_activity_counts_with_period_request_builder.GetOffice365GroupsActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_detail_with_date(self,date: Optional[date] = None) -> get_office365_groups_activity_detail_with_date_request_builder.GetOffice365GroupsActivityDetailWithDateRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_office365_groups_activity_detail_with_date_request_builder.GetOffice365GroupsActivityDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_office365_groups_activity_detail_with_date import get_office365_groups_activity_detail_with_date_request_builder

        return get_office365_groups_activity_detail_with_date_request_builder.GetOffice365GroupsActivityDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_office365_groups_activity_detail_with_period(self,period: Optional[str] = None) -> get_office365_groups_activity_detail_with_period_request_builder.GetOffice365GroupsActivityDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_office365_groups_activity_detail_with_period_request_builder.GetOffice365GroupsActivityDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_office365_groups_activity_detail_with_period import get_office365_groups_activity_detail_with_period_request_builder

        return get_office365_groups_activity_detail_with_period_request_builder.GetOffice365GroupsActivityDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_file_counts_with_period(self,period: Optional[str] = None) -> get_office365_groups_activity_file_counts_with_period_request_builder.GetOffice365GroupsActivityFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityFileCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_office365_groups_activity_file_counts_with_period_request_builder.GetOffice365GroupsActivityFileCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_office365_groups_activity_file_counts_with_period import get_office365_groups_activity_file_counts_with_period_request_builder

        return get_office365_groups_activity_file_counts_with_period_request_builder.GetOffice365GroupsActivityFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_group_counts_with_period(self,period: Optional[str] = None) -> get_office365_groups_activity_group_counts_with_period_request_builder.GetOffice365GroupsActivityGroupCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityGroupCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_office365_groups_activity_group_counts_with_period_request_builder.GetOffice365GroupsActivityGroupCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_office365_groups_activity_group_counts_with_period import get_office365_groups_activity_group_counts_with_period_request_builder

        return get_office365_groups_activity_group_counts_with_period_request_builder.GetOffice365GroupsActivityGroupCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_storage_with_period(self,period: Optional[str] = None) -> get_office365_groups_activity_storage_with_period_request_builder.GetOffice365GroupsActivityStorageWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityStorage method.
        Args:
            period: Usage: period='{period}'
        Returns: get_office365_groups_activity_storage_with_period_request_builder.GetOffice365GroupsActivityStorageWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_office365_groups_activity_storage_with_period import get_office365_groups_activity_storage_with_period_request_builder

        return get_office365_groups_activity_storage_with_period_request_builder.GetOffice365GroupsActivityStorageWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_services_user_counts_with_period(self,period: Optional[str] = None) -> get_office365_services_user_counts_with_period_request_builder.GetOffice365ServicesUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365ServicesUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_office365_services_user_counts_with_period_request_builder.GetOffice365ServicesUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_office365_services_user_counts_with_period import get_office365_services_user_counts_with_period_request_builder

        return get_office365_services_user_counts_with_period_request_builder.GetOffice365ServicesUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_activity_file_counts_with_period(self,period: Optional[str] = None) -> get_one_drive_activity_file_counts_with_period_request_builder.GetOneDriveActivityFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveActivityFileCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_one_drive_activity_file_counts_with_period_request_builder.GetOneDriveActivityFileCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_one_drive_activity_file_counts_with_period import get_one_drive_activity_file_counts_with_period_request_builder

        return get_one_drive_activity_file_counts_with_period_request_builder.GetOneDriveActivityFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_activity_user_counts_with_period(self,period: Optional[str] = None) -> get_one_drive_activity_user_counts_with_period_request_builder.GetOneDriveActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_one_drive_activity_user_counts_with_period_request_builder.GetOneDriveActivityUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_one_drive_activity_user_counts_with_period import get_one_drive_activity_user_counts_with_period_request_builder

        return get_one_drive_activity_user_counts_with_period_request_builder.GetOneDriveActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_activity_user_detail_with_date(self,date: Optional[date] = None) -> get_one_drive_activity_user_detail_with_date_request_builder.GetOneDriveActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getOneDriveActivityUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_one_drive_activity_user_detail_with_date_request_builder.GetOneDriveActivityUserDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_one_drive_activity_user_detail_with_date import get_one_drive_activity_user_detail_with_date_request_builder

        return get_one_drive_activity_user_detail_with_date_request_builder.GetOneDriveActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_one_drive_activity_user_detail_with_period(self,period: Optional[str] = None) -> get_one_drive_activity_user_detail_with_period_request_builder.GetOneDriveActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveActivityUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_one_drive_activity_user_detail_with_period_request_builder.GetOneDriveActivityUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_one_drive_activity_user_detail_with_period import get_one_drive_activity_user_detail_with_period_request_builder

        return get_one_drive_activity_user_detail_with_period_request_builder.GetOneDriveActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_usage_account_counts_with_period(self,period: Optional[str] = None) -> get_one_drive_usage_account_counts_with_period_request_builder.GetOneDriveUsageAccountCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageAccountCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_one_drive_usage_account_counts_with_period_request_builder.GetOneDriveUsageAccountCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_one_drive_usage_account_counts_with_period import get_one_drive_usage_account_counts_with_period_request_builder

        return get_one_drive_usage_account_counts_with_period_request_builder.GetOneDriveUsageAccountCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_usage_account_detail_with_date(self,date: Optional[date] = None) -> get_one_drive_usage_account_detail_with_date_request_builder.GetOneDriveUsageAccountDetailWithDateRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageAccountDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_one_drive_usage_account_detail_with_date_request_builder.GetOneDriveUsageAccountDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_one_drive_usage_account_detail_with_date import get_one_drive_usage_account_detail_with_date_request_builder

        return get_one_drive_usage_account_detail_with_date_request_builder.GetOneDriveUsageAccountDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_one_drive_usage_account_detail_with_period(self,period: Optional[str] = None) -> get_one_drive_usage_account_detail_with_period_request_builder.GetOneDriveUsageAccountDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageAccountDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_one_drive_usage_account_detail_with_period_request_builder.GetOneDriveUsageAccountDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_one_drive_usage_account_detail_with_period import get_one_drive_usage_account_detail_with_period_request_builder

        return get_one_drive_usage_account_detail_with_period_request_builder.GetOneDriveUsageAccountDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_usage_file_counts_with_period(self,period: Optional[str] = None) -> get_one_drive_usage_file_counts_with_period_request_builder.GetOneDriveUsageFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageFileCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_one_drive_usage_file_counts_with_period_request_builder.GetOneDriveUsageFileCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_one_drive_usage_file_counts_with_period import get_one_drive_usage_file_counts_with_period_request_builder

        return get_one_drive_usage_file_counts_with_period_request_builder.GetOneDriveUsageFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_usage_storage_with_period(self,period: Optional[str] = None) -> get_one_drive_usage_storage_with_period_request_builder.GetOneDriveUsageStorageWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageStorage method.
        Args:
            period: Usage: period='{period}'
        Returns: get_one_drive_usage_storage_with_period_request_builder.GetOneDriveUsageStorageWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_one_drive_usage_storage_with_period import get_one_drive_usage_storage_with_period_request_builder

        return get_one_drive_usage_storage_with_period_request_builder.GetOneDriveUsageStorageWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time(self,end_date_time: Optional[datetime] = None, printer_id: Optional[str] = None, start_date_time: Optional[datetime] = None) -> get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time_request_builder.GetPrinterArchivedPrintJobsWithPrinterIdWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the getPrinterArchivedPrintJobs method.
        Args:
            endDateTime: Usage: endDateTime={endDateTime}
            printerId: Usage: printerId='{printerId}'
            startDateTime: Usage: startDateTime={startDateTime}
        Returns: get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time_request_builder.GetPrinterArchivedPrintJobsWithPrinterIdWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if end_date_time is None:
            raise Exception("end_date_time cannot be undefined")
        if printer_id is None:
            raise Exception("printer_id cannot be undefined")
        if start_date_time is None:
            raise Exception("start_date_time cannot be undefined")
        from .get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time import get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time_request_builder

        return get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time_request_builder.GetPrinterArchivedPrintJobsWithPrinterIdWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, printer_id, start_date_time)
    
    def get_relying_party_detailed_summary_with_period(self,period: Optional[str] = None) -> get_relying_party_detailed_summary_with_period_request_builder.GetRelyingPartyDetailedSummaryWithPeriodRequestBuilder:
        """
        Provides operations to call the getRelyingPartyDetailedSummary method.
        Args:
            period: Usage: period='{period}'
        Returns: get_relying_party_detailed_summary_with_period_request_builder.GetRelyingPartyDetailedSummaryWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_relying_party_detailed_summary_with_period import get_relying_party_detailed_summary_with_period_request_builder

        return get_relying_party_detailed_summary_with_period_request_builder.GetRelyingPartyDetailedSummaryWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_activity_file_counts_with_period(self,period: Optional[str] = None) -> get_share_point_activity_file_counts_with_period_request_builder.GetSharePointActivityFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointActivityFileCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_share_point_activity_file_counts_with_period_request_builder.GetSharePointActivityFileCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_share_point_activity_file_counts_with_period import get_share_point_activity_file_counts_with_period_request_builder

        return get_share_point_activity_file_counts_with_period_request_builder.GetSharePointActivityFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_activity_pages_with_period(self,period: Optional[str] = None) -> get_share_point_activity_pages_with_period_request_builder.GetSharePointActivityPagesWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointActivityPages method.
        Args:
            period: Usage: period='{period}'
        Returns: get_share_point_activity_pages_with_period_request_builder.GetSharePointActivityPagesWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_share_point_activity_pages_with_period import get_share_point_activity_pages_with_period_request_builder

        return get_share_point_activity_pages_with_period_request_builder.GetSharePointActivityPagesWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_activity_user_counts_with_period(self,period: Optional[str] = None) -> get_share_point_activity_user_counts_with_period_request_builder.GetSharePointActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_share_point_activity_user_counts_with_period_request_builder.GetSharePointActivityUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_share_point_activity_user_counts_with_period import get_share_point_activity_user_counts_with_period_request_builder

        return get_share_point_activity_user_counts_with_period_request_builder.GetSharePointActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_activity_user_detail_with_date(self,date: Optional[date] = None) -> get_share_point_activity_user_detail_with_date_request_builder.GetSharePointActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getSharePointActivityUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_share_point_activity_user_detail_with_date_request_builder.GetSharePointActivityUserDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_share_point_activity_user_detail_with_date import get_share_point_activity_user_detail_with_date_request_builder

        return get_share_point_activity_user_detail_with_date_request_builder.GetSharePointActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_share_point_activity_user_detail_with_period(self,period: Optional[str] = None) -> get_share_point_activity_user_detail_with_period_request_builder.GetSharePointActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointActivityUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_share_point_activity_user_detail_with_period_request_builder.GetSharePointActivityUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_share_point_activity_user_detail_with_period import get_share_point_activity_user_detail_with_period_request_builder

        return get_share_point_activity_user_detail_with_period_request_builder.GetSharePointActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_detail_with_date(self,date: Optional[date] = None) -> get_share_point_site_usage_detail_with_date_request_builder.GetSharePointSiteUsageDetailWithDateRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_share_point_site_usage_detail_with_date_request_builder.GetSharePointSiteUsageDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_share_point_site_usage_detail_with_date import get_share_point_site_usage_detail_with_date_request_builder

        return get_share_point_site_usage_detail_with_date_request_builder.GetSharePointSiteUsageDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_share_point_site_usage_detail_with_period(self,period: Optional[str] = None) -> get_share_point_site_usage_detail_with_period_request_builder.GetSharePointSiteUsageDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_share_point_site_usage_detail_with_period_request_builder.GetSharePointSiteUsageDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_share_point_site_usage_detail_with_period import get_share_point_site_usage_detail_with_period_request_builder

        return get_share_point_site_usage_detail_with_period_request_builder.GetSharePointSiteUsageDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_file_counts_with_period(self,period: Optional[str] = None) -> get_share_point_site_usage_file_counts_with_period_request_builder.GetSharePointSiteUsageFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageFileCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_share_point_site_usage_file_counts_with_period_request_builder.GetSharePointSiteUsageFileCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_share_point_site_usage_file_counts_with_period import get_share_point_site_usage_file_counts_with_period_request_builder

        return get_share_point_site_usage_file_counts_with_period_request_builder.GetSharePointSiteUsageFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_pages_with_period(self,period: Optional[str] = None) -> get_share_point_site_usage_pages_with_period_request_builder.GetSharePointSiteUsagePagesWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsagePages method.
        Args:
            period: Usage: period='{period}'
        Returns: get_share_point_site_usage_pages_with_period_request_builder.GetSharePointSiteUsagePagesWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_share_point_site_usage_pages_with_period import get_share_point_site_usage_pages_with_period_request_builder

        return get_share_point_site_usage_pages_with_period_request_builder.GetSharePointSiteUsagePagesWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_site_counts_with_period(self,period: Optional[str] = None) -> get_share_point_site_usage_site_counts_with_period_request_builder.GetSharePointSiteUsageSiteCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageSiteCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_share_point_site_usage_site_counts_with_period_request_builder.GetSharePointSiteUsageSiteCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_share_point_site_usage_site_counts_with_period import get_share_point_site_usage_site_counts_with_period_request_builder

        return get_share_point_site_usage_site_counts_with_period_request_builder.GetSharePointSiteUsageSiteCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_storage_with_period(self,period: Optional[str] = None) -> get_share_point_site_usage_storage_with_period_request_builder.GetSharePointSiteUsageStorageWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageStorage method.
        Args:
            period: Usage: period='{period}'
        Returns: get_share_point_site_usage_storage_with_period_request_builder.GetSharePointSiteUsageStorageWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_share_point_site_usage_storage_with_period import get_share_point_site_usage_storage_with_period_request_builder

        return get_share_point_site_usage_storage_with_period_request_builder.GetSharePointSiteUsageStorageWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_activity_counts_with_period(self,period: Optional[str] = None) -> get_skype_for_business_activity_counts_with_period_request_builder.GetSkypeForBusinessActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_activity_counts_with_period_request_builder.GetSkypeForBusinessActivityCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_activity_counts_with_period import get_skype_for_business_activity_counts_with_period_request_builder

        return get_skype_for_business_activity_counts_with_period_request_builder.GetSkypeForBusinessActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_activity_user_counts_with_period(self,period: Optional[str] = None) -> get_skype_for_business_activity_user_counts_with_period_request_builder.GetSkypeForBusinessActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_activity_user_counts_with_period_request_builder.GetSkypeForBusinessActivityUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_activity_user_counts_with_period import get_skype_for_business_activity_user_counts_with_period_request_builder

        return get_skype_for_business_activity_user_counts_with_period_request_builder.GetSkypeForBusinessActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_activity_user_detail_with_date(self,date: Optional[date] = None) -> get_skype_for_business_activity_user_detail_with_date_request_builder.GetSkypeForBusinessActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessActivityUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_skype_for_business_activity_user_detail_with_date_request_builder.GetSkypeForBusinessActivityUserDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_skype_for_business_activity_user_detail_with_date import get_skype_for_business_activity_user_detail_with_date_request_builder

        return get_skype_for_business_activity_user_detail_with_date_request_builder.GetSkypeForBusinessActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_skype_for_business_activity_user_detail_with_period(self,period: Optional[str] = None) -> get_skype_for_business_activity_user_detail_with_period_request_builder.GetSkypeForBusinessActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessActivityUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_activity_user_detail_with_period_request_builder.GetSkypeForBusinessActivityUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_activity_user_detail_with_period import get_skype_for_business_activity_user_detail_with_period_request_builder

        return get_skype_for_business_activity_user_detail_with_period_request_builder.GetSkypeForBusinessActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_device_usage_distribution_user_counts_with_period(self,period: Optional[str] = None) -> get_skype_for_business_device_usage_distribution_user_counts_with_period_request_builder.GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessDeviceUsageDistributionUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_device_usage_distribution_user_counts_with_period_request_builder.GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_device_usage_distribution_user_counts_with_period import get_skype_for_business_device_usage_distribution_user_counts_with_period_request_builder

        return get_skype_for_business_device_usage_distribution_user_counts_with_period_request_builder.GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_device_usage_user_counts_with_period(self,period: Optional[str] = None) -> get_skype_for_business_device_usage_user_counts_with_period_request_builder.GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessDeviceUsageUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_device_usage_user_counts_with_period_request_builder.GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_device_usage_user_counts_with_period import get_skype_for_business_device_usage_user_counts_with_period_request_builder

        return get_skype_for_business_device_usage_user_counts_with_period_request_builder.GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_device_usage_user_detail_with_date(self,date: Optional[date] = None) -> get_skype_for_business_device_usage_user_detail_with_date_request_builder.GetSkypeForBusinessDeviceUsageUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessDeviceUsageUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_skype_for_business_device_usage_user_detail_with_date_request_builder.GetSkypeForBusinessDeviceUsageUserDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_skype_for_business_device_usage_user_detail_with_date import get_skype_for_business_device_usage_user_detail_with_date_request_builder

        return get_skype_for_business_device_usage_user_detail_with_date_request_builder.GetSkypeForBusinessDeviceUsageUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_skype_for_business_device_usage_user_detail_with_period(self,period: Optional[str] = None) -> get_skype_for_business_device_usage_user_detail_with_period_request_builder.GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessDeviceUsageUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_device_usage_user_detail_with_period_request_builder.GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_device_usage_user_detail_with_period import get_skype_for_business_device_usage_user_detail_with_period_request_builder

        return get_skype_for_business_device_usage_user_detail_with_period_request_builder.GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_organizer_activity_counts_with_period(self,period: Optional[str] = None) -> get_skype_for_business_organizer_activity_counts_with_period_request_builder.GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessOrganizerActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_organizer_activity_counts_with_period_request_builder.GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_organizer_activity_counts_with_period import get_skype_for_business_organizer_activity_counts_with_period_request_builder

        return get_skype_for_business_organizer_activity_counts_with_period_request_builder.GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_organizer_activity_minute_counts_with_period(self,period: Optional[str] = None) -> get_skype_for_business_organizer_activity_minute_counts_with_period_request_builder.GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessOrganizerActivityMinuteCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_organizer_activity_minute_counts_with_period_request_builder.GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_organizer_activity_minute_counts_with_period import get_skype_for_business_organizer_activity_minute_counts_with_period_request_builder

        return get_skype_for_business_organizer_activity_minute_counts_with_period_request_builder.GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_organizer_activity_user_counts_with_period(self,period: Optional[str] = None) -> get_skype_for_business_organizer_activity_user_counts_with_period_request_builder.GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessOrganizerActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_organizer_activity_user_counts_with_period_request_builder.GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_organizer_activity_user_counts_with_period import get_skype_for_business_organizer_activity_user_counts_with_period_request_builder

        return get_skype_for_business_organizer_activity_user_counts_with_period_request_builder.GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_participant_activity_counts_with_period(self,period: Optional[str] = None) -> get_skype_for_business_participant_activity_counts_with_period_request_builder.GetSkypeForBusinessParticipantActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessParticipantActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_participant_activity_counts_with_period_request_builder.GetSkypeForBusinessParticipantActivityCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_participant_activity_counts_with_period import get_skype_for_business_participant_activity_counts_with_period_request_builder

        return get_skype_for_business_participant_activity_counts_with_period_request_builder.GetSkypeForBusinessParticipantActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_participant_activity_minute_counts_with_period(self,period: Optional[str] = None) -> get_skype_for_business_participant_activity_minute_counts_with_period_request_builder.GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessParticipantActivityMinuteCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_participant_activity_minute_counts_with_period_request_builder.GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_participant_activity_minute_counts_with_period import get_skype_for_business_participant_activity_minute_counts_with_period_request_builder

        return get_skype_for_business_participant_activity_minute_counts_with_period_request_builder.GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_participant_activity_user_counts_with_period(self,period: Optional[str] = None) -> get_skype_for_business_participant_activity_user_counts_with_period_request_builder.GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessParticipantActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_participant_activity_user_counts_with_period_request_builder.GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_participant_activity_user_counts_with_period import get_skype_for_business_participant_activity_user_counts_with_period_request_builder

        return get_skype_for_business_participant_activity_user_counts_with_period_request_builder.GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_peer_to_peer_activity_counts_with_period(self,period: Optional[str] = None) -> get_skype_for_business_peer_to_peer_activity_counts_with_period_request_builder.GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessPeerToPeerActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_peer_to_peer_activity_counts_with_period_request_builder.GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_peer_to_peer_activity_counts_with_period import get_skype_for_business_peer_to_peer_activity_counts_with_period_request_builder

        return get_skype_for_business_peer_to_peer_activity_counts_with_period_request_builder.GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_peer_to_peer_activity_minute_counts_with_period(self,period: Optional[str] = None) -> get_skype_for_business_peer_to_peer_activity_minute_counts_with_period_request_builder.GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessPeerToPeerActivityMinuteCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_peer_to_peer_activity_minute_counts_with_period_request_builder.GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_peer_to_peer_activity_minute_counts_with_period import get_skype_for_business_peer_to_peer_activity_minute_counts_with_period_request_builder

        return get_skype_for_business_peer_to_peer_activity_minute_counts_with_period_request_builder.GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_peer_to_peer_activity_user_counts_with_period(self,period: Optional[str] = None) -> get_skype_for_business_peer_to_peer_activity_user_counts_with_period_request_builder.GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessPeerToPeerActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_skype_for_business_peer_to_peer_activity_user_counts_with_period_request_builder.GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_skype_for_business_peer_to_peer_activity_user_counts_with_period import get_skype_for_business_peer_to_peer_activity_user_counts_with_period_request_builder

        return get_skype_for_business_peer_to_peer_activity_user_counts_with_period_request_builder.GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_device_usage_distribution_total_user_counts_with_period(self,period: Optional[str] = None) -> get_teams_device_usage_distribution_total_user_counts_with_period_request_builder.GetTeamsDeviceUsageDistributionTotalUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageDistributionTotalUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_device_usage_distribution_total_user_counts_with_period_request_builder.GetTeamsDeviceUsageDistributionTotalUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_device_usage_distribution_total_user_counts_with_period import get_teams_device_usage_distribution_total_user_counts_with_period_request_builder

        return get_teams_device_usage_distribution_total_user_counts_with_period_request_builder.GetTeamsDeviceUsageDistributionTotalUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_device_usage_distribution_user_counts_with_period(self,period: Optional[str] = None) -> get_teams_device_usage_distribution_user_counts_with_period_request_builder.GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageDistributionUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_device_usage_distribution_user_counts_with_period_request_builder.GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_device_usage_distribution_user_counts_with_period import get_teams_device_usage_distribution_user_counts_with_period_request_builder

        return get_teams_device_usage_distribution_user_counts_with_period_request_builder.GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_device_usage_total_user_counts_with_period(self,period: Optional[str] = None) -> get_teams_device_usage_total_user_counts_with_period_request_builder.GetTeamsDeviceUsageTotalUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageTotalUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_device_usage_total_user_counts_with_period_request_builder.GetTeamsDeviceUsageTotalUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_device_usage_total_user_counts_with_period import get_teams_device_usage_total_user_counts_with_period_request_builder

        return get_teams_device_usage_total_user_counts_with_period_request_builder.GetTeamsDeviceUsageTotalUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_device_usage_user_counts_with_period(self,period: Optional[str] = None) -> get_teams_device_usage_user_counts_with_period_request_builder.GetTeamsDeviceUsageUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_device_usage_user_counts_with_period_request_builder.GetTeamsDeviceUsageUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_device_usage_user_counts_with_period import get_teams_device_usage_user_counts_with_period_request_builder

        return get_teams_device_usage_user_counts_with_period_request_builder.GetTeamsDeviceUsageUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_device_usage_user_detail_with_date(self,date: Optional[date] = None) -> get_teams_device_usage_user_detail_with_date_request_builder.GetTeamsDeviceUsageUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_teams_device_usage_user_detail_with_date_request_builder.GetTeamsDeviceUsageUserDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_teams_device_usage_user_detail_with_date import get_teams_device_usage_user_detail_with_date_request_builder

        return get_teams_device_usage_user_detail_with_date_request_builder.GetTeamsDeviceUsageUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_teams_device_usage_user_detail_with_period(self,period: Optional[str] = None) -> get_teams_device_usage_user_detail_with_period_request_builder.GetTeamsDeviceUsageUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_device_usage_user_detail_with_period_request_builder.GetTeamsDeviceUsageUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_device_usage_user_detail_with_period import get_teams_device_usage_user_detail_with_period_request_builder

        return get_teams_device_usage_user_detail_with_period_request_builder.GetTeamsDeviceUsageUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_team_activity_counts_with_period(self,period: Optional[str] = None) -> get_teams_team_activity_counts_with_period_request_builder.GetTeamsTeamActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsTeamActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_team_activity_counts_with_period_request_builder.GetTeamsTeamActivityCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_team_activity_counts_with_period import get_teams_team_activity_counts_with_period_request_builder

        return get_teams_team_activity_counts_with_period_request_builder.GetTeamsTeamActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_team_activity_detail_with_date(self,date: Optional[date] = None) -> get_teams_team_activity_detail_with_date_request_builder.GetTeamsTeamActivityDetailWithDateRequestBuilder:
        """
        Provides operations to call the getTeamsTeamActivityDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_teams_team_activity_detail_with_date_request_builder.GetTeamsTeamActivityDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_teams_team_activity_detail_with_date import get_teams_team_activity_detail_with_date_request_builder

        return get_teams_team_activity_detail_with_date_request_builder.GetTeamsTeamActivityDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_teams_team_activity_detail_with_period(self,period: Optional[str] = None) -> get_teams_team_activity_detail_with_period_request_builder.GetTeamsTeamActivityDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsTeamActivityDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_team_activity_detail_with_period_request_builder.GetTeamsTeamActivityDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_team_activity_detail_with_period import get_teams_team_activity_detail_with_period_request_builder

        return get_teams_team_activity_detail_with_period_request_builder.GetTeamsTeamActivityDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_team_activity_distribution_counts_with_period(self,period: Optional[str] = None) -> get_teams_team_activity_distribution_counts_with_period_request_builder.GetTeamsTeamActivityDistributionCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsTeamActivityDistributionCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_team_activity_distribution_counts_with_period_request_builder.GetTeamsTeamActivityDistributionCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_team_activity_distribution_counts_with_period import get_teams_team_activity_distribution_counts_with_period_request_builder

        return get_teams_team_activity_distribution_counts_with_period_request_builder.GetTeamsTeamActivityDistributionCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_team_counts_with_period(self,period: Optional[str] = None) -> get_teams_team_counts_with_period_request_builder.GetTeamsTeamCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsTeamCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_team_counts_with_period_request_builder.GetTeamsTeamCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_team_counts_with_period import get_teams_team_counts_with_period_request_builder

        return get_teams_team_counts_with_period_request_builder.GetTeamsTeamCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_counts_with_period(self,period: Optional[str] = None) -> get_teams_user_activity_counts_with_period_request_builder.GetTeamsUserActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_user_activity_counts_with_period_request_builder.GetTeamsUserActivityCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_user_activity_counts_with_period import get_teams_user_activity_counts_with_period_request_builder

        return get_teams_user_activity_counts_with_period_request_builder.GetTeamsUserActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_distribution_total_user_counts_with_period(self,period: Optional[str] = None) -> get_teams_user_activity_distribution_total_user_counts_with_period_request_builder.GetTeamsUserActivityDistributionTotalUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityDistributionTotalUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_user_activity_distribution_total_user_counts_with_period_request_builder.GetTeamsUserActivityDistributionTotalUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_user_activity_distribution_total_user_counts_with_period import get_teams_user_activity_distribution_total_user_counts_with_period_request_builder

        return get_teams_user_activity_distribution_total_user_counts_with_period_request_builder.GetTeamsUserActivityDistributionTotalUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_distribution_user_counts_with_period(self,period: Optional[str] = None) -> get_teams_user_activity_distribution_user_counts_with_period_request_builder.GetTeamsUserActivityDistributionUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityDistributionUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_user_activity_distribution_user_counts_with_period_request_builder.GetTeamsUserActivityDistributionUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_user_activity_distribution_user_counts_with_period import get_teams_user_activity_distribution_user_counts_with_period_request_builder

        return get_teams_user_activity_distribution_user_counts_with_period_request_builder.GetTeamsUserActivityDistributionUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_total_counts_with_period(self,period: Optional[str] = None) -> get_teams_user_activity_total_counts_with_period_request_builder.GetTeamsUserActivityTotalCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityTotalCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_user_activity_total_counts_with_period_request_builder.GetTeamsUserActivityTotalCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_user_activity_total_counts_with_period import get_teams_user_activity_total_counts_with_period_request_builder

        return get_teams_user_activity_total_counts_with_period_request_builder.GetTeamsUserActivityTotalCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_total_distribution_counts_with_period(self,period: Optional[str] = None) -> get_teams_user_activity_total_distribution_counts_with_period_request_builder.GetTeamsUserActivityTotalDistributionCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityTotalDistributionCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_user_activity_total_distribution_counts_with_period_request_builder.GetTeamsUserActivityTotalDistributionCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_user_activity_total_distribution_counts_with_period import get_teams_user_activity_total_distribution_counts_with_period_request_builder

        return get_teams_user_activity_total_distribution_counts_with_period_request_builder.GetTeamsUserActivityTotalDistributionCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_total_user_counts_with_period(self,period: Optional[str] = None) -> get_teams_user_activity_total_user_counts_with_period_request_builder.GetTeamsUserActivityTotalUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityTotalUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_user_activity_total_user_counts_with_period_request_builder.GetTeamsUserActivityTotalUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_user_activity_total_user_counts_with_period import get_teams_user_activity_total_user_counts_with_period_request_builder

        return get_teams_user_activity_total_user_counts_with_period_request_builder.GetTeamsUserActivityTotalUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_user_counts_with_period(self,period: Optional[str] = None) -> get_teams_user_activity_user_counts_with_period_request_builder.GetTeamsUserActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_user_activity_user_counts_with_period_request_builder.GetTeamsUserActivityUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_user_activity_user_counts_with_period import get_teams_user_activity_user_counts_with_period_request_builder

        return get_teams_user_activity_user_counts_with_period_request_builder.GetTeamsUserActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_user_detail_with_date(self,date: Optional[date] = None) -> get_teams_user_activity_user_detail_with_date_request_builder.GetTeamsUserActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_teams_user_activity_user_detail_with_date_request_builder.GetTeamsUserActivityUserDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_teams_user_activity_user_detail_with_date import get_teams_user_activity_user_detail_with_date_request_builder

        return get_teams_user_activity_user_detail_with_date_request_builder.GetTeamsUserActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_teams_user_activity_user_detail_with_period(self,period: Optional[str] = None) -> get_teams_user_activity_user_detail_with_period_request_builder.GetTeamsUserActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_teams_user_activity_user_detail_with_period_request_builder.GetTeamsUserActivityUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_teams_user_activity_user_detail_with_period import get_teams_user_activity_user_detail_with_period_request_builder

        return get_teams_user_activity_user_detail_with_period_request_builder.GetTeamsUserActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time(self,end_date_time: Optional[datetime] = None, start_date_time: Optional[datetime] = None, user_id: Optional[str] = None) -> get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time_request_builder.GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the getUserArchivedPrintJobs method.
        Args:
            endDateTime: Usage: endDateTime={endDateTime}
            startDateTime: Usage: startDateTime={startDateTime}
            userId: Usage: userId='{userId}'
        Returns: get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time_request_builder.GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if end_date_time is None:
            raise Exception("end_date_time cannot be undefined")
        if start_date_time is None:
            raise Exception("start_date_time cannot be undefined")
        if user_id is None:
            raise Exception("user_id cannot be undefined")
        from .get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time import get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time_request_builder

        return get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time_request_builder.GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time, user_id)
    
    def get_yammer_activity_counts_with_period(self,period: Optional[str] = None) -> get_yammer_activity_counts_with_period_request_builder.GetYammerActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_yammer_activity_counts_with_period_request_builder.GetYammerActivityCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_yammer_activity_counts_with_period import get_yammer_activity_counts_with_period_request_builder

        return get_yammer_activity_counts_with_period_request_builder.GetYammerActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_activity_user_counts_with_period(self,period: Optional[str] = None) -> get_yammer_activity_user_counts_with_period_request_builder.GetYammerActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_yammer_activity_user_counts_with_period_request_builder.GetYammerActivityUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_yammer_activity_user_counts_with_period import get_yammer_activity_user_counts_with_period_request_builder

        return get_yammer_activity_user_counts_with_period_request_builder.GetYammerActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_activity_user_detail_with_date(self,date: Optional[date] = None) -> get_yammer_activity_user_detail_with_date_request_builder.GetYammerActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getYammerActivityUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_yammer_activity_user_detail_with_date_request_builder.GetYammerActivityUserDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_yammer_activity_user_detail_with_date import get_yammer_activity_user_detail_with_date_request_builder

        return get_yammer_activity_user_detail_with_date_request_builder.GetYammerActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_yammer_activity_user_detail_with_period(self,period: Optional[str] = None) -> get_yammer_activity_user_detail_with_period_request_builder.GetYammerActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerActivityUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_yammer_activity_user_detail_with_period_request_builder.GetYammerActivityUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_yammer_activity_user_detail_with_period import get_yammer_activity_user_detail_with_period_request_builder

        return get_yammer_activity_user_detail_with_period_request_builder.GetYammerActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_device_usage_distribution_user_counts_with_period(self,period: Optional[str] = None) -> get_yammer_device_usage_distribution_user_counts_with_period_request_builder.GetYammerDeviceUsageDistributionUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerDeviceUsageDistributionUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_yammer_device_usage_distribution_user_counts_with_period_request_builder.GetYammerDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_yammer_device_usage_distribution_user_counts_with_period import get_yammer_device_usage_distribution_user_counts_with_period_request_builder

        return get_yammer_device_usage_distribution_user_counts_with_period_request_builder.GetYammerDeviceUsageDistributionUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_device_usage_user_counts_with_period(self,period: Optional[str] = None) -> get_yammer_device_usage_user_counts_with_period_request_builder.GetYammerDeviceUsageUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerDeviceUsageUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_yammer_device_usage_user_counts_with_period_request_builder.GetYammerDeviceUsageUserCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_yammer_device_usage_user_counts_with_period import get_yammer_device_usage_user_counts_with_period_request_builder

        return get_yammer_device_usage_user_counts_with_period_request_builder.GetYammerDeviceUsageUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_device_usage_user_detail_with_date(self,date: Optional[date] = None) -> get_yammer_device_usage_user_detail_with_date_request_builder.GetYammerDeviceUsageUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getYammerDeviceUsageUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_yammer_device_usage_user_detail_with_date_request_builder.GetYammerDeviceUsageUserDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_yammer_device_usage_user_detail_with_date import get_yammer_device_usage_user_detail_with_date_request_builder

        return get_yammer_device_usage_user_detail_with_date_request_builder.GetYammerDeviceUsageUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_yammer_device_usage_user_detail_with_period(self,period: Optional[str] = None) -> get_yammer_device_usage_user_detail_with_period_request_builder.GetYammerDeviceUsageUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerDeviceUsageUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_yammer_device_usage_user_detail_with_period_request_builder.GetYammerDeviceUsageUserDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_yammer_device_usage_user_detail_with_period import get_yammer_device_usage_user_detail_with_period_request_builder

        return get_yammer_device_usage_user_detail_with_period_request_builder.GetYammerDeviceUsageUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_groups_activity_counts_with_period(self,period: Optional[str] = None) -> get_yammer_groups_activity_counts_with_period_request_builder.GetYammerGroupsActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerGroupsActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_yammer_groups_activity_counts_with_period_request_builder.GetYammerGroupsActivityCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_yammer_groups_activity_counts_with_period import get_yammer_groups_activity_counts_with_period_request_builder

        return get_yammer_groups_activity_counts_with_period_request_builder.GetYammerGroupsActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_groups_activity_detail_with_date(self,date: Optional[date] = None) -> get_yammer_groups_activity_detail_with_date_request_builder.GetYammerGroupsActivityDetailWithDateRequestBuilder:
        """
        Provides operations to call the getYammerGroupsActivityDetail method.
        Args:
            date: Usage: date={date}
        Returns: get_yammer_groups_activity_detail_with_date_request_builder.GetYammerGroupsActivityDetailWithDateRequestBuilder
        """
        if date is None:
            raise Exception("date cannot be undefined")
        from .get_yammer_groups_activity_detail_with_date import get_yammer_groups_activity_detail_with_date_request_builder

        return get_yammer_groups_activity_detail_with_date_request_builder.GetYammerGroupsActivityDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_yammer_groups_activity_detail_with_period(self,period: Optional[str] = None) -> get_yammer_groups_activity_detail_with_period_request_builder.GetYammerGroupsActivityDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerGroupsActivityDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: get_yammer_groups_activity_detail_with_period_request_builder.GetYammerGroupsActivityDetailWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_yammer_groups_activity_detail_with_period import get_yammer_groups_activity_detail_with_period_request_builder

        return get_yammer_groups_activity_detail_with_period_request_builder.GetYammerGroupsActivityDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_groups_activity_group_counts_with_period(self,period: Optional[str] = None) -> get_yammer_groups_activity_group_counts_with_period_request_builder.GetYammerGroupsActivityGroupCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerGroupsActivityGroupCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: get_yammer_groups_activity_group_counts_with_period_request_builder.GetYammerGroupsActivityGroupCountsWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .get_yammer_groups_activity_group_counts_with_period import get_yammer_groups_activity_group_counts_with_period_request_builder

        return get_yammer_groups_activity_group_counts_with_period_request_builder.GetYammerGroupsActivityGroupCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def managed_device_enrollment_abandonment_details_with_skip_with_top_with_filter_with_skip_token(self,filter: Optional[str] = None, skip: Optional[int] = None, skip_token: Optional[str] = None, top: Optional[int] = None) -> managed_device_enrollment_abandonment_details_with_skip_with_top_with_filter_with_skip_token_request_builder.ManagedDeviceEnrollmentAbandonmentDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentAbandonmentDetails method.
        Args:
            filter: Usage: filter='{filter}'
            skip: Usage: skip={skip}
            skipToken: Usage: skipToken='{skipToken}'
            top: Usage: top={top}
        Returns: managed_device_enrollment_abandonment_details_with_skip_with_top_with_filter_with_skip_token_request_builder.ManagedDeviceEnrollmentAbandonmentDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder
        """
        if filter is None:
            raise Exception("filter cannot be undefined")
        if skip is None:
            raise Exception("skip cannot be undefined")
        if skip_token is None:
            raise Exception("skip_token cannot be undefined")
        if top is None:
            raise Exception("top cannot be undefined")
        from .managed_device_enrollment_abandonment_details_with_skip_with_top_with_filter_with_skip_token import managed_device_enrollment_abandonment_details_with_skip_with_top_with_filter_with_skip_token_request_builder

        return managed_device_enrollment_abandonment_details_with_skip_with_top_with_filter_with_skip_token_request_builder.ManagedDeviceEnrollmentAbandonmentDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder(self.request_adapter, self.path_parameters, filter, skip, skip_token, top)
    
    def managed_device_enrollment_abandonment_summary_with_skip_with_top_with_filter_with_skip_token(self,filter: Optional[str] = None, skip: Optional[int] = None, skip_token: Optional[str] = None, top: Optional[int] = None) -> managed_device_enrollment_abandonment_summary_with_skip_with_top_with_filter_with_skip_token_request_builder.ManagedDeviceEnrollmentAbandonmentSummaryWithSkipWithTopWithFilterWithSkipTokenRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentAbandonmentSummary method.
        Args:
            filter: Usage: filter='{filter}'
            skip: Usage: skip={skip}
            skipToken: Usage: skipToken='{skipToken}'
            top: Usage: top={top}
        Returns: managed_device_enrollment_abandonment_summary_with_skip_with_top_with_filter_with_skip_token_request_builder.ManagedDeviceEnrollmentAbandonmentSummaryWithSkipWithTopWithFilterWithSkipTokenRequestBuilder
        """
        if filter is None:
            raise Exception("filter cannot be undefined")
        if skip is None:
            raise Exception("skip cannot be undefined")
        if skip_token is None:
            raise Exception("skip_token cannot be undefined")
        if top is None:
            raise Exception("top cannot be undefined")
        from .managed_device_enrollment_abandonment_summary_with_skip_with_top_with_filter_with_skip_token import managed_device_enrollment_abandonment_summary_with_skip_with_top_with_filter_with_skip_token_request_builder

        return managed_device_enrollment_abandonment_summary_with_skip_with_top_with_filter_with_skip_token_request_builder.ManagedDeviceEnrollmentAbandonmentSummaryWithSkipWithTopWithFilterWithSkipTokenRequestBuilder(self.request_adapter, self.path_parameters, filter, skip, skip_token, top)
    
    def managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token(self,filter: Optional[str] = None, skip: Optional[int] = None, skip_token: Optional[str] = None, top: Optional[int] = None) -> managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token_request_builder.ManagedDeviceEnrollmentFailureDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentFailureDetails method.
        Args:
            filter: Usage: filter='{filter}'
            skip: Usage: skip={skip}
            skipToken: Usage: skipToken='{skipToken}'
            top: Usage: top={top}
        Returns: managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token_request_builder.ManagedDeviceEnrollmentFailureDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder
        """
        if filter is None:
            raise Exception("filter cannot be undefined")
        if skip is None:
            raise Exception("skip cannot be undefined")
        if skip_token is None:
            raise Exception("skip_token cannot be undefined")
        if top is None:
            raise Exception("top cannot be undefined")
        from .managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token import managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token_request_builder

        return managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token_request_builder.ManagedDeviceEnrollmentFailureDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder(self.request_adapter, self.path_parameters, filter, skip, skip_token, top)
    
    def managed_device_enrollment_top_failures_with_period(self,period: Optional[str] = None) -> managed_device_enrollment_top_failures_with_period_request_builder.ManagedDeviceEnrollmentTopFailuresWithPeriodRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentTopFailures method.
        Args:
            period: Usage: period='{period}'
        Returns: managed_device_enrollment_top_failures_with_period_request_builder.ManagedDeviceEnrollmentTopFailuresWithPeriodRequestBuilder
        """
        if period is None:
            raise Exception("period cannot be undefined")
        from .managed_device_enrollment_top_failures_with_period import managed_device_enrollment_top_failures_with_period_request_builder

        return managed_device_enrollment_top_failures_with_period_request_builder.ManagedDeviceEnrollmentTopFailuresWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    async def patch(self,body: Optional[report_root.ReportRoot] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> Optional[report_root.ReportRoot]:
        """
        Update reports
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[report_root.ReportRoot]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import report_root

        return await self.request_adapter.send_async(request_info, report_root.ReportRoot, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get reports
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
    
    def to_patch_request_information(self,body: Optional[report_root.ReportRoot] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update reports
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
    def application_sign_in_detailed_summary(self) -> application_sign_in_detailed_summary_request_builder.ApplicationSignInDetailedSummaryRequestBuilder:
        """
        Provides operations to manage the applicationSignInDetailedSummary property of the microsoft.graph.reportRoot entity.
        """
        from .application_sign_in_detailed_summary import application_sign_in_detailed_summary_request_builder

        return application_sign_in_detailed_summary_request_builder.ApplicationSignInDetailedSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_methods(self) -> authentication_methods_request_builder.AuthenticationMethodsRequestBuilder:
        """
        Provides operations to manage the authenticationMethods property of the microsoft.graph.reportRoot entity.
        """
        from .authentication_methods import authentication_methods_request_builder

        return authentication_methods_request_builder.AuthenticationMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def credential_user_registration_details(self) -> credential_user_registration_details_request_builder.CredentialUserRegistrationDetailsRequestBuilder:
        """
        Provides operations to manage the credentialUserRegistrationDetails property of the microsoft.graph.reportRoot entity.
        """
        from .credential_user_registration_details import credential_user_registration_details_request_builder

        return credential_user_registration_details_request_builder.CredentialUserRegistrationDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daily_print_usage(self) -> daily_print_usage_request_builder.DailyPrintUsageRequestBuilder:
        """
        Provides operations to manage the dailyPrintUsage property of the microsoft.graph.reportRoot entity.
        """
        from .daily_print_usage import daily_print_usage_request_builder

        return daily_print_usage_request_builder.DailyPrintUsageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daily_print_usage_by_printer(self) -> daily_print_usage_by_printer_request_builder.DailyPrintUsageByPrinterRequestBuilder:
        """
        Provides operations to manage the dailyPrintUsageByPrinter property of the microsoft.graph.reportRoot entity.
        """
        from .daily_print_usage_by_printer import daily_print_usage_by_printer_request_builder

        return daily_print_usage_by_printer_request_builder.DailyPrintUsageByPrinterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daily_print_usage_by_user(self) -> daily_print_usage_by_user_request_builder.DailyPrintUsageByUserRequestBuilder:
        """
        Provides operations to manage the dailyPrintUsageByUser property of the microsoft.graph.reportRoot entity.
        """
        from .daily_print_usage_by_user import daily_print_usage_by_user_request_builder

        return daily_print_usage_by_user_request_builder.DailyPrintUsageByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daily_print_usage_summaries_by_printer(self) -> daily_print_usage_summaries_by_printer_request_builder.DailyPrintUsageSummariesByPrinterRequestBuilder:
        """
        Provides operations to manage the dailyPrintUsageSummariesByPrinter property of the microsoft.graph.reportRoot entity.
        """
        from .daily_print_usage_summaries_by_printer import daily_print_usage_summaries_by_printer_request_builder

        return daily_print_usage_summaries_by_printer_request_builder.DailyPrintUsageSummariesByPrinterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daily_print_usage_summaries_by_user(self) -> daily_print_usage_summaries_by_user_request_builder.DailyPrintUsageSummariesByUserRequestBuilder:
        """
        Provides operations to manage the dailyPrintUsageSummariesByUser property of the microsoft.graph.reportRoot entity.
        """
        from .daily_print_usage_summaries_by_user import daily_print_usage_summaries_by_user_request_builder

        return daily_print_usage_summaries_by_user_request_builder.DailyPrintUsageSummariesByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_device_activity(self) -> device_configuration_device_activity_request_builder.DeviceConfigurationDeviceActivityRequestBuilder:
        """
        Provides operations to call the deviceConfigurationDeviceActivity method.
        """
        from .device_configuration_device_activity import device_configuration_device_activity_request_builder

        return device_configuration_device_activity_request_builder.DeviceConfigurationDeviceActivityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_user_activity(self) -> device_configuration_user_activity_request_builder.DeviceConfigurationUserActivityRequestBuilder:
        """
        Provides operations to call the deviceConfigurationUserActivity method.
        """
        from .device_configuration_user_activity import device_configuration_user_activity_request_builder

        return device_configuration_user_activity_request_builder.DeviceConfigurationUserActivityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_attack_simulation_repeat_offenders(self) -> get_attack_simulation_repeat_offenders_request_builder.GetAttackSimulationRepeatOffendersRequestBuilder:
        """
        Provides operations to call the getAttackSimulationRepeatOffenders method.
        """
        from .get_attack_simulation_repeat_offenders import get_attack_simulation_repeat_offenders_request_builder

        return get_attack_simulation_repeat_offenders_request_builder.GetAttackSimulationRepeatOffendersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_attack_simulation_simulation_user_coverage(self) -> get_attack_simulation_simulation_user_coverage_request_builder.GetAttackSimulationSimulationUserCoverageRequestBuilder:
        """
        Provides operations to call the getAttackSimulationSimulationUserCoverage method.
        """
        from .get_attack_simulation_simulation_user_coverage import get_attack_simulation_simulation_user_coverage_request_builder

        return get_attack_simulation_simulation_user_coverage_request_builder.GetAttackSimulationSimulationUserCoverageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_attack_simulation_training_user_coverage(self) -> get_attack_simulation_training_user_coverage_request_builder.GetAttackSimulationTrainingUserCoverageRequestBuilder:
        """
        Provides operations to call the getAttackSimulationTrainingUserCoverage method.
        """
        from .get_attack_simulation_training_user_coverage import get_attack_simulation_training_user_coverage_request_builder

        return get_attack_simulation_training_user_coverage_request_builder.GetAttackSimulationTrainingUserCoverageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_credential_user_registration_count(self) -> get_credential_user_registration_count_request_builder.GetCredentialUserRegistrationCountRequestBuilder:
        """
        Provides operations to call the getCredentialUserRegistrationCount method.
        """
        from .get_credential_user_registration_count import get_credential_user_registration_count_request_builder

        return get_credential_user_registration_count_request_builder.GetCredentialUserRegistrationCountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_office365_activation_counts(self) -> get_office365_activation_counts_request_builder.GetOffice365ActivationCountsRequestBuilder:
        """
        Provides operations to call the getOffice365ActivationCounts method.
        """
        from .get_office365_activation_counts import get_office365_activation_counts_request_builder

        return get_office365_activation_counts_request_builder.GetOffice365ActivationCountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_office365_activations_user_counts(self) -> get_office365_activations_user_counts_request_builder.GetOffice365ActivationsUserCountsRequestBuilder:
        """
        Provides operations to call the getOffice365ActivationsUserCounts method.
        """
        from .get_office365_activations_user_counts import get_office365_activations_user_counts_request_builder

        return get_office365_activations_user_counts_request_builder.GetOffice365ActivationsUserCountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_office365_activations_user_detail(self) -> get_office365_activations_user_detail_request_builder.GetOffice365ActivationsUserDetailRequestBuilder:
        """
        Provides operations to call the getOffice365ActivationsUserDetail method.
        """
        from .get_office365_activations_user_detail import get_office365_activations_user_detail_request_builder

        return get_office365_activations_user_detail_request_builder.GetOffice365ActivationsUserDetailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_enrollment_failure_details(self) -> managed_device_enrollment_failure_details_request_builder.ManagedDeviceEnrollmentFailureDetailsRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentFailureDetails method.
        """
        from .managed_device_enrollment_failure_details import managed_device_enrollment_failure_details_request_builder

        return managed_device_enrollment_failure_details_request_builder.ManagedDeviceEnrollmentFailureDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_enrollment_failure_trends(self) -> managed_device_enrollment_failure_trends_request_builder.ManagedDeviceEnrollmentFailureTrendsRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentFailureTrends method.
        """
        from .managed_device_enrollment_failure_trends import managed_device_enrollment_failure_trends_request_builder

        return managed_device_enrollment_failure_trends_request_builder.ManagedDeviceEnrollmentFailureTrendsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_enrollment_top_failures(self) -> managed_device_enrollment_top_failures_request_builder.ManagedDeviceEnrollmentTopFailuresRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentTopFailures method.
        """
        from .managed_device_enrollment_top_failures import managed_device_enrollment_top_failures_request_builder

        return managed_device_enrollment_top_failures_request_builder.ManagedDeviceEnrollmentTopFailuresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monthly_print_usage_by_printer(self) -> monthly_print_usage_by_printer_request_builder.MonthlyPrintUsageByPrinterRequestBuilder:
        """
        Provides operations to manage the monthlyPrintUsageByPrinter property of the microsoft.graph.reportRoot entity.
        """
        from .monthly_print_usage_by_printer import monthly_print_usage_by_printer_request_builder

        return monthly_print_usage_by_printer_request_builder.MonthlyPrintUsageByPrinterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monthly_print_usage_by_user(self) -> monthly_print_usage_by_user_request_builder.MonthlyPrintUsageByUserRequestBuilder:
        """
        Provides operations to manage the monthlyPrintUsageByUser property of the microsoft.graph.reportRoot entity.
        """
        from .monthly_print_usage_by_user import monthly_print_usage_by_user_request_builder

        return monthly_print_usage_by_user_request_builder.MonthlyPrintUsageByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monthly_print_usage_summaries_by_printer(self) -> monthly_print_usage_summaries_by_printer_request_builder.MonthlyPrintUsageSummariesByPrinterRequestBuilder:
        """
        Provides operations to manage the monthlyPrintUsageSummariesByPrinter property of the microsoft.graph.reportRoot entity.
        """
        from .monthly_print_usage_summaries_by_printer import monthly_print_usage_summaries_by_printer_request_builder

        return monthly_print_usage_summaries_by_printer_request_builder.MonthlyPrintUsageSummariesByPrinterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monthly_print_usage_summaries_by_user(self) -> monthly_print_usage_summaries_by_user_request_builder.MonthlyPrintUsageSummariesByUserRequestBuilder:
        """
        Provides operations to manage the monthlyPrintUsageSummariesByUser property of the microsoft.graph.reportRoot entity.
        """
        from .monthly_print_usage_summaries_by_user import monthly_print_usage_summaries_by_user_request_builder

        return monthly_print_usage_summaries_by_user_request_builder.MonthlyPrintUsageSummariesByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security(self) -> security_request_builder.SecurityRequestBuilder:
        """
        Provides operations to manage the security property of the microsoft.graph.reportRoot entity.
        """
        from .security import security_request_builder

        return security_request_builder.SecurityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_credential_usage_details(self) -> user_credential_usage_details_request_builder.UserCredentialUsageDetailsRequestBuilder:
        """
        Provides operations to manage the userCredentialUsageDetails property of the microsoft.graph.reportRoot entity.
        """
        from .user_credential_usage_details import user_credential_usage_details_request_builder

        return user_credential_usage_details_request_builder.UserCredentialUsageDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Get reports
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

    

