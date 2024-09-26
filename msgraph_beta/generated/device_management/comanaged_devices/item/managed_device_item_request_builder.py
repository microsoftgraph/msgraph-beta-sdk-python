from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.managed_device import ManagedDevice
    from ....models.o_data_errors.o_data_error import ODataError
    from .activate_device_esim.activate_device_esim_request_builder import ActivateDeviceEsimRequestBuilder
    from .assignment_filter_evaluation_status_details.assignment_filter_evaluation_status_details_request_builder import AssignmentFilterEvaluationStatusDetailsRequestBuilder
    from .bypass_activation_lock.bypass_activation_lock_request_builder import BypassActivationLockRequestBuilder
    from .change_assignments.change_assignments_request_builder import ChangeAssignmentsRequestBuilder
    from .clean_windows_device.clean_windows_device_request_builder import CleanWindowsDeviceRequestBuilder
    from .create_device_log_collection_request.create_device_log_collection_request_request_builder import CreateDeviceLogCollectionRequestRequestBuilder
    from .delete_user_from_shared_apple_device.delete_user_from_shared_apple_device_request_builder import DeleteUserFromSharedAppleDeviceRequestBuilder
    from .deprovision.deprovision_request_builder import DeprovisionRequestBuilder
    from .detected_apps.detected_apps_request_builder import DetectedAppsRequestBuilder
    from .device_category.device_category_request_builder import DeviceCategoryRequestBuilder
    from .device_compliance_policy_states.device_compliance_policy_states_request_builder import DeviceCompliancePolicyStatesRequestBuilder
    from .device_configuration_states.device_configuration_states_request_builder import DeviceConfigurationStatesRequestBuilder
    from .device_health_script_states.device_health_script_states_request_builder import DeviceHealthScriptStatesRequestBuilder
    from .disable.disable_request_builder import DisableRequestBuilder
    from .disable_lost_mode.disable_lost_mode_request_builder import DisableLostModeRequestBuilder
    from .enable_lost_mode.enable_lost_mode_request_builder import EnableLostModeRequestBuilder
    from .enroll_now_action.enroll_now_action_request_builder import EnrollNowActionRequestBuilder
    from .get_cloud_pc_remote_action_results.get_cloud_pc_remote_action_results_request_builder import GetCloudPcRemoteActionResultsRequestBuilder
    from .get_cloud_pc_review_status.get_cloud_pc_review_status_request_builder import GetCloudPcReviewStatusRequestBuilder
    from .get_file_vault_key.get_file_vault_key_request_builder import GetFileVaultKeyRequestBuilder
    from .get_non_compliant_settings.get_non_compliant_settings_request_builder import GetNonCompliantSettingsRequestBuilder
    from .initiate_device_attestation.initiate_device_attestation_request_builder import InitiateDeviceAttestationRequestBuilder
    from .initiate_mobile_device_management_key_recovery.initiate_mobile_device_management_key_recovery_request_builder import InitiateMobileDeviceManagementKeyRecoveryRequestBuilder
    from .initiate_on_demand_proactive_remediation.initiate_on_demand_proactive_remediation_request_builder import InitiateOnDemandProactiveRemediationRequestBuilder
    from .locate_device.locate_device_request_builder import LocateDeviceRequestBuilder
    from .logout_shared_apple_device_active_user.logout_shared_apple_device_active_user_request_builder import LogoutSharedAppleDeviceActiveUserRequestBuilder
    from .log_collection_requests.log_collection_requests_request_builder import LogCollectionRequestsRequestBuilder
    from .managed_device_mobile_app_configuration_states.managed_device_mobile_app_configuration_states_request_builder import ManagedDeviceMobileAppConfigurationStatesRequestBuilder
    from .override_compliance_state.override_compliance_state_request_builder import OverrideComplianceStateRequestBuilder
    from .pause_configuration_refresh.pause_configuration_refresh_request_builder import PauseConfigurationRefreshRequestBuilder
    from .play_lost_mode_sound.play_lost_mode_sound_request_builder import PlayLostModeSoundRequestBuilder
    from .reboot_now.reboot_now_request_builder import RebootNowRequestBuilder
    from .recover_passcode.recover_passcode_request_builder import RecoverPasscodeRequestBuilder
    from .reenable.reenable_request_builder import ReenableRequestBuilder
    from .remote_lock.remote_lock_request_builder import RemoteLockRequestBuilder
    from .remove_device_firmware_configuration_interface_management.remove_device_firmware_configuration_interface_management_request_builder import RemoveDeviceFirmwareConfigurationInterfaceManagementRequestBuilder
    from .reprovision_cloud_pc.reprovision_cloud_pc_request_builder import ReprovisionCloudPcRequestBuilder
    from .request_remote_assistance.request_remote_assistance_request_builder import RequestRemoteAssistanceRequestBuilder
    from .reset_passcode.reset_passcode_request_builder import ResetPasscodeRequestBuilder
    from .resize_cloud_pc.resize_cloud_pc_request_builder import ResizeCloudPcRequestBuilder
    from .restore_cloud_pc.restore_cloud_pc_request_builder import RestoreCloudPcRequestBuilder
    from .retire.retire_request_builder import RetireRequestBuilder
    from .revoke_apple_vpp_licenses.revoke_apple_vpp_licenses_request_builder import RevokeAppleVppLicensesRequestBuilder
    from .rotate_bit_locker_keys.rotate_bit_locker_keys_request_builder import RotateBitLockerKeysRequestBuilder
    from .rotate_file_vault_key.rotate_file_vault_key_request_builder import RotateFileVaultKeyRequestBuilder
    from .rotate_local_admin_password.rotate_local_admin_password_request_builder import RotateLocalAdminPasswordRequestBuilder
    from .security_baseline_states.security_baseline_states_request_builder import SecurityBaselineStatesRequestBuilder
    from .send_custom_notification_to_company_portal.send_custom_notification_to_company_portal_request_builder import SendCustomNotificationToCompanyPortalRequestBuilder
    from .set_cloud_pc_review_status.set_cloud_pc_review_status_request_builder import SetCloudPcReviewStatusRequestBuilder
    from .set_device_name.set_device_name_request_builder import SetDeviceNameRequestBuilder
    from .shut_down.shut_down_request_builder import ShutDownRequestBuilder
    from .sync_device.sync_device_request_builder import SyncDeviceRequestBuilder
    from .trigger_configuration_manager_action.trigger_configuration_manager_action_request_builder import TriggerConfigurationManagerActionRequestBuilder
    from .update_windows_device_account.update_windows_device_account_request_builder import UpdateWindowsDeviceAccountRequestBuilder
    from .users.users_request_builder import UsersRequestBuilder
    from .windows_defender_scan.windows_defender_scan_request_builder import WindowsDefenderScanRequestBuilder
    from .windows_defender_update_signatures.windows_defender_update_signatures_request_builder import WindowsDefenderUpdateSignaturesRequestBuilder
    from .windows_protection_state.windows_protection_state_request_builder import WindowsProtectionStateRequestBuilder
    from .wipe.wipe_request_builder import WipeRequestBuilder

class ManagedDeviceItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the comanagedDevices property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ManagedDeviceItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/comanagedDevices/{managedDevice%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property comanagedDevices for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ManagedDeviceItemRequestBuilderGetQueryParameters]] = None) -> Optional[ManagedDevice]:
        """
        The list of co-managed devices report
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagedDevice]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.managed_device import ManagedDevice

        return await self.request_adapter.send_async(request_info, ManagedDevice, error_mapping)
    
    async def patch(self,body: ManagedDevice, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManagedDevice]:
        """
        Update the navigation property comanagedDevices in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagedDevice]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.managed_device import ManagedDevice

        return await self.request_adapter.send_async(request_info, ManagedDevice, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property comanagedDevices for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ManagedDeviceItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The list of co-managed devices report
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ManagedDevice, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property comanagedDevices in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ManagedDeviceItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ManagedDeviceItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ManagedDeviceItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def activate_device_esim(self) -> ActivateDeviceEsimRequestBuilder:
        """
        Provides operations to call the activateDeviceEsim method.
        """
        from .activate_device_esim.activate_device_esim_request_builder import ActivateDeviceEsimRequestBuilder

        return ActivateDeviceEsimRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_filter_evaluation_status_details(self) -> AssignmentFilterEvaluationStatusDetailsRequestBuilder:
        """
        Provides operations to manage the assignmentFilterEvaluationStatusDetails property of the microsoft.graph.managedDevice entity.
        """
        from .assignment_filter_evaluation_status_details.assignment_filter_evaluation_status_details_request_builder import AssignmentFilterEvaluationStatusDetailsRequestBuilder

        return AssignmentFilterEvaluationStatusDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bypass_activation_lock(self) -> BypassActivationLockRequestBuilder:
        """
        Provides operations to call the bypassActivationLock method.
        """
        from .bypass_activation_lock.bypass_activation_lock_request_builder import BypassActivationLockRequestBuilder

        return BypassActivationLockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def change_assignments(self) -> ChangeAssignmentsRequestBuilder:
        """
        Provides operations to call the changeAssignments method.
        """
        from .change_assignments.change_assignments_request_builder import ChangeAssignmentsRequestBuilder

        return ChangeAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clean_windows_device(self) -> CleanWindowsDeviceRequestBuilder:
        """
        Provides operations to call the cleanWindowsDevice method.
        """
        from .clean_windows_device.clean_windows_device_request_builder import CleanWindowsDeviceRequestBuilder

        return CleanWindowsDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_device_log_collection_request(self) -> CreateDeviceLogCollectionRequestRequestBuilder:
        """
        Provides operations to call the createDeviceLogCollectionRequest method.
        """
        from .create_device_log_collection_request.create_device_log_collection_request_request_builder import CreateDeviceLogCollectionRequestRequestBuilder

        return CreateDeviceLogCollectionRequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delete_user_from_shared_apple_device(self) -> DeleteUserFromSharedAppleDeviceRequestBuilder:
        """
        Provides operations to call the deleteUserFromSharedAppleDevice method.
        """
        from .delete_user_from_shared_apple_device.delete_user_from_shared_apple_device_request_builder import DeleteUserFromSharedAppleDeviceRequestBuilder

        return DeleteUserFromSharedAppleDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deprovision(self) -> DeprovisionRequestBuilder:
        """
        Provides operations to call the deprovision method.
        """
        from .deprovision.deprovision_request_builder import DeprovisionRequestBuilder

        return DeprovisionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def detected_apps(self) -> DetectedAppsRequestBuilder:
        """
        Provides operations to manage the detectedApps property of the microsoft.graph.managedDevice entity.
        """
        from .detected_apps.detected_apps_request_builder import DetectedAppsRequestBuilder

        return DetectedAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_category(self) -> DeviceCategoryRequestBuilder:
        """
        Provides operations to manage the deviceCategory property of the microsoft.graph.managedDevice entity.
        """
        from .device_category.device_category_request_builder import DeviceCategoryRequestBuilder

        return DeviceCategoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_states(self) -> DeviceCompliancePolicyStatesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicyStates property of the microsoft.graph.managedDevice entity.
        """
        from .device_compliance_policy_states.device_compliance_policy_states_request_builder import DeviceCompliancePolicyStatesRequestBuilder

        return DeviceCompliancePolicyStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_states(self) -> DeviceConfigurationStatesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationStates property of the microsoft.graph.managedDevice entity.
        """
        from .device_configuration_states.device_configuration_states_request_builder import DeviceConfigurationStatesRequestBuilder

        return DeviceConfigurationStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_health_script_states(self) -> DeviceHealthScriptStatesRequestBuilder:
        """
        Provides operations to manage the deviceHealthScriptStates property of the microsoft.graph.managedDevice entity.
        """
        from .device_health_script_states.device_health_script_states_request_builder import DeviceHealthScriptStatesRequestBuilder

        return DeviceHealthScriptStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def disable(self) -> DisableRequestBuilder:
        """
        Provides operations to call the disable method.
        """
        from .disable.disable_request_builder import DisableRequestBuilder

        return DisableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def disable_lost_mode(self) -> DisableLostModeRequestBuilder:
        """
        Provides operations to call the disableLostMode method.
        """
        from .disable_lost_mode.disable_lost_mode_request_builder import DisableLostModeRequestBuilder

        return DisableLostModeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable_lost_mode(self) -> EnableLostModeRequestBuilder:
        """
        Provides operations to call the enableLostMode method.
        """
        from .enable_lost_mode.enable_lost_mode_request_builder import EnableLostModeRequestBuilder

        return EnableLostModeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enroll_now_action(self) -> EnrollNowActionRequestBuilder:
        """
        Provides operations to call the enrollNowAction method.
        """
        from .enroll_now_action.enroll_now_action_request_builder import EnrollNowActionRequestBuilder

        return EnrollNowActionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_cloud_pc_remote_action_results(self) -> GetCloudPcRemoteActionResultsRequestBuilder:
        """
        Provides operations to call the getCloudPcRemoteActionResults method.
        """
        from .get_cloud_pc_remote_action_results.get_cloud_pc_remote_action_results_request_builder import GetCloudPcRemoteActionResultsRequestBuilder

        return GetCloudPcRemoteActionResultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_cloud_pc_review_status(self) -> GetCloudPcReviewStatusRequestBuilder:
        """
        Provides operations to call the getCloudPcReviewStatus method.
        """
        from .get_cloud_pc_review_status.get_cloud_pc_review_status_request_builder import GetCloudPcReviewStatusRequestBuilder

        return GetCloudPcReviewStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_file_vault_key(self) -> GetFileVaultKeyRequestBuilder:
        """
        Provides operations to call the getFileVaultKey method.
        """
        from .get_file_vault_key.get_file_vault_key_request_builder import GetFileVaultKeyRequestBuilder

        return GetFileVaultKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_non_compliant_settings(self) -> GetNonCompliantSettingsRequestBuilder:
        """
        Provides operations to call the getNonCompliantSettings method.
        """
        from .get_non_compliant_settings.get_non_compliant_settings_request_builder import GetNonCompliantSettingsRequestBuilder

        return GetNonCompliantSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def initiate_device_attestation(self) -> InitiateDeviceAttestationRequestBuilder:
        """
        Provides operations to call the initiateDeviceAttestation method.
        """
        from .initiate_device_attestation.initiate_device_attestation_request_builder import InitiateDeviceAttestationRequestBuilder

        return InitiateDeviceAttestationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def initiate_mobile_device_management_key_recovery(self) -> InitiateMobileDeviceManagementKeyRecoveryRequestBuilder:
        """
        Provides operations to call the initiateMobileDeviceManagementKeyRecovery method.
        """
        from .initiate_mobile_device_management_key_recovery.initiate_mobile_device_management_key_recovery_request_builder import InitiateMobileDeviceManagementKeyRecoveryRequestBuilder

        return InitiateMobileDeviceManagementKeyRecoveryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def initiate_on_demand_proactive_remediation(self) -> InitiateOnDemandProactiveRemediationRequestBuilder:
        """
        Provides operations to call the initiateOnDemandProactiveRemediation method.
        """
        from .initiate_on_demand_proactive_remediation.initiate_on_demand_proactive_remediation_request_builder import InitiateOnDemandProactiveRemediationRequestBuilder

        return InitiateOnDemandProactiveRemediationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def locate_device(self) -> LocateDeviceRequestBuilder:
        """
        Provides operations to call the locateDevice method.
        """
        from .locate_device.locate_device_request_builder import LocateDeviceRequestBuilder

        return LocateDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log_collection_requests(self) -> LogCollectionRequestsRequestBuilder:
        """
        Provides operations to manage the logCollectionRequests property of the microsoft.graph.managedDevice entity.
        """
        from .log_collection_requests.log_collection_requests_request_builder import LogCollectionRequestsRequestBuilder

        return LogCollectionRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logout_shared_apple_device_active_user(self) -> LogoutSharedAppleDeviceActiveUserRequestBuilder:
        """
        Provides operations to call the logoutSharedAppleDeviceActiveUser method.
        """
        from .logout_shared_apple_device_active_user.logout_shared_apple_device_active_user_request_builder import LogoutSharedAppleDeviceActiveUserRequestBuilder

        return LogoutSharedAppleDeviceActiveUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_mobile_app_configuration_states(self) -> ManagedDeviceMobileAppConfigurationStatesRequestBuilder:
        """
        Provides operations to manage the managedDeviceMobileAppConfigurationStates property of the microsoft.graph.managedDevice entity.
        """
        from .managed_device_mobile_app_configuration_states.managed_device_mobile_app_configuration_states_request_builder import ManagedDeviceMobileAppConfigurationStatesRequestBuilder

        return ManagedDeviceMobileAppConfigurationStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def override_compliance_state(self) -> OverrideComplianceStateRequestBuilder:
        """
        Provides operations to call the overrideComplianceState method.
        """
        from .override_compliance_state.override_compliance_state_request_builder import OverrideComplianceStateRequestBuilder

        return OverrideComplianceStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pause_configuration_refresh(self) -> PauseConfigurationRefreshRequestBuilder:
        """
        Provides operations to call the pauseConfigurationRefresh method.
        """
        from .pause_configuration_refresh.pause_configuration_refresh_request_builder import PauseConfigurationRefreshRequestBuilder

        return PauseConfigurationRefreshRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def play_lost_mode_sound(self) -> PlayLostModeSoundRequestBuilder:
        """
        Provides operations to call the playLostModeSound method.
        """
        from .play_lost_mode_sound.play_lost_mode_sound_request_builder import PlayLostModeSoundRequestBuilder

        return PlayLostModeSoundRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reboot_now(self) -> RebootNowRequestBuilder:
        """
        Provides operations to call the rebootNow method.
        """
        from .reboot_now.reboot_now_request_builder import RebootNowRequestBuilder

        return RebootNowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recover_passcode(self) -> RecoverPasscodeRequestBuilder:
        """
        Provides operations to call the recoverPasscode method.
        """
        from .recover_passcode.recover_passcode_request_builder import RecoverPasscodeRequestBuilder

        return RecoverPasscodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reenable(self) -> ReenableRequestBuilder:
        """
        Provides operations to call the reenable method.
        """
        from .reenable.reenable_request_builder import ReenableRequestBuilder

        return ReenableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_lock(self) -> RemoteLockRequestBuilder:
        """
        Provides operations to call the remoteLock method.
        """
        from .remote_lock.remote_lock_request_builder import RemoteLockRequestBuilder

        return RemoteLockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_device_firmware_configuration_interface_management(self) -> RemoveDeviceFirmwareConfigurationInterfaceManagementRequestBuilder:
        """
        Provides operations to call the removeDeviceFirmwareConfigurationInterfaceManagement method.
        """
        from .remove_device_firmware_configuration_interface_management.remove_device_firmware_configuration_interface_management_request_builder import RemoveDeviceFirmwareConfigurationInterfaceManagementRequestBuilder

        return RemoveDeviceFirmwareConfigurationInterfaceManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reprovision_cloud_pc(self) -> ReprovisionCloudPcRequestBuilder:
        """
        Provides operations to call the reprovisionCloudPc method.
        """
        from .reprovision_cloud_pc.reprovision_cloud_pc_request_builder import ReprovisionCloudPcRequestBuilder

        return ReprovisionCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def request_remote_assistance(self) -> RequestRemoteAssistanceRequestBuilder:
        """
        Provides operations to call the requestRemoteAssistance method.
        """
        from .request_remote_assistance.request_remote_assistance_request_builder import RequestRemoteAssistanceRequestBuilder

        return RequestRemoteAssistanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_passcode(self) -> ResetPasscodeRequestBuilder:
        """
        Provides operations to call the resetPasscode method.
        """
        from .reset_passcode.reset_passcode_request_builder import ResetPasscodeRequestBuilder

        return ResetPasscodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resize_cloud_pc(self) -> ResizeCloudPcRequestBuilder:
        """
        Provides operations to call the resizeCloudPc method.
        """
        from .resize_cloud_pc.resize_cloud_pc_request_builder import ResizeCloudPcRequestBuilder

        return ResizeCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore_cloud_pc(self) -> RestoreCloudPcRequestBuilder:
        """
        Provides operations to call the restoreCloudPc method.
        """
        from .restore_cloud_pc.restore_cloud_pc_request_builder import RestoreCloudPcRequestBuilder

        return RestoreCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retire(self) -> RetireRequestBuilder:
        """
        Provides operations to call the retire method.
        """
        from .retire.retire_request_builder import RetireRequestBuilder

        return RetireRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def revoke_apple_vpp_licenses(self) -> RevokeAppleVppLicensesRequestBuilder:
        """
        Provides operations to call the revokeAppleVppLicenses method.
        """
        from .revoke_apple_vpp_licenses.revoke_apple_vpp_licenses_request_builder import RevokeAppleVppLicensesRequestBuilder

        return RevokeAppleVppLicensesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rotate_bit_locker_keys(self) -> RotateBitLockerKeysRequestBuilder:
        """
        Provides operations to call the rotateBitLockerKeys method.
        """
        from .rotate_bit_locker_keys.rotate_bit_locker_keys_request_builder import RotateBitLockerKeysRequestBuilder

        return RotateBitLockerKeysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rotate_file_vault_key(self) -> RotateFileVaultKeyRequestBuilder:
        """
        Provides operations to call the rotateFileVaultKey method.
        """
        from .rotate_file_vault_key.rotate_file_vault_key_request_builder import RotateFileVaultKeyRequestBuilder

        return RotateFileVaultKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rotate_local_admin_password(self) -> RotateLocalAdminPasswordRequestBuilder:
        """
        Provides operations to call the rotateLocalAdminPassword method.
        """
        from .rotate_local_admin_password.rotate_local_admin_password_request_builder import RotateLocalAdminPasswordRequestBuilder

        return RotateLocalAdminPasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security_baseline_states(self) -> SecurityBaselineStatesRequestBuilder:
        """
        Provides operations to manage the securityBaselineStates property of the microsoft.graph.managedDevice entity.
        """
        from .security_baseline_states.security_baseline_states_request_builder import SecurityBaselineStatesRequestBuilder

        return SecurityBaselineStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_custom_notification_to_company_portal(self) -> SendCustomNotificationToCompanyPortalRequestBuilder:
        """
        Provides operations to call the sendCustomNotificationToCompanyPortal method.
        """
        from .send_custom_notification_to_company_portal.send_custom_notification_to_company_portal_request_builder import SendCustomNotificationToCompanyPortalRequestBuilder

        return SendCustomNotificationToCompanyPortalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_cloud_pc_review_status(self) -> SetCloudPcReviewStatusRequestBuilder:
        """
        Provides operations to call the setCloudPcReviewStatus method.
        """
        from .set_cloud_pc_review_status.set_cloud_pc_review_status_request_builder import SetCloudPcReviewStatusRequestBuilder

        return SetCloudPcReviewStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_device_name(self) -> SetDeviceNameRequestBuilder:
        """
        Provides operations to call the setDeviceName method.
        """
        from .set_device_name.set_device_name_request_builder import SetDeviceNameRequestBuilder

        return SetDeviceNameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shut_down(self) -> ShutDownRequestBuilder:
        """
        Provides operations to call the shutDown method.
        """
        from .shut_down.shut_down_request_builder import ShutDownRequestBuilder

        return ShutDownRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync_device(self) -> SyncDeviceRequestBuilder:
        """
        Provides operations to call the syncDevice method.
        """
        from .sync_device.sync_device_request_builder import SyncDeviceRequestBuilder

        return SyncDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trigger_configuration_manager_action(self) -> TriggerConfigurationManagerActionRequestBuilder:
        """
        Provides operations to call the triggerConfigurationManagerAction method.
        """
        from .trigger_configuration_manager_action.trigger_configuration_manager_action_request_builder import TriggerConfigurationManagerActionRequestBuilder

        return TriggerConfigurationManagerActionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_windows_device_account(self) -> UpdateWindowsDeviceAccountRequestBuilder:
        """
        Provides operations to call the updateWindowsDeviceAccount method.
        """
        from .update_windows_device_account.update_windows_device_account_request_builder import UpdateWindowsDeviceAccountRequestBuilder

        return UpdateWindowsDeviceAccountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> UsersRequestBuilder:
        """
        Provides operations to manage the users property of the microsoft.graph.managedDevice entity.
        """
        from .users.users_request_builder import UsersRequestBuilder

        return UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_defender_scan(self) -> WindowsDefenderScanRequestBuilder:
        """
        Provides operations to call the windowsDefenderScan method.
        """
        from .windows_defender_scan.windows_defender_scan_request_builder import WindowsDefenderScanRequestBuilder

        return WindowsDefenderScanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_defender_update_signatures(self) -> WindowsDefenderUpdateSignaturesRequestBuilder:
        """
        Provides operations to call the windowsDefenderUpdateSignatures method.
        """
        from .windows_defender_update_signatures.windows_defender_update_signatures_request_builder import WindowsDefenderUpdateSignaturesRequestBuilder

        return WindowsDefenderUpdateSignaturesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_protection_state(self) -> WindowsProtectionStateRequestBuilder:
        """
        Provides operations to manage the windowsProtectionState property of the microsoft.graph.managedDevice entity.
        """
        from .windows_protection_state.windows_protection_state_request_builder import WindowsProtectionStateRequestBuilder

        return WindowsProtectionStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wipe(self) -> WipeRequestBuilder:
        """
        Provides operations to call the wipe method.
        """
        from .wipe.wipe_request_builder import WipeRequestBuilder

        return WipeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ManagedDeviceItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManagedDeviceItemRequestBuilderGetQueryParameters():
        """
        The list of co-managed devices report
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
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

    
    @dataclass
    class ManagedDeviceItemRequestBuilderGetRequestConfiguration(RequestConfiguration[ManagedDeviceItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManagedDeviceItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

