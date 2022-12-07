from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_locker_application_control_type = lazy_import('msgraph.generated.models.app_locker_application_control_type')
application_guard_block_clipboard_sharing_type = lazy_import('msgraph.generated.models.application_guard_block_clipboard_sharing_type')
application_guard_block_file_transfer_type = lazy_import('msgraph.generated.models.application_guard_block_file_transfer_type')
application_guard_enabled_options = lazy_import('msgraph.generated.models.application_guard_enabled_options')
bit_locker_fixed_drive_policy = lazy_import('msgraph.generated.models.bit_locker_fixed_drive_policy')
bit_locker_recovery_password_rotation_type = lazy_import('msgraph.generated.models.bit_locker_recovery_password_rotation_type')
bit_locker_removable_drive_policy = lazy_import('msgraph.generated.models.bit_locker_removable_drive_policy')
bit_locker_system_drive_policy = lazy_import('msgraph.generated.models.bit_locker_system_drive_policy')
defender_attack_surface_type = lazy_import('msgraph.generated.models.defender_attack_surface_type')
defender_cloud_block_level_type = lazy_import('msgraph.generated.models.defender_cloud_block_level_type')
defender_detected_malware_actions = lazy_import('msgraph.generated.models.defender_detected_malware_actions')
defender_protection_type = lazy_import('msgraph.generated.models.defender_protection_type')
defender_realtime_scan_direction = lazy_import('msgraph.generated.models.defender_realtime_scan_direction')
defender_scan_type = lazy_import('msgraph.generated.models.defender_scan_type')
defender_security_center_i_t_contact_display_type = lazy_import('msgraph.generated.models.defender_security_center_i_t_contact_display_type')
defender_security_center_notifications_from_app_type = lazy_import('msgraph.generated.models.defender_security_center_notifications_from_app_type')
defender_submit_samples_consent_type = lazy_import('msgraph.generated.models.defender_submit_samples_consent_type')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
device_guard_local_system_authority_credential_guard_type = lazy_import('msgraph.generated.models.device_guard_local_system_authority_credential_guard_type')
device_management_user_rights_setting = lazy_import('msgraph.generated.models.device_management_user_rights_setting')
dma_guard_device_enumeration_policy_type = lazy_import('msgraph.generated.models.dma_guard_device_enumeration_policy_type')
enablement = lazy_import('msgraph.generated.models.enablement')
firewall_certificate_revocation_list_check_method_type = lazy_import('msgraph.generated.models.firewall_certificate_revocation_list_check_method_type')
firewall_packet_queueing_method_type = lazy_import('msgraph.generated.models.firewall_packet_queueing_method_type')
firewall_pre_shared_key_encoding_method_type = lazy_import('msgraph.generated.models.firewall_pre_shared_key_encoding_method_type')
folder_protection_type = lazy_import('msgraph.generated.models.folder_protection_type')
lan_manager_authentication_level = lazy_import('msgraph.generated.models.lan_manager_authentication_level')
local_security_options_administrator_elevation_prompt_behavior_type = lazy_import('msgraph.generated.models.local_security_options_administrator_elevation_prompt_behavior_type')
local_security_options_format_and_eject_of_removable_media_allowed_user_type = lazy_import('msgraph.generated.models.local_security_options_format_and_eject_of_removable_media_allowed_user_type')
local_security_options_information_displayed_on_lock_screen_type = lazy_import('msgraph.generated.models.local_security_options_information_displayed_on_lock_screen_type')
local_security_options_information_shown_on_lock_screen_type = lazy_import('msgraph.generated.models.local_security_options_information_shown_on_lock_screen_type')
local_security_options_minimum_session_security = lazy_import('msgraph.generated.models.local_security_options_minimum_session_security')
local_security_options_smart_card_removal_behavior_type = lazy_import('msgraph.generated.models.local_security_options_smart_card_removal_behavior_type')
local_security_options_standard_user_elevation_prompt_behavior_type = lazy_import('msgraph.generated.models.local_security_options_standard_user_elevation_prompt_behavior_type')
secure_boot_with_d_m_a_type = lazy_import('msgraph.generated.models.secure_boot_with_d_m_a_type')
service_start_type = lazy_import('msgraph.generated.models.service_start_type')
weekly_schedule = lazy_import('msgraph.generated.models.weekly_schedule')
windows_defender_tamper_protection_options = lazy_import('msgraph.generated.models.windows_defender_tamper_protection_options')
windows_firewall_network_profile = lazy_import('msgraph.generated.models.windows_firewall_network_profile')
windows_firewall_rule = lazy_import('msgraph.generated.models.windows_firewall_rule')

class Windows10EndpointProtectionConfiguration(device_configuration.DeviceConfiguration):
    @property
    def application_guard_allow_camera_microphone_redirection(self,) -> Optional[bool]:
        """
        Gets the applicationGuardAllowCameraMicrophoneRedirection property value. Gets or sets whether applications inside Microsoft Defender Application Guard can access the device’s camera and microphone.
        Returns: Optional[bool]
        """
        return self._application_guard_allow_camera_microphone_redirection
    
    @application_guard_allow_camera_microphone_redirection.setter
    def application_guard_allow_camera_microphone_redirection(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardAllowCameraMicrophoneRedirection property value. Gets or sets whether applications inside Microsoft Defender Application Guard can access the device’s camera and microphone.
        Args:
            value: Value to set for the applicationGuardAllowCameraMicrophoneRedirection property.
        """
        self._application_guard_allow_camera_microphone_redirection = value
    
    @property
    def application_guard_allow_file_save_on_host(self,) -> Optional[bool]:
        """
        Gets the applicationGuardAllowFileSaveOnHost property value. Allow users to download files from Edge in the application guard container and save them on the host file system
        Returns: Optional[bool]
        """
        return self._application_guard_allow_file_save_on_host
    
    @application_guard_allow_file_save_on_host.setter
    def application_guard_allow_file_save_on_host(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardAllowFileSaveOnHost property value. Allow users to download files from Edge in the application guard container and save them on the host file system
        Args:
            value: Value to set for the applicationGuardAllowFileSaveOnHost property.
        """
        self._application_guard_allow_file_save_on_host = value
    
    @property
    def application_guard_allow_persistence(self,) -> Optional[bool]:
        """
        Gets the applicationGuardAllowPersistence property value. Allow persisting user generated data inside the App Guard Containter (favorites, cookies, web passwords, etc.)
        Returns: Optional[bool]
        """
        return self._application_guard_allow_persistence
    
    @application_guard_allow_persistence.setter
    def application_guard_allow_persistence(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardAllowPersistence property value. Allow persisting user generated data inside the App Guard Containter (favorites, cookies, web passwords, etc.)
        Args:
            value: Value to set for the applicationGuardAllowPersistence property.
        """
        self._application_guard_allow_persistence = value
    
    @property
    def application_guard_allow_print_to_local_printers(self,) -> Optional[bool]:
        """
        Gets the applicationGuardAllowPrintToLocalPrinters property value. Allow printing to Local Printers from Container
        Returns: Optional[bool]
        """
        return self._application_guard_allow_print_to_local_printers
    
    @application_guard_allow_print_to_local_printers.setter
    def application_guard_allow_print_to_local_printers(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardAllowPrintToLocalPrinters property value. Allow printing to Local Printers from Container
        Args:
            value: Value to set for the applicationGuardAllowPrintToLocalPrinters property.
        """
        self._application_guard_allow_print_to_local_printers = value
    
    @property
    def application_guard_allow_print_to_network_printers(self,) -> Optional[bool]:
        """
        Gets the applicationGuardAllowPrintToNetworkPrinters property value. Allow printing to Network Printers from Container
        Returns: Optional[bool]
        """
        return self._application_guard_allow_print_to_network_printers
    
    @application_guard_allow_print_to_network_printers.setter
    def application_guard_allow_print_to_network_printers(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardAllowPrintToNetworkPrinters property value. Allow printing to Network Printers from Container
        Args:
            value: Value to set for the applicationGuardAllowPrintToNetworkPrinters property.
        """
        self._application_guard_allow_print_to_network_printers = value
    
    @property
    def application_guard_allow_print_to_p_d_f(self,) -> Optional[bool]:
        """
        Gets the applicationGuardAllowPrintToPDF property value. Allow printing to PDF from Container
        Returns: Optional[bool]
        """
        return self._application_guard_allow_print_to_p_d_f
    
    @application_guard_allow_print_to_p_d_f.setter
    def application_guard_allow_print_to_p_d_f(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardAllowPrintToPDF property value. Allow printing to PDF from Container
        Args:
            value: Value to set for the applicationGuardAllowPrintToPDF property.
        """
        self._application_guard_allow_print_to_p_d_f = value
    
    @property
    def application_guard_allow_print_to_x_p_s(self,) -> Optional[bool]:
        """
        Gets the applicationGuardAllowPrintToXPS property value. Allow printing to XPS from Container
        Returns: Optional[bool]
        """
        return self._application_guard_allow_print_to_x_p_s
    
    @application_guard_allow_print_to_x_p_s.setter
    def application_guard_allow_print_to_x_p_s(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardAllowPrintToXPS property value. Allow printing to XPS from Container
        Args:
            value: Value to set for the applicationGuardAllowPrintToXPS property.
        """
        self._application_guard_allow_print_to_x_p_s = value
    
    @property
    def application_guard_allow_virtual_g_p_u(self,) -> Optional[bool]:
        """
        Gets the applicationGuardAllowVirtualGPU property value. Allow application guard to use virtual GPU
        Returns: Optional[bool]
        """
        return self._application_guard_allow_virtual_g_p_u
    
    @application_guard_allow_virtual_g_p_u.setter
    def application_guard_allow_virtual_g_p_u(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardAllowVirtualGPU property value. Allow application guard to use virtual GPU
        Args:
            value: Value to set for the applicationGuardAllowVirtualGPU property.
        """
        self._application_guard_allow_virtual_g_p_u = value
    
    @property
    def application_guard_block_clipboard_sharing(self,) -> Optional[application_guard_block_clipboard_sharing_type.ApplicationGuardBlockClipboardSharingType]:
        """
        Gets the applicationGuardBlockClipboardSharing property value. Possible values for applicationGuardBlockClipboardSharingType
        Returns: Optional[application_guard_block_clipboard_sharing_type.ApplicationGuardBlockClipboardSharingType]
        """
        return self._application_guard_block_clipboard_sharing
    
    @application_guard_block_clipboard_sharing.setter
    def application_guard_block_clipboard_sharing(self,value: Optional[application_guard_block_clipboard_sharing_type.ApplicationGuardBlockClipboardSharingType] = None) -> None:
        """
        Sets the applicationGuardBlockClipboardSharing property value. Possible values for applicationGuardBlockClipboardSharingType
        Args:
            value: Value to set for the applicationGuardBlockClipboardSharing property.
        """
        self._application_guard_block_clipboard_sharing = value
    
    @property
    def application_guard_block_file_transfer(self,) -> Optional[application_guard_block_file_transfer_type.ApplicationGuardBlockFileTransferType]:
        """
        Gets the applicationGuardBlockFileTransfer property value. Possible values for applicationGuardBlockFileTransfer
        Returns: Optional[application_guard_block_file_transfer_type.ApplicationGuardBlockFileTransferType]
        """
        return self._application_guard_block_file_transfer
    
    @application_guard_block_file_transfer.setter
    def application_guard_block_file_transfer(self,value: Optional[application_guard_block_file_transfer_type.ApplicationGuardBlockFileTransferType] = None) -> None:
        """
        Sets the applicationGuardBlockFileTransfer property value. Possible values for applicationGuardBlockFileTransfer
        Args:
            value: Value to set for the applicationGuardBlockFileTransfer property.
        """
        self._application_guard_block_file_transfer = value
    
    @property
    def application_guard_block_non_enterprise_content(self,) -> Optional[bool]:
        """
        Gets the applicationGuardBlockNonEnterpriseContent property value. Block enterprise sites to load non-enterprise content, such as third party plug-ins
        Returns: Optional[bool]
        """
        return self._application_guard_block_non_enterprise_content
    
    @application_guard_block_non_enterprise_content.setter
    def application_guard_block_non_enterprise_content(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardBlockNonEnterpriseContent property value. Block enterprise sites to load non-enterprise content, such as third party plug-ins
        Args:
            value: Value to set for the applicationGuardBlockNonEnterpriseContent property.
        """
        self._application_guard_block_non_enterprise_content = value
    
    @property
    def application_guard_certificate_thumbprints(self,) -> Optional[List[str]]:
        """
        Gets the applicationGuardCertificateThumbprints property value. Allows certain device level Root Certificates to be shared with the Microsoft Defender Application Guard container.
        Returns: Optional[List[str]]
        """
        return self._application_guard_certificate_thumbprints
    
    @application_guard_certificate_thumbprints.setter
    def application_guard_certificate_thumbprints(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the applicationGuardCertificateThumbprints property value. Allows certain device level Root Certificates to be shared with the Microsoft Defender Application Guard container.
        Args:
            value: Value to set for the applicationGuardCertificateThumbprints property.
        """
        self._application_guard_certificate_thumbprints = value
    
    @property
    def application_guard_enabled(self,) -> Optional[bool]:
        """
        Gets the applicationGuardEnabled property value. Enable Windows Defender Application Guard
        Returns: Optional[bool]
        """
        return self._application_guard_enabled
    
    @application_guard_enabled.setter
    def application_guard_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardEnabled property value. Enable Windows Defender Application Guard
        Args:
            value: Value to set for the applicationGuardEnabled property.
        """
        self._application_guard_enabled = value
    
    @property
    def application_guard_enabled_options(self,) -> Optional[application_guard_enabled_options.ApplicationGuardEnabledOptions]:
        """
        Gets the applicationGuardEnabledOptions property value. Possible values for ApplicationGuardEnabledOptions
        Returns: Optional[application_guard_enabled_options.ApplicationGuardEnabledOptions]
        """
        return self._application_guard_enabled_options
    
    @application_guard_enabled_options.setter
    def application_guard_enabled_options(self,value: Optional[application_guard_enabled_options.ApplicationGuardEnabledOptions] = None) -> None:
        """
        Sets the applicationGuardEnabledOptions property value. Possible values for ApplicationGuardEnabledOptions
        Args:
            value: Value to set for the applicationGuardEnabledOptions property.
        """
        self._application_guard_enabled_options = value
    
    @property
    def application_guard_force_auditing(self,) -> Optional[bool]:
        """
        Gets the applicationGuardForceAuditing property value. Force auditing will persist Windows logs and events to meet security/compliance criteria (sample events are user login-logoff, use of privilege rights, software installation, system changes, etc.)
        Returns: Optional[bool]
        """
        return self._application_guard_force_auditing
    
    @application_guard_force_auditing.setter
    def application_guard_force_auditing(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardForceAuditing property value. Force auditing will persist Windows logs and events to meet security/compliance criteria (sample events are user login-logoff, use of privilege rights, software installation, system changes, etc.)
        Args:
            value: Value to set for the applicationGuardForceAuditing property.
        """
        self._application_guard_force_auditing = value
    
    @property
    def app_locker_application_control(self,) -> Optional[app_locker_application_control_type.AppLockerApplicationControlType]:
        """
        Gets the appLockerApplicationControl property value. Possible values of AppLocker Application Control Types
        Returns: Optional[app_locker_application_control_type.AppLockerApplicationControlType]
        """
        return self._app_locker_application_control
    
    @app_locker_application_control.setter
    def app_locker_application_control(self,value: Optional[app_locker_application_control_type.AppLockerApplicationControlType] = None) -> None:
        """
        Sets the appLockerApplicationControl property value. Possible values of AppLocker Application Control Types
        Args:
            value: Value to set for the appLockerApplicationControl property.
        """
        self._app_locker_application_control = value
    
    @property
    def bit_locker_allow_standard_user_encryption(self,) -> Optional[bool]:
        """
        Gets the bitLockerAllowStandardUserEncryption property value. Allows the admin to allow standard users to enable encrpytion during Azure AD Join.
        Returns: Optional[bool]
        """
        return self._bit_locker_allow_standard_user_encryption
    
    @bit_locker_allow_standard_user_encryption.setter
    def bit_locker_allow_standard_user_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the bitLockerAllowStandardUserEncryption property value. Allows the admin to allow standard users to enable encrpytion during Azure AD Join.
        Args:
            value: Value to set for the bitLockerAllowStandardUserEncryption property.
        """
        self._bit_locker_allow_standard_user_encryption = value
    
    @property
    def bit_locker_disable_warning_for_other_disk_encryption(self,) -> Optional[bool]:
        """
        Gets the bitLockerDisableWarningForOtherDiskEncryption property value. Allows the Admin to disable the warning prompt for other disk encryption on the user machines.
        Returns: Optional[bool]
        """
        return self._bit_locker_disable_warning_for_other_disk_encryption
    
    @bit_locker_disable_warning_for_other_disk_encryption.setter
    def bit_locker_disable_warning_for_other_disk_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the bitLockerDisableWarningForOtherDiskEncryption property value. Allows the Admin to disable the warning prompt for other disk encryption on the user machines.
        Args:
            value: Value to set for the bitLockerDisableWarningForOtherDiskEncryption property.
        """
        self._bit_locker_disable_warning_for_other_disk_encryption = value
    
    @property
    def bit_locker_enable_storage_card_encryption_on_mobile(self,) -> Optional[bool]:
        """
        Gets the bitLockerEnableStorageCardEncryptionOnMobile property value. Allows the admin to require encryption to be turned on using BitLocker. This policy is valid only for a mobile SKU.
        Returns: Optional[bool]
        """
        return self._bit_locker_enable_storage_card_encryption_on_mobile
    
    @bit_locker_enable_storage_card_encryption_on_mobile.setter
    def bit_locker_enable_storage_card_encryption_on_mobile(self,value: Optional[bool] = None) -> None:
        """
        Sets the bitLockerEnableStorageCardEncryptionOnMobile property value. Allows the admin to require encryption to be turned on using BitLocker. This policy is valid only for a mobile SKU.
        Args:
            value: Value to set for the bitLockerEnableStorageCardEncryptionOnMobile property.
        """
        self._bit_locker_enable_storage_card_encryption_on_mobile = value
    
    @property
    def bit_locker_encrypt_device(self,) -> Optional[bool]:
        """
        Gets the bitLockerEncryptDevice property value. Allows the admin to require encryption to be turned on using BitLocker.
        Returns: Optional[bool]
        """
        return self._bit_locker_encrypt_device
    
    @bit_locker_encrypt_device.setter
    def bit_locker_encrypt_device(self,value: Optional[bool] = None) -> None:
        """
        Sets the bitLockerEncryptDevice property value. Allows the admin to require encryption to be turned on using BitLocker.
        Args:
            value: Value to set for the bitLockerEncryptDevice property.
        """
        self._bit_locker_encrypt_device = value
    
    @property
    def bit_locker_fixed_drive_policy(self,) -> Optional[bit_locker_fixed_drive_policy.BitLockerFixedDrivePolicy]:
        """
        Gets the bitLockerFixedDrivePolicy property value. BitLocker Fixed Drive Policy.
        Returns: Optional[bit_locker_fixed_drive_policy.BitLockerFixedDrivePolicy]
        """
        return self._bit_locker_fixed_drive_policy
    
    @bit_locker_fixed_drive_policy.setter
    def bit_locker_fixed_drive_policy(self,value: Optional[bit_locker_fixed_drive_policy.BitLockerFixedDrivePolicy] = None) -> None:
        """
        Sets the bitLockerFixedDrivePolicy property value. BitLocker Fixed Drive Policy.
        Args:
            value: Value to set for the bitLockerFixedDrivePolicy property.
        """
        self._bit_locker_fixed_drive_policy = value
    
    @property
    def bit_locker_recovery_password_rotation(self,) -> Optional[bit_locker_recovery_password_rotation_type.BitLockerRecoveryPasswordRotationType]:
        """
        Gets the bitLockerRecoveryPasswordRotation property value. BitLocker recovery password rotation type
        Returns: Optional[bit_locker_recovery_password_rotation_type.BitLockerRecoveryPasswordRotationType]
        """
        return self._bit_locker_recovery_password_rotation
    
    @bit_locker_recovery_password_rotation.setter
    def bit_locker_recovery_password_rotation(self,value: Optional[bit_locker_recovery_password_rotation_type.BitLockerRecoveryPasswordRotationType] = None) -> None:
        """
        Sets the bitLockerRecoveryPasswordRotation property value. BitLocker recovery password rotation type
        Args:
            value: Value to set for the bitLockerRecoveryPasswordRotation property.
        """
        self._bit_locker_recovery_password_rotation = value
    
    @property
    def bit_locker_removable_drive_policy(self,) -> Optional[bit_locker_removable_drive_policy.BitLockerRemovableDrivePolicy]:
        """
        Gets the bitLockerRemovableDrivePolicy property value. BitLocker Removable Drive Policy.
        Returns: Optional[bit_locker_removable_drive_policy.BitLockerRemovableDrivePolicy]
        """
        return self._bit_locker_removable_drive_policy
    
    @bit_locker_removable_drive_policy.setter
    def bit_locker_removable_drive_policy(self,value: Optional[bit_locker_removable_drive_policy.BitLockerRemovableDrivePolicy] = None) -> None:
        """
        Sets the bitLockerRemovableDrivePolicy property value. BitLocker Removable Drive Policy.
        Args:
            value: Value to set for the bitLockerRemovableDrivePolicy property.
        """
        self._bit_locker_removable_drive_policy = value
    
    @property
    def bit_locker_system_drive_policy(self,) -> Optional[bit_locker_system_drive_policy.BitLockerSystemDrivePolicy]:
        """
        Gets the bitLockerSystemDrivePolicy property value. BitLocker System Drive Policy.
        Returns: Optional[bit_locker_system_drive_policy.BitLockerSystemDrivePolicy]
        """
        return self._bit_locker_system_drive_policy
    
    @bit_locker_system_drive_policy.setter
    def bit_locker_system_drive_policy(self,value: Optional[bit_locker_system_drive_policy.BitLockerSystemDrivePolicy] = None) -> None:
        """
        Sets the bitLockerSystemDrivePolicy property value. BitLocker System Drive Policy.
        Args:
            value: Value to set for the bitLockerSystemDrivePolicy property.
        """
        self._bit_locker_system_drive_policy = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10EndpointProtectionConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10EndpointProtectionConfiguration"
        # Gets or sets whether applications inside Microsoft Defender Application Guard can access the device’s camera and microphone.
        self._application_guard_allow_camera_microphone_redirection: Optional[bool] = None
        # Allow users to download files from Edge in the application guard container and save them on the host file system
        self._application_guard_allow_file_save_on_host: Optional[bool] = None
        # Allow persisting user generated data inside the App Guard Containter (favorites, cookies, web passwords, etc.)
        self._application_guard_allow_persistence: Optional[bool] = None
        # Allow printing to Local Printers from Container
        self._application_guard_allow_print_to_local_printers: Optional[bool] = None
        # Allow printing to Network Printers from Container
        self._application_guard_allow_print_to_network_printers: Optional[bool] = None
        # Allow printing to PDF from Container
        self._application_guard_allow_print_to_p_d_f: Optional[bool] = None
        # Allow printing to XPS from Container
        self._application_guard_allow_print_to_x_p_s: Optional[bool] = None
        # Allow application guard to use virtual GPU
        self._application_guard_allow_virtual_g_p_u: Optional[bool] = None
        # Possible values for applicationGuardBlockClipboardSharingType
        self._application_guard_block_clipboard_sharing: Optional[application_guard_block_clipboard_sharing_type.ApplicationGuardBlockClipboardSharingType] = None
        # Possible values for applicationGuardBlockFileTransfer
        self._application_guard_block_file_transfer: Optional[application_guard_block_file_transfer_type.ApplicationGuardBlockFileTransferType] = None
        # Block enterprise sites to load non-enterprise content, such as third party plug-ins
        self._application_guard_block_non_enterprise_content: Optional[bool] = None
        # Allows certain device level Root Certificates to be shared with the Microsoft Defender Application Guard container.
        self._application_guard_certificate_thumbprints: Optional[List[str]] = None
        # Enable Windows Defender Application Guard
        self._application_guard_enabled: Optional[bool] = None
        # Possible values for ApplicationGuardEnabledOptions
        self._application_guard_enabled_options: Optional[application_guard_enabled_options.ApplicationGuardEnabledOptions] = None
        # Force auditing will persist Windows logs and events to meet security/compliance criteria (sample events are user login-logoff, use of privilege rights, software installation, system changes, etc.)
        self._application_guard_force_auditing: Optional[bool] = None
        # Possible values of AppLocker Application Control Types
        self._app_locker_application_control: Optional[app_locker_application_control_type.AppLockerApplicationControlType] = None
        # Allows the admin to allow standard users to enable encrpytion during Azure AD Join.
        self._bit_locker_allow_standard_user_encryption: Optional[bool] = None
        # Allows the Admin to disable the warning prompt for other disk encryption on the user machines.
        self._bit_locker_disable_warning_for_other_disk_encryption: Optional[bool] = None
        # Allows the admin to require encryption to be turned on using BitLocker. This policy is valid only for a mobile SKU.
        self._bit_locker_enable_storage_card_encryption_on_mobile: Optional[bool] = None
        # Allows the admin to require encryption to be turned on using BitLocker.
        self._bit_locker_encrypt_device: Optional[bool] = None
        # BitLocker Fixed Drive Policy.
        self._bit_locker_fixed_drive_policy: Optional[bit_locker_fixed_drive_policy.BitLockerFixedDrivePolicy] = None
        # BitLocker recovery password rotation type
        self._bit_locker_recovery_password_rotation: Optional[bit_locker_recovery_password_rotation_type.BitLockerRecoveryPasswordRotationType] = None
        # BitLocker Removable Drive Policy.
        self._bit_locker_removable_drive_policy: Optional[bit_locker_removable_drive_policy.BitLockerRemovableDrivePolicy] = None
        # BitLocker System Drive Policy.
        self._bit_locker_system_drive_policy: Optional[bit_locker_system_drive_policy.BitLockerSystemDrivePolicy] = None
        # List of folder paths to be added to the list of protected folders
        self._defender_additional_guarded_folders: Optional[List[str]] = None
        # Possible values of Defender PUA Protection
        self._defender_adobe_reader_launch_child_process: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender PUA Protection
        self._defender_advanced_ransomeware_protection_type: Optional[defender_protection_type.DefenderProtectionType] = None
        # Allows or disallows Windows Defender Behavior Monitoring functionality.
        self._defender_allow_behavior_monitoring: Optional[bool] = None
        # To best protect your PC, Windows Defender will send information to Microsoft about any problems it finds. Microsoft will analyze that information, learn more about problems affecting you and other customers, and offer improved solutions.
        self._defender_allow_cloud_protection: Optional[bool] = None
        # Allows or disallows user access to the Windows Defender UI. If disallowed, all Windows Defender notifications will also be suppressed.
        self._defender_allow_end_user_access: Optional[bool] = None
        # Allows or disallows Windows Defender Intrusion Prevention functionality.
        self._defender_allow_intrusion_prevention_system: Optional[bool] = None
        # Allows or disallows Windows Defender On Access Protection functionality.
        self._defender_allow_on_access_protection: Optional[bool] = None
        # Allows or disallows Windows Defender Realtime Monitoring functionality.
        self._defender_allow_real_time_monitoring: Optional[bool] = None
        # Allows or disallows scanning of archives.
        self._defender_allow_scan_archive_files: Optional[bool] = None
        # Allows or disallows Windows Defender IOAVP Protection functionality.
        self._defender_allow_scan_downloads: Optional[bool] = None
        # Allows or disallows a scanning of network files.
        self._defender_allow_scan_network_files: Optional[bool] = None
        # Allows or disallows a full scan of removable drives. During a quick scan, removable drives may still be scanned.
        self._defender_allow_scan_removable_drives_during_full_scan: Optional[bool] = None
        # Allows or disallows Windows Defender Script Scanning functionality.
        self._defender_allow_scan_scripts_loaded_in_internet_explorer: Optional[bool] = None
        # List of exe files and folders to be excluded from attack surface reduction rules
        self._defender_attack_surface_reduction_excluded_paths: Optional[List[str]] = None
        # Allows or disallows user access to the Windows Defender UI. If disallowed, all Windows Defender notifications will also be suppressed.
        self._defender_block_end_user_access: Optional[bool] = None
        # Possible values of Defender Attack Surface Reduction Rules
        self._defender_block_persistence_through_wmi_type: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None
        # This policy setting allows you to manage whether a check for new virus and spyware definitions will occur before running a scan.
        self._defender_check_for_signatures_before_running_scan: Optional[bool] = None
        # Added in Windows 10, version 1709. This policy setting determines how aggressive Windows Defender Antivirus will be in blocking and scanning suspicious files. Value type is integer. This feature requires the 'Join Microsoft MAPS' setting enabled in order to function. Possible values are: notConfigured, high, highPlus, zeroTolerance.
        self._defender_cloud_block_level: Optional[defender_cloud_block_level_type.DefenderCloudBlockLevelType] = None
        # Added in Windows 10, version 1709. This feature allows Windows Defender Antivirus to block a suspicious file for up to 60 seconds, and scan it in the cloud to make sure it's safe. Value type is integer, range is 0 - 50. This feature depends on three other MAPS settings the must all be enabled- 'Configure the 'Block at First Sight' feature; 'Join Microsoft MAPS'; 'Send file samples when further analysis is required'. Valid values 0 to 50
        self._defender_cloud_extended_timeout_in_seconds: Optional[int] = None
        # Time period (in days) that quarantine items will be stored on the system. Valid values 0 to 90
        self._defender_days_before_deleting_quarantined_malware: Optional[int] = None
        # Allows an administrator to specify any valid threat severity levels and the corresponding default action ID to take.
        self._defender_detected_malware_actions: Optional[defender_detected_malware_actions.DefenderDetectedMalwareActions] = None
        # Allows or disallows Windows Defender Behavior Monitoring functionality.
        self._defender_disable_behavior_monitoring: Optional[bool] = None
        # This policy setting allows you to configure catch-up scans for scheduled full scans. A catch-up scan is a scan that is initiated because a regularly scheduled scan was missed. Usually these scheduled scans are missed because the computer was turned off at the scheduled time.
        self._defender_disable_catchup_full_scan: Optional[bool] = None
        # This policy setting allows you to configure catch-up scans for scheduled quick scans. A catch-up scan is a scan that is initiated because a regularly scheduled scan was missed. Usually these scheduled scans are missed because the computer was turned off at the scheduled time.
        self._defender_disable_catchup_quick_scan: Optional[bool] = None
        # To best protect your PC, Windows Defender will send information to Microsoft about any problems it finds. Microsoft will analyze that information, learn more about problems affecting you and other customers, and offer improved solutions.
        self._defender_disable_cloud_protection: Optional[bool] = None
        # Allows or disallows Windows Defender Intrusion Prevention functionality.
        self._defender_disable_intrusion_prevention_system: Optional[bool] = None
        # Allows or disallows Windows Defender On Access Protection functionality.
        self._defender_disable_on_access_protection: Optional[bool] = None
        # Allows or disallows Windows Defender Realtime Monitoring functionality.
        self._defender_disable_real_time_monitoring: Optional[bool] = None
        # Allows or disallows scanning of archives.
        self._defender_disable_scan_archive_files: Optional[bool] = None
        # Allows or disallows Windows Defender IOAVP Protection functionality.
        self._defender_disable_scan_downloads: Optional[bool] = None
        # Allows or disallows a scanning of network files.
        self._defender_disable_scan_network_files: Optional[bool] = None
        # Allows or disallows a full scan of removable drives. During a quick scan, removable drives may still be scanned.
        self._defender_disable_scan_removable_drives_during_full_scan: Optional[bool] = None
        # Allows or disallows Windows Defender Script Scanning functionality.
        self._defender_disable_scan_scripts_loaded_in_internet_explorer: Optional[bool] = None
        # Possible values of Defender PUA Protection
        self._defender_email_content_execution: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender Attack Surface Reduction Rules
        self._defender_email_content_execution_type: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None
        # This policy setting allows you to enable or disable low CPU priority for scheduled scans.
        self._defender_enable_low_cpu_priority: Optional[bool] = None
        # Allows or disallows scanning of email.
        self._defender_enable_scan_incoming_mail: Optional[bool] = None
        # Allows or disallows a full scan of mapped network drives.
        self._defender_enable_scan_mapped_network_drives_during_full_scan: Optional[bool] = None
        # Xml content containing information regarding exploit protection details.
        self._defender_exploit_protection_xml: Optional[bytes] = None
        # Name of the file from which DefenderExploitProtectionXml was obtained.
        self._defender_exploit_protection_xml_file_name: Optional[str] = None
        # File extensions to exclude from scans and real time protection.
        self._defender_file_extensions_to_exclude: Optional[List[str]] = None
        # Files and folder to exclude from scans and real time protection.
        self._defender_files_and_folders_to_exclude: Optional[List[str]] = None
        # List of paths to exe that are allowed to access protected folders
        self._defender_guarded_folders_allowed_app_paths: Optional[List[str]] = None
        # Possible values of Folder Protection
        self._defender_guard_my_folders_type: Optional[folder_protection_type.FolderProtectionType] = None
        # Possible values of Defender PUA Protection
        self._defender_network_protection_type: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender PUA Protection
        self._defender_office_apps_executable_content_creation_or_launch: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender Attack Surface Reduction Rules
        self._defender_office_apps_executable_content_creation_or_launch_type: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None
        # Possible values of Defender PUA Protection
        self._defender_office_apps_launch_child_process: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender Attack Surface Reduction Rules
        self._defender_office_apps_launch_child_process_type: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None
        # Possible values of Defender PUA Protection
        self._defender_office_apps_other_process_injection: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender Attack Surface Reduction Rules
        self._defender_office_apps_other_process_injection_type: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None
        # Possible values of Defender PUA Protection
        self._defender_office_communication_apps_launch_child_process: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender PUA Protection
        self._defender_office_macro_code_allow_win32_imports: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender Attack Surface Reduction Rules
        self._defender_office_macro_code_allow_win32_imports_type: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None
        # Added in Windows 10, version 1607. Specifies the level of detection for potentially unwanted applications (PUAs). Windows Defender alerts you when potentially unwanted software is being downloaded or attempts to install itself on your computer. Possible values are: userDefined, enable, auditMode, warn, notConfigured.
        self._defender_potentially_unwanted_app_action: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender PUA Protection
        self._defender_prevent_credential_stealing_type: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender PUA Protection
        self._defender_process_creation: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender Attack Surface Reduction Rules
        self._defender_process_creation_type: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None
        # Processes to exclude from scans and real time protection.
        self._defender_processes_to_exclude: Optional[List[str]] = None
        # Controls which sets of files should be monitored. Possible values are: monitorAllFiles, monitorIncomingFilesOnly, monitorOutgoingFilesOnly.
        self._defender_scan_direction: Optional[defender_realtime_scan_direction.DefenderRealtimeScanDirection] = None
        # Represents the average CPU load factor for the Windows Defender scan (in percent). The default value is 50. Valid values 0 to 100
        self._defender_scan_max_cpu_percentage: Optional[int] = None
        # Selects whether to perform a quick scan or full scan. Possible values are: userDefined, disabled, quick, full.
        self._defender_scan_type: Optional[defender_scan_type.DefenderScanType] = None
        # Selects the time of day that the Windows Defender quick scan should run. For example, a value of 0=12:00AM, a value of 60=1:00AM, a value of 120=2:00, and so on, up to a value of 1380=11:00PM. The default value is 120
        self._defender_scheduled_quick_scan_time: Optional[Time] = None
        # Selects the day that the Windows Defender scan should run. Possible values are: userDefined, everyday, sunday, monday, tuesday, wednesday, thursday, friday, saturday, noScheduledScan.
        self._defender_scheduled_scan_day: Optional[weekly_schedule.WeeklySchedule] = None
        # Selects the time of day that the Windows Defender scan should run.
        self._defender_scheduled_scan_time: Optional[Time] = None
        # Possible values of Defender PUA Protection
        self._defender_script_downloaded_payload_execution: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender Attack Surface Reduction Rules
        self._defender_script_downloaded_payload_execution_type: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None
        # Possible values of Defender PUA Protection
        self._defender_script_obfuscated_macro_code: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender Attack Surface Reduction Rules
        self._defender_script_obfuscated_macro_code_type: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None
        # Indicates whether or not to block user from overriding Exploit Protection settings.
        self._defender_security_center_block_exploit_protection_override: Optional[bool] = None
        # Used to disable the display of the account protection area.
        self._defender_security_center_disable_account_u_i: Optional[bool] = None
        # Used to disable the display of the app and browser protection area.
        self._defender_security_center_disable_app_browser_u_i: Optional[bool] = None
        # Used to disable the display of the Clear TPM button.
        self._defender_security_center_disable_clear_tpm_u_i: Optional[bool] = None
        # Used to disable the display of the family options area.
        self._defender_security_center_disable_family_u_i: Optional[bool] = None
        # Used to disable the display of the hardware protection area.
        self._defender_security_center_disable_hardware_u_i: Optional[bool] = None
        # Used to disable the display of the device performance and health area.
        self._defender_security_center_disable_health_u_i: Optional[bool] = None
        # Used to disable the display of the firewall and network protection area.
        self._defender_security_center_disable_network_u_i: Optional[bool] = None
        # Used to disable the display of the notification area control. The user needs to either sign out and sign in or reboot the computer for this setting to take effect.
        self._defender_security_center_disable_notification_area_u_i: Optional[bool] = None
        # Used to disable the display of the ransomware protection area.
        self._defender_security_center_disable_ransomware_u_i: Optional[bool] = None
        # Used to disable the display of the secure boot area under Device security.
        self._defender_security_center_disable_secure_boot_u_i: Optional[bool] = None
        # Used to disable the display of the security process troubleshooting under Device security.
        self._defender_security_center_disable_troubleshooting_u_i: Optional[bool] = None
        # Used to disable the display of the virus and threat protection area.
        self._defender_security_center_disable_virus_u_i: Optional[bool] = None
        # Used to disable the display of update TPM Firmware when a vulnerable firmware is detected.
        self._defender_security_center_disable_vulnerable_tpm_firmware_update_u_i: Optional[bool] = None
        # The email address that is displayed to users.
        self._defender_security_center_help_email: Optional[str] = None
        # The phone number or Skype ID that is displayed to users.
        self._defender_security_center_help_phone: Optional[str] = None
        # The help portal URL this is displayed to users.
        self._defender_security_center_help_u_r_l: Optional[str] = None
        # Possible values for defenderSecurityCenterITContactDisplay
        self._defender_security_center_i_t_contact_display: Optional[defender_security_center_i_t_contact_display_type.DefenderSecurityCenterITContactDisplayType] = None
        # Possible values for defenderSecurityCenterNotificationsFromApp
        self._defender_security_center_notifications_from_app: Optional[defender_security_center_notifications_from_app_type.DefenderSecurityCenterNotificationsFromAppType] = None
        # The company name that is displayed to the users.
        self._defender_security_center_organization_display_name: Optional[str] = None
        # Specifies the interval (in hours) that will be used to check for signatures, so instead of using the ScheduleDay and ScheduleTime the check for new signatures will be set according to the interval. Valid values 0 to 24
        self._defender_signature_update_interval_in_hours: Optional[int] = None
        # Checks for the user consent level in Windows Defender to send data. Possible values are: sendSafeSamplesAutomatically, alwaysPrompt, neverSend, sendAllSamplesAutomatically.
        self._defender_submit_samples_consent_type: Optional[defender_submit_samples_consent_type.DefenderSubmitSamplesConsentType] = None
        # Possible values of Defender PUA Protection
        self._defender_untrusted_executable: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender Attack Surface Reduction Rules
        self._defender_untrusted_executable_type: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None
        # Possible values of Defender PUA Protection
        self._defender_untrusted_u_s_b_process: Optional[defender_protection_type.DefenderProtectionType] = None
        # Possible values of Defender Attack Surface Reduction Rules
        self._defender_untrusted_u_s_b_process_type: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None
        # This property will be deprecated in May 2019 and will be replaced with property DeviceGuardSecureBootWithDMA. Specifies whether Platform Security Level is enabled at next reboot.
        self._device_guard_enable_secure_boot_with_d_m_a: Optional[bool] = None
        # Turns On Virtualization Based Security(VBS).
        self._device_guard_enable_virtualization_based_security: Optional[bool] = None
        # Possible values of a property
        self._device_guard_launch_system_guard: Optional[enablement.Enablement] = None
        # Possible values of Credential Guard settings.
        self._device_guard_local_system_authority_credential_guard_settings: Optional[device_guard_local_system_authority_credential_guard_type.DeviceGuardLocalSystemAuthorityCredentialGuardType] = None
        # Possible values of Secure Boot with DMA
        self._device_guard_secure_boot_with_d_m_a: Optional[secure_boot_with_d_m_a_type.SecureBootWithDMAType] = None
        # Possible values of the DmaGuardDeviceEnumerationPolicy.
        self._dma_guard_device_enumeration_policy: Optional[dma_guard_device_enumeration_policy_type.DmaGuardDeviceEnumerationPolicyType] = None
        # Blocks stateful FTP connections to the device
        self._firewall_block_stateful_f_t_p: Optional[bool] = None
        # Possible values for firewallCertificateRevocationListCheckMethod
        self._firewall_certificate_revocation_list_check_method: Optional[firewall_certificate_revocation_list_check_method_type.FirewallCertificateRevocationListCheckMethodType] = None
        # Configures the idle timeout for security associations, in seconds, from 300 to 3600 inclusive. This is the period after which security associations will expire and be deleted. Valid values 300 to 3600
        self._firewall_idle_timeout_for_security_association_in_seconds: Optional[int] = None
        # Configures IPSec exemptions to allow both IPv4 and IPv6 DHCP traffic
        self._firewall_i_p_sec_exemptions_allow_d_h_c_p: Optional[bool] = None
        # Configures IPSec exemptions to allow ICMP
        self._firewall_i_p_sec_exemptions_allow_i_c_m_p: Optional[bool] = None
        # Configures IPSec exemptions to allow neighbor discovery IPv6 ICMP type-codes
        self._firewall_i_p_sec_exemptions_allow_neighbor_discovery: Optional[bool] = None
        # Configures IPSec exemptions to allow router discovery IPv6 ICMP type-codes
        self._firewall_i_p_sec_exemptions_allow_router_discovery: Optional[bool] = None
        # Configures IPSec exemptions to no exemptions
        self._firewall_i_p_sec_exemptions_none: Optional[bool] = None
        # If an authentication set is not fully supported by a keying module, direct the module to ignore only unsupported authentication suites rather than the entire set
        self._firewall_merge_keying_module_settings: Optional[bool] = None
        # Possible values for firewallPacketQueueingMethod
        self._firewall_packet_queueing_method: Optional[firewall_packet_queueing_method_type.FirewallPacketQueueingMethodType] = None
        # Possible values for firewallPreSharedKeyEncodingMethod
        self._firewall_pre_shared_key_encoding_method: Optional[firewall_pre_shared_key_encoding_method_type.FirewallPreSharedKeyEncodingMethodType] = None
        # Configures the firewall profile settings for domain networks
        self._firewall_profile_domain: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile] = None
        # Configures the firewall profile settings for private networks
        self._firewall_profile_private: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile] = None
        # Configures the firewall profile settings for public networks
        self._firewall_profile_public: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile] = None
        # Configures the firewall rule settings. This collection can contain a maximum of 150 elements.
        self._firewall_rules: Optional[List[windows_firewall_rule.WindowsFirewallRule]] = None
        # Possible values for LanManagerAuthenticationLevel
        self._lan_manager_authentication_level: Optional[lan_manager_authentication_level.LanManagerAuthenticationLevel] = None
        # If enabled,the SMB client will allow insecure guest logons. If not configured, the SMB client will reject insecure guest logons.
        self._lan_manager_workstation_disable_insecure_guest_logons: Optional[bool] = None
        # Define a different account name to be associated with the security identifier (SID) for the account 'Administrator'.
        self._local_security_options_administrator_account_name: Optional[str] = None
        # Possible values for LocalSecurityOptionsAdministratorElevationPromptBehavior
        self._local_security_options_administrator_elevation_prompt_behavior: Optional[local_security_options_administrator_elevation_prompt_behavior_type.LocalSecurityOptionsAdministratorElevationPromptBehaviorType] = None
        # This security setting determines whether to allows anonymous users to perform certain activities, such as enumerating the names of domain accounts and network shares.
        self._local_security_options_allow_anonymous_enumeration_of_s_a_m_accounts_and_shares: Optional[bool] = None
        # Block PKU2U authentication requests to this device to use online identities.
        self._local_security_options_allow_p_k_u2_u_authentication_requests: Optional[bool] = None
        # Edit the default Security Descriptor Definition Language string to allow or deny users and groups to make remote calls to the SAM.
        self._local_security_options_allow_remote_calls_to_security_accounts_manager: Optional[str] = None
        # UI helper boolean for LocalSecurityOptionsAllowRemoteCallsToSecurityAccountsManager entity
        self._local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool: Optional[bool] = None
        # This security setting determines whether a computer can be shut down without having to log on to Windows.
        self._local_security_options_allow_system_to_be_shut_down_without_having_to_log_on: Optional[bool] = None
        # Allow UIAccess apps to prompt for elevation without using the secure desktop.
        self._local_security_options_allow_u_i_access_application_elevation: Optional[bool] = None
        # Allow UIAccess apps to prompt for elevation without using the secure desktop.Default is enabled
        self._local_security_options_allow_u_i_access_applications_for_secure_locations: Optional[bool] = None
        # Prevent a portable computer from being undocked without having to log in.
        self._local_security_options_allow_undock_without_having_to_logon: Optional[bool] = None
        # Prevent users from adding new Microsoft accounts to this computer.
        self._local_security_options_block_microsoft_accounts: Optional[bool] = None
        # Enable Local accounts that are not password protected to log on from locations other than the physical device.Default is enabled
        self._local_security_options_block_remote_logon_with_blank_password: Optional[bool] = None
        # Enabling this settings allows only interactively logged on user to access CD-ROM media.
        self._local_security_options_block_remote_optical_drive_access: Optional[bool] = None
        # Restrict installing printer drivers as part of connecting to a shared printer to admins only.
        self._local_security_options_block_users_installing_printer_drivers: Optional[bool] = None
        # This security setting determines whether the virtual memory pagefile is cleared when the system is shut down.
        self._local_security_options_clear_virtual_memory_page_file: Optional[bool] = None
        # This security setting determines whether packet signing is required by the SMB client component.
        self._local_security_options_client_digitally_sign_communications_always: Optional[bool] = None
        # If this security setting is enabled, the Server Message Block (SMB) redirector is allowed to send plaintext passwords to non-Microsoft SMB servers that do not support password encryption during authentication.
        self._local_security_options_client_send_unencrypted_password_to_third_party_s_m_b_servers: Optional[bool] = None
        # App installations requiring elevated privileges will prompt for admin credentials.Default is enabled
        self._local_security_options_detect_application_installations_and_prompt_for_elevation: Optional[bool] = None
        # Determines whether the Local Administrator account is enabled or disabled.
        self._local_security_options_disable_administrator_account: Optional[bool] = None
        # This security setting determines whether the SMB client attempts to negotiate SMB packet signing.
        self._local_security_options_disable_client_digitally_sign_communications_if_server_agrees: Optional[bool] = None
        # Determines if the Guest account is enabled or disabled.
        self._local_security_options_disable_guest_account: Optional[bool] = None
        # This security setting determines whether packet signing is required by the SMB server component.
        self._local_security_options_disable_server_digitally_sign_communications_always: Optional[bool] = None
        # This security setting determines whether the SMB server will negotiate SMB packet signing with clients that request it.
        self._local_security_options_disable_server_digitally_sign_communications_if_client_agrees: Optional[bool] = None
        # This security setting determines what additional permissions will be granted for anonymous connections to the computer.
        self._local_security_options_do_not_allow_anonymous_enumeration_of_s_a_m_accounts: Optional[bool] = None
        # Require CTRL+ALT+DEL to be pressed before a user can log on.
        self._local_security_options_do_not_require_ctrl_alt_del: Optional[bool] = None
        # This security setting determines if, at the next password change, the LAN Manager (LM) hash value for the new password is stored. It’s not stored by default.
        self._local_security_options_do_not_store_l_a_n_manager_hash_value_on_next_password_change: Optional[bool] = None
        # Possible values for LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser
        self._local_security_options_format_and_eject_of_removable_media_allowed_user: Optional[local_security_options_format_and_eject_of_removable_media_allowed_user_type.LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType] = None
        # Define a different account name to be associated with the security identifier (SID) for the account 'Guest'.
        self._local_security_options_guest_account_name: Optional[str] = None
        # Do not display the username of the last person who signed in on this device.
        self._local_security_options_hide_last_signed_in_user: Optional[bool] = None
        # Do not display the username of the person signing in to this device after credentials are entered and before the device’s desktop is shown.
        self._local_security_options_hide_username_at_sign_in: Optional[bool] = None
        # Possible values for LocalSecurityOptionsInformationDisplayedOnLockScreen
        self._local_security_options_information_displayed_on_lock_screen: Optional[local_security_options_information_displayed_on_lock_screen_type.LocalSecurityOptionsInformationDisplayedOnLockScreenType] = None
        # Possible values for LocalSecurityOptionsInformationShownOnLockScreenType
        self._local_security_options_information_shown_on_lock_screen: Optional[local_security_options_information_shown_on_lock_screen_type.LocalSecurityOptionsInformationShownOnLockScreenType] = None
        # Set message text for users attempting to log in.
        self._local_security_options_log_on_message_text: Optional[str] = None
        # Set message title for users attempting to log in.
        self._local_security_options_log_on_message_title: Optional[str] = None
        # Define maximum minutes of inactivity on the interactive desktop’s login screen until the screen saver runs. Valid values 0 to 9999
        self._local_security_options_machine_inactivity_limit: Optional[int] = None
        # Define maximum minutes of inactivity on the interactive desktop’s login screen until the screen saver runs. Valid values 0 to 9999
        self._local_security_options_machine_inactivity_limit_in_minutes: Optional[int] = None
        # Possible values for LocalSecurityOptionsMinimumSessionSecurity
        self._local_security_options_minimum_session_security_for_ntlm_ssp_based_clients: Optional[local_security_options_minimum_session_security.LocalSecurityOptionsMinimumSessionSecurity] = None
        # Possible values for LocalSecurityOptionsMinimumSessionSecurity
        self._local_security_options_minimum_session_security_for_ntlm_ssp_based_servers: Optional[local_security_options_minimum_session_security.LocalSecurityOptionsMinimumSessionSecurity] = None
        # Enforce PKI certification path validation for a given executable file before it is permitted to run.
        self._local_security_options_only_elevate_signed_executables: Optional[bool] = None
        # By default, this security setting restricts anonymous access to shares and pipes to the settings for named pipes that can be accessed anonymously and Shares that can be accessed anonymously
        self._local_security_options_restrict_anonymous_access_to_named_pipes_and_shares: Optional[bool] = None
        # Possible values for LocalSecurityOptionsSmartCardRemovalBehaviorType
        self._local_security_options_smart_card_removal_behavior: Optional[local_security_options_smart_card_removal_behavior_type.LocalSecurityOptionsSmartCardRemovalBehaviorType] = None
        # Possible values for LocalSecurityOptionsStandardUserElevationPromptBehavior
        self._local_security_options_standard_user_elevation_prompt_behavior: Optional[local_security_options_standard_user_elevation_prompt_behavior_type.LocalSecurityOptionsStandardUserElevationPromptBehaviorType] = None
        # Enable all elevation requests to go to the interactive user's desktop rather than the secure desktop. Prompt behavior policy settings for admins and standard users are used.
        self._local_security_options_switch_to_secure_desktop_when_prompting_for_elevation: Optional[bool] = None
        # Defines whether the built-in admin account uses Admin Approval Mode or runs all apps with full admin privileges.Default is enabled
        self._local_security_options_use_admin_approval_mode: Optional[bool] = None
        # Define whether Admin Approval Mode and all UAC policy settings are enabled, default is enabled
        self._local_security_options_use_admin_approval_mode_for_administrators: Optional[bool] = None
        # Virtualize file and registry write failures to per user locations
        self._local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations: Optional[bool] = None
        # Allows IT Admins to control whether users can can ignore SmartScreen warnings and run malicious files.
        self._smart_screen_block_override_for_files: Optional[bool] = None
        # Allows IT Admins to configure SmartScreen for Windows.
        self._smart_screen_enable_in_shell: Optional[bool] = None
        # This user right is used by Credential Manager during Backup/Restore. Users' saved credentials might be compromised if this privilege is given to other entities. Only states NotConfigured and Allowed are supported
        self._user_rights_access_credential_manager_as_trusted_caller: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right allows a process to impersonate any user without authentication. The process can therefore gain access to the same local resources as that user. Only states NotConfigured and Allowed are supported
        self._user_rights_act_as_part_of_the_operating_system: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users and groups are allowed to connect to the computer over the network. State Allowed is supported.
        self._user_rights_allow_access_from_network: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users can bypass file, directory, registry, and other persistent objects permissions when backing up files and directories. Only states NotConfigured and Allowed are supported
        self._user_rights_backup_data: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users and groups are block from connecting to the computer over the network. State Block is supported.
        self._user_rights_block_access_from_network: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users and groups can change the time and date on the internal clock of the computer. Only states NotConfigured and Allowed are supported
        self._user_rights_change_system_time: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This security setting determines whether users can create global objects that are available to all sessions. Users who can create global objects could affect processes that run under other users' sessions, which could lead to application failure or data corruption. Only states NotConfigured and Allowed are supported
        self._user_rights_create_global_objects: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users and groups can call an internal API to create and change the size of a page file. Only states NotConfigured and Allowed are supported
        self._user_rights_create_page_file: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which accounts can be used by processes to create a directory object using the object manager. Only states NotConfigured and Allowed are supported
        self._user_rights_create_permanent_shared_objects: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines if the user can create a symbolic link from the computer to which they are logged on. Only states NotConfigured and Allowed are supported
        self._user_rights_create_symbolic_links: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users/groups can be used by processes to create a token that can then be used to get access to any local resources when the process uses an internal API to create an access token. Only states NotConfigured and Allowed are supported
        self._user_rights_create_token: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users can attach a debugger to any process or to the kernel. Only states NotConfigured and Allowed are supported
        self._user_rights_debug_programs: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users can set the Trusted for Delegation setting on a user or computer object. Only states NotConfigured and Allowed are supported.
        self._user_rights_delegation: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users cannot log on to the computer. States NotConfigured, Blocked are supported
        self._user_rights_deny_local_log_on: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which accounts can be used by a process to add entries to the security log. The security log is used to trace unauthorized system access.  Only states NotConfigured and Allowed are supported.
        self._user_rights_generate_security_audits: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # Assigning this user right to a user allows programs running on behalf of that user to impersonate a client. Requiring this user right for this kind of impersonation prevents an unauthorized user from convincing a client to connect to a service that they have created and then impersonating that client, which can elevate the unauthorized user's permissions to administrative or system levels. Only states NotConfigured and Allowed are supported.
        self._user_rights_impersonate_client: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which accounts can use a process with Write Property access to another process to increase the execution priority assigned to the other process. Only states NotConfigured and Allowed are supported.
        self._user_rights_increase_scheduling_priority: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users can dynamically load and unload device drivers or other code in to kernel mode. Only states NotConfigured and Allowed are supported.
        self._user_rights_load_unload_drivers: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users can log on to the computer. States NotConfigured, Allowed are supported
        self._user_rights_local_log_on: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which accounts can use a process to keep data in physical memory, which prevents the system from paging the data to virtual memory on disk. Only states NotConfigured and Allowed are supported.
        self._user_rights_lock_memory: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users can specify object access auditing options for individual resources, such as files, Active Directory objects, and registry keys. Only states NotConfigured and Allowed are supported.
        self._user_rights_manage_auditing_and_security_logs: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users and groups can run maintenance tasks on a volume, such as remote defragmentation. Only states NotConfigured and Allowed are supported.
        self._user_rights_manage_volumes: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines who can modify firmware environment values. Only states NotConfigured and Allowed are supported.
        self._user_rights_modify_firmware_environment: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which user accounts can modify the integrity label of objects, such as files, registry keys, or processes owned by other users. Only states NotConfigured and Allowed are supported.
        self._user_rights_modify_object_labels: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users can use performance monitoring tools to monitor the performance of system processes. Only states NotConfigured and Allowed are supported.
        self._user_rights_profile_single_process: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users and groups are prohibited from logging on as a Remote Desktop Services client. Only states NotConfigured and Blocked are supported
        self._user_rights_remote_desktop_services_log_on: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users are allowed to shut down a computer from a remote location on the network. Misuse of this user right can result in a denial of service. Only states NotConfigured and Allowed are supported.
        self._user_rights_remote_shutdown: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users can bypass file, directory, registry, and other persistent objects permissions when restoring backed up files and directories, and determines which users can set any valid security principal as the owner of an object. Only states NotConfigured and Allowed are supported.
        self._user_rights_restore_data: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # This user right determines which users can take ownership of any securable object in the system, including Active Directory objects, files and folders, printers, registry keys, processes, and threads. Only states NotConfigured and Allowed are supported.
        self._user_rights_take_ownership: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None
        # Defender TamperProtection setting options
        self._windows_defender_tamper_protection: Optional[windows_defender_tamper_protection_options.WindowsDefenderTamperProtectionOptions] = None
        # Possible values of xbox service start type
        self._xbox_services_accessory_management_service_startup_mode: Optional[service_start_type.ServiceStartType] = None
        # This setting determines whether xbox game save is enabled (1) or disabled (0).
        self._xbox_services_enable_xbox_game_save_task: Optional[bool] = None
        # Possible values of xbox service start type
        self._xbox_services_live_auth_manager_service_startup_mode: Optional[service_start_type.ServiceStartType] = None
        # Possible values of xbox service start type
        self._xbox_services_live_game_save_service_startup_mode: Optional[service_start_type.ServiceStartType] = None
        # Possible values of xbox service start type
        self._xbox_services_live_networking_service_startup_mode: Optional[service_start_type.ServiceStartType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10EndpointProtectionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10EndpointProtectionConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10EndpointProtectionConfiguration()
    
    @property
    def defender_additional_guarded_folders(self,) -> Optional[List[str]]:
        """
        Gets the defenderAdditionalGuardedFolders property value. List of folder paths to be added to the list of protected folders
        Returns: Optional[List[str]]
        """
        return self._defender_additional_guarded_folders
    
    @defender_additional_guarded_folders.setter
    def defender_additional_guarded_folders(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defenderAdditionalGuardedFolders property value. List of folder paths to be added to the list of protected folders
        Args:
            value: Value to set for the defenderAdditionalGuardedFolders property.
        """
        self._defender_additional_guarded_folders = value
    
    @property
    def defender_adobe_reader_launch_child_process(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderAdobeReaderLaunchChildProcess property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_adobe_reader_launch_child_process
    
    @defender_adobe_reader_launch_child_process.setter
    def defender_adobe_reader_launch_child_process(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderAdobeReaderLaunchChildProcess property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderAdobeReaderLaunchChildProcess property.
        """
        self._defender_adobe_reader_launch_child_process = value
    
    @property
    def defender_advanced_ransomeware_protection_type(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderAdvancedRansomewareProtectionType property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_advanced_ransomeware_protection_type
    
    @defender_advanced_ransomeware_protection_type.setter
    def defender_advanced_ransomeware_protection_type(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderAdvancedRansomewareProtectionType property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderAdvancedRansomewareProtectionType property.
        """
        self._defender_advanced_ransomeware_protection_type = value
    
    @property
    def defender_allow_behavior_monitoring(self,) -> Optional[bool]:
        """
        Gets the defenderAllowBehaviorMonitoring property value. Allows or disallows Windows Defender Behavior Monitoring functionality.
        Returns: Optional[bool]
        """
        return self._defender_allow_behavior_monitoring
    
    @defender_allow_behavior_monitoring.setter
    def defender_allow_behavior_monitoring(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderAllowBehaviorMonitoring property value. Allows or disallows Windows Defender Behavior Monitoring functionality.
        Args:
            value: Value to set for the defenderAllowBehaviorMonitoring property.
        """
        self._defender_allow_behavior_monitoring = value
    
    @property
    def defender_allow_cloud_protection(self,) -> Optional[bool]:
        """
        Gets the defenderAllowCloudProtection property value. To best protect your PC, Windows Defender will send information to Microsoft about any problems it finds. Microsoft will analyze that information, learn more about problems affecting you and other customers, and offer improved solutions.
        Returns: Optional[bool]
        """
        return self._defender_allow_cloud_protection
    
    @defender_allow_cloud_protection.setter
    def defender_allow_cloud_protection(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderAllowCloudProtection property value. To best protect your PC, Windows Defender will send information to Microsoft about any problems it finds. Microsoft will analyze that information, learn more about problems affecting you and other customers, and offer improved solutions.
        Args:
            value: Value to set for the defenderAllowCloudProtection property.
        """
        self._defender_allow_cloud_protection = value
    
    @property
    def defender_allow_end_user_access(self,) -> Optional[bool]:
        """
        Gets the defenderAllowEndUserAccess property value. Allows or disallows user access to the Windows Defender UI. If disallowed, all Windows Defender notifications will also be suppressed.
        Returns: Optional[bool]
        """
        return self._defender_allow_end_user_access
    
    @defender_allow_end_user_access.setter
    def defender_allow_end_user_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderAllowEndUserAccess property value. Allows or disallows user access to the Windows Defender UI. If disallowed, all Windows Defender notifications will also be suppressed.
        Args:
            value: Value to set for the defenderAllowEndUserAccess property.
        """
        self._defender_allow_end_user_access = value
    
    @property
    def defender_allow_intrusion_prevention_system(self,) -> Optional[bool]:
        """
        Gets the defenderAllowIntrusionPreventionSystem property value. Allows or disallows Windows Defender Intrusion Prevention functionality.
        Returns: Optional[bool]
        """
        return self._defender_allow_intrusion_prevention_system
    
    @defender_allow_intrusion_prevention_system.setter
    def defender_allow_intrusion_prevention_system(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderAllowIntrusionPreventionSystem property value. Allows or disallows Windows Defender Intrusion Prevention functionality.
        Args:
            value: Value to set for the defenderAllowIntrusionPreventionSystem property.
        """
        self._defender_allow_intrusion_prevention_system = value
    
    @property
    def defender_allow_on_access_protection(self,) -> Optional[bool]:
        """
        Gets the defenderAllowOnAccessProtection property value. Allows or disallows Windows Defender On Access Protection functionality.
        Returns: Optional[bool]
        """
        return self._defender_allow_on_access_protection
    
    @defender_allow_on_access_protection.setter
    def defender_allow_on_access_protection(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderAllowOnAccessProtection property value. Allows or disallows Windows Defender On Access Protection functionality.
        Args:
            value: Value to set for the defenderAllowOnAccessProtection property.
        """
        self._defender_allow_on_access_protection = value
    
    @property
    def defender_allow_real_time_monitoring(self,) -> Optional[bool]:
        """
        Gets the defenderAllowRealTimeMonitoring property value. Allows or disallows Windows Defender Realtime Monitoring functionality.
        Returns: Optional[bool]
        """
        return self._defender_allow_real_time_monitoring
    
    @defender_allow_real_time_monitoring.setter
    def defender_allow_real_time_monitoring(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderAllowRealTimeMonitoring property value. Allows or disallows Windows Defender Realtime Monitoring functionality.
        Args:
            value: Value to set for the defenderAllowRealTimeMonitoring property.
        """
        self._defender_allow_real_time_monitoring = value
    
    @property
    def defender_allow_scan_archive_files(self,) -> Optional[bool]:
        """
        Gets the defenderAllowScanArchiveFiles property value. Allows or disallows scanning of archives.
        Returns: Optional[bool]
        """
        return self._defender_allow_scan_archive_files
    
    @defender_allow_scan_archive_files.setter
    def defender_allow_scan_archive_files(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderAllowScanArchiveFiles property value. Allows or disallows scanning of archives.
        Args:
            value: Value to set for the defenderAllowScanArchiveFiles property.
        """
        self._defender_allow_scan_archive_files = value
    
    @property
    def defender_allow_scan_downloads(self,) -> Optional[bool]:
        """
        Gets the defenderAllowScanDownloads property value. Allows or disallows Windows Defender IOAVP Protection functionality.
        Returns: Optional[bool]
        """
        return self._defender_allow_scan_downloads
    
    @defender_allow_scan_downloads.setter
    def defender_allow_scan_downloads(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderAllowScanDownloads property value. Allows or disallows Windows Defender IOAVP Protection functionality.
        Args:
            value: Value to set for the defenderAllowScanDownloads property.
        """
        self._defender_allow_scan_downloads = value
    
    @property
    def defender_allow_scan_network_files(self,) -> Optional[bool]:
        """
        Gets the defenderAllowScanNetworkFiles property value. Allows or disallows a scanning of network files.
        Returns: Optional[bool]
        """
        return self._defender_allow_scan_network_files
    
    @defender_allow_scan_network_files.setter
    def defender_allow_scan_network_files(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderAllowScanNetworkFiles property value. Allows or disallows a scanning of network files.
        Args:
            value: Value to set for the defenderAllowScanNetworkFiles property.
        """
        self._defender_allow_scan_network_files = value
    
    @property
    def defender_allow_scan_removable_drives_during_full_scan(self,) -> Optional[bool]:
        """
        Gets the defenderAllowScanRemovableDrivesDuringFullScan property value. Allows or disallows a full scan of removable drives. During a quick scan, removable drives may still be scanned.
        Returns: Optional[bool]
        """
        return self._defender_allow_scan_removable_drives_during_full_scan
    
    @defender_allow_scan_removable_drives_during_full_scan.setter
    def defender_allow_scan_removable_drives_during_full_scan(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderAllowScanRemovableDrivesDuringFullScan property value. Allows or disallows a full scan of removable drives. During a quick scan, removable drives may still be scanned.
        Args:
            value: Value to set for the defenderAllowScanRemovableDrivesDuringFullScan property.
        """
        self._defender_allow_scan_removable_drives_during_full_scan = value
    
    @property
    def defender_allow_scan_scripts_loaded_in_internet_explorer(self,) -> Optional[bool]:
        """
        Gets the defenderAllowScanScriptsLoadedInInternetExplorer property value. Allows or disallows Windows Defender Script Scanning functionality.
        Returns: Optional[bool]
        """
        return self._defender_allow_scan_scripts_loaded_in_internet_explorer
    
    @defender_allow_scan_scripts_loaded_in_internet_explorer.setter
    def defender_allow_scan_scripts_loaded_in_internet_explorer(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderAllowScanScriptsLoadedInInternetExplorer property value. Allows or disallows Windows Defender Script Scanning functionality.
        Args:
            value: Value to set for the defenderAllowScanScriptsLoadedInInternetExplorer property.
        """
        self._defender_allow_scan_scripts_loaded_in_internet_explorer = value
    
    @property
    def defender_attack_surface_reduction_excluded_paths(self,) -> Optional[List[str]]:
        """
        Gets the defenderAttackSurfaceReductionExcludedPaths property value. List of exe files and folders to be excluded from attack surface reduction rules
        Returns: Optional[List[str]]
        """
        return self._defender_attack_surface_reduction_excluded_paths
    
    @defender_attack_surface_reduction_excluded_paths.setter
    def defender_attack_surface_reduction_excluded_paths(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defenderAttackSurfaceReductionExcludedPaths property value. List of exe files and folders to be excluded from attack surface reduction rules
        Args:
            value: Value to set for the defenderAttackSurfaceReductionExcludedPaths property.
        """
        self._defender_attack_surface_reduction_excluded_paths = value
    
    @property
    def defender_block_end_user_access(self,) -> Optional[bool]:
        """
        Gets the defenderBlockEndUserAccess property value. Allows or disallows user access to the Windows Defender UI. If disallowed, all Windows Defender notifications will also be suppressed.
        Returns: Optional[bool]
        """
        return self._defender_block_end_user_access
    
    @defender_block_end_user_access.setter
    def defender_block_end_user_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderBlockEndUserAccess property value. Allows or disallows user access to the Windows Defender UI. If disallowed, all Windows Defender notifications will also be suppressed.
        Args:
            value: Value to set for the defenderBlockEndUserAccess property.
        """
        self._defender_block_end_user_access = value
    
    @property
    def defender_block_persistence_through_wmi_type(self,) -> Optional[defender_attack_surface_type.DefenderAttackSurfaceType]:
        """
        Gets the defenderBlockPersistenceThroughWmiType property value. Possible values of Defender Attack Surface Reduction Rules
        Returns: Optional[defender_attack_surface_type.DefenderAttackSurfaceType]
        """
        return self._defender_block_persistence_through_wmi_type
    
    @defender_block_persistence_through_wmi_type.setter
    def defender_block_persistence_through_wmi_type(self,value: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None) -> None:
        """
        Sets the defenderBlockPersistenceThroughWmiType property value. Possible values of Defender Attack Surface Reduction Rules
        Args:
            value: Value to set for the defenderBlockPersistenceThroughWmiType property.
        """
        self._defender_block_persistence_through_wmi_type = value
    
    @property
    def defender_check_for_signatures_before_running_scan(self,) -> Optional[bool]:
        """
        Gets the defenderCheckForSignaturesBeforeRunningScan property value. This policy setting allows you to manage whether a check for new virus and spyware definitions will occur before running a scan.
        Returns: Optional[bool]
        """
        return self._defender_check_for_signatures_before_running_scan
    
    @defender_check_for_signatures_before_running_scan.setter
    def defender_check_for_signatures_before_running_scan(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderCheckForSignaturesBeforeRunningScan property value. This policy setting allows you to manage whether a check for new virus and spyware definitions will occur before running a scan.
        Args:
            value: Value to set for the defenderCheckForSignaturesBeforeRunningScan property.
        """
        self._defender_check_for_signatures_before_running_scan = value
    
    @property
    def defender_cloud_block_level(self,) -> Optional[defender_cloud_block_level_type.DefenderCloudBlockLevelType]:
        """
        Gets the defenderCloudBlockLevel property value. Added in Windows 10, version 1709. This policy setting determines how aggressive Windows Defender Antivirus will be in blocking and scanning suspicious files. Value type is integer. This feature requires the 'Join Microsoft MAPS' setting enabled in order to function. Possible values are: notConfigured, high, highPlus, zeroTolerance.
        Returns: Optional[defender_cloud_block_level_type.DefenderCloudBlockLevelType]
        """
        return self._defender_cloud_block_level
    
    @defender_cloud_block_level.setter
    def defender_cloud_block_level(self,value: Optional[defender_cloud_block_level_type.DefenderCloudBlockLevelType] = None) -> None:
        """
        Sets the defenderCloudBlockLevel property value. Added in Windows 10, version 1709. This policy setting determines how aggressive Windows Defender Antivirus will be in blocking and scanning suspicious files. Value type is integer. This feature requires the 'Join Microsoft MAPS' setting enabled in order to function. Possible values are: notConfigured, high, highPlus, zeroTolerance.
        Args:
            value: Value to set for the defenderCloudBlockLevel property.
        """
        self._defender_cloud_block_level = value
    
    @property
    def defender_cloud_extended_timeout_in_seconds(self,) -> Optional[int]:
        """
        Gets the defenderCloudExtendedTimeoutInSeconds property value. Added in Windows 10, version 1709. This feature allows Windows Defender Antivirus to block a suspicious file for up to 60 seconds, and scan it in the cloud to make sure it's safe. Value type is integer, range is 0 - 50. This feature depends on three other MAPS settings the must all be enabled- 'Configure the 'Block at First Sight' feature; 'Join Microsoft MAPS'; 'Send file samples when further analysis is required'. Valid values 0 to 50
        Returns: Optional[int]
        """
        return self._defender_cloud_extended_timeout_in_seconds
    
    @defender_cloud_extended_timeout_in_seconds.setter
    def defender_cloud_extended_timeout_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the defenderCloudExtendedTimeoutInSeconds property value. Added in Windows 10, version 1709. This feature allows Windows Defender Antivirus to block a suspicious file for up to 60 seconds, and scan it in the cloud to make sure it's safe. Value type is integer, range is 0 - 50. This feature depends on three other MAPS settings the must all be enabled- 'Configure the 'Block at First Sight' feature; 'Join Microsoft MAPS'; 'Send file samples when further analysis is required'. Valid values 0 to 50
        Args:
            value: Value to set for the defenderCloudExtendedTimeoutInSeconds property.
        """
        self._defender_cloud_extended_timeout_in_seconds = value
    
    @property
    def defender_days_before_deleting_quarantined_malware(self,) -> Optional[int]:
        """
        Gets the defenderDaysBeforeDeletingQuarantinedMalware property value. Time period (in days) that quarantine items will be stored on the system. Valid values 0 to 90
        Returns: Optional[int]
        """
        return self._defender_days_before_deleting_quarantined_malware
    
    @defender_days_before_deleting_quarantined_malware.setter
    def defender_days_before_deleting_quarantined_malware(self,value: Optional[int] = None) -> None:
        """
        Sets the defenderDaysBeforeDeletingQuarantinedMalware property value. Time period (in days) that quarantine items will be stored on the system. Valid values 0 to 90
        Args:
            value: Value to set for the defenderDaysBeforeDeletingQuarantinedMalware property.
        """
        self._defender_days_before_deleting_quarantined_malware = value
    
    @property
    def defender_detected_malware_actions(self,) -> Optional[defender_detected_malware_actions.DefenderDetectedMalwareActions]:
        """
        Gets the defenderDetectedMalwareActions property value. Allows an administrator to specify any valid threat severity levels and the corresponding default action ID to take.
        Returns: Optional[defender_detected_malware_actions.DefenderDetectedMalwareActions]
        """
        return self._defender_detected_malware_actions
    
    @defender_detected_malware_actions.setter
    def defender_detected_malware_actions(self,value: Optional[defender_detected_malware_actions.DefenderDetectedMalwareActions] = None) -> None:
        """
        Sets the defenderDetectedMalwareActions property value. Allows an administrator to specify any valid threat severity levels and the corresponding default action ID to take.
        Args:
            value: Value to set for the defenderDetectedMalwareActions property.
        """
        self._defender_detected_malware_actions = value
    
    @property
    def defender_disable_behavior_monitoring(self,) -> Optional[bool]:
        """
        Gets the defenderDisableBehaviorMonitoring property value. Allows or disallows Windows Defender Behavior Monitoring functionality.
        Returns: Optional[bool]
        """
        return self._defender_disable_behavior_monitoring
    
    @defender_disable_behavior_monitoring.setter
    def defender_disable_behavior_monitoring(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderDisableBehaviorMonitoring property value. Allows or disallows Windows Defender Behavior Monitoring functionality.
        Args:
            value: Value to set for the defenderDisableBehaviorMonitoring property.
        """
        self._defender_disable_behavior_monitoring = value
    
    @property
    def defender_disable_catchup_full_scan(self,) -> Optional[bool]:
        """
        Gets the defenderDisableCatchupFullScan property value. This policy setting allows you to configure catch-up scans for scheduled full scans. A catch-up scan is a scan that is initiated because a regularly scheduled scan was missed. Usually these scheduled scans are missed because the computer was turned off at the scheduled time.
        Returns: Optional[bool]
        """
        return self._defender_disable_catchup_full_scan
    
    @defender_disable_catchup_full_scan.setter
    def defender_disable_catchup_full_scan(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderDisableCatchupFullScan property value. This policy setting allows you to configure catch-up scans for scheduled full scans. A catch-up scan is a scan that is initiated because a regularly scheduled scan was missed. Usually these scheduled scans are missed because the computer was turned off at the scheduled time.
        Args:
            value: Value to set for the defenderDisableCatchupFullScan property.
        """
        self._defender_disable_catchup_full_scan = value
    
    @property
    def defender_disable_catchup_quick_scan(self,) -> Optional[bool]:
        """
        Gets the defenderDisableCatchupQuickScan property value. This policy setting allows you to configure catch-up scans for scheduled quick scans. A catch-up scan is a scan that is initiated because a regularly scheduled scan was missed. Usually these scheduled scans are missed because the computer was turned off at the scheduled time.
        Returns: Optional[bool]
        """
        return self._defender_disable_catchup_quick_scan
    
    @defender_disable_catchup_quick_scan.setter
    def defender_disable_catchup_quick_scan(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderDisableCatchupQuickScan property value. This policy setting allows you to configure catch-up scans for scheduled quick scans. A catch-up scan is a scan that is initiated because a regularly scheduled scan was missed. Usually these scheduled scans are missed because the computer was turned off at the scheduled time.
        Args:
            value: Value to set for the defenderDisableCatchupQuickScan property.
        """
        self._defender_disable_catchup_quick_scan = value
    
    @property
    def defender_disable_cloud_protection(self,) -> Optional[bool]:
        """
        Gets the defenderDisableCloudProtection property value. To best protect your PC, Windows Defender will send information to Microsoft about any problems it finds. Microsoft will analyze that information, learn more about problems affecting you and other customers, and offer improved solutions.
        Returns: Optional[bool]
        """
        return self._defender_disable_cloud_protection
    
    @defender_disable_cloud_protection.setter
    def defender_disable_cloud_protection(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderDisableCloudProtection property value. To best protect your PC, Windows Defender will send information to Microsoft about any problems it finds. Microsoft will analyze that information, learn more about problems affecting you and other customers, and offer improved solutions.
        Args:
            value: Value to set for the defenderDisableCloudProtection property.
        """
        self._defender_disable_cloud_protection = value
    
    @property
    def defender_disable_intrusion_prevention_system(self,) -> Optional[bool]:
        """
        Gets the defenderDisableIntrusionPreventionSystem property value. Allows or disallows Windows Defender Intrusion Prevention functionality.
        Returns: Optional[bool]
        """
        return self._defender_disable_intrusion_prevention_system
    
    @defender_disable_intrusion_prevention_system.setter
    def defender_disable_intrusion_prevention_system(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderDisableIntrusionPreventionSystem property value. Allows or disallows Windows Defender Intrusion Prevention functionality.
        Args:
            value: Value to set for the defenderDisableIntrusionPreventionSystem property.
        """
        self._defender_disable_intrusion_prevention_system = value
    
    @property
    def defender_disable_on_access_protection(self,) -> Optional[bool]:
        """
        Gets the defenderDisableOnAccessProtection property value. Allows or disallows Windows Defender On Access Protection functionality.
        Returns: Optional[bool]
        """
        return self._defender_disable_on_access_protection
    
    @defender_disable_on_access_protection.setter
    def defender_disable_on_access_protection(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderDisableOnAccessProtection property value. Allows or disallows Windows Defender On Access Protection functionality.
        Args:
            value: Value to set for the defenderDisableOnAccessProtection property.
        """
        self._defender_disable_on_access_protection = value
    
    @property
    def defender_disable_real_time_monitoring(self,) -> Optional[bool]:
        """
        Gets the defenderDisableRealTimeMonitoring property value. Allows or disallows Windows Defender Realtime Monitoring functionality.
        Returns: Optional[bool]
        """
        return self._defender_disable_real_time_monitoring
    
    @defender_disable_real_time_monitoring.setter
    def defender_disable_real_time_monitoring(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderDisableRealTimeMonitoring property value. Allows or disallows Windows Defender Realtime Monitoring functionality.
        Args:
            value: Value to set for the defenderDisableRealTimeMonitoring property.
        """
        self._defender_disable_real_time_monitoring = value
    
    @property
    def defender_disable_scan_archive_files(self,) -> Optional[bool]:
        """
        Gets the defenderDisableScanArchiveFiles property value. Allows or disallows scanning of archives.
        Returns: Optional[bool]
        """
        return self._defender_disable_scan_archive_files
    
    @defender_disable_scan_archive_files.setter
    def defender_disable_scan_archive_files(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderDisableScanArchiveFiles property value. Allows or disallows scanning of archives.
        Args:
            value: Value to set for the defenderDisableScanArchiveFiles property.
        """
        self._defender_disable_scan_archive_files = value
    
    @property
    def defender_disable_scan_downloads(self,) -> Optional[bool]:
        """
        Gets the defenderDisableScanDownloads property value. Allows or disallows Windows Defender IOAVP Protection functionality.
        Returns: Optional[bool]
        """
        return self._defender_disable_scan_downloads
    
    @defender_disable_scan_downloads.setter
    def defender_disable_scan_downloads(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderDisableScanDownloads property value. Allows or disallows Windows Defender IOAVP Protection functionality.
        Args:
            value: Value to set for the defenderDisableScanDownloads property.
        """
        self._defender_disable_scan_downloads = value
    
    @property
    def defender_disable_scan_network_files(self,) -> Optional[bool]:
        """
        Gets the defenderDisableScanNetworkFiles property value. Allows or disallows a scanning of network files.
        Returns: Optional[bool]
        """
        return self._defender_disable_scan_network_files
    
    @defender_disable_scan_network_files.setter
    def defender_disable_scan_network_files(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderDisableScanNetworkFiles property value. Allows or disallows a scanning of network files.
        Args:
            value: Value to set for the defenderDisableScanNetworkFiles property.
        """
        self._defender_disable_scan_network_files = value
    
    @property
    def defender_disable_scan_removable_drives_during_full_scan(self,) -> Optional[bool]:
        """
        Gets the defenderDisableScanRemovableDrivesDuringFullScan property value. Allows or disallows a full scan of removable drives. During a quick scan, removable drives may still be scanned.
        Returns: Optional[bool]
        """
        return self._defender_disable_scan_removable_drives_during_full_scan
    
    @defender_disable_scan_removable_drives_during_full_scan.setter
    def defender_disable_scan_removable_drives_during_full_scan(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderDisableScanRemovableDrivesDuringFullScan property value. Allows or disallows a full scan of removable drives. During a quick scan, removable drives may still be scanned.
        Args:
            value: Value to set for the defenderDisableScanRemovableDrivesDuringFullScan property.
        """
        self._defender_disable_scan_removable_drives_during_full_scan = value
    
    @property
    def defender_disable_scan_scripts_loaded_in_internet_explorer(self,) -> Optional[bool]:
        """
        Gets the defenderDisableScanScriptsLoadedInInternetExplorer property value. Allows or disallows Windows Defender Script Scanning functionality.
        Returns: Optional[bool]
        """
        return self._defender_disable_scan_scripts_loaded_in_internet_explorer
    
    @defender_disable_scan_scripts_loaded_in_internet_explorer.setter
    def defender_disable_scan_scripts_loaded_in_internet_explorer(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderDisableScanScriptsLoadedInInternetExplorer property value. Allows or disallows Windows Defender Script Scanning functionality.
        Args:
            value: Value to set for the defenderDisableScanScriptsLoadedInInternetExplorer property.
        """
        self._defender_disable_scan_scripts_loaded_in_internet_explorer = value
    
    @property
    def defender_email_content_execution(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderEmailContentExecution property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_email_content_execution
    
    @defender_email_content_execution.setter
    def defender_email_content_execution(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderEmailContentExecution property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderEmailContentExecution property.
        """
        self._defender_email_content_execution = value
    
    @property
    def defender_email_content_execution_type(self,) -> Optional[defender_attack_surface_type.DefenderAttackSurfaceType]:
        """
        Gets the defenderEmailContentExecutionType property value. Possible values of Defender Attack Surface Reduction Rules
        Returns: Optional[defender_attack_surface_type.DefenderAttackSurfaceType]
        """
        return self._defender_email_content_execution_type
    
    @defender_email_content_execution_type.setter
    def defender_email_content_execution_type(self,value: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None) -> None:
        """
        Sets the defenderEmailContentExecutionType property value. Possible values of Defender Attack Surface Reduction Rules
        Args:
            value: Value to set for the defenderEmailContentExecutionType property.
        """
        self._defender_email_content_execution_type = value
    
    @property
    def defender_enable_low_cpu_priority(self,) -> Optional[bool]:
        """
        Gets the defenderEnableLowCpuPriority property value. This policy setting allows you to enable or disable low CPU priority for scheduled scans.
        Returns: Optional[bool]
        """
        return self._defender_enable_low_cpu_priority
    
    @defender_enable_low_cpu_priority.setter
    def defender_enable_low_cpu_priority(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderEnableLowCpuPriority property value. This policy setting allows you to enable or disable low CPU priority for scheduled scans.
        Args:
            value: Value to set for the defenderEnableLowCpuPriority property.
        """
        self._defender_enable_low_cpu_priority = value
    
    @property
    def defender_enable_scan_incoming_mail(self,) -> Optional[bool]:
        """
        Gets the defenderEnableScanIncomingMail property value. Allows or disallows scanning of email.
        Returns: Optional[bool]
        """
        return self._defender_enable_scan_incoming_mail
    
    @defender_enable_scan_incoming_mail.setter
    def defender_enable_scan_incoming_mail(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderEnableScanIncomingMail property value. Allows or disallows scanning of email.
        Args:
            value: Value to set for the defenderEnableScanIncomingMail property.
        """
        self._defender_enable_scan_incoming_mail = value
    
    @property
    def defender_enable_scan_mapped_network_drives_during_full_scan(self,) -> Optional[bool]:
        """
        Gets the defenderEnableScanMappedNetworkDrivesDuringFullScan property value. Allows or disallows a full scan of mapped network drives.
        Returns: Optional[bool]
        """
        return self._defender_enable_scan_mapped_network_drives_during_full_scan
    
    @defender_enable_scan_mapped_network_drives_during_full_scan.setter
    def defender_enable_scan_mapped_network_drives_during_full_scan(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderEnableScanMappedNetworkDrivesDuringFullScan property value. Allows or disallows a full scan of mapped network drives.
        Args:
            value: Value to set for the defenderEnableScanMappedNetworkDrivesDuringFullScan property.
        """
        self._defender_enable_scan_mapped_network_drives_during_full_scan = value
    
    @property
    def defender_exploit_protection_xml(self,) -> Optional[bytes]:
        """
        Gets the defenderExploitProtectionXml property value. Xml content containing information regarding exploit protection details.
        Returns: Optional[bytes]
        """
        return self._defender_exploit_protection_xml
    
    @defender_exploit_protection_xml.setter
    def defender_exploit_protection_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the defenderExploitProtectionXml property value. Xml content containing information regarding exploit protection details.
        Args:
            value: Value to set for the defenderExploitProtectionXml property.
        """
        self._defender_exploit_protection_xml = value
    
    @property
    def defender_exploit_protection_xml_file_name(self,) -> Optional[str]:
        """
        Gets the defenderExploitProtectionXmlFileName property value. Name of the file from which DefenderExploitProtectionXml was obtained.
        Returns: Optional[str]
        """
        return self._defender_exploit_protection_xml_file_name
    
    @defender_exploit_protection_xml_file_name.setter
    def defender_exploit_protection_xml_file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the defenderExploitProtectionXmlFileName property value. Name of the file from which DefenderExploitProtectionXml was obtained.
        Args:
            value: Value to set for the defenderExploitProtectionXmlFileName property.
        """
        self._defender_exploit_protection_xml_file_name = value
    
    @property
    def defender_file_extensions_to_exclude(self,) -> Optional[List[str]]:
        """
        Gets the defenderFileExtensionsToExclude property value. File extensions to exclude from scans and real time protection.
        Returns: Optional[List[str]]
        """
        return self._defender_file_extensions_to_exclude
    
    @defender_file_extensions_to_exclude.setter
    def defender_file_extensions_to_exclude(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defenderFileExtensionsToExclude property value. File extensions to exclude from scans and real time protection.
        Args:
            value: Value to set for the defenderFileExtensionsToExclude property.
        """
        self._defender_file_extensions_to_exclude = value
    
    @property
    def defender_files_and_folders_to_exclude(self,) -> Optional[List[str]]:
        """
        Gets the defenderFilesAndFoldersToExclude property value. Files and folder to exclude from scans and real time protection.
        Returns: Optional[List[str]]
        """
        return self._defender_files_and_folders_to_exclude
    
    @defender_files_and_folders_to_exclude.setter
    def defender_files_and_folders_to_exclude(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defenderFilesAndFoldersToExclude property value. Files and folder to exclude from scans and real time protection.
        Args:
            value: Value to set for the defenderFilesAndFoldersToExclude property.
        """
        self._defender_files_and_folders_to_exclude = value
    
    @property
    def defender_guarded_folders_allowed_app_paths(self,) -> Optional[List[str]]:
        """
        Gets the defenderGuardedFoldersAllowedAppPaths property value. List of paths to exe that are allowed to access protected folders
        Returns: Optional[List[str]]
        """
        return self._defender_guarded_folders_allowed_app_paths
    
    @defender_guarded_folders_allowed_app_paths.setter
    def defender_guarded_folders_allowed_app_paths(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defenderGuardedFoldersAllowedAppPaths property value. List of paths to exe that are allowed to access protected folders
        Args:
            value: Value to set for the defenderGuardedFoldersAllowedAppPaths property.
        """
        self._defender_guarded_folders_allowed_app_paths = value
    
    @property
    def defender_guard_my_folders_type(self,) -> Optional[folder_protection_type.FolderProtectionType]:
        """
        Gets the defenderGuardMyFoldersType property value. Possible values of Folder Protection
        Returns: Optional[folder_protection_type.FolderProtectionType]
        """
        return self._defender_guard_my_folders_type
    
    @defender_guard_my_folders_type.setter
    def defender_guard_my_folders_type(self,value: Optional[folder_protection_type.FolderProtectionType] = None) -> None:
        """
        Sets the defenderGuardMyFoldersType property value. Possible values of Folder Protection
        Args:
            value: Value to set for the defenderGuardMyFoldersType property.
        """
        self._defender_guard_my_folders_type = value
    
    @property
    def defender_network_protection_type(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderNetworkProtectionType property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_network_protection_type
    
    @defender_network_protection_type.setter
    def defender_network_protection_type(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderNetworkProtectionType property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderNetworkProtectionType property.
        """
        self._defender_network_protection_type = value
    
    @property
    def defender_office_apps_executable_content_creation_or_launch(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderOfficeAppsExecutableContentCreationOrLaunch property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_office_apps_executable_content_creation_or_launch
    
    @defender_office_apps_executable_content_creation_or_launch.setter
    def defender_office_apps_executable_content_creation_or_launch(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderOfficeAppsExecutableContentCreationOrLaunch property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderOfficeAppsExecutableContentCreationOrLaunch property.
        """
        self._defender_office_apps_executable_content_creation_or_launch = value
    
    @property
    def defender_office_apps_executable_content_creation_or_launch_type(self,) -> Optional[defender_attack_surface_type.DefenderAttackSurfaceType]:
        """
        Gets the defenderOfficeAppsExecutableContentCreationOrLaunchType property value. Possible values of Defender Attack Surface Reduction Rules
        Returns: Optional[defender_attack_surface_type.DefenderAttackSurfaceType]
        """
        return self._defender_office_apps_executable_content_creation_or_launch_type
    
    @defender_office_apps_executable_content_creation_or_launch_type.setter
    def defender_office_apps_executable_content_creation_or_launch_type(self,value: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None) -> None:
        """
        Sets the defenderOfficeAppsExecutableContentCreationOrLaunchType property value. Possible values of Defender Attack Surface Reduction Rules
        Args:
            value: Value to set for the defenderOfficeAppsExecutableContentCreationOrLaunchType property.
        """
        self._defender_office_apps_executable_content_creation_or_launch_type = value
    
    @property
    def defender_office_apps_launch_child_process(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderOfficeAppsLaunchChildProcess property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_office_apps_launch_child_process
    
    @defender_office_apps_launch_child_process.setter
    def defender_office_apps_launch_child_process(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderOfficeAppsLaunchChildProcess property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderOfficeAppsLaunchChildProcess property.
        """
        self._defender_office_apps_launch_child_process = value
    
    @property
    def defender_office_apps_launch_child_process_type(self,) -> Optional[defender_attack_surface_type.DefenderAttackSurfaceType]:
        """
        Gets the defenderOfficeAppsLaunchChildProcessType property value. Possible values of Defender Attack Surface Reduction Rules
        Returns: Optional[defender_attack_surface_type.DefenderAttackSurfaceType]
        """
        return self._defender_office_apps_launch_child_process_type
    
    @defender_office_apps_launch_child_process_type.setter
    def defender_office_apps_launch_child_process_type(self,value: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None) -> None:
        """
        Sets the defenderOfficeAppsLaunchChildProcessType property value. Possible values of Defender Attack Surface Reduction Rules
        Args:
            value: Value to set for the defenderOfficeAppsLaunchChildProcessType property.
        """
        self._defender_office_apps_launch_child_process_type = value
    
    @property
    def defender_office_apps_other_process_injection(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderOfficeAppsOtherProcessInjection property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_office_apps_other_process_injection
    
    @defender_office_apps_other_process_injection.setter
    def defender_office_apps_other_process_injection(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderOfficeAppsOtherProcessInjection property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderOfficeAppsOtherProcessInjection property.
        """
        self._defender_office_apps_other_process_injection = value
    
    @property
    def defender_office_apps_other_process_injection_type(self,) -> Optional[defender_attack_surface_type.DefenderAttackSurfaceType]:
        """
        Gets the defenderOfficeAppsOtherProcessInjectionType property value. Possible values of Defender Attack Surface Reduction Rules
        Returns: Optional[defender_attack_surface_type.DefenderAttackSurfaceType]
        """
        return self._defender_office_apps_other_process_injection_type
    
    @defender_office_apps_other_process_injection_type.setter
    def defender_office_apps_other_process_injection_type(self,value: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None) -> None:
        """
        Sets the defenderOfficeAppsOtherProcessInjectionType property value. Possible values of Defender Attack Surface Reduction Rules
        Args:
            value: Value to set for the defenderOfficeAppsOtherProcessInjectionType property.
        """
        self._defender_office_apps_other_process_injection_type = value
    
    @property
    def defender_office_communication_apps_launch_child_process(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderOfficeCommunicationAppsLaunchChildProcess property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_office_communication_apps_launch_child_process
    
    @defender_office_communication_apps_launch_child_process.setter
    def defender_office_communication_apps_launch_child_process(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderOfficeCommunicationAppsLaunchChildProcess property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderOfficeCommunicationAppsLaunchChildProcess property.
        """
        self._defender_office_communication_apps_launch_child_process = value
    
    @property
    def defender_office_macro_code_allow_win32_imports(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderOfficeMacroCodeAllowWin32Imports property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_office_macro_code_allow_win32_imports
    
    @defender_office_macro_code_allow_win32_imports.setter
    def defender_office_macro_code_allow_win32_imports(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderOfficeMacroCodeAllowWin32Imports property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderOfficeMacroCodeAllowWin32Imports property.
        """
        self._defender_office_macro_code_allow_win32_imports = value
    
    @property
    def defender_office_macro_code_allow_win32_imports_type(self,) -> Optional[defender_attack_surface_type.DefenderAttackSurfaceType]:
        """
        Gets the defenderOfficeMacroCodeAllowWin32ImportsType property value. Possible values of Defender Attack Surface Reduction Rules
        Returns: Optional[defender_attack_surface_type.DefenderAttackSurfaceType]
        """
        return self._defender_office_macro_code_allow_win32_imports_type
    
    @defender_office_macro_code_allow_win32_imports_type.setter
    def defender_office_macro_code_allow_win32_imports_type(self,value: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None) -> None:
        """
        Sets the defenderOfficeMacroCodeAllowWin32ImportsType property value. Possible values of Defender Attack Surface Reduction Rules
        Args:
            value: Value to set for the defenderOfficeMacroCodeAllowWin32ImportsType property.
        """
        self._defender_office_macro_code_allow_win32_imports_type = value
    
    @property
    def defender_potentially_unwanted_app_action(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderPotentiallyUnwantedAppAction property value. Added in Windows 10, version 1607. Specifies the level of detection for potentially unwanted applications (PUAs). Windows Defender alerts you when potentially unwanted software is being downloaded or attempts to install itself on your computer. Possible values are: userDefined, enable, auditMode, warn, notConfigured.
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_potentially_unwanted_app_action
    
    @defender_potentially_unwanted_app_action.setter
    def defender_potentially_unwanted_app_action(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderPotentiallyUnwantedAppAction property value. Added in Windows 10, version 1607. Specifies the level of detection for potentially unwanted applications (PUAs). Windows Defender alerts you when potentially unwanted software is being downloaded or attempts to install itself on your computer. Possible values are: userDefined, enable, auditMode, warn, notConfigured.
        Args:
            value: Value to set for the defenderPotentiallyUnwantedAppAction property.
        """
        self._defender_potentially_unwanted_app_action = value
    
    @property
    def defender_prevent_credential_stealing_type(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderPreventCredentialStealingType property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_prevent_credential_stealing_type
    
    @defender_prevent_credential_stealing_type.setter
    def defender_prevent_credential_stealing_type(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderPreventCredentialStealingType property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderPreventCredentialStealingType property.
        """
        self._defender_prevent_credential_stealing_type = value
    
    @property
    def defender_process_creation(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderProcessCreation property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_process_creation
    
    @defender_process_creation.setter
    def defender_process_creation(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderProcessCreation property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderProcessCreation property.
        """
        self._defender_process_creation = value
    
    @property
    def defender_process_creation_type(self,) -> Optional[defender_attack_surface_type.DefenderAttackSurfaceType]:
        """
        Gets the defenderProcessCreationType property value. Possible values of Defender Attack Surface Reduction Rules
        Returns: Optional[defender_attack_surface_type.DefenderAttackSurfaceType]
        """
        return self._defender_process_creation_type
    
    @defender_process_creation_type.setter
    def defender_process_creation_type(self,value: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None) -> None:
        """
        Sets the defenderProcessCreationType property value. Possible values of Defender Attack Surface Reduction Rules
        Args:
            value: Value to set for the defenderProcessCreationType property.
        """
        self._defender_process_creation_type = value
    
    @property
    def defender_processes_to_exclude(self,) -> Optional[List[str]]:
        """
        Gets the defenderProcessesToExclude property value. Processes to exclude from scans and real time protection.
        Returns: Optional[List[str]]
        """
        return self._defender_processes_to_exclude
    
    @defender_processes_to_exclude.setter
    def defender_processes_to_exclude(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defenderProcessesToExclude property value. Processes to exclude from scans and real time protection.
        Args:
            value: Value to set for the defenderProcessesToExclude property.
        """
        self._defender_processes_to_exclude = value
    
    @property
    def defender_scan_direction(self,) -> Optional[defender_realtime_scan_direction.DefenderRealtimeScanDirection]:
        """
        Gets the defenderScanDirection property value. Controls which sets of files should be monitored. Possible values are: monitorAllFiles, monitorIncomingFilesOnly, monitorOutgoingFilesOnly.
        Returns: Optional[defender_realtime_scan_direction.DefenderRealtimeScanDirection]
        """
        return self._defender_scan_direction
    
    @defender_scan_direction.setter
    def defender_scan_direction(self,value: Optional[defender_realtime_scan_direction.DefenderRealtimeScanDirection] = None) -> None:
        """
        Sets the defenderScanDirection property value. Controls which sets of files should be monitored. Possible values are: monitorAllFiles, monitorIncomingFilesOnly, monitorOutgoingFilesOnly.
        Args:
            value: Value to set for the defenderScanDirection property.
        """
        self._defender_scan_direction = value
    
    @property
    def defender_scan_max_cpu_percentage(self,) -> Optional[int]:
        """
        Gets the defenderScanMaxCpuPercentage property value. Represents the average CPU load factor for the Windows Defender scan (in percent). The default value is 50. Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._defender_scan_max_cpu_percentage
    
    @defender_scan_max_cpu_percentage.setter
    def defender_scan_max_cpu_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the defenderScanMaxCpuPercentage property value. Represents the average CPU load factor for the Windows Defender scan (in percent). The default value is 50. Valid values 0 to 100
        Args:
            value: Value to set for the defenderScanMaxCpuPercentage property.
        """
        self._defender_scan_max_cpu_percentage = value
    
    @property
    def defender_scan_type(self,) -> Optional[defender_scan_type.DefenderScanType]:
        """
        Gets the defenderScanType property value. Selects whether to perform a quick scan or full scan. Possible values are: userDefined, disabled, quick, full.
        Returns: Optional[defender_scan_type.DefenderScanType]
        """
        return self._defender_scan_type
    
    @defender_scan_type.setter
    def defender_scan_type(self,value: Optional[defender_scan_type.DefenderScanType] = None) -> None:
        """
        Sets the defenderScanType property value. Selects whether to perform a quick scan or full scan. Possible values are: userDefined, disabled, quick, full.
        Args:
            value: Value to set for the defenderScanType property.
        """
        self._defender_scan_type = value
    
    @property
    def defender_scheduled_quick_scan_time(self,) -> Optional[Time]:
        """
        Gets the defenderScheduledQuickScanTime property value. Selects the time of day that the Windows Defender quick scan should run. For example, a value of 0=12:00AM, a value of 60=1:00AM, a value of 120=2:00, and so on, up to a value of 1380=11:00PM. The default value is 120
        Returns: Optional[Time]
        """
        return self._defender_scheduled_quick_scan_time
    
    @defender_scheduled_quick_scan_time.setter
    def defender_scheduled_quick_scan_time(self,value: Optional[Time] = None) -> None:
        """
        Sets the defenderScheduledQuickScanTime property value. Selects the time of day that the Windows Defender quick scan should run. For example, a value of 0=12:00AM, a value of 60=1:00AM, a value of 120=2:00, and so on, up to a value of 1380=11:00PM. The default value is 120
        Args:
            value: Value to set for the defenderScheduledQuickScanTime property.
        """
        self._defender_scheduled_quick_scan_time = value
    
    @property
    def defender_scheduled_scan_day(self,) -> Optional[weekly_schedule.WeeklySchedule]:
        """
        Gets the defenderScheduledScanDay property value. Selects the day that the Windows Defender scan should run. Possible values are: userDefined, everyday, sunday, monday, tuesday, wednesday, thursday, friday, saturday, noScheduledScan.
        Returns: Optional[weekly_schedule.WeeklySchedule]
        """
        return self._defender_scheduled_scan_day
    
    @defender_scheduled_scan_day.setter
    def defender_scheduled_scan_day(self,value: Optional[weekly_schedule.WeeklySchedule] = None) -> None:
        """
        Sets the defenderScheduledScanDay property value. Selects the day that the Windows Defender scan should run. Possible values are: userDefined, everyday, sunday, monday, tuesday, wednesday, thursday, friday, saturday, noScheduledScan.
        Args:
            value: Value to set for the defenderScheduledScanDay property.
        """
        self._defender_scheduled_scan_day = value
    
    @property
    def defender_scheduled_scan_time(self,) -> Optional[Time]:
        """
        Gets the defenderScheduledScanTime property value. Selects the time of day that the Windows Defender scan should run.
        Returns: Optional[Time]
        """
        return self._defender_scheduled_scan_time
    
    @defender_scheduled_scan_time.setter
    def defender_scheduled_scan_time(self,value: Optional[Time] = None) -> None:
        """
        Sets the defenderScheduledScanTime property value. Selects the time of day that the Windows Defender scan should run.
        Args:
            value: Value to set for the defenderScheduledScanTime property.
        """
        self._defender_scheduled_scan_time = value
    
    @property
    def defender_script_downloaded_payload_execution(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderScriptDownloadedPayloadExecution property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_script_downloaded_payload_execution
    
    @defender_script_downloaded_payload_execution.setter
    def defender_script_downloaded_payload_execution(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderScriptDownloadedPayloadExecution property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderScriptDownloadedPayloadExecution property.
        """
        self._defender_script_downloaded_payload_execution = value
    
    @property
    def defender_script_downloaded_payload_execution_type(self,) -> Optional[defender_attack_surface_type.DefenderAttackSurfaceType]:
        """
        Gets the defenderScriptDownloadedPayloadExecutionType property value. Possible values of Defender Attack Surface Reduction Rules
        Returns: Optional[defender_attack_surface_type.DefenderAttackSurfaceType]
        """
        return self._defender_script_downloaded_payload_execution_type
    
    @defender_script_downloaded_payload_execution_type.setter
    def defender_script_downloaded_payload_execution_type(self,value: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None) -> None:
        """
        Sets the defenderScriptDownloadedPayloadExecutionType property value. Possible values of Defender Attack Surface Reduction Rules
        Args:
            value: Value to set for the defenderScriptDownloadedPayloadExecutionType property.
        """
        self._defender_script_downloaded_payload_execution_type = value
    
    @property
    def defender_script_obfuscated_macro_code(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderScriptObfuscatedMacroCode property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_script_obfuscated_macro_code
    
    @defender_script_obfuscated_macro_code.setter
    def defender_script_obfuscated_macro_code(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderScriptObfuscatedMacroCode property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderScriptObfuscatedMacroCode property.
        """
        self._defender_script_obfuscated_macro_code = value
    
    @property
    def defender_script_obfuscated_macro_code_type(self,) -> Optional[defender_attack_surface_type.DefenderAttackSurfaceType]:
        """
        Gets the defenderScriptObfuscatedMacroCodeType property value. Possible values of Defender Attack Surface Reduction Rules
        Returns: Optional[defender_attack_surface_type.DefenderAttackSurfaceType]
        """
        return self._defender_script_obfuscated_macro_code_type
    
    @defender_script_obfuscated_macro_code_type.setter
    def defender_script_obfuscated_macro_code_type(self,value: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None) -> None:
        """
        Sets the defenderScriptObfuscatedMacroCodeType property value. Possible values of Defender Attack Surface Reduction Rules
        Args:
            value: Value to set for the defenderScriptObfuscatedMacroCodeType property.
        """
        self._defender_script_obfuscated_macro_code_type = value
    
    @property
    def defender_security_center_block_exploit_protection_override(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterBlockExploitProtectionOverride property value. Indicates whether or not to block user from overriding Exploit Protection settings.
        Returns: Optional[bool]
        """
        return self._defender_security_center_block_exploit_protection_override
    
    @defender_security_center_block_exploit_protection_override.setter
    def defender_security_center_block_exploit_protection_override(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterBlockExploitProtectionOverride property value. Indicates whether or not to block user from overriding Exploit Protection settings.
        Args:
            value: Value to set for the defenderSecurityCenterBlockExploitProtectionOverride property.
        """
        self._defender_security_center_block_exploit_protection_override = value
    
    @property
    def defender_security_center_disable_account_u_i(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterDisableAccountUI property value. Used to disable the display of the account protection area.
        Returns: Optional[bool]
        """
        return self._defender_security_center_disable_account_u_i
    
    @defender_security_center_disable_account_u_i.setter
    def defender_security_center_disable_account_u_i(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterDisableAccountUI property value. Used to disable the display of the account protection area.
        Args:
            value: Value to set for the defenderSecurityCenterDisableAccountUI property.
        """
        self._defender_security_center_disable_account_u_i = value
    
    @property
    def defender_security_center_disable_app_browser_u_i(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterDisableAppBrowserUI property value. Used to disable the display of the app and browser protection area.
        Returns: Optional[bool]
        """
        return self._defender_security_center_disable_app_browser_u_i
    
    @defender_security_center_disable_app_browser_u_i.setter
    def defender_security_center_disable_app_browser_u_i(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterDisableAppBrowserUI property value. Used to disable the display of the app and browser protection area.
        Args:
            value: Value to set for the defenderSecurityCenterDisableAppBrowserUI property.
        """
        self._defender_security_center_disable_app_browser_u_i = value
    
    @property
    def defender_security_center_disable_clear_tpm_u_i(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterDisableClearTpmUI property value. Used to disable the display of the Clear TPM button.
        Returns: Optional[bool]
        """
        return self._defender_security_center_disable_clear_tpm_u_i
    
    @defender_security_center_disable_clear_tpm_u_i.setter
    def defender_security_center_disable_clear_tpm_u_i(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterDisableClearTpmUI property value. Used to disable the display of the Clear TPM button.
        Args:
            value: Value to set for the defenderSecurityCenterDisableClearTpmUI property.
        """
        self._defender_security_center_disable_clear_tpm_u_i = value
    
    @property
    def defender_security_center_disable_family_u_i(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterDisableFamilyUI property value. Used to disable the display of the family options area.
        Returns: Optional[bool]
        """
        return self._defender_security_center_disable_family_u_i
    
    @defender_security_center_disable_family_u_i.setter
    def defender_security_center_disable_family_u_i(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterDisableFamilyUI property value. Used to disable the display of the family options area.
        Args:
            value: Value to set for the defenderSecurityCenterDisableFamilyUI property.
        """
        self._defender_security_center_disable_family_u_i = value
    
    @property
    def defender_security_center_disable_hardware_u_i(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterDisableHardwareUI property value. Used to disable the display of the hardware protection area.
        Returns: Optional[bool]
        """
        return self._defender_security_center_disable_hardware_u_i
    
    @defender_security_center_disable_hardware_u_i.setter
    def defender_security_center_disable_hardware_u_i(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterDisableHardwareUI property value. Used to disable the display of the hardware protection area.
        Args:
            value: Value to set for the defenderSecurityCenterDisableHardwareUI property.
        """
        self._defender_security_center_disable_hardware_u_i = value
    
    @property
    def defender_security_center_disable_health_u_i(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterDisableHealthUI property value. Used to disable the display of the device performance and health area.
        Returns: Optional[bool]
        """
        return self._defender_security_center_disable_health_u_i
    
    @defender_security_center_disable_health_u_i.setter
    def defender_security_center_disable_health_u_i(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterDisableHealthUI property value. Used to disable the display of the device performance and health area.
        Args:
            value: Value to set for the defenderSecurityCenterDisableHealthUI property.
        """
        self._defender_security_center_disable_health_u_i = value
    
    @property
    def defender_security_center_disable_network_u_i(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterDisableNetworkUI property value. Used to disable the display of the firewall and network protection area.
        Returns: Optional[bool]
        """
        return self._defender_security_center_disable_network_u_i
    
    @defender_security_center_disable_network_u_i.setter
    def defender_security_center_disable_network_u_i(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterDisableNetworkUI property value. Used to disable the display of the firewall and network protection area.
        Args:
            value: Value to set for the defenderSecurityCenterDisableNetworkUI property.
        """
        self._defender_security_center_disable_network_u_i = value
    
    @property
    def defender_security_center_disable_notification_area_u_i(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterDisableNotificationAreaUI property value. Used to disable the display of the notification area control. The user needs to either sign out and sign in or reboot the computer for this setting to take effect.
        Returns: Optional[bool]
        """
        return self._defender_security_center_disable_notification_area_u_i
    
    @defender_security_center_disable_notification_area_u_i.setter
    def defender_security_center_disable_notification_area_u_i(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterDisableNotificationAreaUI property value. Used to disable the display of the notification area control. The user needs to either sign out and sign in or reboot the computer for this setting to take effect.
        Args:
            value: Value to set for the defenderSecurityCenterDisableNotificationAreaUI property.
        """
        self._defender_security_center_disable_notification_area_u_i = value
    
    @property
    def defender_security_center_disable_ransomware_u_i(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterDisableRansomwareUI property value. Used to disable the display of the ransomware protection area.
        Returns: Optional[bool]
        """
        return self._defender_security_center_disable_ransomware_u_i
    
    @defender_security_center_disable_ransomware_u_i.setter
    def defender_security_center_disable_ransomware_u_i(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterDisableRansomwareUI property value. Used to disable the display of the ransomware protection area.
        Args:
            value: Value to set for the defenderSecurityCenterDisableRansomwareUI property.
        """
        self._defender_security_center_disable_ransomware_u_i = value
    
    @property
    def defender_security_center_disable_secure_boot_u_i(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterDisableSecureBootUI property value. Used to disable the display of the secure boot area under Device security.
        Returns: Optional[bool]
        """
        return self._defender_security_center_disable_secure_boot_u_i
    
    @defender_security_center_disable_secure_boot_u_i.setter
    def defender_security_center_disable_secure_boot_u_i(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterDisableSecureBootUI property value. Used to disable the display of the secure boot area under Device security.
        Args:
            value: Value to set for the defenderSecurityCenterDisableSecureBootUI property.
        """
        self._defender_security_center_disable_secure_boot_u_i = value
    
    @property
    def defender_security_center_disable_troubleshooting_u_i(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterDisableTroubleshootingUI property value. Used to disable the display of the security process troubleshooting under Device security.
        Returns: Optional[bool]
        """
        return self._defender_security_center_disable_troubleshooting_u_i
    
    @defender_security_center_disable_troubleshooting_u_i.setter
    def defender_security_center_disable_troubleshooting_u_i(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterDisableTroubleshootingUI property value. Used to disable the display of the security process troubleshooting under Device security.
        Args:
            value: Value to set for the defenderSecurityCenterDisableTroubleshootingUI property.
        """
        self._defender_security_center_disable_troubleshooting_u_i = value
    
    @property
    def defender_security_center_disable_virus_u_i(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterDisableVirusUI property value. Used to disable the display of the virus and threat protection area.
        Returns: Optional[bool]
        """
        return self._defender_security_center_disable_virus_u_i
    
    @defender_security_center_disable_virus_u_i.setter
    def defender_security_center_disable_virus_u_i(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterDisableVirusUI property value. Used to disable the display of the virus and threat protection area.
        Args:
            value: Value to set for the defenderSecurityCenterDisableVirusUI property.
        """
        self._defender_security_center_disable_virus_u_i = value
    
    @property
    def defender_security_center_disable_vulnerable_tpm_firmware_update_u_i(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterDisableVulnerableTpmFirmwareUpdateUI property value. Used to disable the display of update TPM Firmware when a vulnerable firmware is detected.
        Returns: Optional[bool]
        """
        return self._defender_security_center_disable_vulnerable_tpm_firmware_update_u_i
    
    @defender_security_center_disable_vulnerable_tpm_firmware_update_u_i.setter
    def defender_security_center_disable_vulnerable_tpm_firmware_update_u_i(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterDisableVulnerableTpmFirmwareUpdateUI property value. Used to disable the display of update TPM Firmware when a vulnerable firmware is detected.
        Args:
            value: Value to set for the defenderSecurityCenterDisableVulnerableTpmFirmwareUpdateUI property.
        """
        self._defender_security_center_disable_vulnerable_tpm_firmware_update_u_i = value
    
    @property
    def defender_security_center_help_email(self,) -> Optional[str]:
        """
        Gets the defenderSecurityCenterHelpEmail property value. The email address that is displayed to users.
        Returns: Optional[str]
        """
        return self._defender_security_center_help_email
    
    @defender_security_center_help_email.setter
    def defender_security_center_help_email(self,value: Optional[str] = None) -> None:
        """
        Sets the defenderSecurityCenterHelpEmail property value. The email address that is displayed to users.
        Args:
            value: Value to set for the defenderSecurityCenterHelpEmail property.
        """
        self._defender_security_center_help_email = value
    
    @property
    def defender_security_center_help_phone(self,) -> Optional[str]:
        """
        Gets the defenderSecurityCenterHelpPhone property value. The phone number or Skype ID that is displayed to users.
        Returns: Optional[str]
        """
        return self._defender_security_center_help_phone
    
    @defender_security_center_help_phone.setter
    def defender_security_center_help_phone(self,value: Optional[str] = None) -> None:
        """
        Sets the defenderSecurityCenterHelpPhone property value. The phone number or Skype ID that is displayed to users.
        Args:
            value: Value to set for the defenderSecurityCenterHelpPhone property.
        """
        self._defender_security_center_help_phone = value
    
    @property
    def defender_security_center_help_u_r_l(self,) -> Optional[str]:
        """
        Gets the defenderSecurityCenterHelpURL property value. The help portal URL this is displayed to users.
        Returns: Optional[str]
        """
        return self._defender_security_center_help_u_r_l
    
    @defender_security_center_help_u_r_l.setter
    def defender_security_center_help_u_r_l(self,value: Optional[str] = None) -> None:
        """
        Sets the defenderSecurityCenterHelpURL property value. The help portal URL this is displayed to users.
        Args:
            value: Value to set for the defenderSecurityCenterHelpURL property.
        """
        self._defender_security_center_help_u_r_l = value
    
    @property
    def defender_security_center_i_t_contact_display(self,) -> Optional[defender_security_center_i_t_contact_display_type.DefenderSecurityCenterITContactDisplayType]:
        """
        Gets the defenderSecurityCenterITContactDisplay property value. Possible values for defenderSecurityCenterITContactDisplay
        Returns: Optional[defender_security_center_i_t_contact_display_type.DefenderSecurityCenterITContactDisplayType]
        """
        return self._defender_security_center_i_t_contact_display
    
    @defender_security_center_i_t_contact_display.setter
    def defender_security_center_i_t_contact_display(self,value: Optional[defender_security_center_i_t_contact_display_type.DefenderSecurityCenterITContactDisplayType] = None) -> None:
        """
        Sets the defenderSecurityCenterITContactDisplay property value. Possible values for defenderSecurityCenterITContactDisplay
        Args:
            value: Value to set for the defenderSecurityCenterITContactDisplay property.
        """
        self._defender_security_center_i_t_contact_display = value
    
    @property
    def defender_security_center_notifications_from_app(self,) -> Optional[defender_security_center_notifications_from_app_type.DefenderSecurityCenterNotificationsFromAppType]:
        """
        Gets the defenderSecurityCenterNotificationsFromApp property value. Possible values for defenderSecurityCenterNotificationsFromApp
        Returns: Optional[defender_security_center_notifications_from_app_type.DefenderSecurityCenterNotificationsFromAppType]
        """
        return self._defender_security_center_notifications_from_app
    
    @defender_security_center_notifications_from_app.setter
    def defender_security_center_notifications_from_app(self,value: Optional[defender_security_center_notifications_from_app_type.DefenderSecurityCenterNotificationsFromAppType] = None) -> None:
        """
        Sets the defenderSecurityCenterNotificationsFromApp property value. Possible values for defenderSecurityCenterNotificationsFromApp
        Args:
            value: Value to set for the defenderSecurityCenterNotificationsFromApp property.
        """
        self._defender_security_center_notifications_from_app = value
    
    @property
    def defender_security_center_organization_display_name(self,) -> Optional[str]:
        """
        Gets the defenderSecurityCenterOrganizationDisplayName property value. The company name that is displayed to the users.
        Returns: Optional[str]
        """
        return self._defender_security_center_organization_display_name
    
    @defender_security_center_organization_display_name.setter
    def defender_security_center_organization_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the defenderSecurityCenterOrganizationDisplayName property value. The company name that is displayed to the users.
        Args:
            value: Value to set for the defenderSecurityCenterOrganizationDisplayName property.
        """
        self._defender_security_center_organization_display_name = value
    
    @property
    def defender_signature_update_interval_in_hours(self,) -> Optional[int]:
        """
        Gets the defenderSignatureUpdateIntervalInHours property value. Specifies the interval (in hours) that will be used to check for signatures, so instead of using the ScheduleDay and ScheduleTime the check for new signatures will be set according to the interval. Valid values 0 to 24
        Returns: Optional[int]
        """
        return self._defender_signature_update_interval_in_hours
    
    @defender_signature_update_interval_in_hours.setter
    def defender_signature_update_interval_in_hours(self,value: Optional[int] = None) -> None:
        """
        Sets the defenderSignatureUpdateIntervalInHours property value. Specifies the interval (in hours) that will be used to check for signatures, so instead of using the ScheduleDay and ScheduleTime the check for new signatures will be set according to the interval. Valid values 0 to 24
        Args:
            value: Value to set for the defenderSignatureUpdateIntervalInHours property.
        """
        self._defender_signature_update_interval_in_hours = value
    
    @property
    def defender_submit_samples_consent_type(self,) -> Optional[defender_submit_samples_consent_type.DefenderSubmitSamplesConsentType]:
        """
        Gets the defenderSubmitSamplesConsentType property value. Checks for the user consent level in Windows Defender to send data. Possible values are: sendSafeSamplesAutomatically, alwaysPrompt, neverSend, sendAllSamplesAutomatically.
        Returns: Optional[defender_submit_samples_consent_type.DefenderSubmitSamplesConsentType]
        """
        return self._defender_submit_samples_consent_type
    
    @defender_submit_samples_consent_type.setter
    def defender_submit_samples_consent_type(self,value: Optional[defender_submit_samples_consent_type.DefenderSubmitSamplesConsentType] = None) -> None:
        """
        Sets the defenderSubmitSamplesConsentType property value. Checks for the user consent level in Windows Defender to send data. Possible values are: sendSafeSamplesAutomatically, alwaysPrompt, neverSend, sendAllSamplesAutomatically.
        Args:
            value: Value to set for the defenderSubmitSamplesConsentType property.
        """
        self._defender_submit_samples_consent_type = value
    
    @property
    def defender_untrusted_executable(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderUntrustedExecutable property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_untrusted_executable
    
    @defender_untrusted_executable.setter
    def defender_untrusted_executable(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderUntrustedExecutable property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderUntrustedExecutable property.
        """
        self._defender_untrusted_executable = value
    
    @property
    def defender_untrusted_executable_type(self,) -> Optional[defender_attack_surface_type.DefenderAttackSurfaceType]:
        """
        Gets the defenderUntrustedExecutableType property value. Possible values of Defender Attack Surface Reduction Rules
        Returns: Optional[defender_attack_surface_type.DefenderAttackSurfaceType]
        """
        return self._defender_untrusted_executable_type
    
    @defender_untrusted_executable_type.setter
    def defender_untrusted_executable_type(self,value: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None) -> None:
        """
        Sets the defenderUntrustedExecutableType property value. Possible values of Defender Attack Surface Reduction Rules
        Args:
            value: Value to set for the defenderUntrustedExecutableType property.
        """
        self._defender_untrusted_executable_type = value
    
    @property
    def defender_untrusted_u_s_b_process(self,) -> Optional[defender_protection_type.DefenderProtectionType]:
        """
        Gets the defenderUntrustedUSBProcess property value. Possible values of Defender PUA Protection
        Returns: Optional[defender_protection_type.DefenderProtectionType]
        """
        return self._defender_untrusted_u_s_b_process
    
    @defender_untrusted_u_s_b_process.setter
    def defender_untrusted_u_s_b_process(self,value: Optional[defender_protection_type.DefenderProtectionType] = None) -> None:
        """
        Sets the defenderUntrustedUSBProcess property value. Possible values of Defender PUA Protection
        Args:
            value: Value to set for the defenderUntrustedUSBProcess property.
        """
        self._defender_untrusted_u_s_b_process = value
    
    @property
    def defender_untrusted_u_s_b_process_type(self,) -> Optional[defender_attack_surface_type.DefenderAttackSurfaceType]:
        """
        Gets the defenderUntrustedUSBProcessType property value. Possible values of Defender Attack Surface Reduction Rules
        Returns: Optional[defender_attack_surface_type.DefenderAttackSurfaceType]
        """
        return self._defender_untrusted_u_s_b_process_type
    
    @defender_untrusted_u_s_b_process_type.setter
    def defender_untrusted_u_s_b_process_type(self,value: Optional[defender_attack_surface_type.DefenderAttackSurfaceType] = None) -> None:
        """
        Sets the defenderUntrustedUSBProcessType property value. Possible values of Defender Attack Surface Reduction Rules
        Args:
            value: Value to set for the defenderUntrustedUSBProcessType property.
        """
        self._defender_untrusted_u_s_b_process_type = value
    
    @property
    def device_guard_enable_secure_boot_with_d_m_a(self,) -> Optional[bool]:
        """
        Gets the deviceGuardEnableSecureBootWithDMA property value. This property will be deprecated in May 2019 and will be replaced with property DeviceGuardSecureBootWithDMA. Specifies whether Platform Security Level is enabled at next reboot.
        Returns: Optional[bool]
        """
        return self._device_guard_enable_secure_boot_with_d_m_a
    
    @device_guard_enable_secure_boot_with_d_m_a.setter
    def device_guard_enable_secure_boot_with_d_m_a(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceGuardEnableSecureBootWithDMA property value. This property will be deprecated in May 2019 and will be replaced with property DeviceGuardSecureBootWithDMA. Specifies whether Platform Security Level is enabled at next reboot.
        Args:
            value: Value to set for the deviceGuardEnableSecureBootWithDMA property.
        """
        self._device_guard_enable_secure_boot_with_d_m_a = value
    
    @property
    def device_guard_enable_virtualization_based_security(self,) -> Optional[bool]:
        """
        Gets the deviceGuardEnableVirtualizationBasedSecurity property value. Turns On Virtualization Based Security(VBS).
        Returns: Optional[bool]
        """
        return self._device_guard_enable_virtualization_based_security
    
    @device_guard_enable_virtualization_based_security.setter
    def device_guard_enable_virtualization_based_security(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceGuardEnableVirtualizationBasedSecurity property value. Turns On Virtualization Based Security(VBS).
        Args:
            value: Value to set for the deviceGuardEnableVirtualizationBasedSecurity property.
        """
        self._device_guard_enable_virtualization_based_security = value
    
    @property
    def device_guard_launch_system_guard(self,) -> Optional[enablement.Enablement]:
        """
        Gets the deviceGuardLaunchSystemGuard property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._device_guard_launch_system_guard
    
    @device_guard_launch_system_guard.setter
    def device_guard_launch_system_guard(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the deviceGuardLaunchSystemGuard property value. Possible values of a property
        Args:
            value: Value to set for the deviceGuardLaunchSystemGuard property.
        """
        self._device_guard_launch_system_guard = value
    
    @property
    def device_guard_local_system_authority_credential_guard_settings(self,) -> Optional[device_guard_local_system_authority_credential_guard_type.DeviceGuardLocalSystemAuthorityCredentialGuardType]:
        """
        Gets the deviceGuardLocalSystemAuthorityCredentialGuardSettings property value. Possible values of Credential Guard settings.
        Returns: Optional[device_guard_local_system_authority_credential_guard_type.DeviceGuardLocalSystemAuthorityCredentialGuardType]
        """
        return self._device_guard_local_system_authority_credential_guard_settings
    
    @device_guard_local_system_authority_credential_guard_settings.setter
    def device_guard_local_system_authority_credential_guard_settings(self,value: Optional[device_guard_local_system_authority_credential_guard_type.DeviceGuardLocalSystemAuthorityCredentialGuardType] = None) -> None:
        """
        Sets the deviceGuardLocalSystemAuthorityCredentialGuardSettings property value. Possible values of Credential Guard settings.
        Args:
            value: Value to set for the deviceGuardLocalSystemAuthorityCredentialGuardSettings property.
        """
        self._device_guard_local_system_authority_credential_guard_settings = value
    
    @property
    def device_guard_secure_boot_with_d_m_a(self,) -> Optional[secure_boot_with_d_m_a_type.SecureBootWithDMAType]:
        """
        Gets the deviceGuardSecureBootWithDMA property value. Possible values of Secure Boot with DMA
        Returns: Optional[secure_boot_with_d_m_a_type.SecureBootWithDMAType]
        """
        return self._device_guard_secure_boot_with_d_m_a
    
    @device_guard_secure_boot_with_d_m_a.setter
    def device_guard_secure_boot_with_d_m_a(self,value: Optional[secure_boot_with_d_m_a_type.SecureBootWithDMAType] = None) -> None:
        """
        Sets the deviceGuardSecureBootWithDMA property value. Possible values of Secure Boot with DMA
        Args:
            value: Value to set for the deviceGuardSecureBootWithDMA property.
        """
        self._device_guard_secure_boot_with_d_m_a = value
    
    @property
    def dma_guard_device_enumeration_policy(self,) -> Optional[dma_guard_device_enumeration_policy_type.DmaGuardDeviceEnumerationPolicyType]:
        """
        Gets the dmaGuardDeviceEnumerationPolicy property value. Possible values of the DmaGuardDeviceEnumerationPolicy.
        Returns: Optional[dma_guard_device_enumeration_policy_type.DmaGuardDeviceEnumerationPolicyType]
        """
        return self._dma_guard_device_enumeration_policy
    
    @dma_guard_device_enumeration_policy.setter
    def dma_guard_device_enumeration_policy(self,value: Optional[dma_guard_device_enumeration_policy_type.DmaGuardDeviceEnumerationPolicyType] = None) -> None:
        """
        Sets the dmaGuardDeviceEnumerationPolicy property value. Possible values of the DmaGuardDeviceEnumerationPolicy.
        Args:
            value: Value to set for the dmaGuardDeviceEnumerationPolicy property.
        """
        self._dma_guard_device_enumeration_policy = value
    
    @property
    def firewall_block_stateful_f_t_p(self,) -> Optional[bool]:
        """
        Gets the firewallBlockStatefulFTP property value. Blocks stateful FTP connections to the device
        Returns: Optional[bool]
        """
        return self._firewall_block_stateful_f_t_p
    
    @firewall_block_stateful_f_t_p.setter
    def firewall_block_stateful_f_t_p(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallBlockStatefulFTP property value. Blocks stateful FTP connections to the device
        Args:
            value: Value to set for the firewallBlockStatefulFTP property.
        """
        self._firewall_block_stateful_f_t_p = value
    
    @property
    def firewall_certificate_revocation_list_check_method(self,) -> Optional[firewall_certificate_revocation_list_check_method_type.FirewallCertificateRevocationListCheckMethodType]:
        """
        Gets the firewallCertificateRevocationListCheckMethod property value. Possible values for firewallCertificateRevocationListCheckMethod
        Returns: Optional[firewall_certificate_revocation_list_check_method_type.FirewallCertificateRevocationListCheckMethodType]
        """
        return self._firewall_certificate_revocation_list_check_method
    
    @firewall_certificate_revocation_list_check_method.setter
    def firewall_certificate_revocation_list_check_method(self,value: Optional[firewall_certificate_revocation_list_check_method_type.FirewallCertificateRevocationListCheckMethodType] = None) -> None:
        """
        Sets the firewallCertificateRevocationListCheckMethod property value. Possible values for firewallCertificateRevocationListCheckMethod
        Args:
            value: Value to set for the firewallCertificateRevocationListCheckMethod property.
        """
        self._firewall_certificate_revocation_list_check_method = value
    
    @property
    def firewall_idle_timeout_for_security_association_in_seconds(self,) -> Optional[int]:
        """
        Gets the firewallIdleTimeoutForSecurityAssociationInSeconds property value. Configures the idle timeout for security associations, in seconds, from 300 to 3600 inclusive. This is the period after which security associations will expire and be deleted. Valid values 300 to 3600
        Returns: Optional[int]
        """
        return self._firewall_idle_timeout_for_security_association_in_seconds
    
    @firewall_idle_timeout_for_security_association_in_seconds.setter
    def firewall_idle_timeout_for_security_association_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the firewallIdleTimeoutForSecurityAssociationInSeconds property value. Configures the idle timeout for security associations, in seconds, from 300 to 3600 inclusive. This is the period after which security associations will expire and be deleted. Valid values 300 to 3600
        Args:
            value: Value to set for the firewallIdleTimeoutForSecurityAssociationInSeconds property.
        """
        self._firewall_idle_timeout_for_security_association_in_seconds = value
    
    @property
    def firewall_i_p_sec_exemptions_allow_d_h_c_p(self,) -> Optional[bool]:
        """
        Gets the firewallIPSecExemptionsAllowDHCP property value. Configures IPSec exemptions to allow both IPv4 and IPv6 DHCP traffic
        Returns: Optional[bool]
        """
        return self._firewall_i_p_sec_exemptions_allow_d_h_c_p
    
    @firewall_i_p_sec_exemptions_allow_d_h_c_p.setter
    def firewall_i_p_sec_exemptions_allow_d_h_c_p(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallIPSecExemptionsAllowDHCP property value. Configures IPSec exemptions to allow both IPv4 and IPv6 DHCP traffic
        Args:
            value: Value to set for the firewallIPSecExemptionsAllowDHCP property.
        """
        self._firewall_i_p_sec_exemptions_allow_d_h_c_p = value
    
    @property
    def firewall_i_p_sec_exemptions_allow_i_c_m_p(self,) -> Optional[bool]:
        """
        Gets the firewallIPSecExemptionsAllowICMP property value. Configures IPSec exemptions to allow ICMP
        Returns: Optional[bool]
        """
        return self._firewall_i_p_sec_exemptions_allow_i_c_m_p
    
    @firewall_i_p_sec_exemptions_allow_i_c_m_p.setter
    def firewall_i_p_sec_exemptions_allow_i_c_m_p(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallIPSecExemptionsAllowICMP property value. Configures IPSec exemptions to allow ICMP
        Args:
            value: Value to set for the firewallIPSecExemptionsAllowICMP property.
        """
        self._firewall_i_p_sec_exemptions_allow_i_c_m_p = value
    
    @property
    def firewall_i_p_sec_exemptions_allow_neighbor_discovery(self,) -> Optional[bool]:
        """
        Gets the firewallIPSecExemptionsAllowNeighborDiscovery property value. Configures IPSec exemptions to allow neighbor discovery IPv6 ICMP type-codes
        Returns: Optional[bool]
        """
        return self._firewall_i_p_sec_exemptions_allow_neighbor_discovery
    
    @firewall_i_p_sec_exemptions_allow_neighbor_discovery.setter
    def firewall_i_p_sec_exemptions_allow_neighbor_discovery(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallIPSecExemptionsAllowNeighborDiscovery property value. Configures IPSec exemptions to allow neighbor discovery IPv6 ICMP type-codes
        Args:
            value: Value to set for the firewallIPSecExemptionsAllowNeighborDiscovery property.
        """
        self._firewall_i_p_sec_exemptions_allow_neighbor_discovery = value
    
    @property
    def firewall_i_p_sec_exemptions_allow_router_discovery(self,) -> Optional[bool]:
        """
        Gets the firewallIPSecExemptionsAllowRouterDiscovery property value. Configures IPSec exemptions to allow router discovery IPv6 ICMP type-codes
        Returns: Optional[bool]
        """
        return self._firewall_i_p_sec_exemptions_allow_router_discovery
    
    @firewall_i_p_sec_exemptions_allow_router_discovery.setter
    def firewall_i_p_sec_exemptions_allow_router_discovery(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallIPSecExemptionsAllowRouterDiscovery property value. Configures IPSec exemptions to allow router discovery IPv6 ICMP type-codes
        Args:
            value: Value to set for the firewallIPSecExemptionsAllowRouterDiscovery property.
        """
        self._firewall_i_p_sec_exemptions_allow_router_discovery = value
    
    @property
    def firewall_i_p_sec_exemptions_none(self,) -> Optional[bool]:
        """
        Gets the firewallIPSecExemptionsNone property value. Configures IPSec exemptions to no exemptions
        Returns: Optional[bool]
        """
        return self._firewall_i_p_sec_exemptions_none
    
    @firewall_i_p_sec_exemptions_none.setter
    def firewall_i_p_sec_exemptions_none(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallIPSecExemptionsNone property value. Configures IPSec exemptions to no exemptions
        Args:
            value: Value to set for the firewallIPSecExemptionsNone property.
        """
        self._firewall_i_p_sec_exemptions_none = value
    
    @property
    def firewall_merge_keying_module_settings(self,) -> Optional[bool]:
        """
        Gets the firewallMergeKeyingModuleSettings property value. If an authentication set is not fully supported by a keying module, direct the module to ignore only unsupported authentication suites rather than the entire set
        Returns: Optional[bool]
        """
        return self._firewall_merge_keying_module_settings
    
    @firewall_merge_keying_module_settings.setter
    def firewall_merge_keying_module_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallMergeKeyingModuleSettings property value. If an authentication set is not fully supported by a keying module, direct the module to ignore only unsupported authentication suites rather than the entire set
        Args:
            value: Value to set for the firewallMergeKeyingModuleSettings property.
        """
        self._firewall_merge_keying_module_settings = value
    
    @property
    def firewall_packet_queueing_method(self,) -> Optional[firewall_packet_queueing_method_type.FirewallPacketQueueingMethodType]:
        """
        Gets the firewallPacketQueueingMethod property value. Possible values for firewallPacketQueueingMethod
        Returns: Optional[firewall_packet_queueing_method_type.FirewallPacketQueueingMethodType]
        """
        return self._firewall_packet_queueing_method
    
    @firewall_packet_queueing_method.setter
    def firewall_packet_queueing_method(self,value: Optional[firewall_packet_queueing_method_type.FirewallPacketQueueingMethodType] = None) -> None:
        """
        Sets the firewallPacketQueueingMethod property value. Possible values for firewallPacketQueueingMethod
        Args:
            value: Value to set for the firewallPacketQueueingMethod property.
        """
        self._firewall_packet_queueing_method = value
    
    @property
    def firewall_pre_shared_key_encoding_method(self,) -> Optional[firewall_pre_shared_key_encoding_method_type.FirewallPreSharedKeyEncodingMethodType]:
        """
        Gets the firewallPreSharedKeyEncodingMethod property value. Possible values for firewallPreSharedKeyEncodingMethod
        Returns: Optional[firewall_pre_shared_key_encoding_method_type.FirewallPreSharedKeyEncodingMethodType]
        """
        return self._firewall_pre_shared_key_encoding_method
    
    @firewall_pre_shared_key_encoding_method.setter
    def firewall_pre_shared_key_encoding_method(self,value: Optional[firewall_pre_shared_key_encoding_method_type.FirewallPreSharedKeyEncodingMethodType] = None) -> None:
        """
        Sets the firewallPreSharedKeyEncodingMethod property value. Possible values for firewallPreSharedKeyEncodingMethod
        Args:
            value: Value to set for the firewallPreSharedKeyEncodingMethod property.
        """
        self._firewall_pre_shared_key_encoding_method = value
    
    @property
    def firewall_profile_domain(self,) -> Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile]:
        """
        Gets the firewallProfileDomain property value. Configures the firewall profile settings for domain networks
        Returns: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile]
        """
        return self._firewall_profile_domain
    
    @firewall_profile_domain.setter
    def firewall_profile_domain(self,value: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile] = None) -> None:
        """
        Sets the firewallProfileDomain property value. Configures the firewall profile settings for domain networks
        Args:
            value: Value to set for the firewallProfileDomain property.
        """
        self._firewall_profile_domain = value
    
    @property
    def firewall_profile_private(self,) -> Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile]:
        """
        Gets the firewallProfilePrivate property value. Configures the firewall profile settings for private networks
        Returns: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile]
        """
        return self._firewall_profile_private
    
    @firewall_profile_private.setter
    def firewall_profile_private(self,value: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile] = None) -> None:
        """
        Sets the firewallProfilePrivate property value. Configures the firewall profile settings for private networks
        Args:
            value: Value to set for the firewallProfilePrivate property.
        """
        self._firewall_profile_private = value
    
    @property
    def firewall_profile_public(self,) -> Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile]:
        """
        Gets the firewallProfilePublic property value. Configures the firewall profile settings for public networks
        Returns: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile]
        """
        return self._firewall_profile_public
    
    @firewall_profile_public.setter
    def firewall_profile_public(self,value: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile] = None) -> None:
        """
        Sets the firewallProfilePublic property value. Configures the firewall profile settings for public networks
        Args:
            value: Value to set for the firewallProfilePublic property.
        """
        self._firewall_profile_public = value
    
    @property
    def firewall_rules(self,) -> Optional[List[windows_firewall_rule.WindowsFirewallRule]]:
        """
        Gets the firewallRules property value. Configures the firewall rule settings. This collection can contain a maximum of 150 elements.
        Returns: Optional[List[windows_firewall_rule.WindowsFirewallRule]]
        """
        return self._firewall_rules
    
    @firewall_rules.setter
    def firewall_rules(self,value: Optional[List[windows_firewall_rule.WindowsFirewallRule]] = None) -> None:
        """
        Sets the firewallRules property value. Configures the firewall rule settings. This collection can contain a maximum of 150 elements.
        Args:
            value: Value to set for the firewallRules property.
        """
        self._firewall_rules = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_guard_allow_camera_microphone_redirection": lambda n : setattr(self, 'application_guard_allow_camera_microphone_redirection', n.get_bool_value()),
            "application_guard_allow_file_save_on_host": lambda n : setattr(self, 'application_guard_allow_file_save_on_host', n.get_bool_value()),
            "application_guard_allow_persistence": lambda n : setattr(self, 'application_guard_allow_persistence', n.get_bool_value()),
            "application_guard_allow_print_to_local_printers": lambda n : setattr(self, 'application_guard_allow_print_to_local_printers', n.get_bool_value()),
            "application_guard_allow_print_to_network_printers": lambda n : setattr(self, 'application_guard_allow_print_to_network_printers', n.get_bool_value()),
            "application_guard_allow_print_to_p_d_f": lambda n : setattr(self, 'application_guard_allow_print_to_p_d_f', n.get_bool_value()),
            "application_guard_allow_print_to_x_p_s": lambda n : setattr(self, 'application_guard_allow_print_to_x_p_s', n.get_bool_value()),
            "application_guard_allow_virtual_g_p_u": lambda n : setattr(self, 'application_guard_allow_virtual_g_p_u', n.get_bool_value()),
            "application_guard_block_clipboard_sharing": lambda n : setattr(self, 'application_guard_block_clipboard_sharing', n.get_enum_value(application_guard_block_clipboard_sharing_type.ApplicationGuardBlockClipboardSharingType)),
            "application_guard_block_file_transfer": lambda n : setattr(self, 'application_guard_block_file_transfer', n.get_enum_value(application_guard_block_file_transfer_type.ApplicationGuardBlockFileTransferType)),
            "application_guard_block_non_enterprise_content": lambda n : setattr(self, 'application_guard_block_non_enterprise_content', n.get_bool_value()),
            "application_guard_certificate_thumbprints": lambda n : setattr(self, 'application_guard_certificate_thumbprints', n.get_collection_of_primitive_values(str)),
            "application_guard_enabled": lambda n : setattr(self, 'application_guard_enabled', n.get_bool_value()),
            "application_guard_enabled_options": lambda n : setattr(self, 'application_guard_enabled_options', n.get_enum_value(application_guard_enabled_options.ApplicationGuardEnabledOptions)),
            "application_guard_force_auditing": lambda n : setattr(self, 'application_guard_force_auditing', n.get_bool_value()),
            "app_locker_application_control": lambda n : setattr(self, 'app_locker_application_control', n.get_enum_value(app_locker_application_control_type.AppLockerApplicationControlType)),
            "bit_locker_allow_standard_user_encryption": lambda n : setattr(self, 'bit_locker_allow_standard_user_encryption', n.get_bool_value()),
            "bit_locker_disable_warning_for_other_disk_encryption": lambda n : setattr(self, 'bit_locker_disable_warning_for_other_disk_encryption', n.get_bool_value()),
            "bit_locker_enable_storage_card_encryption_on_mobile": lambda n : setattr(self, 'bit_locker_enable_storage_card_encryption_on_mobile', n.get_bool_value()),
            "bit_locker_encrypt_device": lambda n : setattr(self, 'bit_locker_encrypt_device', n.get_bool_value()),
            "bit_locker_fixed_drive_policy": lambda n : setattr(self, 'bit_locker_fixed_drive_policy', n.get_object_value(bit_locker_fixed_drive_policy.BitLockerFixedDrivePolicy)),
            "bit_locker_recovery_password_rotation": lambda n : setattr(self, 'bit_locker_recovery_password_rotation', n.get_enum_value(bit_locker_recovery_password_rotation_type.BitLockerRecoveryPasswordRotationType)),
            "bit_locker_removable_drive_policy": lambda n : setattr(self, 'bit_locker_removable_drive_policy', n.get_object_value(bit_locker_removable_drive_policy.BitLockerRemovableDrivePolicy)),
            "bit_locker_system_drive_policy": lambda n : setattr(self, 'bit_locker_system_drive_policy', n.get_object_value(bit_locker_system_drive_policy.BitLockerSystemDrivePolicy)),
            "defender_additional_guarded_folders": lambda n : setattr(self, 'defender_additional_guarded_folders', n.get_collection_of_primitive_values(str)),
            "defender_adobe_reader_launch_child_process": lambda n : setattr(self, 'defender_adobe_reader_launch_child_process', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_advanced_ransomeware_protection_type": lambda n : setattr(self, 'defender_advanced_ransomeware_protection_type', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_allow_behavior_monitoring": lambda n : setattr(self, 'defender_allow_behavior_monitoring', n.get_bool_value()),
            "defender_allow_cloud_protection": lambda n : setattr(self, 'defender_allow_cloud_protection', n.get_bool_value()),
            "defender_allow_end_user_access": lambda n : setattr(self, 'defender_allow_end_user_access', n.get_bool_value()),
            "defender_allow_intrusion_prevention_system": lambda n : setattr(self, 'defender_allow_intrusion_prevention_system', n.get_bool_value()),
            "defender_allow_on_access_protection": lambda n : setattr(self, 'defender_allow_on_access_protection', n.get_bool_value()),
            "defender_allow_real_time_monitoring": lambda n : setattr(self, 'defender_allow_real_time_monitoring', n.get_bool_value()),
            "defender_allow_scan_archive_files": lambda n : setattr(self, 'defender_allow_scan_archive_files', n.get_bool_value()),
            "defender_allow_scan_downloads": lambda n : setattr(self, 'defender_allow_scan_downloads', n.get_bool_value()),
            "defender_allow_scan_network_files": lambda n : setattr(self, 'defender_allow_scan_network_files', n.get_bool_value()),
            "defender_allow_scan_removable_drives_during_full_scan": lambda n : setattr(self, 'defender_allow_scan_removable_drives_during_full_scan', n.get_bool_value()),
            "defender_allow_scan_scripts_loaded_in_internet_explorer": lambda n : setattr(self, 'defender_allow_scan_scripts_loaded_in_internet_explorer', n.get_bool_value()),
            "defender_attack_surface_reduction_excluded_paths": lambda n : setattr(self, 'defender_attack_surface_reduction_excluded_paths', n.get_collection_of_primitive_values(str)),
            "defender_block_end_user_access": lambda n : setattr(self, 'defender_block_end_user_access', n.get_bool_value()),
            "defender_block_persistence_through_wmi_type": lambda n : setattr(self, 'defender_block_persistence_through_wmi_type', n.get_enum_value(defender_attack_surface_type.DefenderAttackSurfaceType)),
            "defender_check_for_signatures_before_running_scan": lambda n : setattr(self, 'defender_check_for_signatures_before_running_scan', n.get_bool_value()),
            "defender_cloud_block_level": lambda n : setattr(self, 'defender_cloud_block_level', n.get_enum_value(defender_cloud_block_level_type.DefenderCloudBlockLevelType)),
            "defender_cloud_extended_timeout_in_seconds": lambda n : setattr(self, 'defender_cloud_extended_timeout_in_seconds', n.get_int_value()),
            "defender_days_before_deleting_quarantined_malware": lambda n : setattr(self, 'defender_days_before_deleting_quarantined_malware', n.get_int_value()),
            "defender_detected_malware_actions": lambda n : setattr(self, 'defender_detected_malware_actions', n.get_object_value(defender_detected_malware_actions.DefenderDetectedMalwareActions)),
            "defender_disable_behavior_monitoring": lambda n : setattr(self, 'defender_disable_behavior_monitoring', n.get_bool_value()),
            "defender_disable_catchup_full_scan": lambda n : setattr(self, 'defender_disable_catchup_full_scan', n.get_bool_value()),
            "defender_disable_catchup_quick_scan": lambda n : setattr(self, 'defender_disable_catchup_quick_scan', n.get_bool_value()),
            "defender_disable_cloud_protection": lambda n : setattr(self, 'defender_disable_cloud_protection', n.get_bool_value()),
            "defender_disable_intrusion_prevention_system": lambda n : setattr(self, 'defender_disable_intrusion_prevention_system', n.get_bool_value()),
            "defender_disable_on_access_protection": lambda n : setattr(self, 'defender_disable_on_access_protection', n.get_bool_value()),
            "defender_disable_real_time_monitoring": lambda n : setattr(self, 'defender_disable_real_time_monitoring', n.get_bool_value()),
            "defender_disable_scan_archive_files": lambda n : setattr(self, 'defender_disable_scan_archive_files', n.get_bool_value()),
            "defender_disable_scan_downloads": lambda n : setattr(self, 'defender_disable_scan_downloads', n.get_bool_value()),
            "defender_disable_scan_network_files": lambda n : setattr(self, 'defender_disable_scan_network_files', n.get_bool_value()),
            "defender_disable_scan_removable_drives_during_full_scan": lambda n : setattr(self, 'defender_disable_scan_removable_drives_during_full_scan', n.get_bool_value()),
            "defender_disable_scan_scripts_loaded_in_internet_explorer": lambda n : setattr(self, 'defender_disable_scan_scripts_loaded_in_internet_explorer', n.get_bool_value()),
            "defender_email_content_execution": lambda n : setattr(self, 'defender_email_content_execution', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_email_content_execution_type": lambda n : setattr(self, 'defender_email_content_execution_type', n.get_enum_value(defender_attack_surface_type.DefenderAttackSurfaceType)),
            "defender_enable_low_cpu_priority": lambda n : setattr(self, 'defender_enable_low_cpu_priority', n.get_bool_value()),
            "defender_enable_scan_incoming_mail": lambda n : setattr(self, 'defender_enable_scan_incoming_mail', n.get_bool_value()),
            "defender_enable_scan_mapped_network_drives_during_full_scan": lambda n : setattr(self, 'defender_enable_scan_mapped_network_drives_during_full_scan', n.get_bool_value()),
            "defender_exploit_protection_xml": lambda n : setattr(self, 'defender_exploit_protection_xml', n.get_bytes_value()),
            "defender_exploit_protection_xml_file_name": lambda n : setattr(self, 'defender_exploit_protection_xml_file_name', n.get_str_value()),
            "defender_file_extensions_to_exclude": lambda n : setattr(self, 'defender_file_extensions_to_exclude', n.get_collection_of_primitive_values(str)),
            "defender_files_and_folders_to_exclude": lambda n : setattr(self, 'defender_files_and_folders_to_exclude', n.get_collection_of_primitive_values(str)),
            "defender_guarded_folders_allowed_app_paths": lambda n : setattr(self, 'defender_guarded_folders_allowed_app_paths', n.get_collection_of_primitive_values(str)),
            "defender_guard_my_folders_type": lambda n : setattr(self, 'defender_guard_my_folders_type', n.get_enum_value(folder_protection_type.FolderProtectionType)),
            "defender_network_protection_type": lambda n : setattr(self, 'defender_network_protection_type', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_office_apps_executable_content_creation_or_launch": lambda n : setattr(self, 'defender_office_apps_executable_content_creation_or_launch', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_office_apps_executable_content_creation_or_launch_type": lambda n : setattr(self, 'defender_office_apps_executable_content_creation_or_launch_type', n.get_enum_value(defender_attack_surface_type.DefenderAttackSurfaceType)),
            "defender_office_apps_launch_child_process": lambda n : setattr(self, 'defender_office_apps_launch_child_process', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_office_apps_launch_child_process_type": lambda n : setattr(self, 'defender_office_apps_launch_child_process_type', n.get_enum_value(defender_attack_surface_type.DefenderAttackSurfaceType)),
            "defender_office_apps_other_process_injection": lambda n : setattr(self, 'defender_office_apps_other_process_injection', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_office_apps_other_process_injection_type": lambda n : setattr(self, 'defender_office_apps_other_process_injection_type', n.get_enum_value(defender_attack_surface_type.DefenderAttackSurfaceType)),
            "defender_office_communication_apps_launch_child_process": lambda n : setattr(self, 'defender_office_communication_apps_launch_child_process', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_office_macro_code_allow_win32_imports": lambda n : setattr(self, 'defender_office_macro_code_allow_win32_imports', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_office_macro_code_allow_win32_imports_type": lambda n : setattr(self, 'defender_office_macro_code_allow_win32_imports_type', n.get_enum_value(defender_attack_surface_type.DefenderAttackSurfaceType)),
            "defender_potentially_unwanted_app_action": lambda n : setattr(self, 'defender_potentially_unwanted_app_action', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_prevent_credential_stealing_type": lambda n : setattr(self, 'defender_prevent_credential_stealing_type', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_process_creation": lambda n : setattr(self, 'defender_process_creation', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_process_creation_type": lambda n : setattr(self, 'defender_process_creation_type', n.get_enum_value(defender_attack_surface_type.DefenderAttackSurfaceType)),
            "defender_processes_to_exclude": lambda n : setattr(self, 'defender_processes_to_exclude', n.get_collection_of_primitive_values(str)),
            "defender_scan_direction": lambda n : setattr(self, 'defender_scan_direction', n.get_enum_value(defender_realtime_scan_direction.DefenderRealtimeScanDirection)),
            "defender_scan_max_cpu_percentage": lambda n : setattr(self, 'defender_scan_max_cpu_percentage', n.get_int_value()),
            "defender_scan_type": lambda n : setattr(self, 'defender_scan_type', n.get_enum_value(defender_scan_type.DefenderScanType)),
            "defender_scheduled_quick_scan_time": lambda n : setattr(self, 'defender_scheduled_quick_scan_time', n.get_object_value(Time)),
            "defender_scheduled_scan_day": lambda n : setattr(self, 'defender_scheduled_scan_day', n.get_enum_value(weekly_schedule.WeeklySchedule)),
            "defender_scheduled_scan_time": lambda n : setattr(self, 'defender_scheduled_scan_time', n.get_object_value(Time)),
            "defender_script_downloaded_payload_execution": lambda n : setattr(self, 'defender_script_downloaded_payload_execution', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_script_downloaded_payload_execution_type": lambda n : setattr(self, 'defender_script_downloaded_payload_execution_type', n.get_enum_value(defender_attack_surface_type.DefenderAttackSurfaceType)),
            "defender_script_obfuscated_macro_code": lambda n : setattr(self, 'defender_script_obfuscated_macro_code', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_script_obfuscated_macro_code_type": lambda n : setattr(self, 'defender_script_obfuscated_macro_code_type', n.get_enum_value(defender_attack_surface_type.DefenderAttackSurfaceType)),
            "defender_security_center_block_exploit_protection_override": lambda n : setattr(self, 'defender_security_center_block_exploit_protection_override', n.get_bool_value()),
            "defender_security_center_disable_account_u_i": lambda n : setattr(self, 'defender_security_center_disable_account_u_i', n.get_bool_value()),
            "defender_security_center_disable_app_browser_u_i": lambda n : setattr(self, 'defender_security_center_disable_app_browser_u_i', n.get_bool_value()),
            "defender_security_center_disable_clear_tpm_u_i": lambda n : setattr(self, 'defender_security_center_disable_clear_tpm_u_i', n.get_bool_value()),
            "defender_security_center_disable_family_u_i": lambda n : setattr(self, 'defender_security_center_disable_family_u_i', n.get_bool_value()),
            "defender_security_center_disable_hardware_u_i": lambda n : setattr(self, 'defender_security_center_disable_hardware_u_i', n.get_bool_value()),
            "defender_security_center_disable_health_u_i": lambda n : setattr(self, 'defender_security_center_disable_health_u_i', n.get_bool_value()),
            "defender_security_center_disable_network_u_i": lambda n : setattr(self, 'defender_security_center_disable_network_u_i', n.get_bool_value()),
            "defender_security_center_disable_notification_area_u_i": lambda n : setattr(self, 'defender_security_center_disable_notification_area_u_i', n.get_bool_value()),
            "defender_security_center_disable_ransomware_u_i": lambda n : setattr(self, 'defender_security_center_disable_ransomware_u_i', n.get_bool_value()),
            "defender_security_center_disable_secure_boot_u_i": lambda n : setattr(self, 'defender_security_center_disable_secure_boot_u_i', n.get_bool_value()),
            "defender_security_center_disable_troubleshooting_u_i": lambda n : setattr(self, 'defender_security_center_disable_troubleshooting_u_i', n.get_bool_value()),
            "defender_security_center_disable_virus_u_i": lambda n : setattr(self, 'defender_security_center_disable_virus_u_i', n.get_bool_value()),
            "defender_security_center_disable_vulnerable_tpm_firmware_update_u_i": lambda n : setattr(self, 'defender_security_center_disable_vulnerable_tpm_firmware_update_u_i', n.get_bool_value()),
            "defender_security_center_help_email": lambda n : setattr(self, 'defender_security_center_help_email', n.get_str_value()),
            "defender_security_center_help_phone": lambda n : setattr(self, 'defender_security_center_help_phone', n.get_str_value()),
            "defender_security_center_help_u_r_l": lambda n : setattr(self, 'defender_security_center_help_u_r_l', n.get_str_value()),
            "defender_security_center_i_t_contact_display": lambda n : setattr(self, 'defender_security_center_i_t_contact_display', n.get_enum_value(defender_security_center_i_t_contact_display_type.DefenderSecurityCenterITContactDisplayType)),
            "defender_security_center_notifications_from_app": lambda n : setattr(self, 'defender_security_center_notifications_from_app', n.get_enum_value(defender_security_center_notifications_from_app_type.DefenderSecurityCenterNotificationsFromAppType)),
            "defender_security_center_organization_display_name": lambda n : setattr(self, 'defender_security_center_organization_display_name', n.get_str_value()),
            "defender_signature_update_interval_in_hours": lambda n : setattr(self, 'defender_signature_update_interval_in_hours', n.get_int_value()),
            "defender_submit_samples_consent_type": lambda n : setattr(self, 'defender_submit_samples_consent_type', n.get_enum_value(defender_submit_samples_consent_type.DefenderSubmitSamplesConsentType)),
            "defender_untrusted_executable": lambda n : setattr(self, 'defender_untrusted_executable', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_untrusted_executable_type": lambda n : setattr(self, 'defender_untrusted_executable_type', n.get_enum_value(defender_attack_surface_type.DefenderAttackSurfaceType)),
            "defender_untrusted_u_s_b_process": lambda n : setattr(self, 'defender_untrusted_u_s_b_process', n.get_enum_value(defender_protection_type.DefenderProtectionType)),
            "defender_untrusted_u_s_b_process_type": lambda n : setattr(self, 'defender_untrusted_u_s_b_process_type', n.get_enum_value(defender_attack_surface_type.DefenderAttackSurfaceType)),
            "device_guard_enable_secure_boot_with_d_m_a": lambda n : setattr(self, 'device_guard_enable_secure_boot_with_d_m_a', n.get_bool_value()),
            "device_guard_enable_virtualization_based_security": lambda n : setattr(self, 'device_guard_enable_virtualization_based_security', n.get_bool_value()),
            "device_guard_launch_system_guard": lambda n : setattr(self, 'device_guard_launch_system_guard', n.get_enum_value(enablement.Enablement)),
            "device_guard_local_system_authority_credential_guard_settings": lambda n : setattr(self, 'device_guard_local_system_authority_credential_guard_settings', n.get_enum_value(device_guard_local_system_authority_credential_guard_type.DeviceGuardLocalSystemAuthorityCredentialGuardType)),
            "device_guard_secure_boot_with_d_m_a": lambda n : setattr(self, 'device_guard_secure_boot_with_d_m_a', n.get_enum_value(secure_boot_with_d_m_a_type.SecureBootWithDMAType)),
            "dma_guard_device_enumeration_policy": lambda n : setattr(self, 'dma_guard_device_enumeration_policy', n.get_enum_value(dma_guard_device_enumeration_policy_type.DmaGuardDeviceEnumerationPolicyType)),
            "firewall_block_stateful_f_t_p": lambda n : setattr(self, 'firewall_block_stateful_f_t_p', n.get_bool_value()),
            "firewall_certificate_revocation_list_check_method": lambda n : setattr(self, 'firewall_certificate_revocation_list_check_method', n.get_enum_value(firewall_certificate_revocation_list_check_method_type.FirewallCertificateRevocationListCheckMethodType)),
            "firewall_idle_timeout_for_security_association_in_seconds": lambda n : setattr(self, 'firewall_idle_timeout_for_security_association_in_seconds', n.get_int_value()),
            "firewall_i_p_sec_exemptions_allow_d_h_c_p": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_d_h_c_p', n.get_bool_value()),
            "firewall_i_p_sec_exemptions_allow_i_c_m_p": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_i_c_m_p', n.get_bool_value()),
            "firewall_i_p_sec_exemptions_allow_neighbor_discovery": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_neighbor_discovery', n.get_bool_value()),
            "firewall_i_p_sec_exemptions_allow_router_discovery": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_router_discovery', n.get_bool_value()),
            "firewall_i_p_sec_exemptions_none": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_none', n.get_bool_value()),
            "firewall_merge_keying_module_settings": lambda n : setattr(self, 'firewall_merge_keying_module_settings', n.get_bool_value()),
            "firewall_packet_queueing_method": lambda n : setattr(self, 'firewall_packet_queueing_method', n.get_enum_value(firewall_packet_queueing_method_type.FirewallPacketQueueingMethodType)),
            "firewall_pre_shared_key_encoding_method": lambda n : setattr(self, 'firewall_pre_shared_key_encoding_method', n.get_enum_value(firewall_pre_shared_key_encoding_method_type.FirewallPreSharedKeyEncodingMethodType)),
            "firewall_profile_domain": lambda n : setattr(self, 'firewall_profile_domain', n.get_object_value(windows_firewall_network_profile.WindowsFirewallNetworkProfile)),
            "firewall_profile_private": lambda n : setattr(self, 'firewall_profile_private', n.get_object_value(windows_firewall_network_profile.WindowsFirewallNetworkProfile)),
            "firewall_profile_public": lambda n : setattr(self, 'firewall_profile_public', n.get_object_value(windows_firewall_network_profile.WindowsFirewallNetworkProfile)),
            "firewall_rules": lambda n : setattr(self, 'firewall_rules', n.get_collection_of_object_values(windows_firewall_rule.WindowsFirewallRule)),
            "lan_manager_authentication_level": lambda n : setattr(self, 'lan_manager_authentication_level', n.get_enum_value(lan_manager_authentication_level.LanManagerAuthenticationLevel)),
            "lan_manager_workstation_disable_insecure_guest_logons": lambda n : setattr(self, 'lan_manager_workstation_disable_insecure_guest_logons', n.get_bool_value()),
            "local_security_options_administrator_account_name": lambda n : setattr(self, 'local_security_options_administrator_account_name', n.get_str_value()),
            "local_security_options_administrator_elevation_prompt_behavior": lambda n : setattr(self, 'local_security_options_administrator_elevation_prompt_behavior', n.get_enum_value(local_security_options_administrator_elevation_prompt_behavior_type.LocalSecurityOptionsAdministratorElevationPromptBehaviorType)),
            "local_security_options_allow_anonymous_enumeration_of_s_a_m_accounts_and_shares": lambda n : setattr(self, 'local_security_options_allow_anonymous_enumeration_of_s_a_m_accounts_and_shares', n.get_bool_value()),
            "local_security_options_allow_p_k_u2_u_authentication_requests": lambda n : setattr(self, 'local_security_options_allow_p_k_u2_u_authentication_requests', n.get_bool_value()),
            "local_security_options_allow_remote_calls_to_security_accounts_manager": lambda n : setattr(self, 'local_security_options_allow_remote_calls_to_security_accounts_manager', n.get_str_value()),
            "local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool": lambda n : setattr(self, 'local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool', n.get_bool_value()),
            "local_security_options_allow_system_to_be_shut_down_without_having_to_log_on": lambda n : setattr(self, 'local_security_options_allow_system_to_be_shut_down_without_having_to_log_on', n.get_bool_value()),
            "local_security_options_allow_u_i_access_application_elevation": lambda n : setattr(self, 'local_security_options_allow_u_i_access_application_elevation', n.get_bool_value()),
            "local_security_options_allow_u_i_access_applications_for_secure_locations": lambda n : setattr(self, 'local_security_options_allow_u_i_access_applications_for_secure_locations', n.get_bool_value()),
            "local_security_options_allow_undock_without_having_to_logon": lambda n : setattr(self, 'local_security_options_allow_undock_without_having_to_logon', n.get_bool_value()),
            "local_security_options_block_microsoft_accounts": lambda n : setattr(self, 'local_security_options_block_microsoft_accounts', n.get_bool_value()),
            "local_security_options_block_remote_logon_with_blank_password": lambda n : setattr(self, 'local_security_options_block_remote_logon_with_blank_password', n.get_bool_value()),
            "local_security_options_block_remote_optical_drive_access": lambda n : setattr(self, 'local_security_options_block_remote_optical_drive_access', n.get_bool_value()),
            "local_security_options_block_users_installing_printer_drivers": lambda n : setattr(self, 'local_security_options_block_users_installing_printer_drivers', n.get_bool_value()),
            "local_security_options_clear_virtual_memory_page_file": lambda n : setattr(self, 'local_security_options_clear_virtual_memory_page_file', n.get_bool_value()),
            "local_security_options_client_digitally_sign_communications_always": lambda n : setattr(self, 'local_security_options_client_digitally_sign_communications_always', n.get_bool_value()),
            "local_security_options_client_send_unencrypted_password_to_third_party_s_m_b_servers": lambda n : setattr(self, 'local_security_options_client_send_unencrypted_password_to_third_party_s_m_b_servers', n.get_bool_value()),
            "local_security_options_detect_application_installations_and_prompt_for_elevation": lambda n : setattr(self, 'local_security_options_detect_application_installations_and_prompt_for_elevation', n.get_bool_value()),
            "local_security_options_disable_administrator_account": lambda n : setattr(self, 'local_security_options_disable_administrator_account', n.get_bool_value()),
            "local_security_options_disable_client_digitally_sign_communications_if_server_agrees": lambda n : setattr(self, 'local_security_options_disable_client_digitally_sign_communications_if_server_agrees', n.get_bool_value()),
            "local_security_options_disable_guest_account": lambda n : setattr(self, 'local_security_options_disable_guest_account', n.get_bool_value()),
            "local_security_options_disable_server_digitally_sign_communications_always": lambda n : setattr(self, 'local_security_options_disable_server_digitally_sign_communications_always', n.get_bool_value()),
            "local_security_options_disable_server_digitally_sign_communications_if_client_agrees": lambda n : setattr(self, 'local_security_options_disable_server_digitally_sign_communications_if_client_agrees', n.get_bool_value()),
            "local_security_options_do_not_allow_anonymous_enumeration_of_s_a_m_accounts": lambda n : setattr(self, 'local_security_options_do_not_allow_anonymous_enumeration_of_s_a_m_accounts', n.get_bool_value()),
            "local_security_options_do_not_require_ctrl_alt_del": lambda n : setattr(self, 'local_security_options_do_not_require_ctrl_alt_del', n.get_bool_value()),
            "local_security_options_do_not_store_l_a_n_manager_hash_value_on_next_password_change": lambda n : setattr(self, 'local_security_options_do_not_store_l_a_n_manager_hash_value_on_next_password_change', n.get_bool_value()),
            "local_security_options_format_and_eject_of_removable_media_allowed_user": lambda n : setattr(self, 'local_security_options_format_and_eject_of_removable_media_allowed_user', n.get_enum_value(local_security_options_format_and_eject_of_removable_media_allowed_user_type.LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType)),
            "local_security_options_guest_account_name": lambda n : setattr(self, 'local_security_options_guest_account_name', n.get_str_value()),
            "local_security_options_hide_last_signed_in_user": lambda n : setattr(self, 'local_security_options_hide_last_signed_in_user', n.get_bool_value()),
            "local_security_options_hide_username_at_sign_in": lambda n : setattr(self, 'local_security_options_hide_username_at_sign_in', n.get_bool_value()),
            "local_security_options_information_displayed_on_lock_screen": lambda n : setattr(self, 'local_security_options_information_displayed_on_lock_screen', n.get_enum_value(local_security_options_information_displayed_on_lock_screen_type.LocalSecurityOptionsInformationDisplayedOnLockScreenType)),
            "local_security_options_information_shown_on_lock_screen": lambda n : setattr(self, 'local_security_options_information_shown_on_lock_screen', n.get_enum_value(local_security_options_information_shown_on_lock_screen_type.LocalSecurityOptionsInformationShownOnLockScreenType)),
            "local_security_options_log_on_message_text": lambda n : setattr(self, 'local_security_options_log_on_message_text', n.get_str_value()),
            "local_security_options_log_on_message_title": lambda n : setattr(self, 'local_security_options_log_on_message_title', n.get_str_value()),
            "local_security_options_machine_inactivity_limit": lambda n : setattr(self, 'local_security_options_machine_inactivity_limit', n.get_int_value()),
            "local_security_options_machine_inactivity_limit_in_minutes": lambda n : setattr(self, 'local_security_options_machine_inactivity_limit_in_minutes', n.get_int_value()),
            "local_security_options_minimum_session_security_for_ntlm_ssp_based_clients": lambda n : setattr(self, 'local_security_options_minimum_session_security_for_ntlm_ssp_based_clients', n.get_enum_value(local_security_options_minimum_session_security.LocalSecurityOptionsMinimumSessionSecurity)),
            "local_security_options_minimum_session_security_for_ntlm_ssp_based_servers": lambda n : setattr(self, 'local_security_options_minimum_session_security_for_ntlm_ssp_based_servers', n.get_enum_value(local_security_options_minimum_session_security.LocalSecurityOptionsMinimumSessionSecurity)),
            "local_security_options_only_elevate_signed_executables": lambda n : setattr(self, 'local_security_options_only_elevate_signed_executables', n.get_bool_value()),
            "local_security_options_restrict_anonymous_access_to_named_pipes_and_shares": lambda n : setattr(self, 'local_security_options_restrict_anonymous_access_to_named_pipes_and_shares', n.get_bool_value()),
            "local_security_options_smart_card_removal_behavior": lambda n : setattr(self, 'local_security_options_smart_card_removal_behavior', n.get_enum_value(local_security_options_smart_card_removal_behavior_type.LocalSecurityOptionsSmartCardRemovalBehaviorType)),
            "local_security_options_standard_user_elevation_prompt_behavior": lambda n : setattr(self, 'local_security_options_standard_user_elevation_prompt_behavior', n.get_enum_value(local_security_options_standard_user_elevation_prompt_behavior_type.LocalSecurityOptionsStandardUserElevationPromptBehaviorType)),
            "local_security_options_switch_to_secure_desktop_when_prompting_for_elevation": lambda n : setattr(self, 'local_security_options_switch_to_secure_desktop_when_prompting_for_elevation', n.get_bool_value()),
            "local_security_options_use_admin_approval_mode": lambda n : setattr(self, 'local_security_options_use_admin_approval_mode', n.get_bool_value()),
            "local_security_options_use_admin_approval_mode_for_administrators": lambda n : setattr(self, 'local_security_options_use_admin_approval_mode_for_administrators', n.get_bool_value()),
            "local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations": lambda n : setattr(self, 'local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations', n.get_bool_value()),
            "smart_screen_block_override_for_files": lambda n : setattr(self, 'smart_screen_block_override_for_files', n.get_bool_value()),
            "smart_screen_enable_in_shell": lambda n : setattr(self, 'smart_screen_enable_in_shell', n.get_bool_value()),
            "user_rights_access_credential_manager_as_trusted_caller": lambda n : setattr(self, 'user_rights_access_credential_manager_as_trusted_caller', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_act_as_part_of_the_operating_system": lambda n : setattr(self, 'user_rights_act_as_part_of_the_operating_system', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_allow_access_from_network": lambda n : setattr(self, 'user_rights_allow_access_from_network', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_backup_data": lambda n : setattr(self, 'user_rights_backup_data', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_block_access_from_network": lambda n : setattr(self, 'user_rights_block_access_from_network', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_change_system_time": lambda n : setattr(self, 'user_rights_change_system_time', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_create_global_objects": lambda n : setattr(self, 'user_rights_create_global_objects', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_create_page_file": lambda n : setattr(self, 'user_rights_create_page_file', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_create_permanent_shared_objects": lambda n : setattr(self, 'user_rights_create_permanent_shared_objects', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_create_symbolic_links": lambda n : setattr(self, 'user_rights_create_symbolic_links', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_create_token": lambda n : setattr(self, 'user_rights_create_token', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_debug_programs": lambda n : setattr(self, 'user_rights_debug_programs', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_delegation": lambda n : setattr(self, 'user_rights_delegation', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_deny_local_log_on": lambda n : setattr(self, 'user_rights_deny_local_log_on', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_generate_security_audits": lambda n : setattr(self, 'user_rights_generate_security_audits', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_impersonate_client": lambda n : setattr(self, 'user_rights_impersonate_client', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_increase_scheduling_priority": lambda n : setattr(self, 'user_rights_increase_scheduling_priority', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_load_unload_drivers": lambda n : setattr(self, 'user_rights_load_unload_drivers', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_local_log_on": lambda n : setattr(self, 'user_rights_local_log_on', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_lock_memory": lambda n : setattr(self, 'user_rights_lock_memory', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_manage_auditing_and_security_logs": lambda n : setattr(self, 'user_rights_manage_auditing_and_security_logs', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_manage_volumes": lambda n : setattr(self, 'user_rights_manage_volumes', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_modify_firmware_environment": lambda n : setattr(self, 'user_rights_modify_firmware_environment', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_modify_object_labels": lambda n : setattr(self, 'user_rights_modify_object_labels', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_profile_single_process": lambda n : setattr(self, 'user_rights_profile_single_process', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_remote_desktop_services_log_on": lambda n : setattr(self, 'user_rights_remote_desktop_services_log_on', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_remote_shutdown": lambda n : setattr(self, 'user_rights_remote_shutdown', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_restore_data": lambda n : setattr(self, 'user_rights_restore_data', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "user_rights_take_ownership": lambda n : setattr(self, 'user_rights_take_ownership', n.get_object_value(device_management_user_rights_setting.DeviceManagementUserRightsSetting)),
            "windows_defender_tamper_protection": lambda n : setattr(self, 'windows_defender_tamper_protection', n.get_enum_value(windows_defender_tamper_protection_options.WindowsDefenderTamperProtectionOptions)),
            "xbox_services_accessory_management_service_startup_mode": lambda n : setattr(self, 'xbox_services_accessory_management_service_startup_mode', n.get_enum_value(service_start_type.ServiceStartType)),
            "xbox_services_enable_xbox_game_save_task": lambda n : setattr(self, 'xbox_services_enable_xbox_game_save_task', n.get_bool_value()),
            "xbox_services_live_auth_manager_service_startup_mode": lambda n : setattr(self, 'xbox_services_live_auth_manager_service_startup_mode', n.get_enum_value(service_start_type.ServiceStartType)),
            "xbox_services_live_game_save_service_startup_mode": lambda n : setattr(self, 'xbox_services_live_game_save_service_startup_mode', n.get_enum_value(service_start_type.ServiceStartType)),
            "xbox_services_live_networking_service_startup_mode": lambda n : setattr(self, 'xbox_services_live_networking_service_startup_mode', n.get_enum_value(service_start_type.ServiceStartType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def lan_manager_authentication_level(self,) -> Optional[lan_manager_authentication_level.LanManagerAuthenticationLevel]:
        """
        Gets the lanManagerAuthenticationLevel property value. Possible values for LanManagerAuthenticationLevel
        Returns: Optional[lan_manager_authentication_level.LanManagerAuthenticationLevel]
        """
        return self._lan_manager_authentication_level
    
    @lan_manager_authentication_level.setter
    def lan_manager_authentication_level(self,value: Optional[lan_manager_authentication_level.LanManagerAuthenticationLevel] = None) -> None:
        """
        Sets the lanManagerAuthenticationLevel property value. Possible values for LanManagerAuthenticationLevel
        Args:
            value: Value to set for the lanManagerAuthenticationLevel property.
        """
        self._lan_manager_authentication_level = value
    
    @property
    def lan_manager_workstation_disable_insecure_guest_logons(self,) -> Optional[bool]:
        """
        Gets the lanManagerWorkstationDisableInsecureGuestLogons property value. If enabled,the SMB client will allow insecure guest logons. If not configured, the SMB client will reject insecure guest logons.
        Returns: Optional[bool]
        """
        return self._lan_manager_workstation_disable_insecure_guest_logons
    
    @lan_manager_workstation_disable_insecure_guest_logons.setter
    def lan_manager_workstation_disable_insecure_guest_logons(self,value: Optional[bool] = None) -> None:
        """
        Sets the lanManagerWorkstationDisableInsecureGuestLogons property value. If enabled,the SMB client will allow insecure guest logons. If not configured, the SMB client will reject insecure guest logons.
        Args:
            value: Value to set for the lanManagerWorkstationDisableInsecureGuestLogons property.
        """
        self._lan_manager_workstation_disable_insecure_guest_logons = value
    
    @property
    def local_security_options_administrator_account_name(self,) -> Optional[str]:
        """
        Gets the localSecurityOptionsAdministratorAccountName property value. Define a different account name to be associated with the security identifier (SID) for the account 'Administrator'.
        Returns: Optional[str]
        """
        return self._local_security_options_administrator_account_name
    
    @local_security_options_administrator_account_name.setter
    def local_security_options_administrator_account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the localSecurityOptionsAdministratorAccountName property value. Define a different account name to be associated with the security identifier (SID) for the account 'Administrator'.
        Args:
            value: Value to set for the localSecurityOptionsAdministratorAccountName property.
        """
        self._local_security_options_administrator_account_name = value
    
    @property
    def local_security_options_administrator_elevation_prompt_behavior(self,) -> Optional[local_security_options_administrator_elevation_prompt_behavior_type.LocalSecurityOptionsAdministratorElevationPromptBehaviorType]:
        """
        Gets the localSecurityOptionsAdministratorElevationPromptBehavior property value. Possible values for LocalSecurityOptionsAdministratorElevationPromptBehavior
        Returns: Optional[local_security_options_administrator_elevation_prompt_behavior_type.LocalSecurityOptionsAdministratorElevationPromptBehaviorType]
        """
        return self._local_security_options_administrator_elevation_prompt_behavior
    
    @local_security_options_administrator_elevation_prompt_behavior.setter
    def local_security_options_administrator_elevation_prompt_behavior(self,value: Optional[local_security_options_administrator_elevation_prompt_behavior_type.LocalSecurityOptionsAdministratorElevationPromptBehaviorType] = None) -> None:
        """
        Sets the localSecurityOptionsAdministratorElevationPromptBehavior property value. Possible values for LocalSecurityOptionsAdministratorElevationPromptBehavior
        Args:
            value: Value to set for the localSecurityOptionsAdministratorElevationPromptBehavior property.
        """
        self._local_security_options_administrator_elevation_prompt_behavior = value
    
    @property
    def local_security_options_allow_anonymous_enumeration_of_s_a_m_accounts_and_shares(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsAllowAnonymousEnumerationOfSAMAccountsAndShares property value. This security setting determines whether to allows anonymous users to perform certain activities, such as enumerating the names of domain accounts and network shares.
        Returns: Optional[bool]
        """
        return self._local_security_options_allow_anonymous_enumeration_of_s_a_m_accounts_and_shares
    
    @local_security_options_allow_anonymous_enumeration_of_s_a_m_accounts_and_shares.setter
    def local_security_options_allow_anonymous_enumeration_of_s_a_m_accounts_and_shares(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsAllowAnonymousEnumerationOfSAMAccountsAndShares property value. This security setting determines whether to allows anonymous users to perform certain activities, such as enumerating the names of domain accounts and network shares.
        Args:
            value: Value to set for the localSecurityOptionsAllowAnonymousEnumerationOfSAMAccountsAndShares property.
        """
        self._local_security_options_allow_anonymous_enumeration_of_s_a_m_accounts_and_shares = value
    
    @property
    def local_security_options_allow_p_k_u2_u_authentication_requests(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsAllowPKU2UAuthenticationRequests property value. Block PKU2U authentication requests to this device to use online identities.
        Returns: Optional[bool]
        """
        return self._local_security_options_allow_p_k_u2_u_authentication_requests
    
    @local_security_options_allow_p_k_u2_u_authentication_requests.setter
    def local_security_options_allow_p_k_u2_u_authentication_requests(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsAllowPKU2UAuthenticationRequests property value. Block PKU2U authentication requests to this device to use online identities.
        Args:
            value: Value to set for the localSecurityOptionsAllowPKU2UAuthenticationRequests property.
        """
        self._local_security_options_allow_p_k_u2_u_authentication_requests = value
    
    @property
    def local_security_options_allow_remote_calls_to_security_accounts_manager(self,) -> Optional[str]:
        """
        Gets the localSecurityOptionsAllowRemoteCallsToSecurityAccountsManager property value. Edit the default Security Descriptor Definition Language string to allow or deny users and groups to make remote calls to the SAM.
        Returns: Optional[str]
        """
        return self._local_security_options_allow_remote_calls_to_security_accounts_manager
    
    @local_security_options_allow_remote_calls_to_security_accounts_manager.setter
    def local_security_options_allow_remote_calls_to_security_accounts_manager(self,value: Optional[str] = None) -> None:
        """
        Sets the localSecurityOptionsAllowRemoteCallsToSecurityAccountsManager property value. Edit the default Security Descriptor Definition Language string to allow or deny users and groups to make remote calls to the SAM.
        Args:
            value: Value to set for the localSecurityOptionsAllowRemoteCallsToSecurityAccountsManager property.
        """
        self._local_security_options_allow_remote_calls_to_security_accounts_manager = value
    
    @property
    def local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsAllowRemoteCallsToSecurityAccountsManagerHelperBool property value. UI helper boolean for LocalSecurityOptionsAllowRemoteCallsToSecurityAccountsManager entity
        Returns: Optional[bool]
        """
        return self._local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool
    
    @local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool.setter
    def local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsAllowRemoteCallsToSecurityAccountsManagerHelperBool property value. UI helper boolean for LocalSecurityOptionsAllowRemoteCallsToSecurityAccountsManager entity
        Args:
            value: Value to set for the localSecurityOptionsAllowRemoteCallsToSecurityAccountsManagerHelperBool property.
        """
        self._local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool = value
    
    @property
    def local_security_options_allow_system_to_be_shut_down_without_having_to_log_on(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsAllowSystemToBeShutDownWithoutHavingToLogOn property value. This security setting determines whether a computer can be shut down without having to log on to Windows.
        Returns: Optional[bool]
        """
        return self._local_security_options_allow_system_to_be_shut_down_without_having_to_log_on
    
    @local_security_options_allow_system_to_be_shut_down_without_having_to_log_on.setter
    def local_security_options_allow_system_to_be_shut_down_without_having_to_log_on(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsAllowSystemToBeShutDownWithoutHavingToLogOn property value. This security setting determines whether a computer can be shut down without having to log on to Windows.
        Args:
            value: Value to set for the localSecurityOptionsAllowSystemToBeShutDownWithoutHavingToLogOn property.
        """
        self._local_security_options_allow_system_to_be_shut_down_without_having_to_log_on = value
    
    @property
    def local_security_options_allow_u_i_access_application_elevation(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsAllowUIAccessApplicationElevation property value. Allow UIAccess apps to prompt for elevation without using the secure desktop.
        Returns: Optional[bool]
        """
        return self._local_security_options_allow_u_i_access_application_elevation
    
    @local_security_options_allow_u_i_access_application_elevation.setter
    def local_security_options_allow_u_i_access_application_elevation(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsAllowUIAccessApplicationElevation property value. Allow UIAccess apps to prompt for elevation without using the secure desktop.
        Args:
            value: Value to set for the localSecurityOptionsAllowUIAccessApplicationElevation property.
        """
        self._local_security_options_allow_u_i_access_application_elevation = value
    
    @property
    def local_security_options_allow_u_i_access_applications_for_secure_locations(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsAllowUIAccessApplicationsForSecureLocations property value. Allow UIAccess apps to prompt for elevation without using the secure desktop.Default is enabled
        Returns: Optional[bool]
        """
        return self._local_security_options_allow_u_i_access_applications_for_secure_locations
    
    @local_security_options_allow_u_i_access_applications_for_secure_locations.setter
    def local_security_options_allow_u_i_access_applications_for_secure_locations(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsAllowUIAccessApplicationsForSecureLocations property value. Allow UIAccess apps to prompt for elevation without using the secure desktop.Default is enabled
        Args:
            value: Value to set for the localSecurityOptionsAllowUIAccessApplicationsForSecureLocations property.
        """
        self._local_security_options_allow_u_i_access_applications_for_secure_locations = value
    
    @property
    def local_security_options_allow_undock_without_having_to_logon(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsAllowUndockWithoutHavingToLogon property value. Prevent a portable computer from being undocked without having to log in.
        Returns: Optional[bool]
        """
        return self._local_security_options_allow_undock_without_having_to_logon
    
    @local_security_options_allow_undock_without_having_to_logon.setter
    def local_security_options_allow_undock_without_having_to_logon(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsAllowUndockWithoutHavingToLogon property value. Prevent a portable computer from being undocked without having to log in.
        Args:
            value: Value to set for the localSecurityOptionsAllowUndockWithoutHavingToLogon property.
        """
        self._local_security_options_allow_undock_without_having_to_logon = value
    
    @property
    def local_security_options_block_microsoft_accounts(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsBlockMicrosoftAccounts property value. Prevent users from adding new Microsoft accounts to this computer.
        Returns: Optional[bool]
        """
        return self._local_security_options_block_microsoft_accounts
    
    @local_security_options_block_microsoft_accounts.setter
    def local_security_options_block_microsoft_accounts(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsBlockMicrosoftAccounts property value. Prevent users from adding new Microsoft accounts to this computer.
        Args:
            value: Value to set for the localSecurityOptionsBlockMicrosoftAccounts property.
        """
        self._local_security_options_block_microsoft_accounts = value
    
    @property
    def local_security_options_block_remote_logon_with_blank_password(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsBlockRemoteLogonWithBlankPassword property value. Enable Local accounts that are not password protected to log on from locations other than the physical device.Default is enabled
        Returns: Optional[bool]
        """
        return self._local_security_options_block_remote_logon_with_blank_password
    
    @local_security_options_block_remote_logon_with_blank_password.setter
    def local_security_options_block_remote_logon_with_blank_password(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsBlockRemoteLogonWithBlankPassword property value. Enable Local accounts that are not password protected to log on from locations other than the physical device.Default is enabled
        Args:
            value: Value to set for the localSecurityOptionsBlockRemoteLogonWithBlankPassword property.
        """
        self._local_security_options_block_remote_logon_with_blank_password = value
    
    @property
    def local_security_options_block_remote_optical_drive_access(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsBlockRemoteOpticalDriveAccess property value. Enabling this settings allows only interactively logged on user to access CD-ROM media.
        Returns: Optional[bool]
        """
        return self._local_security_options_block_remote_optical_drive_access
    
    @local_security_options_block_remote_optical_drive_access.setter
    def local_security_options_block_remote_optical_drive_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsBlockRemoteOpticalDriveAccess property value. Enabling this settings allows only interactively logged on user to access CD-ROM media.
        Args:
            value: Value to set for the localSecurityOptionsBlockRemoteOpticalDriveAccess property.
        """
        self._local_security_options_block_remote_optical_drive_access = value
    
    @property
    def local_security_options_block_users_installing_printer_drivers(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsBlockUsersInstallingPrinterDrivers property value. Restrict installing printer drivers as part of connecting to a shared printer to admins only.
        Returns: Optional[bool]
        """
        return self._local_security_options_block_users_installing_printer_drivers
    
    @local_security_options_block_users_installing_printer_drivers.setter
    def local_security_options_block_users_installing_printer_drivers(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsBlockUsersInstallingPrinterDrivers property value. Restrict installing printer drivers as part of connecting to a shared printer to admins only.
        Args:
            value: Value to set for the localSecurityOptionsBlockUsersInstallingPrinterDrivers property.
        """
        self._local_security_options_block_users_installing_printer_drivers = value
    
    @property
    def local_security_options_clear_virtual_memory_page_file(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsClearVirtualMemoryPageFile property value. This security setting determines whether the virtual memory pagefile is cleared when the system is shut down.
        Returns: Optional[bool]
        """
        return self._local_security_options_clear_virtual_memory_page_file
    
    @local_security_options_clear_virtual_memory_page_file.setter
    def local_security_options_clear_virtual_memory_page_file(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsClearVirtualMemoryPageFile property value. This security setting determines whether the virtual memory pagefile is cleared when the system is shut down.
        Args:
            value: Value to set for the localSecurityOptionsClearVirtualMemoryPageFile property.
        """
        self._local_security_options_clear_virtual_memory_page_file = value
    
    @property
    def local_security_options_client_digitally_sign_communications_always(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsClientDigitallySignCommunicationsAlways property value. This security setting determines whether packet signing is required by the SMB client component.
        Returns: Optional[bool]
        """
        return self._local_security_options_client_digitally_sign_communications_always
    
    @local_security_options_client_digitally_sign_communications_always.setter
    def local_security_options_client_digitally_sign_communications_always(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsClientDigitallySignCommunicationsAlways property value. This security setting determines whether packet signing is required by the SMB client component.
        Args:
            value: Value to set for the localSecurityOptionsClientDigitallySignCommunicationsAlways property.
        """
        self._local_security_options_client_digitally_sign_communications_always = value
    
    @property
    def local_security_options_client_send_unencrypted_password_to_third_party_s_m_b_servers(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsClientSendUnencryptedPasswordToThirdPartySMBServers property value. If this security setting is enabled, the Server Message Block (SMB) redirector is allowed to send plaintext passwords to non-Microsoft SMB servers that do not support password encryption during authentication.
        Returns: Optional[bool]
        """
        return self._local_security_options_client_send_unencrypted_password_to_third_party_s_m_b_servers
    
    @local_security_options_client_send_unencrypted_password_to_third_party_s_m_b_servers.setter
    def local_security_options_client_send_unencrypted_password_to_third_party_s_m_b_servers(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsClientSendUnencryptedPasswordToThirdPartySMBServers property value. If this security setting is enabled, the Server Message Block (SMB) redirector is allowed to send plaintext passwords to non-Microsoft SMB servers that do not support password encryption during authentication.
        Args:
            value: Value to set for the localSecurityOptionsClientSendUnencryptedPasswordToThirdPartySMBServers property.
        """
        self._local_security_options_client_send_unencrypted_password_to_third_party_s_m_b_servers = value
    
    @property
    def local_security_options_detect_application_installations_and_prompt_for_elevation(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsDetectApplicationInstallationsAndPromptForElevation property value. App installations requiring elevated privileges will prompt for admin credentials.Default is enabled
        Returns: Optional[bool]
        """
        return self._local_security_options_detect_application_installations_and_prompt_for_elevation
    
    @local_security_options_detect_application_installations_and_prompt_for_elevation.setter
    def local_security_options_detect_application_installations_and_prompt_for_elevation(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsDetectApplicationInstallationsAndPromptForElevation property value. App installations requiring elevated privileges will prompt for admin credentials.Default is enabled
        Args:
            value: Value to set for the localSecurityOptionsDetectApplicationInstallationsAndPromptForElevation property.
        """
        self._local_security_options_detect_application_installations_and_prompt_for_elevation = value
    
    @property
    def local_security_options_disable_administrator_account(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsDisableAdministratorAccount property value. Determines whether the Local Administrator account is enabled or disabled.
        Returns: Optional[bool]
        """
        return self._local_security_options_disable_administrator_account
    
    @local_security_options_disable_administrator_account.setter
    def local_security_options_disable_administrator_account(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsDisableAdministratorAccount property value. Determines whether the Local Administrator account is enabled or disabled.
        Args:
            value: Value to set for the localSecurityOptionsDisableAdministratorAccount property.
        """
        self._local_security_options_disable_administrator_account = value
    
    @property
    def local_security_options_disable_client_digitally_sign_communications_if_server_agrees(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsDisableClientDigitallySignCommunicationsIfServerAgrees property value. This security setting determines whether the SMB client attempts to negotiate SMB packet signing.
        Returns: Optional[bool]
        """
        return self._local_security_options_disable_client_digitally_sign_communications_if_server_agrees
    
    @local_security_options_disable_client_digitally_sign_communications_if_server_agrees.setter
    def local_security_options_disable_client_digitally_sign_communications_if_server_agrees(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsDisableClientDigitallySignCommunicationsIfServerAgrees property value. This security setting determines whether the SMB client attempts to negotiate SMB packet signing.
        Args:
            value: Value to set for the localSecurityOptionsDisableClientDigitallySignCommunicationsIfServerAgrees property.
        """
        self._local_security_options_disable_client_digitally_sign_communications_if_server_agrees = value
    
    @property
    def local_security_options_disable_guest_account(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsDisableGuestAccount property value. Determines if the Guest account is enabled or disabled.
        Returns: Optional[bool]
        """
        return self._local_security_options_disable_guest_account
    
    @local_security_options_disable_guest_account.setter
    def local_security_options_disable_guest_account(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsDisableGuestAccount property value. Determines if the Guest account is enabled or disabled.
        Args:
            value: Value to set for the localSecurityOptionsDisableGuestAccount property.
        """
        self._local_security_options_disable_guest_account = value
    
    @property
    def local_security_options_disable_server_digitally_sign_communications_always(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsDisableServerDigitallySignCommunicationsAlways property value. This security setting determines whether packet signing is required by the SMB server component.
        Returns: Optional[bool]
        """
        return self._local_security_options_disable_server_digitally_sign_communications_always
    
    @local_security_options_disable_server_digitally_sign_communications_always.setter
    def local_security_options_disable_server_digitally_sign_communications_always(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsDisableServerDigitallySignCommunicationsAlways property value. This security setting determines whether packet signing is required by the SMB server component.
        Args:
            value: Value to set for the localSecurityOptionsDisableServerDigitallySignCommunicationsAlways property.
        """
        self._local_security_options_disable_server_digitally_sign_communications_always = value
    
    @property
    def local_security_options_disable_server_digitally_sign_communications_if_client_agrees(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsDisableServerDigitallySignCommunicationsIfClientAgrees property value. This security setting determines whether the SMB server will negotiate SMB packet signing with clients that request it.
        Returns: Optional[bool]
        """
        return self._local_security_options_disable_server_digitally_sign_communications_if_client_agrees
    
    @local_security_options_disable_server_digitally_sign_communications_if_client_agrees.setter
    def local_security_options_disable_server_digitally_sign_communications_if_client_agrees(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsDisableServerDigitallySignCommunicationsIfClientAgrees property value. This security setting determines whether the SMB server will negotiate SMB packet signing with clients that request it.
        Args:
            value: Value to set for the localSecurityOptionsDisableServerDigitallySignCommunicationsIfClientAgrees property.
        """
        self._local_security_options_disable_server_digitally_sign_communications_if_client_agrees = value
    
    @property
    def local_security_options_do_not_allow_anonymous_enumeration_of_s_a_m_accounts(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsDoNotAllowAnonymousEnumerationOfSAMAccounts property value. This security setting determines what additional permissions will be granted for anonymous connections to the computer.
        Returns: Optional[bool]
        """
        return self._local_security_options_do_not_allow_anonymous_enumeration_of_s_a_m_accounts
    
    @local_security_options_do_not_allow_anonymous_enumeration_of_s_a_m_accounts.setter
    def local_security_options_do_not_allow_anonymous_enumeration_of_s_a_m_accounts(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsDoNotAllowAnonymousEnumerationOfSAMAccounts property value. This security setting determines what additional permissions will be granted for anonymous connections to the computer.
        Args:
            value: Value to set for the localSecurityOptionsDoNotAllowAnonymousEnumerationOfSAMAccounts property.
        """
        self._local_security_options_do_not_allow_anonymous_enumeration_of_s_a_m_accounts = value
    
    @property
    def local_security_options_do_not_require_ctrl_alt_del(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsDoNotRequireCtrlAltDel property value. Require CTRL+ALT+DEL to be pressed before a user can log on.
        Returns: Optional[bool]
        """
        return self._local_security_options_do_not_require_ctrl_alt_del
    
    @local_security_options_do_not_require_ctrl_alt_del.setter
    def local_security_options_do_not_require_ctrl_alt_del(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsDoNotRequireCtrlAltDel property value. Require CTRL+ALT+DEL to be pressed before a user can log on.
        Args:
            value: Value to set for the localSecurityOptionsDoNotRequireCtrlAltDel property.
        """
        self._local_security_options_do_not_require_ctrl_alt_del = value
    
    @property
    def local_security_options_do_not_store_l_a_n_manager_hash_value_on_next_password_change(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsDoNotStoreLANManagerHashValueOnNextPasswordChange property value. This security setting determines if, at the next password change, the LAN Manager (LM) hash value for the new password is stored. It’s not stored by default.
        Returns: Optional[bool]
        """
        return self._local_security_options_do_not_store_l_a_n_manager_hash_value_on_next_password_change
    
    @local_security_options_do_not_store_l_a_n_manager_hash_value_on_next_password_change.setter
    def local_security_options_do_not_store_l_a_n_manager_hash_value_on_next_password_change(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsDoNotStoreLANManagerHashValueOnNextPasswordChange property value. This security setting determines if, at the next password change, the LAN Manager (LM) hash value for the new password is stored. It’s not stored by default.
        Args:
            value: Value to set for the localSecurityOptionsDoNotStoreLANManagerHashValueOnNextPasswordChange property.
        """
        self._local_security_options_do_not_store_l_a_n_manager_hash_value_on_next_password_change = value
    
    @property
    def local_security_options_format_and_eject_of_removable_media_allowed_user(self,) -> Optional[local_security_options_format_and_eject_of_removable_media_allowed_user_type.LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType]:
        """
        Gets the localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser property value. Possible values for LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser
        Returns: Optional[local_security_options_format_and_eject_of_removable_media_allowed_user_type.LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType]
        """
        return self._local_security_options_format_and_eject_of_removable_media_allowed_user
    
    @local_security_options_format_and_eject_of_removable_media_allowed_user.setter
    def local_security_options_format_and_eject_of_removable_media_allowed_user(self,value: Optional[local_security_options_format_and_eject_of_removable_media_allowed_user_type.LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType] = None) -> None:
        """
        Sets the localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser property value. Possible values for LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser
        Args:
            value: Value to set for the localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser property.
        """
        self._local_security_options_format_and_eject_of_removable_media_allowed_user = value
    
    @property
    def local_security_options_guest_account_name(self,) -> Optional[str]:
        """
        Gets the localSecurityOptionsGuestAccountName property value. Define a different account name to be associated with the security identifier (SID) for the account 'Guest'.
        Returns: Optional[str]
        """
        return self._local_security_options_guest_account_name
    
    @local_security_options_guest_account_name.setter
    def local_security_options_guest_account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the localSecurityOptionsGuestAccountName property value. Define a different account name to be associated with the security identifier (SID) for the account 'Guest'.
        Args:
            value: Value to set for the localSecurityOptionsGuestAccountName property.
        """
        self._local_security_options_guest_account_name = value
    
    @property
    def local_security_options_hide_last_signed_in_user(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsHideLastSignedInUser property value. Do not display the username of the last person who signed in on this device.
        Returns: Optional[bool]
        """
        return self._local_security_options_hide_last_signed_in_user
    
    @local_security_options_hide_last_signed_in_user.setter
    def local_security_options_hide_last_signed_in_user(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsHideLastSignedInUser property value. Do not display the username of the last person who signed in on this device.
        Args:
            value: Value to set for the localSecurityOptionsHideLastSignedInUser property.
        """
        self._local_security_options_hide_last_signed_in_user = value
    
    @property
    def local_security_options_hide_username_at_sign_in(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsHideUsernameAtSignIn property value. Do not display the username of the person signing in to this device after credentials are entered and before the device’s desktop is shown.
        Returns: Optional[bool]
        """
        return self._local_security_options_hide_username_at_sign_in
    
    @local_security_options_hide_username_at_sign_in.setter
    def local_security_options_hide_username_at_sign_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsHideUsernameAtSignIn property value. Do not display the username of the person signing in to this device after credentials are entered and before the device’s desktop is shown.
        Args:
            value: Value to set for the localSecurityOptionsHideUsernameAtSignIn property.
        """
        self._local_security_options_hide_username_at_sign_in = value
    
    @property
    def local_security_options_information_displayed_on_lock_screen(self,) -> Optional[local_security_options_information_displayed_on_lock_screen_type.LocalSecurityOptionsInformationDisplayedOnLockScreenType]:
        """
        Gets the localSecurityOptionsInformationDisplayedOnLockScreen property value. Possible values for LocalSecurityOptionsInformationDisplayedOnLockScreen
        Returns: Optional[local_security_options_information_displayed_on_lock_screen_type.LocalSecurityOptionsInformationDisplayedOnLockScreenType]
        """
        return self._local_security_options_information_displayed_on_lock_screen
    
    @local_security_options_information_displayed_on_lock_screen.setter
    def local_security_options_information_displayed_on_lock_screen(self,value: Optional[local_security_options_information_displayed_on_lock_screen_type.LocalSecurityOptionsInformationDisplayedOnLockScreenType] = None) -> None:
        """
        Sets the localSecurityOptionsInformationDisplayedOnLockScreen property value. Possible values for LocalSecurityOptionsInformationDisplayedOnLockScreen
        Args:
            value: Value to set for the localSecurityOptionsInformationDisplayedOnLockScreen property.
        """
        self._local_security_options_information_displayed_on_lock_screen = value
    
    @property
    def local_security_options_information_shown_on_lock_screen(self,) -> Optional[local_security_options_information_shown_on_lock_screen_type.LocalSecurityOptionsInformationShownOnLockScreenType]:
        """
        Gets the localSecurityOptionsInformationShownOnLockScreen property value. Possible values for LocalSecurityOptionsInformationShownOnLockScreenType
        Returns: Optional[local_security_options_information_shown_on_lock_screen_type.LocalSecurityOptionsInformationShownOnLockScreenType]
        """
        return self._local_security_options_information_shown_on_lock_screen
    
    @local_security_options_information_shown_on_lock_screen.setter
    def local_security_options_information_shown_on_lock_screen(self,value: Optional[local_security_options_information_shown_on_lock_screen_type.LocalSecurityOptionsInformationShownOnLockScreenType] = None) -> None:
        """
        Sets the localSecurityOptionsInformationShownOnLockScreen property value. Possible values for LocalSecurityOptionsInformationShownOnLockScreenType
        Args:
            value: Value to set for the localSecurityOptionsInformationShownOnLockScreen property.
        """
        self._local_security_options_information_shown_on_lock_screen = value
    
    @property
    def local_security_options_log_on_message_text(self,) -> Optional[str]:
        """
        Gets the localSecurityOptionsLogOnMessageText property value. Set message text for users attempting to log in.
        Returns: Optional[str]
        """
        return self._local_security_options_log_on_message_text
    
    @local_security_options_log_on_message_text.setter
    def local_security_options_log_on_message_text(self,value: Optional[str] = None) -> None:
        """
        Sets the localSecurityOptionsLogOnMessageText property value. Set message text for users attempting to log in.
        Args:
            value: Value to set for the localSecurityOptionsLogOnMessageText property.
        """
        self._local_security_options_log_on_message_text = value
    
    @property
    def local_security_options_log_on_message_title(self,) -> Optional[str]:
        """
        Gets the localSecurityOptionsLogOnMessageTitle property value. Set message title for users attempting to log in.
        Returns: Optional[str]
        """
        return self._local_security_options_log_on_message_title
    
    @local_security_options_log_on_message_title.setter
    def local_security_options_log_on_message_title(self,value: Optional[str] = None) -> None:
        """
        Sets the localSecurityOptionsLogOnMessageTitle property value. Set message title for users attempting to log in.
        Args:
            value: Value to set for the localSecurityOptionsLogOnMessageTitle property.
        """
        self._local_security_options_log_on_message_title = value
    
    @property
    def local_security_options_machine_inactivity_limit(self,) -> Optional[int]:
        """
        Gets the localSecurityOptionsMachineInactivityLimit property value. Define maximum minutes of inactivity on the interactive desktop’s login screen until the screen saver runs. Valid values 0 to 9999
        Returns: Optional[int]
        """
        return self._local_security_options_machine_inactivity_limit
    
    @local_security_options_machine_inactivity_limit.setter
    def local_security_options_machine_inactivity_limit(self,value: Optional[int] = None) -> None:
        """
        Sets the localSecurityOptionsMachineInactivityLimit property value. Define maximum minutes of inactivity on the interactive desktop’s login screen until the screen saver runs. Valid values 0 to 9999
        Args:
            value: Value to set for the localSecurityOptionsMachineInactivityLimit property.
        """
        self._local_security_options_machine_inactivity_limit = value
    
    @property
    def local_security_options_machine_inactivity_limit_in_minutes(self,) -> Optional[int]:
        """
        Gets the localSecurityOptionsMachineInactivityLimitInMinutes property value. Define maximum minutes of inactivity on the interactive desktop’s login screen until the screen saver runs. Valid values 0 to 9999
        Returns: Optional[int]
        """
        return self._local_security_options_machine_inactivity_limit_in_minutes
    
    @local_security_options_machine_inactivity_limit_in_minutes.setter
    def local_security_options_machine_inactivity_limit_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the localSecurityOptionsMachineInactivityLimitInMinutes property value. Define maximum minutes of inactivity on the interactive desktop’s login screen until the screen saver runs. Valid values 0 to 9999
        Args:
            value: Value to set for the localSecurityOptionsMachineInactivityLimitInMinutes property.
        """
        self._local_security_options_machine_inactivity_limit_in_minutes = value
    
    @property
    def local_security_options_minimum_session_security_for_ntlm_ssp_based_clients(self,) -> Optional[local_security_options_minimum_session_security.LocalSecurityOptionsMinimumSessionSecurity]:
        """
        Gets the localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedClients property value. Possible values for LocalSecurityOptionsMinimumSessionSecurity
        Returns: Optional[local_security_options_minimum_session_security.LocalSecurityOptionsMinimumSessionSecurity]
        """
        return self._local_security_options_minimum_session_security_for_ntlm_ssp_based_clients
    
    @local_security_options_minimum_session_security_for_ntlm_ssp_based_clients.setter
    def local_security_options_minimum_session_security_for_ntlm_ssp_based_clients(self,value: Optional[local_security_options_minimum_session_security.LocalSecurityOptionsMinimumSessionSecurity] = None) -> None:
        """
        Sets the localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedClients property value. Possible values for LocalSecurityOptionsMinimumSessionSecurity
        Args:
            value: Value to set for the localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedClients property.
        """
        self._local_security_options_minimum_session_security_for_ntlm_ssp_based_clients = value
    
    @property
    def local_security_options_minimum_session_security_for_ntlm_ssp_based_servers(self,) -> Optional[local_security_options_minimum_session_security.LocalSecurityOptionsMinimumSessionSecurity]:
        """
        Gets the localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedServers property value. Possible values for LocalSecurityOptionsMinimumSessionSecurity
        Returns: Optional[local_security_options_minimum_session_security.LocalSecurityOptionsMinimumSessionSecurity]
        """
        return self._local_security_options_minimum_session_security_for_ntlm_ssp_based_servers
    
    @local_security_options_minimum_session_security_for_ntlm_ssp_based_servers.setter
    def local_security_options_minimum_session_security_for_ntlm_ssp_based_servers(self,value: Optional[local_security_options_minimum_session_security.LocalSecurityOptionsMinimumSessionSecurity] = None) -> None:
        """
        Sets the localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedServers property value. Possible values for LocalSecurityOptionsMinimumSessionSecurity
        Args:
            value: Value to set for the localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedServers property.
        """
        self._local_security_options_minimum_session_security_for_ntlm_ssp_based_servers = value
    
    @property
    def local_security_options_only_elevate_signed_executables(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsOnlyElevateSignedExecutables property value. Enforce PKI certification path validation for a given executable file before it is permitted to run.
        Returns: Optional[bool]
        """
        return self._local_security_options_only_elevate_signed_executables
    
    @local_security_options_only_elevate_signed_executables.setter
    def local_security_options_only_elevate_signed_executables(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsOnlyElevateSignedExecutables property value. Enforce PKI certification path validation for a given executable file before it is permitted to run.
        Args:
            value: Value to set for the localSecurityOptionsOnlyElevateSignedExecutables property.
        """
        self._local_security_options_only_elevate_signed_executables = value
    
    @property
    def local_security_options_restrict_anonymous_access_to_named_pipes_and_shares(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsRestrictAnonymousAccessToNamedPipesAndShares property value. By default, this security setting restricts anonymous access to shares and pipes to the settings for named pipes that can be accessed anonymously and Shares that can be accessed anonymously
        Returns: Optional[bool]
        """
        return self._local_security_options_restrict_anonymous_access_to_named_pipes_and_shares
    
    @local_security_options_restrict_anonymous_access_to_named_pipes_and_shares.setter
    def local_security_options_restrict_anonymous_access_to_named_pipes_and_shares(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsRestrictAnonymousAccessToNamedPipesAndShares property value. By default, this security setting restricts anonymous access to shares and pipes to the settings for named pipes that can be accessed anonymously and Shares that can be accessed anonymously
        Args:
            value: Value to set for the localSecurityOptionsRestrictAnonymousAccessToNamedPipesAndShares property.
        """
        self._local_security_options_restrict_anonymous_access_to_named_pipes_and_shares = value
    
    @property
    def local_security_options_smart_card_removal_behavior(self,) -> Optional[local_security_options_smart_card_removal_behavior_type.LocalSecurityOptionsSmartCardRemovalBehaviorType]:
        """
        Gets the localSecurityOptionsSmartCardRemovalBehavior property value. Possible values for LocalSecurityOptionsSmartCardRemovalBehaviorType
        Returns: Optional[local_security_options_smart_card_removal_behavior_type.LocalSecurityOptionsSmartCardRemovalBehaviorType]
        """
        return self._local_security_options_smart_card_removal_behavior
    
    @local_security_options_smart_card_removal_behavior.setter
    def local_security_options_smart_card_removal_behavior(self,value: Optional[local_security_options_smart_card_removal_behavior_type.LocalSecurityOptionsSmartCardRemovalBehaviorType] = None) -> None:
        """
        Sets the localSecurityOptionsSmartCardRemovalBehavior property value. Possible values for LocalSecurityOptionsSmartCardRemovalBehaviorType
        Args:
            value: Value to set for the localSecurityOptionsSmartCardRemovalBehavior property.
        """
        self._local_security_options_smart_card_removal_behavior = value
    
    @property
    def local_security_options_standard_user_elevation_prompt_behavior(self,) -> Optional[local_security_options_standard_user_elevation_prompt_behavior_type.LocalSecurityOptionsStandardUserElevationPromptBehaviorType]:
        """
        Gets the localSecurityOptionsStandardUserElevationPromptBehavior property value. Possible values for LocalSecurityOptionsStandardUserElevationPromptBehavior
        Returns: Optional[local_security_options_standard_user_elevation_prompt_behavior_type.LocalSecurityOptionsStandardUserElevationPromptBehaviorType]
        """
        return self._local_security_options_standard_user_elevation_prompt_behavior
    
    @local_security_options_standard_user_elevation_prompt_behavior.setter
    def local_security_options_standard_user_elevation_prompt_behavior(self,value: Optional[local_security_options_standard_user_elevation_prompt_behavior_type.LocalSecurityOptionsStandardUserElevationPromptBehaviorType] = None) -> None:
        """
        Sets the localSecurityOptionsStandardUserElevationPromptBehavior property value. Possible values for LocalSecurityOptionsStandardUserElevationPromptBehavior
        Args:
            value: Value to set for the localSecurityOptionsStandardUserElevationPromptBehavior property.
        """
        self._local_security_options_standard_user_elevation_prompt_behavior = value
    
    @property
    def local_security_options_switch_to_secure_desktop_when_prompting_for_elevation(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsSwitchToSecureDesktopWhenPromptingForElevation property value. Enable all elevation requests to go to the interactive user's desktop rather than the secure desktop. Prompt behavior policy settings for admins and standard users are used.
        Returns: Optional[bool]
        """
        return self._local_security_options_switch_to_secure_desktop_when_prompting_for_elevation
    
    @local_security_options_switch_to_secure_desktop_when_prompting_for_elevation.setter
    def local_security_options_switch_to_secure_desktop_when_prompting_for_elevation(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsSwitchToSecureDesktopWhenPromptingForElevation property value. Enable all elevation requests to go to the interactive user's desktop rather than the secure desktop. Prompt behavior policy settings for admins and standard users are used.
        Args:
            value: Value to set for the localSecurityOptionsSwitchToSecureDesktopWhenPromptingForElevation property.
        """
        self._local_security_options_switch_to_secure_desktop_when_prompting_for_elevation = value
    
    @property
    def local_security_options_use_admin_approval_mode(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsUseAdminApprovalMode property value. Defines whether the built-in admin account uses Admin Approval Mode or runs all apps with full admin privileges.Default is enabled
        Returns: Optional[bool]
        """
        return self._local_security_options_use_admin_approval_mode
    
    @local_security_options_use_admin_approval_mode.setter
    def local_security_options_use_admin_approval_mode(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsUseAdminApprovalMode property value. Defines whether the built-in admin account uses Admin Approval Mode or runs all apps with full admin privileges.Default is enabled
        Args:
            value: Value to set for the localSecurityOptionsUseAdminApprovalMode property.
        """
        self._local_security_options_use_admin_approval_mode = value
    
    @property
    def local_security_options_use_admin_approval_mode_for_administrators(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsUseAdminApprovalModeForAdministrators property value. Define whether Admin Approval Mode and all UAC policy settings are enabled, default is enabled
        Returns: Optional[bool]
        """
        return self._local_security_options_use_admin_approval_mode_for_administrators
    
    @local_security_options_use_admin_approval_mode_for_administrators.setter
    def local_security_options_use_admin_approval_mode_for_administrators(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsUseAdminApprovalModeForAdministrators property value. Define whether Admin Approval Mode and all UAC policy settings are enabled, default is enabled
        Args:
            value: Value to set for the localSecurityOptionsUseAdminApprovalModeForAdministrators property.
        """
        self._local_security_options_use_admin_approval_mode_for_administrators = value
    
    @property
    def local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations(self,) -> Optional[bool]:
        """
        Gets the localSecurityOptionsVirtualizeFileAndRegistryWriteFailuresToPerUserLocations property value. Virtualize file and registry write failures to per user locations
        Returns: Optional[bool]
        """
        return self._local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations
    
    @local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations.setter
    def local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations(self,value: Optional[bool] = None) -> None:
        """
        Sets the localSecurityOptionsVirtualizeFileAndRegistryWriteFailuresToPerUserLocations property value. Virtualize file and registry write failures to per user locations
        Args:
            value: Value to set for the localSecurityOptionsVirtualizeFileAndRegistryWriteFailuresToPerUserLocations property.
        """
        self._local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("applicationGuardAllowCameraMicrophoneRedirection", self.application_guard_allow_camera_microphone_redirection)
        writer.write_bool_value("applicationGuardAllowFileSaveOnHost", self.application_guard_allow_file_save_on_host)
        writer.write_bool_value("applicationGuardAllowPersistence", self.application_guard_allow_persistence)
        writer.write_bool_value("applicationGuardAllowPrintToLocalPrinters", self.application_guard_allow_print_to_local_printers)
        writer.write_bool_value("applicationGuardAllowPrintToNetworkPrinters", self.application_guard_allow_print_to_network_printers)
        writer.write_bool_value("applicationGuardAllowPrintToPDF", self.application_guard_allow_print_to_p_d_f)
        writer.write_bool_value("applicationGuardAllowPrintToXPS", self.application_guard_allow_print_to_x_p_s)
        writer.write_bool_value("applicationGuardAllowVirtualGPU", self.application_guard_allow_virtual_g_p_u)
        writer.write_enum_value("applicationGuardBlockClipboardSharing", self.application_guard_block_clipboard_sharing)
        writer.write_enum_value("applicationGuardBlockFileTransfer", self.application_guard_block_file_transfer)
        writer.write_bool_value("applicationGuardBlockNonEnterpriseContent", self.application_guard_block_non_enterprise_content)
        writer.write_collection_of_primitive_values("applicationGuardCertificateThumbprints", self.application_guard_certificate_thumbprints)
        writer.write_bool_value("applicationGuardEnabled", self.application_guard_enabled)
        writer.write_enum_value("applicationGuardEnabledOptions", self.application_guard_enabled_options)
        writer.write_bool_value("applicationGuardForceAuditing", self.application_guard_force_auditing)
        writer.write_enum_value("appLockerApplicationControl", self.app_locker_application_control)
        writer.write_bool_value("bitLockerAllowStandardUserEncryption", self.bit_locker_allow_standard_user_encryption)
        writer.write_bool_value("bitLockerDisableWarningForOtherDiskEncryption", self.bit_locker_disable_warning_for_other_disk_encryption)
        writer.write_bool_value("bitLockerEnableStorageCardEncryptionOnMobile", self.bit_locker_enable_storage_card_encryption_on_mobile)
        writer.write_bool_value("bitLockerEncryptDevice", self.bit_locker_encrypt_device)
        writer.write_object_value("bitLockerFixedDrivePolicy", self.bit_locker_fixed_drive_policy)
        writer.write_enum_value("bitLockerRecoveryPasswordRotation", self.bit_locker_recovery_password_rotation)
        writer.write_object_value("bitLockerRemovableDrivePolicy", self.bit_locker_removable_drive_policy)
        writer.write_object_value("bitLockerSystemDrivePolicy", self.bit_locker_system_drive_policy)
        writer.write_collection_of_primitive_values("defenderAdditionalGuardedFolders", self.defender_additional_guarded_folders)
        writer.write_enum_value("defenderAdobeReaderLaunchChildProcess", self.defender_adobe_reader_launch_child_process)
        writer.write_enum_value("defenderAdvancedRansomewareProtectionType", self.defender_advanced_ransomeware_protection_type)
        writer.write_bool_value("defenderAllowBehaviorMonitoring", self.defender_allow_behavior_monitoring)
        writer.write_bool_value("defenderAllowCloudProtection", self.defender_allow_cloud_protection)
        writer.write_bool_value("defenderAllowEndUserAccess", self.defender_allow_end_user_access)
        writer.write_bool_value("defenderAllowIntrusionPreventionSystem", self.defender_allow_intrusion_prevention_system)
        writer.write_bool_value("defenderAllowOnAccessProtection", self.defender_allow_on_access_protection)
        writer.write_bool_value("defenderAllowRealTimeMonitoring", self.defender_allow_real_time_monitoring)
        writer.write_bool_value("defenderAllowScanArchiveFiles", self.defender_allow_scan_archive_files)
        writer.write_bool_value("defenderAllowScanDownloads", self.defender_allow_scan_downloads)
        writer.write_bool_value("defenderAllowScanNetworkFiles", self.defender_allow_scan_network_files)
        writer.write_bool_value("defenderAllowScanRemovableDrivesDuringFullScan", self.defender_allow_scan_removable_drives_during_full_scan)
        writer.write_bool_value("defenderAllowScanScriptsLoadedInInternetExplorer", self.defender_allow_scan_scripts_loaded_in_internet_explorer)
        writer.write_collection_of_primitive_values("defenderAttackSurfaceReductionExcludedPaths", self.defender_attack_surface_reduction_excluded_paths)
        writer.write_bool_value("defenderBlockEndUserAccess", self.defender_block_end_user_access)
        writer.write_enum_value("defenderBlockPersistenceThroughWmiType", self.defender_block_persistence_through_wmi_type)
        writer.write_bool_value("defenderCheckForSignaturesBeforeRunningScan", self.defender_check_for_signatures_before_running_scan)
        writer.write_enum_value("defenderCloudBlockLevel", self.defender_cloud_block_level)
        writer.write_int_value("defenderCloudExtendedTimeoutInSeconds", self.defender_cloud_extended_timeout_in_seconds)
        writer.write_int_value("defenderDaysBeforeDeletingQuarantinedMalware", self.defender_days_before_deleting_quarantined_malware)
        writer.write_object_value("defenderDetectedMalwareActions", self.defender_detected_malware_actions)
        writer.write_bool_value("defenderDisableBehaviorMonitoring", self.defender_disable_behavior_monitoring)
        writer.write_bool_value("defenderDisableCatchupFullScan", self.defender_disable_catchup_full_scan)
        writer.write_bool_value("defenderDisableCatchupQuickScan", self.defender_disable_catchup_quick_scan)
        writer.write_bool_value("defenderDisableCloudProtection", self.defender_disable_cloud_protection)
        writer.write_bool_value("defenderDisableIntrusionPreventionSystem", self.defender_disable_intrusion_prevention_system)
        writer.write_bool_value("defenderDisableOnAccessProtection", self.defender_disable_on_access_protection)
        writer.write_bool_value("defenderDisableRealTimeMonitoring", self.defender_disable_real_time_monitoring)
        writer.write_bool_value("defenderDisableScanArchiveFiles", self.defender_disable_scan_archive_files)
        writer.write_bool_value("defenderDisableScanDownloads", self.defender_disable_scan_downloads)
        writer.write_bool_value("defenderDisableScanNetworkFiles", self.defender_disable_scan_network_files)
        writer.write_bool_value("defenderDisableScanRemovableDrivesDuringFullScan", self.defender_disable_scan_removable_drives_during_full_scan)
        writer.write_bool_value("defenderDisableScanScriptsLoadedInInternetExplorer", self.defender_disable_scan_scripts_loaded_in_internet_explorer)
        writer.write_enum_value("defenderEmailContentExecution", self.defender_email_content_execution)
        writer.write_enum_value("defenderEmailContentExecutionType", self.defender_email_content_execution_type)
        writer.write_bool_value("defenderEnableLowCpuPriority", self.defender_enable_low_cpu_priority)
        writer.write_bool_value("defenderEnableScanIncomingMail", self.defender_enable_scan_incoming_mail)
        writer.write_bool_value("defenderEnableScanMappedNetworkDrivesDuringFullScan", self.defender_enable_scan_mapped_network_drives_during_full_scan)
        writer.write_object_value("defenderExploitProtectionXml", self.defender_exploit_protection_xml)
        writer.write_str_value("defenderExploitProtectionXmlFileName", self.defender_exploit_protection_xml_file_name)
        writer.write_collection_of_primitive_values("defenderFileExtensionsToExclude", self.defender_file_extensions_to_exclude)
        writer.write_collection_of_primitive_values("defenderFilesAndFoldersToExclude", self.defender_files_and_folders_to_exclude)
        writer.write_collection_of_primitive_values("defenderGuardedFoldersAllowedAppPaths", self.defender_guarded_folders_allowed_app_paths)
        writer.write_enum_value("defenderGuardMyFoldersType", self.defender_guard_my_folders_type)
        writer.write_enum_value("defenderNetworkProtectionType", self.defender_network_protection_type)
        writer.write_enum_value("defenderOfficeAppsExecutableContentCreationOrLaunch", self.defender_office_apps_executable_content_creation_or_launch)
        writer.write_enum_value("defenderOfficeAppsExecutableContentCreationOrLaunchType", self.defender_office_apps_executable_content_creation_or_launch_type)
        writer.write_enum_value("defenderOfficeAppsLaunchChildProcess", self.defender_office_apps_launch_child_process)
        writer.write_enum_value("defenderOfficeAppsLaunchChildProcessType", self.defender_office_apps_launch_child_process_type)
        writer.write_enum_value("defenderOfficeAppsOtherProcessInjection", self.defender_office_apps_other_process_injection)
        writer.write_enum_value("defenderOfficeAppsOtherProcessInjectionType", self.defender_office_apps_other_process_injection_type)
        writer.write_enum_value("defenderOfficeCommunicationAppsLaunchChildProcess", self.defender_office_communication_apps_launch_child_process)
        writer.write_enum_value("defenderOfficeMacroCodeAllowWin32Imports", self.defender_office_macro_code_allow_win32_imports)
        writer.write_enum_value("defenderOfficeMacroCodeAllowWin32ImportsType", self.defender_office_macro_code_allow_win32_imports_type)
        writer.write_enum_value("defenderPotentiallyUnwantedAppAction", self.defender_potentially_unwanted_app_action)
        writer.write_enum_value("defenderPreventCredentialStealingType", self.defender_prevent_credential_stealing_type)
        writer.write_enum_value("defenderProcessCreation", self.defender_process_creation)
        writer.write_enum_value("defenderProcessCreationType", self.defender_process_creation_type)
        writer.write_collection_of_primitive_values("defenderProcessesToExclude", self.defender_processes_to_exclude)
        writer.write_enum_value("defenderScanDirection", self.defender_scan_direction)
        writer.write_int_value("defenderScanMaxCpuPercentage", self.defender_scan_max_cpu_percentage)
        writer.write_enum_value("defenderScanType", self.defender_scan_type)
        writer.write_object_value("defenderScheduledQuickScanTime", self.defender_scheduled_quick_scan_time)
        writer.write_enum_value("defenderScheduledScanDay", self.defender_scheduled_scan_day)
        writer.write_object_value("defenderScheduledScanTime", self.defender_scheduled_scan_time)
        writer.write_enum_value("defenderScriptDownloadedPayloadExecution", self.defender_script_downloaded_payload_execution)
        writer.write_enum_value("defenderScriptDownloadedPayloadExecutionType", self.defender_script_downloaded_payload_execution_type)
        writer.write_enum_value("defenderScriptObfuscatedMacroCode", self.defender_script_obfuscated_macro_code)
        writer.write_enum_value("defenderScriptObfuscatedMacroCodeType", self.defender_script_obfuscated_macro_code_type)
        writer.write_bool_value("defenderSecurityCenterBlockExploitProtectionOverride", self.defender_security_center_block_exploit_protection_override)
        writer.write_bool_value("defenderSecurityCenterDisableAccountUI", self.defender_security_center_disable_account_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableAppBrowserUI", self.defender_security_center_disable_app_browser_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableClearTpmUI", self.defender_security_center_disable_clear_tpm_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableFamilyUI", self.defender_security_center_disable_family_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableHardwareUI", self.defender_security_center_disable_hardware_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableHealthUI", self.defender_security_center_disable_health_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableNetworkUI", self.defender_security_center_disable_network_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableNotificationAreaUI", self.defender_security_center_disable_notification_area_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableRansomwareUI", self.defender_security_center_disable_ransomware_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableSecureBootUI", self.defender_security_center_disable_secure_boot_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableTroubleshootingUI", self.defender_security_center_disable_troubleshooting_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableVirusUI", self.defender_security_center_disable_virus_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableVulnerableTpmFirmwareUpdateUI", self.defender_security_center_disable_vulnerable_tpm_firmware_update_u_i)
        writer.write_str_value("defenderSecurityCenterHelpEmail", self.defender_security_center_help_email)
        writer.write_str_value("defenderSecurityCenterHelpPhone", self.defender_security_center_help_phone)
        writer.write_str_value("defenderSecurityCenterHelpURL", self.defender_security_center_help_u_r_l)
        writer.write_enum_value("defenderSecurityCenterITContactDisplay", self.defender_security_center_i_t_contact_display)
        writer.write_enum_value("defenderSecurityCenterNotificationsFromApp", self.defender_security_center_notifications_from_app)
        writer.write_str_value("defenderSecurityCenterOrganizationDisplayName", self.defender_security_center_organization_display_name)
        writer.write_int_value("defenderSignatureUpdateIntervalInHours", self.defender_signature_update_interval_in_hours)
        writer.write_enum_value("defenderSubmitSamplesConsentType", self.defender_submit_samples_consent_type)
        writer.write_enum_value("defenderUntrustedExecutable", self.defender_untrusted_executable)
        writer.write_enum_value("defenderUntrustedExecutableType", self.defender_untrusted_executable_type)
        writer.write_enum_value("defenderUntrustedUSBProcess", self.defender_untrusted_u_s_b_process)
        writer.write_enum_value("defenderUntrustedUSBProcessType", self.defender_untrusted_u_s_b_process_type)
        writer.write_bool_value("deviceGuardEnableSecureBootWithDMA", self.device_guard_enable_secure_boot_with_d_m_a)
        writer.write_bool_value("deviceGuardEnableVirtualizationBasedSecurity", self.device_guard_enable_virtualization_based_security)
        writer.write_enum_value("deviceGuardLaunchSystemGuard", self.device_guard_launch_system_guard)
        writer.write_enum_value("deviceGuardLocalSystemAuthorityCredentialGuardSettings", self.device_guard_local_system_authority_credential_guard_settings)
        writer.write_enum_value("deviceGuardSecureBootWithDMA", self.device_guard_secure_boot_with_d_m_a)
        writer.write_enum_value("dmaGuardDeviceEnumerationPolicy", self.dma_guard_device_enumeration_policy)
        writer.write_bool_value("firewallBlockStatefulFTP", self.firewall_block_stateful_f_t_p)
        writer.write_enum_value("firewallCertificateRevocationListCheckMethod", self.firewall_certificate_revocation_list_check_method)
        writer.write_int_value("firewallIdleTimeoutForSecurityAssociationInSeconds", self.firewall_idle_timeout_for_security_association_in_seconds)
        writer.write_bool_value("firewallIPSecExemptionsAllowDHCP", self.firewall_i_p_sec_exemptions_allow_d_h_c_p)
        writer.write_bool_value("firewallIPSecExemptionsAllowICMP", self.firewall_i_p_sec_exemptions_allow_i_c_m_p)
        writer.write_bool_value("firewallIPSecExemptionsAllowNeighborDiscovery", self.firewall_i_p_sec_exemptions_allow_neighbor_discovery)
        writer.write_bool_value("firewallIPSecExemptionsAllowRouterDiscovery", self.firewall_i_p_sec_exemptions_allow_router_discovery)
        writer.write_bool_value("firewallIPSecExemptionsNone", self.firewall_i_p_sec_exemptions_none)
        writer.write_bool_value("firewallMergeKeyingModuleSettings", self.firewall_merge_keying_module_settings)
        writer.write_enum_value("firewallPacketQueueingMethod", self.firewall_packet_queueing_method)
        writer.write_enum_value("firewallPreSharedKeyEncodingMethod", self.firewall_pre_shared_key_encoding_method)
        writer.write_object_value("firewallProfileDomain", self.firewall_profile_domain)
        writer.write_object_value("firewallProfilePrivate", self.firewall_profile_private)
        writer.write_object_value("firewallProfilePublic", self.firewall_profile_public)
        writer.write_collection_of_object_values("firewallRules", self.firewall_rules)
        writer.write_enum_value("lanManagerAuthenticationLevel", self.lan_manager_authentication_level)
        writer.write_bool_value("lanManagerWorkstationDisableInsecureGuestLogons", self.lan_manager_workstation_disable_insecure_guest_logons)
        writer.write_str_value("localSecurityOptionsAdministratorAccountName", self.local_security_options_administrator_account_name)
        writer.write_enum_value("localSecurityOptionsAdministratorElevationPromptBehavior", self.local_security_options_administrator_elevation_prompt_behavior)
        writer.write_bool_value("localSecurityOptionsAllowAnonymousEnumerationOfSAMAccountsAndShares", self.local_security_options_allow_anonymous_enumeration_of_s_a_m_accounts_and_shares)
        writer.write_bool_value("localSecurityOptionsAllowPKU2UAuthenticationRequests", self.local_security_options_allow_p_k_u2_u_authentication_requests)
        writer.write_str_value("localSecurityOptionsAllowRemoteCallsToSecurityAccountsManager", self.local_security_options_allow_remote_calls_to_security_accounts_manager)
        writer.write_bool_value("localSecurityOptionsAllowRemoteCallsToSecurityAccountsManagerHelperBool", self.local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool)
        writer.write_bool_value("localSecurityOptionsAllowSystemToBeShutDownWithoutHavingToLogOn", self.local_security_options_allow_system_to_be_shut_down_without_having_to_log_on)
        writer.write_bool_value("localSecurityOptionsAllowUIAccessApplicationElevation", self.local_security_options_allow_u_i_access_application_elevation)
        writer.write_bool_value("localSecurityOptionsAllowUIAccessApplicationsForSecureLocations", self.local_security_options_allow_u_i_access_applications_for_secure_locations)
        writer.write_bool_value("localSecurityOptionsAllowUndockWithoutHavingToLogon", self.local_security_options_allow_undock_without_having_to_logon)
        writer.write_bool_value("localSecurityOptionsBlockMicrosoftAccounts", self.local_security_options_block_microsoft_accounts)
        writer.write_bool_value("localSecurityOptionsBlockRemoteLogonWithBlankPassword", self.local_security_options_block_remote_logon_with_blank_password)
        writer.write_bool_value("localSecurityOptionsBlockRemoteOpticalDriveAccess", self.local_security_options_block_remote_optical_drive_access)
        writer.write_bool_value("localSecurityOptionsBlockUsersInstallingPrinterDrivers", self.local_security_options_block_users_installing_printer_drivers)
        writer.write_bool_value("localSecurityOptionsClearVirtualMemoryPageFile", self.local_security_options_clear_virtual_memory_page_file)
        writer.write_bool_value("localSecurityOptionsClientDigitallySignCommunicationsAlways", self.local_security_options_client_digitally_sign_communications_always)
        writer.write_bool_value("localSecurityOptionsClientSendUnencryptedPasswordToThirdPartySMBServers", self.local_security_options_client_send_unencrypted_password_to_third_party_s_m_b_servers)
        writer.write_bool_value("localSecurityOptionsDetectApplicationInstallationsAndPromptForElevation", self.local_security_options_detect_application_installations_and_prompt_for_elevation)
        writer.write_bool_value("localSecurityOptionsDisableAdministratorAccount", self.local_security_options_disable_administrator_account)
        writer.write_bool_value("localSecurityOptionsDisableClientDigitallySignCommunicationsIfServerAgrees", self.local_security_options_disable_client_digitally_sign_communications_if_server_agrees)
        writer.write_bool_value("localSecurityOptionsDisableGuestAccount", self.local_security_options_disable_guest_account)
        writer.write_bool_value("localSecurityOptionsDisableServerDigitallySignCommunicationsAlways", self.local_security_options_disable_server_digitally_sign_communications_always)
        writer.write_bool_value("localSecurityOptionsDisableServerDigitallySignCommunicationsIfClientAgrees", self.local_security_options_disable_server_digitally_sign_communications_if_client_agrees)
        writer.write_bool_value("localSecurityOptionsDoNotAllowAnonymousEnumerationOfSAMAccounts", self.local_security_options_do_not_allow_anonymous_enumeration_of_s_a_m_accounts)
        writer.write_bool_value("localSecurityOptionsDoNotRequireCtrlAltDel", self.local_security_options_do_not_require_ctrl_alt_del)
        writer.write_bool_value("localSecurityOptionsDoNotStoreLANManagerHashValueOnNextPasswordChange", self.local_security_options_do_not_store_l_a_n_manager_hash_value_on_next_password_change)
        writer.write_enum_value("localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser", self.local_security_options_format_and_eject_of_removable_media_allowed_user)
        writer.write_str_value("localSecurityOptionsGuestAccountName", self.local_security_options_guest_account_name)
        writer.write_bool_value("localSecurityOptionsHideLastSignedInUser", self.local_security_options_hide_last_signed_in_user)
        writer.write_bool_value("localSecurityOptionsHideUsernameAtSignIn", self.local_security_options_hide_username_at_sign_in)
        writer.write_enum_value("localSecurityOptionsInformationDisplayedOnLockScreen", self.local_security_options_information_displayed_on_lock_screen)
        writer.write_enum_value("localSecurityOptionsInformationShownOnLockScreen", self.local_security_options_information_shown_on_lock_screen)
        writer.write_str_value("localSecurityOptionsLogOnMessageText", self.local_security_options_log_on_message_text)
        writer.write_str_value("localSecurityOptionsLogOnMessageTitle", self.local_security_options_log_on_message_title)
        writer.write_int_value("localSecurityOptionsMachineInactivityLimit", self.local_security_options_machine_inactivity_limit)
        writer.write_int_value("localSecurityOptionsMachineInactivityLimitInMinutes", self.local_security_options_machine_inactivity_limit_in_minutes)
        writer.write_enum_value("localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedClients", self.local_security_options_minimum_session_security_for_ntlm_ssp_based_clients)
        writer.write_enum_value("localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedServers", self.local_security_options_minimum_session_security_for_ntlm_ssp_based_servers)
        writer.write_bool_value("localSecurityOptionsOnlyElevateSignedExecutables", self.local_security_options_only_elevate_signed_executables)
        writer.write_bool_value("localSecurityOptionsRestrictAnonymousAccessToNamedPipesAndShares", self.local_security_options_restrict_anonymous_access_to_named_pipes_and_shares)
        writer.write_enum_value("localSecurityOptionsSmartCardRemovalBehavior", self.local_security_options_smart_card_removal_behavior)
        writer.write_enum_value("localSecurityOptionsStandardUserElevationPromptBehavior", self.local_security_options_standard_user_elevation_prompt_behavior)
        writer.write_bool_value("localSecurityOptionsSwitchToSecureDesktopWhenPromptingForElevation", self.local_security_options_switch_to_secure_desktop_when_prompting_for_elevation)
        writer.write_bool_value("localSecurityOptionsUseAdminApprovalMode", self.local_security_options_use_admin_approval_mode)
        writer.write_bool_value("localSecurityOptionsUseAdminApprovalModeForAdministrators", self.local_security_options_use_admin_approval_mode_for_administrators)
        writer.write_bool_value("localSecurityOptionsVirtualizeFileAndRegistryWriteFailuresToPerUserLocations", self.local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations)
        writer.write_bool_value("smartScreenBlockOverrideForFiles", self.smart_screen_block_override_for_files)
        writer.write_bool_value("smartScreenEnableInShell", self.smart_screen_enable_in_shell)
        writer.write_object_value("userRightsAccessCredentialManagerAsTrustedCaller", self.user_rights_access_credential_manager_as_trusted_caller)
        writer.write_object_value("userRightsActAsPartOfTheOperatingSystem", self.user_rights_act_as_part_of_the_operating_system)
        writer.write_object_value("userRightsAllowAccessFromNetwork", self.user_rights_allow_access_from_network)
        writer.write_object_value("userRightsBackupData", self.user_rights_backup_data)
        writer.write_object_value("userRightsBlockAccessFromNetwork", self.user_rights_block_access_from_network)
        writer.write_object_value("userRightsChangeSystemTime", self.user_rights_change_system_time)
        writer.write_object_value("userRightsCreateGlobalObjects", self.user_rights_create_global_objects)
        writer.write_object_value("userRightsCreatePageFile", self.user_rights_create_page_file)
        writer.write_object_value("userRightsCreatePermanentSharedObjects", self.user_rights_create_permanent_shared_objects)
        writer.write_object_value("userRightsCreateSymbolicLinks", self.user_rights_create_symbolic_links)
        writer.write_object_value("userRightsCreateToken", self.user_rights_create_token)
        writer.write_object_value("userRightsDebugPrograms", self.user_rights_debug_programs)
        writer.write_object_value("userRightsDelegation", self.user_rights_delegation)
        writer.write_object_value("userRightsDenyLocalLogOn", self.user_rights_deny_local_log_on)
        writer.write_object_value("userRightsGenerateSecurityAudits", self.user_rights_generate_security_audits)
        writer.write_object_value("userRightsImpersonateClient", self.user_rights_impersonate_client)
        writer.write_object_value("userRightsIncreaseSchedulingPriority", self.user_rights_increase_scheduling_priority)
        writer.write_object_value("userRightsLoadUnloadDrivers", self.user_rights_load_unload_drivers)
        writer.write_object_value("userRightsLocalLogOn", self.user_rights_local_log_on)
        writer.write_object_value("userRightsLockMemory", self.user_rights_lock_memory)
        writer.write_object_value("userRightsManageAuditingAndSecurityLogs", self.user_rights_manage_auditing_and_security_logs)
        writer.write_object_value("userRightsManageVolumes", self.user_rights_manage_volumes)
        writer.write_object_value("userRightsModifyFirmwareEnvironment", self.user_rights_modify_firmware_environment)
        writer.write_object_value("userRightsModifyObjectLabels", self.user_rights_modify_object_labels)
        writer.write_object_value("userRightsProfileSingleProcess", self.user_rights_profile_single_process)
        writer.write_object_value("userRightsRemoteDesktopServicesLogOn", self.user_rights_remote_desktop_services_log_on)
        writer.write_object_value("userRightsRemoteShutdown", self.user_rights_remote_shutdown)
        writer.write_object_value("userRightsRestoreData", self.user_rights_restore_data)
        writer.write_object_value("userRightsTakeOwnership", self.user_rights_take_ownership)
        writer.write_enum_value("windowsDefenderTamperProtection", self.windows_defender_tamper_protection)
        writer.write_enum_value("xboxServicesAccessoryManagementServiceStartupMode", self.xbox_services_accessory_management_service_startup_mode)
        writer.write_bool_value("xboxServicesEnableXboxGameSaveTask", self.xbox_services_enable_xbox_game_save_task)
        writer.write_enum_value("xboxServicesLiveAuthManagerServiceStartupMode", self.xbox_services_live_auth_manager_service_startup_mode)
        writer.write_enum_value("xboxServicesLiveGameSaveServiceStartupMode", self.xbox_services_live_game_save_service_startup_mode)
        writer.write_enum_value("xboxServicesLiveNetworkingServiceStartupMode", self.xbox_services_live_networking_service_startup_mode)
    
    @property
    def smart_screen_block_override_for_files(self,) -> Optional[bool]:
        """
        Gets the smartScreenBlockOverrideForFiles property value. Allows IT Admins to control whether users can can ignore SmartScreen warnings and run malicious files.
        Returns: Optional[bool]
        """
        return self._smart_screen_block_override_for_files
    
    @smart_screen_block_override_for_files.setter
    def smart_screen_block_override_for_files(self,value: Optional[bool] = None) -> None:
        """
        Sets the smartScreenBlockOverrideForFiles property value. Allows IT Admins to control whether users can can ignore SmartScreen warnings and run malicious files.
        Args:
            value: Value to set for the smartScreenBlockOverrideForFiles property.
        """
        self._smart_screen_block_override_for_files = value
    
    @property
    def smart_screen_enable_in_shell(self,) -> Optional[bool]:
        """
        Gets the smartScreenEnableInShell property value. Allows IT Admins to configure SmartScreen for Windows.
        Returns: Optional[bool]
        """
        return self._smart_screen_enable_in_shell
    
    @smart_screen_enable_in_shell.setter
    def smart_screen_enable_in_shell(self,value: Optional[bool] = None) -> None:
        """
        Sets the smartScreenEnableInShell property value. Allows IT Admins to configure SmartScreen for Windows.
        Args:
            value: Value to set for the smartScreenEnableInShell property.
        """
        self._smart_screen_enable_in_shell = value
    
    @property
    def user_rights_access_credential_manager_as_trusted_caller(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsAccessCredentialManagerAsTrustedCaller property value. This user right is used by Credential Manager during Backup/Restore. Users' saved credentials might be compromised if this privilege is given to other entities. Only states NotConfigured and Allowed are supported
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_access_credential_manager_as_trusted_caller
    
    @user_rights_access_credential_manager_as_trusted_caller.setter
    def user_rights_access_credential_manager_as_trusted_caller(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsAccessCredentialManagerAsTrustedCaller property value. This user right is used by Credential Manager during Backup/Restore. Users' saved credentials might be compromised if this privilege is given to other entities. Only states NotConfigured and Allowed are supported
        Args:
            value: Value to set for the userRightsAccessCredentialManagerAsTrustedCaller property.
        """
        self._user_rights_access_credential_manager_as_trusted_caller = value
    
    @property
    def user_rights_act_as_part_of_the_operating_system(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsActAsPartOfTheOperatingSystem property value. This user right allows a process to impersonate any user without authentication. The process can therefore gain access to the same local resources as that user. Only states NotConfigured and Allowed are supported
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_act_as_part_of_the_operating_system
    
    @user_rights_act_as_part_of_the_operating_system.setter
    def user_rights_act_as_part_of_the_operating_system(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsActAsPartOfTheOperatingSystem property value. This user right allows a process to impersonate any user without authentication. The process can therefore gain access to the same local resources as that user. Only states NotConfigured and Allowed are supported
        Args:
            value: Value to set for the userRightsActAsPartOfTheOperatingSystem property.
        """
        self._user_rights_act_as_part_of_the_operating_system = value
    
    @property
    def user_rights_allow_access_from_network(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsAllowAccessFromNetwork property value. This user right determines which users and groups are allowed to connect to the computer over the network. State Allowed is supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_allow_access_from_network
    
    @user_rights_allow_access_from_network.setter
    def user_rights_allow_access_from_network(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsAllowAccessFromNetwork property value. This user right determines which users and groups are allowed to connect to the computer over the network. State Allowed is supported.
        Args:
            value: Value to set for the userRightsAllowAccessFromNetwork property.
        """
        self._user_rights_allow_access_from_network = value
    
    @property
    def user_rights_backup_data(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsBackupData property value. This user right determines which users can bypass file, directory, registry, and other persistent objects permissions when backing up files and directories. Only states NotConfigured and Allowed are supported
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_backup_data
    
    @user_rights_backup_data.setter
    def user_rights_backup_data(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsBackupData property value. This user right determines which users can bypass file, directory, registry, and other persistent objects permissions when backing up files and directories. Only states NotConfigured and Allowed are supported
        Args:
            value: Value to set for the userRightsBackupData property.
        """
        self._user_rights_backup_data = value
    
    @property
    def user_rights_block_access_from_network(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsBlockAccessFromNetwork property value. This user right determines which users and groups are block from connecting to the computer over the network. State Block is supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_block_access_from_network
    
    @user_rights_block_access_from_network.setter
    def user_rights_block_access_from_network(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsBlockAccessFromNetwork property value. This user right determines which users and groups are block from connecting to the computer over the network. State Block is supported.
        Args:
            value: Value to set for the userRightsBlockAccessFromNetwork property.
        """
        self._user_rights_block_access_from_network = value
    
    @property
    def user_rights_change_system_time(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsChangeSystemTime property value. This user right determines which users and groups can change the time and date on the internal clock of the computer. Only states NotConfigured and Allowed are supported
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_change_system_time
    
    @user_rights_change_system_time.setter
    def user_rights_change_system_time(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsChangeSystemTime property value. This user right determines which users and groups can change the time and date on the internal clock of the computer. Only states NotConfigured and Allowed are supported
        Args:
            value: Value to set for the userRightsChangeSystemTime property.
        """
        self._user_rights_change_system_time = value
    
    @property
    def user_rights_create_global_objects(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsCreateGlobalObjects property value. This security setting determines whether users can create global objects that are available to all sessions. Users who can create global objects could affect processes that run under other users' sessions, which could lead to application failure or data corruption. Only states NotConfigured and Allowed are supported
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_create_global_objects
    
    @user_rights_create_global_objects.setter
    def user_rights_create_global_objects(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsCreateGlobalObjects property value. This security setting determines whether users can create global objects that are available to all sessions. Users who can create global objects could affect processes that run under other users' sessions, which could lead to application failure or data corruption. Only states NotConfigured and Allowed are supported
        Args:
            value: Value to set for the userRightsCreateGlobalObjects property.
        """
        self._user_rights_create_global_objects = value
    
    @property
    def user_rights_create_page_file(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsCreatePageFile property value. This user right determines which users and groups can call an internal API to create and change the size of a page file. Only states NotConfigured and Allowed are supported
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_create_page_file
    
    @user_rights_create_page_file.setter
    def user_rights_create_page_file(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsCreatePageFile property value. This user right determines which users and groups can call an internal API to create and change the size of a page file. Only states NotConfigured and Allowed are supported
        Args:
            value: Value to set for the userRightsCreatePageFile property.
        """
        self._user_rights_create_page_file = value
    
    @property
    def user_rights_create_permanent_shared_objects(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsCreatePermanentSharedObjects property value. This user right determines which accounts can be used by processes to create a directory object using the object manager. Only states NotConfigured and Allowed are supported
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_create_permanent_shared_objects
    
    @user_rights_create_permanent_shared_objects.setter
    def user_rights_create_permanent_shared_objects(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsCreatePermanentSharedObjects property value. This user right determines which accounts can be used by processes to create a directory object using the object manager. Only states NotConfigured and Allowed are supported
        Args:
            value: Value to set for the userRightsCreatePermanentSharedObjects property.
        """
        self._user_rights_create_permanent_shared_objects = value
    
    @property
    def user_rights_create_symbolic_links(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsCreateSymbolicLinks property value. This user right determines if the user can create a symbolic link from the computer to which they are logged on. Only states NotConfigured and Allowed are supported
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_create_symbolic_links
    
    @user_rights_create_symbolic_links.setter
    def user_rights_create_symbolic_links(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsCreateSymbolicLinks property value. This user right determines if the user can create a symbolic link from the computer to which they are logged on. Only states NotConfigured and Allowed are supported
        Args:
            value: Value to set for the userRightsCreateSymbolicLinks property.
        """
        self._user_rights_create_symbolic_links = value
    
    @property
    def user_rights_create_token(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsCreateToken property value. This user right determines which users/groups can be used by processes to create a token that can then be used to get access to any local resources when the process uses an internal API to create an access token. Only states NotConfigured and Allowed are supported
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_create_token
    
    @user_rights_create_token.setter
    def user_rights_create_token(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsCreateToken property value. This user right determines which users/groups can be used by processes to create a token that can then be used to get access to any local resources when the process uses an internal API to create an access token. Only states NotConfigured and Allowed are supported
        Args:
            value: Value to set for the userRightsCreateToken property.
        """
        self._user_rights_create_token = value
    
    @property
    def user_rights_debug_programs(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsDebugPrograms property value. This user right determines which users can attach a debugger to any process or to the kernel. Only states NotConfigured and Allowed are supported
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_debug_programs
    
    @user_rights_debug_programs.setter
    def user_rights_debug_programs(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsDebugPrograms property value. This user right determines which users can attach a debugger to any process or to the kernel. Only states NotConfigured and Allowed are supported
        Args:
            value: Value to set for the userRightsDebugPrograms property.
        """
        self._user_rights_debug_programs = value
    
    @property
    def user_rights_delegation(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsDelegation property value. This user right determines which users can set the Trusted for Delegation setting on a user or computer object. Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_delegation
    
    @user_rights_delegation.setter
    def user_rights_delegation(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsDelegation property value. This user right determines which users can set the Trusted for Delegation setting on a user or computer object. Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsDelegation property.
        """
        self._user_rights_delegation = value
    
    @property
    def user_rights_deny_local_log_on(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsDenyLocalLogOn property value. This user right determines which users cannot log on to the computer. States NotConfigured, Blocked are supported
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_deny_local_log_on
    
    @user_rights_deny_local_log_on.setter
    def user_rights_deny_local_log_on(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsDenyLocalLogOn property value. This user right determines which users cannot log on to the computer. States NotConfigured, Blocked are supported
        Args:
            value: Value to set for the userRightsDenyLocalLogOn property.
        """
        self._user_rights_deny_local_log_on = value
    
    @property
    def user_rights_generate_security_audits(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsGenerateSecurityAudits property value. This user right determines which accounts can be used by a process to add entries to the security log. The security log is used to trace unauthorized system access.  Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_generate_security_audits
    
    @user_rights_generate_security_audits.setter
    def user_rights_generate_security_audits(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsGenerateSecurityAudits property value. This user right determines which accounts can be used by a process to add entries to the security log. The security log is used to trace unauthorized system access.  Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsGenerateSecurityAudits property.
        """
        self._user_rights_generate_security_audits = value
    
    @property
    def user_rights_impersonate_client(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsImpersonateClient property value. Assigning this user right to a user allows programs running on behalf of that user to impersonate a client. Requiring this user right for this kind of impersonation prevents an unauthorized user from convincing a client to connect to a service that they have created and then impersonating that client, which can elevate the unauthorized user's permissions to administrative or system levels. Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_impersonate_client
    
    @user_rights_impersonate_client.setter
    def user_rights_impersonate_client(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsImpersonateClient property value. Assigning this user right to a user allows programs running on behalf of that user to impersonate a client. Requiring this user right for this kind of impersonation prevents an unauthorized user from convincing a client to connect to a service that they have created and then impersonating that client, which can elevate the unauthorized user's permissions to administrative or system levels. Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsImpersonateClient property.
        """
        self._user_rights_impersonate_client = value
    
    @property
    def user_rights_increase_scheduling_priority(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsIncreaseSchedulingPriority property value. This user right determines which accounts can use a process with Write Property access to another process to increase the execution priority assigned to the other process. Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_increase_scheduling_priority
    
    @user_rights_increase_scheduling_priority.setter
    def user_rights_increase_scheduling_priority(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsIncreaseSchedulingPriority property value. This user right determines which accounts can use a process with Write Property access to another process to increase the execution priority assigned to the other process. Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsIncreaseSchedulingPriority property.
        """
        self._user_rights_increase_scheduling_priority = value
    
    @property
    def user_rights_load_unload_drivers(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsLoadUnloadDrivers property value. This user right determines which users can dynamically load and unload device drivers or other code in to kernel mode. Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_load_unload_drivers
    
    @user_rights_load_unload_drivers.setter
    def user_rights_load_unload_drivers(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsLoadUnloadDrivers property value. This user right determines which users can dynamically load and unload device drivers or other code in to kernel mode. Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsLoadUnloadDrivers property.
        """
        self._user_rights_load_unload_drivers = value
    
    @property
    def user_rights_local_log_on(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsLocalLogOn property value. This user right determines which users can log on to the computer. States NotConfigured, Allowed are supported
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_local_log_on
    
    @user_rights_local_log_on.setter
    def user_rights_local_log_on(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsLocalLogOn property value. This user right determines which users can log on to the computer. States NotConfigured, Allowed are supported
        Args:
            value: Value to set for the userRightsLocalLogOn property.
        """
        self._user_rights_local_log_on = value
    
    @property
    def user_rights_lock_memory(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsLockMemory property value. This user right determines which accounts can use a process to keep data in physical memory, which prevents the system from paging the data to virtual memory on disk. Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_lock_memory
    
    @user_rights_lock_memory.setter
    def user_rights_lock_memory(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsLockMemory property value. This user right determines which accounts can use a process to keep data in physical memory, which prevents the system from paging the data to virtual memory on disk. Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsLockMemory property.
        """
        self._user_rights_lock_memory = value
    
    @property
    def user_rights_manage_auditing_and_security_logs(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsManageAuditingAndSecurityLogs property value. This user right determines which users can specify object access auditing options for individual resources, such as files, Active Directory objects, and registry keys. Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_manage_auditing_and_security_logs
    
    @user_rights_manage_auditing_and_security_logs.setter
    def user_rights_manage_auditing_and_security_logs(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsManageAuditingAndSecurityLogs property value. This user right determines which users can specify object access auditing options for individual resources, such as files, Active Directory objects, and registry keys. Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsManageAuditingAndSecurityLogs property.
        """
        self._user_rights_manage_auditing_and_security_logs = value
    
    @property
    def user_rights_manage_volumes(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsManageVolumes property value. This user right determines which users and groups can run maintenance tasks on a volume, such as remote defragmentation. Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_manage_volumes
    
    @user_rights_manage_volumes.setter
    def user_rights_manage_volumes(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsManageVolumes property value. This user right determines which users and groups can run maintenance tasks on a volume, such as remote defragmentation. Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsManageVolumes property.
        """
        self._user_rights_manage_volumes = value
    
    @property
    def user_rights_modify_firmware_environment(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsModifyFirmwareEnvironment property value. This user right determines who can modify firmware environment values. Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_modify_firmware_environment
    
    @user_rights_modify_firmware_environment.setter
    def user_rights_modify_firmware_environment(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsModifyFirmwareEnvironment property value. This user right determines who can modify firmware environment values. Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsModifyFirmwareEnvironment property.
        """
        self._user_rights_modify_firmware_environment = value
    
    @property
    def user_rights_modify_object_labels(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsModifyObjectLabels property value. This user right determines which user accounts can modify the integrity label of objects, such as files, registry keys, or processes owned by other users. Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_modify_object_labels
    
    @user_rights_modify_object_labels.setter
    def user_rights_modify_object_labels(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsModifyObjectLabels property value. This user right determines which user accounts can modify the integrity label of objects, such as files, registry keys, or processes owned by other users. Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsModifyObjectLabels property.
        """
        self._user_rights_modify_object_labels = value
    
    @property
    def user_rights_profile_single_process(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsProfileSingleProcess property value. This user right determines which users can use performance monitoring tools to monitor the performance of system processes. Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_profile_single_process
    
    @user_rights_profile_single_process.setter
    def user_rights_profile_single_process(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsProfileSingleProcess property value. This user right determines which users can use performance monitoring tools to monitor the performance of system processes. Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsProfileSingleProcess property.
        """
        self._user_rights_profile_single_process = value
    
    @property
    def user_rights_remote_desktop_services_log_on(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsRemoteDesktopServicesLogOn property value. This user right determines which users and groups are prohibited from logging on as a Remote Desktop Services client. Only states NotConfigured and Blocked are supported
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_remote_desktop_services_log_on
    
    @user_rights_remote_desktop_services_log_on.setter
    def user_rights_remote_desktop_services_log_on(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsRemoteDesktopServicesLogOn property value. This user right determines which users and groups are prohibited from logging on as a Remote Desktop Services client. Only states NotConfigured and Blocked are supported
        Args:
            value: Value to set for the userRightsRemoteDesktopServicesLogOn property.
        """
        self._user_rights_remote_desktop_services_log_on = value
    
    @property
    def user_rights_remote_shutdown(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsRemoteShutdown property value. This user right determines which users are allowed to shut down a computer from a remote location on the network. Misuse of this user right can result in a denial of service. Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_remote_shutdown
    
    @user_rights_remote_shutdown.setter
    def user_rights_remote_shutdown(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsRemoteShutdown property value. This user right determines which users are allowed to shut down a computer from a remote location on the network. Misuse of this user right can result in a denial of service. Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsRemoteShutdown property.
        """
        self._user_rights_remote_shutdown = value
    
    @property
    def user_rights_restore_data(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsRestoreData property value. This user right determines which users can bypass file, directory, registry, and other persistent objects permissions when restoring backed up files and directories, and determines which users can set any valid security principal as the owner of an object. Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_restore_data
    
    @user_rights_restore_data.setter
    def user_rights_restore_data(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsRestoreData property value. This user right determines which users can bypass file, directory, registry, and other persistent objects permissions when restoring backed up files and directories, and determines which users can set any valid security principal as the owner of an object. Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsRestoreData property.
        """
        self._user_rights_restore_data = value
    
    @property
    def user_rights_take_ownership(self,) -> Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]:
        """
        Gets the userRightsTakeOwnership property value. This user right determines which users can take ownership of any securable object in the system, including Active Directory objects, files and folders, printers, registry keys, processes, and threads. Only states NotConfigured and Allowed are supported.
        Returns: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting]
        """
        return self._user_rights_take_ownership
    
    @user_rights_take_ownership.setter
    def user_rights_take_ownership(self,value: Optional[device_management_user_rights_setting.DeviceManagementUserRightsSetting] = None) -> None:
        """
        Sets the userRightsTakeOwnership property value. This user right determines which users can take ownership of any securable object in the system, including Active Directory objects, files and folders, printers, registry keys, processes, and threads. Only states NotConfigured and Allowed are supported.
        Args:
            value: Value to set for the userRightsTakeOwnership property.
        """
        self._user_rights_take_ownership = value
    
    @property
    def windows_defender_tamper_protection(self,) -> Optional[windows_defender_tamper_protection_options.WindowsDefenderTamperProtectionOptions]:
        """
        Gets the windowsDefenderTamperProtection property value. Defender TamperProtection setting options
        Returns: Optional[windows_defender_tamper_protection_options.WindowsDefenderTamperProtectionOptions]
        """
        return self._windows_defender_tamper_protection
    
    @windows_defender_tamper_protection.setter
    def windows_defender_tamper_protection(self,value: Optional[windows_defender_tamper_protection_options.WindowsDefenderTamperProtectionOptions] = None) -> None:
        """
        Sets the windowsDefenderTamperProtection property value. Defender TamperProtection setting options
        Args:
            value: Value to set for the windowsDefenderTamperProtection property.
        """
        self._windows_defender_tamper_protection = value
    
    @property
    def xbox_services_accessory_management_service_startup_mode(self,) -> Optional[service_start_type.ServiceStartType]:
        """
        Gets the xboxServicesAccessoryManagementServiceStartupMode property value. Possible values of xbox service start type
        Returns: Optional[service_start_type.ServiceStartType]
        """
        return self._xbox_services_accessory_management_service_startup_mode
    
    @xbox_services_accessory_management_service_startup_mode.setter
    def xbox_services_accessory_management_service_startup_mode(self,value: Optional[service_start_type.ServiceStartType] = None) -> None:
        """
        Sets the xboxServicesAccessoryManagementServiceStartupMode property value. Possible values of xbox service start type
        Args:
            value: Value to set for the xboxServicesAccessoryManagementServiceStartupMode property.
        """
        self._xbox_services_accessory_management_service_startup_mode = value
    
    @property
    def xbox_services_enable_xbox_game_save_task(self,) -> Optional[bool]:
        """
        Gets the xboxServicesEnableXboxGameSaveTask property value. This setting determines whether xbox game save is enabled (1) or disabled (0).
        Returns: Optional[bool]
        """
        return self._xbox_services_enable_xbox_game_save_task
    
    @xbox_services_enable_xbox_game_save_task.setter
    def xbox_services_enable_xbox_game_save_task(self,value: Optional[bool] = None) -> None:
        """
        Sets the xboxServicesEnableXboxGameSaveTask property value. This setting determines whether xbox game save is enabled (1) or disabled (0).
        Args:
            value: Value to set for the xboxServicesEnableXboxGameSaveTask property.
        """
        self._xbox_services_enable_xbox_game_save_task = value
    
    @property
    def xbox_services_live_auth_manager_service_startup_mode(self,) -> Optional[service_start_type.ServiceStartType]:
        """
        Gets the xboxServicesLiveAuthManagerServiceStartupMode property value. Possible values of xbox service start type
        Returns: Optional[service_start_type.ServiceStartType]
        """
        return self._xbox_services_live_auth_manager_service_startup_mode
    
    @xbox_services_live_auth_manager_service_startup_mode.setter
    def xbox_services_live_auth_manager_service_startup_mode(self,value: Optional[service_start_type.ServiceStartType] = None) -> None:
        """
        Sets the xboxServicesLiveAuthManagerServiceStartupMode property value. Possible values of xbox service start type
        Args:
            value: Value to set for the xboxServicesLiveAuthManagerServiceStartupMode property.
        """
        self._xbox_services_live_auth_manager_service_startup_mode = value
    
    @property
    def xbox_services_live_game_save_service_startup_mode(self,) -> Optional[service_start_type.ServiceStartType]:
        """
        Gets the xboxServicesLiveGameSaveServiceStartupMode property value. Possible values of xbox service start type
        Returns: Optional[service_start_type.ServiceStartType]
        """
        return self._xbox_services_live_game_save_service_startup_mode
    
    @xbox_services_live_game_save_service_startup_mode.setter
    def xbox_services_live_game_save_service_startup_mode(self,value: Optional[service_start_type.ServiceStartType] = None) -> None:
        """
        Sets the xboxServicesLiveGameSaveServiceStartupMode property value. Possible values of xbox service start type
        Args:
            value: Value to set for the xboxServicesLiveGameSaveServiceStartupMode property.
        """
        self._xbox_services_live_game_save_service_startup_mode = value
    
    @property
    def xbox_services_live_networking_service_startup_mode(self,) -> Optional[service_start_type.ServiceStartType]:
        """
        Gets the xboxServicesLiveNetworkingServiceStartupMode property value. Possible values of xbox service start type
        Returns: Optional[service_start_type.ServiceStartType]
        """
        return self._xbox_services_live_networking_service_startup_mode
    
    @xbox_services_live_networking_service_startup_mode.setter
    def xbox_services_live_networking_service_startup_mode(self,value: Optional[service_start_type.ServiceStartType] = None) -> None:
        """
        Sets the xboxServicesLiveNetworkingServiceStartupMode property value. Possible values of xbox service start type
        Args:
            value: Value to set for the xboxServicesLiveNetworkingServiceStartupMode property.
        """
        self._xbox_services_live_networking_service_startup_mode = value
    

