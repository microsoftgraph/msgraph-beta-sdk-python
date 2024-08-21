from __future__ import annotations
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from kiota_abstractions.store import BackingStoreFactory, BackingStoreFactorySingleton
from kiota_serialization_form.form_parse_node_factory import FormParseNodeFactory
from kiota_serialization_form.form_serialization_writer_factory import FormSerializationWriterFactory
from kiota_serialization_json.json_parse_node_factory import JsonParseNodeFactory
from kiota_serialization_json.json_serialization_writer_factory import JsonSerializationWriterFactory
from kiota_serialization_multipart.multipart_serialization_writer_factory import MultipartSerializationWriterFactory
from kiota_serialization_text.text_parse_node_factory import TextParseNodeFactory
from kiota_serialization_text.text_serialization_writer_factory import TextSerializationWriterFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_reviews.access_reviews_request_builder import AccessReviewsRequestBuilder
    from .access_review_decisions.access_review_decisions_request_builder import AccessReviewDecisionsRequestBuilder
    from .activitystatistics.activitystatistics_request_builder import ActivitystatisticsRequestBuilder
    from .admin.admin_request_builder import AdminRequestBuilder
    from .administrative_units.administrative_units_request_builder import AdministrativeUnitsRequestBuilder
    from .agreements.agreements_request_builder import AgreementsRequestBuilder
    from .agreement_acceptances.agreement_acceptances_request_builder import AgreementAcceptancesRequestBuilder
    from .allowed_data_locations.allowed_data_locations_request_builder import AllowedDataLocationsRequestBuilder
    from .app.app_request_builder import AppRequestBuilder
    from .applications.applications_request_builder import ApplicationsRequestBuilder
    from .applications_with_app_id.applications_with_app_id_request_builder import ApplicationsWithAppIdRequestBuilder
    from .applications_with_unique_name.applications_with_unique_name_request_builder import ApplicationsWithUniqueNameRequestBuilder
    from .application_templates.application_templates_request_builder import ApplicationTemplatesRequestBuilder
    from .approval_workflow_providers.approval_workflow_providers_request_builder import ApprovalWorkflowProvidersRequestBuilder
    from .app_catalogs.app_catalogs_request_builder import AppCatalogsRequestBuilder
    from .app_role_assignments.app_role_assignments_request_builder import AppRoleAssignmentsRequestBuilder
    from .audit_logs.audit_logs_request_builder import AuditLogsRequestBuilder
    from .authentication_methods_policy.authentication_methods_policy_request_builder import AuthenticationMethodsPolicyRequestBuilder
    from .authentication_method_configurations.authentication_method_configurations_request_builder import AuthenticationMethodConfigurationsRequestBuilder
    from .booking_businesses.booking_businesses_request_builder import BookingBusinessesRequestBuilder
    from .booking_currencies.booking_currencies_request_builder import BookingCurrenciesRequestBuilder
    from .business_flow_templates.business_flow_templates_request_builder import BusinessFlowTemplatesRequestBuilder
    from .certificate_based_auth_configuration.certificate_based_auth_configuration_request_builder import CertificateBasedAuthConfigurationRequestBuilder
    from .chats.chats_request_builder import ChatsRequestBuilder
    from .commands.commands_request_builder import CommandsRequestBuilder
    from .communications.communications_request_builder import CommunicationsRequestBuilder
    from .compliance.compliance_request_builder import ComplianceRequestBuilder
    from .connections.connections_request_builder import ConnectionsRequestBuilder
    from .contacts.contacts_request_builder import ContactsRequestBuilder
    from .contracts.contracts_request_builder import ContractsRequestBuilder
    from .data_classification.data_classification_request_builder import DataClassificationRequestBuilder
    from .data_policy_operations.data_policy_operations_request_builder import DataPolicyOperationsRequestBuilder
    from .devices.devices_request_builder import DevicesRequestBuilder
    from .devices_with_device_id.devices_with_device_id_request_builder import DevicesWithDeviceIdRequestBuilder
    from .device_app_management.device_app_management_request_builder import DeviceAppManagementRequestBuilder
    from .device_local_credentials.device_local_credentials_request_builder import DeviceLocalCredentialsRequestBuilder
    from .device_management.device_management_request_builder import DeviceManagementRequestBuilder
    from .directory.directory_request_builder import DirectoryRequestBuilder
    from .directory_objects.directory_objects_request_builder import DirectoryObjectsRequestBuilder
    from .directory_roles.directory_roles_request_builder import DirectoryRolesRequestBuilder
    from .directory_roles_with_role_template_id.directory_roles_with_role_template_id_request_builder import DirectoryRolesWithRoleTemplateIdRequestBuilder
    from .directory_role_templates.directory_role_templates_request_builder import DirectoryRoleTemplatesRequestBuilder
    from .directory_setting_templates.directory_setting_templates_request_builder import DirectorySettingTemplatesRequestBuilder
    from .domains.domains_request_builder import DomainsRequestBuilder
    from .domain_dns_records.domain_dns_records_request_builder import DomainDnsRecordsRequestBuilder
    from .drives.drives_request_builder import DrivesRequestBuilder
    from .education.education_request_builder import EducationRequestBuilder
    from .employee_experience.employee_experience_request_builder import EmployeeExperienceRequestBuilder
    from .external.external_request_builder import ExternalRequestBuilder
    from .filtering_policies.filtering_policies_request_builder import FilteringPoliciesRequestBuilder
    from .filter_operators.filter_operators_request_builder import FilterOperatorsRequestBuilder
    from .financials.financials_request_builder import FinancialsRequestBuilder
    from .functions.functions_request_builder import FunctionsRequestBuilder
    from .governance_resources.governance_resources_request_builder import GovernanceResourcesRequestBuilder
    from .governance_role_assignments.governance_role_assignments_request_builder import GovernanceRoleAssignmentsRequestBuilder
    from .governance_role_assignment_requests.governance_role_assignment_requests_request_builder import GovernanceRoleAssignmentRequestsRequestBuilder
    from .governance_role_definitions.governance_role_definitions_request_builder import GovernanceRoleDefinitionsRequestBuilder
    from .governance_role_settings.governance_role_settings_request_builder import GovernanceRoleSettingsRequestBuilder
    from .governance_subjects.governance_subjects_request_builder import GovernanceSubjectsRequestBuilder
    from .groups.groups_request_builder import GroupsRequestBuilder
    from .groups_with_unique_name.groups_with_unique_name_request_builder import GroupsWithUniqueNameRequestBuilder
    from .group_lifecycle_policies.group_lifecycle_policies_request_builder import GroupLifecyclePoliciesRequestBuilder
    from .identity.identity_request_builder import IdentityRequestBuilder
    from .identity_governance.identity_governance_request_builder import IdentityGovernanceRequestBuilder
    from .identity_protection.identity_protection_request_builder import IdentityProtectionRequestBuilder
    from .identity_providers.identity_providers_request_builder import IdentityProvidersRequestBuilder
    from .information_protection.information_protection_request_builder import InformationProtectionRequestBuilder
    from .invitations.invitations_request_builder import InvitationsRequestBuilder
    from .message_events.message_events_request_builder import MessageEventsRequestBuilder
    from .message_recipients.message_recipients_request_builder import MessageRecipientsRequestBuilder
    from .message_traces.message_traces_request_builder import MessageTracesRequestBuilder
    from .mobility_management_policies.mobility_management_policies_request_builder import MobilityManagementPoliciesRequestBuilder
    from .monitoring.monitoring_request_builder import MonitoringRequestBuilder
    from .network.network_request_builder import NetworkRequestBuilder
    from .network_access.network_access_request_builder import NetworkAccessRequestBuilder
    from .oauth2_permission_grants.oauth2_permission_grants_request_builder import Oauth2PermissionGrantsRequestBuilder
    from .on_premises_publishing_profiles.on_premises_publishing_profiles_request_builder import OnPremisesPublishingProfilesRequestBuilder
    from .organization.organization_request_builder import OrganizationRequestBuilder
    from .payload_response.payload_response_request_builder import PayloadResponseRequestBuilder
    from .permission_grants.permission_grants_request_builder import PermissionGrantsRequestBuilder
    from .places.places_request_builder import PlacesRequestBuilder
    from .places_with_place_id.places_with_place_id_request_builder import PlacesWithPlaceIdRequestBuilder
    from .planner.planner_request_builder import PlannerRequestBuilder
    from .policies.policies_request_builder import PoliciesRequestBuilder
    from .print.print_request_builder import PrintRequestBuilder
    from .privacy.privacy_request_builder import PrivacyRequestBuilder
    from .privileged_access.privileged_access_request_builder import PrivilegedAccessRequestBuilder
    from .privileged_approval.privileged_approval_request_builder import PrivilegedApprovalRequestBuilder
    from .privileged_operation_events.privileged_operation_events_request_builder import PrivilegedOperationEventsRequestBuilder
    from .privileged_roles.privileged_roles_request_builder import PrivilegedRolesRequestBuilder
    from .privileged_role_assignments.privileged_role_assignments_request_builder import PrivilegedRoleAssignmentsRequestBuilder
    from .privileged_role_assignment_requests.privileged_role_assignment_requests_request_builder import PrivilegedRoleAssignmentRequestsRequestBuilder
    from .privileged_signup_status.privileged_signup_status_request_builder import PrivilegedSignupStatusRequestBuilder
    from .programs.programs_request_builder import ProgramsRequestBuilder
    from .program_controls.program_controls_request_builder import ProgramControlsRequestBuilder
    from .program_control_types.program_control_types_request_builder import ProgramControlTypesRequestBuilder
    from .reports.reports_request_builder import ReportsRequestBuilder
    from .risky_users.risky_users_request_builder import RiskyUsersRequestBuilder
    from .risk_detections.risk_detections_request_builder import RiskDetectionsRequestBuilder
    from .role_management.role_management_request_builder import RoleManagementRequestBuilder
    from .schema_extensions.schema_extensions_request_builder import SchemaExtensionsRequestBuilder
    from .scoped_role_memberships.scoped_role_memberships_request_builder import ScopedRoleMembershipsRequestBuilder
    from .search.search_request_builder import SearchRequestBuilder
    from .security.security_request_builder import SecurityRequestBuilder
    from .service_principals.service_principals_request_builder import ServicePrincipalsRequestBuilder
    from .service_principals_with_app_id.service_principals_with_app_id_request_builder import ServicePrincipalsWithAppIdRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder
    from .shares.shares_request_builder import SharesRequestBuilder
    from .sites.sites_request_builder import SitesRequestBuilder
    from .solutions.solutions_request_builder import SolutionsRequestBuilder
    from .storage.storage_request_builder import StorageRequestBuilder
    from .subscribed_skus.subscribed_skus_request_builder import SubscribedSkusRequestBuilder
    from .subscriptions.subscriptions_request_builder import SubscriptionsRequestBuilder
    from .teams.teams_request_builder import TeamsRequestBuilder
    from .teams_templates.teams_templates_request_builder import TeamsTemplatesRequestBuilder
    from .teamwork.teamwork_request_builder import TeamworkRequestBuilder
    from .team_template_definition.team_template_definition_request_builder import TeamTemplateDefinitionRequestBuilder
    from .tenant_relationships.tenant_relationships_request_builder import TenantRelationshipsRequestBuilder
    from .term_store.term_store_request_builder import TermStoreRequestBuilder
    from .threat_submission.threat_submission_request_builder import ThreatSubmissionRequestBuilder
    from .trust_framework.trust_framework_request_builder import TrustFrameworkRequestBuilder
    from .users.users_request_builder import UsersRequestBuilder
    from .workplace.workplace_request_builder import WorkplaceRequestBuilder

class BaseGraphServiceClient(BaseRequestBuilder):
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    def __init__(self,request_adapter: RequestAdapter, backing_store: Optional[BackingStoreFactory] = None) -> None:
        """
        Instantiates a new BaseGraphServiceClient and sets the default values.
        param backing_store: The backing store to use for the models.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if request_adapter is None:
            raise TypeError("request_adapter cannot be null.")
        super().__init__(request_adapter, "{+baseurl}", None)
        register_default_serializer(JsonSerializationWriterFactory)
        register_default_serializer(TextSerializationWriterFactory)
        register_default_serializer(FormSerializationWriterFactory)
        register_default_serializer(MultipartSerializationWriterFactory)
        register_default_deserializer(JsonParseNodeFactory)
        register_default_deserializer(TextParseNodeFactory)
        register_default_deserializer(FormParseNodeFactory)
        if not self.request_adapter.base_url:
            self.request_adapter.base_url = "https://graph.microsoft.com/beta"
        self.path_parameters["base_url"] = self.request_adapter.base_url
        self.request_adapter.enable_backing_store(backing_store)
    
    def applications_with_app_id(self,app_id: str) -> ApplicationsWithAppIdRequestBuilder:
        """
        Provides operations to manage the collection of application entities.
        param app_id: Alternate key of application
        Returns: ApplicationsWithAppIdRequestBuilder
        """
        if app_id is None:
            raise TypeError("app_id cannot be null.")
        from .applications_with_app_id.applications_with_app_id_request_builder import ApplicationsWithAppIdRequestBuilder

        return ApplicationsWithAppIdRequestBuilder(self.request_adapter, self.path_parameters, app_id)
    
    def applications_with_unique_name(self,unique_name: str) -> ApplicationsWithUniqueNameRequestBuilder:
        """
        Provides operations to manage the collection of application entities.
        param unique_name: Alternate key of application
        Returns: ApplicationsWithUniqueNameRequestBuilder
        """
        if unique_name is None:
            raise TypeError("unique_name cannot be null.")
        from .applications_with_unique_name.applications_with_unique_name_request_builder import ApplicationsWithUniqueNameRequestBuilder

        return ApplicationsWithUniqueNameRequestBuilder(self.request_adapter, self.path_parameters, unique_name)
    
    def devices_with_device_id(self,device_id: str) -> DevicesWithDeviceIdRequestBuilder:
        """
        Provides operations to manage the collection of device entities.
        param device_id: Alternate key of device
        Returns: DevicesWithDeviceIdRequestBuilder
        """
        if device_id is None:
            raise TypeError("device_id cannot be null.")
        from .devices_with_device_id.devices_with_device_id_request_builder import DevicesWithDeviceIdRequestBuilder

        return DevicesWithDeviceIdRequestBuilder(self.request_adapter, self.path_parameters, device_id)
    
    def directory_roles_with_role_template_id(self,role_template_id: str) -> DirectoryRolesWithRoleTemplateIdRequestBuilder:
        """
        Provides operations to manage the collection of directoryRole entities.
        param role_template_id: Alternate key of directoryRole
        Returns: DirectoryRolesWithRoleTemplateIdRequestBuilder
        """
        if role_template_id is None:
            raise TypeError("role_template_id cannot be null.")
        from .directory_roles_with_role_template_id.directory_roles_with_role_template_id_request_builder import DirectoryRolesWithRoleTemplateIdRequestBuilder

        return DirectoryRolesWithRoleTemplateIdRequestBuilder(self.request_adapter, self.path_parameters, role_template_id)
    
    def groups_with_unique_name(self,unique_name: str) -> GroupsWithUniqueNameRequestBuilder:
        """
        Provides operations to manage the collection of group entities.
        param unique_name: Alternate key of group
        Returns: GroupsWithUniqueNameRequestBuilder
        """
        if unique_name is None:
            raise TypeError("unique_name cannot be null.")
        from .groups_with_unique_name.groups_with_unique_name_request_builder import GroupsWithUniqueNameRequestBuilder

        return GroupsWithUniqueNameRequestBuilder(self.request_adapter, self.path_parameters, unique_name)
    
    def places_with_place_id(self,place_id: str) -> PlacesWithPlaceIdRequestBuilder:
        """
        Provides operations to manage the collection of place entities.
        param place_id: Alternate key of place
        Returns: PlacesWithPlaceIdRequestBuilder
        """
        if place_id is None:
            raise TypeError("place_id cannot be null.")
        from .places_with_place_id.places_with_place_id_request_builder import PlacesWithPlaceIdRequestBuilder

        return PlacesWithPlaceIdRequestBuilder(self.request_adapter, self.path_parameters, place_id)
    
    def service_principals_with_app_id(self,app_id: str) -> ServicePrincipalsWithAppIdRequestBuilder:
        """
        Provides operations to manage the collection of servicePrincipal entities.
        param app_id: Alternate key of servicePrincipal
        Returns: ServicePrincipalsWithAppIdRequestBuilder
        """
        if app_id is None:
            raise TypeError("app_id cannot be null.")
        from .service_principals_with_app_id.service_principals_with_app_id_request_builder import ServicePrincipalsWithAppIdRequestBuilder

        return ServicePrincipalsWithAppIdRequestBuilder(self.request_adapter, self.path_parameters, app_id)
    
    @property
    def access_review_decisions(self) -> AccessReviewDecisionsRequestBuilder:
        """
        Provides operations to manage the collection of accessReviewDecision entities.
        """
        from .access_review_decisions.access_review_decisions_request_builder import AccessReviewDecisionsRequestBuilder

        return AccessReviewDecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_reviews(self) -> AccessReviewsRequestBuilder:
        """
        Provides operations to manage the collection of accessReview entities.
        """
        from .access_reviews.access_reviews_request_builder import AccessReviewsRequestBuilder

        return AccessReviewsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def activitystatistics(self) -> ActivitystatisticsRequestBuilder:
        """
        Provides operations to manage the collection of activityStatistics entities.
        """
        from .activitystatistics.activitystatistics_request_builder import ActivitystatisticsRequestBuilder

        return ActivitystatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def admin(self) -> AdminRequestBuilder:
        """
        Provides operations to manage the admin singleton.
        """
        from .admin.admin_request_builder import AdminRequestBuilder

        return AdminRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def administrative_units(self) -> AdministrativeUnitsRequestBuilder:
        """
        Provides operations to manage the collection of administrativeUnit entities.
        """
        from .administrative_units.administrative_units_request_builder import AdministrativeUnitsRequestBuilder

        return AdministrativeUnitsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agreement_acceptances(self) -> AgreementAcceptancesRequestBuilder:
        """
        Provides operations to manage the collection of agreementAcceptance entities.
        """
        from .agreement_acceptances.agreement_acceptances_request_builder import AgreementAcceptancesRequestBuilder

        return AgreementAcceptancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agreements(self) -> AgreementsRequestBuilder:
        """
        Provides operations to manage the collection of agreement entities.
        """
        from .agreements.agreements_request_builder import AgreementsRequestBuilder

        return AgreementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def allowed_data_locations(self) -> AllowedDataLocationsRequestBuilder:
        """
        Provides operations to manage the collection of allowedDataLocation entities.
        """
        from .allowed_data_locations.allowed_data_locations_request_builder import AllowedDataLocationsRequestBuilder

        return AllowedDataLocationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app(self) -> AppRequestBuilder:
        """
        Provides operations to manage the commsApplication singleton.
        """
        from .app.app_request_builder import AppRequestBuilder

        return AppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_catalogs(self) -> AppCatalogsRequestBuilder:
        """
        Provides operations to manage the appCatalogs singleton.
        """
        from .app_catalogs.app_catalogs_request_builder import AppCatalogsRequestBuilder

        return AppCatalogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_role_assignments(self) -> AppRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the collection of appRoleAssignment entities.
        """
        from .app_role_assignments.app_role_assignments_request_builder import AppRoleAssignmentsRequestBuilder

        return AppRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def application_templates(self) -> ApplicationTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of applicationTemplate entities.
        """
        from .application_templates.application_templates_request_builder import ApplicationTemplatesRequestBuilder

        return ApplicationTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def applications(self) -> ApplicationsRequestBuilder:
        """
        Provides operations to manage the collection of application entities.
        """
        from .applications.applications_request_builder import ApplicationsRequestBuilder

        return ApplicationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def approval_workflow_providers(self) -> ApprovalWorkflowProvidersRequestBuilder:
        """
        Provides operations to manage the collection of approvalWorkflowProvider entities.
        """
        from .approval_workflow_providers.approval_workflow_providers_request_builder import ApprovalWorkflowProvidersRequestBuilder

        return ApprovalWorkflowProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def audit_logs(self) -> AuditLogsRequestBuilder:
        """
        Provides operations to manage the auditLogRoot singleton.
        """
        from .audit_logs.audit_logs_request_builder import AuditLogsRequestBuilder

        return AuditLogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_method_configurations(self) -> AuthenticationMethodConfigurationsRequestBuilder:
        """
        Provides operations to manage the collection of authenticationMethodConfiguration entities.
        """
        from .authentication_method_configurations.authentication_method_configurations_request_builder import AuthenticationMethodConfigurationsRequestBuilder

        return AuthenticationMethodConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_methods_policy(self) -> AuthenticationMethodsPolicyRequestBuilder:
        """
        Provides operations to manage the authenticationMethodsPolicy singleton.
        """
        from .authentication_methods_policy.authentication_methods_policy_request_builder import AuthenticationMethodsPolicyRequestBuilder

        return AuthenticationMethodsPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def booking_businesses(self) -> BookingBusinessesRequestBuilder:
        """
        Provides operations to manage the collection of bookingBusiness entities.
        """
        from .booking_businesses.booking_businesses_request_builder import BookingBusinessesRequestBuilder

        return BookingBusinessesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def booking_currencies(self) -> BookingCurrenciesRequestBuilder:
        """
        Provides operations to manage the collection of bookingCurrency entities.
        """
        from .booking_currencies.booking_currencies_request_builder import BookingCurrenciesRequestBuilder

        return BookingCurrenciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def business_flow_templates(self) -> BusinessFlowTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of businessFlowTemplate entities.
        """
        from .business_flow_templates.business_flow_templates_request_builder import BusinessFlowTemplatesRequestBuilder

        return BusinessFlowTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def certificate_based_auth_configuration(self) -> CertificateBasedAuthConfigurationRequestBuilder:
        """
        Provides operations to manage the collection of certificateBasedAuthConfiguration entities.
        """
        from .certificate_based_auth_configuration.certificate_based_auth_configuration_request_builder import CertificateBasedAuthConfigurationRequestBuilder

        return CertificateBasedAuthConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chats(self) -> ChatsRequestBuilder:
        """
        Provides operations to manage the collection of chat entities.
        """
        from .chats.chats_request_builder import ChatsRequestBuilder

        return ChatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def commands(self) -> CommandsRequestBuilder:
        """
        Provides operations to manage the collection of command entities.
        """
        from .commands.commands_request_builder import CommandsRequestBuilder

        return CommandsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def communications(self) -> CommunicationsRequestBuilder:
        """
        Provides operations to manage the cloudCommunications singleton.
        """
        from .communications.communications_request_builder import CommunicationsRequestBuilder

        return CommunicationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance(self) -> ComplianceRequestBuilder:
        """
        Provides operations to manage the compliance singleton.
        """
        from .compliance.compliance_request_builder import ComplianceRequestBuilder

        return ComplianceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def connections(self) -> ConnectionsRequestBuilder:
        """
        Provides operations to manage the collection of externalConnection entities.
        """
        from .connections.connections_request_builder import ConnectionsRequestBuilder

        return ConnectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contacts(self) -> ContactsRequestBuilder:
        """
        Provides operations to manage the collection of orgContact entities.
        """
        from .contacts.contacts_request_builder import ContactsRequestBuilder

        return ContactsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contracts(self) -> ContractsRequestBuilder:
        """
        Provides operations to manage the collection of contract entities.
        """
        from .contracts.contracts_request_builder import ContractsRequestBuilder

        return ContractsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_classification(self) -> DataClassificationRequestBuilder:
        """
        Provides operations to manage the dataClassificationService singleton.
        """
        from .data_classification.data_classification_request_builder import DataClassificationRequestBuilder

        return DataClassificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_policy_operations(self) -> DataPolicyOperationsRequestBuilder:
        """
        Provides operations to manage the collection of dataPolicyOperation entities.
        """
        from .data_policy_operations.data_policy_operations_request_builder import DataPolicyOperationsRequestBuilder

        return DataPolicyOperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_app_management(self) -> DeviceAppManagementRequestBuilder:
        """
        Provides operations to manage the deviceAppManagement singleton.
        """
        from .device_app_management.device_app_management_request_builder import DeviceAppManagementRequestBuilder

        return DeviceAppManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_local_credentials(self) -> DeviceLocalCredentialsRequestBuilder:
        """
        Provides operations to manage the collection of deviceLocalCredentialInfo entities.
        """
        from .device_local_credentials.device_local_credentials_request_builder import DeviceLocalCredentialsRequestBuilder

        return DeviceLocalCredentialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management(self) -> DeviceManagementRequestBuilder:
        """
        Provides operations to manage the deviceManagement singleton.
        """
        from .device_management.device_management_request_builder import DeviceManagementRequestBuilder

        return DeviceManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def devices(self) -> DevicesRequestBuilder:
        """
        Provides operations to manage the collection of device entities.
        """
        from .devices.devices_request_builder import DevicesRequestBuilder

        return DevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory(self) -> DirectoryRequestBuilder:
        """
        Provides operations to manage the directory singleton.
        """
        from .directory.directory_request_builder import DirectoryRequestBuilder

        return DirectoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_objects(self) -> DirectoryObjectsRequestBuilder:
        """
        Provides operations to manage the collection of directoryObject entities.
        """
        from .directory_objects.directory_objects_request_builder import DirectoryObjectsRequestBuilder

        return DirectoryObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_role_templates(self) -> DirectoryRoleTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of directoryRoleTemplate entities.
        """
        from .directory_role_templates.directory_role_templates_request_builder import DirectoryRoleTemplatesRequestBuilder

        return DirectoryRoleTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_roles(self) -> DirectoryRolesRequestBuilder:
        """
        Provides operations to manage the collection of directoryRole entities.
        """
        from .directory_roles.directory_roles_request_builder import DirectoryRolesRequestBuilder

        return DirectoryRolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_setting_templates(self) -> DirectorySettingTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of directorySettingTemplate entities.
        """
        from .directory_setting_templates.directory_setting_templates_request_builder import DirectorySettingTemplatesRequestBuilder

        return DirectorySettingTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def domain_dns_records(self) -> DomainDnsRecordsRequestBuilder:
        """
        Provides operations to manage the collection of domainDnsRecord entities.
        """
        from .domain_dns_records.domain_dns_records_request_builder import DomainDnsRecordsRequestBuilder

        return DomainDnsRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def domains(self) -> DomainsRequestBuilder:
        """
        Provides operations to manage the collection of domain entities.
        """
        from .domains.domains_request_builder import DomainsRequestBuilder

        return DomainsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drives(self) -> DrivesRequestBuilder:
        """
        Provides operations to manage the collection of drive entities.
        """
        from .drives.drives_request_builder import DrivesRequestBuilder

        return DrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def education(self) -> EducationRequestBuilder:
        """
        Provides operations to manage the educationRoot singleton.
        """
        from .education.education_request_builder import EducationRequestBuilder

        return EducationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employee_experience(self) -> EmployeeExperienceRequestBuilder:
        """
        Provides operations to manage the employeeExperience singleton.
        """
        from .employee_experience.employee_experience_request_builder import EmployeeExperienceRequestBuilder

        return EmployeeExperienceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external(self) -> ExternalRequestBuilder:
        """
        Provides operations to manage the external singleton.
        """
        from .external.external_request_builder import ExternalRequestBuilder

        return ExternalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def filter_operators(self) -> FilterOperatorsRequestBuilder:
        """
        Provides operations to manage the collection of filterOperatorSchema entities.
        """
        from .filter_operators.filter_operators_request_builder import FilterOperatorsRequestBuilder

        return FilterOperatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def filtering_policies(self) -> FilteringPoliciesRequestBuilder:
        """
        Provides operations to manage the collection of filteringPolicy entities.
        """
        from .filtering_policies.filtering_policies_request_builder import FilteringPoliciesRequestBuilder

        return FilteringPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def financials(self) -> FinancialsRequestBuilder:
        """
        Provides operations to manage the financials singleton.
        """
        from .financials.financials_request_builder import FinancialsRequestBuilder

        return FinancialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def functions(self) -> FunctionsRequestBuilder:
        """
        Provides operations to manage the collection of attributeMappingFunctionSchema entities.
        """
        from .functions.functions_request_builder import FunctionsRequestBuilder

        return FunctionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def governance_resources(self) -> GovernanceResourcesRequestBuilder:
        """
        Provides operations to manage the collection of governanceResource entities.
        """
        from .governance_resources.governance_resources_request_builder import GovernanceResourcesRequestBuilder

        return GovernanceResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def governance_role_assignment_requests(self) -> GovernanceRoleAssignmentRequestsRequestBuilder:
        """
        Provides operations to manage the collection of governanceRoleAssignmentRequest entities.
        """
        from .governance_role_assignment_requests.governance_role_assignment_requests_request_builder import GovernanceRoleAssignmentRequestsRequestBuilder

        return GovernanceRoleAssignmentRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def governance_role_assignments(self) -> GovernanceRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the collection of governanceRoleAssignment entities.
        """
        from .governance_role_assignments.governance_role_assignments_request_builder import GovernanceRoleAssignmentsRequestBuilder

        return GovernanceRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def governance_role_definitions(self) -> GovernanceRoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the collection of governanceRoleDefinition entities.
        """
        from .governance_role_definitions.governance_role_definitions_request_builder import GovernanceRoleDefinitionsRequestBuilder

        return GovernanceRoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def governance_role_settings(self) -> GovernanceRoleSettingsRequestBuilder:
        """
        Provides operations to manage the collection of governanceRoleSetting entities.
        """
        from .governance_role_settings.governance_role_settings_request_builder import GovernanceRoleSettingsRequestBuilder

        return GovernanceRoleSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def governance_subjects(self) -> GovernanceSubjectsRequestBuilder:
        """
        Provides operations to manage the collection of governanceSubject entities.
        """
        from .governance_subjects.governance_subjects_request_builder import GovernanceSubjectsRequestBuilder

        return GovernanceSubjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_lifecycle_policies(self) -> GroupLifecyclePoliciesRequestBuilder:
        """
        Provides operations to manage the collection of groupLifecyclePolicy entities.
        """
        from .group_lifecycle_policies.group_lifecycle_policies_request_builder import GroupLifecyclePoliciesRequestBuilder

        return GroupLifecyclePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def groups(self) -> GroupsRequestBuilder:
        """
        Provides operations to manage the collection of group entities.
        """
        from .groups.groups_request_builder import GroupsRequestBuilder

        return GroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity(self) -> IdentityRequestBuilder:
        """
        Provides operations to manage the identityContainer singleton.
        """
        from .identity.identity_request_builder import IdentityRequestBuilder

        return IdentityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_governance(self) -> IdentityGovernanceRequestBuilder:
        """
        Provides operations to manage the identityGovernance singleton.
        """
        from .identity_governance.identity_governance_request_builder import IdentityGovernanceRequestBuilder

        return IdentityGovernanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_protection(self) -> IdentityProtectionRequestBuilder:
        """
        Provides operations to manage the identityProtectionRoot singleton.
        """
        from .identity_protection.identity_protection_request_builder import IdentityProtectionRequestBuilder

        return IdentityProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_providers(self) -> IdentityProvidersRequestBuilder:
        """
        Provides operations to manage the collection of identityProvider entities.
        """
        from .identity_providers.identity_providers_request_builder import IdentityProvidersRequestBuilder

        return IdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def information_protection(self) -> InformationProtectionRequestBuilder:
        """
        Provides operations to manage the informationProtection singleton.
        """
        from .information_protection.information_protection_request_builder import InformationProtectionRequestBuilder

        return InformationProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invitations(self) -> InvitationsRequestBuilder:
        """
        Provides operations to manage the collection of invitation entities.
        """
        from .invitations.invitations_request_builder import InvitationsRequestBuilder

        return InvitationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def message_events(self) -> MessageEventsRequestBuilder:
        """
        Provides operations to manage the collection of messageEvent entities.
        """
        from .message_events.message_events_request_builder import MessageEventsRequestBuilder

        return MessageEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def message_recipients(self) -> MessageRecipientsRequestBuilder:
        """
        Provides operations to manage the collection of messageRecipient entities.
        """
        from .message_recipients.message_recipients_request_builder import MessageRecipientsRequestBuilder

        return MessageRecipientsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def message_traces(self) -> MessageTracesRequestBuilder:
        """
        Provides operations to manage the collection of messageTrace entities.
        """
        from .message_traces.message_traces_request_builder import MessageTracesRequestBuilder

        return MessageTracesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobility_management_policies(self) -> MobilityManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the collection of mobilityManagementPolicy entities.
        """
        from .mobility_management_policies.mobility_management_policies_request_builder import MobilityManagementPoliciesRequestBuilder

        return MobilityManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monitoring(self) -> MonitoringRequestBuilder:
        """
        Provides operations to manage the monitoring singleton.
        """
        from .monitoring.monitoring_request_builder import MonitoringRequestBuilder

        return MonitoringRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def network(self) -> NetworkRequestBuilder:
        """
        Provides operations to manage the network singleton.
        """
        from .network.network_request_builder import NetworkRequestBuilder

        return NetworkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def network_access(self) -> NetworkAccessRequestBuilder:
        """
        Provides operations to manage the networkAccessRoot singleton.
        """
        from .network_access.network_access_request_builder import NetworkAccessRequestBuilder

        return NetworkAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oauth2_permission_grants(self) -> Oauth2PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the collection of oAuth2PermissionGrant entities.
        """
        from .oauth2_permission_grants.oauth2_permission_grants_request_builder import Oauth2PermissionGrantsRequestBuilder

        return Oauth2PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def on_premises_publishing_profiles(self) -> OnPremisesPublishingProfilesRequestBuilder:
        """
        Provides operations to manage the collection of onPremisesPublishingProfile entities.
        """
        from .on_premises_publishing_profiles.on_premises_publishing_profiles_request_builder import OnPremisesPublishingProfilesRequestBuilder

        return OnPremisesPublishingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def organization(self) -> OrganizationRequestBuilder:
        """
        Provides operations to manage the collection of organization entities.
        """
        from .organization.organization_request_builder import OrganizationRequestBuilder

        return OrganizationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payload_response(self) -> PayloadResponseRequestBuilder:
        """
        Provides operations to manage the collection of payloadResponse entities.
        """
        from .payload_response.payload_response_request_builder import PayloadResponseRequestBuilder

        return PayloadResponseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grants(self) -> PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the collection of resourceSpecificPermissionGrant entities.
        """
        from .permission_grants.permission_grants_request_builder import PermissionGrantsRequestBuilder

        return PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def places(self) -> PlacesRequestBuilder:
        """
        The places property
        """
        from .places.places_request_builder import PlacesRequestBuilder

        return PlacesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def planner(self) -> PlannerRequestBuilder:
        """
        Provides operations to manage the planner singleton.
        """
        from .planner.planner_request_builder import PlannerRequestBuilder

        return PlannerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policies(self) -> PoliciesRequestBuilder:
        """
        Provides operations to manage the policyRoot singleton.
        """
        from .policies.policies_request_builder import PoliciesRequestBuilder

        return PoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def print(self) -> PrintRequestBuilder:
        """
        Provides operations to manage the print singleton.
        """
        from .print.print_request_builder import PrintRequestBuilder

        return PrintRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privacy(self) -> PrivacyRequestBuilder:
        """
        Provides operations to manage the privacy singleton.
        """
        from .privacy.privacy_request_builder import PrivacyRequestBuilder

        return PrivacyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_access(self) -> PrivilegedAccessRequestBuilder:
        """
        Provides operations to manage the collection of privilegedAccess entities.
        """
        from .privileged_access.privileged_access_request_builder import PrivilegedAccessRequestBuilder

        return PrivilegedAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_approval(self) -> PrivilegedApprovalRequestBuilder:
        """
        Provides operations to manage the collection of privilegedApproval entities.
        """
        from .privileged_approval.privileged_approval_request_builder import PrivilegedApprovalRequestBuilder

        return PrivilegedApprovalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_operation_events(self) -> PrivilegedOperationEventsRequestBuilder:
        """
        Provides operations to manage the collection of privilegedOperationEvent entities.
        """
        from .privileged_operation_events.privileged_operation_events_request_builder import PrivilegedOperationEventsRequestBuilder

        return PrivilegedOperationEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_role_assignment_requests(self) -> PrivilegedRoleAssignmentRequestsRequestBuilder:
        """
        Provides operations to manage the collection of privilegedRoleAssignmentRequest entities.
        """
        from .privileged_role_assignment_requests.privileged_role_assignment_requests_request_builder import PrivilegedRoleAssignmentRequestsRequestBuilder

        return PrivilegedRoleAssignmentRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_role_assignments(self) -> PrivilegedRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the collection of privilegedRoleAssignment entities.
        """
        from .privileged_role_assignments.privileged_role_assignments_request_builder import PrivilegedRoleAssignmentsRequestBuilder

        return PrivilegedRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_roles(self) -> PrivilegedRolesRequestBuilder:
        """
        Provides operations to manage the collection of privilegedRole entities.
        """
        from .privileged_roles.privileged_roles_request_builder import PrivilegedRolesRequestBuilder

        return PrivilegedRolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_signup_status(self) -> PrivilegedSignupStatusRequestBuilder:
        """
        Provides operations to manage the collection of privilegedSignupStatus entities.
        """
        from .privileged_signup_status.privileged_signup_status_request_builder import PrivilegedSignupStatusRequestBuilder

        return PrivilegedSignupStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def program_control_types(self) -> ProgramControlTypesRequestBuilder:
        """
        Provides operations to manage the collection of programControlType entities.
        """
        from .program_control_types.program_control_types_request_builder import ProgramControlTypesRequestBuilder

        return ProgramControlTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def program_controls(self) -> ProgramControlsRequestBuilder:
        """
        Provides operations to manage the collection of programControl entities.
        """
        from .program_controls.program_controls_request_builder import ProgramControlsRequestBuilder

        return ProgramControlsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def programs(self) -> ProgramsRequestBuilder:
        """
        Provides operations to manage the collection of program entities.
        """
        from .programs.programs_request_builder import ProgramsRequestBuilder

        return ProgramsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reports(self) -> ReportsRequestBuilder:
        """
        Provides operations to manage the reportRoot singleton.
        """
        from .reports.reports_request_builder import ReportsRequestBuilder

        return ReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def risk_detections(self) -> RiskDetectionsRequestBuilder:
        """
        Provides operations to manage the collection of riskDetection entities.
        """
        from .risk_detections.risk_detections_request_builder import RiskDetectionsRequestBuilder

        return RiskDetectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def risky_users(self) -> RiskyUsersRequestBuilder:
        """
        Provides operations to manage the collection of riskyUser entities.
        """
        from .risky_users.risky_users_request_builder import RiskyUsersRequestBuilder

        return RiskyUsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_management(self) -> RoleManagementRequestBuilder:
        """
        Provides operations to manage the roleManagement singleton.
        """
        from .role_management.role_management_request_builder import RoleManagementRequestBuilder

        return RoleManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schema_extensions(self) -> SchemaExtensionsRequestBuilder:
        """
        Provides operations to manage the collection of schemaExtension entities.
        """
        from .schema_extensions.schema_extensions_request_builder import SchemaExtensionsRequestBuilder

        return SchemaExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def scoped_role_memberships(self) -> ScopedRoleMembershipsRequestBuilder:
        """
        Provides operations to manage the collection of scopedRoleMembership entities.
        """
        from .scoped_role_memberships.scoped_role_memberships_request_builder import ScopedRoleMembershipsRequestBuilder

        return ScopedRoleMembershipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> SearchRequestBuilder:
        """
        Provides operations to manage the searchEntity singleton.
        """
        from .search.search_request_builder import SearchRequestBuilder

        return SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security(self) -> SecurityRequestBuilder:
        """
        Provides operations to manage the security singleton.
        """
        from .security.security_request_builder import SecurityRequestBuilder

        return SecurityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_principals(self) -> ServicePrincipalsRequestBuilder:
        """
        Provides operations to manage the collection of servicePrincipal entities.
        """
        from .service_principals.service_principals_request_builder import ServicePrincipalsRequestBuilder

        return ServicePrincipalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        Provides operations to manage the collection of directorySetting entities.
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shares(self) -> SharesRequestBuilder:
        """
        Provides operations to manage the collection of sharedDriveItem entities.
        """
        from .shares.shares_request_builder import SharesRequestBuilder

        return SharesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sites(self) -> SitesRequestBuilder:
        """
        Provides operations to manage the collection of site entities.
        """
        from .sites.sites_request_builder import SitesRequestBuilder

        return SitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def solutions(self) -> SolutionsRequestBuilder:
        """
        Provides operations to manage the solutionsRoot singleton.
        """
        from .solutions.solutions_request_builder import SolutionsRequestBuilder

        return SolutionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def storage(self) -> StorageRequestBuilder:
        """
        Provides operations to manage the storage singleton.
        """
        from .storage.storage_request_builder import StorageRequestBuilder

        return StorageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscribed_skus(self) -> SubscribedSkusRequestBuilder:
        """
        Provides operations to manage the collection of subscribedSku entities.
        """
        from .subscribed_skus.subscribed_skus_request_builder import SubscribedSkusRequestBuilder

        return SubscribedSkusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscriptions(self) -> SubscriptionsRequestBuilder:
        """
        Provides operations to manage the collection of subscription entities.
        """
        from .subscriptions.subscriptions_request_builder import SubscriptionsRequestBuilder

        return SubscriptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def team_template_definition(self) -> TeamTemplateDefinitionRequestBuilder:
        """
        Provides operations to manage the collection of teamTemplateDefinition entities.
        """
        from .team_template_definition.team_template_definition_request_builder import TeamTemplateDefinitionRequestBuilder

        return TeamTemplateDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teams(self) -> TeamsRequestBuilder:
        """
        Provides operations to manage the collection of team entities.
        """
        from .teams.teams_request_builder import TeamsRequestBuilder

        return TeamsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teams_templates(self) -> TeamsTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of teamsTemplate entities.
        """
        from .teams_templates.teams_templates_request_builder import TeamsTemplatesRequestBuilder

        return TeamsTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teamwork(self) -> TeamworkRequestBuilder:
        """
        Provides operations to manage the teamwork singleton.
        """
        from .teamwork.teamwork_request_builder import TeamworkRequestBuilder

        return TeamworkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenant_relationships(self) -> TenantRelationshipsRequestBuilder:
        """
        Provides operations to manage the tenantRelationship singleton.
        """
        from .tenant_relationships.tenant_relationships_request_builder import TenantRelationshipsRequestBuilder

        return TenantRelationshipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def term_store(self) -> TermStoreRequestBuilder:
        """
        Provides operations to manage the store singleton.
        """
        from .term_store.term_store_request_builder import TermStoreRequestBuilder

        return TermStoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def threat_submission(self) -> ThreatSubmissionRequestBuilder:
        """
        Provides operations to manage the threatSubmissionRoot singleton.
        """
        from .threat_submission.threat_submission_request_builder import ThreatSubmissionRequestBuilder

        return ThreatSubmissionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trust_framework(self) -> TrustFrameworkRequestBuilder:
        """
        Provides operations to manage the trustFramework singleton.
        """
        from .trust_framework.trust_framework_request_builder import TrustFrameworkRequestBuilder

        return TrustFrameworkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> UsersRequestBuilder:
        """
        Provides operations to manage the collection of user entities.
        """
        from .users.users_request_builder import UsersRequestBuilder

        return UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def workplace(self) -> WorkplaceRequestBuilder:
        """
        Provides operations to manage the workplace singleton.
        """
        from .workplace.workplace_request_builder import WorkplaceRequestBuilder

        return WorkplaceRequestBuilder(self.request_adapter, self.path_parameters)
    

