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

activate_device_esim_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.activate_device_esim.activate_device_esim_request_builder')
assignment_filter_evaluation_status_details_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.assignment_filter_evaluation_status_details.assignment_filter_evaluation_status_details_request_builder')
assignment_filter_evaluation_status_details_item_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.assignment_filter_evaluation_status_details.item.assignment_filter_evaluation_status_details_item_request_builder')
bypass_activation_lock_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.bypass_activation_lock.bypass_activation_lock_request_builder')
clean_windows_device_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.clean_windows_device.clean_windows_device_request_builder')
create_device_log_collection_request_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.create_device_log_collection_request.create_device_log_collection_request_request_builder')
create_remote_help_session_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.create_remote_help_session.create_remote_help_session_request_builder')
delete_user_from_shared_apple_device_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.delete_user_from_shared_apple_device.delete_user_from_shared_apple_device_request_builder')
deprovision_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.deprovision.deprovision_request_builder')
detected_apps_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.detected_apps.detected_apps_request_builder')
detected_app_item_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.detected_apps.item.detected_app_item_request_builder')
device_category_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.device_category.device_category_request_builder')
device_compliance_policy_states_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.device_compliance_policy_states.device_compliance_policy_states_request_builder')
device_compliance_policy_state_item_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.device_compliance_policy_states.item.device_compliance_policy_state_item_request_builder')
device_configuration_states_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.device_configuration_states.device_configuration_states_request_builder')
device_configuration_state_item_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.device_configuration_states.item.device_configuration_state_item_request_builder')
disable_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.disable.disable_request_builder')
disable_lost_mode_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.disable_lost_mode.disable_lost_mode_request_builder')
enable_lost_mode_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.enable_lost_mode.enable_lost_mode_request_builder')
end_remote_help_session_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.end_remote_help_session.end_remote_help_session_request_builder')
enroll_now_action_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.enroll_now_action.enroll_now_action_request_builder')
get_cloud_pc_remote_action_results_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.get_cloud_pc_remote_action_results.get_cloud_pc_remote_action_results_request_builder')
get_cloud_pc_review_status_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.get_cloud_pc_review_status.get_cloud_pc_review_status_request_builder')
get_file_vault_key_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.get_file_vault_key.get_file_vault_key_request_builder')
get_non_compliant_settings_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.get_non_compliant_settings.get_non_compliant_settings_request_builder')
get_oem_warranty_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.get_oem_warranty.get_oem_warranty_request_builder')
initiate_mobile_device_management_key_recovery_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.initiate_mobile_device_management_key_recovery.initiate_mobile_device_management_key_recovery_request_builder')
locate_device_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.locate_device.locate_device_request_builder')
log_collection_requests_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.log_collection_requests.log_collection_requests_request_builder')
device_log_collection_response_item_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.log_collection_requests.item.device_log_collection_response_item_request_builder')
logout_shared_apple_device_active_user_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.logout_shared_apple_device_active_user.logout_shared_apple_device_active_user_request_builder')
managed_device_mobile_app_configuration_states_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.managed_device_mobile_app_configuration_states.managed_device_mobile_app_configuration_states_request_builder')
managed_device_mobile_app_configuration_state_item_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.managed_device_mobile_app_configuration_states.item.managed_device_mobile_app_configuration_state_item_request_builder')
override_compliance_state_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.override_compliance_state.override_compliance_state_request_builder')
play_lost_mode_sound_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.play_lost_mode_sound.play_lost_mode_sound_request_builder')
reboot_now_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.reboot_now.reboot_now_request_builder')
recover_passcode_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.recover_passcode.recover_passcode_request_builder')
reenable_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.reenable.reenable_request_builder')
remote_lock_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.remote_lock.remote_lock_request_builder')
remove_device_firmware_configuration_interface_management_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.remove_device_firmware_configuration_interface_management.remove_device_firmware_configuration_interface_management_request_builder')
reprovision_cloud_pc_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.reprovision_cloud_pc.reprovision_cloud_pc_request_builder')
request_remote_assistance_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.request_remote_assistance.request_remote_assistance_request_builder')
request_remote_help_session_access_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.request_remote_help_session_access.request_remote_help_session_access_request_builder')
reset_passcode_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.reset_passcode.reset_passcode_request_builder')
resize_cloud_pc_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.resize_cloud_pc.resize_cloud_pc_request_builder')
restore_cloud_pc_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.restore_cloud_pc.restore_cloud_pc_request_builder')
retire_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.retire.retire_request_builder')
retrieve_remote_help_session_with_session_key_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.retrieve_remote_help_session_with_session_key.retrieve_remote_help_session_with_session_key_request_builder')
revoke_apple_vpp_licenses_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.revoke_apple_vpp_licenses.revoke_apple_vpp_licenses_request_builder')
rotate_bit_locker_keys_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.rotate_bit_locker_keys.rotate_bit_locker_keys_request_builder')
rotate_file_vault_key_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.rotate_file_vault_key.rotate_file_vault_key_request_builder')
security_baseline_states_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.security_baseline_states.security_baseline_states_request_builder')
security_baseline_state_item_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.security_baseline_states.item.security_baseline_state_item_request_builder')
send_custom_notification_to_company_portal_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.send_custom_notification_to_company_portal.send_custom_notification_to_company_portal_request_builder')
set_cloud_pc_review_status_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.set_cloud_pc_review_status.set_cloud_pc_review_status_request_builder')
set_device_name_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.set_device_name.set_device_name_request_builder')
shut_down_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.shut_down.shut_down_request_builder')
sync_device_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.sync_device.sync_device_request_builder')
trigger_configuration_manager_action_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.trigger_configuration_manager_action.trigger_configuration_manager_action_request_builder')
update_windows_device_account_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.update_windows_device_account.update_windows_device_account_request_builder')
users_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.users.users_request_builder')
windows_defender_scan_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.windows_defender_scan.windows_defender_scan_request_builder')
windows_defender_update_signatures_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.windows_defender_update_signatures.windows_defender_update_signatures_request_builder')
windows_protection_state_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.windows_protection_state.windows_protection_state_request_builder')
wipe_request_builder = lazy_import('msgraph.generated.me.managed_devices.item.wipe.wipe_request_builder')
managed_device = lazy_import('msgraph.generated.models.managed_device')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class ManagedDeviceItemRequestBuilder():
    """
    Provides operations to manage the managedDevices property of the microsoft.graph.user entity.
    """
    @property
    def activate_device_esim(self) -> activate_device_esim_request_builder.ActivateDeviceEsimRequestBuilder:
        """
        Provides operations to call the activateDeviceEsim method.
        """
        return activate_device_esim_request_builder.ActivateDeviceEsimRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_filter_evaluation_status_details(self) -> assignment_filter_evaluation_status_details_request_builder.AssignmentFilterEvaluationStatusDetailsRequestBuilder:
        """
        Provides operations to manage the assignmentFilterEvaluationStatusDetails property of the microsoft.graph.managedDevice entity.
        """
        return assignment_filter_evaluation_status_details_request_builder.AssignmentFilterEvaluationStatusDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bypass_activation_lock(self) -> bypass_activation_lock_request_builder.BypassActivationLockRequestBuilder:
        """
        Provides operations to call the bypassActivationLock method.
        """
        return bypass_activation_lock_request_builder.BypassActivationLockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clean_windows_device(self) -> clean_windows_device_request_builder.CleanWindowsDeviceRequestBuilder:
        """
        Provides operations to call the cleanWindowsDevice method.
        """
        return clean_windows_device_request_builder.CleanWindowsDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_device_log_collection_request(self) -> create_device_log_collection_request_request_builder.CreateDeviceLogCollectionRequestRequestBuilder:
        """
        Provides operations to call the createDeviceLogCollectionRequest method.
        """
        return create_device_log_collection_request_request_builder.CreateDeviceLogCollectionRequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_remote_help_session(self) -> create_remote_help_session_request_builder.CreateRemoteHelpSessionRequestBuilder:
        """
        Provides operations to call the createRemoteHelpSession method.
        """
        return create_remote_help_session_request_builder.CreateRemoteHelpSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delete_user_from_shared_apple_device(self) -> delete_user_from_shared_apple_device_request_builder.DeleteUserFromSharedAppleDeviceRequestBuilder:
        """
        Provides operations to call the deleteUserFromSharedAppleDevice method.
        """
        return delete_user_from_shared_apple_device_request_builder.DeleteUserFromSharedAppleDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deprovision(self) -> deprovision_request_builder.DeprovisionRequestBuilder:
        """
        Provides operations to call the deprovision method.
        """
        return deprovision_request_builder.DeprovisionRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    def disable(self) -> disable_request_builder.DisableRequestBuilder:
        """
        Provides operations to call the disable method.
        """
        return disable_request_builder.DisableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def disable_lost_mode(self) -> disable_lost_mode_request_builder.DisableLostModeRequestBuilder:
        """
        Provides operations to call the disableLostMode method.
        """
        return disable_lost_mode_request_builder.DisableLostModeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable_lost_mode(self) -> enable_lost_mode_request_builder.EnableLostModeRequestBuilder:
        """
        Provides operations to call the enableLostMode method.
        """
        return enable_lost_mode_request_builder.EnableLostModeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def end_remote_help_session(self) -> end_remote_help_session_request_builder.EndRemoteHelpSessionRequestBuilder:
        """
        Provides operations to call the endRemoteHelpSession method.
        """
        return end_remote_help_session_request_builder.EndRemoteHelpSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enroll_now_action(self) -> enroll_now_action_request_builder.EnrollNowActionRequestBuilder:
        """
        Provides operations to call the enrollNowAction method.
        """
        return enroll_now_action_request_builder.EnrollNowActionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def initiate_mobile_device_management_key_recovery(self) -> initiate_mobile_device_management_key_recovery_request_builder.InitiateMobileDeviceManagementKeyRecoveryRequestBuilder:
        """
        Provides operations to call the initiateMobileDeviceManagementKeyRecovery method.
        """
        return initiate_mobile_device_management_key_recovery_request_builder.InitiateMobileDeviceManagementKeyRecoveryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def locate_device(self) -> locate_device_request_builder.LocateDeviceRequestBuilder:
        """
        Provides operations to call the locateDevice method.
        """
        return locate_device_request_builder.LocateDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log_collection_requests(self) -> log_collection_requests_request_builder.LogCollectionRequestsRequestBuilder:
        """
        Provides operations to manage the logCollectionRequests property of the microsoft.graph.managedDevice entity.
        """
        return log_collection_requests_request_builder.LogCollectionRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logout_shared_apple_device_active_user(self) -> logout_shared_apple_device_active_user_request_builder.LogoutSharedAppleDeviceActiveUserRequestBuilder:
        """
        Provides operations to call the logoutSharedAppleDeviceActiveUser method.
        """
        return logout_shared_apple_device_active_user_request_builder.LogoutSharedAppleDeviceActiveUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_mobile_app_configuration_states(self) -> managed_device_mobile_app_configuration_states_request_builder.ManagedDeviceMobileAppConfigurationStatesRequestBuilder:
        """
        Provides operations to manage the managedDeviceMobileAppConfigurationStates property of the microsoft.graph.managedDevice entity.
        """
        return managed_device_mobile_app_configuration_states_request_builder.ManagedDeviceMobileAppConfigurationStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def override_compliance_state(self) -> override_compliance_state_request_builder.OverrideComplianceStateRequestBuilder:
        """
        Provides operations to call the overrideComplianceState method.
        """
        return override_compliance_state_request_builder.OverrideComplianceStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def play_lost_mode_sound(self) -> play_lost_mode_sound_request_builder.PlayLostModeSoundRequestBuilder:
        """
        Provides operations to call the playLostModeSound method.
        """
        return play_lost_mode_sound_request_builder.PlayLostModeSoundRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reboot_now(self) -> reboot_now_request_builder.RebootNowRequestBuilder:
        """
        Provides operations to call the rebootNow method.
        """
        return reboot_now_request_builder.RebootNowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recover_passcode(self) -> recover_passcode_request_builder.RecoverPasscodeRequestBuilder:
        """
        Provides operations to call the recoverPasscode method.
        """
        return recover_passcode_request_builder.RecoverPasscodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reenable(self) -> reenable_request_builder.ReenableRequestBuilder:
        """
        Provides operations to call the reenable method.
        """
        return reenable_request_builder.ReenableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_lock(self) -> remote_lock_request_builder.RemoteLockRequestBuilder:
        """
        Provides operations to call the remoteLock method.
        """
        return remote_lock_request_builder.RemoteLockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_device_firmware_configuration_interface_management(self) -> remove_device_firmware_configuration_interface_management_request_builder.RemoveDeviceFirmwareConfigurationInterfaceManagementRequestBuilder:
        """
        Provides operations to call the removeDeviceFirmwareConfigurationInterfaceManagement method.
        """
        return remove_device_firmware_configuration_interface_management_request_builder.RemoveDeviceFirmwareConfigurationInterfaceManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reprovision_cloud_pc(self) -> reprovision_cloud_pc_request_builder.ReprovisionCloudPcRequestBuilder:
        """
        Provides operations to call the reprovisionCloudPc method.
        """
        return reprovision_cloud_pc_request_builder.ReprovisionCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def request_remote_assistance(self) -> request_remote_assistance_request_builder.RequestRemoteAssistanceRequestBuilder:
        """
        Provides operations to call the requestRemoteAssistance method.
        """
        return request_remote_assistance_request_builder.RequestRemoteAssistanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def request_remote_help_session_access(self) -> request_remote_help_session_access_request_builder.RequestRemoteHelpSessionAccessRequestBuilder:
        """
        Provides operations to call the requestRemoteHelpSessionAccess method.
        """
        return request_remote_help_session_access_request_builder.RequestRemoteHelpSessionAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_passcode(self) -> reset_passcode_request_builder.ResetPasscodeRequestBuilder:
        """
        Provides operations to call the resetPasscode method.
        """
        return reset_passcode_request_builder.ResetPasscodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resize_cloud_pc(self) -> resize_cloud_pc_request_builder.ResizeCloudPcRequestBuilder:
        """
        Provides operations to call the resizeCloudPc method.
        """
        return resize_cloud_pc_request_builder.ResizeCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore_cloud_pc(self) -> restore_cloud_pc_request_builder.RestoreCloudPcRequestBuilder:
        """
        Provides operations to call the restoreCloudPc method.
        """
        return restore_cloud_pc_request_builder.RestoreCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retire(self) -> retire_request_builder.RetireRequestBuilder:
        """
        Provides operations to call the retire method.
        """
        return retire_request_builder.RetireRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def revoke_apple_vpp_licenses(self) -> revoke_apple_vpp_licenses_request_builder.RevokeAppleVppLicensesRequestBuilder:
        """
        Provides operations to call the revokeAppleVppLicenses method.
        """
        return revoke_apple_vpp_licenses_request_builder.RevokeAppleVppLicensesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rotate_bit_locker_keys(self) -> rotate_bit_locker_keys_request_builder.RotateBitLockerKeysRequestBuilder:
        """
        Provides operations to call the rotateBitLockerKeys method.
        """
        return rotate_bit_locker_keys_request_builder.RotateBitLockerKeysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rotate_file_vault_key(self) -> rotate_file_vault_key_request_builder.RotateFileVaultKeyRequestBuilder:
        """
        Provides operations to call the rotateFileVaultKey method.
        """
        return rotate_file_vault_key_request_builder.RotateFileVaultKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security_baseline_states(self) -> security_baseline_states_request_builder.SecurityBaselineStatesRequestBuilder:
        """
        Provides operations to manage the securityBaselineStates property of the microsoft.graph.managedDevice entity.
        """
        return security_baseline_states_request_builder.SecurityBaselineStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_custom_notification_to_company_portal(self) -> send_custom_notification_to_company_portal_request_builder.SendCustomNotificationToCompanyPortalRequestBuilder:
        """
        Provides operations to call the sendCustomNotificationToCompanyPortal method.
        """
        return send_custom_notification_to_company_portal_request_builder.SendCustomNotificationToCompanyPortalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_cloud_pc_review_status(self) -> set_cloud_pc_review_status_request_builder.SetCloudPcReviewStatusRequestBuilder:
        """
        Provides operations to call the setCloudPcReviewStatus method.
        """
        return set_cloud_pc_review_status_request_builder.SetCloudPcReviewStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_device_name(self) -> set_device_name_request_builder.SetDeviceNameRequestBuilder:
        """
        Provides operations to call the setDeviceName method.
        """
        return set_device_name_request_builder.SetDeviceNameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shut_down(self) -> shut_down_request_builder.ShutDownRequestBuilder:
        """
        Provides operations to call the shutDown method.
        """
        return shut_down_request_builder.ShutDownRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync_device(self) -> sync_device_request_builder.SyncDeviceRequestBuilder:
        """
        Provides operations to call the syncDevice method.
        """
        return sync_device_request_builder.SyncDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trigger_configuration_manager_action(self) -> trigger_configuration_manager_action_request_builder.TriggerConfigurationManagerActionRequestBuilder:
        """
        Provides operations to call the triggerConfigurationManagerAction method.
        """
        return trigger_configuration_manager_action_request_builder.TriggerConfigurationManagerActionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_windows_device_account(self) -> update_windows_device_account_request_builder.UpdateWindowsDeviceAccountRequestBuilder:
        """
        Provides operations to call the updateWindowsDeviceAccount method.
        """
        return update_windows_device_account_request_builder.UpdateWindowsDeviceAccountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> users_request_builder.UsersRequestBuilder:
        """
        Provides operations to manage the users property of the microsoft.graph.managedDevice entity.
        """
        return users_request_builder.UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_defender_scan(self) -> windows_defender_scan_request_builder.WindowsDefenderScanRequestBuilder:
        """
        Provides operations to call the windowsDefenderScan method.
        """
        return windows_defender_scan_request_builder.WindowsDefenderScanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_defender_update_signatures(self) -> windows_defender_update_signatures_request_builder.WindowsDefenderUpdateSignaturesRequestBuilder:
        """
        Provides operations to call the windowsDefenderUpdateSignatures method.
        """
        return windows_defender_update_signatures_request_builder.WindowsDefenderUpdateSignaturesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_protection_state(self) -> windows_protection_state_request_builder.WindowsProtectionStateRequestBuilder:
        """
        Provides operations to manage the windowsProtectionState property of the microsoft.graph.managedDevice entity.
        """
        return windows_protection_state_request_builder.WindowsProtectionStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wipe(self) -> wipe_request_builder.WipeRequestBuilder:
        """
        Provides operations to call the wipe method.
        """
        return wipe_request_builder.WipeRequestBuilder(self.request_adapter, self.path_parameters)
    
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
        self.url_template: str = "{+baseurl}/me/managedDevices/{managedDevice%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property managedDevices for me
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
    
    def create_get_request_information(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The managed devices associated with the user.
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
    
    def create_patch_request_information(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ManagedDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property managedDevices in me
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
    
    async def delete(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property managedDevices for me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
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
    
    async def get(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[managed_device.ManagedDevice]:
        """
        The managed devices associated with the user.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[managed_device.ManagedDevice]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, managed_device.ManagedDevice, response_handler, error_mapping)
    
    def get_cloud_pc_remote_action_results(self,) -> get_cloud_pc_remote_action_results_request_builder.GetCloudPcRemoteActionResultsRequestBuilder:
        """
        Provides operations to call the getCloudPcRemoteActionResults method.
        Returns: get_cloud_pc_remote_action_results_request_builder.GetCloudPcRemoteActionResultsRequestBuilder
        """
        return get_cloud_pc_remote_action_results_request_builder.GetCloudPcRemoteActionResultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_cloud_pc_review_status(self,) -> get_cloud_pc_review_status_request_builder.GetCloudPcReviewStatusRequestBuilder:
        """
        Provides operations to call the getCloudPcReviewStatus method.
        Returns: get_cloud_pc_review_status_request_builder.GetCloudPcReviewStatusRequestBuilder
        """
        return get_cloud_pc_review_status_request_builder.GetCloudPcReviewStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_file_vault_key(self,) -> get_file_vault_key_request_builder.GetFileVaultKeyRequestBuilder:
        """
        Provides operations to call the getFileVaultKey method.
        Returns: get_file_vault_key_request_builder.GetFileVaultKeyRequestBuilder
        """
        return get_file_vault_key_request_builder.GetFileVaultKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_non_compliant_settings(self,) -> get_non_compliant_settings_request_builder.GetNonCompliantSettingsRequestBuilder:
        """
        Provides operations to call the getNonCompliantSettings method.
        Returns: get_non_compliant_settings_request_builder.GetNonCompliantSettingsRequestBuilder
        """
        return get_non_compliant_settings_request_builder.GetNonCompliantSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_oem_warranty(self,) -> get_oem_warranty_request_builder.GetOemWarrantyRequestBuilder:
        """
        Provides operations to call the getOemWarranty method.
        Returns: get_oem_warranty_request_builder.GetOemWarrantyRequestBuilder
        """
        return get_oem_warranty_request_builder.GetOemWarrantyRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    
    async def patch(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ManagedDeviceItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[managed_device.ManagedDevice]:
        """
        Update the navigation property managedDevices in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[managed_device.ManagedDevice]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, managed_device.ManagedDevice, response_handler, error_mapping)
    
    def retrieve_remote_help_session_with_session_key(self,session_key: Optional[str] = None) -> retrieve_remote_help_session_with_session_key_request_builder.RetrieveRemoteHelpSessionWithSessionKeyRequestBuilder:
        """
        Provides operations to call the retrieveRemoteHelpSession method.
        Args:
            sessionKey: Usage: sessionKey='{sessionKey}'
        Returns: retrieve_remote_help_session_with_session_key_request_builder.RetrieveRemoteHelpSessionWithSessionKeyRequestBuilder
        """
        if session_key is None:
            raise Exception("session_key cannot be undefined")
        return retrieve_remote_help_session_with_session_key_request_builder.RetrieveRemoteHelpSessionWithSessionKeyRequestBuilder(self.request_adapter, self.path_parameters, sessionKey)
    
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
        The managed devices associated with the user.
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

    

