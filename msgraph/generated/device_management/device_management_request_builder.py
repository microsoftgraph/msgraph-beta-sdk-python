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
    from ..models.device_management import device_management
    from ..models.o_data_errors import o_data_error
    from .advanced_threat_protection_onboarding_state_summary import advanced_threat_protection_onboarding_state_summary_request_builder
    from .android_device_owner_enrollment_profiles import android_device_owner_enrollment_profiles_request_builder
    from .android_device_owner_enrollment_profiles.item import android_device_owner_enrollment_profile_item_request_builder
    from .android_for_work_app_configuration_schemas import android_for_work_app_configuration_schemas_request_builder
    from .android_for_work_app_configuration_schemas.item import android_for_work_app_configuration_schema_item_request_builder
    from .android_for_work_enrollment_profiles import android_for_work_enrollment_profiles_request_builder
    from .android_for_work_enrollment_profiles.item import android_for_work_enrollment_profile_item_request_builder
    from .android_for_work_settings import android_for_work_settings_request_builder
    from .android_managed_store_account_enterprise_settings import android_managed_store_account_enterprise_settings_request_builder
    from .android_managed_store_app_configuration_schemas import android_managed_store_app_configuration_schemas_request_builder
    from .android_managed_store_app_configuration_schemas.item import android_managed_store_app_configuration_schema_item_request_builder
    from .apple_push_notification_certificate import apple_push_notification_certificate_request_builder
    from .apple_user_initiated_enrollment_profiles import apple_user_initiated_enrollment_profiles_request_builder
    from .apple_user_initiated_enrollment_profiles.item import apple_user_initiated_enrollment_profile_item_request_builder
    from .assignment_filters import assignment_filters_request_builder
    from .assignment_filters.item import device_and_app_management_assignment_filter_item_request_builder
    from .audit_events import audit_events_request_builder
    from .audit_events.item import audit_event_item_request_builder
    from .autopilot_events import autopilot_events_request_builder
    from .autopilot_events.item import device_management_autopilot_event_item_request_builder
    from .cart_to_class_associations import cart_to_class_associations_request_builder
    from .cart_to_class_associations.item import cart_to_class_association_item_request_builder
    from .categories import categories_request_builder
    from .categories.item import device_management_setting_category_item_request_builder
    from .certificate_connector_details import certificate_connector_details_request_builder
    from .certificate_connector_details.item import certificate_connector_details_item_request_builder
    from .chrome_o_s_onboarding_settings import chrome_o_s_onboarding_settings_request_builder
    from .chrome_o_s_onboarding_settings.item import chrome_o_s_onboarding_settings_item_request_builder
    from .cloud_p_c_connectivity_issues import cloud_p_c_connectivity_issues_request_builder
    from .cloud_p_c_connectivity_issues.item import cloud_p_c_connectivity_issue_item_request_builder
    from .comanaged_devices import comanaged_devices_request_builder
    from .comanaged_devices.item import managed_device_item_request_builder
    from .comanagement_eligible_devices import comanagement_eligible_devices_request_builder
    from .comanagement_eligible_devices.item import comanagement_eligible_device_item_request_builder
    from .compliance_categories import compliance_categories_request_builder
    from .compliance_categories.item import device_management_configuration_category_item_request_builder
    from .compliance_management_partners import compliance_management_partners_request_builder
    from .compliance_management_partners.item import compliance_management_partner_item_request_builder
    from .compliance_policies import compliance_policies_request_builder
    from .compliance_policies.item import device_management_compliance_policy_item_request_builder
    from .compliance_settings import compliance_settings_request_builder
    from .compliance_settings.item import device_management_configuration_setting_definition_item_request_builder
    from .conditional_access_settings import conditional_access_settings_request_builder
    from .config_manager_collections import config_manager_collections_request_builder
    from .config_manager_collections.item import config_manager_collection_item_request_builder
    from .configuration_categories import configuration_categories_request_builder
    from .configuration_categories.item import device_management_configuration_category_item_request_builder
    from .configuration_policies import configuration_policies_request_builder
    from .configuration_policies.item import device_management_configuration_policy_item_request_builder
    from .configuration_policy_templates import configuration_policy_templates_request_builder
    from .configuration_policy_templates.item import device_management_configuration_policy_template_item_request_builder
    from .configuration_settings import configuration_settings_request_builder
    from .configuration_settings.item import device_management_configuration_setting_definition_item_request_builder
    from .data_sharing_consents import data_sharing_consents_request_builder
    from .data_sharing_consents.item import data_sharing_consent_item_request_builder
    from .dep_onboarding_settings import dep_onboarding_settings_request_builder
    from .dep_onboarding_settings.item import dep_onboarding_setting_item_request_builder
    from .derived_credentials import derived_credentials_request_builder
    from .derived_credentials.item import device_management_derived_credential_settings_item_request_builder
    from .detected_apps import detected_apps_request_builder
    from .detected_apps.item import detected_app_item_request_builder
    from .device_categories import device_categories_request_builder
    from .device_categories.item import device_category_item_request_builder
    from .device_compliance_policies import device_compliance_policies_request_builder
    from .device_compliance_policies.item import device_compliance_policy_item_request_builder
    from .device_compliance_policy_device_state_summary import device_compliance_policy_device_state_summary_request_builder
    from .device_compliance_policy_setting_state_summaries import device_compliance_policy_setting_state_summaries_request_builder
    from .device_compliance_policy_setting_state_summaries.item import device_compliance_policy_setting_state_summary_item_request_builder
    from .device_compliance_scripts import device_compliance_scripts_request_builder
    from .device_compliance_scripts.item import device_compliance_script_item_request_builder
    from .device_configuration_conflict_summary import device_configuration_conflict_summary_request_builder
    from .device_configuration_conflict_summary.item import device_configuration_conflict_summary_item_request_builder
    from .device_configuration_device_state_summaries import device_configuration_device_state_summaries_request_builder
    from .device_configuration_restricted_apps_violations import device_configuration_restricted_apps_violations_request_builder
    from .device_configuration_restricted_apps_violations.item import restricted_apps_violation_item_request_builder
    from .device_configurations import device_configurations_request_builder
    from .device_configurations.item import device_configuration_item_request_builder
    from .device_configurations_all_managed_device_certificate_states import device_configurations_all_managed_device_certificate_states_request_builder
    from .device_configurations_all_managed_device_certificate_states.item import managed_all_device_certificate_state_item_request_builder
    from .device_configuration_user_state_summaries import device_configuration_user_state_summaries_request_builder
    from .device_custom_attribute_shell_scripts import device_custom_attribute_shell_scripts_request_builder
    from .device_custom_attribute_shell_scripts.item import device_custom_attribute_shell_script_item_request_builder
    from .device_enrollment_configurations import device_enrollment_configurations_request_builder
    from .device_enrollment_configurations.item import device_enrollment_configuration_item_request_builder
    from .device_health_scripts import device_health_scripts_request_builder
    from .device_health_scripts.item import device_health_script_item_request_builder
    from .device_management_partners import device_management_partners_request_builder
    from .device_management_partners.item import device_management_partner_item_request_builder
    from .device_management_scripts import device_management_scripts_request_builder
    from .device_management_scripts.item import device_management_script_item_request_builder
    from .device_shell_scripts import device_shell_scripts_request_builder
    from .device_shell_scripts.item import device_shell_script_item_request_builder
    from .domain_join_connectors import domain_join_connectors_request_builder
    from .domain_join_connectors.item import device_management_domain_join_connector_item_request_builder
    from .embedded_s_i_m_activation_code_pools import embedded_s_i_m_activation_code_pools_request_builder
    from .embedded_s_i_m_activation_code_pools.item import embedded_s_i_m_activation_code_pool_item_request_builder
    from .enable_android_device_administrator_enrollment import enable_android_device_administrator_enrollment_request_builder
    from .enable_legacy_pc_management import enable_legacy_pc_management_request_builder
    from .enable_unlicensed_adminstrators import enable_unlicensed_adminstrators_request_builder
    from .evaluate_assignment_filter import evaluate_assignment_filter_request_builder
    from .exchange_connectors import exchange_connectors_request_builder
    from .exchange_connectors.item import device_management_exchange_connector_item_request_builder
    from .exchange_on_premises_policies import exchange_on_premises_policies_request_builder
    from .exchange_on_premises_policies.item import device_management_exchange_on_premises_policy_item_request_builder
    from .exchange_on_premises_policy import exchange_on_premises_policy_request_builder
    from .get_assigned_role_details import get_assigned_role_details_request_builder
    from .get_assignment_filters_status_details import get_assignment_filters_status_details_request_builder
    from .get_comanaged_devices_summary import get_comanaged_devices_summary_request_builder
    from .get_comanagement_eligible_devices_summary import get_comanagement_eligible_devices_summary_request_builder
    from .get_effective_permissions import get_effective_permissions_request_builder
    from .get_effective_permissions_with_scope import get_effective_permissions_with_scope_request_builder
    from .get_role_scope_tags_by_ids_with_ids import get_role_scope_tags_by_ids_with_ids_request_builder
    from .get_role_scope_tags_by_resource_with_resource import get_role_scope_tags_by_resource_with_resource_request_builder
    from .get_suggested_enrollment_limit_with_enrollment_type import get_suggested_enrollment_limit_with_enrollment_type_request_builder
    from .group_policy_categories import group_policy_categories_request_builder
    from .group_policy_categories.item import group_policy_category_item_request_builder
    from .group_policy_configurations import group_policy_configurations_request_builder
    from .group_policy_configurations.item import group_policy_configuration_item_request_builder
    from .group_policy_definition_files import group_policy_definition_files_request_builder
    from .group_policy_definition_files.item import group_policy_definition_file_item_request_builder
    from .group_policy_definitions import group_policy_definitions_request_builder
    from .group_policy_definitions.item import group_policy_definition_item_request_builder
    from .group_policy_migration_reports import group_policy_migration_reports_request_builder
    from .group_policy_migration_reports.item import group_policy_migration_report_item_request_builder
    from .group_policy_object_files import group_policy_object_files_request_builder
    from .group_policy_object_files.item import group_policy_object_file_item_request_builder
    from .group_policy_uploaded_definition_files import group_policy_uploaded_definition_files_request_builder
    from .group_policy_uploaded_definition_files.item import group_policy_uploaded_definition_file_item_request_builder
    from .imported_device_identities import imported_device_identities_request_builder
    from .imported_device_identities.item import imported_device_identity_item_request_builder
    from .imported_windows_autopilot_device_identities import imported_windows_autopilot_device_identities_request_builder
    from .imported_windows_autopilot_device_identities.item import imported_windows_autopilot_device_identity_item_request_builder
    from .intents import intents_request_builder
    from .intents.item import device_management_intent_item_request_builder
    from .intune_branding_profiles import intune_branding_profiles_request_builder
    from .intune_branding_profiles.item import intune_branding_profile_item_request_builder
    from .ios_update_statuses import ios_update_statuses_request_builder
    from .ios_update_statuses.item import ios_update_device_status_item_request_builder
    from .mac_o_s_software_update_account_summaries import mac_o_s_software_update_account_summaries_request_builder
    from .mac_o_s_software_update_account_summaries.item import mac_o_s_software_update_account_summary_item_request_builder
    from .managed_device_encryption_states import managed_device_encryption_states_request_builder
    from .managed_device_encryption_states.item import managed_device_encryption_state_item_request_builder
    from .managed_device_overview import managed_device_overview_request_builder
    from .managed_devices import managed_devices_request_builder
    from .managed_devices.item import managed_device_item_request_builder
    from .microsoft_tunnel_configurations import microsoft_tunnel_configurations_request_builder
    from .microsoft_tunnel_configurations.item import microsoft_tunnel_configuration_item_request_builder
    from .microsoft_tunnel_health_thresholds import microsoft_tunnel_health_thresholds_request_builder
    from .microsoft_tunnel_health_thresholds.item import microsoft_tunnel_health_threshold_item_request_builder
    from .microsoft_tunnel_server_log_collection_responses import microsoft_tunnel_server_log_collection_responses_request_builder
    from .microsoft_tunnel_server_log_collection_responses.item import microsoft_tunnel_server_log_collection_response_item_request_builder
    from .microsoft_tunnel_sites import microsoft_tunnel_sites_request_builder
    from .microsoft_tunnel_sites.item import microsoft_tunnel_site_item_request_builder
    from .mobile_app_troubleshooting_events import mobile_app_troubleshooting_events_request_builder
    from .mobile_app_troubleshooting_events.item import mobile_app_troubleshooting_event_item_request_builder
    from .mobile_threat_defense_connectors import mobile_threat_defense_connectors_request_builder
    from .mobile_threat_defense_connectors.item import mobile_threat_defense_connector_item_request_builder
    from .monitoring import monitoring_request_builder
    from .ndes_connectors import ndes_connectors_request_builder
    from .ndes_connectors.item import ndes_connector_item_request_builder
    from .notification_message_templates import notification_message_templates_request_builder
    from .notification_message_templates.item import notification_message_template_item_request_builder
    from .oem_warranty_information_onboarding import oem_warranty_information_onboarding_request_builder
    from .oem_warranty_information_onboarding.item import oem_warranty_information_onboarding_item_request_builder
    from .privilege_management_elevations import privilege_management_elevations_request_builder
    from .privilege_management_elevations.item import privilege_management_elevation_item_request_builder
    from .remote_action_audits import remote_action_audits_request_builder
    from .remote_action_audits.item import remote_action_audit_item_request_builder
    from .remote_assistance_partners import remote_assistance_partners_request_builder
    from .remote_assistance_partners.item import remote_assistance_partner_item_request_builder
    from .remote_assistance_settings import remote_assistance_settings_request_builder
    from .reports import reports_request_builder
    from .resource_access_profiles import resource_access_profiles_request_builder
    from .resource_access_profiles.item import device_management_resource_access_profile_base_item_request_builder
    from .resource_operations import resource_operations_request_builder
    from .resource_operations.item import resource_operation_item_request_builder
    from .reusable_policy_settings import reusable_policy_settings_request_builder
    from .reusable_policy_settings.item import device_management_reusable_policy_setting_item_request_builder
    from .reusable_settings import reusable_settings_request_builder
    from .reusable_settings.item import device_management_configuration_setting_definition_item_request_builder
    from .role_assignments import role_assignments_request_builder
    from .role_assignments.item import device_and_app_management_role_assignment_item_request_builder
    from .role_definitions import role_definitions_request_builder
    from .role_definitions.item import role_definition_item_request_builder
    from .role_scope_tags import role_scope_tags_request_builder
    from .role_scope_tags.item import role_scope_tag_item_request_builder
    from .scoped_for_resource_with_resource import scoped_for_resource_with_resource_request_builder
    from .send_custom_notification_to_company_portal import send_custom_notification_to_company_portal_request_builder
    from .service_now_connections import service_now_connections_request_builder
    from .service_now_connections.item import service_now_connection_item_request_builder
    from .setting_definitions import setting_definitions_request_builder
    from .setting_definitions.item import device_management_setting_definition_item_request_builder
    from .software_update_status_summary import software_update_status_summary_request_builder
    from .telecom_expense_management_partners import telecom_expense_management_partners_request_builder
    from .telecom_expense_management_partners.item import telecom_expense_management_partner_item_request_builder
    from .templates import templates_request_builder
    from .templates.item import device_management_template_item_request_builder
    from .template_settings import template_settings_request_builder
    from .template_settings.item import device_management_configuration_setting_template_item_request_builder
    from .tenant_attach_r_b_a_c import tenant_attach_r_b_a_c_request_builder
    from .terms_and_conditions import terms_and_conditions_request_builder
    from .terms_and_conditions.item import terms_and_conditions_item_request_builder
    from .troubleshooting_events import troubleshooting_events_request_builder
    from .troubleshooting_events.item import device_management_troubleshooting_event_item_request_builder
    from .user_experience_analytics_anomaly import user_experience_analytics_anomaly_request_builder
    from .user_experience_analytics_anomaly.item import user_experience_analytics_anomaly_item_request_builder
    from .user_experience_analytics_anomaly_device import user_experience_analytics_anomaly_device_request_builder
    from .user_experience_analytics_anomaly_device.item import user_experience_analytics_anomaly_device_item_request_builder
    from .user_experience_analytics_app_health_application_performance import user_experience_analytics_app_health_application_performance_request_builder
    from .user_experience_analytics_app_health_application_performance.item import user_experience_analytics_app_health_application_performance_item_request_builder
    from .user_experience_analytics_app_health_application_performance_by_app_version import user_experience_analytics_app_health_application_performance_by_app_version_request_builder
    from .user_experience_analytics_app_health_application_performance_by_app_version.item import user_experience_analytics_app_health_app_performance_by_app_version_item_request_builder
    from .user_experience_analytics_app_health_application_performance_by_app_version_details import user_experience_analytics_app_health_application_performance_by_app_version_details_request_builder
    from .user_experience_analytics_app_health_application_performance_by_app_version_details.item import user_experience_analytics_app_health_app_performance_by_app_version_details_item_request_builder
    from .user_experience_analytics_app_health_application_performance_by_app_version_device_id import user_experience_analytics_app_health_application_performance_by_app_version_device_id_request_builder
    from .user_experience_analytics_app_health_application_performance_by_app_version_device_id.item import user_experience_analytics_app_health_app_performance_by_app_version_device_id_item_request_builder
    from .user_experience_analytics_app_health_application_performance_by_o_s_version import user_experience_analytics_app_health_application_performance_by_o_s_version_request_builder
    from .user_experience_analytics_app_health_application_performance_by_o_s_version.item import user_experience_analytics_app_health_app_performance_by_o_s_version_item_request_builder
    from .user_experience_analytics_app_health_device_model_performance import user_experience_analytics_app_health_device_model_performance_request_builder
    from .user_experience_analytics_app_health_device_model_performance.item import user_experience_analytics_app_health_device_model_performance_item_request_builder
    from .user_experience_analytics_app_health_device_performance import user_experience_analytics_app_health_device_performance_request_builder
    from .user_experience_analytics_app_health_device_performance.item import user_experience_analytics_app_health_device_performance_item_request_builder
    from .user_experience_analytics_app_health_device_performance_details import user_experience_analytics_app_health_device_performance_details_request_builder
    from .user_experience_analytics_app_health_device_performance_details.item import user_experience_analytics_app_health_device_performance_details_item_request_builder
    from .user_experience_analytics_app_health_o_s_version_performance import user_experience_analytics_app_health_o_s_version_performance_request_builder
    from .user_experience_analytics_app_health_o_s_version_performance.item import user_experience_analytics_app_health_o_s_version_performance_item_request_builder
    from .user_experience_analytics_app_health_overview import user_experience_analytics_app_health_overview_request_builder
    from .user_experience_analytics_baselines import user_experience_analytics_baselines_request_builder
    from .user_experience_analytics_baselines.item import user_experience_analytics_baseline_item_request_builder
    from .user_experience_analytics_battery_health_app_impact import user_experience_analytics_battery_health_app_impact_request_builder
    from .user_experience_analytics_battery_health_app_impact.item import user_experience_analytics_battery_health_app_impact_item_request_builder
    from .user_experience_analytics_battery_health_capacity_details import user_experience_analytics_battery_health_capacity_details_request_builder
    from .user_experience_analytics_battery_health_device_app_impact import user_experience_analytics_battery_health_device_app_impact_request_builder
    from .user_experience_analytics_battery_health_device_app_impact.item import user_experience_analytics_battery_health_device_app_impact_item_request_builder
    from .user_experience_analytics_battery_health_device_performance import user_experience_analytics_battery_health_device_performance_request_builder
    from .user_experience_analytics_battery_health_device_performance.item import user_experience_analytics_battery_health_device_performance_item_request_builder
    from .user_experience_analytics_battery_health_device_runtime_history import user_experience_analytics_battery_health_device_runtime_history_request_builder
    from .user_experience_analytics_battery_health_device_runtime_history.item import user_experience_analytics_battery_health_device_runtime_history_item_request_builder
    from .user_experience_analytics_battery_health_model_performance import user_experience_analytics_battery_health_model_performance_request_builder
    from .user_experience_analytics_battery_health_model_performance.item import user_experience_analytics_battery_health_model_performance_item_request_builder
    from .user_experience_analytics_battery_health_os_performance import user_experience_analytics_battery_health_os_performance_request_builder
    from .user_experience_analytics_battery_health_os_performance.item import user_experience_analytics_battery_health_os_performance_item_request_builder
    from .user_experience_analytics_battery_health_runtime_details import user_experience_analytics_battery_health_runtime_details_request_builder
    from .user_experience_analytics_categories import user_experience_analytics_categories_request_builder
    from .user_experience_analytics_categories.item import user_experience_analytics_category_item_request_builder
    from .user_experience_analytics_device_metric_history import user_experience_analytics_device_metric_history_request_builder
    from .user_experience_analytics_device_metric_history.item import user_experience_analytics_metric_history_item_request_builder
    from .user_experience_analytics_device_performance import user_experience_analytics_device_performance_request_builder
    from .user_experience_analytics_device_performance.item import user_experience_analytics_device_performance_item_request_builder
    from .user_experience_analytics_device_scope import user_experience_analytics_device_scope_request_builder
    from .user_experience_analytics_device_scopes import user_experience_analytics_device_scopes_request_builder
    from .user_experience_analytics_device_scopes.item import user_experience_analytics_device_scope_item_request_builder
    from .user_experience_analytics_device_scores import user_experience_analytics_device_scores_request_builder
    from .user_experience_analytics_device_scores.item import user_experience_analytics_device_scores_item_request_builder
    from .user_experience_analytics_device_startup_history import user_experience_analytics_device_startup_history_request_builder
    from .user_experience_analytics_device_startup_history.item import user_experience_analytics_device_startup_history_item_request_builder
    from .user_experience_analytics_device_startup_processes import user_experience_analytics_device_startup_processes_request_builder
    from .user_experience_analytics_device_startup_processes.item import user_experience_analytics_device_startup_process_item_request_builder
    from .user_experience_analytics_device_startup_process_performance import user_experience_analytics_device_startup_process_performance_request_builder
    from .user_experience_analytics_device_startup_process_performance.item import user_experience_analytics_device_startup_process_performance_item_request_builder
    from .user_experience_analytics_devices_without_cloud_identity import user_experience_analytics_devices_without_cloud_identity_request_builder
    from .user_experience_analytics_devices_without_cloud_identity.item import user_experience_analytics_device_without_cloud_identity_item_request_builder
    from .user_experience_analytics_device_timeline_event import user_experience_analytics_device_timeline_event_request_builder
    from .user_experience_analytics_device_timeline_event.item import user_experience_analytics_device_timeline_event_item_request_builder
    from .user_experience_analytics_impacting_process import user_experience_analytics_impacting_process_request_builder
    from .user_experience_analytics_impacting_process.item import user_experience_analytics_impacting_process_item_request_builder
    from .user_experience_analytics_metric_history import user_experience_analytics_metric_history_request_builder
    from .user_experience_analytics_metric_history.item import user_experience_analytics_metric_history_item_request_builder
    from .user_experience_analytics_model_scores import user_experience_analytics_model_scores_request_builder
    from .user_experience_analytics_model_scores.item import user_experience_analytics_model_scores_item_request_builder
    from .user_experience_analytics_not_autopilot_ready_device import user_experience_analytics_not_autopilot_ready_device_request_builder
    from .user_experience_analytics_not_autopilot_ready_device.item import user_experience_analytics_not_autopilot_ready_device_item_request_builder
    from .user_experience_analytics_overview import user_experience_analytics_overview_request_builder
    from .user_experience_analytics_remote_connection import user_experience_analytics_remote_connection_request_builder
    from .user_experience_analytics_remote_connection.item import user_experience_analytics_remote_connection_item_request_builder
    from .user_experience_analytics_resource_performance import user_experience_analytics_resource_performance_request_builder
    from .user_experience_analytics_resource_performance.item import user_experience_analytics_resource_performance_item_request_builder
    from .user_experience_analytics_score_history import user_experience_analytics_score_history_request_builder
    from .user_experience_analytics_score_history.item import user_experience_analytics_score_history_item_request_builder
    from .user_experience_analytics_summarized_device_scopes import user_experience_analytics_summarized_device_scopes_request_builder
    from .user_experience_analytics_summarize_work_from_anywhere_devices import user_experience_analytics_summarize_work_from_anywhere_devices_request_builder
    from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import user_experience_analytics_work_from_anywhere_hardware_readiness_metric_request_builder
    from .user_experience_analytics_work_from_anywhere_metrics import user_experience_analytics_work_from_anywhere_metrics_request_builder
    from .user_experience_analytics_work_from_anywhere_metrics.item import user_experience_analytics_work_from_anywhere_metric_item_request_builder
    from .user_experience_analytics_work_from_anywhere_model_performance import user_experience_analytics_work_from_anywhere_model_performance_request_builder
    from .user_experience_analytics_work_from_anywhere_model_performance.item import user_experience_analytics_work_from_anywhere_model_performance_item_request_builder
    from .user_pfx_certificates import user_pfx_certificates_request_builder
    from .user_pfx_certificates.item import user_p_f_x_certificate_item_request_builder
    from .verify_windows_enrollment_auto_discovery_with_domain_name import verify_windows_enrollment_auto_discovery_with_domain_name_request_builder
    from .virtual_endpoint import virtual_endpoint_request_builder
    from .windows_autopilot_deployment_profiles import windows_autopilot_deployment_profiles_request_builder
    from .windows_autopilot_deployment_profiles.item import windows_autopilot_deployment_profile_item_request_builder
    from .windows_autopilot_device_identities import windows_autopilot_device_identities_request_builder
    from .windows_autopilot_device_identities.item import windows_autopilot_device_identity_item_request_builder
    from .windows_autopilot_settings import windows_autopilot_settings_request_builder
    from .windows_driver_update_profiles import windows_driver_update_profiles_request_builder
    from .windows_driver_update_profiles.item import windows_driver_update_profile_item_request_builder
    from .windows_feature_update_profiles import windows_feature_update_profiles_request_builder
    from .windows_feature_update_profiles.item import windows_feature_update_profile_item_request_builder
    from .windows_information_protection_app_learning_summaries import windows_information_protection_app_learning_summaries_request_builder
    from .windows_information_protection_app_learning_summaries.item import windows_information_protection_app_learning_summary_item_request_builder
    from .windows_information_protection_network_learning_summaries import windows_information_protection_network_learning_summaries_request_builder
    from .windows_information_protection_network_learning_summaries.item import windows_information_protection_network_learning_summary_item_request_builder
    from .windows_malware_information import windows_malware_information_request_builder
    from .windows_malware_information.item import windows_malware_information_item_request_builder
    from .windows_quality_update_profiles import windows_quality_update_profiles_request_builder
    from .windows_quality_update_profiles.item import windows_quality_update_profile_item_request_builder
    from .windows_update_catalog_items import windows_update_catalog_items_request_builder
    from .windows_update_catalog_items.item import windows_update_catalog_item_item_request_builder
    from .zebra_fota_artifacts import zebra_fota_artifacts_request_builder
    from .zebra_fota_artifacts.item import zebra_fota_artifact_item_request_builder
    from .zebra_fota_connector import zebra_fota_connector_request_builder
    from .zebra_fota_deployments import zebra_fota_deployments_request_builder
    from .zebra_fota_deployments.item import zebra_fota_deployment_item_request_builder

class DeviceManagementRequestBuilder():
    """
    Provides operations to manage the deviceManagement singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceManagementRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def android_device_owner_enrollment_profiles_by_id(self,id: str) -> android_device_owner_enrollment_profile_item_request_builder.AndroidDeviceOwnerEnrollmentProfileItemRequestBuilder:
        """
        Provides operations to manage the androidDeviceOwnerEnrollmentProfiles property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: android_device_owner_enrollment_profile_item_request_builder.AndroidDeviceOwnerEnrollmentProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .android_device_owner_enrollment_profiles.item import android_device_owner_enrollment_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["androidDeviceOwnerEnrollmentProfile%2Did"] = id
        return android_device_owner_enrollment_profile_item_request_builder.AndroidDeviceOwnerEnrollmentProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def android_for_work_app_configuration_schemas_by_id(self,id: str) -> android_for_work_app_configuration_schema_item_request_builder.AndroidForWorkAppConfigurationSchemaItemRequestBuilder:
        """
        Provides operations to manage the androidForWorkAppConfigurationSchemas property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: android_for_work_app_configuration_schema_item_request_builder.AndroidForWorkAppConfigurationSchemaItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .android_for_work_app_configuration_schemas.item import android_for_work_app_configuration_schema_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["androidForWorkAppConfigurationSchema%2Did"] = id
        return android_for_work_app_configuration_schema_item_request_builder.AndroidForWorkAppConfigurationSchemaItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def android_for_work_enrollment_profiles_by_id(self,id: str) -> android_for_work_enrollment_profile_item_request_builder.AndroidForWorkEnrollmentProfileItemRequestBuilder:
        """
        Provides operations to manage the androidForWorkEnrollmentProfiles property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: android_for_work_enrollment_profile_item_request_builder.AndroidForWorkEnrollmentProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .android_for_work_enrollment_profiles.item import android_for_work_enrollment_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["androidForWorkEnrollmentProfile%2Did"] = id
        return android_for_work_enrollment_profile_item_request_builder.AndroidForWorkEnrollmentProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def android_managed_store_app_configuration_schemas_by_id(self,id: str) -> android_managed_store_app_configuration_schema_item_request_builder.AndroidManagedStoreAppConfigurationSchemaItemRequestBuilder:
        """
        Provides operations to manage the androidManagedStoreAppConfigurationSchemas property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: android_managed_store_app_configuration_schema_item_request_builder.AndroidManagedStoreAppConfigurationSchemaItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .android_managed_store_app_configuration_schemas.item import android_managed_store_app_configuration_schema_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["androidManagedStoreAppConfigurationSchema%2Did"] = id
        return android_managed_store_app_configuration_schema_item_request_builder.AndroidManagedStoreAppConfigurationSchemaItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def apple_user_initiated_enrollment_profiles_by_id(self,id: str) -> apple_user_initiated_enrollment_profile_item_request_builder.AppleUserInitiatedEnrollmentProfileItemRequestBuilder:
        """
        Provides operations to manage the appleUserInitiatedEnrollmentProfiles property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: apple_user_initiated_enrollment_profile_item_request_builder.AppleUserInitiatedEnrollmentProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .apple_user_initiated_enrollment_profiles.item import apple_user_initiated_enrollment_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["appleUserInitiatedEnrollmentProfile%2Did"] = id
        return apple_user_initiated_enrollment_profile_item_request_builder.AppleUserInitiatedEnrollmentProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def assignment_filters_by_id(self,id: str) -> device_and_app_management_assignment_filter_item_request_builder.DeviceAndAppManagementAssignmentFilterItemRequestBuilder:
        """
        Provides operations to manage the assignmentFilters property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_and_app_management_assignment_filter_item_request_builder.DeviceAndAppManagementAssignmentFilterItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .assignment_filters.item import device_and_app_management_assignment_filter_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceAndAppManagementAssignmentFilter%2Did"] = id
        return device_and_app_management_assignment_filter_item_request_builder.DeviceAndAppManagementAssignmentFilterItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def audit_events_by_id(self,id: str) -> audit_event_item_request_builder.AuditEventItemRequestBuilder:
        """
        Provides operations to manage the auditEvents property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: audit_event_item_request_builder.AuditEventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .audit_events.item import audit_event_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["auditEvent%2Did"] = id
        return audit_event_item_request_builder.AuditEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def autopilot_events_by_id(self,id: str) -> device_management_autopilot_event_item_request_builder.DeviceManagementAutopilotEventItemRequestBuilder:
        """
        Provides operations to manage the autopilotEvents property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_autopilot_event_item_request_builder.DeviceManagementAutopilotEventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .autopilot_events.item import device_management_autopilot_event_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementAutopilotEvent%2Did"] = id
        return device_management_autopilot_event_item_request_builder.DeviceManagementAutopilotEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def cart_to_class_associations_by_id(self,id: str) -> cart_to_class_association_item_request_builder.CartToClassAssociationItemRequestBuilder:
        """
        Provides operations to manage the cartToClassAssociations property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: cart_to_class_association_item_request_builder.CartToClassAssociationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .cart_to_class_associations.item import cart_to_class_association_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cartToClassAssociation%2Did"] = id
        return cart_to_class_association_item_request_builder.CartToClassAssociationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def categories_by_id(self,id: str) -> device_management_setting_category_item_request_builder.DeviceManagementSettingCategoryItemRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_setting_category_item_request_builder.DeviceManagementSettingCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .categories.item import device_management_setting_category_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementSettingCategory%2Did"] = id
        return device_management_setting_category_item_request_builder.DeviceManagementSettingCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def certificate_connector_details_by_id(self,id: str) -> certificate_connector_details_item_request_builder.CertificateConnectorDetailsItemRequestBuilder:
        """
        Provides operations to manage the certificateConnectorDetails property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: certificate_connector_details_item_request_builder.CertificateConnectorDetailsItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .certificate_connector_details.item import certificate_connector_details_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["certificateConnectorDetails%2Did"] = id
        return certificate_connector_details_item_request_builder.CertificateConnectorDetailsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def chrome_o_s_onboarding_settings_by_id(self,id: str) -> chrome_o_s_onboarding_settings_item_request_builder.ChromeOSOnboardingSettingsItemRequestBuilder:
        """
        Provides operations to manage the chromeOSOnboardingSettings property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: chrome_o_s_onboarding_settings_item_request_builder.ChromeOSOnboardingSettingsItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .chrome_o_s_onboarding_settings.item import chrome_o_s_onboarding_settings_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["chromeOSOnboardingSettings%2Did"] = id
        return chrome_o_s_onboarding_settings_item_request_builder.ChromeOSOnboardingSettingsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def cloud_p_c_connectivity_issues_by_id(self,id: str) -> cloud_p_c_connectivity_issue_item_request_builder.CloudPCConnectivityIssueItemRequestBuilder:
        """
        Provides operations to manage the cloudPCConnectivityIssues property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_p_c_connectivity_issue_item_request_builder.CloudPCConnectivityIssueItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .cloud_p_c_connectivity_issues.item import cloud_p_c_connectivity_issue_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPCConnectivityIssue%2Did"] = id
        return cloud_p_c_connectivity_issue_item_request_builder.CloudPCConnectivityIssueItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def comanaged_devices_by_id(self,id: str) -> managed_device_item_request_builder.ManagedDeviceItemRequestBuilder:
        """
        Provides operations to manage the comanagedDevices property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_device_item_request_builder.ManagedDeviceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .comanaged_devices.item import managed_device_item_request_builder
        from .managed_devices.item import managed_device_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDevice%2Did"] = id
        return managed_device_item_request_builder.ManagedDeviceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def comanagement_eligible_devices_by_id(self,id: str) -> comanagement_eligible_device_item_request_builder.ComanagementEligibleDeviceItemRequestBuilder:
        """
        Provides operations to manage the comanagementEligibleDevices property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: comanagement_eligible_device_item_request_builder.ComanagementEligibleDeviceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .comanagement_eligible_devices.item import comanagement_eligible_device_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["comanagementEligibleDevice%2Did"] = id
        return comanagement_eligible_device_item_request_builder.ComanagementEligibleDeviceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def compliance_categories_by_id(self,id: str) -> device_management_configuration_category_item_request_builder.DeviceManagementConfigurationCategoryItemRequestBuilder:
        """
        Provides operations to manage the complianceCategories property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_configuration_category_item_request_builder.DeviceManagementConfigurationCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .compliance_categories.item import device_management_configuration_category_item_request_builder
        from .configuration_categories.item import device_management_configuration_category_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementConfigurationCategory%2Did"] = id
        return device_management_configuration_category_item_request_builder.DeviceManagementConfigurationCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def compliance_management_partners_by_id(self,id: str) -> compliance_management_partner_item_request_builder.ComplianceManagementPartnerItemRequestBuilder:
        """
        Provides operations to manage the complianceManagementPartners property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: compliance_management_partner_item_request_builder.ComplianceManagementPartnerItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .compliance_management_partners.item import compliance_management_partner_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["complianceManagementPartner%2Did"] = id
        return compliance_management_partner_item_request_builder.ComplianceManagementPartnerItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def compliance_policies_by_id(self,id: str) -> device_management_compliance_policy_item_request_builder.DeviceManagementCompliancePolicyItemRequestBuilder:
        """
        Provides operations to manage the compliancePolicies property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_compliance_policy_item_request_builder.DeviceManagementCompliancePolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .compliance_policies.item import device_management_compliance_policy_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementCompliancePolicy%2Did"] = id
        return device_management_compliance_policy_item_request_builder.DeviceManagementCompliancePolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def compliance_settings_by_id(self,id: str) -> device_management_configuration_setting_definition_item_request_builder.DeviceManagementConfigurationSettingDefinitionItemRequestBuilder:
        """
        Provides operations to manage the complianceSettings property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_configuration_setting_definition_item_request_builder.DeviceManagementConfigurationSettingDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .compliance_settings.item import device_management_configuration_setting_definition_item_request_builder
        from .configuration_settings.item import device_management_configuration_setting_definition_item_request_builder
        from .reusable_settings.item import device_management_configuration_setting_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementConfigurationSettingDefinition%2Did"] = id
        return device_management_configuration_setting_definition_item_request_builder.DeviceManagementConfigurationSettingDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def config_manager_collections_by_id(self,id: str) -> config_manager_collection_item_request_builder.ConfigManagerCollectionItemRequestBuilder:
        """
        Provides operations to manage the configManagerCollections property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: config_manager_collection_item_request_builder.ConfigManagerCollectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .config_manager_collections.item import config_manager_collection_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["configManagerCollection%2Did"] = id
        return config_manager_collection_item_request_builder.ConfigManagerCollectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def configuration_categories_by_id(self,id: str) -> device_management_configuration_category_item_request_builder.DeviceManagementConfigurationCategoryItemRequestBuilder:
        """
        Provides operations to manage the configurationCategories property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_configuration_category_item_request_builder.DeviceManagementConfigurationCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .compliance_categories.item import device_management_configuration_category_item_request_builder
        from .configuration_categories.item import device_management_configuration_category_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementConfigurationCategory%2Did"] = id
        return device_management_configuration_category_item_request_builder.DeviceManagementConfigurationCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def configuration_policies_by_id(self,id: str) -> device_management_configuration_policy_item_request_builder.DeviceManagementConfigurationPolicyItemRequestBuilder:
        """
        Provides operations to manage the configurationPolicies property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_configuration_policy_item_request_builder.DeviceManagementConfigurationPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .configuration_policies.item import device_management_configuration_policy_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementConfigurationPolicy%2Did"] = id
        return device_management_configuration_policy_item_request_builder.DeviceManagementConfigurationPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def configuration_policy_templates_by_id(self,id: str) -> device_management_configuration_policy_template_item_request_builder.DeviceManagementConfigurationPolicyTemplateItemRequestBuilder:
        """
        Provides operations to manage the configurationPolicyTemplates property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_configuration_policy_template_item_request_builder.DeviceManagementConfigurationPolicyTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .configuration_policy_templates.item import device_management_configuration_policy_template_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementConfigurationPolicyTemplate%2Did"] = id
        return device_management_configuration_policy_template_item_request_builder.DeviceManagementConfigurationPolicyTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def configuration_settings_by_id(self,id: str) -> device_management_configuration_setting_definition_item_request_builder.DeviceManagementConfigurationSettingDefinitionItemRequestBuilder:
        """
        Provides operations to manage the configurationSettings property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_configuration_setting_definition_item_request_builder.DeviceManagementConfigurationSettingDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .compliance_settings.item import device_management_configuration_setting_definition_item_request_builder
        from .configuration_settings.item import device_management_configuration_setting_definition_item_request_builder
        from .reusable_settings.item import device_management_configuration_setting_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementConfigurationSettingDefinition%2Did"] = id
        return device_management_configuration_setting_definition_item_request_builder.DeviceManagementConfigurationSettingDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def data_sharing_consents_by_id(self,id: str) -> data_sharing_consent_item_request_builder.DataSharingConsentItemRequestBuilder:
        """
        Provides operations to manage the dataSharingConsents property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: data_sharing_consent_item_request_builder.DataSharingConsentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .data_sharing_consents.item import data_sharing_consent_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["dataSharingConsent%2Did"] = id
        return data_sharing_consent_item_request_builder.DataSharingConsentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def dep_onboarding_settings_by_id(self,id: str) -> dep_onboarding_setting_item_request_builder.DepOnboardingSettingItemRequestBuilder:
        """
        Provides operations to manage the depOnboardingSettings property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: dep_onboarding_setting_item_request_builder.DepOnboardingSettingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .dep_onboarding_settings.item import dep_onboarding_setting_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["depOnboardingSetting%2Did"] = id
        return dep_onboarding_setting_item_request_builder.DepOnboardingSettingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def derived_credentials_by_id(self,id: str) -> device_management_derived_credential_settings_item_request_builder.DeviceManagementDerivedCredentialSettingsItemRequestBuilder:
        """
        Provides operations to manage the derivedCredentials property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_derived_credential_settings_item_request_builder.DeviceManagementDerivedCredentialSettingsItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .derived_credentials.item import device_management_derived_credential_settings_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementDerivedCredentialSettings%2Did"] = id
        return device_management_derived_credential_settings_item_request_builder.DeviceManagementDerivedCredentialSettingsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def detected_apps_by_id(self,id: str) -> detected_app_item_request_builder.DetectedAppItemRequestBuilder:
        """
        Provides operations to manage the detectedApps property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: detected_app_item_request_builder.DetectedAppItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .detected_apps.item import detected_app_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["detectedApp%2Did"] = id
        return detected_app_item_request_builder.DetectedAppItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_categories_by_id(self,id: str) -> device_category_item_request_builder.DeviceCategoryItemRequestBuilder:
        """
        Provides operations to manage the deviceCategories property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_category_item_request_builder.DeviceCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_categories.item import device_category_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceCategory%2Did"] = id
        return device_category_item_request_builder.DeviceCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_compliance_policies_by_id(self,id: str) -> device_compliance_policy_item_request_builder.DeviceCompliancePolicyItemRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicies property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_compliance_policy_item_request_builder.DeviceCompliancePolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_compliance_policies.item import device_compliance_policy_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceCompliancePolicy%2Did"] = id
        return device_compliance_policy_item_request_builder.DeviceCompliancePolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_compliance_policy_setting_state_summaries_by_id(self,id: str) -> device_compliance_policy_setting_state_summary_item_request_builder.DeviceCompliancePolicySettingStateSummaryItemRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicySettingStateSummaries property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_compliance_policy_setting_state_summary_item_request_builder.DeviceCompliancePolicySettingStateSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_compliance_policy_setting_state_summaries.item import device_compliance_policy_setting_state_summary_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceCompliancePolicySettingStateSummary%2Did"] = id
        return device_compliance_policy_setting_state_summary_item_request_builder.DeviceCompliancePolicySettingStateSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_compliance_scripts_by_id(self,id: str) -> device_compliance_script_item_request_builder.DeviceComplianceScriptItemRequestBuilder:
        """
        Provides operations to manage the deviceComplianceScripts property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_compliance_script_item_request_builder.DeviceComplianceScriptItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_compliance_scripts.item import device_compliance_script_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceComplianceScript%2Did"] = id
        return device_compliance_script_item_request_builder.DeviceComplianceScriptItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_configuration_conflict_summary_by_id(self,id: str) -> device_configuration_conflict_summary_item_request_builder.DeviceConfigurationConflictSummaryItemRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationConflictSummary property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_configuration_conflict_summary_item_request_builder.DeviceConfigurationConflictSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_configuration_conflict_summary.item import device_configuration_conflict_summary_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceConfigurationConflictSummary%2Did"] = id
        return device_configuration_conflict_summary_item_request_builder.DeviceConfigurationConflictSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_configuration_restricted_apps_violations_by_id(self,id: str) -> restricted_apps_violation_item_request_builder.RestrictedAppsViolationItemRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationRestrictedAppsViolations property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: restricted_apps_violation_item_request_builder.RestrictedAppsViolationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_configuration_restricted_apps_violations.item import restricted_apps_violation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["restrictedAppsViolation%2Did"] = id
        return restricted_apps_violation_item_request_builder.RestrictedAppsViolationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_configurations_by_id(self,id: str) -> device_configuration_item_request_builder.DeviceConfigurationItemRequestBuilder:
        """
        Provides operations to manage the deviceConfigurations property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_configuration_item_request_builder.DeviceConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_configurations.item import device_configuration_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceConfiguration%2Did"] = id
        return device_configuration_item_request_builder.DeviceConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_configurations_all_managed_device_certificate_states_by_id(self,id: str) -> managed_all_device_certificate_state_item_request_builder.ManagedAllDeviceCertificateStateItemRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationsAllManagedDeviceCertificateStates property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_all_device_certificate_state_item_request_builder.ManagedAllDeviceCertificateStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_configurations_all_managed_device_certificate_states.item import managed_all_device_certificate_state_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedAllDeviceCertificateState%2Did"] = id
        return managed_all_device_certificate_state_item_request_builder.ManagedAllDeviceCertificateStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_custom_attribute_shell_scripts_by_id(self,id: str) -> device_custom_attribute_shell_script_item_request_builder.DeviceCustomAttributeShellScriptItemRequestBuilder:
        """
        Provides operations to manage the deviceCustomAttributeShellScripts property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_custom_attribute_shell_script_item_request_builder.DeviceCustomAttributeShellScriptItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_custom_attribute_shell_scripts.item import device_custom_attribute_shell_script_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceCustomAttributeShellScript%2Did"] = id
        return device_custom_attribute_shell_script_item_request_builder.DeviceCustomAttributeShellScriptItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_enrollment_configurations_by_id(self,id: str) -> device_enrollment_configuration_item_request_builder.DeviceEnrollmentConfigurationItemRequestBuilder:
        """
        Provides operations to manage the deviceEnrollmentConfigurations property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_enrollment_configuration_item_request_builder.DeviceEnrollmentConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_enrollment_configurations.item import device_enrollment_configuration_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceEnrollmentConfiguration%2Did"] = id
        return device_enrollment_configuration_item_request_builder.DeviceEnrollmentConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_health_scripts_by_id(self,id: str) -> device_health_script_item_request_builder.DeviceHealthScriptItemRequestBuilder:
        """
        Provides operations to manage the deviceHealthScripts property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_health_script_item_request_builder.DeviceHealthScriptItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_health_scripts.item import device_health_script_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceHealthScript%2Did"] = id
        return device_health_script_item_request_builder.DeviceHealthScriptItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_management_partners_by_id(self,id: str) -> device_management_partner_item_request_builder.DeviceManagementPartnerItemRequestBuilder:
        """
        Provides operations to manage the deviceManagementPartners property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_partner_item_request_builder.DeviceManagementPartnerItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_management_partners.item import device_management_partner_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementPartner%2Did"] = id
        return device_management_partner_item_request_builder.DeviceManagementPartnerItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_management_scripts_by_id(self,id: str) -> device_management_script_item_request_builder.DeviceManagementScriptItemRequestBuilder:
        """
        Provides operations to manage the deviceManagementScripts property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_script_item_request_builder.DeviceManagementScriptItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_management_scripts.item import device_management_script_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementScript%2Did"] = id
        return device_management_script_item_request_builder.DeviceManagementScriptItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_shell_scripts_by_id(self,id: str) -> device_shell_script_item_request_builder.DeviceShellScriptItemRequestBuilder:
        """
        Provides operations to manage the deviceShellScripts property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_shell_script_item_request_builder.DeviceShellScriptItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_shell_scripts.item import device_shell_script_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceShellScript%2Did"] = id
        return device_shell_script_item_request_builder.DeviceShellScriptItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def domain_join_connectors_by_id(self,id: str) -> device_management_domain_join_connector_item_request_builder.DeviceManagementDomainJoinConnectorItemRequestBuilder:
        """
        Provides operations to manage the domainJoinConnectors property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_domain_join_connector_item_request_builder.DeviceManagementDomainJoinConnectorItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .domain_join_connectors.item import device_management_domain_join_connector_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementDomainJoinConnector%2Did"] = id
        return device_management_domain_join_connector_item_request_builder.DeviceManagementDomainJoinConnectorItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def embedded_s_i_m_activation_code_pools_by_id(self,id: str) -> embedded_s_i_m_activation_code_pool_item_request_builder.EmbeddedSIMActivationCodePoolItemRequestBuilder:
        """
        Provides operations to manage the embeddedSIMActivationCodePools property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: embedded_s_i_m_activation_code_pool_item_request_builder.EmbeddedSIMActivationCodePoolItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .embedded_s_i_m_activation_code_pools.item import embedded_s_i_m_activation_code_pool_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["embeddedSIMActivationCodePool%2Did"] = id
        return embedded_s_i_m_activation_code_pool_item_request_builder.EmbeddedSIMActivationCodePoolItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def exchange_connectors_by_id(self,id: str) -> device_management_exchange_connector_item_request_builder.DeviceManagementExchangeConnectorItemRequestBuilder:
        """
        Provides operations to manage the exchangeConnectors property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_exchange_connector_item_request_builder.DeviceManagementExchangeConnectorItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .exchange_connectors.item import device_management_exchange_connector_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementExchangeConnector%2Did"] = id
        return device_management_exchange_connector_item_request_builder.DeviceManagementExchangeConnectorItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def exchange_on_premises_policies_by_id(self,id: str) -> device_management_exchange_on_premises_policy_item_request_builder.DeviceManagementExchangeOnPremisesPolicyItemRequestBuilder:
        """
        Provides operations to manage the exchangeOnPremisesPolicies property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_exchange_on_premises_policy_item_request_builder.DeviceManagementExchangeOnPremisesPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .exchange_on_premises_policies.item import device_management_exchange_on_premises_policy_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementExchangeOnPremisesPolicy%2Did"] = id
        return device_management_exchange_on_premises_policy_item_request_builder.DeviceManagementExchangeOnPremisesPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DeviceManagementRequestBuilderGetRequestConfiguration] = None) -> Optional[device_management.DeviceManagement]:
        """
        Get deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management.DeviceManagement]
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
        from ..models.device_management import device_management

        return await self.request_adapter.send_async(request_info, device_management.DeviceManagement, error_mapping)
    
    def get_effective_permissions_with_scope(self,scope: Optional[str] = None) -> get_effective_permissions_with_scope_request_builder.GetEffectivePermissionsWithScopeRequestBuilder:
        """
        Provides operations to call the getEffectivePermissions method.
        Args:
            scope: Usage: scope='{scope}'
        Returns: get_effective_permissions_with_scope_request_builder.GetEffectivePermissionsWithScopeRequestBuilder
        """
        if scope is None:
            raise Exception("scope cannot be undefined")
        from .get_effective_permissions_with_scope import get_effective_permissions_with_scope_request_builder

        return get_effective_permissions_with_scope_request_builder.GetEffectivePermissionsWithScopeRequestBuilder(self.request_adapter, self.path_parameters, scope)
    
    def get_role_scope_tags_by_ids_with_ids(self,ids: Optional[str] = None) -> get_role_scope_tags_by_ids_with_ids_request_builder.GetRoleScopeTagsByIdsWithIdsRequestBuilder:
        """
        Provides operations to call the getRoleScopeTagsByIds method.
        Args:
            ids: Usage: ids={ids}
        Returns: get_role_scope_tags_by_ids_with_ids_request_builder.GetRoleScopeTagsByIdsWithIdsRequestBuilder
        """
        if ids is None:
            raise Exception("ids cannot be undefined")
        from .get_role_scope_tags_by_ids_with_ids import get_role_scope_tags_by_ids_with_ids_request_builder

        return get_role_scope_tags_by_ids_with_ids_request_builder.GetRoleScopeTagsByIdsWithIdsRequestBuilder(self.request_adapter, self.path_parameters, ids)
    
    def get_role_scope_tags_by_resource_with_resource(self,resource: Optional[str] = None) -> get_role_scope_tags_by_resource_with_resource_request_builder.GetRoleScopeTagsByResourceWithResourceRequestBuilder:
        """
        Provides operations to call the getRoleScopeTagsByResource method.
        Args:
            resource: Usage: resource='{resource}'
        Returns: get_role_scope_tags_by_resource_with_resource_request_builder.GetRoleScopeTagsByResourceWithResourceRequestBuilder
        """
        if resource is None:
            raise Exception("resource cannot be undefined")
        from .get_role_scope_tags_by_resource_with_resource import get_role_scope_tags_by_resource_with_resource_request_builder

        return get_role_scope_tags_by_resource_with_resource_request_builder.GetRoleScopeTagsByResourceWithResourceRequestBuilder(self.request_adapter, self.path_parameters, resource)
    
    def get_suggested_enrollment_limit_with_enrollment_type(self,enrollment_type: Optional[str] = None) -> get_suggested_enrollment_limit_with_enrollment_type_request_builder.GetSuggestedEnrollmentLimitWithEnrollmentTypeRequestBuilder:
        """
        Provides operations to call the getSuggestedEnrollmentLimit method.
        Args:
            enrollmentType: Usage: enrollmentType='{enrollmentType}'
        Returns: get_suggested_enrollment_limit_with_enrollment_type_request_builder.GetSuggestedEnrollmentLimitWithEnrollmentTypeRequestBuilder
        """
        if enrollment_type is None:
            raise Exception("enrollment_type cannot be undefined")
        from .get_suggested_enrollment_limit_with_enrollment_type import get_suggested_enrollment_limit_with_enrollment_type_request_builder

        return get_suggested_enrollment_limit_with_enrollment_type_request_builder.GetSuggestedEnrollmentLimitWithEnrollmentTypeRequestBuilder(self.request_adapter, self.path_parameters, enrollment_type)
    
    def group_policy_categories_by_id(self,id: str) -> group_policy_category_item_request_builder.GroupPolicyCategoryItemRequestBuilder:
        """
        Provides operations to manage the groupPolicyCategories property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: group_policy_category_item_request_builder.GroupPolicyCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .group_policy_categories.item import group_policy_category_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupPolicyCategory%2Did"] = id
        return group_policy_category_item_request_builder.GroupPolicyCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def group_policy_configurations_by_id(self,id: str) -> group_policy_configuration_item_request_builder.GroupPolicyConfigurationItemRequestBuilder:
        """
        Provides operations to manage the groupPolicyConfigurations property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: group_policy_configuration_item_request_builder.GroupPolicyConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .group_policy_configurations.item import group_policy_configuration_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupPolicyConfiguration%2Did"] = id
        return group_policy_configuration_item_request_builder.GroupPolicyConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def group_policy_definition_files_by_id(self,id: str) -> group_policy_definition_file_item_request_builder.GroupPolicyDefinitionFileItemRequestBuilder:
        """
        Provides operations to manage the groupPolicyDefinitionFiles property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: group_policy_definition_file_item_request_builder.GroupPolicyDefinitionFileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .group_policy_definition_files.item import group_policy_definition_file_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupPolicyDefinitionFile%2Did"] = id
        return group_policy_definition_file_item_request_builder.GroupPolicyDefinitionFileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def group_policy_definitions_by_id(self,id: str) -> group_policy_definition_item_request_builder.GroupPolicyDefinitionItemRequestBuilder:
        """
        Provides operations to manage the groupPolicyDefinitions property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: group_policy_definition_item_request_builder.GroupPolicyDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .group_policy_definitions.item import group_policy_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupPolicyDefinition%2Did"] = id
        return group_policy_definition_item_request_builder.GroupPolicyDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def group_policy_migration_reports_by_id(self,id: str) -> group_policy_migration_report_item_request_builder.GroupPolicyMigrationReportItemRequestBuilder:
        """
        Provides operations to manage the groupPolicyMigrationReports property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: group_policy_migration_report_item_request_builder.GroupPolicyMigrationReportItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .group_policy_migration_reports.item import group_policy_migration_report_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupPolicyMigrationReport%2Did"] = id
        return group_policy_migration_report_item_request_builder.GroupPolicyMigrationReportItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def group_policy_object_files_by_id(self,id: str) -> group_policy_object_file_item_request_builder.GroupPolicyObjectFileItemRequestBuilder:
        """
        Provides operations to manage the groupPolicyObjectFiles property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: group_policy_object_file_item_request_builder.GroupPolicyObjectFileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .group_policy_object_files.item import group_policy_object_file_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupPolicyObjectFile%2Did"] = id
        return group_policy_object_file_item_request_builder.GroupPolicyObjectFileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def group_policy_uploaded_definition_files_by_id(self,id: str) -> group_policy_uploaded_definition_file_item_request_builder.GroupPolicyUploadedDefinitionFileItemRequestBuilder:
        """
        Provides operations to manage the groupPolicyUploadedDefinitionFiles property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: group_policy_uploaded_definition_file_item_request_builder.GroupPolicyUploadedDefinitionFileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .group_policy_uploaded_definition_files.item import group_policy_uploaded_definition_file_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupPolicyUploadedDefinitionFile%2Did"] = id
        return group_policy_uploaded_definition_file_item_request_builder.GroupPolicyUploadedDefinitionFileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def imported_device_identities_by_id(self,id: str) -> imported_device_identity_item_request_builder.ImportedDeviceIdentityItemRequestBuilder:
        """
        Provides operations to manage the importedDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: imported_device_identity_item_request_builder.ImportedDeviceIdentityItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .imported_device_identities.item import imported_device_identity_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["importedDeviceIdentity%2Did"] = id
        return imported_device_identity_item_request_builder.ImportedDeviceIdentityItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def imported_windows_autopilot_device_identities_by_id(self,id: str) -> imported_windows_autopilot_device_identity_item_request_builder.ImportedWindowsAutopilotDeviceIdentityItemRequestBuilder:
        """
        Provides operations to manage the importedWindowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: imported_windows_autopilot_device_identity_item_request_builder.ImportedWindowsAutopilotDeviceIdentityItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .imported_windows_autopilot_device_identities.item import imported_windows_autopilot_device_identity_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["importedWindowsAutopilotDeviceIdentity%2Did"] = id
        return imported_windows_autopilot_device_identity_item_request_builder.ImportedWindowsAutopilotDeviceIdentityItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def intents_by_id(self,id: str) -> device_management_intent_item_request_builder.DeviceManagementIntentItemRequestBuilder:
        """
        Provides operations to manage the intents property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_intent_item_request_builder.DeviceManagementIntentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .intents.item import device_management_intent_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementIntent%2Did"] = id
        return device_management_intent_item_request_builder.DeviceManagementIntentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def intune_branding_profiles_by_id(self,id: str) -> intune_branding_profile_item_request_builder.IntuneBrandingProfileItemRequestBuilder:
        """
        Provides operations to manage the intuneBrandingProfiles property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: intune_branding_profile_item_request_builder.IntuneBrandingProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .intune_branding_profiles.item import intune_branding_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["intuneBrandingProfile%2Did"] = id
        return intune_branding_profile_item_request_builder.IntuneBrandingProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def ios_update_statuses_by_id(self,id: str) -> ios_update_device_status_item_request_builder.IosUpdateDeviceStatusItemRequestBuilder:
        """
        Provides operations to manage the iosUpdateStatuses property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: ios_update_device_status_item_request_builder.IosUpdateDeviceStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .ios_update_statuses.item import ios_update_device_status_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["iosUpdateDeviceStatus%2Did"] = id
        return ios_update_device_status_item_request_builder.IosUpdateDeviceStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def mac_o_s_software_update_account_summaries_by_id(self,id: str) -> mac_o_s_software_update_account_summary_item_request_builder.MacOSSoftwareUpdateAccountSummaryItemRequestBuilder:
        """
        Provides operations to manage the macOSSoftwareUpdateAccountSummaries property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: mac_o_s_software_update_account_summary_item_request_builder.MacOSSoftwareUpdateAccountSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .mac_o_s_software_update_account_summaries.item import mac_o_s_software_update_account_summary_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["macOSSoftwareUpdateAccountSummary%2Did"] = id
        return mac_o_s_software_update_account_summary_item_request_builder.MacOSSoftwareUpdateAccountSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_device_encryption_states_by_id(self,id: str) -> managed_device_encryption_state_item_request_builder.ManagedDeviceEncryptionStateItemRequestBuilder:
        """
        Provides operations to manage the managedDeviceEncryptionStates property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_device_encryption_state_item_request_builder.ManagedDeviceEncryptionStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .managed_device_encryption_states.item import managed_device_encryption_state_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDeviceEncryptionState%2Did"] = id
        return managed_device_encryption_state_item_request_builder.ManagedDeviceEncryptionStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_devices_by_id(self,id: str) -> managed_device_item_request_builder.ManagedDeviceItemRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_device_item_request_builder.ManagedDeviceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .comanaged_devices.item import managed_device_item_request_builder
        from .managed_devices.item import managed_device_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDevice%2Did"] = id
        return managed_device_item_request_builder.ManagedDeviceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def microsoft_tunnel_configurations_by_id(self,id: str) -> microsoft_tunnel_configuration_item_request_builder.MicrosoftTunnelConfigurationItemRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelConfigurations property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: microsoft_tunnel_configuration_item_request_builder.MicrosoftTunnelConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .microsoft_tunnel_configurations.item import microsoft_tunnel_configuration_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["microsoftTunnelConfiguration%2Did"] = id
        return microsoft_tunnel_configuration_item_request_builder.MicrosoftTunnelConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def microsoft_tunnel_health_thresholds_by_id(self,id: str) -> microsoft_tunnel_health_threshold_item_request_builder.MicrosoftTunnelHealthThresholdItemRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelHealthThresholds property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: microsoft_tunnel_health_threshold_item_request_builder.MicrosoftTunnelHealthThresholdItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .microsoft_tunnel_health_thresholds.item import microsoft_tunnel_health_threshold_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["microsoftTunnelHealthThreshold%2Did"] = id
        return microsoft_tunnel_health_threshold_item_request_builder.MicrosoftTunnelHealthThresholdItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def microsoft_tunnel_server_log_collection_responses_by_id(self,id: str) -> microsoft_tunnel_server_log_collection_response_item_request_builder.MicrosoftTunnelServerLogCollectionResponseItemRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelServerLogCollectionResponses property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: microsoft_tunnel_server_log_collection_response_item_request_builder.MicrosoftTunnelServerLogCollectionResponseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .microsoft_tunnel_server_log_collection_responses.item import microsoft_tunnel_server_log_collection_response_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["microsoftTunnelServerLogCollectionResponse%2Did"] = id
        return microsoft_tunnel_server_log_collection_response_item_request_builder.MicrosoftTunnelServerLogCollectionResponseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def microsoft_tunnel_sites_by_id(self,id: str) -> microsoft_tunnel_site_item_request_builder.MicrosoftTunnelSiteItemRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelSites property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: microsoft_tunnel_site_item_request_builder.MicrosoftTunnelSiteItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .microsoft_tunnel_sites.item import microsoft_tunnel_site_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["microsoftTunnelSite%2Did"] = id
        return microsoft_tunnel_site_item_request_builder.MicrosoftTunnelSiteItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def mobile_app_troubleshooting_events_by_id(self,id: str) -> mobile_app_troubleshooting_event_item_request_builder.MobileAppTroubleshootingEventItemRequestBuilder:
        """
        Provides operations to manage the mobileAppTroubleshootingEvents property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: mobile_app_troubleshooting_event_item_request_builder.MobileAppTroubleshootingEventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .mobile_app_troubleshooting_events.item import mobile_app_troubleshooting_event_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobileAppTroubleshootingEvent%2Did"] = id
        return mobile_app_troubleshooting_event_item_request_builder.MobileAppTroubleshootingEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def mobile_threat_defense_connectors_by_id(self,id: str) -> mobile_threat_defense_connector_item_request_builder.MobileThreatDefenseConnectorItemRequestBuilder:
        """
        Provides operations to manage the mobileThreatDefenseConnectors property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: mobile_threat_defense_connector_item_request_builder.MobileThreatDefenseConnectorItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .mobile_threat_defense_connectors.item import mobile_threat_defense_connector_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobileThreatDefenseConnector%2Did"] = id
        return mobile_threat_defense_connector_item_request_builder.MobileThreatDefenseConnectorItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def ndes_connectors_by_id(self,id: str) -> ndes_connector_item_request_builder.NdesConnectorItemRequestBuilder:
        """
        Provides operations to manage the ndesConnectors property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: ndes_connector_item_request_builder.NdesConnectorItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .ndes_connectors.item import ndes_connector_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ndesConnector%2Did"] = id
        return ndes_connector_item_request_builder.NdesConnectorItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def notification_message_templates_by_id(self,id: str) -> notification_message_template_item_request_builder.NotificationMessageTemplateItemRequestBuilder:
        """
        Provides operations to manage the notificationMessageTemplates property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: notification_message_template_item_request_builder.NotificationMessageTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .notification_message_templates.item import notification_message_template_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["notificationMessageTemplate%2Did"] = id
        return notification_message_template_item_request_builder.NotificationMessageTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def oem_warranty_information_onboarding_by_id(self,id: str) -> oem_warranty_information_onboarding_item_request_builder.OemWarrantyInformationOnboardingItemRequestBuilder:
        """
        Provides operations to manage the oemWarrantyInformationOnboarding property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: oem_warranty_information_onboarding_item_request_builder.OemWarrantyInformationOnboardingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .oem_warranty_information_onboarding.item import oem_warranty_information_onboarding_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["oemWarrantyInformationOnboarding%2Did"] = id
        return oem_warranty_information_onboarding_item_request_builder.OemWarrantyInformationOnboardingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[device_management.DeviceManagement] = None, request_configuration: Optional[DeviceManagementRequestBuilderPatchRequestConfiguration] = None) -> Optional[device_management.DeviceManagement]:
        """
        Update deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management.DeviceManagement]
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
        from ..models.device_management import device_management

        return await self.request_adapter.send_async(request_info, device_management.DeviceManagement, error_mapping)
    
    def privilege_management_elevations_by_id(self,id: str) -> privilege_management_elevation_item_request_builder.PrivilegeManagementElevationItemRequestBuilder:
        """
        Provides operations to manage the privilegeManagementElevations property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: privilege_management_elevation_item_request_builder.PrivilegeManagementElevationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .privilege_management_elevations.item import privilege_management_elevation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegeManagementElevation%2Did"] = id
        return privilege_management_elevation_item_request_builder.PrivilegeManagementElevationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def remote_action_audits_by_id(self,id: str) -> remote_action_audit_item_request_builder.RemoteActionAuditItemRequestBuilder:
        """
        Provides operations to manage the remoteActionAudits property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: remote_action_audit_item_request_builder.RemoteActionAuditItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .remote_action_audits.item import remote_action_audit_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["remoteActionAudit%2Did"] = id
        return remote_action_audit_item_request_builder.RemoteActionAuditItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def remote_assistance_partners_by_id(self,id: str) -> remote_assistance_partner_item_request_builder.RemoteAssistancePartnerItemRequestBuilder:
        """
        Provides operations to manage the remoteAssistancePartners property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: remote_assistance_partner_item_request_builder.RemoteAssistancePartnerItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .remote_assistance_partners.item import remote_assistance_partner_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["remoteAssistancePartner%2Did"] = id
        return remote_assistance_partner_item_request_builder.RemoteAssistancePartnerItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def resource_access_profiles_by_id(self,id: str) -> device_management_resource_access_profile_base_item_request_builder.DeviceManagementResourceAccessProfileBaseItemRequestBuilder:
        """
        Provides operations to manage the resourceAccessProfiles property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_resource_access_profile_base_item_request_builder.DeviceManagementResourceAccessProfileBaseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .resource_access_profiles.item import device_management_resource_access_profile_base_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementResourceAccessProfileBase%2Did"] = id
        return device_management_resource_access_profile_base_item_request_builder.DeviceManagementResourceAccessProfileBaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def resource_operations_by_id(self,id: str) -> resource_operation_item_request_builder.ResourceOperationItemRequestBuilder:
        """
        Provides operations to manage the resourceOperations property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: resource_operation_item_request_builder.ResourceOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .resource_operations.item import resource_operation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["resourceOperation%2Did"] = id
        return resource_operation_item_request_builder.ResourceOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def reusable_policy_settings_by_id(self,id: str) -> device_management_reusable_policy_setting_item_request_builder.DeviceManagementReusablePolicySettingItemRequestBuilder:
        """
        Provides operations to manage the reusablePolicySettings property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_reusable_policy_setting_item_request_builder.DeviceManagementReusablePolicySettingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .reusable_policy_settings.item import device_management_reusable_policy_setting_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementReusablePolicySetting%2Did"] = id
        return device_management_reusable_policy_setting_item_request_builder.DeviceManagementReusablePolicySettingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def reusable_settings_by_id(self,id: str) -> device_management_configuration_setting_definition_item_request_builder.DeviceManagementConfigurationSettingDefinitionItemRequestBuilder:
        """
        Provides operations to manage the reusableSettings property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_configuration_setting_definition_item_request_builder.DeviceManagementConfigurationSettingDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .compliance_settings.item import device_management_configuration_setting_definition_item_request_builder
        from .configuration_settings.item import device_management_configuration_setting_definition_item_request_builder
        from .reusable_settings.item import device_management_configuration_setting_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementConfigurationSettingDefinition%2Did"] = id
        return device_management_configuration_setting_definition_item_request_builder.DeviceManagementConfigurationSettingDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_assignments_by_id(self,id: str) -> device_and_app_management_role_assignment_item_request_builder.DeviceAndAppManagementRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_and_app_management_role_assignment_item_request_builder.DeviceAndAppManagementRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_assignments.item import device_and_app_management_role_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceAndAppManagementRoleAssignment%2Did"] = id
        return device_and_app_management_role_assignment_item_request_builder.DeviceAndAppManagementRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_definitions_by_id(self,id: str) -> role_definition_item_request_builder.RoleDefinitionItemRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: role_definition_item_request_builder.RoleDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_definitions.item import role_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["roleDefinition%2Did"] = id
        return role_definition_item_request_builder.RoleDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_scope_tags_by_id(self,id: str) -> role_scope_tag_item_request_builder.RoleScopeTagItemRequestBuilder:
        """
        Provides operations to manage the roleScopeTags property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: role_scope_tag_item_request_builder.RoleScopeTagItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_scope_tags.item import role_scope_tag_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["roleScopeTag%2Did"] = id
        return role_scope_tag_item_request_builder.RoleScopeTagItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def scoped_for_resource_with_resource(self,resource: Optional[str] = None) -> scoped_for_resource_with_resource_request_builder.ScopedForResourceWithResourceRequestBuilder:
        """
        Provides operations to call the scopedForResource method.
        Args:
            resource: Usage: resource='{resource}'
        Returns: scoped_for_resource_with_resource_request_builder.ScopedForResourceWithResourceRequestBuilder
        """
        if resource is None:
            raise Exception("resource cannot be undefined")
        from .scoped_for_resource_with_resource import scoped_for_resource_with_resource_request_builder

        return scoped_for_resource_with_resource_request_builder.ScopedForResourceWithResourceRequestBuilder(self.request_adapter, self.path_parameters, resource)
    
    def service_now_connections_by_id(self,id: str) -> service_now_connection_item_request_builder.ServiceNowConnectionItemRequestBuilder:
        """
        Provides operations to manage the serviceNowConnections property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: service_now_connection_item_request_builder.ServiceNowConnectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .service_now_connections.item import service_now_connection_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["serviceNowConnection%2Did"] = id
        return service_now_connection_item_request_builder.ServiceNowConnectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def setting_definitions_by_id(self,id: str) -> device_management_setting_definition_item_request_builder.DeviceManagementSettingDefinitionItemRequestBuilder:
        """
        Provides operations to manage the settingDefinitions property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_setting_definition_item_request_builder.DeviceManagementSettingDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .setting_definitions.item import device_management_setting_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementSettingDefinition%2Did"] = id
        return device_management_setting_definition_item_request_builder.DeviceManagementSettingDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def telecom_expense_management_partners_by_id(self,id: str) -> telecom_expense_management_partner_item_request_builder.TelecomExpenseManagementPartnerItemRequestBuilder:
        """
        Provides operations to manage the telecomExpenseManagementPartners property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: telecom_expense_management_partner_item_request_builder.TelecomExpenseManagementPartnerItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .telecom_expense_management_partners.item import telecom_expense_management_partner_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["telecomExpenseManagementPartner%2Did"] = id
        return telecom_expense_management_partner_item_request_builder.TelecomExpenseManagementPartnerItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def templates_by_id(self,id: str) -> device_management_template_item_request_builder.DeviceManagementTemplateItemRequestBuilder:
        """
        Provides operations to manage the templates property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_template_item_request_builder.DeviceManagementTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .templates.item import device_management_template_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementTemplate%2Did"] = id
        return device_management_template_item_request_builder.DeviceManagementTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def template_settings_by_id(self,id: str) -> device_management_configuration_setting_template_item_request_builder.DeviceManagementConfigurationSettingTemplateItemRequestBuilder:
        """
        Provides operations to manage the templateSettings property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_configuration_setting_template_item_request_builder.DeviceManagementConfigurationSettingTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .template_settings.item import device_management_configuration_setting_template_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementConfigurationSettingTemplate%2Did"] = id
        return device_management_configuration_setting_template_item_request_builder.DeviceManagementConfigurationSettingTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def terms_and_conditions_by_id(self,id: str) -> terms_and_conditions_item_request_builder.TermsAndConditionsItemRequestBuilder:
        """
        Provides operations to manage the termsAndConditions property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: terms_and_conditions_item_request_builder.TermsAndConditionsItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .terms_and_conditions.item import terms_and_conditions_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["termsAndConditions%2Did"] = id
        return terms_and_conditions_item_request_builder.TermsAndConditionsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[DeviceManagementRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get deviceManagement
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
    
    def to_patch_request_information(self,body: Optional[device_management.DeviceManagement] = None, request_configuration: Optional[DeviceManagementRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update deviceManagement
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
    
    def troubleshooting_events_by_id(self,id: str) -> device_management_troubleshooting_event_item_request_builder.DeviceManagementTroubleshootingEventItemRequestBuilder:
        """
        Provides operations to manage the troubleshootingEvents property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_troubleshooting_event_item_request_builder.DeviceManagementTroubleshootingEventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .troubleshooting_events.item import device_management_troubleshooting_event_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementTroubleshootingEvent%2Did"] = id
        return device_management_troubleshooting_event_item_request_builder.DeviceManagementTroubleshootingEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_anomaly_by_id(self,id: str) -> user_experience_analytics_anomaly_item_request_builder.UserExperienceAnalyticsAnomalyItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAnomaly property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_anomaly_item_request_builder.UserExperienceAnalyticsAnomalyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_anomaly.item import user_experience_analytics_anomaly_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsAnomaly%2Did"] = id
        return user_experience_analytics_anomaly_item_request_builder.UserExperienceAnalyticsAnomalyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_anomaly_device_by_id(self,id: str) -> user_experience_analytics_anomaly_device_item_request_builder.UserExperienceAnalyticsAnomalyDeviceItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAnomalyDevice property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_anomaly_device_item_request_builder.UserExperienceAnalyticsAnomalyDeviceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_anomaly_device.item import user_experience_analytics_anomaly_device_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsAnomalyDevice%2Did"] = id
        return user_experience_analytics_anomaly_device_item_request_builder.UserExperienceAnalyticsAnomalyDeviceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_app_health_application_performance_by_id(self,id: str) -> user_experience_analytics_app_health_application_performance_item_request_builder.UserExperienceAnalyticsAppHealthApplicationPerformanceItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformance property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_app_health_application_performance_item_request_builder.UserExperienceAnalyticsAppHealthApplicationPerformanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_app_health_application_performance.item import user_experience_analytics_app_health_application_performance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsAppHealthApplicationPerformance%2Did"] = id
        return user_experience_analytics_app_health_application_performance_item_request_builder.UserExperienceAnalyticsAppHealthApplicationPerformanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_app_health_application_performance_by_app_version_by_id(self,id: str) -> user_experience_analytics_app_health_app_performance_by_app_version_item_request_builder.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_app_health_app_performance_by_app_version_item_request_builder.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_app_health_application_performance_by_app_version.item import user_experience_analytics_app_health_app_performance_by_app_version_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsAppHealthAppPerformanceByAppVersion%2Did"] = id
        return user_experience_analytics_app_health_app_performance_by_app_version_item_request_builder.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_app_health_application_performance_by_app_version_details_by_id(self,id: str) -> user_experience_analytics_app_health_app_performance_by_app_version_details_item_request_builder.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetailsItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_app_health_app_performance_by_app_version_details_item_request_builder.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetailsItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_app_health_application_performance_by_app_version_details.item import user_experience_analytics_app_health_app_performance_by_app_version_details_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails%2Did"] = id
        return user_experience_analytics_app_health_app_performance_by_app_version_details_item_request_builder.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetailsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_app_health_application_performance_by_app_version_device_id_by_id(self,id: str) -> user_experience_analytics_app_health_app_performance_by_app_version_device_id_item_request_builder.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceIdItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_app_health_app_performance_by_app_version_device_id_item_request_builder.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceIdItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_app_health_application_performance_by_app_version_device_id.item import user_experience_analytics_app_health_app_performance_by_app_version_device_id_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId%2Did"] = id
        return user_experience_analytics_app_health_app_performance_by_app_version_device_id_item_request_builder.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceIdItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_app_health_application_performance_by_o_s_version_by_id(self,id: str) -> user_experience_analytics_app_health_app_performance_by_o_s_version_item_request_builder.UserExperienceAnalyticsAppHealthAppPerformanceByOSVersionItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_app_health_app_performance_by_o_s_version_item_request_builder.UserExperienceAnalyticsAppHealthAppPerformanceByOSVersionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_app_health_application_performance_by_o_s_version.item import user_experience_analytics_app_health_app_performance_by_o_s_version_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsAppHealthAppPerformanceByOSVersion%2Did"] = id
        return user_experience_analytics_app_health_app_performance_by_o_s_version_item_request_builder.UserExperienceAnalyticsAppHealthAppPerformanceByOSVersionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_app_health_device_model_performance_by_id(self,id: str) -> user_experience_analytics_app_health_device_model_performance_item_request_builder.UserExperienceAnalyticsAppHealthDeviceModelPerformanceItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthDeviceModelPerformance property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_app_health_device_model_performance_item_request_builder.UserExperienceAnalyticsAppHealthDeviceModelPerformanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_app_health_device_model_performance.item import user_experience_analytics_app_health_device_model_performance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsAppHealthDeviceModelPerformance%2Did"] = id
        return user_experience_analytics_app_health_device_model_performance_item_request_builder.UserExperienceAnalyticsAppHealthDeviceModelPerformanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_app_health_device_performance_by_id(self,id: str) -> user_experience_analytics_app_health_device_performance_item_request_builder.UserExperienceAnalyticsAppHealthDevicePerformanceItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthDevicePerformance property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_app_health_device_performance_item_request_builder.UserExperienceAnalyticsAppHealthDevicePerformanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_app_health_device_performance.item import user_experience_analytics_app_health_device_performance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsAppHealthDevicePerformance%2Did"] = id
        return user_experience_analytics_app_health_device_performance_item_request_builder.UserExperienceAnalyticsAppHealthDevicePerformanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_app_health_device_performance_details_by_id(self,id: str) -> user_experience_analytics_app_health_device_performance_details_item_request_builder.UserExperienceAnalyticsAppHealthDevicePerformanceDetailsItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthDevicePerformanceDetails property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_app_health_device_performance_details_item_request_builder.UserExperienceAnalyticsAppHealthDevicePerformanceDetailsItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_app_health_device_performance_details.item import user_experience_analytics_app_health_device_performance_details_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsAppHealthDevicePerformanceDetails%2Did"] = id
        return user_experience_analytics_app_health_device_performance_details_item_request_builder.UserExperienceAnalyticsAppHealthDevicePerformanceDetailsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_app_health_o_s_version_performance_by_id(self,id: str) -> user_experience_analytics_app_health_o_s_version_performance_item_request_builder.UserExperienceAnalyticsAppHealthOSVersionPerformanceItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthOSVersionPerformance property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_app_health_o_s_version_performance_item_request_builder.UserExperienceAnalyticsAppHealthOSVersionPerformanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_app_health_o_s_version_performance.item import user_experience_analytics_app_health_o_s_version_performance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsAppHealthOSVersionPerformance%2Did"] = id
        return user_experience_analytics_app_health_o_s_version_performance_item_request_builder.UserExperienceAnalyticsAppHealthOSVersionPerformanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_baselines_by_id(self,id: str) -> user_experience_analytics_baseline_item_request_builder.UserExperienceAnalyticsBaselineItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBaselines property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_baseline_item_request_builder.UserExperienceAnalyticsBaselineItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_baselines.item import user_experience_analytics_baseline_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsBaseline%2Did"] = id
        return user_experience_analytics_baseline_item_request_builder.UserExperienceAnalyticsBaselineItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_battery_health_app_impact_by_id(self,id: str) -> user_experience_analytics_battery_health_app_impact_item_request_builder.UserExperienceAnalyticsBatteryHealthAppImpactItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthAppImpact property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_battery_health_app_impact_item_request_builder.UserExperienceAnalyticsBatteryHealthAppImpactItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_battery_health_app_impact.item import user_experience_analytics_battery_health_app_impact_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsBatteryHealthAppImpact%2Did"] = id
        return user_experience_analytics_battery_health_app_impact_item_request_builder.UserExperienceAnalyticsBatteryHealthAppImpactItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_battery_health_device_app_impact_by_id(self,id: str) -> user_experience_analytics_battery_health_device_app_impact_item_request_builder.UserExperienceAnalyticsBatteryHealthDeviceAppImpactItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthDeviceAppImpact property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_battery_health_device_app_impact_item_request_builder.UserExperienceAnalyticsBatteryHealthDeviceAppImpactItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_battery_health_device_app_impact.item import user_experience_analytics_battery_health_device_app_impact_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsBatteryHealthDeviceAppImpact%2Did"] = id
        return user_experience_analytics_battery_health_device_app_impact_item_request_builder.UserExperienceAnalyticsBatteryHealthDeviceAppImpactItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_battery_health_device_performance_by_id(self,id: str) -> user_experience_analytics_battery_health_device_performance_item_request_builder.UserExperienceAnalyticsBatteryHealthDevicePerformanceItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthDevicePerformance property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_battery_health_device_performance_item_request_builder.UserExperienceAnalyticsBatteryHealthDevicePerformanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_battery_health_device_performance.item import user_experience_analytics_battery_health_device_performance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsBatteryHealthDevicePerformance%2Did"] = id
        return user_experience_analytics_battery_health_device_performance_item_request_builder.UserExperienceAnalyticsBatteryHealthDevicePerformanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_battery_health_device_runtime_history_by_id(self,id: str) -> user_experience_analytics_battery_health_device_runtime_history_item_request_builder.UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistoryItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_battery_health_device_runtime_history_item_request_builder.UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_battery_health_device_runtime_history.item import user_experience_analytics_battery_health_device_runtime_history_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory%2Did"] = id
        return user_experience_analytics_battery_health_device_runtime_history_item_request_builder.UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_battery_health_model_performance_by_id(self,id: str) -> user_experience_analytics_battery_health_model_performance_item_request_builder.UserExperienceAnalyticsBatteryHealthModelPerformanceItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthModelPerformance property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_battery_health_model_performance_item_request_builder.UserExperienceAnalyticsBatteryHealthModelPerformanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_battery_health_model_performance.item import user_experience_analytics_battery_health_model_performance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsBatteryHealthModelPerformance%2Did"] = id
        return user_experience_analytics_battery_health_model_performance_item_request_builder.UserExperienceAnalyticsBatteryHealthModelPerformanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_battery_health_os_performance_by_id(self,id: str) -> user_experience_analytics_battery_health_os_performance_item_request_builder.UserExperienceAnalyticsBatteryHealthOsPerformanceItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthOsPerformance property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_battery_health_os_performance_item_request_builder.UserExperienceAnalyticsBatteryHealthOsPerformanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_battery_health_os_performance.item import user_experience_analytics_battery_health_os_performance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsBatteryHealthOsPerformance%2Did"] = id
        return user_experience_analytics_battery_health_os_performance_item_request_builder.UserExperienceAnalyticsBatteryHealthOsPerformanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_categories_by_id(self,id: str) -> user_experience_analytics_category_item_request_builder.UserExperienceAnalyticsCategoryItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsCategories property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_category_item_request_builder.UserExperienceAnalyticsCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_categories.item import user_experience_analytics_category_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsCategory%2Did"] = id
        return user_experience_analytics_category_item_request_builder.UserExperienceAnalyticsCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_device_metric_history_by_id(self,id: str) -> user_experience_analytics_metric_history_item_request_builder.UserExperienceAnalyticsMetricHistoryItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceMetricHistory property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_metric_history_item_request_builder.UserExperienceAnalyticsMetricHistoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_device_metric_history.item import user_experience_analytics_metric_history_item_request_builder
        from .user_experience_analytics_metric_history.item import user_experience_analytics_metric_history_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsMetricHistory%2Did"] = id
        return user_experience_analytics_metric_history_item_request_builder.UserExperienceAnalyticsMetricHistoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_device_performance_by_id(self,id: str) -> user_experience_analytics_device_performance_item_request_builder.UserExperienceAnalyticsDevicePerformanceItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDevicePerformance property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_device_performance_item_request_builder.UserExperienceAnalyticsDevicePerformanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_device_performance.item import user_experience_analytics_device_performance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsDevicePerformance%2Did"] = id
        return user_experience_analytics_device_performance_item_request_builder.UserExperienceAnalyticsDevicePerformanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_device_scopes_by_id(self,id: str) -> user_experience_analytics_device_scope_item_request_builder.UserExperienceAnalyticsDeviceScopeItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceScopes property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_device_scope_item_request_builder.UserExperienceAnalyticsDeviceScopeItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_device_scopes.item import user_experience_analytics_device_scope_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsDeviceScope%2Did"] = id
        return user_experience_analytics_device_scope_item_request_builder.UserExperienceAnalyticsDeviceScopeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_device_scores_by_id(self,id: str) -> user_experience_analytics_device_scores_item_request_builder.UserExperienceAnalyticsDeviceScoresItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceScores property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_device_scores_item_request_builder.UserExperienceAnalyticsDeviceScoresItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_device_scores.item import user_experience_analytics_device_scores_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsDeviceScores%2Did"] = id
        return user_experience_analytics_device_scores_item_request_builder.UserExperienceAnalyticsDeviceScoresItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_device_startup_history_by_id(self,id: str) -> user_experience_analytics_device_startup_history_item_request_builder.UserExperienceAnalyticsDeviceStartupHistoryItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceStartupHistory property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_device_startup_history_item_request_builder.UserExperienceAnalyticsDeviceStartupHistoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_device_startup_history.item import user_experience_analytics_device_startup_history_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsDeviceStartupHistory%2Did"] = id
        return user_experience_analytics_device_startup_history_item_request_builder.UserExperienceAnalyticsDeviceStartupHistoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_device_startup_processes_by_id(self,id: str) -> user_experience_analytics_device_startup_process_item_request_builder.UserExperienceAnalyticsDeviceStartupProcessItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceStartupProcesses property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_device_startup_process_item_request_builder.UserExperienceAnalyticsDeviceStartupProcessItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_device_startup_processes.item import user_experience_analytics_device_startup_process_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsDeviceStartupProcess%2Did"] = id
        return user_experience_analytics_device_startup_process_item_request_builder.UserExperienceAnalyticsDeviceStartupProcessItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_device_startup_process_performance_by_id(self,id: str) -> user_experience_analytics_device_startup_process_performance_item_request_builder.UserExperienceAnalyticsDeviceStartupProcessPerformanceItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceStartupProcessPerformance property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_device_startup_process_performance_item_request_builder.UserExperienceAnalyticsDeviceStartupProcessPerformanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_device_startup_process_performance.item import user_experience_analytics_device_startup_process_performance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsDeviceStartupProcessPerformance%2Did"] = id
        return user_experience_analytics_device_startup_process_performance_item_request_builder.UserExperienceAnalyticsDeviceStartupProcessPerformanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_devices_without_cloud_identity_by_id(self,id: str) -> user_experience_analytics_device_without_cloud_identity_item_request_builder.UserExperienceAnalyticsDeviceWithoutCloudIdentityItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDevicesWithoutCloudIdentity property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_device_without_cloud_identity_item_request_builder.UserExperienceAnalyticsDeviceWithoutCloudIdentityItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_devices_without_cloud_identity.item import user_experience_analytics_device_without_cloud_identity_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsDeviceWithoutCloudIdentity%2Did"] = id
        return user_experience_analytics_device_without_cloud_identity_item_request_builder.UserExperienceAnalyticsDeviceWithoutCloudIdentityItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_device_timeline_event_by_id(self,id: str) -> user_experience_analytics_device_timeline_event_item_request_builder.UserExperienceAnalyticsDeviceTimelineEventItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceTimelineEvent property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_device_timeline_event_item_request_builder.UserExperienceAnalyticsDeviceTimelineEventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_device_timeline_event.item import user_experience_analytics_device_timeline_event_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsDeviceTimelineEvent%2Did"] = id
        return user_experience_analytics_device_timeline_event_item_request_builder.UserExperienceAnalyticsDeviceTimelineEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_impacting_process_by_id(self,id: str) -> user_experience_analytics_impacting_process_item_request_builder.UserExperienceAnalyticsImpactingProcessItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsImpactingProcess property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_impacting_process_item_request_builder.UserExperienceAnalyticsImpactingProcessItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_impacting_process.item import user_experience_analytics_impacting_process_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsImpactingProcess%2Did"] = id
        return user_experience_analytics_impacting_process_item_request_builder.UserExperienceAnalyticsImpactingProcessItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_metric_history_by_id(self,id: str) -> user_experience_analytics_metric_history_item_request_builder.UserExperienceAnalyticsMetricHistoryItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsMetricHistory property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_metric_history_item_request_builder.UserExperienceAnalyticsMetricHistoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_device_metric_history.item import user_experience_analytics_metric_history_item_request_builder
        from .user_experience_analytics_metric_history.item import user_experience_analytics_metric_history_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsMetricHistory%2Did"] = id
        return user_experience_analytics_metric_history_item_request_builder.UserExperienceAnalyticsMetricHistoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_model_scores_by_id(self,id: str) -> user_experience_analytics_model_scores_item_request_builder.UserExperienceAnalyticsModelScoresItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsModelScores property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_model_scores_item_request_builder.UserExperienceAnalyticsModelScoresItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_model_scores.item import user_experience_analytics_model_scores_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsModelScores%2Did"] = id
        return user_experience_analytics_model_scores_item_request_builder.UserExperienceAnalyticsModelScoresItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_not_autopilot_ready_device_by_id(self,id: str) -> user_experience_analytics_not_autopilot_ready_device_item_request_builder.UserExperienceAnalyticsNotAutopilotReadyDeviceItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsNotAutopilotReadyDevice property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_not_autopilot_ready_device_item_request_builder.UserExperienceAnalyticsNotAutopilotReadyDeviceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_not_autopilot_ready_device.item import user_experience_analytics_not_autopilot_ready_device_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsNotAutopilotReadyDevice%2Did"] = id
        return user_experience_analytics_not_autopilot_ready_device_item_request_builder.UserExperienceAnalyticsNotAutopilotReadyDeviceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_remote_connection_by_id(self,id: str) -> user_experience_analytics_remote_connection_item_request_builder.UserExperienceAnalyticsRemoteConnectionItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsRemoteConnection property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_remote_connection_item_request_builder.UserExperienceAnalyticsRemoteConnectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_remote_connection.item import user_experience_analytics_remote_connection_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsRemoteConnection%2Did"] = id
        return user_experience_analytics_remote_connection_item_request_builder.UserExperienceAnalyticsRemoteConnectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_resource_performance_by_id(self,id: str) -> user_experience_analytics_resource_performance_item_request_builder.UserExperienceAnalyticsResourcePerformanceItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsResourcePerformance property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_resource_performance_item_request_builder.UserExperienceAnalyticsResourcePerformanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_resource_performance.item import user_experience_analytics_resource_performance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsResourcePerformance%2Did"] = id
        return user_experience_analytics_resource_performance_item_request_builder.UserExperienceAnalyticsResourcePerformanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_score_history_by_id(self,id: str) -> user_experience_analytics_score_history_item_request_builder.UserExperienceAnalyticsScoreHistoryItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsScoreHistory property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_score_history_item_request_builder.UserExperienceAnalyticsScoreHistoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_score_history.item import user_experience_analytics_score_history_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsScoreHistory%2Did"] = id
        return user_experience_analytics_score_history_item_request_builder.UserExperienceAnalyticsScoreHistoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_work_from_anywhere_metrics_by_id(self,id: str) -> user_experience_analytics_work_from_anywhere_metric_item_request_builder.UserExperienceAnalyticsWorkFromAnywhereMetricItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsWorkFromAnywhereMetrics property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_work_from_anywhere_metric_item_request_builder.UserExperienceAnalyticsWorkFromAnywhereMetricItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_work_from_anywhere_metrics.item import user_experience_analytics_work_from_anywhere_metric_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsWorkFromAnywhereMetric%2Did"] = id
        return user_experience_analytics_work_from_anywhere_metric_item_request_builder.UserExperienceAnalyticsWorkFromAnywhereMetricItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_experience_analytics_work_from_anywhere_model_performance_by_id(self,id: str) -> user_experience_analytics_work_from_anywhere_model_performance_item_request_builder.UserExperienceAnalyticsWorkFromAnywhereModelPerformanceItemRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsWorkFromAnywhereModelPerformance property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_experience_analytics_work_from_anywhere_model_performance_item_request_builder.UserExperienceAnalyticsWorkFromAnywhereModelPerformanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_experience_analytics_work_from_anywhere_model_performance.item import user_experience_analytics_work_from_anywhere_model_performance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsWorkFromAnywhereModelPerformance%2Did"] = id
        return user_experience_analytics_work_from_anywhere_model_performance_item_request_builder.UserExperienceAnalyticsWorkFromAnywhereModelPerformanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_pfx_certificates_by_id(self,id: str) -> user_p_f_x_certificate_item_request_builder.UserPFXCertificateItemRequestBuilder:
        """
        Provides operations to manage the userPfxCertificates property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: user_p_f_x_certificate_item_request_builder.UserPFXCertificateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_pfx_certificates.item import user_p_f_x_certificate_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userPFXCertificate%2Did"] = id
        return user_p_f_x_certificate_item_request_builder.UserPFXCertificateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def verify_windows_enrollment_auto_discovery_with_domain_name(self,domain_name: Optional[str] = None) -> verify_windows_enrollment_auto_discovery_with_domain_name_request_builder.VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder:
        """
        Provides operations to call the verifyWindowsEnrollmentAutoDiscovery method.
        Args:
            domainName: Usage: domainName='{domainName}'
        Returns: verify_windows_enrollment_auto_discovery_with_domain_name_request_builder.VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder
        """
        if domain_name is None:
            raise Exception("domain_name cannot be undefined")
        from .verify_windows_enrollment_auto_discovery_with_domain_name import verify_windows_enrollment_auto_discovery_with_domain_name_request_builder

        return verify_windows_enrollment_auto_discovery_with_domain_name_request_builder.VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder(self.request_adapter, self.path_parameters, domain_name)
    
    def windows_autopilot_deployment_profiles_by_id(self,id: str) -> windows_autopilot_deployment_profile_item_request_builder.WindowsAutopilotDeploymentProfileItemRequestBuilder:
        """
        Provides operations to manage the windowsAutopilotDeploymentProfiles property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_autopilot_deployment_profile_item_request_builder.WindowsAutopilotDeploymentProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .windows_autopilot_deployment_profiles.item import windows_autopilot_deployment_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsAutopilotDeploymentProfile%2Did"] = id
        return windows_autopilot_deployment_profile_item_request_builder.WindowsAutopilotDeploymentProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_autopilot_device_identities_by_id(self,id: str) -> windows_autopilot_device_identity_item_request_builder.WindowsAutopilotDeviceIdentityItemRequestBuilder:
        """
        Provides operations to manage the windowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_autopilot_device_identity_item_request_builder.WindowsAutopilotDeviceIdentityItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .windows_autopilot_device_identities.item import windows_autopilot_device_identity_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsAutopilotDeviceIdentity%2Did"] = id
        return windows_autopilot_device_identity_item_request_builder.WindowsAutopilotDeviceIdentityItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_driver_update_profiles_by_id(self,id: str) -> windows_driver_update_profile_item_request_builder.WindowsDriverUpdateProfileItemRequestBuilder:
        """
        Provides operations to manage the windowsDriverUpdateProfiles property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_driver_update_profile_item_request_builder.WindowsDriverUpdateProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .windows_driver_update_profiles.item import windows_driver_update_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsDriverUpdateProfile%2Did"] = id
        return windows_driver_update_profile_item_request_builder.WindowsDriverUpdateProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_feature_update_profiles_by_id(self,id: str) -> windows_feature_update_profile_item_request_builder.WindowsFeatureUpdateProfileItemRequestBuilder:
        """
        Provides operations to manage the windowsFeatureUpdateProfiles property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_feature_update_profile_item_request_builder.WindowsFeatureUpdateProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .windows_feature_update_profiles.item import windows_feature_update_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsFeatureUpdateProfile%2Did"] = id
        return windows_feature_update_profile_item_request_builder.WindowsFeatureUpdateProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_information_protection_app_learning_summaries_by_id(self,id: str) -> windows_information_protection_app_learning_summary_item_request_builder.WindowsInformationProtectionAppLearningSummaryItemRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionAppLearningSummaries property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_information_protection_app_learning_summary_item_request_builder.WindowsInformationProtectionAppLearningSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .windows_information_protection_app_learning_summaries.item import windows_information_protection_app_learning_summary_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsInformationProtectionAppLearningSummary%2Did"] = id
        return windows_information_protection_app_learning_summary_item_request_builder.WindowsInformationProtectionAppLearningSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_information_protection_network_learning_summaries_by_id(self,id: str) -> windows_information_protection_network_learning_summary_item_request_builder.WindowsInformationProtectionNetworkLearningSummaryItemRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionNetworkLearningSummaries property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_information_protection_network_learning_summary_item_request_builder.WindowsInformationProtectionNetworkLearningSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .windows_information_protection_network_learning_summaries.item import windows_information_protection_network_learning_summary_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsInformationProtectionNetworkLearningSummary%2Did"] = id
        return windows_information_protection_network_learning_summary_item_request_builder.WindowsInformationProtectionNetworkLearningSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_malware_information_by_id(self,id: str) -> windows_malware_information_item_request_builder.WindowsMalwareInformationItemRequestBuilder:
        """
        Provides operations to manage the windowsMalwareInformation property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_malware_information_item_request_builder.WindowsMalwareInformationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .windows_malware_information.item import windows_malware_information_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsMalwareInformation%2Did"] = id
        return windows_malware_information_item_request_builder.WindowsMalwareInformationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_quality_update_profiles_by_id(self,id: str) -> windows_quality_update_profile_item_request_builder.WindowsQualityUpdateProfileItemRequestBuilder:
        """
        Provides operations to manage the windowsQualityUpdateProfiles property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_quality_update_profile_item_request_builder.WindowsQualityUpdateProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .windows_quality_update_profiles.item import windows_quality_update_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsQualityUpdateProfile%2Did"] = id
        return windows_quality_update_profile_item_request_builder.WindowsQualityUpdateProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_update_catalog_items_by_id(self,id: str) -> windows_update_catalog_item_item_request_builder.WindowsUpdateCatalogItemItemRequestBuilder:
        """
        Provides operations to manage the windowsUpdateCatalogItems property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_update_catalog_item_item_request_builder.WindowsUpdateCatalogItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .windows_update_catalog_items.item import windows_update_catalog_item_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsUpdateCatalogItem%2Did"] = id
        return windows_update_catalog_item_item_request_builder.WindowsUpdateCatalogItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def zebra_fota_artifacts_by_id(self,id: str) -> zebra_fota_artifact_item_request_builder.ZebraFotaArtifactItemRequestBuilder:
        """
        Provides operations to manage the zebraFotaArtifacts property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: zebra_fota_artifact_item_request_builder.ZebraFotaArtifactItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .zebra_fota_artifacts.item import zebra_fota_artifact_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["zebraFotaArtifact%2Did"] = id
        return zebra_fota_artifact_item_request_builder.ZebraFotaArtifactItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def zebra_fota_deployments_by_id(self,id: str) -> zebra_fota_deployment_item_request_builder.ZebraFotaDeploymentItemRequestBuilder:
        """
        Provides operations to manage the zebraFotaDeployments property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: zebra_fota_deployment_item_request_builder.ZebraFotaDeploymentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .zebra_fota_deployments.item import zebra_fota_deployment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["zebraFotaDeployment%2Did"] = id
        return zebra_fota_deployment_item_request_builder.ZebraFotaDeploymentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def advanced_threat_protection_onboarding_state_summary(self) -> advanced_threat_protection_onboarding_state_summary_request_builder.AdvancedThreatProtectionOnboardingStateSummaryRequestBuilder:
        """
        Provides operations to manage the advancedThreatProtectionOnboardingStateSummary property of the microsoft.graph.deviceManagement entity.
        """
        from .advanced_threat_protection_onboarding_state_summary import advanced_threat_protection_onboarding_state_summary_request_builder

        return advanced_threat_protection_onboarding_state_summary_request_builder.AdvancedThreatProtectionOnboardingStateSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def android_device_owner_enrollment_profiles(self) -> android_device_owner_enrollment_profiles_request_builder.AndroidDeviceOwnerEnrollmentProfilesRequestBuilder:
        """
        Provides operations to manage the androidDeviceOwnerEnrollmentProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .android_device_owner_enrollment_profiles import android_device_owner_enrollment_profiles_request_builder

        return android_device_owner_enrollment_profiles_request_builder.AndroidDeviceOwnerEnrollmentProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def android_for_work_app_configuration_schemas(self) -> android_for_work_app_configuration_schemas_request_builder.AndroidForWorkAppConfigurationSchemasRequestBuilder:
        """
        Provides operations to manage the androidForWorkAppConfigurationSchemas property of the microsoft.graph.deviceManagement entity.
        """
        from .android_for_work_app_configuration_schemas import android_for_work_app_configuration_schemas_request_builder

        return android_for_work_app_configuration_schemas_request_builder.AndroidForWorkAppConfigurationSchemasRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def android_for_work_enrollment_profiles(self) -> android_for_work_enrollment_profiles_request_builder.AndroidForWorkEnrollmentProfilesRequestBuilder:
        """
        Provides operations to manage the androidForWorkEnrollmentProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .android_for_work_enrollment_profiles import android_for_work_enrollment_profiles_request_builder

        return android_for_work_enrollment_profiles_request_builder.AndroidForWorkEnrollmentProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def android_for_work_settings(self) -> android_for_work_settings_request_builder.AndroidForWorkSettingsRequestBuilder:
        """
        Provides operations to manage the androidForWorkSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .android_for_work_settings import android_for_work_settings_request_builder

        return android_for_work_settings_request_builder.AndroidForWorkSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def android_managed_store_account_enterprise_settings(self) -> android_managed_store_account_enterprise_settings_request_builder.AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder:
        """
        Provides operations to manage the androidManagedStoreAccountEnterpriseSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .android_managed_store_account_enterprise_settings import android_managed_store_account_enterprise_settings_request_builder

        return android_managed_store_account_enterprise_settings_request_builder.AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def android_managed_store_app_configuration_schemas(self) -> android_managed_store_app_configuration_schemas_request_builder.AndroidManagedStoreAppConfigurationSchemasRequestBuilder:
        """
        Provides operations to manage the androidManagedStoreAppConfigurationSchemas property of the microsoft.graph.deviceManagement entity.
        """
        from .android_managed_store_app_configuration_schemas import android_managed_store_app_configuration_schemas_request_builder

        return android_managed_store_app_configuration_schemas_request_builder.AndroidManagedStoreAppConfigurationSchemasRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apple_push_notification_certificate(self) -> apple_push_notification_certificate_request_builder.ApplePushNotificationCertificateRequestBuilder:
        """
        Provides operations to manage the applePushNotificationCertificate property of the microsoft.graph.deviceManagement entity.
        """
        from .apple_push_notification_certificate import apple_push_notification_certificate_request_builder

        return apple_push_notification_certificate_request_builder.ApplePushNotificationCertificateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apple_user_initiated_enrollment_profiles(self) -> apple_user_initiated_enrollment_profiles_request_builder.AppleUserInitiatedEnrollmentProfilesRequestBuilder:
        """
        Provides operations to manage the appleUserInitiatedEnrollmentProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .apple_user_initiated_enrollment_profiles import apple_user_initiated_enrollment_profiles_request_builder

        return apple_user_initiated_enrollment_profiles_request_builder.AppleUserInitiatedEnrollmentProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_filters(self) -> assignment_filters_request_builder.AssignmentFiltersRequestBuilder:
        """
        Provides operations to manage the assignmentFilters property of the microsoft.graph.deviceManagement entity.
        """
        from .assignment_filters import assignment_filters_request_builder

        return assignment_filters_request_builder.AssignmentFiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def audit_events(self) -> audit_events_request_builder.AuditEventsRequestBuilder:
        """
        Provides operations to manage the auditEvents property of the microsoft.graph.deviceManagement entity.
        """
        from .audit_events import audit_events_request_builder

        return audit_events_request_builder.AuditEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def autopilot_events(self) -> autopilot_events_request_builder.AutopilotEventsRequestBuilder:
        """
        Provides operations to manage the autopilotEvents property of the microsoft.graph.deviceManagement entity.
        """
        from .autopilot_events import autopilot_events_request_builder

        return autopilot_events_request_builder.AutopilotEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cart_to_class_associations(self) -> cart_to_class_associations_request_builder.CartToClassAssociationsRequestBuilder:
        """
        Provides operations to manage the cartToClassAssociations property of the microsoft.graph.deviceManagement entity.
        """
        from .cart_to_class_associations import cart_to_class_associations_request_builder

        return cart_to_class_associations_request_builder.CartToClassAssociationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def categories(self) -> categories_request_builder.CategoriesRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.deviceManagement entity.
        """
        from .categories import categories_request_builder

        return categories_request_builder.CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def certificate_connector_details(self) -> certificate_connector_details_request_builder.CertificateConnectorDetailsRequestBuilder:
        """
        Provides operations to manage the certificateConnectorDetails property of the microsoft.graph.deviceManagement entity.
        """
        from .certificate_connector_details import certificate_connector_details_request_builder

        return certificate_connector_details_request_builder.CertificateConnectorDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chrome_o_s_onboarding_settings(self) -> chrome_o_s_onboarding_settings_request_builder.ChromeOSOnboardingSettingsRequestBuilder:
        """
        Provides operations to manage the chromeOSOnboardingSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .chrome_o_s_onboarding_settings import chrome_o_s_onboarding_settings_request_builder

        return chrome_o_s_onboarding_settings_request_builder.ChromeOSOnboardingSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_p_c_connectivity_issues(self) -> cloud_p_c_connectivity_issues_request_builder.CloudPCConnectivityIssuesRequestBuilder:
        """
        Provides operations to manage the cloudPCConnectivityIssues property of the microsoft.graph.deviceManagement entity.
        """
        from .cloud_p_c_connectivity_issues import cloud_p_c_connectivity_issues_request_builder

        return cloud_p_c_connectivity_issues_request_builder.CloudPCConnectivityIssuesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def comanaged_devices(self) -> comanaged_devices_request_builder.ComanagedDevicesRequestBuilder:
        """
        Provides operations to manage the comanagedDevices property of the microsoft.graph.deviceManagement entity.
        """
        from .comanaged_devices import comanaged_devices_request_builder

        return comanaged_devices_request_builder.ComanagedDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def comanagement_eligible_devices(self) -> comanagement_eligible_devices_request_builder.ComanagementEligibleDevicesRequestBuilder:
        """
        Provides operations to manage the comanagementEligibleDevices property of the microsoft.graph.deviceManagement entity.
        """
        from .comanagement_eligible_devices import comanagement_eligible_devices_request_builder

        return comanagement_eligible_devices_request_builder.ComanagementEligibleDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance_categories(self) -> compliance_categories_request_builder.ComplianceCategoriesRequestBuilder:
        """
        Provides operations to manage the complianceCategories property of the microsoft.graph.deviceManagement entity.
        """
        from .compliance_categories import compliance_categories_request_builder

        return compliance_categories_request_builder.ComplianceCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance_management_partners(self) -> compliance_management_partners_request_builder.ComplianceManagementPartnersRequestBuilder:
        """
        Provides operations to manage the complianceManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        from .compliance_management_partners import compliance_management_partners_request_builder

        return compliance_management_partners_request_builder.ComplianceManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance_policies(self) -> compliance_policies_request_builder.CompliancePoliciesRequestBuilder:
        """
        Provides operations to manage the compliancePolicies property of the microsoft.graph.deviceManagement entity.
        """
        from .compliance_policies import compliance_policies_request_builder

        return compliance_policies_request_builder.CompliancePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance_settings(self) -> compliance_settings_request_builder.ComplianceSettingsRequestBuilder:
        """
        Provides operations to manage the complianceSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .compliance_settings import compliance_settings_request_builder

        return compliance_settings_request_builder.ComplianceSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conditional_access_settings(self) -> conditional_access_settings_request_builder.ConditionalAccessSettingsRequestBuilder:
        """
        Provides operations to manage the conditionalAccessSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .conditional_access_settings import conditional_access_settings_request_builder

        return conditional_access_settings_request_builder.ConditionalAccessSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def config_manager_collections(self) -> config_manager_collections_request_builder.ConfigManagerCollectionsRequestBuilder:
        """
        Provides operations to manage the configManagerCollections property of the microsoft.graph.deviceManagement entity.
        """
        from .config_manager_collections import config_manager_collections_request_builder

        return config_manager_collections_request_builder.ConfigManagerCollectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration_categories(self) -> configuration_categories_request_builder.ConfigurationCategoriesRequestBuilder:
        """
        Provides operations to manage the configurationCategories property of the microsoft.graph.deviceManagement entity.
        """
        from .configuration_categories import configuration_categories_request_builder

        return configuration_categories_request_builder.ConfigurationCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration_policies(self) -> configuration_policies_request_builder.ConfigurationPoliciesRequestBuilder:
        """
        Provides operations to manage the configurationPolicies property of the microsoft.graph.deviceManagement entity.
        """
        from .configuration_policies import configuration_policies_request_builder

        return configuration_policies_request_builder.ConfigurationPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration_policy_templates(self) -> configuration_policy_templates_request_builder.ConfigurationPolicyTemplatesRequestBuilder:
        """
        Provides operations to manage the configurationPolicyTemplates property of the microsoft.graph.deviceManagement entity.
        """
        from .configuration_policy_templates import configuration_policy_templates_request_builder

        return configuration_policy_templates_request_builder.ConfigurationPolicyTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration_settings(self) -> configuration_settings_request_builder.ConfigurationSettingsRequestBuilder:
        """
        Provides operations to manage the configurationSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .configuration_settings import configuration_settings_request_builder

        return configuration_settings_request_builder.ConfigurationSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_sharing_consents(self) -> data_sharing_consents_request_builder.DataSharingConsentsRequestBuilder:
        """
        Provides operations to manage the dataSharingConsents property of the microsoft.graph.deviceManagement entity.
        """
        from .data_sharing_consents import data_sharing_consents_request_builder

        return data_sharing_consents_request_builder.DataSharingConsentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dep_onboarding_settings(self) -> dep_onboarding_settings_request_builder.DepOnboardingSettingsRequestBuilder:
        """
        Provides operations to manage the depOnboardingSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .dep_onboarding_settings import dep_onboarding_settings_request_builder

        return dep_onboarding_settings_request_builder.DepOnboardingSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def derived_credentials(self) -> derived_credentials_request_builder.DerivedCredentialsRequestBuilder:
        """
        Provides operations to manage the derivedCredentials property of the microsoft.graph.deviceManagement entity.
        """
        from .derived_credentials import derived_credentials_request_builder

        return derived_credentials_request_builder.DerivedCredentialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def detected_apps(self) -> detected_apps_request_builder.DetectedAppsRequestBuilder:
        """
        Provides operations to manage the detectedApps property of the microsoft.graph.deviceManagement entity.
        """
        from .detected_apps import detected_apps_request_builder

        return detected_apps_request_builder.DetectedAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_categories(self) -> device_categories_request_builder.DeviceCategoriesRequestBuilder:
        """
        Provides operations to manage the deviceCategories property of the microsoft.graph.deviceManagement entity.
        """
        from .device_categories import device_categories_request_builder

        return device_categories_request_builder.DeviceCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policies(self) -> device_compliance_policies_request_builder.DeviceCompliancePoliciesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicies property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_policies import device_compliance_policies_request_builder

        return device_compliance_policies_request_builder.DeviceCompliancePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_device_state_summary(self) -> device_compliance_policy_device_state_summary_request_builder.DeviceCompliancePolicyDeviceStateSummaryRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicyDeviceStateSummary property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_policy_device_state_summary import device_compliance_policy_device_state_summary_request_builder

        return device_compliance_policy_device_state_summary_request_builder.DeviceCompliancePolicyDeviceStateSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_setting_state_summaries(self) -> device_compliance_policy_setting_state_summaries_request_builder.DeviceCompliancePolicySettingStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicySettingStateSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_policy_setting_state_summaries import device_compliance_policy_setting_state_summaries_request_builder

        return device_compliance_policy_setting_state_summaries_request_builder.DeviceCompliancePolicySettingStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_scripts(self) -> device_compliance_scripts_request_builder.DeviceComplianceScriptsRequestBuilder:
        """
        Provides operations to manage the deviceComplianceScripts property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_scripts import device_compliance_scripts_request_builder

        return device_compliance_scripts_request_builder.DeviceComplianceScriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_conflict_summary(self) -> device_configuration_conflict_summary_request_builder.DeviceConfigurationConflictSummaryRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationConflictSummary property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configuration_conflict_summary import device_configuration_conflict_summary_request_builder

        return device_configuration_conflict_summary_request_builder.DeviceConfigurationConflictSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_device_state_summaries(self) -> device_configuration_device_state_summaries_request_builder.DeviceConfigurationDeviceStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationDeviceStateSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configuration_device_state_summaries import device_configuration_device_state_summaries_request_builder

        return device_configuration_device_state_summaries_request_builder.DeviceConfigurationDeviceStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_restricted_apps_violations(self) -> device_configuration_restricted_apps_violations_request_builder.DeviceConfigurationRestrictedAppsViolationsRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationRestrictedAppsViolations property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configuration_restricted_apps_violations import device_configuration_restricted_apps_violations_request_builder

        return device_configuration_restricted_apps_violations_request_builder.DeviceConfigurationRestrictedAppsViolationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configurations(self) -> device_configurations_request_builder.DeviceConfigurationsRequestBuilder:
        """
        Provides operations to manage the deviceConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configurations import device_configurations_request_builder

        return device_configurations_request_builder.DeviceConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configurations_all_managed_device_certificate_states(self) -> device_configurations_all_managed_device_certificate_states_request_builder.DeviceConfigurationsAllManagedDeviceCertificateStatesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationsAllManagedDeviceCertificateStates property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configurations_all_managed_device_certificate_states import device_configurations_all_managed_device_certificate_states_request_builder

        return device_configurations_all_managed_device_certificate_states_request_builder.DeviceConfigurationsAllManagedDeviceCertificateStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_user_state_summaries(self) -> device_configuration_user_state_summaries_request_builder.DeviceConfigurationUserStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationUserStateSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configuration_user_state_summaries import device_configuration_user_state_summaries_request_builder

        return device_configuration_user_state_summaries_request_builder.DeviceConfigurationUserStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_custom_attribute_shell_scripts(self) -> device_custom_attribute_shell_scripts_request_builder.DeviceCustomAttributeShellScriptsRequestBuilder:
        """
        Provides operations to manage the deviceCustomAttributeShellScripts property of the microsoft.graph.deviceManagement entity.
        """
        from .device_custom_attribute_shell_scripts import device_custom_attribute_shell_scripts_request_builder

        return device_custom_attribute_shell_scripts_request_builder.DeviceCustomAttributeShellScriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_enrollment_configurations(self) -> device_enrollment_configurations_request_builder.DeviceEnrollmentConfigurationsRequestBuilder:
        """
        Provides operations to manage the deviceEnrollmentConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        from .device_enrollment_configurations import device_enrollment_configurations_request_builder

        return device_enrollment_configurations_request_builder.DeviceEnrollmentConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_health_scripts(self) -> device_health_scripts_request_builder.DeviceHealthScriptsRequestBuilder:
        """
        Provides operations to manage the deviceHealthScripts property of the microsoft.graph.deviceManagement entity.
        """
        from .device_health_scripts import device_health_scripts_request_builder

        return device_health_scripts_request_builder.DeviceHealthScriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management_partners(self) -> device_management_partners_request_builder.DeviceManagementPartnersRequestBuilder:
        """
        Provides operations to manage the deviceManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        from .device_management_partners import device_management_partners_request_builder

        return device_management_partners_request_builder.DeviceManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management_scripts(self) -> device_management_scripts_request_builder.DeviceManagementScriptsRequestBuilder:
        """
        Provides operations to manage the deviceManagementScripts property of the microsoft.graph.deviceManagement entity.
        """
        from .device_management_scripts import device_management_scripts_request_builder

        return device_management_scripts_request_builder.DeviceManagementScriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_shell_scripts(self) -> device_shell_scripts_request_builder.DeviceShellScriptsRequestBuilder:
        """
        Provides operations to manage the deviceShellScripts property of the microsoft.graph.deviceManagement entity.
        """
        from .device_shell_scripts import device_shell_scripts_request_builder

        return device_shell_scripts_request_builder.DeviceShellScriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def domain_join_connectors(self) -> domain_join_connectors_request_builder.DomainJoinConnectorsRequestBuilder:
        """
        Provides operations to manage the domainJoinConnectors property of the microsoft.graph.deviceManagement entity.
        """
        from .domain_join_connectors import domain_join_connectors_request_builder

        return domain_join_connectors_request_builder.DomainJoinConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def embedded_s_i_m_activation_code_pools(self) -> embedded_s_i_m_activation_code_pools_request_builder.EmbeddedSIMActivationCodePoolsRequestBuilder:
        """
        Provides operations to manage the embeddedSIMActivationCodePools property of the microsoft.graph.deviceManagement entity.
        """
        from .embedded_s_i_m_activation_code_pools import embedded_s_i_m_activation_code_pools_request_builder

        return embedded_s_i_m_activation_code_pools_request_builder.EmbeddedSIMActivationCodePoolsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable_android_device_administrator_enrollment(self) -> enable_android_device_administrator_enrollment_request_builder.EnableAndroidDeviceAdministratorEnrollmentRequestBuilder:
        """
        Provides operations to call the enableAndroidDeviceAdministratorEnrollment method.
        """
        from .enable_android_device_administrator_enrollment import enable_android_device_administrator_enrollment_request_builder

        return enable_android_device_administrator_enrollment_request_builder.EnableAndroidDeviceAdministratorEnrollmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable_legacy_pc_management(self) -> enable_legacy_pc_management_request_builder.EnableLegacyPcManagementRequestBuilder:
        """
        Provides operations to call the enableLegacyPcManagement method.
        """
        from .enable_legacy_pc_management import enable_legacy_pc_management_request_builder

        return enable_legacy_pc_management_request_builder.EnableLegacyPcManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable_unlicensed_adminstrators(self) -> enable_unlicensed_adminstrators_request_builder.EnableUnlicensedAdminstratorsRequestBuilder:
        """
        Provides operations to call the enableUnlicensedAdminstrators method.
        """
        from .enable_unlicensed_adminstrators import enable_unlicensed_adminstrators_request_builder

        return enable_unlicensed_adminstrators_request_builder.EnableUnlicensedAdminstratorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def evaluate_assignment_filter(self) -> evaluate_assignment_filter_request_builder.EvaluateAssignmentFilterRequestBuilder:
        """
        Provides operations to call the evaluateAssignmentFilter method.
        """
        from .evaluate_assignment_filter import evaluate_assignment_filter_request_builder

        return evaluate_assignment_filter_request_builder.EvaluateAssignmentFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange_connectors(self) -> exchange_connectors_request_builder.ExchangeConnectorsRequestBuilder:
        """
        Provides operations to manage the exchangeConnectors property of the microsoft.graph.deviceManagement entity.
        """
        from .exchange_connectors import exchange_connectors_request_builder

        return exchange_connectors_request_builder.ExchangeConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange_on_premises_policies(self) -> exchange_on_premises_policies_request_builder.ExchangeOnPremisesPoliciesRequestBuilder:
        """
        Provides operations to manage the exchangeOnPremisesPolicies property of the microsoft.graph.deviceManagement entity.
        """
        from .exchange_on_premises_policies import exchange_on_premises_policies_request_builder

        return exchange_on_premises_policies_request_builder.ExchangeOnPremisesPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange_on_premises_policy(self) -> exchange_on_premises_policy_request_builder.ExchangeOnPremisesPolicyRequestBuilder:
        """
        Provides operations to manage the exchangeOnPremisesPolicy property of the microsoft.graph.deviceManagement entity.
        """
        from .exchange_on_premises_policy import exchange_on_premises_policy_request_builder

        return exchange_on_premises_policy_request_builder.ExchangeOnPremisesPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_assigned_role_details(self) -> get_assigned_role_details_request_builder.GetAssignedRoleDetailsRequestBuilder:
        """
        Provides operations to call the getAssignedRoleDetails method.
        """
        from .get_assigned_role_details import get_assigned_role_details_request_builder

        return get_assigned_role_details_request_builder.GetAssignedRoleDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_assignment_filters_status_details(self) -> get_assignment_filters_status_details_request_builder.GetAssignmentFiltersStatusDetailsRequestBuilder:
        """
        Provides operations to call the getAssignmentFiltersStatusDetails method.
        """
        from .get_assignment_filters_status_details import get_assignment_filters_status_details_request_builder

        return get_assignment_filters_status_details_request_builder.GetAssignmentFiltersStatusDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_comanaged_devices_summary(self) -> get_comanaged_devices_summary_request_builder.GetComanagedDevicesSummaryRequestBuilder:
        """
        Provides operations to call the getComanagedDevicesSummary method.
        """
        from .get_comanaged_devices_summary import get_comanaged_devices_summary_request_builder

        return get_comanaged_devices_summary_request_builder.GetComanagedDevicesSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_comanagement_eligible_devices_summary(self) -> get_comanagement_eligible_devices_summary_request_builder.GetComanagementEligibleDevicesSummaryRequestBuilder:
        """
        Provides operations to call the getComanagementEligibleDevicesSummary method.
        """
        from .get_comanagement_eligible_devices_summary import get_comanagement_eligible_devices_summary_request_builder

        return get_comanagement_eligible_devices_summary_request_builder.GetComanagementEligibleDevicesSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_effective_permissions(self) -> get_effective_permissions_request_builder.GetEffectivePermissionsRequestBuilder:
        """
        Provides operations to call the getEffectivePermissions method.
        """
        from .get_effective_permissions import get_effective_permissions_request_builder

        return get_effective_permissions_request_builder.GetEffectivePermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_categories(self) -> group_policy_categories_request_builder.GroupPolicyCategoriesRequestBuilder:
        """
        Provides operations to manage the groupPolicyCategories property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_categories import group_policy_categories_request_builder

        return group_policy_categories_request_builder.GroupPolicyCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_configurations(self) -> group_policy_configurations_request_builder.GroupPolicyConfigurationsRequestBuilder:
        """
        Provides operations to manage the groupPolicyConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_configurations import group_policy_configurations_request_builder

        return group_policy_configurations_request_builder.GroupPolicyConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_definition_files(self) -> group_policy_definition_files_request_builder.GroupPolicyDefinitionFilesRequestBuilder:
        """
        Provides operations to manage the groupPolicyDefinitionFiles property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_definition_files import group_policy_definition_files_request_builder

        return group_policy_definition_files_request_builder.GroupPolicyDefinitionFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_definitions(self) -> group_policy_definitions_request_builder.GroupPolicyDefinitionsRequestBuilder:
        """
        Provides operations to manage the groupPolicyDefinitions property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_definitions import group_policy_definitions_request_builder

        return group_policy_definitions_request_builder.GroupPolicyDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_migration_reports(self) -> group_policy_migration_reports_request_builder.GroupPolicyMigrationReportsRequestBuilder:
        """
        Provides operations to manage the groupPolicyMigrationReports property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_migration_reports import group_policy_migration_reports_request_builder

        return group_policy_migration_reports_request_builder.GroupPolicyMigrationReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_object_files(self) -> group_policy_object_files_request_builder.GroupPolicyObjectFilesRequestBuilder:
        """
        Provides operations to manage the groupPolicyObjectFiles property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_object_files import group_policy_object_files_request_builder

        return group_policy_object_files_request_builder.GroupPolicyObjectFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_uploaded_definition_files(self) -> group_policy_uploaded_definition_files_request_builder.GroupPolicyUploadedDefinitionFilesRequestBuilder:
        """
        Provides operations to manage the groupPolicyUploadedDefinitionFiles property of the microsoft.graph.deviceManagement entity.
        """
        from .group_policy_uploaded_definition_files import group_policy_uploaded_definition_files_request_builder

        return group_policy_uploaded_definition_files_request_builder.GroupPolicyUploadedDefinitionFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def imported_device_identities(self) -> imported_device_identities_request_builder.ImportedDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the importedDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        """
        from .imported_device_identities import imported_device_identities_request_builder

        return imported_device_identities_request_builder.ImportedDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def imported_windows_autopilot_device_identities(self) -> imported_windows_autopilot_device_identities_request_builder.ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the importedWindowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        """
        from .imported_windows_autopilot_device_identities import imported_windows_autopilot_device_identities_request_builder

        return imported_windows_autopilot_device_identities_request_builder.ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intents(self) -> intents_request_builder.IntentsRequestBuilder:
        """
        Provides operations to manage the intents property of the microsoft.graph.deviceManagement entity.
        """
        from .intents import intents_request_builder

        return intents_request_builder.IntentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intune_branding_profiles(self) -> intune_branding_profiles_request_builder.IntuneBrandingProfilesRequestBuilder:
        """
        Provides operations to manage the intuneBrandingProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .intune_branding_profiles import intune_branding_profiles_request_builder

        return intune_branding_profiles_request_builder.IntuneBrandingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ios_update_statuses(self) -> ios_update_statuses_request_builder.IosUpdateStatusesRequestBuilder:
        """
        Provides operations to manage the iosUpdateStatuses property of the microsoft.graph.deviceManagement entity.
        """
        from .ios_update_statuses import ios_update_statuses_request_builder

        return ios_update_statuses_request_builder.IosUpdateStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mac_o_s_software_update_account_summaries(self) -> mac_o_s_software_update_account_summaries_request_builder.MacOSSoftwareUpdateAccountSummariesRequestBuilder:
        """
        Provides operations to manage the macOSSoftwareUpdateAccountSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .mac_o_s_software_update_account_summaries import mac_o_s_software_update_account_summaries_request_builder

        return mac_o_s_software_update_account_summaries_request_builder.MacOSSoftwareUpdateAccountSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_encryption_states(self) -> managed_device_encryption_states_request_builder.ManagedDeviceEncryptionStatesRequestBuilder:
        """
        Provides operations to manage the managedDeviceEncryptionStates property of the microsoft.graph.deviceManagement entity.
        """
        from .managed_device_encryption_states import managed_device_encryption_states_request_builder

        return managed_device_encryption_states_request_builder.ManagedDeviceEncryptionStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_overview(self) -> managed_device_overview_request_builder.ManagedDeviceOverviewRequestBuilder:
        """
        Provides operations to manage the managedDeviceOverview property of the microsoft.graph.deviceManagement entity.
        """
        from .managed_device_overview import managed_device_overview_request_builder

        return managed_device_overview_request_builder.ManagedDeviceOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_devices(self) -> managed_devices_request_builder.ManagedDevicesRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.deviceManagement entity.
        """
        from .managed_devices import managed_devices_request_builder

        return managed_devices_request_builder.ManagedDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_tunnel_configurations(self) -> microsoft_tunnel_configurations_request_builder.MicrosoftTunnelConfigurationsRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        from .microsoft_tunnel_configurations import microsoft_tunnel_configurations_request_builder

        return microsoft_tunnel_configurations_request_builder.MicrosoftTunnelConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_tunnel_health_thresholds(self) -> microsoft_tunnel_health_thresholds_request_builder.MicrosoftTunnelHealthThresholdsRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelHealthThresholds property of the microsoft.graph.deviceManagement entity.
        """
        from .microsoft_tunnel_health_thresholds import microsoft_tunnel_health_thresholds_request_builder

        return microsoft_tunnel_health_thresholds_request_builder.MicrosoftTunnelHealthThresholdsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_tunnel_server_log_collection_responses(self) -> microsoft_tunnel_server_log_collection_responses_request_builder.MicrosoftTunnelServerLogCollectionResponsesRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelServerLogCollectionResponses property of the microsoft.graph.deviceManagement entity.
        """
        from .microsoft_tunnel_server_log_collection_responses import microsoft_tunnel_server_log_collection_responses_request_builder

        return microsoft_tunnel_server_log_collection_responses_request_builder.MicrosoftTunnelServerLogCollectionResponsesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_tunnel_sites(self) -> microsoft_tunnel_sites_request_builder.MicrosoftTunnelSitesRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelSites property of the microsoft.graph.deviceManagement entity.
        """
        from .microsoft_tunnel_sites import microsoft_tunnel_sites_request_builder

        return microsoft_tunnel_sites_request_builder.MicrosoftTunnelSitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_troubleshooting_events(self) -> mobile_app_troubleshooting_events_request_builder.MobileAppTroubleshootingEventsRequestBuilder:
        """
        Provides operations to manage the mobileAppTroubleshootingEvents property of the microsoft.graph.deviceManagement entity.
        """
        from .mobile_app_troubleshooting_events import mobile_app_troubleshooting_events_request_builder

        return mobile_app_troubleshooting_events_request_builder.MobileAppTroubleshootingEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_threat_defense_connectors(self) -> mobile_threat_defense_connectors_request_builder.MobileThreatDefenseConnectorsRequestBuilder:
        """
        Provides operations to manage the mobileThreatDefenseConnectors property of the microsoft.graph.deviceManagement entity.
        """
        from .mobile_threat_defense_connectors import mobile_threat_defense_connectors_request_builder

        return mobile_threat_defense_connectors_request_builder.MobileThreatDefenseConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monitoring(self) -> monitoring_request_builder.MonitoringRequestBuilder:
        """
        Provides operations to manage the monitoring property of the microsoft.graph.deviceManagement entity.
        """
        from .monitoring import monitoring_request_builder

        return monitoring_request_builder.MonitoringRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ndes_connectors(self) -> ndes_connectors_request_builder.NdesConnectorsRequestBuilder:
        """
        Provides operations to manage the ndesConnectors property of the microsoft.graph.deviceManagement entity.
        """
        from .ndes_connectors import ndes_connectors_request_builder

        return ndes_connectors_request_builder.NdesConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notification_message_templates(self) -> notification_message_templates_request_builder.NotificationMessageTemplatesRequestBuilder:
        """
        Provides operations to manage the notificationMessageTemplates property of the microsoft.graph.deviceManagement entity.
        """
        from .notification_message_templates import notification_message_templates_request_builder

        return notification_message_templates_request_builder.NotificationMessageTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oem_warranty_information_onboarding(self) -> oem_warranty_information_onboarding_request_builder.OemWarrantyInformationOnboardingRequestBuilder:
        """
        Provides operations to manage the oemWarrantyInformationOnboarding property of the microsoft.graph.deviceManagement entity.
        """
        from .oem_warranty_information_onboarding import oem_warranty_information_onboarding_request_builder

        return oem_warranty_information_onboarding_request_builder.OemWarrantyInformationOnboardingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privilege_management_elevations(self) -> privilege_management_elevations_request_builder.PrivilegeManagementElevationsRequestBuilder:
        """
        Provides operations to manage the privilegeManagementElevations property of the microsoft.graph.deviceManagement entity.
        """
        from .privilege_management_elevations import privilege_management_elevations_request_builder

        return privilege_management_elevations_request_builder.PrivilegeManagementElevationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_action_audits(self) -> remote_action_audits_request_builder.RemoteActionAuditsRequestBuilder:
        """
        Provides operations to manage the remoteActionAudits property of the microsoft.graph.deviceManagement entity.
        """
        from .remote_action_audits import remote_action_audits_request_builder

        return remote_action_audits_request_builder.RemoteActionAuditsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_assistance_partners(self) -> remote_assistance_partners_request_builder.RemoteAssistancePartnersRequestBuilder:
        """
        Provides operations to manage the remoteAssistancePartners property of the microsoft.graph.deviceManagement entity.
        """
        from .remote_assistance_partners import remote_assistance_partners_request_builder

        return remote_assistance_partners_request_builder.RemoteAssistancePartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_assistance_settings(self) -> remote_assistance_settings_request_builder.RemoteAssistanceSettingsRequestBuilder:
        """
        Provides operations to manage the remoteAssistanceSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .remote_assistance_settings import remote_assistance_settings_request_builder

        return remote_assistance_settings_request_builder.RemoteAssistanceSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reports(self) -> reports_request_builder.ReportsRequestBuilder:
        """
        Provides operations to manage the reports property of the microsoft.graph.deviceManagement entity.
        """
        from .reports import reports_request_builder

        return reports_request_builder.ReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_access_profiles(self) -> resource_access_profiles_request_builder.ResourceAccessProfilesRequestBuilder:
        """
        Provides operations to manage the resourceAccessProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .resource_access_profiles import resource_access_profiles_request_builder

        return resource_access_profiles_request_builder.ResourceAccessProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_operations(self) -> resource_operations_request_builder.ResourceOperationsRequestBuilder:
        """
        Provides operations to manage the resourceOperations property of the microsoft.graph.deviceManagement entity.
        """
        from .resource_operations import resource_operations_request_builder

        return resource_operations_request_builder.ResourceOperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reusable_policy_settings(self) -> reusable_policy_settings_request_builder.ReusablePolicySettingsRequestBuilder:
        """
        Provides operations to manage the reusablePolicySettings property of the microsoft.graph.deviceManagement entity.
        """
        from .reusable_policy_settings import reusable_policy_settings_request_builder

        return reusable_policy_settings_request_builder.ReusablePolicySettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reusable_settings(self) -> reusable_settings_request_builder.ReusableSettingsRequestBuilder:
        """
        Provides operations to manage the reusableSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .reusable_settings import reusable_settings_request_builder

        return reusable_settings_request_builder.ReusableSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignments(self) -> role_assignments_request_builder.RoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.deviceManagement entity.
        """
        from .role_assignments import role_assignments_request_builder

        return role_assignments_request_builder.RoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definitions(self) -> role_definitions_request_builder.RoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.deviceManagement entity.
        """
        from .role_definitions import role_definitions_request_builder

        return role_definitions_request_builder.RoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_scope_tags(self) -> role_scope_tags_request_builder.RoleScopeTagsRequestBuilder:
        """
        Provides operations to manage the roleScopeTags property of the microsoft.graph.deviceManagement entity.
        """
        from .role_scope_tags import role_scope_tags_request_builder

        return role_scope_tags_request_builder.RoleScopeTagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_custom_notification_to_company_portal(self) -> send_custom_notification_to_company_portal_request_builder.SendCustomNotificationToCompanyPortalRequestBuilder:
        """
        Provides operations to call the sendCustomNotificationToCompanyPortal method.
        """
        from .send_custom_notification_to_company_portal import send_custom_notification_to_company_portal_request_builder

        return send_custom_notification_to_company_portal_request_builder.SendCustomNotificationToCompanyPortalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_now_connections(self) -> service_now_connections_request_builder.ServiceNowConnectionsRequestBuilder:
        """
        Provides operations to manage the serviceNowConnections property of the microsoft.graph.deviceManagement entity.
        """
        from .service_now_connections import service_now_connections_request_builder

        return service_now_connections_request_builder.ServiceNowConnectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def setting_definitions(self) -> setting_definitions_request_builder.SettingDefinitionsRequestBuilder:
        """
        Provides operations to manage the settingDefinitions property of the microsoft.graph.deviceManagement entity.
        """
        from .setting_definitions import setting_definitions_request_builder

        return setting_definitions_request_builder.SettingDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def software_update_status_summary(self) -> software_update_status_summary_request_builder.SoftwareUpdateStatusSummaryRequestBuilder:
        """
        Provides operations to manage the softwareUpdateStatusSummary property of the microsoft.graph.deviceManagement entity.
        """
        from .software_update_status_summary import software_update_status_summary_request_builder

        return software_update_status_summary_request_builder.SoftwareUpdateStatusSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def telecom_expense_management_partners(self) -> telecom_expense_management_partners_request_builder.TelecomExpenseManagementPartnersRequestBuilder:
        """
        Provides operations to manage the telecomExpenseManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        from .telecom_expense_management_partners import telecom_expense_management_partners_request_builder

        return telecom_expense_management_partners_request_builder.TelecomExpenseManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def templates(self) -> templates_request_builder.TemplatesRequestBuilder:
        """
        Provides operations to manage the templates property of the microsoft.graph.deviceManagement entity.
        """
        from .templates import templates_request_builder

        return templates_request_builder.TemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def template_settings(self) -> template_settings_request_builder.TemplateSettingsRequestBuilder:
        """
        Provides operations to manage the templateSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .template_settings import template_settings_request_builder

        return template_settings_request_builder.TemplateSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenant_attach_r_b_a_c(self) -> tenant_attach_r_b_a_c_request_builder.TenantAttachRBACRequestBuilder:
        """
        Provides operations to manage the tenantAttachRBAC property of the microsoft.graph.deviceManagement entity.
        """
        from .tenant_attach_r_b_a_c import tenant_attach_r_b_a_c_request_builder

        return tenant_attach_r_b_a_c_request_builder.TenantAttachRBACRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def terms_and_conditions(self) -> terms_and_conditions_request_builder.TermsAndConditionsRequestBuilder:
        """
        Provides operations to manage the termsAndConditions property of the microsoft.graph.deviceManagement entity.
        """
        from .terms_and_conditions import terms_and_conditions_request_builder

        return terms_and_conditions_request_builder.TermsAndConditionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def troubleshooting_events(self) -> troubleshooting_events_request_builder.TroubleshootingEventsRequestBuilder:
        """
        Provides operations to manage the troubleshootingEvents property of the microsoft.graph.deviceManagement entity.
        """
        from .troubleshooting_events import troubleshooting_events_request_builder

        return troubleshooting_events_request_builder.TroubleshootingEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_anomaly(self) -> user_experience_analytics_anomaly_request_builder.UserExperienceAnalyticsAnomalyRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAnomaly property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_anomaly import user_experience_analytics_anomaly_request_builder

        return user_experience_analytics_anomaly_request_builder.UserExperienceAnalyticsAnomalyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_anomaly_device(self) -> user_experience_analytics_anomaly_device_request_builder.UserExperienceAnalyticsAnomalyDeviceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAnomalyDevice property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_anomaly_device import user_experience_analytics_anomaly_device_request_builder

        return user_experience_analytics_anomaly_device_request_builder.UserExperienceAnalyticsAnomalyDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_application_performance(self) -> user_experience_analytics_app_health_application_performance_request_builder.UserExperienceAnalyticsAppHealthApplicationPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance import user_experience_analytics_app_health_application_performance_request_builder

        return user_experience_analytics_app_health_application_performance_request_builder.UserExperienceAnalyticsAppHealthApplicationPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_application_performance_by_app_version(self) -> user_experience_analytics_app_health_application_performance_by_app_version_request_builder.UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance_by_app_version import user_experience_analytics_app_health_application_performance_by_app_version_request_builder

        return user_experience_analytics_app_health_application_performance_by_app_version_request_builder.UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_application_performance_by_app_version_details(self) -> user_experience_analytics_app_health_application_performance_by_app_version_details_request_builder.UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance_by_app_version_details import user_experience_analytics_app_health_application_performance_by_app_version_details_request_builder

        return user_experience_analytics_app_health_application_performance_by_app_version_details_request_builder.UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_application_performance_by_app_version_device_id(self) -> user_experience_analytics_app_health_application_performance_by_app_version_device_id_request_builder.UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance_by_app_version_device_id import user_experience_analytics_app_health_application_performance_by_app_version_device_id_request_builder

        return user_experience_analytics_app_health_application_performance_by_app_version_device_id_request_builder.UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_application_performance_by_o_s_version(self) -> user_experience_analytics_app_health_application_performance_by_o_s_version_request_builder.UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance_by_o_s_version import user_experience_analytics_app_health_application_performance_by_o_s_version_request_builder

        return user_experience_analytics_app_health_application_performance_by_o_s_version_request_builder.UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_device_model_performance(self) -> user_experience_analytics_app_health_device_model_performance_request_builder.UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthDeviceModelPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_device_model_performance import user_experience_analytics_app_health_device_model_performance_request_builder

        return user_experience_analytics_app_health_device_model_performance_request_builder.UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_device_performance(self) -> user_experience_analytics_app_health_device_performance_request_builder.UserExperienceAnalyticsAppHealthDevicePerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthDevicePerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_device_performance import user_experience_analytics_app_health_device_performance_request_builder

        return user_experience_analytics_app_health_device_performance_request_builder.UserExperienceAnalyticsAppHealthDevicePerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_device_performance_details(self) -> user_experience_analytics_app_health_device_performance_details_request_builder.UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthDevicePerformanceDetails property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_device_performance_details import user_experience_analytics_app_health_device_performance_details_request_builder

        return user_experience_analytics_app_health_device_performance_details_request_builder.UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_o_s_version_performance(self) -> user_experience_analytics_app_health_o_s_version_performance_request_builder.UserExperienceAnalyticsAppHealthOSVersionPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthOSVersionPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_o_s_version_performance import user_experience_analytics_app_health_o_s_version_performance_request_builder

        return user_experience_analytics_app_health_o_s_version_performance_request_builder.UserExperienceAnalyticsAppHealthOSVersionPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_overview(self) -> user_experience_analytics_app_health_overview_request_builder.UserExperienceAnalyticsAppHealthOverviewRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthOverview property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_overview import user_experience_analytics_app_health_overview_request_builder

        return user_experience_analytics_app_health_overview_request_builder.UserExperienceAnalyticsAppHealthOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_baselines(self) -> user_experience_analytics_baselines_request_builder.UserExperienceAnalyticsBaselinesRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBaselines property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_baselines import user_experience_analytics_baselines_request_builder

        return user_experience_analytics_baselines_request_builder.UserExperienceAnalyticsBaselinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_app_impact(self) -> user_experience_analytics_battery_health_app_impact_request_builder.UserExperienceAnalyticsBatteryHealthAppImpactRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthAppImpact property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_app_impact import user_experience_analytics_battery_health_app_impact_request_builder

        return user_experience_analytics_battery_health_app_impact_request_builder.UserExperienceAnalyticsBatteryHealthAppImpactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_capacity_details(self) -> user_experience_analytics_battery_health_capacity_details_request_builder.UserExperienceAnalyticsBatteryHealthCapacityDetailsRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthCapacityDetails property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_capacity_details import user_experience_analytics_battery_health_capacity_details_request_builder

        return user_experience_analytics_battery_health_capacity_details_request_builder.UserExperienceAnalyticsBatteryHealthCapacityDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_device_app_impact(self) -> user_experience_analytics_battery_health_device_app_impact_request_builder.UserExperienceAnalyticsBatteryHealthDeviceAppImpactRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthDeviceAppImpact property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_device_app_impact import user_experience_analytics_battery_health_device_app_impact_request_builder

        return user_experience_analytics_battery_health_device_app_impact_request_builder.UserExperienceAnalyticsBatteryHealthDeviceAppImpactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_device_performance(self) -> user_experience_analytics_battery_health_device_performance_request_builder.UserExperienceAnalyticsBatteryHealthDevicePerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthDevicePerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_device_performance import user_experience_analytics_battery_health_device_performance_request_builder

        return user_experience_analytics_battery_health_device_performance_request_builder.UserExperienceAnalyticsBatteryHealthDevicePerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_device_runtime_history(self) -> user_experience_analytics_battery_health_device_runtime_history_request_builder.UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistoryRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_device_runtime_history import user_experience_analytics_battery_health_device_runtime_history_request_builder

        return user_experience_analytics_battery_health_device_runtime_history_request_builder.UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_model_performance(self) -> user_experience_analytics_battery_health_model_performance_request_builder.UserExperienceAnalyticsBatteryHealthModelPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthModelPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_model_performance import user_experience_analytics_battery_health_model_performance_request_builder

        return user_experience_analytics_battery_health_model_performance_request_builder.UserExperienceAnalyticsBatteryHealthModelPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_os_performance(self) -> user_experience_analytics_battery_health_os_performance_request_builder.UserExperienceAnalyticsBatteryHealthOsPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthOsPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_os_performance import user_experience_analytics_battery_health_os_performance_request_builder

        return user_experience_analytics_battery_health_os_performance_request_builder.UserExperienceAnalyticsBatteryHealthOsPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_battery_health_runtime_details(self) -> user_experience_analytics_battery_health_runtime_details_request_builder.UserExperienceAnalyticsBatteryHealthRuntimeDetailsRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBatteryHealthRuntimeDetails property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_battery_health_runtime_details import user_experience_analytics_battery_health_runtime_details_request_builder

        return user_experience_analytics_battery_health_runtime_details_request_builder.UserExperienceAnalyticsBatteryHealthRuntimeDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_categories(self) -> user_experience_analytics_categories_request_builder.UserExperienceAnalyticsCategoriesRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsCategories property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_categories import user_experience_analytics_categories_request_builder

        return user_experience_analytics_categories_request_builder.UserExperienceAnalyticsCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_metric_history(self) -> user_experience_analytics_device_metric_history_request_builder.UserExperienceAnalyticsDeviceMetricHistoryRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceMetricHistory property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_metric_history import user_experience_analytics_device_metric_history_request_builder

        return user_experience_analytics_device_metric_history_request_builder.UserExperienceAnalyticsDeviceMetricHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_performance(self) -> user_experience_analytics_device_performance_request_builder.UserExperienceAnalyticsDevicePerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDevicePerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_performance import user_experience_analytics_device_performance_request_builder

        return user_experience_analytics_device_performance_request_builder.UserExperienceAnalyticsDevicePerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_scope(self) -> user_experience_analytics_device_scope_request_builder.UserExperienceAnalyticsDeviceScopeRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceScope property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_scope import user_experience_analytics_device_scope_request_builder

        return user_experience_analytics_device_scope_request_builder.UserExperienceAnalyticsDeviceScopeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_scopes(self) -> user_experience_analytics_device_scopes_request_builder.UserExperienceAnalyticsDeviceScopesRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceScopes property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_scopes import user_experience_analytics_device_scopes_request_builder

        return user_experience_analytics_device_scopes_request_builder.UserExperienceAnalyticsDeviceScopesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_scores(self) -> user_experience_analytics_device_scores_request_builder.UserExperienceAnalyticsDeviceScoresRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceScores property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_scores import user_experience_analytics_device_scores_request_builder

        return user_experience_analytics_device_scores_request_builder.UserExperienceAnalyticsDeviceScoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_startup_history(self) -> user_experience_analytics_device_startup_history_request_builder.UserExperienceAnalyticsDeviceStartupHistoryRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceStartupHistory property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_startup_history import user_experience_analytics_device_startup_history_request_builder

        return user_experience_analytics_device_startup_history_request_builder.UserExperienceAnalyticsDeviceStartupHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_startup_processes(self) -> user_experience_analytics_device_startup_processes_request_builder.UserExperienceAnalyticsDeviceStartupProcessesRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceStartupProcesses property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_startup_processes import user_experience_analytics_device_startup_processes_request_builder

        return user_experience_analytics_device_startup_processes_request_builder.UserExperienceAnalyticsDeviceStartupProcessesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_startup_process_performance(self) -> user_experience_analytics_device_startup_process_performance_request_builder.UserExperienceAnalyticsDeviceStartupProcessPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceStartupProcessPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_startup_process_performance import user_experience_analytics_device_startup_process_performance_request_builder

        return user_experience_analytics_device_startup_process_performance_request_builder.UserExperienceAnalyticsDeviceStartupProcessPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_devices_without_cloud_identity(self) -> user_experience_analytics_devices_without_cloud_identity_request_builder.UserExperienceAnalyticsDevicesWithoutCloudIdentityRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDevicesWithoutCloudIdentity property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_devices_without_cloud_identity import user_experience_analytics_devices_without_cloud_identity_request_builder

        return user_experience_analytics_devices_without_cloud_identity_request_builder.UserExperienceAnalyticsDevicesWithoutCloudIdentityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_timeline_event(self) -> user_experience_analytics_device_timeline_event_request_builder.UserExperienceAnalyticsDeviceTimelineEventRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceTimelineEvent property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_timeline_event import user_experience_analytics_device_timeline_event_request_builder

        return user_experience_analytics_device_timeline_event_request_builder.UserExperienceAnalyticsDeviceTimelineEventRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_impacting_process(self) -> user_experience_analytics_impacting_process_request_builder.UserExperienceAnalyticsImpactingProcessRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsImpactingProcess property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_impacting_process import user_experience_analytics_impacting_process_request_builder

        return user_experience_analytics_impacting_process_request_builder.UserExperienceAnalyticsImpactingProcessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_metric_history(self) -> user_experience_analytics_metric_history_request_builder.UserExperienceAnalyticsMetricHistoryRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsMetricHistory property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_metric_history import user_experience_analytics_metric_history_request_builder

        return user_experience_analytics_metric_history_request_builder.UserExperienceAnalyticsMetricHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_model_scores(self) -> user_experience_analytics_model_scores_request_builder.UserExperienceAnalyticsModelScoresRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsModelScores property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_model_scores import user_experience_analytics_model_scores_request_builder

        return user_experience_analytics_model_scores_request_builder.UserExperienceAnalyticsModelScoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_not_autopilot_ready_device(self) -> user_experience_analytics_not_autopilot_ready_device_request_builder.UserExperienceAnalyticsNotAutopilotReadyDeviceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsNotAutopilotReadyDevice property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_not_autopilot_ready_device import user_experience_analytics_not_autopilot_ready_device_request_builder

        return user_experience_analytics_not_autopilot_ready_device_request_builder.UserExperienceAnalyticsNotAutopilotReadyDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_overview(self) -> user_experience_analytics_overview_request_builder.UserExperienceAnalyticsOverviewRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsOverview property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_overview import user_experience_analytics_overview_request_builder

        return user_experience_analytics_overview_request_builder.UserExperienceAnalyticsOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_remote_connection(self) -> user_experience_analytics_remote_connection_request_builder.UserExperienceAnalyticsRemoteConnectionRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsRemoteConnection property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_remote_connection import user_experience_analytics_remote_connection_request_builder

        return user_experience_analytics_remote_connection_request_builder.UserExperienceAnalyticsRemoteConnectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_resource_performance(self) -> user_experience_analytics_resource_performance_request_builder.UserExperienceAnalyticsResourcePerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsResourcePerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_resource_performance import user_experience_analytics_resource_performance_request_builder

        return user_experience_analytics_resource_performance_request_builder.UserExperienceAnalyticsResourcePerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_score_history(self) -> user_experience_analytics_score_history_request_builder.UserExperienceAnalyticsScoreHistoryRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsScoreHistory property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_score_history import user_experience_analytics_score_history_request_builder

        return user_experience_analytics_score_history_request_builder.UserExperienceAnalyticsScoreHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_summarized_device_scopes(self) -> user_experience_analytics_summarized_device_scopes_request_builder.UserExperienceAnalyticsSummarizedDeviceScopesRequestBuilder:
        """
        Provides operations to call the userExperienceAnalyticsSummarizedDeviceScopes method.
        """
        from .user_experience_analytics_summarized_device_scopes import user_experience_analytics_summarized_device_scopes_request_builder

        return user_experience_analytics_summarized_device_scopes_request_builder.UserExperienceAnalyticsSummarizedDeviceScopesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_summarize_work_from_anywhere_devices(self) -> user_experience_analytics_summarize_work_from_anywhere_devices_request_builder.UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequestBuilder:
        """
        Provides operations to call the userExperienceAnalyticsSummarizeWorkFromAnywhereDevices method.
        """
        from .user_experience_analytics_summarize_work_from_anywhere_devices import user_experience_analytics_summarize_work_from_anywhere_devices_request_builder

        return user_experience_analytics_summarize_work_from_anywhere_devices_request_builder.UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_work_from_anywhere_hardware_readiness_metric(self) -> user_experience_analytics_work_from_anywhere_hardware_readiness_metric_request_builder.UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import user_experience_analytics_work_from_anywhere_hardware_readiness_metric_request_builder

        return user_experience_analytics_work_from_anywhere_hardware_readiness_metric_request_builder.UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_work_from_anywhere_metrics(self) -> user_experience_analytics_work_from_anywhere_metrics_request_builder.UserExperienceAnalyticsWorkFromAnywhereMetricsRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsWorkFromAnywhereMetrics property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_work_from_anywhere_metrics import user_experience_analytics_work_from_anywhere_metrics_request_builder

        return user_experience_analytics_work_from_anywhere_metrics_request_builder.UserExperienceAnalyticsWorkFromAnywhereMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_work_from_anywhere_model_performance(self) -> user_experience_analytics_work_from_anywhere_model_performance_request_builder.UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsWorkFromAnywhereModelPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_work_from_anywhere_model_performance import user_experience_analytics_work_from_anywhere_model_performance_request_builder

        return user_experience_analytics_work_from_anywhere_model_performance_request_builder.UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_pfx_certificates(self) -> user_pfx_certificates_request_builder.UserPfxCertificatesRequestBuilder:
        """
        Provides operations to manage the userPfxCertificates property of the microsoft.graph.deviceManagement entity.
        """
        from .user_pfx_certificates import user_pfx_certificates_request_builder

        return user_pfx_certificates_request_builder.UserPfxCertificatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def virtual_endpoint(self) -> virtual_endpoint_request_builder.VirtualEndpointRequestBuilder:
        """
        Provides operations to manage the virtualEndpoint property of the microsoft.graph.deviceManagement entity.
        """
        from .virtual_endpoint import virtual_endpoint_request_builder

        return virtual_endpoint_request_builder.VirtualEndpointRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_autopilot_deployment_profiles(self) -> windows_autopilot_deployment_profiles_request_builder.WindowsAutopilotDeploymentProfilesRequestBuilder:
        """
        Provides operations to manage the windowsAutopilotDeploymentProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_autopilot_deployment_profiles import windows_autopilot_deployment_profiles_request_builder

        return windows_autopilot_deployment_profiles_request_builder.WindowsAutopilotDeploymentProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_autopilot_device_identities(self) -> windows_autopilot_device_identities_request_builder.WindowsAutopilotDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the windowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_autopilot_device_identities import windows_autopilot_device_identities_request_builder

        return windows_autopilot_device_identities_request_builder.WindowsAutopilotDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_autopilot_settings(self) -> windows_autopilot_settings_request_builder.WindowsAutopilotSettingsRequestBuilder:
        """
        Provides operations to manage the windowsAutopilotSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_autopilot_settings import windows_autopilot_settings_request_builder

        return windows_autopilot_settings_request_builder.WindowsAutopilotSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_driver_update_profiles(self) -> windows_driver_update_profiles_request_builder.WindowsDriverUpdateProfilesRequestBuilder:
        """
        Provides operations to manage the windowsDriverUpdateProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_driver_update_profiles import windows_driver_update_profiles_request_builder

        return windows_driver_update_profiles_request_builder.WindowsDriverUpdateProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_feature_update_profiles(self) -> windows_feature_update_profiles_request_builder.WindowsFeatureUpdateProfilesRequestBuilder:
        """
        Provides operations to manage the windowsFeatureUpdateProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_feature_update_profiles import windows_feature_update_profiles_request_builder

        return windows_feature_update_profiles_request_builder.WindowsFeatureUpdateProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_app_learning_summaries(self) -> windows_information_protection_app_learning_summaries_request_builder.WindowsInformationProtectionAppLearningSummariesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionAppLearningSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_information_protection_app_learning_summaries import windows_information_protection_app_learning_summaries_request_builder

        return windows_information_protection_app_learning_summaries_request_builder.WindowsInformationProtectionAppLearningSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_network_learning_summaries(self) -> windows_information_protection_network_learning_summaries_request_builder.WindowsInformationProtectionNetworkLearningSummariesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionNetworkLearningSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_information_protection_network_learning_summaries import windows_information_protection_network_learning_summaries_request_builder

        return windows_information_protection_network_learning_summaries_request_builder.WindowsInformationProtectionNetworkLearningSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_malware_information(self) -> windows_malware_information_request_builder.WindowsMalwareInformationRequestBuilder:
        """
        Provides operations to manage the windowsMalwareInformation property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_malware_information import windows_malware_information_request_builder

        return windows_malware_information_request_builder.WindowsMalwareInformationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_quality_update_profiles(self) -> windows_quality_update_profiles_request_builder.WindowsQualityUpdateProfilesRequestBuilder:
        """
        Provides operations to manage the windowsQualityUpdateProfiles property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_quality_update_profiles import windows_quality_update_profiles_request_builder

        return windows_quality_update_profiles_request_builder.WindowsQualityUpdateProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_update_catalog_items(self) -> windows_update_catalog_items_request_builder.WindowsUpdateCatalogItemsRequestBuilder:
        """
        Provides operations to manage the windowsUpdateCatalogItems property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_update_catalog_items import windows_update_catalog_items_request_builder

        return windows_update_catalog_items_request_builder.WindowsUpdateCatalogItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def zebra_fota_artifacts(self) -> zebra_fota_artifacts_request_builder.ZebraFotaArtifactsRequestBuilder:
        """
        Provides operations to manage the zebraFotaArtifacts property of the microsoft.graph.deviceManagement entity.
        """
        from .zebra_fota_artifacts import zebra_fota_artifacts_request_builder

        return zebra_fota_artifacts_request_builder.ZebraFotaArtifactsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def zebra_fota_connector(self) -> zebra_fota_connector_request_builder.ZebraFotaConnectorRequestBuilder:
        """
        Provides operations to manage the zebraFotaConnector property of the microsoft.graph.deviceManagement entity.
        """
        from .zebra_fota_connector import zebra_fota_connector_request_builder

        return zebra_fota_connector_request_builder.ZebraFotaConnectorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def zebra_fota_deployments(self) -> zebra_fota_deployments_request_builder.ZebraFotaDeploymentsRequestBuilder:
        """
        Provides operations to manage the zebraFotaDeployments property of the microsoft.graph.deviceManagement entity.
        """
        from .zebra_fota_deployments import zebra_fota_deployments_request_builder

        return zebra_fota_deployments_request_builder.ZebraFotaDeploymentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceManagementRequestBuilderGetQueryParameters():
        """
        Get deviceManagement
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
    class DeviceManagementRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceManagementRequestBuilder.DeviceManagementRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceManagementRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

