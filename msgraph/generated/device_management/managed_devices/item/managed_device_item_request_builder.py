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

assignment_filter_evaluation_status_details_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.assignment_filter_evaluation_status_details.assignment_filter_evaluation_status_details_request_builder')
assignment_filter_evaluation_status_details_item_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.assignment_filter_evaluation_status_details.item.assignment_filter_evaluation_status_details_item_request_builder')
detected_apps_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.detected_apps.detected_apps_request_builder')
detected_app_item_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.detected_apps.item.detected_app_item_request_builder')
device_category_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.device_category.device_category_request_builder')
device_compliance_policy_states_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.device_compliance_policy_states.device_compliance_policy_states_request_builder')
device_compliance_policy_state_item_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.device_compliance_policy_states.item.device_compliance_policy_state_item_request_builder')
device_configuration_states_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.device_configuration_states.device_configuration_states_request_builder')
device_configuration_state_item_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.device_configuration_states.item.device_configuration_state_item_request_builder')
device_health_script_states_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.device_health_script_states.device_health_script_states_request_builder')
log_collection_requests_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.log_collection_requests.log_collection_requests_request_builder')
device_log_collection_response_item_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.log_collection_requests.item.device_log_collection_response_item_request_builder')
managed_device_mobile_app_configuration_states_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.managed_device_mobile_app_configuration_states.managed_device_mobile_app_configuration_states_request_builder')
managed_device_mobile_app_configuration_state_item_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.managed_device_mobile_app_configuration_states.item.managed_device_mobile_app_configuration_state_item_request_builder')
microsoft_graph_activate_device_esim_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_activate_device_esim.microsoft_graph_activate_device_esim_request_builder')
microsoft_graph_bypass_activation_lock_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_bypass_activation_lock.microsoft_graph_bypass_activation_lock_request_builder')
microsoft_graph_clean_windows_device_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_clean_windows_device.microsoft_graph_clean_windows_device_request_builder')
microsoft_graph_create_device_log_collection_request_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_create_device_log_collection_request.microsoft_graph_create_device_log_collection_request_request_builder')
microsoft_graph_create_remote_help_session_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_create_remote_help_session.microsoft_graph_create_remote_help_session_request_builder')
microsoft_graph_delete_user_from_shared_apple_device_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_delete_user_from_shared_apple_device.microsoft_graph_delete_user_from_shared_apple_device_request_builder')
microsoft_graph_deprovision_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_deprovision.microsoft_graph_deprovision_request_builder')
microsoft_graph_disable_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_disable.microsoft_graph_disable_request_builder')
microsoft_graph_disable_lost_mode_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_disable_lost_mode.microsoft_graph_disable_lost_mode_request_builder')
microsoft_graph_enable_lost_mode_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_enable_lost_mode.microsoft_graph_enable_lost_mode_request_builder')
microsoft_graph_end_remote_help_session_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_end_remote_help_session.microsoft_graph_end_remote_help_session_request_builder')
microsoft_graph_enroll_now_action_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_enroll_now_action.microsoft_graph_enroll_now_action_request_builder')
microsoft_graph_get_cloud_pc_remote_action_results_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_get_cloud_pc_remote_action_results.microsoft_graph_get_cloud_pc_remote_action_results_request_builder')
microsoft_graph_get_cloud_pc_review_status_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_get_cloud_pc_review_status.microsoft_graph_get_cloud_pc_review_status_request_builder')
microsoft_graph_get_file_vault_key_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_get_file_vault_key.microsoft_graph_get_file_vault_key_request_builder')
microsoft_graph_get_non_compliant_settings_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_get_non_compliant_settings.microsoft_graph_get_non_compliant_settings_request_builder')
microsoft_graph_get_oem_warranty_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_get_oem_warranty.microsoft_graph_get_oem_warranty_request_builder')
microsoft_graph_initiate_mobile_device_management_key_recovery_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_initiate_mobile_device_management_key_recovery.microsoft_graph_initiate_mobile_device_management_key_recovery_request_builder')
microsoft_graph_initiate_on_demand_proactive_remediation_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_initiate_on_demand_proactive_remediation.microsoft_graph_initiate_on_demand_proactive_remediation_request_builder')
microsoft_graph_locate_device_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_locate_device.microsoft_graph_locate_device_request_builder')
microsoft_graph_logout_shared_apple_device_active_user_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_logout_shared_apple_device_active_user.microsoft_graph_logout_shared_apple_device_active_user_request_builder')
microsoft_graph_override_compliance_state_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_override_compliance_state.microsoft_graph_override_compliance_state_request_builder')
microsoft_graph_play_lost_mode_sound_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_play_lost_mode_sound.microsoft_graph_play_lost_mode_sound_request_builder')
microsoft_graph_reboot_now_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_reboot_now.microsoft_graph_reboot_now_request_builder')
microsoft_graph_recover_passcode_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_recover_passcode.microsoft_graph_recover_passcode_request_builder')
microsoft_graph_reenable_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_reenable.microsoft_graph_reenable_request_builder')
microsoft_graph_remote_lock_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_remote_lock.microsoft_graph_remote_lock_request_builder')
microsoft_graph_remove_device_firmware_configuration_interface_management_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_remove_device_firmware_configuration_interface_management.microsoft_graph_remove_device_firmware_configuration_interface_management_request_builder')
microsoft_graph_reprovision_cloud_pc_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_reprovision_cloud_pc.microsoft_graph_reprovision_cloud_pc_request_builder')
microsoft_graph_request_remote_assistance_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_request_remote_assistance.microsoft_graph_request_remote_assistance_request_builder')
microsoft_graph_request_remote_help_session_access_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_request_remote_help_session_access.microsoft_graph_request_remote_help_session_access_request_builder')
microsoft_graph_reset_passcode_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_reset_passcode.microsoft_graph_reset_passcode_request_builder')
microsoft_graph_resize_cloud_pc_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_resize_cloud_pc.microsoft_graph_resize_cloud_pc_request_builder')
microsoft_graph_restore_cloud_pc_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_restore_cloud_pc.microsoft_graph_restore_cloud_pc_request_builder')
microsoft_graph_retire_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_retire.microsoft_graph_retire_request_builder')
microsoft_graph_retrieve_remote_help_session_with_session_key_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_retrieve_remote_help_session_with_session_key.microsoft_graph_retrieve_remote_help_session_with_session_key_request_builder')
microsoft_graph_revoke_apple_vpp_licenses_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_revoke_apple_vpp_licenses.microsoft_graph_revoke_apple_vpp_licenses_request_builder')
microsoft_graph_rotate_bit_locker_keys_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_rotate_bit_locker_keys.microsoft_graph_rotate_bit_locker_keys_request_builder')
microsoft_graph_rotate_file_vault_key_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_rotate_file_vault_key.microsoft_graph_rotate_file_vault_key_request_builder')
microsoft_graph_send_custom_notification_to_company_portal_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_send_custom_notification_to_company_portal.microsoft_graph_send_custom_notification_to_company_portal_request_builder')
microsoft_graph_set_cloud_pc_review_status_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_set_cloud_pc_review_status.microsoft_graph_set_cloud_pc_review_status_request_builder')
microsoft_graph_set_device_name_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_set_device_name.microsoft_graph_set_device_name_request_builder')
microsoft_graph_shut_down_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_shut_down.microsoft_graph_shut_down_request_builder')
microsoft_graph_sync_device_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_sync_device.microsoft_graph_sync_device_request_builder')
microsoft_graph_trigger_configuration_manager_action_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_trigger_configuration_manager_action.microsoft_graph_trigger_configuration_manager_action_request_builder')
microsoft_graph_update_windows_device_account_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_update_windows_device_account.microsoft_graph_update_windows_device_account_request_builder')
microsoft_graph_windows_defender_scan_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_windows_defender_scan.microsoft_graph_windows_defender_scan_request_builder')
microsoft_graph_windows_defender_update_signatures_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_windows_defender_update_signatures.microsoft_graph_windows_defender_update_signatures_request_builder')
microsoft_graph_wipe_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.microsoft_graph_wipe.microsoft_graph_wipe_request_builder')
security_baseline_states_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.security_baseline_states.security_baseline_states_request_builder')
security_baseline_state_item_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.security_baseline_states.item.security_baseline_state_item_request_builder')
users_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.users.users_request_builder')
windows_protection_state_request_builder = lazy_import('msgraph.generated.device_management.managed_devices.item.windows_protection_state.windows_protection_state_request_builder')
managed_device = lazy_import('msgraph.generated.models.managed_device')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class ManagedDeviceItemRequestBuilder():
    """
    Provides operations to manage the managedDevices property of the microsoft.graph.deviceManagement entity.
    """
    @property
    def assignment_filter_evaluation_status_details(self) -> assignment_filter_evaluation_status_details_request_builder.AssignmentFilterEvaluationStatusDetailsRequestBuilder:
        """
        Provides operations to manage the assignmentFilterEvaluationStatusDetails property of the microsoft.graph.managedDevice entity.
        """
        return assignment_filter_evaluation_status_details_request_builder.AssignmentFilterEvaluationStatusDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def detected_apps(self) -> detected_apps_request_builder.DetectedAppsRequestBuilder:
        """
        Provides operations to manage the detectedApps property of the microsoft.graph.managedDevice entity.
        """
        return detected_apps_request_builder.DetectedAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_category(self) -> device_category_request_builder.DeviceCategoryRequestBuilder:
        """
        Provides operations to manage the deviceCategory property of the microsoft.graph.managedDevice entity.
        """
        return device_category_request_builder.DeviceCategoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_states(self) -> device_compliance_policy_states_request_builder.DeviceCompliancePolicyStatesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicyStates property of the microsoft.graph.managedDevice entity.
        """
        return device_compliance_policy_states_request_builder.DeviceCompliancePolicyStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_states(self) -> device_configuration_states_request_builder.DeviceConfigurationStatesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationStates property of the microsoft.graph.managedDevice entity.
        """
        return device_configuration_states_request_builder.DeviceConfigurationStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_health_script_states(self) -> device_health_script_states_request_builder.DeviceHealthScriptStatesRequestBuilder:
        """
        Provides operations to manage the deviceHealthScriptStates property of the microsoft.graph.managedDevice entity.
        """
        return device_health_script_states_request_builder.DeviceHealthScriptStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log_collection_requests(self) -> log_collection_requests_request_builder.LogCollectionRequestsRequestBuilder:
        """
        Provides operations to manage the logCollectionRequests property of the microsoft.graph.managedDevice entity.
        """
        return log_collection_requests_request_builder.LogCollectionRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_mobile_app_configuration_states(self) -> managed_device_mobile_app_configuration_states_request_builder.ManagedDeviceMobileAppConfigurationStatesRequestBuilder:
        """
        Provides operations to manage the managedDeviceMobileAppConfigurationStates property of the microsoft.graph.managedDevice entity.
        """
        return managed_device_mobile_app_configuration_states_request_builder.ManagedDeviceMobileAppConfigurationStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_activate_device_esim(self) -> microsoft_graph_activate_device_esim_request_builder.MicrosoftGraphActivateDeviceEsimRequestBuilder:
        """
        Provides operations to call the activateDeviceEsim method.
        """
        return microsoft_graph_activate_device_esim_request_builder.MicrosoftGraphActivateDeviceEsimRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_bypass_activation_lock(self) -> microsoft_graph_bypass_activation_lock_request_builder.MicrosoftGraphBypassActivationLockRequestBuilder:
        """
        Provides operations to call the bypassActivationLock method.
        """
        return microsoft_graph_bypass_activation_lock_request_builder.MicrosoftGraphBypassActivationLockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_clean_windows_device(self) -> microsoft_graph_clean_windows_device_request_builder.MicrosoftGraphCleanWindowsDeviceRequestBuilder:
        """
        Provides operations to call the cleanWindowsDevice method.
        """
        return microsoft_graph_clean_windows_device_request_builder.MicrosoftGraphCleanWindowsDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_create_device_log_collection_request(self) -> microsoft_graph_create_device_log_collection_request_request_builder.MicrosoftGraphCreateDeviceLogCollectionRequestRequestBuilder:
        """
        Provides operations to call the createDeviceLogCollectionRequest method.
        """
        return microsoft_graph_create_device_log_collection_request_request_builder.MicrosoftGraphCreateDeviceLogCollectionRequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_create_remote_help_session(self) -> microsoft_graph_create_remote_help_session_request_builder.MicrosoftGraphCreateRemoteHelpSessionRequestBuilder:
        """
        Provides operations to call the createRemoteHelpSession method.
        """
        return microsoft_graph_create_remote_help_session_request_builder.MicrosoftGraphCreateRemoteHelpSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_delete_user_from_shared_apple_device(self) -> microsoft_graph_delete_user_from_shared_apple_device_request_builder.MicrosoftGraphDeleteUserFromSharedAppleDeviceRequestBuilder:
        """
        Provides operations to call the deleteUserFromSharedAppleDevice method.
        """
        return microsoft_graph_delete_user_from_shared_apple_device_request_builder.MicrosoftGraphDeleteUserFromSharedAppleDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_deprovision(self) -> microsoft_graph_deprovision_request_builder.MicrosoftGraphDeprovisionRequestBuilder:
        """
        Provides operations to call the deprovision method.
        """
        return microsoft_graph_deprovision_request_builder.MicrosoftGraphDeprovisionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_disable(self) -> microsoft_graph_disable_request_builder.MicrosoftGraphDisableRequestBuilder:
        """
        Provides operations to call the disable method.
        """
        return microsoft_graph_disable_request_builder.MicrosoftGraphDisableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_disable_lost_mode(self) -> microsoft_graph_disable_lost_mode_request_builder.MicrosoftGraphDisableLostModeRequestBuilder:
        """
        Provides operations to call the disableLostMode method.
        """
        return microsoft_graph_disable_lost_mode_request_builder.MicrosoftGraphDisableLostModeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_enable_lost_mode(self) -> microsoft_graph_enable_lost_mode_request_builder.MicrosoftGraphEnableLostModeRequestBuilder:
        """
        Provides operations to call the enableLostMode method.
        """
        return microsoft_graph_enable_lost_mode_request_builder.MicrosoftGraphEnableLostModeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_end_remote_help_session(self) -> microsoft_graph_end_remote_help_session_request_builder.MicrosoftGraphEndRemoteHelpSessionRequestBuilder:
        """
        Provides operations to call the endRemoteHelpSession method.
        """
        return microsoft_graph_end_remote_help_session_request_builder.MicrosoftGraphEndRemoteHelpSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_enroll_now_action(self) -> microsoft_graph_enroll_now_action_request_builder.MicrosoftGraphEnrollNowActionRequestBuilder:
        """
        Provides operations to call the enrollNowAction method.
        """
        return microsoft_graph_enroll_now_action_request_builder.MicrosoftGraphEnrollNowActionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_cloud_pc_remote_action_results(self) -> microsoft_graph_get_cloud_pc_remote_action_results_request_builder.MicrosoftGraphGetCloudPcRemoteActionResultsRequestBuilder:
        """
        Provides operations to call the getCloudPcRemoteActionResults method.
        """
        return microsoft_graph_get_cloud_pc_remote_action_results_request_builder.MicrosoftGraphGetCloudPcRemoteActionResultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_cloud_pc_review_status(self) -> microsoft_graph_get_cloud_pc_review_status_request_builder.MicrosoftGraphGetCloudPcReviewStatusRequestBuilder:
        """
        Provides operations to call the getCloudPcReviewStatus method.
        """
        return microsoft_graph_get_cloud_pc_review_status_request_builder.MicrosoftGraphGetCloudPcReviewStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_file_vault_key(self) -> microsoft_graph_get_file_vault_key_request_builder.MicrosoftGraphGetFileVaultKeyRequestBuilder:
        """
        Provides operations to call the getFileVaultKey method.
        """
        return microsoft_graph_get_file_vault_key_request_builder.MicrosoftGraphGetFileVaultKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_non_compliant_settings(self) -> microsoft_graph_get_non_compliant_settings_request_builder.MicrosoftGraphGetNonCompliantSettingsRequestBuilder:
        """
        Provides operations to call the getNonCompliantSettings method.
        """
        return microsoft_graph_get_non_compliant_settings_request_builder.MicrosoftGraphGetNonCompliantSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_oem_warranty(self) -> microsoft_graph_get_oem_warranty_request_builder.MicrosoftGraphGetOemWarrantyRequestBuilder:
        """
        Provides operations to call the getOemWarranty method.
        """
        return microsoft_graph_get_oem_warranty_request_builder.MicrosoftGraphGetOemWarrantyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_initiate_mobile_device_management_key_recovery(self) -> microsoft_graph_initiate_mobile_device_management_key_recovery_request_builder.MicrosoftGraphInitiateMobileDeviceManagementKeyRecoveryRequestBuilder:
        """
        Provides operations to call the initiateMobileDeviceManagementKeyRecovery method.
        """
        return microsoft_graph_initiate_mobile_device_management_key_recovery_request_builder.MicrosoftGraphInitiateMobileDeviceManagementKeyRecoveryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_initiate_on_demand_proactive_remediation(self) -> microsoft_graph_initiate_on_demand_proactive_remediation_request_builder.MicrosoftGraphInitiateOnDemandProactiveRemediationRequestBuilder:
        """
        Provides operations to call the initiateOnDemandProactiveRemediation method.
        """
        return microsoft_graph_initiate_on_demand_proactive_remediation_request_builder.MicrosoftGraphInitiateOnDemandProactiveRemediationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_locate_device(self) -> microsoft_graph_locate_device_request_builder.MicrosoftGraphLocateDeviceRequestBuilder:
        """
        Provides operations to call the locateDevice method.
        """
        return microsoft_graph_locate_device_request_builder.MicrosoftGraphLocateDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_logout_shared_apple_device_active_user(self) -> microsoft_graph_logout_shared_apple_device_active_user_request_builder.MicrosoftGraphLogoutSharedAppleDeviceActiveUserRequestBuilder:
        """
        Provides operations to call the logoutSharedAppleDeviceActiveUser method.
        """
        return microsoft_graph_logout_shared_apple_device_active_user_request_builder.MicrosoftGraphLogoutSharedAppleDeviceActiveUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_override_compliance_state(self) -> microsoft_graph_override_compliance_state_request_builder.MicrosoftGraphOverrideComplianceStateRequestBuilder:
        """
        Provides operations to call the overrideComplianceState method.
        """
        return microsoft_graph_override_compliance_state_request_builder.MicrosoftGraphOverrideComplianceStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_play_lost_mode_sound(self) -> microsoft_graph_play_lost_mode_sound_request_builder.MicrosoftGraphPlayLostModeSoundRequestBuilder:
        """
        Provides operations to call the playLostModeSound method.
        """
        return microsoft_graph_play_lost_mode_sound_request_builder.MicrosoftGraphPlayLostModeSoundRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_reboot_now(self) -> microsoft_graph_reboot_now_request_builder.MicrosoftGraphRebootNowRequestBuilder:
        """
        Provides operations to call the rebootNow method.
        """
        return microsoft_graph_reboot_now_request_builder.MicrosoftGraphRebootNowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_recover_passcode(self) -> microsoft_graph_recover_passcode_request_builder.MicrosoftGraphRecoverPasscodeRequestBuilder:
        """
        Provides operations to call the recoverPasscode method.
        """
        return microsoft_graph_recover_passcode_request_builder.MicrosoftGraphRecoverPasscodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_reenable(self) -> microsoft_graph_reenable_request_builder.MicrosoftGraphReenableRequestBuilder:
        """
        Provides operations to call the reenable method.
        """
        return microsoft_graph_reenable_request_builder.MicrosoftGraphReenableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_remote_lock(self) -> microsoft_graph_remote_lock_request_builder.MicrosoftGraphRemoteLockRequestBuilder:
        """
        Provides operations to call the remoteLock method.
        """
        return microsoft_graph_remote_lock_request_builder.MicrosoftGraphRemoteLockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_remove_device_firmware_configuration_interface_management(self) -> microsoft_graph_remove_device_firmware_configuration_interface_management_request_builder.MicrosoftGraphRemoveDeviceFirmwareConfigurationInterfaceManagementRequestBuilder:
        """
        Provides operations to call the removeDeviceFirmwareConfigurationInterfaceManagement method.
        """
        return microsoft_graph_remove_device_firmware_configuration_interface_management_request_builder.MicrosoftGraphRemoveDeviceFirmwareConfigurationInterfaceManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_reprovision_cloud_pc(self) -> microsoft_graph_reprovision_cloud_pc_request_builder.MicrosoftGraphReprovisionCloudPcRequestBuilder:
        """
        Provides operations to call the reprovisionCloudPc method.
        """
        return microsoft_graph_reprovision_cloud_pc_request_builder.MicrosoftGraphReprovisionCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_request_remote_assistance(self) -> microsoft_graph_request_remote_assistance_request_builder.MicrosoftGraphRequestRemoteAssistanceRequestBuilder:
        """
        Provides operations to call the requestRemoteAssistance method.
        """
        return microsoft_graph_request_remote_assistance_request_builder.MicrosoftGraphRequestRemoteAssistanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_request_remote_help_session_access(self) -> microsoft_graph_request_remote_help_session_access_request_builder.MicrosoftGraphRequestRemoteHelpSessionAccessRequestBuilder:
        """
        Provides operations to call the requestRemoteHelpSessionAccess method.
        """
        return microsoft_graph_request_remote_help_session_access_request_builder.MicrosoftGraphRequestRemoteHelpSessionAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_reset_passcode(self) -> microsoft_graph_reset_passcode_request_builder.MicrosoftGraphResetPasscodeRequestBuilder:
        """
        Provides operations to call the resetPasscode method.
        """
        return microsoft_graph_reset_passcode_request_builder.MicrosoftGraphResetPasscodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_resize_cloud_pc(self) -> microsoft_graph_resize_cloud_pc_request_builder.MicrosoftGraphResizeCloudPcRequestBuilder:
        """
        Provides operations to call the resizeCloudPc method.
        """
        return microsoft_graph_resize_cloud_pc_request_builder.MicrosoftGraphResizeCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_restore_cloud_pc(self) -> microsoft_graph_restore_cloud_pc_request_builder.MicrosoftGraphRestoreCloudPcRequestBuilder:
        """
        Provides operations to call the restoreCloudPc method.
        """
        return microsoft_graph_restore_cloud_pc_request_builder.MicrosoftGraphRestoreCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_retire(self) -> microsoft_graph_retire_request_builder.MicrosoftGraphRetireRequestBuilder:
        """
        Provides operations to call the retire method.
        """
        return microsoft_graph_retire_request_builder.MicrosoftGraphRetireRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_revoke_apple_vpp_licenses(self) -> microsoft_graph_revoke_apple_vpp_licenses_request_builder.MicrosoftGraphRevokeAppleVppLicensesRequestBuilder:
        """
        Provides operations to call the revokeAppleVppLicenses method.
        """
        return microsoft_graph_revoke_apple_vpp_licenses_request_builder.MicrosoftGraphRevokeAppleVppLicensesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_rotate_bit_locker_keys(self) -> microsoft_graph_rotate_bit_locker_keys_request_builder.MicrosoftGraphRotateBitLockerKeysRequestBuilder:
        """
        Provides operations to call the rotateBitLockerKeys method.
        """
        return microsoft_graph_rotate_bit_locker_keys_request_builder.MicrosoftGraphRotateBitLockerKeysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_rotate_file_vault_key(self) -> microsoft_graph_rotate_file_vault_key_request_builder.MicrosoftGraphRotateFileVaultKeyRequestBuilder:
        """
        Provides operations to call the rotateFileVaultKey method.
        """
        return microsoft_graph_rotate_file_vault_key_request_builder.MicrosoftGraphRotateFileVaultKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_send_custom_notification_to_company_portal(self) -> microsoft_graph_send_custom_notification_to_company_portal_request_builder.MicrosoftGraphSendCustomNotificationToCompanyPortalRequestBuilder:
        """
        Provides operations to call the sendCustomNotificationToCompanyPortal method.
        """
        return microsoft_graph_send_custom_notification_to_company_portal_request_builder.MicrosoftGraphSendCustomNotificationToCompanyPortalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_set_cloud_pc_review_status(self) -> microsoft_graph_set_cloud_pc_review_status_request_builder.MicrosoftGraphSetCloudPcReviewStatusRequestBuilder:
        """
        Provides operations to call the setCloudPcReviewStatus method.
        """
        return microsoft_graph_set_cloud_pc_review_status_request_builder.MicrosoftGraphSetCloudPcReviewStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_set_device_name(self) -> microsoft_graph_set_device_name_request_builder.MicrosoftGraphSetDeviceNameRequestBuilder:
        """
        Provides operations to call the setDeviceName method.
        """
        return microsoft_graph_set_device_name_request_builder.MicrosoftGraphSetDeviceNameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_shut_down(self) -> microsoft_graph_shut_down_request_builder.MicrosoftGraphShutDownRequestBuilder:
        """
        Provides operations to call the shutDown method.
        """
        return microsoft_graph_shut_down_request_builder.MicrosoftGraphShutDownRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_sync_device(self) -> microsoft_graph_sync_device_request_builder.MicrosoftGraphSyncDeviceRequestBuilder:
        """
        Provides operations to call the syncDevice method.
        """
        return microsoft_graph_sync_device_request_builder.MicrosoftGraphSyncDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_trigger_configuration_manager_action(self) -> microsoft_graph_trigger_configuration_manager_action_request_builder.MicrosoftGraphTriggerConfigurationManagerActionRequestBuilder:
        """
        Provides operations to call the triggerConfigurationManagerAction method.
        """
        return microsoft_graph_trigger_configuration_manager_action_request_builder.MicrosoftGraphTriggerConfigurationManagerActionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_update_windows_device_account(self) -> microsoft_graph_update_windows_device_account_request_builder.MicrosoftGraphUpdateWindowsDeviceAccountRequestBuilder:
        """
        Provides operations to call the updateWindowsDeviceAccount method.
        """
        return microsoft_graph_update_windows_device_account_request_builder.MicrosoftGraphUpdateWindowsDeviceAccountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_windows_defender_scan(self) -> microsoft_graph_windows_defender_scan_request_builder.MicrosoftGraphWindowsDefenderScanRequestBuilder:
        """
        Provides operations to call the windowsDefenderScan method.
        """
        return microsoft_graph_windows_defender_scan_request_builder.MicrosoftGraphWindowsDefenderScanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_windows_defender_update_signatures(self) -> microsoft_graph_windows_defender_update_signatures_request_builder.MicrosoftGraphWindowsDefenderUpdateSignaturesRequestBuilder:
        """
        Provides operations to call the windowsDefenderUpdateSignatures method.
        """
        return microsoft_graph_windows_defender_update_signatures_request_builder.MicrosoftGraphWindowsDefenderUpdateSignaturesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_wipe(self) -> microsoft_graph_wipe_request_builder.MicrosoftGraphWipeRequestBuilder:
        """
        Provides operations to call the wipe method.
        """
        return microsoft_graph_wipe_request_builder.MicrosoftGraphWipeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security_baseline_states(self) -> security_baseline_states_request_builder.SecurityBaselineStatesRequestBuilder:
        """
        Provides operations to manage the securityBaselineStates property of the microsoft.graph.managedDevice entity.
        """
        return security_baseline_states_request_builder.SecurityBaselineStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> users_request_builder.UsersRequestBuilder:
        """
        Provides operations to manage the users property of the microsoft.graph.managedDevice entity.
        """
        return users_request_builder.UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_protection_state(self) -> windows_protection_state_request_builder.WindowsProtectionStateRequestBuilder:
        """
        Provides operations to manage the windowsProtectionState property of the microsoft.graph.managedDevice entity.
        """
        return windows_protection_state_request_builder.WindowsProtectionStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    def assignment_filter_evaluation_status_details_by_id(self,id: str) -> assignment_filter_evaluation_status_details_item_request_builder.AssignmentFilterEvaluationStatusDetailsItemRequestBuilder:
        """
        Provides operations to manage the assignmentFilterEvaluationStatusDetails property of the microsoft.graph.managedDevice entity.
        Args:
            id: Unique identifier of the item
        Returns: assignment_filter_evaluation_status_details_item_request_builder.AssignmentFilterEvaluationStatusDetailsItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["assignmentFilterEvaluationStatusDetails%2Did"] = id
        return assignment_filter_evaluation_status_details_item_request_builder.AssignmentFilterEvaluationStatusDetailsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ManagedDeviceItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/managedDevices/{managedDevice%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property managedDevices for deviceManagement
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
    
    def detected_apps_by_id(self,id: str) -> detected_app_item_request_builder.DetectedAppItemRequestBuilder:
        """
        Provides operations to manage the detectedApps property of the microsoft.graph.managedDevice entity.
        Args:
            id: Unique identifier of the item
        Returns: detected_app_item_request_builder.DetectedAppItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["detectedApp%2Did"] = id
        return detected_app_item_request_builder.DetectedAppItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_compliance_policy_states_by_id(self,id: str) -> device_compliance_policy_state_item_request_builder.DeviceCompliancePolicyStateItemRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicyStates property of the microsoft.graph.managedDevice entity.
        Args:
            id: Unique identifier of the item
        Returns: device_compliance_policy_state_item_request_builder.DeviceCompliancePolicyStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceCompliancePolicyState%2Did"] = id
        return device_compliance_policy_state_item_request_builder.DeviceCompliancePolicyStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_configuration_states_by_id(self,id: str) -> device_configuration_state_item_request_builder.DeviceConfigurationStateItemRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationStates property of the microsoft.graph.managedDevice entity.
        Args:
            id: Unique identifier of the item
        Returns: device_configuration_state_item_request_builder.DeviceConfigurationStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceConfigurationState%2Did"] = id
        return device_configuration_state_item_request_builder.DeviceConfigurationStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[managed_device.ManagedDevice]:
        """
        The list of managed devices.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_device.ManagedDevice]
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
        return await self.request_adapter.send_async(request_info, managed_device.ManagedDevice, error_mapping)
    
    def log_collection_requests_by_id(self,id: str) -> device_log_collection_response_item_request_builder.DeviceLogCollectionResponseItemRequestBuilder:
        """
        Provides operations to manage the logCollectionRequests property of the microsoft.graph.managedDevice entity.
        Args:
            id: Unique identifier of the item
        Returns: device_log_collection_response_item_request_builder.DeviceLogCollectionResponseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceLogCollectionResponse%2Did"] = id
        return device_log_collection_response_item_request_builder.DeviceLogCollectionResponseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_device_mobile_app_configuration_states_by_id(self,id: str) -> managed_device_mobile_app_configuration_state_item_request_builder.ManagedDeviceMobileAppConfigurationStateItemRequestBuilder:
        """
        Provides operations to manage the managedDeviceMobileAppConfigurationStates property of the microsoft.graph.managedDevice entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_device_mobile_app_configuration_state_item_request_builder.ManagedDeviceMobileAppConfigurationStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDeviceMobileAppConfigurationState%2Did"] = id
        return managed_device_mobile_app_configuration_state_item_request_builder.ManagedDeviceMobileAppConfigurationStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def microsoft_graph_retrieve_remote_help_session_with_session_key(self,session_key: Optional[str] = None) -> microsoft_graph_retrieve_remote_help_session_with_session_key_request_builder.MicrosoftGraphRetrieveRemoteHelpSessionWithSessionKeyRequestBuilder:
        """
        Provides operations to call the retrieveRemoteHelpSession method.
        Args:
            sessionKey: Usage: sessionKey='{sessionKey}'
        Returns: microsoft_graph_retrieve_remote_help_session_with_session_key_request_builder.MicrosoftGraphRetrieveRemoteHelpSessionWithSessionKeyRequestBuilder
        """
        if session_key is None:
            raise Exception("session_key cannot be undefined")
        return microsoft_graph_retrieve_remote_help_session_with_session_key_request_builder.MicrosoftGraphRetrieveRemoteHelpSessionWithSessionKeyRequestBuilder(self.request_adapter, self.path_parameters, sessionKey)
    
    async def patch(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ManagedDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[managed_device.ManagedDevice]:
        """
        Update the navigation property managedDevices in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_device.ManagedDevice]
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
        return await self.request_adapter.send_async(request_info, managed_device.ManagedDevice, error_mapping)
    
    def security_baseline_states_by_id(self,id: str) -> security_baseline_state_item_request_builder.SecurityBaselineStateItemRequestBuilder:
        """
        Provides operations to manage the securityBaselineStates property of the microsoft.graph.managedDevice entity.
        Args:
            id: Unique identifier of the item
        Returns: security_baseline_state_item_request_builder.SecurityBaselineStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["securityBaselineState%2Did"] = id
        return security_baseline_state_item_request_builder.SecurityBaselineStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property managedDevices for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The list of managed devices.
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
    
    def to_patch_request_information(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ManagedDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property managedDevices in deviceManagement
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
    class ManagedDeviceItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ManagedDeviceItemRequestBuilderGetQueryParameters():
        """
        The list of managed devices.
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
    class ManagedDeviceItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ManagedDeviceItemRequestBuilder.ManagedDeviceItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ManagedDeviceItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

