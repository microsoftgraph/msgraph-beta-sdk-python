from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aad_user_conversation_member import AadUserConversationMember
    from .access_package import AccessPackage
    from .access_package_assignment import AccessPackageAssignment
    from .access_package_assignment_policy import AccessPackageAssignmentPolicy
    from .access_package_assignment_request import AccessPackageAssignmentRequest
    from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
    from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
    from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
    from .access_package_catalog import AccessPackageCatalog
    from .access_package_resource import AccessPackageResource
    from .access_package_resource_environment import AccessPackageResourceEnvironment
    from .access_package_resource_request import AccessPackageResourceRequest
    from .access_package_resource_role import AccessPackageResourceRole
    from .access_package_resource_role_scope import AccessPackageResourceRoleScope
    from .access_package_resource_scope import AccessPackageResourceScope
    from .access_package_subject import AccessPackageSubject
    from .access_review import AccessReview
    from .access_review_decision import AccessReviewDecision
    from .access_review_history_definition import AccessReviewHistoryDefinition
    from .access_review_history_instance import AccessReviewHistoryInstance
    from .access_review_instance import AccessReviewInstance
    from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
    from .access_review_policy import AccessReviewPolicy
    from .access_review_reviewer import AccessReviewReviewer
    from .access_review_schedule_definition import AccessReviewScheduleDefinition
    from .access_review_set import AccessReviewSet
    from .access_review_stage import AccessReviewStage
    from .active_directory_windows_autopilot_deployment_profile import ActiveDirectoryWindowsAutopilotDeploymentProfile
    from .active_users_breakdown_metric import ActiveUsersBreakdownMetric
    from .active_users_metric import ActiveUsersMetric
    from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
    from .activity_history_item import ActivityHistoryItem
    from .activity_statistics import ActivityStatistics
    from .add_large_gallery_view_operation import AddLargeGalleryViewOperation
    from .administrative_unit import AdministrativeUnit
    from .admin_apps_and_services import AdminAppsAndServices
    from .admin_consent_request_policy import AdminConsentRequestPolicy
    from .admin_dynamics import AdminDynamics
    from .admin_forms import AdminForms
    from .admin_microsoft365_apps import AdminMicrosoft365Apps
    from .admin_report_settings import AdminReportSettings
    from .admin_todo import AdminTodo
    from .admin_windows import AdminWindows
    from .admin_windows_updates import AdminWindowsUpdates
    from .advanced_threat_protection_onboarding_device_setting_state import AdvancedThreatProtectionOnboardingDeviceSettingState
    from .advanced_threat_protection_onboarding_state_summary import AdvancedThreatProtectionOnboardingStateSummary
    from .agreement import Agreement
    from .agreement_acceptance import AgreementAcceptance
    from .agreement_file import AgreementFile
    from .agreement_file_localization import AgreementFileLocalization
    from .agreement_file_properties import AgreementFileProperties
    from .agreement_file_version import AgreementFileVersion
    from .alert import Alert
    from .allowed_data_location import AllowedDataLocation
    from .allowed_value import AllowedValue
    from .android_certificate_profile_base import AndroidCertificateProfileBase
    from .android_compliance_policy import AndroidCompliancePolicy
    from .android_custom_configuration import AndroidCustomConfiguration
    from .android_device_compliance_local_action_base import AndroidDeviceComplianceLocalActionBase
    from .android_device_compliance_local_action_lock_device import AndroidDeviceComplianceLocalActionLockDevice
    from .android_device_compliance_local_action_lock_device_with_passcode import AndroidDeviceComplianceLocalActionLockDeviceWithPasscode
    from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
    from .android_device_owner_compliance_policy import AndroidDeviceOwnerCompliancePolicy
    from .android_device_owner_derived_credential_authentication_configuration import AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration
    from .android_device_owner_enrollment_profile import AndroidDeviceOwnerEnrollmentProfile
    from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration
    from .android_device_owner_general_device_configuration import AndroidDeviceOwnerGeneralDeviceConfiguration
    from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile
    from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile
    from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile
    from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate
    from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration
    from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration
    from .android_eas_email_profile_configuration import AndroidEasEmailProfileConfiguration
    from .android_enterprise_wi_fi_configuration import AndroidEnterpriseWiFiConfiguration
    from .android_for_work_app import AndroidForWorkApp
    from .android_for_work_app_configuration_schema import AndroidForWorkAppConfigurationSchema
    from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
    from .android_for_work_compliance_policy import AndroidForWorkCompliancePolicy
    from .android_for_work_custom_configuration import AndroidForWorkCustomConfiguration
    from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase
    from .android_for_work_enrollment_profile import AndroidForWorkEnrollmentProfile
    from .android_for_work_enterprise_wi_fi_configuration import AndroidForWorkEnterpriseWiFiConfiguration
    from .android_for_work_general_device_configuration import AndroidForWorkGeneralDeviceConfiguration
    from .android_for_work_gmail_eas_configuration import AndroidForWorkGmailEasConfiguration
    from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile
    from .android_for_work_mobile_app_configuration import AndroidForWorkMobileAppConfiguration
    from .android_for_work_nine_work_eas_configuration import AndroidForWorkNineWorkEasConfiguration
    from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
    from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile
    from .android_for_work_settings import AndroidForWorkSettings
    from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
    from .android_for_work_vpn_configuration import AndroidForWorkVpnConfiguration
    from .android_for_work_wi_fi_configuration import AndroidForWorkWiFiConfiguration
    from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
    from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile
    from .android_lob_app import AndroidLobApp
    from .android_managed_app_protection import AndroidManagedAppProtection
    from .android_managed_app_registration import AndroidManagedAppRegistration
    from .android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings
    from .android_managed_store_app import AndroidManagedStoreApp
    from .android_managed_store_app_configuration import AndroidManagedStoreAppConfiguration
    from .android_managed_store_app_configuration_schema import AndroidManagedStoreAppConfigurationSchema
    from .android_managed_store_web_app import AndroidManagedStoreWebApp
    from .android_oma_cp_configuration import AndroidOmaCpConfiguration
    from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile
    from .android_scep_certificate_profile import AndroidScepCertificateProfile
    from .android_store_app import AndroidStoreApp
    from .android_trusted_root_certificate import AndroidTrustedRootCertificate
    from .android_vpn_configuration import AndroidVpnConfiguration
    from .android_wi_fi_configuration import AndroidWiFiConfiguration
    from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
    from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
    from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
    from .android_work_profile_eas_email_profile_base import AndroidWorkProfileEasEmailProfileBase
    from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration
    from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
    from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
    from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
    from .android_work_profile_pkcs_certificate_profile import AndroidWorkProfilePkcsCertificateProfile
    from .android_work_profile_scep_certificate_profile import AndroidWorkProfileScepCertificateProfile
    from .android_work_profile_trusted_root_certificate import AndroidWorkProfileTrustedRootCertificate
    from .android_work_profile_vpn_configuration import AndroidWorkProfileVpnConfiguration
    from .android_work_profile_wi_fi_configuration import AndroidWorkProfileWiFiConfiguration
    from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
    from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase
    from .aosp_device_owner_compliance_policy import AospDeviceOwnerCompliancePolicy
    from .aosp_device_owner_device_configuration import AospDeviceOwnerDeviceConfiguration
    from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration
    from .aosp_device_owner_pkcs_certificate_profile import AospDeviceOwnerPkcsCertificateProfile
    from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile
    from .aosp_device_owner_trusted_root_certificate import AospDeviceOwnerTrustedRootCertificate
    from .aosp_device_owner_wi_fi_configuration import AospDeviceOwnerWiFiConfiguration
    from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
    from .apple_enrollment_profile_assignment import AppleEnrollmentProfileAssignment
    from .apple_expedited_checkin_configuration_base import AppleExpeditedCheckinConfigurationBase
    from .apple_managed_identity_provider import AppleManagedIdentityProvider
    from .apple_push_notification_certificate import ApplePushNotificationCertificate
    from .apple_user_initiated_enrollment_profile import AppleUserInitiatedEnrollmentProfile
    from .apple_vpn_configuration import AppleVpnConfiguration
    from .apple_vpp_token_troubleshooting_event import AppleVppTokenTroubleshootingEvent
    from .application import Application
    from .application_segment import ApplicationSegment
    from .application_sign_in_detailed_summary import ApplicationSignInDetailedSummary
    from .application_sign_in_summary import ApplicationSignInSummary
    from .application_template import ApplicationTemplate
    from .approval import Approval
    from .approval_step import ApprovalStep
    from .approval_workflow_provider import ApprovalWorkflowProvider
    from .app_consent_approval_route import AppConsentApprovalRoute
    from .app_consent_request import AppConsentRequest
    from .app_credential_sign_in_activity import AppCredentialSignInActivity
    from .app_log_collection_request import AppLogCollectionRequest
    from .app_management_policy import AppManagementPolicy
    from .app_role_assignment import AppRoleAssignment
    from .app_scope import AppScope
    from .app_vulnerability_managed_device import AppVulnerabilityManagedDevice
    from .app_vulnerability_mobile_app import AppVulnerabilityMobileApp
    from .app_vulnerability_task import AppVulnerabilityTask
    from .assigned_compute_instance_details import AssignedComputeInstanceDetails
    from .assignment_filter_evaluation_status_details import AssignmentFilterEvaluationStatusDetails
    from .associated_team_info import AssociatedTeamInfo
    from .attachment import Attachment
    from .attachment_base import AttachmentBase
    from .attachment_session import AttachmentSession
    from .attack_simulation_operation import AttackSimulationOperation
    from .attack_simulation_root import AttackSimulationRoot
    from .attendance_record import AttendanceRecord
    from .attribute_mapping_function_schema import AttributeMappingFunctionSchema
    from .attribute_set import AttributeSet
    from .audio_routing_group import AudioRoutingGroup
    from .audit_event import AuditEvent
    from .authentication import Authentication
    from .authentications_metric import AuthenticationsMetric
    from .authentication_combination_configuration import AuthenticationCombinationConfiguration
    from .authentication_context_class_reference import AuthenticationContextClassReference
    from .authentication_events_flow import AuthenticationEventsFlow
    from .authentication_events_policy import AuthenticationEventsPolicy
    from .authentication_event_listener import AuthenticationEventListener
    from .authentication_flows_policy import AuthenticationFlowsPolicy
    from .authentication_listener import AuthenticationListener
    from .authentication_method import AuthenticationMethod
    from .authentication_methods_policy import AuthenticationMethodsPolicy
    from .authentication_methods_root import AuthenticationMethodsRoot
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .authentication_method_mode_detail import AuthenticationMethodModeDetail
    from .authentication_method_target import AuthenticationMethodTarget
    from .authentication_strength_policy import AuthenticationStrengthPolicy
    from .authentication_strength_root import AuthenticationStrengthRoot
    from .authored_note import AuthoredNote
    from .authorization_policy import AuthorizationPolicy
    from .authorization_system import AuthorizationSystem
    from .authorization_system_identity import AuthorizationSystemIdentity
    from .authorization_system_resource import AuthorizationSystemResource
    from .authorization_system_type_action import AuthorizationSystemTypeAction
    from .authorization_system_type_service import AuthorizationSystemTypeService
    from .aws_access_key import AwsAccessKey
    from .aws_authorization_system import AwsAuthorizationSystem
    from .aws_authorization_system_resource import AwsAuthorizationSystemResource
    from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction
    from .aws_ec2_instance import AwsEc2Instance
    from .aws_external_system_access_finding import AwsExternalSystemAccessFinding
    from .aws_external_system_access_role_finding import AwsExternalSystemAccessRoleFinding
    from .aws_group import AwsGroup
    from .aws_identity import AwsIdentity
    from .aws_identity_access_management_key_age_finding import AwsIdentityAccessManagementKeyAgeFinding
    from .aws_identity_access_management_key_usage_finding import AwsIdentityAccessManagementKeyUsageFinding
    from .aws_lambda import AwsLambda
    from .aws_policy import AwsPolicy
    from .aws_role import AwsRole
    from .aws_secret_information_access_finding import AwsSecretInformationAccessFinding
    from .aws_security_tool_administration_finding import AwsSecurityToolAdministrationFinding
    from .aws_user import AwsUser
    from .azure_authorization_system import AzureAuthorizationSystem
    from .azure_authorization_system_resource import AzureAuthorizationSystemResource
    from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction
    from .azure_a_d_authentication import AzureADAuthentication
    from .azure_a_d_windows_autopilot_deployment_profile import AzureADWindowsAutopilotDeploymentProfile
    from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
    from .azure_group import AzureGroup
    from .azure_identity import AzureIdentity
    from .azure_managed_identity import AzureManagedIdentity
    from .azure_role_definition import AzureRoleDefinition
    from .azure_serverless_function import AzureServerlessFunction
    from .azure_service_principal import AzureServicePrincipal
    from .azure_user import AzureUser
    from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicy
    from .b2c_identity_user_flow import B2cIdentityUserFlow
    from .b2x_identity_user_flow import B2xIdentityUserFlow
    from .base_item import BaseItem
    from .base_item_version import BaseItemVersion
    from .base_site_page import BaseSitePage
    from .bitlocker import Bitlocker
    from .bitlocker_recovery_key import BitlockerRecoveryKey
    from .booking_appointment import BookingAppointment
    from .booking_business import BookingBusiness
    from .booking_currency import BookingCurrency
    from .booking_customer import BookingCustomer
    from .booking_custom_question import BookingCustomQuestion
    from .booking_named_entity import BookingNamedEntity
    from .booking_person import BookingPerson
    from .booking_service import BookingService
    from .booking_staff_member import BookingStaffMember
    from .browser_shared_cookie import BrowserSharedCookie
    from .browser_site import BrowserSite
    from .browser_site_list import BrowserSiteList
    from .built_in_identity_provider import BuiltInIdentityProvider
    from .bulk_upload import BulkUpload
    from .business_flow import BusinessFlow
    from .business_flow_template import BusinessFlowTemplate
    from .business_scenario import BusinessScenario
    from .business_scenario_planner import BusinessScenarioPlanner
    from .business_scenario_plan_reference import BusinessScenarioPlanReference
    from .business_scenario_task import BusinessScenarioTask
    from .calendar import Calendar
    from .calendar_group import CalendarGroup
    from .calendar_permission import CalendarPermission
    from .calendar_sharing_message import CalendarSharingMessage
    from .call import Call
    from .call_activity_statistics import CallActivityStatistics
    from .call_event import CallEvent
    from .call_recording import CallRecording
    from .call_records.call_record import CallRecord
    from .call_records.organizer import Organizer
    from .call_records.participant import Participant
    from .call_records.participant_base import ParticipantBase
    from .call_records.segment import Segment
    from .call_records.session import Session
    from .call_transcript import CallTranscript
    from .cancel_media_processing_operation import CancelMediaProcessingOperation
    from .canvas_layout import CanvasLayout
    from .cart_to_class_association import CartToClassAssociation
    from .certificate_authority_as_entity import CertificateAuthorityAsEntity
    from .certificate_authority_path import CertificateAuthorityPath
    from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
    from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
    from .certificate_connector_details import CertificateConnectorDetails
    from .change_tracked_entity import ChangeTrackedEntity
    from .channel import Channel
    from .chat import Chat
    from .chat_activity_statistics import ChatActivityStatistics
    from .chat_message import ChatMessage
    from .chat_message_hosted_content import ChatMessageHostedContent
    from .chat_message_info import ChatMessageInfo
    from .checklist_item import ChecklistItem
    from .chrome_o_s_onboarding_settings import ChromeOSOnboardingSettings
    from .claims_mapping_policy import ClaimsMappingPolicy
    from .classification_job_response import ClassificationJobResponse
    from .cloud_app_security_profile import CloudAppSecurityProfile
    from .cloud_clipboard_item import CloudClipboardItem
    from .cloud_clipboard_root import CloudClipboardRoot
    from .cloud_pc_audit_event import CloudPcAuditEvent
    from .cloud_pc_bulk_action import CloudPcBulkAction
    from .cloud_pc_bulk_disaster_recovery_failback import CloudPcBulkDisasterRecoveryFailback
    from .cloud_pc_bulk_disaster_recovery_failover import CloudPcBulkDisasterRecoveryFailover
    from .cloud_pc_bulk_modify_disk_encryption_type import CloudPcBulkModifyDiskEncryptionType
    from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff
    from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn
    from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision
    from .cloud_pc_bulk_resize import CloudPcBulkResize
    from .cloud_pc_bulk_restart import CloudPcBulkRestart
    from .cloud_pc_bulk_restore import CloudPcBulkRestore
    from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot
    from .cloud_pc_cross_cloud_government_organization_mapping import CloudPcCrossCloudGovernmentOrganizationMapping
    from .cloud_pc_device_image import CloudPcDeviceImage
    from .cloud_pc_export_job import CloudPcExportJob
    from .cloud_pc_external_partner_setting import CloudPcExternalPartnerSetting
    from .cloud_pc_front_line_service_plan import CloudPcFrontLineServicePlan
    from .cloud_pc_gallery_image import CloudPcGalleryImage
    from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
    from .cloud_pc_organization_settings import CloudPcOrganizationSettings
    from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
    from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
    from .cloud_pc_reports import CloudPcReports
    from .cloud_pc_service_plan import CloudPcServicePlan
    from .cloud_pc_shared_use_service_plan import CloudPcSharedUseServicePlan
    from .cloud_pc_snapshot import CloudPcSnapshot
    from .cloud_pc_supported_region import CloudPcSupportedRegion
    from .cloud_pc_user_setting import CloudPcUserSetting
    from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment
    from .cloud_p_c import CloudPC
    from .cloud_p_c_connectivity_issue import CloudPCConnectivityIssue
    from .column_definition import ColumnDefinition
    from .column_link import ColumnLink
    from .comanagement_eligible_device import ComanagementEligibleDevice
    from .command import Command
    from .comms_operation import CommsOperation
    from .community import Community
    from .company_subscription import CompanySubscription
    from .compliance_management_partner import ComplianceManagementPartner
    from .conditional_access_policy import ConditionalAccessPolicy
    from .conditional_access_root import ConditionalAccessRoot
    from .conditional_access_template import ConditionalAccessTemplate
    from .conditional_access_what_if_policy import ConditionalAccessWhatIfPolicy
    from .config_manager_collection import ConfigManagerCollection
    from .connected_organization import ConnectedOrganization
    from .connection_operation import ConnectionOperation
    from .connector import Connector
    from .connector_group import ConnectorGroup
    from .contact import Contact
    from .contact_folder import ContactFolder
    from .contact_merge_suggestions import ContactMergeSuggestions
    from .content_sharing_session import ContentSharingSession
    from .content_type import ContentType
    from .continuous_access_evaluation_policy import ContinuousAccessEvaluationPolicy
    from .contract import Contract
    from .conversation import Conversation
    from .conversation_member import ConversationMember
    from .conversation_thread import ConversationThread
    from .cors_configuration_v2 import CorsConfiguration_v2
    from .country_named_location import CountryNamedLocation
    from .credential_usage_summary import CredentialUsageSummary
    from .credential_user_registration_count import CredentialUserRegistrationCount
    from .credential_user_registration_details import CredentialUserRegistrationDetails
    from .cross_tenant_access_policy import CrossTenantAccessPolicy
    from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault
    from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
    from .custom_app_scope import CustomAppScope
    from .custom_authentication_extension import CustomAuthenticationExtension
    from .custom_callout_extension import CustomCalloutExtension
    from .custom_extension_handler import CustomExtensionHandler
    from .custom_extension_stage_setting import CustomExtensionStageSetting
    from .custom_security_attribute_audit import CustomSecurityAttributeAudit
    from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
    from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
    from .daily_inactive_users_metric import DailyInactiveUsersMetric
    from .daily_user_insight_metrics_root import DailyUserInsightMetricsRoot
    from .data_classification_service import DataClassificationService
    from .data_collection_info import DataCollectionInfo
    from .data_loss_prevention_policy import DataLossPreventionPolicy
    from .data_policy_operation import DataPolicyOperation
    from .data_sharing_consent import DataSharingConsent
    from .day_note import DayNote
    from .default_device_compliance_policy import DefaultDeviceCompliancePolicy
    from .default_managed_app_protection import DefaultManagedAppProtection
    from .default_user_role_override import DefaultUserRoleOverride
    from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment
    from .delegated_admin_customer import DelegatedAdminCustomer
    from .delegated_admin_relationship import DelegatedAdminRelationship
    from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
    from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest
    from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail
    from .delegated_permission_classification import DelegatedPermissionClassification
    from .deleted_chat import DeletedChat
    from .deleted_item_container import DeletedItemContainer
    from .deleted_team import DeletedTeam
    from .delta_participants import DeltaParticipants
    from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
    from .dep_enrollment_profile import DepEnrollmentProfile
    from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
    from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
    from .dep_onboarding_setting import DepOnboardingSetting
    from .detected_app import DetectedApp
    from .device import Device
    from .device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter
    from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
    from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
    from .device_app_management import DeviceAppManagement
    from .device_app_management_task import DeviceAppManagementTask
    from .device_category import DeviceCategory
    from .device_comanagement_authority_configuration import DeviceComanagementAuthorityConfiguration
    from .device_compliance_action_item import DeviceComplianceActionItem
    from .device_compliance_device_overview import DeviceComplianceDeviceOverview
    from .device_compliance_device_status import DeviceComplianceDeviceStatus
    from .device_compliance_policy import DeviceCompliancePolicy
    from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
    from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
    from .device_compliance_policy_group_assignment import DeviceCompliancePolicyGroupAssignment
    from .device_compliance_policy_policy_set_item import DeviceCompliancePolicyPolicySetItem
    from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
    from .device_compliance_policy_state import DeviceCompliancePolicyState
    from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
    from .device_compliance_script import DeviceComplianceScript
    from .device_compliance_script_device_state import DeviceComplianceScriptDeviceState
    from .device_compliance_script_run_summary import DeviceComplianceScriptRunSummary
    from .device_compliance_setting_state import DeviceComplianceSettingState
    from .device_compliance_user_overview import DeviceComplianceUserOverview
    from .device_compliance_user_status import DeviceComplianceUserStatus
    from .device_configuration import DeviceConfiguration
    from .device_configuration_assignment import DeviceConfigurationAssignment
    from .device_configuration_conflict_summary import DeviceConfigurationConflictSummary
    from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
    from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
    from .device_configuration_device_status import DeviceConfigurationDeviceStatus
    from .device_configuration_group_assignment import DeviceConfigurationGroupAssignment
    from .device_configuration_policy_set_item import DeviceConfigurationPolicySetItem
    from .device_configuration_profile import DeviceConfigurationProfile
    from .device_configuration_state import DeviceConfigurationState
    from .device_configuration_user_overview import DeviceConfigurationUserOverview
    from .device_configuration_user_state_summary import DeviceConfigurationUserStateSummary
    from .device_configuration_user_status import DeviceConfigurationUserStatus
    from .device_custom_attribute_shell_script import DeviceCustomAttributeShellScript
    from .device_enrollment_configuration import DeviceEnrollmentConfiguration
    from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
    from .device_enrollment_notification_configuration import DeviceEnrollmentNotificationConfiguration
    from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
    from .device_enrollment_platform_restriction_configuration import DeviceEnrollmentPlatformRestrictionConfiguration
    from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
    from .device_health_script import DeviceHealthScript
    from .device_health_script_assignment import DeviceHealthScriptAssignment
    from .device_health_script_device_state import DeviceHealthScriptDeviceState
    from .device_health_script_run_summary import DeviceHealthScriptRunSummary
    from .device_install_state import DeviceInstallState
    from .device_local_credential_info import DeviceLocalCredentialInfo
    from .device_log_collection_response import DeviceLogCollectionResponse
    from .device_management.alert_record import AlertRecord
    from .device_management.alert_rule import AlertRule
    from .device_management.device_management import DeviceManagement
    from .device_management.monitoring import Monitoring
    from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition
    from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
    from .device_management_autopilot_event import DeviceManagementAutopilotEvent
    from .device_management_autopilot_policy_status_detail import DeviceManagementAutopilotPolicyStatusDetail
    from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
    from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration
    from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition
    from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance
    from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition
    from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
    from .device_management_compliance_action_item import DeviceManagementComplianceActionItem
    from .device_management_compliance_policy import DeviceManagementCompliancePolicy
    from .device_management_compliance_scheduled_action_for_rule import DeviceManagementComplianceScheduledActionForRule
    from .device_management_configuration_category import DeviceManagementConfigurationCategory
    from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
    from .device_management_configuration_choice_setting_definition import DeviceManagementConfigurationChoiceSettingDefinition
    from .device_management_configuration_policy import DeviceManagementConfigurationPolicy
    from .device_management_configuration_policy_assignment import DeviceManagementConfigurationPolicyAssignment
    from .device_management_configuration_policy_policy_set_item import DeviceManagementConfigurationPolicyPolicySetItem
    from .device_management_configuration_policy_template import DeviceManagementConfigurationPolicyTemplate
    from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition
    from .device_management_configuration_setting import DeviceManagementConfigurationSetting
    from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
    from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition
    from .device_management_configuration_setting_group_definition import DeviceManagementConfigurationSettingGroupDefinition
    from .device_management_configuration_setting_template import DeviceManagementConfigurationSettingTemplate
    from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition
    from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition
    from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
    from .device_management_domain_join_connector import DeviceManagementDomainJoinConnector
    from .device_management_exchange_connector import DeviceManagementExchangeConnector
    from .device_management_exchange_on_premises_policy import DeviceManagementExchangeOnPremisesPolicy
    from .device_management_export_job import DeviceManagementExportJob
    from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
    from .device_management_intent import DeviceManagementIntent
    from .device_management_intent_assignment import DeviceManagementIntentAssignment
    from .device_management_intent_device_setting_state_summary import DeviceManagementIntentDeviceSettingStateSummary
    from .device_management_intent_device_state import DeviceManagementIntentDeviceState
    from .device_management_intent_device_state_summary import DeviceManagementIntentDeviceStateSummary
    from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory
    from .device_management_intent_user_state import DeviceManagementIntentUserState
    from .device_management_intent_user_state_summary import DeviceManagementIntentUserStateSummary
    from .device_management_partner import DeviceManagementPartner
    from .device_management_reports import DeviceManagementReports
    from .device_management_resource_access_profile_assignment import DeviceManagementResourceAccessProfileAssignment
    from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase
    from .device_management_reusable_policy_setting import DeviceManagementReusablePolicySetting
    from .device_management_script import DeviceManagementScript
    from .device_management_script_assignment import DeviceManagementScriptAssignment
    from .device_management_script_device_state import DeviceManagementScriptDeviceState
    from .device_management_script_group_assignment import DeviceManagementScriptGroupAssignment
    from .device_management_script_policy_set_item import DeviceManagementScriptPolicySetItem
    from .device_management_script_run_summary import DeviceManagementScriptRunSummary
    from .device_management_script_user_state import DeviceManagementScriptUserState
    from .device_management_setting_category import DeviceManagementSettingCategory
    from .device_management_setting_definition import DeviceManagementSettingDefinition
    from .device_management_setting_instance import DeviceManagementSettingInstance
    from .device_management_string_setting_instance import DeviceManagementStringSettingInstance
    from .device_management_template import DeviceManagementTemplate
    from .device_management_template_insights_definition import DeviceManagementTemplateInsightsDefinition
    from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
    from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
    from .device_registration_policy import DeviceRegistrationPolicy
    from .device_setup_configuration import DeviceSetupConfiguration
    from .device_shell_script import DeviceShellScript
    from .directory import Directory
    from .directory_audit import DirectoryAudit
    from .directory_definition import DirectoryDefinition
    from .directory_object import DirectoryObject
    from .directory_object_partner_reference import DirectoryObjectPartnerReference
    from .directory_role import DirectoryRole
    from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicy
    from .directory_role_template import DirectoryRoleTemplate
    from .directory_setting import DirectorySetting
    from .directory_setting_template import DirectorySettingTemplate
    from .dlp_evaluate_policies_job_response import DlpEvaluatePoliciesJobResponse
    from .document import Document
    from .document_comment import DocumentComment
    from .document_comment_reply import DocumentCommentReply
    from .document_set_version import DocumentSetVersion
    from .domain import Domain
    from .domain_dns_cname_record import DomainDnsCnameRecord
    from .domain_dns_mx_record import DomainDnsMxRecord
    from .domain_dns_record import DomainDnsRecord
    from .domain_dns_srv_record import DomainDnsSrvRecord
    from .domain_dns_txt_record import DomainDnsTxtRecord
    from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
    from .domain_security_profile import DomainSecurityProfile
    from .drive import Drive
    from .drive_item import DriveItem
    from .drive_item_version import DriveItemVersion
    from .eas_email_profile_configuration_base import EasEmailProfileConfigurationBase
    from .edge import Edge
    from .ediscovery.add_to_review_set_operation import AddToReviewSetOperation
    from .ediscovery.case import Case
    from .ediscovery.case_export_operation import CaseExportOperation
    from .ediscovery.case_hold_operation import CaseHoldOperation
    from .ediscovery.case_index_operation import CaseIndexOperation
    from .ediscovery.case_operation import CaseOperation
    from .ediscovery.case_settings import CaseSettings
    from .ediscovery.custodian import Custodian
    from .ediscovery.data_source import DataSource
    from .ediscovery.data_source_container import DataSourceContainer
    from .ediscovery.ediscoveryroot import Ediscoveryroot
    from .ediscovery.estimate_statistics_operation import EstimateStatisticsOperation
    from .ediscovery.legal_hold import LegalHold
    from .ediscovery.noncustodial_data_source import NoncustodialDataSource
    from .ediscovery.purge_data_operation import PurgeDataOperation
    from .ediscovery.review_set import ReviewSet
    from .ediscovery.review_set_query import ReviewSetQuery
    from .ediscovery.site_source import SiteSource
    from .ediscovery.source_collection import SourceCollection
    from .ediscovery.tag import Tag
    from .ediscovery.tag_operation import TagOperation
    from .ediscovery.unified_group_source import UnifiedGroupSource
    from .ediscovery.user_source import UserSource
    from .edition_upgrade_configuration import EditionUpgradeConfiguration
    from .educational_activity import EducationalActivity
    from .education_assignment import EducationAssignment
    from .education_assignment_defaults import EducationAssignmentDefaults
    from .education_assignment_resource import EducationAssignmentResource
    from .education_assignment_settings import EducationAssignmentSettings
    from .education_category import EducationCategory
    from .education_class import EducationClass
    from .education_feedback_outcome import EducationFeedbackOutcome
    from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome
    from .education_grading_category import EducationGradingCategory
    from .education_grading_scheme import EducationGradingScheme
    from .education_module import EducationModule
    from .education_module_resource import EducationModuleResource
    from .education_organization import EducationOrganization
    from .education_outcome import EducationOutcome
    from .education_points_outcome import EducationPointsOutcome
    from .education_rubric import EducationRubric
    from .education_rubric_outcome import EducationRubricOutcome
    from .education_school import EducationSchool
    from .education_submission import EducationSubmission
    from .education_submission_resource import EducationSubmissionResource
    from .education_synchronization_error import EducationSynchronizationError
    from .education_synchronization_profile import EducationSynchronizationProfile
    from .education_synchronization_profile_status import EducationSynchronizationProfileStatus
    from .education_user import EducationUser
    from .email_activity_statistics import EmailActivityStatistics
    from .email_authentication_method import EmailAuthenticationMethod
    from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration
    from .email_file_assessment_request import EmailFileAssessmentRequest
    from .embedded_s_i_m_activation_code_pool import EmbeddedSIMActivationCodePool
    from .embedded_s_i_m_activation_code_pool_assignment import EmbeddedSIMActivationCodePoolAssignment
    from .embedded_s_i_m_device_state import EmbeddedSIMDeviceState
    from .employee_experience_user import EmployeeExperienceUser
    from .encrypted_aws_storage_bucket_finding import EncryptedAwsStorageBucketFinding
    from .encrypted_azure_storage_account_finding import EncryptedAzureStorageAccountFinding
    from .encrypted_gcp_storage_bucket_finding import EncryptedGcpStorageBucketFinding
    from .endpoint import Endpoint
    from .end_user_notification import EndUserNotification
    from .end_user_notification_detail import EndUserNotificationDetail
    from .engagement_async_operation import EngagementAsyncOperation
    from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
    from .enrollment_profile import EnrollmentProfile
    from .enrollment_restrictions_configuration_policy_set_item import EnrollmentRestrictionsConfigurationPolicySetItem
    from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
    from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
    from .entitlement_management import EntitlementManagement
    from .entitlement_management_settings import EntitlementManagementSettings
    from .evaluate_label_job_response import EvaluateLabelJobResponse
    from .event import Event
    from .event_message import EventMessage
    from .event_message_request import EventMessageRequest
    from .event_message_response import EventMessageResponse
    from .exact_match_data_store import ExactMatchDataStore
    from .exact_match_data_store_base import ExactMatchDataStoreBase
    from .exact_match_job_base import ExactMatchJobBase
    from .exact_match_lookup_job import ExactMatchLookupJob
    from .exact_match_session import ExactMatchSession
    from .exact_match_session_base import ExactMatchSessionBase
    from .exact_match_upload_agent import ExactMatchUploadAgent
    from .extension import Extension
    from .extension_property import ExtensionProperty
    from .external import External
    from .externally_accessible_aws_storage_bucket_finding import ExternallyAccessibleAwsStorageBucketFinding
    from .externally_accessible_azure_blob_container_finding import ExternallyAccessibleAzureBlobContainerFinding
    from .externally_accessible_gcp_storage_bucket_finding import ExternallyAccessibleGcpStorageBucketFinding
    from .external_connection import ExternalConnection
    from .external_connectors.connection_operation import ConnectionOperation
    from .external_connectors.connection_quota import ConnectionQuota
    from .external_connectors.external_activity import ExternalActivity
    from .external_connectors.external_activity_result import ExternalActivityResult
    from .external_connectors.external_connection import ExternalConnection
    from .external_connectors.external_group import ExternalGroup
    from .external_connectors.external_item import ExternalItem
    from .external_connectors.identity import Identity
    from .external_connectors.schema import Schema
    from .external_domain_name import ExternalDomainName
    from .external_group import ExternalGroup
    from .external_identities_policy import ExternalIdentitiesPolicy
    from .external_item import ExternalItem
    from .external_meeting_registrant import ExternalMeetingRegistrant
    from .external_meeting_registration import ExternalMeetingRegistration
    from .external_profile import ExternalProfile
    from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow
    from .external_user_profile import ExternalUserProfile
    from .e_book_install_summary import EBookInstallSummary
    from .feature_rollout_policy import FeatureRolloutPolicy
    from .federated_identity_credential import FederatedIdentityCredential
    from .federated_token_validation_policy import FederatedTokenValidationPolicy
    from .fido2_authentication_method import Fido2AuthenticationMethod
    from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
    from .fido2_combination_configuration import Fido2CombinationConfiguration
    from .field_value_set import FieldValueSet
    from .file_assessment_request import FileAssessmentRequest
    from .file_attachment import FileAttachment
    from .file_classification_request import FileClassificationRequest
    from .file_security_profile import FileSecurityProfile
    from .filter_operator_schema import FilterOperatorSchema
    from .finding import Finding
    from .focus_activity_statistics import FocusActivityStatistics
    from .gcp_authorization_system import GcpAuthorizationSystem
    from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
    from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
    from .gcp_cloud_function import GcpCloudFunction
    from .gcp_group import GcpGroup
    from .gcp_identity import GcpIdentity
    from .gcp_role import GcpRole
    from .gcp_service_account import GcpServiceAccount
    from .gcp_user import GcpUser
    from .goals import Goals
    from .goals_export_job import GoalsExportJob
    from .governance_insight import GovernanceInsight
    from .governance_policy_template import GovernancePolicyTemplate
    from .governance_resource import GovernanceResource
    from .governance_role_assignment import GovernanceRoleAssignment
    from .governance_role_assignment_request import GovernanceRoleAssignmentRequest
    from .governance_role_definition import GovernanceRoleDefinition
    from .governance_role_setting import GovernanceRoleSetting
    from .governance_subject import GovernanceSubject
    from .group import Group
    from .group_lifecycle_policy import GroupLifecyclePolicy
    from .group_policy_category import GroupPolicyCategory
    from .group_policy_configuration import GroupPolicyConfiguration
    from .group_policy_configuration_assignment import GroupPolicyConfigurationAssignment
    from .group_policy_definition import GroupPolicyDefinition
    from .group_policy_definition_file import GroupPolicyDefinitionFile
    from .group_policy_definition_value import GroupPolicyDefinitionValue
    from .group_policy_migration_report import GroupPolicyMigrationReport
    from .group_policy_object_file import GroupPolicyObjectFile
    from .group_policy_operation import GroupPolicyOperation
    from .group_policy_presentation import GroupPolicyPresentation
    from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
    from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
    from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
    from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
    from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
    from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
    from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
    from .group_policy_presentation_text import GroupPolicyPresentationText
    from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox
    from .group_policy_presentation_value import GroupPolicyPresentationValue
    from .group_policy_presentation_value_boolean import GroupPolicyPresentationValueBoolean
    from .group_policy_presentation_value_decimal import GroupPolicyPresentationValueDecimal
    from .group_policy_presentation_value_list import GroupPolicyPresentationValueList
    from .group_policy_presentation_value_long_decimal import GroupPolicyPresentationValueLongDecimal
    from .group_policy_presentation_value_multi_text import GroupPolicyPresentationValueMultiText
    from .group_policy_presentation_value_text import GroupPolicyPresentationValueText
    from .group_policy_setting_mapping import GroupPolicySettingMapping
    from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile
    from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation
    from .hardware_configuration import HardwareConfiguration
    from .hardware_configuration_assignment import HardwareConfigurationAssignment
    from .hardware_configuration_device_state import HardwareConfigurationDeviceState
    from .hardware_configuration_run_summary import HardwareConfigurationRunSummary
    from .hardware_configuration_user_state import HardwareConfigurationUserState
    from .hardware_oath_authentication_method_configuration import HardwareOathAuthenticationMethodConfiguration
    from .hardware_password_info import HardwarePasswordInfo
    from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
    from .horizontal_section import HorizontalSection
    from .horizontal_section_column import HorizontalSectionColumn
    from .host_security_profile import HostSecurityProfile
    from .identity_api_connector import IdentityApiConnector
    from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
    from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute
    from .identity_finding import IdentityFinding
    from .identity_governance.custom_task_extension import CustomTaskExtension
    from .identity_governance.lifecycle_management_settings import LifecycleManagementSettings
    from .identity_governance.lifecycle_workflows_container import LifecycleWorkflowsContainer
    from .identity_governance.run import Run
    from .identity_governance.task import Task
    from .identity_governance.task_definition import TaskDefinition
    from .identity_governance.task_processing_result import TaskProcessingResult
    from .identity_governance.task_report import TaskReport
    from .identity_governance.user_processing_result import UserProcessingResult
    from .identity_governance.workflow_template import WorkflowTemplate
    from .identity_provider import IdentityProvider
    from .identity_provider_base import IdentityProviderBase
    from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
    from .identity_user_flow import IdentityUserFlow
    from .identity_user_flow_attribute import IdentityUserFlowAttribute
    from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
    from .impacted_resource import ImpactedResource
    from .imported_apple_device_identity import ImportedAppleDeviceIdentity
    from .imported_apple_device_identity_result import ImportedAppleDeviceIdentityResult
    from .imported_device_identity import ImportedDeviceIdentity
    from .imported_device_identity_result import ImportedDeviceIdentityResult
    from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
    from .imported_windows_autopilot_device_identity_upload import ImportedWindowsAutopilotDeviceIdentityUpload
    from .inactive_aws_resource_finding import InactiveAwsResourceFinding
    from .inactive_aws_role_finding import InactiveAwsRoleFinding
    from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding
    from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding
    from .inactive_group_finding import InactiveGroupFinding
    from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding
    from .inactive_users_by_application_metric_base import InactiveUsersByApplicationMetricBase
    from .inactive_users_metric_base import InactiveUsersMetricBase
    from .inactive_user_finding import InactiveUserFinding
    from .industry_data.administrative_unit_provisioning_flow import AdministrativeUnitProvisioningFlow
    from .industry_data.azure_data_lake_connector import AzureDataLakeConnector
    from .industry_data.class_group_provisioning_flow import ClassGroupProvisioningFlow
    from .industry_data.file_data_connector import FileDataConnector
    from .industry_data.file_validate_operation import FileValidateOperation
    from .industry_data.inbound_file_flow import InboundFileFlow
    from .industry_data.inbound_flow import InboundFlow
    from .industry_data.inbound_flow_activity import InboundFlowActivity
    from .industry_data.industry_data_activity import IndustryDataActivity
    from .industry_data.industry_data_connector import IndustryDataConnector
    from .industry_data.industry_data_root import IndustryDataRoot
    from .industry_data.industry_data_run import IndustryDataRun
    from .industry_data.industry_data_run_activity import IndustryDataRunActivity
    from .industry_data.outbound_flow_activity import OutboundFlowActivity
    from .industry_data.outbound_provisioning_flow_set import OutboundProvisioningFlowSet
    from .industry_data.provisioning_flow import ProvisioningFlow
    from .industry_data.reference_definition import ReferenceDefinition
    from .industry_data.role_group import RoleGroup
    from .industry_data.security_group_provisioning_flow import SecurityGroupProvisioningFlow
    from .industry_data.source_system_definition import SourceSystemDefinition
    from .industry_data.user_provisioning_flow import UserProvisioningFlow
    from .industry_data.validate_operation import ValidateOperation
    from .industry_data.year_time_period_definition import YearTimePeriodDefinition
    from .inference_classification import InferenceClassification
    from .inference_classification_override import InferenceClassificationOverride
    from .information_protection import InformationProtection
    from .information_protection_label import InformationProtectionLabel
    from .information_protection_policy import InformationProtectionPolicy
    from .insights_settings import InsightsSettings
    from .insight_summary import InsightSummary
    from .internal_domain_federation import InternalDomainFederation
    from .internet_explorer_mode import InternetExplorerMode
    from .intune_branding_profile import IntuneBrandingProfile
    from .intune_branding_profile_assignment import IntuneBrandingProfileAssignment
    from .invalid_license_alert_configuration import InvalidLicenseAlertConfiguration
    from .invalid_license_alert_incident import InvalidLicenseAlertIncident
    from .invitation import Invitation
    from .invite_participants_operation import InviteParticipantsOperation
    from .invoke_user_flow_listener import InvokeUserFlowListener
    from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
    from .iosi_pad_o_s_web_clip import IosiPadOSWebClip
    from .ios_certificate_profile import IosCertificateProfile
    from .ios_certificate_profile_base import IosCertificateProfileBase
    from .ios_compliance_policy import IosCompliancePolicy
    from .ios_custom_configuration import IosCustomConfiguration
    from .ios_derived_credential_authentication_configuration import IosDerivedCredentialAuthenticationConfiguration
    from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
    from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
    from .ios_education_device_configuration import IosEducationDeviceConfiguration
    from .ios_edu_device_configuration import IosEduDeviceConfiguration
    from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration
    from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration
    from .ios_general_device_configuration import IosGeneralDeviceConfiguration
    from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
    from .ios_lob_app import IosLobApp
    from .ios_lob_app_provisioning_configuration import IosLobAppProvisioningConfiguration
    from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment
    from .ios_lob_app_provisioning_configuration_policy_set_item import IosLobAppProvisioningConfigurationPolicySetItem
    from .ios_managed_app_protection import IosManagedAppProtection
    from .ios_managed_app_registration import IosManagedAppRegistration
    from .ios_mobile_app_configuration import IosMobileAppConfiguration
    from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
    from .ios_scep_certificate_profile import IosScepCertificateProfile
    from .ios_store_app import IosStoreApp
    from .ios_trusted_root_certificate import IosTrustedRootCertificate
    from .ios_update_configuration import IosUpdateConfiguration
    from .ios_update_device_status import IosUpdateDeviceStatus
    from .ios_vpn_configuration import IosVpnConfiguration
    from .ios_vpp_app import IosVppApp
    from .ios_vpp_app_assigned_device_license import IosVppAppAssignedDeviceLicense
    from .ios_vpp_app_assigned_license import IosVppAppAssignedLicense
    from .ios_vpp_app_assigned_user_license import IosVppAppAssignedUserLicense
    from .ios_vpp_e_book import IosVppEBook
    from .ios_vpp_e_book_assignment import IosVppEBookAssignment
    from .ios_wi_fi_configuration import IosWiFiConfiguration
    from .ip_application_segment import IpApplicationSegment
    from .ip_named_location import IpNamedLocation
    from .ip_security_profile import IpSecurityProfile
    from .item_activity import ItemActivity
    from .item_activity_o_l_d import ItemActivityOLD
    from .item_activity_stat import ItemActivityStat
    from .item_address import ItemAddress
    from .item_analytics import ItemAnalytics
    from .item_attachment import ItemAttachment
    from .item_email import ItemEmail
    from .item_facet import ItemFacet
    from .item_insights import ItemInsights
    from .item_patent import ItemPatent
    from .item_phone import ItemPhone
    from .item_publication import ItemPublication
    from .item_retention_label import ItemRetentionLabel
    from .job_response_base import JobResponseBase
    from .landing_page import LandingPage
    from .landing_page_detail import LandingPageDetail
    from .language_proficiency import LanguageProficiency
    from .learning_assignment import LearningAssignment
    from .learning_content import LearningContent
    from .learning_course_activity import LearningCourseActivity
    from .learning_provider import LearningProvider
    from .learning_self_initiated_course import LearningSelfInitiatedCourse
    from .license_details import LicenseDetails
    from .linked_resource import LinkedResource
    from .list_ import List_
    from .list_item import ListItem
    from .list_item_version import ListItemVersion
    from .localized_notification_message import LocalizedNotificationMessage
    from .login_page import LoginPage
    from .long_running_operation import LongRunningOperation
    from .lookup_result_row import LookupResultRow
    from .m365_apps_installation_options import M365AppsInstallationOptions
    from .mac_os_vpp_app import MacOsVppApp
    from .mac_os_vpp_app_assigned_license import MacOsVppAppAssignedLicense
    from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
    from .mac_o_s_compliance_policy import MacOSCompliancePolicy
    from .mac_o_s_custom_app_configuration import MacOSCustomAppConfiguration
    from .mac_o_s_custom_configuration import MacOSCustomConfiguration
    from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
    from .mac_o_s_dmg_app import MacOSDmgApp
    from .mac_o_s_endpoint_protection_configuration import MacOSEndpointProtectionConfiguration
    from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration
    from .mac_o_s_extensions_configuration import MacOSExtensionsConfiguration
    from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
    from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
    from .mac_o_s_lob_app import MacOSLobApp
    from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp
    from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp
    from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
    from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
    from .mac_o_s_pkg_app import MacOSPkgApp
    from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
    from .mac_o_s_software_update_account_summary import MacOSSoftwareUpdateAccountSummary
    from .mac_o_s_software_update_category_summary import MacOSSoftwareUpdateCategorySummary
    from .mac_o_s_software_update_configuration import MacOSSoftwareUpdateConfiguration
    from .mac_o_s_software_update_state_summary import MacOSSoftwareUpdateStateSummary
    from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
    from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
    from .mac_o_s_web_clip import MacOSWebClip
    from .mac_o_s_wired_network_configuration import MacOSWiredNetworkConfiguration
    from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration
    from .mail_assessment_request import MailAssessmentRequest
    from .mail_folder import MailFolder
    from .mail_search_folder import MailSearchFolder
    from .malware_state_for_windows_device import MalwareStateForWindowsDevice
    from .managed_all_device_certificate_state import ManagedAllDeviceCertificateState
    from .managed_android_lob_app import ManagedAndroidLobApp
    from .managed_android_store_app import ManagedAndroidStoreApp
    from .managed_app import ManagedApp
    from .managed_app_configuration import ManagedAppConfiguration
    from .managed_app_log_collection_request import ManagedAppLogCollectionRequest
    from .managed_app_operation import ManagedAppOperation
    from .managed_app_policy import ManagedAppPolicy
    from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
    from .managed_app_protection import ManagedAppProtection
    from .managed_app_protection_policy_set_item import ManagedAppProtectionPolicySetItem
    from .managed_app_registration import ManagedAppRegistration
    from .managed_app_status import ManagedAppStatus
    from .managed_app_status_raw import ManagedAppStatusRaw
    from .managed_device import ManagedDevice
    from .managed_device_certificate_state import ManagedDeviceCertificateState
    from .managed_device_cleanup_rule import ManagedDeviceCleanupRule
    from .managed_device_encryption_state import ManagedDeviceEncryptionState
    from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
    from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
    from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
    from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
    from .managed_device_mobile_app_configuration_policy_set_item import ManagedDeviceMobileAppConfigurationPolicySetItem
    from .managed_device_mobile_app_configuration_state import ManagedDeviceMobileAppConfigurationState
    from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
    from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary
    from .managed_device_overview import ManagedDeviceOverview
    from .managed_e_book import ManagedEBook
    from .managed_e_book_assignment import ManagedEBookAssignment
    from .managed_e_book_category import ManagedEBookCategory
    from .managed_i_o_s_lob_app import ManagedIOSLobApp
    from .managed_i_o_s_store_app import ManagedIOSStoreApp
    from .managed_mobile_app import ManagedMobileApp
    from .managed_mobile_lob_app import ManagedMobileLobApp
    from .managed_tenants.aggregated_policy_compliance import AggregatedPolicyCompliance
    from .managed_tenants.app_performance import AppPerformance
    from .managed_tenants.audit_event import AuditEvent
    from .managed_tenants.cloud_pc_connection import CloudPcConnection
    from .managed_tenants.cloud_pc_device import CloudPcDevice
    from .managed_tenants.cloud_pc_overview import CloudPcOverview
    from .managed_tenants.conditional_access_policy_coverage import ConditionalAccessPolicyCoverage
    from .managed_tenants.credential_user_registrations_summary import CredentialUserRegistrationsSummary
    from .managed_tenants.device_app_performance import DeviceAppPerformance
    from .managed_tenants.device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
    from .managed_tenants.device_health_status import DeviceHealthStatus
    from .managed_tenants.managed_device_compliance import ManagedDeviceCompliance
    from .managed_tenants.managed_device_compliance_trend import ManagedDeviceComplianceTrend
    from .managed_tenants.managed_tenant import ManagedTenant
    from .managed_tenants.managed_tenant_alert import ManagedTenantAlert
    from .managed_tenants.managed_tenant_alert_log import ManagedTenantAlertLog
    from .managed_tenants.managed_tenant_alert_rule import ManagedTenantAlertRule
    from .managed_tenants.managed_tenant_alert_rule_definition import ManagedTenantAlertRuleDefinition
    from .managed_tenants.managed_tenant_api_notification import ManagedTenantApiNotification
    from .managed_tenants.managed_tenant_email_notification import ManagedTenantEmailNotification
    from .managed_tenants.managed_tenant_ticketing_endpoint import ManagedTenantTicketingEndpoint
    from .managed_tenants.management_action import ManagementAction
    from .managed_tenants.management_action_tenant_deployment_status import ManagementActionTenantDeploymentStatus
    from .managed_tenants.management_intent import ManagementIntent
    from .managed_tenants.management_template import ManagementTemplate
    from .managed_tenants.management_template_collection import ManagementTemplateCollection
    from .managed_tenants.management_template_collection_tenant_summary import ManagementTemplateCollectionTenantSummary
    from .managed_tenants.management_template_step import ManagementTemplateStep
    from .managed_tenants.management_template_step_deployment import ManagementTemplateStepDeployment
    from .managed_tenants.management_template_step_tenant_summary import ManagementTemplateStepTenantSummary
    from .managed_tenants.management_template_step_version import ManagementTemplateStepVersion
    from .managed_tenants.tenant import Tenant
    from .managed_tenants.tenant_customized_information import TenantCustomizedInformation
    from .managed_tenants.tenant_detailed_information import TenantDetailedInformation
    from .managed_tenants.tenant_group import TenantGroup
    from .managed_tenants.tenant_tag import TenantTag
    from .managed_tenants.windows_device_malware_state import WindowsDeviceMalwareState
    from .managed_tenants.windows_protection_state import WindowsProtectionState
    from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
    from .mdm_windows_information_protection_policy_policy_set_item import MdmWindowsInformationProtectionPolicyPolicySetItem
    from .meeting_activity_statistics import MeetingActivityStatistics
    from .meeting_attendance_report import MeetingAttendanceReport
    from .meeting_registrant import MeetingRegistrant
    from .meeting_registrant_base import MeetingRegistrantBase
    from .meeting_registration import MeetingRegistration
    from .meeting_registration_base import MeetingRegistrationBase
    from .meeting_registration_question import MeetingRegistrationQuestion
    from .membership_outlier_insight import MembershipOutlierInsight
    from .mention import Mention
    from .message import Message
    from .message_event import MessageEvent
    from .message_recipient import MessageRecipient
    from .message_rule import MessageRule
    from .message_trace import MessageTrace
    from .mfa_completion_metric import MfaCompletionMetric
    from .mfa_failure import MfaFailure
    from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
    from .microsoft_application_data_access_settings import MicrosoftApplicationDataAccessSettings
    from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
    from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration
    from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
    from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
    from .microsoft_store_for_business_contained_app import MicrosoftStoreForBusinessContainedApp
    from .microsoft_tunnel_configuration import MicrosoftTunnelConfiguration
    from .microsoft_tunnel_health_threshold import MicrosoftTunnelHealthThreshold
    from .microsoft_tunnel_server import MicrosoftTunnelServer
    from .microsoft_tunnel_server_log_collection_response import MicrosoftTunnelServerLogCollectionResponse
    from .microsoft_tunnel_site import MicrosoftTunnelSite
    from .mobile_app import MobileApp
    from .mobile_app_assignment import MobileAppAssignment
    from .mobile_app_catalog_package import MobileAppCatalogPackage
    from .mobile_app_category import MobileAppCategory
    from .mobile_app_content import MobileAppContent
    from .mobile_app_content_file import MobileAppContentFile
    from .mobile_app_dependency import MobileAppDependency
    from .mobile_app_install_status import MobileAppInstallStatus
    from .mobile_app_install_summary import MobileAppInstallSummary
    from .mobile_app_intent_and_state import MobileAppIntentAndState
    from .mobile_app_policy_set_item import MobileAppPolicySetItem
    from .mobile_app_provisioning_config_group_assignment import MobileAppProvisioningConfigGroupAssignment
    from .mobile_app_relationship import MobileAppRelationship
    from .mobile_app_supersedence import MobileAppSupersedence
    from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
    from .mobile_contained_app import MobileContainedApp
    from .mobile_lob_app import MobileLobApp
    from .mobile_threat_defense_connector import MobileThreatDefenseConnector
    from .mobility_management_policy import MobilityManagementPolicy
    from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric
    from .monthly_inactive_users_metric import MonthlyInactiveUsersMetric
    from .monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot
    from .multi_tenant_organization import MultiTenantOrganization
    from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate
    from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord
    from .multi_tenant_organization_member import MultiTenantOrganizationMember
    from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate
    from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
    from .mute_participants_operation import MuteParticipantsOperation
    from .mute_participant_operation import MuteParticipantOperation
    from .named_location import NamedLocation
    from .ndes_connector import NdesConnector
    from .networkaccess.alert import Alert
    from .networkaccess.branch_site import BranchSite
    from .networkaccess.conditional_access_policy import ConditionalAccessPolicy
    from .networkaccess.conditional_access_settings import ConditionalAccessSettings
    from .networkaccess.connectivity import Connectivity
    from .networkaccess.connectivity_configuration_link import ConnectivityConfigurationLink
    from .networkaccess.cross_tenant_access_settings import CrossTenantAccessSettings
    from .networkaccess.device_link import DeviceLink
    from .networkaccess.enriched_audit_logs import EnrichedAuditLogs
    from .networkaccess.filtering_policy import FilteringPolicy
    from .networkaccess.filtering_policy_link import FilteringPolicyLink
    from .networkaccess.filtering_profile import FilteringProfile
    from .networkaccess.filtering_rule import FilteringRule
    from .networkaccess.forwarding_options import ForwardingOptions
    from .networkaccess.forwarding_policy import ForwardingPolicy
    from .networkaccess.forwarding_policy_link import ForwardingPolicyLink
    from .networkaccess.forwarding_profile import ForwardingProfile
    from .networkaccess.forwarding_rule import ForwardingRule
    from .networkaccess.fqdn_filtering_rule import FqdnFilteringRule
    from .networkaccess.internet_access_forwarding_rule import InternetAccessForwardingRule
    from .networkaccess.logs import Logs
    from .networkaccess.m365_forwarding_rule import M365ForwardingRule
    from .networkaccess.network_access_root import NetworkAccessRoot
    from .networkaccess.policy import Policy
    from .networkaccess.policy_link import PolicyLink
    from .networkaccess.policy_rule import PolicyRule
    from .networkaccess.private_access_forwarding_rule import PrivateAccessForwardingRule
    from .networkaccess.profile import Profile
    from .networkaccess.remote_network import RemoteNetwork
    from .networkaccess.remote_network_health_event import RemoteNetworkHealthEvent
    from .networkaccess.reports import Reports
    from .networkaccess.settings import Settings
    from .networkaccess.tenant_status import TenantStatus
    from .networkaccess.web_category_filtering_rule import WebCategoryFilteringRule
    from .news_link_page import NewsLinkPage
    from .note import Note
    from .notebook import Notebook
    from .notification import Notification
    from .notification_message_template import NotificationMessageTemplate
    from .no_mfa_on_role_activation_alert_configuration import NoMfaOnRoleActivationAlertConfiguration
    from .no_mfa_on_role_activation_alert_incident import NoMfaOnRoleActivationAlertIncident
    from .offer_shift_request import OfferShiftRequest
    from .office365_active_user_counts import Office365ActiveUserCounts
    from .office365_active_user_detail import Office365ActiveUserDetail
    from .office365_groups_activity_counts import Office365GroupsActivityCounts
    from .office365_groups_activity_detail import Office365GroupsActivityDetail
    from .office365_groups_activity_file_counts import Office365GroupsActivityFileCounts
    from .office365_groups_activity_group_counts import Office365GroupsActivityGroupCounts
    from .office365_groups_activity_storage import Office365GroupsActivityStorage
    from .office365_services_user_counts import Office365ServicesUserCounts
    from .office_graph_insights import OfficeGraphInsights
    from .office_suite_app import OfficeSuiteApp
    from .onenote import Onenote
    from .onenote_entity_base_model import OnenoteEntityBaseModel
    from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
    from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
    from .onenote_operation import OnenoteOperation
    from .onenote_page import OnenotePage
    from .onenote_resource import OnenoteResource
    from .onenote_section import OnenoteSection
    from .online_meeting import OnlineMeeting
    from .online_meeting_base import OnlineMeetingBase
    from .on_attribute_collection_listener import OnAttributeCollectionListener
    from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
    from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener
    from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
    from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener
    from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
    from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
    from .on_premises_agent import OnPremisesAgent
    from .on_premises_agent_group import OnPremisesAgentGroup
    from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
    from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
    from .on_premises_publishing_profile import OnPremisesPublishingProfile
    from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
    from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
    from .on_user_create_start_listener import OnUserCreateStartListener
    from .open_aws_security_group_finding import OpenAwsSecurityGroupFinding
    from .open_id_connect_identity_provider import OpenIdConnectIdentityProvider
    from .open_id_connect_provider import OpenIdConnectProvider
    from .open_network_azure_security_group_finding import OpenNetworkAzureSecurityGroupFinding
    from .open_shift import OpenShift
    from .open_shift_change_request import OpenShiftChangeRequest
    from .open_type_extension import OpenTypeExtension
    from .operation import Operation
    from .operation_approval_policy import OperationApprovalPolicy
    from .operation_approval_request import OperationApprovalRequest
    from .organization import Organization
    from .organizational_branding import OrganizationalBranding
    from .organizational_branding_localization import OrganizationalBrandingLocalization
    from .organizational_branding_properties import OrganizationalBrandingProperties
    from .organization_settings import OrganizationSettings
    from .org_contact import OrgContact
    from .outlook_category import OutlookCategory
    from .outlook_item import OutlookItem
    from .outlook_task import OutlookTask
    from .outlook_task_folder import OutlookTaskFolder
    from .outlook_task_group import OutlookTaskGroup
    from .outlook_user import OutlookUser
    from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding
    from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding
    from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
    from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding
    from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding
    from .overprovisioned_user_finding import OverprovisionedUserFinding
    from .o_auth2_permission_grant import OAuth2PermissionGrant
    from .participant import Participant
    from .participant_joining_notification import ParticipantJoiningNotification
    from .participant_left_notification import ParticipantLeftNotification
    from .partners.billing.azure_usage import AzureUsage
    from .partners.billing.billed_reconciliation import BilledReconciliation
    from .partners.billing.billed_usage import BilledUsage
    from .partners.billing.billing import Billing
    from .partners.billing.billing_reconciliation import BillingReconciliation
    from .partners.billing.export_success_operation import ExportSuccessOperation
    from .partners.billing.failed_operation import FailedOperation
    from .partners.billing.manifest import Manifest
    from .partners.billing.operation import Operation
    from .partners.billing.running_operation import RunningOperation
    from .partners.billing.unbilled_usage import UnbilledUsage
    from .partners.partners import Partners
    from .passwordless_microsoft_authenticator_authentication_method import PasswordlessMicrosoftAuthenticatorAuthenticationMethod
    from .password_authentication_method import PasswordAuthenticationMethod
    from .payload import Payload
    from .payload_compatible_assignment_filter import PayloadCompatibleAssignmentFilter
    from .payload_response import PayloadResponse
    from .pending_external_user_profile import PendingExternalUserProfile
    from .people_admin_settings import PeopleAdminSettings
    from .permission import Permission
    from .permissions_analytics import PermissionsAnalytics
    from .permissions_analytics_aggregation import PermissionsAnalyticsAggregation
    from .permissions_creep_index_distribution import PermissionsCreepIndexDistribution
    from .permissions_definition_aws_policy import PermissionsDefinitionAwsPolicy
    from .permissions_definition_azure_role import PermissionsDefinitionAzureRole
    from .permissions_definition_gcp_role import PermissionsDefinitionGcpRole
    from .permissions_management import PermissionsManagement
    from .permissions_request_change import PermissionsRequestChange
    from .permission_grant_condition_set import PermissionGrantConditionSet
    from .permission_grant_policy import PermissionGrantPolicy
    from .person import Person
    from .person_annotation import PersonAnnotation
    from .person_annual_event import PersonAnnualEvent
    from .person_award import PersonAward
    from .person_certification import PersonCertification
    from .person_extension import PersonExtension
    from .person_interest import PersonInterest
    from .person_name import PersonName
    from .person_responsibility import PersonResponsibility
    from .person_website import PersonWebsite
    from .phone_authentication_method import PhoneAuthenticationMethod
    from .pinned_chat_message_info import PinnedChatMessageInfo
    from .place import Place
    from .planner import Planner
    from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
    from .planner_bucket import PlannerBucket
    from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
    from .planner_delta import PlannerDelta
    from .planner_group import PlannerGroup
    from .planner_plan import PlannerPlan
    from .planner_plan_configuration import PlannerPlanConfiguration
    from .planner_plan_configuration_localization import PlannerPlanConfigurationLocalization
    from .planner_plan_details import PlannerPlanDetails
    from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
    from .planner_roster import PlannerRoster
    from .planner_roster_member import PlannerRosterMember
    from .planner_task import PlannerTask
    from .planner_task_configuration import PlannerTaskConfiguration
    from .planner_task_details import PlannerTaskDetails
    from .planner_user import PlannerUser
    from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
    from .play_prompt_operation import PlayPromptOperation
    from .policy_base import PolicyBase
    from .policy_root import PolicyRoot
    from .policy_set import PolicySet
    from .policy_set_assignment import PolicySetAssignment
    from .policy_set_item import PolicySetItem
    from .policy_template import PolicyTemplate
    from .post import Post
    from .presence import Presence
    from .presentation import Presentation
    from .printer import Printer
    from .printer_base import PrinterBase
    from .printer_create_operation import PrinterCreateOperation
    from .printer_share import PrinterShare
    from .print_connector import PrintConnector
    from .print_document import PrintDocument
    from .print_job import PrintJob
    from .print_operation import PrintOperation
    from .print_service import PrintService
    from .print_service_endpoint import PrintServiceEndpoint
    from .print_task import PrintTask
    from .print_task_definition import PrintTaskDefinition
    from .print_task_trigger import PrintTaskTrigger
    from .print_usage import PrintUsage
    from .print_usage_by_printer import PrintUsageByPrinter
    from .print_usage_by_user import PrintUsageByUser
    from .privileged_access import PrivilegedAccess
    from .privileged_access_group import PrivilegedAccessGroup
    from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
    from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
    from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
    from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
    from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
    from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
    from .privileged_access_root import PrivilegedAccessRoot
    from .privileged_access_schedule import PrivilegedAccessSchedule
    from .privileged_access_schedule_instance import PrivilegedAccessScheduleInstance
    from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest
    from .privileged_approval import PrivilegedApproval
    from .privileged_operation_event import PrivilegedOperationEvent
    from .privileged_role import PrivilegedRole
    from .privileged_role_assignment import PrivilegedRoleAssignment
    from .privileged_role_assignment_request import PrivilegedRoleAssignmentRequest
    from .privileged_role_settings import PrivilegedRoleSettings
    from .privileged_role_summary import PrivilegedRoleSummary
    from .privileged_signup_status import PrivilegedSignupStatus
    from .privilege_escalation import PrivilegeEscalation
    from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
    from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
    from .privilege_escalation_finding import PrivilegeEscalationFinding
    from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
    from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding
    from .privilege_management_elevation import PrivilegeManagementElevation
    from .privilege_management_elevation_request import PrivilegeManagementElevationRequest
    from .profile import Profile
    from .profile_card_property import ProfileCardProperty
    from .profile_photo import ProfilePhoto
    from .program import Program
    from .program_control import ProgramControl
    from .program_control_type import ProgramControlType
    from .project_participation import ProjectParticipation
    from .pronouns_settings import PronounsSettings
    from .provider_tenant_setting import ProviderTenantSetting
    from .provisioning_object_summary import ProvisioningObjectSummary
    from .published_resource import PublishedResource
    from .purchase_invoice_line import PurchaseInvoiceLine
    from .rbac_application import RbacApplication
    from .rbac_application_multiple import RbacApplicationMultiple
    from .recommendation import Recommendation
    from .recommendation_base import RecommendationBase
    from .record_operation import RecordOperation
    from .recycle_bin import RecycleBin
    from .recycle_bin_item import RecycleBinItem
    from .redundant_assignment_alert_configuration import RedundantAssignmentAlertConfiguration
    from .redundant_assignment_alert_incident import RedundantAssignmentAlertIncident
    from .reference_attachment import ReferenceAttachment
    from .regional_and_language_settings import RegionalAndLanguageSettings
    from .relying_party_detailed_summary import RelyingPartyDetailedSummary
    from .remote_action_audit import RemoteActionAudit
    from .remote_assistance_partner import RemoteAssistancePartner
    from .remote_assistance_settings import RemoteAssistanceSettings
    from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
    from .report_root import ReportRoot
    from .request import Request
    from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship
    from .resource_operation import ResourceOperation
    from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
    from .restricted_apps_violation import RestrictedAppsViolation
    from .rich_long_running_operation import RichLongRunningOperation
    from .risky_service_principal import RiskyServicePrincipal
    from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
    from .risky_user import RiskyUser
    from .risky_user_history_item import RiskyUserHistoryItem
    from .risk_detection import RiskDetection
    from .roles_assigned_outside_privileged_identity_management_alert_configuration import RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration
    from .roles_assigned_outside_privileged_identity_management_alert_incident import RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident
    from .role_assignment import RoleAssignment
    from .role_definition import RoleDefinition
    from .role_management_alert import RoleManagementAlert
    from .role_scope_tag import RoleScopeTag
    from .role_scope_tag_auto_assignment import RoleScopeTagAutoAssignment
    from .room import Room
    from .room_list import RoomList
    from .sales_credit_memo_line import SalesCreditMemoLine
    from .sales_invoice_line import SalesInvoiceLine
    from .sales_order_line import SalesOrderLine
    from .sales_quote_line import SalesQuoteLine
    from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
    from .saml_or_ws_fed_provider import SamlOrWsFedProvider
    from .schedule import Schedule
    from .scheduled_permissions_request import ScheduledPermissionsRequest
    from .schedule_change_request import ScheduleChangeRequest
    from .scheduling_group import SchedulingGroup
    from .schema import Schema
    from .schema_extension import SchemaExtension
    from .scoped_role_membership import ScopedRoleMembership
    from .search.acronym import Acronym
    from .search.bookmark import Bookmark
    from .search.qna import Qna
    from .search.search_answer import SearchAnswer
    from .search_entity import SearchEntity
    from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding
    from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding
    from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding
    from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding
    from .section_group import SectionGroup
    from .secure_score import SecureScore
    from .secure_score_control_profile import SecureScoreControlProfile
    from .security.alert import Alert
    from .security.analyzed_email import AnalyzedEmail
    from .security.article import Article
    from .security.article_indicator import ArticleIndicator
    from .security.artifact import Artifact
    from .security.audit_core_root import AuditCoreRoot
    from .security.audit_log_query import AuditLogQuery
    from .security.audit_log_record import AuditLogRecord
    from .security.authority_template import AuthorityTemplate
    from .security.case import Case
    from .security.cases_root import CasesRoot
    from .security.case_operation import CaseOperation
    from .security.category_template import CategoryTemplate
    from .security.citation_template import CitationTemplate
    from .security.collaboration_root import CollaborationRoot
    from .security.data_set import DataSet
    from .security.data_source import DataSource
    from .security.data_source_container import DataSourceContainer
    from .security.department_template import DepartmentTemplate
    from .security.detection_rule import DetectionRule
    from .security.disposition_review_stage import DispositionReviewStage
    from .security.ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
    from .security.ediscovery_case import EdiscoveryCase
    from .security.ediscovery_case_settings import EdiscoveryCaseSettings
    from .security.ediscovery_custodian import EdiscoveryCustodian
    from .security.ediscovery_estimate_operation import EdiscoveryEstimateOperation
    from .security.ediscovery_export_operation import EdiscoveryExportOperation
    from .security.ediscovery_file import EdiscoveryFile
    from .security.ediscovery_hold_operation import EdiscoveryHoldOperation
    from .security.ediscovery_hold_policy import EdiscoveryHoldPolicy
    from .security.ediscovery_index_operation import EdiscoveryIndexOperation
    from .security.ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
    from .security.ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
    from .security.ediscovery_review_set import EdiscoveryReviewSet
    from .security.ediscovery_review_set_query import EdiscoveryReviewSetQuery
    from .security.ediscovery_review_tag import EdiscoveryReviewTag
    from .security.ediscovery_search import EdiscoverySearch
    from .security.ediscovery_search_export_operation import EdiscoverySearchExportOperation
    from .security.ediscovery_tag_operation import EdiscoveryTagOperation
    from .security.email_content_threat_submission import EmailContentThreatSubmission
    from .security.email_threat_submission import EmailThreatSubmission
    from .security.email_threat_submission_policy import EmailThreatSubmissionPolicy
    from .security.email_url_threat_submission import EmailUrlThreatSubmission
    from .security.file import File
    from .security.file_content_threat_submission import FileContentThreatSubmission
    from .security.file_plan_descriptor import FilePlanDescriptor
    from .security.file_plan_descriptor_template import FilePlanDescriptorTemplate
    from .security.file_plan_reference_template import FilePlanReferenceTemplate
    from .security.file_threat_submission import FileThreatSubmission
    from .security.file_url_threat_submission import FileUrlThreatSubmission
    from .security.health_issue import HealthIssue
    from .security.host import Host
    from .security.hostname import Hostname
    from .security.host_component import HostComponent
    from .security.host_cookie import HostCookie
    from .security.host_pair import HostPair
    from .security.host_port import HostPort
    from .security.host_reputation import HostReputation
    from .security.host_ssl_certificate import HostSslCertificate
    from .security.host_tracker import HostTracker
    from .security.identity_container import IdentityContainer
    from .security.incident import Incident
    from .security.indicator import Indicator
    from .security.information_protection import InformationProtection
    from .security.information_protection_policy_setting import InformationProtectionPolicySetting
    from .security.intelligence_profile import IntelligenceProfile
    from .security.intelligence_profile_indicator import IntelligenceProfileIndicator
    from .security.ip_address import IpAddress
    from .security.labels_root import LabelsRoot
    from .security.passive_dns_record import PassiveDnsRecord
    from .security.policy_base import PolicyBase
    from .security.protection_rule import ProtectionRule
    from .security.retention_event import RetentionEvent
    from .security.retention_event_type import RetentionEventType
    from .security.retention_label import RetentionLabel
    from .security.rules_root import RulesRoot
    from .security.search import Search
    from .security.security import Security
    from .security.sensitivity_label import SensitivityLabel
    from .security.site_source import SiteSource
    from .security.ssl_certificate import SslCertificate
    from .security.subcategory_template import SubcategoryTemplate
    from .security.subdomain import Subdomain
    from .security.tag import Tag
    from .security.threat_intelligence import ThreatIntelligence
    from .security.threat_submission import ThreatSubmission
    from .security.threat_submission_root import ThreatSubmissionRoot
    from .security.triggers_root import TriggersRoot
    from .security.trigger_types_root import TriggerTypesRoot
    from .security.unclassified_artifact import UnclassifiedArtifact
    from .security.unified_group_source import UnifiedGroupSource
    from .security.url_threat_submission import UrlThreatSubmission
    from .security.user_source import UserSource
    from .security.vulnerability import Vulnerability
    from .security.vulnerability_component import VulnerabilityComponent
    from .security.whois_base_record import WhoisBaseRecord
    from .security.whois_history_record import WhoisHistoryRecord
    from .security.whois_record import WhoisRecord
    from .security_action import SecurityAction
    from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary
    from .security_baseline_device_state import SecurityBaselineDeviceState
    from .security_baseline_setting_state import SecurityBaselineSettingState
    from .security_baseline_state import SecurityBaselineState
    from .security_baseline_state_summary import SecurityBaselineStateSummary
    from .security_baseline_template import SecurityBaselineTemplate
    from .security_configuration_task import SecurityConfigurationTask
    from .security_reports_root import SecurityReportsRoot
    from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
    from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
    from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
    from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding
    from .send_dtmf_tones_operation import SendDtmfTonesOperation
    from .sensitive_type import SensitiveType
    from .sensitivity_label import SensitivityLabel
    from .sensitivity_policy_settings import SensitivityPolicySettings
    from .sequential_activation_renewals_alert_configuration import SequentialActivationRenewalsAlertConfiguration
    from .sequential_activation_renewals_alert_incident import SequentialActivationRenewalsAlertIncident
    from .service_activity import ServiceActivity
    from .service_announcement import ServiceAnnouncement
    from .service_announcement_attachment import ServiceAnnouncementAttachment
    from .service_announcement_base import ServiceAnnouncementBase
    from .service_health import ServiceHealth
    from .service_health_issue import ServiceHealthIssue
    from .service_level_agreement_root import ServiceLevelAgreementRoot
    from .service_now_connection import ServiceNowConnection
    from .service_principal import ServicePrincipal
    from .service_principal_creation_condition_set import ServicePrincipalCreationConditionSet
    from .service_principal_creation_policy import ServicePrincipalCreationPolicy
    from .service_principal_risk_detection import ServicePrincipalRiskDetection
    from .service_principal_sign_in_activity import ServicePrincipalSignInActivity
    from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown
    from .service_update_message import ServiceUpdateMessage
    from .setting_state_device_summary import SettingStateDeviceSummary
    from .shared_drive_item import SharedDriveItem
    from .shared_email_domain import SharedEmailDomain
    from .shared_email_domain_invitation import SharedEmailDomainInvitation
    from .shared_insight import SharedInsight
    from .shared_p_c_configuration import SharedPCConfiguration
    from .shared_with_channel_team_info import SharedWithChannelTeamInfo
    from .sharepoint import Sharepoint
    from .sharepoint_settings import SharepointSettings
    from .shift import Shift
    from .shifts_role_definition import ShiftsRoleDefinition
    from .shift_preferences import ShiftPreferences
    from .sign_in import SignIn
    from .simulation import Simulation
    from .simulation_automation import SimulationAutomation
    from .simulation_automation_run import SimulationAutomationRun
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
    from .site import Site
    from .site_page import SitePage
    from .skill_proficiency import SkillProficiency
    from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
    from .skype_user_conversation_member import SkypeUserConversationMember
    from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration
    from .sms_authentication_method_target import SmsAuthenticationMethodTarget
    from .social_identity_provider import SocialIdentityProvider
    from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
    from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration
    from .software_update_status_summary import SoftwareUpdateStatusSummary
    from .stale_sign_in_alert_configuration import StaleSignInAlertConfiguration
    from .stale_sign_in_alert_incident import StaleSignInAlertIncident
    from .standard_web_part import StandardWebPart
    from .start_hold_music_operation import StartHoldMusicOperation
    from .stop_hold_music_operation import StopHoldMusicOperation
    from .storage_quota_breakdown import StorageQuotaBreakdown
    from .storage_settings import StorageSettings
    from .strong_authentication_detail import StrongAuthenticationDetail
    from .strong_authentication_phone_app_detail import StrongAuthenticationPhoneAppDetail
    from .sts_policy import StsPolicy
    from .subject_rights_request import SubjectRightsRequest
    from .subscribed_sku import SubscribedSku
    from .subscribe_to_tone_operation import SubscribeToToneOperation
    from .subscription import Subscription
    from .super_aws_resource_finding import SuperAwsResourceFinding
    from .super_aws_role_finding import SuperAwsRoleFinding
    from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding
    from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding
    from .super_serverless_function_finding import SuperServerlessFunctionFinding
    from .super_user_finding import SuperUserFinding
    from .swap_shifts_change_request import SwapShiftsChangeRequest
    from .symantec_code_signing_certificate import SymantecCodeSigningCertificate
    from .synchronization import Synchronization
    from .synchronization_job import SynchronizationJob
    from .synchronization_schema import SynchronizationSchema
    from .synchronization_template import SynchronizationTemplate
    from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
    from .targeted_managed_app_configuration_policy_set_item import TargetedManagedAppConfigurationPolicySetItem
    from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
    from .targeted_managed_app_protection import TargetedManagedAppProtection
    from .target_device_group import TargetDeviceGroup
    from .task_file_attachment import TaskFileAttachment
    from .tax_group import TaxGroup
    from .team import Team
    from .teams_app import TeamsApp
    from .teams_app_dashboard_card_definition import TeamsAppDashboardCardDefinition
    from .teams_app_definition import TeamsAppDefinition
    from .teams_app_icon import TeamsAppIcon
    from .teams_app_installation import TeamsAppInstallation
    from .teams_app_settings import TeamsAppSettings
    from .teams_async_operation import TeamsAsyncOperation
    from .teams_tab import TeamsTab
    from .teams_template import TeamsTemplate
    from .teams_user_configuration.teams_admin_root import TeamsAdminRoot
    from .teams_user_configuration.user_configuration import UserConfiguration
    from .teamwork import Teamwork
    from .teamwork_bot import TeamworkBot
    from .teamwork_device import TeamworkDevice
    from .teamwork_device_activity import TeamworkDeviceActivity
    from .teamwork_device_configuration import TeamworkDeviceConfiguration
    from .teamwork_device_health import TeamworkDeviceHealth
    from .teamwork_device_operation import TeamworkDeviceOperation
    from .teamwork_hosted_content import TeamworkHostedContent
    from .teamwork_peripheral import TeamworkPeripheral
    from .teamwork_tag import TeamworkTag
    from .teamwork_tag_member import TeamworkTagMember
    from .team_info import TeamInfo
    from .team_template import TeamTemplate
    from .team_template_definition import TeamTemplateDefinition
    from .telecom_expense_management_partner import TelecomExpenseManagementPartner
    from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
    from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration
    from .tenant_app_management_policy import TenantAppManagementPolicy
    from .tenant_attach_r_b_a_c import TenantAttachRBAC
    from .tenant_relationship_access_policy_base import TenantRelationshipAccessPolicyBase
    from .tenant_setup_info import TenantSetupInfo
    from .terms_and_conditions import TermsAndConditions
    from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
    from .terms_and_conditions_assignment import TermsAndConditionsAssignment
    from .terms_and_conditions_group_assignment import TermsAndConditionsGroupAssignment
    from .terms_of_use_container import TermsOfUseContainer
    from .term_store.group import Group
    from .term_store.relation import Relation
    from .term_store.set import Set
    from .term_store.store import Store
    from .term_store.term import Term
    from .text_classification_request import TextClassificationRequest
    from .text_web_part import TextWebPart
    from .threat_assessment_request import ThreatAssessmentRequest
    from .threat_assessment_result import ThreatAssessmentResult
    from .thumbnail_set import ThumbnailSet
    from .time_card import TimeCard
    from .time_off import TimeOff
    from .time_off_reason import TimeOffReason
    from .time_off_request import TimeOffRequest
    from .ti_indicator import TiIndicator
    from .todo import Todo
    from .todo_task import TodoTask
    from .todo_task_list import TodoTaskList
    from .token_issuance_policy import TokenIssuancePolicy
    from .token_lifetime_policy import TokenLifetimePolicy
    from .too_many_global_admins_assigned_to_tenant_alert_configuration import TooManyGlobalAdminsAssignedToTenantAlertConfiguration
    from .too_many_global_admins_assigned_to_tenant_alert_incident import TooManyGlobalAdminsAssignedToTenantAlertIncident
    from .training import Training
    from .training_campaign import TrainingCampaign
    from .training_language_detail import TrainingLanguageDetail
    from .trending import Trending
    from .trusted_certificate_authority_as_entity_base import TrustedCertificateAuthorityAsEntityBase
    from .trust_framework_key_set import TrustFrameworkKeySet
    from .trust_framework_policy import TrustFrameworkPolicy
    from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding
    from .unified_rbac_application import UnifiedRbacApplication
    from .unified_rbac_resource_action import UnifiedRbacResourceAction
    from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
    from .unified_rbac_resource_scope import UnifiedRbacResourceScope
    from .unified_role_assignment import UnifiedRoleAssignment
    from .unified_role_assignment_multiple import UnifiedRoleAssignmentMultiple
    from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
    from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
    from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
    from .unified_role_definition import UnifiedRoleDefinition
    from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
    from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
    from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
    from .unified_role_management_alert import UnifiedRoleManagementAlert
    from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration
    from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition
    from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident
    from .unified_role_management_policy import UnifiedRoleManagementPolicy
    from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
    from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment
    from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
    from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
    from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
    from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule
    from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule
    from .unified_role_schedule_base import UnifiedRoleScheduleBase
    from .unified_role_schedule_instance_base import UnifiedRoleScheduleInstanceBase
    from .unified_storage_quota import UnifiedStorageQuota
    from .unmanaged_device_discovery_task import UnmanagedDeviceDiscoveryTask
    from .unmute_participant_operation import UnmuteParticipantOperation
    from .unsupported_device_configuration import UnsupportedDeviceConfiguration
    from .unsupported_group_policy_extension import UnsupportedGroupPolicyExtension
    from .update_recording_status_operation import UpdateRecordingStatusOperation
    from .url_assessment_request import UrlAssessmentRequest
    from .usage_right import UsageRight
    from .used_insight import UsedInsight
    from .user import User
    from .user_account_information import UserAccountInformation
    from .user_activity import UserActivity
    from .user_analytics import UserAnalytics
    from .user_app_install_status import UserAppInstallStatus
    from .user_consent_request import UserConsentRequest
    from .user_count_metric import UserCountMetric
    from .user_credential_usage_details import UserCredentialUsageDetails
    from .user_experience_analytics_anomaly import UserExperienceAnalyticsAnomaly
    from .user_experience_analytics_anomaly_correlation_group_overview import UserExperienceAnalyticsAnomalyCorrelationGroupOverview
    from .user_experience_analytics_anomaly_device import UserExperienceAnalyticsAnomalyDevice
    from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance
    from .user_experience_analytics_app_health_app_performance_by_app_version import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion
    from .user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
    from .user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
    from .user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
    from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance
    from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance
    from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails
    from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance
    from .user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
    from .user_experience_analytics_battery_health_app_impact import UserExperienceAnalyticsBatteryHealthAppImpact
    from .user_experience_analytics_battery_health_capacity_details import UserExperienceAnalyticsBatteryHealthCapacityDetails
    from .user_experience_analytics_battery_health_device_app_impact import UserExperienceAnalyticsBatteryHealthDeviceAppImpact
    from .user_experience_analytics_battery_health_device_performance import UserExperienceAnalyticsBatteryHealthDevicePerformance
    from .user_experience_analytics_battery_health_device_runtime_history import UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory
    from .user_experience_analytics_battery_health_model_performance import UserExperienceAnalyticsBatteryHealthModelPerformance
    from .user_experience_analytics_battery_health_os_performance import UserExperienceAnalyticsBatteryHealthOsPerformance
    from .user_experience_analytics_battery_health_runtime_details import UserExperienceAnalyticsBatteryHealthRuntimeDetails
    from .user_experience_analytics_category import UserExperienceAnalyticsCategory
    from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance
    from .user_experience_analytics_device_scope import UserExperienceAnalyticsDeviceScope
    from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores
    from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory
    from .user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess
    from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance
    from .user_experience_analytics_device_timeline_event import UserExperienceAnalyticsDeviceTimelineEvent
    from .user_experience_analytics_device_without_cloud_identity import UserExperienceAnalyticsDeviceWithoutCloudIdentity
    from .user_experience_analytics_impacting_process import UserExperienceAnalyticsImpactingProcess
    from .user_experience_analytics_metric import UserExperienceAnalyticsMetric
    from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
    from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
    from .user_experience_analytics_not_autopilot_ready_device import UserExperienceAnalyticsNotAutopilotReadyDevice
    from .user_experience_analytics_overview import UserExperienceAnalyticsOverview
    from .user_experience_analytics_remote_connection import UserExperienceAnalyticsRemoteConnection
    from .user_experience_analytics_resource_performance import UserExperienceAnalyticsResourcePerformance
    from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
    from .user_experience_analytics_work_from_anywhere_device import UserExperienceAnalyticsWorkFromAnywhereDevice
    from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
    from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
    from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
    from .user_flow_language_configuration import UserFlowLanguageConfiguration
    from .user_flow_language_page import UserFlowLanguagePage
    from .user_insights_root import UserInsightsRoot
    from .user_insights_settings import UserInsightsSettings
    from .user_install_state_summary import UserInstallStateSummary
    from .user_p_f_x_certificate import UserPFXCertificate
    from .user_registration_details import UserRegistrationDetails
    from .user_requests_metric import UserRequestsMetric
    from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation
    from .user_security_profile import UserSecurityProfile
    from .user_settings import UserSettings
    from .user_sign_in_insight import UserSignInInsight
    from .user_sign_up_metric import UserSignUpMetric
    from .user_storage import UserStorage
    from .user_teamwork import UserTeamwork
    from .user_virtual_events_root import UserVirtualEventsRoot
    from .vertical_section import VerticalSection
    from .video_news_link_page import VideoNewsLinkPage
    from .virtual_endpoint import VirtualEndpoint
    from .virtual_event import VirtualEvent
    from .virtual_events_root import VirtualEventsRoot
    from .virtual_event_presenter import VirtualEventPresenter
    from .virtual_event_registration import VirtualEventRegistration
    from .virtual_event_registration_configuration import VirtualEventRegistrationConfiguration
    from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion
    from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion
    from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase
    from .virtual_event_session import VirtualEventSession
    from .virtual_event_townhall import VirtualEventTownhall
    from .virtual_event_webinar import VirtualEventWebinar
    from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration
    from .virtual_machine_details import VirtualMachineDetails
    from .virtual_machine_with_aws_storage_bucket_access_finding import VirtualMachineWithAwsStorageBucketAccessFinding
    from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration
    from .voice_authentication_method_target import VoiceAuthenticationMethodTarget
    from .vpn_configuration import VpnConfiguration
    from .vpp_token import VppToken
    from .vulnerable_managed_device import VulnerableManagedDevice
    from .web_account import WebAccount
    from .web_app import WebApp
    from .web_application_segment import WebApplicationSegment
    from .web_part import WebPart
    from .win32_catalog_app import Win32CatalogApp
    from .win32_lob_app import Win32LobApp
    from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage
    from .windows10_certificate_profile_base import Windows10CertificateProfileBase
    from .windows10_compliance_policy import Windows10CompliancePolicy
    from .windows10_custom_configuration import Windows10CustomConfiguration
    from .windows10_device_firmware_configuration_interface import Windows10DeviceFirmwareConfigurationInterface
    from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
    from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
    from .windows10_enrollment_completion_page_configuration import Windows10EnrollmentCompletionPageConfiguration
    from .windows10_enrollment_completion_page_configuration_policy_set_item import Windows10EnrollmentCompletionPageConfigurationPolicySetItem
    from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
    from .windows10_general_configuration import Windows10GeneralConfiguration
    from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
    from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
    from .windows10_network_boundary_configuration import Windows10NetworkBoundaryConfiguration
    from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
    from .windows10_p_f_x_import_certificate_profile import Windows10PFXImportCertificateProfile
    from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
    from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
    from .windows10_vpn_configuration import Windows10VpnConfiguration
    from .windows10_x_certificate_profile import Windows10XCertificateProfile
    from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile
    from .windows10_x_trusted_root_certificate import Windows10XTrustedRootCertificate
    from .windows10_x_vpn_configuration import Windows10XVpnConfiguration
    from .windows10_x_wifi_configuration import Windows10XWifiConfiguration
    from .windows81_certificate_profile_base import Windows81CertificateProfileBase
    from .windows81_compliance_policy import Windows81CompliancePolicy
    from .windows81_general_configuration import Windows81GeneralConfiguration
    from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
    from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
    from .windows81_vpn_configuration import Windows81VpnConfiguration
    from .windows81_wifi_import_configuration import Windows81WifiImportConfiguration
    from .windows_app_x import WindowsAppX
    from .windows_assigned_access_profile import WindowsAssignedAccessProfile
    from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
    from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment
    from .windows_autopilot_deployment_profile_policy_set_item import WindowsAutopilotDeploymentProfilePolicySetItem
    from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
    from .windows_autopilot_settings import WindowsAutopilotSettings
    from .windows_certificate_profile_base import WindowsCertificateProfileBase
    from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
    from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy
    from .windows_defender_application_control_supplemental_policy_assignment import WindowsDefenderApplicationControlSupplementalPolicyAssignment
    from .windows_defender_application_control_supplemental_policy_deployment_status import WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus
    from .windows_defender_application_control_supplemental_policy_deployment_summary import WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary
    from .windows_delivery_optimization_configuration import WindowsDeliveryOptimizationConfiguration
    from .windows_device_malware_state import WindowsDeviceMalwareState
    from .windows_domain_join_configuration import WindowsDomainJoinConfiguration
    from .windows_driver_update_inventory import WindowsDriverUpdateInventory
    from .windows_driver_update_profile import WindowsDriverUpdateProfile
    from .windows_driver_update_profile_assignment import WindowsDriverUpdateProfileAssignment
    from .windows_feature_update_catalog_item import WindowsFeatureUpdateCatalogItem
    from .windows_feature_update_profile import WindowsFeatureUpdateProfile
    from .windows_feature_update_profile_assignment import WindowsFeatureUpdateProfileAssignment
    from .windows_health_monitoring_configuration import WindowsHealthMonitoringConfiguration
    from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod
    from .windows_identity_protection_configuration import WindowsIdentityProtectionConfiguration
    from .windows_information_protection import WindowsInformationProtection
    from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
    from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
    from .windows_information_protection_device_registration import WindowsInformationProtectionDeviceRegistration
    from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
    from .windows_information_protection_policy import WindowsInformationProtectionPolicy
    from .windows_information_protection_wipe_action import WindowsInformationProtectionWipeAction
    from .windows_kiosk_configuration import WindowsKioskConfiguration
    from .windows_malware_information import WindowsMalwareInformation
    from .windows_managed_app_protection import WindowsManagedAppProtection
    from .windows_managed_app_registration import WindowsManagedAppRegistration
    from .windows_managed_device import WindowsManagedDevice
    from .windows_management_app import WindowsManagementApp
    from .windows_management_app_health_state import WindowsManagementAppHealthState
    from .windows_management_app_health_summary import WindowsManagementAppHealthSummary
    from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
    from .windows_mobile_m_s_i import WindowsMobileMSI
    from .windows_phone81_app_x import WindowsPhone81AppX
    from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle
    from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase
    from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy
    from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
    from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
    from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
    from .windows_phone81_store_app import WindowsPhone81StoreApp
    from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile
    from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate
    from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration
    from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration
    from .windows_phone_x_a_p import WindowsPhoneXAP
    from .windows_privacy_data_access_control_item import WindowsPrivacyDataAccessControlItem
    from .windows_protection_state import WindowsProtectionState
    from .windows_quality_update_catalog_item import WindowsQualityUpdateCatalogItem
    from .windows_quality_update_profile import WindowsQualityUpdateProfile
    from .windows_quality_update_profile_assignment import WindowsQualityUpdateProfileAssignment
    from .windows_setting import WindowsSetting
    from .windows_setting_instance import WindowsSettingInstance
    from .windows_store_app import WindowsStoreApp
    from .windows_universal_app_x import WindowsUniversalAppX
    from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp
    from .windows_updates.azure_a_d_device import AzureADDevice
    from .windows_updates.catalog import Catalog
    from .windows_updates.catalog_entry import CatalogEntry
    from .windows_updates.compliance_change import ComplianceChange
    from .windows_updates.content_approval import ContentApproval
    from .windows_updates.deployment import Deployment
    from .windows_updates.deployment_audience import DeploymentAudience
    from .windows_updates.driver_update_catalog_entry import DriverUpdateCatalogEntry
    from .windows_updates.edition import Edition
    from .windows_updates.feature_update_catalog_entry import FeatureUpdateCatalogEntry
    from .windows_updates.knowledge_base_article import KnowledgeBaseArticle
    from .windows_updates.known_issue import KnownIssue
    from .windows_updates.operational_insights_connection import OperationalInsightsConnection
    from .windows_updates.product import Product
    from .windows_updates.product_revision import ProductRevision
    from .windows_updates.quality_update_catalog_entry import QualityUpdateCatalogEntry
    from .windows_updates.resource_connection import ResourceConnection
    from .windows_updates.software_update_catalog_entry import SoftwareUpdateCatalogEntry
    from .windows_updates.updatable_asset import UpdatableAsset
    from .windows_updates.updatable_asset_group import UpdatableAssetGroup
    from .windows_updates.update_policy import UpdatePolicy
    from .windows_update_catalog_item import WindowsUpdateCatalogItem
    from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
    from .windows_update_state import WindowsUpdateState
    from .windows_vpn_configuration import WindowsVpnConfiguration
    from .windows_web_app import WindowsWebApp
    from .windows_wifi_configuration import WindowsWifiConfiguration
    from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
    from .windows_wired_network_configuration import WindowsWiredNetworkConfiguration
    from .win_get_app import WinGetApp
    from .workbook import Workbook
    from .workbook_application import WorkbookApplication
    from .workbook_chart import WorkbookChart
    from .workbook_chart_area_format import WorkbookChartAreaFormat
    from .workbook_chart_axes import WorkbookChartAxes
    from .workbook_chart_axis import WorkbookChartAxis
    from .workbook_chart_axis_format import WorkbookChartAxisFormat
    from .workbook_chart_axis_title import WorkbookChartAxisTitle
    from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat
    from .workbook_chart_data_labels import WorkbookChartDataLabels
    from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat
    from .workbook_chart_fill import WorkbookChartFill
    from .workbook_chart_font import WorkbookChartFont
    from .workbook_chart_gridlines import WorkbookChartGridlines
    from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat
    from .workbook_chart_legend import WorkbookChartLegend
    from .workbook_chart_legend_format import WorkbookChartLegendFormat
    from .workbook_chart_line_format import WorkbookChartLineFormat
    from .workbook_chart_point import WorkbookChartPoint
    from .workbook_chart_point_format import WorkbookChartPointFormat
    from .workbook_chart_series import WorkbookChartSeries
    from .workbook_chart_series_format import WorkbookChartSeriesFormat
    from .workbook_chart_title import WorkbookChartTitle
    from .workbook_chart_title_format import WorkbookChartTitleFormat
    from .workbook_comment import WorkbookComment
    from .workbook_comment_reply import WorkbookCommentReply
    from .workbook_document_task import WorkbookDocumentTask
    from .workbook_document_task_change import WorkbookDocumentTaskChange
    from .workbook_filter import WorkbookFilter
    from .workbook_format_protection import WorkbookFormatProtection
    from .workbook_functions import WorkbookFunctions
    from .workbook_function_result import WorkbookFunctionResult
    from .workbook_named_item import WorkbookNamedItem
    from .workbook_operation import WorkbookOperation
    from .workbook_pivot_table import WorkbookPivotTable
    from .workbook_range import WorkbookRange
    from .workbook_range_border import WorkbookRangeBorder
    from .workbook_range_fill import WorkbookRangeFill
    from .workbook_range_font import WorkbookRangeFont
    from .workbook_range_format import WorkbookRangeFormat
    from .workbook_range_sort import WorkbookRangeSort
    from .workbook_range_view import WorkbookRangeView
    from .workbook_table import WorkbookTable
    from .workbook_table_column import WorkbookTableColumn
    from .workbook_table_row import WorkbookTableRow
    from .workbook_table_sort import WorkbookTableSort
    from .workbook_worksheet import WorkbookWorksheet
    from .workbook_worksheet_protection import WorkbookWorksheetProtection
    from .workforce_integration import WorkforceIntegration
    from .workplace_sensor_device import WorkplaceSensorDevice
    from .workspace import Workspace
    from .work_position import WorkPosition
    from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration
    from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration
    from .zebra_fota_artifact import ZebraFotaArtifact
    from .zebra_fota_connector import ZebraFotaConnector
    from .zebra_fota_deployment import ZebraFotaDeployment

@dataclass
class Entity(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The unique identifier for an entity. Read-only.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Entity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Entity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aadUserConversationMember".casefold():
            from .aad_user_conversation_member import AadUserConversationMember

            return AadUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackage".casefold():
            from .access_package import AccessPackage

            return AccessPackage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignment".casefold():
            from .access_package_assignment import AccessPackageAssignment

            return AccessPackageAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentPolicy".casefold():
            from .access_package_assignment_policy import AccessPackageAssignmentPolicy

            return AccessPackageAssignmentPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentRequest".casefold():
            from .access_package_assignment_request import AccessPackageAssignmentRequest

            return AccessPackageAssignmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentRequestWorkflowExtension".casefold():
            from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension

            return AccessPackageAssignmentRequestWorkflowExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentResourceRole".casefold():
            from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole

            return AccessPackageAssignmentResourceRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentWorkflowExtension".casefold():
            from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension

            return AccessPackageAssignmentWorkflowExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageCatalog".casefold():
            from .access_package_catalog import AccessPackageCatalog

            return AccessPackageCatalog()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageResource".casefold():
            from .access_package_resource import AccessPackageResource

            return AccessPackageResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageResourceEnvironment".casefold():
            from .access_package_resource_environment import AccessPackageResourceEnvironment

            return AccessPackageResourceEnvironment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageResourceRequest".casefold():
            from .access_package_resource_request import AccessPackageResourceRequest

            return AccessPackageResourceRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageResourceRole".casefold():
            from .access_package_resource_role import AccessPackageResourceRole

            return AccessPackageResourceRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageResourceRoleScope".casefold():
            from .access_package_resource_role_scope import AccessPackageResourceRoleScope

            return AccessPackageResourceRoleScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageResourceScope".casefold():
            from .access_package_resource_scope import AccessPackageResourceScope

            return AccessPackageResourceScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageSubject".casefold():
            from .access_package_subject import AccessPackageSubject

            return AccessPackageSubject()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReview".casefold():
            from .access_review import AccessReview

            return AccessReview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewDecision".casefold():
            from .access_review_decision import AccessReviewDecision

            return AccessReviewDecision()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewHistoryDefinition".casefold():
            from .access_review_history_definition import AccessReviewHistoryDefinition

            return AccessReviewHistoryDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewHistoryInstance".casefold():
            from .access_review_history_instance import AccessReviewHistoryInstance

            return AccessReviewHistoryInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInstance".casefold():
            from .access_review_instance import AccessReviewInstance

            return AccessReviewInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInstanceDecisionItem".casefold():
            from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem

            return AccessReviewInstanceDecisionItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewPolicy".casefold():
            from .access_review_policy import AccessReviewPolicy

            return AccessReviewPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewReviewer".casefold():
            from .access_review_reviewer import AccessReviewReviewer

            return AccessReviewReviewer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewScheduleDefinition".casefold():
            from .access_review_schedule_definition import AccessReviewScheduleDefinition

            return AccessReviewScheduleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewSet".casefold():
            from .access_review_set import AccessReviewSet

            return AccessReviewSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewStage".casefold():
            from .access_review_stage import AccessReviewStage

            return AccessReviewStage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activeDirectoryWindowsAutopilotDeploymentProfile".casefold():
            from .active_directory_windows_autopilot_deployment_profile import ActiveDirectoryWindowsAutopilotDeploymentProfile

            return ActiveDirectoryWindowsAutopilotDeploymentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activeUsersBreakdownMetric".casefold():
            from .active_users_breakdown_metric import ActiveUsersBreakdownMetric

            return ActiveUsersBreakdownMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activeUsersMetric".casefold():
            from .active_users_metric import ActiveUsersMetric

            return ActiveUsersMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activityBasedTimeoutPolicy".casefold():
            from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy

            return ActivityBasedTimeoutPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activityHistoryItem".casefold():
            from .activity_history_item import ActivityHistoryItem

            return ActivityHistoryItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activityStatistics".casefold():
            from .activity_statistics import ActivityStatistics

            return ActivityStatistics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addLargeGalleryViewOperation".casefold():
            from .add_large_gallery_view_operation import AddLargeGalleryViewOperation

            return AddLargeGalleryViewOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adminAppsAndServices".casefold():
            from .admin_apps_and_services import AdminAppsAndServices

            return AdminAppsAndServices()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adminConsentRequestPolicy".casefold():
            from .admin_consent_request_policy import AdminConsentRequestPolicy

            return AdminConsentRequestPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adminDynamics".casefold():
            from .admin_dynamics import AdminDynamics

            return AdminDynamics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adminForms".casefold():
            from .admin_forms import AdminForms

            return AdminForms()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.administrativeUnit".casefold():
            from .administrative_unit import AdministrativeUnit

            return AdministrativeUnit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adminMicrosoft365Apps".casefold():
            from .admin_microsoft365_apps import AdminMicrosoft365Apps

            return AdminMicrosoft365Apps()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adminReportSettings".casefold():
            from .admin_report_settings import AdminReportSettings

            return AdminReportSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adminTodo".casefold():
            from .admin_todo import AdminTodo

            return AdminTodo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adminWindows".casefold():
            from .admin_windows import AdminWindows

            return AdminWindows()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adminWindowsUpdates".casefold():
            from .admin_windows_updates import AdminWindowsUpdates

            return AdminWindowsUpdates()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.advancedThreatProtectionOnboardingDeviceSettingState".casefold():
            from .advanced_threat_protection_onboarding_device_setting_state import AdvancedThreatProtectionOnboardingDeviceSettingState

            return AdvancedThreatProtectionOnboardingDeviceSettingState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.advancedThreatProtectionOnboardingStateSummary".casefold():
            from .advanced_threat_protection_onboarding_state_summary import AdvancedThreatProtectionOnboardingStateSummary

            return AdvancedThreatProtectionOnboardingStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreement".casefold():
            from .agreement import Agreement

            return Agreement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementAcceptance".casefold():
            from .agreement_acceptance import AgreementAcceptance

            return AgreementAcceptance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFile".casefold():
            from .agreement_file import AgreementFile

            return AgreementFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFileLocalization".casefold():
            from .agreement_file_localization import AgreementFileLocalization

            return AgreementFileLocalization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFileProperties".casefold():
            from .agreement_file_properties import AgreementFileProperties

            return AgreementFileProperties()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFileVersion".casefold():
            from .agreement_file_version import AgreementFileVersion

            return AgreementFileVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.alert".casefold():
            from .alert import Alert
            from .networkaccess.alert import Alert
            from .security.alert import Alert

            return Alert()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.allowedDataLocation".casefold():
            from .allowed_data_location import AllowedDataLocation

            return AllowedDataLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.allowedValue".casefold():
            from .allowed_value import AllowedValue

            return AllowedValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCertificateProfileBase".casefold():
            from .android_certificate_profile_base import AndroidCertificateProfileBase

            return AndroidCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCompliancePolicy".casefold():
            from .android_compliance_policy import AndroidCompliancePolicy

            return AndroidCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCustomConfiguration".casefold():
            from .android_custom_configuration import AndroidCustomConfiguration

            return AndroidCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceComplianceLocalActionBase".casefold():
            from .android_device_compliance_local_action_base import AndroidDeviceComplianceLocalActionBase

            return AndroidDeviceComplianceLocalActionBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceComplianceLocalActionLockDevice".casefold():
            from .android_device_compliance_local_action_lock_device import AndroidDeviceComplianceLocalActionLockDevice

            return AndroidDeviceComplianceLocalActionLockDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceComplianceLocalActionLockDeviceWithPasscode".casefold():
            from .android_device_compliance_local_action_lock_device_with_passcode import AndroidDeviceComplianceLocalActionLockDeviceWithPasscode

            return AndroidDeviceComplianceLocalActionLockDeviceWithPasscode()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerCertificateProfileBase".casefold():
            from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase

            return AndroidDeviceOwnerCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerCompliancePolicy".casefold():
            from .android_device_owner_compliance_policy import AndroidDeviceOwnerCompliancePolicy

            return AndroidDeviceOwnerCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerDerivedCredentialAuthenticationConfiguration".casefold():
            from .android_device_owner_derived_credential_authentication_configuration import AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration

            return AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerEnrollmentProfile".casefold():
            from .android_device_owner_enrollment_profile import AndroidDeviceOwnerEnrollmentProfile

            return AndroidDeviceOwnerEnrollmentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerEnterpriseWiFiConfiguration".casefold():
            from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration

            return AndroidDeviceOwnerEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerGeneralDeviceConfiguration".casefold():
            from .android_device_owner_general_device_configuration import AndroidDeviceOwnerGeneralDeviceConfiguration

            return AndroidDeviceOwnerGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerImportedPFXCertificateProfile".casefold():
            from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile

            return AndroidDeviceOwnerImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerPkcsCertificateProfile".casefold():
            from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile

            return AndroidDeviceOwnerPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerScepCertificateProfile".casefold():
            from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile

            return AndroidDeviceOwnerScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerTrustedRootCertificate".casefold():
            from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate

            return AndroidDeviceOwnerTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerVpnConfiguration".casefold():
            from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration

            return AndroidDeviceOwnerVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerWiFiConfiguration".casefold():
            from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration

            return AndroidDeviceOwnerWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidEasEmailProfileConfiguration".casefold():
            from .android_eas_email_profile_configuration import AndroidEasEmailProfileConfiguration

            return AndroidEasEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidEnterpriseWiFiConfiguration".casefold():
            from .android_enterprise_wi_fi_configuration import AndroidEnterpriseWiFiConfiguration

            return AndroidEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkApp".casefold():
            from .android_for_work_app import AndroidForWorkApp

            return AndroidForWorkApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkAppConfigurationSchema".casefold():
            from .android_for_work_app_configuration_schema import AndroidForWorkAppConfigurationSchema

            return AndroidForWorkAppConfigurationSchema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkCertificateProfileBase".casefold():
            from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase

            return AndroidForWorkCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkCompliancePolicy".casefold():
            from .android_for_work_compliance_policy import AndroidForWorkCompliancePolicy

            return AndroidForWorkCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkCustomConfiguration".casefold():
            from .android_for_work_custom_configuration import AndroidForWorkCustomConfiguration

            return AndroidForWorkCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkEasEmailProfileBase".casefold():
            from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase

            return AndroidForWorkEasEmailProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkEnrollmentProfile".casefold():
            from .android_for_work_enrollment_profile import AndroidForWorkEnrollmentProfile

            return AndroidForWorkEnrollmentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkEnterpriseWiFiConfiguration".casefold():
            from .android_for_work_enterprise_wi_fi_configuration import AndroidForWorkEnterpriseWiFiConfiguration

            return AndroidForWorkEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkGeneralDeviceConfiguration".casefold():
            from .android_for_work_general_device_configuration import AndroidForWorkGeneralDeviceConfiguration

            return AndroidForWorkGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkGmailEasConfiguration".casefold():
            from .android_for_work_gmail_eas_configuration import AndroidForWorkGmailEasConfiguration

            return AndroidForWorkGmailEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkImportedPFXCertificateProfile".casefold():
            from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile

            return AndroidForWorkImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkMobileAppConfiguration".casefold():
            from .android_for_work_mobile_app_configuration import AndroidForWorkMobileAppConfiguration

            return AndroidForWorkMobileAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkNineWorkEasConfiguration".casefold():
            from .android_for_work_nine_work_eas_configuration import AndroidForWorkNineWorkEasConfiguration

            return AndroidForWorkNineWorkEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkPkcsCertificateProfile".casefold():
            from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile

            return AndroidForWorkPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkScepCertificateProfile".casefold():
            from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile

            return AndroidForWorkScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkSettings".casefold():
            from .android_for_work_settings import AndroidForWorkSettings

            return AndroidForWorkSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkTrustedRootCertificate".casefold():
            from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate

            return AndroidForWorkTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkVpnConfiguration".casefold():
            from .android_for_work_vpn_configuration import AndroidForWorkVpnConfiguration

            return AndroidForWorkVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkWiFiConfiguration".casefold():
            from .android_for_work_wi_fi_configuration import AndroidForWorkWiFiConfiguration

            return AndroidForWorkWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidGeneralDeviceConfiguration".casefold():
            from .android_general_device_configuration import AndroidGeneralDeviceConfiguration

            return AndroidGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidImportedPFXCertificateProfile".casefold():
            from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile

            return AndroidImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidLobApp".casefold():
            from .android_lob_app import AndroidLobApp

            return AndroidLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedAppProtection".casefold():
            from .android_managed_app_protection import AndroidManagedAppProtection

            return AndroidManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedAppRegistration".casefold():
            from .android_managed_app_registration import AndroidManagedAppRegistration

            return AndroidManagedAppRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedStoreAccountEnterpriseSettings".casefold():
            from .android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings

            return AndroidManagedStoreAccountEnterpriseSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedStoreApp".casefold():
            from .android_managed_store_app import AndroidManagedStoreApp

            return AndroidManagedStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedStoreAppConfiguration".casefold():
            from .android_managed_store_app_configuration import AndroidManagedStoreAppConfiguration

            return AndroidManagedStoreAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedStoreAppConfigurationSchema".casefold():
            from .android_managed_store_app_configuration_schema import AndroidManagedStoreAppConfigurationSchema

            return AndroidManagedStoreAppConfigurationSchema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedStoreWebApp".casefold():
            from .android_managed_store_web_app import AndroidManagedStoreWebApp

            return AndroidManagedStoreWebApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidOmaCpConfiguration".casefold():
            from .android_oma_cp_configuration import AndroidOmaCpConfiguration

            return AndroidOmaCpConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidPkcsCertificateProfile".casefold():
            from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile

            return AndroidPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidScepCertificateProfile".casefold():
            from .android_scep_certificate_profile import AndroidScepCertificateProfile

            return AndroidScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidStoreApp".casefold():
            from .android_store_app import AndroidStoreApp

            return AndroidStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidTrustedRootCertificate".casefold():
            from .android_trusted_root_certificate import AndroidTrustedRootCertificate

            return AndroidTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidVpnConfiguration".casefold():
            from .android_vpn_configuration import AndroidVpnConfiguration

            return AndroidVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWiFiConfiguration".casefold():
            from .android_wi_fi_configuration import AndroidWiFiConfiguration

            return AndroidWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCertificateProfileBase".casefold():
            from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase

            return AndroidWorkProfileCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCompliancePolicy".casefold():
            from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy

            return AndroidWorkProfileCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCustomConfiguration".casefold():
            from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration

            return AndroidWorkProfileCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileEasEmailProfileBase".casefold():
            from .android_work_profile_eas_email_profile_base import AndroidWorkProfileEasEmailProfileBase

            return AndroidWorkProfileEasEmailProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileEnterpriseWiFiConfiguration".casefold():
            from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration

            return AndroidWorkProfileEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration".casefold():
            from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration

            return AndroidWorkProfileGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileGmailEasConfiguration".casefold():
            from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration

            return AndroidWorkProfileGmailEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileNineWorkEasConfiguration".casefold():
            from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration

            return AndroidWorkProfileNineWorkEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfilePkcsCertificateProfile".casefold():
            from .android_work_profile_pkcs_certificate_profile import AndroidWorkProfilePkcsCertificateProfile

            return AndroidWorkProfilePkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileScepCertificateProfile".casefold():
            from .android_work_profile_scep_certificate_profile import AndroidWorkProfileScepCertificateProfile

            return AndroidWorkProfileScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileTrustedRootCertificate".casefold():
            from .android_work_profile_trusted_root_certificate import AndroidWorkProfileTrustedRootCertificate

            return AndroidWorkProfileTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileVpnConfiguration".casefold():
            from .android_work_profile_vpn_configuration import AndroidWorkProfileVpnConfiguration

            return AndroidWorkProfileVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileWiFiConfiguration".casefold():
            from .android_work_profile_wi_fi_configuration import AndroidWorkProfileWiFiConfiguration

            return AndroidWorkProfileWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.anonymousGuestConversationMember".casefold():
            from .anonymous_guest_conversation_member import AnonymousGuestConversationMember

            return AnonymousGuestConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerCertificateProfileBase".casefold():
            from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase

            return AospDeviceOwnerCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerCompliancePolicy".casefold():
            from .aosp_device_owner_compliance_policy import AospDeviceOwnerCompliancePolicy

            return AospDeviceOwnerCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerDeviceConfiguration".casefold():
            from .aosp_device_owner_device_configuration import AospDeviceOwnerDeviceConfiguration

            return AospDeviceOwnerDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerEnterpriseWiFiConfiguration".casefold():
            from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration

            return AospDeviceOwnerEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerPkcsCertificateProfile".casefold():
            from .aosp_device_owner_pkcs_certificate_profile import AospDeviceOwnerPkcsCertificateProfile

            return AospDeviceOwnerPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerScepCertificateProfile".casefold():
            from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile

            return AospDeviceOwnerScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerTrustedRootCertificate".casefold():
            from .aosp_device_owner_trusted_root_certificate import AospDeviceOwnerTrustedRootCertificate

            return AospDeviceOwnerTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerWiFiConfiguration".casefold():
            from .aosp_device_owner_wi_fi_configuration import AospDeviceOwnerWiFiConfiguration

            return AospDeviceOwnerWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConsentApprovalRoute".casefold():
            from .app_consent_approval_route import AppConsentApprovalRoute

            return AppConsentApprovalRoute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConsentRequest".casefold():
            from .app_consent_request import AppConsentRequest

            return AppConsentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appCredentialSignInActivity".casefold():
            from .app_credential_sign_in_activity import AppCredentialSignInActivity

            return AppCredentialSignInActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleDeviceFeaturesConfigurationBase".casefold():
            from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase

            return AppleDeviceFeaturesConfigurationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleEnrollmentProfileAssignment".casefold():
            from .apple_enrollment_profile_assignment import AppleEnrollmentProfileAssignment

            return AppleEnrollmentProfileAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleExpeditedCheckinConfigurationBase".casefold():
            from .apple_expedited_checkin_configuration_base import AppleExpeditedCheckinConfigurationBase

            return AppleExpeditedCheckinConfigurationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleManagedIdentityProvider".casefold():
            from .apple_managed_identity_provider import AppleManagedIdentityProvider

            return AppleManagedIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.applePushNotificationCertificate".casefold():
            from .apple_push_notification_certificate import ApplePushNotificationCertificate

            return ApplePushNotificationCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleUserInitiatedEnrollmentProfile".casefold():
            from .apple_user_initiated_enrollment_profile import AppleUserInitiatedEnrollmentProfile

            return AppleUserInitiatedEnrollmentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleVpnConfiguration".casefold():
            from .apple_vpn_configuration import AppleVpnConfiguration

            return AppleVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleVppTokenTroubleshootingEvent".casefold():
            from .apple_vpp_token_troubleshooting_event import AppleVppTokenTroubleshootingEvent

            return AppleVppTokenTroubleshootingEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.application".casefold():
            from .application import Application

            return Application()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.applicationSegment".casefold():
            from .application_segment import ApplicationSegment

            return ApplicationSegment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.applicationSignInDetailedSummary".casefold():
            from .application_sign_in_detailed_summary import ApplicationSignInDetailedSummary

            return ApplicationSignInDetailedSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.applicationSignInSummary".casefold():
            from .application_sign_in_summary import ApplicationSignInSummary

            return ApplicationSignInSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.applicationTemplate".casefold():
            from .application_template import ApplicationTemplate

            return ApplicationTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appLogCollectionRequest".casefold():
            from .app_log_collection_request import AppLogCollectionRequest

            return AppLogCollectionRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appManagementPolicy".casefold():
            from .app_management_policy import AppManagementPolicy

            return AppManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appRoleAssignment".casefold():
            from .app_role_assignment import AppRoleAssignment

            return AppRoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.approval".casefold():
            from .approval import Approval

            return Approval()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.approvalStep".casefold():
            from .approval_step import ApprovalStep

            return ApprovalStep()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.approvalWorkflowProvider".casefold():
            from .approval_workflow_provider import ApprovalWorkflowProvider

            return ApprovalWorkflowProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appScope".casefold():
            from .app_scope import AppScope

            return AppScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appVulnerabilityManagedDevice".casefold():
            from .app_vulnerability_managed_device import AppVulnerabilityManagedDevice

            return AppVulnerabilityManagedDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appVulnerabilityMobileApp".casefold():
            from .app_vulnerability_mobile_app import AppVulnerabilityMobileApp

            return AppVulnerabilityMobileApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appVulnerabilityTask".casefold():
            from .app_vulnerability_task import AppVulnerabilityTask

            return AppVulnerabilityTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.assignedComputeInstanceDetails".casefold():
            from .assigned_compute_instance_details import AssignedComputeInstanceDetails

            return AssignedComputeInstanceDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.assignmentFilterEvaluationStatusDetails".casefold():
            from .assignment_filter_evaluation_status_details import AssignmentFilterEvaluationStatusDetails

            return AssignmentFilterEvaluationStatusDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.associatedTeamInfo".casefold():
            from .associated_team_info import AssociatedTeamInfo

            return AssociatedTeamInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attachment".casefold():
            from .attachment import Attachment

            return Attachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attachmentBase".casefold():
            from .attachment_base import AttachmentBase

            return AttachmentBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attachmentSession".casefold():
            from .attachment_session import AttachmentSession

            return AttachmentSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attackSimulationOperation".casefold():
            from .attack_simulation_operation import AttackSimulationOperation

            return AttackSimulationOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attackSimulationRoot".casefold():
            from .attack_simulation_root import AttackSimulationRoot

            return AttackSimulationRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attendanceRecord".casefold():
            from .attendance_record import AttendanceRecord

            return AttendanceRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attributeMappingFunctionSchema".casefold():
            from .attribute_mapping_function_schema import AttributeMappingFunctionSchema

            return AttributeMappingFunctionSchema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attributeSet".casefold():
            from .attribute_set import AttributeSet

            return AttributeSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.audioRoutingGroup".casefold():
            from .audio_routing_group import AudioRoutingGroup

            return AudioRoutingGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.auditEvent".casefold():
            from .audit_event import AuditEvent
            from .managed_tenants.audit_event import AuditEvent

            return AuditEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authentication".casefold():
            from .authentication import Authentication

            return Authentication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationCombinationConfiguration".casefold():
            from .authentication_combination_configuration import AuthenticationCombinationConfiguration

            return AuthenticationCombinationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationContextClassReference".casefold():
            from .authentication_context_class_reference import AuthenticationContextClassReference

            return AuthenticationContextClassReference()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationEventListener".casefold():
            from .authentication_event_listener import AuthenticationEventListener

            return AuthenticationEventListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationEventsFlow".casefold():
            from .authentication_events_flow import AuthenticationEventsFlow

            return AuthenticationEventsFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationEventsPolicy".casefold():
            from .authentication_events_policy import AuthenticationEventsPolicy

            return AuthenticationEventsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationFlowsPolicy".casefold():
            from .authentication_flows_policy import AuthenticationFlowsPolicy

            return AuthenticationFlowsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationListener".casefold():
            from .authentication_listener import AuthenticationListener

            return AuthenticationListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethod".casefold():
            from .authentication_method import AuthenticationMethod

            return AuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodConfiguration".casefold():
            from .authentication_method_configuration import AuthenticationMethodConfiguration

            return AuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodModeDetail".casefold():
            from .authentication_method_mode_detail import AuthenticationMethodModeDetail

            return AuthenticationMethodModeDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodsPolicy".casefold():
            from .authentication_methods_policy import AuthenticationMethodsPolicy

            return AuthenticationMethodsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodsRoot".casefold():
            from .authentication_methods_root import AuthenticationMethodsRoot

            return AuthenticationMethodsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodTarget".casefold():
            from .authentication_method_target import AuthenticationMethodTarget

            return AuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationsMetric".casefold():
            from .authentications_metric import AuthenticationsMetric

            return AuthenticationsMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationStrengthPolicy".casefold():
            from .authentication_strength_policy import AuthenticationStrengthPolicy

            return AuthenticationStrengthPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationStrengthRoot".casefold():
            from .authentication_strength_root import AuthenticationStrengthRoot

            return AuthenticationStrengthRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authoredNote".casefold():
            from .authored_note import AuthoredNote

            return AuthoredNote()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authorizationPolicy".casefold():
            from .authorization_policy import AuthorizationPolicy

            return AuthorizationPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authorizationSystem".casefold():
            from .authorization_system import AuthorizationSystem

            return AuthorizationSystem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authorizationSystemIdentity".casefold():
            from .authorization_system_identity import AuthorizationSystemIdentity

            return AuthorizationSystemIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authorizationSystemResource".casefold():
            from .authorization_system_resource import AuthorizationSystemResource

            return AuthorizationSystemResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authorizationSystemTypeAction".casefold():
            from .authorization_system_type_action import AuthorizationSystemTypeAction

            return AuthorizationSystemTypeAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authorizationSystemTypeService".casefold():
            from .authorization_system_type_service import AuthorizationSystemTypeService

            return AuthorizationSystemTypeService()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsAccessKey".casefold():
            from .aws_access_key import AwsAccessKey

            return AwsAccessKey()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsAuthorizationSystem".casefold():
            from .aws_authorization_system import AwsAuthorizationSystem

            return AwsAuthorizationSystem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsAuthorizationSystemResource".casefold():
            from .aws_authorization_system_resource import AwsAuthorizationSystemResource

            return AwsAuthorizationSystemResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsAuthorizationSystemTypeAction".casefold():
            from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction

            return AwsAuthorizationSystemTypeAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsEc2Instance".casefold():
            from .aws_ec2_instance import AwsEc2Instance

            return AwsEc2Instance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsExternalSystemAccessFinding".casefold():
            from .aws_external_system_access_finding import AwsExternalSystemAccessFinding

            return AwsExternalSystemAccessFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsExternalSystemAccessRoleFinding".casefold():
            from .aws_external_system_access_role_finding import AwsExternalSystemAccessRoleFinding

            return AwsExternalSystemAccessRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsGroup".casefold():
            from .aws_group import AwsGroup

            return AwsGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsIdentity".casefold():
            from .aws_identity import AwsIdentity

            return AwsIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsIdentityAccessManagementKeyAgeFinding".casefold():
            from .aws_identity_access_management_key_age_finding import AwsIdentityAccessManagementKeyAgeFinding

            return AwsIdentityAccessManagementKeyAgeFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsIdentityAccessManagementKeyUsageFinding".casefold():
            from .aws_identity_access_management_key_usage_finding import AwsIdentityAccessManagementKeyUsageFinding

            return AwsIdentityAccessManagementKeyUsageFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsLambda".casefold():
            from .aws_lambda import AwsLambda

            return AwsLambda()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsPolicy".casefold():
            from .aws_policy import AwsPolicy

            return AwsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsRole".casefold():
            from .aws_role import AwsRole

            return AwsRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsSecretInformationAccessFinding".casefold():
            from .aws_secret_information_access_finding import AwsSecretInformationAccessFinding

            return AwsSecretInformationAccessFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsSecurityToolAdministrationFinding".casefold():
            from .aws_security_tool_administration_finding import AwsSecurityToolAdministrationFinding

            return AwsSecurityToolAdministrationFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsUser".casefold():
            from .aws_user import AwsUser

            return AwsUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureADAuthentication".casefold():
            from .azure_a_d_authentication import AzureADAuthentication

            return AzureADAuthentication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureADWindowsAutopilotDeploymentProfile".casefold():
            from .azure_a_d_windows_autopilot_deployment_profile import AzureADWindowsAutopilotDeploymentProfile

            return AzureADWindowsAutopilotDeploymentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureAuthorizationSystem".casefold():
            from .azure_authorization_system import AzureAuthorizationSystem

            return AzureAuthorizationSystem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureAuthorizationSystemResource".casefold():
            from .azure_authorization_system_resource import AzureAuthorizationSystemResource

            return AzureAuthorizationSystemResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureAuthorizationSystemTypeAction".casefold():
            from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction

            return AzureAuthorizationSystemTypeAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureCommunicationServicesUserConversationMember".casefold():
            from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember

            return AzureCommunicationServicesUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureGroup".casefold():
            from .azure_group import AzureGroup

            return AzureGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureIdentity".casefold():
            from .azure_identity import AzureIdentity

            return AzureIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureManagedIdentity".casefold():
            from .azure_managed_identity import AzureManagedIdentity

            return AzureManagedIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureRoleDefinition".casefold():
            from .azure_role_definition import AzureRoleDefinition

            return AzureRoleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureServerlessFunction".casefold():
            from .azure_serverless_function import AzureServerlessFunction

            return AzureServerlessFunction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureServicePrincipal".casefold():
            from .azure_service_principal import AzureServicePrincipal

            return AzureServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureUser".casefold():
            from .azure_user import AzureUser

            return AzureUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.b2cAuthenticationMethodsPolicy".casefold():
            from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicy

            return B2cAuthenticationMethodsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.b2cIdentityUserFlow".casefold():
            from .b2c_identity_user_flow import B2cIdentityUserFlow

            return B2cIdentityUserFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.b2xIdentityUserFlow".casefold():
            from .b2x_identity_user_flow import B2xIdentityUserFlow

            return B2xIdentityUserFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.baseItem".casefold():
            from .base_item import BaseItem

            return BaseItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.baseItemVersion".casefold():
            from .base_item_version import BaseItemVersion

            return BaseItemVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.baseSitePage".casefold():
            from .base_site_page import BaseSitePage

            return BaseSitePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bitlocker".casefold():
            from .bitlocker import Bitlocker

            return Bitlocker()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bitlockerRecoveryKey".casefold():
            from .bitlocker_recovery_key import BitlockerRecoveryKey

            return BitlockerRecoveryKey()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingAppointment".casefold():
            from .booking_appointment import BookingAppointment

            return BookingAppointment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingBusiness".casefold():
            from .booking_business import BookingBusiness

            return BookingBusiness()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCurrency".casefold():
            from .booking_currency import BookingCurrency

            return BookingCurrency()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCustomer".casefold():
            from .booking_customer import BookingCustomer

            return BookingCustomer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCustomQuestion".casefold():
            from .booking_custom_question import BookingCustomQuestion

            return BookingCustomQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingNamedEntity".casefold():
            from .booking_named_entity import BookingNamedEntity

            return BookingNamedEntity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingPerson".casefold():
            from .booking_person import BookingPerson

            return BookingPerson()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingService".casefold():
            from .booking_service import BookingService

            return BookingService()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingStaffMember".casefold():
            from .booking_staff_member import BookingStaffMember

            return BookingStaffMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.browserSharedCookie".casefold():
            from .browser_shared_cookie import BrowserSharedCookie

            return BrowserSharedCookie()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.browserSite".casefold():
            from .browser_site import BrowserSite

            return BrowserSite()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.browserSiteList".casefold():
            from .browser_site_list import BrowserSiteList

            return BrowserSiteList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.builtInIdentityProvider".casefold():
            from .built_in_identity_provider import BuiltInIdentityProvider

            return BuiltInIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bulkUpload".casefold():
            from .bulk_upload import BulkUpload

            return BulkUpload()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.businessFlow".casefold():
            from .business_flow import BusinessFlow

            return BusinessFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.businessFlowTemplate".casefold():
            from .business_flow_template import BusinessFlowTemplate

            return BusinessFlowTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.businessScenario".casefold():
            from .business_scenario import BusinessScenario

            return BusinessScenario()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.businessScenarioPlanner".casefold():
            from .business_scenario_planner import BusinessScenarioPlanner

            return BusinessScenarioPlanner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.businessScenarioPlanReference".casefold():
            from .business_scenario_plan_reference import BusinessScenarioPlanReference

            return BusinessScenarioPlanReference()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.businessScenarioTask".casefold():
            from .business_scenario_task import BusinessScenarioTask

            return BusinessScenarioTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendar".casefold():
            from .calendar import Calendar

            return Calendar()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendarGroup".casefold():
            from .calendar_group import CalendarGroup

            return CalendarGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendarPermission".casefold():
            from .calendar_permission import CalendarPermission

            return CalendarPermission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendarSharingMessage".casefold():
            from .calendar_sharing_message import CalendarSharingMessage

            return CalendarSharingMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.call".casefold():
            from .call import Call

            return Call()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callActivityStatistics".casefold():
            from .call_activity_statistics import CallActivityStatistics

            return CallActivityStatistics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callEvent".casefold():
            from .call_event import CallEvent

            return CallEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecording".casefold():
            from .call_recording import CallRecording

            return CallRecording()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.callRecord".casefold():
            from .call_records.call_record import CallRecord

            return CallRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.organizer".casefold():
            from .call_records.organizer import Organizer

            return Organizer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.participant".casefold():
            from .call_records.participant import Participant
            from .participant import Participant

            return Participant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.participantBase".casefold():
            from .call_records.participant_base import ParticipantBase

            return ParticipantBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.segment".casefold():
            from .call_records.segment import Segment

            return Segment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.session".casefold():
            from .call_records.session import Session

            return Session()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callTranscript".casefold():
            from .call_transcript import CallTranscript

            return CallTranscript()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cancelMediaProcessingOperation".casefold():
            from .cancel_media_processing_operation import CancelMediaProcessingOperation

            return CancelMediaProcessingOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.canvasLayout".casefold():
            from .canvas_layout import CanvasLayout

            return CanvasLayout()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cartToClassAssociation".casefold():
            from .cart_to_class_association import CartToClassAssociation

            return CartToClassAssociation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.certificateAuthorityAsEntity".casefold():
            from .certificate_authority_as_entity import CertificateAuthorityAsEntity

            return CertificateAuthorityAsEntity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.certificateAuthorityPath".casefold():
            from .certificate_authority_path import CertificateAuthorityPath

            return CertificateAuthorityPath()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.certificateBasedApplicationConfiguration".casefold():
            from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration

            return CertificateBasedApplicationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.certificateBasedAuthConfiguration".casefold():
            from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration

            return CertificateBasedAuthConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.certificateConnectorDetails".casefold():
            from .certificate_connector_details import CertificateConnectorDetails

            return CertificateConnectorDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.changeTrackedEntity".casefold():
            from .change_tracked_entity import ChangeTrackedEntity

            return ChangeTrackedEntity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channel".casefold():
            from .channel import Channel

            return Channel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chat".casefold():
            from .chat import Chat

            return Chat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatActivityStatistics".casefold():
            from .chat_activity_statistics import ChatActivityStatistics

            return ChatActivityStatistics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessage".casefold():
            from .chat_message import ChatMessage

            return ChatMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessageHostedContent".casefold():
            from .chat_message_hosted_content import ChatMessageHostedContent

            return ChatMessageHostedContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessageInfo".casefold():
            from .chat_message_info import ChatMessageInfo

            return ChatMessageInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.checklistItem".casefold():
            from .checklist_item import ChecklistItem

            return ChecklistItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chromeOSOnboardingSettings".casefold():
            from .chrome_o_s_onboarding_settings import ChromeOSOnboardingSettings

            return ChromeOSOnboardingSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.claimsMappingPolicy".casefold():
            from .claims_mapping_policy import ClaimsMappingPolicy

            return ClaimsMappingPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.classificationJobResponse".casefold():
            from .classification_job_response import ClassificationJobResponse

            return ClassificationJobResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudAppSecurityProfile".casefold():
            from .cloud_app_security_profile import CloudAppSecurityProfile

            return CloudAppSecurityProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudClipboardItem".casefold():
            from .cloud_clipboard_item import CloudClipboardItem

            return CloudClipboardItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudClipboardRoot".casefold():
            from .cloud_clipboard_root import CloudClipboardRoot

            return CloudClipboardRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPC".casefold():
            from .cloud_p_c import CloudPC

            return CloudPC()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcAuditEvent".casefold():
            from .cloud_pc_audit_event import CloudPcAuditEvent

            return CloudPcAuditEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkAction".casefold():
            from .cloud_pc_bulk_action import CloudPcBulkAction

            return CloudPcBulkAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkDisasterRecoveryFailback".casefold():
            from .cloud_pc_bulk_disaster_recovery_failback import CloudPcBulkDisasterRecoveryFailback

            return CloudPcBulkDisasterRecoveryFailback()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkDisasterRecoveryFailover".casefold():
            from .cloud_pc_bulk_disaster_recovery_failover import CloudPcBulkDisasterRecoveryFailover

            return CloudPcBulkDisasterRecoveryFailover()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkModifyDiskEncryptionType".casefold():
            from .cloud_pc_bulk_modify_disk_encryption_type import CloudPcBulkModifyDiskEncryptionType

            return CloudPcBulkModifyDiskEncryptionType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkPowerOff".casefold():
            from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff

            return CloudPcBulkPowerOff()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkPowerOn".casefold():
            from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn

            return CloudPcBulkPowerOn()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkReprovision".casefold():
            from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision

            return CloudPcBulkReprovision()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkResize".casefold():
            from .cloud_pc_bulk_resize import CloudPcBulkResize

            return CloudPcBulkResize()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkRestart".casefold():
            from .cloud_pc_bulk_restart import CloudPcBulkRestart

            return CloudPcBulkRestart()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkRestore".casefold():
            from .cloud_pc_bulk_restore import CloudPcBulkRestore

            return CloudPcBulkRestore()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkTroubleshoot".casefold():
            from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot

            return CloudPcBulkTroubleshoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPCConnectivityIssue".casefold():
            from .cloud_p_c_connectivity_issue import CloudPCConnectivityIssue

            return CloudPCConnectivityIssue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcCrossCloudGovernmentOrganizationMapping".casefold():
            from .cloud_pc_cross_cloud_government_organization_mapping import CloudPcCrossCloudGovernmentOrganizationMapping

            return CloudPcCrossCloudGovernmentOrganizationMapping()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcDeviceImage".casefold():
            from .cloud_pc_device_image import CloudPcDeviceImage

            return CloudPcDeviceImage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcExportJob".casefold():
            from .cloud_pc_export_job import CloudPcExportJob

            return CloudPcExportJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcExternalPartnerSetting".casefold():
            from .cloud_pc_external_partner_setting import CloudPcExternalPartnerSetting

            return CloudPcExternalPartnerSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcFrontLineServicePlan".casefold():
            from .cloud_pc_front_line_service_plan import CloudPcFrontLineServicePlan

            return CloudPcFrontLineServicePlan()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcGalleryImage".casefold():
            from .cloud_pc_gallery_image import CloudPcGalleryImage

            return CloudPcGalleryImage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcOnPremisesConnection".casefold():
            from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection

            return CloudPcOnPremisesConnection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcOrganizationSettings".casefold():
            from .cloud_pc_organization_settings import CloudPcOrganizationSettings

            return CloudPcOrganizationSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcProvisioningPolicy".casefold():
            from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy

            return CloudPcProvisioningPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcProvisioningPolicyAssignment".casefold():
            from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment

            return CloudPcProvisioningPolicyAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcReports".casefold():
            from .cloud_pc_reports import CloudPcReports

            return CloudPcReports()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcServicePlan".casefold():
            from .cloud_pc_service_plan import CloudPcServicePlan

            return CloudPcServicePlan()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcSharedUseServicePlan".casefold():
            from .cloud_pc_shared_use_service_plan import CloudPcSharedUseServicePlan

            return CloudPcSharedUseServicePlan()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcSnapshot".casefold():
            from .cloud_pc_snapshot import CloudPcSnapshot

            return CloudPcSnapshot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcSupportedRegion".casefold():
            from .cloud_pc_supported_region import CloudPcSupportedRegion

            return CloudPcSupportedRegion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcUserSetting".casefold():
            from .cloud_pc_user_setting import CloudPcUserSetting

            return CloudPcUserSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcUserSettingAssignment".casefold():
            from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment

            return CloudPcUserSettingAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.columnDefinition".casefold():
            from .column_definition import ColumnDefinition

            return ColumnDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.columnLink".casefold():
            from .column_link import ColumnLink

            return ColumnLink()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.comanagementEligibleDevice".casefold():
            from .comanagement_eligible_device import ComanagementEligibleDevice

            return ComanagementEligibleDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.command".casefold():
            from .command import Command

            return Command()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.commsOperation".casefold():
            from .comms_operation import CommsOperation

            return CommsOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.community".casefold():
            from .community import Community

            return Community()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.companySubscription".casefold():
            from .company_subscription import CompanySubscription

            return CompanySubscription()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.complianceManagementPartner".casefold():
            from .compliance_management_partner import ComplianceManagementPartner

            return ComplianceManagementPartner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conditionalAccessPolicy".casefold():
            from .conditional_access_policy import ConditionalAccessPolicy
            from .networkaccess.conditional_access_policy import ConditionalAccessPolicy

            return ConditionalAccessPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conditionalAccessRoot".casefold():
            from .conditional_access_root import ConditionalAccessRoot

            return ConditionalAccessRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conditionalAccessTemplate".casefold():
            from .conditional_access_template import ConditionalAccessTemplate

            return ConditionalAccessTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conditionalAccessWhatIfPolicy".casefold():
            from .conditional_access_what_if_policy import ConditionalAccessWhatIfPolicy

            return ConditionalAccessWhatIfPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.configManagerCollection".casefold():
            from .config_manager_collection import ConfigManagerCollection

            return ConfigManagerCollection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.connectedOrganization".casefold():
            from .connected_organization import ConnectedOrganization

            return ConnectedOrganization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.connectionOperation".casefold():
            from .connection_operation import ConnectionOperation
            from .external_connectors.connection_operation import ConnectionOperation

            return ConnectionOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.connector".casefold():
            from .connector import Connector

            return Connector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.connectorGroup".casefold():
            from .connector_group import ConnectorGroup

            return ConnectorGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contact".casefold():
            from .contact import Contact

            return Contact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contactFolder".casefold():
            from .contact_folder import ContactFolder

            return ContactFolder()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contactMergeSuggestions".casefold():
            from .contact_merge_suggestions import ContactMergeSuggestions

            return ContactMergeSuggestions()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contentSharingSession".casefold():
            from .content_sharing_session import ContentSharingSession

            return ContentSharingSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contentType".casefold():
            from .content_type import ContentType

            return ContentType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.continuousAccessEvaluationPolicy".casefold():
            from .continuous_access_evaluation_policy import ContinuousAccessEvaluationPolicy

            return ContinuousAccessEvaluationPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contract".casefold():
            from .contract import Contract

            return Contract()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conversation".casefold():
            from .conversation import Conversation

            return Conversation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conversationMember".casefold():
            from .conversation_member import ConversationMember

            return ConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conversationThread".casefold():
            from .conversation_thread import ConversationThread

            return ConversationThread()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.corsConfiguration_v2".casefold():
            from .cors_configuration_v2 import CorsConfiguration_v2

            return CorsConfiguration_v2()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.countryNamedLocation".casefold():
            from .country_named_location import CountryNamedLocation

            return CountryNamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.credentialUsageSummary".casefold():
            from .credential_usage_summary import CredentialUsageSummary

            return CredentialUsageSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.credentialUserRegistrationCount".casefold():
            from .credential_user_registration_count import CredentialUserRegistrationCount

            return CredentialUserRegistrationCount()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.credentialUserRegistrationDetails".casefold():
            from .credential_user_registration_details import CredentialUserRegistrationDetails

            return CredentialUserRegistrationDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantAccessPolicy".casefold():
            from .cross_tenant_access_policy import CrossTenantAccessPolicy

            return CrossTenantAccessPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantAccessPolicyConfigurationDefault".casefold():
            from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault

            return CrossTenantAccessPolicyConfigurationDefault()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customAccessPackageWorkflowExtension".casefold():
            from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension

            return CustomAccessPackageWorkflowExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customAppScope".casefold():
            from .custom_app_scope import CustomAppScope

            return CustomAppScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customAuthenticationExtension".casefold():
            from .custom_authentication_extension import CustomAuthenticationExtension

            return CustomAuthenticationExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customCalloutExtension".casefold():
            from .custom_callout_extension import CustomCalloutExtension

            return CustomCalloutExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customExtensionHandler".casefold():
            from .custom_extension_handler import CustomExtensionHandler

            return CustomExtensionHandler()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customExtensionStageSetting".casefold():
            from .custom_extension_stage_setting import CustomExtensionStageSetting

            return CustomExtensionStageSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customSecurityAttributeAudit".casefold():
            from .custom_security_attribute_audit import CustomSecurityAttributeAudit

            return CustomSecurityAttributeAudit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customSecurityAttributeDefinition".casefold():
            from .custom_security_attribute_definition import CustomSecurityAttributeDefinition

            return CustomSecurityAttributeDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dailyInactiveUsersByApplicationMetric".casefold():
            from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric

            return DailyInactiveUsersByApplicationMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dailyInactiveUsersMetric".casefold():
            from .daily_inactive_users_metric import DailyInactiveUsersMetric

            return DailyInactiveUsersMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dailyUserInsightMetricsRoot".casefold():
            from .daily_user_insight_metrics_root import DailyUserInsightMetricsRoot

            return DailyUserInsightMetricsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dataClassificationService".casefold():
            from .data_classification_service import DataClassificationService

            return DataClassificationService()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dataCollectionInfo".casefold():
            from .data_collection_info import DataCollectionInfo

            return DataCollectionInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dataLossPreventionPolicy".casefold():
            from .data_loss_prevention_policy import DataLossPreventionPolicy

            return DataLossPreventionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dataPolicyOperation".casefold():
            from .data_policy_operation import DataPolicyOperation

            return DataPolicyOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dataSharingConsent".casefold():
            from .data_sharing_consent import DataSharingConsent

            return DataSharingConsent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dayNote".casefold():
            from .day_note import DayNote

            return DayNote()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.defaultDeviceCompliancePolicy".casefold():
            from .default_device_compliance_policy import DefaultDeviceCompliancePolicy

            return DefaultDeviceCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.defaultManagedAppProtection".casefold():
            from .default_managed_app_protection import DefaultManagedAppProtection

            return DefaultManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.defaultUserRoleOverride".casefold():
            from .default_user_role_override import DefaultUserRoleOverride

            return DefaultUserRoleOverride()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminAccessAssignment".casefold():
            from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment

            return DelegatedAdminAccessAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminCustomer".casefold():
            from .delegated_admin_customer import DelegatedAdminCustomer

            return DelegatedAdminCustomer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminRelationship".casefold():
            from .delegated_admin_relationship import DelegatedAdminRelationship

            return DelegatedAdminRelationship()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminRelationshipOperation".casefold():
            from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation

            return DelegatedAdminRelationshipOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminRelationshipRequest".casefold():
            from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest

            return DelegatedAdminRelationshipRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminServiceManagementDetail".casefold():
            from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail

            return DelegatedAdminServiceManagementDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedPermissionClassification".casefold():
            from .delegated_permission_classification import DelegatedPermissionClassification

            return DelegatedPermissionClassification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deletedChat".casefold():
            from .deleted_chat import DeletedChat

            return DeletedChat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deletedItemContainer".casefold():
            from .deleted_item_container import DeletedItemContainer

            return DeletedItemContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deletedTeam".casefold():
            from .deleted_team import DeletedTeam

            return DeletedTeam()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deltaParticipants".casefold():
            from .delta_participants import DeltaParticipants

            return DeltaParticipants()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.depEnrollmentBaseProfile".casefold():
            from .dep_enrollment_base_profile import DepEnrollmentBaseProfile

            return DepEnrollmentBaseProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.depEnrollmentProfile".casefold():
            from .dep_enrollment_profile import DepEnrollmentProfile

            return DepEnrollmentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.depIOSEnrollmentProfile".casefold():
            from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile

            return DepIOSEnrollmentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.depMacOSEnrollmentProfile".casefold():
            from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile

            return DepMacOSEnrollmentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.depOnboardingSetting".casefold():
            from .dep_onboarding_setting import DepOnboardingSetting

            return DepOnboardingSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.detectedApp".casefold():
            from .detected_app import DetectedApp

            return DetectedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.device".casefold():
            from .device import Device

            return Device()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAndAppManagementAssignmentFilter".casefold():
            from .device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter

            return DeviceAndAppManagementAssignmentFilter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAndAppManagementRoleAssignment".casefold():
            from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment

            return DeviceAndAppManagementRoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAndAppManagementRoleDefinition".casefold():
            from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition

            return DeviceAndAppManagementRoleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAppManagement".casefold():
            from .device_app_management import DeviceAppManagement

            return DeviceAppManagement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAppManagementTask".casefold():
            from .device_app_management_task import DeviceAppManagementTask

            return DeviceAppManagementTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCategory".casefold():
            from .device_category import DeviceCategory

            return DeviceCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComanagementAuthorityConfiguration".casefold():
            from .device_comanagement_authority_configuration import DeviceComanagementAuthorityConfiguration

            return DeviceComanagementAuthorityConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceActionItem".casefold():
            from .device_compliance_action_item import DeviceComplianceActionItem

            return DeviceComplianceActionItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceDeviceOverview".casefold():
            from .device_compliance_device_overview import DeviceComplianceDeviceOverview

            return DeviceComplianceDeviceOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceDeviceStatus".casefold():
            from .device_compliance_device_status import DeviceComplianceDeviceStatus

            return DeviceComplianceDeviceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicy".casefold():
            from .device_compliance_policy import DeviceCompliancePolicy

            return DeviceCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicyAssignment".casefold():
            from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment

            return DeviceCompliancePolicyAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicyDeviceStateSummary".casefold():
            from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary

            return DeviceCompliancePolicyDeviceStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicyGroupAssignment".casefold():
            from .device_compliance_policy_group_assignment import DeviceCompliancePolicyGroupAssignment

            return DeviceCompliancePolicyGroupAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicyPolicySetItem".casefold():
            from .device_compliance_policy_policy_set_item import DeviceCompliancePolicyPolicySetItem

            return DeviceCompliancePolicyPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicySettingStateSummary".casefold():
            from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
            from .managed_tenants.device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary

            return DeviceCompliancePolicySettingStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicyState".casefold():
            from .device_compliance_policy_state import DeviceCompliancePolicyState

            return DeviceCompliancePolicyState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceScheduledActionForRule".casefold():
            from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule

            return DeviceComplianceScheduledActionForRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceScript".casefold():
            from .device_compliance_script import DeviceComplianceScript

            return DeviceComplianceScript()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceScriptDeviceState".casefold():
            from .device_compliance_script_device_state import DeviceComplianceScriptDeviceState

            return DeviceComplianceScriptDeviceState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceScriptRunSummary".casefold():
            from .device_compliance_script_run_summary import DeviceComplianceScriptRunSummary

            return DeviceComplianceScriptRunSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceSettingState".casefold():
            from .device_compliance_setting_state import DeviceComplianceSettingState

            return DeviceComplianceSettingState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceUserOverview".casefold():
            from .device_compliance_user_overview import DeviceComplianceUserOverview

            return DeviceComplianceUserOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceUserStatus".casefold():
            from .device_compliance_user_status import DeviceComplianceUserStatus

            return DeviceComplianceUserStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfiguration".casefold():
            from .device_configuration import DeviceConfiguration

            return DeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationAssignment".casefold():
            from .device_configuration_assignment import DeviceConfigurationAssignment

            return DeviceConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationConflictSummary".casefold():
            from .device_configuration_conflict_summary import DeviceConfigurationConflictSummary

            return DeviceConfigurationConflictSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationDeviceOverview".casefold():
            from .device_configuration_device_overview import DeviceConfigurationDeviceOverview

            return DeviceConfigurationDeviceOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationDeviceStateSummary".casefold():
            from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary

            return DeviceConfigurationDeviceStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationDeviceStatus".casefold():
            from .device_configuration_device_status import DeviceConfigurationDeviceStatus

            return DeviceConfigurationDeviceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationGroupAssignment".casefold():
            from .device_configuration_group_assignment import DeviceConfigurationGroupAssignment

            return DeviceConfigurationGroupAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationPolicySetItem".casefold():
            from .device_configuration_policy_set_item import DeviceConfigurationPolicySetItem

            return DeviceConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationProfile".casefold():
            from .device_configuration_profile import DeviceConfigurationProfile

            return DeviceConfigurationProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationState".casefold():
            from .device_configuration_state import DeviceConfigurationState

            return DeviceConfigurationState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationUserOverview".casefold():
            from .device_configuration_user_overview import DeviceConfigurationUserOverview

            return DeviceConfigurationUserOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationUserStateSummary".casefold():
            from .device_configuration_user_state_summary import DeviceConfigurationUserStateSummary

            return DeviceConfigurationUserStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationUserStatus".casefold():
            from .device_configuration_user_status import DeviceConfigurationUserStatus

            return DeviceConfigurationUserStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCustomAttributeShellScript".casefold():
            from .device_custom_attribute_shell_script import DeviceCustomAttributeShellScript

            return DeviceCustomAttributeShellScript()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentConfiguration".casefold():
            from .device_enrollment_configuration import DeviceEnrollmentConfiguration

            return DeviceEnrollmentConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentLimitConfiguration".casefold():
            from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration

            return DeviceEnrollmentLimitConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentNotificationConfiguration".casefold():
            from .device_enrollment_notification_configuration import DeviceEnrollmentNotificationConfiguration

            return DeviceEnrollmentNotificationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentPlatformRestrictionConfiguration".casefold():
            from .device_enrollment_platform_restriction_configuration import DeviceEnrollmentPlatformRestrictionConfiguration

            return DeviceEnrollmentPlatformRestrictionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration".casefold():
            from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration

            return DeviceEnrollmentPlatformRestrictionsConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentWindowsHelloForBusinessConfiguration".casefold():
            from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration

            return DeviceEnrollmentWindowsHelloForBusinessConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceHealthScript".casefold():
            from .device_health_script import DeviceHealthScript

            return DeviceHealthScript()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceHealthScriptAssignment".casefold():
            from .device_health_script_assignment import DeviceHealthScriptAssignment

            return DeviceHealthScriptAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceHealthScriptDeviceState".casefold():
            from .device_health_script_device_state import DeviceHealthScriptDeviceState

            return DeviceHealthScriptDeviceState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceHealthScriptRunSummary".casefold():
            from .device_health_script_run_summary import DeviceHealthScriptRunSummary

            return DeviceHealthScriptRunSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceInstallState".casefold():
            from .device_install_state import DeviceInstallState

            return DeviceInstallState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceLocalCredentialInfo".casefold():
            from .device_local_credential_info import DeviceLocalCredentialInfo

            return DeviceLocalCredentialInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceLogCollectionResponse".casefold():
            from .device_log_collection_response import DeviceLogCollectionResponse

            return DeviceLogCollectionResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagement".casefold():
            from .device_management.device_management import DeviceManagement

            return DeviceManagement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagement.alertRecord".casefold():
            from .device_management.alert_record import AlertRecord

            return AlertRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagement.alertRule".casefold():
            from .device_management.alert_rule import AlertRule

            return AlertRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagement.monitoring".casefold():
            from .device_management.monitoring import Monitoring

            return Monitoring()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementAbstractComplexSettingDefinition".casefold():
            from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition

            return DeviceManagementAbstractComplexSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementAbstractComplexSettingInstance".casefold():
            from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance

            return DeviceManagementAbstractComplexSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementAutopilotEvent".casefold():
            from .device_management_autopilot_event import DeviceManagementAutopilotEvent

            return DeviceManagementAutopilotEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementAutopilotPolicyStatusDetail".casefold():
            from .device_management_autopilot_policy_status_detail import DeviceManagementAutopilotPolicyStatusDetail

            return DeviceManagementAutopilotPolicyStatusDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementBooleanSettingInstance".casefold():
            from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance

            return DeviceManagementBooleanSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementCachedReportConfiguration".casefold():
            from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration

            return DeviceManagementCachedReportConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementCollectionSettingDefinition".casefold():
            from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition

            return DeviceManagementCollectionSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementCollectionSettingInstance".casefold():
            from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance

            return DeviceManagementCollectionSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementComplexSettingDefinition".casefold():
            from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition

            return DeviceManagementComplexSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementComplexSettingInstance".casefold():
            from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance

            return DeviceManagementComplexSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementComplianceActionItem".casefold():
            from .device_management_compliance_action_item import DeviceManagementComplianceActionItem

            return DeviceManagementComplianceActionItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementCompliancePolicy".casefold():
            from .device_management_compliance_policy import DeviceManagementCompliancePolicy

            return DeviceManagementCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementComplianceScheduledActionForRule".casefold():
            from .device_management_compliance_scheduled_action_for_rule import DeviceManagementComplianceScheduledActionForRule

            return DeviceManagementComplianceScheduledActionForRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationCategory".casefold():
            from .device_management_configuration_category import DeviceManagementConfigurationCategory

            return DeviceManagementConfigurationCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionDefinition".casefold():
            from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition

            return DeviceManagementConfigurationChoiceSettingCollectionDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingDefinition".casefold():
            from .device_management_configuration_choice_setting_definition import DeviceManagementConfigurationChoiceSettingDefinition

            return DeviceManagementConfigurationChoiceSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationPolicy".casefold():
            from .device_management_configuration_policy import DeviceManagementConfigurationPolicy

            return DeviceManagementConfigurationPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationPolicyAssignment".casefold():
            from .device_management_configuration_policy_assignment import DeviceManagementConfigurationPolicyAssignment

            return DeviceManagementConfigurationPolicyAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationPolicyPolicySetItem".casefold():
            from .device_management_configuration_policy_policy_set_item import DeviceManagementConfigurationPolicyPolicySetItem

            return DeviceManagementConfigurationPolicyPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationPolicyTemplate".casefold():
            from .device_management_configuration_policy_template import DeviceManagementConfigurationPolicyTemplate

            return DeviceManagementConfigurationPolicyTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationRedirectSettingDefinition".casefold():
            from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition

            return DeviceManagementConfigurationRedirectSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSetting".casefold():
            from .device_management_configuration_setting import DeviceManagementConfigurationSetting

            return DeviceManagementConfigurationSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSettingDefinition".casefold():
            from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition

            return DeviceManagementConfigurationSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSettingGroupCollectionDefinition".casefold():
            from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition

            return DeviceManagementConfigurationSettingGroupCollectionDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSettingGroupDefinition".casefold():
            from .device_management_configuration_setting_group_definition import DeviceManagementConfigurationSettingGroupDefinition

            return DeviceManagementConfigurationSettingGroupDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSettingTemplate".casefold():
            from .device_management_configuration_setting_template import DeviceManagementConfigurationSettingTemplate

            return DeviceManagementConfigurationSettingTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionDefinition".casefold():
            from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition

            return DeviceManagementConfigurationSimpleSettingCollectionDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingDefinition".casefold():
            from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition

            return DeviceManagementConfigurationSimpleSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementDerivedCredentialSettings".casefold():
            from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings

            return DeviceManagementDerivedCredentialSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementDomainJoinConnector".casefold():
            from .device_management_domain_join_connector import DeviceManagementDomainJoinConnector

            return DeviceManagementDomainJoinConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementExchangeConnector".casefold():
            from .device_management_exchange_connector import DeviceManagementExchangeConnector

            return DeviceManagementExchangeConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementExchangeOnPremisesPolicy".casefold():
            from .device_management_exchange_on_premises_policy import DeviceManagementExchangeOnPremisesPolicy

            return DeviceManagementExchangeOnPremisesPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementExportJob".casefold():
            from .device_management_export_job import DeviceManagementExportJob

            return DeviceManagementExportJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntegerSettingInstance".casefold():
            from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance

            return DeviceManagementIntegerSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntent".casefold():
            from .device_management_intent import DeviceManagementIntent

            return DeviceManagementIntent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntentAssignment".casefold():
            from .device_management_intent_assignment import DeviceManagementIntentAssignment

            return DeviceManagementIntentAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntentDeviceSettingStateSummary".casefold():
            from .device_management_intent_device_setting_state_summary import DeviceManagementIntentDeviceSettingStateSummary

            return DeviceManagementIntentDeviceSettingStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntentDeviceState".casefold():
            from .device_management_intent_device_state import DeviceManagementIntentDeviceState

            return DeviceManagementIntentDeviceState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntentDeviceStateSummary".casefold():
            from .device_management_intent_device_state_summary import DeviceManagementIntentDeviceStateSummary

            return DeviceManagementIntentDeviceStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntentSettingCategory".casefold():
            from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory

            return DeviceManagementIntentSettingCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntentUserState".casefold():
            from .device_management_intent_user_state import DeviceManagementIntentUserState

            return DeviceManagementIntentUserState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntentUserStateSummary".casefold():
            from .device_management_intent_user_state_summary import DeviceManagementIntentUserStateSummary

            return DeviceManagementIntentUserStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementPartner".casefold():
            from .device_management_partner import DeviceManagementPartner

            return DeviceManagementPartner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementReports".casefold():
            from .device_management_reports import DeviceManagementReports

            return DeviceManagementReports()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementResourceAccessProfileAssignment".casefold():
            from .device_management_resource_access_profile_assignment import DeviceManagementResourceAccessProfileAssignment

            return DeviceManagementResourceAccessProfileAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementResourceAccessProfileBase".casefold():
            from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase

            return DeviceManagementResourceAccessProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementReusablePolicySetting".casefold():
            from .device_management_reusable_policy_setting import DeviceManagementReusablePolicySetting

            return DeviceManagementReusablePolicySetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementScript".casefold():
            from .device_management_script import DeviceManagementScript

            return DeviceManagementScript()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementScriptAssignment".casefold():
            from .device_management_script_assignment import DeviceManagementScriptAssignment

            return DeviceManagementScriptAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementScriptDeviceState".casefold():
            from .device_management_script_device_state import DeviceManagementScriptDeviceState

            return DeviceManagementScriptDeviceState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementScriptGroupAssignment".casefold():
            from .device_management_script_group_assignment import DeviceManagementScriptGroupAssignment

            return DeviceManagementScriptGroupAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementScriptPolicySetItem".casefold():
            from .device_management_script_policy_set_item import DeviceManagementScriptPolicySetItem

            return DeviceManagementScriptPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementScriptRunSummary".casefold():
            from .device_management_script_run_summary import DeviceManagementScriptRunSummary

            return DeviceManagementScriptRunSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementScriptUserState".casefold():
            from .device_management_script_user_state import DeviceManagementScriptUserState

            return DeviceManagementScriptUserState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingCategory".casefold():
            from .device_management_setting_category import DeviceManagementSettingCategory

            return DeviceManagementSettingCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingDefinition".casefold():
            from .device_management_setting_definition import DeviceManagementSettingDefinition

            return DeviceManagementSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingInstance".casefold():
            from .device_management_setting_instance import DeviceManagementSettingInstance

            return DeviceManagementSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementStringSettingInstance".casefold():
            from .device_management_string_setting_instance import DeviceManagementStringSettingInstance

            return DeviceManagementStringSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementTemplate".casefold():
            from .device_management_template import DeviceManagementTemplate

            return DeviceManagementTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementTemplateInsightsDefinition".casefold():
            from .device_management_template_insights_definition import DeviceManagementTemplateInsightsDefinition

            return DeviceManagementTemplateInsightsDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementTemplateSettingCategory".casefold():
            from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory

            return DeviceManagementTemplateSettingCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementTroubleshootingEvent".casefold():
            from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent

            return DeviceManagementTroubleshootingEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceRegistrationPolicy".casefold():
            from .device_registration_policy import DeviceRegistrationPolicy

            return DeviceRegistrationPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceSetupConfiguration".casefold():
            from .device_setup_configuration import DeviceSetupConfiguration

            return DeviceSetupConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceShellScript".casefold():
            from .device_shell_script import DeviceShellScript

            return DeviceShellScript()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directory".casefold():
            from .directory import Directory

            return Directory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryAudit".casefold():
            from .directory_audit import DirectoryAudit

            return DirectoryAudit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryDefinition".casefold():
            from .directory_definition import DirectoryDefinition

            return DirectoryDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryObject".casefold():
            from .directory_object import DirectoryObject

            return DirectoryObject()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryObjectPartnerReference".casefold():
            from .directory_object_partner_reference import DirectoryObjectPartnerReference

            return DirectoryObjectPartnerReference()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryRole".casefold():
            from .directory_role import DirectoryRole

            return DirectoryRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryRoleAccessReviewPolicy".casefold():
            from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicy

            return DirectoryRoleAccessReviewPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryRoleTemplate".casefold():
            from .directory_role_template import DirectoryRoleTemplate

            return DirectoryRoleTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directorySetting".casefold():
            from .directory_setting import DirectorySetting

            return DirectorySetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directorySettingTemplate".casefold():
            from .directory_setting_template import DirectorySettingTemplate

            return DirectorySettingTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dlpEvaluatePoliciesJobResponse".casefold():
            from .dlp_evaluate_policies_job_response import DlpEvaluatePoliciesJobResponse

            return DlpEvaluatePoliciesJobResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.document".casefold():
            from .document import Document

            return Document()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.documentComment".casefold():
            from .document_comment import DocumentComment

            return DocumentComment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.documentCommentReply".casefold():
            from .document_comment_reply import DocumentCommentReply

            return DocumentCommentReply()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.documentSetVersion".casefold():
            from .document_set_version import DocumentSetVersion

            return DocumentSetVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domain".casefold():
            from .domain import Domain

            return Domain()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsCnameRecord".casefold():
            from .domain_dns_cname_record import DomainDnsCnameRecord

            return DomainDnsCnameRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsMxRecord".casefold():
            from .domain_dns_mx_record import DomainDnsMxRecord

            return DomainDnsMxRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsRecord".casefold():
            from .domain_dns_record import DomainDnsRecord

            return DomainDnsRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsSrvRecord".casefold():
            from .domain_dns_srv_record import DomainDnsSrvRecord

            return DomainDnsSrvRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsTxtRecord".casefold():
            from .domain_dns_txt_record import DomainDnsTxtRecord

            return DomainDnsTxtRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsUnavailableRecord".casefold():
            from .domain_dns_unavailable_record import DomainDnsUnavailableRecord

            return DomainDnsUnavailableRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainSecurityProfile".casefold():
            from .domain_security_profile import DomainSecurityProfile

            return DomainSecurityProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.drive".casefold():
            from .drive import Drive

            return Drive()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveItem".casefold():
            from .drive_item import DriveItem

            return DriveItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveItemVersion".casefold():
            from .drive_item_version import DriveItemVersion

            return DriveItemVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.easEmailProfileConfigurationBase".casefold():
            from .eas_email_profile_configuration_base import EasEmailProfileConfigurationBase

            return EasEmailProfileConfigurationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eBookInstallSummary".casefold():
            from .e_book_install_summary import EBookInstallSummary

            return EBookInstallSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.edge".casefold():
            from .edge import Edge

            return Edge()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.addToReviewSetOperation".casefold():
            from .ediscovery.add_to_review_set_operation import AddToReviewSetOperation

            return AddToReviewSetOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.case".casefold():
            from .ediscovery.case import Case
            from .security.case import Case

            return Case()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.caseExportOperation".casefold():
            from .ediscovery.case_export_operation import CaseExportOperation

            return CaseExportOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.caseHoldOperation".casefold():
            from .ediscovery.case_hold_operation import CaseHoldOperation

            return CaseHoldOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.caseIndexOperation".casefold():
            from .ediscovery.case_index_operation import CaseIndexOperation

            return CaseIndexOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.caseOperation".casefold():
            from .ediscovery.case_operation import CaseOperation
            from .security.case_operation import CaseOperation

            return CaseOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.caseSettings".casefold():
            from .ediscovery.case_settings import CaseSettings

            return CaseSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.custodian".casefold():
            from .ediscovery.custodian import Custodian

            return Custodian()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.dataSource".casefold():
            from .ediscovery.data_source import DataSource
            from .security.data_source import DataSource

            return DataSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.dataSourceContainer".casefold():
            from .ediscovery.data_source_container import DataSourceContainer
            from .security.data_source_container import DataSourceContainer

            return DataSourceContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.ediscoveryroot".casefold():
            from .ediscovery.ediscoveryroot import Ediscoveryroot

            return Ediscoveryroot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.estimateStatisticsOperation".casefold():
            from .ediscovery.estimate_statistics_operation import EstimateStatisticsOperation

            return EstimateStatisticsOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.legalHold".casefold():
            from .ediscovery.legal_hold import LegalHold

            return LegalHold()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.noncustodialDataSource".casefold():
            from .ediscovery.noncustodial_data_source import NoncustodialDataSource

            return NoncustodialDataSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.purgeDataOperation".casefold():
            from .ediscovery.purge_data_operation import PurgeDataOperation

            return PurgeDataOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.reviewSet".casefold():
            from .ediscovery.review_set import ReviewSet

            return ReviewSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.reviewSetQuery".casefold():
            from .ediscovery.review_set_query import ReviewSetQuery

            return ReviewSetQuery()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.siteSource".casefold():
            from .ediscovery.site_source import SiteSource
            from .security.site_source import SiteSource

            return SiteSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.sourceCollection".casefold():
            from .ediscovery.source_collection import SourceCollection

            return SourceCollection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.tag".casefold():
            from .ediscovery.tag import Tag
            from .security.tag import Tag

            return Tag()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.tagOperation".casefold():
            from .ediscovery.tag_operation import TagOperation

            return TagOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.unifiedGroupSource".casefold():
            from .ediscovery.unified_group_source import UnifiedGroupSource
            from .security.unified_group_source import UnifiedGroupSource

            return UnifiedGroupSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.userSource".casefold():
            from .ediscovery.user_source import UserSource
            from .security.user_source import UserSource

            return UserSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.editionUpgradeConfiguration".casefold():
            from .edition_upgrade_configuration import EditionUpgradeConfiguration

            return EditionUpgradeConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationalActivity".casefold():
            from .educational_activity import EducationalActivity

            return EducationalActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationAssignment".casefold():
            from .education_assignment import EducationAssignment

            return EducationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationAssignmentDefaults".casefold():
            from .education_assignment_defaults import EducationAssignmentDefaults

            return EducationAssignmentDefaults()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationAssignmentResource".casefold():
            from .education_assignment_resource import EducationAssignmentResource

            return EducationAssignmentResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationAssignmentSettings".casefold():
            from .education_assignment_settings import EducationAssignmentSettings

            return EducationAssignmentSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationCategory".casefold():
            from .education_category import EducationCategory

            return EducationCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationClass".casefold():
            from .education_class import EducationClass

            return EducationClass()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationFeedbackOutcome".casefold():
            from .education_feedback_outcome import EducationFeedbackOutcome

            return EducationFeedbackOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationFeedbackResourceOutcome".casefold():
            from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome

            return EducationFeedbackResourceOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationGradingCategory".casefold():
            from .education_grading_category import EducationGradingCategory

            return EducationGradingCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationGradingScheme".casefold():
            from .education_grading_scheme import EducationGradingScheme

            return EducationGradingScheme()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationModule".casefold():
            from .education_module import EducationModule

            return EducationModule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationModuleResource".casefold():
            from .education_module_resource import EducationModuleResource

            return EducationModuleResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationOrganization".casefold():
            from .education_organization import EducationOrganization

            return EducationOrganization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationOutcome".casefold():
            from .education_outcome import EducationOutcome

            return EducationOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationPointsOutcome".casefold():
            from .education_points_outcome import EducationPointsOutcome

            return EducationPointsOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationRubric".casefold():
            from .education_rubric import EducationRubric

            return EducationRubric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationRubricOutcome".casefold():
            from .education_rubric_outcome import EducationRubricOutcome

            return EducationRubricOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSchool".casefold():
            from .education_school import EducationSchool

            return EducationSchool()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSubmission".casefold():
            from .education_submission import EducationSubmission

            return EducationSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSubmissionResource".casefold():
            from .education_submission_resource import EducationSubmissionResource

            return EducationSubmissionResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSynchronizationError".casefold():
            from .education_synchronization_error import EducationSynchronizationError

            return EducationSynchronizationError()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSynchronizationProfile".casefold():
            from .education_synchronization_profile import EducationSynchronizationProfile

            return EducationSynchronizationProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSynchronizationProfileStatus".casefold():
            from .education_synchronization_profile_status import EducationSynchronizationProfileStatus

            return EducationSynchronizationProfileStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationUser".casefold():
            from .education_user import EducationUser

            return EducationUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailActivityStatistics".casefold():
            from .email_activity_statistics import EmailActivityStatistics

            return EmailActivityStatistics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailAuthenticationMethod".casefold():
            from .email_authentication_method import EmailAuthenticationMethod

            return EmailAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailAuthenticationMethodConfiguration".casefold():
            from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration

            return EmailAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailFileAssessmentRequest".casefold():
            from .email_file_assessment_request import EmailFileAssessmentRequest

            return EmailFileAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.embeddedSIMActivationCodePool".casefold():
            from .embedded_s_i_m_activation_code_pool import EmbeddedSIMActivationCodePool

            return EmbeddedSIMActivationCodePool()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.embeddedSIMActivationCodePoolAssignment".casefold():
            from .embedded_s_i_m_activation_code_pool_assignment import EmbeddedSIMActivationCodePoolAssignment

            return EmbeddedSIMActivationCodePoolAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.embeddedSIMDeviceState".casefold():
            from .embedded_s_i_m_device_state import EmbeddedSIMDeviceState

            return EmbeddedSIMDeviceState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.employeeExperienceUser".casefold():
            from .employee_experience_user import EmployeeExperienceUser

            return EmployeeExperienceUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptedAwsStorageBucketFinding".casefold():
            from .encrypted_aws_storage_bucket_finding import EncryptedAwsStorageBucketFinding

            return EncryptedAwsStorageBucketFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptedAzureStorageAccountFinding".casefold():
            from .encrypted_azure_storage_account_finding import EncryptedAzureStorageAccountFinding

            return EncryptedAzureStorageAccountFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptedGcpStorageBucketFinding".casefold():
            from .encrypted_gcp_storage_bucket_finding import EncryptedGcpStorageBucketFinding

            return EncryptedGcpStorageBucketFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.endpoint".casefold():
            from .endpoint import Endpoint

            return Endpoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.endUserNotification".casefold():
            from .end_user_notification import EndUserNotification

            return EndUserNotification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.endUserNotificationDetail".casefold():
            from .end_user_notification_detail import EndUserNotificationDetail

            return EndUserNotificationDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementAsyncOperation".casefold():
            from .engagement_async_operation import EngagementAsyncOperation

            return EngagementAsyncOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enrollmentConfigurationAssignment".casefold():
            from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment

            return EnrollmentConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enrollmentProfile".casefold():
            from .enrollment_profile import EnrollmentProfile

            return EnrollmentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enrollmentRestrictionsConfigurationPolicySetItem".casefold():
            from .enrollment_restrictions_configuration_policy_set_item import EnrollmentRestrictionsConfigurationPolicySetItem

            return EnrollmentRestrictionsConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enrollmentTroubleshootingEvent".casefold():
            from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent

            return EnrollmentTroubleshootingEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enterpriseCodeSigningCertificate".casefold():
            from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate

            return EnterpriseCodeSigningCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.entitlementManagement".casefold():
            from .entitlement_management import EntitlementManagement

            return EntitlementManagement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.entitlementManagementSettings".casefold():
            from .entitlement_management_settings import EntitlementManagementSettings

            return EntitlementManagementSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.evaluateLabelJobResponse".casefold():
            from .evaluate_label_job_response import EvaluateLabelJobResponse

            return EvaluateLabelJobResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.event".casefold():
            from .event import Event

            return Event()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessage".casefold():
            from .event_message import EventMessage

            return EventMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageRequest".casefold():
            from .event_message_request import EventMessageRequest

            return EventMessageRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageResponse".casefold():
            from .event_message_response import EventMessageResponse

            return EventMessageResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exactMatchDataStore".casefold():
            from .exact_match_data_store import ExactMatchDataStore

            return ExactMatchDataStore()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exactMatchDataStoreBase".casefold():
            from .exact_match_data_store_base import ExactMatchDataStoreBase

            return ExactMatchDataStoreBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exactMatchJobBase".casefold():
            from .exact_match_job_base import ExactMatchJobBase

            return ExactMatchJobBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exactMatchLookupJob".casefold():
            from .exact_match_lookup_job import ExactMatchLookupJob

            return ExactMatchLookupJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exactMatchSession".casefold():
            from .exact_match_session import ExactMatchSession

            return ExactMatchSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exactMatchSessionBase".casefold():
            from .exact_match_session_base import ExactMatchSessionBase

            return ExactMatchSessionBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exactMatchUploadAgent".casefold():
            from .exact_match_upload_agent import ExactMatchUploadAgent

            return ExactMatchUploadAgent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.extension".casefold():
            from .extension import Extension

            return Extension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.extensionProperty".casefold():
            from .extension_property import ExtensionProperty

            return ExtensionProperty()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.external".casefold():
            from .external import External

            return External()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnection".casefold():
            from .external_connection import ExternalConnection
            from .external_connectors.external_connection import ExternalConnection

            return ExternalConnection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.connectionOperation".casefold():
            from .connection_operation import ConnectionOperation
            from .external_connectors.connection_operation import ConnectionOperation

            return ConnectionOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.connectionQuota".casefold():
            from .external_connectors.connection_quota import ConnectionQuota

            return ConnectionQuota()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalActivity".casefold():
            from .external_connectors.external_activity import ExternalActivity

            return ExternalActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalActivityResult".casefold():
            from .external_connectors.external_activity_result import ExternalActivityResult

            return ExternalActivityResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalConnection".casefold():
            from .external_connection import ExternalConnection
            from .external_connectors.external_connection import ExternalConnection

            return ExternalConnection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalGroup".casefold():
            from .external_connectors.external_group import ExternalGroup
            from .external_group import ExternalGroup

            return ExternalGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalItem".casefold():
            from .external_connectors.external_item import ExternalItem
            from .external_item import ExternalItem

            return ExternalItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.identity".casefold():
            from .external_connectors.identity import Identity

            return Identity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.schema".casefold():
            from .external_connectors.schema import Schema
            from .schema import Schema

            return Schema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalDomainName".casefold():
            from .external_domain_name import ExternalDomainName

            return ExternalDomainName()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalGroup".casefold():
            from .external_connectors.external_group import ExternalGroup
            from .external_group import ExternalGroup

            return ExternalGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalIdentitiesPolicy".casefold():
            from .external_identities_policy import ExternalIdentitiesPolicy

            return ExternalIdentitiesPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalItem".casefold():
            from .external_connectors.external_item import ExternalItem
            from .external_item import ExternalItem

            return ExternalItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externallyAccessibleAwsStorageBucketFinding".casefold():
            from .externally_accessible_aws_storage_bucket_finding import ExternallyAccessibleAwsStorageBucketFinding

            return ExternallyAccessibleAwsStorageBucketFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externallyAccessibleAzureBlobContainerFinding".casefold():
            from .externally_accessible_azure_blob_container_finding import ExternallyAccessibleAzureBlobContainerFinding

            return ExternallyAccessibleAzureBlobContainerFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externallyAccessibleGcpStorageBucketFinding".casefold():
            from .externally_accessible_gcp_storage_bucket_finding import ExternallyAccessibleGcpStorageBucketFinding

            return ExternallyAccessibleGcpStorageBucketFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalMeetingRegistrant".casefold():
            from .external_meeting_registrant import ExternalMeetingRegistrant

            return ExternalMeetingRegistrant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalMeetingRegistration".casefold():
            from .external_meeting_registration import ExternalMeetingRegistration

            return ExternalMeetingRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalProfile".casefold():
            from .external_profile import ExternalProfile

            return ExternalProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalUserProfile".casefold():
            from .external_user_profile import ExternalUserProfile

            return ExternalUserProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalUsersSelfServiceSignUpEventsFlow".casefold():
            from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow

            return ExternalUsersSelfServiceSignUpEventsFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.featureRolloutPolicy".casefold():
            from .feature_rollout_policy import FeatureRolloutPolicy

            return FeatureRolloutPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.federatedIdentityCredential".casefold():
            from .federated_identity_credential import FederatedIdentityCredential

            return FederatedIdentityCredential()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.federatedTokenValidationPolicy".casefold():
            from .federated_token_validation_policy import FederatedTokenValidationPolicy

            return FederatedTokenValidationPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2AuthenticationMethod".casefold():
            from .fido2_authentication_method import Fido2AuthenticationMethod

            return Fido2AuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2AuthenticationMethodConfiguration".casefold():
            from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration

            return Fido2AuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2CombinationConfiguration".casefold():
            from .fido2_combination_configuration import Fido2CombinationConfiguration

            return Fido2CombinationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fieldValueSet".casefold():
            from .field_value_set import FieldValueSet

            return FieldValueSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileAssessmentRequest".casefold():
            from .file_assessment_request import FileAssessmentRequest

            return FileAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileAttachment".casefold():
            from .file_attachment import FileAttachment

            return FileAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileClassificationRequest".casefold():
            from .file_classification_request import FileClassificationRequest

            return FileClassificationRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileSecurityProfile".casefold():
            from .file_security_profile import FileSecurityProfile

            return FileSecurityProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.filterOperatorSchema".casefold():
            from .filter_operator_schema import FilterOperatorSchema

            return FilterOperatorSchema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.finding".casefold():
            from .finding import Finding

            return Finding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.focusActivityStatistics".casefold():
            from .focus_activity_statistics import FocusActivityStatistics

            return FocusActivityStatistics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpAuthorizationSystem".casefold():
            from .gcp_authorization_system import GcpAuthorizationSystem

            return GcpAuthorizationSystem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpAuthorizationSystemResource".casefold():
            from .gcp_authorization_system_resource import GcpAuthorizationSystemResource

            return GcpAuthorizationSystemResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpAuthorizationSystemTypeAction".casefold():
            from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction

            return GcpAuthorizationSystemTypeAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpCloudFunction".casefold():
            from .gcp_cloud_function import GcpCloudFunction

            return GcpCloudFunction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpGroup".casefold():
            from .gcp_group import GcpGroup

            return GcpGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpIdentity".casefold():
            from .gcp_identity import GcpIdentity

            return GcpIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpRole".casefold():
            from .gcp_role import GcpRole

            return GcpRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpServiceAccount".casefold():
            from .gcp_service_account import GcpServiceAccount

            return GcpServiceAccount()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpUser".casefold():
            from .gcp_user import GcpUser

            return GcpUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.goals".casefold():
            from .goals import Goals

            return Goals()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.goalsExportJob".casefold():
            from .goals_export_job import GoalsExportJob

            return GoalsExportJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.governanceInsight".casefold():
            from .governance_insight import GovernanceInsight

            return GovernanceInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.governancePolicyTemplate".casefold():
            from .governance_policy_template import GovernancePolicyTemplate

            return GovernancePolicyTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.governanceResource".casefold():
            from .governance_resource import GovernanceResource

            return GovernanceResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.governanceRoleAssignment".casefold():
            from .governance_role_assignment import GovernanceRoleAssignment

            return GovernanceRoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.governanceRoleAssignmentRequest".casefold():
            from .governance_role_assignment_request import GovernanceRoleAssignmentRequest

            return GovernanceRoleAssignmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.governanceRoleDefinition".casefold():
            from .governance_role_definition import GovernanceRoleDefinition

            return GovernanceRoleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.governanceRoleSetting".casefold():
            from .governance_role_setting import GovernanceRoleSetting

            return GovernanceRoleSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.governanceSubject".casefold():
            from .governance_subject import GovernanceSubject

            return GovernanceSubject()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.group".casefold():
            from .group import Group
            from .term_store.group import Group

            return Group()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupLifecyclePolicy".casefold():
            from .group_lifecycle_policy import GroupLifecyclePolicy

            return GroupLifecyclePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyCategory".casefold():
            from .group_policy_category import GroupPolicyCategory

            return GroupPolicyCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyConfiguration".casefold():
            from .group_policy_configuration import GroupPolicyConfiguration

            return GroupPolicyConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyConfigurationAssignment".casefold():
            from .group_policy_configuration_assignment import GroupPolicyConfigurationAssignment

            return GroupPolicyConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyDefinition".casefold():
            from .group_policy_definition import GroupPolicyDefinition

            return GroupPolicyDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyDefinitionFile".casefold():
            from .group_policy_definition_file import GroupPolicyDefinitionFile

            return GroupPolicyDefinitionFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyDefinitionValue".casefold():
            from .group_policy_definition_value import GroupPolicyDefinitionValue

            return GroupPolicyDefinitionValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyMigrationReport".casefold():
            from .group_policy_migration_report import GroupPolicyMigrationReport

            return GroupPolicyMigrationReport()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyObjectFile".casefold():
            from .group_policy_object_file import GroupPolicyObjectFile

            return GroupPolicyObjectFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyOperation".casefold():
            from .group_policy_operation import GroupPolicyOperation

            return GroupPolicyOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentation".casefold():
            from .group_policy_presentation import GroupPolicyPresentation

            return GroupPolicyPresentation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationCheckBox".casefold():
            from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox

            return GroupPolicyPresentationCheckBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationComboBox".casefold():
            from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox

            return GroupPolicyPresentationComboBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationDecimalTextBox".casefold():
            from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox

            return GroupPolicyPresentationDecimalTextBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationDropdownList".casefold():
            from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList

            return GroupPolicyPresentationDropdownList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationListBox".casefold():
            from .group_policy_presentation_list_box import GroupPolicyPresentationListBox

            return GroupPolicyPresentationListBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationLongDecimalTextBox".casefold():
            from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox

            return GroupPolicyPresentationLongDecimalTextBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationMultiTextBox".casefold():
            from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox

            return GroupPolicyPresentationMultiTextBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationText".casefold():
            from .group_policy_presentation_text import GroupPolicyPresentationText

            return GroupPolicyPresentationText()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationTextBox".casefold():
            from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox

            return GroupPolicyPresentationTextBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValue".casefold():
            from .group_policy_presentation_value import GroupPolicyPresentationValue

            return GroupPolicyPresentationValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueBoolean".casefold():
            from .group_policy_presentation_value_boolean import GroupPolicyPresentationValueBoolean

            return GroupPolicyPresentationValueBoolean()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueDecimal".casefold():
            from .group_policy_presentation_value_decimal import GroupPolicyPresentationValueDecimal

            return GroupPolicyPresentationValueDecimal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueList".casefold():
            from .group_policy_presentation_value_list import GroupPolicyPresentationValueList

            return GroupPolicyPresentationValueList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueLongDecimal".casefold():
            from .group_policy_presentation_value_long_decimal import GroupPolicyPresentationValueLongDecimal

            return GroupPolicyPresentationValueLongDecimal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueMultiText".casefold():
            from .group_policy_presentation_value_multi_text import GroupPolicyPresentationValueMultiText

            return GroupPolicyPresentationValueMultiText()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueText".casefold():
            from .group_policy_presentation_value_text import GroupPolicyPresentationValueText

            return GroupPolicyPresentationValueText()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicySettingMapping".casefold():
            from .group_policy_setting_mapping import GroupPolicySettingMapping

            return GroupPolicySettingMapping()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyUploadedDefinitionFile".casefold():
            from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile

            return GroupPolicyUploadedDefinitionFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyUploadedPresentation".casefold():
            from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

            return GroupPolicyUploadedPresentation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.hardwareConfiguration".casefold():
            from .hardware_configuration import HardwareConfiguration

            return HardwareConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.hardwareConfigurationAssignment".casefold():
            from .hardware_configuration_assignment import HardwareConfigurationAssignment

            return HardwareConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.hardwareConfigurationDeviceState".casefold():
            from .hardware_configuration_device_state import HardwareConfigurationDeviceState

            return HardwareConfigurationDeviceState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.hardwareConfigurationRunSummary".casefold():
            from .hardware_configuration_run_summary import HardwareConfigurationRunSummary

            return HardwareConfigurationRunSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.hardwareConfigurationUserState".casefold():
            from .hardware_configuration_user_state import HardwareConfigurationUserState

            return HardwareConfigurationUserState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.hardwareOathAuthenticationMethodConfiguration".casefold():
            from .hardware_oath_authentication_method_configuration import HardwareOathAuthenticationMethodConfiguration

            return HardwareOathAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.hardwarePasswordInfo".casefold():
            from .hardware_password_info import HardwarePasswordInfo

            return HardwarePasswordInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.homeRealmDiscoveryPolicy".casefold():
            from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy

            return HomeRealmDiscoveryPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.horizontalSection".casefold():
            from .horizontal_section import HorizontalSection

            return HorizontalSection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.horizontalSectionColumn".casefold():
            from .horizontal_section_column import HorizontalSectionColumn

            return HorizontalSectionColumn()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.hostSecurityProfile".casefold():
            from .host_security_profile import HostSecurityProfile

            return HostSecurityProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityApiConnector".casefold():
            from .identity_api_connector import IdentityApiConnector

            return IdentityApiConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityBuiltInUserFlowAttribute".casefold():
            from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute

            return IdentityBuiltInUserFlowAttribute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityCustomUserFlowAttribute".casefold():
            from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute

            return IdentityCustomUserFlowAttribute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityFinding".casefold():
            from .identity_finding import IdentityFinding

            return IdentityFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.customTaskExtension".casefold():
            from .identity_governance.custom_task_extension import CustomTaskExtension

            return CustomTaskExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.lifecycleManagementSettings".casefold():
            from .identity_governance.lifecycle_management_settings import LifecycleManagementSettings

            return LifecycleManagementSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.lifecycleWorkflowsContainer".casefold():
            from .identity_governance.lifecycle_workflows_container import LifecycleWorkflowsContainer

            return LifecycleWorkflowsContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.run".casefold():
            from .identity_governance.run import Run

            return Run()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.task".casefold():
            from .identity_governance.task import Task

            return Task()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.taskDefinition".casefold():
            from .identity_governance.task_definition import TaskDefinition

            return TaskDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.taskProcessingResult".casefold():
            from .identity_governance.task_processing_result import TaskProcessingResult

            return TaskProcessingResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.taskReport".casefold():
            from .identity_governance.task_report import TaskReport

            return TaskReport()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.userProcessingResult".casefold():
            from .identity_governance.user_processing_result import UserProcessingResult

            return UserProcessingResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.workflowTemplate".casefold():
            from .identity_governance.workflow_template import WorkflowTemplate

            return WorkflowTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityProvider".casefold():
            from .identity_provider import IdentityProvider

            return IdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityProviderBase".casefold():
            from .identity_provider_base import IdentityProviderBase

            return IdentityProviderBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy".casefold():
            from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy

            return IdentitySecurityDefaultsEnforcementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityUserFlow".casefold():
            from .identity_user_flow import IdentityUserFlow

            return IdentityUserFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityUserFlowAttribute".casefold():
            from .identity_user_flow_attribute import IdentityUserFlowAttribute

            return IdentityUserFlowAttribute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityUserFlowAttributeAssignment".casefold():
            from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment

            return IdentityUserFlowAttributeAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.impactedResource".casefold():
            from .impacted_resource import ImpactedResource

            return ImpactedResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.importedAppleDeviceIdentity".casefold():
            from .imported_apple_device_identity import ImportedAppleDeviceIdentity

            return ImportedAppleDeviceIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.importedAppleDeviceIdentityResult".casefold():
            from .imported_apple_device_identity_result import ImportedAppleDeviceIdentityResult

            return ImportedAppleDeviceIdentityResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.importedDeviceIdentity".casefold():
            from .imported_device_identity import ImportedDeviceIdentity

            return ImportedDeviceIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.importedDeviceIdentityResult".casefold():
            from .imported_device_identity_result import ImportedDeviceIdentityResult

            return ImportedDeviceIdentityResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.importedWindowsAutopilotDeviceIdentity".casefold():
            from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity

            return ImportedWindowsAutopilotDeviceIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.importedWindowsAutopilotDeviceIdentityUpload".casefold():
            from .imported_windows_autopilot_device_identity_upload import ImportedWindowsAutopilotDeviceIdentityUpload

            return ImportedWindowsAutopilotDeviceIdentityUpload()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveAwsResourceFinding".casefold():
            from .inactive_aws_resource_finding import InactiveAwsResourceFinding

            return InactiveAwsResourceFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveAwsRoleFinding".casefold():
            from .inactive_aws_role_finding import InactiveAwsRoleFinding

            return InactiveAwsRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveAzureServicePrincipalFinding".casefold():
            from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding

            return InactiveAzureServicePrincipalFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveGcpServiceAccountFinding".casefold():
            from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding

            return InactiveGcpServiceAccountFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveGroupFinding".casefold():
            from .inactive_group_finding import InactiveGroupFinding

            return InactiveGroupFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveServerlessFunctionFinding".casefold():
            from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding

            return InactiveServerlessFunctionFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveUserFinding".casefold():
            from .inactive_user_finding import InactiveUserFinding

            return InactiveUserFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveUsersByApplicationMetricBase".casefold():
            from .inactive_users_by_application_metric_base import InactiveUsersByApplicationMetricBase

            return InactiveUsersByApplicationMetricBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveUsersMetricBase".casefold():
            from .inactive_users_metric_base import InactiveUsersMetricBase

            return InactiveUsersMetricBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.administrativeUnitProvisioningFlow".casefold():
            from .industry_data.administrative_unit_provisioning_flow import AdministrativeUnitProvisioningFlow

            return AdministrativeUnitProvisioningFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.azureDataLakeConnector".casefold():
            from .industry_data.azure_data_lake_connector import AzureDataLakeConnector

            return AzureDataLakeConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.classGroupProvisioningFlow".casefold():
            from .industry_data.class_group_provisioning_flow import ClassGroupProvisioningFlow

            return ClassGroupProvisioningFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.fileDataConnector".casefold():
            from .industry_data.file_data_connector import FileDataConnector

            return FileDataConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.fileValidateOperation".casefold():
            from .industry_data.file_validate_operation import FileValidateOperation

            return FileValidateOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.inboundFileFlow".casefold():
            from .industry_data.inbound_file_flow import InboundFileFlow

            return InboundFileFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.inboundFlow".casefold():
            from .industry_data.inbound_flow import InboundFlow

            return InboundFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.inboundFlowActivity".casefold():
            from .industry_data.inbound_flow_activity import InboundFlowActivity

            return InboundFlowActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.industryDataActivity".casefold():
            from .industry_data.industry_data_activity import IndustryDataActivity

            return IndustryDataActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.industryDataConnector".casefold():
            from .industry_data.industry_data_connector import IndustryDataConnector

            return IndustryDataConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.industryDataRoot".casefold():
            from .industry_data.industry_data_root import IndustryDataRoot

            return IndustryDataRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.industryDataRun".casefold():
            from .industry_data.industry_data_run import IndustryDataRun

            return IndustryDataRun()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.industryDataRunActivity".casefold():
            from .industry_data.industry_data_run_activity import IndustryDataRunActivity

            return IndustryDataRunActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.outboundFlowActivity".casefold():
            from .industry_data.outbound_flow_activity import OutboundFlowActivity

            return OutboundFlowActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.outboundProvisioningFlowSet".casefold():
            from .industry_data.outbound_provisioning_flow_set import OutboundProvisioningFlowSet

            return OutboundProvisioningFlowSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.provisioningFlow".casefold():
            from .industry_data.provisioning_flow import ProvisioningFlow

            return ProvisioningFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.referenceDefinition".casefold():
            from .industry_data.reference_definition import ReferenceDefinition

            return ReferenceDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.roleGroup".casefold():
            from .industry_data.role_group import RoleGroup

            return RoleGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.securityGroupProvisioningFlow".casefold():
            from .industry_data.security_group_provisioning_flow import SecurityGroupProvisioningFlow

            return SecurityGroupProvisioningFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.sourceSystemDefinition".casefold():
            from .industry_data.source_system_definition import SourceSystemDefinition

            return SourceSystemDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.userProvisioningFlow".casefold():
            from .industry_data.user_provisioning_flow import UserProvisioningFlow

            return UserProvisioningFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.validateOperation".casefold():
            from .industry_data.validate_operation import ValidateOperation

            return ValidateOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.yearTimePeriodDefinition".casefold():
            from .industry_data.year_time_period_definition import YearTimePeriodDefinition

            return YearTimePeriodDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inferenceClassification".casefold():
            from .inference_classification import InferenceClassification

            return InferenceClassification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inferenceClassificationOverride".casefold():
            from .inference_classification_override import InferenceClassificationOverride

            return InferenceClassificationOverride()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.informationProtection".casefold():
            from .information_protection import InformationProtection
            from .security.information_protection import InformationProtection

            return InformationProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.informationProtectionLabel".casefold():
            from .information_protection_label import InformationProtectionLabel

            return InformationProtectionLabel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.informationProtectionPolicy".casefold():
            from .information_protection_policy import InformationProtectionPolicy

            return InformationProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.insightsSettings".casefold():
            from .insights_settings import InsightsSettings

            return InsightsSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.insightSummary".casefold():
            from .insight_summary import InsightSummary

            return InsightSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.internalDomainFederation".casefold():
            from .internal_domain_federation import InternalDomainFederation

            return InternalDomainFederation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.internetExplorerMode".casefold():
            from .internet_explorer_mode import InternetExplorerMode

            return InternetExplorerMode()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.intuneBrandingProfile".casefold():
            from .intune_branding_profile import IntuneBrandingProfile

            return IntuneBrandingProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.intuneBrandingProfileAssignment".casefold():
            from .intune_branding_profile_assignment import IntuneBrandingProfileAssignment

            return IntuneBrandingProfileAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.invalidLicenseAlertConfiguration".casefold():
            from .invalid_license_alert_configuration import InvalidLicenseAlertConfiguration

            return InvalidLicenseAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.invalidLicenseAlertIncident".casefold():
            from .invalid_license_alert_incident import InvalidLicenseAlertIncident

            return InvalidLicenseAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.invitation".casefold():
            from .invitation import Invitation

            return Invitation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inviteParticipantsOperation".casefold():
            from .invite_participants_operation import InviteParticipantsOperation

            return InviteParticipantsOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.invokeUserFlowListener".casefold():
            from .invoke_user_flow_listener import InvokeUserFlowListener

            return InvokeUserFlowListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCertificateProfile".casefold():
            from .ios_certificate_profile import IosCertificateProfile

            return IosCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCertificateProfileBase".casefold():
            from .ios_certificate_profile_base import IosCertificateProfileBase

            return IosCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCompliancePolicy".casefold():
            from .ios_compliance_policy import IosCompliancePolicy

            return IosCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCustomConfiguration".casefold():
            from .ios_custom_configuration import IosCustomConfiguration

            return IosCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosDerivedCredentialAuthenticationConfiguration".casefold():
            from .ios_derived_credential_authentication_configuration import IosDerivedCredentialAuthenticationConfiguration

            return IosDerivedCredentialAuthenticationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosDeviceFeaturesConfiguration".casefold():
            from .ios_device_features_configuration import IosDeviceFeaturesConfiguration

            return IosDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEasEmailProfileConfiguration".casefold():
            from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration

            return IosEasEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEducationDeviceConfiguration".casefold():
            from .ios_education_device_configuration import IosEducationDeviceConfiguration

            return IosEducationDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEduDeviceConfiguration".casefold():
            from .ios_edu_device_configuration import IosEduDeviceConfiguration

            return IosEduDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEnterpriseWiFiConfiguration".casefold():
            from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration

            return IosEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosExpeditedCheckinConfiguration".casefold():
            from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration

            return IosExpeditedCheckinConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosGeneralDeviceConfiguration".casefold():
            from .ios_general_device_configuration import IosGeneralDeviceConfiguration

            return IosGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosikEv2VpnConfiguration".casefold():
            from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration

            return IosikEv2VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosImportedPFXCertificateProfile".casefold():
            from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile

            return IosImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosiPadOSWebClip".casefold():
            from .iosi_pad_o_s_web_clip import IosiPadOSWebClip

            return IosiPadOSWebClip()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobApp".casefold():
            from .ios_lob_app import IosLobApp

            return IosLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobAppProvisioningConfiguration".casefold():
            from .ios_lob_app_provisioning_configuration import IosLobAppProvisioningConfiguration

            return IosLobAppProvisioningConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobAppProvisioningConfigurationAssignment".casefold():
            from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment

            return IosLobAppProvisioningConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobAppProvisioningConfigurationPolicySetItem".casefold():
            from .ios_lob_app_provisioning_configuration_policy_set_item import IosLobAppProvisioningConfigurationPolicySetItem

            return IosLobAppProvisioningConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosManagedAppProtection".casefold():
            from .ios_managed_app_protection import IosManagedAppProtection

            return IosManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosManagedAppRegistration".casefold():
            from .ios_managed_app_registration import IosManagedAppRegistration

            return IosManagedAppRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosMobileAppConfiguration".casefold():
            from .ios_mobile_app_configuration import IosMobileAppConfiguration

            return IosMobileAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosPkcsCertificateProfile".casefold():
            from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile

            return IosPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosScepCertificateProfile".casefold():
            from .ios_scep_certificate_profile import IosScepCertificateProfile

            return IosScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosStoreApp".casefold():
            from .ios_store_app import IosStoreApp

            return IosStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosTrustedRootCertificate".casefold():
            from .ios_trusted_root_certificate import IosTrustedRootCertificate

            return IosTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosUpdateConfiguration".casefold():
            from .ios_update_configuration import IosUpdateConfiguration

            return IosUpdateConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosUpdateDeviceStatus".casefold():
            from .ios_update_device_status import IosUpdateDeviceStatus

            return IosUpdateDeviceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVpnConfiguration".casefold():
            from .ios_vpn_configuration import IosVpnConfiguration

            return IosVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppApp".casefold():
            from .ios_vpp_app import IosVppApp

            return IosVppApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppAppAssignedDeviceLicense".casefold():
            from .ios_vpp_app_assigned_device_license import IosVppAppAssignedDeviceLicense

            return IosVppAppAssignedDeviceLicense()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppAppAssignedLicense".casefold():
            from .ios_vpp_app_assigned_license import IosVppAppAssignedLicense

            return IosVppAppAssignedLicense()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppAppAssignedUserLicense".casefold():
            from .ios_vpp_app_assigned_user_license import IosVppAppAssignedUserLicense

            return IosVppAppAssignedUserLicense()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppEBook".casefold():
            from .ios_vpp_e_book import IosVppEBook

            return IosVppEBook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppEBookAssignment".casefold():
            from .ios_vpp_e_book_assignment import IosVppEBookAssignment

            return IosVppEBookAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosWiFiConfiguration".casefold():
            from .ios_wi_fi_configuration import IosWiFiConfiguration

            return IosWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ipApplicationSegment".casefold():
            from .ip_application_segment import IpApplicationSegment

            return IpApplicationSegment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ipNamedLocation".casefold():
            from .ip_named_location import IpNamedLocation

            return IpNamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ipSecurityProfile".casefold():
            from .ip_security_profile import IpSecurityProfile

            return IpSecurityProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemActivity".casefold():
            from .item_activity import ItemActivity

            return ItemActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemActivityOLD".casefold():
            from .item_activity_o_l_d import ItemActivityOLD

            return ItemActivityOLD()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemActivityStat".casefold():
            from .item_activity_stat import ItemActivityStat

            return ItemActivityStat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemAddress".casefold():
            from .item_address import ItemAddress

            return ItemAddress()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemAnalytics".casefold():
            from .item_analytics import ItemAnalytics

            return ItemAnalytics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemAttachment".casefold():
            from .item_attachment import ItemAttachment

            return ItemAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemEmail".casefold():
            from .item_email import ItemEmail

            return ItemEmail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemFacet".casefold():
            from .item_facet import ItemFacet

            return ItemFacet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemInsights".casefold():
            from .item_insights import ItemInsights

            return ItemInsights()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemPatent".casefold():
            from .item_patent import ItemPatent

            return ItemPatent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemPhone".casefold():
            from .item_phone import ItemPhone

            return ItemPhone()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemPublication".casefold():
            from .item_publication import ItemPublication

            return ItemPublication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemRetentionLabel".casefold():
            from .item_retention_label import ItemRetentionLabel

            return ItemRetentionLabel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.jobResponseBase".casefold():
            from .job_response_base import JobResponseBase

            return JobResponseBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.landingPage".casefold():
            from .landing_page import LandingPage

            return LandingPage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.landingPageDetail".casefold():
            from .landing_page_detail import LandingPageDetail

            return LandingPageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.languageProficiency".casefold():
            from .language_proficiency import LanguageProficiency

            return LanguageProficiency()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningAssignment".casefold():
            from .learning_assignment import LearningAssignment

            return LearningAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningContent".casefold():
            from .learning_content import LearningContent

            return LearningContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningCourseActivity".casefold():
            from .learning_course_activity import LearningCourseActivity

            return LearningCourseActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningProvider".casefold():
            from .learning_provider import LearningProvider

            return LearningProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningSelfInitiatedCourse".casefold():
            from .learning_self_initiated_course import LearningSelfInitiatedCourse

            return LearningSelfInitiatedCourse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.licenseDetails".casefold():
            from .license_details import LicenseDetails

            return LicenseDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.linkedResource".casefold():
            from .linked_resource import LinkedResource

            return LinkedResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.list".casefold():
            from .list_ import List_

            return List_()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.listItem".casefold():
            from .list_item import ListItem

            return ListItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.listItemVersion".casefold():
            from .list_item_version import ListItemVersion

            return ListItemVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.localizedNotificationMessage".casefold():
            from .localized_notification_message import LocalizedNotificationMessage

            return LocalizedNotificationMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.loginPage".casefold():
            from .login_page import LoginPage

            return LoginPage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.longRunningOperation".casefold():
            from .long_running_operation import LongRunningOperation

            return LongRunningOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.lookupResultRow".casefold():
            from .lookup_result_row import LookupResultRow

            return LookupResultRow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.m365AppsInstallationOptions".casefold():
            from .m365_apps_installation_options import M365AppsInstallationOptions

            return M365AppsInstallationOptions()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCertificateProfileBase".casefold():
            from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase

            return MacOSCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCompliancePolicy".casefold():
            from .mac_o_s_compliance_policy import MacOSCompliancePolicy

            return MacOSCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCustomAppConfiguration".casefold():
            from .mac_o_s_custom_app_configuration import MacOSCustomAppConfiguration

            return MacOSCustomAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCustomConfiguration".casefold():
            from .mac_o_s_custom_configuration import MacOSCustomConfiguration

            return MacOSCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDeviceFeaturesConfiguration".casefold():
            from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration

            return MacOSDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDmgApp".casefold():
            from .mac_o_s_dmg_app import MacOSDmgApp

            return MacOSDmgApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSEndpointProtectionConfiguration".casefold():
            from .mac_o_s_endpoint_protection_configuration import MacOSEndpointProtectionConfiguration

            return MacOSEndpointProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSEnterpriseWiFiConfiguration".casefold():
            from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration

            return MacOSEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSExtensionsConfiguration".casefold():
            from .mac_o_s_extensions_configuration import MacOSExtensionsConfiguration

            return MacOSExtensionsConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSGeneralDeviceConfiguration".casefold():
            from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration

            return MacOSGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSImportedPFXCertificateProfile".casefold():
            from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile

            return MacOSImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSLobApp".casefold():
            from .mac_o_s_lob_app import MacOSLobApp

            return MacOSLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSMicrosoftDefenderApp".casefold():
            from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp

            return MacOSMicrosoftDefenderApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSMicrosoftEdgeApp".casefold():
            from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp

            return MacOSMicrosoftEdgeApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSOfficeSuiteApp".casefold():
            from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp

            return MacOSOfficeSuiteApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSPkcsCertificateProfile".casefold():
            from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile

            return MacOSPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSPkgApp".casefold():
            from .mac_o_s_pkg_app import MacOSPkgApp

            return MacOSPkgApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSScepCertificateProfile".casefold():
            from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile

            return MacOSScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSSoftwareUpdateAccountSummary".casefold():
            from .mac_o_s_software_update_account_summary import MacOSSoftwareUpdateAccountSummary

            return MacOSSoftwareUpdateAccountSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSSoftwareUpdateCategorySummary".casefold():
            from .mac_o_s_software_update_category_summary import MacOSSoftwareUpdateCategorySummary

            return MacOSSoftwareUpdateCategorySummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSSoftwareUpdateConfiguration".casefold():
            from .mac_o_s_software_update_configuration import MacOSSoftwareUpdateConfiguration

            return MacOSSoftwareUpdateConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSSoftwareUpdateStateSummary".casefold():
            from .mac_o_s_software_update_state_summary import MacOSSoftwareUpdateStateSummary

            return MacOSSoftwareUpdateStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSTrustedRootCertificate".casefold():
            from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate

            return MacOSTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSVpnConfiguration".casefold():
            from .mac_o_s_vpn_configuration import MacOSVpnConfiguration

            return MacOSVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOsVppApp".casefold():
            from .mac_os_vpp_app import MacOsVppApp

            return MacOsVppApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOsVppAppAssignedLicense".casefold():
            from .mac_os_vpp_app_assigned_license import MacOsVppAppAssignedLicense

            return MacOsVppAppAssignedLicense()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSWebClip".casefold():
            from .mac_o_s_web_clip import MacOSWebClip

            return MacOSWebClip()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSWiFiConfiguration".casefold():
            from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration

            return MacOSWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSWiredNetworkConfiguration".casefold():
            from .mac_o_s_wired_network_configuration import MacOSWiredNetworkConfiguration

            return MacOSWiredNetworkConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailAssessmentRequest".casefold():
            from .mail_assessment_request import MailAssessmentRequest

            return MailAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailFolder".casefold():
            from .mail_folder import MailFolder

            return MailFolder()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailSearchFolder".casefold():
            from .mail_search_folder import MailSearchFolder

            return MailSearchFolder()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.malwareStateForWindowsDevice".casefold():
            from .malware_state_for_windows_device import MalwareStateForWindowsDevice

            return MalwareStateForWindowsDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAllDeviceCertificateState".casefold():
            from .managed_all_device_certificate_state import ManagedAllDeviceCertificateState

            return ManagedAllDeviceCertificateState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAndroidLobApp".casefold():
            from .managed_android_lob_app import ManagedAndroidLobApp

            return ManagedAndroidLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAndroidStoreApp".casefold():
            from .managed_android_store_app import ManagedAndroidStoreApp

            return ManagedAndroidStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedApp".casefold():
            from .managed_app import ManagedApp

            return ManagedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppConfiguration".casefold():
            from .managed_app_configuration import ManagedAppConfiguration

            return ManagedAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppLogCollectionRequest".casefold():
            from .managed_app_log_collection_request import ManagedAppLogCollectionRequest

            return ManagedAppLogCollectionRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppOperation".casefold():
            from .managed_app_operation import ManagedAppOperation

            return ManagedAppOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppPolicy".casefold():
            from .managed_app_policy import ManagedAppPolicy

            return ManagedAppPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppPolicyDeploymentSummary".casefold():
            from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary

            return ManagedAppPolicyDeploymentSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppProtection".casefold():
            from .managed_app_protection import ManagedAppProtection

            return ManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppProtectionPolicySetItem".casefold():
            from .managed_app_protection_policy_set_item import ManagedAppProtectionPolicySetItem

            return ManagedAppProtectionPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppRegistration".casefold():
            from .managed_app_registration import ManagedAppRegistration

            return ManagedAppRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppStatus".casefold():
            from .managed_app_status import ManagedAppStatus

            return ManagedAppStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppStatusRaw".casefold():
            from .managed_app_status_raw import ManagedAppStatusRaw

            return ManagedAppStatusRaw()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDevice".casefold():
            from .managed_device import ManagedDevice

            return ManagedDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceCertificateState".casefold():
            from .managed_device_certificate_state import ManagedDeviceCertificateState

            return ManagedDeviceCertificateState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceCleanupRule".casefold():
            from .managed_device_cleanup_rule import ManagedDeviceCleanupRule

            return ManagedDeviceCleanupRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceEncryptionState".casefold():
            from .managed_device_encryption_state import ManagedDeviceEncryptionState

            return ManagedDeviceEncryptionState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfiguration".casefold():
            from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

            return ManagedDeviceMobileAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationAssignment".casefold():
            from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment

            return ManagedDeviceMobileAppConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationDeviceStatus".casefold():
            from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus

            return ManagedDeviceMobileAppConfigurationDeviceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationDeviceSummary".casefold():
            from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary

            return ManagedDeviceMobileAppConfigurationDeviceSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationPolicySetItem".casefold():
            from .managed_device_mobile_app_configuration_policy_set_item import ManagedDeviceMobileAppConfigurationPolicySetItem

            return ManagedDeviceMobileAppConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationState".casefold():
            from .managed_device_mobile_app_configuration_state import ManagedDeviceMobileAppConfigurationState

            return ManagedDeviceMobileAppConfigurationState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationUserStatus".casefold():
            from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus

            return ManagedDeviceMobileAppConfigurationUserStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationUserSummary".casefold():
            from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary

            return ManagedDeviceMobileAppConfigurationUserSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceOverview".casefold():
            from .managed_device_overview import ManagedDeviceOverview

            return ManagedDeviceOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedEBook".casefold():
            from .managed_e_book import ManagedEBook

            return ManagedEBook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedEBookAssignment".casefold():
            from .managed_e_book_assignment import ManagedEBookAssignment

            return ManagedEBookAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedEBookCategory".casefold():
            from .managed_e_book_category import ManagedEBookCategory

            return ManagedEBookCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedIOSLobApp".casefold():
            from .managed_i_o_s_lob_app import ManagedIOSLobApp

            return ManagedIOSLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedIOSStoreApp".casefold():
            from .managed_i_o_s_store_app import ManagedIOSStoreApp

            return ManagedIOSStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedMobileApp".casefold():
            from .managed_mobile_app import ManagedMobileApp

            return ManagedMobileApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedMobileLobApp".casefold():
            from .managed_mobile_lob_app import ManagedMobileLobApp

            return ManagedMobileLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.aggregatedPolicyCompliance".casefold():
            from .managed_tenants.aggregated_policy_compliance import AggregatedPolicyCompliance

            return AggregatedPolicyCompliance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.appPerformance".casefold():
            from .managed_tenants.app_performance import AppPerformance

            return AppPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.auditEvent".casefold():
            from .audit_event import AuditEvent
            from .managed_tenants.audit_event import AuditEvent

            return AuditEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.cloudPcConnection".casefold():
            from .managed_tenants.cloud_pc_connection import CloudPcConnection

            return CloudPcConnection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.cloudPcDevice".casefold():
            from .managed_tenants.cloud_pc_device import CloudPcDevice

            return CloudPcDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.cloudPcOverview".casefold():
            from .managed_tenants.cloud_pc_overview import CloudPcOverview

            return CloudPcOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.conditionalAccessPolicyCoverage".casefold():
            from .managed_tenants.conditional_access_policy_coverage import ConditionalAccessPolicyCoverage

            return ConditionalAccessPolicyCoverage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.credentialUserRegistrationsSummary".casefold():
            from .managed_tenants.credential_user_registrations_summary import CredentialUserRegistrationsSummary

            return CredentialUserRegistrationsSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.deviceAppPerformance".casefold():
            from .managed_tenants.device_app_performance import DeviceAppPerformance

            return DeviceAppPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.deviceCompliancePolicySettingStateSummary".casefold():
            from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
            from .managed_tenants.device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary

            return DeviceCompliancePolicySettingStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.deviceHealthStatus".casefold():
            from .managed_tenants.device_health_status import DeviceHealthStatus

            return DeviceHealthStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managedDeviceCompliance".casefold():
            from .managed_tenants.managed_device_compliance import ManagedDeviceCompliance

            return ManagedDeviceCompliance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managedDeviceComplianceTrend".casefold():
            from .managed_tenants.managed_device_compliance_trend import ManagedDeviceComplianceTrend

            return ManagedDeviceComplianceTrend()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managedTenant".casefold():
            from .managed_tenants.managed_tenant import ManagedTenant

            return ManagedTenant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managedTenantAlert".casefold():
            from .managed_tenants.managed_tenant_alert import ManagedTenantAlert

            return ManagedTenantAlert()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managedTenantAlertLog".casefold():
            from .managed_tenants.managed_tenant_alert_log import ManagedTenantAlertLog

            return ManagedTenantAlertLog()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managedTenantAlertRule".casefold():
            from .managed_tenants.managed_tenant_alert_rule import ManagedTenantAlertRule

            return ManagedTenantAlertRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managedTenantAlertRuleDefinition".casefold():
            from .managed_tenants.managed_tenant_alert_rule_definition import ManagedTenantAlertRuleDefinition

            return ManagedTenantAlertRuleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managedTenantApiNotification".casefold():
            from .managed_tenants.managed_tenant_api_notification import ManagedTenantApiNotification

            return ManagedTenantApiNotification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managedTenantEmailNotification".casefold():
            from .managed_tenants.managed_tenant_email_notification import ManagedTenantEmailNotification

            return ManagedTenantEmailNotification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managedTenantTicketingEndpoint".casefold():
            from .managed_tenants.managed_tenant_ticketing_endpoint import ManagedTenantTicketingEndpoint

            return ManagedTenantTicketingEndpoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managementAction".casefold():
            from .managed_tenants.management_action import ManagementAction

            return ManagementAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managementActionTenantDeploymentStatus".casefold():
            from .managed_tenants.management_action_tenant_deployment_status import ManagementActionTenantDeploymentStatus

            return ManagementActionTenantDeploymentStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managementIntent".casefold():
            from .managed_tenants.management_intent import ManagementIntent

            return ManagementIntent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managementTemplate".casefold():
            from .managed_tenants.management_template import ManagementTemplate

            return ManagementTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managementTemplateCollection".casefold():
            from .managed_tenants.management_template_collection import ManagementTemplateCollection

            return ManagementTemplateCollection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managementTemplateCollectionTenantSummary".casefold():
            from .managed_tenants.management_template_collection_tenant_summary import ManagementTemplateCollectionTenantSummary

            return ManagementTemplateCollectionTenantSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managementTemplateStep".casefold():
            from .managed_tenants.management_template_step import ManagementTemplateStep

            return ManagementTemplateStep()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managementTemplateStepDeployment".casefold():
            from .managed_tenants.management_template_step_deployment import ManagementTemplateStepDeployment

            return ManagementTemplateStepDeployment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managementTemplateStepTenantSummary".casefold():
            from .managed_tenants.management_template_step_tenant_summary import ManagementTemplateStepTenantSummary

            return ManagementTemplateStepTenantSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.managementTemplateStepVersion".casefold():
            from .managed_tenants.management_template_step_version import ManagementTemplateStepVersion

            return ManagementTemplateStepVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.tenant".casefold():
            from .managed_tenants.tenant import Tenant

            return Tenant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.tenantCustomizedInformation".casefold():
            from .managed_tenants.tenant_customized_information import TenantCustomizedInformation

            return TenantCustomizedInformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.tenantDetailedInformation".casefold():
            from .managed_tenants.tenant_detailed_information import TenantDetailedInformation

            return TenantDetailedInformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.tenantGroup".casefold():
            from .managed_tenants.tenant_group import TenantGroup

            return TenantGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.tenantTag".casefold():
            from .managed_tenants.tenant_tag import TenantTag

            return TenantTag()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.windowsDeviceMalwareState".casefold():
            from .managed_tenants.windows_device_malware_state import WindowsDeviceMalwareState
            from .windows_device_malware_state import WindowsDeviceMalwareState

            return WindowsDeviceMalwareState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedTenants.windowsProtectionState".casefold():
            from .managed_tenants.windows_protection_state import WindowsProtectionState
            from .windows_protection_state import WindowsProtectionState

            return WindowsProtectionState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mdmWindowsInformationProtectionPolicy".casefold():
            from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy

            return MdmWindowsInformationProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mdmWindowsInformationProtectionPolicyPolicySetItem".casefold():
            from .mdm_windows_information_protection_policy_policy_set_item import MdmWindowsInformationProtectionPolicyPolicySetItem

            return MdmWindowsInformationProtectionPolicyPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingActivityStatistics".casefold():
            from .meeting_activity_statistics import MeetingActivityStatistics

            return MeetingActivityStatistics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingAttendanceReport".casefold():
            from .meeting_attendance_report import MeetingAttendanceReport

            return MeetingAttendanceReport()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingRegistrant".casefold():
            from .meeting_registrant import MeetingRegistrant

            return MeetingRegistrant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingRegistrantBase".casefold():
            from .meeting_registrant_base import MeetingRegistrantBase

            return MeetingRegistrantBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingRegistration".casefold():
            from .meeting_registration import MeetingRegistration

            return MeetingRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingRegistrationBase".casefold():
            from .meeting_registration_base import MeetingRegistrationBase

            return MeetingRegistrationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingRegistrationQuestion".casefold():
            from .meeting_registration_question import MeetingRegistrationQuestion

            return MeetingRegistrationQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.membershipOutlierInsight".casefold():
            from .membership_outlier_insight import MembershipOutlierInsight

            return MembershipOutlierInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mention".casefold():
            from .mention import Mention

            return Mention()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.message".casefold():
            from .message import Message

            return Message()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.messageEvent".casefold():
            from .message_event import MessageEvent

            return MessageEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.messageRecipient".casefold():
            from .message_recipient import MessageRecipient

            return MessageRecipient()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.messageRule".casefold():
            from .message_rule import MessageRule

            return MessageRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.messageTrace".casefold():
            from .message_trace import MessageTrace

            return MessageTrace()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mfaCompletionMetric".casefold():
            from .mfa_completion_metric import MfaCompletionMetric

            return MfaCompletionMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mfaFailure".casefold():
            from .mfa_failure import MfaFailure

            return MfaFailure()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAccountUserConversationMember".casefold():
            from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember

            return MicrosoftAccountUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftApplicationDataAccessSettings".casefold():
            from .microsoft_application_data_access_settings import MicrosoftApplicationDataAccessSettings

            return MicrosoftApplicationDataAccessSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod".casefold():
            from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod

            return MicrosoftAuthenticatorAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodConfiguration".casefold():
            from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration

            return MicrosoftAuthenticatorAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodTarget".casefold():
            from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget

            return MicrosoftAuthenticatorAuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftStoreForBusinessApp".casefold():
            from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp

            return MicrosoftStoreForBusinessApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftStoreForBusinessContainedApp".casefold():
            from .microsoft_store_for_business_contained_app import MicrosoftStoreForBusinessContainedApp

            return MicrosoftStoreForBusinessContainedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftTunnelConfiguration".casefold():
            from .microsoft_tunnel_configuration import MicrosoftTunnelConfiguration

            return MicrosoftTunnelConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftTunnelHealthThreshold".casefold():
            from .microsoft_tunnel_health_threshold import MicrosoftTunnelHealthThreshold

            return MicrosoftTunnelHealthThreshold()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftTunnelServer".casefold():
            from .microsoft_tunnel_server import MicrosoftTunnelServer

            return MicrosoftTunnelServer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftTunnelServerLogCollectionResponse".casefold():
            from .microsoft_tunnel_server_log_collection_response import MicrosoftTunnelServerLogCollectionResponse

            return MicrosoftTunnelServerLogCollectionResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftTunnelSite".casefold():
            from .microsoft_tunnel_site import MicrosoftTunnelSite

            return MicrosoftTunnelSite()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileApp".casefold():
            from .mobile_app import MobileApp

            return MobileApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppAssignment".casefold():
            from .mobile_app_assignment import MobileAppAssignment

            return MobileAppAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppCatalogPackage".casefold():
            from .mobile_app_catalog_package import MobileAppCatalogPackage

            return MobileAppCatalogPackage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppCategory".casefold():
            from .mobile_app_category import MobileAppCategory

            return MobileAppCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppContent".casefold():
            from .mobile_app_content import MobileAppContent

            return MobileAppContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppContentFile".casefold():
            from .mobile_app_content_file import MobileAppContentFile

            return MobileAppContentFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppDependency".casefold():
            from .mobile_app_dependency import MobileAppDependency

            return MobileAppDependency()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppInstallStatus".casefold():
            from .mobile_app_install_status import MobileAppInstallStatus

            return MobileAppInstallStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppInstallSummary".casefold():
            from .mobile_app_install_summary import MobileAppInstallSummary

            return MobileAppInstallSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppIntentAndState".casefold():
            from .mobile_app_intent_and_state import MobileAppIntentAndState

            return MobileAppIntentAndState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppPolicySetItem".casefold():
            from .mobile_app_policy_set_item import MobileAppPolicySetItem

            return MobileAppPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppProvisioningConfigGroupAssignment".casefold():
            from .mobile_app_provisioning_config_group_assignment import MobileAppProvisioningConfigGroupAssignment

            return MobileAppProvisioningConfigGroupAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppRelationship".casefold():
            from .mobile_app_relationship import MobileAppRelationship

            return MobileAppRelationship()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppSupersedence".casefold():
            from .mobile_app_supersedence import MobileAppSupersedence

            return MobileAppSupersedence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppTroubleshootingEvent".casefold():
            from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent

            return MobileAppTroubleshootingEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileContainedApp".casefold():
            from .mobile_contained_app import MobileContainedApp

            return MobileContainedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileLobApp".casefold():
            from .mobile_lob_app import MobileLobApp

            return MobileLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileThreatDefenseConnector".casefold():
            from .mobile_threat_defense_connector import MobileThreatDefenseConnector

            return MobileThreatDefenseConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobilityManagementPolicy".casefold():
            from .mobility_management_policy import MobilityManagementPolicy

            return MobilityManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.monthlyInactiveUsersByApplicationMetric".casefold():
            from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric

            return MonthlyInactiveUsersByApplicationMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.monthlyInactiveUsersMetric".casefold():
            from .monthly_inactive_users_metric import MonthlyInactiveUsersMetric

            return MonthlyInactiveUsersMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.monthlyUserInsightMetricsRoot".casefold():
            from .monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot

            return MonthlyUserInsightMetricsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiTenantOrganization".casefold():
            from .multi_tenant_organization import MultiTenantOrganization

            return MultiTenantOrganization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiTenantOrganizationIdentitySyncPolicyTemplate".casefold():
            from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate

            return MultiTenantOrganizationIdentitySyncPolicyTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiTenantOrganizationJoinRequestRecord".casefold():
            from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord

            return MultiTenantOrganizationJoinRequestRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiTenantOrganizationMember".casefold():
            from .multi_tenant_organization_member import MultiTenantOrganizationMember

            return MultiTenantOrganizationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiTenantOrganizationPartnerConfigurationTemplate".casefold():
            from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate

            return MultiTenantOrganizationPartnerConfigurationTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiValueLegacyExtendedProperty".casefold():
            from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty

            return MultiValueLegacyExtendedProperty()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.muteParticipantOperation".casefold():
            from .mute_participant_operation import MuteParticipantOperation

            return MuteParticipantOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.muteParticipantsOperation".casefold():
            from .mute_participants_operation import MuteParticipantsOperation

            return MuteParticipantsOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.namedLocation".casefold():
            from .named_location import NamedLocation

            return NamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ndesConnector".casefold():
            from .ndes_connector import NdesConnector

            return NdesConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.alert".casefold():
            from .alert import Alert
            from .networkaccess.alert import Alert
            from .security.alert import Alert

            return Alert()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.branchSite".casefold():
            from .networkaccess.branch_site import BranchSite

            return BranchSite()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.conditionalAccessPolicy".casefold():
            from .conditional_access_policy import ConditionalAccessPolicy
            from .networkaccess.conditional_access_policy import ConditionalAccessPolicy

            return ConditionalAccessPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.conditionalAccessSettings".casefold():
            from .networkaccess.conditional_access_settings import ConditionalAccessSettings

            return ConditionalAccessSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.connectivity".casefold():
            from .networkaccess.connectivity import Connectivity

            return Connectivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.connectivityConfigurationLink".casefold():
            from .networkaccess.connectivity_configuration_link import ConnectivityConfigurationLink

            return ConnectivityConfigurationLink()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.crossTenantAccessSettings".casefold():
            from .networkaccess.cross_tenant_access_settings import CrossTenantAccessSettings

            return CrossTenantAccessSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.deviceLink".casefold():
            from .networkaccess.device_link import DeviceLink

            return DeviceLink()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.enrichedAuditLogs".casefold():
            from .networkaccess.enriched_audit_logs import EnrichedAuditLogs

            return EnrichedAuditLogs()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.filteringPolicy".casefold():
            from .networkaccess.filtering_policy import FilteringPolicy

            return FilteringPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.filteringPolicyLink".casefold():
            from .networkaccess.filtering_policy_link import FilteringPolicyLink

            return FilteringPolicyLink()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.filteringProfile".casefold():
            from .networkaccess.filtering_profile import FilteringProfile

            return FilteringProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.filteringRule".casefold():
            from .networkaccess.filtering_rule import FilteringRule

            return FilteringRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingOptions".casefold():
            from .networkaccess.forwarding_options import ForwardingOptions

            return ForwardingOptions()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingPolicy".casefold():
            from .networkaccess.forwarding_policy import ForwardingPolicy

            return ForwardingPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingPolicyLink".casefold():
            from .networkaccess.forwarding_policy_link import ForwardingPolicyLink

            return ForwardingPolicyLink()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingProfile".casefold():
            from .networkaccess.forwarding_profile import ForwardingProfile

            return ForwardingProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingRule".casefold():
            from .networkaccess.forwarding_rule import ForwardingRule

            return ForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.fqdnFilteringRule".casefold():
            from .networkaccess.fqdn_filtering_rule import FqdnFilteringRule

            return FqdnFilteringRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.internetAccessForwardingRule".casefold():
            from .networkaccess.internet_access_forwarding_rule import InternetAccessForwardingRule

            return InternetAccessForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.logs".casefold():
            from .networkaccess.logs import Logs

            return Logs()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.m365ForwardingRule".casefold():
            from .networkaccess.m365_forwarding_rule import M365ForwardingRule

            return M365ForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.networkAccessRoot".casefold():
            from .networkaccess.network_access_root import NetworkAccessRoot

            return NetworkAccessRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.policy".casefold():
            from .networkaccess.policy import Policy

            return Policy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.policyLink".casefold():
            from .networkaccess.policy_link import PolicyLink

            return PolicyLink()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.policyRule".casefold():
            from .networkaccess.policy_rule import PolicyRule

            return PolicyRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.privateAccessForwardingRule".casefold():
            from .networkaccess.private_access_forwarding_rule import PrivateAccessForwardingRule

            return PrivateAccessForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.profile".casefold():
            from .networkaccess.profile import Profile
            from .profile import Profile

            return Profile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.remoteNetwork".casefold():
            from .networkaccess.remote_network import RemoteNetwork

            return RemoteNetwork()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.remoteNetworkHealthEvent".casefold():
            from .networkaccess.remote_network_health_event import RemoteNetworkHealthEvent

            return RemoteNetworkHealthEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.reports".casefold():
            from .networkaccess.reports import Reports

            return Reports()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.settings".casefold():
            from .networkaccess.settings import Settings

            return Settings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.tenantStatus".casefold():
            from .networkaccess.tenant_status import TenantStatus

            return TenantStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.webCategoryFilteringRule".casefold():
            from .networkaccess.web_category_filtering_rule import WebCategoryFilteringRule

            return WebCategoryFilteringRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.newsLinkPage".casefold():
            from .news_link_page import NewsLinkPage

            return NewsLinkPage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.noMfaOnRoleActivationAlertConfiguration".casefold():
            from .no_mfa_on_role_activation_alert_configuration import NoMfaOnRoleActivationAlertConfiguration

            return NoMfaOnRoleActivationAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.noMfaOnRoleActivationAlertIncident".casefold():
            from .no_mfa_on_role_activation_alert_incident import NoMfaOnRoleActivationAlertIncident

            return NoMfaOnRoleActivationAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.note".casefold():
            from .note import Note

            return Note()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.notebook".casefold():
            from .notebook import Notebook

            return Notebook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.notification".casefold():
            from .notification import Notification

            return Notification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.notificationMessageTemplate".casefold():
            from .notification_message_template import NotificationMessageTemplate

            return NotificationMessageTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.oAuth2PermissionGrant".casefold():
            from .o_auth2_permission_grant import OAuth2PermissionGrant

            return OAuth2PermissionGrant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.offerShiftRequest".casefold():
            from .offer_shift_request import OfferShiftRequest

            return OfferShiftRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.office365ActiveUserCounts".casefold():
            from .office365_active_user_counts import Office365ActiveUserCounts

            return Office365ActiveUserCounts()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.office365ActiveUserDetail".casefold():
            from .office365_active_user_detail import Office365ActiveUserDetail

            return Office365ActiveUserDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.office365GroupsActivityCounts".casefold():
            from .office365_groups_activity_counts import Office365GroupsActivityCounts

            return Office365GroupsActivityCounts()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.office365GroupsActivityDetail".casefold():
            from .office365_groups_activity_detail import Office365GroupsActivityDetail

            return Office365GroupsActivityDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.office365GroupsActivityFileCounts".casefold():
            from .office365_groups_activity_file_counts import Office365GroupsActivityFileCounts

            return Office365GroupsActivityFileCounts()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.office365GroupsActivityGroupCounts".casefold():
            from .office365_groups_activity_group_counts import Office365GroupsActivityGroupCounts

            return Office365GroupsActivityGroupCounts()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.office365GroupsActivityStorage".casefold():
            from .office365_groups_activity_storage import Office365GroupsActivityStorage

            return Office365GroupsActivityStorage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.office365ServicesUserCounts".casefold():
            from .office365_services_user_counts import Office365ServicesUserCounts

            return Office365ServicesUserCounts()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.officeGraphInsights".casefold():
            from .office_graph_insights import OfficeGraphInsights

            return OfficeGraphInsights()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.officeSuiteApp".casefold():
            from .office_suite_app import OfficeSuiteApp

            return OfficeSuiteApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionListener".casefold():
            from .on_attribute_collection_listener import OnAttributeCollectionListener

            return OnAttributeCollectionListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionStartCustomExtension".casefold():
            from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension

            return OnAttributeCollectionStartCustomExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionStartListener".casefold():
            from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener

            return OnAttributeCollectionStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionSubmitCustomExtension".casefold():
            from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension

            return OnAttributeCollectionSubmitCustomExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionSubmitListener".casefold():
            from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener

            return OnAttributeCollectionSubmitListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAuthenticationMethodLoadStartListener".casefold():
            from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener

            return OnAuthenticationMethodLoadStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenote".casefold():
            from .onenote import Onenote

            return Onenote()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteEntityBaseModel".casefold():
            from .onenote_entity_base_model import OnenoteEntityBaseModel

            return OnenoteEntityBaseModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteEntityHierarchyModel".casefold():
            from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel

            return OnenoteEntityHierarchyModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteEntitySchemaObjectModel".casefold():
            from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel

            return OnenoteEntitySchemaObjectModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteOperation".casefold():
            from .onenote_operation import OnenoteOperation

            return OnenoteOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenotePage".casefold():
            from .onenote_page import OnenotePage

            return OnenotePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteResource".casefold():
            from .onenote_resource import OnenoteResource

            return OnenoteResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteSection".casefold():
            from .onenote_section import OnenoteSection

            return OnenoteSection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onInteractiveAuthFlowStartListener".casefold():
            from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener

            return OnInteractiveAuthFlowStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onlineMeeting".casefold():
            from .online_meeting import OnlineMeeting

            return OnlineMeeting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onlineMeetingBase".casefold():
            from .online_meeting_base import OnlineMeetingBase

            return OnlineMeetingBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onPremisesAgent".casefold():
            from .on_premises_agent import OnPremisesAgent

            return OnPremisesAgent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onPremisesAgentGroup".casefold():
            from .on_premises_agent_group import OnPremisesAgentGroup

            return OnPremisesAgentGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onPremisesConditionalAccessSettings".casefold():
            from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings

            return OnPremisesConditionalAccessSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onPremisesDirectorySynchronization".casefold():
            from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization

            return OnPremisesDirectorySynchronization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onPremisesPublishingProfile".casefold():
            from .on_premises_publishing_profile import OnPremisesPublishingProfile

            return OnPremisesPublishingProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onTokenIssuanceStartCustomExtension".casefold():
            from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

            return OnTokenIssuanceStartCustomExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onTokenIssuanceStartListener".casefold():
            from .on_token_issuance_start_listener import OnTokenIssuanceStartListener

            return OnTokenIssuanceStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onUserCreateStartListener".casefold():
            from .on_user_create_start_listener import OnUserCreateStartListener

            return OnUserCreateStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openAwsSecurityGroupFinding".casefold():
            from .open_aws_security_group_finding import OpenAwsSecurityGroupFinding

            return OpenAwsSecurityGroupFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openIdConnectIdentityProvider".casefold():
            from .open_id_connect_identity_provider import OpenIdConnectIdentityProvider

            return OpenIdConnectIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openIdConnectProvider".casefold():
            from .open_id_connect_provider import OpenIdConnectProvider

            return OpenIdConnectProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openNetworkAzureSecurityGroupFinding".casefold():
            from .open_network_azure_security_group_finding import OpenNetworkAzureSecurityGroupFinding

            return OpenNetworkAzureSecurityGroupFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShift".casefold():
            from .open_shift import OpenShift

            return OpenShift()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShiftChangeRequest".casefold():
            from .open_shift_change_request import OpenShiftChangeRequest

            return OpenShiftChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openTypeExtension".casefold():
            from .open_type_extension import OpenTypeExtension

            return OpenTypeExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.operation".casefold():
            from .operation import Operation
            from .partners.billing.operation import Operation

            return Operation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.operationApprovalPolicy".casefold():
            from .operation_approval_policy import OperationApprovalPolicy

            return OperationApprovalPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.operationApprovalRequest".casefold():
            from .operation_approval_request import OperationApprovalRequest

            return OperationApprovalRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organization".casefold():
            from .organization import Organization

            return Organization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organizationalBranding".casefold():
            from .organizational_branding import OrganizationalBranding

            return OrganizationalBranding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organizationalBrandingLocalization".casefold():
            from .organizational_branding_localization import OrganizationalBrandingLocalization

            return OrganizationalBrandingLocalization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organizationalBrandingProperties".casefold():
            from .organizational_branding_properties import OrganizationalBrandingProperties

            return OrganizationalBrandingProperties()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organizationSettings".casefold():
            from .organization_settings import OrganizationSettings

            return OrganizationSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.orgContact".casefold():
            from .org_contact import OrgContact

            return OrgContact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outlookCategory".casefold():
            from .outlook_category import OutlookCategory

            return OutlookCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outlookItem".casefold():
            from .outlook_item import OutlookItem

            return OutlookItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outlookTask".casefold():
            from .outlook_task import OutlookTask

            return OutlookTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outlookTaskFolder".casefold():
            from .outlook_task_folder import OutlookTaskFolder

            return OutlookTaskFolder()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outlookTaskGroup".casefold():
            from .outlook_task_group import OutlookTaskGroup

            return OutlookTaskGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outlookUser".casefold():
            from .outlook_user import OutlookUser

            return OutlookUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.overprovisionedAwsResourceFinding".casefold():
            from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding

            return OverprovisionedAwsResourceFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.overprovisionedAwsRoleFinding".casefold():
            from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding

            return OverprovisionedAwsRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.overprovisionedAzureServicePrincipalFinding".casefold():
            from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding

            return OverprovisionedAzureServicePrincipalFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.overprovisionedGcpServiceAccountFinding".casefold():
            from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding

            return OverprovisionedGcpServiceAccountFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.overprovisionedServerlessFunctionFinding".casefold():
            from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding

            return OverprovisionedServerlessFunctionFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.overprovisionedUserFinding".casefold():
            from .overprovisioned_user_finding import OverprovisionedUserFinding

            return OverprovisionedUserFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.participant".casefold():
            from .call_records.participant import Participant
            from .participant import Participant

            return Participant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.participantJoiningNotification".casefold():
            from .participant_joining_notification import ParticipantJoiningNotification

            return ParticipantJoiningNotification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.participantLeftNotification".casefold():
            from .participant_left_notification import ParticipantLeftNotification

            return ParticipantLeftNotification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners".casefold():
            from .partners.partners import Partners

            return Partners()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.azureUsage".casefold():
            from .partners.billing.azure_usage import AzureUsage

            return AzureUsage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.billedReconciliation".casefold():
            from .partners.billing.billed_reconciliation import BilledReconciliation

            return BilledReconciliation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.billedUsage".casefold():
            from .partners.billing.billed_usage import BilledUsage

            return BilledUsage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.billing".casefold():
            from .partners.billing.billing import Billing

            return Billing()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.billingReconciliation".casefold():
            from .partners.billing.billing_reconciliation import BillingReconciliation

            return BillingReconciliation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.exportSuccessOperation".casefold():
            from .partners.billing.export_success_operation import ExportSuccessOperation

            return ExportSuccessOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.failedOperation".casefold():
            from .partners.billing.failed_operation import FailedOperation

            return FailedOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.manifest".casefold():
            from .partners.billing.manifest import Manifest

            return Manifest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.operation".casefold():
            from .operation import Operation
            from .partners.billing.operation import Operation

            return Operation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.runningOperation".casefold():
            from .partners.billing.running_operation import RunningOperation

            return RunningOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.unbilledUsage".casefold():
            from .partners.billing.unbilled_usage import UnbilledUsage

            return UnbilledUsage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.passwordAuthenticationMethod".casefold():
            from .password_authentication_method import PasswordAuthenticationMethod

            return PasswordAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.passwordlessMicrosoftAuthenticatorAuthenticationMethod".casefold():
            from .passwordless_microsoft_authenticator_authentication_method import PasswordlessMicrosoftAuthenticatorAuthenticationMethod

            return PasswordlessMicrosoftAuthenticatorAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.payload".casefold():
            from .payload import Payload

            return Payload()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.payloadCompatibleAssignmentFilter".casefold():
            from .payload_compatible_assignment_filter import PayloadCompatibleAssignmentFilter

            return PayloadCompatibleAssignmentFilter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.payloadResponse".casefold():
            from .payload_response import PayloadResponse

            return PayloadResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.pendingExternalUserProfile".casefold():
            from .pending_external_user_profile import PendingExternalUserProfile

            return PendingExternalUserProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.peopleAdminSettings".casefold():
            from .people_admin_settings import PeopleAdminSettings

            return PeopleAdminSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permission".casefold():
            from .permission import Permission

            return Permission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionGrantConditionSet".casefold():
            from .permission_grant_condition_set import PermissionGrantConditionSet

            return PermissionGrantConditionSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionGrantPolicy".casefold():
            from .permission_grant_policy import PermissionGrantPolicy

            return PermissionGrantPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionsAnalytics".casefold():
            from .permissions_analytics import PermissionsAnalytics

            return PermissionsAnalytics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionsAnalyticsAggregation".casefold():
            from .permissions_analytics_aggregation import PermissionsAnalyticsAggregation

            return PermissionsAnalyticsAggregation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionsCreepIndexDistribution".casefold():
            from .permissions_creep_index_distribution import PermissionsCreepIndexDistribution

            return PermissionsCreepIndexDistribution()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionsDefinitionAwsPolicy".casefold():
            from .permissions_definition_aws_policy import PermissionsDefinitionAwsPolicy

            return PermissionsDefinitionAwsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionsDefinitionAzureRole".casefold():
            from .permissions_definition_azure_role import PermissionsDefinitionAzureRole

            return PermissionsDefinitionAzureRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionsDefinitionGcpRole".casefold():
            from .permissions_definition_gcp_role import PermissionsDefinitionGcpRole

            return PermissionsDefinitionGcpRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionsManagement".casefold():
            from .permissions_management import PermissionsManagement

            return PermissionsManagement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionsRequestChange".casefold():
            from .permissions_request_change import PermissionsRequestChange

            return PermissionsRequestChange()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.person".casefold():
            from .person import Person

            return Person()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personAnnotation".casefold():
            from .person_annotation import PersonAnnotation

            return PersonAnnotation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personAnnualEvent".casefold():
            from .person_annual_event import PersonAnnualEvent

            return PersonAnnualEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personAward".casefold():
            from .person_award import PersonAward

            return PersonAward()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personCertification".casefold():
            from .person_certification import PersonCertification

            return PersonCertification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personExtension".casefold():
            from .person_extension import PersonExtension

            return PersonExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personInterest".casefold():
            from .person_interest import PersonInterest

            return PersonInterest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personName".casefold():
            from .person_name import PersonName

            return PersonName()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personResponsibility".casefold():
            from .person_responsibility import PersonResponsibility

            return PersonResponsibility()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personWebsite".casefold():
            from .person_website import PersonWebsite

            return PersonWebsite()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.phoneAuthenticationMethod".casefold():
            from .phone_authentication_method import PhoneAuthenticationMethod

            return PhoneAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.pinnedChatMessageInfo".casefold():
            from .pinned_chat_message_info import PinnedChatMessageInfo

            return PinnedChatMessageInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.place".casefold():
            from .place import Place

            return Place()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.planner".casefold():
            from .planner import Planner

            return Planner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerAssignedToTaskBoardTaskFormat".casefold():
            from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat

            return PlannerAssignedToTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerBucket".casefold():
            from .planner_bucket import PlannerBucket

            return PlannerBucket()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerBucketTaskBoardTaskFormat".casefold():
            from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat

            return PlannerBucketTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerDelta".casefold():
            from .planner_delta import PlannerDelta

            return PlannerDelta()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerGroup".casefold():
            from .planner_group import PlannerGroup

            return PlannerGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerPlan".casefold():
            from .planner_plan import PlannerPlan

            return PlannerPlan()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerPlanConfiguration".casefold():
            from .planner_plan_configuration import PlannerPlanConfiguration

            return PlannerPlanConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerPlanConfigurationLocalization".casefold():
            from .planner_plan_configuration_localization import PlannerPlanConfigurationLocalization

            return PlannerPlanConfigurationLocalization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerPlanDetails".casefold():
            from .planner_plan_details import PlannerPlanDetails

            return PlannerPlanDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerProgressTaskBoardTaskFormat".casefold():
            from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat

            return PlannerProgressTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerRoster".casefold():
            from .planner_roster import PlannerRoster

            return PlannerRoster()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerRosterMember".casefold():
            from .planner_roster_member import PlannerRosterMember

            return PlannerRosterMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerTask".casefold():
            from .planner_task import PlannerTask

            return PlannerTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerTaskConfiguration".casefold():
            from .planner_task_configuration import PlannerTaskConfiguration

            return PlannerTaskConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerTaskDetails".casefold():
            from .planner_task_details import PlannerTaskDetails

            return PlannerTaskDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerUser".casefold():
            from .planner_user import PlannerUser

            return PlannerUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.platformCredentialAuthenticationMethod".casefold():
            from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod

            return PlatformCredentialAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.playPromptOperation".casefold():
            from .play_prompt_operation import PlayPromptOperation

            return PlayPromptOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policyBase".casefold():
            from .policy_base import PolicyBase
            from .security.policy_base import PolicyBase

            return PolicyBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policyRoot".casefold():
            from .policy_root import PolicyRoot

            return PolicyRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policySet".casefold():
            from .policy_set import PolicySet

            return PolicySet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policySetAssignment".casefold():
            from .policy_set_assignment import PolicySetAssignment

            return PolicySetAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policySetItem".casefold():
            from .policy_set_item import PolicySetItem

            return PolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policyTemplate".casefold():
            from .policy_template import PolicyTemplate

            return PolicyTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.post".casefold():
            from .post import Post

            return Post()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.presence".casefold():
            from .presence import Presence

            return Presence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.presentation".casefold():
            from .presentation import Presentation

            return Presentation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printConnector".casefold():
            from .print_connector import PrintConnector

            return PrintConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printDocument".casefold():
            from .print_document import PrintDocument

            return PrintDocument()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printer".casefold():
            from .printer import Printer

            return Printer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printerBase".casefold():
            from .printer_base import PrinterBase

            return PrinterBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printerCreateOperation".casefold():
            from .printer_create_operation import PrinterCreateOperation

            return PrinterCreateOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printerShare".casefold():
            from .printer_share import PrinterShare

            return PrinterShare()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printJob".casefold():
            from .print_job import PrintJob

            return PrintJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printOperation".casefold():
            from .print_operation import PrintOperation

            return PrintOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printService".casefold():
            from .print_service import PrintService

            return PrintService()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printServiceEndpoint".casefold():
            from .print_service_endpoint import PrintServiceEndpoint

            return PrintServiceEndpoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printTask".casefold():
            from .print_task import PrintTask

            return PrintTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printTaskDefinition".casefold():
            from .print_task_definition import PrintTaskDefinition

            return PrintTaskDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printTaskTrigger".casefold():
            from .print_task_trigger import PrintTaskTrigger

            return PrintTaskTrigger()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printUsage".casefold():
            from .print_usage import PrintUsage

            return PrintUsage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printUsageByPrinter".casefold():
            from .print_usage_by_printer import PrintUsageByPrinter

            return PrintUsageByPrinter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printUsageByUser".casefold():
            from .print_usage_by_user import PrintUsageByUser

            return PrintUsageByUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccess".casefold():
            from .privileged_access import PrivilegedAccess

            return PrivilegedAccess()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroup".casefold():
            from .privileged_access_group import PrivilegedAccessGroup

            return PrivilegedAccessGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupAssignmentSchedule".casefold():
            from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule

            return PrivilegedAccessGroupAssignmentSchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupAssignmentScheduleInstance".casefold():
            from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance

            return PrivilegedAccessGroupAssignmentScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupAssignmentScheduleRequest".casefold():
            from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest

            return PrivilegedAccessGroupAssignmentScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupEligibilitySchedule".casefold():
            from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule

            return PrivilegedAccessGroupEligibilitySchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupEligibilityScheduleInstance".casefold():
            from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance

            return PrivilegedAccessGroupEligibilityScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest".casefold():
            from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest

            return PrivilegedAccessGroupEligibilityScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessRoot".casefold():
            from .privileged_access_root import PrivilegedAccessRoot

            return PrivilegedAccessRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessSchedule".casefold():
            from .privileged_access_schedule import PrivilegedAccessSchedule

            return PrivilegedAccessSchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessScheduleInstance".casefold():
            from .privileged_access_schedule_instance import PrivilegedAccessScheduleInstance

            return PrivilegedAccessScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessScheduleRequest".casefold():
            from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest

            return PrivilegedAccessScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedApproval".casefold():
            from .privileged_approval import PrivilegedApproval

            return PrivilegedApproval()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedOperationEvent".casefold():
            from .privileged_operation_event import PrivilegedOperationEvent

            return PrivilegedOperationEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedRole".casefold():
            from .privileged_role import PrivilegedRole

            return PrivilegedRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedRoleAssignment".casefold():
            from .privileged_role_assignment import PrivilegedRoleAssignment

            return PrivilegedRoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedRoleAssignmentRequest".casefold():
            from .privileged_role_assignment_request import PrivilegedRoleAssignmentRequest

            return PrivilegedRoleAssignmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedRoleSettings".casefold():
            from .privileged_role_settings import PrivilegedRoleSettings

            return PrivilegedRoleSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedRoleSummary".casefold():
            from .privileged_role_summary import PrivilegedRoleSummary

            return PrivilegedRoleSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedSignupStatus".casefold():
            from .privileged_signup_status import PrivilegedSignupStatus

            return PrivilegedSignupStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalation".casefold():
            from .privilege_escalation import PrivilegeEscalation

            return PrivilegeEscalation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationAwsResourceFinding".casefold():
            from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding

            return PrivilegeEscalationAwsResourceFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationAwsRoleFinding".casefold():
            from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding

            return PrivilegeEscalationAwsRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationFinding".casefold():
            from .privilege_escalation_finding import PrivilegeEscalationFinding

            return PrivilegeEscalationFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationGcpServiceAccountFinding".casefold():
            from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding

            return PrivilegeEscalationGcpServiceAccountFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationUserFinding".casefold():
            from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding

            return PrivilegeEscalationUserFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeManagementElevation".casefold():
            from .privilege_management_elevation import PrivilegeManagementElevation

            return PrivilegeManagementElevation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeManagementElevationRequest".casefold():
            from .privilege_management_elevation_request import PrivilegeManagementElevationRequest

            return PrivilegeManagementElevationRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.profile".casefold():
            from .networkaccess.profile import Profile
            from .profile import Profile

            return Profile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.profileCardProperty".casefold():
            from .profile_card_property import ProfileCardProperty

            return ProfileCardProperty()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.profilePhoto".casefold():
            from .profile_photo import ProfilePhoto

            return ProfilePhoto()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.program".casefold():
            from .program import Program

            return Program()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.programControl".casefold():
            from .program_control import ProgramControl

            return ProgramControl()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.programControlType".casefold():
            from .program_control_type import ProgramControlType

            return ProgramControlType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.projectParticipation".casefold():
            from .project_participation import ProjectParticipation

            return ProjectParticipation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.pronounsSettings".casefold():
            from .pronouns_settings import PronounsSettings

            return PronounsSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.providerTenantSetting".casefold():
            from .provider_tenant_setting import ProviderTenantSetting

            return ProviderTenantSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.provisioningObjectSummary".casefold():
            from .provisioning_object_summary import ProvisioningObjectSummary

            return ProvisioningObjectSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.publishedResource".casefold():
            from .published_resource import PublishedResource

            return PublishedResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.purchaseInvoiceLine".casefold():
            from .purchase_invoice_line import PurchaseInvoiceLine

            return PurchaseInvoiceLine()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.rbacApplication".casefold():
            from .rbac_application import RbacApplication

            return RbacApplication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.rbacApplicationMultiple".casefold():
            from .rbac_application_multiple import RbacApplicationMultiple

            return RbacApplicationMultiple()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recommendation".casefold():
            from .recommendation import Recommendation

            return Recommendation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recommendationBase".casefold():
            from .recommendation_base import RecommendationBase

            return RecommendationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recordOperation".casefold():
            from .record_operation import RecordOperation

            return RecordOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recycleBin".casefold():
            from .recycle_bin import RecycleBin

            return RecycleBin()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recycleBinItem".casefold():
            from .recycle_bin_item import RecycleBinItem

            return RecycleBinItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.redundantAssignmentAlertConfiguration".casefold():
            from .redundant_assignment_alert_configuration import RedundantAssignmentAlertConfiguration

            return RedundantAssignmentAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.redundantAssignmentAlertIncident".casefold():
            from .redundant_assignment_alert_incident import RedundantAssignmentAlertIncident

            return RedundantAssignmentAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.referenceAttachment".casefold():
            from .reference_attachment import ReferenceAttachment

            return ReferenceAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.regionalAndLanguageSettings".casefold():
            from .regional_and_language_settings import RegionalAndLanguageSettings

            return RegionalAndLanguageSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.relyingPartyDetailedSummary".casefold():
            from .relying_party_detailed_summary import RelyingPartyDetailedSummary

            return RelyingPartyDetailedSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.remoteActionAudit".casefold():
            from .remote_action_audit import RemoteActionAudit

            return RemoteActionAudit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.remoteAssistancePartner".casefold():
            from .remote_assistance_partner import RemoteAssistancePartner

            return RemoteAssistancePartner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.remoteAssistanceSettings".casefold():
            from .remote_assistance_settings import RemoteAssistanceSettings

            return RemoteAssistanceSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.remoteDesktopSecurityConfiguration".casefold():
            from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration

            return RemoteDesktopSecurityConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.reportRoot".casefold():
            from .report_root import ReportRoot

            return ReportRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.request".casefold():
            from .request import Request

            return Request()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resellerDelegatedAdminRelationship".casefold():
            from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship

            return ResellerDelegatedAdminRelationship()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resourceOperation".casefold():
            from .resource_operation import ResourceOperation

            return ResourceOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resourceSpecificPermissionGrant".casefold():
            from .resource_specific_permission_grant import ResourceSpecificPermissionGrant

            return ResourceSpecificPermissionGrant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.restrictedAppsViolation".casefold():
            from .restricted_apps_violation import RestrictedAppsViolation

            return RestrictedAppsViolation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.richLongRunningOperation".casefold():
            from .rich_long_running_operation import RichLongRunningOperation

            return RichLongRunningOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskDetection".casefold():
            from .risk_detection import RiskDetection

            return RiskDetection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyServicePrincipal".casefold():
            from .risky_service_principal import RiskyServicePrincipal

            return RiskyServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyServicePrincipalHistoryItem".casefold():
            from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem

            return RiskyServicePrincipalHistoryItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyUser".casefold():
            from .risky_user import RiskyUser

            return RiskyUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyUserHistoryItem".casefold():
            from .risky_user_history_item import RiskyUserHistoryItem

            return RiskyUserHistoryItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roleAssignment".casefold():
            from .role_assignment import RoleAssignment

            return RoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roleDefinition".casefold():
            from .role_definition import RoleDefinition

            return RoleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roleManagementAlert".casefold():
            from .role_management_alert import RoleManagementAlert

            return RoleManagementAlert()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration".casefold():
            from .roles_assigned_outside_privileged_identity_management_alert_configuration import RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration

            return RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertIncident".casefold():
            from .roles_assigned_outside_privileged_identity_management_alert_incident import RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident

            return RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roleScopeTag".casefold():
            from .role_scope_tag import RoleScopeTag

            return RoleScopeTag()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roleScopeTagAutoAssignment".casefold():
            from .role_scope_tag_auto_assignment import RoleScopeTagAutoAssignment

            return RoleScopeTagAutoAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.room".casefold():
            from .room import Room

            return Room()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roomList".casefold():
            from .room_list import RoomList

            return RoomList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.salesCreditMemoLine".casefold():
            from .sales_credit_memo_line import SalesCreditMemoLine

            return SalesCreditMemoLine()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.salesInvoiceLine".casefold():
            from .sales_invoice_line import SalesInvoiceLine

            return SalesInvoiceLine()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.salesOrderLine".casefold():
            from .sales_order_line import SalesOrderLine

            return SalesOrderLine()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.salesQuoteLine".casefold():
            from .sales_quote_line import SalesQuoteLine

            return SalesQuoteLine()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.samlOrWsFedExternalDomainFederation".casefold():
            from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation

            return SamlOrWsFedExternalDomainFederation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.samlOrWsFedProvider".casefold():
            from .saml_or_ws_fed_provider import SamlOrWsFedProvider

            return SamlOrWsFedProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.schedule".casefold():
            from .schedule import Schedule

            return Schedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.scheduleChangeRequest".casefold():
            from .schedule_change_request import ScheduleChangeRequest

            return ScheduleChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.scheduledPermissionsRequest".casefold():
            from .scheduled_permissions_request import ScheduledPermissionsRequest

            return ScheduledPermissionsRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.schedulingGroup".casefold():
            from .scheduling_group import SchedulingGroup

            return SchedulingGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.schema".casefold():
            from .external_connectors.schema import Schema
            from .schema import Schema

            return Schema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.schemaExtension".casefold():
            from .schema_extension import SchemaExtension

            return SchemaExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.scopedRoleMembership".casefold():
            from .scoped_role_membership import ScopedRoleMembership

            return ScopedRoleMembership()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.acronym".casefold():
            from .search.acronym import Acronym

            return Acronym()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.bookmark".casefold():
            from .search.bookmark import Bookmark

            return Bookmark()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.qna".casefold():
            from .search.qna import Qna

            return Qna()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.searchAnswer".casefold():
            from .search.search_answer import SearchAnswer

            return SearchAnswer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.searchEntity".casefold():
            from .search_entity import SearchEntity

            return SearchEntity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secretInformationAccessAwsResourceFinding".casefold():
            from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding

            return SecretInformationAccessAwsResourceFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secretInformationAccessAwsRoleFinding".casefold():
            from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding

            return SecretInformationAccessAwsRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secretInformationAccessAwsServerlessFunctionFinding".casefold():
            from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding

            return SecretInformationAccessAwsServerlessFunctionFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secretInformationAccessAwsUserFinding".casefold():
            from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding

            return SecretInformationAccessAwsUserFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sectionGroup".casefold():
            from .section_group import SectionGroup

            return SectionGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secureScore".casefold():
            from .secure_score import SecureScore

            return SecureScore()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secureScoreControlProfile".casefold():
            from .secure_score_control_profile import SecureScoreControlProfile

            return SecureScoreControlProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security".casefold():
            from .security.security import Security

            return Security()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.alert".casefold():
            from .alert import Alert
            from .networkaccess.alert import Alert
            from .security.alert import Alert

            return Alert()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.analyzedEmail".casefold():
            from .security.analyzed_email import AnalyzedEmail

            return AnalyzedEmail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.article".casefold():
            from .security.article import Article

            return Article()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.articleIndicator".casefold():
            from .security.article_indicator import ArticleIndicator

            return ArticleIndicator()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.artifact".casefold():
            from .security.artifact import Artifact

            return Artifact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.auditCoreRoot".casefold():
            from .security.audit_core_root import AuditCoreRoot

            return AuditCoreRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.auditLogQuery".casefold():
            from .security.audit_log_query import AuditLogQuery

            return AuditLogQuery()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.auditLogRecord".casefold():
            from .security.audit_log_record import AuditLogRecord

            return AuditLogRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.authorityTemplate".casefold():
            from .security.authority_template import AuthorityTemplate

            return AuthorityTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.case".casefold():
            from .ediscovery.case import Case
            from .security.case import Case

            return Case()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseOperation".casefold():
            from .ediscovery.case_operation import CaseOperation
            from .security.case_operation import CaseOperation

            return CaseOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.casesRoot".casefold():
            from .security.cases_root import CasesRoot

            return CasesRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.categoryTemplate".casefold():
            from .security.category_template import CategoryTemplate

            return CategoryTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.citationTemplate".casefold():
            from .security.citation_template import CitationTemplate

            return CitationTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.collaborationRoot".casefold():
            from .security.collaboration_root import CollaborationRoot

            return CollaborationRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataSet".casefold():
            from .security.data_set import DataSet

            return DataSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataSource".casefold():
            from .ediscovery.data_source import DataSource
            from .security.data_source import DataSource

            return DataSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataSourceContainer".casefold():
            from .ediscovery.data_source_container import DataSourceContainer
            from .security.data_source_container import DataSourceContainer

            return DataSourceContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.departmentTemplate".casefold():
            from .security.department_template import DepartmentTemplate

            return DepartmentTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.detectionRule".casefold():
            from .security.detection_rule import DetectionRule

            return DetectionRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dispositionReviewStage".casefold():
            from .security.disposition_review_stage import DispositionReviewStage

            return DispositionReviewStage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryAddToReviewSetOperation".casefold():
            from .security.ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation

            return EdiscoveryAddToReviewSetOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryCase".casefold():
            from .security.ediscovery_case import EdiscoveryCase

            return EdiscoveryCase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryCaseSettings".casefold():
            from .security.ediscovery_case_settings import EdiscoveryCaseSettings

            return EdiscoveryCaseSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryCustodian".casefold():
            from .security.ediscovery_custodian import EdiscoveryCustodian

            return EdiscoveryCustodian()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryEstimateOperation".casefold():
            from .security.ediscovery_estimate_operation import EdiscoveryEstimateOperation

            return EdiscoveryEstimateOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryExportOperation".casefold():
            from .security.ediscovery_export_operation import EdiscoveryExportOperation

            return EdiscoveryExportOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryFile".casefold():
            from .security.ediscovery_file import EdiscoveryFile

            return EdiscoveryFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryHoldOperation".casefold():
            from .security.ediscovery_hold_operation import EdiscoveryHoldOperation

            return EdiscoveryHoldOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryHoldPolicy".casefold():
            from .security.ediscovery_hold_policy import EdiscoveryHoldPolicy

            return EdiscoveryHoldPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryIndexOperation".casefold():
            from .security.ediscovery_index_operation import EdiscoveryIndexOperation

            return EdiscoveryIndexOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryNoncustodialDataSource".casefold():
            from .security.ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource

            return EdiscoveryNoncustodialDataSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryPurgeDataOperation".casefold():
            from .security.ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation

            return EdiscoveryPurgeDataOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryReviewSet".casefold():
            from .security.ediscovery_review_set import EdiscoveryReviewSet

            return EdiscoveryReviewSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryReviewSetQuery".casefold():
            from .security.ediscovery_review_set_query import EdiscoveryReviewSetQuery

            return EdiscoveryReviewSetQuery()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryReviewTag".casefold():
            from .security.ediscovery_review_tag import EdiscoveryReviewTag

            return EdiscoveryReviewTag()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoverySearch".casefold():
            from .security.ediscovery_search import EdiscoverySearch

            return EdiscoverySearch()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoverySearchExportOperation".casefold():
            from .security.ediscovery_search_export_operation import EdiscoverySearchExportOperation

            return EdiscoverySearchExportOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryTagOperation".casefold():
            from .security.ediscovery_tag_operation import EdiscoveryTagOperation

            return EdiscoveryTagOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.emailContentThreatSubmission".casefold():
            from .security.email_content_threat_submission import EmailContentThreatSubmission

            return EmailContentThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.emailThreatSubmission".casefold():
            from .security.email_threat_submission import EmailThreatSubmission

            return EmailThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.emailThreatSubmissionPolicy".casefold():
            from .security.email_threat_submission_policy import EmailThreatSubmissionPolicy

            return EmailThreatSubmissionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.emailUrlThreatSubmission".casefold():
            from .security.email_url_threat_submission import EmailUrlThreatSubmission

            return EmailUrlThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.file".casefold():
            from .security.file import File

            return File()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileContentThreatSubmission".casefold():
            from .security.file_content_threat_submission import FileContentThreatSubmission

            return FileContentThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanDescriptor".casefold():
            from .security.file_plan_descriptor import FilePlanDescriptor

            return FilePlanDescriptor()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanDescriptorTemplate".casefold():
            from .security.file_plan_descriptor_template import FilePlanDescriptorTemplate

            return FilePlanDescriptorTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanReferenceTemplate".casefold():
            from .security.file_plan_reference_template import FilePlanReferenceTemplate

            return FilePlanReferenceTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileThreatSubmission".casefold():
            from .security.file_threat_submission import FileThreatSubmission

            return FileThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileUrlThreatSubmission".casefold():
            from .security.file_url_threat_submission import FileUrlThreatSubmission

            return FileUrlThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.healthIssue".casefold():
            from .security.health_issue import HealthIssue

            return HealthIssue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.host".casefold():
            from .security.host import Host

            return Host()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostComponent".casefold():
            from .security.host_component import HostComponent

            return HostComponent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostCookie".casefold():
            from .security.host_cookie import HostCookie

            return HostCookie()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostname".casefold():
            from .security.hostname import Hostname

            return Hostname()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostPair".casefold():
            from .security.host_pair import HostPair

            return HostPair()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostPort".casefold():
            from .security.host_port import HostPort

            return HostPort()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostReputation".casefold():
            from .security.host_reputation import HostReputation

            return HostReputation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostSslCertificate".casefold():
            from .security.host_ssl_certificate import HostSslCertificate

            return HostSslCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostTracker".casefold():
            from .security.host_tracker import HostTracker

            return HostTracker()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.identityContainer".casefold():
            from .security.identity_container import IdentityContainer

            return IdentityContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.incident".casefold():
            from .security.incident import Incident

            return Incident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.indicator".casefold():
            from .security.indicator import Indicator

            return Indicator()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.informationProtection".casefold():
            from .information_protection import InformationProtection
            from .security.information_protection import InformationProtection

            return InformationProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.informationProtectionPolicySetting".casefold():
            from .security.information_protection_policy_setting import InformationProtectionPolicySetting

            return InformationProtectionPolicySetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.intelligenceProfile".casefold():
            from .security.intelligence_profile import IntelligenceProfile

            return IntelligenceProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.intelligenceProfileIndicator".casefold():
            from .security.intelligence_profile_indicator import IntelligenceProfileIndicator

            return IntelligenceProfileIndicator()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ipAddress".casefold():
            from .security.ip_address import IpAddress

            return IpAddress()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.labelsRoot".casefold():
            from .security.labels_root import LabelsRoot

            return LabelsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.passiveDnsRecord".casefold():
            from .security.passive_dns_record import PassiveDnsRecord

            return PassiveDnsRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.policyBase".casefold():
            from .policy_base import PolicyBase
            from .security.policy_base import PolicyBase

            return PolicyBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.protectionRule".casefold():
            from .security.protection_rule import ProtectionRule

            return ProtectionRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.retentionEvent".casefold():
            from .security.retention_event import RetentionEvent

            return RetentionEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.retentionEventType".casefold():
            from .security.retention_event_type import RetentionEventType

            return RetentionEventType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.retentionLabel".casefold():
            from .security.retention_label import RetentionLabel

            return RetentionLabel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.rulesRoot".casefold():
            from .security.rules_root import RulesRoot

            return RulesRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.search".casefold():
            from .security.search import Search

            return Search()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.security".casefold():
            from .security.security import Security

            return Security()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sensitivityLabel".casefold():
            from .security.sensitivity_label import SensitivityLabel
            from .sensitivity_label import SensitivityLabel

            return SensitivityLabel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.siteSource".casefold():
            from .ediscovery.site_source import SiteSource
            from .security.site_source import SiteSource

            return SiteSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sslCertificate".casefold():
            from .security.ssl_certificate import SslCertificate

            return SslCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.subcategoryTemplate".casefold():
            from .security.subcategory_template import SubcategoryTemplate

            return SubcategoryTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.subdomain".casefold():
            from .security.subdomain import Subdomain

            return Subdomain()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.tag".casefold():
            from .ediscovery.tag import Tag
            from .security.tag import Tag

            return Tag()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.threatIntelligence".casefold():
            from .security.threat_intelligence import ThreatIntelligence

            return ThreatIntelligence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.threatSubmission".casefold():
            from .security.threat_submission import ThreatSubmission

            return ThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.threatSubmissionRoot".casefold():
            from .security.threat_submission_root import ThreatSubmissionRoot

            return ThreatSubmissionRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.triggersRoot".casefold():
            from .security.triggers_root import TriggersRoot

            return TriggersRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.triggerTypesRoot".casefold():
            from .security.trigger_types_root import TriggerTypesRoot

            return TriggerTypesRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unclassifiedArtifact".casefold():
            from .security.unclassified_artifact import UnclassifiedArtifact

            return UnclassifiedArtifact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unifiedGroupSource".casefold():
            from .ediscovery.unified_group_source import UnifiedGroupSource
            from .security.unified_group_source import UnifiedGroupSource

            return UnifiedGroupSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.urlThreatSubmission".casefold():
            from .security.url_threat_submission import UrlThreatSubmission

            return UrlThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.userSource".casefold():
            from .ediscovery.user_source import UserSource
            from .security.user_source import UserSource

            return UserSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vulnerability".casefold():
            from .security.vulnerability import Vulnerability

            return Vulnerability()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vulnerabilityComponent".casefold():
            from .security.vulnerability_component import VulnerabilityComponent

            return VulnerabilityComponent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.whoisBaseRecord".casefold():
            from .security.whois_base_record import WhoisBaseRecord

            return WhoisBaseRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.whoisHistoryRecord".casefold():
            from .security.whois_history_record import WhoisHistoryRecord

            return WhoisHistoryRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.whoisRecord".casefold():
            from .security.whois_record import WhoisRecord

            return WhoisRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityAction".casefold():
            from .security_action import SecurityAction

            return SecurityAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityBaselineCategoryStateSummary".casefold():
            from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary

            return SecurityBaselineCategoryStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityBaselineDeviceState".casefold():
            from .security_baseline_device_state import SecurityBaselineDeviceState

            return SecurityBaselineDeviceState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityBaselineSettingState".casefold():
            from .security_baseline_setting_state import SecurityBaselineSettingState

            return SecurityBaselineSettingState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityBaselineState".casefold():
            from .security_baseline_state import SecurityBaselineState

            return SecurityBaselineState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityBaselineStateSummary".casefold():
            from .security_baseline_state_summary import SecurityBaselineStateSummary

            return SecurityBaselineStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityBaselineTemplate".casefold():
            from .security_baseline_template import SecurityBaselineTemplate

            return SecurityBaselineTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityConfigurationTask".casefold():
            from .security_configuration_task import SecurityConfigurationTask

            return SecurityConfigurationTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityReportsRoot".casefold():
            from .security_reports_root import SecurityReportsRoot

            return SecurityReportsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityToolAwsResourceAdministratorFinding".casefold():
            from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding

            return SecurityToolAwsResourceAdministratorFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityToolAwsRoleAdministratorFinding".casefold():
            from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding

            return SecurityToolAwsRoleAdministratorFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityToolAwsServerlessFunctionAdministratorFinding".casefold():
            from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding

            return SecurityToolAwsServerlessFunctionAdministratorFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityToolAwsUserAdministratorFinding".casefold():
            from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding

            return SecurityToolAwsUserAdministratorFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sendDtmfTonesOperation".casefold():
            from .send_dtmf_tones_operation import SendDtmfTonesOperation

            return SendDtmfTonesOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sensitiveType".casefold():
            from .sensitive_type import SensitiveType

            return SensitiveType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sensitivityLabel".casefold():
            from .security.sensitivity_label import SensitivityLabel
            from .sensitivity_label import SensitivityLabel

            return SensitivityLabel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sensitivityPolicySettings".casefold():
            from .sensitivity_policy_settings import SensitivityPolicySettings

            return SensitivityPolicySettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sequentialActivationRenewalsAlertConfiguration".casefold():
            from .sequential_activation_renewals_alert_configuration import SequentialActivationRenewalsAlertConfiguration

            return SequentialActivationRenewalsAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sequentialActivationRenewalsAlertIncident".casefold():
            from .sequential_activation_renewals_alert_incident import SequentialActivationRenewalsAlertIncident

            return SequentialActivationRenewalsAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceActivity".casefold():
            from .service_activity import ServiceActivity

            return ServiceActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceAnnouncement".casefold():
            from .service_announcement import ServiceAnnouncement

            return ServiceAnnouncement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceAnnouncementAttachment".casefold():
            from .service_announcement_attachment import ServiceAnnouncementAttachment

            return ServiceAnnouncementAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceAnnouncementBase".casefold():
            from .service_announcement_base import ServiceAnnouncementBase

            return ServiceAnnouncementBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceHealth".casefold():
            from .service_health import ServiceHealth

            return ServiceHealth()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceHealthIssue".casefold():
            from .service_health_issue import ServiceHealthIssue

            return ServiceHealthIssue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceLevelAgreementRoot".casefold():
            from .service_level_agreement_root import ServiceLevelAgreementRoot

            return ServiceLevelAgreementRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceNowConnection".casefold():
            from .service_now_connection import ServiceNowConnection

            return ServiceNowConnection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipal".casefold():
            from .service_principal import ServicePrincipal

            return ServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipalCreationConditionSet".casefold():
            from .service_principal_creation_condition_set import ServicePrincipalCreationConditionSet

            return ServicePrincipalCreationConditionSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipalCreationPolicy".casefold():
            from .service_principal_creation_policy import ServicePrincipalCreationPolicy

            return ServicePrincipalCreationPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipalRiskDetection".casefold():
            from .service_principal_risk_detection import ServicePrincipalRiskDetection

            return ServicePrincipalRiskDetection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipalSignInActivity".casefold():
            from .service_principal_sign_in_activity import ServicePrincipalSignInActivity

            return ServicePrincipalSignInActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceStorageQuotaBreakdown".casefold():
            from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown

            return ServiceStorageQuotaBreakdown()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceUpdateMessage".casefold():
            from .service_update_message import ServiceUpdateMessage

            return ServiceUpdateMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.settingStateDeviceSummary".casefold():
            from .setting_state_device_summary import SettingStateDeviceSummary

            return SettingStateDeviceSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedDriveItem".casefold():
            from .shared_drive_item import SharedDriveItem

            return SharedDriveItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedEmailDomain".casefold():
            from .shared_email_domain import SharedEmailDomain

            return SharedEmailDomain()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedEmailDomainInvitation".casefold():
            from .shared_email_domain_invitation import SharedEmailDomainInvitation

            return SharedEmailDomainInvitation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedInsight".casefold():
            from .shared_insight import SharedInsight

            return SharedInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedPCConfiguration".casefold():
            from .shared_p_c_configuration import SharedPCConfiguration

            return SharedPCConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedWithChannelTeamInfo".casefold():
            from .shared_with_channel_team_info import SharedWithChannelTeamInfo

            return SharedWithChannelTeamInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharepoint".casefold():
            from .sharepoint import Sharepoint

            return Sharepoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharepointSettings".casefold():
            from .sharepoint_settings import SharepointSettings

            return SharepointSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.shift".casefold():
            from .shift import Shift

            return Shift()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.shiftPreferences".casefold():
            from .shift_preferences import ShiftPreferences

            return ShiftPreferences()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.shiftsRoleDefinition".casefold():
            from .shifts_role_definition import ShiftsRoleDefinition

            return ShiftsRoleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.signIn".casefold():
            from .sign_in import SignIn

            return SignIn()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.simulation".casefold():
            from .simulation import Simulation

            return Simulation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.simulationAutomation".casefold():
            from .simulation_automation import SimulationAutomation

            return SimulationAutomation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.simulationAutomationRun".casefold():
            from .simulation_automation_run import SimulationAutomationRun

            return SimulationAutomationRun()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.singleValueLegacyExtendedProperty".casefold():
            from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

            return SingleValueLegacyExtendedProperty()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.site".casefold():
            from .site import Site

            return Site()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sitePage".casefold():
            from .site_page import SitePage

            return SitePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.skillProficiency".casefold():
            from .skill_proficiency import SkillProficiency

            return SkillProficiency()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.skypeForBusinessUserConversationMember".casefold():
            from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember

            return SkypeForBusinessUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.skypeUserConversationMember".casefold():
            from .skype_user_conversation_member import SkypeUserConversationMember

            return SkypeUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.smsAuthenticationMethodConfiguration".casefold():
            from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration

            return SmsAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.smsAuthenticationMethodTarget".casefold():
            from .sms_authentication_method_target import SmsAuthenticationMethodTarget

            return SmsAuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.socialIdentityProvider".casefold():
            from .social_identity_provider import SocialIdentityProvider

            return SocialIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.softwareOathAuthenticationMethod".casefold():
            from .software_oath_authentication_method import SoftwareOathAuthenticationMethod

            return SoftwareOathAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.softwareOathAuthenticationMethodConfiguration".casefold():
            from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration

            return SoftwareOathAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.softwareUpdateStatusSummary".casefold():
            from .software_update_status_summary import SoftwareUpdateStatusSummary

            return SoftwareUpdateStatusSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.staleSignInAlertConfiguration".casefold():
            from .stale_sign_in_alert_configuration import StaleSignInAlertConfiguration

            return StaleSignInAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.staleSignInAlertIncident".casefold():
            from .stale_sign_in_alert_incident import StaleSignInAlertIncident

            return StaleSignInAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.standardWebPart".casefold():
            from .standard_web_part import StandardWebPart

            return StandardWebPart()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.startHoldMusicOperation".casefold():
            from .start_hold_music_operation import StartHoldMusicOperation

            return StartHoldMusicOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.stopHoldMusicOperation".casefold():
            from .stop_hold_music_operation import StopHoldMusicOperation

            return StopHoldMusicOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.storageQuotaBreakdown".casefold():
            from .storage_quota_breakdown import StorageQuotaBreakdown

            return StorageQuotaBreakdown()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.storageSettings".casefold():
            from .storage_settings import StorageSettings

            return StorageSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.strongAuthenticationDetail".casefold():
            from .strong_authentication_detail import StrongAuthenticationDetail

            return StrongAuthenticationDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.strongAuthenticationPhoneAppDetail".casefold():
            from .strong_authentication_phone_app_detail import StrongAuthenticationPhoneAppDetail

            return StrongAuthenticationPhoneAppDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.stsPolicy".casefold():
            from .sts_policy import StsPolicy

            return StsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subjectRightsRequest".casefold():
            from .subject_rights_request import SubjectRightsRequest

            return SubjectRightsRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subscribedSku".casefold():
            from .subscribed_sku import SubscribedSku

            return SubscribedSku()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subscribeToToneOperation".casefold():
            from .subscribe_to_tone_operation import SubscribeToToneOperation

            return SubscribeToToneOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subscription".casefold():
            from .subscription import Subscription

            return Subscription()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.superAwsResourceFinding".casefold():
            from .super_aws_resource_finding import SuperAwsResourceFinding

            return SuperAwsResourceFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.superAwsRoleFinding".casefold():
            from .super_aws_role_finding import SuperAwsRoleFinding

            return SuperAwsRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.superAzureServicePrincipalFinding".casefold():
            from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding

            return SuperAzureServicePrincipalFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.superGcpServiceAccountFinding".casefold():
            from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding

            return SuperGcpServiceAccountFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.superServerlessFunctionFinding".casefold():
            from .super_serverless_function_finding import SuperServerlessFunctionFinding

            return SuperServerlessFunctionFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.superUserFinding".casefold():
            from .super_user_finding import SuperUserFinding

            return SuperUserFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.swapShiftsChangeRequest".casefold():
            from .swap_shifts_change_request import SwapShiftsChangeRequest

            return SwapShiftsChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.symantecCodeSigningCertificate".casefold():
            from .symantec_code_signing_certificate import SymantecCodeSigningCertificate

            return SymantecCodeSigningCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.synchronization".casefold():
            from .synchronization import Synchronization

            return Synchronization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.synchronizationJob".casefold():
            from .synchronization_job import SynchronizationJob

            return SynchronizationJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.synchronizationSchema".casefold():
            from .synchronization_schema import SynchronizationSchema

            return SynchronizationSchema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.synchronizationTemplate".casefold():
            from .synchronization_template import SynchronizationTemplate

            return SynchronizationTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetDeviceGroup".casefold():
            from .target_device_group import TargetDeviceGroup

            return TargetDeviceGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppConfiguration".casefold():
            from .targeted_managed_app_configuration import TargetedManagedAppConfiguration

            return TargetedManagedAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppConfigurationPolicySetItem".casefold():
            from .targeted_managed_app_configuration_policy_set_item import TargetedManagedAppConfigurationPolicySetItem

            return TargetedManagedAppConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppPolicyAssignment".casefold():
            from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment

            return TargetedManagedAppPolicyAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppProtection".casefold():
            from .targeted_managed_app_protection import TargetedManagedAppProtection

            return TargetedManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.taskFileAttachment".casefold():
            from .task_file_attachment import TaskFileAttachment

            return TaskFileAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.taxGroup".casefold():
            from .tax_group import TaxGroup

            return TaxGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.team".casefold():
            from .team import Team

            return Team()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamInfo".casefold():
            from .team_info import TeamInfo

            return TeamInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsApp".casefold():
            from .teams_app import TeamsApp

            return TeamsApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppDashboardCardDefinition".casefold():
            from .teams_app_dashboard_card_definition import TeamsAppDashboardCardDefinition

            return TeamsAppDashboardCardDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppDefinition".casefold():
            from .teams_app_definition import TeamsAppDefinition

            return TeamsAppDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppIcon".casefold():
            from .teams_app_icon import TeamsAppIcon

            return TeamsAppIcon()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppInstallation".casefold():
            from .teams_app_installation import TeamsAppInstallation

            return TeamsAppInstallation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppSettings".casefold():
            from .teams_app_settings import TeamsAppSettings

            return TeamsAppSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAsyncOperation".casefold():
            from .teams_async_operation import TeamsAsyncOperation

            return TeamsAsyncOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsTab".casefold():
            from .teams_tab import TeamsTab

            return TeamsTab()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsTemplate".casefold():
            from .teams_template import TeamsTemplate

            return TeamsTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsUserConfiguration.teamsAdminRoot".casefold():
            from .teams_user_configuration.teams_admin_root import TeamsAdminRoot

            return TeamsAdminRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamTemplate".casefold():
            from .team_template import TeamTemplate

            return TeamTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamTemplateDefinition".casefold():
            from .team_template_definition import TeamTemplateDefinition

            return TeamTemplateDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamwork".casefold():
            from .teamwork import Teamwork

            return Teamwork()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkBot".casefold():
            from .teamwork_bot import TeamworkBot

            return TeamworkBot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkDevice".casefold():
            from .teamwork_device import TeamworkDevice

            return TeamworkDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkDeviceActivity".casefold():
            from .teamwork_device_activity import TeamworkDeviceActivity

            return TeamworkDeviceActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkDeviceConfiguration".casefold():
            from .teamwork_device_configuration import TeamworkDeviceConfiguration

            return TeamworkDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkDeviceHealth".casefold():
            from .teamwork_device_health import TeamworkDeviceHealth

            return TeamworkDeviceHealth()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkDeviceOperation".casefold():
            from .teamwork_device_operation import TeamworkDeviceOperation

            return TeamworkDeviceOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkHostedContent".casefold():
            from .teamwork_hosted_content import TeamworkHostedContent

            return TeamworkHostedContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkPeripheral".casefold():
            from .teamwork_peripheral import TeamworkPeripheral

            return TeamworkPeripheral()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkTag".casefold():
            from .teamwork_tag import TeamworkTag

            return TeamworkTag()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkTagMember".casefold():
            from .teamwork_tag_member import TeamworkTagMember

            return TeamworkTagMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.telecomExpenseManagementPartner".casefold():
            from .telecom_expense_management_partner import TelecomExpenseManagementPartner

            return TelecomExpenseManagementPartner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.temporaryAccessPassAuthenticationMethod".casefold():
            from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod

            return TemporaryAccessPassAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.temporaryAccessPassAuthenticationMethodConfiguration".casefold():
            from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration

            return TemporaryAccessPassAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tenantAppManagementPolicy".casefold():
            from .tenant_app_management_policy import TenantAppManagementPolicy

            return TenantAppManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tenantAttachRBAC".casefold():
            from .tenant_attach_r_b_a_c import TenantAttachRBAC

            return TenantAttachRBAC()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tenantRelationshipAccessPolicyBase".casefold():
            from .tenant_relationship_access_policy_base import TenantRelationshipAccessPolicyBase

            return TenantRelationshipAccessPolicyBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tenantSetupInfo".casefold():
            from .tenant_setup_info import TenantSetupInfo

            return TenantSetupInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termsAndConditions".casefold():
            from .terms_and_conditions import TermsAndConditions

            return TermsAndConditions()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termsAndConditionsAcceptanceStatus".casefold():
            from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus

            return TermsAndConditionsAcceptanceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termsAndConditionsAssignment".casefold():
            from .terms_and_conditions_assignment import TermsAndConditionsAssignment

            return TermsAndConditionsAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termsAndConditionsGroupAssignment".casefold():
            from .terms_and_conditions_group_assignment import TermsAndConditionsGroupAssignment

            return TermsAndConditionsGroupAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termsOfUseContainer".casefold():
            from .terms_of_use_container import TermsOfUseContainer

            return TermsOfUseContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.group".casefold():
            from .group import Group
            from .term_store.group import Group

            return Group()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.relation".casefold():
            from .term_store.relation import Relation

            return Relation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.set".casefold():
            from .term_store.set import Set

            return Set()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.store".casefold():
            from .term_store.store import Store

            return Store()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.term".casefold():
            from .term_store.term import Term

            return Term()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.textClassificationRequest".casefold():
            from .text_classification_request import TextClassificationRequest

            return TextClassificationRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.textWebPart".casefold():
            from .text_web_part import TextWebPart

            return TextWebPart()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.threatAssessmentRequest".casefold():
            from .threat_assessment_request import ThreatAssessmentRequest

            return ThreatAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.threatAssessmentResult".casefold():
            from .threat_assessment_result import ThreatAssessmentResult

            return ThreatAssessmentResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.thumbnailSet".casefold():
            from .thumbnail_set import ThumbnailSet

            return ThumbnailSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tiIndicator".casefold():
            from .ti_indicator import TiIndicator

            return TiIndicator()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeCard".casefold():
            from .time_card import TimeCard

            return TimeCard()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOff".casefold():
            from .time_off import TimeOff

            return TimeOff()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffReason".casefold():
            from .time_off_reason import TimeOffReason

            return TimeOffReason()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffRequest".casefold():
            from .time_off_request import TimeOffRequest

            return TimeOffRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.todo".casefold():
            from .todo import Todo

            return Todo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.todoTask".casefold():
            from .todo_task import TodoTask

            return TodoTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.todoTaskList".casefold():
            from .todo_task_list import TodoTaskList

            return TodoTaskList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tokenIssuancePolicy".casefold():
            from .token_issuance_policy import TokenIssuancePolicy

            return TokenIssuancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tokenLifetimePolicy".casefold():
            from .token_lifetime_policy import TokenLifetimePolicy

            return TokenLifetimePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertConfiguration".casefold():
            from .too_many_global_admins_assigned_to_tenant_alert_configuration import TooManyGlobalAdminsAssignedToTenantAlertConfiguration

            return TooManyGlobalAdminsAssignedToTenantAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertIncident".casefold():
            from .too_many_global_admins_assigned_to_tenant_alert_incident import TooManyGlobalAdminsAssignedToTenantAlertIncident

            return TooManyGlobalAdminsAssignedToTenantAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.training".casefold():
            from .training import Training

            return Training()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.trainingCampaign".casefold():
            from .training_campaign import TrainingCampaign

            return TrainingCampaign()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.trainingLanguageDetail".casefold():
            from .training_language_detail import TrainingLanguageDetail

            return TrainingLanguageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.trending".casefold():
            from .trending import Trending

            return Trending()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.trustedCertificateAuthorityAsEntityBase".casefold():
            from .trusted_certificate_authority_as_entity_base import TrustedCertificateAuthorityAsEntityBase

            return TrustedCertificateAuthorityAsEntityBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.trustFrameworkKeySet".casefold():
            from .trust_framework_key_set import TrustFrameworkKeySet

            return TrustFrameworkKeySet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.trustFrameworkPolicy".casefold():
            from .trust_framework_policy import TrustFrameworkPolicy

            return TrustFrameworkPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unenforcedMfaAwsUserFinding".casefold():
            from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding

            return UnenforcedMfaAwsUserFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRbacApplication".casefold():
            from .unified_rbac_application import UnifiedRbacApplication

            return UnifiedRbacApplication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRbacResourceAction".casefold():
            from .unified_rbac_resource_action import UnifiedRbacResourceAction

            return UnifiedRbacResourceAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRbacResourceNamespace".casefold():
            from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace

            return UnifiedRbacResourceNamespace()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRbacResourceScope".casefold():
            from .unified_rbac_resource_scope import UnifiedRbacResourceScope

            return UnifiedRbacResourceScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignment".casefold():
            from .unified_role_assignment import UnifiedRoleAssignment

            return UnifiedRoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentMultiple".casefold():
            from .unified_role_assignment_multiple import UnifiedRoleAssignmentMultiple

            return UnifiedRoleAssignmentMultiple()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentSchedule".casefold():
            from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule

            return UnifiedRoleAssignmentSchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentScheduleInstance".casefold():
            from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance

            return UnifiedRoleAssignmentScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentScheduleRequest".casefold():
            from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest

            return UnifiedRoleAssignmentScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleDefinition".casefold():
            from .unified_role_definition import UnifiedRoleDefinition

            return UnifiedRoleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleEligibilitySchedule".casefold():
            from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule

            return UnifiedRoleEligibilitySchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleEligibilityScheduleInstance".casefold():
            from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance

            return UnifiedRoleEligibilityScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleEligibilityScheduleRequest".casefold():
            from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest

            return UnifiedRoleEligibilityScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementAlert".casefold():
            from .unified_role_management_alert import UnifiedRoleManagementAlert

            return UnifiedRoleManagementAlert()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementAlertConfiguration".casefold():
            from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

            return UnifiedRoleManagementAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementAlertDefinition".casefold():
            from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition

            return UnifiedRoleManagementAlertDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementAlertIncident".casefold():
            from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

            return UnifiedRoleManagementAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicy".casefold():
            from .unified_role_management_policy import UnifiedRoleManagementPolicy

            return UnifiedRoleManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule".casefold():
            from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule

            return UnifiedRoleManagementPolicyApprovalRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyAssignment".casefold():
            from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment

            return UnifiedRoleManagementPolicyAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule".casefold():
            from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule

            return UnifiedRoleManagementPolicyAuthenticationContextRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule".casefold():
            from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule

            return UnifiedRoleManagementPolicyEnablementRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule".casefold():
            from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule

            return UnifiedRoleManagementPolicyExpirationRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule".casefold():
            from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule

            return UnifiedRoleManagementPolicyNotificationRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyRule".casefold():
            from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

            return UnifiedRoleManagementPolicyRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleScheduleBase".casefold():
            from .unified_role_schedule_base import UnifiedRoleScheduleBase

            return UnifiedRoleScheduleBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleScheduleInstanceBase".casefold():
            from .unified_role_schedule_instance_base import UnifiedRoleScheduleInstanceBase

            return UnifiedRoleScheduleInstanceBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedStorageQuota".casefold():
            from .unified_storage_quota import UnifiedStorageQuota

            return UnifiedStorageQuota()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unmanagedDeviceDiscoveryTask".casefold():
            from .unmanaged_device_discovery_task import UnmanagedDeviceDiscoveryTask

            return UnmanagedDeviceDiscoveryTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unmuteParticipantOperation".casefold():
            from .unmute_participant_operation import UnmuteParticipantOperation

            return UnmuteParticipantOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unsupportedDeviceConfiguration".casefold():
            from .unsupported_device_configuration import UnsupportedDeviceConfiguration

            return UnsupportedDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unsupportedGroupPolicyExtension".casefold():
            from .unsupported_group_policy_extension import UnsupportedGroupPolicyExtension

            return UnsupportedGroupPolicyExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.updateRecordingStatusOperation".casefold():
            from .update_recording_status_operation import UpdateRecordingStatusOperation

            return UpdateRecordingStatusOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.urlAssessmentRequest".casefold():
            from .url_assessment_request import UrlAssessmentRequest

            return UrlAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.usageRight".casefold():
            from .usage_right import UsageRight

            return UsageRight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.usedInsight".casefold():
            from .used_insight import UsedInsight

            return UsedInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.user".casefold():
            from .user import User

            return User()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userAccountInformation".casefold():
            from .user_account_information import UserAccountInformation

            return UserAccountInformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userActivity".casefold():
            from .user_activity import UserActivity

            return UserActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userAnalytics".casefold():
            from .user_analytics import UserAnalytics

            return UserAnalytics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userAppInstallStatus".casefold():
            from .user_app_install_status import UserAppInstallStatus

            return UserAppInstallStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userConfiguration".casefold():
            from .teams_user_configuration.user_configuration import UserConfiguration

            return UserConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userConsentRequest".casefold():
            from .user_consent_request import UserConsentRequest

            return UserConsentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userCountMetric".casefold():
            from .user_count_metric import UserCountMetric

            return UserCountMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userCredentialUsageDetails".casefold():
            from .user_credential_usage_details import UserCredentialUsageDetails

            return UserCredentialUsageDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAnomaly".casefold():
            from .user_experience_analytics_anomaly import UserExperienceAnalyticsAnomaly

            return UserExperienceAnalyticsAnomaly()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAnomalyCorrelationGroupOverview".casefold():
            from .user_experience_analytics_anomaly_correlation_group_overview import UserExperienceAnalyticsAnomalyCorrelationGroupOverview

            return UserExperienceAnalyticsAnomalyCorrelationGroupOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAnomalyDevice".casefold():
            from .user_experience_analytics_anomaly_device import UserExperienceAnalyticsAnomalyDevice

            return UserExperienceAnalyticsAnomalyDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthApplicationPerformance".casefold():
            from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance

            return UserExperienceAnalyticsAppHealthApplicationPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByAppVersion".casefold():
            from .user_experience_analytics_app_health_app_performance_by_app_version import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion

            return UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails".casefold():
            from .user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails

            return UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId".casefold():
            from .user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId

            return UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByOSVersion".casefold():
            from .user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion

            return UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthDeviceModelPerformance".casefold():
            from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance

            return UserExperienceAnalyticsAppHealthDeviceModelPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthDevicePerformance".casefold():
            from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance

            return UserExperienceAnalyticsAppHealthDevicePerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthDevicePerformanceDetails".casefold():
            from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails

            return UserExperienceAnalyticsAppHealthDevicePerformanceDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthOSVersionPerformance".casefold():
            from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance

            return UserExperienceAnalyticsAppHealthOSVersionPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsBaseline".casefold():
            from .user_experience_analytics_baseline import UserExperienceAnalyticsBaseline

            return UserExperienceAnalyticsBaseline()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsBatteryHealthAppImpact".casefold():
            from .user_experience_analytics_battery_health_app_impact import UserExperienceAnalyticsBatteryHealthAppImpact

            return UserExperienceAnalyticsBatteryHealthAppImpact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsBatteryHealthCapacityDetails".casefold():
            from .user_experience_analytics_battery_health_capacity_details import UserExperienceAnalyticsBatteryHealthCapacityDetails

            return UserExperienceAnalyticsBatteryHealthCapacityDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsBatteryHealthDeviceAppImpact".casefold():
            from .user_experience_analytics_battery_health_device_app_impact import UserExperienceAnalyticsBatteryHealthDeviceAppImpact

            return UserExperienceAnalyticsBatteryHealthDeviceAppImpact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsBatteryHealthDevicePerformance".casefold():
            from .user_experience_analytics_battery_health_device_performance import UserExperienceAnalyticsBatteryHealthDevicePerformance

            return UserExperienceAnalyticsBatteryHealthDevicePerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory".casefold():
            from .user_experience_analytics_battery_health_device_runtime_history import UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory

            return UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsBatteryHealthModelPerformance".casefold():
            from .user_experience_analytics_battery_health_model_performance import UserExperienceAnalyticsBatteryHealthModelPerformance

            return UserExperienceAnalyticsBatteryHealthModelPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsBatteryHealthOsPerformance".casefold():
            from .user_experience_analytics_battery_health_os_performance import UserExperienceAnalyticsBatteryHealthOsPerformance

            return UserExperienceAnalyticsBatteryHealthOsPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsBatteryHealthRuntimeDetails".casefold():
            from .user_experience_analytics_battery_health_runtime_details import UserExperienceAnalyticsBatteryHealthRuntimeDetails

            return UserExperienceAnalyticsBatteryHealthRuntimeDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsCategory".casefold():
            from .user_experience_analytics_category import UserExperienceAnalyticsCategory

            return UserExperienceAnalyticsCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDevicePerformance".casefold():
            from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance

            return UserExperienceAnalyticsDevicePerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDeviceScope".casefold():
            from .user_experience_analytics_device_scope import UserExperienceAnalyticsDeviceScope

            return UserExperienceAnalyticsDeviceScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDeviceScores".casefold():
            from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores

            return UserExperienceAnalyticsDeviceScores()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDeviceStartupHistory".casefold():
            from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory

            return UserExperienceAnalyticsDeviceStartupHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDeviceStartupProcess".casefold():
            from .user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess

            return UserExperienceAnalyticsDeviceStartupProcess()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDeviceStartupProcessPerformance".casefold():
            from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance

            return UserExperienceAnalyticsDeviceStartupProcessPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDeviceTimelineEvent".casefold():
            from .user_experience_analytics_device_timeline_event import UserExperienceAnalyticsDeviceTimelineEvent

            return UserExperienceAnalyticsDeviceTimelineEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDeviceWithoutCloudIdentity".casefold():
            from .user_experience_analytics_device_without_cloud_identity import UserExperienceAnalyticsDeviceWithoutCloudIdentity

            return UserExperienceAnalyticsDeviceWithoutCloudIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsImpactingProcess".casefold():
            from .user_experience_analytics_impacting_process import UserExperienceAnalyticsImpactingProcess

            return UserExperienceAnalyticsImpactingProcess()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsMetric".casefold():
            from .user_experience_analytics_metric import UserExperienceAnalyticsMetric

            return UserExperienceAnalyticsMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsMetricHistory".casefold():
            from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory

            return UserExperienceAnalyticsMetricHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsModelScores".casefold():
            from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores

            return UserExperienceAnalyticsModelScores()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsNotAutopilotReadyDevice".casefold():
            from .user_experience_analytics_not_autopilot_ready_device import UserExperienceAnalyticsNotAutopilotReadyDevice

            return UserExperienceAnalyticsNotAutopilotReadyDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsOverview".casefold():
            from .user_experience_analytics_overview import UserExperienceAnalyticsOverview

            return UserExperienceAnalyticsOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsRemoteConnection".casefold():
            from .user_experience_analytics_remote_connection import UserExperienceAnalyticsRemoteConnection

            return UserExperienceAnalyticsRemoteConnection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsResourcePerformance".casefold():
            from .user_experience_analytics_resource_performance import UserExperienceAnalyticsResourcePerformance

            return UserExperienceAnalyticsResourcePerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsScoreHistory".casefold():
            from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory

            return UserExperienceAnalyticsScoreHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereDevice".casefold():
            from .user_experience_analytics_work_from_anywhere_device import UserExperienceAnalyticsWorkFromAnywhereDevice

            return UserExperienceAnalyticsWorkFromAnywhereDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric".casefold():
            from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric

            return UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereMetric".casefold():
            from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric

            return UserExperienceAnalyticsWorkFromAnywhereMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereModelPerformance".casefold():
            from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance

            return UserExperienceAnalyticsWorkFromAnywhereModelPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userFlowLanguageConfiguration".casefold():
            from .user_flow_language_configuration import UserFlowLanguageConfiguration

            return UserFlowLanguageConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userFlowLanguagePage".casefold():
            from .user_flow_language_page import UserFlowLanguagePage

            return UserFlowLanguagePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userInsightsRoot".casefold():
            from .user_insights_root import UserInsightsRoot

            return UserInsightsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userInsightsSettings".casefold():
            from .user_insights_settings import UserInsightsSettings

            return UserInsightsSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userInstallStateSummary".casefold():
            from .user_install_state_summary import UserInstallStateSummary

            return UserInstallStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userPFXCertificate".casefold():
            from .user_p_f_x_certificate import UserPFXCertificate

            return UserPFXCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userRegistrationDetails".casefold():
            from .user_registration_details import UserRegistrationDetails

            return UserRegistrationDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userRequestsMetric".casefold():
            from .user_requests_metric import UserRequestsMetric

            return UserRequestsMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userScopeTeamsAppInstallation".casefold():
            from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

            return UserScopeTeamsAppInstallation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userSecurityProfile".casefold():
            from .user_security_profile import UserSecurityProfile

            return UserSecurityProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userSettings".casefold():
            from .user_settings import UserSettings

            return UserSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userSignInInsight".casefold():
            from .user_sign_in_insight import UserSignInInsight

            return UserSignInInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userSignUpMetric".casefold():
            from .user_sign_up_metric import UserSignUpMetric

            return UserSignUpMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userStorage".casefold():
            from .user_storage import UserStorage

            return UserStorage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userTeamwork".casefold():
            from .user_teamwork import UserTeamwork

            return UserTeamwork()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userVirtualEventsRoot".casefold():
            from .user_virtual_events_root import UserVirtualEventsRoot

            return UserVirtualEventsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.verticalSection".casefold():
            from .vertical_section import VerticalSection

            return VerticalSection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.videoNewsLinkPage".casefold():
            from .video_news_link_page import VideoNewsLinkPage

            return VideoNewsLinkPage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEndpoint".casefold():
            from .virtual_endpoint import VirtualEndpoint

            return VirtualEndpoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEvent".casefold():
            from .virtual_event import VirtualEvent

            return VirtualEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventPresenter".casefold():
            from .virtual_event_presenter import VirtualEventPresenter

            return VirtualEventPresenter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventRegistration".casefold():
            from .virtual_event_registration import VirtualEventRegistration

            return VirtualEventRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventRegistrationConfiguration".casefold():
            from .virtual_event_registration_configuration import VirtualEventRegistrationConfiguration

            return VirtualEventRegistrationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventRegistrationCustomQuestion".casefold():
            from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion

            return VirtualEventRegistrationCustomQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventRegistrationPredefinedQuestion".casefold():
            from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion

            return VirtualEventRegistrationPredefinedQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventRegistrationQuestionBase".casefold():
            from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase

            return VirtualEventRegistrationQuestionBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventSession".casefold():
            from .virtual_event_session import VirtualEventSession

            return VirtualEventSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventsRoot".casefold():
            from .virtual_events_root import VirtualEventsRoot

            return VirtualEventsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventTownhall".casefold():
            from .virtual_event_townhall import VirtualEventTownhall

            return VirtualEventTownhall()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventWebinar".casefold():
            from .virtual_event_webinar import VirtualEventWebinar

            return VirtualEventWebinar()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventWebinarRegistrationConfiguration".casefold():
            from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration

            return VirtualEventWebinarRegistrationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualMachineDetails".casefold():
            from .virtual_machine_details import VirtualMachineDetails

            return VirtualMachineDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualMachineWithAwsStorageBucketAccessFinding".casefold():
            from .virtual_machine_with_aws_storage_bucket_access_finding import VirtualMachineWithAwsStorageBucketAccessFinding

            return VirtualMachineWithAwsStorageBucketAccessFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.voiceAuthenticationMethodConfiguration".casefold():
            from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration

            return VoiceAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.voiceAuthenticationMethodTarget".casefold():
            from .voice_authentication_method_target import VoiceAuthenticationMethodTarget

            return VoiceAuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.vpnConfiguration".casefold():
            from .vpn_configuration import VpnConfiguration

            return VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.vppToken".casefold():
            from .vpp_token import VppToken

            return VppToken()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.vulnerableManagedDevice".casefold():
            from .vulnerable_managed_device import VulnerableManagedDevice

            return VulnerableManagedDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.webAccount".casefold():
            from .web_account import WebAccount

            return WebAccount()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.webApp".casefold():
            from .web_app import WebApp

            return WebApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.webApplicationSegment".casefold():
            from .web_application_segment import WebApplicationSegment

            return WebApplicationSegment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.webPart".casefold():
            from .web_part import WebPart

            return WebPart()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32CatalogApp".casefold():
            from .win32_catalog_app import Win32CatalogApp

            return Win32CatalogApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobApp".casefold():
            from .win32_lob_app import Win32LobApp

            return Win32LobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32MobileAppCatalogPackage".casefold():
            from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage

            return Win32MobileAppCatalogPackage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CertificateProfileBase".casefold():
            from .windows10_certificate_profile_base import Windows10CertificateProfileBase

            return Windows10CertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CompliancePolicy".casefold():
            from .windows10_compliance_policy import Windows10CompliancePolicy

            return Windows10CompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CustomConfiguration".casefold():
            from .windows10_custom_configuration import Windows10CustomConfiguration

            return Windows10CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10DeviceFirmwareConfigurationInterface".casefold():
            from .windows10_device_firmware_configuration_interface import Windows10DeviceFirmwareConfigurationInterface

            return Windows10DeviceFirmwareConfigurationInterface()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EasEmailProfileConfiguration".casefold():
            from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration

            return Windows10EasEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EndpointProtectionConfiguration".casefold():
            from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration

            return Windows10EndpointProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EnrollmentCompletionPageConfiguration".casefold():
            from .windows10_enrollment_completion_page_configuration import Windows10EnrollmentCompletionPageConfiguration

            return Windows10EnrollmentCompletionPageConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EnrollmentCompletionPageConfigurationPolicySetItem".casefold():
            from .windows10_enrollment_completion_page_configuration_policy_set_item import Windows10EnrollmentCompletionPageConfigurationPolicySetItem

            return Windows10EnrollmentCompletionPageConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration".casefold():
            from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration

            return Windows10EnterpriseModernAppManagementConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10GeneralConfiguration".casefold():
            from .windows10_general_configuration import Windows10GeneralConfiguration

            return Windows10GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10ImportedPFXCertificateProfile".casefold():
            from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile

            return Windows10ImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10MobileCompliancePolicy".casefold():
            from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy

            return Windows10MobileCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10NetworkBoundaryConfiguration".casefold():
            from .windows10_network_boundary_configuration import Windows10NetworkBoundaryConfiguration

            return Windows10NetworkBoundaryConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10PFXImportCertificateProfile".casefold():
            from .windows10_p_f_x_import_certificate_profile import Windows10PFXImportCertificateProfile

            return Windows10PFXImportCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10PkcsCertificateProfile".casefold():
            from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile

            return Windows10PkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10SecureAssessmentConfiguration".casefold():
            from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration

            return Windows10SecureAssessmentConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10TeamGeneralConfiguration".casefold():
            from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration

            return Windows10TeamGeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10VpnConfiguration".casefold():
            from .windows10_vpn_configuration import Windows10VpnConfiguration

            return Windows10VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10XCertificateProfile".casefold():
            from .windows10_x_certificate_profile import Windows10XCertificateProfile

            return Windows10XCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10XSCEPCertificateProfile".casefold():
            from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile

            return Windows10XSCEPCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10XTrustedRootCertificate".casefold():
            from .windows10_x_trusted_root_certificate import Windows10XTrustedRootCertificate

            return Windows10XTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10XVpnConfiguration".casefold():
            from .windows10_x_vpn_configuration import Windows10XVpnConfiguration

            return Windows10XVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10XWifiConfiguration".casefold():
            from .windows10_x_wifi_configuration import Windows10XWifiConfiguration

            return Windows10XWifiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81CertificateProfileBase".casefold():
            from .windows81_certificate_profile_base import Windows81CertificateProfileBase

            return Windows81CertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81CompliancePolicy".casefold():
            from .windows81_compliance_policy import Windows81CompliancePolicy

            return Windows81CompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81GeneralConfiguration".casefold():
            from .windows81_general_configuration import Windows81GeneralConfiguration

            return Windows81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81SCEPCertificateProfile".casefold():
            from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile

            return Windows81SCEPCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81TrustedRootCertificate".casefold():
            from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate

            return Windows81TrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81VpnConfiguration".casefold():
            from .windows81_vpn_configuration import Windows81VpnConfiguration

            return Windows81VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81WifiImportConfiguration".casefold():
            from .windows81_wifi_import_configuration import Windows81WifiImportConfiguration

            return Windows81WifiImportConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAppX".casefold():
            from .windows_app_x import WindowsAppX

            return WindowsAppX()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAssignedAccessProfile".casefold():
            from .windows_assigned_access_profile import WindowsAssignedAccessProfile

            return WindowsAssignedAccessProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAutopilotDeploymentProfile".casefold():
            from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile

            return WindowsAutopilotDeploymentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAutopilotDeploymentProfileAssignment".casefold():
            from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment

            return WindowsAutopilotDeploymentProfileAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAutopilotDeploymentProfilePolicySetItem".casefold():
            from .windows_autopilot_deployment_profile_policy_set_item import WindowsAutopilotDeploymentProfilePolicySetItem

            return WindowsAutopilotDeploymentProfilePolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAutopilotDeviceIdentity".casefold():
            from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity

            return WindowsAutopilotDeviceIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAutopilotSettings".casefold():
            from .windows_autopilot_settings import WindowsAutopilotSettings

            return WindowsAutopilotSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsCertificateProfileBase".casefold():
            from .windows_certificate_profile_base import WindowsCertificateProfileBase

            return WindowsCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration".casefold():
            from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration

            return WindowsDefenderAdvancedThreatProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDefenderApplicationControlSupplementalPolicy".casefold():
            from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy

            return WindowsDefenderApplicationControlSupplementalPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDefenderApplicationControlSupplementalPolicyAssignment".casefold():
            from .windows_defender_application_control_supplemental_policy_assignment import WindowsDefenderApplicationControlSupplementalPolicyAssignment

            return WindowsDefenderApplicationControlSupplementalPolicyAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDefenderApplicationControlSupplementalPolicyDeploymentStatus".casefold():
            from .windows_defender_application_control_supplemental_policy_deployment_status import WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus

            return WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDefenderApplicationControlSupplementalPolicyDeploymentSummary".casefold():
            from .windows_defender_application_control_supplemental_policy_deployment_summary import WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary

            return WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDeliveryOptimizationConfiguration".casefold():
            from .windows_delivery_optimization_configuration import WindowsDeliveryOptimizationConfiguration

            return WindowsDeliveryOptimizationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDeviceMalwareState".casefold():
            from .managed_tenants.windows_device_malware_state import WindowsDeviceMalwareState
            from .windows_device_malware_state import WindowsDeviceMalwareState

            return WindowsDeviceMalwareState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDomainJoinConfiguration".casefold():
            from .windows_domain_join_configuration import WindowsDomainJoinConfiguration

            return WindowsDomainJoinConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDriverUpdateInventory".casefold():
            from .windows_driver_update_inventory import WindowsDriverUpdateInventory

            return WindowsDriverUpdateInventory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDriverUpdateProfile".casefold():
            from .windows_driver_update_profile import WindowsDriverUpdateProfile

            return WindowsDriverUpdateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDriverUpdateProfileAssignment".casefold():
            from .windows_driver_update_profile_assignment import WindowsDriverUpdateProfileAssignment

            return WindowsDriverUpdateProfileAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsFeatureUpdateCatalogItem".casefold():
            from .windows_feature_update_catalog_item import WindowsFeatureUpdateCatalogItem

            return WindowsFeatureUpdateCatalogItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsFeatureUpdateProfile".casefold():
            from .windows_feature_update_profile import WindowsFeatureUpdateProfile

            return WindowsFeatureUpdateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsFeatureUpdateProfileAssignment".casefold():
            from .windows_feature_update_profile_assignment import WindowsFeatureUpdateProfileAssignment

            return WindowsFeatureUpdateProfileAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsHealthMonitoringConfiguration".casefold():
            from .windows_health_monitoring_configuration import WindowsHealthMonitoringConfiguration

            return WindowsHealthMonitoringConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsHelloForBusinessAuthenticationMethod".casefold():
            from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod

            return WindowsHelloForBusinessAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsIdentityProtectionConfiguration".casefold():
            from .windows_identity_protection_configuration import WindowsIdentityProtectionConfiguration

            return WindowsIdentityProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtection".casefold():
            from .windows_information_protection import WindowsInformationProtection

            return WindowsInformationProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionAppLearningSummary".casefold():
            from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary

            return WindowsInformationProtectionAppLearningSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionAppLockerFile".casefold():
            from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile

            return WindowsInformationProtectionAppLockerFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionDeviceRegistration".casefold():
            from .windows_information_protection_device_registration import WindowsInformationProtectionDeviceRegistration

            return WindowsInformationProtectionDeviceRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionNetworkLearningSummary".casefold():
            from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary

            return WindowsInformationProtectionNetworkLearningSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionPolicy".casefold():
            from .windows_information_protection_policy import WindowsInformationProtectionPolicy

            return WindowsInformationProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionWipeAction".casefold():
            from .windows_information_protection_wipe_action import WindowsInformationProtectionWipeAction

            return WindowsInformationProtectionWipeAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskConfiguration".casefold():
            from .windows_kiosk_configuration import WindowsKioskConfiguration

            return WindowsKioskConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsMalwareInformation".casefold():
            from .windows_malware_information import WindowsMalwareInformation

            return WindowsMalwareInformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsManagedAppProtection".casefold():
            from .windows_managed_app_protection import WindowsManagedAppProtection

            return WindowsManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsManagedAppRegistration".casefold():
            from .windows_managed_app_registration import WindowsManagedAppRegistration

            return WindowsManagedAppRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsManagedDevice".casefold():
            from .windows_managed_device import WindowsManagedDevice

            return WindowsManagedDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsManagementApp".casefold():
            from .windows_management_app import WindowsManagementApp

            return WindowsManagementApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsManagementAppHealthState".casefold():
            from .windows_management_app_health_state import WindowsManagementAppHealthState

            return WindowsManagementAppHealthState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsManagementAppHealthSummary".casefold():
            from .windows_management_app_health_summary import WindowsManagementAppHealthSummary

            return WindowsManagementAppHealthSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsMicrosoftEdgeApp".casefold():
            from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp

            return WindowsMicrosoftEdgeApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsMobileMSI".casefold():
            from .windows_mobile_m_s_i import WindowsMobileMSI

            return WindowsMobileMSI()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81AppX".casefold():
            from .windows_phone81_app_x import WindowsPhone81AppX

            return WindowsPhone81AppX()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81AppXBundle".casefold():
            from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle

            return WindowsPhone81AppXBundle()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CertificateProfileBase".casefold():
            from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase

            return WindowsPhone81CertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CompliancePolicy".casefold():
            from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy

            return WindowsPhone81CompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CustomConfiguration".casefold():
            from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration

            return WindowsPhone81CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81GeneralConfiguration".casefold():
            from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration

            return WindowsPhone81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81ImportedPFXCertificateProfile".casefold():
            from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile

            return WindowsPhone81ImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81SCEPCertificateProfile".casefold():
            from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile

            return WindowsPhone81SCEPCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81StoreApp".casefold():
            from .windows_phone81_store_app import WindowsPhone81StoreApp

            return WindowsPhone81StoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81TrustedRootCertificate".casefold():
            from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate

            return WindowsPhone81TrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81VpnConfiguration".casefold():
            from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration

            return WindowsPhone81VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhoneEASEmailProfileConfiguration".casefold():
            from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration

            return WindowsPhoneEASEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhoneXAP".casefold():
            from .windows_phone_x_a_p import WindowsPhoneXAP

            return WindowsPhoneXAP()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPrivacyDataAccessControlItem".casefold():
            from .windows_privacy_data_access_control_item import WindowsPrivacyDataAccessControlItem

            return WindowsPrivacyDataAccessControlItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsProtectionState".casefold():
            from .managed_tenants.windows_protection_state import WindowsProtectionState
            from .windows_protection_state import WindowsProtectionState

            return WindowsProtectionState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsQualityUpdateCatalogItem".casefold():
            from .windows_quality_update_catalog_item import WindowsQualityUpdateCatalogItem

            return WindowsQualityUpdateCatalogItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsQualityUpdateProfile".casefold():
            from .windows_quality_update_profile import WindowsQualityUpdateProfile

            return WindowsQualityUpdateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsQualityUpdateProfileAssignment".casefold():
            from .windows_quality_update_profile_assignment import WindowsQualityUpdateProfileAssignment

            return WindowsQualityUpdateProfileAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsSetting".casefold():
            from .windows_setting import WindowsSetting

            return WindowsSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsSettingInstance".casefold():
            from .windows_setting_instance import WindowsSettingInstance

            return WindowsSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsStoreApp".casefold():
            from .windows_store_app import WindowsStoreApp

            return WindowsStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUniversalAppX".casefold():
            from .windows_universal_app_x import WindowsUniversalAppX

            return WindowsUniversalAppX()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUniversalAppXContainedApp".casefold():
            from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp

            return WindowsUniversalAppXContainedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdateCatalogItem".casefold():
            from .windows_update_catalog_item import WindowsUpdateCatalogItem

            return WindowsUpdateCatalogItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdateForBusinessConfiguration".casefold():
            from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration

            return WindowsUpdateForBusinessConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.azureADDevice".casefold():
            from .windows_updates.azure_a_d_device import AzureADDevice

            return AzureADDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.catalog".casefold():
            from .windows_updates.catalog import Catalog

            return Catalog()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.catalogEntry".casefold():
            from .windows_updates.catalog_entry import CatalogEntry

            return CatalogEntry()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.complianceChange".casefold():
            from .windows_updates.compliance_change import ComplianceChange

            return ComplianceChange()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.contentApproval".casefold():
            from .windows_updates.content_approval import ContentApproval

            return ContentApproval()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.deployment".casefold():
            from .windows_updates.deployment import Deployment

            return Deployment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.deploymentAudience".casefold():
            from .windows_updates.deployment_audience import DeploymentAudience

            return DeploymentAudience()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.driverUpdateCatalogEntry".casefold():
            from .windows_updates.driver_update_catalog_entry import DriverUpdateCatalogEntry

            return DriverUpdateCatalogEntry()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.edition".casefold():
            from .windows_updates.edition import Edition

            return Edition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.featureUpdateCatalogEntry".casefold():
            from .windows_updates.feature_update_catalog_entry import FeatureUpdateCatalogEntry

            return FeatureUpdateCatalogEntry()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.knowledgeBaseArticle".casefold():
            from .windows_updates.knowledge_base_article import KnowledgeBaseArticle

            return KnowledgeBaseArticle()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.knownIssue".casefold():
            from .windows_updates.known_issue import KnownIssue

            return KnownIssue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.operationalInsightsConnection".casefold():
            from .windows_updates.operational_insights_connection import OperationalInsightsConnection

            return OperationalInsightsConnection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.product".casefold():
            from .windows_updates.product import Product

            return Product()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.productRevision".casefold():
            from .windows_updates.product_revision import ProductRevision

            return ProductRevision()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.qualityUpdateCatalogEntry".casefold():
            from .windows_updates.quality_update_catalog_entry import QualityUpdateCatalogEntry

            return QualityUpdateCatalogEntry()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.resourceConnection".casefold():
            from .windows_updates.resource_connection import ResourceConnection

            return ResourceConnection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.softwareUpdateCatalogEntry".casefold():
            from .windows_updates.software_update_catalog_entry import SoftwareUpdateCatalogEntry

            return SoftwareUpdateCatalogEntry()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.updatableAsset".casefold():
            from .windows_updates.updatable_asset import UpdatableAsset

            return UpdatableAsset()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.updatableAssetGroup".casefold():
            from .windows_updates.updatable_asset_group import UpdatableAssetGroup

            return UpdatableAssetGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.updatePolicy".casefold():
            from .windows_updates.update_policy import UpdatePolicy

            return UpdatePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdateState".casefold():
            from .windows_update_state import WindowsUpdateState

            return WindowsUpdateState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsVpnConfiguration".casefold():
            from .windows_vpn_configuration import WindowsVpnConfiguration

            return WindowsVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWebApp".casefold():
            from .windows_web_app import WindowsWebApp

            return WindowsWebApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWifiConfiguration".casefold():
            from .windows_wifi_configuration import WindowsWifiConfiguration

            return WindowsWifiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWifiEnterpriseEAPConfiguration".casefold():
            from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration

            return WindowsWifiEnterpriseEAPConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWiredNetworkConfiguration".casefold():
            from .windows_wired_network_configuration import WindowsWiredNetworkConfiguration

            return WindowsWiredNetworkConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.winGetApp".casefold():
            from .win_get_app import WinGetApp

            return WinGetApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbook".casefold():
            from .workbook import Workbook

            return Workbook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookApplication".casefold():
            from .workbook_application import WorkbookApplication

            return WorkbookApplication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChart".casefold():
            from .workbook_chart import WorkbookChart

            return WorkbookChart()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAreaFormat".casefold():
            from .workbook_chart_area_format import WorkbookChartAreaFormat

            return WorkbookChartAreaFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxes".casefold():
            from .workbook_chart_axes import WorkbookChartAxes

            return WorkbookChartAxes()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxis".casefold():
            from .workbook_chart_axis import WorkbookChartAxis

            return WorkbookChartAxis()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxisFormat".casefold():
            from .workbook_chart_axis_format import WorkbookChartAxisFormat

            return WorkbookChartAxisFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxisTitle".casefold():
            from .workbook_chart_axis_title import WorkbookChartAxisTitle

            return WorkbookChartAxisTitle()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxisTitleFormat".casefold():
            from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat

            return WorkbookChartAxisTitleFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartDataLabelFormat".casefold():
            from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat

            return WorkbookChartDataLabelFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartDataLabels".casefold():
            from .workbook_chart_data_labels import WorkbookChartDataLabels

            return WorkbookChartDataLabels()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartFill".casefold():
            from .workbook_chart_fill import WorkbookChartFill

            return WorkbookChartFill()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartFont".casefold():
            from .workbook_chart_font import WorkbookChartFont

            return WorkbookChartFont()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartGridlines".casefold():
            from .workbook_chart_gridlines import WorkbookChartGridlines

            return WorkbookChartGridlines()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartGridlinesFormat".casefold():
            from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat

            return WorkbookChartGridlinesFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartLegend".casefold():
            from .workbook_chart_legend import WorkbookChartLegend

            return WorkbookChartLegend()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartLegendFormat".casefold():
            from .workbook_chart_legend_format import WorkbookChartLegendFormat

            return WorkbookChartLegendFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartLineFormat".casefold():
            from .workbook_chart_line_format import WorkbookChartLineFormat

            return WorkbookChartLineFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartPoint".casefold():
            from .workbook_chart_point import WorkbookChartPoint

            return WorkbookChartPoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartPointFormat".casefold():
            from .workbook_chart_point_format import WorkbookChartPointFormat

            return WorkbookChartPointFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartSeries".casefold():
            from .workbook_chart_series import WorkbookChartSeries

            return WorkbookChartSeries()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartSeriesFormat".casefold():
            from .workbook_chart_series_format import WorkbookChartSeriesFormat

            return WorkbookChartSeriesFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartTitle".casefold():
            from .workbook_chart_title import WorkbookChartTitle

            return WorkbookChartTitle()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartTitleFormat".casefold():
            from .workbook_chart_title_format import WorkbookChartTitleFormat

            return WorkbookChartTitleFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookComment".casefold():
            from .workbook_comment import WorkbookComment

            return WorkbookComment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookCommentReply".casefold():
            from .workbook_comment_reply import WorkbookCommentReply

            return WorkbookCommentReply()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookDocumentTask".casefold():
            from .workbook_document_task import WorkbookDocumentTask

            return WorkbookDocumentTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookDocumentTaskChange".casefold():
            from .workbook_document_task_change import WorkbookDocumentTaskChange

            return WorkbookDocumentTaskChange()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookFilter".casefold():
            from .workbook_filter import WorkbookFilter

            return WorkbookFilter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookFormatProtection".casefold():
            from .workbook_format_protection import WorkbookFormatProtection

            return WorkbookFormatProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookFunctionResult".casefold():
            from .workbook_function_result import WorkbookFunctionResult

            return WorkbookFunctionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookFunctions".casefold():
            from .workbook_functions import WorkbookFunctions

            return WorkbookFunctions()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookNamedItem".casefold():
            from .workbook_named_item import WorkbookNamedItem

            return WorkbookNamedItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookOperation".casefold():
            from .workbook_operation import WorkbookOperation

            return WorkbookOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookPivotTable".casefold():
            from .workbook_pivot_table import WorkbookPivotTable

            return WorkbookPivotTable()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRange".casefold():
            from .workbook_range import WorkbookRange

            return WorkbookRange()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeBorder".casefold():
            from .workbook_range_border import WorkbookRangeBorder

            return WorkbookRangeBorder()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeFill".casefold():
            from .workbook_range_fill import WorkbookRangeFill

            return WorkbookRangeFill()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeFont".casefold():
            from .workbook_range_font import WorkbookRangeFont

            return WorkbookRangeFont()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeFormat".casefold():
            from .workbook_range_format import WorkbookRangeFormat

            return WorkbookRangeFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeSort".casefold():
            from .workbook_range_sort import WorkbookRangeSort

            return WorkbookRangeSort()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeView".casefold():
            from .workbook_range_view import WorkbookRangeView

            return WorkbookRangeView()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookTable".casefold():
            from .workbook_table import WorkbookTable

            return WorkbookTable()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookTableColumn".casefold():
            from .workbook_table_column import WorkbookTableColumn

            return WorkbookTableColumn()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookTableRow".casefold():
            from .workbook_table_row import WorkbookTableRow

            return WorkbookTableRow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookTableSort".casefold():
            from .workbook_table_sort import WorkbookTableSort

            return WorkbookTableSort()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookWorksheet".casefold():
            from .workbook_worksheet import WorkbookWorksheet

            return WorkbookWorksheet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookWorksheetProtection".casefold():
            from .workbook_worksheet_protection import WorkbookWorksheetProtection

            return WorkbookWorksheetProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workforceIntegration".casefold():
            from .workforce_integration import WorkforceIntegration

            return WorkforceIntegration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workplaceSensorDevice".casefold():
            from .workplace_sensor_device import WorkplaceSensorDevice

            return WorkplaceSensorDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workPosition".casefold():
            from .work_position import WorkPosition

            return WorkPosition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workspace".casefold():
            from .workspace import Workspace

            return Workspace()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.x509CertificateAuthenticationMethodConfiguration".casefold():
            from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration

            return X509CertificateAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.x509CertificateCombinationConfiguration".casefold():
            from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration

            return X509CertificateCombinationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.zebraFotaArtifact".casefold():
            from .zebra_fota_artifact import ZebraFotaArtifact

            return ZebraFotaArtifact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.zebraFotaConnector".casefold():
            from .zebra_fota_connector import ZebraFotaConnector

            return ZebraFotaConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.zebraFotaDeployment".casefold():
            from .zebra_fota_deployment import ZebraFotaDeployment

            return ZebraFotaDeployment()
        return Entity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .aad_user_conversation_member import AadUserConversationMember
        from .access_package import AccessPackage
        from .access_package_assignment import AccessPackageAssignment
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
        from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
        from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_request import AccessPackageResourceRequest
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_role_scope import AccessPackageResourceRoleScope
        from .access_package_resource_scope import AccessPackageResourceScope
        from .access_package_subject import AccessPackageSubject
        from .access_review import AccessReview
        from .access_review_decision import AccessReviewDecision
        from .access_review_history_definition import AccessReviewHistoryDefinition
        from .access_review_history_instance import AccessReviewHistoryInstance
        from .access_review_instance import AccessReviewInstance
        from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
        from .access_review_policy import AccessReviewPolicy
        from .access_review_reviewer import AccessReviewReviewer
        from .access_review_schedule_definition import AccessReviewScheduleDefinition
        from .access_review_set import AccessReviewSet
        from .access_review_stage import AccessReviewStage
        from .active_directory_windows_autopilot_deployment_profile import ActiveDirectoryWindowsAutopilotDeploymentProfile
        from .active_users_breakdown_metric import ActiveUsersBreakdownMetric
        from .active_users_metric import ActiveUsersMetric
        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .activity_history_item import ActivityHistoryItem
        from .activity_statistics import ActivityStatistics
        from .add_large_gallery_view_operation import AddLargeGalleryViewOperation
        from .administrative_unit import AdministrativeUnit
        from .admin_apps_and_services import AdminAppsAndServices
        from .admin_consent_request_policy import AdminConsentRequestPolicy
        from .admin_dynamics import AdminDynamics
        from .admin_forms import AdminForms
        from .admin_microsoft365_apps import AdminMicrosoft365Apps
        from .admin_report_settings import AdminReportSettings
        from .admin_todo import AdminTodo
        from .admin_windows import AdminWindows
        from .admin_windows_updates import AdminWindowsUpdates
        from .advanced_threat_protection_onboarding_device_setting_state import AdvancedThreatProtectionOnboardingDeviceSettingState
        from .advanced_threat_protection_onboarding_state_summary import AdvancedThreatProtectionOnboardingStateSummary
        from .agreement import Agreement
        from .agreement_acceptance import AgreementAcceptance
        from .agreement_file import AgreementFile
        from .agreement_file_localization import AgreementFileLocalization
        from .agreement_file_properties import AgreementFileProperties
        from .agreement_file_version import AgreementFileVersion
        from .alert import Alert
        from .allowed_data_location import AllowedDataLocation
        from .allowed_value import AllowedValue
        from .android_certificate_profile_base import AndroidCertificateProfileBase
        from .android_compliance_policy import AndroidCompliancePolicy
        from .android_custom_configuration import AndroidCustomConfiguration
        from .android_device_compliance_local_action_base import AndroidDeviceComplianceLocalActionBase
        from .android_device_compliance_local_action_lock_device import AndroidDeviceComplianceLocalActionLockDevice
        from .android_device_compliance_local_action_lock_device_with_passcode import AndroidDeviceComplianceLocalActionLockDeviceWithPasscode
        from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
        from .android_device_owner_compliance_policy import AndroidDeviceOwnerCompliancePolicy
        from .android_device_owner_derived_credential_authentication_configuration import AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration
        from .android_device_owner_enrollment_profile import AndroidDeviceOwnerEnrollmentProfile
        from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration
        from .android_device_owner_general_device_configuration import AndroidDeviceOwnerGeneralDeviceConfiguration
        from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile
        from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile
        from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile
        from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate
        from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration
        from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration
        from .android_eas_email_profile_configuration import AndroidEasEmailProfileConfiguration
        from .android_enterprise_wi_fi_configuration import AndroidEnterpriseWiFiConfiguration
        from .android_for_work_app import AndroidForWorkApp
        from .android_for_work_app_configuration_schema import AndroidForWorkAppConfigurationSchema
        from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
        from .android_for_work_compliance_policy import AndroidForWorkCompliancePolicy
        from .android_for_work_custom_configuration import AndroidForWorkCustomConfiguration
        from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase
        from .android_for_work_enrollment_profile import AndroidForWorkEnrollmentProfile
        from .android_for_work_enterprise_wi_fi_configuration import AndroidForWorkEnterpriseWiFiConfiguration
        from .android_for_work_general_device_configuration import AndroidForWorkGeneralDeviceConfiguration
        from .android_for_work_gmail_eas_configuration import AndroidForWorkGmailEasConfiguration
        from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile
        from .android_for_work_mobile_app_configuration import AndroidForWorkMobileAppConfiguration
        from .android_for_work_nine_work_eas_configuration import AndroidForWorkNineWorkEasConfiguration
        from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
        from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile
        from .android_for_work_settings import AndroidForWorkSettings
        from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
        from .android_for_work_vpn_configuration import AndroidForWorkVpnConfiguration
        from .android_for_work_wi_fi_configuration import AndroidForWorkWiFiConfiguration
        from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
        from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile
        from .android_lob_app import AndroidLobApp
        from .android_managed_app_protection import AndroidManagedAppProtection
        from .android_managed_app_registration import AndroidManagedAppRegistration
        from .android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings
        from .android_managed_store_app import AndroidManagedStoreApp
        from .android_managed_store_app_configuration import AndroidManagedStoreAppConfiguration
        from .android_managed_store_app_configuration_schema import AndroidManagedStoreAppConfigurationSchema
        from .android_managed_store_web_app import AndroidManagedStoreWebApp
        from .android_oma_cp_configuration import AndroidOmaCpConfiguration
        from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile
        from .android_scep_certificate_profile import AndroidScepCertificateProfile
        from .android_store_app import AndroidStoreApp
        from .android_trusted_root_certificate import AndroidTrustedRootCertificate
        from .android_vpn_configuration import AndroidVpnConfiguration
        from .android_wi_fi_configuration import AndroidWiFiConfiguration
        from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
        from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
        from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
        from .android_work_profile_eas_email_profile_base import AndroidWorkProfileEasEmailProfileBase
        from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration
        from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
        from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
        from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
        from .android_work_profile_pkcs_certificate_profile import AndroidWorkProfilePkcsCertificateProfile
        from .android_work_profile_scep_certificate_profile import AndroidWorkProfileScepCertificateProfile
        from .android_work_profile_trusted_root_certificate import AndroidWorkProfileTrustedRootCertificate
        from .android_work_profile_vpn_configuration import AndroidWorkProfileVpnConfiguration
        from .android_work_profile_wi_fi_configuration import AndroidWorkProfileWiFiConfiguration
        from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
        from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase
        from .aosp_device_owner_compliance_policy import AospDeviceOwnerCompliancePolicy
        from .aosp_device_owner_device_configuration import AospDeviceOwnerDeviceConfiguration
        from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration
        from .aosp_device_owner_pkcs_certificate_profile import AospDeviceOwnerPkcsCertificateProfile
        from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile
        from .aosp_device_owner_trusted_root_certificate import AospDeviceOwnerTrustedRootCertificate
        from .aosp_device_owner_wi_fi_configuration import AospDeviceOwnerWiFiConfiguration
        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .apple_enrollment_profile_assignment import AppleEnrollmentProfileAssignment
        from .apple_expedited_checkin_configuration_base import AppleExpeditedCheckinConfigurationBase
        from .apple_managed_identity_provider import AppleManagedIdentityProvider
        from .apple_push_notification_certificate import ApplePushNotificationCertificate
        from .apple_user_initiated_enrollment_profile import AppleUserInitiatedEnrollmentProfile
        from .apple_vpn_configuration import AppleVpnConfiguration
        from .apple_vpp_token_troubleshooting_event import AppleVppTokenTroubleshootingEvent
        from .application import Application
        from .application_segment import ApplicationSegment
        from .application_sign_in_detailed_summary import ApplicationSignInDetailedSummary
        from .application_sign_in_summary import ApplicationSignInSummary
        from .application_template import ApplicationTemplate
        from .approval import Approval
        from .approval_step import ApprovalStep
        from .approval_workflow_provider import ApprovalWorkflowProvider
        from .app_consent_approval_route import AppConsentApprovalRoute
        from .app_consent_request import AppConsentRequest
        from .app_credential_sign_in_activity import AppCredentialSignInActivity
        from .app_log_collection_request import AppLogCollectionRequest
        from .app_management_policy import AppManagementPolicy
        from .app_role_assignment import AppRoleAssignment
        from .app_scope import AppScope
        from .app_vulnerability_managed_device import AppVulnerabilityManagedDevice
        from .app_vulnerability_mobile_app import AppVulnerabilityMobileApp
        from .app_vulnerability_task import AppVulnerabilityTask
        from .assigned_compute_instance_details import AssignedComputeInstanceDetails
        from .assignment_filter_evaluation_status_details import AssignmentFilterEvaluationStatusDetails
        from .associated_team_info import AssociatedTeamInfo
        from .attachment import Attachment
        from .attachment_base import AttachmentBase
        from .attachment_session import AttachmentSession
        from .attack_simulation_operation import AttackSimulationOperation
        from .attack_simulation_root import AttackSimulationRoot
        from .attendance_record import AttendanceRecord
        from .attribute_mapping_function_schema import AttributeMappingFunctionSchema
        from .attribute_set import AttributeSet
        from .audio_routing_group import AudioRoutingGroup
        from .audit_event import AuditEvent
        from .authentication import Authentication
        from .authentications_metric import AuthenticationsMetric
        from .authentication_combination_configuration import AuthenticationCombinationConfiguration
        from .authentication_context_class_reference import AuthenticationContextClassReference
        from .authentication_events_flow import AuthenticationEventsFlow
        from .authentication_events_policy import AuthenticationEventsPolicy
        from .authentication_event_listener import AuthenticationEventListener
        from .authentication_flows_policy import AuthenticationFlowsPolicy
        from .authentication_listener import AuthenticationListener
        from .authentication_method import AuthenticationMethod
        from .authentication_methods_policy import AuthenticationMethodsPolicy
        from .authentication_methods_root import AuthenticationMethodsRoot
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_mode_detail import AuthenticationMethodModeDetail
        from .authentication_method_target import AuthenticationMethodTarget
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .authentication_strength_root import AuthenticationStrengthRoot
        from .authored_note import AuthoredNote
        from .authorization_policy import AuthorizationPolicy
        from .authorization_system import AuthorizationSystem
        from .authorization_system_identity import AuthorizationSystemIdentity
        from .authorization_system_resource import AuthorizationSystemResource
        from .authorization_system_type_action import AuthorizationSystemTypeAction
        from .authorization_system_type_service import AuthorizationSystemTypeService
        from .aws_access_key import AwsAccessKey
        from .aws_authorization_system import AwsAuthorizationSystem
        from .aws_authorization_system_resource import AwsAuthorizationSystemResource
        from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction
        from .aws_ec2_instance import AwsEc2Instance
        from .aws_external_system_access_finding import AwsExternalSystemAccessFinding
        from .aws_external_system_access_role_finding import AwsExternalSystemAccessRoleFinding
        from .aws_group import AwsGroup
        from .aws_identity import AwsIdentity
        from .aws_identity_access_management_key_age_finding import AwsIdentityAccessManagementKeyAgeFinding
        from .aws_identity_access_management_key_usage_finding import AwsIdentityAccessManagementKeyUsageFinding
        from .aws_lambda import AwsLambda
        from .aws_policy import AwsPolicy
        from .aws_role import AwsRole
        from .aws_secret_information_access_finding import AwsSecretInformationAccessFinding
        from .aws_security_tool_administration_finding import AwsSecurityToolAdministrationFinding
        from .aws_user import AwsUser
        from .azure_authorization_system import AzureAuthorizationSystem
        from .azure_authorization_system_resource import AzureAuthorizationSystemResource
        from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction
        from .azure_a_d_authentication import AzureADAuthentication
        from .azure_a_d_windows_autopilot_deployment_profile import AzureADWindowsAutopilotDeploymentProfile
        from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
        from .azure_group import AzureGroup
        from .azure_identity import AzureIdentity
        from .azure_managed_identity import AzureManagedIdentity
        from .azure_role_definition import AzureRoleDefinition
        from .azure_serverless_function import AzureServerlessFunction
        from .azure_service_principal import AzureServicePrincipal
        from .azure_user import AzureUser
        from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicy
        from .b2c_identity_user_flow import B2cIdentityUserFlow
        from .b2x_identity_user_flow import B2xIdentityUserFlow
        from .base_item import BaseItem
        from .base_item_version import BaseItemVersion
        from .base_site_page import BaseSitePage
        from .bitlocker import Bitlocker
        from .bitlocker_recovery_key import BitlockerRecoveryKey
        from .booking_appointment import BookingAppointment
        from .booking_business import BookingBusiness
        from .booking_currency import BookingCurrency
        from .booking_customer import BookingCustomer
        from .booking_custom_question import BookingCustomQuestion
        from .booking_named_entity import BookingNamedEntity
        from .booking_person import BookingPerson
        from .booking_service import BookingService
        from .booking_staff_member import BookingStaffMember
        from .browser_shared_cookie import BrowserSharedCookie
        from .browser_site import BrowserSite
        from .browser_site_list import BrowserSiteList
        from .built_in_identity_provider import BuiltInIdentityProvider
        from .bulk_upload import BulkUpload
        from .business_flow import BusinessFlow
        from .business_flow_template import BusinessFlowTemplate
        from .business_scenario import BusinessScenario
        from .business_scenario_planner import BusinessScenarioPlanner
        from .business_scenario_plan_reference import BusinessScenarioPlanReference
        from .business_scenario_task import BusinessScenarioTask
        from .calendar import Calendar
        from .calendar_group import CalendarGroup
        from .calendar_permission import CalendarPermission
        from .calendar_sharing_message import CalendarSharingMessage
        from .call import Call
        from .call_activity_statistics import CallActivityStatistics
        from .call_event import CallEvent
        from .call_recording import CallRecording
        from .call_records.call_record import CallRecord
        from .call_records.organizer import Organizer
        from .call_records.participant import Participant
        from .call_records.participant_base import ParticipantBase
        from .call_records.segment import Segment
        from .call_records.session import Session
        from .call_transcript import CallTranscript
        from .cancel_media_processing_operation import CancelMediaProcessingOperation
        from .canvas_layout import CanvasLayout
        from .cart_to_class_association import CartToClassAssociation
        from .certificate_authority_as_entity import CertificateAuthorityAsEntity
        from .certificate_authority_path import CertificateAuthorityPath
        from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
        from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
        from .certificate_connector_details import CertificateConnectorDetails
        from .change_tracked_entity import ChangeTrackedEntity
        from .channel import Channel
        from .chat import Chat
        from .chat_activity_statistics import ChatActivityStatistics
        from .chat_message import ChatMessage
        from .chat_message_hosted_content import ChatMessageHostedContent
        from .chat_message_info import ChatMessageInfo
        from .checklist_item import ChecklistItem
        from .chrome_o_s_onboarding_settings import ChromeOSOnboardingSettings
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .classification_job_response import ClassificationJobResponse
        from .cloud_app_security_profile import CloudAppSecurityProfile
        from .cloud_clipboard_item import CloudClipboardItem
        from .cloud_clipboard_root import CloudClipboardRoot
        from .cloud_pc_audit_event import CloudPcAuditEvent
        from .cloud_pc_bulk_action import CloudPcBulkAction
        from .cloud_pc_bulk_disaster_recovery_failback import CloudPcBulkDisasterRecoveryFailback
        from .cloud_pc_bulk_disaster_recovery_failover import CloudPcBulkDisasterRecoveryFailover
        from .cloud_pc_bulk_modify_disk_encryption_type import CloudPcBulkModifyDiskEncryptionType
        from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff
        from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn
        from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision
        from .cloud_pc_bulk_resize import CloudPcBulkResize
        from .cloud_pc_bulk_restart import CloudPcBulkRestart
        from .cloud_pc_bulk_restore import CloudPcBulkRestore
        from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot
        from .cloud_pc_cross_cloud_government_organization_mapping import CloudPcCrossCloudGovernmentOrganizationMapping
        from .cloud_pc_device_image import CloudPcDeviceImage
        from .cloud_pc_export_job import CloudPcExportJob
        from .cloud_pc_external_partner_setting import CloudPcExternalPartnerSetting
        from .cloud_pc_front_line_service_plan import CloudPcFrontLineServicePlan
        from .cloud_pc_gallery_image import CloudPcGalleryImage
        from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
        from .cloud_pc_organization_settings import CloudPcOrganizationSettings
        from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
        from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
        from .cloud_pc_reports import CloudPcReports
        from .cloud_pc_service_plan import CloudPcServicePlan
        from .cloud_pc_shared_use_service_plan import CloudPcSharedUseServicePlan
        from .cloud_pc_snapshot import CloudPcSnapshot
        from .cloud_pc_supported_region import CloudPcSupportedRegion
        from .cloud_pc_user_setting import CloudPcUserSetting
        from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment
        from .cloud_p_c import CloudPC
        from .cloud_p_c_connectivity_issue import CloudPCConnectivityIssue
        from .column_definition import ColumnDefinition
        from .column_link import ColumnLink
        from .comanagement_eligible_device import ComanagementEligibleDevice
        from .command import Command
        from .comms_operation import CommsOperation
        from .community import Community
        from .company_subscription import CompanySubscription
        from .compliance_management_partner import ComplianceManagementPartner
        from .conditional_access_policy import ConditionalAccessPolicy
        from .conditional_access_root import ConditionalAccessRoot
        from .conditional_access_template import ConditionalAccessTemplate
        from .conditional_access_what_if_policy import ConditionalAccessWhatIfPolicy
        from .config_manager_collection import ConfigManagerCollection
        from .connected_organization import ConnectedOrganization
        from .connection_operation import ConnectionOperation
        from .connector import Connector
        from .connector_group import ConnectorGroup
        from .contact import Contact
        from .contact_folder import ContactFolder
        from .contact_merge_suggestions import ContactMergeSuggestions
        from .content_sharing_session import ContentSharingSession
        from .content_type import ContentType
        from .continuous_access_evaluation_policy import ContinuousAccessEvaluationPolicy
        from .contract import Contract
        from .conversation import Conversation
        from .conversation_member import ConversationMember
        from .conversation_thread import ConversationThread
        from .cors_configuration_v2 import CorsConfiguration_v2
        from .country_named_location import CountryNamedLocation
        from .credential_usage_summary import CredentialUsageSummary
        from .credential_user_registration_count import CredentialUserRegistrationCount
        from .credential_user_registration_details import CredentialUserRegistrationDetails
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault
        from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
        from .custom_app_scope import CustomAppScope
        from .custom_authentication_extension import CustomAuthenticationExtension
        from .custom_callout_extension import CustomCalloutExtension
        from .custom_extension_handler import CustomExtensionHandler
        from .custom_extension_stage_setting import CustomExtensionStageSetting
        from .custom_security_attribute_audit import CustomSecurityAttributeAudit
        from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
        from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
        from .daily_inactive_users_metric import DailyInactiveUsersMetric
        from .daily_user_insight_metrics_root import DailyUserInsightMetricsRoot
        from .data_classification_service import DataClassificationService
        from .data_collection_info import DataCollectionInfo
        from .data_loss_prevention_policy import DataLossPreventionPolicy
        from .data_policy_operation import DataPolicyOperation
        from .data_sharing_consent import DataSharingConsent
        from .day_note import DayNote
        from .default_device_compliance_policy import DefaultDeviceCompliancePolicy
        from .default_managed_app_protection import DefaultManagedAppProtection
        from .default_user_role_override import DefaultUserRoleOverride
        from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment
        from .delegated_admin_customer import DelegatedAdminCustomer
        from .delegated_admin_relationship import DelegatedAdminRelationship
        from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
        from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest
        from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail
        from .delegated_permission_classification import DelegatedPermissionClassification
        from .deleted_chat import DeletedChat
        from .deleted_item_container import DeletedItemContainer
        from .deleted_team import DeletedTeam
        from .delta_participants import DeltaParticipants
        from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
        from .dep_enrollment_profile import DepEnrollmentProfile
        from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
        from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
        from .dep_onboarding_setting import DepOnboardingSetting
        from .detected_app import DetectedApp
        from .device import Device
        from .device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter
        from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
        from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
        from .device_app_management import DeviceAppManagement
        from .device_app_management_task import DeviceAppManagementTask
        from .device_category import DeviceCategory
        from .device_comanagement_authority_configuration import DeviceComanagementAuthorityConfiguration
        from .device_compliance_action_item import DeviceComplianceActionItem
        from .device_compliance_device_overview import DeviceComplianceDeviceOverview
        from .device_compliance_device_status import DeviceComplianceDeviceStatus
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
        from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
        from .device_compliance_policy_group_assignment import DeviceCompliancePolicyGroupAssignment
        from .device_compliance_policy_policy_set_item import DeviceCompliancePolicyPolicySetItem
        from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
        from .device_compliance_policy_state import DeviceCompliancePolicyState
        from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
        from .device_compliance_script import DeviceComplianceScript
        from .device_compliance_script_device_state import DeviceComplianceScriptDeviceState
        from .device_compliance_script_run_summary import DeviceComplianceScriptRunSummary
        from .device_compliance_setting_state import DeviceComplianceSettingState
        from .device_compliance_user_overview import DeviceComplianceUserOverview
        from .device_compliance_user_status import DeviceComplianceUserStatus
        from .device_configuration import DeviceConfiguration
        from .device_configuration_assignment import DeviceConfigurationAssignment
        from .device_configuration_conflict_summary import DeviceConfigurationConflictSummary
        from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
        from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
        from .device_configuration_device_status import DeviceConfigurationDeviceStatus
        from .device_configuration_group_assignment import DeviceConfigurationGroupAssignment
        from .device_configuration_policy_set_item import DeviceConfigurationPolicySetItem
        from .device_configuration_profile import DeviceConfigurationProfile
        from .device_configuration_state import DeviceConfigurationState
        from .device_configuration_user_overview import DeviceConfigurationUserOverview
        from .device_configuration_user_state_summary import DeviceConfigurationUserStateSummary
        from .device_configuration_user_status import DeviceConfigurationUserStatus
        from .device_custom_attribute_shell_script import DeviceCustomAttributeShellScript
        from .device_enrollment_configuration import DeviceEnrollmentConfiguration
        from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
        from .device_enrollment_notification_configuration import DeviceEnrollmentNotificationConfiguration
        from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
        from .device_enrollment_platform_restriction_configuration import DeviceEnrollmentPlatformRestrictionConfiguration
        from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
        from .device_health_script import DeviceHealthScript
        from .device_health_script_assignment import DeviceHealthScriptAssignment
        from .device_health_script_device_state import DeviceHealthScriptDeviceState
        from .device_health_script_run_summary import DeviceHealthScriptRunSummary
        from .device_install_state import DeviceInstallState
        from .device_local_credential_info import DeviceLocalCredentialInfo
        from .device_log_collection_response import DeviceLogCollectionResponse
        from .device_management.alert_record import AlertRecord
        from .device_management.alert_rule import AlertRule
        from .device_management.device_management import DeviceManagement
        from .device_management.monitoring import Monitoring
        from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition
        from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
        from .device_management_autopilot_event import DeviceManagementAutopilotEvent
        from .device_management_autopilot_policy_status_detail import DeviceManagementAutopilotPolicyStatusDetail
        from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
        from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration
        from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition
        from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance
        from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition
        from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
        from .device_management_compliance_action_item import DeviceManagementComplianceActionItem
        from .device_management_compliance_policy import DeviceManagementCompliancePolicy
        from .device_management_compliance_scheduled_action_for_rule import DeviceManagementComplianceScheduledActionForRule
        from .device_management_configuration_category import DeviceManagementConfigurationCategory
        from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
        from .device_management_configuration_choice_setting_definition import DeviceManagementConfigurationChoiceSettingDefinition
        from .device_management_configuration_policy import DeviceManagementConfigurationPolicy
        from .device_management_configuration_policy_assignment import DeviceManagementConfigurationPolicyAssignment
        from .device_management_configuration_policy_policy_set_item import DeviceManagementConfigurationPolicyPolicySetItem
        from .device_management_configuration_policy_template import DeviceManagementConfigurationPolicyTemplate
        from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition
        from .device_management_configuration_setting import DeviceManagementConfigurationSetting
        from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
        from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition
        from .device_management_configuration_setting_group_definition import DeviceManagementConfigurationSettingGroupDefinition
        from .device_management_configuration_setting_template import DeviceManagementConfigurationSettingTemplate
        from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition
        from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition
        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
        from .device_management_domain_join_connector import DeviceManagementDomainJoinConnector
        from .device_management_exchange_connector import DeviceManagementExchangeConnector
        from .device_management_exchange_on_premises_policy import DeviceManagementExchangeOnPremisesPolicy
        from .device_management_export_job import DeviceManagementExportJob
        from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
        from .device_management_intent import DeviceManagementIntent
        from .device_management_intent_assignment import DeviceManagementIntentAssignment
        from .device_management_intent_device_setting_state_summary import DeviceManagementIntentDeviceSettingStateSummary
        from .device_management_intent_device_state import DeviceManagementIntentDeviceState
        from .device_management_intent_device_state_summary import DeviceManagementIntentDeviceStateSummary
        from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory
        from .device_management_intent_user_state import DeviceManagementIntentUserState
        from .device_management_intent_user_state_summary import DeviceManagementIntentUserStateSummary
        from .device_management_partner import DeviceManagementPartner
        from .device_management_reports import DeviceManagementReports
        from .device_management_resource_access_profile_assignment import DeviceManagementResourceAccessProfileAssignment
        from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase
        from .device_management_reusable_policy_setting import DeviceManagementReusablePolicySetting
        from .device_management_script import DeviceManagementScript
        from .device_management_script_assignment import DeviceManagementScriptAssignment
        from .device_management_script_device_state import DeviceManagementScriptDeviceState
        from .device_management_script_group_assignment import DeviceManagementScriptGroupAssignment
        from .device_management_script_policy_set_item import DeviceManagementScriptPolicySetItem
        from .device_management_script_run_summary import DeviceManagementScriptRunSummary
        from .device_management_script_user_state import DeviceManagementScriptUserState
        from .device_management_setting_category import DeviceManagementSettingCategory
        from .device_management_setting_definition import DeviceManagementSettingDefinition
        from .device_management_setting_instance import DeviceManagementSettingInstance
        from .device_management_string_setting_instance import DeviceManagementStringSettingInstance
        from .device_management_template import DeviceManagementTemplate
        from .device_management_template_insights_definition import DeviceManagementTemplateInsightsDefinition
        from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
        from .device_registration_policy import DeviceRegistrationPolicy
        from .device_setup_configuration import DeviceSetupConfiguration
        from .device_shell_script import DeviceShellScript
        from .directory import Directory
        from .directory_audit import DirectoryAudit
        from .directory_definition import DirectoryDefinition
        from .directory_object import DirectoryObject
        from .directory_object_partner_reference import DirectoryObjectPartnerReference
        from .directory_role import DirectoryRole
        from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicy
        from .directory_role_template import DirectoryRoleTemplate
        from .directory_setting import DirectorySetting
        from .directory_setting_template import DirectorySettingTemplate
        from .dlp_evaluate_policies_job_response import DlpEvaluatePoliciesJobResponse
        from .document import Document
        from .document_comment import DocumentComment
        from .document_comment_reply import DocumentCommentReply
        from .document_set_version import DocumentSetVersion
        from .domain import Domain
        from .domain_dns_cname_record import DomainDnsCnameRecord
        from .domain_dns_mx_record import DomainDnsMxRecord
        from .domain_dns_record import DomainDnsRecord
        from .domain_dns_srv_record import DomainDnsSrvRecord
        from .domain_dns_txt_record import DomainDnsTxtRecord
        from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
        from .domain_security_profile import DomainSecurityProfile
        from .drive import Drive
        from .drive_item import DriveItem
        from .drive_item_version import DriveItemVersion
        from .eas_email_profile_configuration_base import EasEmailProfileConfigurationBase
        from .edge import Edge
        from .ediscovery.add_to_review_set_operation import AddToReviewSetOperation
        from .ediscovery.case import Case
        from .ediscovery.case_export_operation import CaseExportOperation
        from .ediscovery.case_hold_operation import CaseHoldOperation
        from .ediscovery.case_index_operation import CaseIndexOperation
        from .ediscovery.case_operation import CaseOperation
        from .ediscovery.case_settings import CaseSettings
        from .ediscovery.custodian import Custodian
        from .ediscovery.data_source import DataSource
        from .ediscovery.data_source_container import DataSourceContainer
        from .ediscovery.ediscoveryroot import Ediscoveryroot
        from .ediscovery.estimate_statistics_operation import EstimateStatisticsOperation
        from .ediscovery.legal_hold import LegalHold
        from .ediscovery.noncustodial_data_source import NoncustodialDataSource
        from .ediscovery.purge_data_operation import PurgeDataOperation
        from .ediscovery.review_set import ReviewSet
        from .ediscovery.review_set_query import ReviewSetQuery
        from .ediscovery.site_source import SiteSource
        from .ediscovery.source_collection import SourceCollection
        from .ediscovery.tag import Tag
        from .ediscovery.tag_operation import TagOperation
        from .ediscovery.unified_group_source import UnifiedGroupSource
        from .ediscovery.user_source import UserSource
        from .edition_upgrade_configuration import EditionUpgradeConfiguration
        from .educational_activity import EducationalActivity
        from .education_assignment import EducationAssignment
        from .education_assignment_defaults import EducationAssignmentDefaults
        from .education_assignment_resource import EducationAssignmentResource
        from .education_assignment_settings import EducationAssignmentSettings
        from .education_category import EducationCategory
        from .education_class import EducationClass
        from .education_feedback_outcome import EducationFeedbackOutcome
        from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome
        from .education_grading_category import EducationGradingCategory
        from .education_grading_scheme import EducationGradingScheme
        from .education_module import EducationModule
        from .education_module_resource import EducationModuleResource
        from .education_organization import EducationOrganization
        from .education_outcome import EducationOutcome
        from .education_points_outcome import EducationPointsOutcome
        from .education_rubric import EducationRubric
        from .education_rubric_outcome import EducationRubricOutcome
        from .education_school import EducationSchool
        from .education_submission import EducationSubmission
        from .education_submission_resource import EducationSubmissionResource
        from .education_synchronization_error import EducationSynchronizationError
        from .education_synchronization_profile import EducationSynchronizationProfile
        from .education_synchronization_profile_status import EducationSynchronizationProfileStatus
        from .education_user import EducationUser
        from .email_activity_statistics import EmailActivityStatistics
        from .email_authentication_method import EmailAuthenticationMethod
        from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration
        from .email_file_assessment_request import EmailFileAssessmentRequest
        from .embedded_s_i_m_activation_code_pool import EmbeddedSIMActivationCodePool
        from .embedded_s_i_m_activation_code_pool_assignment import EmbeddedSIMActivationCodePoolAssignment
        from .embedded_s_i_m_device_state import EmbeddedSIMDeviceState
        from .employee_experience_user import EmployeeExperienceUser
        from .encrypted_aws_storage_bucket_finding import EncryptedAwsStorageBucketFinding
        from .encrypted_azure_storage_account_finding import EncryptedAzureStorageAccountFinding
        from .encrypted_gcp_storage_bucket_finding import EncryptedGcpStorageBucketFinding
        from .endpoint import Endpoint
        from .end_user_notification import EndUserNotification
        from .end_user_notification_detail import EndUserNotificationDetail
        from .engagement_async_operation import EngagementAsyncOperation
        from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
        from .enrollment_profile import EnrollmentProfile
        from .enrollment_restrictions_configuration_policy_set_item import EnrollmentRestrictionsConfigurationPolicySetItem
        from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
        from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
        from .entitlement_management import EntitlementManagement
        from .entitlement_management_settings import EntitlementManagementSettings
        from .evaluate_label_job_response import EvaluateLabelJobResponse
        from .event import Event
        from .event_message import EventMessage
        from .event_message_request import EventMessageRequest
        from .event_message_response import EventMessageResponse
        from .exact_match_data_store import ExactMatchDataStore
        from .exact_match_data_store_base import ExactMatchDataStoreBase
        from .exact_match_job_base import ExactMatchJobBase
        from .exact_match_lookup_job import ExactMatchLookupJob
        from .exact_match_session import ExactMatchSession
        from .exact_match_session_base import ExactMatchSessionBase
        from .exact_match_upload_agent import ExactMatchUploadAgent
        from .extension import Extension
        from .extension_property import ExtensionProperty
        from .external import External
        from .externally_accessible_aws_storage_bucket_finding import ExternallyAccessibleAwsStorageBucketFinding
        from .externally_accessible_azure_blob_container_finding import ExternallyAccessibleAzureBlobContainerFinding
        from .externally_accessible_gcp_storage_bucket_finding import ExternallyAccessibleGcpStorageBucketFinding
        from .external_connection import ExternalConnection
        from .external_connectors.connection_operation import ConnectionOperation
        from .external_connectors.connection_quota import ConnectionQuota
        from .external_connectors.external_activity import ExternalActivity
        from .external_connectors.external_activity_result import ExternalActivityResult
        from .external_connectors.external_connection import ExternalConnection
        from .external_connectors.external_group import ExternalGroup
        from .external_connectors.external_item import ExternalItem
        from .external_connectors.identity import Identity
        from .external_connectors.schema import Schema
        from .external_domain_name import ExternalDomainName
        from .external_group import ExternalGroup
        from .external_identities_policy import ExternalIdentitiesPolicy
        from .external_item import ExternalItem
        from .external_meeting_registrant import ExternalMeetingRegistrant
        from .external_meeting_registration import ExternalMeetingRegistration
        from .external_profile import ExternalProfile
        from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow
        from .external_user_profile import ExternalUserProfile
        from .e_book_install_summary import EBookInstallSummary
        from .feature_rollout_policy import FeatureRolloutPolicy
        from .federated_identity_credential import FederatedIdentityCredential
        from .federated_token_validation_policy import FederatedTokenValidationPolicy
        from .fido2_authentication_method import Fido2AuthenticationMethod
        from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
        from .fido2_combination_configuration import Fido2CombinationConfiguration
        from .field_value_set import FieldValueSet
        from .file_assessment_request import FileAssessmentRequest
        from .file_attachment import FileAttachment
        from .file_classification_request import FileClassificationRequest
        from .file_security_profile import FileSecurityProfile
        from .filter_operator_schema import FilterOperatorSchema
        from .finding import Finding
        from .focus_activity_statistics import FocusActivityStatistics
        from .gcp_authorization_system import GcpAuthorizationSystem
        from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
        from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
        from .gcp_cloud_function import GcpCloudFunction
        from .gcp_group import GcpGroup
        from .gcp_identity import GcpIdentity
        from .gcp_role import GcpRole
        from .gcp_service_account import GcpServiceAccount
        from .gcp_user import GcpUser
        from .goals import Goals
        from .goals_export_job import GoalsExportJob
        from .governance_insight import GovernanceInsight
        from .governance_policy_template import GovernancePolicyTemplate
        from .governance_resource import GovernanceResource
        from .governance_role_assignment import GovernanceRoleAssignment
        from .governance_role_assignment_request import GovernanceRoleAssignmentRequest
        from .governance_role_definition import GovernanceRoleDefinition
        from .governance_role_setting import GovernanceRoleSetting
        from .governance_subject import GovernanceSubject
        from .group import Group
        from .group_lifecycle_policy import GroupLifecyclePolicy
        from .group_policy_category import GroupPolicyCategory
        from .group_policy_configuration import GroupPolicyConfiguration
        from .group_policy_configuration_assignment import GroupPolicyConfigurationAssignment
        from .group_policy_definition import GroupPolicyDefinition
        from .group_policy_definition_file import GroupPolicyDefinitionFile
        from .group_policy_definition_value import GroupPolicyDefinitionValue
        from .group_policy_migration_report import GroupPolicyMigrationReport
        from .group_policy_object_file import GroupPolicyObjectFile
        from .group_policy_operation import GroupPolicyOperation
        from .group_policy_presentation import GroupPolicyPresentation
        from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
        from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
        from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
        from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
        from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
        from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
        from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
        from .group_policy_presentation_text import GroupPolicyPresentationText
        from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox
        from .group_policy_presentation_value import GroupPolicyPresentationValue
        from .group_policy_presentation_value_boolean import GroupPolicyPresentationValueBoolean
        from .group_policy_presentation_value_decimal import GroupPolicyPresentationValueDecimal
        from .group_policy_presentation_value_list import GroupPolicyPresentationValueList
        from .group_policy_presentation_value_long_decimal import GroupPolicyPresentationValueLongDecimal
        from .group_policy_presentation_value_multi_text import GroupPolicyPresentationValueMultiText
        from .group_policy_presentation_value_text import GroupPolicyPresentationValueText
        from .group_policy_setting_mapping import GroupPolicySettingMapping
        from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile
        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation
        from .hardware_configuration import HardwareConfiguration
        from .hardware_configuration_assignment import HardwareConfigurationAssignment
        from .hardware_configuration_device_state import HardwareConfigurationDeviceState
        from .hardware_configuration_run_summary import HardwareConfigurationRunSummary
        from .hardware_configuration_user_state import HardwareConfigurationUserState
        from .hardware_oath_authentication_method_configuration import HardwareOathAuthenticationMethodConfiguration
        from .hardware_password_info import HardwarePasswordInfo
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .horizontal_section import HorizontalSection
        from .horizontal_section_column import HorizontalSectionColumn
        from .host_security_profile import HostSecurityProfile
        from .identity_api_connector import IdentityApiConnector
        from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
        from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute
        from .identity_finding import IdentityFinding
        from .identity_governance.custom_task_extension import CustomTaskExtension
        from .identity_governance.lifecycle_management_settings import LifecycleManagementSettings
        from .identity_governance.lifecycle_workflows_container import LifecycleWorkflowsContainer
        from .identity_governance.run import Run
        from .identity_governance.task import Task
        from .identity_governance.task_definition import TaskDefinition
        from .identity_governance.task_processing_result import TaskProcessingResult
        from .identity_governance.task_report import TaskReport
        from .identity_governance.user_processing_result import UserProcessingResult
        from .identity_governance.workflow_template import WorkflowTemplate
        from .identity_provider import IdentityProvider
        from .identity_provider_base import IdentityProviderBase
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .identity_user_flow import IdentityUserFlow
        from .identity_user_flow_attribute import IdentityUserFlowAttribute
        from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
        from .impacted_resource import ImpactedResource
        from .imported_apple_device_identity import ImportedAppleDeviceIdentity
        from .imported_apple_device_identity_result import ImportedAppleDeviceIdentityResult
        from .imported_device_identity import ImportedDeviceIdentity
        from .imported_device_identity_result import ImportedDeviceIdentityResult
        from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
        from .imported_windows_autopilot_device_identity_upload import ImportedWindowsAutopilotDeviceIdentityUpload
        from .inactive_aws_resource_finding import InactiveAwsResourceFinding
        from .inactive_aws_role_finding import InactiveAwsRoleFinding
        from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding
        from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding
        from .inactive_group_finding import InactiveGroupFinding
        from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding
        from .inactive_users_by_application_metric_base import InactiveUsersByApplicationMetricBase
        from .inactive_users_metric_base import InactiveUsersMetricBase
        from .inactive_user_finding import InactiveUserFinding
        from .industry_data.administrative_unit_provisioning_flow import AdministrativeUnitProvisioningFlow
        from .industry_data.azure_data_lake_connector import AzureDataLakeConnector
        from .industry_data.class_group_provisioning_flow import ClassGroupProvisioningFlow
        from .industry_data.file_data_connector import FileDataConnector
        from .industry_data.file_validate_operation import FileValidateOperation
        from .industry_data.inbound_file_flow import InboundFileFlow
        from .industry_data.inbound_flow import InboundFlow
        from .industry_data.inbound_flow_activity import InboundFlowActivity
        from .industry_data.industry_data_activity import IndustryDataActivity
        from .industry_data.industry_data_connector import IndustryDataConnector
        from .industry_data.industry_data_root import IndustryDataRoot
        from .industry_data.industry_data_run import IndustryDataRun
        from .industry_data.industry_data_run_activity import IndustryDataRunActivity
        from .industry_data.outbound_flow_activity import OutboundFlowActivity
        from .industry_data.outbound_provisioning_flow_set import OutboundProvisioningFlowSet
        from .industry_data.provisioning_flow import ProvisioningFlow
        from .industry_data.reference_definition import ReferenceDefinition
        from .industry_data.role_group import RoleGroup
        from .industry_data.security_group_provisioning_flow import SecurityGroupProvisioningFlow
        from .industry_data.source_system_definition import SourceSystemDefinition
        from .industry_data.user_provisioning_flow import UserProvisioningFlow
        from .industry_data.validate_operation import ValidateOperation
        from .industry_data.year_time_period_definition import YearTimePeriodDefinition
        from .inference_classification import InferenceClassification
        from .inference_classification_override import InferenceClassificationOverride
        from .information_protection import InformationProtection
        from .information_protection_label import InformationProtectionLabel
        from .information_protection_policy import InformationProtectionPolicy
        from .insights_settings import InsightsSettings
        from .insight_summary import InsightSummary
        from .internal_domain_federation import InternalDomainFederation
        from .internet_explorer_mode import InternetExplorerMode
        from .intune_branding_profile import IntuneBrandingProfile
        from .intune_branding_profile_assignment import IntuneBrandingProfileAssignment
        from .invalid_license_alert_configuration import InvalidLicenseAlertConfiguration
        from .invalid_license_alert_incident import InvalidLicenseAlertIncident
        from .invitation import Invitation
        from .invite_participants_operation import InviteParticipantsOperation
        from .invoke_user_flow_listener import InvokeUserFlowListener
        from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
        from .iosi_pad_o_s_web_clip import IosiPadOSWebClip
        from .ios_certificate_profile import IosCertificateProfile
        from .ios_certificate_profile_base import IosCertificateProfileBase
        from .ios_compliance_policy import IosCompliancePolicy
        from .ios_custom_configuration import IosCustomConfiguration
        from .ios_derived_credential_authentication_configuration import IosDerivedCredentialAuthenticationConfiguration
        from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
        from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
        from .ios_education_device_configuration import IosEducationDeviceConfiguration
        from .ios_edu_device_configuration import IosEduDeviceConfiguration
        from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration
        from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration
        from .ios_general_device_configuration import IosGeneralDeviceConfiguration
        from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
        from .ios_lob_app import IosLobApp
        from .ios_lob_app_provisioning_configuration import IosLobAppProvisioningConfiguration
        from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment
        from .ios_lob_app_provisioning_configuration_policy_set_item import IosLobAppProvisioningConfigurationPolicySetItem
        from .ios_managed_app_protection import IosManagedAppProtection
        from .ios_managed_app_registration import IosManagedAppRegistration
        from .ios_mobile_app_configuration import IosMobileAppConfiguration
        from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
        from .ios_scep_certificate_profile import IosScepCertificateProfile
        from .ios_store_app import IosStoreApp
        from .ios_trusted_root_certificate import IosTrustedRootCertificate
        from .ios_update_configuration import IosUpdateConfiguration
        from .ios_update_device_status import IosUpdateDeviceStatus
        from .ios_vpn_configuration import IosVpnConfiguration
        from .ios_vpp_app import IosVppApp
        from .ios_vpp_app_assigned_device_license import IosVppAppAssignedDeviceLicense
        from .ios_vpp_app_assigned_license import IosVppAppAssignedLicense
        from .ios_vpp_app_assigned_user_license import IosVppAppAssignedUserLicense
        from .ios_vpp_e_book import IosVppEBook
        from .ios_vpp_e_book_assignment import IosVppEBookAssignment
        from .ios_wi_fi_configuration import IosWiFiConfiguration
        from .ip_application_segment import IpApplicationSegment
        from .ip_named_location import IpNamedLocation
        from .ip_security_profile import IpSecurityProfile
        from .item_activity import ItemActivity
        from .item_activity_o_l_d import ItemActivityOLD
        from .item_activity_stat import ItemActivityStat
        from .item_address import ItemAddress
        from .item_analytics import ItemAnalytics
        from .item_attachment import ItemAttachment
        from .item_email import ItemEmail
        from .item_facet import ItemFacet
        from .item_insights import ItemInsights
        from .item_patent import ItemPatent
        from .item_phone import ItemPhone
        from .item_publication import ItemPublication
        from .item_retention_label import ItemRetentionLabel
        from .job_response_base import JobResponseBase
        from .landing_page import LandingPage
        from .landing_page_detail import LandingPageDetail
        from .language_proficiency import LanguageProficiency
        from .learning_assignment import LearningAssignment
        from .learning_content import LearningContent
        from .learning_course_activity import LearningCourseActivity
        from .learning_provider import LearningProvider
        from .learning_self_initiated_course import LearningSelfInitiatedCourse
        from .license_details import LicenseDetails
        from .linked_resource import LinkedResource
        from .list_ import List_
        from .list_item import ListItem
        from .list_item_version import ListItemVersion
        from .localized_notification_message import LocalizedNotificationMessage
        from .login_page import LoginPage
        from .long_running_operation import LongRunningOperation
        from .lookup_result_row import LookupResultRow
        from .m365_apps_installation_options import M365AppsInstallationOptions
        from .mac_os_vpp_app import MacOsVppApp
        from .mac_os_vpp_app_assigned_license import MacOsVppAppAssignedLicense
        from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
        from .mac_o_s_compliance_policy import MacOSCompliancePolicy
        from .mac_o_s_custom_app_configuration import MacOSCustomAppConfiguration
        from .mac_o_s_custom_configuration import MacOSCustomConfiguration
        from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
        from .mac_o_s_dmg_app import MacOSDmgApp
        from .mac_o_s_endpoint_protection_configuration import MacOSEndpointProtectionConfiguration
        from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration
        from .mac_o_s_extensions_configuration import MacOSExtensionsConfiguration
        from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
        from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
        from .mac_o_s_lob_app import MacOSLobApp
        from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp
        from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp
        from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
        from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
        from .mac_o_s_pkg_app import MacOSPkgApp
        from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
        from .mac_o_s_software_update_account_summary import MacOSSoftwareUpdateAccountSummary
        from .mac_o_s_software_update_category_summary import MacOSSoftwareUpdateCategorySummary
        from .mac_o_s_software_update_configuration import MacOSSoftwareUpdateConfiguration
        from .mac_o_s_software_update_state_summary import MacOSSoftwareUpdateStateSummary
        from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
        from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
        from .mac_o_s_web_clip import MacOSWebClip
        from .mac_o_s_wired_network_configuration import MacOSWiredNetworkConfiguration
        from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration
        from .mail_assessment_request import MailAssessmentRequest
        from .mail_folder import MailFolder
        from .mail_search_folder import MailSearchFolder
        from .malware_state_for_windows_device import MalwareStateForWindowsDevice
        from .managed_all_device_certificate_state import ManagedAllDeviceCertificateState
        from .managed_android_lob_app import ManagedAndroidLobApp
        from .managed_android_store_app import ManagedAndroidStoreApp
        from .managed_app import ManagedApp
        from .managed_app_configuration import ManagedAppConfiguration
        from .managed_app_log_collection_request import ManagedAppLogCollectionRequest
        from .managed_app_operation import ManagedAppOperation
        from .managed_app_policy import ManagedAppPolicy
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_app_protection import ManagedAppProtection
        from .managed_app_protection_policy_set_item import ManagedAppProtectionPolicySetItem
        from .managed_app_registration import ManagedAppRegistration
        from .managed_app_status import ManagedAppStatus
        from .managed_app_status_raw import ManagedAppStatusRaw
        from .managed_device import ManagedDevice
        from .managed_device_certificate_state import ManagedDeviceCertificateState
        from .managed_device_cleanup_rule import ManagedDeviceCleanupRule
        from .managed_device_encryption_state import ManagedDeviceEncryptionState
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
        from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
        from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
        from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
        from .managed_device_mobile_app_configuration_policy_set_item import ManagedDeviceMobileAppConfigurationPolicySetItem
        from .managed_device_mobile_app_configuration_state import ManagedDeviceMobileAppConfigurationState
        from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
        from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary
        from .managed_device_overview import ManagedDeviceOverview
        from .managed_e_book import ManagedEBook
        from .managed_e_book_assignment import ManagedEBookAssignment
        from .managed_e_book_category import ManagedEBookCategory
        from .managed_i_o_s_lob_app import ManagedIOSLobApp
        from .managed_i_o_s_store_app import ManagedIOSStoreApp
        from .managed_mobile_app import ManagedMobileApp
        from .managed_mobile_lob_app import ManagedMobileLobApp
        from .managed_tenants.aggregated_policy_compliance import AggregatedPolicyCompliance
        from .managed_tenants.app_performance import AppPerformance
        from .managed_tenants.audit_event import AuditEvent
        from .managed_tenants.cloud_pc_connection import CloudPcConnection
        from .managed_tenants.cloud_pc_device import CloudPcDevice
        from .managed_tenants.cloud_pc_overview import CloudPcOverview
        from .managed_tenants.conditional_access_policy_coverage import ConditionalAccessPolicyCoverage
        from .managed_tenants.credential_user_registrations_summary import CredentialUserRegistrationsSummary
        from .managed_tenants.device_app_performance import DeviceAppPerformance
        from .managed_tenants.device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
        from .managed_tenants.device_health_status import DeviceHealthStatus
        from .managed_tenants.managed_device_compliance import ManagedDeviceCompliance
        from .managed_tenants.managed_device_compliance_trend import ManagedDeviceComplianceTrend
        from .managed_tenants.managed_tenant import ManagedTenant
        from .managed_tenants.managed_tenant_alert import ManagedTenantAlert
        from .managed_tenants.managed_tenant_alert_log import ManagedTenantAlertLog
        from .managed_tenants.managed_tenant_alert_rule import ManagedTenantAlertRule
        from .managed_tenants.managed_tenant_alert_rule_definition import ManagedTenantAlertRuleDefinition
        from .managed_tenants.managed_tenant_api_notification import ManagedTenantApiNotification
        from .managed_tenants.managed_tenant_email_notification import ManagedTenantEmailNotification
        from .managed_tenants.managed_tenant_ticketing_endpoint import ManagedTenantTicketingEndpoint
        from .managed_tenants.management_action import ManagementAction
        from .managed_tenants.management_action_tenant_deployment_status import ManagementActionTenantDeploymentStatus
        from .managed_tenants.management_intent import ManagementIntent
        from .managed_tenants.management_template import ManagementTemplate
        from .managed_tenants.management_template_collection import ManagementTemplateCollection
        from .managed_tenants.management_template_collection_tenant_summary import ManagementTemplateCollectionTenantSummary
        from .managed_tenants.management_template_step import ManagementTemplateStep
        from .managed_tenants.management_template_step_deployment import ManagementTemplateStepDeployment
        from .managed_tenants.management_template_step_tenant_summary import ManagementTemplateStepTenantSummary
        from .managed_tenants.management_template_step_version import ManagementTemplateStepVersion
        from .managed_tenants.tenant import Tenant
        from .managed_tenants.tenant_customized_information import TenantCustomizedInformation
        from .managed_tenants.tenant_detailed_information import TenantDetailedInformation
        from .managed_tenants.tenant_group import TenantGroup
        from .managed_tenants.tenant_tag import TenantTag
        from .managed_tenants.windows_device_malware_state import WindowsDeviceMalwareState
        from .managed_tenants.windows_protection_state import WindowsProtectionState
        from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
        from .mdm_windows_information_protection_policy_policy_set_item import MdmWindowsInformationProtectionPolicyPolicySetItem
        from .meeting_activity_statistics import MeetingActivityStatistics
        from .meeting_attendance_report import MeetingAttendanceReport
        from .meeting_registrant import MeetingRegistrant
        from .meeting_registrant_base import MeetingRegistrantBase
        from .meeting_registration import MeetingRegistration
        from .meeting_registration_base import MeetingRegistrationBase
        from .meeting_registration_question import MeetingRegistrationQuestion
        from .membership_outlier_insight import MembershipOutlierInsight
        from .mention import Mention
        from .message import Message
        from .message_event import MessageEvent
        from .message_recipient import MessageRecipient
        from .message_rule import MessageRule
        from .message_trace import MessageTrace
        from .mfa_completion_metric import MfaCompletionMetric
        from .mfa_failure import MfaFailure
        from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
        from .microsoft_application_data_access_settings import MicrosoftApplicationDataAccessSettings
        from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
        from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration
        from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
        from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
        from .microsoft_store_for_business_contained_app import MicrosoftStoreForBusinessContainedApp
        from .microsoft_tunnel_configuration import MicrosoftTunnelConfiguration
        from .microsoft_tunnel_health_threshold import MicrosoftTunnelHealthThreshold
        from .microsoft_tunnel_server import MicrosoftTunnelServer
        from .microsoft_tunnel_server_log_collection_response import MicrosoftTunnelServerLogCollectionResponse
        from .microsoft_tunnel_site import MicrosoftTunnelSite
        from .mobile_app import MobileApp
        from .mobile_app_assignment import MobileAppAssignment
        from .mobile_app_catalog_package import MobileAppCatalogPackage
        from .mobile_app_category import MobileAppCategory
        from .mobile_app_content import MobileAppContent
        from .mobile_app_content_file import MobileAppContentFile
        from .mobile_app_dependency import MobileAppDependency
        from .mobile_app_install_status import MobileAppInstallStatus
        from .mobile_app_install_summary import MobileAppInstallSummary
        from .mobile_app_intent_and_state import MobileAppIntentAndState
        from .mobile_app_policy_set_item import MobileAppPolicySetItem
        from .mobile_app_provisioning_config_group_assignment import MobileAppProvisioningConfigGroupAssignment
        from .mobile_app_relationship import MobileAppRelationship
        from .mobile_app_supersedence import MobileAppSupersedence
        from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
        from .mobile_contained_app import MobileContainedApp
        from .mobile_lob_app import MobileLobApp
        from .mobile_threat_defense_connector import MobileThreatDefenseConnector
        from .mobility_management_policy import MobilityManagementPolicy
        from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric
        from .monthly_inactive_users_metric import MonthlyInactiveUsersMetric
        from .monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot
        from .multi_tenant_organization import MultiTenantOrganization
        from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate
        from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord
        from .multi_tenant_organization_member import MultiTenantOrganizationMember
        from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .mute_participants_operation import MuteParticipantsOperation
        from .mute_participant_operation import MuteParticipantOperation
        from .named_location import NamedLocation
        from .ndes_connector import NdesConnector
        from .networkaccess.alert import Alert
        from .networkaccess.branch_site import BranchSite
        from .networkaccess.conditional_access_policy import ConditionalAccessPolicy
        from .networkaccess.conditional_access_settings import ConditionalAccessSettings
        from .networkaccess.connectivity import Connectivity
        from .networkaccess.connectivity_configuration_link import ConnectivityConfigurationLink
        from .networkaccess.cross_tenant_access_settings import CrossTenantAccessSettings
        from .networkaccess.device_link import DeviceLink
        from .networkaccess.enriched_audit_logs import EnrichedAuditLogs
        from .networkaccess.filtering_policy import FilteringPolicy
        from .networkaccess.filtering_policy_link import FilteringPolicyLink
        from .networkaccess.filtering_profile import FilteringProfile
        from .networkaccess.filtering_rule import FilteringRule
        from .networkaccess.forwarding_options import ForwardingOptions
        from .networkaccess.forwarding_policy import ForwardingPolicy
        from .networkaccess.forwarding_policy_link import ForwardingPolicyLink
        from .networkaccess.forwarding_profile import ForwardingProfile
        from .networkaccess.forwarding_rule import ForwardingRule
        from .networkaccess.fqdn_filtering_rule import FqdnFilteringRule
        from .networkaccess.internet_access_forwarding_rule import InternetAccessForwardingRule
        from .networkaccess.logs import Logs
        from .networkaccess.m365_forwarding_rule import M365ForwardingRule
        from .networkaccess.network_access_root import NetworkAccessRoot
        from .networkaccess.policy import Policy
        from .networkaccess.policy_link import PolicyLink
        from .networkaccess.policy_rule import PolicyRule
        from .networkaccess.private_access_forwarding_rule import PrivateAccessForwardingRule
        from .networkaccess.profile import Profile
        from .networkaccess.remote_network import RemoteNetwork
        from .networkaccess.remote_network_health_event import RemoteNetworkHealthEvent
        from .networkaccess.reports import Reports
        from .networkaccess.settings import Settings
        from .networkaccess.tenant_status import TenantStatus
        from .networkaccess.web_category_filtering_rule import WebCategoryFilteringRule
        from .news_link_page import NewsLinkPage
        from .note import Note
        from .notebook import Notebook
        from .notification import Notification
        from .notification_message_template import NotificationMessageTemplate
        from .no_mfa_on_role_activation_alert_configuration import NoMfaOnRoleActivationAlertConfiguration
        from .no_mfa_on_role_activation_alert_incident import NoMfaOnRoleActivationAlertIncident
        from .offer_shift_request import OfferShiftRequest
        from .office365_active_user_counts import Office365ActiveUserCounts
        from .office365_active_user_detail import Office365ActiveUserDetail
        from .office365_groups_activity_counts import Office365GroupsActivityCounts
        from .office365_groups_activity_detail import Office365GroupsActivityDetail
        from .office365_groups_activity_file_counts import Office365GroupsActivityFileCounts
        from .office365_groups_activity_group_counts import Office365GroupsActivityGroupCounts
        from .office365_groups_activity_storage import Office365GroupsActivityStorage
        from .office365_services_user_counts import Office365ServicesUserCounts
        from .office_graph_insights import OfficeGraphInsights
        from .office_suite_app import OfficeSuiteApp
        from .onenote import Onenote
        from .onenote_entity_base_model import OnenoteEntityBaseModel
        from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
        from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
        from .onenote_operation import OnenoteOperation
        from .onenote_page import OnenotePage
        from .onenote_resource import OnenoteResource
        from .onenote_section import OnenoteSection
        from .online_meeting import OnlineMeeting
        from .online_meeting_base import OnlineMeetingBase
        from .on_attribute_collection_listener import OnAttributeCollectionListener
        from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
        from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener
        from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
        from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener
        from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
        from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
        from .on_premises_agent import OnPremisesAgent
        from .on_premises_agent_group import OnPremisesAgentGroup
        from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
        from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
        from .on_premises_publishing_profile import OnPremisesPublishingProfile
        from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
        from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
        from .on_user_create_start_listener import OnUserCreateStartListener
        from .open_aws_security_group_finding import OpenAwsSecurityGroupFinding
        from .open_id_connect_identity_provider import OpenIdConnectIdentityProvider
        from .open_id_connect_provider import OpenIdConnectProvider
        from .open_network_azure_security_group_finding import OpenNetworkAzureSecurityGroupFinding
        from .open_shift import OpenShift
        from .open_shift_change_request import OpenShiftChangeRequest
        from .open_type_extension import OpenTypeExtension
        from .operation import Operation
        from .operation_approval_policy import OperationApprovalPolicy
        from .operation_approval_request import OperationApprovalRequest
        from .organization import Organization
        from .organizational_branding import OrganizationalBranding
        from .organizational_branding_localization import OrganizationalBrandingLocalization
        from .organizational_branding_properties import OrganizationalBrandingProperties
        from .organization_settings import OrganizationSettings
        from .org_contact import OrgContact
        from .outlook_category import OutlookCategory
        from .outlook_item import OutlookItem
        from .outlook_task import OutlookTask
        from .outlook_task_folder import OutlookTaskFolder
        from .outlook_task_group import OutlookTaskGroup
        from .outlook_user import OutlookUser
        from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding
        from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding
        from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
        from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding
        from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding
        from .overprovisioned_user_finding import OverprovisionedUserFinding
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .participant import Participant
        from .participant_joining_notification import ParticipantJoiningNotification
        from .participant_left_notification import ParticipantLeftNotification
        from .partners.billing.azure_usage import AzureUsage
        from .partners.billing.billed_reconciliation import BilledReconciliation
        from .partners.billing.billed_usage import BilledUsage
        from .partners.billing.billing import Billing
        from .partners.billing.billing_reconciliation import BillingReconciliation
        from .partners.billing.export_success_operation import ExportSuccessOperation
        from .partners.billing.failed_operation import FailedOperation
        from .partners.billing.manifest import Manifest
        from .partners.billing.operation import Operation
        from .partners.billing.running_operation import RunningOperation
        from .partners.billing.unbilled_usage import UnbilledUsage
        from .partners.partners import Partners
        from .passwordless_microsoft_authenticator_authentication_method import PasswordlessMicrosoftAuthenticatorAuthenticationMethod
        from .password_authentication_method import PasswordAuthenticationMethod
        from .payload import Payload
        from .payload_compatible_assignment_filter import PayloadCompatibleAssignmentFilter
        from .payload_response import PayloadResponse
        from .pending_external_user_profile import PendingExternalUserProfile
        from .people_admin_settings import PeopleAdminSettings
        from .permission import Permission
        from .permissions_analytics import PermissionsAnalytics
        from .permissions_analytics_aggregation import PermissionsAnalyticsAggregation
        from .permissions_creep_index_distribution import PermissionsCreepIndexDistribution
        from .permissions_definition_aws_policy import PermissionsDefinitionAwsPolicy
        from .permissions_definition_azure_role import PermissionsDefinitionAzureRole
        from .permissions_definition_gcp_role import PermissionsDefinitionGcpRole
        from .permissions_management import PermissionsManagement
        from .permissions_request_change import PermissionsRequestChange
        from .permission_grant_condition_set import PermissionGrantConditionSet
        from .permission_grant_policy import PermissionGrantPolicy
        from .person import Person
        from .person_annotation import PersonAnnotation
        from .person_annual_event import PersonAnnualEvent
        from .person_award import PersonAward
        from .person_certification import PersonCertification
        from .person_extension import PersonExtension
        from .person_interest import PersonInterest
        from .person_name import PersonName
        from .person_responsibility import PersonResponsibility
        from .person_website import PersonWebsite
        from .phone_authentication_method import PhoneAuthenticationMethod
        from .pinned_chat_message_info import PinnedChatMessageInfo
        from .place import Place
        from .planner import Planner
        from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
        from .planner_bucket import PlannerBucket
        from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
        from .planner_delta import PlannerDelta
        from .planner_group import PlannerGroup
        from .planner_plan import PlannerPlan
        from .planner_plan_configuration import PlannerPlanConfiguration
        from .planner_plan_configuration_localization import PlannerPlanConfigurationLocalization
        from .planner_plan_details import PlannerPlanDetails
        from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
        from .planner_roster import PlannerRoster
        from .planner_roster_member import PlannerRosterMember
        from .planner_task import PlannerTask
        from .planner_task_configuration import PlannerTaskConfiguration
        from .planner_task_details import PlannerTaskDetails
        from .planner_user import PlannerUser
        from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
        from .play_prompt_operation import PlayPromptOperation
        from .policy_base import PolicyBase
        from .policy_root import PolicyRoot
        from .policy_set import PolicySet
        from .policy_set_assignment import PolicySetAssignment
        from .policy_set_item import PolicySetItem
        from .policy_template import PolicyTemplate
        from .post import Post
        from .presence import Presence
        from .presentation import Presentation
        from .printer import Printer
        from .printer_base import PrinterBase
        from .printer_create_operation import PrinterCreateOperation
        from .printer_share import PrinterShare
        from .print_connector import PrintConnector
        from .print_document import PrintDocument
        from .print_job import PrintJob
        from .print_operation import PrintOperation
        from .print_service import PrintService
        from .print_service_endpoint import PrintServiceEndpoint
        from .print_task import PrintTask
        from .print_task_definition import PrintTaskDefinition
        from .print_task_trigger import PrintTaskTrigger
        from .print_usage import PrintUsage
        from .print_usage_by_printer import PrintUsageByPrinter
        from .print_usage_by_user import PrintUsageByUser
        from .privileged_access import PrivilegedAccess
        from .privileged_access_group import PrivilegedAccessGroup
        from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
        from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
        from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
        from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
        from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
        from .privileged_access_root import PrivilegedAccessRoot
        from .privileged_access_schedule import PrivilegedAccessSchedule
        from .privileged_access_schedule_instance import PrivilegedAccessScheduleInstance
        from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest
        from .privileged_approval import PrivilegedApproval
        from .privileged_operation_event import PrivilegedOperationEvent
        from .privileged_role import PrivilegedRole
        from .privileged_role_assignment import PrivilegedRoleAssignment
        from .privileged_role_assignment_request import PrivilegedRoleAssignmentRequest
        from .privileged_role_settings import PrivilegedRoleSettings
        from .privileged_role_summary import PrivilegedRoleSummary
        from .privileged_signup_status import PrivilegedSignupStatus
        from .privilege_escalation import PrivilegeEscalation
        from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
        from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
        from .privilege_escalation_finding import PrivilegeEscalationFinding
        from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
        from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding
        from .privilege_management_elevation import PrivilegeManagementElevation
        from .privilege_management_elevation_request import PrivilegeManagementElevationRequest
        from .profile import Profile
        from .profile_card_property import ProfileCardProperty
        from .profile_photo import ProfilePhoto
        from .program import Program
        from .program_control import ProgramControl
        from .program_control_type import ProgramControlType
        from .project_participation import ProjectParticipation
        from .pronouns_settings import PronounsSettings
        from .provider_tenant_setting import ProviderTenantSetting
        from .provisioning_object_summary import ProvisioningObjectSummary
        from .published_resource import PublishedResource
        from .purchase_invoice_line import PurchaseInvoiceLine
        from .rbac_application import RbacApplication
        from .rbac_application_multiple import RbacApplicationMultiple
        from .recommendation import Recommendation
        from .recommendation_base import RecommendationBase
        from .record_operation import RecordOperation
        from .recycle_bin import RecycleBin
        from .recycle_bin_item import RecycleBinItem
        from .redundant_assignment_alert_configuration import RedundantAssignmentAlertConfiguration
        from .redundant_assignment_alert_incident import RedundantAssignmentAlertIncident
        from .reference_attachment import ReferenceAttachment
        from .regional_and_language_settings import RegionalAndLanguageSettings
        from .relying_party_detailed_summary import RelyingPartyDetailedSummary
        from .remote_action_audit import RemoteActionAudit
        from .remote_assistance_partner import RemoteAssistancePartner
        from .remote_assistance_settings import RemoteAssistanceSettings
        from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
        from .report_root import ReportRoot
        from .request import Request
        from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship
        from .resource_operation import ResourceOperation
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .restricted_apps_violation import RestrictedAppsViolation
        from .rich_long_running_operation import RichLongRunningOperation
        from .risky_service_principal import RiskyServicePrincipal
        from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
        from .risky_user import RiskyUser
        from .risky_user_history_item import RiskyUserHistoryItem
        from .risk_detection import RiskDetection
        from .roles_assigned_outside_privileged_identity_management_alert_configuration import RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration
        from .roles_assigned_outside_privileged_identity_management_alert_incident import RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident
        from .role_assignment import RoleAssignment
        from .role_definition import RoleDefinition
        from .role_management_alert import RoleManagementAlert
        from .role_scope_tag import RoleScopeTag
        from .role_scope_tag_auto_assignment import RoleScopeTagAutoAssignment
        from .room import Room
        from .room_list import RoomList
        from .sales_credit_memo_line import SalesCreditMemoLine
        from .sales_invoice_line import SalesInvoiceLine
        from .sales_order_line import SalesOrderLine
        from .sales_quote_line import SalesQuoteLine
        from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
        from .saml_or_ws_fed_provider import SamlOrWsFedProvider
        from .schedule import Schedule
        from .scheduled_permissions_request import ScheduledPermissionsRequest
        from .schedule_change_request import ScheduleChangeRequest
        from .scheduling_group import SchedulingGroup
        from .schema import Schema
        from .schema_extension import SchemaExtension
        from .scoped_role_membership import ScopedRoleMembership
        from .search.acronym import Acronym
        from .search.bookmark import Bookmark
        from .search.qna import Qna
        from .search.search_answer import SearchAnswer
        from .search_entity import SearchEntity
        from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding
        from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding
        from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding
        from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding
        from .section_group import SectionGroup
        from .secure_score import SecureScore
        from .secure_score_control_profile import SecureScoreControlProfile
        from .security.alert import Alert
        from .security.analyzed_email import AnalyzedEmail
        from .security.article import Article
        from .security.article_indicator import ArticleIndicator
        from .security.artifact import Artifact
        from .security.audit_core_root import AuditCoreRoot
        from .security.audit_log_query import AuditLogQuery
        from .security.audit_log_record import AuditLogRecord
        from .security.authority_template import AuthorityTemplate
        from .security.case import Case
        from .security.cases_root import CasesRoot
        from .security.case_operation import CaseOperation
        from .security.category_template import CategoryTemplate
        from .security.citation_template import CitationTemplate
        from .security.collaboration_root import CollaborationRoot
        from .security.data_set import DataSet
        from .security.data_source import DataSource
        from .security.data_source_container import DataSourceContainer
        from .security.department_template import DepartmentTemplate
        from .security.detection_rule import DetectionRule
        from .security.disposition_review_stage import DispositionReviewStage
        from .security.ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
        from .security.ediscovery_case import EdiscoveryCase
        from .security.ediscovery_case_settings import EdiscoveryCaseSettings
        from .security.ediscovery_custodian import EdiscoveryCustodian
        from .security.ediscovery_estimate_operation import EdiscoveryEstimateOperation
        from .security.ediscovery_export_operation import EdiscoveryExportOperation
        from .security.ediscovery_file import EdiscoveryFile
        from .security.ediscovery_hold_operation import EdiscoveryHoldOperation
        from .security.ediscovery_hold_policy import EdiscoveryHoldPolicy
        from .security.ediscovery_index_operation import EdiscoveryIndexOperation
        from .security.ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
        from .security.ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
        from .security.ediscovery_review_set import EdiscoveryReviewSet
        from .security.ediscovery_review_set_query import EdiscoveryReviewSetQuery
        from .security.ediscovery_review_tag import EdiscoveryReviewTag
        from .security.ediscovery_search import EdiscoverySearch
        from .security.ediscovery_search_export_operation import EdiscoverySearchExportOperation
        from .security.ediscovery_tag_operation import EdiscoveryTagOperation
        from .security.email_content_threat_submission import EmailContentThreatSubmission
        from .security.email_threat_submission import EmailThreatSubmission
        from .security.email_threat_submission_policy import EmailThreatSubmissionPolicy
        from .security.email_url_threat_submission import EmailUrlThreatSubmission
        from .security.file import File
        from .security.file_content_threat_submission import FileContentThreatSubmission
        from .security.file_plan_descriptor import FilePlanDescriptor
        from .security.file_plan_descriptor_template import FilePlanDescriptorTemplate
        from .security.file_plan_reference_template import FilePlanReferenceTemplate
        from .security.file_threat_submission import FileThreatSubmission
        from .security.file_url_threat_submission import FileUrlThreatSubmission
        from .security.health_issue import HealthIssue
        from .security.host import Host
        from .security.hostname import Hostname
        from .security.host_component import HostComponent
        from .security.host_cookie import HostCookie
        from .security.host_pair import HostPair
        from .security.host_port import HostPort
        from .security.host_reputation import HostReputation
        from .security.host_ssl_certificate import HostSslCertificate
        from .security.host_tracker import HostTracker
        from .security.identity_container import IdentityContainer
        from .security.incident import Incident
        from .security.indicator import Indicator
        from .security.information_protection import InformationProtection
        from .security.information_protection_policy_setting import InformationProtectionPolicySetting
        from .security.intelligence_profile import IntelligenceProfile
        from .security.intelligence_profile_indicator import IntelligenceProfileIndicator
        from .security.ip_address import IpAddress
        from .security.labels_root import LabelsRoot
        from .security.passive_dns_record import PassiveDnsRecord
        from .security.policy_base import PolicyBase
        from .security.protection_rule import ProtectionRule
        from .security.retention_event import RetentionEvent
        from .security.retention_event_type import RetentionEventType
        from .security.retention_label import RetentionLabel
        from .security.rules_root import RulesRoot
        from .security.search import Search
        from .security.security import Security
        from .security.sensitivity_label import SensitivityLabel
        from .security.site_source import SiteSource
        from .security.ssl_certificate import SslCertificate
        from .security.subcategory_template import SubcategoryTemplate
        from .security.subdomain import Subdomain
        from .security.tag import Tag
        from .security.threat_intelligence import ThreatIntelligence
        from .security.threat_submission import ThreatSubmission
        from .security.threat_submission_root import ThreatSubmissionRoot
        from .security.triggers_root import TriggersRoot
        from .security.trigger_types_root import TriggerTypesRoot
        from .security.unclassified_artifact import UnclassifiedArtifact
        from .security.unified_group_source import UnifiedGroupSource
        from .security.url_threat_submission import UrlThreatSubmission
        from .security.user_source import UserSource
        from .security.vulnerability import Vulnerability
        from .security.vulnerability_component import VulnerabilityComponent
        from .security.whois_base_record import WhoisBaseRecord
        from .security.whois_history_record import WhoisHistoryRecord
        from .security.whois_record import WhoisRecord
        from .security_action import SecurityAction
        from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary
        from .security_baseline_device_state import SecurityBaselineDeviceState
        from .security_baseline_setting_state import SecurityBaselineSettingState
        from .security_baseline_state import SecurityBaselineState
        from .security_baseline_state_summary import SecurityBaselineStateSummary
        from .security_baseline_template import SecurityBaselineTemplate
        from .security_configuration_task import SecurityConfigurationTask
        from .security_reports_root import SecurityReportsRoot
        from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
        from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
        from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
        from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding
        from .send_dtmf_tones_operation import SendDtmfTonesOperation
        from .sensitive_type import SensitiveType
        from .sensitivity_label import SensitivityLabel
        from .sensitivity_policy_settings import SensitivityPolicySettings
        from .sequential_activation_renewals_alert_configuration import SequentialActivationRenewalsAlertConfiguration
        from .sequential_activation_renewals_alert_incident import SequentialActivationRenewalsAlertIncident
        from .service_activity import ServiceActivity
        from .service_announcement import ServiceAnnouncement
        from .service_announcement_attachment import ServiceAnnouncementAttachment
        from .service_announcement_base import ServiceAnnouncementBase
        from .service_health import ServiceHealth
        from .service_health_issue import ServiceHealthIssue
        from .service_level_agreement_root import ServiceLevelAgreementRoot
        from .service_now_connection import ServiceNowConnection
        from .service_principal import ServicePrincipal
        from .service_principal_creation_condition_set import ServicePrincipalCreationConditionSet
        from .service_principal_creation_policy import ServicePrincipalCreationPolicy
        from .service_principal_risk_detection import ServicePrincipalRiskDetection
        from .service_principal_sign_in_activity import ServicePrincipalSignInActivity
        from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown
        from .service_update_message import ServiceUpdateMessage
        from .setting_state_device_summary import SettingStateDeviceSummary
        from .shared_drive_item import SharedDriveItem
        from .shared_email_domain import SharedEmailDomain
        from .shared_email_domain_invitation import SharedEmailDomainInvitation
        from .shared_insight import SharedInsight
        from .shared_p_c_configuration import SharedPCConfiguration
        from .shared_with_channel_team_info import SharedWithChannelTeamInfo
        from .sharepoint import Sharepoint
        from .sharepoint_settings import SharepointSettings
        from .shift import Shift
        from .shifts_role_definition import ShiftsRoleDefinition
        from .shift_preferences import ShiftPreferences
        from .sign_in import SignIn
        from .simulation import Simulation
        from .simulation_automation import SimulationAutomation
        from .simulation_automation_run import SimulationAutomationRun
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
        from .site import Site
        from .site_page import SitePage
        from .skill_proficiency import SkillProficiency
        from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
        from .skype_user_conversation_member import SkypeUserConversationMember
        from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration
        from .sms_authentication_method_target import SmsAuthenticationMethodTarget
        from .social_identity_provider import SocialIdentityProvider
        from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
        from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration
        from .software_update_status_summary import SoftwareUpdateStatusSummary
        from .stale_sign_in_alert_configuration import StaleSignInAlertConfiguration
        from .stale_sign_in_alert_incident import StaleSignInAlertIncident
        from .standard_web_part import StandardWebPart
        from .start_hold_music_operation import StartHoldMusicOperation
        from .stop_hold_music_operation import StopHoldMusicOperation
        from .storage_quota_breakdown import StorageQuotaBreakdown
        from .storage_settings import StorageSettings
        from .strong_authentication_detail import StrongAuthenticationDetail
        from .strong_authentication_phone_app_detail import StrongAuthenticationPhoneAppDetail
        from .sts_policy import StsPolicy
        from .subject_rights_request import SubjectRightsRequest
        from .subscribed_sku import SubscribedSku
        from .subscribe_to_tone_operation import SubscribeToToneOperation
        from .subscription import Subscription
        from .super_aws_resource_finding import SuperAwsResourceFinding
        from .super_aws_role_finding import SuperAwsRoleFinding
        from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding
        from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding
        from .super_serverless_function_finding import SuperServerlessFunctionFinding
        from .super_user_finding import SuperUserFinding
        from .swap_shifts_change_request import SwapShiftsChangeRequest
        from .symantec_code_signing_certificate import SymantecCodeSigningCertificate
        from .synchronization import Synchronization
        from .synchronization_job import SynchronizationJob
        from .synchronization_schema import SynchronizationSchema
        from .synchronization_template import SynchronizationTemplate
        from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
        from .targeted_managed_app_configuration_policy_set_item import TargetedManagedAppConfigurationPolicySetItem
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
        from .targeted_managed_app_protection import TargetedManagedAppProtection
        from .target_device_group import TargetDeviceGroup
        from .task_file_attachment import TaskFileAttachment
        from .tax_group import TaxGroup
        from .team import Team
        from .teams_app import TeamsApp
        from .teams_app_dashboard_card_definition import TeamsAppDashboardCardDefinition
        from .teams_app_definition import TeamsAppDefinition
        from .teams_app_icon import TeamsAppIcon
        from .teams_app_installation import TeamsAppInstallation
        from .teams_app_settings import TeamsAppSettings
        from .teams_async_operation import TeamsAsyncOperation
        from .teams_tab import TeamsTab
        from .teams_template import TeamsTemplate
        from .teams_user_configuration.teams_admin_root import TeamsAdminRoot
        from .teams_user_configuration.user_configuration import UserConfiguration
        from .teamwork import Teamwork
        from .teamwork_bot import TeamworkBot
        from .teamwork_device import TeamworkDevice
        from .teamwork_device_activity import TeamworkDeviceActivity
        from .teamwork_device_configuration import TeamworkDeviceConfiguration
        from .teamwork_device_health import TeamworkDeviceHealth
        from .teamwork_device_operation import TeamworkDeviceOperation
        from .teamwork_hosted_content import TeamworkHostedContent
        from .teamwork_peripheral import TeamworkPeripheral
        from .teamwork_tag import TeamworkTag
        from .teamwork_tag_member import TeamworkTagMember
        from .team_info import TeamInfo
        from .team_template import TeamTemplate
        from .team_template_definition import TeamTemplateDefinition
        from .telecom_expense_management_partner import TelecomExpenseManagementPartner
        from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
        from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .tenant_attach_r_b_a_c import TenantAttachRBAC
        from .tenant_relationship_access_policy_base import TenantRelationshipAccessPolicyBase
        from .tenant_setup_info import TenantSetupInfo
        from .terms_and_conditions import TermsAndConditions
        from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
        from .terms_and_conditions_assignment import TermsAndConditionsAssignment
        from .terms_and_conditions_group_assignment import TermsAndConditionsGroupAssignment
        from .terms_of_use_container import TermsOfUseContainer
        from .term_store.group import Group
        from .term_store.relation import Relation
        from .term_store.set import Set
        from .term_store.store import Store
        from .term_store.term import Term
        from .text_classification_request import TextClassificationRequest
        from .text_web_part import TextWebPart
        from .threat_assessment_request import ThreatAssessmentRequest
        from .threat_assessment_result import ThreatAssessmentResult
        from .thumbnail_set import ThumbnailSet
        from .time_card import TimeCard
        from .time_off import TimeOff
        from .time_off_reason import TimeOffReason
        from .time_off_request import TimeOffRequest
        from .ti_indicator import TiIndicator
        from .todo import Todo
        from .todo_task import TodoTask
        from .todo_task_list import TodoTaskList
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .too_many_global_admins_assigned_to_tenant_alert_configuration import TooManyGlobalAdminsAssignedToTenantAlertConfiguration
        from .too_many_global_admins_assigned_to_tenant_alert_incident import TooManyGlobalAdminsAssignedToTenantAlertIncident
        from .training import Training
        from .training_campaign import TrainingCampaign
        from .training_language_detail import TrainingLanguageDetail
        from .trending import Trending
        from .trusted_certificate_authority_as_entity_base import TrustedCertificateAuthorityAsEntityBase
        from .trust_framework_key_set import TrustFrameworkKeySet
        from .trust_framework_policy import TrustFrameworkPolicy
        from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding
        from .unified_rbac_application import UnifiedRbacApplication
        from .unified_rbac_resource_action import UnifiedRbacResourceAction
        from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
        from .unified_rbac_resource_scope import UnifiedRbacResourceScope
        from .unified_role_assignment import UnifiedRoleAssignment
        from .unified_role_assignment_multiple import UnifiedRoleAssignmentMultiple
        from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
        from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
        from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
        from .unified_role_definition import UnifiedRoleDefinition
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
        from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
        from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
        from .unified_role_management_alert import UnifiedRoleManagementAlert
        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration
        from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition
        from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident
        from .unified_role_management_policy import UnifiedRoleManagementPolicy
        from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
        from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment
        from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
        from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
        from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
        from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule
        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule
        from .unified_role_schedule_base import UnifiedRoleScheduleBase
        from .unified_role_schedule_instance_base import UnifiedRoleScheduleInstanceBase
        from .unified_storage_quota import UnifiedStorageQuota
        from .unmanaged_device_discovery_task import UnmanagedDeviceDiscoveryTask
        from .unmute_participant_operation import UnmuteParticipantOperation
        from .unsupported_device_configuration import UnsupportedDeviceConfiguration
        from .unsupported_group_policy_extension import UnsupportedGroupPolicyExtension
        from .update_recording_status_operation import UpdateRecordingStatusOperation
        from .url_assessment_request import UrlAssessmentRequest
        from .usage_right import UsageRight
        from .used_insight import UsedInsight
        from .user import User
        from .user_account_information import UserAccountInformation
        from .user_activity import UserActivity
        from .user_analytics import UserAnalytics
        from .user_app_install_status import UserAppInstallStatus
        from .user_consent_request import UserConsentRequest
        from .user_count_metric import UserCountMetric
        from .user_credential_usage_details import UserCredentialUsageDetails
        from .user_experience_analytics_anomaly import UserExperienceAnalyticsAnomaly
        from .user_experience_analytics_anomaly_correlation_group_overview import UserExperienceAnalyticsAnomalyCorrelationGroupOverview
        from .user_experience_analytics_anomaly_device import UserExperienceAnalyticsAnomalyDevice
        from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance
        from .user_experience_analytics_app_health_app_performance_by_app_version import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion
        from .user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
        from .user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
        from .user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
        from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance
        from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance
        from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails
        from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance
        from .user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
        from .user_experience_analytics_battery_health_app_impact import UserExperienceAnalyticsBatteryHealthAppImpact
        from .user_experience_analytics_battery_health_capacity_details import UserExperienceAnalyticsBatteryHealthCapacityDetails
        from .user_experience_analytics_battery_health_device_app_impact import UserExperienceAnalyticsBatteryHealthDeviceAppImpact
        from .user_experience_analytics_battery_health_device_performance import UserExperienceAnalyticsBatteryHealthDevicePerformance
        from .user_experience_analytics_battery_health_device_runtime_history import UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory
        from .user_experience_analytics_battery_health_model_performance import UserExperienceAnalyticsBatteryHealthModelPerformance
        from .user_experience_analytics_battery_health_os_performance import UserExperienceAnalyticsBatteryHealthOsPerformance
        from .user_experience_analytics_battery_health_runtime_details import UserExperienceAnalyticsBatteryHealthRuntimeDetails
        from .user_experience_analytics_category import UserExperienceAnalyticsCategory
        from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance
        from .user_experience_analytics_device_scope import UserExperienceAnalyticsDeviceScope
        from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores
        from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory
        from .user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess
        from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance
        from .user_experience_analytics_device_timeline_event import UserExperienceAnalyticsDeviceTimelineEvent
        from .user_experience_analytics_device_without_cloud_identity import UserExperienceAnalyticsDeviceWithoutCloudIdentity
        from .user_experience_analytics_impacting_process import UserExperienceAnalyticsImpactingProcess
        from .user_experience_analytics_metric import UserExperienceAnalyticsMetric
        from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
        from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
        from .user_experience_analytics_not_autopilot_ready_device import UserExperienceAnalyticsNotAutopilotReadyDevice
        from .user_experience_analytics_overview import UserExperienceAnalyticsOverview
        from .user_experience_analytics_remote_connection import UserExperienceAnalyticsRemoteConnection
        from .user_experience_analytics_resource_performance import UserExperienceAnalyticsResourcePerformance
        from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
        from .user_experience_analytics_work_from_anywhere_device import UserExperienceAnalyticsWorkFromAnywhereDevice
        from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
        from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
        from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
        from .user_flow_language_configuration import UserFlowLanguageConfiguration
        from .user_flow_language_page import UserFlowLanguagePage
        from .user_insights_root import UserInsightsRoot
        from .user_insights_settings import UserInsightsSettings
        from .user_install_state_summary import UserInstallStateSummary
        from .user_p_f_x_certificate import UserPFXCertificate
        from .user_registration_details import UserRegistrationDetails
        from .user_requests_metric import UserRequestsMetric
        from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation
        from .user_security_profile import UserSecurityProfile
        from .user_settings import UserSettings
        from .user_sign_in_insight import UserSignInInsight
        from .user_sign_up_metric import UserSignUpMetric
        from .user_storage import UserStorage
        from .user_teamwork import UserTeamwork
        from .user_virtual_events_root import UserVirtualEventsRoot
        from .vertical_section import VerticalSection
        from .video_news_link_page import VideoNewsLinkPage
        from .virtual_endpoint import VirtualEndpoint
        from .virtual_event import VirtualEvent
        from .virtual_events_root import VirtualEventsRoot
        from .virtual_event_presenter import VirtualEventPresenter
        from .virtual_event_registration import VirtualEventRegistration
        from .virtual_event_registration_configuration import VirtualEventRegistrationConfiguration
        from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion
        from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion
        from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase
        from .virtual_event_session import VirtualEventSession
        from .virtual_event_townhall import VirtualEventTownhall
        from .virtual_event_webinar import VirtualEventWebinar
        from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration
        from .virtual_machine_details import VirtualMachineDetails
        from .virtual_machine_with_aws_storage_bucket_access_finding import VirtualMachineWithAwsStorageBucketAccessFinding
        from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration
        from .voice_authentication_method_target import VoiceAuthenticationMethodTarget
        from .vpn_configuration import VpnConfiguration
        from .vpp_token import VppToken
        from .vulnerable_managed_device import VulnerableManagedDevice
        from .web_account import WebAccount
        from .web_app import WebApp
        from .web_application_segment import WebApplicationSegment
        from .web_part import WebPart
        from .win32_catalog_app import Win32CatalogApp
        from .win32_lob_app import Win32LobApp
        from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage
        from .windows10_certificate_profile_base import Windows10CertificateProfileBase
        from .windows10_compliance_policy import Windows10CompliancePolicy
        from .windows10_custom_configuration import Windows10CustomConfiguration
        from .windows10_device_firmware_configuration_interface import Windows10DeviceFirmwareConfigurationInterface
        from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
        from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
        from .windows10_enrollment_completion_page_configuration import Windows10EnrollmentCompletionPageConfiguration
        from .windows10_enrollment_completion_page_configuration_policy_set_item import Windows10EnrollmentCompletionPageConfigurationPolicySetItem
        from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
        from .windows10_general_configuration import Windows10GeneralConfiguration
        from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
        from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
        from .windows10_network_boundary_configuration import Windows10NetworkBoundaryConfiguration
        from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
        from .windows10_p_f_x_import_certificate_profile import Windows10PFXImportCertificateProfile
        from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
        from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
        from .windows10_vpn_configuration import Windows10VpnConfiguration
        from .windows10_x_certificate_profile import Windows10XCertificateProfile
        from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile
        from .windows10_x_trusted_root_certificate import Windows10XTrustedRootCertificate
        from .windows10_x_vpn_configuration import Windows10XVpnConfiguration
        from .windows10_x_wifi_configuration import Windows10XWifiConfiguration
        from .windows81_certificate_profile_base import Windows81CertificateProfileBase
        from .windows81_compliance_policy import Windows81CompliancePolicy
        from .windows81_general_configuration import Windows81GeneralConfiguration
        from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
        from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
        from .windows81_vpn_configuration import Windows81VpnConfiguration
        from .windows81_wifi_import_configuration import Windows81WifiImportConfiguration
        from .windows_app_x import WindowsAppX
        from .windows_assigned_access_profile import WindowsAssignedAccessProfile
        from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
        from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment
        from .windows_autopilot_deployment_profile_policy_set_item import WindowsAutopilotDeploymentProfilePolicySetItem
        from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
        from .windows_autopilot_settings import WindowsAutopilotSettings
        from .windows_certificate_profile_base import WindowsCertificateProfileBase
        from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
        from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy
        from .windows_defender_application_control_supplemental_policy_assignment import WindowsDefenderApplicationControlSupplementalPolicyAssignment
        from .windows_defender_application_control_supplemental_policy_deployment_status import WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus
        from .windows_defender_application_control_supplemental_policy_deployment_summary import WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary
        from .windows_delivery_optimization_configuration import WindowsDeliveryOptimizationConfiguration
        from .windows_device_malware_state import WindowsDeviceMalwareState
        from .windows_domain_join_configuration import WindowsDomainJoinConfiguration
        from .windows_driver_update_inventory import WindowsDriverUpdateInventory
        from .windows_driver_update_profile import WindowsDriverUpdateProfile
        from .windows_driver_update_profile_assignment import WindowsDriverUpdateProfileAssignment
        from .windows_feature_update_catalog_item import WindowsFeatureUpdateCatalogItem
        from .windows_feature_update_profile import WindowsFeatureUpdateProfile
        from .windows_feature_update_profile_assignment import WindowsFeatureUpdateProfileAssignment
        from .windows_health_monitoring_configuration import WindowsHealthMonitoringConfiguration
        from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod
        from .windows_identity_protection_configuration import WindowsIdentityProtectionConfiguration
        from .windows_information_protection import WindowsInformationProtection
        from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
        from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
        from .windows_information_protection_device_registration import WindowsInformationProtectionDeviceRegistration
        from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
        from .windows_information_protection_policy import WindowsInformationProtectionPolicy
        from .windows_information_protection_wipe_action import WindowsInformationProtectionWipeAction
        from .windows_kiosk_configuration import WindowsKioskConfiguration
        from .windows_malware_information import WindowsMalwareInformation
        from .windows_managed_app_protection import WindowsManagedAppProtection
        from .windows_managed_app_registration import WindowsManagedAppRegistration
        from .windows_managed_device import WindowsManagedDevice
        from .windows_management_app import WindowsManagementApp
        from .windows_management_app_health_state import WindowsManagementAppHealthState
        from .windows_management_app_health_summary import WindowsManagementAppHealthSummary
        from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
        from .windows_mobile_m_s_i import WindowsMobileMSI
        from .windows_phone81_app_x import WindowsPhone81AppX
        from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle
        from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase
        from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy
        from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
        from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
        from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
        from .windows_phone81_store_app import WindowsPhone81StoreApp
        from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile
        from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate
        from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration
        from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration
        from .windows_phone_x_a_p import WindowsPhoneXAP
        from .windows_privacy_data_access_control_item import WindowsPrivacyDataAccessControlItem
        from .windows_protection_state import WindowsProtectionState
        from .windows_quality_update_catalog_item import WindowsQualityUpdateCatalogItem
        from .windows_quality_update_profile import WindowsQualityUpdateProfile
        from .windows_quality_update_profile_assignment import WindowsQualityUpdateProfileAssignment
        from .windows_setting import WindowsSetting
        from .windows_setting_instance import WindowsSettingInstance
        from .windows_store_app import WindowsStoreApp
        from .windows_universal_app_x import WindowsUniversalAppX
        from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp
        from .windows_updates.azure_a_d_device import AzureADDevice
        from .windows_updates.catalog import Catalog
        from .windows_updates.catalog_entry import CatalogEntry
        from .windows_updates.compliance_change import ComplianceChange
        from .windows_updates.content_approval import ContentApproval
        from .windows_updates.deployment import Deployment
        from .windows_updates.deployment_audience import DeploymentAudience
        from .windows_updates.driver_update_catalog_entry import DriverUpdateCatalogEntry
        from .windows_updates.edition import Edition
        from .windows_updates.feature_update_catalog_entry import FeatureUpdateCatalogEntry
        from .windows_updates.knowledge_base_article import KnowledgeBaseArticle
        from .windows_updates.known_issue import KnownIssue
        from .windows_updates.operational_insights_connection import OperationalInsightsConnection
        from .windows_updates.product import Product
        from .windows_updates.product_revision import ProductRevision
        from .windows_updates.quality_update_catalog_entry import QualityUpdateCatalogEntry
        from .windows_updates.resource_connection import ResourceConnection
        from .windows_updates.software_update_catalog_entry import SoftwareUpdateCatalogEntry
        from .windows_updates.updatable_asset import UpdatableAsset
        from .windows_updates.updatable_asset_group import UpdatableAssetGroup
        from .windows_updates.update_policy import UpdatePolicy
        from .windows_update_catalog_item import WindowsUpdateCatalogItem
        from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
        from .windows_update_state import WindowsUpdateState
        from .windows_vpn_configuration import WindowsVpnConfiguration
        from .windows_web_app import WindowsWebApp
        from .windows_wifi_configuration import WindowsWifiConfiguration
        from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
        from .windows_wired_network_configuration import WindowsWiredNetworkConfiguration
        from .win_get_app import WinGetApp
        from .workbook import Workbook
        from .workbook_application import WorkbookApplication
        from .workbook_chart import WorkbookChart
        from .workbook_chart_area_format import WorkbookChartAreaFormat
        from .workbook_chart_axes import WorkbookChartAxes
        from .workbook_chart_axis import WorkbookChartAxis
        from .workbook_chart_axis_format import WorkbookChartAxisFormat
        from .workbook_chart_axis_title import WorkbookChartAxisTitle
        from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat
        from .workbook_chart_data_labels import WorkbookChartDataLabels
        from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat
        from .workbook_chart_fill import WorkbookChartFill
        from .workbook_chart_font import WorkbookChartFont
        from .workbook_chart_gridlines import WorkbookChartGridlines
        from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat
        from .workbook_chart_legend import WorkbookChartLegend
        from .workbook_chart_legend_format import WorkbookChartLegendFormat
        from .workbook_chart_line_format import WorkbookChartLineFormat
        from .workbook_chart_point import WorkbookChartPoint
        from .workbook_chart_point_format import WorkbookChartPointFormat
        from .workbook_chart_series import WorkbookChartSeries
        from .workbook_chart_series_format import WorkbookChartSeriesFormat
        from .workbook_chart_title import WorkbookChartTitle
        from .workbook_chart_title_format import WorkbookChartTitleFormat
        from .workbook_comment import WorkbookComment
        from .workbook_comment_reply import WorkbookCommentReply
        from .workbook_document_task import WorkbookDocumentTask
        from .workbook_document_task_change import WorkbookDocumentTaskChange
        from .workbook_filter import WorkbookFilter
        from .workbook_format_protection import WorkbookFormatProtection
        from .workbook_functions import WorkbookFunctions
        from .workbook_function_result import WorkbookFunctionResult
        from .workbook_named_item import WorkbookNamedItem
        from .workbook_operation import WorkbookOperation
        from .workbook_pivot_table import WorkbookPivotTable
        from .workbook_range import WorkbookRange
        from .workbook_range_border import WorkbookRangeBorder
        from .workbook_range_fill import WorkbookRangeFill
        from .workbook_range_font import WorkbookRangeFont
        from .workbook_range_format import WorkbookRangeFormat
        from .workbook_range_sort import WorkbookRangeSort
        from .workbook_range_view import WorkbookRangeView
        from .workbook_table import WorkbookTable
        from .workbook_table_column import WorkbookTableColumn
        from .workbook_table_row import WorkbookTableRow
        from .workbook_table_sort import WorkbookTableSort
        from .workbook_worksheet import WorkbookWorksheet
        from .workbook_worksheet_protection import WorkbookWorksheetProtection
        from .workforce_integration import WorkforceIntegration
        from .workplace_sensor_device import WorkplaceSensorDevice
        from .workspace import Workspace
        from .work_position import WorkPosition
        from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration
        from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration
        from .zebra_fota_artifact import ZebraFotaArtifact
        from .zebra_fota_connector import ZebraFotaConnector
        from .zebra_fota_deployment import ZebraFotaDeployment

        from .aad_user_conversation_member import AadUserConversationMember
        from .access_package import AccessPackage
        from .access_package_assignment import AccessPackageAssignment
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
        from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
        from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_request import AccessPackageResourceRequest
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_role_scope import AccessPackageResourceRoleScope
        from .access_package_resource_scope import AccessPackageResourceScope
        from .access_package_subject import AccessPackageSubject
        from .access_review import AccessReview
        from .access_review_decision import AccessReviewDecision
        from .access_review_history_definition import AccessReviewHistoryDefinition
        from .access_review_history_instance import AccessReviewHistoryInstance
        from .access_review_instance import AccessReviewInstance
        from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
        from .access_review_policy import AccessReviewPolicy
        from .access_review_reviewer import AccessReviewReviewer
        from .access_review_schedule_definition import AccessReviewScheduleDefinition
        from .access_review_set import AccessReviewSet
        from .access_review_stage import AccessReviewStage
        from .active_directory_windows_autopilot_deployment_profile import ActiveDirectoryWindowsAutopilotDeploymentProfile
        from .active_users_breakdown_metric import ActiveUsersBreakdownMetric
        from .active_users_metric import ActiveUsersMetric
        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .activity_history_item import ActivityHistoryItem
        from .activity_statistics import ActivityStatistics
        from .add_large_gallery_view_operation import AddLargeGalleryViewOperation
        from .administrative_unit import AdministrativeUnit
        from .admin_apps_and_services import AdminAppsAndServices
        from .admin_consent_request_policy import AdminConsentRequestPolicy
        from .admin_dynamics import AdminDynamics
        from .admin_forms import AdminForms
        from .admin_microsoft365_apps import AdminMicrosoft365Apps
        from .admin_report_settings import AdminReportSettings
        from .admin_todo import AdminTodo
        from .admin_windows import AdminWindows
        from .admin_windows_updates import AdminWindowsUpdates
        from .advanced_threat_protection_onboarding_device_setting_state import AdvancedThreatProtectionOnboardingDeviceSettingState
        from .advanced_threat_protection_onboarding_state_summary import AdvancedThreatProtectionOnboardingStateSummary
        from .agreement import Agreement
        from .agreement_acceptance import AgreementAcceptance
        from .agreement_file import AgreementFile
        from .agreement_file_localization import AgreementFileLocalization
        from .agreement_file_properties import AgreementFileProperties
        from .agreement_file_version import AgreementFileVersion
        from .alert import Alert
        from .allowed_data_location import AllowedDataLocation
        from .allowed_value import AllowedValue
        from .android_certificate_profile_base import AndroidCertificateProfileBase
        from .android_compliance_policy import AndroidCompliancePolicy
        from .android_custom_configuration import AndroidCustomConfiguration
        from .android_device_compliance_local_action_base import AndroidDeviceComplianceLocalActionBase
        from .android_device_compliance_local_action_lock_device import AndroidDeviceComplianceLocalActionLockDevice
        from .android_device_compliance_local_action_lock_device_with_passcode import AndroidDeviceComplianceLocalActionLockDeviceWithPasscode
        from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
        from .android_device_owner_compliance_policy import AndroidDeviceOwnerCompliancePolicy
        from .android_device_owner_derived_credential_authentication_configuration import AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration
        from .android_device_owner_enrollment_profile import AndroidDeviceOwnerEnrollmentProfile
        from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration
        from .android_device_owner_general_device_configuration import AndroidDeviceOwnerGeneralDeviceConfiguration
        from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile
        from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile
        from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile
        from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate
        from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration
        from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration
        from .android_eas_email_profile_configuration import AndroidEasEmailProfileConfiguration
        from .android_enterprise_wi_fi_configuration import AndroidEnterpriseWiFiConfiguration
        from .android_for_work_app import AndroidForWorkApp
        from .android_for_work_app_configuration_schema import AndroidForWorkAppConfigurationSchema
        from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
        from .android_for_work_compliance_policy import AndroidForWorkCompliancePolicy
        from .android_for_work_custom_configuration import AndroidForWorkCustomConfiguration
        from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase
        from .android_for_work_enrollment_profile import AndroidForWorkEnrollmentProfile
        from .android_for_work_enterprise_wi_fi_configuration import AndroidForWorkEnterpriseWiFiConfiguration
        from .android_for_work_general_device_configuration import AndroidForWorkGeneralDeviceConfiguration
        from .android_for_work_gmail_eas_configuration import AndroidForWorkGmailEasConfiguration
        from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile
        from .android_for_work_mobile_app_configuration import AndroidForWorkMobileAppConfiguration
        from .android_for_work_nine_work_eas_configuration import AndroidForWorkNineWorkEasConfiguration
        from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
        from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile
        from .android_for_work_settings import AndroidForWorkSettings
        from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
        from .android_for_work_vpn_configuration import AndroidForWorkVpnConfiguration
        from .android_for_work_wi_fi_configuration import AndroidForWorkWiFiConfiguration
        from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
        from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile
        from .android_lob_app import AndroidLobApp
        from .android_managed_app_protection import AndroidManagedAppProtection
        from .android_managed_app_registration import AndroidManagedAppRegistration
        from .android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings
        from .android_managed_store_app import AndroidManagedStoreApp
        from .android_managed_store_app_configuration import AndroidManagedStoreAppConfiguration
        from .android_managed_store_app_configuration_schema import AndroidManagedStoreAppConfigurationSchema
        from .android_managed_store_web_app import AndroidManagedStoreWebApp
        from .android_oma_cp_configuration import AndroidOmaCpConfiguration
        from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile
        from .android_scep_certificate_profile import AndroidScepCertificateProfile
        from .android_store_app import AndroidStoreApp
        from .android_trusted_root_certificate import AndroidTrustedRootCertificate
        from .android_vpn_configuration import AndroidVpnConfiguration
        from .android_wi_fi_configuration import AndroidWiFiConfiguration
        from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
        from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
        from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
        from .android_work_profile_eas_email_profile_base import AndroidWorkProfileEasEmailProfileBase
        from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration
        from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
        from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
        from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
        from .android_work_profile_pkcs_certificate_profile import AndroidWorkProfilePkcsCertificateProfile
        from .android_work_profile_scep_certificate_profile import AndroidWorkProfileScepCertificateProfile
        from .android_work_profile_trusted_root_certificate import AndroidWorkProfileTrustedRootCertificate
        from .android_work_profile_vpn_configuration import AndroidWorkProfileVpnConfiguration
        from .android_work_profile_wi_fi_configuration import AndroidWorkProfileWiFiConfiguration
        from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
        from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase
        from .aosp_device_owner_compliance_policy import AospDeviceOwnerCompliancePolicy
        from .aosp_device_owner_device_configuration import AospDeviceOwnerDeviceConfiguration
        from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration
        from .aosp_device_owner_pkcs_certificate_profile import AospDeviceOwnerPkcsCertificateProfile
        from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile
        from .aosp_device_owner_trusted_root_certificate import AospDeviceOwnerTrustedRootCertificate
        from .aosp_device_owner_wi_fi_configuration import AospDeviceOwnerWiFiConfiguration
        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .apple_enrollment_profile_assignment import AppleEnrollmentProfileAssignment
        from .apple_expedited_checkin_configuration_base import AppleExpeditedCheckinConfigurationBase
        from .apple_managed_identity_provider import AppleManagedIdentityProvider
        from .apple_push_notification_certificate import ApplePushNotificationCertificate
        from .apple_user_initiated_enrollment_profile import AppleUserInitiatedEnrollmentProfile
        from .apple_vpn_configuration import AppleVpnConfiguration
        from .apple_vpp_token_troubleshooting_event import AppleVppTokenTroubleshootingEvent
        from .application import Application
        from .application_segment import ApplicationSegment
        from .application_sign_in_detailed_summary import ApplicationSignInDetailedSummary
        from .application_sign_in_summary import ApplicationSignInSummary
        from .application_template import ApplicationTemplate
        from .approval import Approval
        from .approval_step import ApprovalStep
        from .approval_workflow_provider import ApprovalWorkflowProvider
        from .app_consent_approval_route import AppConsentApprovalRoute
        from .app_consent_request import AppConsentRequest
        from .app_credential_sign_in_activity import AppCredentialSignInActivity
        from .app_log_collection_request import AppLogCollectionRequest
        from .app_management_policy import AppManagementPolicy
        from .app_role_assignment import AppRoleAssignment
        from .app_scope import AppScope
        from .app_vulnerability_managed_device import AppVulnerabilityManagedDevice
        from .app_vulnerability_mobile_app import AppVulnerabilityMobileApp
        from .app_vulnerability_task import AppVulnerabilityTask
        from .assigned_compute_instance_details import AssignedComputeInstanceDetails
        from .assignment_filter_evaluation_status_details import AssignmentFilterEvaluationStatusDetails
        from .associated_team_info import AssociatedTeamInfo
        from .attachment import Attachment
        from .attachment_base import AttachmentBase
        from .attachment_session import AttachmentSession
        from .attack_simulation_operation import AttackSimulationOperation
        from .attack_simulation_root import AttackSimulationRoot
        from .attendance_record import AttendanceRecord
        from .attribute_mapping_function_schema import AttributeMappingFunctionSchema
        from .attribute_set import AttributeSet
        from .audio_routing_group import AudioRoutingGroup
        from .audit_event import AuditEvent
        from .authentication import Authentication
        from .authentications_metric import AuthenticationsMetric
        from .authentication_combination_configuration import AuthenticationCombinationConfiguration
        from .authentication_context_class_reference import AuthenticationContextClassReference
        from .authentication_events_flow import AuthenticationEventsFlow
        from .authentication_events_policy import AuthenticationEventsPolicy
        from .authentication_event_listener import AuthenticationEventListener
        from .authentication_flows_policy import AuthenticationFlowsPolicy
        from .authentication_listener import AuthenticationListener
        from .authentication_method import AuthenticationMethod
        from .authentication_methods_policy import AuthenticationMethodsPolicy
        from .authentication_methods_root import AuthenticationMethodsRoot
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_mode_detail import AuthenticationMethodModeDetail
        from .authentication_method_target import AuthenticationMethodTarget
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .authentication_strength_root import AuthenticationStrengthRoot
        from .authored_note import AuthoredNote
        from .authorization_policy import AuthorizationPolicy
        from .authorization_system import AuthorizationSystem
        from .authorization_system_identity import AuthorizationSystemIdentity
        from .authorization_system_resource import AuthorizationSystemResource
        from .authorization_system_type_action import AuthorizationSystemTypeAction
        from .authorization_system_type_service import AuthorizationSystemTypeService
        from .aws_access_key import AwsAccessKey
        from .aws_authorization_system import AwsAuthorizationSystem
        from .aws_authorization_system_resource import AwsAuthorizationSystemResource
        from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction
        from .aws_ec2_instance import AwsEc2Instance
        from .aws_external_system_access_finding import AwsExternalSystemAccessFinding
        from .aws_external_system_access_role_finding import AwsExternalSystemAccessRoleFinding
        from .aws_group import AwsGroup
        from .aws_identity import AwsIdentity
        from .aws_identity_access_management_key_age_finding import AwsIdentityAccessManagementKeyAgeFinding
        from .aws_identity_access_management_key_usage_finding import AwsIdentityAccessManagementKeyUsageFinding
        from .aws_lambda import AwsLambda
        from .aws_policy import AwsPolicy
        from .aws_role import AwsRole
        from .aws_secret_information_access_finding import AwsSecretInformationAccessFinding
        from .aws_security_tool_administration_finding import AwsSecurityToolAdministrationFinding
        from .aws_user import AwsUser
        from .azure_authorization_system import AzureAuthorizationSystem
        from .azure_authorization_system_resource import AzureAuthorizationSystemResource
        from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction
        from .azure_a_d_authentication import AzureADAuthentication
        from .azure_a_d_windows_autopilot_deployment_profile import AzureADWindowsAutopilotDeploymentProfile
        from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
        from .azure_group import AzureGroup
        from .azure_identity import AzureIdentity
        from .azure_managed_identity import AzureManagedIdentity
        from .azure_role_definition import AzureRoleDefinition
        from .azure_serverless_function import AzureServerlessFunction
        from .azure_service_principal import AzureServicePrincipal
        from .azure_user import AzureUser
        from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicy
        from .b2c_identity_user_flow import B2cIdentityUserFlow
        from .b2x_identity_user_flow import B2xIdentityUserFlow
        from .base_item import BaseItem
        from .base_item_version import BaseItemVersion
        from .base_site_page import BaseSitePage
        from .bitlocker import Bitlocker
        from .bitlocker_recovery_key import BitlockerRecoveryKey
        from .booking_appointment import BookingAppointment
        from .booking_business import BookingBusiness
        from .booking_currency import BookingCurrency
        from .booking_customer import BookingCustomer
        from .booking_custom_question import BookingCustomQuestion
        from .booking_named_entity import BookingNamedEntity
        from .booking_person import BookingPerson
        from .booking_service import BookingService
        from .booking_staff_member import BookingStaffMember
        from .browser_shared_cookie import BrowserSharedCookie
        from .browser_site import BrowserSite
        from .browser_site_list import BrowserSiteList
        from .built_in_identity_provider import BuiltInIdentityProvider
        from .bulk_upload import BulkUpload
        from .business_flow import BusinessFlow
        from .business_flow_template import BusinessFlowTemplate
        from .business_scenario import BusinessScenario
        from .business_scenario_planner import BusinessScenarioPlanner
        from .business_scenario_plan_reference import BusinessScenarioPlanReference
        from .business_scenario_task import BusinessScenarioTask
        from .calendar import Calendar
        from .calendar_group import CalendarGroup
        from .calendar_permission import CalendarPermission
        from .calendar_sharing_message import CalendarSharingMessage
        from .call import Call
        from .call_activity_statistics import CallActivityStatistics
        from .call_event import CallEvent
        from .call_recording import CallRecording
        from .call_records.call_record import CallRecord
        from .call_records.organizer import Organizer
        from .call_records.participant import Participant
        from .call_records.participant_base import ParticipantBase
        from .call_records.segment import Segment
        from .call_records.session import Session
        from .call_transcript import CallTranscript
        from .cancel_media_processing_operation import CancelMediaProcessingOperation
        from .canvas_layout import CanvasLayout
        from .cart_to_class_association import CartToClassAssociation
        from .certificate_authority_as_entity import CertificateAuthorityAsEntity
        from .certificate_authority_path import CertificateAuthorityPath
        from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
        from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
        from .certificate_connector_details import CertificateConnectorDetails
        from .change_tracked_entity import ChangeTrackedEntity
        from .channel import Channel
        from .chat import Chat
        from .chat_activity_statistics import ChatActivityStatistics
        from .chat_message import ChatMessage
        from .chat_message_hosted_content import ChatMessageHostedContent
        from .chat_message_info import ChatMessageInfo
        from .checklist_item import ChecklistItem
        from .chrome_o_s_onboarding_settings import ChromeOSOnboardingSettings
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .classification_job_response import ClassificationJobResponse
        from .cloud_app_security_profile import CloudAppSecurityProfile
        from .cloud_clipboard_item import CloudClipboardItem
        from .cloud_clipboard_root import CloudClipboardRoot
        from .cloud_pc_audit_event import CloudPcAuditEvent
        from .cloud_pc_bulk_action import CloudPcBulkAction
        from .cloud_pc_bulk_disaster_recovery_failback import CloudPcBulkDisasterRecoveryFailback
        from .cloud_pc_bulk_disaster_recovery_failover import CloudPcBulkDisasterRecoveryFailover
        from .cloud_pc_bulk_modify_disk_encryption_type import CloudPcBulkModifyDiskEncryptionType
        from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff
        from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn
        from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision
        from .cloud_pc_bulk_resize import CloudPcBulkResize
        from .cloud_pc_bulk_restart import CloudPcBulkRestart
        from .cloud_pc_bulk_restore import CloudPcBulkRestore
        from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot
        from .cloud_pc_cross_cloud_government_organization_mapping import CloudPcCrossCloudGovernmentOrganizationMapping
        from .cloud_pc_device_image import CloudPcDeviceImage
        from .cloud_pc_export_job import CloudPcExportJob
        from .cloud_pc_external_partner_setting import CloudPcExternalPartnerSetting
        from .cloud_pc_front_line_service_plan import CloudPcFrontLineServicePlan
        from .cloud_pc_gallery_image import CloudPcGalleryImage
        from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
        from .cloud_pc_organization_settings import CloudPcOrganizationSettings
        from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
        from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
        from .cloud_pc_reports import CloudPcReports
        from .cloud_pc_service_plan import CloudPcServicePlan
        from .cloud_pc_shared_use_service_plan import CloudPcSharedUseServicePlan
        from .cloud_pc_snapshot import CloudPcSnapshot
        from .cloud_pc_supported_region import CloudPcSupportedRegion
        from .cloud_pc_user_setting import CloudPcUserSetting
        from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment
        from .cloud_p_c import CloudPC
        from .cloud_p_c_connectivity_issue import CloudPCConnectivityIssue
        from .column_definition import ColumnDefinition
        from .column_link import ColumnLink
        from .comanagement_eligible_device import ComanagementEligibleDevice
        from .command import Command
        from .comms_operation import CommsOperation
        from .community import Community
        from .company_subscription import CompanySubscription
        from .compliance_management_partner import ComplianceManagementPartner
        from .conditional_access_policy import ConditionalAccessPolicy
        from .conditional_access_root import ConditionalAccessRoot
        from .conditional_access_template import ConditionalAccessTemplate
        from .conditional_access_what_if_policy import ConditionalAccessWhatIfPolicy
        from .config_manager_collection import ConfigManagerCollection
        from .connected_organization import ConnectedOrganization
        from .connection_operation import ConnectionOperation
        from .connector import Connector
        from .connector_group import ConnectorGroup
        from .contact import Contact
        from .contact_folder import ContactFolder
        from .contact_merge_suggestions import ContactMergeSuggestions
        from .content_sharing_session import ContentSharingSession
        from .content_type import ContentType
        from .continuous_access_evaluation_policy import ContinuousAccessEvaluationPolicy
        from .contract import Contract
        from .conversation import Conversation
        from .conversation_member import ConversationMember
        from .conversation_thread import ConversationThread
        from .cors_configuration_v2 import CorsConfiguration_v2
        from .country_named_location import CountryNamedLocation
        from .credential_usage_summary import CredentialUsageSummary
        from .credential_user_registration_count import CredentialUserRegistrationCount
        from .credential_user_registration_details import CredentialUserRegistrationDetails
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault
        from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
        from .custom_app_scope import CustomAppScope
        from .custom_authentication_extension import CustomAuthenticationExtension
        from .custom_callout_extension import CustomCalloutExtension
        from .custom_extension_handler import CustomExtensionHandler
        from .custom_extension_stage_setting import CustomExtensionStageSetting
        from .custom_security_attribute_audit import CustomSecurityAttributeAudit
        from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
        from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
        from .daily_inactive_users_metric import DailyInactiveUsersMetric
        from .daily_user_insight_metrics_root import DailyUserInsightMetricsRoot
        from .data_classification_service import DataClassificationService
        from .data_collection_info import DataCollectionInfo
        from .data_loss_prevention_policy import DataLossPreventionPolicy
        from .data_policy_operation import DataPolicyOperation
        from .data_sharing_consent import DataSharingConsent
        from .day_note import DayNote
        from .default_device_compliance_policy import DefaultDeviceCompliancePolicy
        from .default_managed_app_protection import DefaultManagedAppProtection
        from .default_user_role_override import DefaultUserRoleOverride
        from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment
        from .delegated_admin_customer import DelegatedAdminCustomer
        from .delegated_admin_relationship import DelegatedAdminRelationship
        from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
        from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest
        from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail
        from .delegated_permission_classification import DelegatedPermissionClassification
        from .deleted_chat import DeletedChat
        from .deleted_item_container import DeletedItemContainer
        from .deleted_team import DeletedTeam
        from .delta_participants import DeltaParticipants
        from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
        from .dep_enrollment_profile import DepEnrollmentProfile
        from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
        from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
        from .dep_onboarding_setting import DepOnboardingSetting
        from .detected_app import DetectedApp
        from .device import Device
        from .device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter
        from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
        from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
        from .device_app_management import DeviceAppManagement
        from .device_app_management_task import DeviceAppManagementTask
        from .device_category import DeviceCategory
        from .device_comanagement_authority_configuration import DeviceComanagementAuthorityConfiguration
        from .device_compliance_action_item import DeviceComplianceActionItem
        from .device_compliance_device_overview import DeviceComplianceDeviceOverview
        from .device_compliance_device_status import DeviceComplianceDeviceStatus
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
        from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
        from .device_compliance_policy_group_assignment import DeviceCompliancePolicyGroupAssignment
        from .device_compliance_policy_policy_set_item import DeviceCompliancePolicyPolicySetItem
        from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
        from .device_compliance_policy_state import DeviceCompliancePolicyState
        from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
        from .device_compliance_script import DeviceComplianceScript
        from .device_compliance_script_device_state import DeviceComplianceScriptDeviceState
        from .device_compliance_script_run_summary import DeviceComplianceScriptRunSummary
        from .device_compliance_setting_state import DeviceComplianceSettingState
        from .device_compliance_user_overview import DeviceComplianceUserOverview
        from .device_compliance_user_status import DeviceComplianceUserStatus
        from .device_configuration import DeviceConfiguration
        from .device_configuration_assignment import DeviceConfigurationAssignment
        from .device_configuration_conflict_summary import DeviceConfigurationConflictSummary
        from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
        from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
        from .device_configuration_device_status import DeviceConfigurationDeviceStatus
        from .device_configuration_group_assignment import DeviceConfigurationGroupAssignment
        from .device_configuration_policy_set_item import DeviceConfigurationPolicySetItem
        from .device_configuration_profile import DeviceConfigurationProfile
        from .device_configuration_state import DeviceConfigurationState
        from .device_configuration_user_overview import DeviceConfigurationUserOverview
        from .device_configuration_user_state_summary import DeviceConfigurationUserStateSummary
        from .device_configuration_user_status import DeviceConfigurationUserStatus
        from .device_custom_attribute_shell_script import DeviceCustomAttributeShellScript
        from .device_enrollment_configuration import DeviceEnrollmentConfiguration
        from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
        from .device_enrollment_notification_configuration import DeviceEnrollmentNotificationConfiguration
        from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
        from .device_enrollment_platform_restriction_configuration import DeviceEnrollmentPlatformRestrictionConfiguration
        from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
        from .device_health_script import DeviceHealthScript
        from .device_health_script_assignment import DeviceHealthScriptAssignment
        from .device_health_script_device_state import DeviceHealthScriptDeviceState
        from .device_health_script_run_summary import DeviceHealthScriptRunSummary
        from .device_install_state import DeviceInstallState
        from .device_local_credential_info import DeviceLocalCredentialInfo
        from .device_log_collection_response import DeviceLogCollectionResponse
        from .device_management.alert_record import AlertRecord
        from .device_management.alert_rule import AlertRule
        from .device_management.device_management import DeviceManagement
        from .device_management.monitoring import Monitoring
        from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition
        from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
        from .device_management_autopilot_event import DeviceManagementAutopilotEvent
        from .device_management_autopilot_policy_status_detail import DeviceManagementAutopilotPolicyStatusDetail
        from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
        from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration
        from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition
        from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance
        from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition
        from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
        from .device_management_compliance_action_item import DeviceManagementComplianceActionItem
        from .device_management_compliance_policy import DeviceManagementCompliancePolicy
        from .device_management_compliance_scheduled_action_for_rule import DeviceManagementComplianceScheduledActionForRule
        from .device_management_configuration_category import DeviceManagementConfigurationCategory
        from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
        from .device_management_configuration_choice_setting_definition import DeviceManagementConfigurationChoiceSettingDefinition
        from .device_management_configuration_policy import DeviceManagementConfigurationPolicy
        from .device_management_configuration_policy_assignment import DeviceManagementConfigurationPolicyAssignment
        from .device_management_configuration_policy_policy_set_item import DeviceManagementConfigurationPolicyPolicySetItem
        from .device_management_configuration_policy_template import DeviceManagementConfigurationPolicyTemplate
        from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition
        from .device_management_configuration_setting import DeviceManagementConfigurationSetting
        from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
        from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition
        from .device_management_configuration_setting_group_definition import DeviceManagementConfigurationSettingGroupDefinition
        from .device_management_configuration_setting_template import DeviceManagementConfigurationSettingTemplate
        from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition
        from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition
        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
        from .device_management_domain_join_connector import DeviceManagementDomainJoinConnector
        from .device_management_exchange_connector import DeviceManagementExchangeConnector
        from .device_management_exchange_on_premises_policy import DeviceManagementExchangeOnPremisesPolicy
        from .device_management_export_job import DeviceManagementExportJob
        from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
        from .device_management_intent import DeviceManagementIntent
        from .device_management_intent_assignment import DeviceManagementIntentAssignment
        from .device_management_intent_device_setting_state_summary import DeviceManagementIntentDeviceSettingStateSummary
        from .device_management_intent_device_state import DeviceManagementIntentDeviceState
        from .device_management_intent_device_state_summary import DeviceManagementIntentDeviceStateSummary
        from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory
        from .device_management_intent_user_state import DeviceManagementIntentUserState
        from .device_management_intent_user_state_summary import DeviceManagementIntentUserStateSummary
        from .device_management_partner import DeviceManagementPartner
        from .device_management_reports import DeviceManagementReports
        from .device_management_resource_access_profile_assignment import DeviceManagementResourceAccessProfileAssignment
        from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase
        from .device_management_reusable_policy_setting import DeviceManagementReusablePolicySetting
        from .device_management_script import DeviceManagementScript
        from .device_management_script_assignment import DeviceManagementScriptAssignment
        from .device_management_script_device_state import DeviceManagementScriptDeviceState
        from .device_management_script_group_assignment import DeviceManagementScriptGroupAssignment
        from .device_management_script_policy_set_item import DeviceManagementScriptPolicySetItem
        from .device_management_script_run_summary import DeviceManagementScriptRunSummary
        from .device_management_script_user_state import DeviceManagementScriptUserState
        from .device_management_setting_category import DeviceManagementSettingCategory
        from .device_management_setting_definition import DeviceManagementSettingDefinition
        from .device_management_setting_instance import DeviceManagementSettingInstance
        from .device_management_string_setting_instance import DeviceManagementStringSettingInstance
        from .device_management_template import DeviceManagementTemplate
        from .device_management_template_insights_definition import DeviceManagementTemplateInsightsDefinition
        from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
        from .device_registration_policy import DeviceRegistrationPolicy
        from .device_setup_configuration import DeviceSetupConfiguration
        from .device_shell_script import DeviceShellScript
        from .directory import Directory
        from .directory_audit import DirectoryAudit
        from .directory_definition import DirectoryDefinition
        from .directory_object import DirectoryObject
        from .directory_object_partner_reference import DirectoryObjectPartnerReference
        from .directory_role import DirectoryRole
        from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicy
        from .directory_role_template import DirectoryRoleTemplate
        from .directory_setting import DirectorySetting
        from .directory_setting_template import DirectorySettingTemplate
        from .dlp_evaluate_policies_job_response import DlpEvaluatePoliciesJobResponse
        from .document import Document
        from .document_comment import DocumentComment
        from .document_comment_reply import DocumentCommentReply
        from .document_set_version import DocumentSetVersion
        from .domain import Domain
        from .domain_dns_cname_record import DomainDnsCnameRecord
        from .domain_dns_mx_record import DomainDnsMxRecord
        from .domain_dns_record import DomainDnsRecord
        from .domain_dns_srv_record import DomainDnsSrvRecord
        from .domain_dns_txt_record import DomainDnsTxtRecord
        from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
        from .domain_security_profile import DomainSecurityProfile
        from .drive import Drive
        from .drive_item import DriveItem
        from .drive_item_version import DriveItemVersion
        from .eas_email_profile_configuration_base import EasEmailProfileConfigurationBase
        from .edge import Edge
        from .ediscovery.add_to_review_set_operation import AddToReviewSetOperation
        from .ediscovery.case import Case
        from .ediscovery.case_export_operation import CaseExportOperation
        from .ediscovery.case_hold_operation import CaseHoldOperation
        from .ediscovery.case_index_operation import CaseIndexOperation
        from .ediscovery.case_operation import CaseOperation
        from .ediscovery.case_settings import CaseSettings
        from .ediscovery.custodian import Custodian
        from .ediscovery.data_source import DataSource
        from .ediscovery.data_source_container import DataSourceContainer
        from .ediscovery.ediscoveryroot import Ediscoveryroot
        from .ediscovery.estimate_statistics_operation import EstimateStatisticsOperation
        from .ediscovery.legal_hold import LegalHold
        from .ediscovery.noncustodial_data_source import NoncustodialDataSource
        from .ediscovery.purge_data_operation import PurgeDataOperation
        from .ediscovery.review_set import ReviewSet
        from .ediscovery.review_set_query import ReviewSetQuery
        from .ediscovery.site_source import SiteSource
        from .ediscovery.source_collection import SourceCollection
        from .ediscovery.tag import Tag
        from .ediscovery.tag_operation import TagOperation
        from .ediscovery.unified_group_source import UnifiedGroupSource
        from .ediscovery.user_source import UserSource
        from .edition_upgrade_configuration import EditionUpgradeConfiguration
        from .educational_activity import EducationalActivity
        from .education_assignment import EducationAssignment
        from .education_assignment_defaults import EducationAssignmentDefaults
        from .education_assignment_resource import EducationAssignmentResource
        from .education_assignment_settings import EducationAssignmentSettings
        from .education_category import EducationCategory
        from .education_class import EducationClass
        from .education_feedback_outcome import EducationFeedbackOutcome
        from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome
        from .education_grading_category import EducationGradingCategory
        from .education_grading_scheme import EducationGradingScheme
        from .education_module import EducationModule
        from .education_module_resource import EducationModuleResource
        from .education_organization import EducationOrganization
        from .education_outcome import EducationOutcome
        from .education_points_outcome import EducationPointsOutcome
        from .education_rubric import EducationRubric
        from .education_rubric_outcome import EducationRubricOutcome
        from .education_school import EducationSchool
        from .education_submission import EducationSubmission
        from .education_submission_resource import EducationSubmissionResource
        from .education_synchronization_error import EducationSynchronizationError
        from .education_synchronization_profile import EducationSynchronizationProfile
        from .education_synchronization_profile_status import EducationSynchronizationProfileStatus
        from .education_user import EducationUser
        from .email_activity_statistics import EmailActivityStatistics
        from .email_authentication_method import EmailAuthenticationMethod
        from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration
        from .email_file_assessment_request import EmailFileAssessmentRequest
        from .embedded_s_i_m_activation_code_pool import EmbeddedSIMActivationCodePool
        from .embedded_s_i_m_activation_code_pool_assignment import EmbeddedSIMActivationCodePoolAssignment
        from .embedded_s_i_m_device_state import EmbeddedSIMDeviceState
        from .employee_experience_user import EmployeeExperienceUser
        from .encrypted_aws_storage_bucket_finding import EncryptedAwsStorageBucketFinding
        from .encrypted_azure_storage_account_finding import EncryptedAzureStorageAccountFinding
        from .encrypted_gcp_storage_bucket_finding import EncryptedGcpStorageBucketFinding
        from .endpoint import Endpoint
        from .end_user_notification import EndUserNotification
        from .end_user_notification_detail import EndUserNotificationDetail
        from .engagement_async_operation import EngagementAsyncOperation
        from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
        from .enrollment_profile import EnrollmentProfile
        from .enrollment_restrictions_configuration_policy_set_item import EnrollmentRestrictionsConfigurationPolicySetItem
        from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
        from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
        from .entitlement_management import EntitlementManagement
        from .entitlement_management_settings import EntitlementManagementSettings
        from .evaluate_label_job_response import EvaluateLabelJobResponse
        from .event import Event
        from .event_message import EventMessage
        from .event_message_request import EventMessageRequest
        from .event_message_response import EventMessageResponse
        from .exact_match_data_store import ExactMatchDataStore
        from .exact_match_data_store_base import ExactMatchDataStoreBase
        from .exact_match_job_base import ExactMatchJobBase
        from .exact_match_lookup_job import ExactMatchLookupJob
        from .exact_match_session import ExactMatchSession
        from .exact_match_session_base import ExactMatchSessionBase
        from .exact_match_upload_agent import ExactMatchUploadAgent
        from .extension import Extension
        from .extension_property import ExtensionProperty
        from .external import External
        from .externally_accessible_aws_storage_bucket_finding import ExternallyAccessibleAwsStorageBucketFinding
        from .externally_accessible_azure_blob_container_finding import ExternallyAccessibleAzureBlobContainerFinding
        from .externally_accessible_gcp_storage_bucket_finding import ExternallyAccessibleGcpStorageBucketFinding
        from .external_connection import ExternalConnection
        from .external_connectors.connection_operation import ConnectionOperation
        from .external_connectors.connection_quota import ConnectionQuota
        from .external_connectors.external_activity import ExternalActivity
        from .external_connectors.external_activity_result import ExternalActivityResult
        from .external_connectors.external_connection import ExternalConnection
        from .external_connectors.external_group import ExternalGroup
        from .external_connectors.external_item import ExternalItem
        from .external_connectors.identity import Identity
        from .external_connectors.schema import Schema
        from .external_domain_name import ExternalDomainName
        from .external_group import ExternalGroup
        from .external_identities_policy import ExternalIdentitiesPolicy
        from .external_item import ExternalItem
        from .external_meeting_registrant import ExternalMeetingRegistrant
        from .external_meeting_registration import ExternalMeetingRegistration
        from .external_profile import ExternalProfile
        from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow
        from .external_user_profile import ExternalUserProfile
        from .e_book_install_summary import EBookInstallSummary
        from .feature_rollout_policy import FeatureRolloutPolicy
        from .federated_identity_credential import FederatedIdentityCredential
        from .federated_token_validation_policy import FederatedTokenValidationPolicy
        from .fido2_authentication_method import Fido2AuthenticationMethod
        from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
        from .fido2_combination_configuration import Fido2CombinationConfiguration
        from .field_value_set import FieldValueSet
        from .file_assessment_request import FileAssessmentRequest
        from .file_attachment import FileAttachment
        from .file_classification_request import FileClassificationRequest
        from .file_security_profile import FileSecurityProfile
        from .filter_operator_schema import FilterOperatorSchema
        from .finding import Finding
        from .focus_activity_statistics import FocusActivityStatistics
        from .gcp_authorization_system import GcpAuthorizationSystem
        from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
        from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
        from .gcp_cloud_function import GcpCloudFunction
        from .gcp_group import GcpGroup
        from .gcp_identity import GcpIdentity
        from .gcp_role import GcpRole
        from .gcp_service_account import GcpServiceAccount
        from .gcp_user import GcpUser
        from .goals import Goals
        from .goals_export_job import GoalsExportJob
        from .governance_insight import GovernanceInsight
        from .governance_policy_template import GovernancePolicyTemplate
        from .governance_resource import GovernanceResource
        from .governance_role_assignment import GovernanceRoleAssignment
        from .governance_role_assignment_request import GovernanceRoleAssignmentRequest
        from .governance_role_definition import GovernanceRoleDefinition
        from .governance_role_setting import GovernanceRoleSetting
        from .governance_subject import GovernanceSubject
        from .group import Group
        from .group_lifecycle_policy import GroupLifecyclePolicy
        from .group_policy_category import GroupPolicyCategory
        from .group_policy_configuration import GroupPolicyConfiguration
        from .group_policy_configuration_assignment import GroupPolicyConfigurationAssignment
        from .group_policy_definition import GroupPolicyDefinition
        from .group_policy_definition_file import GroupPolicyDefinitionFile
        from .group_policy_definition_value import GroupPolicyDefinitionValue
        from .group_policy_migration_report import GroupPolicyMigrationReport
        from .group_policy_object_file import GroupPolicyObjectFile
        from .group_policy_operation import GroupPolicyOperation
        from .group_policy_presentation import GroupPolicyPresentation
        from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
        from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
        from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
        from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
        from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
        from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
        from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
        from .group_policy_presentation_text import GroupPolicyPresentationText
        from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox
        from .group_policy_presentation_value import GroupPolicyPresentationValue
        from .group_policy_presentation_value_boolean import GroupPolicyPresentationValueBoolean
        from .group_policy_presentation_value_decimal import GroupPolicyPresentationValueDecimal
        from .group_policy_presentation_value_list import GroupPolicyPresentationValueList
        from .group_policy_presentation_value_long_decimal import GroupPolicyPresentationValueLongDecimal
        from .group_policy_presentation_value_multi_text import GroupPolicyPresentationValueMultiText
        from .group_policy_presentation_value_text import GroupPolicyPresentationValueText
        from .group_policy_setting_mapping import GroupPolicySettingMapping
        from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile
        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation
        from .hardware_configuration import HardwareConfiguration
        from .hardware_configuration_assignment import HardwareConfigurationAssignment
        from .hardware_configuration_device_state import HardwareConfigurationDeviceState
        from .hardware_configuration_run_summary import HardwareConfigurationRunSummary
        from .hardware_configuration_user_state import HardwareConfigurationUserState
        from .hardware_oath_authentication_method_configuration import HardwareOathAuthenticationMethodConfiguration
        from .hardware_password_info import HardwarePasswordInfo
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .horizontal_section import HorizontalSection
        from .horizontal_section_column import HorizontalSectionColumn
        from .host_security_profile import HostSecurityProfile
        from .identity_api_connector import IdentityApiConnector
        from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
        from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute
        from .identity_finding import IdentityFinding
        from .identity_governance.custom_task_extension import CustomTaskExtension
        from .identity_governance.lifecycle_management_settings import LifecycleManagementSettings
        from .identity_governance.lifecycle_workflows_container import LifecycleWorkflowsContainer
        from .identity_governance.run import Run
        from .identity_governance.task import Task
        from .identity_governance.task_definition import TaskDefinition
        from .identity_governance.task_processing_result import TaskProcessingResult
        from .identity_governance.task_report import TaskReport
        from .identity_governance.user_processing_result import UserProcessingResult
        from .identity_governance.workflow_template import WorkflowTemplate
        from .identity_provider import IdentityProvider
        from .identity_provider_base import IdentityProviderBase
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .identity_user_flow import IdentityUserFlow
        from .identity_user_flow_attribute import IdentityUserFlowAttribute
        from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
        from .impacted_resource import ImpactedResource
        from .imported_apple_device_identity import ImportedAppleDeviceIdentity
        from .imported_apple_device_identity_result import ImportedAppleDeviceIdentityResult
        from .imported_device_identity import ImportedDeviceIdentity
        from .imported_device_identity_result import ImportedDeviceIdentityResult
        from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
        from .imported_windows_autopilot_device_identity_upload import ImportedWindowsAutopilotDeviceIdentityUpload
        from .inactive_aws_resource_finding import InactiveAwsResourceFinding
        from .inactive_aws_role_finding import InactiveAwsRoleFinding
        from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding
        from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding
        from .inactive_group_finding import InactiveGroupFinding
        from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding
        from .inactive_users_by_application_metric_base import InactiveUsersByApplicationMetricBase
        from .inactive_users_metric_base import InactiveUsersMetricBase
        from .inactive_user_finding import InactiveUserFinding
        from .industry_data.administrative_unit_provisioning_flow import AdministrativeUnitProvisioningFlow
        from .industry_data.azure_data_lake_connector import AzureDataLakeConnector
        from .industry_data.class_group_provisioning_flow import ClassGroupProvisioningFlow
        from .industry_data.file_data_connector import FileDataConnector
        from .industry_data.file_validate_operation import FileValidateOperation
        from .industry_data.inbound_file_flow import InboundFileFlow
        from .industry_data.inbound_flow import InboundFlow
        from .industry_data.inbound_flow_activity import InboundFlowActivity
        from .industry_data.industry_data_activity import IndustryDataActivity
        from .industry_data.industry_data_connector import IndustryDataConnector
        from .industry_data.industry_data_root import IndustryDataRoot
        from .industry_data.industry_data_run import IndustryDataRun
        from .industry_data.industry_data_run_activity import IndustryDataRunActivity
        from .industry_data.outbound_flow_activity import OutboundFlowActivity
        from .industry_data.outbound_provisioning_flow_set import OutboundProvisioningFlowSet
        from .industry_data.provisioning_flow import ProvisioningFlow
        from .industry_data.reference_definition import ReferenceDefinition
        from .industry_data.role_group import RoleGroup
        from .industry_data.security_group_provisioning_flow import SecurityGroupProvisioningFlow
        from .industry_data.source_system_definition import SourceSystemDefinition
        from .industry_data.user_provisioning_flow import UserProvisioningFlow
        from .industry_data.validate_operation import ValidateOperation
        from .industry_data.year_time_period_definition import YearTimePeriodDefinition
        from .inference_classification import InferenceClassification
        from .inference_classification_override import InferenceClassificationOverride
        from .information_protection import InformationProtection
        from .information_protection_label import InformationProtectionLabel
        from .information_protection_policy import InformationProtectionPolicy
        from .insights_settings import InsightsSettings
        from .insight_summary import InsightSummary
        from .internal_domain_federation import InternalDomainFederation
        from .internet_explorer_mode import InternetExplorerMode
        from .intune_branding_profile import IntuneBrandingProfile
        from .intune_branding_profile_assignment import IntuneBrandingProfileAssignment
        from .invalid_license_alert_configuration import InvalidLicenseAlertConfiguration
        from .invalid_license_alert_incident import InvalidLicenseAlertIncident
        from .invitation import Invitation
        from .invite_participants_operation import InviteParticipantsOperation
        from .invoke_user_flow_listener import InvokeUserFlowListener
        from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
        from .iosi_pad_o_s_web_clip import IosiPadOSWebClip
        from .ios_certificate_profile import IosCertificateProfile
        from .ios_certificate_profile_base import IosCertificateProfileBase
        from .ios_compliance_policy import IosCompliancePolicy
        from .ios_custom_configuration import IosCustomConfiguration
        from .ios_derived_credential_authentication_configuration import IosDerivedCredentialAuthenticationConfiguration
        from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
        from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
        from .ios_education_device_configuration import IosEducationDeviceConfiguration
        from .ios_edu_device_configuration import IosEduDeviceConfiguration
        from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration
        from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration
        from .ios_general_device_configuration import IosGeneralDeviceConfiguration
        from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
        from .ios_lob_app import IosLobApp
        from .ios_lob_app_provisioning_configuration import IosLobAppProvisioningConfiguration
        from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment
        from .ios_lob_app_provisioning_configuration_policy_set_item import IosLobAppProvisioningConfigurationPolicySetItem
        from .ios_managed_app_protection import IosManagedAppProtection
        from .ios_managed_app_registration import IosManagedAppRegistration
        from .ios_mobile_app_configuration import IosMobileAppConfiguration
        from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
        from .ios_scep_certificate_profile import IosScepCertificateProfile
        from .ios_store_app import IosStoreApp
        from .ios_trusted_root_certificate import IosTrustedRootCertificate
        from .ios_update_configuration import IosUpdateConfiguration
        from .ios_update_device_status import IosUpdateDeviceStatus
        from .ios_vpn_configuration import IosVpnConfiguration
        from .ios_vpp_app import IosVppApp
        from .ios_vpp_app_assigned_device_license import IosVppAppAssignedDeviceLicense
        from .ios_vpp_app_assigned_license import IosVppAppAssignedLicense
        from .ios_vpp_app_assigned_user_license import IosVppAppAssignedUserLicense
        from .ios_vpp_e_book import IosVppEBook
        from .ios_vpp_e_book_assignment import IosVppEBookAssignment
        from .ios_wi_fi_configuration import IosWiFiConfiguration
        from .ip_application_segment import IpApplicationSegment
        from .ip_named_location import IpNamedLocation
        from .ip_security_profile import IpSecurityProfile
        from .item_activity import ItemActivity
        from .item_activity_o_l_d import ItemActivityOLD
        from .item_activity_stat import ItemActivityStat
        from .item_address import ItemAddress
        from .item_analytics import ItemAnalytics
        from .item_attachment import ItemAttachment
        from .item_email import ItemEmail
        from .item_facet import ItemFacet
        from .item_insights import ItemInsights
        from .item_patent import ItemPatent
        from .item_phone import ItemPhone
        from .item_publication import ItemPublication
        from .item_retention_label import ItemRetentionLabel
        from .job_response_base import JobResponseBase
        from .landing_page import LandingPage
        from .landing_page_detail import LandingPageDetail
        from .language_proficiency import LanguageProficiency
        from .learning_assignment import LearningAssignment
        from .learning_content import LearningContent
        from .learning_course_activity import LearningCourseActivity
        from .learning_provider import LearningProvider
        from .learning_self_initiated_course import LearningSelfInitiatedCourse
        from .license_details import LicenseDetails
        from .linked_resource import LinkedResource
        from .list_ import List_
        from .list_item import ListItem
        from .list_item_version import ListItemVersion
        from .localized_notification_message import LocalizedNotificationMessage
        from .login_page import LoginPage
        from .long_running_operation import LongRunningOperation
        from .lookup_result_row import LookupResultRow
        from .m365_apps_installation_options import M365AppsInstallationOptions
        from .mac_os_vpp_app import MacOsVppApp
        from .mac_os_vpp_app_assigned_license import MacOsVppAppAssignedLicense
        from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
        from .mac_o_s_compliance_policy import MacOSCompliancePolicy
        from .mac_o_s_custom_app_configuration import MacOSCustomAppConfiguration
        from .mac_o_s_custom_configuration import MacOSCustomConfiguration
        from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
        from .mac_o_s_dmg_app import MacOSDmgApp
        from .mac_o_s_endpoint_protection_configuration import MacOSEndpointProtectionConfiguration
        from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration
        from .mac_o_s_extensions_configuration import MacOSExtensionsConfiguration
        from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
        from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
        from .mac_o_s_lob_app import MacOSLobApp
        from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp
        from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp
        from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
        from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
        from .mac_o_s_pkg_app import MacOSPkgApp
        from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
        from .mac_o_s_software_update_account_summary import MacOSSoftwareUpdateAccountSummary
        from .mac_o_s_software_update_category_summary import MacOSSoftwareUpdateCategorySummary
        from .mac_o_s_software_update_configuration import MacOSSoftwareUpdateConfiguration
        from .mac_o_s_software_update_state_summary import MacOSSoftwareUpdateStateSummary
        from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
        from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
        from .mac_o_s_web_clip import MacOSWebClip
        from .mac_o_s_wired_network_configuration import MacOSWiredNetworkConfiguration
        from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration
        from .mail_assessment_request import MailAssessmentRequest
        from .mail_folder import MailFolder
        from .mail_search_folder import MailSearchFolder
        from .malware_state_for_windows_device import MalwareStateForWindowsDevice
        from .managed_all_device_certificate_state import ManagedAllDeviceCertificateState
        from .managed_android_lob_app import ManagedAndroidLobApp
        from .managed_android_store_app import ManagedAndroidStoreApp
        from .managed_app import ManagedApp
        from .managed_app_configuration import ManagedAppConfiguration
        from .managed_app_log_collection_request import ManagedAppLogCollectionRequest
        from .managed_app_operation import ManagedAppOperation
        from .managed_app_policy import ManagedAppPolicy
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_app_protection import ManagedAppProtection
        from .managed_app_protection_policy_set_item import ManagedAppProtectionPolicySetItem
        from .managed_app_registration import ManagedAppRegistration
        from .managed_app_status import ManagedAppStatus
        from .managed_app_status_raw import ManagedAppStatusRaw
        from .managed_device import ManagedDevice
        from .managed_device_certificate_state import ManagedDeviceCertificateState
        from .managed_device_cleanup_rule import ManagedDeviceCleanupRule
        from .managed_device_encryption_state import ManagedDeviceEncryptionState
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
        from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
        from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
        from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
        from .managed_device_mobile_app_configuration_policy_set_item import ManagedDeviceMobileAppConfigurationPolicySetItem
        from .managed_device_mobile_app_configuration_state import ManagedDeviceMobileAppConfigurationState
        from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
        from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary
        from .managed_device_overview import ManagedDeviceOverview
        from .managed_e_book import ManagedEBook
        from .managed_e_book_assignment import ManagedEBookAssignment
        from .managed_e_book_category import ManagedEBookCategory
        from .managed_i_o_s_lob_app import ManagedIOSLobApp
        from .managed_i_o_s_store_app import ManagedIOSStoreApp
        from .managed_mobile_app import ManagedMobileApp
        from .managed_mobile_lob_app import ManagedMobileLobApp
        from .managed_tenants.aggregated_policy_compliance import AggregatedPolicyCompliance
        from .managed_tenants.app_performance import AppPerformance
        from .managed_tenants.audit_event import AuditEvent
        from .managed_tenants.cloud_pc_connection import CloudPcConnection
        from .managed_tenants.cloud_pc_device import CloudPcDevice
        from .managed_tenants.cloud_pc_overview import CloudPcOverview
        from .managed_tenants.conditional_access_policy_coverage import ConditionalAccessPolicyCoverage
        from .managed_tenants.credential_user_registrations_summary import CredentialUserRegistrationsSummary
        from .managed_tenants.device_app_performance import DeviceAppPerformance
        from .managed_tenants.device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
        from .managed_tenants.device_health_status import DeviceHealthStatus
        from .managed_tenants.managed_device_compliance import ManagedDeviceCompliance
        from .managed_tenants.managed_device_compliance_trend import ManagedDeviceComplianceTrend
        from .managed_tenants.managed_tenant import ManagedTenant
        from .managed_tenants.managed_tenant_alert import ManagedTenantAlert
        from .managed_tenants.managed_tenant_alert_log import ManagedTenantAlertLog
        from .managed_tenants.managed_tenant_alert_rule import ManagedTenantAlertRule
        from .managed_tenants.managed_tenant_alert_rule_definition import ManagedTenantAlertRuleDefinition
        from .managed_tenants.managed_tenant_api_notification import ManagedTenantApiNotification
        from .managed_tenants.managed_tenant_email_notification import ManagedTenantEmailNotification
        from .managed_tenants.managed_tenant_ticketing_endpoint import ManagedTenantTicketingEndpoint
        from .managed_tenants.management_action import ManagementAction
        from .managed_tenants.management_action_tenant_deployment_status import ManagementActionTenantDeploymentStatus
        from .managed_tenants.management_intent import ManagementIntent
        from .managed_tenants.management_template import ManagementTemplate
        from .managed_tenants.management_template_collection import ManagementTemplateCollection
        from .managed_tenants.management_template_collection_tenant_summary import ManagementTemplateCollectionTenantSummary
        from .managed_tenants.management_template_step import ManagementTemplateStep
        from .managed_tenants.management_template_step_deployment import ManagementTemplateStepDeployment
        from .managed_tenants.management_template_step_tenant_summary import ManagementTemplateStepTenantSummary
        from .managed_tenants.management_template_step_version import ManagementTemplateStepVersion
        from .managed_tenants.tenant import Tenant
        from .managed_tenants.tenant_customized_information import TenantCustomizedInformation
        from .managed_tenants.tenant_detailed_information import TenantDetailedInformation
        from .managed_tenants.tenant_group import TenantGroup
        from .managed_tenants.tenant_tag import TenantTag
        from .managed_tenants.windows_device_malware_state import WindowsDeviceMalwareState
        from .managed_tenants.windows_protection_state import WindowsProtectionState
        from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
        from .mdm_windows_information_protection_policy_policy_set_item import MdmWindowsInformationProtectionPolicyPolicySetItem
        from .meeting_activity_statistics import MeetingActivityStatistics
        from .meeting_attendance_report import MeetingAttendanceReport
        from .meeting_registrant import MeetingRegistrant
        from .meeting_registrant_base import MeetingRegistrantBase
        from .meeting_registration import MeetingRegistration
        from .meeting_registration_base import MeetingRegistrationBase
        from .meeting_registration_question import MeetingRegistrationQuestion
        from .membership_outlier_insight import MembershipOutlierInsight
        from .mention import Mention
        from .message import Message
        from .message_event import MessageEvent
        from .message_recipient import MessageRecipient
        from .message_rule import MessageRule
        from .message_trace import MessageTrace
        from .mfa_completion_metric import MfaCompletionMetric
        from .mfa_failure import MfaFailure
        from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
        from .microsoft_application_data_access_settings import MicrosoftApplicationDataAccessSettings
        from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
        from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration
        from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
        from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
        from .microsoft_store_for_business_contained_app import MicrosoftStoreForBusinessContainedApp
        from .microsoft_tunnel_configuration import MicrosoftTunnelConfiguration
        from .microsoft_tunnel_health_threshold import MicrosoftTunnelHealthThreshold
        from .microsoft_tunnel_server import MicrosoftTunnelServer
        from .microsoft_tunnel_server_log_collection_response import MicrosoftTunnelServerLogCollectionResponse
        from .microsoft_tunnel_site import MicrosoftTunnelSite
        from .mobile_app import MobileApp
        from .mobile_app_assignment import MobileAppAssignment
        from .mobile_app_catalog_package import MobileAppCatalogPackage
        from .mobile_app_category import MobileAppCategory
        from .mobile_app_content import MobileAppContent
        from .mobile_app_content_file import MobileAppContentFile
        from .mobile_app_dependency import MobileAppDependency
        from .mobile_app_install_status import MobileAppInstallStatus
        from .mobile_app_install_summary import MobileAppInstallSummary
        from .mobile_app_intent_and_state import MobileAppIntentAndState
        from .mobile_app_policy_set_item import MobileAppPolicySetItem
        from .mobile_app_provisioning_config_group_assignment import MobileAppProvisioningConfigGroupAssignment
        from .mobile_app_relationship import MobileAppRelationship
        from .mobile_app_supersedence import MobileAppSupersedence
        from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
        from .mobile_contained_app import MobileContainedApp
        from .mobile_lob_app import MobileLobApp
        from .mobile_threat_defense_connector import MobileThreatDefenseConnector
        from .mobility_management_policy import MobilityManagementPolicy
        from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric
        from .monthly_inactive_users_metric import MonthlyInactiveUsersMetric
        from .monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot
        from .multi_tenant_organization import MultiTenantOrganization
        from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate
        from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord
        from .multi_tenant_organization_member import MultiTenantOrganizationMember
        from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .mute_participants_operation import MuteParticipantsOperation
        from .mute_participant_operation import MuteParticipantOperation
        from .named_location import NamedLocation
        from .ndes_connector import NdesConnector
        from .networkaccess.alert import Alert
        from .networkaccess.branch_site import BranchSite
        from .networkaccess.conditional_access_policy import ConditionalAccessPolicy
        from .networkaccess.conditional_access_settings import ConditionalAccessSettings
        from .networkaccess.connectivity import Connectivity
        from .networkaccess.connectivity_configuration_link import ConnectivityConfigurationLink
        from .networkaccess.cross_tenant_access_settings import CrossTenantAccessSettings
        from .networkaccess.device_link import DeviceLink
        from .networkaccess.enriched_audit_logs import EnrichedAuditLogs
        from .networkaccess.filtering_policy import FilteringPolicy
        from .networkaccess.filtering_policy_link import FilteringPolicyLink
        from .networkaccess.filtering_profile import FilteringProfile
        from .networkaccess.filtering_rule import FilteringRule
        from .networkaccess.forwarding_options import ForwardingOptions
        from .networkaccess.forwarding_policy import ForwardingPolicy
        from .networkaccess.forwarding_policy_link import ForwardingPolicyLink
        from .networkaccess.forwarding_profile import ForwardingProfile
        from .networkaccess.forwarding_rule import ForwardingRule
        from .networkaccess.fqdn_filtering_rule import FqdnFilteringRule
        from .networkaccess.internet_access_forwarding_rule import InternetAccessForwardingRule
        from .networkaccess.logs import Logs
        from .networkaccess.m365_forwarding_rule import M365ForwardingRule
        from .networkaccess.network_access_root import NetworkAccessRoot
        from .networkaccess.policy import Policy
        from .networkaccess.policy_link import PolicyLink
        from .networkaccess.policy_rule import PolicyRule
        from .networkaccess.private_access_forwarding_rule import PrivateAccessForwardingRule
        from .networkaccess.profile import Profile
        from .networkaccess.remote_network import RemoteNetwork
        from .networkaccess.remote_network_health_event import RemoteNetworkHealthEvent
        from .networkaccess.reports import Reports
        from .networkaccess.settings import Settings
        from .networkaccess.tenant_status import TenantStatus
        from .networkaccess.web_category_filtering_rule import WebCategoryFilteringRule
        from .news_link_page import NewsLinkPage
        from .note import Note
        from .notebook import Notebook
        from .notification import Notification
        from .notification_message_template import NotificationMessageTemplate
        from .no_mfa_on_role_activation_alert_configuration import NoMfaOnRoleActivationAlertConfiguration
        from .no_mfa_on_role_activation_alert_incident import NoMfaOnRoleActivationAlertIncident
        from .offer_shift_request import OfferShiftRequest
        from .office365_active_user_counts import Office365ActiveUserCounts
        from .office365_active_user_detail import Office365ActiveUserDetail
        from .office365_groups_activity_counts import Office365GroupsActivityCounts
        from .office365_groups_activity_detail import Office365GroupsActivityDetail
        from .office365_groups_activity_file_counts import Office365GroupsActivityFileCounts
        from .office365_groups_activity_group_counts import Office365GroupsActivityGroupCounts
        from .office365_groups_activity_storage import Office365GroupsActivityStorage
        from .office365_services_user_counts import Office365ServicesUserCounts
        from .office_graph_insights import OfficeGraphInsights
        from .office_suite_app import OfficeSuiteApp
        from .onenote import Onenote
        from .onenote_entity_base_model import OnenoteEntityBaseModel
        from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
        from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
        from .onenote_operation import OnenoteOperation
        from .onenote_page import OnenotePage
        from .onenote_resource import OnenoteResource
        from .onenote_section import OnenoteSection
        from .online_meeting import OnlineMeeting
        from .online_meeting_base import OnlineMeetingBase
        from .on_attribute_collection_listener import OnAttributeCollectionListener
        from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
        from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener
        from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
        from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener
        from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
        from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
        from .on_premises_agent import OnPremisesAgent
        from .on_premises_agent_group import OnPremisesAgentGroup
        from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
        from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
        from .on_premises_publishing_profile import OnPremisesPublishingProfile
        from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
        from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
        from .on_user_create_start_listener import OnUserCreateStartListener
        from .open_aws_security_group_finding import OpenAwsSecurityGroupFinding
        from .open_id_connect_identity_provider import OpenIdConnectIdentityProvider
        from .open_id_connect_provider import OpenIdConnectProvider
        from .open_network_azure_security_group_finding import OpenNetworkAzureSecurityGroupFinding
        from .open_shift import OpenShift
        from .open_shift_change_request import OpenShiftChangeRequest
        from .open_type_extension import OpenTypeExtension
        from .operation import Operation
        from .operation_approval_policy import OperationApprovalPolicy
        from .operation_approval_request import OperationApprovalRequest
        from .organization import Organization
        from .organizational_branding import OrganizationalBranding
        from .organizational_branding_localization import OrganizationalBrandingLocalization
        from .organizational_branding_properties import OrganizationalBrandingProperties
        from .organization_settings import OrganizationSettings
        from .org_contact import OrgContact
        from .outlook_category import OutlookCategory
        from .outlook_item import OutlookItem
        from .outlook_task import OutlookTask
        from .outlook_task_folder import OutlookTaskFolder
        from .outlook_task_group import OutlookTaskGroup
        from .outlook_user import OutlookUser
        from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding
        from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding
        from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
        from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding
        from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding
        from .overprovisioned_user_finding import OverprovisionedUserFinding
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .participant import Participant
        from .participant_joining_notification import ParticipantJoiningNotification
        from .participant_left_notification import ParticipantLeftNotification
        from .partners.billing.azure_usage import AzureUsage
        from .partners.billing.billed_reconciliation import BilledReconciliation
        from .partners.billing.billed_usage import BilledUsage
        from .partners.billing.billing import Billing
        from .partners.billing.billing_reconciliation import BillingReconciliation
        from .partners.billing.export_success_operation import ExportSuccessOperation
        from .partners.billing.failed_operation import FailedOperation
        from .partners.billing.manifest import Manifest
        from .partners.billing.operation import Operation
        from .partners.billing.running_operation import RunningOperation
        from .partners.billing.unbilled_usage import UnbilledUsage
        from .partners.partners import Partners
        from .passwordless_microsoft_authenticator_authentication_method import PasswordlessMicrosoftAuthenticatorAuthenticationMethod
        from .password_authentication_method import PasswordAuthenticationMethod
        from .payload import Payload
        from .payload_compatible_assignment_filter import PayloadCompatibleAssignmentFilter
        from .payload_response import PayloadResponse
        from .pending_external_user_profile import PendingExternalUserProfile
        from .people_admin_settings import PeopleAdminSettings
        from .permission import Permission
        from .permissions_analytics import PermissionsAnalytics
        from .permissions_analytics_aggregation import PermissionsAnalyticsAggregation
        from .permissions_creep_index_distribution import PermissionsCreepIndexDistribution
        from .permissions_definition_aws_policy import PermissionsDefinitionAwsPolicy
        from .permissions_definition_azure_role import PermissionsDefinitionAzureRole
        from .permissions_definition_gcp_role import PermissionsDefinitionGcpRole
        from .permissions_management import PermissionsManagement
        from .permissions_request_change import PermissionsRequestChange
        from .permission_grant_condition_set import PermissionGrantConditionSet
        from .permission_grant_policy import PermissionGrantPolicy
        from .person import Person
        from .person_annotation import PersonAnnotation
        from .person_annual_event import PersonAnnualEvent
        from .person_award import PersonAward
        from .person_certification import PersonCertification
        from .person_extension import PersonExtension
        from .person_interest import PersonInterest
        from .person_name import PersonName
        from .person_responsibility import PersonResponsibility
        from .person_website import PersonWebsite
        from .phone_authentication_method import PhoneAuthenticationMethod
        from .pinned_chat_message_info import PinnedChatMessageInfo
        from .place import Place
        from .planner import Planner
        from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
        from .planner_bucket import PlannerBucket
        from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
        from .planner_delta import PlannerDelta
        from .planner_group import PlannerGroup
        from .planner_plan import PlannerPlan
        from .planner_plan_configuration import PlannerPlanConfiguration
        from .planner_plan_configuration_localization import PlannerPlanConfigurationLocalization
        from .planner_plan_details import PlannerPlanDetails
        from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
        from .planner_roster import PlannerRoster
        from .planner_roster_member import PlannerRosterMember
        from .planner_task import PlannerTask
        from .planner_task_configuration import PlannerTaskConfiguration
        from .planner_task_details import PlannerTaskDetails
        from .planner_user import PlannerUser
        from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
        from .play_prompt_operation import PlayPromptOperation
        from .policy_base import PolicyBase
        from .policy_root import PolicyRoot
        from .policy_set import PolicySet
        from .policy_set_assignment import PolicySetAssignment
        from .policy_set_item import PolicySetItem
        from .policy_template import PolicyTemplate
        from .post import Post
        from .presence import Presence
        from .presentation import Presentation
        from .printer import Printer
        from .printer_base import PrinterBase
        from .printer_create_operation import PrinterCreateOperation
        from .printer_share import PrinterShare
        from .print_connector import PrintConnector
        from .print_document import PrintDocument
        from .print_job import PrintJob
        from .print_operation import PrintOperation
        from .print_service import PrintService
        from .print_service_endpoint import PrintServiceEndpoint
        from .print_task import PrintTask
        from .print_task_definition import PrintTaskDefinition
        from .print_task_trigger import PrintTaskTrigger
        from .print_usage import PrintUsage
        from .print_usage_by_printer import PrintUsageByPrinter
        from .print_usage_by_user import PrintUsageByUser
        from .privileged_access import PrivilegedAccess
        from .privileged_access_group import PrivilegedAccessGroup
        from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
        from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
        from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
        from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
        from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
        from .privileged_access_root import PrivilegedAccessRoot
        from .privileged_access_schedule import PrivilegedAccessSchedule
        from .privileged_access_schedule_instance import PrivilegedAccessScheduleInstance
        from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest
        from .privileged_approval import PrivilegedApproval
        from .privileged_operation_event import PrivilegedOperationEvent
        from .privileged_role import PrivilegedRole
        from .privileged_role_assignment import PrivilegedRoleAssignment
        from .privileged_role_assignment_request import PrivilegedRoleAssignmentRequest
        from .privileged_role_settings import PrivilegedRoleSettings
        from .privileged_role_summary import PrivilegedRoleSummary
        from .privileged_signup_status import PrivilegedSignupStatus
        from .privilege_escalation import PrivilegeEscalation
        from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
        from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
        from .privilege_escalation_finding import PrivilegeEscalationFinding
        from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
        from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding
        from .privilege_management_elevation import PrivilegeManagementElevation
        from .privilege_management_elevation_request import PrivilegeManagementElevationRequest
        from .profile import Profile
        from .profile_card_property import ProfileCardProperty
        from .profile_photo import ProfilePhoto
        from .program import Program
        from .program_control import ProgramControl
        from .program_control_type import ProgramControlType
        from .project_participation import ProjectParticipation
        from .pronouns_settings import PronounsSettings
        from .provider_tenant_setting import ProviderTenantSetting
        from .provisioning_object_summary import ProvisioningObjectSummary
        from .published_resource import PublishedResource
        from .purchase_invoice_line import PurchaseInvoiceLine
        from .rbac_application import RbacApplication
        from .rbac_application_multiple import RbacApplicationMultiple
        from .recommendation import Recommendation
        from .recommendation_base import RecommendationBase
        from .record_operation import RecordOperation
        from .recycle_bin import RecycleBin
        from .recycle_bin_item import RecycleBinItem
        from .redundant_assignment_alert_configuration import RedundantAssignmentAlertConfiguration
        from .redundant_assignment_alert_incident import RedundantAssignmentAlertIncident
        from .reference_attachment import ReferenceAttachment
        from .regional_and_language_settings import RegionalAndLanguageSettings
        from .relying_party_detailed_summary import RelyingPartyDetailedSummary
        from .remote_action_audit import RemoteActionAudit
        from .remote_assistance_partner import RemoteAssistancePartner
        from .remote_assistance_settings import RemoteAssistanceSettings
        from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
        from .report_root import ReportRoot
        from .request import Request
        from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship
        from .resource_operation import ResourceOperation
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .restricted_apps_violation import RestrictedAppsViolation
        from .rich_long_running_operation import RichLongRunningOperation
        from .risky_service_principal import RiskyServicePrincipal
        from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
        from .risky_user import RiskyUser
        from .risky_user_history_item import RiskyUserHistoryItem
        from .risk_detection import RiskDetection
        from .roles_assigned_outside_privileged_identity_management_alert_configuration import RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration
        from .roles_assigned_outside_privileged_identity_management_alert_incident import RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident
        from .role_assignment import RoleAssignment
        from .role_definition import RoleDefinition
        from .role_management_alert import RoleManagementAlert
        from .role_scope_tag import RoleScopeTag
        from .role_scope_tag_auto_assignment import RoleScopeTagAutoAssignment
        from .room import Room
        from .room_list import RoomList
        from .sales_credit_memo_line import SalesCreditMemoLine
        from .sales_invoice_line import SalesInvoiceLine
        from .sales_order_line import SalesOrderLine
        from .sales_quote_line import SalesQuoteLine
        from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
        from .saml_or_ws_fed_provider import SamlOrWsFedProvider
        from .schedule import Schedule
        from .scheduled_permissions_request import ScheduledPermissionsRequest
        from .schedule_change_request import ScheduleChangeRequest
        from .scheduling_group import SchedulingGroup
        from .schema import Schema
        from .schema_extension import SchemaExtension
        from .scoped_role_membership import ScopedRoleMembership
        from .search.acronym import Acronym
        from .search.bookmark import Bookmark
        from .search.qna import Qna
        from .search.search_answer import SearchAnswer
        from .search_entity import SearchEntity
        from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding
        from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding
        from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding
        from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding
        from .section_group import SectionGroup
        from .secure_score import SecureScore
        from .secure_score_control_profile import SecureScoreControlProfile
        from .security.alert import Alert
        from .security.analyzed_email import AnalyzedEmail
        from .security.article import Article
        from .security.article_indicator import ArticleIndicator
        from .security.artifact import Artifact
        from .security.audit_core_root import AuditCoreRoot
        from .security.audit_log_query import AuditLogQuery
        from .security.audit_log_record import AuditLogRecord
        from .security.authority_template import AuthorityTemplate
        from .security.case import Case
        from .security.cases_root import CasesRoot
        from .security.case_operation import CaseOperation
        from .security.category_template import CategoryTemplate
        from .security.citation_template import CitationTemplate
        from .security.collaboration_root import CollaborationRoot
        from .security.data_set import DataSet
        from .security.data_source import DataSource
        from .security.data_source_container import DataSourceContainer
        from .security.department_template import DepartmentTemplate
        from .security.detection_rule import DetectionRule
        from .security.disposition_review_stage import DispositionReviewStage
        from .security.ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
        from .security.ediscovery_case import EdiscoveryCase
        from .security.ediscovery_case_settings import EdiscoveryCaseSettings
        from .security.ediscovery_custodian import EdiscoveryCustodian
        from .security.ediscovery_estimate_operation import EdiscoveryEstimateOperation
        from .security.ediscovery_export_operation import EdiscoveryExportOperation
        from .security.ediscovery_file import EdiscoveryFile
        from .security.ediscovery_hold_operation import EdiscoveryHoldOperation
        from .security.ediscovery_hold_policy import EdiscoveryHoldPolicy
        from .security.ediscovery_index_operation import EdiscoveryIndexOperation
        from .security.ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
        from .security.ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
        from .security.ediscovery_review_set import EdiscoveryReviewSet
        from .security.ediscovery_review_set_query import EdiscoveryReviewSetQuery
        from .security.ediscovery_review_tag import EdiscoveryReviewTag
        from .security.ediscovery_search import EdiscoverySearch
        from .security.ediscovery_search_export_operation import EdiscoverySearchExportOperation
        from .security.ediscovery_tag_operation import EdiscoveryTagOperation
        from .security.email_content_threat_submission import EmailContentThreatSubmission
        from .security.email_threat_submission import EmailThreatSubmission
        from .security.email_threat_submission_policy import EmailThreatSubmissionPolicy
        from .security.email_url_threat_submission import EmailUrlThreatSubmission
        from .security.file import File
        from .security.file_content_threat_submission import FileContentThreatSubmission
        from .security.file_plan_descriptor import FilePlanDescriptor
        from .security.file_plan_descriptor_template import FilePlanDescriptorTemplate
        from .security.file_plan_reference_template import FilePlanReferenceTemplate
        from .security.file_threat_submission import FileThreatSubmission
        from .security.file_url_threat_submission import FileUrlThreatSubmission
        from .security.health_issue import HealthIssue
        from .security.host import Host
        from .security.hostname import Hostname
        from .security.host_component import HostComponent
        from .security.host_cookie import HostCookie
        from .security.host_pair import HostPair
        from .security.host_port import HostPort
        from .security.host_reputation import HostReputation
        from .security.host_ssl_certificate import HostSslCertificate
        from .security.host_tracker import HostTracker
        from .security.identity_container import IdentityContainer
        from .security.incident import Incident
        from .security.indicator import Indicator
        from .security.information_protection import InformationProtection
        from .security.information_protection_policy_setting import InformationProtectionPolicySetting
        from .security.intelligence_profile import IntelligenceProfile
        from .security.intelligence_profile_indicator import IntelligenceProfileIndicator
        from .security.ip_address import IpAddress
        from .security.labels_root import LabelsRoot
        from .security.passive_dns_record import PassiveDnsRecord
        from .security.policy_base import PolicyBase
        from .security.protection_rule import ProtectionRule
        from .security.retention_event import RetentionEvent
        from .security.retention_event_type import RetentionEventType
        from .security.retention_label import RetentionLabel
        from .security.rules_root import RulesRoot
        from .security.search import Search
        from .security.security import Security
        from .security.sensitivity_label import SensitivityLabel
        from .security.site_source import SiteSource
        from .security.ssl_certificate import SslCertificate
        from .security.subcategory_template import SubcategoryTemplate
        from .security.subdomain import Subdomain
        from .security.tag import Tag
        from .security.threat_intelligence import ThreatIntelligence
        from .security.threat_submission import ThreatSubmission
        from .security.threat_submission_root import ThreatSubmissionRoot
        from .security.triggers_root import TriggersRoot
        from .security.trigger_types_root import TriggerTypesRoot
        from .security.unclassified_artifact import UnclassifiedArtifact
        from .security.unified_group_source import UnifiedGroupSource
        from .security.url_threat_submission import UrlThreatSubmission
        from .security.user_source import UserSource
        from .security.vulnerability import Vulnerability
        from .security.vulnerability_component import VulnerabilityComponent
        from .security.whois_base_record import WhoisBaseRecord
        from .security.whois_history_record import WhoisHistoryRecord
        from .security.whois_record import WhoisRecord
        from .security_action import SecurityAction
        from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary
        from .security_baseline_device_state import SecurityBaselineDeviceState
        from .security_baseline_setting_state import SecurityBaselineSettingState
        from .security_baseline_state import SecurityBaselineState
        from .security_baseline_state_summary import SecurityBaselineStateSummary
        from .security_baseline_template import SecurityBaselineTemplate
        from .security_configuration_task import SecurityConfigurationTask
        from .security_reports_root import SecurityReportsRoot
        from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
        from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
        from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
        from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding
        from .send_dtmf_tones_operation import SendDtmfTonesOperation
        from .sensitive_type import SensitiveType
        from .sensitivity_label import SensitivityLabel
        from .sensitivity_policy_settings import SensitivityPolicySettings
        from .sequential_activation_renewals_alert_configuration import SequentialActivationRenewalsAlertConfiguration
        from .sequential_activation_renewals_alert_incident import SequentialActivationRenewalsAlertIncident
        from .service_activity import ServiceActivity
        from .service_announcement import ServiceAnnouncement
        from .service_announcement_attachment import ServiceAnnouncementAttachment
        from .service_announcement_base import ServiceAnnouncementBase
        from .service_health import ServiceHealth
        from .service_health_issue import ServiceHealthIssue
        from .service_level_agreement_root import ServiceLevelAgreementRoot
        from .service_now_connection import ServiceNowConnection
        from .service_principal import ServicePrincipal
        from .service_principal_creation_condition_set import ServicePrincipalCreationConditionSet
        from .service_principal_creation_policy import ServicePrincipalCreationPolicy
        from .service_principal_risk_detection import ServicePrincipalRiskDetection
        from .service_principal_sign_in_activity import ServicePrincipalSignInActivity
        from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown
        from .service_update_message import ServiceUpdateMessage
        from .setting_state_device_summary import SettingStateDeviceSummary
        from .shared_drive_item import SharedDriveItem
        from .shared_email_domain import SharedEmailDomain
        from .shared_email_domain_invitation import SharedEmailDomainInvitation
        from .shared_insight import SharedInsight
        from .shared_p_c_configuration import SharedPCConfiguration
        from .shared_with_channel_team_info import SharedWithChannelTeamInfo
        from .sharepoint import Sharepoint
        from .sharepoint_settings import SharepointSettings
        from .shift import Shift
        from .shifts_role_definition import ShiftsRoleDefinition
        from .shift_preferences import ShiftPreferences
        from .sign_in import SignIn
        from .simulation import Simulation
        from .simulation_automation import SimulationAutomation
        from .simulation_automation_run import SimulationAutomationRun
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
        from .site import Site
        from .site_page import SitePage
        from .skill_proficiency import SkillProficiency
        from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
        from .skype_user_conversation_member import SkypeUserConversationMember
        from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration
        from .sms_authentication_method_target import SmsAuthenticationMethodTarget
        from .social_identity_provider import SocialIdentityProvider
        from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
        from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration
        from .software_update_status_summary import SoftwareUpdateStatusSummary
        from .stale_sign_in_alert_configuration import StaleSignInAlertConfiguration
        from .stale_sign_in_alert_incident import StaleSignInAlertIncident
        from .standard_web_part import StandardWebPart
        from .start_hold_music_operation import StartHoldMusicOperation
        from .stop_hold_music_operation import StopHoldMusicOperation
        from .storage_quota_breakdown import StorageQuotaBreakdown
        from .storage_settings import StorageSettings
        from .strong_authentication_detail import StrongAuthenticationDetail
        from .strong_authentication_phone_app_detail import StrongAuthenticationPhoneAppDetail
        from .sts_policy import StsPolicy
        from .subject_rights_request import SubjectRightsRequest
        from .subscribed_sku import SubscribedSku
        from .subscribe_to_tone_operation import SubscribeToToneOperation
        from .subscription import Subscription
        from .super_aws_resource_finding import SuperAwsResourceFinding
        from .super_aws_role_finding import SuperAwsRoleFinding
        from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding
        from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding
        from .super_serverless_function_finding import SuperServerlessFunctionFinding
        from .super_user_finding import SuperUserFinding
        from .swap_shifts_change_request import SwapShiftsChangeRequest
        from .symantec_code_signing_certificate import SymantecCodeSigningCertificate
        from .synchronization import Synchronization
        from .synchronization_job import SynchronizationJob
        from .synchronization_schema import SynchronizationSchema
        from .synchronization_template import SynchronizationTemplate
        from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
        from .targeted_managed_app_configuration_policy_set_item import TargetedManagedAppConfigurationPolicySetItem
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
        from .targeted_managed_app_protection import TargetedManagedAppProtection
        from .target_device_group import TargetDeviceGroup
        from .task_file_attachment import TaskFileAttachment
        from .tax_group import TaxGroup
        from .team import Team
        from .teams_app import TeamsApp
        from .teams_app_dashboard_card_definition import TeamsAppDashboardCardDefinition
        from .teams_app_definition import TeamsAppDefinition
        from .teams_app_icon import TeamsAppIcon
        from .teams_app_installation import TeamsAppInstallation
        from .teams_app_settings import TeamsAppSettings
        from .teams_async_operation import TeamsAsyncOperation
        from .teams_tab import TeamsTab
        from .teams_template import TeamsTemplate
        from .teams_user_configuration.teams_admin_root import TeamsAdminRoot
        from .teams_user_configuration.user_configuration import UserConfiguration
        from .teamwork import Teamwork
        from .teamwork_bot import TeamworkBot
        from .teamwork_device import TeamworkDevice
        from .teamwork_device_activity import TeamworkDeviceActivity
        from .teamwork_device_configuration import TeamworkDeviceConfiguration
        from .teamwork_device_health import TeamworkDeviceHealth
        from .teamwork_device_operation import TeamworkDeviceOperation
        from .teamwork_hosted_content import TeamworkHostedContent
        from .teamwork_peripheral import TeamworkPeripheral
        from .teamwork_tag import TeamworkTag
        from .teamwork_tag_member import TeamworkTagMember
        from .team_info import TeamInfo
        from .team_template import TeamTemplate
        from .team_template_definition import TeamTemplateDefinition
        from .telecom_expense_management_partner import TelecomExpenseManagementPartner
        from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
        from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .tenant_attach_r_b_a_c import TenantAttachRBAC
        from .tenant_relationship_access_policy_base import TenantRelationshipAccessPolicyBase
        from .tenant_setup_info import TenantSetupInfo
        from .terms_and_conditions import TermsAndConditions
        from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
        from .terms_and_conditions_assignment import TermsAndConditionsAssignment
        from .terms_and_conditions_group_assignment import TermsAndConditionsGroupAssignment
        from .terms_of_use_container import TermsOfUseContainer
        from .term_store.group import Group
        from .term_store.relation import Relation
        from .term_store.set import Set
        from .term_store.store import Store
        from .term_store.term import Term
        from .text_classification_request import TextClassificationRequest
        from .text_web_part import TextWebPart
        from .threat_assessment_request import ThreatAssessmentRequest
        from .threat_assessment_result import ThreatAssessmentResult
        from .thumbnail_set import ThumbnailSet
        from .time_card import TimeCard
        from .time_off import TimeOff
        from .time_off_reason import TimeOffReason
        from .time_off_request import TimeOffRequest
        from .ti_indicator import TiIndicator
        from .todo import Todo
        from .todo_task import TodoTask
        from .todo_task_list import TodoTaskList
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .too_many_global_admins_assigned_to_tenant_alert_configuration import TooManyGlobalAdminsAssignedToTenantAlertConfiguration
        from .too_many_global_admins_assigned_to_tenant_alert_incident import TooManyGlobalAdminsAssignedToTenantAlertIncident
        from .training import Training
        from .training_campaign import TrainingCampaign
        from .training_language_detail import TrainingLanguageDetail
        from .trending import Trending
        from .trusted_certificate_authority_as_entity_base import TrustedCertificateAuthorityAsEntityBase
        from .trust_framework_key_set import TrustFrameworkKeySet
        from .trust_framework_policy import TrustFrameworkPolicy
        from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding
        from .unified_rbac_application import UnifiedRbacApplication
        from .unified_rbac_resource_action import UnifiedRbacResourceAction
        from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
        from .unified_rbac_resource_scope import UnifiedRbacResourceScope
        from .unified_role_assignment import UnifiedRoleAssignment
        from .unified_role_assignment_multiple import UnifiedRoleAssignmentMultiple
        from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
        from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
        from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
        from .unified_role_definition import UnifiedRoleDefinition
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
        from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
        from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
        from .unified_role_management_alert import UnifiedRoleManagementAlert
        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration
        from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition
        from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident
        from .unified_role_management_policy import UnifiedRoleManagementPolicy
        from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
        from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment
        from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
        from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
        from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
        from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule
        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule
        from .unified_role_schedule_base import UnifiedRoleScheduleBase
        from .unified_role_schedule_instance_base import UnifiedRoleScheduleInstanceBase
        from .unified_storage_quota import UnifiedStorageQuota
        from .unmanaged_device_discovery_task import UnmanagedDeviceDiscoveryTask
        from .unmute_participant_operation import UnmuteParticipantOperation
        from .unsupported_device_configuration import UnsupportedDeviceConfiguration
        from .unsupported_group_policy_extension import UnsupportedGroupPolicyExtension
        from .update_recording_status_operation import UpdateRecordingStatusOperation
        from .url_assessment_request import UrlAssessmentRequest
        from .usage_right import UsageRight
        from .used_insight import UsedInsight
        from .user import User
        from .user_account_information import UserAccountInformation
        from .user_activity import UserActivity
        from .user_analytics import UserAnalytics
        from .user_app_install_status import UserAppInstallStatus
        from .user_consent_request import UserConsentRequest
        from .user_count_metric import UserCountMetric
        from .user_credential_usage_details import UserCredentialUsageDetails
        from .user_experience_analytics_anomaly import UserExperienceAnalyticsAnomaly
        from .user_experience_analytics_anomaly_correlation_group_overview import UserExperienceAnalyticsAnomalyCorrelationGroupOverview
        from .user_experience_analytics_anomaly_device import UserExperienceAnalyticsAnomalyDevice
        from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance
        from .user_experience_analytics_app_health_app_performance_by_app_version import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion
        from .user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
        from .user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
        from .user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
        from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance
        from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance
        from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails
        from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance
        from .user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
        from .user_experience_analytics_battery_health_app_impact import UserExperienceAnalyticsBatteryHealthAppImpact
        from .user_experience_analytics_battery_health_capacity_details import UserExperienceAnalyticsBatteryHealthCapacityDetails
        from .user_experience_analytics_battery_health_device_app_impact import UserExperienceAnalyticsBatteryHealthDeviceAppImpact
        from .user_experience_analytics_battery_health_device_performance import UserExperienceAnalyticsBatteryHealthDevicePerformance
        from .user_experience_analytics_battery_health_device_runtime_history import UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory
        from .user_experience_analytics_battery_health_model_performance import UserExperienceAnalyticsBatteryHealthModelPerformance
        from .user_experience_analytics_battery_health_os_performance import UserExperienceAnalyticsBatteryHealthOsPerformance
        from .user_experience_analytics_battery_health_runtime_details import UserExperienceAnalyticsBatteryHealthRuntimeDetails
        from .user_experience_analytics_category import UserExperienceAnalyticsCategory
        from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance
        from .user_experience_analytics_device_scope import UserExperienceAnalyticsDeviceScope
        from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores
        from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory
        from .user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess
        from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance
        from .user_experience_analytics_device_timeline_event import UserExperienceAnalyticsDeviceTimelineEvent
        from .user_experience_analytics_device_without_cloud_identity import UserExperienceAnalyticsDeviceWithoutCloudIdentity
        from .user_experience_analytics_impacting_process import UserExperienceAnalyticsImpactingProcess
        from .user_experience_analytics_metric import UserExperienceAnalyticsMetric
        from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
        from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
        from .user_experience_analytics_not_autopilot_ready_device import UserExperienceAnalyticsNotAutopilotReadyDevice
        from .user_experience_analytics_overview import UserExperienceAnalyticsOverview
        from .user_experience_analytics_remote_connection import UserExperienceAnalyticsRemoteConnection
        from .user_experience_analytics_resource_performance import UserExperienceAnalyticsResourcePerformance
        from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
        from .user_experience_analytics_work_from_anywhere_device import UserExperienceAnalyticsWorkFromAnywhereDevice
        from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
        from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
        from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
        from .user_flow_language_configuration import UserFlowLanguageConfiguration
        from .user_flow_language_page import UserFlowLanguagePage
        from .user_insights_root import UserInsightsRoot
        from .user_insights_settings import UserInsightsSettings
        from .user_install_state_summary import UserInstallStateSummary
        from .user_p_f_x_certificate import UserPFXCertificate
        from .user_registration_details import UserRegistrationDetails
        from .user_requests_metric import UserRequestsMetric
        from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation
        from .user_security_profile import UserSecurityProfile
        from .user_settings import UserSettings
        from .user_sign_in_insight import UserSignInInsight
        from .user_sign_up_metric import UserSignUpMetric
        from .user_storage import UserStorage
        from .user_teamwork import UserTeamwork
        from .user_virtual_events_root import UserVirtualEventsRoot
        from .vertical_section import VerticalSection
        from .video_news_link_page import VideoNewsLinkPage
        from .virtual_endpoint import VirtualEndpoint
        from .virtual_event import VirtualEvent
        from .virtual_events_root import VirtualEventsRoot
        from .virtual_event_presenter import VirtualEventPresenter
        from .virtual_event_registration import VirtualEventRegistration
        from .virtual_event_registration_configuration import VirtualEventRegistrationConfiguration
        from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion
        from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion
        from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase
        from .virtual_event_session import VirtualEventSession
        from .virtual_event_townhall import VirtualEventTownhall
        from .virtual_event_webinar import VirtualEventWebinar
        from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration
        from .virtual_machine_details import VirtualMachineDetails
        from .virtual_machine_with_aws_storage_bucket_access_finding import VirtualMachineWithAwsStorageBucketAccessFinding
        from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration
        from .voice_authentication_method_target import VoiceAuthenticationMethodTarget
        from .vpn_configuration import VpnConfiguration
        from .vpp_token import VppToken
        from .vulnerable_managed_device import VulnerableManagedDevice
        from .web_account import WebAccount
        from .web_app import WebApp
        from .web_application_segment import WebApplicationSegment
        from .web_part import WebPart
        from .win32_catalog_app import Win32CatalogApp
        from .win32_lob_app import Win32LobApp
        from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage
        from .windows10_certificate_profile_base import Windows10CertificateProfileBase
        from .windows10_compliance_policy import Windows10CompliancePolicy
        from .windows10_custom_configuration import Windows10CustomConfiguration
        from .windows10_device_firmware_configuration_interface import Windows10DeviceFirmwareConfigurationInterface
        from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
        from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
        from .windows10_enrollment_completion_page_configuration import Windows10EnrollmentCompletionPageConfiguration
        from .windows10_enrollment_completion_page_configuration_policy_set_item import Windows10EnrollmentCompletionPageConfigurationPolicySetItem
        from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
        from .windows10_general_configuration import Windows10GeneralConfiguration
        from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
        from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
        from .windows10_network_boundary_configuration import Windows10NetworkBoundaryConfiguration
        from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
        from .windows10_p_f_x_import_certificate_profile import Windows10PFXImportCertificateProfile
        from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
        from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
        from .windows10_vpn_configuration import Windows10VpnConfiguration
        from .windows10_x_certificate_profile import Windows10XCertificateProfile
        from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile
        from .windows10_x_trusted_root_certificate import Windows10XTrustedRootCertificate
        from .windows10_x_vpn_configuration import Windows10XVpnConfiguration
        from .windows10_x_wifi_configuration import Windows10XWifiConfiguration
        from .windows81_certificate_profile_base import Windows81CertificateProfileBase
        from .windows81_compliance_policy import Windows81CompliancePolicy
        from .windows81_general_configuration import Windows81GeneralConfiguration
        from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
        from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
        from .windows81_vpn_configuration import Windows81VpnConfiguration
        from .windows81_wifi_import_configuration import Windows81WifiImportConfiguration
        from .windows_app_x import WindowsAppX
        from .windows_assigned_access_profile import WindowsAssignedAccessProfile
        from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
        from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment
        from .windows_autopilot_deployment_profile_policy_set_item import WindowsAutopilotDeploymentProfilePolicySetItem
        from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
        from .windows_autopilot_settings import WindowsAutopilotSettings
        from .windows_certificate_profile_base import WindowsCertificateProfileBase
        from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
        from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy
        from .windows_defender_application_control_supplemental_policy_assignment import WindowsDefenderApplicationControlSupplementalPolicyAssignment
        from .windows_defender_application_control_supplemental_policy_deployment_status import WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus
        from .windows_defender_application_control_supplemental_policy_deployment_summary import WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary
        from .windows_delivery_optimization_configuration import WindowsDeliveryOptimizationConfiguration
        from .windows_device_malware_state import WindowsDeviceMalwareState
        from .windows_domain_join_configuration import WindowsDomainJoinConfiguration
        from .windows_driver_update_inventory import WindowsDriverUpdateInventory
        from .windows_driver_update_profile import WindowsDriverUpdateProfile
        from .windows_driver_update_profile_assignment import WindowsDriverUpdateProfileAssignment
        from .windows_feature_update_catalog_item import WindowsFeatureUpdateCatalogItem
        from .windows_feature_update_profile import WindowsFeatureUpdateProfile
        from .windows_feature_update_profile_assignment import WindowsFeatureUpdateProfileAssignment
        from .windows_health_monitoring_configuration import WindowsHealthMonitoringConfiguration
        from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod
        from .windows_identity_protection_configuration import WindowsIdentityProtectionConfiguration
        from .windows_information_protection import WindowsInformationProtection
        from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
        from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
        from .windows_information_protection_device_registration import WindowsInformationProtectionDeviceRegistration
        from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
        from .windows_information_protection_policy import WindowsInformationProtectionPolicy
        from .windows_information_protection_wipe_action import WindowsInformationProtectionWipeAction
        from .windows_kiosk_configuration import WindowsKioskConfiguration
        from .windows_malware_information import WindowsMalwareInformation
        from .windows_managed_app_protection import WindowsManagedAppProtection
        from .windows_managed_app_registration import WindowsManagedAppRegistration
        from .windows_managed_device import WindowsManagedDevice
        from .windows_management_app import WindowsManagementApp
        from .windows_management_app_health_state import WindowsManagementAppHealthState
        from .windows_management_app_health_summary import WindowsManagementAppHealthSummary
        from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
        from .windows_mobile_m_s_i import WindowsMobileMSI
        from .windows_phone81_app_x import WindowsPhone81AppX
        from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle
        from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase
        from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy
        from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
        from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
        from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
        from .windows_phone81_store_app import WindowsPhone81StoreApp
        from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile
        from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate
        from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration
        from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration
        from .windows_phone_x_a_p import WindowsPhoneXAP
        from .windows_privacy_data_access_control_item import WindowsPrivacyDataAccessControlItem
        from .windows_protection_state import WindowsProtectionState
        from .windows_quality_update_catalog_item import WindowsQualityUpdateCatalogItem
        from .windows_quality_update_profile import WindowsQualityUpdateProfile
        from .windows_quality_update_profile_assignment import WindowsQualityUpdateProfileAssignment
        from .windows_setting import WindowsSetting
        from .windows_setting_instance import WindowsSettingInstance
        from .windows_store_app import WindowsStoreApp
        from .windows_universal_app_x import WindowsUniversalAppX
        from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp
        from .windows_updates.azure_a_d_device import AzureADDevice
        from .windows_updates.catalog import Catalog
        from .windows_updates.catalog_entry import CatalogEntry
        from .windows_updates.compliance_change import ComplianceChange
        from .windows_updates.content_approval import ContentApproval
        from .windows_updates.deployment import Deployment
        from .windows_updates.deployment_audience import DeploymentAudience
        from .windows_updates.driver_update_catalog_entry import DriverUpdateCatalogEntry
        from .windows_updates.edition import Edition
        from .windows_updates.feature_update_catalog_entry import FeatureUpdateCatalogEntry
        from .windows_updates.knowledge_base_article import KnowledgeBaseArticle
        from .windows_updates.known_issue import KnownIssue
        from .windows_updates.operational_insights_connection import OperationalInsightsConnection
        from .windows_updates.product import Product
        from .windows_updates.product_revision import ProductRevision
        from .windows_updates.quality_update_catalog_entry import QualityUpdateCatalogEntry
        from .windows_updates.resource_connection import ResourceConnection
        from .windows_updates.software_update_catalog_entry import SoftwareUpdateCatalogEntry
        from .windows_updates.updatable_asset import UpdatableAsset
        from .windows_updates.updatable_asset_group import UpdatableAssetGroup
        from .windows_updates.update_policy import UpdatePolicy
        from .windows_update_catalog_item import WindowsUpdateCatalogItem
        from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
        from .windows_update_state import WindowsUpdateState
        from .windows_vpn_configuration import WindowsVpnConfiguration
        from .windows_web_app import WindowsWebApp
        from .windows_wifi_configuration import WindowsWifiConfiguration
        from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
        from .windows_wired_network_configuration import WindowsWiredNetworkConfiguration
        from .win_get_app import WinGetApp
        from .workbook import Workbook
        from .workbook_application import WorkbookApplication
        from .workbook_chart import WorkbookChart
        from .workbook_chart_area_format import WorkbookChartAreaFormat
        from .workbook_chart_axes import WorkbookChartAxes
        from .workbook_chart_axis import WorkbookChartAxis
        from .workbook_chart_axis_format import WorkbookChartAxisFormat
        from .workbook_chart_axis_title import WorkbookChartAxisTitle
        from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat
        from .workbook_chart_data_labels import WorkbookChartDataLabels
        from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat
        from .workbook_chart_fill import WorkbookChartFill
        from .workbook_chart_font import WorkbookChartFont
        from .workbook_chart_gridlines import WorkbookChartGridlines
        from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat
        from .workbook_chart_legend import WorkbookChartLegend
        from .workbook_chart_legend_format import WorkbookChartLegendFormat
        from .workbook_chart_line_format import WorkbookChartLineFormat
        from .workbook_chart_point import WorkbookChartPoint
        from .workbook_chart_point_format import WorkbookChartPointFormat
        from .workbook_chart_series import WorkbookChartSeries
        from .workbook_chart_series_format import WorkbookChartSeriesFormat
        from .workbook_chart_title import WorkbookChartTitle
        from .workbook_chart_title_format import WorkbookChartTitleFormat
        from .workbook_comment import WorkbookComment
        from .workbook_comment_reply import WorkbookCommentReply
        from .workbook_document_task import WorkbookDocumentTask
        from .workbook_document_task_change import WorkbookDocumentTaskChange
        from .workbook_filter import WorkbookFilter
        from .workbook_format_protection import WorkbookFormatProtection
        from .workbook_functions import WorkbookFunctions
        from .workbook_function_result import WorkbookFunctionResult
        from .workbook_named_item import WorkbookNamedItem
        from .workbook_operation import WorkbookOperation
        from .workbook_pivot_table import WorkbookPivotTable
        from .workbook_range import WorkbookRange
        from .workbook_range_border import WorkbookRangeBorder
        from .workbook_range_fill import WorkbookRangeFill
        from .workbook_range_font import WorkbookRangeFont
        from .workbook_range_format import WorkbookRangeFormat
        from .workbook_range_sort import WorkbookRangeSort
        from .workbook_range_view import WorkbookRangeView
        from .workbook_table import WorkbookTable
        from .workbook_table_column import WorkbookTableColumn
        from .workbook_table_row import WorkbookTableRow
        from .workbook_table_sort import WorkbookTableSort
        from .workbook_worksheet import WorkbookWorksheet
        from .workbook_worksheet_protection import WorkbookWorksheetProtection
        from .workforce_integration import WorkforceIntegration
        from .workplace_sensor_device import WorkplaceSensorDevice
        from .workspace import Workspace
        from .work_position import WorkPosition
        from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration
        from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration
        from .zebra_fota_artifact import ZebraFotaArtifact
        from .zebra_fota_connector import ZebraFotaConnector
        from .zebra_fota_deployment import ZebraFotaDeployment

        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

