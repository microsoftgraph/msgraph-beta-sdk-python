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

user = lazy_import('msgraph.generated.models.user')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
activate_service_plan_request_builder = lazy_import('msgraph.generated.users.item.activate_service_plan.activate_service_plan_request_builder')
activities_request_builder = lazy_import('msgraph.generated.users.item.activities.activities_request_builder')
user_activity_item_request_builder = lazy_import('msgraph.generated.users.item.activities.item.user_activity_item_request_builder')
agreement_acceptances_request_builder = lazy_import('msgraph.generated.users.item.agreement_acceptances.agreement_acceptances_request_builder')
agreement_acceptance_item_request_builder = lazy_import('msgraph.generated.users.item.agreement_acceptances.item.agreement_acceptance_item_request_builder')
analytics_request_builder = lazy_import('msgraph.generated.users.item.analytics.analytics_request_builder')
app_consent_requests_for_approval_request_builder = lazy_import('msgraph.generated.users.item.app_consent_requests_for_approval.app_consent_requests_for_approval_request_builder')
app_consent_request_item_request_builder = lazy_import('msgraph.generated.users.item.app_consent_requests_for_approval.item.app_consent_request_item_request_builder')
app_role_assigned_resources_request_builder = lazy_import('msgraph.generated.users.item.app_role_assigned_resources.app_role_assigned_resources_request_builder')
service_principal_item_request_builder = lazy_import('msgraph.generated.users.item.app_role_assigned_resources.item.service_principal_item_request_builder')
app_role_assignments_request_builder = lazy_import('msgraph.generated.users.item.app_role_assignments.app_role_assignments_request_builder')
app_role_assignment_item_request_builder = lazy_import('msgraph.generated.users.item.app_role_assignments.item.app_role_assignment_item_request_builder')
approvals_request_builder = lazy_import('msgraph.generated.users.item.approvals.approvals_request_builder')
approval_item_request_builder = lazy_import('msgraph.generated.users.item.approvals.item.approval_item_request_builder')
assign_license_request_builder = lazy_import('msgraph.generated.users.item.assign_license.assign_license_request_builder')
authentication_request_builder = lazy_import('msgraph.generated.users.item.authentication.authentication_request_builder')
calendar_request_builder = lazy_import('msgraph.generated.users.item.calendar.calendar_request_builder')
calendar_groups_request_builder = lazy_import('msgraph.generated.users.item.calendar_groups.calendar_groups_request_builder')
calendar_group_item_request_builder = lazy_import('msgraph.generated.users.item.calendar_groups.item.calendar_group_item_request_builder')
calendars_request_builder = lazy_import('msgraph.generated.users.item.calendars.calendars_request_builder')
calendar_item_request_builder = lazy_import('msgraph.generated.users.item.calendars.item.calendar_item_request_builder')
calendar_view_request_builder = lazy_import('msgraph.generated.users.item.calendar_view.calendar_view_request_builder')
event_item_request_builder = lazy_import('msgraph.generated.users.item.calendar_view.item.event_item_request_builder')
change_password_request_builder = lazy_import('msgraph.generated.users.item.change_password.change_password_request_builder')
chats_request_builder = lazy_import('msgraph.generated.users.item.chats.chats_request_builder')
chat_item_request_builder = lazy_import('msgraph.generated.users.item.chats.item.chat_item_request_builder')
check_member_groups_request_builder = lazy_import('msgraph.generated.users.item.check_member_groups.check_member_groups_request_builder')
check_member_objects_request_builder = lazy_import('msgraph.generated.users.item.check_member_objects.check_member_objects_request_builder')
cloud_p_cs_request_builder = lazy_import('msgraph.generated.users.item.cloud_p_cs.cloud_p_cs_request_builder')
cloud_p_c_item_request_builder = lazy_import('msgraph.generated.users.item.cloud_p_cs.item.cloud_p_c_item_request_builder')
contact_folders_request_builder = lazy_import('msgraph.generated.users.item.contact_folders.contact_folders_request_builder')
contact_folder_item_request_builder = lazy_import('msgraph.generated.users.item.contact_folders.item.contact_folder_item_request_builder')
contacts_request_builder = lazy_import('msgraph.generated.users.item.contacts.contacts_request_builder')
contact_item_request_builder = lazy_import('msgraph.generated.users.item.contacts.item.contact_item_request_builder')
created_objects_request_builder = lazy_import('msgraph.generated.users.item.created_objects.created_objects_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.users.item.created_objects.item.directory_object_item_request_builder')
device_enrollment_configurations_request_builder = lazy_import('msgraph.generated.users.item.device_enrollment_configurations.device_enrollment_configurations_request_builder')
device_enrollment_configuration_item_request_builder = lazy_import('msgraph.generated.users.item.device_enrollment_configurations.item.device_enrollment_configuration_item_request_builder')
device_management_troubleshooting_events_request_builder = lazy_import('msgraph.generated.users.item.device_management_troubleshooting_events.device_management_troubleshooting_events_request_builder')
device_management_troubleshooting_event_item_request_builder = lazy_import('msgraph.generated.users.item.device_management_troubleshooting_events.item.device_management_troubleshooting_event_item_request_builder')
devices_request_builder = lazy_import('msgraph.generated.users.item.devices.devices_request_builder')
device_item_request_builder = lazy_import('msgraph.generated.users.item.devices.item.device_item_request_builder')
direct_reports_request_builder = lazy_import('msgraph.generated.users.item.direct_reports.direct_reports_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.users.item.direct_reports.item.directory_object_item_request_builder')
drive_request_builder = lazy_import('msgraph.generated.users.item.drive.drive_request_builder')
drives_request_builder = lazy_import('msgraph.generated.users.item.drives.drives_request_builder')
drive_item_request_builder = lazy_import('msgraph.generated.users.item.drives.item.drive_item_request_builder')
events_request_builder = lazy_import('msgraph.generated.users.item.events.events_request_builder')
event_item_request_builder = lazy_import('msgraph.generated.users.item.events.item.event_item_request_builder')
export_device_and_app_management_data_request_builder = lazy_import('msgraph.generated.users.item.export_device_and_app_management_data.export_device_and_app_management_data_request_builder')
export_device_and_app_management_data_with_skip_with_top_request_builder = lazy_import('msgraph.generated.users.item.export_device_and_app_management_data_with_skip_with_top.export_device_and_app_management_data_with_skip_with_top_request_builder')
export_personal_data_request_builder = lazy_import('msgraph.generated.users.item.export_personal_data.export_personal_data_request_builder')
extensions_request_builder = lazy_import('msgraph.generated.users.item.extensions.extensions_request_builder')
extension_item_request_builder = lazy_import('msgraph.generated.users.item.extensions.item.extension_item_request_builder')
find_meeting_times_request_builder = lazy_import('msgraph.generated.users.item.find_meeting_times.find_meeting_times_request_builder')
find_room_lists_request_builder = lazy_import('msgraph.generated.users.item.find_room_lists.find_room_lists_request_builder')
find_rooms_request_builder = lazy_import('msgraph.generated.users.item.find_rooms.find_rooms_request_builder')
find_rooms_with_room_list_request_builder = lazy_import('msgraph.generated.users.item.find_rooms_with_room_list.find_rooms_with_room_list_request_builder')
followed_sites_request_builder = lazy_import('msgraph.generated.users.item.followed_sites.followed_sites_request_builder')
site_item_request_builder = lazy_import('msgraph.generated.users.item.followed_sites.item.site_item_request_builder')
get_effective_device_enrollment_configurations_request_builder = lazy_import('msgraph.generated.users.item.get_effective_device_enrollment_configurations.get_effective_device_enrollment_configurations_request_builder')
get_logged_on_managed_devices_request_builder = lazy_import('msgraph.generated.users.item.get_logged_on_managed_devices.get_logged_on_managed_devices_request_builder')
get_mail_tips_request_builder = lazy_import('msgraph.generated.users.item.get_mail_tips.get_mail_tips_request_builder')
get_managed_app_diagnostic_statuses_request_builder = lazy_import('msgraph.generated.users.item.get_managed_app_diagnostic_statuses.get_managed_app_diagnostic_statuses_request_builder')
get_managed_app_policies_request_builder = lazy_import('msgraph.generated.users.item.get_managed_app_policies.get_managed_app_policies_request_builder')
get_managed_devices_with_app_failures_request_builder = lazy_import('msgraph.generated.users.item.get_managed_devices_with_app_failures.get_managed_devices_with_app_failures_request_builder')
get_managed_devices_with_failed_or_pending_apps_request_builder = lazy_import('msgraph.generated.users.item.get_managed_devices_with_failed_or_pending_apps.get_managed_devices_with_failed_or_pending_apps_request_builder')
get_member_groups_request_builder = lazy_import('msgraph.generated.users.item.get_member_groups.get_member_groups_request_builder')
get_member_objects_request_builder = lazy_import('msgraph.generated.users.item.get_member_objects.get_member_objects_request_builder')
inference_classification_request_builder = lazy_import('msgraph.generated.users.item.inference_classification.inference_classification_request_builder')
information_protection_request_builder = lazy_import('msgraph.generated.users.item.information_protection.information_protection_request_builder')
insights_request_builder = lazy_import('msgraph.generated.users.item.insights.insights_request_builder')
invalidate_all_refresh_tokens_request_builder = lazy_import('msgraph.generated.users.item.invalidate_all_refresh_tokens.invalidate_all_refresh_tokens_request_builder')
is_managed_app_user_blocked_request_builder = lazy_import('msgraph.generated.users.item.is_managed_app_user_blocked.is_managed_app_user_blocked_request_builder')
joined_groups_request_builder = lazy_import('msgraph.generated.users.item.joined_groups.joined_groups_request_builder')
joined_teams_request_builder = lazy_import('msgraph.generated.users.item.joined_teams.joined_teams_request_builder')
team_item_request_builder = lazy_import('msgraph.generated.users.item.joined_teams.item.team_item_request_builder')
license_details_request_builder = lazy_import('msgraph.generated.users.item.license_details.license_details_request_builder')
license_details_item_request_builder = lazy_import('msgraph.generated.users.item.license_details.item.license_details_item_request_builder')
mail_folders_request_builder = lazy_import('msgraph.generated.users.item.mail_folders.mail_folders_request_builder')
mail_folder_item_request_builder = lazy_import('msgraph.generated.users.item.mail_folders.item.mail_folder_item_request_builder')
managed_app_registrations_request_builder = lazy_import('msgraph.generated.users.item.managed_app_registrations.managed_app_registrations_request_builder')
managed_app_registration_item_request_builder = lazy_import('msgraph.generated.users.item.managed_app_registrations.item.managed_app_registration_item_request_builder')
managed_devices_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.managed_devices_request_builder')
managed_device_item_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.managed_device_item_request_builder')
manager_request_builder = lazy_import('msgraph.generated.users.item.manager.manager_request_builder')
member_of_request_builder = lazy_import('msgraph.generated.users.item.member_of.member_of_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.users.item.member_of.item.directory_object_item_request_builder')
messages_request_builder = lazy_import('msgraph.generated.users.item.messages.messages_request_builder')
message_item_request_builder = lazy_import('msgraph.generated.users.item.messages.item.message_item_request_builder')
mobile_app_intent_and_states_request_builder = lazy_import('msgraph.generated.users.item.mobile_app_intent_and_states.mobile_app_intent_and_states_request_builder')
mobile_app_intent_and_state_item_request_builder = lazy_import('msgraph.generated.users.item.mobile_app_intent_and_states.item.mobile_app_intent_and_state_item_request_builder')
mobile_app_troubleshooting_events_request_builder = lazy_import('msgraph.generated.users.item.mobile_app_troubleshooting_events.mobile_app_troubleshooting_events_request_builder')
mobile_app_troubleshooting_event_item_request_builder = lazy_import('msgraph.generated.users.item.mobile_app_troubleshooting_events.item.mobile_app_troubleshooting_event_item_request_builder')
notifications_request_builder = lazy_import('msgraph.generated.users.item.notifications.notifications_request_builder')
notification_item_request_builder = lazy_import('msgraph.generated.users.item.notifications.item.notification_item_request_builder')
oauth2_permission_grants_request_builder = lazy_import('msgraph.generated.users.item.oauth2_permission_grants.oauth2_permission_grants_request_builder')
o_auth2_permission_grant_item_request_builder = lazy_import('msgraph.generated.users.item.oauth2_permission_grants.item.o_auth2_permission_grant_item_request_builder')
onenote_request_builder = lazy_import('msgraph.generated.users.item.onenote.onenote_request_builder')
online_meetings_request_builder = lazy_import('msgraph.generated.users.item.online_meetings.online_meetings_request_builder')
online_meeting_item_request_builder = lazy_import('msgraph.generated.users.item.online_meetings.item.online_meeting_item_request_builder')
outlook_request_builder = lazy_import('msgraph.generated.users.item.outlook.outlook_request_builder')
owned_devices_request_builder = lazy_import('msgraph.generated.users.item.owned_devices.owned_devices_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.users.item.owned_devices.item.directory_object_item_request_builder')
owned_objects_request_builder = lazy_import('msgraph.generated.users.item.owned_objects.owned_objects_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.users.item.owned_objects.item.directory_object_item_request_builder')
pending_access_review_instances_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.pending_access_review_instances_request_builder')
access_review_instance_item_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.access_review_instance_item_request_builder')
people_request_builder = lazy_import('msgraph.generated.users.item.people.people_request_builder')
person_item_request_builder = lazy_import('msgraph.generated.users.item.people.item.person_item_request_builder')
photo_request_builder = lazy_import('msgraph.generated.users.item.photo.photo_request_builder')
photos_request_builder = lazy_import('msgraph.generated.users.item.photos.photos_request_builder')
profile_photo_item_request_builder = lazy_import('msgraph.generated.users.item.photos.item.profile_photo_item_request_builder')
planner_request_builder = lazy_import('msgraph.generated.users.item.planner.planner_request_builder')
presence_request_builder = lazy_import('msgraph.generated.users.item.presence.presence_request_builder')
profile_request_builder = lazy_import('msgraph.generated.users.item.profile.profile_request_builder')
registered_devices_request_builder = lazy_import('msgraph.generated.users.item.registered_devices.registered_devices_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.users.item.registered_devices.item.directory_object_item_request_builder')
reminder_view_with_start_date_time_with_end_date_time_request_builder = lazy_import('msgraph.generated.users.item.reminder_view_with_start_date_time_with_end_date_time.reminder_view_with_start_date_time_with_end_date_time_request_builder')
remove_all_devices_from_management_request_builder = lazy_import('msgraph.generated.users.item.remove_all_devices_from_management.remove_all_devices_from_management_request_builder')
reprocess_license_assignment_request_builder = lazy_import('msgraph.generated.users.item.reprocess_license_assignment.reprocess_license_assignment_request_builder')
restore_request_builder = lazy_import('msgraph.generated.users.item.restore.restore_request_builder')
revoke_sign_in_sessions_request_builder = lazy_import('msgraph.generated.users.item.revoke_sign_in_sessions.revoke_sign_in_sessions_request_builder')
scoped_role_member_of_request_builder = lazy_import('msgraph.generated.users.item.scoped_role_member_of.scoped_role_member_of_request_builder')
scoped_role_membership_item_request_builder = lazy_import('msgraph.generated.users.item.scoped_role_member_of.item.scoped_role_membership_item_request_builder')
security_request_builder = lazy_import('msgraph.generated.users.item.security.security_request_builder')
send_mail_request_builder = lazy_import('msgraph.generated.users.item.send_mail.send_mail_request_builder')
settings_request_builder = lazy_import('msgraph.generated.users.item.settings.settings_request_builder')
teamwork_request_builder = lazy_import('msgraph.generated.users.item.teamwork.teamwork_request_builder')
todo_request_builder = lazy_import('msgraph.generated.users.item.todo.todo_request_builder')
transitive_member_of_request_builder = lazy_import('msgraph.generated.users.item.transitive_member_of.transitive_member_of_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.users.item.transitive_member_of.item.directory_object_item_request_builder')
transitive_reports_request_builder = lazy_import('msgraph.generated.users.item.transitive_reports.transitive_reports_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.users.item.transitive_reports.item.directory_object_item_request_builder')
translate_exchange_ids_request_builder = lazy_import('msgraph.generated.users.item.translate_exchange_ids.translate_exchange_ids_request_builder')
unblock_managed_apps_request_builder = lazy_import('msgraph.generated.users.item.unblock_managed_apps.unblock_managed_apps_request_builder')
usage_rights_request_builder = lazy_import('msgraph.generated.users.item.usage_rights.usage_rights_request_builder')
usage_right_item_request_builder = lazy_import('msgraph.generated.users.item.usage_rights.item.usage_right_item_request_builder')
windows_information_protection_device_registrations_request_builder = lazy_import('msgraph.generated.users.item.windows_information_protection_device_registrations.windows_information_protection_device_registrations_request_builder')
windows_information_protection_device_registration_item_request_builder = lazy_import('msgraph.generated.users.item.windows_information_protection_device_registrations.item.windows_information_protection_device_registration_item_request_builder')
wipe_and_block_managed_apps_request_builder = lazy_import('msgraph.generated.users.item.wipe_and_block_managed_apps.wipe_and_block_managed_apps_request_builder')
wipe_managed_app_registration_by_device_tag_request_builder = lazy_import('msgraph.generated.users.item.wipe_managed_app_registration_by_device_tag.wipe_managed_app_registration_by_device_tag_request_builder')
wipe_managed_app_registrations_by_azure_ad_device_id_request_builder = lazy_import('msgraph.generated.users.item.wipe_managed_app_registrations_by_azure_ad_device_id.wipe_managed_app_registrations_by_azure_ad_device_id_request_builder')
wipe_managed_app_registrations_by_device_tag_request_builder = lazy_import('msgraph.generated.users.item.wipe_managed_app_registrations_by_device_tag.wipe_managed_app_registrations_by_device_tag_request_builder')

class UserItemRequestBuilder():
    """
    Provides operations to manage the collection of user entities.
    """
    @property
    def activate_service_plan(self) -> activate_service_plan_request_builder.ActivateServicePlanRequestBuilder:
        """
        Provides operations to call the activateServicePlan method.
        """
        return activate_service_plan_request_builder.ActivateServicePlanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def activities(self) -> activities_request_builder.ActivitiesRequestBuilder:
        """
        Provides operations to manage the activities property of the microsoft.graph.user entity.
        """
        return activities_request_builder.ActivitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agreement_acceptances(self) -> agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder:
        """
        Provides operations to manage the agreementAcceptances property of the microsoft.graph.user entity.
        """
        return agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def analytics(self) -> analytics_request_builder.AnalyticsRequestBuilder:
        """
        Provides operations to manage the analytics property of the microsoft.graph.user entity.
        """
        return analytics_request_builder.AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_consent_requests_for_approval(self) -> app_consent_requests_for_approval_request_builder.AppConsentRequestsForApprovalRequestBuilder:
        """
        Provides operations to manage the appConsentRequestsForApproval property of the microsoft.graph.user entity.
        """
        return app_consent_requests_for_approval_request_builder.AppConsentRequestsForApprovalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_role_assigned_resources(self) -> app_role_assigned_resources_request_builder.AppRoleAssignedResourcesRequestBuilder:
        """
        Provides operations to manage the appRoleAssignedResources property of the microsoft.graph.user entity.
        """
        return app_role_assigned_resources_request_builder.AppRoleAssignedResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_role_assignments(self) -> app_role_assignments_request_builder.AppRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the appRoleAssignments property of the microsoft.graph.user entity.
        """
        return app_role_assignments_request_builder.AppRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def approvals(self) -> approvals_request_builder.ApprovalsRequestBuilder:
        """
        Provides operations to manage the approvals property of the microsoft.graph.user entity.
        """
        return approvals_request_builder.ApprovalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assign_license(self) -> assign_license_request_builder.AssignLicenseRequestBuilder:
        """
        Provides operations to call the assignLicense method.
        """
        return assign_license_request_builder.AssignLicenseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication(self) -> authentication_request_builder.AuthenticationRequestBuilder:
        """
        Provides operations to manage the authentication property of the microsoft.graph.user entity.
        """
        return authentication_request_builder.AuthenticationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar(self) -> calendar_request_builder.CalendarRequestBuilder:
        """
        Provides operations to manage the calendar property of the microsoft.graph.user entity.
        """
        return calendar_request_builder.CalendarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar_groups(self) -> calendar_groups_request_builder.CalendarGroupsRequestBuilder:
        """
        Provides operations to manage the calendarGroups property of the microsoft.graph.user entity.
        """
        return calendar_groups_request_builder.CalendarGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendars(self) -> calendars_request_builder.CalendarsRequestBuilder:
        """
        Provides operations to manage the calendars property of the microsoft.graph.user entity.
        """
        return calendars_request_builder.CalendarsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar_view(self) -> calendar_view_request_builder.CalendarViewRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.user entity.
        """
        return calendar_view_request_builder.CalendarViewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def change_password(self) -> change_password_request_builder.ChangePasswordRequestBuilder:
        """
        Provides operations to call the changePassword method.
        """
        return change_password_request_builder.ChangePasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chats(self) -> chats_request_builder.ChatsRequestBuilder:
        """
        Provides operations to manage the chats property of the microsoft.graph.user entity.
        """
        return chats_request_builder.ChatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_groups(self) -> check_member_groups_request_builder.CheckMemberGroupsRequestBuilder:
        """
        Provides operations to call the checkMemberGroups method.
        """
        return check_member_groups_request_builder.CheckMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_objects(self) -> check_member_objects_request_builder.CheckMemberObjectsRequestBuilder:
        """
        Provides operations to call the checkMemberObjects method.
        """
        return check_member_objects_request_builder.CheckMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_p_cs(self) -> cloud_p_cs_request_builder.CloudPCsRequestBuilder:
        """
        Provides operations to manage the cloudPCs property of the microsoft.graph.user entity.
        """
        return cloud_p_cs_request_builder.CloudPCsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contact_folders(self) -> contact_folders_request_builder.ContactFoldersRequestBuilder:
        """
        Provides operations to manage the contactFolders property of the microsoft.graph.user entity.
        """
        return contact_folders_request_builder.ContactFoldersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contacts(self) -> contacts_request_builder.ContactsRequestBuilder:
        """
        Provides operations to manage the contacts property of the microsoft.graph.user entity.
        """
        return contacts_request_builder.ContactsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def created_objects(self) -> created_objects_request_builder.CreatedObjectsRequestBuilder:
        """
        Provides operations to manage the createdObjects property of the microsoft.graph.user entity.
        """
        return created_objects_request_builder.CreatedObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_enrollment_configurations(self) -> device_enrollment_configurations_request_builder.DeviceEnrollmentConfigurationsRequestBuilder:
        """
        Provides operations to manage the deviceEnrollmentConfigurations property of the microsoft.graph.user entity.
        """
        return device_enrollment_configurations_request_builder.DeviceEnrollmentConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management_troubleshooting_events(self) -> device_management_troubleshooting_events_request_builder.DeviceManagementTroubleshootingEventsRequestBuilder:
        """
        Provides operations to manage the deviceManagementTroubleshootingEvents property of the microsoft.graph.user entity.
        """
        return device_management_troubleshooting_events_request_builder.DeviceManagementTroubleshootingEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def devices(self) -> devices_request_builder.DevicesRequestBuilder:
        """
        Provides operations to manage the devices property of the microsoft.graph.user entity.
        """
        return devices_request_builder.DevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def direct_reports(self) -> direct_reports_request_builder.DirectReportsRequestBuilder:
        """
        Provides operations to manage the directReports property of the microsoft.graph.user entity.
        """
        return direct_reports_request_builder.DirectReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive(self) -> drive_request_builder.DriveRequestBuilder:
        """
        Provides operations to manage the drive property of the microsoft.graph.user entity.
        """
        return drive_request_builder.DriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drives(self) -> drives_request_builder.DrivesRequestBuilder:
        """
        Provides operations to manage the drives property of the microsoft.graph.user entity.
        """
        return drives_request_builder.DrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def events(self) -> events_request_builder.EventsRequestBuilder:
        """
        Provides operations to manage the events property of the microsoft.graph.user entity.
        """
        return events_request_builder.EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def export_personal_data(self) -> export_personal_data_request_builder.ExportPersonalDataRequestBuilder:
        """
        Provides operations to call the exportPersonalData method.
        """
        return export_personal_data_request_builder.ExportPersonalDataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> extensions_request_builder.ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.user entity.
        """
        return extensions_request_builder.ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def find_meeting_times(self) -> find_meeting_times_request_builder.FindMeetingTimesRequestBuilder:
        """
        Provides operations to call the findMeetingTimes method.
        """
        return find_meeting_times_request_builder.FindMeetingTimesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def followed_sites(self) -> followed_sites_request_builder.FollowedSitesRequestBuilder:
        """
        Provides operations to manage the followedSites property of the microsoft.graph.user entity.
        """
        return followed_sites_request_builder.FollowedSitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_mail_tips(self) -> get_mail_tips_request_builder.GetMailTipsRequestBuilder:
        """
        Provides operations to call the getMailTips method.
        """
        return get_mail_tips_request_builder.GetMailTipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_groups(self) -> get_member_groups_request_builder.GetMemberGroupsRequestBuilder:
        """
        Provides operations to call the getMemberGroups method.
        """
        return get_member_groups_request_builder.GetMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_objects(self) -> get_member_objects_request_builder.GetMemberObjectsRequestBuilder:
        """
        Provides operations to call the getMemberObjects method.
        """
        return get_member_objects_request_builder.GetMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inference_classification(self) -> inference_classification_request_builder.InferenceClassificationRequestBuilder:
        """
        Provides operations to manage the inferenceClassification property of the microsoft.graph.user entity.
        """
        return inference_classification_request_builder.InferenceClassificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def information_protection(self) -> information_protection_request_builder.InformationProtectionRequestBuilder:
        """
        Provides operations to manage the informationProtection property of the microsoft.graph.user entity.
        """
        return information_protection_request_builder.InformationProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def insights(self) -> insights_request_builder.InsightsRequestBuilder:
        """
        Provides operations to manage the insights property of the microsoft.graph.user entity.
        """
        return insights_request_builder.InsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invalidate_all_refresh_tokens(self) -> invalidate_all_refresh_tokens_request_builder.InvalidateAllRefreshTokensRequestBuilder:
        """
        Provides operations to call the invalidateAllRefreshTokens method.
        """
        return invalidate_all_refresh_tokens_request_builder.InvalidateAllRefreshTokensRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def joined_groups(self) -> joined_groups_request_builder.JoinedGroupsRequestBuilder:
        """
        Provides operations to manage the joinedGroups property of the microsoft.graph.user entity.
        """
        return joined_groups_request_builder.JoinedGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def joined_teams(self) -> joined_teams_request_builder.JoinedTeamsRequestBuilder:
        """
        Provides operations to manage the joinedTeams property of the microsoft.graph.user entity.
        """
        return joined_teams_request_builder.JoinedTeamsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def license_details(self) -> license_details_request_builder.LicenseDetailsRequestBuilder:
        """
        Provides operations to manage the licenseDetails property of the microsoft.graph.user entity.
        """
        return license_details_request_builder.LicenseDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mail_folders(self) -> mail_folders_request_builder.MailFoldersRequestBuilder:
        """
        Provides operations to manage the mailFolders property of the microsoft.graph.user entity.
        """
        return mail_folders_request_builder.MailFoldersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_registrations(self) -> managed_app_registrations_request_builder.ManagedAppRegistrationsRequestBuilder:
        """
        Provides operations to manage the managedAppRegistrations property of the microsoft.graph.user entity.
        """
        return managed_app_registrations_request_builder.ManagedAppRegistrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_devices(self) -> managed_devices_request_builder.ManagedDevicesRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.user entity.
        """
        return managed_devices_request_builder.ManagedDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def manager(self) -> manager_request_builder.ManagerRequestBuilder:
        """
        Provides operations to manage the manager property of the microsoft.graph.user entity.
        """
        return manager_request_builder.ManagerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_of(self) -> member_of_request_builder.MemberOfRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.user entity.
        """
        return member_of_request_builder.MemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messages(self) -> messages_request_builder.MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.user entity.
        """
        return messages_request_builder.MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_intent_and_states(self) -> mobile_app_intent_and_states_request_builder.MobileAppIntentAndStatesRequestBuilder:
        """
        Provides operations to manage the mobileAppIntentAndStates property of the microsoft.graph.user entity.
        """
        return mobile_app_intent_and_states_request_builder.MobileAppIntentAndStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_troubleshooting_events(self) -> mobile_app_troubleshooting_events_request_builder.MobileAppTroubleshootingEventsRequestBuilder:
        """
        Provides operations to manage the mobileAppTroubleshootingEvents property of the microsoft.graph.user entity.
        """
        return mobile_app_troubleshooting_events_request_builder.MobileAppTroubleshootingEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notifications(self) -> notifications_request_builder.NotificationsRequestBuilder:
        """
        Provides operations to manage the notifications property of the microsoft.graph.user entity.
        """
        return notifications_request_builder.NotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oauth2_permission_grants(self) -> oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the oauth2PermissionGrants property of the microsoft.graph.user entity.
        """
        return oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def onenote(self) -> onenote_request_builder.OnenoteRequestBuilder:
        """
        Provides operations to manage the onenote property of the microsoft.graph.user entity.
        """
        return onenote_request_builder.OnenoteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def online_meetings(self) -> online_meetings_request_builder.OnlineMeetingsRequestBuilder:
        """
        Provides operations to manage the onlineMeetings property of the microsoft.graph.user entity.
        """
        return online_meetings_request_builder.OnlineMeetingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def outlook(self) -> outlook_request_builder.OutlookRequestBuilder:
        """
        Provides operations to manage the outlook property of the microsoft.graph.user entity.
        """
        return outlook_request_builder.OutlookRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owned_devices(self) -> owned_devices_request_builder.OwnedDevicesRequestBuilder:
        """
        Provides operations to manage the ownedDevices property of the microsoft.graph.user entity.
        """
        return owned_devices_request_builder.OwnedDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owned_objects(self) -> owned_objects_request_builder.OwnedObjectsRequestBuilder:
        """
        Provides operations to manage the ownedObjects property of the microsoft.graph.user entity.
        """
        return owned_objects_request_builder.OwnedObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pending_access_review_instances(self) -> pending_access_review_instances_request_builder.PendingAccessReviewInstancesRequestBuilder:
        """
        Provides operations to manage the pendingAccessReviewInstances property of the microsoft.graph.user entity.
        """
        return pending_access_review_instances_request_builder.PendingAccessReviewInstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def people(self) -> people_request_builder.PeopleRequestBuilder:
        """
        Provides operations to manage the people property of the microsoft.graph.user entity.
        """
        return people_request_builder.PeopleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photo(self) -> photo_request_builder.PhotoRequestBuilder:
        """
        Provides operations to manage the photo property of the microsoft.graph.user entity.
        """
        return photo_request_builder.PhotoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photos(self) -> photos_request_builder.PhotosRequestBuilder:
        """
        Provides operations to manage the photos property of the microsoft.graph.user entity.
        """
        return photos_request_builder.PhotosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def planner(self) -> planner_request_builder.PlannerRequestBuilder:
        """
        Provides operations to manage the planner property of the microsoft.graph.user entity.
        """
        return planner_request_builder.PlannerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def presence(self) -> presence_request_builder.PresenceRequestBuilder:
        """
        Provides operations to manage the presence property of the microsoft.graph.user entity.
        """
        return presence_request_builder.PresenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def profile(self) -> profile_request_builder.ProfileRequestBuilder:
        """
        Provides operations to manage the profile property of the microsoft.graph.user entity.
        """
        return profile_request_builder.ProfileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def registered_devices(self) -> registered_devices_request_builder.RegisteredDevicesRequestBuilder:
        """
        Provides operations to manage the registeredDevices property of the microsoft.graph.user entity.
        """
        return registered_devices_request_builder.RegisteredDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_all_devices_from_management(self) -> remove_all_devices_from_management_request_builder.RemoveAllDevicesFromManagementRequestBuilder:
        """
        Provides operations to call the removeAllDevicesFromManagement method.
        """
        return remove_all_devices_from_management_request_builder.RemoveAllDevicesFromManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reprocess_license_assignment(self) -> reprocess_license_assignment_request_builder.ReprocessLicenseAssignmentRequestBuilder:
        """
        Provides operations to call the reprocessLicenseAssignment method.
        """
        return reprocess_license_assignment_request_builder.ReprocessLicenseAssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> restore_request_builder.RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        return restore_request_builder.RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def revoke_sign_in_sessions(self) -> revoke_sign_in_sessions_request_builder.RevokeSignInSessionsRequestBuilder:
        """
        Provides operations to call the revokeSignInSessions method.
        """
        return revoke_sign_in_sessions_request_builder.RevokeSignInSessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def scoped_role_member_of(self) -> scoped_role_member_of_request_builder.ScopedRoleMemberOfRequestBuilder:
        """
        Provides operations to manage the scopedRoleMemberOf property of the microsoft.graph.user entity.
        """
        return scoped_role_member_of_request_builder.ScopedRoleMemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security(self) -> security_request_builder.SecurityRequestBuilder:
        """
        Provides operations to manage the security property of the microsoft.graph.user entity.
        """
        return security_request_builder.SecurityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_mail(self) -> send_mail_request_builder.SendMailRequestBuilder:
        """
        Provides operations to call the sendMail method.
        """
        return send_mail_request_builder.SendMailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.user entity.
        """
        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teamwork(self) -> teamwork_request_builder.TeamworkRequestBuilder:
        """
        Provides operations to manage the teamwork property of the microsoft.graph.user entity.
        """
        return teamwork_request_builder.TeamworkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def todo(self) -> todo_request_builder.TodoRequestBuilder:
        """
        Provides operations to manage the todo property of the microsoft.graph.user entity.
        """
        return todo_request_builder.TodoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_member_of(self) -> transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.user entity.
        """
        return transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_reports(self) -> transitive_reports_request_builder.TransitiveReportsRequestBuilder:
        """
        Provides operations to manage the transitiveReports property of the microsoft.graph.user entity.
        """
        return transitive_reports_request_builder.TransitiveReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def translate_exchange_ids(self) -> translate_exchange_ids_request_builder.TranslateExchangeIdsRequestBuilder:
        """
        Provides operations to call the translateExchangeIds method.
        """
        return translate_exchange_ids_request_builder.TranslateExchangeIdsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unblock_managed_apps(self) -> unblock_managed_apps_request_builder.UnblockManagedAppsRequestBuilder:
        """
        Provides operations to call the unblockManagedApps method.
        """
        return unblock_managed_apps_request_builder.UnblockManagedAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def usage_rights(self) -> usage_rights_request_builder.UsageRightsRequestBuilder:
        """
        Provides operations to manage the usageRights property of the microsoft.graph.user entity.
        """
        return usage_rights_request_builder.UsageRightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_device_registrations(self) -> windows_information_protection_device_registrations_request_builder.WindowsInformationProtectionDeviceRegistrationsRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionDeviceRegistrations property of the microsoft.graph.user entity.
        """
        return windows_information_protection_device_registrations_request_builder.WindowsInformationProtectionDeviceRegistrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wipe_and_block_managed_apps(self) -> wipe_and_block_managed_apps_request_builder.WipeAndBlockManagedAppsRequestBuilder:
        """
        Provides operations to call the wipeAndBlockManagedApps method.
        """
        return wipe_and_block_managed_apps_request_builder.WipeAndBlockManagedAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wipe_managed_app_registration_by_device_tag(self) -> wipe_managed_app_registration_by_device_tag_request_builder.WipeManagedAppRegistrationByDeviceTagRequestBuilder:
        """
        Provides operations to call the wipeManagedAppRegistrationByDeviceTag method.
        """
        return wipe_managed_app_registration_by_device_tag_request_builder.WipeManagedAppRegistrationByDeviceTagRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wipe_managed_app_registrations_by_azure_ad_device_id(self) -> wipe_managed_app_registrations_by_azure_ad_device_id_request_builder.WipeManagedAppRegistrationsByAzureAdDeviceIdRequestBuilder:
        """
        Provides operations to call the wipeManagedAppRegistrationsByAzureAdDeviceId method.
        """
        return wipe_managed_app_registrations_by_azure_ad_device_id_request_builder.WipeManagedAppRegistrationsByAzureAdDeviceIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wipe_managed_app_registrations_by_device_tag(self) -> wipe_managed_app_registrations_by_device_tag_request_builder.WipeManagedAppRegistrationsByDeviceTagRequestBuilder:
        """
        Provides operations to call the wipeManagedAppRegistrationsByDeviceTag method.
        """
        return wipe_managed_app_registrations_by_device_tag_request_builder.WipeManagedAppRegistrationsByDeviceTagRequestBuilder(self.request_adapter, self.path_parameters)
    
    def activities_by_id(self,id: str) -> user_activity_item_request_builder.UserActivityItemRequestBuilder:
        """
        Provides operations to manage the activities property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: user_activity_item_request_builder.UserActivityItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userActivity%2Did"] = id
        return user_activity_item_request_builder.UserActivityItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def agreement_acceptances_by_id(self,id: str) -> agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder:
        """
        Provides operations to manage the agreementAcceptances property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreementAcceptance%2Did"] = id
        return agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def app_consent_requests_for_approval_by_id(self,id: str) -> app_consent_request_item_request_builder.AppConsentRequestItemRequestBuilder:
        """
        Provides operations to manage the appConsentRequestsForApproval property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: app_consent_request_item_request_builder.AppConsentRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["appConsentRequest%2Did"] = id
        return app_consent_request_item_request_builder.AppConsentRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def app_role_assigned_resources_by_id(self,id: str) -> service_principal_item_request_builder.ServicePrincipalItemRequestBuilder:
        """
        Provides operations to manage the appRoleAssignedResources property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: service_principal_item_request_builder.ServicePrincipalItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["servicePrincipal%2Did"] = id
        return service_principal_item_request_builder.ServicePrincipalItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def app_role_assignments_by_id(self,id: str) -> app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the appRoleAssignments property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["appRoleAssignment%2Did"] = id
        return app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def approvals_by_id(self,id: str) -> approval_item_request_builder.ApprovalItemRequestBuilder:
        """
        Provides operations to manage the approvals property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: approval_item_request_builder.ApprovalItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["approval%2Did"] = id
        return approval_item_request_builder.ApprovalItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def calendar_groups_by_id(self,id: str) -> calendar_group_item_request_builder.CalendarGroupItemRequestBuilder:
        """
        Provides operations to manage the calendarGroups property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: calendar_group_item_request_builder.CalendarGroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["calendarGroup%2Did"] = id
        return calendar_group_item_request_builder.CalendarGroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def calendars_by_id(self,id: str) -> calendar_item_request_builder.CalendarItemRequestBuilder:
        """
        Provides operations to manage the calendars property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: calendar_item_request_builder.CalendarItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["calendar%2Did"] = id
        return calendar_item_request_builder.CalendarItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def calendar_view_by_id(self,id: str) -> event_item_request_builder.EventItemRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: event_item_request_builder.EventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["event%2Did"] = id
        return event_item_request_builder.EventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def chats_by_id(self,id: str) -> chat_item_request_builder.ChatItemRequestBuilder:
        """
        Provides operations to manage the chats property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: chat_item_request_builder.ChatItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["chat%2Did"] = id
        return chat_item_request_builder.ChatItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def cloud_p_cs_by_id(self,id: str) -> cloud_p_c_item_request_builder.CloudPCItemRequestBuilder:
        """
        Provides operations to manage the cloudPCs property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_p_c_item_request_builder.CloudPCItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPC%2Did"] = id
        return cloud_p_c_item_request_builder.CloudPCItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UserItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def contact_folders_by_id(self,id: str) -> contact_folder_item_request_builder.ContactFolderItemRequestBuilder:
        """
        Provides operations to manage the contactFolders property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: contact_folder_item_request_builder.ContactFolderItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["contactFolder%2Did"] = id
        return contact_folder_item_request_builder.ContactFolderItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def contacts_by_id(self,id: str) -> contact_item_request_builder.ContactItemRequestBuilder:
        """
        Provides operations to manage the contacts property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: contact_item_request_builder.ContactItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["contact%2Did"] = id
        return contact_item_request_builder.ContactItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def created_objects_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the createdObjects property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[UserItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete user.   When deleted, user resources are moved to a temporary container and can be restored within 30 days.  After that time, they are permanently deleted.  To learn more, see deletedItems.
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
    
    def device_enrollment_configurations_by_id(self,id: str) -> device_enrollment_configuration_item_request_builder.DeviceEnrollmentConfigurationItemRequestBuilder:
        """
        Provides operations to manage the deviceEnrollmentConfigurations property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: device_enrollment_configuration_item_request_builder.DeviceEnrollmentConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceEnrollmentConfiguration%2Did"] = id
        return device_enrollment_configuration_item_request_builder.DeviceEnrollmentConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_management_troubleshooting_events_by_id(self,id: str) -> device_management_troubleshooting_event_item_request_builder.DeviceManagementTroubleshootingEventItemRequestBuilder:
        """
        Provides operations to manage the deviceManagementTroubleshootingEvents property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_troubleshooting_event_item_request_builder.DeviceManagementTroubleshootingEventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementTroubleshootingEvent%2Did"] = id
        return device_management_troubleshooting_event_item_request_builder.DeviceManagementTroubleshootingEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def devices_by_id(self,id: str) -> device_item_request_builder.DeviceItemRequestBuilder:
        """
        Provides operations to manage the devices property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: device_item_request_builder.DeviceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["device%2Did"] = id
        return device_item_request_builder.DeviceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def direct_reports_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the directReports property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def drives_by_id(self,id: str) -> drive_item_request_builder.DriveItemRequestBuilder:
        """
        Provides operations to manage the drives property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_request_builder.DriveItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["drive%2Did"] = id
        return drive_item_request_builder.DriveItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def events_by_id(self,id: str) -> event_item_request_builder.EventItemRequestBuilder:
        """
        Provides operations to manage the events property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: event_item_request_builder.EventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["event%2Did"] = id
        return event_item_request_builder.EventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def export_device_and_app_management_data(self,) -> export_device_and_app_management_data_request_builder.ExportDeviceAndAppManagementDataRequestBuilder:
        """
        Provides operations to call the exportDeviceAndAppManagementData method.
        Returns: export_device_and_app_management_data_request_builder.ExportDeviceAndAppManagementDataRequestBuilder
        """
        return export_device_and_app_management_data_request_builder.ExportDeviceAndAppManagementDataRequestBuilder(self.request_adapter, self.path_parameters)
    
    def export_device_and_app_management_data_with_skip_with_top(self,skip: Optional[int] = None, top: Optional[int] = None) -> export_device_and_app_management_data_with_skip_with_top_request_builder.ExportDeviceAndAppManagementDataWithSkipWithTopRequestBuilder:
        """
        Provides operations to call the exportDeviceAndAppManagementData method.
        Args:
            skip: Usage: skip={skip}
            top: Usage: top={top}
        Returns: export_device_and_app_management_data_with_skip_with_top_request_builder.ExportDeviceAndAppManagementDataWithSkipWithTopRequestBuilder
        """
        if skip is None:
            raise Exception("skip cannot be undefined")
        if top is None:
            raise Exception("top cannot be undefined")
        return export_device_and_app_management_data_with_skip_with_top_request_builder.ExportDeviceAndAppManagementDataWithSkipWithTopRequestBuilder(self.request_adapter, self.path_parameters, skip, top)
    
    def extensions_by_id(self,id: str) -> extension_item_request_builder.ExtensionItemRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: extension_item_request_builder.ExtensionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["extension%2Did"] = id
        return extension_item_request_builder.ExtensionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def find_room_lists(self,) -> find_room_lists_request_builder.FindRoomListsRequestBuilder:
        """
        Provides operations to call the findRoomLists method.
        Returns: find_room_lists_request_builder.FindRoomListsRequestBuilder
        """
        return find_room_lists_request_builder.FindRoomListsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def find_rooms(self,) -> find_rooms_request_builder.FindRoomsRequestBuilder:
        """
        Provides operations to call the findRooms method.
        Returns: find_rooms_request_builder.FindRoomsRequestBuilder
        """
        return find_rooms_request_builder.FindRoomsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def find_rooms_with_room_list(self,room_list: Optional[str] = None) -> find_rooms_with_room_list_request_builder.FindRoomsWithRoomListRequestBuilder:
        """
        Provides operations to call the findRooms method.
        Args:
            RoomList: Usage: RoomList='{RoomList}'
        Returns: find_rooms_with_room_list_request_builder.FindRoomsWithRoomListRequestBuilder
        """
        if room_list is None:
            raise Exception("room_list cannot be undefined")
        return find_rooms_with_room_list_request_builder.FindRoomsWithRoomListRequestBuilder(self.request_adapter, self.path_parameters, RoomList)
    
    def followed_sites_by_id(self,id: str) -> site_item_request_builder.SiteItemRequestBuilder:
        """
        Provides operations to manage the followedSites property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: site_item_request_builder.SiteItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["site%2Did"] = id
        return site_item_request_builder.SiteItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[UserItemRequestBuilderGetRequestConfiguration] = None) -> Optional[user.User]:
        """
        Retrieve the properties and relationships of user object. This operation returns by default only a subset of the more commonly used properties for each user. These _default_ properties are noted in the Properties section. To get properties that are _not_ returned by default, do a GET operation for the user and specify the properties in a `$select` OData query option. Because the **user** resource supports extensions, you can also use the `GET` operation to get custom properties and extension data in a **user** instance.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[user.User]
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
        return await self.request_adapter.send_async(request_info, user.User, error_mapping)
    
    def get_effective_device_enrollment_configurations(self,) -> get_effective_device_enrollment_configurations_request_builder.GetEffectiveDeviceEnrollmentConfigurationsRequestBuilder:
        """
        Provides operations to call the getEffectiveDeviceEnrollmentConfigurations method.
        Returns: get_effective_device_enrollment_configurations_request_builder.GetEffectiveDeviceEnrollmentConfigurationsRequestBuilder
        """
        return get_effective_device_enrollment_configurations_request_builder.GetEffectiveDeviceEnrollmentConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_logged_on_managed_devices(self,) -> get_logged_on_managed_devices_request_builder.GetLoggedOnManagedDevicesRequestBuilder:
        """
        Provides operations to call the getLoggedOnManagedDevices method.
        Returns: get_logged_on_managed_devices_request_builder.GetLoggedOnManagedDevicesRequestBuilder
        """
        return get_logged_on_managed_devices_request_builder.GetLoggedOnManagedDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_managed_app_diagnostic_statuses(self,) -> get_managed_app_diagnostic_statuses_request_builder.GetManagedAppDiagnosticStatusesRequestBuilder:
        """
        Provides operations to call the getManagedAppDiagnosticStatuses method.
        Returns: get_managed_app_diagnostic_statuses_request_builder.GetManagedAppDiagnosticStatusesRequestBuilder
        """
        return get_managed_app_diagnostic_statuses_request_builder.GetManagedAppDiagnosticStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_managed_app_policies(self,) -> get_managed_app_policies_request_builder.GetManagedAppPoliciesRequestBuilder:
        """
        Provides operations to call the getManagedAppPolicies method.
        Returns: get_managed_app_policies_request_builder.GetManagedAppPoliciesRequestBuilder
        """
        return get_managed_app_policies_request_builder.GetManagedAppPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_managed_devices_with_app_failures(self,) -> get_managed_devices_with_app_failures_request_builder.GetManagedDevicesWithAppFailuresRequestBuilder:
        """
        Provides operations to call the getManagedDevicesWithAppFailures method.
        Returns: get_managed_devices_with_app_failures_request_builder.GetManagedDevicesWithAppFailuresRequestBuilder
        """
        return get_managed_devices_with_app_failures_request_builder.GetManagedDevicesWithAppFailuresRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_managed_devices_with_failed_or_pending_apps(self,) -> get_managed_devices_with_failed_or_pending_apps_request_builder.GetManagedDevicesWithFailedOrPendingAppsRequestBuilder:
        """
        Provides operations to call the getManagedDevicesWithFailedOrPendingApps method.
        Returns: get_managed_devices_with_failed_or_pending_apps_request_builder.GetManagedDevicesWithFailedOrPendingAppsRequestBuilder
        """
        return get_managed_devices_with_failed_or_pending_apps_request_builder.GetManagedDevicesWithFailedOrPendingAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def is_managed_app_user_blocked(self,) -> is_managed_app_user_blocked_request_builder.IsManagedAppUserBlockedRequestBuilder:
        """
        Provides operations to call the isManagedAppUserBlocked method.
        Returns: is_managed_app_user_blocked_request_builder.IsManagedAppUserBlockedRequestBuilder
        """
        return is_managed_app_user_blocked_request_builder.IsManagedAppUserBlockedRequestBuilder(self.request_adapter, self.path_parameters)
    
    def joined_teams_by_id(self,id: str) -> team_item_request_builder.TeamItemRequestBuilder:
        """
        Provides operations to manage the joinedTeams property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: team_item_request_builder.TeamItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["team%2Did"] = id
        return team_item_request_builder.TeamItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def license_details_by_id(self,id: str) -> license_details_item_request_builder.LicenseDetailsItemRequestBuilder:
        """
        Provides operations to manage the licenseDetails property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: license_details_item_request_builder.LicenseDetailsItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["licenseDetails%2Did"] = id
        return license_details_item_request_builder.LicenseDetailsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def mail_folders_by_id(self,id: str) -> mail_folder_item_request_builder.MailFolderItemRequestBuilder:
        """
        Provides operations to manage the mailFolders property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: mail_folder_item_request_builder.MailFolderItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mailFolder%2Did"] = id
        return mail_folder_item_request_builder.MailFolderItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_app_registrations_by_id(self,id: str) -> managed_app_registration_item_request_builder.ManagedAppRegistrationItemRequestBuilder:
        """
        Provides operations to manage the managedAppRegistrations property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_app_registration_item_request_builder.ManagedAppRegistrationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedAppRegistration%2Did"] = id
        return managed_app_registration_item_request_builder.ManagedAppRegistrationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_devices_by_id(self,id: str) -> managed_device_item_request_builder.ManagedDeviceItemRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_device_item_request_builder.ManagedDeviceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDevice%2Did"] = id
        return managed_device_item_request_builder.ManagedDeviceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def member_of_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def messages_by_id(self,id: str) -> message_item_request_builder.MessageItemRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: message_item_request_builder.MessageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["message%2Did"] = id
        return message_item_request_builder.MessageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def mobile_app_intent_and_states_by_id(self,id: str) -> mobile_app_intent_and_state_item_request_builder.MobileAppIntentAndStateItemRequestBuilder:
        """
        Provides operations to manage the mobileAppIntentAndStates property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: mobile_app_intent_and_state_item_request_builder.MobileAppIntentAndStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobileAppIntentAndState%2Did"] = id
        return mobile_app_intent_and_state_item_request_builder.MobileAppIntentAndStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def mobile_app_troubleshooting_events_by_id(self,id: str) -> mobile_app_troubleshooting_event_item_request_builder.MobileAppTroubleshootingEventItemRequestBuilder:
        """
        Provides operations to manage the mobileAppTroubleshootingEvents property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: mobile_app_troubleshooting_event_item_request_builder.MobileAppTroubleshootingEventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobileAppTroubleshootingEvent%2Did"] = id
        return mobile_app_troubleshooting_event_item_request_builder.MobileAppTroubleshootingEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def notifications_by_id(self,id: str) -> notification_item_request_builder.NotificationItemRequestBuilder:
        """
        Provides operations to manage the notifications property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: notification_item_request_builder.NotificationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["notification%2Did"] = id
        return notification_item_request_builder.NotificationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def oauth2_permission_grants_by_id(self,id: str) -> o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder:
        """
        Provides operations to manage the oauth2PermissionGrants property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["oAuth2PermissionGrant%2Did"] = id
        return o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def online_meetings_by_id(self,id: str) -> online_meeting_item_request_builder.OnlineMeetingItemRequestBuilder:
        """
        Provides operations to manage the onlineMeetings property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: online_meeting_item_request_builder.OnlineMeetingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["onlineMeeting%2Did"] = id
        return online_meeting_item_request_builder.OnlineMeetingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def owned_devices_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the ownedDevices property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def owned_objects_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the ownedObjects property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[user.User] = None, request_configuration: Optional[UserItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[user.User]:
        """
        Update the properties of a user object. Not all properties can be updated by Member or Guest users with their default permissions without Administrator roles. Compare member and guest default permissions to see properties they can manage.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[user.User]
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
        return await self.request_adapter.send_async(request_info, user.User, error_mapping)
    
    def pending_access_review_instances_by_id(self,id: str) -> access_review_instance_item_request_builder.AccessReviewInstanceItemRequestBuilder:
        """
        Provides operations to manage the pendingAccessReviewInstances property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: access_review_instance_item_request_builder.AccessReviewInstanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReviewInstance%2Did"] = id
        return access_review_instance_item_request_builder.AccessReviewInstanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def people_by_id(self,id: str) -> person_item_request_builder.PersonItemRequestBuilder:
        """
        Provides operations to manage the people property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: person_item_request_builder.PersonItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["person%2Did"] = id
        return person_item_request_builder.PersonItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def photos_by_id(self,id: str) -> profile_photo_item_request_builder.ProfilePhotoItemRequestBuilder:
        """
        Provides operations to manage the photos property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: profile_photo_item_request_builder.ProfilePhotoItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["profilePhoto%2Did"] = id
        return profile_photo_item_request_builder.ProfilePhotoItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def registered_devices_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the registeredDevices property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def reminder_view_with_start_date_time_with_end_date_time(self,end_date_time: Optional[str] = None, start_date_time: Optional[str] = None) -> reminder_view_with_start_date_time_with_end_date_time_request_builder.ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the reminderView method.
        Args:
            EndDateTime: Usage: EndDateTime='{EndDateTime}'
            StartDateTime: Usage: StartDateTime='{StartDateTime}'
        Returns: reminder_view_with_start_date_time_with_end_date_time_request_builder.ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if end_date_time is None:
            raise Exception("end_date_time cannot be undefined")
        if start_date_time is None:
            raise Exception("start_date_time cannot be undefined")
        return reminder_view_with_start_date_time_with_end_date_time_request_builder.ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, EndDateTime, StartDateTime)
    
    def scoped_role_member_of_by_id(self,id: str) -> scoped_role_membership_item_request_builder.ScopedRoleMembershipItemRequestBuilder:
        """
        Provides operations to manage the scopedRoleMemberOf property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: scoped_role_membership_item_request_builder.ScopedRoleMembershipItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["scopedRoleMembership%2Did"] = id
        return scoped_role_membership_item_request_builder.ScopedRoleMembershipItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[UserItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete user.   When deleted, user resources are moved to a temporary container and can be restored within 30 days.  After that time, they are permanently deleted.  To learn more, see deletedItems.
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
    
    def to_get_request_information(self,request_configuration: Optional[UserItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of user object. This operation returns by default only a subset of the more commonly used properties for each user. These _default_ properties are noted in the Properties section. To get properties that are _not_ returned by default, do a GET operation for the user and specify the properties in a `$select` OData query option. Because the **user** resource supports extensions, you can also use the `GET` operation to get custom properties and extension data in a **user** instance.
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
    
    def to_patch_request_information(self,body: Optional[user.User] = None, request_configuration: Optional[UserItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a user object. Not all properties can be updated by Member or Guest users with their default permissions without Administrator roles. Compare member and guest default permissions to see properties they can manage.
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
    
    def transitive_member_of_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def transitive_reports_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the transitiveReports property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def usage_rights_by_id(self,id: str) -> usage_right_item_request_builder.UsageRightItemRequestBuilder:
        """
        Provides operations to manage the usageRights property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: usage_right_item_request_builder.UsageRightItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["usageRight%2Did"] = id
        return usage_right_item_request_builder.UsageRightItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_information_protection_device_registrations_by_id(self,id: str) -> windows_information_protection_device_registration_item_request_builder.WindowsInformationProtectionDeviceRegistrationItemRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionDeviceRegistrations property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_information_protection_device_registration_item_request_builder.WindowsInformationProtectionDeviceRegistrationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsInformationProtectionDeviceRegistration%2Did"] = id
        return windows_information_protection_device_registration_item_request_builder.WindowsInformationProtectionDeviceRegistrationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class UserItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UserItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of user object. This operation returns by default only a subset of the more commonly used properties for each user. These _default_ properties are noted in the Properties section. To get properties that are _not_ returned by default, do a GET operation for the user and specify the properties in a `$select` OData query option. Because the **user** resource supports extensions, you can also use the `GET` operation to get custom properties and extension data in a **user** instance.
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
    class UserItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UserItemRequestBuilder.UserItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UserItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

