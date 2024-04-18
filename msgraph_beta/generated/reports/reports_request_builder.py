from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.report_root import ReportRoot
    from .application_sign_in_detailed_summary.application_sign_in_detailed_summary_request_builder import ApplicationSignInDetailedSummaryRequestBuilder
    from .app_credential_sign_in_activities.app_credential_sign_in_activities_request_builder import AppCredentialSignInActivitiesRequestBuilder
    from .authentication_methods.authentication_methods_request_builder import AuthenticationMethodsRequestBuilder
    from .credential_user_registration_details.credential_user_registration_details_request_builder import CredentialUserRegistrationDetailsRequestBuilder
    from .daily_print_usage.daily_print_usage_request_builder import DailyPrintUsageRequestBuilder
    from .daily_print_usage_by_printer.daily_print_usage_by_printer_request_builder import DailyPrintUsageByPrinterRequestBuilder
    from .daily_print_usage_by_user.daily_print_usage_by_user_request_builder import DailyPrintUsageByUserRequestBuilder
    from .daily_print_usage_summaries_by_printer.daily_print_usage_summaries_by_printer_request_builder import DailyPrintUsageSummariesByPrinterRequestBuilder
    from .daily_print_usage_summaries_by_user.daily_print_usage_summaries_by_user_request_builder import DailyPrintUsageSummariesByUserRequestBuilder
    from .device_configuration_device_activity.device_configuration_device_activity_request_builder import DeviceConfigurationDeviceActivityRequestBuilder
    from .device_configuration_user_activity.device_configuration_user_activity_request_builder import DeviceConfigurationUserActivityRequestBuilder
    from .get_attack_simulation_repeat_offenders.get_attack_simulation_repeat_offenders_request_builder import GetAttackSimulationRepeatOffendersRequestBuilder
    from .get_attack_simulation_simulation_user_coverage.get_attack_simulation_simulation_user_coverage_request_builder import GetAttackSimulationSimulationUserCoverageRequestBuilder
    from .get_attack_simulation_training_user_coverage.get_attack_simulation_training_user_coverage_request_builder import GetAttackSimulationTrainingUserCoverageRequestBuilder
    from .get_azure_a_d_application_sign_in_summary_with_period.get_azure_a_d_application_sign_in_summary_with_period_request_builder import GetAzureADApplicationSignInSummaryWithPeriodRequestBuilder
    from .get_browser_distribution_user_counts_with_period.get_browser_distribution_user_counts_with_period_request_builder import GetBrowserDistributionUserCountsWithPeriodRequestBuilder
    from .get_browser_user_counts_with_period.get_browser_user_counts_with_period_request_builder import GetBrowserUserCountsWithPeriodRequestBuilder
    from .get_browser_user_detail_with_period.get_browser_user_detail_with_period_request_builder import GetBrowserUserDetailWithPeriodRequestBuilder
    from .get_credential_usage_summary_with_period.get_credential_usage_summary_with_period_request_builder import GetCredentialUsageSummaryWithPeriodRequestBuilder
    from .get_credential_user_registration_count.get_credential_user_registration_count_request_builder import GetCredentialUserRegistrationCountRequestBuilder
    from .get_email_activity_counts_with_period.get_email_activity_counts_with_period_request_builder import GetEmailActivityCountsWithPeriodRequestBuilder
    from .get_email_activity_user_counts_with_period.get_email_activity_user_counts_with_period_request_builder import GetEmailActivityUserCountsWithPeriodRequestBuilder
    from .get_email_activity_user_detail_with_date.get_email_activity_user_detail_with_date_request_builder import GetEmailActivityUserDetailWithDateRequestBuilder
    from .get_email_activity_user_detail_with_period.get_email_activity_user_detail_with_period_request_builder import GetEmailActivityUserDetailWithPeriodRequestBuilder
    from .get_email_app_usage_apps_user_counts_with_period.get_email_app_usage_apps_user_counts_with_period_request_builder import GetEmailAppUsageAppsUserCountsWithPeriodRequestBuilder
    from .get_email_app_usage_user_counts_with_period.get_email_app_usage_user_counts_with_period_request_builder import GetEmailAppUsageUserCountsWithPeriodRequestBuilder
    from .get_email_app_usage_user_detail_with_date.get_email_app_usage_user_detail_with_date_request_builder import GetEmailAppUsageUserDetailWithDateRequestBuilder
    from .get_email_app_usage_user_detail_with_period.get_email_app_usage_user_detail_with_period_request_builder import GetEmailAppUsageUserDetailWithPeriodRequestBuilder
    from .get_email_app_usage_versions_user_counts_with_period.get_email_app_usage_versions_user_counts_with_period_request_builder import GetEmailAppUsageVersionsUserCountsWithPeriodRequestBuilder
    from .get_forms_user_activity_counts_with_period.get_forms_user_activity_counts_with_period_request_builder import GetFormsUserActivityCountsWithPeriodRequestBuilder
    from .get_forms_user_activity_user_counts_with_period.get_forms_user_activity_user_counts_with_period_request_builder import GetFormsUserActivityUserCountsWithPeriodRequestBuilder
    from .get_forms_user_activity_user_detail_with_date.get_forms_user_activity_user_detail_with_date_request_builder import GetFormsUserActivityUserDetailWithDateRequestBuilder
    from .get_forms_user_activity_user_detail_with_period.get_forms_user_activity_user_detail_with_period_request_builder import GetFormsUserActivityUserDetailWithPeriodRequestBuilder
    from .get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time.get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time_request_builder import GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeRequestBuilder
    from .get_m365_app_platform_user_counts_with_period.get_m365_app_platform_user_counts_with_period_request_builder import GetM365AppPlatformUserCountsWithPeriodRequestBuilder
    from .get_m365_app_user_counts_with_period.get_m365_app_user_counts_with_period_request_builder import GetM365AppUserCountsWithPeriodRequestBuilder
    from .get_m365_app_user_detail_with_date.get_m365_app_user_detail_with_date_request_builder import GetM365AppUserDetailWithDateRequestBuilder
    from .get_m365_app_user_detail_with_period.get_m365_app_user_detail_with_period_request_builder import GetM365AppUserDetailWithPeriodRequestBuilder
    from .get_mailbox_usage_detail_with_period.get_mailbox_usage_detail_with_period_request_builder import GetMailboxUsageDetailWithPeriodRequestBuilder
    from .get_mailbox_usage_mailbox_counts_with_period.get_mailbox_usage_mailbox_counts_with_period_request_builder import GetMailboxUsageMailboxCountsWithPeriodRequestBuilder
    from .get_mailbox_usage_quota_status_mailbox_counts_with_period.get_mailbox_usage_quota_status_mailbox_counts_with_period_request_builder import GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequestBuilder
    from .get_mailbox_usage_storage_with_period.get_mailbox_usage_storage_with_period_request_builder import GetMailboxUsageStorageWithPeriodRequestBuilder
    from .get_office365_activations_user_counts.get_office365_activations_user_counts_request_builder import GetOffice365ActivationsUserCountsRequestBuilder
    from .get_office365_activations_user_detail.get_office365_activations_user_detail_request_builder import GetOffice365ActivationsUserDetailRequestBuilder
    from .get_office365_activation_counts.get_office365_activation_counts_request_builder import GetOffice365ActivationCountsRequestBuilder
    from .get_office365_active_user_counts_with_period.get_office365_active_user_counts_with_period_request_builder import GetOffice365ActiveUserCountsWithPeriodRequestBuilder
    from .get_office365_active_user_detail_with_date.get_office365_active_user_detail_with_date_request_builder import GetOffice365ActiveUserDetailWithDateRequestBuilder
    from .get_office365_active_user_detail_with_period.get_office365_active_user_detail_with_period_request_builder import GetOffice365ActiveUserDetailWithPeriodRequestBuilder
    from .get_office365_groups_activity_counts_with_period.get_office365_groups_activity_counts_with_period_request_builder import GetOffice365GroupsActivityCountsWithPeriodRequestBuilder
    from .get_office365_groups_activity_detail_with_date.get_office365_groups_activity_detail_with_date_request_builder import GetOffice365GroupsActivityDetailWithDateRequestBuilder
    from .get_office365_groups_activity_detail_with_period.get_office365_groups_activity_detail_with_period_request_builder import GetOffice365GroupsActivityDetailWithPeriodRequestBuilder
    from .get_office365_groups_activity_file_counts_with_period.get_office365_groups_activity_file_counts_with_period_request_builder import GetOffice365GroupsActivityFileCountsWithPeriodRequestBuilder
    from .get_office365_groups_activity_group_counts_with_period.get_office365_groups_activity_group_counts_with_period_request_builder import GetOffice365GroupsActivityGroupCountsWithPeriodRequestBuilder
    from .get_office365_groups_activity_storage_with_period.get_office365_groups_activity_storage_with_period_request_builder import GetOffice365GroupsActivityStorageWithPeriodRequestBuilder
    from .get_office365_services_user_counts_with_period.get_office365_services_user_counts_with_period_request_builder import GetOffice365ServicesUserCountsWithPeriodRequestBuilder
    from .get_one_drive_activity_file_counts_with_period.get_one_drive_activity_file_counts_with_period_request_builder import GetOneDriveActivityFileCountsWithPeriodRequestBuilder
    from .get_one_drive_activity_user_counts_with_period.get_one_drive_activity_user_counts_with_period_request_builder import GetOneDriveActivityUserCountsWithPeriodRequestBuilder
    from .get_one_drive_activity_user_detail_with_date.get_one_drive_activity_user_detail_with_date_request_builder import GetOneDriveActivityUserDetailWithDateRequestBuilder
    from .get_one_drive_activity_user_detail_with_period.get_one_drive_activity_user_detail_with_period_request_builder import GetOneDriveActivityUserDetailWithPeriodRequestBuilder
    from .get_one_drive_usage_account_counts_with_period.get_one_drive_usage_account_counts_with_period_request_builder import GetOneDriveUsageAccountCountsWithPeriodRequestBuilder
    from .get_one_drive_usage_account_detail_with_date.get_one_drive_usage_account_detail_with_date_request_builder import GetOneDriveUsageAccountDetailWithDateRequestBuilder
    from .get_one_drive_usage_account_detail_with_period.get_one_drive_usage_account_detail_with_period_request_builder import GetOneDriveUsageAccountDetailWithPeriodRequestBuilder
    from .get_one_drive_usage_file_counts_with_period.get_one_drive_usage_file_counts_with_period_request_builder import GetOneDriveUsageFileCountsWithPeriodRequestBuilder
    from .get_one_drive_usage_storage_with_period.get_one_drive_usage_storage_with_period_request_builder import GetOneDriveUsageStorageWithPeriodRequestBuilder
    from .get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time.get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time_request_builder import GetPrinterArchivedPrintJobsWithPrinterIdWithStartDateTimeWithEndDateTimeRequestBuilder
    from .get_relying_party_detailed_summary_with_period.get_relying_party_detailed_summary_with_period_request_builder import GetRelyingPartyDetailedSummaryWithPeriodRequestBuilder
    from .get_share_point_activity_file_counts_with_period.get_share_point_activity_file_counts_with_period_request_builder import GetSharePointActivityFileCountsWithPeriodRequestBuilder
    from .get_share_point_activity_pages_with_period.get_share_point_activity_pages_with_period_request_builder import GetSharePointActivityPagesWithPeriodRequestBuilder
    from .get_share_point_activity_user_counts_with_period.get_share_point_activity_user_counts_with_period_request_builder import GetSharePointActivityUserCountsWithPeriodRequestBuilder
    from .get_share_point_activity_user_detail_with_date.get_share_point_activity_user_detail_with_date_request_builder import GetSharePointActivityUserDetailWithDateRequestBuilder
    from .get_share_point_activity_user_detail_with_period.get_share_point_activity_user_detail_with_period_request_builder import GetSharePointActivityUserDetailWithPeriodRequestBuilder
    from .get_share_point_site_usage_detail_with_date.get_share_point_site_usage_detail_with_date_request_builder import GetSharePointSiteUsageDetailWithDateRequestBuilder
    from .get_share_point_site_usage_detail_with_period.get_share_point_site_usage_detail_with_period_request_builder import GetSharePointSiteUsageDetailWithPeriodRequestBuilder
    from .get_share_point_site_usage_file_counts_with_period.get_share_point_site_usage_file_counts_with_period_request_builder import GetSharePointSiteUsageFileCountsWithPeriodRequestBuilder
    from .get_share_point_site_usage_pages_with_period.get_share_point_site_usage_pages_with_period_request_builder import GetSharePointSiteUsagePagesWithPeriodRequestBuilder
    from .get_share_point_site_usage_site_counts_with_period.get_share_point_site_usage_site_counts_with_period_request_builder import GetSharePointSiteUsageSiteCountsWithPeriodRequestBuilder
    from .get_share_point_site_usage_storage_with_period.get_share_point_site_usage_storage_with_period_request_builder import GetSharePointSiteUsageStorageWithPeriodRequestBuilder
    from .get_skype_for_business_activity_counts_with_period.get_skype_for_business_activity_counts_with_period_request_builder import GetSkypeForBusinessActivityCountsWithPeriodRequestBuilder
    from .get_skype_for_business_activity_user_counts_with_period.get_skype_for_business_activity_user_counts_with_period_request_builder import GetSkypeForBusinessActivityUserCountsWithPeriodRequestBuilder
    from .get_skype_for_business_activity_user_detail_with_date.get_skype_for_business_activity_user_detail_with_date_request_builder import GetSkypeForBusinessActivityUserDetailWithDateRequestBuilder
    from .get_skype_for_business_activity_user_detail_with_period.get_skype_for_business_activity_user_detail_with_period_request_builder import GetSkypeForBusinessActivityUserDetailWithPeriodRequestBuilder
    from .get_skype_for_business_device_usage_distribution_user_counts_with_period.get_skype_for_business_device_usage_distribution_user_counts_with_period_request_builder import GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
    from .get_skype_for_business_device_usage_user_counts_with_period.get_skype_for_business_device_usage_user_counts_with_period_request_builder import GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequestBuilder
    from .get_skype_for_business_device_usage_user_detail_with_date.get_skype_for_business_device_usage_user_detail_with_date_request_builder import GetSkypeForBusinessDeviceUsageUserDetailWithDateRequestBuilder
    from .get_skype_for_business_device_usage_user_detail_with_period.get_skype_for_business_device_usage_user_detail_with_period_request_builder import GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequestBuilder
    from .get_skype_for_business_organizer_activity_counts_with_period.get_skype_for_business_organizer_activity_counts_with_period_request_builder import GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequestBuilder
    from .get_skype_for_business_organizer_activity_minute_counts_with_period.get_skype_for_business_organizer_activity_minute_counts_with_period_request_builder import GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequestBuilder
    from .get_skype_for_business_organizer_activity_user_counts_with_period.get_skype_for_business_organizer_activity_user_counts_with_period_request_builder import GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequestBuilder
    from .get_skype_for_business_participant_activity_counts_with_period.get_skype_for_business_participant_activity_counts_with_period_request_builder import GetSkypeForBusinessParticipantActivityCountsWithPeriodRequestBuilder
    from .get_skype_for_business_participant_activity_minute_counts_with_period.get_skype_for_business_participant_activity_minute_counts_with_period_request_builder import GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequestBuilder
    from .get_skype_for_business_participant_activity_user_counts_with_period.get_skype_for_business_participant_activity_user_counts_with_period_request_builder import GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequestBuilder
    from .get_skype_for_business_peer_to_peer_activity_counts_with_period.get_skype_for_business_peer_to_peer_activity_counts_with_period_request_builder import GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequestBuilder
    from .get_skype_for_business_peer_to_peer_activity_minute_counts_with_period.get_skype_for_business_peer_to_peer_activity_minute_counts_with_period_request_builder import GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequestBuilder
    from .get_skype_for_business_peer_to_peer_activity_user_counts_with_period.get_skype_for_business_peer_to_peer_activity_user_counts_with_period_request_builder import GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequestBuilder
    from .get_teams_device_usage_distribution_total_user_counts_with_period.get_teams_device_usage_distribution_total_user_counts_with_period_request_builder import GetTeamsDeviceUsageDistributionTotalUserCountsWithPeriodRequestBuilder
    from .get_teams_device_usage_distribution_user_counts_with_period.get_teams_device_usage_distribution_user_counts_with_period_request_builder import GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
    from .get_teams_device_usage_total_user_counts_with_period.get_teams_device_usage_total_user_counts_with_period_request_builder import GetTeamsDeviceUsageTotalUserCountsWithPeriodRequestBuilder
    from .get_teams_device_usage_user_counts_with_period.get_teams_device_usage_user_counts_with_period_request_builder import GetTeamsDeviceUsageUserCountsWithPeriodRequestBuilder
    from .get_teams_device_usage_user_detail_with_date.get_teams_device_usage_user_detail_with_date_request_builder import GetTeamsDeviceUsageUserDetailWithDateRequestBuilder
    from .get_teams_device_usage_user_detail_with_period.get_teams_device_usage_user_detail_with_period_request_builder import GetTeamsDeviceUsageUserDetailWithPeriodRequestBuilder
    from .get_teams_team_activity_counts_with_period.get_teams_team_activity_counts_with_period_request_builder import GetTeamsTeamActivityCountsWithPeriodRequestBuilder
    from .get_teams_team_activity_detail_with_date.get_teams_team_activity_detail_with_date_request_builder import GetTeamsTeamActivityDetailWithDateRequestBuilder
    from .get_teams_team_activity_detail_with_period.get_teams_team_activity_detail_with_period_request_builder import GetTeamsTeamActivityDetailWithPeriodRequestBuilder
    from .get_teams_team_activity_distribution_counts_with_period.get_teams_team_activity_distribution_counts_with_period_request_builder import GetTeamsTeamActivityDistributionCountsWithPeriodRequestBuilder
    from .get_teams_team_counts_with_period.get_teams_team_counts_with_period_request_builder import GetTeamsTeamCountsWithPeriodRequestBuilder
    from .get_teams_user_activity_counts_with_period.get_teams_user_activity_counts_with_period_request_builder import GetTeamsUserActivityCountsWithPeriodRequestBuilder
    from .get_teams_user_activity_distribution_total_user_counts_with_period.get_teams_user_activity_distribution_total_user_counts_with_period_request_builder import GetTeamsUserActivityDistributionTotalUserCountsWithPeriodRequestBuilder
    from .get_teams_user_activity_distribution_user_counts_with_period.get_teams_user_activity_distribution_user_counts_with_period_request_builder import GetTeamsUserActivityDistributionUserCountsWithPeriodRequestBuilder
    from .get_teams_user_activity_total_counts_with_period.get_teams_user_activity_total_counts_with_period_request_builder import GetTeamsUserActivityTotalCountsWithPeriodRequestBuilder
    from .get_teams_user_activity_total_distribution_counts_with_period.get_teams_user_activity_total_distribution_counts_with_period_request_builder import GetTeamsUserActivityTotalDistributionCountsWithPeriodRequestBuilder
    from .get_teams_user_activity_total_user_counts_with_period.get_teams_user_activity_total_user_counts_with_period_request_builder import GetTeamsUserActivityTotalUserCountsWithPeriodRequestBuilder
    from .get_teams_user_activity_user_counts_with_period.get_teams_user_activity_user_counts_with_period_request_builder import GetTeamsUserActivityUserCountsWithPeriodRequestBuilder
    from .get_teams_user_activity_user_detail_with_date.get_teams_user_activity_user_detail_with_date_request_builder import GetTeamsUserActivityUserDetailWithDateRequestBuilder
    from .get_teams_user_activity_user_detail_with_period.get_teams_user_activity_user_detail_with_period_request_builder import GetTeamsUserActivityUserDetailWithPeriodRequestBuilder
    from .get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time.get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time_request_builder import GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder
    from .get_yammer_activity_counts_with_period.get_yammer_activity_counts_with_period_request_builder import GetYammerActivityCountsWithPeriodRequestBuilder
    from .get_yammer_activity_user_counts_with_period.get_yammer_activity_user_counts_with_period_request_builder import GetYammerActivityUserCountsWithPeriodRequestBuilder
    from .get_yammer_activity_user_detail_with_date.get_yammer_activity_user_detail_with_date_request_builder import GetYammerActivityUserDetailWithDateRequestBuilder
    from .get_yammer_activity_user_detail_with_period.get_yammer_activity_user_detail_with_period_request_builder import GetYammerActivityUserDetailWithPeriodRequestBuilder
    from .get_yammer_device_usage_distribution_user_counts_with_period.get_yammer_device_usage_distribution_user_counts_with_period_request_builder import GetYammerDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
    from .get_yammer_device_usage_user_counts_with_period.get_yammer_device_usage_user_counts_with_period_request_builder import GetYammerDeviceUsageUserCountsWithPeriodRequestBuilder
    from .get_yammer_device_usage_user_detail_with_date.get_yammer_device_usage_user_detail_with_date_request_builder import GetYammerDeviceUsageUserDetailWithDateRequestBuilder
    from .get_yammer_device_usage_user_detail_with_period.get_yammer_device_usage_user_detail_with_period_request_builder import GetYammerDeviceUsageUserDetailWithPeriodRequestBuilder
    from .get_yammer_groups_activity_counts_with_period.get_yammer_groups_activity_counts_with_period_request_builder import GetYammerGroupsActivityCountsWithPeriodRequestBuilder
    from .get_yammer_groups_activity_detail_with_date.get_yammer_groups_activity_detail_with_date_request_builder import GetYammerGroupsActivityDetailWithDateRequestBuilder
    from .get_yammer_groups_activity_detail_with_period.get_yammer_groups_activity_detail_with_period_request_builder import GetYammerGroupsActivityDetailWithPeriodRequestBuilder
    from .get_yammer_groups_activity_group_counts_with_period.get_yammer_groups_activity_group_counts_with_period_request_builder import GetYammerGroupsActivityGroupCountsWithPeriodRequestBuilder
    from .managed_device_enrollment_abandonment_details_with_skip_with_top_with_filter_with_skip_token.managed_device_enrollment_abandonment_details_with_skip_with_top_with_filter_with_skip_token_request_builder import ManagedDeviceEnrollmentAbandonmentDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder
    from .managed_device_enrollment_abandonment_summary_with_skip_with_top_with_filter_with_skip_token.managed_device_enrollment_abandonment_summary_with_skip_with_top_with_filter_with_skip_token_request_builder import ManagedDeviceEnrollmentAbandonmentSummaryWithSkipWithTopWithFilterWithSkipTokenRequestBuilder
    from .managed_device_enrollment_failure_details.managed_device_enrollment_failure_details_request_builder import ManagedDeviceEnrollmentFailureDetailsRequestBuilder
    from .managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token.managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token_request_builder import ManagedDeviceEnrollmentFailureDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder
    from .managed_device_enrollment_failure_trends.managed_device_enrollment_failure_trends_request_builder import ManagedDeviceEnrollmentFailureTrendsRequestBuilder
    from .managed_device_enrollment_top_failures.managed_device_enrollment_top_failures_request_builder import ManagedDeviceEnrollmentTopFailuresRequestBuilder
    from .managed_device_enrollment_top_failures_with_period.managed_device_enrollment_top_failures_with_period_request_builder import ManagedDeviceEnrollmentTopFailuresWithPeriodRequestBuilder
    from .monthly_print_usage_by_printer.monthly_print_usage_by_printer_request_builder import MonthlyPrintUsageByPrinterRequestBuilder
    from .monthly_print_usage_by_user.monthly_print_usage_by_user_request_builder import MonthlyPrintUsageByUserRequestBuilder
    from .monthly_print_usage_summaries_by_printer.monthly_print_usage_summaries_by_printer_request_builder import MonthlyPrintUsageSummariesByPrinterRequestBuilder
    from .monthly_print_usage_summaries_by_user.monthly_print_usage_summaries_by_user_request_builder import MonthlyPrintUsageSummariesByUserRequestBuilder
    from .partners.partners_request_builder import PartnersRequestBuilder
    from .security.security_request_builder import SecurityRequestBuilder
    from .service_activity.service_activity_request_builder import ServiceActivityRequestBuilder
    from .service_principal_sign_in_activities.service_principal_sign_in_activities_request_builder import ServicePrincipalSignInActivitiesRequestBuilder
    from .sla.sla_request_builder import SlaRequestBuilder
    from .user_credential_usage_details.user_credential_usage_details_request_builder import UserCredentialUsageDetailsRequestBuilder
    from .user_insights.user_insights_request_builder import UserInsightsRequestBuilder

class ReportsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the reportRoot singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ReportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/reports{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[ReportRoot]:
        """
        Get reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ReportRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.report_root import ReportRoot

        return await self.request_adapter.send_async(request_info, ReportRoot, error_mapping)
    
    def get_azure_a_d_application_sign_in_summary_with_period(self,period: Optional[str] = None) -> GetAzureADApplicationSignInSummaryWithPeriodRequestBuilder:
        """
        Provides operations to call the getAzureADApplicationSignInSummary method.
        param period: Usage: period='{period}'
        Returns: GetAzureADApplicationSignInSummaryWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_azure_a_d_application_sign_in_summary_with_period.get_azure_a_d_application_sign_in_summary_with_period_request_builder import GetAzureADApplicationSignInSummaryWithPeriodRequestBuilder

        return GetAzureADApplicationSignInSummaryWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_browser_distribution_user_counts_with_period(self,period: Optional[str] = None) -> GetBrowserDistributionUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getBrowserDistributionUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetBrowserDistributionUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_browser_distribution_user_counts_with_period.get_browser_distribution_user_counts_with_period_request_builder import GetBrowserDistributionUserCountsWithPeriodRequestBuilder

        return GetBrowserDistributionUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_browser_user_counts_with_period(self,period: Optional[str] = None) -> GetBrowserUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getBrowserUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetBrowserUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_browser_user_counts_with_period.get_browser_user_counts_with_period_request_builder import GetBrowserUserCountsWithPeriodRequestBuilder

        return GetBrowserUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_browser_user_detail_with_period(self,period: Optional[str] = None) -> GetBrowserUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getBrowserUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetBrowserUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_browser_user_detail_with_period.get_browser_user_detail_with_period_request_builder import GetBrowserUserDetailWithPeriodRequestBuilder

        return GetBrowserUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_credential_usage_summary_with_period(self,period: Optional[str] = None) -> GetCredentialUsageSummaryWithPeriodRequestBuilder:
        """
        Provides operations to call the getCredentialUsageSummary method.
        param period: Usage: period='{period}'
        Returns: GetCredentialUsageSummaryWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_credential_usage_summary_with_period.get_credential_usage_summary_with_period_request_builder import GetCredentialUsageSummaryWithPeriodRequestBuilder

        return GetCredentialUsageSummaryWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_activity_counts_with_period(self,period: Optional[str] = None) -> GetEmailActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailActivityCounts method.
        param period: Usage: period='{period}'
        Returns: GetEmailActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_activity_counts_with_period.get_email_activity_counts_with_period_request_builder import GetEmailActivityCountsWithPeriodRequestBuilder

        return GetEmailActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetEmailActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailActivityUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetEmailActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_activity_user_counts_with_period.get_email_activity_user_counts_with_period_request_builder import GetEmailActivityUserCountsWithPeriodRequestBuilder

        return GetEmailActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_activity_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetEmailActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getEmailActivityUserDetail method.
        param date: Usage: date={date}
        Returns: GetEmailActivityUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_email_activity_user_detail_with_date.get_email_activity_user_detail_with_date_request_builder import GetEmailActivityUserDetailWithDateRequestBuilder

        return GetEmailActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_email_activity_user_detail_with_period(self,period: Optional[str] = None) -> GetEmailActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailActivityUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetEmailActivityUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_activity_user_detail_with_period.get_email_activity_user_detail_with_period_request_builder import GetEmailActivityUserDetailWithPeriodRequestBuilder

        return GetEmailActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_app_usage_apps_user_counts_with_period(self,period: Optional[str] = None) -> GetEmailAppUsageAppsUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageAppsUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetEmailAppUsageAppsUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_app_usage_apps_user_counts_with_period.get_email_app_usage_apps_user_counts_with_period_request_builder import GetEmailAppUsageAppsUserCountsWithPeriodRequestBuilder

        return GetEmailAppUsageAppsUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_app_usage_user_counts_with_period(self,period: Optional[str] = None) -> GetEmailAppUsageUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetEmailAppUsageUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_app_usage_user_counts_with_period.get_email_app_usage_user_counts_with_period_request_builder import GetEmailAppUsageUserCountsWithPeriodRequestBuilder

        return GetEmailAppUsageUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_app_usage_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetEmailAppUsageUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageUserDetail method.
        param date: Usage: date={date}
        Returns: GetEmailAppUsageUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_email_app_usage_user_detail_with_date.get_email_app_usage_user_detail_with_date_request_builder import GetEmailAppUsageUserDetailWithDateRequestBuilder

        return GetEmailAppUsageUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_email_app_usage_user_detail_with_period(self,period: Optional[str] = None) -> GetEmailAppUsageUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetEmailAppUsageUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_app_usage_user_detail_with_period.get_email_app_usage_user_detail_with_period_request_builder import GetEmailAppUsageUserDetailWithPeriodRequestBuilder

        return GetEmailAppUsageUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_app_usage_versions_user_counts_with_period(self,period: Optional[str] = None) -> GetEmailAppUsageVersionsUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageVersionsUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetEmailAppUsageVersionsUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_app_usage_versions_user_counts_with_period.get_email_app_usage_versions_user_counts_with_period_request_builder import GetEmailAppUsageVersionsUserCountsWithPeriodRequestBuilder

        return GetEmailAppUsageVersionsUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_forms_user_activity_counts_with_period(self,period: Optional[str] = None) -> GetFormsUserActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getFormsUserActivityCounts method.
        param period: Usage: period='{period}'
        Returns: GetFormsUserActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_forms_user_activity_counts_with_period.get_forms_user_activity_counts_with_period_request_builder import GetFormsUserActivityCountsWithPeriodRequestBuilder

        return GetFormsUserActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_forms_user_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetFormsUserActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getFormsUserActivityUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetFormsUserActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_forms_user_activity_user_counts_with_period.get_forms_user_activity_user_counts_with_period_request_builder import GetFormsUserActivityUserCountsWithPeriodRequestBuilder

        return GetFormsUserActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_forms_user_activity_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetFormsUserActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getFormsUserActivityUserDetail method.
        param date: Usage: date={date}
        Returns: GetFormsUserActivityUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_forms_user_activity_user_detail_with_date.get_forms_user_activity_user_detail_with_date_request_builder import GetFormsUserActivityUserDetailWithDateRequestBuilder

        return GetFormsUserActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_forms_user_activity_user_detail_with_period(self,period: Optional[str] = None) -> GetFormsUserActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getFormsUserActivityUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetFormsUserActivityUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_forms_user_activity_user_detail_with_period.get_forms_user_activity_user_detail_with_period_request_builder import GetFormsUserActivityUserDetailWithPeriodRequestBuilder

        return GetFormsUserActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time(self,end_date_time: Optional[datetime.datetime] = None, group_id: Optional[str] = None, start_date_time: Optional[datetime.datetime] = None) -> GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the getGroupArchivedPrintJobs method.
        param end_date_time: Usage: endDateTime={endDateTime}
        param group_id: Usage: groupId='{groupId}'
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if not end_date_time:
            raise TypeError("end_date_time cannot be null.")
        if not group_id:
            raise TypeError("group_id cannot be null.")
        if not start_date_time:
            raise TypeError("start_date_time cannot be null.")
        from .get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time.get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time_request_builder import GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeRequestBuilder

        return GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, group_id, start_date_time)
    
    def get_m365_app_platform_user_counts_with_period(self,period: Optional[str] = None) -> GetM365AppPlatformUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getM365AppPlatformUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetM365AppPlatformUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_m365_app_platform_user_counts_with_period.get_m365_app_platform_user_counts_with_period_request_builder import GetM365AppPlatformUserCountsWithPeriodRequestBuilder

        return GetM365AppPlatformUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_m365_app_user_counts_with_period(self,period: Optional[str] = None) -> GetM365AppUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getM365AppUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetM365AppUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_m365_app_user_counts_with_period.get_m365_app_user_counts_with_period_request_builder import GetM365AppUserCountsWithPeriodRequestBuilder

        return GetM365AppUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_m365_app_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetM365AppUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getM365AppUserDetail method.
        param date: Usage: date={date}
        Returns: GetM365AppUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_m365_app_user_detail_with_date.get_m365_app_user_detail_with_date_request_builder import GetM365AppUserDetailWithDateRequestBuilder

        return GetM365AppUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_m365_app_user_detail_with_period(self,period: Optional[str] = None) -> GetM365AppUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getM365AppUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetM365AppUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_m365_app_user_detail_with_period.get_m365_app_user_detail_with_period_request_builder import GetM365AppUserDetailWithPeriodRequestBuilder

        return GetM365AppUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_mailbox_usage_detail_with_period(self,period: Optional[str] = None) -> GetMailboxUsageDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getMailboxUsageDetail method.
        param period: Usage: period='{period}'
        Returns: GetMailboxUsageDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_mailbox_usage_detail_with_period.get_mailbox_usage_detail_with_period_request_builder import GetMailboxUsageDetailWithPeriodRequestBuilder

        return GetMailboxUsageDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_mailbox_usage_mailbox_counts_with_period(self,period: Optional[str] = None) -> GetMailboxUsageMailboxCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getMailboxUsageMailboxCounts method.
        param period: Usage: period='{period}'
        Returns: GetMailboxUsageMailboxCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_mailbox_usage_mailbox_counts_with_period.get_mailbox_usage_mailbox_counts_with_period_request_builder import GetMailboxUsageMailboxCountsWithPeriodRequestBuilder

        return GetMailboxUsageMailboxCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_mailbox_usage_quota_status_mailbox_counts_with_period(self,period: Optional[str] = None) -> GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getMailboxUsageQuotaStatusMailboxCounts method.
        param period: Usage: period='{period}'
        Returns: GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_mailbox_usage_quota_status_mailbox_counts_with_period.get_mailbox_usage_quota_status_mailbox_counts_with_period_request_builder import GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequestBuilder

        return GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_mailbox_usage_storage_with_period(self,period: Optional[str] = None) -> GetMailboxUsageStorageWithPeriodRequestBuilder:
        """
        Provides operations to call the getMailboxUsageStorage method.
        param period: Usage: period='{period}'
        Returns: GetMailboxUsageStorageWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_mailbox_usage_storage_with_period.get_mailbox_usage_storage_with_period_request_builder import GetMailboxUsageStorageWithPeriodRequestBuilder

        return GetMailboxUsageStorageWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_active_user_counts_with_period(self,period: Optional[str] = None) -> GetOffice365ActiveUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365ActiveUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetOffice365ActiveUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_active_user_counts_with_period.get_office365_active_user_counts_with_period_request_builder import GetOffice365ActiveUserCountsWithPeriodRequestBuilder

        return GetOffice365ActiveUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_active_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetOffice365ActiveUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getOffice365ActiveUserDetail method.
        param date: Usage: date={date}
        Returns: GetOffice365ActiveUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_office365_active_user_detail_with_date.get_office365_active_user_detail_with_date_request_builder import GetOffice365ActiveUserDetailWithDateRequestBuilder

        return GetOffice365ActiveUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_office365_active_user_detail_with_period(self,period: Optional[str] = None) -> GetOffice365ActiveUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365ActiveUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetOffice365ActiveUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_active_user_detail_with_period.get_office365_active_user_detail_with_period_request_builder import GetOffice365ActiveUserDetailWithPeriodRequestBuilder

        return GetOffice365ActiveUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_counts_with_period(self,period: Optional[str] = None) -> GetOffice365GroupsActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityCounts method.
        param period: Usage: period='{period}'
        Returns: GetOffice365GroupsActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_groups_activity_counts_with_period.get_office365_groups_activity_counts_with_period_request_builder import GetOffice365GroupsActivityCountsWithPeriodRequestBuilder

        return GetOffice365GroupsActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_detail_with_date(self,date: Optional[datetime.date] = None) -> GetOffice365GroupsActivityDetailWithDateRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityDetail method.
        param date: Usage: date={date}
        Returns: GetOffice365GroupsActivityDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_office365_groups_activity_detail_with_date.get_office365_groups_activity_detail_with_date_request_builder import GetOffice365GroupsActivityDetailWithDateRequestBuilder

        return GetOffice365GroupsActivityDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_office365_groups_activity_detail_with_period(self,period: Optional[str] = None) -> GetOffice365GroupsActivityDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityDetail method.
        param period: Usage: period='{period}'
        Returns: GetOffice365GroupsActivityDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_groups_activity_detail_with_period.get_office365_groups_activity_detail_with_period_request_builder import GetOffice365GroupsActivityDetailWithPeriodRequestBuilder

        return GetOffice365GroupsActivityDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_file_counts_with_period(self,period: Optional[str] = None) -> GetOffice365GroupsActivityFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityFileCounts method.
        param period: Usage: period='{period}'
        Returns: GetOffice365GroupsActivityFileCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_groups_activity_file_counts_with_period.get_office365_groups_activity_file_counts_with_period_request_builder import GetOffice365GroupsActivityFileCountsWithPeriodRequestBuilder

        return GetOffice365GroupsActivityFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_group_counts_with_period(self,period: Optional[str] = None) -> GetOffice365GroupsActivityGroupCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityGroupCounts method.
        param period: Usage: period='{period}'
        Returns: GetOffice365GroupsActivityGroupCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_groups_activity_group_counts_with_period.get_office365_groups_activity_group_counts_with_period_request_builder import GetOffice365GroupsActivityGroupCountsWithPeriodRequestBuilder

        return GetOffice365GroupsActivityGroupCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_storage_with_period(self,period: Optional[str] = None) -> GetOffice365GroupsActivityStorageWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityStorage method.
        param period: Usage: period='{period}'
        Returns: GetOffice365GroupsActivityStorageWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_groups_activity_storage_with_period.get_office365_groups_activity_storage_with_period_request_builder import GetOffice365GroupsActivityStorageWithPeriodRequestBuilder

        return GetOffice365GroupsActivityStorageWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_services_user_counts_with_period(self,period: Optional[str] = None) -> GetOffice365ServicesUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365ServicesUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetOffice365ServicesUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_services_user_counts_with_period.get_office365_services_user_counts_with_period_request_builder import GetOffice365ServicesUserCountsWithPeriodRequestBuilder

        return GetOffice365ServicesUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_activity_file_counts_with_period(self,period: Optional[str] = None) -> GetOneDriveActivityFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveActivityFileCounts method.
        param period: Usage: period='{period}'
        Returns: GetOneDriveActivityFileCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_activity_file_counts_with_period.get_one_drive_activity_file_counts_with_period_request_builder import GetOneDriveActivityFileCountsWithPeriodRequestBuilder

        return GetOneDriveActivityFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetOneDriveActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveActivityUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetOneDriveActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_activity_user_counts_with_period.get_one_drive_activity_user_counts_with_period_request_builder import GetOneDriveActivityUserCountsWithPeriodRequestBuilder

        return GetOneDriveActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_activity_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetOneDriveActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getOneDriveActivityUserDetail method.
        param date: Usage: date={date}
        Returns: GetOneDriveActivityUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_one_drive_activity_user_detail_with_date.get_one_drive_activity_user_detail_with_date_request_builder import GetOneDriveActivityUserDetailWithDateRequestBuilder

        return GetOneDriveActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_one_drive_activity_user_detail_with_period(self,period: Optional[str] = None) -> GetOneDriveActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveActivityUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetOneDriveActivityUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_activity_user_detail_with_period.get_one_drive_activity_user_detail_with_period_request_builder import GetOneDriveActivityUserDetailWithPeriodRequestBuilder

        return GetOneDriveActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_usage_account_counts_with_period(self,period: Optional[str] = None) -> GetOneDriveUsageAccountCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageAccountCounts method.
        param period: Usage: period='{period}'
        Returns: GetOneDriveUsageAccountCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_usage_account_counts_with_period.get_one_drive_usage_account_counts_with_period_request_builder import GetOneDriveUsageAccountCountsWithPeriodRequestBuilder

        return GetOneDriveUsageAccountCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_usage_account_detail_with_date(self,date: Optional[datetime.date] = None) -> GetOneDriveUsageAccountDetailWithDateRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageAccountDetail method.
        param date: Usage: date={date}
        Returns: GetOneDriveUsageAccountDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_one_drive_usage_account_detail_with_date.get_one_drive_usage_account_detail_with_date_request_builder import GetOneDriveUsageAccountDetailWithDateRequestBuilder

        return GetOneDriveUsageAccountDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_one_drive_usage_account_detail_with_period(self,period: Optional[str] = None) -> GetOneDriveUsageAccountDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageAccountDetail method.
        param period: Usage: period='{period}'
        Returns: GetOneDriveUsageAccountDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_usage_account_detail_with_period.get_one_drive_usage_account_detail_with_period_request_builder import GetOneDriveUsageAccountDetailWithPeriodRequestBuilder

        return GetOneDriveUsageAccountDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_usage_file_counts_with_period(self,period: Optional[str] = None) -> GetOneDriveUsageFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageFileCounts method.
        param period: Usage: period='{period}'
        Returns: GetOneDriveUsageFileCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_usage_file_counts_with_period.get_one_drive_usage_file_counts_with_period_request_builder import GetOneDriveUsageFileCountsWithPeriodRequestBuilder

        return GetOneDriveUsageFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_usage_storage_with_period(self,period: Optional[str] = None) -> GetOneDriveUsageStorageWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageStorage method.
        param period: Usage: period='{period}'
        Returns: GetOneDriveUsageStorageWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_usage_storage_with_period.get_one_drive_usage_storage_with_period_request_builder import GetOneDriveUsageStorageWithPeriodRequestBuilder

        return GetOneDriveUsageStorageWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time(self,end_date_time: Optional[datetime.datetime] = None, printer_id: Optional[str] = None, start_date_time: Optional[datetime.datetime] = None) -> GetPrinterArchivedPrintJobsWithPrinterIdWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the getPrinterArchivedPrintJobs method.
        param end_date_time: Usage: endDateTime={endDateTime}
        param printer_id: Usage: printerId='{printerId}'
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: GetPrinterArchivedPrintJobsWithPrinterIdWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if not end_date_time:
            raise TypeError("end_date_time cannot be null.")
        if not printer_id:
            raise TypeError("printer_id cannot be null.")
        if not start_date_time:
            raise TypeError("start_date_time cannot be null.")
        from .get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time.get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time_request_builder import GetPrinterArchivedPrintJobsWithPrinterIdWithStartDateTimeWithEndDateTimeRequestBuilder

        return GetPrinterArchivedPrintJobsWithPrinterIdWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, printer_id, start_date_time)
    
    def get_relying_party_detailed_summary_with_period(self,period: Optional[str] = None) -> GetRelyingPartyDetailedSummaryWithPeriodRequestBuilder:
        """
        Provides operations to call the getRelyingPartyDetailedSummary method.
        param period: Usage: period='{period}'
        Returns: GetRelyingPartyDetailedSummaryWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_relying_party_detailed_summary_with_period.get_relying_party_detailed_summary_with_period_request_builder import GetRelyingPartyDetailedSummaryWithPeriodRequestBuilder

        return GetRelyingPartyDetailedSummaryWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_activity_file_counts_with_period(self,period: Optional[str] = None) -> GetSharePointActivityFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointActivityFileCounts method.
        param period: Usage: period='{period}'
        Returns: GetSharePointActivityFileCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_activity_file_counts_with_period.get_share_point_activity_file_counts_with_period_request_builder import GetSharePointActivityFileCountsWithPeriodRequestBuilder

        return GetSharePointActivityFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_activity_pages_with_period(self,period: Optional[str] = None) -> GetSharePointActivityPagesWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointActivityPages method.
        param period: Usage: period='{period}'
        Returns: GetSharePointActivityPagesWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_activity_pages_with_period.get_share_point_activity_pages_with_period_request_builder import GetSharePointActivityPagesWithPeriodRequestBuilder

        return GetSharePointActivityPagesWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetSharePointActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointActivityUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetSharePointActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_activity_user_counts_with_period.get_share_point_activity_user_counts_with_period_request_builder import GetSharePointActivityUserCountsWithPeriodRequestBuilder

        return GetSharePointActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_activity_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetSharePointActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getSharePointActivityUserDetail method.
        param date: Usage: date={date}
        Returns: GetSharePointActivityUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_share_point_activity_user_detail_with_date.get_share_point_activity_user_detail_with_date_request_builder import GetSharePointActivityUserDetailWithDateRequestBuilder

        return GetSharePointActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_share_point_activity_user_detail_with_period(self,period: Optional[str] = None) -> GetSharePointActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointActivityUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetSharePointActivityUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_activity_user_detail_with_period.get_share_point_activity_user_detail_with_period_request_builder import GetSharePointActivityUserDetailWithPeriodRequestBuilder

        return GetSharePointActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_detail_with_date(self,date: Optional[datetime.date] = None) -> GetSharePointSiteUsageDetailWithDateRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageDetail method.
        param date: Usage: date={date}
        Returns: GetSharePointSiteUsageDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_share_point_site_usage_detail_with_date.get_share_point_site_usage_detail_with_date_request_builder import GetSharePointSiteUsageDetailWithDateRequestBuilder

        return GetSharePointSiteUsageDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_share_point_site_usage_detail_with_period(self,period: Optional[str] = None) -> GetSharePointSiteUsageDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageDetail method.
        param period: Usage: period='{period}'
        Returns: GetSharePointSiteUsageDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_site_usage_detail_with_period.get_share_point_site_usage_detail_with_period_request_builder import GetSharePointSiteUsageDetailWithPeriodRequestBuilder

        return GetSharePointSiteUsageDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_file_counts_with_period(self,period: Optional[str] = None) -> GetSharePointSiteUsageFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageFileCounts method.
        param period: Usage: period='{period}'
        Returns: GetSharePointSiteUsageFileCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_site_usage_file_counts_with_period.get_share_point_site_usage_file_counts_with_period_request_builder import GetSharePointSiteUsageFileCountsWithPeriodRequestBuilder

        return GetSharePointSiteUsageFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_pages_with_period(self,period: Optional[str] = None) -> GetSharePointSiteUsagePagesWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsagePages method.
        param period: Usage: period='{period}'
        Returns: GetSharePointSiteUsagePagesWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_site_usage_pages_with_period.get_share_point_site_usage_pages_with_period_request_builder import GetSharePointSiteUsagePagesWithPeriodRequestBuilder

        return GetSharePointSiteUsagePagesWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_site_counts_with_period(self,period: Optional[str] = None) -> GetSharePointSiteUsageSiteCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageSiteCounts method.
        param period: Usage: period='{period}'
        Returns: GetSharePointSiteUsageSiteCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_site_usage_site_counts_with_period.get_share_point_site_usage_site_counts_with_period_request_builder import GetSharePointSiteUsageSiteCountsWithPeriodRequestBuilder

        return GetSharePointSiteUsageSiteCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_storage_with_period(self,period: Optional[str] = None) -> GetSharePointSiteUsageStorageWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageStorage method.
        param period: Usage: period='{period}'
        Returns: GetSharePointSiteUsageStorageWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_site_usage_storage_with_period.get_share_point_site_usage_storage_with_period_request_builder import GetSharePointSiteUsageStorageWithPeriodRequestBuilder

        return GetSharePointSiteUsageStorageWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_activity_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessActivityCounts method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_activity_counts_with_period.get_skype_for_business_activity_counts_with_period_request_builder import GetSkypeForBusinessActivityCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessActivityUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_activity_user_counts_with_period.get_skype_for_business_activity_user_counts_with_period_request_builder import GetSkypeForBusinessActivityUserCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_activity_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetSkypeForBusinessActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessActivityUserDetail method.
        param date: Usage: date={date}
        Returns: GetSkypeForBusinessActivityUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_skype_for_business_activity_user_detail_with_date.get_skype_for_business_activity_user_detail_with_date_request_builder import GetSkypeForBusinessActivityUserDetailWithDateRequestBuilder

        return GetSkypeForBusinessActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_skype_for_business_activity_user_detail_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessActivityUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessActivityUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_activity_user_detail_with_period.get_skype_for_business_activity_user_detail_with_period_request_builder import GetSkypeForBusinessActivityUserDetailWithPeriodRequestBuilder

        return GetSkypeForBusinessActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_device_usage_distribution_user_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessDeviceUsageDistributionUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_device_usage_distribution_user_counts_with_period.get_skype_for_business_device_usage_distribution_user_counts_with_period_request_builder import GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_device_usage_user_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessDeviceUsageUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_device_usage_user_counts_with_period.get_skype_for_business_device_usage_user_counts_with_period_request_builder import GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_device_usage_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetSkypeForBusinessDeviceUsageUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessDeviceUsageUserDetail method.
        param date: Usage: date={date}
        Returns: GetSkypeForBusinessDeviceUsageUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_skype_for_business_device_usage_user_detail_with_date.get_skype_for_business_device_usage_user_detail_with_date_request_builder import GetSkypeForBusinessDeviceUsageUserDetailWithDateRequestBuilder

        return GetSkypeForBusinessDeviceUsageUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_skype_for_business_device_usage_user_detail_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessDeviceUsageUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_device_usage_user_detail_with_period.get_skype_for_business_device_usage_user_detail_with_period_request_builder import GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequestBuilder

        return GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_organizer_activity_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessOrganizerActivityCounts method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_organizer_activity_counts_with_period.get_skype_for_business_organizer_activity_counts_with_period_request_builder import GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_organizer_activity_minute_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessOrganizerActivityMinuteCounts method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_organizer_activity_minute_counts_with_period.get_skype_for_business_organizer_activity_minute_counts_with_period_request_builder import GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_organizer_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessOrganizerActivityUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_organizer_activity_user_counts_with_period.get_skype_for_business_organizer_activity_user_counts_with_period_request_builder import GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_participant_activity_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessParticipantActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessParticipantActivityCounts method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessParticipantActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_participant_activity_counts_with_period.get_skype_for_business_participant_activity_counts_with_period_request_builder import GetSkypeForBusinessParticipantActivityCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessParticipantActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_participant_activity_minute_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessParticipantActivityMinuteCounts method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_participant_activity_minute_counts_with_period.get_skype_for_business_participant_activity_minute_counts_with_period_request_builder import GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_participant_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessParticipantActivityUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_participant_activity_user_counts_with_period.get_skype_for_business_participant_activity_user_counts_with_period_request_builder import GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_peer_to_peer_activity_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessPeerToPeerActivityCounts method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_peer_to_peer_activity_counts_with_period.get_skype_for_business_peer_to_peer_activity_counts_with_period_request_builder import GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_peer_to_peer_activity_minute_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessPeerToPeerActivityMinuteCounts method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_peer_to_peer_activity_minute_counts_with_period.get_skype_for_business_peer_to_peer_activity_minute_counts_with_period_request_builder import GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_peer_to_peer_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessPeerToPeerActivityUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_peer_to_peer_activity_user_counts_with_period.get_skype_for_business_peer_to_peer_activity_user_counts_with_period_request_builder import GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_device_usage_distribution_total_user_counts_with_period(self,period: Optional[str] = None) -> GetTeamsDeviceUsageDistributionTotalUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageDistributionTotalUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsDeviceUsageDistributionTotalUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_device_usage_distribution_total_user_counts_with_period.get_teams_device_usage_distribution_total_user_counts_with_period_request_builder import GetTeamsDeviceUsageDistributionTotalUserCountsWithPeriodRequestBuilder

        return GetTeamsDeviceUsageDistributionTotalUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_device_usage_distribution_user_counts_with_period(self,period: Optional[str] = None) -> GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageDistributionUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_device_usage_distribution_user_counts_with_period.get_teams_device_usage_distribution_user_counts_with_period_request_builder import GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequestBuilder

        return GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_device_usage_total_user_counts_with_period(self,period: Optional[str] = None) -> GetTeamsDeviceUsageTotalUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageTotalUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsDeviceUsageTotalUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_device_usage_total_user_counts_with_period.get_teams_device_usage_total_user_counts_with_period_request_builder import GetTeamsDeviceUsageTotalUserCountsWithPeriodRequestBuilder

        return GetTeamsDeviceUsageTotalUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_device_usage_user_counts_with_period(self,period: Optional[str] = None) -> GetTeamsDeviceUsageUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsDeviceUsageUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_device_usage_user_counts_with_period.get_teams_device_usage_user_counts_with_period_request_builder import GetTeamsDeviceUsageUserCountsWithPeriodRequestBuilder

        return GetTeamsDeviceUsageUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_device_usage_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetTeamsDeviceUsageUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageUserDetail method.
        param date: Usage: date={date}
        Returns: GetTeamsDeviceUsageUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_teams_device_usage_user_detail_with_date.get_teams_device_usage_user_detail_with_date_request_builder import GetTeamsDeviceUsageUserDetailWithDateRequestBuilder

        return GetTeamsDeviceUsageUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_teams_device_usage_user_detail_with_period(self,period: Optional[str] = None) -> GetTeamsDeviceUsageUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetTeamsDeviceUsageUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_device_usage_user_detail_with_period.get_teams_device_usage_user_detail_with_period_request_builder import GetTeamsDeviceUsageUserDetailWithPeriodRequestBuilder

        return GetTeamsDeviceUsageUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_team_activity_counts_with_period(self,period: Optional[str] = None) -> GetTeamsTeamActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsTeamActivityCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsTeamActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_team_activity_counts_with_period.get_teams_team_activity_counts_with_period_request_builder import GetTeamsTeamActivityCountsWithPeriodRequestBuilder

        return GetTeamsTeamActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_team_activity_detail_with_date(self,date: Optional[datetime.date] = None) -> GetTeamsTeamActivityDetailWithDateRequestBuilder:
        """
        Provides operations to call the getTeamsTeamActivityDetail method.
        param date: Usage: date={date}
        Returns: GetTeamsTeamActivityDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_teams_team_activity_detail_with_date.get_teams_team_activity_detail_with_date_request_builder import GetTeamsTeamActivityDetailWithDateRequestBuilder

        return GetTeamsTeamActivityDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_teams_team_activity_detail_with_period(self,period: Optional[str] = None) -> GetTeamsTeamActivityDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsTeamActivityDetail method.
        param period: Usage: period='{period}'
        Returns: GetTeamsTeamActivityDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_team_activity_detail_with_period.get_teams_team_activity_detail_with_period_request_builder import GetTeamsTeamActivityDetailWithPeriodRequestBuilder

        return GetTeamsTeamActivityDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_team_activity_distribution_counts_with_period(self,period: Optional[str] = None) -> GetTeamsTeamActivityDistributionCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsTeamActivityDistributionCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsTeamActivityDistributionCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_team_activity_distribution_counts_with_period.get_teams_team_activity_distribution_counts_with_period_request_builder import GetTeamsTeamActivityDistributionCountsWithPeriodRequestBuilder

        return GetTeamsTeamActivityDistributionCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_team_counts_with_period(self,period: Optional[str] = None) -> GetTeamsTeamCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsTeamCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsTeamCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_team_counts_with_period.get_teams_team_counts_with_period_request_builder import GetTeamsTeamCountsWithPeriodRequestBuilder

        return GetTeamsTeamCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_counts_with_period(self,period: Optional[str] = None) -> GetTeamsUserActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsUserActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_user_activity_counts_with_period.get_teams_user_activity_counts_with_period_request_builder import GetTeamsUserActivityCountsWithPeriodRequestBuilder

        return GetTeamsUserActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_distribution_total_user_counts_with_period(self,period: Optional[str] = None) -> GetTeamsUserActivityDistributionTotalUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityDistributionTotalUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsUserActivityDistributionTotalUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_user_activity_distribution_total_user_counts_with_period.get_teams_user_activity_distribution_total_user_counts_with_period_request_builder import GetTeamsUserActivityDistributionTotalUserCountsWithPeriodRequestBuilder

        return GetTeamsUserActivityDistributionTotalUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_distribution_user_counts_with_period(self,period: Optional[str] = None) -> GetTeamsUserActivityDistributionUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityDistributionUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsUserActivityDistributionUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_user_activity_distribution_user_counts_with_period.get_teams_user_activity_distribution_user_counts_with_period_request_builder import GetTeamsUserActivityDistributionUserCountsWithPeriodRequestBuilder

        return GetTeamsUserActivityDistributionUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_total_counts_with_period(self,period: Optional[str] = None) -> GetTeamsUserActivityTotalCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityTotalCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsUserActivityTotalCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_user_activity_total_counts_with_period.get_teams_user_activity_total_counts_with_period_request_builder import GetTeamsUserActivityTotalCountsWithPeriodRequestBuilder

        return GetTeamsUserActivityTotalCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_total_distribution_counts_with_period(self,period: Optional[str] = None) -> GetTeamsUserActivityTotalDistributionCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityTotalDistributionCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsUserActivityTotalDistributionCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_user_activity_total_distribution_counts_with_period.get_teams_user_activity_total_distribution_counts_with_period_request_builder import GetTeamsUserActivityTotalDistributionCountsWithPeriodRequestBuilder

        return GetTeamsUserActivityTotalDistributionCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_total_user_counts_with_period(self,period: Optional[str] = None) -> GetTeamsUserActivityTotalUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityTotalUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsUserActivityTotalUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_user_activity_total_user_counts_with_period.get_teams_user_activity_total_user_counts_with_period_request_builder import GetTeamsUserActivityTotalUserCountsWithPeriodRequestBuilder

        return GetTeamsUserActivityTotalUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetTeamsUserActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetTeamsUserActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_user_activity_user_counts_with_period.get_teams_user_activity_user_counts_with_period_request_builder import GetTeamsUserActivityUserCountsWithPeriodRequestBuilder

        return GetTeamsUserActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetTeamsUserActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityUserDetail method.
        param date: Usage: date={date}
        Returns: GetTeamsUserActivityUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_teams_user_activity_user_detail_with_date.get_teams_user_activity_user_detail_with_date_request_builder import GetTeamsUserActivityUserDetailWithDateRequestBuilder

        return GetTeamsUserActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_teams_user_activity_user_detail_with_period(self,period: Optional[str] = None) -> GetTeamsUserActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetTeamsUserActivityUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_user_activity_user_detail_with_period.get_teams_user_activity_user_detail_with_period_request_builder import GetTeamsUserActivityUserDetailWithPeriodRequestBuilder

        return GetTeamsUserActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time(self,end_date_time: Optional[datetime.datetime] = None, start_date_time: Optional[datetime.datetime] = None, user_id: Optional[str] = None) -> GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the getUserArchivedPrintJobs method.
        param end_date_time: Usage: endDateTime={endDateTime}
        param start_date_time: Usage: startDateTime={startDateTime}
        param user_id: Usage: userId='{userId}'
        Returns: GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if not end_date_time:
            raise TypeError("end_date_time cannot be null.")
        if not start_date_time:
            raise TypeError("start_date_time cannot be null.")
        if not user_id:
            raise TypeError("user_id cannot be null.")
        from .get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time.get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time_request_builder import GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder

        return GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time, user_id)
    
    def get_yammer_activity_counts_with_period(self,period: Optional[str] = None) -> GetYammerActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerActivityCounts method.
        param period: Usage: period='{period}'
        Returns: GetYammerActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_activity_counts_with_period.get_yammer_activity_counts_with_period_request_builder import GetYammerActivityCountsWithPeriodRequestBuilder

        return GetYammerActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetYammerActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerActivityUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetYammerActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_activity_user_counts_with_period.get_yammer_activity_user_counts_with_period_request_builder import GetYammerActivityUserCountsWithPeriodRequestBuilder

        return GetYammerActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_activity_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetYammerActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getYammerActivityUserDetail method.
        param date: Usage: date={date}
        Returns: GetYammerActivityUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_yammer_activity_user_detail_with_date.get_yammer_activity_user_detail_with_date_request_builder import GetYammerActivityUserDetailWithDateRequestBuilder

        return GetYammerActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_yammer_activity_user_detail_with_period(self,period: Optional[str] = None) -> GetYammerActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerActivityUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetYammerActivityUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_activity_user_detail_with_period.get_yammer_activity_user_detail_with_period_request_builder import GetYammerActivityUserDetailWithPeriodRequestBuilder

        return GetYammerActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_device_usage_distribution_user_counts_with_period(self,period: Optional[str] = None) -> GetYammerDeviceUsageDistributionUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerDeviceUsageDistributionUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetYammerDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_device_usage_distribution_user_counts_with_period.get_yammer_device_usage_distribution_user_counts_with_period_request_builder import GetYammerDeviceUsageDistributionUserCountsWithPeriodRequestBuilder

        return GetYammerDeviceUsageDistributionUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_device_usage_user_counts_with_period(self,period: Optional[str] = None) -> GetYammerDeviceUsageUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerDeviceUsageUserCounts method.
        param period: Usage: period='{period}'
        Returns: GetYammerDeviceUsageUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_device_usage_user_counts_with_period.get_yammer_device_usage_user_counts_with_period_request_builder import GetYammerDeviceUsageUserCountsWithPeriodRequestBuilder

        return GetYammerDeviceUsageUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_device_usage_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetYammerDeviceUsageUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getYammerDeviceUsageUserDetail method.
        param date: Usage: date={date}
        Returns: GetYammerDeviceUsageUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_yammer_device_usage_user_detail_with_date.get_yammer_device_usage_user_detail_with_date_request_builder import GetYammerDeviceUsageUserDetailWithDateRequestBuilder

        return GetYammerDeviceUsageUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_yammer_device_usage_user_detail_with_period(self,period: Optional[str] = None) -> GetYammerDeviceUsageUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerDeviceUsageUserDetail method.
        param period: Usage: period='{period}'
        Returns: GetYammerDeviceUsageUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_device_usage_user_detail_with_period.get_yammer_device_usage_user_detail_with_period_request_builder import GetYammerDeviceUsageUserDetailWithPeriodRequestBuilder

        return GetYammerDeviceUsageUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_groups_activity_counts_with_period(self,period: Optional[str] = None) -> GetYammerGroupsActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerGroupsActivityCounts method.
        param period: Usage: period='{period}'
        Returns: GetYammerGroupsActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_groups_activity_counts_with_period.get_yammer_groups_activity_counts_with_period_request_builder import GetYammerGroupsActivityCountsWithPeriodRequestBuilder

        return GetYammerGroupsActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_groups_activity_detail_with_date(self,date: Optional[datetime.date] = None) -> GetYammerGroupsActivityDetailWithDateRequestBuilder:
        """
        Provides operations to call the getYammerGroupsActivityDetail method.
        param date: Usage: date={date}
        Returns: GetYammerGroupsActivityDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_yammer_groups_activity_detail_with_date.get_yammer_groups_activity_detail_with_date_request_builder import GetYammerGroupsActivityDetailWithDateRequestBuilder

        return GetYammerGroupsActivityDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_yammer_groups_activity_detail_with_period(self,period: Optional[str] = None) -> GetYammerGroupsActivityDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerGroupsActivityDetail method.
        param period: Usage: period='{period}'
        Returns: GetYammerGroupsActivityDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_groups_activity_detail_with_period.get_yammer_groups_activity_detail_with_period_request_builder import GetYammerGroupsActivityDetailWithPeriodRequestBuilder

        return GetYammerGroupsActivityDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_groups_activity_group_counts_with_period(self,period: Optional[str] = None) -> GetYammerGroupsActivityGroupCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerGroupsActivityGroupCounts method.
        param period: Usage: period='{period}'
        Returns: GetYammerGroupsActivityGroupCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_groups_activity_group_counts_with_period.get_yammer_groups_activity_group_counts_with_period_request_builder import GetYammerGroupsActivityGroupCountsWithPeriodRequestBuilder

        return GetYammerGroupsActivityGroupCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def managed_device_enrollment_abandonment_details_with_skip_with_top_with_filter_with_skip_token(self,filter: Optional[str] = None, skip: Optional[int] = None, skip_token: Optional[str] = None, top: Optional[int] = None) -> ManagedDeviceEnrollmentAbandonmentDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentAbandonmentDetails method.
        param filter: Usage: filter='{filter}'
        param skip: Usage: skip={skip}
        param skip_token: Usage: skipToken='{skipToken}'
        param top: Usage: top={top}
        Returns: ManagedDeviceEnrollmentAbandonmentDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder
        """
        if not filter:
            raise TypeError("filter cannot be null.")
        if not skip:
            raise TypeError("skip cannot be null.")
        if not skip_token:
            raise TypeError("skip_token cannot be null.")
        if not top:
            raise TypeError("top cannot be null.")
        from .managed_device_enrollment_abandonment_details_with_skip_with_top_with_filter_with_skip_token.managed_device_enrollment_abandonment_details_with_skip_with_top_with_filter_with_skip_token_request_builder import ManagedDeviceEnrollmentAbandonmentDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder

        return ManagedDeviceEnrollmentAbandonmentDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder(self.request_adapter, self.path_parameters, filter, skip, skip_token, top)
    
    def managed_device_enrollment_abandonment_summary_with_skip_with_top_with_filter_with_skip_token(self,filter: Optional[str] = None, skip: Optional[int] = None, skip_token: Optional[str] = None, top: Optional[int] = None) -> ManagedDeviceEnrollmentAbandonmentSummaryWithSkipWithTopWithFilterWithSkipTokenRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentAbandonmentSummary method.
        param filter: Usage: filter='{filter}'
        param skip: Usage: skip={skip}
        param skip_token: Usage: skipToken='{skipToken}'
        param top: Usage: top={top}
        Returns: ManagedDeviceEnrollmentAbandonmentSummaryWithSkipWithTopWithFilterWithSkipTokenRequestBuilder
        """
        if not filter:
            raise TypeError("filter cannot be null.")
        if not skip:
            raise TypeError("skip cannot be null.")
        if not skip_token:
            raise TypeError("skip_token cannot be null.")
        if not top:
            raise TypeError("top cannot be null.")
        from .managed_device_enrollment_abandonment_summary_with_skip_with_top_with_filter_with_skip_token.managed_device_enrollment_abandonment_summary_with_skip_with_top_with_filter_with_skip_token_request_builder import ManagedDeviceEnrollmentAbandonmentSummaryWithSkipWithTopWithFilterWithSkipTokenRequestBuilder

        return ManagedDeviceEnrollmentAbandonmentSummaryWithSkipWithTopWithFilterWithSkipTokenRequestBuilder(self.request_adapter, self.path_parameters, filter, skip, skip_token, top)
    
    def managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token(self,filter: Optional[str] = None, skip: Optional[int] = None, skip_token: Optional[str] = None, top: Optional[int] = None) -> ManagedDeviceEnrollmentFailureDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentFailureDetails method.
        param filter: Usage: filter='{filter}'
        param skip: Usage: skip={skip}
        param skip_token: Usage: skipToken='{skipToken}'
        param top: Usage: top={top}
        Returns: ManagedDeviceEnrollmentFailureDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder
        """
        if not filter:
            raise TypeError("filter cannot be null.")
        if not skip:
            raise TypeError("skip cannot be null.")
        if not skip_token:
            raise TypeError("skip_token cannot be null.")
        if not top:
            raise TypeError("top cannot be null.")
        from .managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token.managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token_request_builder import ManagedDeviceEnrollmentFailureDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder

        return ManagedDeviceEnrollmentFailureDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder(self.request_adapter, self.path_parameters, filter, skip, skip_token, top)
    
    def managed_device_enrollment_top_failures_with_period(self,period: Optional[str] = None) -> ManagedDeviceEnrollmentTopFailuresWithPeriodRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentTopFailures method.
        param period: Usage: period='{period}'
        Returns: ManagedDeviceEnrollmentTopFailuresWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .managed_device_enrollment_top_failures_with_period.managed_device_enrollment_top_failures_with_period_request_builder import ManagedDeviceEnrollmentTopFailuresWithPeriodRequestBuilder

        return ManagedDeviceEnrollmentTopFailuresWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    async def patch(self,body: Optional[ReportRoot] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[ReportRoot]:
        """
        Update reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ReportRoot]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.report_root import ReportRoot

        return await self.request_adapter.send_async(request_info, ReportRoot, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Get reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[ReportRoot] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ReportsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ReportsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ReportsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def app_credential_sign_in_activities(self) -> AppCredentialSignInActivitiesRequestBuilder:
        """
        Provides operations to manage the appCredentialSignInActivities property of the microsoft.graph.reportRoot entity.
        """
        from .app_credential_sign_in_activities.app_credential_sign_in_activities_request_builder import AppCredentialSignInActivitiesRequestBuilder

        return AppCredentialSignInActivitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def application_sign_in_detailed_summary(self) -> ApplicationSignInDetailedSummaryRequestBuilder:
        """
        Provides operations to manage the applicationSignInDetailedSummary property of the microsoft.graph.reportRoot entity.
        """
        from .application_sign_in_detailed_summary.application_sign_in_detailed_summary_request_builder import ApplicationSignInDetailedSummaryRequestBuilder

        return ApplicationSignInDetailedSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_methods(self) -> AuthenticationMethodsRequestBuilder:
        """
        Provides operations to manage the authenticationMethods property of the microsoft.graph.reportRoot entity.
        """
        from .authentication_methods.authentication_methods_request_builder import AuthenticationMethodsRequestBuilder

        return AuthenticationMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def credential_user_registration_details(self) -> CredentialUserRegistrationDetailsRequestBuilder:
        """
        Provides operations to manage the credentialUserRegistrationDetails property of the microsoft.graph.reportRoot entity.
        """
        from .credential_user_registration_details.credential_user_registration_details_request_builder import CredentialUserRegistrationDetailsRequestBuilder

        return CredentialUserRegistrationDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daily_print_usage(self) -> DailyPrintUsageRequestBuilder:
        """
        Provides operations to manage the dailyPrintUsage property of the microsoft.graph.reportRoot entity.
        """
        from .daily_print_usage.daily_print_usage_request_builder import DailyPrintUsageRequestBuilder

        return DailyPrintUsageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daily_print_usage_by_printer(self) -> DailyPrintUsageByPrinterRequestBuilder:
        """
        Provides operations to manage the dailyPrintUsageByPrinter property of the microsoft.graph.reportRoot entity.
        """
        from .daily_print_usage_by_printer.daily_print_usage_by_printer_request_builder import DailyPrintUsageByPrinterRequestBuilder

        return DailyPrintUsageByPrinterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daily_print_usage_by_user(self) -> DailyPrintUsageByUserRequestBuilder:
        """
        Provides operations to manage the dailyPrintUsageByUser property of the microsoft.graph.reportRoot entity.
        """
        from .daily_print_usage_by_user.daily_print_usage_by_user_request_builder import DailyPrintUsageByUserRequestBuilder

        return DailyPrintUsageByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daily_print_usage_summaries_by_printer(self) -> DailyPrintUsageSummariesByPrinterRequestBuilder:
        """
        Provides operations to manage the dailyPrintUsageSummariesByPrinter property of the microsoft.graph.reportRoot entity.
        """
        from .daily_print_usage_summaries_by_printer.daily_print_usage_summaries_by_printer_request_builder import DailyPrintUsageSummariesByPrinterRequestBuilder

        return DailyPrintUsageSummariesByPrinterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daily_print_usage_summaries_by_user(self) -> DailyPrintUsageSummariesByUserRequestBuilder:
        """
        Provides operations to manage the dailyPrintUsageSummariesByUser property of the microsoft.graph.reportRoot entity.
        """
        from .daily_print_usage_summaries_by_user.daily_print_usage_summaries_by_user_request_builder import DailyPrintUsageSummariesByUserRequestBuilder

        return DailyPrintUsageSummariesByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_device_activity(self) -> DeviceConfigurationDeviceActivityRequestBuilder:
        """
        Provides operations to call the deviceConfigurationDeviceActivity method.
        """
        from .device_configuration_device_activity.device_configuration_device_activity_request_builder import DeviceConfigurationDeviceActivityRequestBuilder

        return DeviceConfigurationDeviceActivityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_user_activity(self) -> DeviceConfigurationUserActivityRequestBuilder:
        """
        Provides operations to call the deviceConfigurationUserActivity method.
        """
        from .device_configuration_user_activity.device_configuration_user_activity_request_builder import DeviceConfigurationUserActivityRequestBuilder

        return DeviceConfigurationUserActivityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_attack_simulation_repeat_offenders(self) -> GetAttackSimulationRepeatOffendersRequestBuilder:
        """
        Provides operations to call the getAttackSimulationRepeatOffenders method.
        """
        from .get_attack_simulation_repeat_offenders.get_attack_simulation_repeat_offenders_request_builder import GetAttackSimulationRepeatOffendersRequestBuilder

        return GetAttackSimulationRepeatOffendersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_attack_simulation_simulation_user_coverage(self) -> GetAttackSimulationSimulationUserCoverageRequestBuilder:
        """
        Provides operations to call the getAttackSimulationSimulationUserCoverage method.
        """
        from .get_attack_simulation_simulation_user_coverage.get_attack_simulation_simulation_user_coverage_request_builder import GetAttackSimulationSimulationUserCoverageRequestBuilder

        return GetAttackSimulationSimulationUserCoverageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_attack_simulation_training_user_coverage(self) -> GetAttackSimulationTrainingUserCoverageRequestBuilder:
        """
        Provides operations to call the getAttackSimulationTrainingUserCoverage method.
        """
        from .get_attack_simulation_training_user_coverage.get_attack_simulation_training_user_coverage_request_builder import GetAttackSimulationTrainingUserCoverageRequestBuilder

        return GetAttackSimulationTrainingUserCoverageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_credential_user_registration_count(self) -> GetCredentialUserRegistrationCountRequestBuilder:
        """
        Provides operations to call the getCredentialUserRegistrationCount method.
        """
        from .get_credential_user_registration_count.get_credential_user_registration_count_request_builder import GetCredentialUserRegistrationCountRequestBuilder

        return GetCredentialUserRegistrationCountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_office365_activation_counts(self) -> GetOffice365ActivationCountsRequestBuilder:
        """
        Provides operations to call the getOffice365ActivationCounts method.
        """
        from .get_office365_activation_counts.get_office365_activation_counts_request_builder import GetOffice365ActivationCountsRequestBuilder

        return GetOffice365ActivationCountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_office365_activations_user_counts(self) -> GetOffice365ActivationsUserCountsRequestBuilder:
        """
        Provides operations to call the getOffice365ActivationsUserCounts method.
        """
        from .get_office365_activations_user_counts.get_office365_activations_user_counts_request_builder import GetOffice365ActivationsUserCountsRequestBuilder

        return GetOffice365ActivationsUserCountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_office365_activations_user_detail(self) -> GetOffice365ActivationsUserDetailRequestBuilder:
        """
        Provides operations to call the getOffice365ActivationsUserDetail method.
        """
        from .get_office365_activations_user_detail.get_office365_activations_user_detail_request_builder import GetOffice365ActivationsUserDetailRequestBuilder

        return GetOffice365ActivationsUserDetailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_enrollment_failure_details(self) -> ManagedDeviceEnrollmentFailureDetailsRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentFailureDetails method.
        """
        from .managed_device_enrollment_failure_details.managed_device_enrollment_failure_details_request_builder import ManagedDeviceEnrollmentFailureDetailsRequestBuilder

        return ManagedDeviceEnrollmentFailureDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_enrollment_failure_trends(self) -> ManagedDeviceEnrollmentFailureTrendsRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentFailureTrends method.
        """
        from .managed_device_enrollment_failure_trends.managed_device_enrollment_failure_trends_request_builder import ManagedDeviceEnrollmentFailureTrendsRequestBuilder

        return ManagedDeviceEnrollmentFailureTrendsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_enrollment_top_failures(self) -> ManagedDeviceEnrollmentTopFailuresRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentTopFailures method.
        """
        from .managed_device_enrollment_top_failures.managed_device_enrollment_top_failures_request_builder import ManagedDeviceEnrollmentTopFailuresRequestBuilder

        return ManagedDeviceEnrollmentTopFailuresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monthly_print_usage_by_printer(self) -> MonthlyPrintUsageByPrinterRequestBuilder:
        """
        Provides operations to manage the monthlyPrintUsageByPrinter property of the microsoft.graph.reportRoot entity.
        """
        from .monthly_print_usage_by_printer.monthly_print_usage_by_printer_request_builder import MonthlyPrintUsageByPrinterRequestBuilder

        return MonthlyPrintUsageByPrinterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monthly_print_usage_by_user(self) -> MonthlyPrintUsageByUserRequestBuilder:
        """
        Provides operations to manage the monthlyPrintUsageByUser property of the microsoft.graph.reportRoot entity.
        """
        from .monthly_print_usage_by_user.monthly_print_usage_by_user_request_builder import MonthlyPrintUsageByUserRequestBuilder

        return MonthlyPrintUsageByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monthly_print_usage_summaries_by_printer(self) -> MonthlyPrintUsageSummariesByPrinterRequestBuilder:
        """
        Provides operations to manage the monthlyPrintUsageSummariesByPrinter property of the microsoft.graph.reportRoot entity.
        """
        from .monthly_print_usage_summaries_by_printer.monthly_print_usage_summaries_by_printer_request_builder import MonthlyPrintUsageSummariesByPrinterRequestBuilder

        return MonthlyPrintUsageSummariesByPrinterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monthly_print_usage_summaries_by_user(self) -> MonthlyPrintUsageSummariesByUserRequestBuilder:
        """
        Provides operations to manage the monthlyPrintUsageSummariesByUser property of the microsoft.graph.reportRoot entity.
        """
        from .monthly_print_usage_summaries_by_user.monthly_print_usage_summaries_by_user_request_builder import MonthlyPrintUsageSummariesByUserRequestBuilder

        return MonthlyPrintUsageSummariesByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def partners(self) -> PartnersRequestBuilder:
        """
        Provides operations to manage the partners property of the microsoft.graph.reportRoot entity.
        """
        from .partners.partners_request_builder import PartnersRequestBuilder

        return PartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security(self) -> SecurityRequestBuilder:
        """
        Provides operations to manage the security property of the microsoft.graph.reportRoot entity.
        """
        from .security.security_request_builder import SecurityRequestBuilder

        return SecurityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_activity(self) -> ServiceActivityRequestBuilder:
        """
        Provides operations to manage the serviceActivity property of the microsoft.graph.reportRoot entity.
        """
        from .service_activity.service_activity_request_builder import ServiceActivityRequestBuilder

        return ServiceActivityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_principal_sign_in_activities(self) -> ServicePrincipalSignInActivitiesRequestBuilder:
        """
        Provides operations to manage the servicePrincipalSignInActivities property of the microsoft.graph.reportRoot entity.
        """
        from .service_principal_sign_in_activities.service_principal_sign_in_activities_request_builder import ServicePrincipalSignInActivitiesRequestBuilder

        return ServicePrincipalSignInActivitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sla(self) -> SlaRequestBuilder:
        """
        Provides operations to manage the sla property of the microsoft.graph.reportRoot entity.
        """
        from .sla.sla_request_builder import SlaRequestBuilder

        return SlaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_credential_usage_details(self) -> UserCredentialUsageDetailsRequestBuilder:
        """
        Provides operations to manage the userCredentialUsageDetails property of the microsoft.graph.reportRoot entity.
        """
        from .user_credential_usage_details.user_credential_usage_details_request_builder import UserCredentialUsageDetailsRequestBuilder

        return UserCredentialUsageDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_insights(self) -> UserInsightsRequestBuilder:
        """
        Provides operations to manage the userInsights property of the microsoft.graph.reportRoot entity.
        """
        from .user_insights.user_insights_request_builder import UserInsightsRequestBuilder

        return UserInsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Get reports
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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

    

