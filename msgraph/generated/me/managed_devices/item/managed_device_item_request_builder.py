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
    from ....models import managed_device
    from ....models.o_data_errors import o_data_error
    from .activate_device_esim import activate_device_esim_request_builder
    from .assignment_filter_evaluation_status_details import assignment_filter_evaluation_status_details_request_builder
    from .bypass_activation_lock import bypass_activation_lock_request_builder
    from .clean_windows_device import clean_windows_device_request_builder
    from .create_device_log_collection_request import create_device_log_collection_request_request_builder
    from .delete_user_from_shared_apple_device import delete_user_from_shared_apple_device_request_builder
    from .deprovision import deprovision_request_builder
    from .detected_apps import detected_apps_request_builder
    from .device_category import device_category_request_builder
    from .device_compliance_policy_states import device_compliance_policy_states_request_builder
    from .device_configuration_states import device_configuration_states_request_builder
    from .device_health_script_states import device_health_script_states_request_builder
    from .disable import disable_request_builder
    from .disable_lost_mode import disable_lost_mode_request_builder
    from .enable_lost_mode import enable_lost_mode_request_builder
    from .enroll_now_action import enroll_now_action_request_builder
    from .get_cloud_pc_remote_action_results import get_cloud_pc_remote_action_results_request_builder
    from .get_cloud_pc_review_status import get_cloud_pc_review_status_request_builder
    from .get_file_vault_key import get_file_vault_key_request_builder
    from .get_non_compliant_settings import get_non_compliant_settings_request_builder
    from .get_oem_warranty import get_oem_warranty_request_builder
    from .initiate_mobile_device_management_key_recovery import initiate_mobile_device_management_key_recovery_request_builder
    from .initiate_on_demand_proactive_remediation import initiate_on_demand_proactive_remediation_request_builder
    from .locate_device import locate_device_request_builder
    from .log_collection_requests import log_collection_requests_request_builder
    from .logout_shared_apple_device_active_user import logout_shared_apple_device_active_user_request_builder
    from .managed_device_mobile_app_configuration_states import managed_device_mobile_app_configuration_states_request_builder
    from .override_compliance_state import override_compliance_state_request_builder
    from .play_lost_mode_sound import play_lost_mode_sound_request_builder
    from .reboot_now import reboot_now_request_builder
    from .recover_passcode import recover_passcode_request_builder
    from .reenable import reenable_request_builder
    from .remote_lock import remote_lock_request_builder
    from .remove_device_firmware_configuration_interface_management import remove_device_firmware_configuration_interface_management_request_builder
    from .reprovision_cloud_pc import reprovision_cloud_pc_request_builder
    from .request_remote_assistance import request_remote_assistance_request_builder
    from .reset_passcode import reset_passcode_request_builder
    from .resize_cloud_pc import resize_cloud_pc_request_builder
    from .restore_cloud_pc import restore_cloud_pc_request_builder
    from .retire import retire_request_builder
    from .revoke_apple_vpp_licenses import revoke_apple_vpp_licenses_request_builder
    from .rotate_bit_locker_keys import rotate_bit_locker_keys_request_builder
    from .rotate_file_vault_key import rotate_file_vault_key_request_builder
    from .rotate_local_admin_password import rotate_local_admin_password_request_builder
    from .security_baseline_states import security_baseline_states_request_builder
    from .send_custom_notification_to_company_portal import send_custom_notification_to_company_portal_request_builder
    from .set_cloud_pc_review_status import set_cloud_pc_review_status_request_builder
    from .set_device_name import set_device_name_request_builder
    from .shut_down import shut_down_request_builder
    from .sync_device import sync_device_request_builder
    from .trigger_configuration_manager_action import trigger_configuration_manager_action_request_builder
    from .update_windows_device_account import update_windows_device_account_request_builder
    from .users import users_request_builder
    from .windows_defender_scan import windows_defender_scan_request_builder
    from .windows_defender_update_signatures import windows_defender_update_signatures_request_builder
    from .windows_protection_state import windows_protection_state_request_builder
    from .wipe import wipe_request_builder

class ManagedDeviceItemRequestBuilder():
    """
    Provides operations to manage the managedDevices property of the microsoft.graph.user entity.
    """
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
    
    async def delete(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property managedDevices for me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[managed_device.ManagedDevice]:
        """
        The managed devices associated with the user.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_device.ManagedDevice]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import managed_device

        return await self.request_adapter.send_async(request_info, managed_device.ManagedDevice, error_mapping)
    
    async def patch(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ManagedDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[managed_device.ManagedDevice]:
        """
        Update the navigation property managedDevices in me
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
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import managed_device

        return await self.request_adapter.send_async(request_info, managed_device.ManagedDevice, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
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
    
    def to_get_request_information(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ManagedDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def activate_device_esim(self) -> activate_device_esim_request_builder.ActivateDeviceEsimRequestBuilder:
        """
        Provides operations to call the activateDeviceEsim method.
        """
        from .activate_device_esim import activate_device_esim_request_builder

        return activate_device_esim_request_builder.ActivateDeviceEsimRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_filter_evaluation_status_details(self) -> assignment_filter_evaluation_status_details_request_builder.AssignmentFilterEvaluationStatusDetailsRequestBuilder:
        """
        Provides operations to manage the assignmentFilterEvaluationStatusDetails property of the microsoft.graph.managedDevice entity.
        """
        from .assignment_filter_evaluation_status_details import assignment_filter_evaluation_status_details_request_builder

        return assignment_filter_evaluation_status_details_request_builder.AssignmentFilterEvaluationStatusDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bypass_activation_lock(self) -> bypass_activation_lock_request_builder.BypassActivationLockRequestBuilder:
        """
        Provides operations to call the bypassActivationLock method.
        """
        from .bypass_activation_lock import bypass_activation_lock_request_builder

        return bypass_activation_lock_request_builder.BypassActivationLockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clean_windows_device(self) -> clean_windows_device_request_builder.CleanWindowsDeviceRequestBuilder:
        """
        Provides operations to call the cleanWindowsDevice method.
        """
        from .clean_windows_device import clean_windows_device_request_builder

        return clean_windows_device_request_builder.CleanWindowsDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_device_log_collection_request(self) -> create_device_log_collection_request_request_builder.CreateDeviceLogCollectionRequestRequestBuilder:
        """
        Provides operations to call the createDeviceLogCollectionRequest method.
        """
        from .create_device_log_collection_request import create_device_log_collection_request_request_builder

        return create_device_log_collection_request_request_builder.CreateDeviceLogCollectionRequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delete_user_from_shared_apple_device(self) -> delete_user_from_shared_apple_device_request_builder.DeleteUserFromSharedAppleDeviceRequestBuilder:
        """
        Provides operations to call the deleteUserFromSharedAppleDevice method.
        """
        from .delete_user_from_shared_apple_device import delete_user_from_shared_apple_device_request_builder

        return delete_user_from_shared_apple_device_request_builder.DeleteUserFromSharedAppleDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deprovision(self) -> deprovision_request_builder.DeprovisionRequestBuilder:
        """
        Provides operations to call the deprovision method.
        """
        from .deprovision import deprovision_request_builder

        return deprovision_request_builder.DeprovisionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def detected_apps(self) -> detected_apps_request_builder.DetectedAppsRequestBuilder:
        """
        Provides operations to manage the detectedApps property of the microsoft.graph.managedDevice entity.
        """
        from .detected_apps import detected_apps_request_builder

        return detected_apps_request_builder.DetectedAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_category(self) -> device_category_request_builder.DeviceCategoryRequestBuilder:
        """
        Provides operations to manage the deviceCategory property of the microsoft.graph.managedDevice entity.
        """
        from .device_category import device_category_request_builder

        return device_category_request_builder.DeviceCategoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_states(self) -> device_compliance_policy_states_request_builder.DeviceCompliancePolicyStatesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicyStates property of the microsoft.graph.managedDevice entity.
        """
        from .device_compliance_policy_states import device_compliance_policy_states_request_builder

        return device_compliance_policy_states_request_builder.DeviceCompliancePolicyStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_states(self) -> device_configuration_states_request_builder.DeviceConfigurationStatesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationStates property of the microsoft.graph.managedDevice entity.
        """
        from .device_configuration_states import device_configuration_states_request_builder

        return device_configuration_states_request_builder.DeviceConfigurationStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_health_script_states(self) -> device_health_script_states_request_builder.DeviceHealthScriptStatesRequestBuilder:
        """
        Provides operations to manage the deviceHealthScriptStates property of the microsoft.graph.managedDevice entity.
        """
        from .device_health_script_states import device_health_script_states_request_builder

        return device_health_script_states_request_builder.DeviceHealthScriptStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def disable(self) -> disable_request_builder.DisableRequestBuilder:
        """
        Provides operations to call the disable method.
        """
        from .disable import disable_request_builder

        return disable_request_builder.DisableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def disable_lost_mode(self) -> disable_lost_mode_request_builder.DisableLostModeRequestBuilder:
        """
        Provides operations to call the disableLostMode method.
        """
        from .disable_lost_mode import disable_lost_mode_request_builder

        return disable_lost_mode_request_builder.DisableLostModeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable_lost_mode(self) -> enable_lost_mode_request_builder.EnableLostModeRequestBuilder:
        """
        Provides operations to call the enableLostMode method.
        """
        from .enable_lost_mode import enable_lost_mode_request_builder

        return enable_lost_mode_request_builder.EnableLostModeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enroll_now_action(self) -> enroll_now_action_request_builder.EnrollNowActionRequestBuilder:
        """
        Provides operations to call the enrollNowAction method.
        """
        from .enroll_now_action import enroll_now_action_request_builder

        return enroll_now_action_request_builder.EnrollNowActionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_cloud_pc_remote_action_results(self) -> get_cloud_pc_remote_action_results_request_builder.GetCloudPcRemoteActionResultsRequestBuilder:
        """
        Provides operations to call the getCloudPcRemoteActionResults method.
        """
        from .get_cloud_pc_remote_action_results import get_cloud_pc_remote_action_results_request_builder

        return get_cloud_pc_remote_action_results_request_builder.GetCloudPcRemoteActionResultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_cloud_pc_review_status(self) -> get_cloud_pc_review_status_request_builder.GetCloudPcReviewStatusRequestBuilder:
        """
        Provides operations to call the getCloudPcReviewStatus method.
        """
        from .get_cloud_pc_review_status import get_cloud_pc_review_status_request_builder

        return get_cloud_pc_review_status_request_builder.GetCloudPcReviewStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_file_vault_key(self) -> get_file_vault_key_request_builder.GetFileVaultKeyRequestBuilder:
        """
        Provides operations to call the getFileVaultKey method.
        """
        from .get_file_vault_key import get_file_vault_key_request_builder

        return get_file_vault_key_request_builder.GetFileVaultKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_non_compliant_settings(self) -> get_non_compliant_settings_request_builder.GetNonCompliantSettingsRequestBuilder:
        """
        Provides operations to call the getNonCompliantSettings method.
        """
        from .get_non_compliant_settings import get_non_compliant_settings_request_builder

        return get_non_compliant_settings_request_builder.GetNonCompliantSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_oem_warranty(self) -> get_oem_warranty_request_builder.GetOemWarrantyRequestBuilder:
        """
        Provides operations to call the getOemWarranty method.
        """
        from .get_oem_warranty import get_oem_warranty_request_builder

        return get_oem_warranty_request_builder.GetOemWarrantyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def initiate_mobile_device_management_key_recovery(self) -> initiate_mobile_device_management_key_recovery_request_builder.InitiateMobileDeviceManagementKeyRecoveryRequestBuilder:
        """
        Provides operations to call the initiateMobileDeviceManagementKeyRecovery method.
        """
        from .initiate_mobile_device_management_key_recovery import initiate_mobile_device_management_key_recovery_request_builder

        return initiate_mobile_device_management_key_recovery_request_builder.InitiateMobileDeviceManagementKeyRecoveryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def initiate_on_demand_proactive_remediation(self) -> initiate_on_demand_proactive_remediation_request_builder.InitiateOnDemandProactiveRemediationRequestBuilder:
        """
        Provides operations to call the initiateOnDemandProactiveRemediation method.
        """
        from .initiate_on_demand_proactive_remediation import initiate_on_demand_proactive_remediation_request_builder

        return initiate_on_demand_proactive_remediation_request_builder.InitiateOnDemandProactiveRemediationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def locate_device(self) -> locate_device_request_builder.LocateDeviceRequestBuilder:
        """
        Provides operations to call the locateDevice method.
        """
        from .locate_device import locate_device_request_builder

        return locate_device_request_builder.LocateDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log_collection_requests(self) -> log_collection_requests_request_builder.LogCollectionRequestsRequestBuilder:
        """
        Provides operations to manage the logCollectionRequests property of the microsoft.graph.managedDevice entity.
        """
        from .log_collection_requests import log_collection_requests_request_builder

        return log_collection_requests_request_builder.LogCollectionRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logout_shared_apple_device_active_user(self) -> logout_shared_apple_device_active_user_request_builder.LogoutSharedAppleDeviceActiveUserRequestBuilder:
        """
        Provides operations to call the logoutSharedAppleDeviceActiveUser method.
        """
        from .logout_shared_apple_device_active_user import logout_shared_apple_device_active_user_request_builder

        return logout_shared_apple_device_active_user_request_builder.LogoutSharedAppleDeviceActiveUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_mobile_app_configuration_states(self) -> managed_device_mobile_app_configuration_states_request_builder.ManagedDeviceMobileAppConfigurationStatesRequestBuilder:
        """
        Provides operations to manage the managedDeviceMobileAppConfigurationStates property of the microsoft.graph.managedDevice entity.
        """
        from .managed_device_mobile_app_configuration_states import managed_device_mobile_app_configuration_states_request_builder

        return managed_device_mobile_app_configuration_states_request_builder.ManagedDeviceMobileAppConfigurationStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def override_compliance_state(self) -> override_compliance_state_request_builder.OverrideComplianceStateRequestBuilder:
        """
        Provides operations to call the overrideComplianceState method.
        """
        from .override_compliance_state import override_compliance_state_request_builder

        return override_compliance_state_request_builder.OverrideComplianceStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def play_lost_mode_sound(self) -> play_lost_mode_sound_request_builder.PlayLostModeSoundRequestBuilder:
        """
        Provides operations to call the playLostModeSound method.
        """
        from .play_lost_mode_sound import play_lost_mode_sound_request_builder

        return play_lost_mode_sound_request_builder.PlayLostModeSoundRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reboot_now(self) -> reboot_now_request_builder.RebootNowRequestBuilder:
        """
        Provides operations to call the rebootNow method.
        """
        from .reboot_now import reboot_now_request_builder

        return reboot_now_request_builder.RebootNowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recover_passcode(self) -> recover_passcode_request_builder.RecoverPasscodeRequestBuilder:
        """
        Provides operations to call the recoverPasscode method.
        """
        from .recover_passcode import recover_passcode_request_builder

        return recover_passcode_request_builder.RecoverPasscodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reenable(self) -> reenable_request_builder.ReenableRequestBuilder:
        """
        Provides operations to call the reenable method.
        """
        from .reenable import reenable_request_builder

        return reenable_request_builder.ReenableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_lock(self) -> remote_lock_request_builder.RemoteLockRequestBuilder:
        """
        Provides operations to call the remoteLock method.
        """
        from .remote_lock import remote_lock_request_builder

        return remote_lock_request_builder.RemoteLockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_device_firmware_configuration_interface_management(self) -> remove_device_firmware_configuration_interface_management_request_builder.RemoveDeviceFirmwareConfigurationInterfaceManagementRequestBuilder:
        """
        Provides operations to call the removeDeviceFirmwareConfigurationInterfaceManagement method.
        """
        from .remove_device_firmware_configuration_interface_management import remove_device_firmware_configuration_interface_management_request_builder

        return remove_device_firmware_configuration_interface_management_request_builder.RemoveDeviceFirmwareConfigurationInterfaceManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reprovision_cloud_pc(self) -> reprovision_cloud_pc_request_builder.ReprovisionCloudPcRequestBuilder:
        """
        Provides operations to call the reprovisionCloudPc method.
        """
        from .reprovision_cloud_pc import reprovision_cloud_pc_request_builder

        return reprovision_cloud_pc_request_builder.ReprovisionCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def request_remote_assistance(self) -> request_remote_assistance_request_builder.RequestRemoteAssistanceRequestBuilder:
        """
        Provides operations to call the requestRemoteAssistance method.
        """
        from .request_remote_assistance import request_remote_assistance_request_builder

        return request_remote_assistance_request_builder.RequestRemoteAssistanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_passcode(self) -> reset_passcode_request_builder.ResetPasscodeRequestBuilder:
        """
        Provides operations to call the resetPasscode method.
        """
        from .reset_passcode import reset_passcode_request_builder

        return reset_passcode_request_builder.ResetPasscodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resize_cloud_pc(self) -> resize_cloud_pc_request_builder.ResizeCloudPcRequestBuilder:
        """
        Provides operations to call the resizeCloudPc method.
        """
        from .resize_cloud_pc import resize_cloud_pc_request_builder

        return resize_cloud_pc_request_builder.ResizeCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore_cloud_pc(self) -> restore_cloud_pc_request_builder.RestoreCloudPcRequestBuilder:
        """
        Provides operations to call the restoreCloudPc method.
        """
        from .restore_cloud_pc import restore_cloud_pc_request_builder

        return restore_cloud_pc_request_builder.RestoreCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retire(self) -> retire_request_builder.RetireRequestBuilder:
        """
        Provides operations to call the retire method.
        """
        from .retire import retire_request_builder

        return retire_request_builder.RetireRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def revoke_apple_vpp_licenses(self) -> revoke_apple_vpp_licenses_request_builder.RevokeAppleVppLicensesRequestBuilder:
        """
        Provides operations to call the revokeAppleVppLicenses method.
        """
        from .revoke_apple_vpp_licenses import revoke_apple_vpp_licenses_request_builder

        return revoke_apple_vpp_licenses_request_builder.RevokeAppleVppLicensesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rotate_bit_locker_keys(self) -> rotate_bit_locker_keys_request_builder.RotateBitLockerKeysRequestBuilder:
        """
        Provides operations to call the rotateBitLockerKeys method.
        """
        from .rotate_bit_locker_keys import rotate_bit_locker_keys_request_builder

        return rotate_bit_locker_keys_request_builder.RotateBitLockerKeysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rotate_file_vault_key(self) -> rotate_file_vault_key_request_builder.RotateFileVaultKeyRequestBuilder:
        """
        Provides operations to call the rotateFileVaultKey method.
        """
        from .rotate_file_vault_key import rotate_file_vault_key_request_builder

        return rotate_file_vault_key_request_builder.RotateFileVaultKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rotate_local_admin_password(self) -> rotate_local_admin_password_request_builder.RotateLocalAdminPasswordRequestBuilder:
        """
        Provides operations to call the rotateLocalAdminPassword method.
        """
        from .rotate_local_admin_password import rotate_local_admin_password_request_builder

        return rotate_local_admin_password_request_builder.RotateLocalAdminPasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security_baseline_states(self) -> security_baseline_states_request_builder.SecurityBaselineStatesRequestBuilder:
        """
        Provides operations to manage the securityBaselineStates property of the microsoft.graph.managedDevice entity.
        """
        from .security_baseline_states import security_baseline_states_request_builder

        return security_baseline_states_request_builder.SecurityBaselineStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_custom_notification_to_company_portal(self) -> send_custom_notification_to_company_portal_request_builder.SendCustomNotificationToCompanyPortalRequestBuilder:
        """
        Provides operations to call the sendCustomNotificationToCompanyPortal method.
        """
        from .send_custom_notification_to_company_portal import send_custom_notification_to_company_portal_request_builder

        return send_custom_notification_to_company_portal_request_builder.SendCustomNotificationToCompanyPortalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_cloud_pc_review_status(self) -> set_cloud_pc_review_status_request_builder.SetCloudPcReviewStatusRequestBuilder:
        """
        Provides operations to call the setCloudPcReviewStatus method.
        """
        from .set_cloud_pc_review_status import set_cloud_pc_review_status_request_builder

        return set_cloud_pc_review_status_request_builder.SetCloudPcReviewStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_device_name(self) -> set_device_name_request_builder.SetDeviceNameRequestBuilder:
        """
        Provides operations to call the setDeviceName method.
        """
        from .set_device_name import set_device_name_request_builder

        return set_device_name_request_builder.SetDeviceNameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shut_down(self) -> shut_down_request_builder.ShutDownRequestBuilder:
        """
        Provides operations to call the shutDown method.
        """
        from .shut_down import shut_down_request_builder

        return shut_down_request_builder.ShutDownRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync_device(self) -> sync_device_request_builder.SyncDeviceRequestBuilder:
        """
        Provides operations to call the syncDevice method.
        """
        from .sync_device import sync_device_request_builder

        return sync_device_request_builder.SyncDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trigger_configuration_manager_action(self) -> trigger_configuration_manager_action_request_builder.TriggerConfigurationManagerActionRequestBuilder:
        """
        Provides operations to call the triggerConfigurationManagerAction method.
        """
        from .trigger_configuration_manager_action import trigger_configuration_manager_action_request_builder

        return trigger_configuration_manager_action_request_builder.TriggerConfigurationManagerActionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_windows_device_account(self) -> update_windows_device_account_request_builder.UpdateWindowsDeviceAccountRequestBuilder:
        """
        Provides operations to call the updateWindowsDeviceAccount method.
        """
        from .update_windows_device_account import update_windows_device_account_request_builder

        return update_windows_device_account_request_builder.UpdateWindowsDeviceAccountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> users_request_builder.UsersRequestBuilder:
        """
        Provides operations to manage the users property of the microsoft.graph.managedDevice entity.
        """
        from .users import users_request_builder

        return users_request_builder.UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_defender_scan(self) -> windows_defender_scan_request_builder.WindowsDefenderScanRequestBuilder:
        """
        Provides operations to call the windowsDefenderScan method.
        """
        from .windows_defender_scan import windows_defender_scan_request_builder

        return windows_defender_scan_request_builder.WindowsDefenderScanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_defender_update_signatures(self) -> windows_defender_update_signatures_request_builder.WindowsDefenderUpdateSignaturesRequestBuilder:
        """
        Provides operations to call the windowsDefenderUpdateSignatures method.
        """
        from .windows_defender_update_signatures import windows_defender_update_signatures_request_builder

        return windows_defender_update_signatures_request_builder.WindowsDefenderUpdateSignaturesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_protection_state(self) -> windows_protection_state_request_builder.WindowsProtectionStateRequestBuilder:
        """
        Provides operations to manage the windowsProtectionState property of the microsoft.graph.managedDevice entity.
        """
        from .windows_protection_state import windows_protection_state_request_builder

        return windows_protection_state_request_builder.WindowsProtectionStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wipe(self) -> wipe_request_builder.WipeRequestBuilder:
        """
        Provides operations to call the wipe method.
        """
        from .wipe import wipe_request_builder

        return wipe_request_builder.WipeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ManagedDeviceItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ManagedDeviceItemRequestBuilderGetQueryParameters():
        """
        The managed devices associated with the user.
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
    class ManagedDeviceItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

