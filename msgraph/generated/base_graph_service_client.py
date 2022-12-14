from __future__ import annotations
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from kiota_abstractions.utils import lazy_import
from kiota_serialization_json.json_parse_node_factory import JsonParseNodeFactory
from kiota_serialization_json.json_serialization_writer_factory import JsonSerializationWriterFactory
from kiota_serialization_text.text_parse_node_factory import TextParseNodeFactory
from kiota_serialization_text.text_serialization_writer_factory import TextSerializationWriterFactory
from typing import Any, Callable, Dict, List, Optional, Union

access_review_decisions_request_builder = lazy_import('msgraph.generated.access_review_decisions.access_review_decisions_request_builder')
access_review_decision_item_request_builder = lazy_import('msgraph.generated.access_review_decisions.item.access_review_decision_item_request_builder')
access_reviews_request_builder = lazy_import('msgraph.generated.access_reviews.access_reviews_request_builder')
access_review_item_request_builder = lazy_import('msgraph.generated.access_reviews.item.access_review_item_request_builder')
activitystatistics_request_builder = lazy_import('msgraph.generated.activitystatistics.activitystatistics_request_builder')
activity_statistics_item_request_builder = lazy_import('msgraph.generated.activitystatistics.item.activity_statistics_item_request_builder')
admin_request_builder = lazy_import('msgraph.generated.admin.admin_request_builder')
administrative_units_request_builder = lazy_import('msgraph.generated.administrative_units.administrative_units_request_builder')
administrative_unit_item_request_builder = lazy_import('msgraph.generated.administrative_units.item.administrative_unit_item_request_builder')
agreement_acceptances_request_builder = lazy_import('msgraph.generated.agreement_acceptances.agreement_acceptances_request_builder')
agreement_acceptance_item_request_builder = lazy_import('msgraph.generated.agreement_acceptances.item.agreement_acceptance_item_request_builder')
agreements_request_builder = lazy_import('msgraph.generated.agreements.agreements_request_builder')
agreement_item_request_builder = lazy_import('msgraph.generated.agreements.item.agreement_item_request_builder')
allowed_data_locations_request_builder = lazy_import('msgraph.generated.allowed_data_locations.allowed_data_locations_request_builder')
allowed_data_location_item_request_builder = lazy_import('msgraph.generated.allowed_data_locations.item.allowed_data_location_item_request_builder')
app_request_builder = lazy_import('msgraph.generated.app.app_request_builder')
app_catalogs_request_builder = lazy_import('msgraph.generated.app_catalogs.app_catalogs_request_builder')
applications_request_builder = lazy_import('msgraph.generated.applications.applications_request_builder')
application_item_request_builder = lazy_import('msgraph.generated.applications.item.application_item_request_builder')
application_templates_request_builder = lazy_import('msgraph.generated.application_templates.application_templates_request_builder')
application_template_item_request_builder = lazy_import('msgraph.generated.application_templates.item.application_template_item_request_builder')
app_role_assignments_request_builder = lazy_import('msgraph.generated.app_role_assignments.app_role_assignments_request_builder')
app_role_assignment_item_request_builder = lazy_import('msgraph.generated.app_role_assignments.item.app_role_assignment_item_request_builder')
approval_workflow_providers_request_builder = lazy_import('msgraph.generated.approval_workflow_providers.approval_workflow_providers_request_builder')
approval_workflow_provider_item_request_builder = lazy_import('msgraph.generated.approval_workflow_providers.item.approval_workflow_provider_item_request_builder')
audit_logs_request_builder = lazy_import('msgraph.generated.audit_logs.audit_logs_request_builder')
authentication_method_configurations_request_builder = lazy_import('msgraph.generated.authentication_method_configurations.authentication_method_configurations_request_builder')
authentication_method_configuration_item_request_builder = lazy_import('msgraph.generated.authentication_method_configurations.item.authentication_method_configuration_item_request_builder')
authentication_methods_policy_request_builder = lazy_import('msgraph.generated.authentication_methods_policy.authentication_methods_policy_request_builder')
booking_businesses_request_builder = lazy_import('msgraph.generated.booking_businesses.booking_businesses_request_builder')
booking_business_item_request_builder = lazy_import('msgraph.generated.booking_businesses.item.booking_business_item_request_builder')
booking_currencies_request_builder = lazy_import('msgraph.generated.booking_currencies.booking_currencies_request_builder')
booking_currency_item_request_builder = lazy_import('msgraph.generated.booking_currencies.item.booking_currency_item_request_builder')
branding_request_builder = lazy_import('msgraph.generated.branding.branding_request_builder')
business_flow_templates_request_builder = lazy_import('msgraph.generated.business_flow_templates.business_flow_templates_request_builder')
business_flow_template_item_request_builder = lazy_import('msgraph.generated.business_flow_templates.item.business_flow_template_item_request_builder')
certificate_based_auth_configuration_request_builder = lazy_import('msgraph.generated.certificate_based_auth_configuration.certificate_based_auth_configuration_request_builder')
certificate_based_auth_configuration_item_request_builder = lazy_import('msgraph.generated.certificate_based_auth_configuration.item.certificate_based_auth_configuration_item_request_builder')
chats_request_builder = lazy_import('msgraph.generated.chats.chats_request_builder')
chat_item_request_builder = lazy_import('msgraph.generated.chats.item.chat_item_request_builder')
commands_request_builder = lazy_import('msgraph.generated.commands.commands_request_builder')
command_item_request_builder = lazy_import('msgraph.generated.commands.item.command_item_request_builder')
communications_request_builder = lazy_import('msgraph.generated.communications.communications_request_builder')
compliance_request_builder = lazy_import('msgraph.generated.compliance.compliance_request_builder')
connections_request_builder = lazy_import('msgraph.generated.connections.connections_request_builder')
external_connection_item_request_builder = lazy_import('msgraph.generated.connections.item.external_connection_item_request_builder')
contacts_request_builder = lazy_import('msgraph.generated.contacts.contacts_request_builder')
org_contact_item_request_builder = lazy_import('msgraph.generated.contacts.item.org_contact_item_request_builder')
contracts_request_builder = lazy_import('msgraph.generated.contracts.contracts_request_builder')
contract_item_request_builder = lazy_import('msgraph.generated.contracts.item.contract_item_request_builder')
data_classification_request_builder = lazy_import('msgraph.generated.data_classification.data_classification_request_builder')
data_policy_operations_request_builder = lazy_import('msgraph.generated.data_policy_operations.data_policy_operations_request_builder')
data_policy_operation_item_request_builder = lazy_import('msgraph.generated.data_policy_operations.item.data_policy_operation_item_request_builder')
device_app_management_request_builder = lazy_import('msgraph.generated.device_app_management.device_app_management_request_builder')
device_management_request_builder = lazy_import('msgraph.generated.device_management.device_management_request_builder')
devices_request_builder = lazy_import('msgraph.generated.devices.devices_request_builder')
device_item_request_builder = lazy_import('msgraph.generated.devices.item.device_item_request_builder')
directory_request_builder = lazy_import('msgraph.generated.directory.directory_request_builder')
directory_objects_request_builder = lazy_import('msgraph.generated.directory_objects.directory_objects_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.directory_objects.item.directory_object_item_request_builder')
directory_roles_request_builder = lazy_import('msgraph.generated.directory_roles.directory_roles_request_builder')
directory_role_item_request_builder = lazy_import('msgraph.generated.directory_roles.item.directory_role_item_request_builder')
directory_role_templates_request_builder = lazy_import('msgraph.generated.directory_role_templates.directory_role_templates_request_builder')
directory_role_template_item_request_builder = lazy_import('msgraph.generated.directory_role_templates.item.directory_role_template_item_request_builder')
directory_setting_templates_request_builder = lazy_import('msgraph.generated.directory_setting_templates.directory_setting_templates_request_builder')
directory_setting_template_item_request_builder = lazy_import('msgraph.generated.directory_setting_templates.item.directory_setting_template_item_request_builder')
domain_dns_records_request_builder = lazy_import('msgraph.generated.domain_dns_records.domain_dns_records_request_builder')
domain_dns_record_item_request_builder = lazy_import('msgraph.generated.domain_dns_records.item.domain_dns_record_item_request_builder')
domains_request_builder = lazy_import('msgraph.generated.domains.domains_request_builder')
domain_item_request_builder = lazy_import('msgraph.generated.domains.item.domain_item_request_builder')
drive_request_builder = lazy_import('msgraph.generated.drive.drive_request_builder')
drives_request_builder = lazy_import('msgraph.generated.drives.drives_request_builder')
drive_item_request_builder = lazy_import('msgraph.generated.drives.item.drive_item_request_builder')
education_request_builder = lazy_import('msgraph.generated.education.education_request_builder')
employee_experience_request_builder = lazy_import('msgraph.generated.employee_experience.employee_experience_request_builder')
external_request_builder = lazy_import('msgraph.generated.external.external_request_builder')
filter_operators_request_builder = lazy_import('msgraph.generated.filter_operators.filter_operators_request_builder')
filter_operator_schema_item_request_builder = lazy_import('msgraph.generated.filter_operators.item.filter_operator_schema_item_request_builder')
financials_request_builder = lazy_import('msgraph.generated.financials.financials_request_builder')
functions_request_builder = lazy_import('msgraph.generated.functions.functions_request_builder')
attribute_mapping_function_schema_item_request_builder = lazy_import('msgraph.generated.functions.item.attribute_mapping_function_schema_item_request_builder')
governance_resources_request_builder = lazy_import('msgraph.generated.governance_resources.governance_resources_request_builder')
governance_resource_item_request_builder = lazy_import('msgraph.generated.governance_resources.item.governance_resource_item_request_builder')
governance_role_assignment_requests_request_builder = lazy_import('msgraph.generated.governance_role_assignment_requests.governance_role_assignment_requests_request_builder')
governance_role_assignment_request_item_request_builder = lazy_import('msgraph.generated.governance_role_assignment_requests.item.governance_role_assignment_request_item_request_builder')
governance_role_assignments_request_builder = lazy_import('msgraph.generated.governance_role_assignments.governance_role_assignments_request_builder')
governance_role_assignment_item_request_builder = lazy_import('msgraph.generated.governance_role_assignments.item.governance_role_assignment_item_request_builder')
governance_role_definitions_request_builder = lazy_import('msgraph.generated.governance_role_definitions.governance_role_definitions_request_builder')
governance_role_definition_item_request_builder = lazy_import('msgraph.generated.governance_role_definitions.item.governance_role_definition_item_request_builder')
governance_role_settings_request_builder = lazy_import('msgraph.generated.governance_role_settings.governance_role_settings_request_builder')
governance_role_setting_item_request_builder = lazy_import('msgraph.generated.governance_role_settings.item.governance_role_setting_item_request_builder')
governance_subjects_request_builder = lazy_import('msgraph.generated.governance_subjects.governance_subjects_request_builder')
governance_subject_item_request_builder = lazy_import('msgraph.generated.governance_subjects.item.governance_subject_item_request_builder')
group_lifecycle_policies_request_builder = lazy_import('msgraph.generated.group_lifecycle_policies.group_lifecycle_policies_request_builder')
group_lifecycle_policy_item_request_builder = lazy_import('msgraph.generated.group_lifecycle_policies.item.group_lifecycle_policy_item_request_builder')
groups_request_builder = lazy_import('msgraph.generated.groups.groups_request_builder')
group_item_request_builder = lazy_import('msgraph.generated.groups.item.group_item_request_builder')
identity_request_builder = lazy_import('msgraph.generated.identity.identity_request_builder')
identity_governance_request_builder = lazy_import('msgraph.generated.identity_governance.identity_governance_request_builder')
identity_protection_request_builder = lazy_import('msgraph.generated.identity_protection.identity_protection_request_builder')
identity_providers_request_builder = lazy_import('msgraph.generated.identity_providers.identity_providers_request_builder')
identity_provider_item_request_builder = lazy_import('msgraph.generated.identity_providers.item.identity_provider_item_request_builder')
information_protection_request_builder = lazy_import('msgraph.generated.information_protection.information_protection_request_builder')
invitations_request_builder = lazy_import('msgraph.generated.invitations.invitations_request_builder')
invitation_item_request_builder = lazy_import('msgraph.generated.invitations.item.invitation_item_request_builder')
me_request_builder = lazy_import('msgraph.generated.me.me_request_builder')
message_events_request_builder = lazy_import('msgraph.generated.message_events.message_events_request_builder')
message_event_item_request_builder = lazy_import('msgraph.generated.message_events.item.message_event_item_request_builder')
message_recipients_request_builder = lazy_import('msgraph.generated.message_recipients.message_recipients_request_builder')
message_recipient_item_request_builder = lazy_import('msgraph.generated.message_recipients.item.message_recipient_item_request_builder')
message_traces_request_builder = lazy_import('msgraph.generated.message_traces.message_traces_request_builder')
message_trace_item_request_builder = lazy_import('msgraph.generated.message_traces.item.message_trace_item_request_builder')
mobility_management_policies_request_builder = lazy_import('msgraph.generated.mobility_management_policies.mobility_management_policies_request_builder')
mobility_management_policy_item_request_builder = lazy_import('msgraph.generated.mobility_management_policies.item.mobility_management_policy_item_request_builder')
monitoring_request_builder = lazy_import('msgraph.generated.monitoring.monitoring_request_builder')
oauth2_permission_grants_request_builder = lazy_import('msgraph.generated.oauth2_permission_grants.oauth2_permission_grants_request_builder')
o_auth2_permission_grant_item_request_builder = lazy_import('msgraph.generated.oauth2_permission_grants.item.o_auth2_permission_grant_item_request_builder')
office_configuration_request_builder = lazy_import('msgraph.generated.office_configuration.office_configuration_request_builder')
on_premises_publishing_profiles_request_builder = lazy_import('msgraph.generated.on_premises_publishing_profiles.on_premises_publishing_profiles_request_builder')
on_premises_publishing_profile_item_request_builder = lazy_import('msgraph.generated.on_premises_publishing_profiles.item.on_premises_publishing_profile_item_request_builder')
organization_request_builder = lazy_import('msgraph.generated.organization.organization_request_builder')
organization_item_request_builder = lazy_import('msgraph.generated.organization.item.organization_item_request_builder')
payload_response_request_builder = lazy_import('msgraph.generated.payload_response.payload_response_request_builder')
payload_response_item_request_builder = lazy_import('msgraph.generated.payload_response.item.payload_response_item_request_builder')
permission_grants_request_builder = lazy_import('msgraph.generated.permission_grants.permission_grants_request_builder')
resource_specific_permission_grant_item_request_builder = lazy_import('msgraph.generated.permission_grants.item.resource_specific_permission_grant_item_request_builder')
places_request_builder = lazy_import('msgraph.generated.places.places_request_builder')
place_item_request_builder = lazy_import('msgraph.generated.places.item.place_item_request_builder')
planner_request_builder = lazy_import('msgraph.generated.planner.planner_request_builder')
policies_request_builder = lazy_import('msgraph.generated.policies.policies_request_builder')
print_request_builder = lazy_import('msgraph.generated.print.print_request_builder')
privacy_request_builder = lazy_import('msgraph.generated.privacy.privacy_request_builder')
privileged_access_request_builder = lazy_import('msgraph.generated.privileged_access.privileged_access_request_builder')
privileged_access_item_request_builder = lazy_import('msgraph.generated.privileged_access.item.privileged_access_item_request_builder')
privileged_approval_request_builder = lazy_import('msgraph.generated.privileged_approval.privileged_approval_request_builder')
privileged_approval_item_request_builder = lazy_import('msgraph.generated.privileged_approval.item.privileged_approval_item_request_builder')
privileged_operation_events_request_builder = lazy_import('msgraph.generated.privileged_operation_events.privileged_operation_events_request_builder')
privileged_operation_event_item_request_builder = lazy_import('msgraph.generated.privileged_operation_events.item.privileged_operation_event_item_request_builder')
privileged_role_assignment_requests_request_builder = lazy_import('msgraph.generated.privileged_role_assignment_requests.privileged_role_assignment_requests_request_builder')
privileged_role_assignment_request_item_request_builder = lazy_import('msgraph.generated.privileged_role_assignment_requests.item.privileged_role_assignment_request_item_request_builder')
privileged_role_assignments_request_builder = lazy_import('msgraph.generated.privileged_role_assignments.privileged_role_assignments_request_builder')
privileged_role_assignment_item_request_builder = lazy_import('msgraph.generated.privileged_role_assignments.item.privileged_role_assignment_item_request_builder')
privileged_roles_request_builder = lazy_import('msgraph.generated.privileged_roles.privileged_roles_request_builder')
privileged_role_item_request_builder = lazy_import('msgraph.generated.privileged_roles.item.privileged_role_item_request_builder')
privileged_signup_status_request_builder = lazy_import('msgraph.generated.privileged_signup_status.privileged_signup_status_request_builder')
privileged_signup_status_item_request_builder = lazy_import('msgraph.generated.privileged_signup_status.item.privileged_signup_status_item_request_builder')
program_controls_request_builder = lazy_import('msgraph.generated.program_controls.program_controls_request_builder')
program_control_item_request_builder = lazy_import('msgraph.generated.program_controls.item.program_control_item_request_builder')
program_control_types_request_builder = lazy_import('msgraph.generated.program_control_types.program_control_types_request_builder')
program_control_type_item_request_builder = lazy_import('msgraph.generated.program_control_types.item.program_control_type_item_request_builder')
programs_request_builder = lazy_import('msgraph.generated.programs.programs_request_builder')
program_item_request_builder = lazy_import('msgraph.generated.programs.item.program_item_request_builder')
reports_request_builder = lazy_import('msgraph.generated.reports.reports_request_builder')
risk_detections_request_builder = lazy_import('msgraph.generated.risk_detections.risk_detections_request_builder')
risk_detection_item_request_builder = lazy_import('msgraph.generated.risk_detections.item.risk_detection_item_request_builder')
risky_users_request_builder = lazy_import('msgraph.generated.risky_users.risky_users_request_builder')
risky_user_item_request_builder = lazy_import('msgraph.generated.risky_users.item.risky_user_item_request_builder')
role_management_request_builder = lazy_import('msgraph.generated.role_management.role_management_request_builder')
schema_extensions_request_builder = lazy_import('msgraph.generated.schema_extensions.schema_extensions_request_builder')
schema_extension_item_request_builder = lazy_import('msgraph.generated.schema_extensions.item.schema_extension_item_request_builder')
scoped_role_memberships_request_builder = lazy_import('msgraph.generated.scoped_role_memberships.scoped_role_memberships_request_builder')
scoped_role_membership_item_request_builder = lazy_import('msgraph.generated.scoped_role_memberships.item.scoped_role_membership_item_request_builder')
search_request_builder = lazy_import('msgraph.generated.search.search_request_builder')
security_request_builder = lazy_import('msgraph.generated.security.security_request_builder')
service_principals_request_builder = lazy_import('msgraph.generated.service_principals.service_principals_request_builder')
service_principal_item_request_builder = lazy_import('msgraph.generated.service_principals.item.service_principal_item_request_builder')
settings_request_builder = lazy_import('msgraph.generated.settings.settings_request_builder')
directory_setting_item_request_builder = lazy_import('msgraph.generated.settings.item.directory_setting_item_request_builder')
shares_request_builder = lazy_import('msgraph.generated.shares.shares_request_builder')
shared_drive_item_item_request_builder = lazy_import('msgraph.generated.shares.item.shared_drive_item_item_request_builder')
sites_request_builder = lazy_import('msgraph.generated.sites.sites_request_builder')
site_item_request_builder = lazy_import('msgraph.generated.sites.item.site_item_request_builder')
solutions_request_builder = lazy_import('msgraph.generated.solutions.solutions_request_builder')
storage_request_builder = lazy_import('msgraph.generated.storage.storage_request_builder')
subscribed_skus_request_builder = lazy_import('msgraph.generated.subscribed_skus.subscribed_skus_request_builder')
subscribed_sku_item_request_builder = lazy_import('msgraph.generated.subscribed_skus.item.subscribed_sku_item_request_builder')
subscriptions_request_builder = lazy_import('msgraph.generated.subscriptions.subscriptions_request_builder')
subscription_item_request_builder = lazy_import('msgraph.generated.subscriptions.item.subscription_item_request_builder')
teams_request_builder = lazy_import('msgraph.generated.teams.teams_request_builder')
team_item_request_builder = lazy_import('msgraph.generated.teams.item.team_item_request_builder')
teams_templates_request_builder = lazy_import('msgraph.generated.teams_templates.teams_templates_request_builder')
teams_template_item_request_builder = lazy_import('msgraph.generated.teams_templates.item.teams_template_item_request_builder')
team_template_definition_request_builder = lazy_import('msgraph.generated.team_template_definition.team_template_definition_request_builder')
team_template_definition_item_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_template_definition_item_request_builder')
teamwork_request_builder = lazy_import('msgraph.generated.teamwork.teamwork_request_builder')
tenant_relationships_request_builder = lazy_import('msgraph.generated.tenant_relationships.tenant_relationships_request_builder')
term_store_request_builder = lazy_import('msgraph.generated.term_store.term_store_request_builder')
threat_submission_request_builder = lazy_import('msgraph.generated.threat_submission.threat_submission_request_builder')
trust_framework_request_builder = lazy_import('msgraph.generated.trust_framework.trust_framework_request_builder')
users_request_builder = lazy_import('msgraph.generated.users.users_request_builder')
user_item_request_builder = lazy_import('msgraph.generated.users.item.user_item_request_builder')
workbooks_request_builder = lazy_import('msgraph.generated.workbooks.workbooks_request_builder')
drive_item_item_request_builder = lazy_import('msgraph.generated.workbooks.item.drive_item_item_request_builder')

class BaseGraphServiceClient():
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    @property
    def access_review_decisions(self) -> access_review_decisions_request_builder.AccessReviewDecisionsRequestBuilder:
        """
        Provides operations to manage the collection of accessReviewDecision entities.
        """
        return access_review_decisions_request_builder.AccessReviewDecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_reviews(self) -> access_reviews_request_builder.AccessReviewsRequestBuilder:
        """
        Provides operations to manage the collection of accessReview entities.
        """
        return access_reviews_request_builder.AccessReviewsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def activitystatistics(self) -> activitystatistics_request_builder.ActivitystatisticsRequestBuilder:
        """
        Provides operations to manage the collection of activityStatistics entities.
        """
        return activitystatistics_request_builder.ActivitystatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def admin(self) -> admin_request_builder.AdminRequestBuilder:
        """
        Provides operations to manage the admin singleton.
        """
        return admin_request_builder.AdminRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def administrative_units(self) -> administrative_units_request_builder.AdministrativeUnitsRequestBuilder:
        """
        Provides operations to manage the collection of administrativeUnit entities.
        """
        return administrative_units_request_builder.AdministrativeUnitsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agreement_acceptances(self) -> agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder:
        """
        Provides operations to manage the collection of agreementAcceptance entities.
        """
        return agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agreements(self) -> agreements_request_builder.AgreementsRequestBuilder:
        """
        Provides operations to manage the collection of agreement entities.
        """
        return agreements_request_builder.AgreementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def allowed_data_locations(self) -> allowed_data_locations_request_builder.AllowedDataLocationsRequestBuilder:
        """
        Provides operations to manage the collection of allowedDataLocation entities.
        """
        return allowed_data_locations_request_builder.AllowedDataLocationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app(self) -> app_request_builder.AppRequestBuilder:
        """
        Provides operations to manage the commsApplication singleton.
        """
        return app_request_builder.AppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_catalogs(self) -> app_catalogs_request_builder.AppCatalogsRequestBuilder:
        """
        Provides operations to manage the appCatalogs singleton.
        """
        return app_catalogs_request_builder.AppCatalogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def applications(self) -> applications_request_builder.ApplicationsRequestBuilder:
        """
        Provides operations to manage the collection of application entities.
        """
        return applications_request_builder.ApplicationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def application_templates(self) -> application_templates_request_builder.ApplicationTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of applicationTemplate entities.
        """
        return application_templates_request_builder.ApplicationTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_role_assignments(self) -> app_role_assignments_request_builder.AppRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the collection of appRoleAssignment entities.
        """
        return app_role_assignments_request_builder.AppRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def approval_workflow_providers(self) -> approval_workflow_providers_request_builder.ApprovalWorkflowProvidersRequestBuilder:
        """
        Provides operations to manage the collection of approvalWorkflowProvider entities.
        """
        return approval_workflow_providers_request_builder.ApprovalWorkflowProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def audit_logs(self) -> audit_logs_request_builder.AuditLogsRequestBuilder:
        """
        Provides operations to manage the auditLogRoot singleton.
        """
        return audit_logs_request_builder.AuditLogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_method_configurations(self) -> authentication_method_configurations_request_builder.AuthenticationMethodConfigurationsRequestBuilder:
        """
        Provides operations to manage the collection of authenticationMethodConfiguration entities.
        """
        return authentication_method_configurations_request_builder.AuthenticationMethodConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_methods_policy(self) -> authentication_methods_policy_request_builder.AuthenticationMethodsPolicyRequestBuilder:
        """
        Provides operations to manage the authenticationMethodsPolicy singleton.
        """
        return authentication_methods_policy_request_builder.AuthenticationMethodsPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def booking_businesses(self) -> booking_businesses_request_builder.BookingBusinessesRequestBuilder:
        """
        Provides operations to manage the collection of bookingBusiness entities.
        """
        return booking_businesses_request_builder.BookingBusinessesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def booking_currencies(self) -> booking_currencies_request_builder.BookingCurrenciesRequestBuilder:
        """
        Provides operations to manage the collection of bookingCurrency entities.
        """
        return booking_currencies_request_builder.BookingCurrenciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def branding(self) -> branding_request_builder.BrandingRequestBuilder:
        """
        Provides operations to manage the organizationalBranding singleton.
        """
        return branding_request_builder.BrandingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def business_flow_templates(self) -> business_flow_templates_request_builder.BusinessFlowTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of businessFlowTemplate entities.
        """
        return business_flow_templates_request_builder.BusinessFlowTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def certificate_based_auth_configuration(self) -> certificate_based_auth_configuration_request_builder.CertificateBasedAuthConfigurationRequestBuilder:
        """
        Provides operations to manage the collection of certificateBasedAuthConfiguration entities.
        """
        return certificate_based_auth_configuration_request_builder.CertificateBasedAuthConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chats(self) -> chats_request_builder.ChatsRequestBuilder:
        """
        Provides operations to manage the collection of chat entities.
        """
        return chats_request_builder.ChatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def commands(self) -> commands_request_builder.CommandsRequestBuilder:
        """
        Provides operations to manage the collection of command entities.
        """
        return commands_request_builder.CommandsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def communications(self) -> communications_request_builder.CommunicationsRequestBuilder:
        """
        Provides operations to manage the cloudCommunications singleton.
        """
        return communications_request_builder.CommunicationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance(self) -> compliance_request_builder.ComplianceRequestBuilder:
        """
        Provides operations to manage the compliance singleton.
        """
        return compliance_request_builder.ComplianceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def connections(self) -> connections_request_builder.ConnectionsRequestBuilder:
        """
        Provides operations to manage the collection of externalConnection entities.
        """
        return connections_request_builder.ConnectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contacts(self) -> contacts_request_builder.ContactsRequestBuilder:
        """
        Provides operations to manage the collection of orgContact entities.
        """
        return contacts_request_builder.ContactsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contracts(self) -> contracts_request_builder.ContractsRequestBuilder:
        """
        Provides operations to manage the collection of contract entities.
        """
        return contracts_request_builder.ContractsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_classification(self) -> data_classification_request_builder.DataClassificationRequestBuilder:
        """
        Provides operations to manage the dataClassificationService singleton.
        """
        return data_classification_request_builder.DataClassificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_policy_operations(self) -> data_policy_operations_request_builder.DataPolicyOperationsRequestBuilder:
        """
        Provides operations to manage the collection of dataPolicyOperation entities.
        """
        return data_policy_operations_request_builder.DataPolicyOperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_app_management(self) -> device_app_management_request_builder.DeviceAppManagementRequestBuilder:
        """
        Provides operations to manage the deviceAppManagement singleton.
        """
        return device_app_management_request_builder.DeviceAppManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management(self) -> device_management_request_builder.DeviceManagementRequestBuilder:
        """
        Provides operations to manage the deviceManagement singleton.
        """
        return device_management_request_builder.DeviceManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def devices(self) -> devices_request_builder.DevicesRequestBuilder:
        """
        Provides operations to manage the collection of device entities.
        """
        return devices_request_builder.DevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory(self) -> directory_request_builder.DirectoryRequestBuilder:
        """
        Provides operations to manage the directory singleton.
        """
        return directory_request_builder.DirectoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_objects(self) -> directory_objects_request_builder.DirectoryObjectsRequestBuilder:
        """
        Provides operations to manage the collection of directoryObject entities.
        """
        return directory_objects_request_builder.DirectoryObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_roles(self) -> directory_roles_request_builder.DirectoryRolesRequestBuilder:
        """
        Provides operations to manage the collection of directoryRole entities.
        """
        return directory_roles_request_builder.DirectoryRolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_role_templates(self) -> directory_role_templates_request_builder.DirectoryRoleTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of directoryRoleTemplate entities.
        """
        return directory_role_templates_request_builder.DirectoryRoleTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_setting_templates(self) -> directory_setting_templates_request_builder.DirectorySettingTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of directorySettingTemplate entities.
        """
        return directory_setting_templates_request_builder.DirectorySettingTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def domain_dns_records(self) -> domain_dns_records_request_builder.DomainDnsRecordsRequestBuilder:
        """
        Provides operations to manage the collection of domainDnsRecord entities.
        """
        return domain_dns_records_request_builder.DomainDnsRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def domains(self) -> domains_request_builder.DomainsRequestBuilder:
        """
        Provides operations to manage the collection of domain entities.
        """
        return domains_request_builder.DomainsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive(self) -> drive_request_builder.DriveRequestBuilder:
        """
        Provides operations to manage the drive singleton.
        """
        return drive_request_builder.DriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drives(self) -> drives_request_builder.DrivesRequestBuilder:
        """
        Provides operations to manage the collection of drive entities.
        """
        return drives_request_builder.DrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def education(self) -> education_request_builder.EducationRequestBuilder:
        """
        Provides operations to manage the educationRoot singleton.
        """
        return education_request_builder.EducationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employee_experience(self) -> employee_experience_request_builder.EmployeeExperienceRequestBuilder:
        """
        Provides operations to manage the employeeExperience singleton.
        """
        return employee_experience_request_builder.EmployeeExperienceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external(self) -> external_request_builder.ExternalRequestBuilder:
        """
        Provides operations to manage the external singleton.
        """
        return external_request_builder.ExternalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def filter_operators(self) -> filter_operators_request_builder.FilterOperatorsRequestBuilder:
        """
        Provides operations to manage the collection of filterOperatorSchema entities.
        """
        return filter_operators_request_builder.FilterOperatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def financials(self) -> financials_request_builder.FinancialsRequestBuilder:
        """
        Provides operations to manage the financials singleton.
        """
        return financials_request_builder.FinancialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def functions(self) -> functions_request_builder.FunctionsRequestBuilder:
        """
        Provides operations to manage the collection of attributeMappingFunctionSchema entities.
        """
        return functions_request_builder.FunctionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def governance_resources(self) -> governance_resources_request_builder.GovernanceResourcesRequestBuilder:
        """
        Provides operations to manage the collection of governanceResource entities.
        """
        return governance_resources_request_builder.GovernanceResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def governance_role_assignment_requests(self) -> governance_role_assignment_requests_request_builder.GovernanceRoleAssignmentRequestsRequestBuilder:
        """
        Provides operations to manage the collection of governanceRoleAssignmentRequest entities.
        """
        return governance_role_assignment_requests_request_builder.GovernanceRoleAssignmentRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def governance_role_assignments(self) -> governance_role_assignments_request_builder.GovernanceRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the collection of governanceRoleAssignment entities.
        """
        return governance_role_assignments_request_builder.GovernanceRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def governance_role_definitions(self) -> governance_role_definitions_request_builder.GovernanceRoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the collection of governanceRoleDefinition entities.
        """
        return governance_role_definitions_request_builder.GovernanceRoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def governance_role_settings(self) -> governance_role_settings_request_builder.GovernanceRoleSettingsRequestBuilder:
        """
        Provides operations to manage the collection of governanceRoleSetting entities.
        """
        return governance_role_settings_request_builder.GovernanceRoleSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def governance_subjects(self) -> governance_subjects_request_builder.GovernanceSubjectsRequestBuilder:
        """
        Provides operations to manage the collection of governanceSubject entities.
        """
        return governance_subjects_request_builder.GovernanceSubjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_lifecycle_policies(self) -> group_lifecycle_policies_request_builder.GroupLifecyclePoliciesRequestBuilder:
        """
        Provides operations to manage the collection of groupLifecyclePolicy entities.
        """
        return group_lifecycle_policies_request_builder.GroupLifecyclePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def groups(self) -> groups_request_builder.GroupsRequestBuilder:
        """
        Provides operations to manage the collection of group entities.
        """
        return groups_request_builder.GroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity(self) -> identity_request_builder.IdentityRequestBuilder:
        """
        Provides operations to manage the identityContainer singleton.
        """
        return identity_request_builder.IdentityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_governance(self) -> identity_governance_request_builder.IdentityGovernanceRequestBuilder:
        """
        Provides operations to manage the identityGovernance singleton.
        """
        return identity_governance_request_builder.IdentityGovernanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_protection(self) -> identity_protection_request_builder.IdentityProtectionRequestBuilder:
        """
        Provides operations to manage the identityProtectionRoot singleton.
        """
        return identity_protection_request_builder.IdentityProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_providers(self) -> identity_providers_request_builder.IdentityProvidersRequestBuilder:
        """
        Provides operations to manage the collection of identityProvider entities.
        """
        return identity_providers_request_builder.IdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def information_protection(self) -> information_protection_request_builder.InformationProtectionRequestBuilder:
        """
        Provides operations to manage the informationProtection singleton.
        """
        return information_protection_request_builder.InformationProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invitations(self) -> invitations_request_builder.InvitationsRequestBuilder:
        """
        Provides operations to manage the collection of invitation entities.
        """
        return invitations_request_builder.InvitationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def me(self) -> me_request_builder.MeRequestBuilder:
        """
        Provides operations to manage the user singleton.
        """
        return me_request_builder.MeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def message_events(self) -> message_events_request_builder.MessageEventsRequestBuilder:
        """
        Provides operations to manage the collection of messageEvent entities.
        """
        return message_events_request_builder.MessageEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def message_recipients(self) -> message_recipients_request_builder.MessageRecipientsRequestBuilder:
        """
        Provides operations to manage the collection of messageRecipient entities.
        """
        return message_recipients_request_builder.MessageRecipientsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def message_traces(self) -> message_traces_request_builder.MessageTracesRequestBuilder:
        """
        Provides operations to manage the collection of messageTrace entities.
        """
        return message_traces_request_builder.MessageTracesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobility_management_policies(self) -> mobility_management_policies_request_builder.MobilityManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the collection of mobilityManagementPolicy entities.
        """
        return mobility_management_policies_request_builder.MobilityManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monitoring(self) -> monitoring_request_builder.MonitoringRequestBuilder:
        """
        Provides operations to manage the monitoring singleton.
        """
        return monitoring_request_builder.MonitoringRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oauth2_permission_grants(self) -> oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the collection of oAuth2PermissionGrant entities.
        """
        return oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def office_configuration(self) -> office_configuration_request_builder.OfficeConfigurationRequestBuilder:
        """
        Provides operations to manage the officeConfiguration singleton.
        """
        return office_configuration_request_builder.OfficeConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def on_premises_publishing_profiles(self) -> on_premises_publishing_profiles_request_builder.OnPremisesPublishingProfilesRequestBuilder:
        """
        Provides operations to manage the collection of onPremisesPublishingProfile entities.
        """
        return on_premises_publishing_profiles_request_builder.OnPremisesPublishingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def organization(self) -> organization_request_builder.OrganizationRequestBuilder:
        """
        Provides operations to manage the collection of organization entities.
        """
        return organization_request_builder.OrganizationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payload_response(self) -> payload_response_request_builder.PayloadResponseRequestBuilder:
        """
        Provides operations to manage the collection of payloadResponse entities.
        """
        return payload_response_request_builder.PayloadResponseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grants(self) -> permission_grants_request_builder.PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the collection of resourceSpecificPermissionGrant entities.
        """
        return permission_grants_request_builder.PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def places(self) -> places_request_builder.PlacesRequestBuilder:
        """
        Provides operations to manage the collection of place entities.
        """
        return places_request_builder.PlacesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def planner(self) -> planner_request_builder.PlannerRequestBuilder:
        """
        Provides operations to manage the planner singleton.
        """
        return planner_request_builder.PlannerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policies(self) -> policies_request_builder.PoliciesRequestBuilder:
        """
        Provides operations to manage the policyRoot singleton.
        """
        return policies_request_builder.PoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def print(self) -> print_request_builder.PrintRequestBuilder:
        """
        Provides operations to manage the print singleton.
        """
        return print_request_builder.PrintRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privacy(self) -> privacy_request_builder.PrivacyRequestBuilder:
        """
        Provides operations to manage the privacy singleton.
        """
        return privacy_request_builder.PrivacyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_access(self) -> privileged_access_request_builder.PrivilegedAccessRequestBuilder:
        """
        Provides operations to manage the collection of privilegedAccess entities.
        """
        return privileged_access_request_builder.PrivilegedAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_approval(self) -> privileged_approval_request_builder.PrivilegedApprovalRequestBuilder:
        """
        Provides operations to manage the collection of privilegedApproval entities.
        """
        return privileged_approval_request_builder.PrivilegedApprovalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_operation_events(self) -> privileged_operation_events_request_builder.PrivilegedOperationEventsRequestBuilder:
        """
        Provides operations to manage the collection of privilegedOperationEvent entities.
        """
        return privileged_operation_events_request_builder.PrivilegedOperationEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_role_assignment_requests(self) -> privileged_role_assignment_requests_request_builder.PrivilegedRoleAssignmentRequestsRequestBuilder:
        """
        Provides operations to manage the collection of privilegedRoleAssignmentRequest entities.
        """
        return privileged_role_assignment_requests_request_builder.PrivilegedRoleAssignmentRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_role_assignments(self) -> privileged_role_assignments_request_builder.PrivilegedRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the collection of privilegedRoleAssignment entities.
        """
        return privileged_role_assignments_request_builder.PrivilegedRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_roles(self) -> privileged_roles_request_builder.PrivilegedRolesRequestBuilder:
        """
        Provides operations to manage the collection of privilegedRole entities.
        """
        return privileged_roles_request_builder.PrivilegedRolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_signup_status(self) -> privileged_signup_status_request_builder.PrivilegedSignupStatusRequestBuilder:
        """
        Provides operations to manage the collection of privilegedSignupStatus entities.
        """
        return privileged_signup_status_request_builder.PrivilegedSignupStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def program_controls(self) -> program_controls_request_builder.ProgramControlsRequestBuilder:
        """
        Provides operations to manage the collection of programControl entities.
        """
        return program_controls_request_builder.ProgramControlsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def program_control_types(self) -> program_control_types_request_builder.ProgramControlTypesRequestBuilder:
        """
        Provides operations to manage the collection of programControlType entities.
        """
        return program_control_types_request_builder.ProgramControlTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def programs(self) -> programs_request_builder.ProgramsRequestBuilder:
        """
        Provides operations to manage the collection of program entities.
        """
        return programs_request_builder.ProgramsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reports(self) -> reports_request_builder.ReportsRequestBuilder:
        """
        Provides operations to manage the reportRoot singleton.
        """
        return reports_request_builder.ReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def risk_detections(self) -> risk_detections_request_builder.RiskDetectionsRequestBuilder:
        """
        Provides operations to manage the collection of riskDetection entities.
        """
        return risk_detections_request_builder.RiskDetectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def risky_users(self) -> risky_users_request_builder.RiskyUsersRequestBuilder:
        """
        Provides operations to manage the collection of riskyUser entities.
        """
        return risky_users_request_builder.RiskyUsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_management(self) -> role_management_request_builder.RoleManagementRequestBuilder:
        """
        Provides operations to manage the roleManagement singleton.
        """
        return role_management_request_builder.RoleManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schema_extensions(self) -> schema_extensions_request_builder.SchemaExtensionsRequestBuilder:
        """
        Provides operations to manage the collection of schemaExtension entities.
        """
        return schema_extensions_request_builder.SchemaExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def scoped_role_memberships(self) -> scoped_role_memberships_request_builder.ScopedRoleMembershipsRequestBuilder:
        """
        Provides operations to manage the collection of scopedRoleMembership entities.
        """
        return scoped_role_memberships_request_builder.ScopedRoleMembershipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> search_request_builder.SearchRequestBuilder:
        """
        Provides operations to manage the searchEntity singleton.
        """
        return search_request_builder.SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security(self) -> security_request_builder.SecurityRequestBuilder:
        """
        Provides operations to manage the security singleton.
        """
        return security_request_builder.SecurityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_principals(self) -> service_principals_request_builder.ServicePrincipalsRequestBuilder:
        """
        Provides operations to manage the collection of servicePrincipal entities.
        """
        return service_principals_request_builder.ServicePrincipalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the collection of directorySetting entities.
        """
        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shares(self) -> shares_request_builder.SharesRequestBuilder:
        """
        Provides operations to manage the collection of sharedDriveItem entities.
        """
        return shares_request_builder.SharesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sites(self) -> sites_request_builder.SitesRequestBuilder:
        """
        Provides operations to manage the collection of site entities.
        """
        return sites_request_builder.SitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def solutions(self) -> solutions_request_builder.SolutionsRequestBuilder:
        """
        Provides operations to manage the solutionsRoot singleton.
        """
        return solutions_request_builder.SolutionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def storage(self) -> storage_request_builder.StorageRequestBuilder:
        """
        Provides operations to manage the storage singleton.
        """
        return storage_request_builder.StorageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscribed_skus(self) -> subscribed_skus_request_builder.SubscribedSkusRequestBuilder:
        """
        Provides operations to manage the collection of subscribedSku entities.
        """
        return subscribed_skus_request_builder.SubscribedSkusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscriptions(self) -> subscriptions_request_builder.SubscriptionsRequestBuilder:
        """
        Provides operations to manage the collection of subscription entities.
        """
        return subscriptions_request_builder.SubscriptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teams(self) -> teams_request_builder.TeamsRequestBuilder:
        """
        Provides operations to manage the collection of team entities.
        """
        return teams_request_builder.TeamsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teams_templates(self) -> teams_templates_request_builder.TeamsTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of teamsTemplate entities.
        """
        return teams_templates_request_builder.TeamsTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def team_template_definition(self) -> team_template_definition_request_builder.TeamTemplateDefinitionRequestBuilder:
        """
        Provides operations to manage the collection of teamTemplateDefinition entities.
        """
        return team_template_definition_request_builder.TeamTemplateDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teamwork(self) -> teamwork_request_builder.TeamworkRequestBuilder:
        """
        Provides operations to manage the teamwork singleton.
        """
        return teamwork_request_builder.TeamworkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenant_relationships(self) -> tenant_relationships_request_builder.TenantRelationshipsRequestBuilder:
        """
        Provides operations to manage the tenantRelationship singleton.
        """
        return tenant_relationships_request_builder.TenantRelationshipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def term_store(self) -> term_store_request_builder.TermStoreRequestBuilder:
        """
        Provides operations to manage the store singleton.
        """
        return term_store_request_builder.TermStoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def threat_submission(self) -> threat_submission_request_builder.ThreatSubmissionRequestBuilder:
        """
        Provides operations to manage the threatSubmissionRoot singleton.
        """
        return threat_submission_request_builder.ThreatSubmissionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trust_framework(self) -> trust_framework_request_builder.TrustFrameworkRequestBuilder:
        """
        Provides operations to manage the trustFramework singleton.
        """
        return trust_framework_request_builder.TrustFrameworkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> users_request_builder.UsersRequestBuilder:
        """
        Provides operations to manage the collection of user entities.
        """
        return users_request_builder.UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def workbooks(self) -> workbooks_request_builder.WorkbooksRequestBuilder:
        """
        Provides operations to manage the collection of driveItem entities.
        """
        return workbooks_request_builder.WorkbooksRequestBuilder(self.request_adapter, self.path_parameters)
    
    def access_review_decisions_by_id(self,id: str) -> access_review_decision_item_request_builder.AccessReviewDecisionItemRequestBuilder:
        """
        Provides operations to manage the collection of accessReviewDecision entities.
        Args:
            id: Unique identifier of the item
        Returns: access_review_decision_item_request_builder.AccessReviewDecisionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReviewDecision%2Did"] = id
        return access_review_decision_item_request_builder.AccessReviewDecisionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def access_reviews_by_id(self,id: str) -> access_review_item_request_builder.AccessReviewItemRequestBuilder:
        """
        Provides operations to manage the collection of accessReview entities.
        Args:
            id: Unique identifier of the item
        Returns: access_review_item_request_builder.AccessReviewItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReview%2Did"] = id
        return access_review_item_request_builder.AccessReviewItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def activitystatistics_by_id(self,id: str) -> activity_statistics_item_request_builder.ActivityStatisticsItemRequestBuilder:
        """
        Provides operations to manage the collection of activityStatistics entities.
        Args:
            id: Unique identifier of the item
        Returns: activity_statistics_item_request_builder.ActivityStatisticsItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["activityStatistics%2Did"] = id
        return activity_statistics_item_request_builder.ActivityStatisticsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def administrative_units_by_id(self,id: str) -> administrative_unit_item_request_builder.AdministrativeUnitItemRequestBuilder:
        """
        Provides operations to manage the collection of administrativeUnit entities.
        Args:
            id: Unique identifier of the item
        Returns: administrative_unit_item_request_builder.AdministrativeUnitItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["administrativeUnit%2Did"] = id
        return administrative_unit_item_request_builder.AdministrativeUnitItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def agreement_acceptances_by_id(self,id: str) -> agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder:
        """
        Provides operations to manage the collection of agreementAcceptance entities.
        Args:
            id: Unique identifier of the item
        Returns: agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreementAcceptance%2Did"] = id
        return agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def agreements_by_id(self,id: str) -> agreement_item_request_builder.AgreementItemRequestBuilder:
        """
        Provides operations to manage the collection of agreement entities.
        Args:
            id: Unique identifier of the item
        Returns: agreement_item_request_builder.AgreementItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreement%2Did"] = id
        return agreement_item_request_builder.AgreementItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def allowed_data_locations_by_id(self,id: str) -> allowed_data_location_item_request_builder.AllowedDataLocationItemRequestBuilder:
        """
        Provides operations to manage the collection of allowedDataLocation entities.
        Args:
            id: Unique identifier of the item
        Returns: allowed_data_location_item_request_builder.AllowedDataLocationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["allowedDataLocation%2Did"] = id
        return allowed_data_location_item_request_builder.AllowedDataLocationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def applications_by_id(self,id: str) -> application_item_request_builder.ApplicationItemRequestBuilder:
        """
        Provides operations to manage the collection of application entities.
        Args:
            id: Unique identifier of the item
        Returns: application_item_request_builder.ApplicationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["application%2Did"] = id
        return application_item_request_builder.ApplicationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def application_templates_by_id(self,id: str) -> application_template_item_request_builder.ApplicationTemplateItemRequestBuilder:
        """
        Provides operations to manage the collection of applicationTemplate entities.
        Args:
            id: Unique identifier of the item
        Returns: application_template_item_request_builder.ApplicationTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["applicationTemplate%2Did"] = id
        return application_template_item_request_builder.ApplicationTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def app_role_assignments_by_id(self,id: str) -> app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the collection of appRoleAssignment entities.
        Args:
            id: Unique identifier of the item
        Returns: app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["appRoleAssignment%2Did"] = id
        return app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def approval_workflow_providers_by_id(self,id: str) -> approval_workflow_provider_item_request_builder.ApprovalWorkflowProviderItemRequestBuilder:
        """
        Provides operations to manage the collection of approvalWorkflowProvider entities.
        Args:
            id: Unique identifier of the item
        Returns: approval_workflow_provider_item_request_builder.ApprovalWorkflowProviderItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["approvalWorkflowProvider%2Did"] = id
        return approval_workflow_provider_item_request_builder.ApprovalWorkflowProviderItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def authentication_method_configurations_by_id(self,id: str) -> authentication_method_configuration_item_request_builder.AuthenticationMethodConfigurationItemRequestBuilder:
        """
        Provides operations to manage the collection of authenticationMethodConfiguration entities.
        Args:
            id: Unique identifier of the item
        Returns: authentication_method_configuration_item_request_builder.AuthenticationMethodConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["authenticationMethodConfiguration%2Did"] = id
        return authentication_method_configuration_item_request_builder.AuthenticationMethodConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def booking_businesses_by_id(self,id: str) -> booking_business_item_request_builder.BookingBusinessItemRequestBuilder:
        """
        Provides operations to manage the collection of bookingBusiness entities.
        Args:
            id: Unique identifier of the item
        Returns: booking_business_item_request_builder.BookingBusinessItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["bookingBusiness%2Did"] = id
        return booking_business_item_request_builder.BookingBusinessItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def booking_currencies_by_id(self,id: str) -> booking_currency_item_request_builder.BookingCurrencyItemRequestBuilder:
        """
        Provides operations to manage the collection of bookingCurrency entities.
        Args:
            id: Unique identifier of the item
        Returns: booking_currency_item_request_builder.BookingCurrencyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["bookingCurrency%2Did"] = id
        return booking_currency_item_request_builder.BookingCurrencyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def business_flow_templates_by_id(self,id: str) -> business_flow_template_item_request_builder.BusinessFlowTemplateItemRequestBuilder:
        """
        Provides operations to manage the collection of businessFlowTemplate entities.
        Args:
            id: Unique identifier of the item
        Returns: business_flow_template_item_request_builder.BusinessFlowTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["businessFlowTemplate%2Did"] = id
        return business_flow_template_item_request_builder.BusinessFlowTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def certificate_based_auth_configuration_by_id(self,id: str) -> certificate_based_auth_configuration_item_request_builder.CertificateBasedAuthConfigurationItemRequestBuilder:
        """
        Provides operations to manage the collection of certificateBasedAuthConfiguration entities.
        Args:
            id: Unique identifier of the item
        Returns: certificate_based_auth_configuration_item_request_builder.CertificateBasedAuthConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["certificateBasedAuthConfiguration%2Did"] = id
        return certificate_based_auth_configuration_item_request_builder.CertificateBasedAuthConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def chats_by_id(self,id: str) -> chat_item_request_builder.ChatItemRequestBuilder:
        """
        Provides operations to manage the collection of chat entities.
        Args:
            id: Unique identifier of the item
        Returns: chat_item_request_builder.ChatItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["chat%2Did"] = id
        return chat_item_request_builder.ChatItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def commands_by_id(self,id: str) -> command_item_request_builder.CommandItemRequestBuilder:
        """
        Provides operations to manage the collection of command entities.
        Args:
            id: Unique identifier of the item
        Returns: command_item_request_builder.CommandItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["command%2Did"] = id
        return command_item_request_builder.CommandItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def connections_by_id(self,id: str) -> external_connection_item_request_builder.ExternalConnectionItemRequestBuilder:
        """
        Provides operations to manage the collection of externalConnection entities.
        Args:
            id: Unique identifier of the item
        Returns: external_connection_item_request_builder.ExternalConnectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["externalConnection%2Did"] = id
        return external_connection_item_request_builder.ExternalConnectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter) -> None:
        """
        Instantiates a new BaseGraphServiceClient and sets the default values.
        Args:
            requestAdapter: The request adapter to use to execute the requests.
        """
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Path parameters for the request
        self.path_parameters: Dict[str, Any] = {}

        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}"

        self.request_adapter = request_adapter
        register_default_serializer(JsonSerializationWriterFactory)
        register_default_serializer(TextSerializationWriterFactory)
        register_default_deserializer(JsonParseNodeFactory)
        register_default_deserializer(TextParseNodeFactory)
        if not request_adapter.base_url:
            request_adapter.base_url = "https://graph.microsoft.com/beta"
    
    def contacts_by_id(self,id: str) -> org_contact_item_request_builder.OrgContactItemRequestBuilder:
        """
        Provides operations to manage the collection of orgContact entities.
        Args:
            id: Unique identifier of the item
        Returns: org_contact_item_request_builder.OrgContactItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["orgContact%2Did"] = id
        return org_contact_item_request_builder.OrgContactItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def contracts_by_id(self,id: str) -> contract_item_request_builder.ContractItemRequestBuilder:
        """
        Provides operations to manage the collection of contract entities.
        Args:
            id: Unique identifier of the item
        Returns: contract_item_request_builder.ContractItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["contract%2Did"] = id
        return contract_item_request_builder.ContractItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def data_policy_operations_by_id(self,id: str) -> data_policy_operation_item_request_builder.DataPolicyOperationItemRequestBuilder:
        """
        Provides operations to manage the collection of dataPolicyOperation entities.
        Args:
            id: Unique identifier of the item
        Returns: data_policy_operation_item_request_builder.DataPolicyOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["dataPolicyOperation%2Did"] = id
        return data_policy_operation_item_request_builder.DataPolicyOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def devices_by_id(self,id: str) -> device_item_request_builder.DeviceItemRequestBuilder:
        """
        Provides operations to manage the collection of device entities.
        Args:
            id: Unique identifier of the item
        Returns: device_item_request_builder.DeviceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["device%2Did"] = id
        return device_item_request_builder.DeviceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def directory_objects_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the collection of directoryObject entities.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def directory_roles_by_id(self,id: str) -> directory_role_item_request_builder.DirectoryRoleItemRequestBuilder:
        """
        Provides operations to manage the collection of directoryRole entities.
        Args:
            id: Unique identifier of the item
        Returns: directory_role_item_request_builder.DirectoryRoleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryRole%2Did"] = id
        return directory_role_item_request_builder.DirectoryRoleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def directory_role_templates_by_id(self,id: str) -> directory_role_template_item_request_builder.DirectoryRoleTemplateItemRequestBuilder:
        """
        Provides operations to manage the collection of directoryRoleTemplate entities.
        Args:
            id: Unique identifier of the item
        Returns: directory_role_template_item_request_builder.DirectoryRoleTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryRoleTemplate%2Did"] = id
        return directory_role_template_item_request_builder.DirectoryRoleTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def directory_setting_templates_by_id(self,id: str) -> directory_setting_template_item_request_builder.DirectorySettingTemplateItemRequestBuilder:
        """
        Provides operations to manage the collection of directorySettingTemplate entities.
        Args:
            id: Unique identifier of the item
        Returns: directory_setting_template_item_request_builder.DirectorySettingTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directorySettingTemplate%2Did"] = id
        return directory_setting_template_item_request_builder.DirectorySettingTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def domain_dns_records_by_id(self,id: str) -> domain_dns_record_item_request_builder.DomainDnsRecordItemRequestBuilder:
        """
        Provides operations to manage the collection of domainDnsRecord entities.
        Args:
            id: Unique identifier of the item
        Returns: domain_dns_record_item_request_builder.DomainDnsRecordItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["domainDnsRecord%2Did"] = id
        return domain_dns_record_item_request_builder.DomainDnsRecordItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def domains_by_id(self,id: str) -> domain_item_request_builder.DomainItemRequestBuilder:
        """
        Provides operations to manage the collection of domain entities.
        Args:
            id: Unique identifier of the item
        Returns: domain_item_request_builder.DomainItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["domain%2Did"] = id
        return domain_item_request_builder.DomainItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def drives_by_id(self,id: str) -> drive_item_request_builder.DriveItemRequestBuilder:
        """
        Provides operations to manage the collection of drive entities.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_request_builder.DriveItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["drive%2Did"] = id
        return drive_item_request_builder.DriveItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def filter_operators_by_id(self,id: str) -> filter_operator_schema_item_request_builder.FilterOperatorSchemaItemRequestBuilder:
        """
        Provides operations to manage the collection of filterOperatorSchema entities.
        Args:
            id: Unique identifier of the item
        Returns: filter_operator_schema_item_request_builder.FilterOperatorSchemaItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["filterOperatorSchema%2Did"] = id
        return filter_operator_schema_item_request_builder.FilterOperatorSchemaItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def functions_by_id(self,id: str) -> attribute_mapping_function_schema_item_request_builder.AttributeMappingFunctionSchemaItemRequestBuilder:
        """
        Provides operations to manage the collection of attributeMappingFunctionSchema entities.
        Args:
            id: Unique identifier of the item
        Returns: attribute_mapping_function_schema_item_request_builder.AttributeMappingFunctionSchemaItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["attributeMappingFunctionSchema%2Did"] = id
        return attribute_mapping_function_schema_item_request_builder.AttributeMappingFunctionSchemaItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def governance_resources_by_id(self,id: str) -> governance_resource_item_request_builder.GovernanceResourceItemRequestBuilder:
        """
        Provides operations to manage the collection of governanceResource entities.
        Args:
            id: Unique identifier of the item
        Returns: governance_resource_item_request_builder.GovernanceResourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["governanceResource%2Did"] = id
        return governance_resource_item_request_builder.GovernanceResourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def governance_role_assignment_requests_by_id(self,id: str) -> governance_role_assignment_request_item_request_builder.GovernanceRoleAssignmentRequestItemRequestBuilder:
        """
        Provides operations to manage the collection of governanceRoleAssignmentRequest entities.
        Args:
            id: Unique identifier of the item
        Returns: governance_role_assignment_request_item_request_builder.GovernanceRoleAssignmentRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["governanceRoleAssignmentRequest%2Did"] = id
        return governance_role_assignment_request_item_request_builder.GovernanceRoleAssignmentRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def governance_role_assignments_by_id(self,id: str) -> governance_role_assignment_item_request_builder.GovernanceRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the collection of governanceRoleAssignment entities.
        Args:
            id: Unique identifier of the item
        Returns: governance_role_assignment_item_request_builder.GovernanceRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["governanceRoleAssignment%2Did"] = id
        return governance_role_assignment_item_request_builder.GovernanceRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def governance_role_definitions_by_id(self,id: str) -> governance_role_definition_item_request_builder.GovernanceRoleDefinitionItemRequestBuilder:
        """
        Provides operations to manage the collection of governanceRoleDefinition entities.
        Args:
            id: Unique identifier of the item
        Returns: governance_role_definition_item_request_builder.GovernanceRoleDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["governanceRoleDefinition%2Did"] = id
        return governance_role_definition_item_request_builder.GovernanceRoleDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def governance_role_settings_by_id(self,id: str) -> governance_role_setting_item_request_builder.GovernanceRoleSettingItemRequestBuilder:
        """
        Provides operations to manage the collection of governanceRoleSetting entities.
        Args:
            id: Unique identifier of the item
        Returns: governance_role_setting_item_request_builder.GovernanceRoleSettingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["governanceRoleSetting%2Did"] = id
        return governance_role_setting_item_request_builder.GovernanceRoleSettingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def governance_subjects_by_id(self,id: str) -> governance_subject_item_request_builder.GovernanceSubjectItemRequestBuilder:
        """
        Provides operations to manage the collection of governanceSubject entities.
        Args:
            id: Unique identifier of the item
        Returns: governance_subject_item_request_builder.GovernanceSubjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["governanceSubject%2Did"] = id
        return governance_subject_item_request_builder.GovernanceSubjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def group_lifecycle_policies_by_id(self,id: str) -> group_lifecycle_policy_item_request_builder.GroupLifecyclePolicyItemRequestBuilder:
        """
        Provides operations to manage the collection of groupLifecyclePolicy entities.
        Args:
            id: Unique identifier of the item
        Returns: group_lifecycle_policy_item_request_builder.GroupLifecyclePolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupLifecyclePolicy%2Did"] = id
        return group_lifecycle_policy_item_request_builder.GroupLifecyclePolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def groups_by_id(self,id: str) -> group_item_request_builder.GroupItemRequestBuilder:
        """
        Provides operations to manage the collection of group entities.
        Args:
            id: Unique identifier of the item
        Returns: group_item_request_builder.GroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["group%2Did"] = id
        return group_item_request_builder.GroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def identity_providers_by_id(self,id: str) -> identity_provider_item_request_builder.IdentityProviderItemRequestBuilder:
        """
        Provides operations to manage the collection of identityProvider entities.
        Args:
            id: Unique identifier of the item
        Returns: identity_provider_item_request_builder.IdentityProviderItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["identityProvider%2Did"] = id
        return identity_provider_item_request_builder.IdentityProviderItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def invitations_by_id(self,id: str) -> invitation_item_request_builder.InvitationItemRequestBuilder:
        """
        Provides operations to manage the collection of invitation entities.
        Args:
            id: Unique identifier of the item
        Returns: invitation_item_request_builder.InvitationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["invitation%2Did"] = id
        return invitation_item_request_builder.InvitationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def message_events_by_id(self,id: str) -> message_event_item_request_builder.MessageEventItemRequestBuilder:
        """
        Provides operations to manage the collection of messageEvent entities.
        Args:
            id: Unique identifier of the item
        Returns: message_event_item_request_builder.MessageEventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["messageEvent%2Did"] = id
        return message_event_item_request_builder.MessageEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def message_recipients_by_id(self,id: str) -> message_recipient_item_request_builder.MessageRecipientItemRequestBuilder:
        """
        Provides operations to manage the collection of messageRecipient entities.
        Args:
            id: Unique identifier of the item
        Returns: message_recipient_item_request_builder.MessageRecipientItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["messageRecipient%2Did"] = id
        return message_recipient_item_request_builder.MessageRecipientItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def message_traces_by_id(self,id: str) -> message_trace_item_request_builder.MessageTraceItemRequestBuilder:
        """
        Provides operations to manage the collection of messageTrace entities.
        Args:
            id: Unique identifier of the item
        Returns: message_trace_item_request_builder.MessageTraceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["messageTrace%2Did"] = id
        return message_trace_item_request_builder.MessageTraceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def mobility_management_policies_by_id(self,id: str) -> mobility_management_policy_item_request_builder.MobilityManagementPolicyItemRequestBuilder:
        """
        Provides operations to manage the collection of mobilityManagementPolicy entities.
        Args:
            id: Unique identifier of the item
        Returns: mobility_management_policy_item_request_builder.MobilityManagementPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobilityManagementPolicy%2Did"] = id
        return mobility_management_policy_item_request_builder.MobilityManagementPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def oauth2_permission_grants_by_id(self,id: str) -> o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder:
        """
        Provides operations to manage the collection of oAuth2PermissionGrant entities.
        Args:
            id: Unique identifier of the item
        Returns: o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["oAuth2PermissionGrant%2Did"] = id
        return o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def on_premises_publishing_profiles_by_id(self,id: str) -> on_premises_publishing_profile_item_request_builder.OnPremisesPublishingProfileItemRequestBuilder:
        """
        Provides operations to manage the collection of onPremisesPublishingProfile entities.
        Args:
            id: Unique identifier of the item
        Returns: on_premises_publishing_profile_item_request_builder.OnPremisesPublishingProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["onPremisesPublishingProfile%2Did"] = id
        return on_premises_publishing_profile_item_request_builder.OnPremisesPublishingProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def organization_by_id(self,id: str) -> organization_item_request_builder.OrganizationItemRequestBuilder:
        """
        Provides operations to manage the collection of organization entities.
        Args:
            id: Unique identifier of the item
        Returns: organization_item_request_builder.OrganizationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["organization%2Did"] = id
        return organization_item_request_builder.OrganizationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def payload_response_by_id(self,id: str) -> payload_response_item_request_builder.PayloadResponseItemRequestBuilder:
        """
        Provides operations to manage the collection of payloadResponse entities.
        Args:
            id: Unique identifier of the item
        Returns: payload_response_item_request_builder.PayloadResponseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["payloadResponse%2Did"] = id
        return payload_response_item_request_builder.PayloadResponseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def permission_grants_by_id(self,id: str) -> resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder:
        """
        Provides operations to manage the collection of resourceSpecificPermissionGrant entities.
        Args:
            id: Unique identifier of the item
        Returns: resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["resourceSpecificPermissionGrant%2Did"] = id
        return resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def places_by_id(self,id: str) -> place_item_request_builder.PlaceItemRequestBuilder:
        """
        Provides operations to manage the collection of place entities.
        Args:
            id: Unique identifier of the item
        Returns: place_item_request_builder.PlaceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["place%2Did"] = id
        return place_item_request_builder.PlaceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def privileged_access_by_id(self,id: str) -> privileged_access_item_request_builder.PrivilegedAccessItemRequestBuilder:
        """
        Provides operations to manage the collection of privilegedAccess entities.
        Args:
            id: Unique identifier of the item
        Returns: privileged_access_item_request_builder.PrivilegedAccessItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedAccess%2Did"] = id
        return privileged_access_item_request_builder.PrivilegedAccessItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def privileged_approval_by_id(self,id: str) -> privileged_approval_item_request_builder.PrivilegedApprovalItemRequestBuilder:
        """
        Provides operations to manage the collection of privilegedApproval entities.
        Args:
            id: Unique identifier of the item
        Returns: privileged_approval_item_request_builder.PrivilegedApprovalItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedApproval%2Did"] = id
        return privileged_approval_item_request_builder.PrivilegedApprovalItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def privileged_operation_events_by_id(self,id: str) -> privileged_operation_event_item_request_builder.PrivilegedOperationEventItemRequestBuilder:
        """
        Provides operations to manage the collection of privilegedOperationEvent entities.
        Args:
            id: Unique identifier of the item
        Returns: privileged_operation_event_item_request_builder.PrivilegedOperationEventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedOperationEvent%2Did"] = id
        return privileged_operation_event_item_request_builder.PrivilegedOperationEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def privileged_role_assignment_requests_by_id(self,id: str) -> privileged_role_assignment_request_item_request_builder.PrivilegedRoleAssignmentRequestItemRequestBuilder:
        """
        Provides operations to manage the collection of privilegedRoleAssignmentRequest entities.
        Args:
            id: Unique identifier of the item
        Returns: privileged_role_assignment_request_item_request_builder.PrivilegedRoleAssignmentRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedRoleAssignmentRequest%2Did"] = id
        return privileged_role_assignment_request_item_request_builder.PrivilegedRoleAssignmentRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def privileged_role_assignments_by_id(self,id: str) -> privileged_role_assignment_item_request_builder.PrivilegedRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the collection of privilegedRoleAssignment entities.
        Args:
            id: Unique identifier of the item
        Returns: privileged_role_assignment_item_request_builder.PrivilegedRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedRoleAssignment%2Did"] = id
        return privileged_role_assignment_item_request_builder.PrivilegedRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def privileged_roles_by_id(self,id: str) -> privileged_role_item_request_builder.PrivilegedRoleItemRequestBuilder:
        """
        Provides operations to manage the collection of privilegedRole entities.
        Args:
            id: Unique identifier of the item
        Returns: privileged_role_item_request_builder.PrivilegedRoleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedRole%2Did"] = id
        return privileged_role_item_request_builder.PrivilegedRoleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def privileged_signup_status_by_id(self,id: str) -> privileged_signup_status_item_request_builder.PrivilegedSignupStatusItemRequestBuilder:
        """
        Provides operations to manage the collection of privilegedSignupStatus entities.
        Args:
            id: Unique identifier of the item
        Returns: privileged_signup_status_item_request_builder.PrivilegedSignupStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedSignupStatus%2Did"] = id
        return privileged_signup_status_item_request_builder.PrivilegedSignupStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def program_controls_by_id(self,id: str) -> program_control_item_request_builder.ProgramControlItemRequestBuilder:
        """
        Provides operations to manage the collection of programControl entities.
        Args:
            id: Unique identifier of the item
        Returns: program_control_item_request_builder.ProgramControlItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["programControl%2Did"] = id
        return program_control_item_request_builder.ProgramControlItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def program_control_types_by_id(self,id: str) -> program_control_type_item_request_builder.ProgramControlTypeItemRequestBuilder:
        """
        Provides operations to manage the collection of programControlType entities.
        Args:
            id: Unique identifier of the item
        Returns: program_control_type_item_request_builder.ProgramControlTypeItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["programControlType%2Did"] = id
        return program_control_type_item_request_builder.ProgramControlTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def programs_by_id(self,id: str) -> program_item_request_builder.ProgramItemRequestBuilder:
        """
        Provides operations to manage the collection of program entities.
        Args:
            id: Unique identifier of the item
        Returns: program_item_request_builder.ProgramItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["program%2Did"] = id
        return program_item_request_builder.ProgramItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def risk_detections_by_id(self,id: str) -> risk_detection_item_request_builder.RiskDetectionItemRequestBuilder:
        """
        Provides operations to manage the collection of riskDetection entities.
        Args:
            id: Unique identifier of the item
        Returns: risk_detection_item_request_builder.RiskDetectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["riskDetection%2Did"] = id
        return risk_detection_item_request_builder.RiskDetectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def risky_users_by_id(self,id: str) -> risky_user_item_request_builder.RiskyUserItemRequestBuilder:
        """
        Provides operations to manage the collection of riskyUser entities.
        Args:
            id: Unique identifier of the item
        Returns: risky_user_item_request_builder.RiskyUserItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["riskyUser%2Did"] = id
        return risky_user_item_request_builder.RiskyUserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def schema_extensions_by_id(self,id: str) -> schema_extension_item_request_builder.SchemaExtensionItemRequestBuilder:
        """
        Provides operations to manage the collection of schemaExtension entities.
        Args:
            id: Unique identifier of the item
        Returns: schema_extension_item_request_builder.SchemaExtensionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["schemaExtension%2Did"] = id
        return schema_extension_item_request_builder.SchemaExtensionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def scoped_role_memberships_by_id(self,id: str) -> scoped_role_membership_item_request_builder.ScopedRoleMembershipItemRequestBuilder:
        """
        Provides operations to manage the collection of scopedRoleMembership entities.
        Args:
            id: Unique identifier of the item
        Returns: scoped_role_membership_item_request_builder.ScopedRoleMembershipItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["scopedRoleMembership%2Did"] = id
        return scoped_role_membership_item_request_builder.ScopedRoleMembershipItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def service_principals_by_id(self,id: str) -> service_principal_item_request_builder.ServicePrincipalItemRequestBuilder:
        """
        Provides operations to manage the collection of servicePrincipal entities.
        Args:
            id: Unique identifier of the item
        Returns: service_principal_item_request_builder.ServicePrincipalItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["servicePrincipal%2Did"] = id
        return service_principal_item_request_builder.ServicePrincipalItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def settings_by_id(self,id: str) -> directory_setting_item_request_builder.DirectorySettingItemRequestBuilder:
        """
        Provides operations to manage the collection of directorySetting entities.
        Args:
            id: Unique identifier of the item
        Returns: directory_setting_item_request_builder.DirectorySettingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directorySetting%2Did"] = id
        return directory_setting_item_request_builder.DirectorySettingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def shares_by_id(self,id: str) -> shared_drive_item_item_request_builder.SharedDriveItemItemRequestBuilder:
        """
        Provides operations to manage the collection of sharedDriveItem entities.
        Args:
            id: Unique identifier of the item
        Returns: shared_drive_item_item_request_builder.SharedDriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sharedDriveItem%2Did"] = id
        return shared_drive_item_item_request_builder.SharedDriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sites_by_id(self,id: str) -> site_item_request_builder.SiteItemRequestBuilder:
        """
        Provides operations to manage the collection of site entities.
        Args:
            id: Unique identifier of the item
        Returns: site_item_request_builder.SiteItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["site%2Did"] = id
        return site_item_request_builder.SiteItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def subscribed_skus_by_id(self,id: str) -> subscribed_sku_item_request_builder.SubscribedSkuItemRequestBuilder:
        """
        Provides operations to manage the collection of subscribedSku entities.
        Args:
            id: Unique identifier of the item
        Returns: subscribed_sku_item_request_builder.SubscribedSkuItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["subscribedSku%2Did"] = id
        return subscribed_sku_item_request_builder.SubscribedSkuItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def subscriptions_by_id(self,id: str) -> subscription_item_request_builder.SubscriptionItemRequestBuilder:
        """
        Provides operations to manage the collection of subscription entities.
        Args:
            id: Unique identifier of the item
        Returns: subscription_item_request_builder.SubscriptionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["subscription%2Did"] = id
        return subscription_item_request_builder.SubscriptionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def teams_by_id(self,id: str) -> team_item_request_builder.TeamItemRequestBuilder:
        """
        Provides operations to manage the collection of team entities.
        Args:
            id: Unique identifier of the item
        Returns: team_item_request_builder.TeamItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["team%2Did"] = id
        return team_item_request_builder.TeamItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def teams_templates_by_id(self,id: str) -> teams_template_item_request_builder.TeamsTemplateItemRequestBuilder:
        """
        Provides operations to manage the collection of teamsTemplate entities.
        Args:
            id: Unique identifier of the item
        Returns: teams_template_item_request_builder.TeamsTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamsTemplate%2Did"] = id
        return teams_template_item_request_builder.TeamsTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def team_template_definition_by_id(self,id: str) -> team_template_definition_item_request_builder.TeamTemplateDefinitionItemRequestBuilder:
        """
        Provides operations to manage the collection of teamTemplateDefinition entities.
        Args:
            id: Unique identifier of the item
        Returns: team_template_definition_item_request_builder.TeamTemplateDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamTemplateDefinition%2Did"] = id
        return team_template_definition_item_request_builder.TeamTemplateDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def users_by_id(self,id: str) -> user_item_request_builder.UserItemRequestBuilder:
        """
        Provides operations to manage the collection of user entities.
        Args:
            id: Unique identifier of the item
        Returns: user_item_request_builder.UserItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["user%2Did"] = id
        return user_item_request_builder.UserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def workbooks_by_id(self,id: str) -> drive_item_item_request_builder.DriveItemItemRequestBuilder:
        """
        Provides operations to manage the collection of driveItem entities.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_item_request_builder.DriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItem%2Did"] = id
        return drive_item_item_request_builder.DriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    

