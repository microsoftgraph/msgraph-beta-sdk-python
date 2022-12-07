from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_device_owner_app_auto_update_policy_type = lazy_import('msgraph.generated.models.android_device_owner_app_auto_update_policy_type')
android_device_owner_battery_plugged_mode = lazy_import('msgraph.generated.models.android_device_owner_battery_plugged_mode')
android_device_owner_cross_profile_data_sharing = lazy_import('msgraph.generated.models.android_device_owner_cross_profile_data_sharing')
android_device_owner_default_app_permission_policy_type = lazy_import('msgraph.generated.models.android_device_owner_default_app_permission_policy_type')
android_device_owner_enrollment_profile_type = lazy_import('msgraph.generated.models.android_device_owner_enrollment_profile_type')
android_device_owner_global_proxy = lazy_import('msgraph.generated.models.android_device_owner_global_proxy')
android_device_owner_kiosk_customization_status_bar = lazy_import('msgraph.generated.models.android_device_owner_kiosk_customization_status_bar')
android_device_owner_kiosk_customization_system_navigation = lazy_import('msgraph.generated.models.android_device_owner_kiosk_customization_system_navigation')
android_device_owner_kiosk_mode_app_position_item = lazy_import('msgraph.generated.models.android_device_owner_kiosk_mode_app_position_item')
android_device_owner_kiosk_mode_folder_icon = lazy_import('msgraph.generated.models.android_device_owner_kiosk_mode_folder_icon')
android_device_owner_kiosk_mode_icon_size = lazy_import('msgraph.generated.models.android_device_owner_kiosk_mode_icon_size')
android_device_owner_kiosk_mode_managed_folder = lazy_import('msgraph.generated.models.android_device_owner_kiosk_mode_managed_folder')
android_device_owner_kiosk_mode_screen_orientation = lazy_import('msgraph.generated.models.android_device_owner_kiosk_mode_screen_orientation')
android_device_owner_play_store_mode = lazy_import('msgraph.generated.models.android_device_owner_play_store_mode')
android_device_owner_required_password_type = lazy_import('msgraph.generated.models.android_device_owner_required_password_type')
android_device_owner_required_password_unlock = lazy_import('msgraph.generated.models.android_device_owner_required_password_unlock')
android_device_owner_system_update_freeze_period = lazy_import('msgraph.generated.models.android_device_owner_system_update_freeze_period')
android_device_owner_system_update_install_type = lazy_import('msgraph.generated.models.android_device_owner_system_update_install_type')
android_device_owner_user_facing_message = lazy_import('msgraph.generated.models.android_device_owner_user_facing_message')
android_device_owner_virtual_home_button_type = lazy_import('msgraph.generated.models.android_device_owner_virtual_home_button_type')
android_keyguard_feature = lazy_import('msgraph.generated.models.android_keyguard_feature')
app_list_item = lazy_import('msgraph.generated.models.app_list_item')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
kiosk_mode_managed_home_screen_pin_complexity = lazy_import('msgraph.generated.models.kiosk_mode_managed_home_screen_pin_complexity')
kiosk_mode_type = lazy_import('msgraph.generated.models.kiosk_mode_type')
microsoft_launcher_dock_presence = lazy_import('msgraph.generated.models.microsoft_launcher_dock_presence')
microsoft_launcher_search_bar_placement = lazy_import('msgraph.generated.models.microsoft_launcher_search_bar_placement')
personal_profile_personal_play_store_mode = lazy_import('msgraph.generated.models.personal_profile_personal_play_store_mode')

class AndroidDeviceOwnerGeneralDeviceConfiguration(device_configuration.DeviceConfiguration):
    @property
    def accounts_block_modification(self,) -> Optional[bool]:
        """
        Gets the accountsBlockModification property value. Indicates whether or not adding or removing accounts is disabled.
        Returns: Optional[bool]
        """
        return self._accounts_block_modification
    
    @accounts_block_modification.setter
    def accounts_block_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the accountsBlockModification property value. Indicates whether or not adding or removing accounts is disabled.
        Args:
            value: Value to set for the accountsBlockModification property.
        """
        self._accounts_block_modification = value
    
    @property
    def apps_allow_install_from_unknown_sources(self,) -> Optional[bool]:
        """
        Gets the appsAllowInstallFromUnknownSources property value. Indicates whether or not the user is allowed to enable to unknown sources setting.
        Returns: Optional[bool]
        """
        return self._apps_allow_install_from_unknown_sources
    
    @apps_allow_install_from_unknown_sources.setter
    def apps_allow_install_from_unknown_sources(self,value: Optional[bool] = None) -> None:
        """
        Sets the appsAllowInstallFromUnknownSources property value. Indicates whether or not the user is allowed to enable to unknown sources setting.
        Args:
            value: Value to set for the appsAllowInstallFromUnknownSources property.
        """
        self._apps_allow_install_from_unknown_sources = value
    
    @property
    def apps_auto_update_policy(self,) -> Optional[android_device_owner_app_auto_update_policy_type.AndroidDeviceOwnerAppAutoUpdatePolicyType]:
        """
        Gets the appsAutoUpdatePolicy property value. Indicates the value of the app auto update policy. Possible values are: notConfigured, userChoice, never, wiFiOnly, always.
        Returns: Optional[android_device_owner_app_auto_update_policy_type.AndroidDeviceOwnerAppAutoUpdatePolicyType]
        """
        return self._apps_auto_update_policy
    
    @apps_auto_update_policy.setter
    def apps_auto_update_policy(self,value: Optional[android_device_owner_app_auto_update_policy_type.AndroidDeviceOwnerAppAutoUpdatePolicyType] = None) -> None:
        """
        Sets the appsAutoUpdatePolicy property value. Indicates the value of the app auto update policy. Possible values are: notConfigured, userChoice, never, wiFiOnly, always.
        Args:
            value: Value to set for the appsAutoUpdatePolicy property.
        """
        self._apps_auto_update_policy = value
    
    @property
    def apps_default_permission_policy(self,) -> Optional[android_device_owner_default_app_permission_policy_type.AndroidDeviceOwnerDefaultAppPermissionPolicyType]:
        """
        Gets the appsDefaultPermissionPolicy property value. Indicates the permission policy for requests for runtime permissions if one is not defined for the app specifically. Possible values are: deviceDefault, prompt, autoGrant, autoDeny.
        Returns: Optional[android_device_owner_default_app_permission_policy_type.AndroidDeviceOwnerDefaultAppPermissionPolicyType]
        """
        return self._apps_default_permission_policy
    
    @apps_default_permission_policy.setter
    def apps_default_permission_policy(self,value: Optional[android_device_owner_default_app_permission_policy_type.AndroidDeviceOwnerDefaultAppPermissionPolicyType] = None) -> None:
        """
        Sets the appsDefaultPermissionPolicy property value. Indicates the permission policy for requests for runtime permissions if one is not defined for the app specifically. Possible values are: deviceDefault, prompt, autoGrant, autoDeny.
        Args:
            value: Value to set for the appsDefaultPermissionPolicy property.
        """
        self._apps_default_permission_policy = value
    
    @property
    def apps_recommend_skipping_first_use_hints(self,) -> Optional[bool]:
        """
        Gets the appsRecommendSkippingFirstUseHints property value. Whether or not to recommend all apps skip any first-time-use hints they may have added.
        Returns: Optional[bool]
        """
        return self._apps_recommend_skipping_first_use_hints
    
    @apps_recommend_skipping_first_use_hints.setter
    def apps_recommend_skipping_first_use_hints(self,value: Optional[bool] = None) -> None:
        """
        Sets the appsRecommendSkippingFirstUseHints property value. Whether or not to recommend all apps skip any first-time-use hints they may have added.
        Args:
            value: Value to set for the appsRecommendSkippingFirstUseHints property.
        """
        self._apps_recommend_skipping_first_use_hints = value
    
    @property
    def azure_ad_shared_device_data_clear_apps(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the azureAdSharedDeviceDataClearApps property value. A list of managed apps that will have their data cleared during a global sign-out in AAD shared device mode. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._azure_ad_shared_device_data_clear_apps
    
    @azure_ad_shared_device_data_clear_apps.setter
    def azure_ad_shared_device_data_clear_apps(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the azureAdSharedDeviceDataClearApps property value. A list of managed apps that will have their data cleared during a global sign-out in AAD shared device mode. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the azureAdSharedDeviceDataClearApps property.
        """
        self._azure_ad_shared_device_data_clear_apps = value
    
    @property
    def bluetooth_block_configuration(self,) -> Optional[bool]:
        """
        Gets the bluetoothBlockConfiguration property value. Indicates whether or not to block a user from configuring bluetooth.
        Returns: Optional[bool]
        """
        return self._bluetooth_block_configuration
    
    @bluetooth_block_configuration.setter
    def bluetooth_block_configuration(self,value: Optional[bool] = None) -> None:
        """
        Sets the bluetoothBlockConfiguration property value. Indicates whether or not to block a user from configuring bluetooth.
        Args:
            value: Value to set for the bluetoothBlockConfiguration property.
        """
        self._bluetooth_block_configuration = value
    
    @property
    def bluetooth_block_contact_sharing(self,) -> Optional[bool]:
        """
        Gets the bluetoothBlockContactSharing property value. Indicates whether or not to block a user from sharing contacts via bluetooth.
        Returns: Optional[bool]
        """
        return self._bluetooth_block_contact_sharing
    
    @bluetooth_block_contact_sharing.setter
    def bluetooth_block_contact_sharing(self,value: Optional[bool] = None) -> None:
        """
        Sets the bluetoothBlockContactSharing property value. Indicates whether or not to block a user from sharing contacts via bluetooth.
        Args:
            value: Value to set for the bluetoothBlockContactSharing property.
        """
        self._bluetooth_block_contact_sharing = value
    
    @property
    def camera_blocked(self,) -> Optional[bool]:
        """
        Gets the cameraBlocked property value. Indicates whether or not to disable the use of the camera.
        Returns: Optional[bool]
        """
        return self._camera_blocked
    
    @camera_blocked.setter
    def camera_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the cameraBlocked property value. Indicates whether or not to disable the use of the camera.
        Args:
            value: Value to set for the cameraBlocked property.
        """
        self._camera_blocked = value
    
    @property
    def cellular_block_wi_fi_tethering(self,) -> Optional[bool]:
        """
        Gets the cellularBlockWiFiTethering property value. Indicates whether or not to block Wi-Fi tethering.
        Returns: Optional[bool]
        """
        return self._cellular_block_wi_fi_tethering
    
    @cellular_block_wi_fi_tethering.setter
    def cellular_block_wi_fi_tethering(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockWiFiTethering property value. Indicates whether or not to block Wi-Fi tethering.
        Args:
            value: Value to set for the cellularBlockWiFiTethering property.
        """
        self._cellular_block_wi_fi_tethering = value
    
    @property
    def certificate_credential_configuration_disabled(self,) -> Optional[bool]:
        """
        Gets the certificateCredentialConfigurationDisabled property value. Indicates whether or not to block users from any certificate credential configuration.
        Returns: Optional[bool]
        """
        return self._certificate_credential_configuration_disabled
    
    @certificate_credential_configuration_disabled.setter
    def certificate_credential_configuration_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the certificateCredentialConfigurationDisabled property value. Indicates whether or not to block users from any certificate credential configuration.
        Args:
            value: Value to set for the certificateCredentialConfigurationDisabled property.
        """
        self._certificate_credential_configuration_disabled = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceOwnerGeneralDeviceConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceOwnerGeneralDeviceConfiguration"
        # Indicates whether or not adding or removing accounts is disabled.
        self._accounts_block_modification: Optional[bool] = None
        # Indicates whether or not the user is allowed to enable to unknown sources setting.
        self._apps_allow_install_from_unknown_sources: Optional[bool] = None
        # Indicates the value of the app auto update policy. Possible values are: notConfigured, userChoice, never, wiFiOnly, always.
        self._apps_auto_update_policy: Optional[android_device_owner_app_auto_update_policy_type.AndroidDeviceOwnerAppAutoUpdatePolicyType] = None
        # Indicates the permission policy for requests for runtime permissions if one is not defined for the app specifically. Possible values are: deviceDefault, prompt, autoGrant, autoDeny.
        self._apps_default_permission_policy: Optional[android_device_owner_default_app_permission_policy_type.AndroidDeviceOwnerDefaultAppPermissionPolicyType] = None
        # Whether or not to recommend all apps skip any first-time-use hints they may have added.
        self._apps_recommend_skipping_first_use_hints: Optional[bool] = None
        # A list of managed apps that will have their data cleared during a global sign-out in AAD shared device mode. This collection can contain a maximum of 500 elements.
        self._azure_ad_shared_device_data_clear_apps: Optional[List[app_list_item.AppListItem]] = None
        # Indicates whether or not to block a user from configuring bluetooth.
        self._bluetooth_block_configuration: Optional[bool] = None
        # Indicates whether or not to block a user from sharing contacts via bluetooth.
        self._bluetooth_block_contact_sharing: Optional[bool] = None
        # Indicates whether or not to disable the use of the camera.
        self._camera_blocked: Optional[bool] = None
        # Indicates whether or not to block Wi-Fi tethering.
        self._cellular_block_wi_fi_tethering: Optional[bool] = None
        # Indicates whether or not to block users from any certificate credential configuration.
        self._certificate_credential_configuration_disabled: Optional[bool] = None
        # Indicates whether or not text copied from one profile (personal or work) can be pasted in the other.
        self._cross_profile_policies_allow_copy_paste: Optional[bool] = None
        # Indicates whether data from one profile (personal or work) can be shared with apps in the other profile. Possible values are: notConfigured, crossProfileDataSharingBlocked, dataSharingFromWorkToPersonalBlocked, crossProfileDataSharingAllowed, unkownFutureValue.
        self._cross_profile_policies_allow_data_sharing: Optional[android_device_owner_cross_profile_data_sharing.AndroidDeviceOwnerCrossProfileDataSharing] = None
        # Indicates whether or not contacts stored in work profile are shown in personal profile contact searches/incoming calls.
        self._cross_profile_policies_show_work_contacts_in_personal_profile: Optional[bool] = None
        # Indicates whether or not to block a user from data roaming.
        self._data_roaming_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from manually changing the date or time on the device
        self._date_time_configuration_blocked: Optional[bool] = None
        # Represents the customized detailed help text provided to users when they attempt to modify managed settings on their device.
        self._detailed_help_text: Optional[android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage] = None
        # Represents the customized lock screen message provided to users when they attempt to modify managed settings on their device.
        self._device_owner_lock_screen_message: Optional[android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage] = None
        # Android Device Owner Enrollment Profile types.
        self._enrollment_profile: Optional[android_device_owner_enrollment_profile_type.AndroidDeviceOwnerEnrollmentProfileType] = None
        # Indicates whether or not the factory reset option in settings is disabled.
        self._factory_reset_blocked: Optional[bool] = None
        # List of Google account emails that will be required to authenticate after a device is factory reset before it can be set up.
        self._factory_reset_device_administrator_emails: Optional[List[str]] = None
        # Proxy is set up directly with host, port and excluded hosts.
        self._global_proxy: Optional[android_device_owner_global_proxy.AndroidDeviceOwnerGlobalProxy] = None
        # Indicates whether or not google accounts will be blocked.
        self._google_accounts_blocked: Optional[bool] = None
        # Indicates whether a user can access the device's Settings app while in Kiosk Mode.
        self._kiosk_customization_device_settings_blocked: Optional[bool] = None
        # Whether the power menu is shown when a user long presses the Power button of a device in Kiosk Mode.
        self._kiosk_customization_power_button_actions_blocked: Optional[bool] = None
        # Indicates whether system info and notifications are disabled in Kiosk Mode. Possible values are: notConfigured, notificationsAndSystemInfoEnabled, systemInfoOnly.
        self._kiosk_customization_status_bar: Optional[android_device_owner_kiosk_customization_status_bar.AndroidDeviceOwnerKioskCustomizationStatusBar] = None
        # Indicates whether system error dialogs for crashed or unresponsive apps are shown in Kiosk Mode.
        self._kiosk_customization_system_error_warnings: Optional[bool] = None
        # Indicates which navigation features are enabled in Kiosk Mode. Possible values are: notConfigured, navigationEnabled, homeButtonOnly.
        self._kiosk_customization_system_navigation: Optional[android_device_owner_kiosk_customization_system_navigation.AndroidDeviceOwnerKioskCustomizationSystemNavigation] = None
        # Whether or not to enable app ordering in Kiosk Mode.
        self._kiosk_mode_app_order_enabled: Optional[bool] = None
        # The ordering of items on Kiosk Mode Managed Home Screen. This collection can contain a maximum of 500 elements.
        self._kiosk_mode_app_positions: Optional[List[android_device_owner_kiosk_mode_app_position_item.AndroidDeviceOwnerKioskModeAppPositionItem]] = None
        # A list of managed apps that will be shown when the device is in Kiosk Mode. This collection can contain a maximum of 500 elements.
        self._kiosk_mode_apps: Optional[List[app_list_item.AppListItem]] = None
        # Whether or not to alphabetize applications within a folder in Kiosk Mode.
        self._kiosk_mode_apps_in_folder_ordered_by_name: Optional[bool] = None
        # Whether or not to allow a user to configure Bluetooth settings in Kiosk Mode.
        self._kiosk_mode_bluetooth_configuration_enabled: Optional[bool] = None
        # Whether or not to allow a user to easy access to the debug menu in Kiosk Mode.
        self._kiosk_mode_debug_menu_easy_access_enabled: Optional[bool] = None
        # Exit code to allow a user to escape from Kiosk Mode when the device is in Kiosk Mode.
        self._kiosk_mode_exit_code: Optional[str] = None
        # Whether or not to allow a user to use the flashlight in Kiosk Mode.
        self._kiosk_mode_flashlight_configuration_enabled: Optional[bool] = None
        # Folder icon configuration for managed home screen in Kiosk Mode. Possible values are: notConfigured, darkSquare, darkCircle, lightSquare, lightCircle.
        self._kiosk_mode_folder_icon: Optional[android_device_owner_kiosk_mode_folder_icon.AndroidDeviceOwnerKioskModeFolderIcon] = None
        # Number of rows for Managed Home Screen grid with app ordering enabled in Kiosk Mode. Valid values 1 to 9999999
        self._kiosk_mode_grid_height: Optional[int] = None
        # Number of columns for Managed Home Screen grid with app ordering enabled in Kiosk Mode. Valid values 1 to 9999999
        self._kiosk_mode_grid_width: Optional[int] = None
        # Icon size configuration for managed home screen in Kiosk Mode. Possible values are: notConfigured, smallest, small, regular, large, largest.
        self._kiosk_mode_icon_size: Optional[android_device_owner_kiosk_mode_icon_size.AndroidDeviceOwnerKioskModeIconSize] = None
        # Whether or not to lock home screen to the end user in Kiosk Mode.
        self._kiosk_mode_lock_home_screen: Optional[bool] = None
        # A list of managed folders for a device in Kiosk Mode. This collection can contain a maximum of 500 elements.
        self._kiosk_mode_managed_folders: Optional[List[android_device_owner_kiosk_mode_managed_folder.AndroidDeviceOwnerKioskModeManagedFolder]] = None
        # Whether or not to automatically sign-out of MHS and Shared device mode applications after inactive for Managed Home Screen.
        self._kiosk_mode_managed_home_screen_auto_signout: Optional[bool] = None
        # Number of seconds to give user notice before automatically signing them out for Managed Home Screen. Valid values 0 to 9999999
        self._kiosk_mode_managed_home_screen_inactive_sign_out_delay_in_seconds: Optional[int] = None
        # Number of seconds device is inactive before automatically signing user out for Managed Home Screen. Valid values 0 to 9999999
        self._kiosk_mode_managed_home_screen_inactive_sign_out_notice_in_seconds: Optional[int] = None
        # Complexity of PIN for sign-in session for Managed Home Screen. Possible values are: notConfigured, simple, complex.
        self._kiosk_mode_managed_home_screen_pin_complexity: Optional[kiosk_mode_managed_home_screen_pin_complexity.KioskModeManagedHomeScreenPinComplexity] = None
        # Whether or not require user to set a PIN for sign-in session for Managed Home Screen.
        self._kiosk_mode_managed_home_screen_pin_required: Optional[bool] = None
        # Whether or not required user to enter session PIN if screensaver has appeared for Managed Home Screen.
        self._kiosk_mode_managed_home_screen_pin_required_to_resume: Optional[bool] = None
        # Custom URL background for sign-in screen for Managed Home Screen.
        self._kiosk_mode_managed_home_screen_sign_in_background: Optional[str] = None
        # Custom URL branding logo for sign-in screen and session pin page for Managed Home Screen.
        self._kiosk_mode_managed_home_screen_sign_in_branding_logo: Optional[str] = None
        # Whether or not show sign-in screen for Managed Home Screen.
        self._kiosk_mode_managed_home_screen_sign_in_enabled: Optional[bool] = None
        # Whether or not to display the Managed Settings entry point on the managed home screen in Kiosk Mode.
        self._kiosk_mode_managed_settings_entry_disabled: Optional[bool] = None
        # Whether or not to allow a user to change the media volume in Kiosk Mode.
        self._kiosk_mode_media_volume_configuration_enabled: Optional[bool] = None
        # Screen orientation configuration for managed home screen in Kiosk Mode. Possible values are: notConfigured, portrait, landscape, autoRotate.
        self._kiosk_mode_screen_orientation: Optional[android_device_owner_kiosk_mode_screen_orientation.AndroidDeviceOwnerKioskModeScreenOrientation] = None
        # Whether or not to enable screen saver mode or not in Kiosk Mode.
        self._kiosk_mode_screen_saver_configuration_enabled: Optional[bool] = None
        # Whether or not the device screen should show the screen saver if audio/video is playing in Kiosk Mode.
        self._kiosk_mode_screen_saver_detect_media_disabled: Optional[bool] = None
        # The number of seconds that the device will display the screen saver for in Kiosk Mode. Valid values 0 to 9999999
        self._kiosk_mode_screen_saver_display_time_in_seconds: Optional[int] = None
        # URL for an image that will be the device's screen saver in Kiosk Mode.
        self._kiosk_mode_screen_saver_image_url: Optional[str] = None
        # The number of seconds the device needs to be inactive for before the screen saver is shown in Kiosk Mode. Valid values 1 to 9999999
        self._kiosk_mode_screen_saver_start_delay_in_seconds: Optional[int] = None
        # Whether or not to display application notification badges in Kiosk Mode.
        self._kiosk_mode_show_app_notification_badge: Optional[bool] = None
        # Whether or not to allow a user to access basic device information.
        self._kiosk_mode_show_device_info: Optional[bool] = None
        # Whether or not to use single app kiosk mode or multi-app kiosk mode. Possible values are: notConfigured, singleAppMode, multiAppMode.
        self._kiosk_mode_use_managed_home_screen_app: Optional[kiosk_mode_type.KioskModeType] = None
        # Whether or not to display a virtual home button when the device is in Kiosk Mode.
        self._kiosk_mode_virtual_home_button_enabled: Optional[bool] = None
        # Indicates whether the virtual home button is a swipe up home button or a floating home button. Possible values are: notConfigured, swipeUp, floating.
        self._kiosk_mode_virtual_home_button_type: Optional[android_device_owner_virtual_home_button_type.AndroidDeviceOwnerVirtualHomeButtonType] = None
        # URL to a publicly accessible image to use for the wallpaper when the device is in Kiosk Mode.
        self._kiosk_mode_wallpaper_url: Optional[str] = None
        # The restricted set of WIFI SSIDs available for the user to configure in Kiosk Mode. This collection can contain a maximum of 500 elements.
        self._kiosk_mode_wifi_allowed_ssids: Optional[List[str]] = None
        # Whether or not to allow a user to configure Wi-Fi settings in Kiosk Mode.
        self._kiosk_mode_wi_fi_configuration_enabled: Optional[bool] = None
        # Indicates whether or not to block unmuting the microphone on the device.
        self._microphone_force_mute: Optional[bool] = None
        # Indicates whether or not to you want configure Microsoft Launcher.
        self._microsoft_launcher_configuration_enabled: Optional[bool] = None
        # Indicates whether or not the user can modify the wallpaper to personalize their device.
        self._microsoft_launcher_custom_wallpaper_allow_user_modification: Optional[bool] = None
        # Indicates whether or not to configure the wallpaper on the targeted devices.
        self._microsoft_launcher_custom_wallpaper_enabled: Optional[bool] = None
        # Indicates the URL for the image file to use as the wallpaper on the targeted devices.
        self._microsoft_launcher_custom_wallpaper_image_url: Optional[str] = None
        # Indicates whether or not the user can modify the device dock configuration on the device.
        self._microsoft_launcher_dock_presence_allow_user_modification: Optional[bool] = None
        # Indicates whether or not you want to configure the device dock. Possible values are: notConfigured, show, hide, disabled.
        self._microsoft_launcher_dock_presence_configuration: Optional[microsoft_launcher_dock_presence.MicrosoftLauncherDockPresence] = None
        # Indicates whether or not the user can modify the launcher feed on the device.
        self._microsoft_launcher_feed_allow_user_modification: Optional[bool] = None
        # Indicates whether or not you want to enable the launcher feed on the device.
        self._microsoft_launcher_feed_enabled: Optional[bool] = None
        # Indicates the search bar placement configuration on the device. Possible values are: notConfigured, top, bottom, hide.
        self._microsoft_launcher_search_bar_placement_configuration: Optional[microsoft_launcher_search_bar_placement.MicrosoftLauncherSearchBarPlacement] = None
        # Indicates whether or not the device will allow connecting to a temporary network connection at boot time.
        self._network_escape_hatch_allowed: Optional[bool] = None
        # Indicates whether or not to block NFC outgoing beam.
        self._nfc_block_outgoing_beam: Optional[bool] = None
        # Indicates whether or not the keyguard is disabled.
        self._password_block_keyguard: Optional[bool] = None
        # List of device keyguard features to block. This collection can contain a maximum of 11 elements.
        self._password_block_keyguard_features: Optional[List[android_keyguard_feature.AndroidKeyguardFeature]] = None
        # Indicates the amount of time that a password can be set for before it expires and a new password will be required. Valid values 1 to 365
        self._password_expiration_days: Optional[int] = None
        # Indicates the minimum length of the password required on the device. Valid values 4 to 16
        self._password_minimum_length: Optional[int] = None
        # Indicates the minimum number of letter characters required for device password. Valid values 1 to 16
        self._password_minimum_letter_characters: Optional[int] = None
        # Indicates the minimum number of lower case characters required for device password. Valid values 1 to 16
        self._password_minimum_lower_case_characters: Optional[int] = None
        # Indicates the minimum number of non-letter characters required for device password. Valid values 1 to 16
        self._password_minimum_non_letter_characters: Optional[int] = None
        # Indicates the minimum number of numeric characters required for device password. Valid values 1 to 16
        self._password_minimum_numeric_characters: Optional[int] = None
        # Indicates the minimum number of symbol characters required for device password. Valid values 1 to 16
        self._password_minimum_symbol_characters: Optional[int] = None
        # Indicates the minimum number of upper case letter characters required for device password. Valid values 1 to 16
        self._password_minimum_upper_case_characters: Optional[int] = None
        # Minutes of inactivity before the screen times out.
        self._password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
        # Indicates the length of password history, where the user will not be able to enter a new password that is the same as any password in the history. Valid values 0 to 24
        self._password_previous_password_count_to_block: Optional[int] = None
        # Indicates the minimum password quality required on the device. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
        self._password_required_type: Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType] = None
        # Indicates the timeout period after which a device must be unlocked using a form of strong authentication. Possible values are: deviceDefault, daily, unkownFutureValue.
        self._password_require_unlock: Optional[android_device_owner_required_password_unlock.AndroidDeviceOwnerRequiredPasswordUnlock] = None
        # Indicates the number of times a user can enter an incorrect password before the device is wiped. Valid values 4 to 11
        self._password_sign_in_failure_count_before_factory_reset: Optional[int] = None
        # Indicates whether the user can install apps from unknown sources on the personal profile.
        self._personal_profile_apps_allow_install_from_unknown_sources: Optional[bool] = None
        # Indicates whether to disable the use of the camera on the personal profile.
        self._personal_profile_camera_blocked: Optional[bool] = None
        # Policy applied to applications in the personal profile. This collection can contain a maximum of 500 elements.
        self._personal_profile_personal_applications: Optional[List[app_list_item.AppListItem]] = None
        # Used together with PersonalProfilePersonalApplications to control how apps in the personal profile are allowed or blocked. Possible values are: notConfigured, blockedApps, allowedApps.
        self._personal_profile_play_store_mode: Optional[personal_profile_personal_play_store_mode.PersonalProfilePersonalPlayStoreMode] = None
        # Indicates whether to disable the capability to take screenshots on the personal profile.
        self._personal_profile_screen_capture_blocked: Optional[bool] = None
        # Indicates the Play Store mode of the device. Possible values are: notConfigured, allowList, blockList.
        self._play_store_mode: Optional[android_device_owner_play_store_mode.AndroidDeviceOwnerPlayStoreMode] = None
        # Indicates whether or not to disable the capability to take screenshots.
        self._screen_capture_blocked: Optional[bool] = None
        # Represents the security common criteria mode enabled provided to users when they attempt to modify managed settings on their device.
        self._security_common_criteria_mode_enabled: Optional[bool] = None
        # Indicates whether or not the user is allowed to access developer settings like developer options and safe boot on the device.
        self._security_developer_settings_enabled: Optional[bool] = None
        # Indicates whether or not verify apps is required.
        self._security_require_verify_apps: Optional[bool] = None
        # Represents the customized short help text provided to users when they attempt to modify managed settings on their device.
        self._short_help_text: Optional[android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage] = None
        # Indicates whether or the status bar is disabled, including notifications, quick settings and other screen overlays.
        self._status_bar_blocked: Optional[bool] = None
        # List of modes in which the device's display will stay powered-on. This collection can contain a maximum of 4 elements.
        self._stay_on_modes: Optional[List[android_device_owner_battery_plugged_mode.AndroidDeviceOwnerBatteryPluggedMode]] = None
        # Indicates whether or not to allow USB mass storage.
        self._storage_allow_usb: Optional[bool] = None
        # Indicates whether or not to block external media.
        self._storage_block_external_media: Optional[bool] = None
        # Indicates whether or not to block USB file transfer.
        self._storage_block_usb_file_transfer: Optional[bool] = None
        # Indicates the annually repeating time periods during which system updates are postponed. This collection can contain a maximum of 500 elements.
        self._system_update_freeze_periods: Optional[List[android_device_owner_system_update_freeze_period.AndroidDeviceOwnerSystemUpdateFreezePeriod]] = None
        # The type of system update configuration. Possible values are: deviceDefault, postpone, windowed, automatic.
        self._system_update_install_type: Optional[android_device_owner_system_update_install_type.AndroidDeviceOwnerSystemUpdateInstallType] = None
        # Indicates the number of minutes after midnight that the system update window ends. Valid values 0 to 1440
        self._system_update_window_end_minutes_after_midnight: Optional[int] = None
        # Indicates the number of minutes after midnight that the system update window starts. Valid values 0 to 1440
        self._system_update_window_start_minutes_after_midnight: Optional[int] = None
        # Whether or not to block Android system prompt windows, like toasts, phone activities, and system alerts.
        self._system_windows_blocked: Optional[bool] = None
        # Indicates whether or not adding users and profiles is disabled.
        self._users_block_add: Optional[bool] = None
        # Indicates whether or not to disable removing other users from the device.
        self._users_block_remove: Optional[bool] = None
        # Indicates whether or not adjusting the master volume is disabled.
        self._volume_block_adjustment: Optional[bool] = None
        # If an always on VPN package name is specified, whether or not to lock network traffic when that VPN is disconnected.
        self._vpn_always_on_lockdown_mode: Optional[bool] = None
        # Android app package name for app that will handle an always-on VPN connection.
        self._vpn_always_on_package_identifier: Optional[str] = None
        # Indicates whether or not to block the user from editing the wifi connection settings.
        self._wifi_block_edit_configurations: Optional[bool] = None
        # Indicates whether or not to block the user from editing just the networks defined by the policy.
        self._wifi_block_edit_policy_defined_configurations: Optional[bool] = None
        # Indicates the number of days that a work profile password can be set before it expires and a new password will be required. Valid values 1 to 365
        self._work_profile_password_expiration_days: Optional[int] = None
        # Indicates the minimum length of the work profile password. Valid values 4 to 16
        self._work_profile_password_minimum_length: Optional[int] = None
        # Indicates the minimum number of letter characters required for the work profile password. Valid values 1 to 16
        self._work_profile_password_minimum_letter_characters: Optional[int] = None
        # Indicates the minimum number of lower-case characters required for the work profile password. Valid values 1 to 16
        self._work_profile_password_minimum_lower_case_characters: Optional[int] = None
        # Indicates the minimum number of non-letter characters required for the work profile password. Valid values 1 to 16
        self._work_profile_password_minimum_non_letter_characters: Optional[int] = None
        # Indicates the minimum number of numeric characters required for the work profile password. Valid values 1 to 16
        self._work_profile_password_minimum_numeric_characters: Optional[int] = None
        # Indicates the minimum number of symbol characters required for the work profile password. Valid values 1 to 16
        self._work_profile_password_minimum_symbol_characters: Optional[int] = None
        # Indicates the minimum number of upper-case letter characters required for the work profile password. Valid values 1 to 16
        self._work_profile_password_minimum_upper_case_characters: Optional[int] = None
        # Indicates the length of the work profile password history, where the user will not be able to enter a new password that is the same as any password in the history. Valid values 0 to 24
        self._work_profile_password_previous_password_count_to_block: Optional[int] = None
        # Indicates the minimum password quality required on the work profile password. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
        self._work_profile_password_required_type: Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType] = None
        # Indicates the timeout period after which a work profile must be unlocked using a form of strong authentication. Possible values are: deviceDefault, daily, unkownFutureValue.
        self._work_profile_password_require_unlock: Optional[android_device_owner_required_password_unlock.AndroidDeviceOwnerRequiredPasswordUnlock] = None
        # Indicates the number of times a user can enter an incorrect work profile password before the device is wiped. Valid values 4 to 11
        self._work_profile_password_sign_in_failure_count_before_factory_reset: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerGeneralDeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerGeneralDeviceConfiguration()
    
    @property
    def cross_profile_policies_allow_copy_paste(self,) -> Optional[bool]:
        """
        Gets the crossProfilePoliciesAllowCopyPaste property value. Indicates whether or not text copied from one profile (personal or work) can be pasted in the other.
        Returns: Optional[bool]
        """
        return self._cross_profile_policies_allow_copy_paste
    
    @cross_profile_policies_allow_copy_paste.setter
    def cross_profile_policies_allow_copy_paste(self,value: Optional[bool] = None) -> None:
        """
        Sets the crossProfilePoliciesAllowCopyPaste property value. Indicates whether or not text copied from one profile (personal or work) can be pasted in the other.
        Args:
            value: Value to set for the crossProfilePoliciesAllowCopyPaste property.
        """
        self._cross_profile_policies_allow_copy_paste = value
    
    @property
    def cross_profile_policies_allow_data_sharing(self,) -> Optional[android_device_owner_cross_profile_data_sharing.AndroidDeviceOwnerCrossProfileDataSharing]:
        """
        Gets the crossProfilePoliciesAllowDataSharing property value. Indicates whether data from one profile (personal or work) can be shared with apps in the other profile. Possible values are: notConfigured, crossProfileDataSharingBlocked, dataSharingFromWorkToPersonalBlocked, crossProfileDataSharingAllowed, unkownFutureValue.
        Returns: Optional[android_device_owner_cross_profile_data_sharing.AndroidDeviceOwnerCrossProfileDataSharing]
        """
        return self._cross_profile_policies_allow_data_sharing
    
    @cross_profile_policies_allow_data_sharing.setter
    def cross_profile_policies_allow_data_sharing(self,value: Optional[android_device_owner_cross_profile_data_sharing.AndroidDeviceOwnerCrossProfileDataSharing] = None) -> None:
        """
        Sets the crossProfilePoliciesAllowDataSharing property value. Indicates whether data from one profile (personal or work) can be shared with apps in the other profile. Possible values are: notConfigured, crossProfileDataSharingBlocked, dataSharingFromWorkToPersonalBlocked, crossProfileDataSharingAllowed, unkownFutureValue.
        Args:
            value: Value to set for the crossProfilePoliciesAllowDataSharing property.
        """
        self._cross_profile_policies_allow_data_sharing = value
    
    @property
    def cross_profile_policies_show_work_contacts_in_personal_profile(self,) -> Optional[bool]:
        """
        Gets the crossProfilePoliciesShowWorkContactsInPersonalProfile property value. Indicates whether or not contacts stored in work profile are shown in personal profile contact searches/incoming calls.
        Returns: Optional[bool]
        """
        return self._cross_profile_policies_show_work_contacts_in_personal_profile
    
    @cross_profile_policies_show_work_contacts_in_personal_profile.setter
    def cross_profile_policies_show_work_contacts_in_personal_profile(self,value: Optional[bool] = None) -> None:
        """
        Sets the crossProfilePoliciesShowWorkContactsInPersonalProfile property value. Indicates whether or not contacts stored in work profile are shown in personal profile contact searches/incoming calls.
        Args:
            value: Value to set for the crossProfilePoliciesShowWorkContactsInPersonalProfile property.
        """
        self._cross_profile_policies_show_work_contacts_in_personal_profile = value
    
    @property
    def data_roaming_blocked(self,) -> Optional[bool]:
        """
        Gets the dataRoamingBlocked property value. Indicates whether or not to block a user from data roaming.
        Returns: Optional[bool]
        """
        return self._data_roaming_blocked
    
    @data_roaming_blocked.setter
    def data_roaming_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the dataRoamingBlocked property value. Indicates whether or not to block a user from data roaming.
        Args:
            value: Value to set for the dataRoamingBlocked property.
        """
        self._data_roaming_blocked = value
    
    @property
    def date_time_configuration_blocked(self,) -> Optional[bool]:
        """
        Gets the dateTimeConfigurationBlocked property value. Indicates whether or not to block the user from manually changing the date or time on the device
        Returns: Optional[bool]
        """
        return self._date_time_configuration_blocked
    
    @date_time_configuration_blocked.setter
    def date_time_configuration_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the dateTimeConfigurationBlocked property value. Indicates whether or not to block the user from manually changing the date or time on the device
        Args:
            value: Value to set for the dateTimeConfigurationBlocked property.
        """
        self._date_time_configuration_blocked = value
    
    @property
    def detailed_help_text(self,) -> Optional[android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage]:
        """
        Gets the detailedHelpText property value. Represents the customized detailed help text provided to users when they attempt to modify managed settings on their device.
        Returns: Optional[android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage]
        """
        return self._detailed_help_text
    
    @detailed_help_text.setter
    def detailed_help_text(self,value: Optional[android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage] = None) -> None:
        """
        Sets the detailedHelpText property value. Represents the customized detailed help text provided to users when they attempt to modify managed settings on their device.
        Args:
            value: Value to set for the detailedHelpText property.
        """
        self._detailed_help_text = value
    
    @property
    def device_owner_lock_screen_message(self,) -> Optional[android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage]:
        """
        Gets the deviceOwnerLockScreenMessage property value. Represents the customized lock screen message provided to users when they attempt to modify managed settings on their device.
        Returns: Optional[android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage]
        """
        return self._device_owner_lock_screen_message
    
    @device_owner_lock_screen_message.setter
    def device_owner_lock_screen_message(self,value: Optional[android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage] = None) -> None:
        """
        Sets the deviceOwnerLockScreenMessage property value. Represents the customized lock screen message provided to users when they attempt to modify managed settings on their device.
        Args:
            value: Value to set for the deviceOwnerLockScreenMessage property.
        """
        self._device_owner_lock_screen_message = value
    
    @property
    def enrollment_profile(self,) -> Optional[android_device_owner_enrollment_profile_type.AndroidDeviceOwnerEnrollmentProfileType]:
        """
        Gets the enrollmentProfile property value. Android Device Owner Enrollment Profile types.
        Returns: Optional[android_device_owner_enrollment_profile_type.AndroidDeviceOwnerEnrollmentProfileType]
        """
        return self._enrollment_profile
    
    @enrollment_profile.setter
    def enrollment_profile(self,value: Optional[android_device_owner_enrollment_profile_type.AndroidDeviceOwnerEnrollmentProfileType] = None) -> None:
        """
        Sets the enrollmentProfile property value. Android Device Owner Enrollment Profile types.
        Args:
            value: Value to set for the enrollmentProfile property.
        """
        self._enrollment_profile = value
    
    @property
    def factory_reset_blocked(self,) -> Optional[bool]:
        """
        Gets the factoryResetBlocked property value. Indicates whether or not the factory reset option in settings is disabled.
        Returns: Optional[bool]
        """
        return self._factory_reset_blocked
    
    @factory_reset_blocked.setter
    def factory_reset_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the factoryResetBlocked property value. Indicates whether or not the factory reset option in settings is disabled.
        Args:
            value: Value to set for the factoryResetBlocked property.
        """
        self._factory_reset_blocked = value
    
    @property
    def factory_reset_device_administrator_emails(self,) -> Optional[List[str]]:
        """
        Gets the factoryResetDeviceAdministratorEmails property value. List of Google account emails that will be required to authenticate after a device is factory reset before it can be set up.
        Returns: Optional[List[str]]
        """
        return self._factory_reset_device_administrator_emails
    
    @factory_reset_device_administrator_emails.setter
    def factory_reset_device_administrator_emails(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the factoryResetDeviceAdministratorEmails property value. List of Google account emails that will be required to authenticate after a device is factory reset before it can be set up.
        Args:
            value: Value to set for the factoryResetDeviceAdministratorEmails property.
        """
        self._factory_reset_device_administrator_emails = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "accounts_block_modification": lambda n : setattr(self, 'accounts_block_modification', n.get_bool_value()),
            "apps_allow_install_from_unknown_sources": lambda n : setattr(self, 'apps_allow_install_from_unknown_sources', n.get_bool_value()),
            "apps_auto_update_policy": lambda n : setattr(self, 'apps_auto_update_policy', n.get_enum_value(android_device_owner_app_auto_update_policy_type.AndroidDeviceOwnerAppAutoUpdatePolicyType)),
            "apps_default_permission_policy": lambda n : setattr(self, 'apps_default_permission_policy', n.get_enum_value(android_device_owner_default_app_permission_policy_type.AndroidDeviceOwnerDefaultAppPermissionPolicyType)),
            "apps_recommend_skipping_first_use_hints": lambda n : setattr(self, 'apps_recommend_skipping_first_use_hints', n.get_bool_value()),
            "azure_ad_shared_device_data_clear_apps": lambda n : setattr(self, 'azure_ad_shared_device_data_clear_apps', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "bluetooth_block_configuration": lambda n : setattr(self, 'bluetooth_block_configuration', n.get_bool_value()),
            "bluetooth_block_contact_sharing": lambda n : setattr(self, 'bluetooth_block_contact_sharing', n.get_bool_value()),
            "camera_blocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "cellular_block_wi_fi_tethering": lambda n : setattr(self, 'cellular_block_wi_fi_tethering', n.get_bool_value()),
            "certificate_credential_configuration_disabled": lambda n : setattr(self, 'certificate_credential_configuration_disabled', n.get_bool_value()),
            "cross_profile_policies_allow_copy_paste": lambda n : setattr(self, 'cross_profile_policies_allow_copy_paste', n.get_bool_value()),
            "cross_profile_policies_allow_data_sharing": lambda n : setattr(self, 'cross_profile_policies_allow_data_sharing', n.get_enum_value(android_device_owner_cross_profile_data_sharing.AndroidDeviceOwnerCrossProfileDataSharing)),
            "cross_profile_policies_show_work_contacts_in_personal_profile": lambda n : setattr(self, 'cross_profile_policies_show_work_contacts_in_personal_profile', n.get_bool_value()),
            "data_roaming_blocked": lambda n : setattr(self, 'data_roaming_blocked', n.get_bool_value()),
            "date_time_configuration_blocked": lambda n : setattr(self, 'date_time_configuration_blocked', n.get_bool_value()),
            "detailed_help_text": lambda n : setattr(self, 'detailed_help_text', n.get_object_value(android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage)),
            "device_owner_lock_screen_message": lambda n : setattr(self, 'device_owner_lock_screen_message', n.get_object_value(android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage)),
            "enrollment_profile": lambda n : setattr(self, 'enrollment_profile', n.get_enum_value(android_device_owner_enrollment_profile_type.AndroidDeviceOwnerEnrollmentProfileType)),
            "factory_reset_blocked": lambda n : setattr(self, 'factory_reset_blocked', n.get_bool_value()),
            "factory_reset_device_administrator_emails": lambda n : setattr(self, 'factory_reset_device_administrator_emails', n.get_collection_of_primitive_values(str)),
            "global_proxy": lambda n : setattr(self, 'global_proxy', n.get_object_value(android_device_owner_global_proxy.AndroidDeviceOwnerGlobalProxy)),
            "google_accounts_blocked": lambda n : setattr(self, 'google_accounts_blocked', n.get_bool_value()),
            "kiosk_customization_device_settings_blocked": lambda n : setattr(self, 'kiosk_customization_device_settings_blocked', n.get_bool_value()),
            "kiosk_customization_power_button_actions_blocked": lambda n : setattr(self, 'kiosk_customization_power_button_actions_blocked', n.get_bool_value()),
            "kiosk_customization_status_bar": lambda n : setattr(self, 'kiosk_customization_status_bar', n.get_enum_value(android_device_owner_kiosk_customization_status_bar.AndroidDeviceOwnerKioskCustomizationStatusBar)),
            "kiosk_customization_system_error_warnings": lambda n : setattr(self, 'kiosk_customization_system_error_warnings', n.get_bool_value()),
            "kiosk_customization_system_navigation": lambda n : setattr(self, 'kiosk_customization_system_navigation', n.get_enum_value(android_device_owner_kiosk_customization_system_navigation.AndroidDeviceOwnerKioskCustomizationSystemNavigation)),
            "kiosk_mode_app_order_enabled": lambda n : setattr(self, 'kiosk_mode_app_order_enabled', n.get_bool_value()),
            "kiosk_mode_app_positions": lambda n : setattr(self, 'kiosk_mode_app_positions', n.get_collection_of_object_values(android_device_owner_kiosk_mode_app_position_item.AndroidDeviceOwnerKioskModeAppPositionItem)),
            "kiosk_mode_apps": lambda n : setattr(self, 'kiosk_mode_apps', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "kiosk_mode_apps_in_folder_ordered_by_name": lambda n : setattr(self, 'kiosk_mode_apps_in_folder_ordered_by_name', n.get_bool_value()),
            "kiosk_mode_bluetooth_configuration_enabled": lambda n : setattr(self, 'kiosk_mode_bluetooth_configuration_enabled', n.get_bool_value()),
            "kiosk_mode_debug_menu_easy_access_enabled": lambda n : setattr(self, 'kiosk_mode_debug_menu_easy_access_enabled', n.get_bool_value()),
            "kiosk_mode_exit_code": lambda n : setattr(self, 'kiosk_mode_exit_code', n.get_str_value()),
            "kiosk_mode_flashlight_configuration_enabled": lambda n : setattr(self, 'kiosk_mode_flashlight_configuration_enabled', n.get_bool_value()),
            "kiosk_mode_folder_icon": lambda n : setattr(self, 'kiosk_mode_folder_icon', n.get_enum_value(android_device_owner_kiosk_mode_folder_icon.AndroidDeviceOwnerKioskModeFolderIcon)),
            "kiosk_mode_grid_height": lambda n : setattr(self, 'kiosk_mode_grid_height', n.get_int_value()),
            "kiosk_mode_grid_width": lambda n : setattr(self, 'kiosk_mode_grid_width', n.get_int_value()),
            "kiosk_mode_icon_size": lambda n : setattr(self, 'kiosk_mode_icon_size', n.get_enum_value(android_device_owner_kiosk_mode_icon_size.AndroidDeviceOwnerKioskModeIconSize)),
            "kiosk_mode_lock_home_screen": lambda n : setattr(self, 'kiosk_mode_lock_home_screen', n.get_bool_value()),
            "kiosk_mode_managed_folders": lambda n : setattr(self, 'kiosk_mode_managed_folders', n.get_collection_of_object_values(android_device_owner_kiosk_mode_managed_folder.AndroidDeviceOwnerKioskModeManagedFolder)),
            "kiosk_mode_managed_home_screen_auto_signout": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_auto_signout', n.get_bool_value()),
            "kiosk_mode_managed_home_screen_inactive_sign_out_delay_in_seconds": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_inactive_sign_out_delay_in_seconds', n.get_int_value()),
            "kiosk_mode_managed_home_screen_inactive_sign_out_notice_in_seconds": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_inactive_sign_out_notice_in_seconds', n.get_int_value()),
            "kiosk_mode_managed_home_screen_pin_complexity": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_pin_complexity', n.get_enum_value(kiosk_mode_managed_home_screen_pin_complexity.KioskModeManagedHomeScreenPinComplexity)),
            "kiosk_mode_managed_home_screen_pin_required": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_pin_required', n.get_bool_value()),
            "kiosk_mode_managed_home_screen_pin_required_to_resume": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_pin_required_to_resume', n.get_bool_value()),
            "kiosk_mode_managed_home_screen_sign_in_background": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_sign_in_background', n.get_str_value()),
            "kiosk_mode_managed_home_screen_sign_in_branding_logo": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_sign_in_branding_logo', n.get_str_value()),
            "kiosk_mode_managed_home_screen_sign_in_enabled": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_sign_in_enabled', n.get_bool_value()),
            "kiosk_mode_managed_settings_entry_disabled": lambda n : setattr(self, 'kiosk_mode_managed_settings_entry_disabled', n.get_bool_value()),
            "kiosk_mode_media_volume_configuration_enabled": lambda n : setattr(self, 'kiosk_mode_media_volume_configuration_enabled', n.get_bool_value()),
            "kiosk_mode_screen_orientation": lambda n : setattr(self, 'kiosk_mode_screen_orientation', n.get_enum_value(android_device_owner_kiosk_mode_screen_orientation.AndroidDeviceOwnerKioskModeScreenOrientation)),
            "kiosk_mode_screen_saver_configuration_enabled": lambda n : setattr(self, 'kiosk_mode_screen_saver_configuration_enabled', n.get_bool_value()),
            "kiosk_mode_screen_saver_detect_media_disabled": lambda n : setattr(self, 'kiosk_mode_screen_saver_detect_media_disabled', n.get_bool_value()),
            "kiosk_mode_screen_saver_display_time_in_seconds": lambda n : setattr(self, 'kiosk_mode_screen_saver_display_time_in_seconds', n.get_int_value()),
            "kiosk_mode_screen_saver_image_url": lambda n : setattr(self, 'kiosk_mode_screen_saver_image_url', n.get_str_value()),
            "kiosk_mode_screen_saver_start_delay_in_seconds": lambda n : setattr(self, 'kiosk_mode_screen_saver_start_delay_in_seconds', n.get_int_value()),
            "kiosk_mode_show_app_notification_badge": lambda n : setattr(self, 'kiosk_mode_show_app_notification_badge', n.get_bool_value()),
            "kiosk_mode_show_device_info": lambda n : setattr(self, 'kiosk_mode_show_device_info', n.get_bool_value()),
            "kiosk_mode_use_managed_home_screen_app": lambda n : setattr(self, 'kiosk_mode_use_managed_home_screen_app', n.get_enum_value(kiosk_mode_type.KioskModeType)),
            "kiosk_mode_virtual_home_button_enabled": lambda n : setattr(self, 'kiosk_mode_virtual_home_button_enabled', n.get_bool_value()),
            "kiosk_mode_virtual_home_button_type": lambda n : setattr(self, 'kiosk_mode_virtual_home_button_type', n.get_enum_value(android_device_owner_virtual_home_button_type.AndroidDeviceOwnerVirtualHomeButtonType)),
            "kiosk_mode_wallpaper_url": lambda n : setattr(self, 'kiosk_mode_wallpaper_url', n.get_str_value()),
            "kiosk_mode_wifi_allowed_ssids": lambda n : setattr(self, 'kiosk_mode_wifi_allowed_ssids', n.get_collection_of_primitive_values(str)),
            "kiosk_mode_wi_fi_configuration_enabled": lambda n : setattr(self, 'kiosk_mode_wi_fi_configuration_enabled', n.get_bool_value()),
            "microphone_force_mute": lambda n : setattr(self, 'microphone_force_mute', n.get_bool_value()),
            "microsoft_launcher_configuration_enabled": lambda n : setattr(self, 'microsoft_launcher_configuration_enabled', n.get_bool_value()),
            "microsoft_launcher_custom_wallpaper_allow_user_modification": lambda n : setattr(self, 'microsoft_launcher_custom_wallpaper_allow_user_modification', n.get_bool_value()),
            "microsoft_launcher_custom_wallpaper_enabled": lambda n : setattr(self, 'microsoft_launcher_custom_wallpaper_enabled', n.get_bool_value()),
            "microsoft_launcher_custom_wallpaper_image_url": lambda n : setattr(self, 'microsoft_launcher_custom_wallpaper_image_url', n.get_str_value()),
            "microsoft_launcher_dock_presence_allow_user_modification": lambda n : setattr(self, 'microsoft_launcher_dock_presence_allow_user_modification', n.get_bool_value()),
            "microsoft_launcher_dock_presence_configuration": lambda n : setattr(self, 'microsoft_launcher_dock_presence_configuration', n.get_enum_value(microsoft_launcher_dock_presence.MicrosoftLauncherDockPresence)),
            "microsoft_launcher_feed_allow_user_modification": lambda n : setattr(self, 'microsoft_launcher_feed_allow_user_modification', n.get_bool_value()),
            "microsoft_launcher_feed_enabled": lambda n : setattr(self, 'microsoft_launcher_feed_enabled', n.get_bool_value()),
            "microsoft_launcher_search_bar_placement_configuration": lambda n : setattr(self, 'microsoft_launcher_search_bar_placement_configuration', n.get_enum_value(microsoft_launcher_search_bar_placement.MicrosoftLauncherSearchBarPlacement)),
            "network_escape_hatch_allowed": lambda n : setattr(self, 'network_escape_hatch_allowed', n.get_bool_value()),
            "nfc_block_outgoing_beam": lambda n : setattr(self, 'nfc_block_outgoing_beam', n.get_bool_value()),
            "password_block_keyguard": lambda n : setattr(self, 'password_block_keyguard', n.get_bool_value()),
            "password_block_keyguard_features": lambda n : setattr(self, 'password_block_keyguard_features', n.get_collection_of_enum_values(android_keyguard_feature.AndroidKeyguardFeature)),
            "password_expiration_days": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "password_minimum_length": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "password_minimum_letter_characters": lambda n : setattr(self, 'password_minimum_letter_characters', n.get_int_value()),
            "password_minimum_lower_case_characters": lambda n : setattr(self, 'password_minimum_lower_case_characters', n.get_int_value()),
            "password_minimum_non_letter_characters": lambda n : setattr(self, 'password_minimum_non_letter_characters', n.get_int_value()),
            "password_minimum_numeric_characters": lambda n : setattr(self, 'password_minimum_numeric_characters', n.get_int_value()),
            "password_minimum_symbol_characters": lambda n : setattr(self, 'password_minimum_symbol_characters', n.get_int_value()),
            "password_minimum_upper_case_characters": lambda n : setattr(self, 'password_minimum_upper_case_characters', n.get_int_value()),
            "password_minutes_of_inactivity_before_screen_timeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "password_previous_password_count_to_block": lambda n : setattr(self, 'password_previous_password_count_to_block', n.get_int_value()),
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType)),
            "password_require_unlock": lambda n : setattr(self, 'password_require_unlock', n.get_enum_value(android_device_owner_required_password_unlock.AndroidDeviceOwnerRequiredPasswordUnlock)),
            "password_sign_in_failure_count_before_factory_reset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "personal_profile_apps_allow_install_from_unknown_sources": lambda n : setattr(self, 'personal_profile_apps_allow_install_from_unknown_sources', n.get_bool_value()),
            "personal_profile_camera_blocked": lambda n : setattr(self, 'personal_profile_camera_blocked', n.get_bool_value()),
            "personal_profile_personal_applications": lambda n : setattr(self, 'personal_profile_personal_applications', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "personal_profile_play_store_mode": lambda n : setattr(self, 'personal_profile_play_store_mode', n.get_enum_value(personal_profile_personal_play_store_mode.PersonalProfilePersonalPlayStoreMode)),
            "personal_profile_screen_capture_blocked": lambda n : setattr(self, 'personal_profile_screen_capture_blocked', n.get_bool_value()),
            "play_store_mode": lambda n : setattr(self, 'play_store_mode', n.get_enum_value(android_device_owner_play_store_mode.AndroidDeviceOwnerPlayStoreMode)),
            "screen_capture_blocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "security_common_criteria_mode_enabled": lambda n : setattr(self, 'security_common_criteria_mode_enabled', n.get_bool_value()),
            "security_developer_settings_enabled": lambda n : setattr(self, 'security_developer_settings_enabled', n.get_bool_value()),
            "security_require_verify_apps": lambda n : setattr(self, 'security_require_verify_apps', n.get_bool_value()),
            "short_help_text": lambda n : setattr(self, 'short_help_text', n.get_object_value(android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage)),
            "status_bar_blocked": lambda n : setattr(self, 'status_bar_blocked', n.get_bool_value()),
            "stay_on_modes": lambda n : setattr(self, 'stay_on_modes', n.get_collection_of_enum_values(android_device_owner_battery_plugged_mode.AndroidDeviceOwnerBatteryPluggedMode)),
            "storage_allow_usb": lambda n : setattr(self, 'storage_allow_usb', n.get_bool_value()),
            "storage_block_external_media": lambda n : setattr(self, 'storage_block_external_media', n.get_bool_value()),
            "storage_block_usb_file_transfer": lambda n : setattr(self, 'storage_block_usb_file_transfer', n.get_bool_value()),
            "system_update_freeze_periods": lambda n : setattr(self, 'system_update_freeze_periods', n.get_collection_of_object_values(android_device_owner_system_update_freeze_period.AndroidDeviceOwnerSystemUpdateFreezePeriod)),
            "system_update_install_type": lambda n : setattr(self, 'system_update_install_type', n.get_enum_value(android_device_owner_system_update_install_type.AndroidDeviceOwnerSystemUpdateInstallType)),
            "system_update_window_end_minutes_after_midnight": lambda n : setattr(self, 'system_update_window_end_minutes_after_midnight', n.get_int_value()),
            "system_update_window_start_minutes_after_midnight": lambda n : setattr(self, 'system_update_window_start_minutes_after_midnight', n.get_int_value()),
            "system_windows_blocked": lambda n : setattr(self, 'system_windows_blocked', n.get_bool_value()),
            "users_block_add": lambda n : setattr(self, 'users_block_add', n.get_bool_value()),
            "users_block_remove": lambda n : setattr(self, 'users_block_remove', n.get_bool_value()),
            "volume_block_adjustment": lambda n : setattr(self, 'volume_block_adjustment', n.get_bool_value()),
            "vpn_always_on_lockdown_mode": lambda n : setattr(self, 'vpn_always_on_lockdown_mode', n.get_bool_value()),
            "vpn_always_on_package_identifier": lambda n : setattr(self, 'vpn_always_on_package_identifier', n.get_str_value()),
            "wifi_block_edit_configurations": lambda n : setattr(self, 'wifi_block_edit_configurations', n.get_bool_value()),
            "wifi_block_edit_policy_defined_configurations": lambda n : setattr(self, 'wifi_block_edit_policy_defined_configurations', n.get_bool_value()),
            "work_profile_password_expiration_days": lambda n : setattr(self, 'work_profile_password_expiration_days', n.get_int_value()),
            "work_profile_password_minimum_length": lambda n : setattr(self, 'work_profile_password_minimum_length', n.get_int_value()),
            "work_profile_password_minimum_letter_characters": lambda n : setattr(self, 'work_profile_password_minimum_letter_characters', n.get_int_value()),
            "work_profile_password_minimum_lower_case_characters": lambda n : setattr(self, 'work_profile_password_minimum_lower_case_characters', n.get_int_value()),
            "work_profile_password_minimum_non_letter_characters": lambda n : setattr(self, 'work_profile_password_minimum_non_letter_characters', n.get_int_value()),
            "work_profile_password_minimum_numeric_characters": lambda n : setattr(self, 'work_profile_password_minimum_numeric_characters', n.get_int_value()),
            "work_profile_password_minimum_symbol_characters": lambda n : setattr(self, 'work_profile_password_minimum_symbol_characters', n.get_int_value()),
            "work_profile_password_minimum_upper_case_characters": lambda n : setattr(self, 'work_profile_password_minimum_upper_case_characters', n.get_int_value()),
            "work_profile_password_previous_password_count_to_block": lambda n : setattr(self, 'work_profile_password_previous_password_count_to_block', n.get_int_value()),
            "work_profile_password_required_type": lambda n : setattr(self, 'work_profile_password_required_type', n.get_enum_value(android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType)),
            "work_profile_password_require_unlock": lambda n : setattr(self, 'work_profile_password_require_unlock', n.get_enum_value(android_device_owner_required_password_unlock.AndroidDeviceOwnerRequiredPasswordUnlock)),
            "work_profile_password_sign_in_failure_count_before_factory_reset": lambda n : setattr(self, 'work_profile_password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def global_proxy(self,) -> Optional[android_device_owner_global_proxy.AndroidDeviceOwnerGlobalProxy]:
        """
        Gets the globalProxy property value. Proxy is set up directly with host, port and excluded hosts.
        Returns: Optional[android_device_owner_global_proxy.AndroidDeviceOwnerGlobalProxy]
        """
        return self._global_proxy
    
    @global_proxy.setter
    def global_proxy(self,value: Optional[android_device_owner_global_proxy.AndroidDeviceOwnerGlobalProxy] = None) -> None:
        """
        Sets the globalProxy property value. Proxy is set up directly with host, port and excluded hosts.
        Args:
            value: Value to set for the globalProxy property.
        """
        self._global_proxy = value
    
    @property
    def google_accounts_blocked(self,) -> Optional[bool]:
        """
        Gets the googleAccountsBlocked property value. Indicates whether or not google accounts will be blocked.
        Returns: Optional[bool]
        """
        return self._google_accounts_blocked
    
    @google_accounts_blocked.setter
    def google_accounts_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the googleAccountsBlocked property value. Indicates whether or not google accounts will be blocked.
        Args:
            value: Value to set for the googleAccountsBlocked property.
        """
        self._google_accounts_blocked = value
    
    @property
    def kiosk_customization_device_settings_blocked(self,) -> Optional[bool]:
        """
        Gets the kioskCustomizationDeviceSettingsBlocked property value. Indicates whether a user can access the device's Settings app while in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_customization_device_settings_blocked
    
    @kiosk_customization_device_settings_blocked.setter
    def kiosk_customization_device_settings_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskCustomizationDeviceSettingsBlocked property value. Indicates whether a user can access the device's Settings app while in Kiosk Mode.
        Args:
            value: Value to set for the kioskCustomizationDeviceSettingsBlocked property.
        """
        self._kiosk_customization_device_settings_blocked = value
    
    @property
    def kiosk_customization_power_button_actions_blocked(self,) -> Optional[bool]:
        """
        Gets the kioskCustomizationPowerButtonActionsBlocked property value. Whether the power menu is shown when a user long presses the Power button of a device in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_customization_power_button_actions_blocked
    
    @kiosk_customization_power_button_actions_blocked.setter
    def kiosk_customization_power_button_actions_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskCustomizationPowerButtonActionsBlocked property value. Whether the power menu is shown when a user long presses the Power button of a device in Kiosk Mode.
        Args:
            value: Value to set for the kioskCustomizationPowerButtonActionsBlocked property.
        """
        self._kiosk_customization_power_button_actions_blocked = value
    
    @property
    def kiosk_customization_status_bar(self,) -> Optional[android_device_owner_kiosk_customization_status_bar.AndroidDeviceOwnerKioskCustomizationStatusBar]:
        """
        Gets the kioskCustomizationStatusBar property value. Indicates whether system info and notifications are disabled in Kiosk Mode. Possible values are: notConfigured, notificationsAndSystemInfoEnabled, systemInfoOnly.
        Returns: Optional[android_device_owner_kiosk_customization_status_bar.AndroidDeviceOwnerKioskCustomizationStatusBar]
        """
        return self._kiosk_customization_status_bar
    
    @kiosk_customization_status_bar.setter
    def kiosk_customization_status_bar(self,value: Optional[android_device_owner_kiosk_customization_status_bar.AndroidDeviceOwnerKioskCustomizationStatusBar] = None) -> None:
        """
        Sets the kioskCustomizationStatusBar property value. Indicates whether system info and notifications are disabled in Kiosk Mode. Possible values are: notConfigured, notificationsAndSystemInfoEnabled, systemInfoOnly.
        Args:
            value: Value to set for the kioskCustomizationStatusBar property.
        """
        self._kiosk_customization_status_bar = value
    
    @property
    def kiosk_customization_system_error_warnings(self,) -> Optional[bool]:
        """
        Gets the kioskCustomizationSystemErrorWarnings property value. Indicates whether system error dialogs for crashed or unresponsive apps are shown in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_customization_system_error_warnings
    
    @kiosk_customization_system_error_warnings.setter
    def kiosk_customization_system_error_warnings(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskCustomizationSystemErrorWarnings property value. Indicates whether system error dialogs for crashed or unresponsive apps are shown in Kiosk Mode.
        Args:
            value: Value to set for the kioskCustomizationSystemErrorWarnings property.
        """
        self._kiosk_customization_system_error_warnings = value
    
    @property
    def kiosk_customization_system_navigation(self,) -> Optional[android_device_owner_kiosk_customization_system_navigation.AndroidDeviceOwnerKioskCustomizationSystemNavigation]:
        """
        Gets the kioskCustomizationSystemNavigation property value. Indicates which navigation features are enabled in Kiosk Mode. Possible values are: notConfigured, navigationEnabled, homeButtonOnly.
        Returns: Optional[android_device_owner_kiosk_customization_system_navigation.AndroidDeviceOwnerKioskCustomizationSystemNavigation]
        """
        return self._kiosk_customization_system_navigation
    
    @kiosk_customization_system_navigation.setter
    def kiosk_customization_system_navigation(self,value: Optional[android_device_owner_kiosk_customization_system_navigation.AndroidDeviceOwnerKioskCustomizationSystemNavigation] = None) -> None:
        """
        Sets the kioskCustomizationSystemNavigation property value. Indicates which navigation features are enabled in Kiosk Mode. Possible values are: notConfigured, navigationEnabled, homeButtonOnly.
        Args:
            value: Value to set for the kioskCustomizationSystemNavigation property.
        """
        self._kiosk_customization_system_navigation = value
    
    @property
    def kiosk_mode_app_order_enabled(self,) -> Optional[bool]:
        """
        Gets the kioskModeAppOrderEnabled property value. Whether or not to enable app ordering in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_app_order_enabled
    
    @kiosk_mode_app_order_enabled.setter
    def kiosk_mode_app_order_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAppOrderEnabled property value. Whether or not to enable app ordering in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeAppOrderEnabled property.
        """
        self._kiosk_mode_app_order_enabled = value
    
    @property
    def kiosk_mode_app_positions(self,) -> Optional[List[android_device_owner_kiosk_mode_app_position_item.AndroidDeviceOwnerKioskModeAppPositionItem]]:
        """
        Gets the kioskModeAppPositions property value. The ordering of items on Kiosk Mode Managed Home Screen. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[android_device_owner_kiosk_mode_app_position_item.AndroidDeviceOwnerKioskModeAppPositionItem]]
        """
        return self._kiosk_mode_app_positions
    
    @kiosk_mode_app_positions.setter
    def kiosk_mode_app_positions(self,value: Optional[List[android_device_owner_kiosk_mode_app_position_item.AndroidDeviceOwnerKioskModeAppPositionItem]] = None) -> None:
        """
        Sets the kioskModeAppPositions property value. The ordering of items on Kiosk Mode Managed Home Screen. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the kioskModeAppPositions property.
        """
        self._kiosk_mode_app_positions = value
    
    @property
    def kiosk_mode_apps(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the kioskModeApps property value. A list of managed apps that will be shown when the device is in Kiosk Mode. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._kiosk_mode_apps
    
    @kiosk_mode_apps.setter
    def kiosk_mode_apps(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the kioskModeApps property value. A list of managed apps that will be shown when the device is in Kiosk Mode. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the kioskModeApps property.
        """
        self._kiosk_mode_apps = value
    
    @property
    def kiosk_mode_apps_in_folder_ordered_by_name(self,) -> Optional[bool]:
        """
        Gets the kioskModeAppsInFolderOrderedByName property value. Whether or not to alphabetize applications within a folder in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_apps_in_folder_ordered_by_name
    
    @kiosk_mode_apps_in_folder_ordered_by_name.setter
    def kiosk_mode_apps_in_folder_ordered_by_name(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAppsInFolderOrderedByName property value. Whether or not to alphabetize applications within a folder in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeAppsInFolderOrderedByName property.
        """
        self._kiosk_mode_apps_in_folder_ordered_by_name = value
    
    @property
    def kiosk_mode_bluetooth_configuration_enabled(self,) -> Optional[bool]:
        """
        Gets the kioskModeBluetoothConfigurationEnabled property value. Whether or not to allow a user to configure Bluetooth settings in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_bluetooth_configuration_enabled
    
    @kiosk_mode_bluetooth_configuration_enabled.setter
    def kiosk_mode_bluetooth_configuration_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeBluetoothConfigurationEnabled property value. Whether or not to allow a user to configure Bluetooth settings in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeBluetoothConfigurationEnabled property.
        """
        self._kiosk_mode_bluetooth_configuration_enabled = value
    
    @property
    def kiosk_mode_debug_menu_easy_access_enabled(self,) -> Optional[bool]:
        """
        Gets the kioskModeDebugMenuEasyAccessEnabled property value. Whether or not to allow a user to easy access to the debug menu in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_debug_menu_easy_access_enabled
    
    @kiosk_mode_debug_menu_easy_access_enabled.setter
    def kiosk_mode_debug_menu_easy_access_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeDebugMenuEasyAccessEnabled property value. Whether or not to allow a user to easy access to the debug menu in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeDebugMenuEasyAccessEnabled property.
        """
        self._kiosk_mode_debug_menu_easy_access_enabled = value
    
    @property
    def kiosk_mode_exit_code(self,) -> Optional[str]:
        """
        Gets the kioskModeExitCode property value. Exit code to allow a user to escape from Kiosk Mode when the device is in Kiosk Mode.
        Returns: Optional[str]
        """
        return self._kiosk_mode_exit_code
    
    @kiosk_mode_exit_code.setter
    def kiosk_mode_exit_code(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskModeExitCode property value. Exit code to allow a user to escape from Kiosk Mode when the device is in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeExitCode property.
        """
        self._kiosk_mode_exit_code = value
    
    @property
    def kiosk_mode_flashlight_configuration_enabled(self,) -> Optional[bool]:
        """
        Gets the kioskModeFlashlightConfigurationEnabled property value. Whether or not to allow a user to use the flashlight in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_flashlight_configuration_enabled
    
    @kiosk_mode_flashlight_configuration_enabled.setter
    def kiosk_mode_flashlight_configuration_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeFlashlightConfigurationEnabled property value. Whether or not to allow a user to use the flashlight in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeFlashlightConfigurationEnabled property.
        """
        self._kiosk_mode_flashlight_configuration_enabled = value
    
    @property
    def kiosk_mode_folder_icon(self,) -> Optional[android_device_owner_kiosk_mode_folder_icon.AndroidDeviceOwnerKioskModeFolderIcon]:
        """
        Gets the kioskModeFolderIcon property value. Folder icon configuration for managed home screen in Kiosk Mode. Possible values are: notConfigured, darkSquare, darkCircle, lightSquare, lightCircle.
        Returns: Optional[android_device_owner_kiosk_mode_folder_icon.AndroidDeviceOwnerKioskModeFolderIcon]
        """
        return self._kiosk_mode_folder_icon
    
    @kiosk_mode_folder_icon.setter
    def kiosk_mode_folder_icon(self,value: Optional[android_device_owner_kiosk_mode_folder_icon.AndroidDeviceOwnerKioskModeFolderIcon] = None) -> None:
        """
        Sets the kioskModeFolderIcon property value. Folder icon configuration for managed home screen in Kiosk Mode. Possible values are: notConfigured, darkSquare, darkCircle, lightSquare, lightCircle.
        Args:
            value: Value to set for the kioskModeFolderIcon property.
        """
        self._kiosk_mode_folder_icon = value
    
    @property
    def kiosk_mode_grid_height(self,) -> Optional[int]:
        """
        Gets the kioskModeGridHeight property value. Number of rows for Managed Home Screen grid with app ordering enabled in Kiosk Mode. Valid values 1 to 9999999
        Returns: Optional[int]
        """
        return self._kiosk_mode_grid_height
    
    @kiosk_mode_grid_height.setter
    def kiosk_mode_grid_height(self,value: Optional[int] = None) -> None:
        """
        Sets the kioskModeGridHeight property value. Number of rows for Managed Home Screen grid with app ordering enabled in Kiosk Mode. Valid values 1 to 9999999
        Args:
            value: Value to set for the kioskModeGridHeight property.
        """
        self._kiosk_mode_grid_height = value
    
    @property
    def kiosk_mode_grid_width(self,) -> Optional[int]:
        """
        Gets the kioskModeGridWidth property value. Number of columns for Managed Home Screen grid with app ordering enabled in Kiosk Mode. Valid values 1 to 9999999
        Returns: Optional[int]
        """
        return self._kiosk_mode_grid_width
    
    @kiosk_mode_grid_width.setter
    def kiosk_mode_grid_width(self,value: Optional[int] = None) -> None:
        """
        Sets the kioskModeGridWidth property value. Number of columns for Managed Home Screen grid with app ordering enabled in Kiosk Mode. Valid values 1 to 9999999
        Args:
            value: Value to set for the kioskModeGridWidth property.
        """
        self._kiosk_mode_grid_width = value
    
    @property
    def kiosk_mode_icon_size(self,) -> Optional[android_device_owner_kiosk_mode_icon_size.AndroidDeviceOwnerKioskModeIconSize]:
        """
        Gets the kioskModeIconSize property value. Icon size configuration for managed home screen in Kiosk Mode. Possible values are: notConfigured, smallest, small, regular, large, largest.
        Returns: Optional[android_device_owner_kiosk_mode_icon_size.AndroidDeviceOwnerKioskModeIconSize]
        """
        return self._kiosk_mode_icon_size
    
    @kiosk_mode_icon_size.setter
    def kiosk_mode_icon_size(self,value: Optional[android_device_owner_kiosk_mode_icon_size.AndroidDeviceOwnerKioskModeIconSize] = None) -> None:
        """
        Sets the kioskModeIconSize property value. Icon size configuration for managed home screen in Kiosk Mode. Possible values are: notConfigured, smallest, small, regular, large, largest.
        Args:
            value: Value to set for the kioskModeIconSize property.
        """
        self._kiosk_mode_icon_size = value
    
    @property
    def kiosk_mode_lock_home_screen(self,) -> Optional[bool]:
        """
        Gets the kioskModeLockHomeScreen property value. Whether or not to lock home screen to the end user in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_lock_home_screen
    
    @kiosk_mode_lock_home_screen.setter
    def kiosk_mode_lock_home_screen(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeLockHomeScreen property value. Whether or not to lock home screen to the end user in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeLockHomeScreen property.
        """
        self._kiosk_mode_lock_home_screen = value
    
    @property
    def kiosk_mode_managed_folders(self,) -> Optional[List[android_device_owner_kiosk_mode_managed_folder.AndroidDeviceOwnerKioskModeManagedFolder]]:
        """
        Gets the kioskModeManagedFolders property value. A list of managed folders for a device in Kiosk Mode. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[android_device_owner_kiosk_mode_managed_folder.AndroidDeviceOwnerKioskModeManagedFolder]]
        """
        return self._kiosk_mode_managed_folders
    
    @kiosk_mode_managed_folders.setter
    def kiosk_mode_managed_folders(self,value: Optional[List[android_device_owner_kiosk_mode_managed_folder.AndroidDeviceOwnerKioskModeManagedFolder]] = None) -> None:
        """
        Sets the kioskModeManagedFolders property value. A list of managed folders for a device in Kiosk Mode. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the kioskModeManagedFolders property.
        """
        self._kiosk_mode_managed_folders = value
    
    @property
    def kiosk_mode_managed_home_screen_auto_signout(self,) -> Optional[bool]:
        """
        Gets the kioskModeManagedHomeScreenAutoSignout property value. Whether or not to automatically sign-out of MHS and Shared device mode applications after inactive for Managed Home Screen.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_managed_home_screen_auto_signout
    
    @kiosk_mode_managed_home_screen_auto_signout.setter
    def kiosk_mode_managed_home_screen_auto_signout(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeManagedHomeScreenAutoSignout property value. Whether or not to automatically sign-out of MHS and Shared device mode applications after inactive for Managed Home Screen.
        Args:
            value: Value to set for the kioskModeManagedHomeScreenAutoSignout property.
        """
        self._kiosk_mode_managed_home_screen_auto_signout = value
    
    @property
    def kiosk_mode_managed_home_screen_inactive_sign_out_delay_in_seconds(self,) -> Optional[int]:
        """
        Gets the kioskModeManagedHomeScreenInactiveSignOutDelayInSeconds property value. Number of seconds to give user notice before automatically signing them out for Managed Home Screen. Valid values 0 to 9999999
        Returns: Optional[int]
        """
        return self._kiosk_mode_managed_home_screen_inactive_sign_out_delay_in_seconds
    
    @kiosk_mode_managed_home_screen_inactive_sign_out_delay_in_seconds.setter
    def kiosk_mode_managed_home_screen_inactive_sign_out_delay_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the kioskModeManagedHomeScreenInactiveSignOutDelayInSeconds property value. Number of seconds to give user notice before automatically signing them out for Managed Home Screen. Valid values 0 to 9999999
        Args:
            value: Value to set for the kioskModeManagedHomeScreenInactiveSignOutDelayInSeconds property.
        """
        self._kiosk_mode_managed_home_screen_inactive_sign_out_delay_in_seconds = value
    
    @property
    def kiosk_mode_managed_home_screen_inactive_sign_out_notice_in_seconds(self,) -> Optional[int]:
        """
        Gets the kioskModeManagedHomeScreenInactiveSignOutNoticeInSeconds property value. Number of seconds device is inactive before automatically signing user out for Managed Home Screen. Valid values 0 to 9999999
        Returns: Optional[int]
        """
        return self._kiosk_mode_managed_home_screen_inactive_sign_out_notice_in_seconds
    
    @kiosk_mode_managed_home_screen_inactive_sign_out_notice_in_seconds.setter
    def kiosk_mode_managed_home_screen_inactive_sign_out_notice_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the kioskModeManagedHomeScreenInactiveSignOutNoticeInSeconds property value. Number of seconds device is inactive before automatically signing user out for Managed Home Screen. Valid values 0 to 9999999
        Args:
            value: Value to set for the kioskModeManagedHomeScreenInactiveSignOutNoticeInSeconds property.
        """
        self._kiosk_mode_managed_home_screen_inactive_sign_out_notice_in_seconds = value
    
    @property
    def kiosk_mode_managed_home_screen_pin_complexity(self,) -> Optional[kiosk_mode_managed_home_screen_pin_complexity.KioskModeManagedHomeScreenPinComplexity]:
        """
        Gets the kioskModeManagedHomeScreenPinComplexity property value. Complexity of PIN for sign-in session for Managed Home Screen. Possible values are: notConfigured, simple, complex.
        Returns: Optional[kiosk_mode_managed_home_screen_pin_complexity.KioskModeManagedHomeScreenPinComplexity]
        """
        return self._kiosk_mode_managed_home_screen_pin_complexity
    
    @kiosk_mode_managed_home_screen_pin_complexity.setter
    def kiosk_mode_managed_home_screen_pin_complexity(self,value: Optional[kiosk_mode_managed_home_screen_pin_complexity.KioskModeManagedHomeScreenPinComplexity] = None) -> None:
        """
        Sets the kioskModeManagedHomeScreenPinComplexity property value. Complexity of PIN for sign-in session for Managed Home Screen. Possible values are: notConfigured, simple, complex.
        Args:
            value: Value to set for the kioskModeManagedHomeScreenPinComplexity property.
        """
        self._kiosk_mode_managed_home_screen_pin_complexity = value
    
    @property
    def kiosk_mode_managed_home_screen_pin_required(self,) -> Optional[bool]:
        """
        Gets the kioskModeManagedHomeScreenPinRequired property value. Whether or not require user to set a PIN for sign-in session for Managed Home Screen.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_managed_home_screen_pin_required
    
    @kiosk_mode_managed_home_screen_pin_required.setter
    def kiosk_mode_managed_home_screen_pin_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeManagedHomeScreenPinRequired property value. Whether or not require user to set a PIN for sign-in session for Managed Home Screen.
        Args:
            value: Value to set for the kioskModeManagedHomeScreenPinRequired property.
        """
        self._kiosk_mode_managed_home_screen_pin_required = value
    
    @property
    def kiosk_mode_managed_home_screen_pin_required_to_resume(self,) -> Optional[bool]:
        """
        Gets the kioskModeManagedHomeScreenPinRequiredToResume property value. Whether or not required user to enter session PIN if screensaver has appeared for Managed Home Screen.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_managed_home_screen_pin_required_to_resume
    
    @kiosk_mode_managed_home_screen_pin_required_to_resume.setter
    def kiosk_mode_managed_home_screen_pin_required_to_resume(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeManagedHomeScreenPinRequiredToResume property value. Whether or not required user to enter session PIN if screensaver has appeared for Managed Home Screen.
        Args:
            value: Value to set for the kioskModeManagedHomeScreenPinRequiredToResume property.
        """
        self._kiosk_mode_managed_home_screen_pin_required_to_resume = value
    
    @property
    def kiosk_mode_managed_home_screen_sign_in_background(self,) -> Optional[str]:
        """
        Gets the kioskModeManagedHomeScreenSignInBackground property value. Custom URL background for sign-in screen for Managed Home Screen.
        Returns: Optional[str]
        """
        return self._kiosk_mode_managed_home_screen_sign_in_background
    
    @kiosk_mode_managed_home_screen_sign_in_background.setter
    def kiosk_mode_managed_home_screen_sign_in_background(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskModeManagedHomeScreenSignInBackground property value. Custom URL background for sign-in screen for Managed Home Screen.
        Args:
            value: Value to set for the kioskModeManagedHomeScreenSignInBackground property.
        """
        self._kiosk_mode_managed_home_screen_sign_in_background = value
    
    @property
    def kiosk_mode_managed_home_screen_sign_in_branding_logo(self,) -> Optional[str]:
        """
        Gets the kioskModeManagedHomeScreenSignInBrandingLogo property value. Custom URL branding logo for sign-in screen and session pin page for Managed Home Screen.
        Returns: Optional[str]
        """
        return self._kiosk_mode_managed_home_screen_sign_in_branding_logo
    
    @kiosk_mode_managed_home_screen_sign_in_branding_logo.setter
    def kiosk_mode_managed_home_screen_sign_in_branding_logo(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskModeManagedHomeScreenSignInBrandingLogo property value. Custom URL branding logo for sign-in screen and session pin page for Managed Home Screen.
        Args:
            value: Value to set for the kioskModeManagedHomeScreenSignInBrandingLogo property.
        """
        self._kiosk_mode_managed_home_screen_sign_in_branding_logo = value
    
    @property
    def kiosk_mode_managed_home_screen_sign_in_enabled(self,) -> Optional[bool]:
        """
        Gets the kioskModeManagedHomeScreenSignInEnabled property value. Whether or not show sign-in screen for Managed Home Screen.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_managed_home_screen_sign_in_enabled
    
    @kiosk_mode_managed_home_screen_sign_in_enabled.setter
    def kiosk_mode_managed_home_screen_sign_in_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeManagedHomeScreenSignInEnabled property value. Whether or not show sign-in screen for Managed Home Screen.
        Args:
            value: Value to set for the kioskModeManagedHomeScreenSignInEnabled property.
        """
        self._kiosk_mode_managed_home_screen_sign_in_enabled = value
    
    @property
    def kiosk_mode_managed_settings_entry_disabled(self,) -> Optional[bool]:
        """
        Gets the kioskModeManagedSettingsEntryDisabled property value. Whether or not to display the Managed Settings entry point on the managed home screen in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_managed_settings_entry_disabled
    
    @kiosk_mode_managed_settings_entry_disabled.setter
    def kiosk_mode_managed_settings_entry_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeManagedSettingsEntryDisabled property value. Whether or not to display the Managed Settings entry point on the managed home screen in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeManagedSettingsEntryDisabled property.
        """
        self._kiosk_mode_managed_settings_entry_disabled = value
    
    @property
    def kiosk_mode_media_volume_configuration_enabled(self,) -> Optional[bool]:
        """
        Gets the kioskModeMediaVolumeConfigurationEnabled property value. Whether or not to allow a user to change the media volume in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_media_volume_configuration_enabled
    
    @kiosk_mode_media_volume_configuration_enabled.setter
    def kiosk_mode_media_volume_configuration_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeMediaVolumeConfigurationEnabled property value. Whether or not to allow a user to change the media volume in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeMediaVolumeConfigurationEnabled property.
        """
        self._kiosk_mode_media_volume_configuration_enabled = value
    
    @property
    def kiosk_mode_screen_orientation(self,) -> Optional[android_device_owner_kiosk_mode_screen_orientation.AndroidDeviceOwnerKioskModeScreenOrientation]:
        """
        Gets the kioskModeScreenOrientation property value. Screen orientation configuration for managed home screen in Kiosk Mode. Possible values are: notConfigured, portrait, landscape, autoRotate.
        Returns: Optional[android_device_owner_kiosk_mode_screen_orientation.AndroidDeviceOwnerKioskModeScreenOrientation]
        """
        return self._kiosk_mode_screen_orientation
    
    @kiosk_mode_screen_orientation.setter
    def kiosk_mode_screen_orientation(self,value: Optional[android_device_owner_kiosk_mode_screen_orientation.AndroidDeviceOwnerKioskModeScreenOrientation] = None) -> None:
        """
        Sets the kioskModeScreenOrientation property value. Screen orientation configuration for managed home screen in Kiosk Mode. Possible values are: notConfigured, portrait, landscape, autoRotate.
        Args:
            value: Value to set for the kioskModeScreenOrientation property.
        """
        self._kiosk_mode_screen_orientation = value
    
    @property
    def kiosk_mode_screen_saver_configuration_enabled(self,) -> Optional[bool]:
        """
        Gets the kioskModeScreenSaverConfigurationEnabled property value. Whether or not to enable screen saver mode or not in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_screen_saver_configuration_enabled
    
    @kiosk_mode_screen_saver_configuration_enabled.setter
    def kiosk_mode_screen_saver_configuration_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeScreenSaverConfigurationEnabled property value. Whether or not to enable screen saver mode or not in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeScreenSaverConfigurationEnabled property.
        """
        self._kiosk_mode_screen_saver_configuration_enabled = value
    
    @property
    def kiosk_mode_screen_saver_detect_media_disabled(self,) -> Optional[bool]:
        """
        Gets the kioskModeScreenSaverDetectMediaDisabled property value. Whether or not the device screen should show the screen saver if audio/video is playing in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_screen_saver_detect_media_disabled
    
    @kiosk_mode_screen_saver_detect_media_disabled.setter
    def kiosk_mode_screen_saver_detect_media_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeScreenSaverDetectMediaDisabled property value. Whether or not the device screen should show the screen saver if audio/video is playing in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeScreenSaverDetectMediaDisabled property.
        """
        self._kiosk_mode_screen_saver_detect_media_disabled = value
    
    @property
    def kiosk_mode_screen_saver_display_time_in_seconds(self,) -> Optional[int]:
        """
        Gets the kioskModeScreenSaverDisplayTimeInSeconds property value. The number of seconds that the device will display the screen saver for in Kiosk Mode. Valid values 0 to 9999999
        Returns: Optional[int]
        """
        return self._kiosk_mode_screen_saver_display_time_in_seconds
    
    @kiosk_mode_screen_saver_display_time_in_seconds.setter
    def kiosk_mode_screen_saver_display_time_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the kioskModeScreenSaverDisplayTimeInSeconds property value. The number of seconds that the device will display the screen saver for in Kiosk Mode. Valid values 0 to 9999999
        Args:
            value: Value to set for the kioskModeScreenSaverDisplayTimeInSeconds property.
        """
        self._kiosk_mode_screen_saver_display_time_in_seconds = value
    
    @property
    def kiosk_mode_screen_saver_image_url(self,) -> Optional[str]:
        """
        Gets the kioskModeScreenSaverImageUrl property value. URL for an image that will be the device's screen saver in Kiosk Mode.
        Returns: Optional[str]
        """
        return self._kiosk_mode_screen_saver_image_url
    
    @kiosk_mode_screen_saver_image_url.setter
    def kiosk_mode_screen_saver_image_url(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskModeScreenSaverImageUrl property value. URL for an image that will be the device's screen saver in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeScreenSaverImageUrl property.
        """
        self._kiosk_mode_screen_saver_image_url = value
    
    @property
    def kiosk_mode_screen_saver_start_delay_in_seconds(self,) -> Optional[int]:
        """
        Gets the kioskModeScreenSaverStartDelayInSeconds property value. The number of seconds the device needs to be inactive for before the screen saver is shown in Kiosk Mode. Valid values 1 to 9999999
        Returns: Optional[int]
        """
        return self._kiosk_mode_screen_saver_start_delay_in_seconds
    
    @kiosk_mode_screen_saver_start_delay_in_seconds.setter
    def kiosk_mode_screen_saver_start_delay_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the kioskModeScreenSaverStartDelayInSeconds property value. The number of seconds the device needs to be inactive for before the screen saver is shown in Kiosk Mode. Valid values 1 to 9999999
        Args:
            value: Value to set for the kioskModeScreenSaverStartDelayInSeconds property.
        """
        self._kiosk_mode_screen_saver_start_delay_in_seconds = value
    
    @property
    def kiosk_mode_show_app_notification_badge(self,) -> Optional[bool]:
        """
        Gets the kioskModeShowAppNotificationBadge property value. Whether or not to display application notification badges in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_show_app_notification_badge
    
    @kiosk_mode_show_app_notification_badge.setter
    def kiosk_mode_show_app_notification_badge(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeShowAppNotificationBadge property value. Whether or not to display application notification badges in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeShowAppNotificationBadge property.
        """
        self._kiosk_mode_show_app_notification_badge = value
    
    @property
    def kiosk_mode_show_device_info(self,) -> Optional[bool]:
        """
        Gets the kioskModeShowDeviceInfo property value. Whether or not to allow a user to access basic device information.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_show_device_info
    
    @kiosk_mode_show_device_info.setter
    def kiosk_mode_show_device_info(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeShowDeviceInfo property value. Whether or not to allow a user to access basic device information.
        Args:
            value: Value to set for the kioskModeShowDeviceInfo property.
        """
        self._kiosk_mode_show_device_info = value
    
    @property
    def kiosk_mode_use_managed_home_screen_app(self,) -> Optional[kiosk_mode_type.KioskModeType]:
        """
        Gets the kioskModeUseManagedHomeScreenApp property value. Whether or not to use single app kiosk mode or multi-app kiosk mode. Possible values are: notConfigured, singleAppMode, multiAppMode.
        Returns: Optional[kiosk_mode_type.KioskModeType]
        """
        return self._kiosk_mode_use_managed_home_screen_app
    
    @kiosk_mode_use_managed_home_screen_app.setter
    def kiosk_mode_use_managed_home_screen_app(self,value: Optional[kiosk_mode_type.KioskModeType] = None) -> None:
        """
        Sets the kioskModeUseManagedHomeScreenApp property value. Whether or not to use single app kiosk mode or multi-app kiosk mode. Possible values are: notConfigured, singleAppMode, multiAppMode.
        Args:
            value: Value to set for the kioskModeUseManagedHomeScreenApp property.
        """
        self._kiosk_mode_use_managed_home_screen_app = value
    
    @property
    def kiosk_mode_virtual_home_button_enabled(self,) -> Optional[bool]:
        """
        Gets the kioskModeVirtualHomeButtonEnabled property value. Whether or not to display a virtual home button when the device is in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_virtual_home_button_enabled
    
    @kiosk_mode_virtual_home_button_enabled.setter
    def kiosk_mode_virtual_home_button_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeVirtualHomeButtonEnabled property value. Whether or not to display a virtual home button when the device is in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeVirtualHomeButtonEnabled property.
        """
        self._kiosk_mode_virtual_home_button_enabled = value
    
    @property
    def kiosk_mode_virtual_home_button_type(self,) -> Optional[android_device_owner_virtual_home_button_type.AndroidDeviceOwnerVirtualHomeButtonType]:
        """
        Gets the kioskModeVirtualHomeButtonType property value. Indicates whether the virtual home button is a swipe up home button or a floating home button. Possible values are: notConfigured, swipeUp, floating.
        Returns: Optional[android_device_owner_virtual_home_button_type.AndroidDeviceOwnerVirtualHomeButtonType]
        """
        return self._kiosk_mode_virtual_home_button_type
    
    @kiosk_mode_virtual_home_button_type.setter
    def kiosk_mode_virtual_home_button_type(self,value: Optional[android_device_owner_virtual_home_button_type.AndroidDeviceOwnerVirtualHomeButtonType] = None) -> None:
        """
        Sets the kioskModeVirtualHomeButtonType property value. Indicates whether the virtual home button is a swipe up home button or a floating home button. Possible values are: notConfigured, swipeUp, floating.
        Args:
            value: Value to set for the kioskModeVirtualHomeButtonType property.
        """
        self._kiosk_mode_virtual_home_button_type = value
    
    @property
    def kiosk_mode_wallpaper_url(self,) -> Optional[str]:
        """
        Gets the kioskModeWallpaperUrl property value. URL to a publicly accessible image to use for the wallpaper when the device is in Kiosk Mode.
        Returns: Optional[str]
        """
        return self._kiosk_mode_wallpaper_url
    
    @kiosk_mode_wallpaper_url.setter
    def kiosk_mode_wallpaper_url(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskModeWallpaperUrl property value. URL to a publicly accessible image to use for the wallpaper when the device is in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeWallpaperUrl property.
        """
        self._kiosk_mode_wallpaper_url = value
    
    @property
    def kiosk_mode_wifi_allowed_ssids(self,) -> Optional[List[str]]:
        """
        Gets the kioskModeWifiAllowedSsids property value. The restricted set of WIFI SSIDs available for the user to configure in Kiosk Mode. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[str]]
        """
        return self._kiosk_mode_wifi_allowed_ssids
    
    @kiosk_mode_wifi_allowed_ssids.setter
    def kiosk_mode_wifi_allowed_ssids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the kioskModeWifiAllowedSsids property value. The restricted set of WIFI SSIDs available for the user to configure in Kiosk Mode. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the kioskModeWifiAllowedSsids property.
        """
        self._kiosk_mode_wifi_allowed_ssids = value
    
    @property
    def kiosk_mode_wi_fi_configuration_enabled(self,) -> Optional[bool]:
        """
        Gets the kioskModeWiFiConfigurationEnabled property value. Whether or not to allow a user to configure Wi-Fi settings in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_wi_fi_configuration_enabled
    
    @kiosk_mode_wi_fi_configuration_enabled.setter
    def kiosk_mode_wi_fi_configuration_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeWiFiConfigurationEnabled property value. Whether or not to allow a user to configure Wi-Fi settings in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeWiFiConfigurationEnabled property.
        """
        self._kiosk_mode_wi_fi_configuration_enabled = value
    
    @property
    def microphone_force_mute(self,) -> Optional[bool]:
        """
        Gets the microphoneForceMute property value. Indicates whether or not to block unmuting the microphone on the device.
        Returns: Optional[bool]
        """
        return self._microphone_force_mute
    
    @microphone_force_mute.setter
    def microphone_force_mute(self,value: Optional[bool] = None) -> None:
        """
        Sets the microphoneForceMute property value. Indicates whether or not to block unmuting the microphone on the device.
        Args:
            value: Value to set for the microphoneForceMute property.
        """
        self._microphone_force_mute = value
    
    @property
    def microsoft_launcher_configuration_enabled(self,) -> Optional[bool]:
        """
        Gets the microsoftLauncherConfigurationEnabled property value. Indicates whether or not to you want configure Microsoft Launcher.
        Returns: Optional[bool]
        """
        return self._microsoft_launcher_configuration_enabled
    
    @microsoft_launcher_configuration_enabled.setter
    def microsoft_launcher_configuration_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the microsoftLauncherConfigurationEnabled property value. Indicates whether or not to you want configure Microsoft Launcher.
        Args:
            value: Value to set for the microsoftLauncherConfigurationEnabled property.
        """
        self._microsoft_launcher_configuration_enabled = value
    
    @property
    def microsoft_launcher_custom_wallpaper_allow_user_modification(self,) -> Optional[bool]:
        """
        Gets the microsoftLauncherCustomWallpaperAllowUserModification property value. Indicates whether or not the user can modify the wallpaper to personalize their device.
        Returns: Optional[bool]
        """
        return self._microsoft_launcher_custom_wallpaper_allow_user_modification
    
    @microsoft_launcher_custom_wallpaper_allow_user_modification.setter
    def microsoft_launcher_custom_wallpaper_allow_user_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the microsoftLauncherCustomWallpaperAllowUserModification property value. Indicates whether or not the user can modify the wallpaper to personalize their device.
        Args:
            value: Value to set for the microsoftLauncherCustomWallpaperAllowUserModification property.
        """
        self._microsoft_launcher_custom_wallpaper_allow_user_modification = value
    
    @property
    def microsoft_launcher_custom_wallpaper_enabled(self,) -> Optional[bool]:
        """
        Gets the microsoftLauncherCustomWallpaperEnabled property value. Indicates whether or not to configure the wallpaper on the targeted devices.
        Returns: Optional[bool]
        """
        return self._microsoft_launcher_custom_wallpaper_enabled
    
    @microsoft_launcher_custom_wallpaper_enabled.setter
    def microsoft_launcher_custom_wallpaper_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the microsoftLauncherCustomWallpaperEnabled property value. Indicates whether or not to configure the wallpaper on the targeted devices.
        Args:
            value: Value to set for the microsoftLauncherCustomWallpaperEnabled property.
        """
        self._microsoft_launcher_custom_wallpaper_enabled = value
    
    @property
    def microsoft_launcher_custom_wallpaper_image_url(self,) -> Optional[str]:
        """
        Gets the microsoftLauncherCustomWallpaperImageUrl property value. Indicates the URL for the image file to use as the wallpaper on the targeted devices.
        Returns: Optional[str]
        """
        return self._microsoft_launcher_custom_wallpaper_image_url
    
    @microsoft_launcher_custom_wallpaper_image_url.setter
    def microsoft_launcher_custom_wallpaper_image_url(self,value: Optional[str] = None) -> None:
        """
        Sets the microsoftLauncherCustomWallpaperImageUrl property value. Indicates the URL for the image file to use as the wallpaper on the targeted devices.
        Args:
            value: Value to set for the microsoftLauncherCustomWallpaperImageUrl property.
        """
        self._microsoft_launcher_custom_wallpaper_image_url = value
    
    @property
    def microsoft_launcher_dock_presence_allow_user_modification(self,) -> Optional[bool]:
        """
        Gets the microsoftLauncherDockPresenceAllowUserModification property value. Indicates whether or not the user can modify the device dock configuration on the device.
        Returns: Optional[bool]
        """
        return self._microsoft_launcher_dock_presence_allow_user_modification
    
    @microsoft_launcher_dock_presence_allow_user_modification.setter
    def microsoft_launcher_dock_presence_allow_user_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the microsoftLauncherDockPresenceAllowUserModification property value. Indicates whether or not the user can modify the device dock configuration on the device.
        Args:
            value: Value to set for the microsoftLauncherDockPresenceAllowUserModification property.
        """
        self._microsoft_launcher_dock_presence_allow_user_modification = value
    
    @property
    def microsoft_launcher_dock_presence_configuration(self,) -> Optional[microsoft_launcher_dock_presence.MicrosoftLauncherDockPresence]:
        """
        Gets the microsoftLauncherDockPresenceConfiguration property value. Indicates whether or not you want to configure the device dock. Possible values are: notConfigured, show, hide, disabled.
        Returns: Optional[microsoft_launcher_dock_presence.MicrosoftLauncherDockPresence]
        """
        return self._microsoft_launcher_dock_presence_configuration
    
    @microsoft_launcher_dock_presence_configuration.setter
    def microsoft_launcher_dock_presence_configuration(self,value: Optional[microsoft_launcher_dock_presence.MicrosoftLauncherDockPresence] = None) -> None:
        """
        Sets the microsoftLauncherDockPresenceConfiguration property value. Indicates whether or not you want to configure the device dock. Possible values are: notConfigured, show, hide, disabled.
        Args:
            value: Value to set for the microsoftLauncherDockPresenceConfiguration property.
        """
        self._microsoft_launcher_dock_presence_configuration = value
    
    @property
    def microsoft_launcher_feed_allow_user_modification(self,) -> Optional[bool]:
        """
        Gets the microsoftLauncherFeedAllowUserModification property value. Indicates whether or not the user can modify the launcher feed on the device.
        Returns: Optional[bool]
        """
        return self._microsoft_launcher_feed_allow_user_modification
    
    @microsoft_launcher_feed_allow_user_modification.setter
    def microsoft_launcher_feed_allow_user_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the microsoftLauncherFeedAllowUserModification property value. Indicates whether or not the user can modify the launcher feed on the device.
        Args:
            value: Value to set for the microsoftLauncherFeedAllowUserModification property.
        """
        self._microsoft_launcher_feed_allow_user_modification = value
    
    @property
    def microsoft_launcher_feed_enabled(self,) -> Optional[bool]:
        """
        Gets the microsoftLauncherFeedEnabled property value. Indicates whether or not you want to enable the launcher feed on the device.
        Returns: Optional[bool]
        """
        return self._microsoft_launcher_feed_enabled
    
    @microsoft_launcher_feed_enabled.setter
    def microsoft_launcher_feed_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the microsoftLauncherFeedEnabled property value. Indicates whether or not you want to enable the launcher feed on the device.
        Args:
            value: Value to set for the microsoftLauncherFeedEnabled property.
        """
        self._microsoft_launcher_feed_enabled = value
    
    @property
    def microsoft_launcher_search_bar_placement_configuration(self,) -> Optional[microsoft_launcher_search_bar_placement.MicrosoftLauncherSearchBarPlacement]:
        """
        Gets the microsoftLauncherSearchBarPlacementConfiguration property value. Indicates the search bar placement configuration on the device. Possible values are: notConfigured, top, bottom, hide.
        Returns: Optional[microsoft_launcher_search_bar_placement.MicrosoftLauncherSearchBarPlacement]
        """
        return self._microsoft_launcher_search_bar_placement_configuration
    
    @microsoft_launcher_search_bar_placement_configuration.setter
    def microsoft_launcher_search_bar_placement_configuration(self,value: Optional[microsoft_launcher_search_bar_placement.MicrosoftLauncherSearchBarPlacement] = None) -> None:
        """
        Sets the microsoftLauncherSearchBarPlacementConfiguration property value. Indicates the search bar placement configuration on the device. Possible values are: notConfigured, top, bottom, hide.
        Args:
            value: Value to set for the microsoftLauncherSearchBarPlacementConfiguration property.
        """
        self._microsoft_launcher_search_bar_placement_configuration = value
    
    @property
    def network_escape_hatch_allowed(self,) -> Optional[bool]:
        """
        Gets the networkEscapeHatchAllowed property value. Indicates whether or not the device will allow connecting to a temporary network connection at boot time.
        Returns: Optional[bool]
        """
        return self._network_escape_hatch_allowed
    
    @network_escape_hatch_allowed.setter
    def network_escape_hatch_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the networkEscapeHatchAllowed property value. Indicates whether or not the device will allow connecting to a temporary network connection at boot time.
        Args:
            value: Value to set for the networkEscapeHatchAllowed property.
        """
        self._network_escape_hatch_allowed = value
    
    @property
    def nfc_block_outgoing_beam(self,) -> Optional[bool]:
        """
        Gets the nfcBlockOutgoingBeam property value. Indicates whether or not to block NFC outgoing beam.
        Returns: Optional[bool]
        """
        return self._nfc_block_outgoing_beam
    
    @nfc_block_outgoing_beam.setter
    def nfc_block_outgoing_beam(self,value: Optional[bool] = None) -> None:
        """
        Sets the nfcBlockOutgoingBeam property value. Indicates whether or not to block NFC outgoing beam.
        Args:
            value: Value to set for the nfcBlockOutgoingBeam property.
        """
        self._nfc_block_outgoing_beam = value
    
    @property
    def password_block_keyguard(self,) -> Optional[bool]:
        """
        Gets the passwordBlockKeyguard property value. Indicates whether or not the keyguard is disabled.
        Returns: Optional[bool]
        """
        return self._password_block_keyguard
    
    @password_block_keyguard.setter
    def password_block_keyguard(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockKeyguard property value. Indicates whether or not the keyguard is disabled.
        Args:
            value: Value to set for the passwordBlockKeyguard property.
        """
        self._password_block_keyguard = value
    
    @property
    def password_block_keyguard_features(self,) -> Optional[List[android_keyguard_feature.AndroidKeyguardFeature]]:
        """
        Gets the passwordBlockKeyguardFeatures property value. List of device keyguard features to block. This collection can contain a maximum of 11 elements.
        Returns: Optional[List[android_keyguard_feature.AndroidKeyguardFeature]]
        """
        return self._password_block_keyguard_features
    
    @password_block_keyguard_features.setter
    def password_block_keyguard_features(self,value: Optional[List[android_keyguard_feature.AndroidKeyguardFeature]] = None) -> None:
        """
        Sets the passwordBlockKeyguardFeatures property value. List of device keyguard features to block. This collection can contain a maximum of 11 elements.
        Args:
            value: Value to set for the passwordBlockKeyguardFeatures property.
        """
        self._password_block_keyguard_features = value
    
    @property
    def password_expiration_days(self,) -> Optional[int]:
        """
        Gets the passwordExpirationDays property value. Indicates the amount of time that a password can be set for before it expires and a new password will be required. Valid values 1 to 365
        Returns: Optional[int]
        """
        return self._password_expiration_days
    
    @password_expiration_days.setter
    def password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordExpirationDays property value. Indicates the amount of time that a password can be set for before it expires and a new password will be required. Valid values 1 to 365
        Args:
            value: Value to set for the passwordExpirationDays property.
        """
        self._password_expiration_days = value
    
    @property
    def password_minimum_length(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLength property value. Indicates the minimum length of the password required on the device. Valid values 4 to 16
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. Indicates the minimum length of the password required on the device. Valid values 4 to 16
        Args:
            value: Value to set for the passwordMinimumLength property.
        """
        self._password_minimum_length = value
    
    @property
    def password_minimum_letter_characters(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLetterCharacters property value. Indicates the minimum number of letter characters required for device password. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._password_minimum_letter_characters
    
    @password_minimum_letter_characters.setter
    def password_minimum_letter_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLetterCharacters property value. Indicates the minimum number of letter characters required for device password. Valid values 1 to 16
        Args:
            value: Value to set for the passwordMinimumLetterCharacters property.
        """
        self._password_minimum_letter_characters = value
    
    @property
    def password_minimum_lower_case_characters(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLowerCaseCharacters property value. Indicates the minimum number of lower case characters required for device password. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._password_minimum_lower_case_characters
    
    @password_minimum_lower_case_characters.setter
    def password_minimum_lower_case_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLowerCaseCharacters property value. Indicates the minimum number of lower case characters required for device password. Valid values 1 to 16
        Args:
            value: Value to set for the passwordMinimumLowerCaseCharacters property.
        """
        self._password_minimum_lower_case_characters = value
    
    @property
    def password_minimum_non_letter_characters(self,) -> Optional[int]:
        """
        Gets the passwordMinimumNonLetterCharacters property value. Indicates the minimum number of non-letter characters required for device password. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._password_minimum_non_letter_characters
    
    @password_minimum_non_letter_characters.setter
    def password_minimum_non_letter_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumNonLetterCharacters property value. Indicates the minimum number of non-letter characters required for device password. Valid values 1 to 16
        Args:
            value: Value to set for the passwordMinimumNonLetterCharacters property.
        """
        self._password_minimum_non_letter_characters = value
    
    @property
    def password_minimum_numeric_characters(self,) -> Optional[int]:
        """
        Gets the passwordMinimumNumericCharacters property value. Indicates the minimum number of numeric characters required for device password. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._password_minimum_numeric_characters
    
    @password_minimum_numeric_characters.setter
    def password_minimum_numeric_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumNumericCharacters property value. Indicates the minimum number of numeric characters required for device password. Valid values 1 to 16
        Args:
            value: Value to set for the passwordMinimumNumericCharacters property.
        """
        self._password_minimum_numeric_characters = value
    
    @property
    def password_minimum_symbol_characters(self,) -> Optional[int]:
        """
        Gets the passwordMinimumSymbolCharacters property value. Indicates the minimum number of symbol characters required for device password. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._password_minimum_symbol_characters
    
    @password_minimum_symbol_characters.setter
    def password_minimum_symbol_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumSymbolCharacters property value. Indicates the minimum number of symbol characters required for device password. Valid values 1 to 16
        Args:
            value: Value to set for the passwordMinimumSymbolCharacters property.
        """
        self._password_minimum_symbol_characters = value
    
    @property
    def password_minimum_upper_case_characters(self,) -> Optional[int]:
        """
        Gets the passwordMinimumUpperCaseCharacters property value. Indicates the minimum number of upper case letter characters required for device password. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._password_minimum_upper_case_characters
    
    @password_minimum_upper_case_characters.setter
    def password_minimum_upper_case_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumUpperCaseCharacters property value. Indicates the minimum number of upper case letter characters required for device password. Valid values 1 to 16
        Args:
            value: Value to set for the passwordMinimumUpperCaseCharacters property.
        """
        self._password_minimum_upper_case_characters = value
    
    @property
    def password_minutes_of_inactivity_before_screen_timeout(self,) -> Optional[int]:
        """
        Gets the passwordMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity before the screen times out.
        Returns: Optional[int]
        """
        return self._password_minutes_of_inactivity_before_screen_timeout
    
    @password_minutes_of_inactivity_before_screen_timeout.setter
    def password_minutes_of_inactivity_before_screen_timeout(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity before the screen times out.
        Args:
            value: Value to set for the passwordMinutesOfInactivityBeforeScreenTimeout property.
        """
        self._password_minutes_of_inactivity_before_screen_timeout = value
    
    @property
    def password_previous_password_count_to_block(self,) -> Optional[int]:
        """
        Gets the passwordPreviousPasswordCountToBlock property value. Indicates the length of password history, where the user will not be able to enter a new password that is the same as any password in the history. Valid values 0 to 24
        Returns: Optional[int]
        """
        return self._password_previous_password_count_to_block
    
    @password_previous_password_count_to_block.setter
    def password_previous_password_count_to_block(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordPreviousPasswordCountToBlock property value. Indicates the length of password history, where the user will not be able to enter a new password that is the same as any password in the history. Valid values 0 to 24
        Args:
            value: Value to set for the passwordPreviousPasswordCountToBlock property.
        """
        self._password_previous_password_count_to_block = value
    
    @property
    def password_required_type(self,) -> Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType]:
        """
        Gets the passwordRequiredType property value. Indicates the minimum password quality required on the device. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
        Returns: Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType]
        """
        return self._password_required_type
    
    @password_required_type.setter
    def password_required_type(self,value: Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType] = None) -> None:
        """
        Sets the passwordRequiredType property value. Indicates the minimum password quality required on the device. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
        Args:
            value: Value to set for the passwordRequiredType property.
        """
        self._password_required_type = value
    
    @property
    def password_require_unlock(self,) -> Optional[android_device_owner_required_password_unlock.AndroidDeviceOwnerRequiredPasswordUnlock]:
        """
        Gets the passwordRequireUnlock property value. Indicates the timeout period after which a device must be unlocked using a form of strong authentication. Possible values are: deviceDefault, daily, unkownFutureValue.
        Returns: Optional[android_device_owner_required_password_unlock.AndroidDeviceOwnerRequiredPasswordUnlock]
        """
        return self._password_require_unlock
    
    @password_require_unlock.setter
    def password_require_unlock(self,value: Optional[android_device_owner_required_password_unlock.AndroidDeviceOwnerRequiredPasswordUnlock] = None) -> None:
        """
        Sets the passwordRequireUnlock property value. Indicates the timeout period after which a device must be unlocked using a form of strong authentication. Possible values are: deviceDefault, daily, unkownFutureValue.
        Args:
            value: Value to set for the passwordRequireUnlock property.
        """
        self._password_require_unlock = value
    
    @property
    def password_sign_in_failure_count_before_factory_reset(self,) -> Optional[int]:
        """
        Gets the passwordSignInFailureCountBeforeFactoryReset property value. Indicates the number of times a user can enter an incorrect password before the device is wiped. Valid values 4 to 11
        Returns: Optional[int]
        """
        return self._password_sign_in_failure_count_before_factory_reset
    
    @password_sign_in_failure_count_before_factory_reset.setter
    def password_sign_in_failure_count_before_factory_reset(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordSignInFailureCountBeforeFactoryReset property value. Indicates the number of times a user can enter an incorrect password before the device is wiped. Valid values 4 to 11
        Args:
            value: Value to set for the passwordSignInFailureCountBeforeFactoryReset property.
        """
        self._password_sign_in_failure_count_before_factory_reset = value
    
    @property
    def personal_profile_apps_allow_install_from_unknown_sources(self,) -> Optional[bool]:
        """
        Gets the personalProfileAppsAllowInstallFromUnknownSources property value. Indicates whether the user can install apps from unknown sources on the personal profile.
        Returns: Optional[bool]
        """
        return self._personal_profile_apps_allow_install_from_unknown_sources
    
    @personal_profile_apps_allow_install_from_unknown_sources.setter
    def personal_profile_apps_allow_install_from_unknown_sources(self,value: Optional[bool] = None) -> None:
        """
        Sets the personalProfileAppsAllowInstallFromUnknownSources property value. Indicates whether the user can install apps from unknown sources on the personal profile.
        Args:
            value: Value to set for the personalProfileAppsAllowInstallFromUnknownSources property.
        """
        self._personal_profile_apps_allow_install_from_unknown_sources = value
    
    @property
    def personal_profile_camera_blocked(self,) -> Optional[bool]:
        """
        Gets the personalProfileCameraBlocked property value. Indicates whether to disable the use of the camera on the personal profile.
        Returns: Optional[bool]
        """
        return self._personal_profile_camera_blocked
    
    @personal_profile_camera_blocked.setter
    def personal_profile_camera_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the personalProfileCameraBlocked property value. Indicates whether to disable the use of the camera on the personal profile.
        Args:
            value: Value to set for the personalProfileCameraBlocked property.
        """
        self._personal_profile_camera_blocked = value
    
    @property
    def personal_profile_personal_applications(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the personalProfilePersonalApplications property value. Policy applied to applications in the personal profile. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._personal_profile_personal_applications
    
    @personal_profile_personal_applications.setter
    def personal_profile_personal_applications(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the personalProfilePersonalApplications property value. Policy applied to applications in the personal profile. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the personalProfilePersonalApplications property.
        """
        self._personal_profile_personal_applications = value
    
    @property
    def personal_profile_play_store_mode(self,) -> Optional[personal_profile_personal_play_store_mode.PersonalProfilePersonalPlayStoreMode]:
        """
        Gets the personalProfilePlayStoreMode property value. Used together with PersonalProfilePersonalApplications to control how apps in the personal profile are allowed or blocked. Possible values are: notConfigured, blockedApps, allowedApps.
        Returns: Optional[personal_profile_personal_play_store_mode.PersonalProfilePersonalPlayStoreMode]
        """
        return self._personal_profile_play_store_mode
    
    @personal_profile_play_store_mode.setter
    def personal_profile_play_store_mode(self,value: Optional[personal_profile_personal_play_store_mode.PersonalProfilePersonalPlayStoreMode] = None) -> None:
        """
        Sets the personalProfilePlayStoreMode property value. Used together with PersonalProfilePersonalApplications to control how apps in the personal profile are allowed or blocked. Possible values are: notConfigured, blockedApps, allowedApps.
        Args:
            value: Value to set for the personalProfilePlayStoreMode property.
        """
        self._personal_profile_play_store_mode = value
    
    @property
    def personal_profile_screen_capture_blocked(self,) -> Optional[bool]:
        """
        Gets the personalProfileScreenCaptureBlocked property value. Indicates whether to disable the capability to take screenshots on the personal profile.
        Returns: Optional[bool]
        """
        return self._personal_profile_screen_capture_blocked
    
    @personal_profile_screen_capture_blocked.setter
    def personal_profile_screen_capture_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the personalProfileScreenCaptureBlocked property value. Indicates whether to disable the capability to take screenshots on the personal profile.
        Args:
            value: Value to set for the personalProfileScreenCaptureBlocked property.
        """
        self._personal_profile_screen_capture_blocked = value
    
    @property
    def play_store_mode(self,) -> Optional[android_device_owner_play_store_mode.AndroidDeviceOwnerPlayStoreMode]:
        """
        Gets the playStoreMode property value. Indicates the Play Store mode of the device. Possible values are: notConfigured, allowList, blockList.
        Returns: Optional[android_device_owner_play_store_mode.AndroidDeviceOwnerPlayStoreMode]
        """
        return self._play_store_mode
    
    @play_store_mode.setter
    def play_store_mode(self,value: Optional[android_device_owner_play_store_mode.AndroidDeviceOwnerPlayStoreMode] = None) -> None:
        """
        Sets the playStoreMode property value. Indicates the Play Store mode of the device. Possible values are: notConfigured, allowList, blockList.
        Args:
            value: Value to set for the playStoreMode property.
        """
        self._play_store_mode = value
    
    @property
    def screen_capture_blocked(self,) -> Optional[bool]:
        """
        Gets the screenCaptureBlocked property value. Indicates whether or not to disable the capability to take screenshots.
        Returns: Optional[bool]
        """
        return self._screen_capture_blocked
    
    @screen_capture_blocked.setter
    def screen_capture_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the screenCaptureBlocked property value. Indicates whether or not to disable the capability to take screenshots.
        Args:
            value: Value to set for the screenCaptureBlocked property.
        """
        self._screen_capture_blocked = value
    
    @property
    def security_common_criteria_mode_enabled(self,) -> Optional[bool]:
        """
        Gets the securityCommonCriteriaModeEnabled property value. Represents the security common criteria mode enabled provided to users when they attempt to modify managed settings on their device.
        Returns: Optional[bool]
        """
        return self._security_common_criteria_mode_enabled
    
    @security_common_criteria_mode_enabled.setter
    def security_common_criteria_mode_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityCommonCriteriaModeEnabled property value. Represents the security common criteria mode enabled provided to users when they attempt to modify managed settings on their device.
        Args:
            value: Value to set for the securityCommonCriteriaModeEnabled property.
        """
        self._security_common_criteria_mode_enabled = value
    
    @property
    def security_developer_settings_enabled(self,) -> Optional[bool]:
        """
        Gets the securityDeveloperSettingsEnabled property value. Indicates whether or not the user is allowed to access developer settings like developer options and safe boot on the device.
        Returns: Optional[bool]
        """
        return self._security_developer_settings_enabled
    
    @security_developer_settings_enabled.setter
    def security_developer_settings_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityDeveloperSettingsEnabled property value. Indicates whether or not the user is allowed to access developer settings like developer options and safe boot on the device.
        Args:
            value: Value to set for the securityDeveloperSettingsEnabled property.
        """
        self._security_developer_settings_enabled = value
    
    @property
    def security_require_verify_apps(self,) -> Optional[bool]:
        """
        Gets the securityRequireVerifyApps property value. Indicates whether or not verify apps is required.
        Returns: Optional[bool]
        """
        return self._security_require_verify_apps
    
    @security_require_verify_apps.setter
    def security_require_verify_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityRequireVerifyApps property value. Indicates whether or not verify apps is required.
        Args:
            value: Value to set for the securityRequireVerifyApps property.
        """
        self._security_require_verify_apps = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("accountsBlockModification", self.accounts_block_modification)
        writer.write_bool_value("appsAllowInstallFromUnknownSources", self.apps_allow_install_from_unknown_sources)
        writer.write_enum_value("appsAutoUpdatePolicy", self.apps_auto_update_policy)
        writer.write_enum_value("appsDefaultPermissionPolicy", self.apps_default_permission_policy)
        writer.write_bool_value("appsRecommendSkippingFirstUseHints", self.apps_recommend_skipping_first_use_hints)
        writer.write_collection_of_object_values("azureAdSharedDeviceDataClearApps", self.azure_ad_shared_device_data_clear_apps)
        writer.write_bool_value("bluetoothBlockConfiguration", self.bluetooth_block_configuration)
        writer.write_bool_value("bluetoothBlockContactSharing", self.bluetooth_block_contact_sharing)
        writer.write_bool_value("cameraBlocked", self.camera_blocked)
        writer.write_bool_value("cellularBlockWiFiTethering", self.cellular_block_wi_fi_tethering)
        writer.write_bool_value("certificateCredentialConfigurationDisabled", self.certificate_credential_configuration_disabled)
        writer.write_bool_value("crossProfilePoliciesAllowCopyPaste", self.cross_profile_policies_allow_copy_paste)
        writer.write_enum_value("crossProfilePoliciesAllowDataSharing", self.cross_profile_policies_allow_data_sharing)
        writer.write_bool_value("crossProfilePoliciesShowWorkContactsInPersonalProfile", self.cross_profile_policies_show_work_contacts_in_personal_profile)
        writer.write_bool_value("dataRoamingBlocked", self.data_roaming_blocked)
        writer.write_bool_value("dateTimeConfigurationBlocked", self.date_time_configuration_blocked)
        writer.write_object_value("detailedHelpText", self.detailed_help_text)
        writer.write_object_value("deviceOwnerLockScreenMessage", self.device_owner_lock_screen_message)
        writer.write_enum_value("enrollmentProfile", self.enrollment_profile)
        writer.write_bool_value("factoryResetBlocked", self.factory_reset_blocked)
        writer.write_collection_of_primitive_values("factoryResetDeviceAdministratorEmails", self.factory_reset_device_administrator_emails)
        writer.write_object_value("globalProxy", self.global_proxy)
        writer.write_bool_value("googleAccountsBlocked", self.google_accounts_blocked)
        writer.write_bool_value("kioskCustomizationDeviceSettingsBlocked", self.kiosk_customization_device_settings_blocked)
        writer.write_bool_value("kioskCustomizationPowerButtonActionsBlocked", self.kiosk_customization_power_button_actions_blocked)
        writer.write_enum_value("kioskCustomizationStatusBar", self.kiosk_customization_status_bar)
        writer.write_bool_value("kioskCustomizationSystemErrorWarnings", self.kiosk_customization_system_error_warnings)
        writer.write_enum_value("kioskCustomizationSystemNavigation", self.kiosk_customization_system_navigation)
        writer.write_bool_value("kioskModeAppOrderEnabled", self.kiosk_mode_app_order_enabled)
        writer.write_collection_of_object_values("kioskModeAppPositions", self.kiosk_mode_app_positions)
        writer.write_collection_of_object_values("kioskModeApps", self.kiosk_mode_apps)
        writer.write_bool_value("kioskModeAppsInFolderOrderedByName", self.kiosk_mode_apps_in_folder_ordered_by_name)
        writer.write_bool_value("kioskModeBluetoothConfigurationEnabled", self.kiosk_mode_bluetooth_configuration_enabled)
        writer.write_bool_value("kioskModeDebugMenuEasyAccessEnabled", self.kiosk_mode_debug_menu_easy_access_enabled)
        writer.write_str_value("kioskModeExitCode", self.kiosk_mode_exit_code)
        writer.write_bool_value("kioskModeFlashlightConfigurationEnabled", self.kiosk_mode_flashlight_configuration_enabled)
        writer.write_enum_value("kioskModeFolderIcon", self.kiosk_mode_folder_icon)
        writer.write_int_value("kioskModeGridHeight", self.kiosk_mode_grid_height)
        writer.write_int_value("kioskModeGridWidth", self.kiosk_mode_grid_width)
        writer.write_enum_value("kioskModeIconSize", self.kiosk_mode_icon_size)
        writer.write_bool_value("kioskModeLockHomeScreen", self.kiosk_mode_lock_home_screen)
        writer.write_collection_of_object_values("kioskModeManagedFolders", self.kiosk_mode_managed_folders)
        writer.write_bool_value("kioskModeManagedHomeScreenAutoSignout", self.kiosk_mode_managed_home_screen_auto_signout)
        writer.write_int_value("kioskModeManagedHomeScreenInactiveSignOutDelayInSeconds", self.kiosk_mode_managed_home_screen_inactive_sign_out_delay_in_seconds)
        writer.write_int_value("kioskModeManagedHomeScreenInactiveSignOutNoticeInSeconds", self.kiosk_mode_managed_home_screen_inactive_sign_out_notice_in_seconds)
        writer.write_enum_value("kioskModeManagedHomeScreenPinComplexity", self.kiosk_mode_managed_home_screen_pin_complexity)
        writer.write_bool_value("kioskModeManagedHomeScreenPinRequired", self.kiosk_mode_managed_home_screen_pin_required)
        writer.write_bool_value("kioskModeManagedHomeScreenPinRequiredToResume", self.kiosk_mode_managed_home_screen_pin_required_to_resume)
        writer.write_str_value("kioskModeManagedHomeScreenSignInBackground", self.kiosk_mode_managed_home_screen_sign_in_background)
        writer.write_str_value("kioskModeManagedHomeScreenSignInBrandingLogo", self.kiosk_mode_managed_home_screen_sign_in_branding_logo)
        writer.write_bool_value("kioskModeManagedHomeScreenSignInEnabled", self.kiosk_mode_managed_home_screen_sign_in_enabled)
        writer.write_bool_value("kioskModeManagedSettingsEntryDisabled", self.kiosk_mode_managed_settings_entry_disabled)
        writer.write_bool_value("kioskModeMediaVolumeConfigurationEnabled", self.kiosk_mode_media_volume_configuration_enabled)
        writer.write_enum_value("kioskModeScreenOrientation", self.kiosk_mode_screen_orientation)
        writer.write_bool_value("kioskModeScreenSaverConfigurationEnabled", self.kiosk_mode_screen_saver_configuration_enabled)
        writer.write_bool_value("kioskModeScreenSaverDetectMediaDisabled", self.kiosk_mode_screen_saver_detect_media_disabled)
        writer.write_int_value("kioskModeScreenSaverDisplayTimeInSeconds", self.kiosk_mode_screen_saver_display_time_in_seconds)
        writer.write_str_value("kioskModeScreenSaverImageUrl", self.kiosk_mode_screen_saver_image_url)
        writer.write_int_value("kioskModeScreenSaverStartDelayInSeconds", self.kiosk_mode_screen_saver_start_delay_in_seconds)
        writer.write_bool_value("kioskModeShowAppNotificationBadge", self.kiosk_mode_show_app_notification_badge)
        writer.write_bool_value("kioskModeShowDeviceInfo", self.kiosk_mode_show_device_info)
        writer.write_enum_value("kioskModeUseManagedHomeScreenApp", self.kiosk_mode_use_managed_home_screen_app)
        writer.write_bool_value("kioskModeVirtualHomeButtonEnabled", self.kiosk_mode_virtual_home_button_enabled)
        writer.write_enum_value("kioskModeVirtualHomeButtonType", self.kiosk_mode_virtual_home_button_type)
        writer.write_str_value("kioskModeWallpaperUrl", self.kiosk_mode_wallpaper_url)
        writer.write_collection_of_primitive_values("kioskModeWifiAllowedSsids", self.kiosk_mode_wifi_allowed_ssids)
        writer.write_bool_value("kioskModeWiFiConfigurationEnabled", self.kiosk_mode_wi_fi_configuration_enabled)
        writer.write_bool_value("microphoneForceMute", self.microphone_force_mute)
        writer.write_bool_value("microsoftLauncherConfigurationEnabled", self.microsoft_launcher_configuration_enabled)
        writer.write_bool_value("microsoftLauncherCustomWallpaperAllowUserModification", self.microsoft_launcher_custom_wallpaper_allow_user_modification)
        writer.write_bool_value("microsoftLauncherCustomWallpaperEnabled", self.microsoft_launcher_custom_wallpaper_enabled)
        writer.write_str_value("microsoftLauncherCustomWallpaperImageUrl", self.microsoft_launcher_custom_wallpaper_image_url)
        writer.write_bool_value("microsoftLauncherDockPresenceAllowUserModification", self.microsoft_launcher_dock_presence_allow_user_modification)
        writer.write_enum_value("microsoftLauncherDockPresenceConfiguration", self.microsoft_launcher_dock_presence_configuration)
        writer.write_bool_value("microsoftLauncherFeedAllowUserModification", self.microsoft_launcher_feed_allow_user_modification)
        writer.write_bool_value("microsoftLauncherFeedEnabled", self.microsoft_launcher_feed_enabled)
        writer.write_enum_value("microsoftLauncherSearchBarPlacementConfiguration", self.microsoft_launcher_search_bar_placement_configuration)
        writer.write_bool_value("networkEscapeHatchAllowed", self.network_escape_hatch_allowed)
        writer.write_bool_value("nfcBlockOutgoingBeam", self.nfc_block_outgoing_beam)
        writer.write_bool_value("passwordBlockKeyguard", self.password_block_keyguard)
        writer.write_enum_value("passwordBlockKeyguardFeatures", self.password_block_keyguard_features)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinimumLetterCharacters", self.password_minimum_letter_characters)
        writer.write_int_value("passwordMinimumLowerCaseCharacters", self.password_minimum_lower_case_characters)
        writer.write_int_value("passwordMinimumNonLetterCharacters", self.password_minimum_non_letter_characters)
        writer.write_int_value("passwordMinimumNumericCharacters", self.password_minimum_numeric_characters)
        writer.write_int_value("passwordMinimumSymbolCharacters", self.password_minimum_symbol_characters)
        writer.write_int_value("passwordMinimumUpperCaseCharacters", self.password_minimum_upper_case_characters)
        writer.write_int_value("passwordMinutesOfInactivityBeforeScreenTimeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("passwordPreviousPasswordCountToBlock", self.password_previous_password_count_to_block)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_enum_value("passwordRequireUnlock", self.password_require_unlock)
        writer.write_int_value("passwordSignInFailureCountBeforeFactoryReset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_bool_value("personalProfileAppsAllowInstallFromUnknownSources", self.personal_profile_apps_allow_install_from_unknown_sources)
        writer.write_bool_value("personalProfileCameraBlocked", self.personal_profile_camera_blocked)
        writer.write_collection_of_object_values("personalProfilePersonalApplications", self.personal_profile_personal_applications)
        writer.write_enum_value("personalProfilePlayStoreMode", self.personal_profile_play_store_mode)
        writer.write_bool_value("personalProfileScreenCaptureBlocked", self.personal_profile_screen_capture_blocked)
        writer.write_enum_value("playStoreMode", self.play_store_mode)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_bool_value("securityCommonCriteriaModeEnabled", self.security_common_criteria_mode_enabled)
        writer.write_bool_value("securityDeveloperSettingsEnabled", self.security_developer_settings_enabled)
        writer.write_bool_value("securityRequireVerifyApps", self.security_require_verify_apps)
        writer.write_object_value("shortHelpText", self.short_help_text)
        writer.write_bool_value("statusBarBlocked", self.status_bar_blocked)
        writer.write_enum_value("stayOnModes", self.stay_on_modes)
        writer.write_bool_value("storageAllowUsb", self.storage_allow_usb)
        writer.write_bool_value("storageBlockExternalMedia", self.storage_block_external_media)
        writer.write_bool_value("storageBlockUsbFileTransfer", self.storage_block_usb_file_transfer)
        writer.write_collection_of_object_values("systemUpdateFreezePeriods", self.system_update_freeze_periods)
        writer.write_enum_value("systemUpdateInstallType", self.system_update_install_type)
        writer.write_int_value("systemUpdateWindowEndMinutesAfterMidnight", self.system_update_window_end_minutes_after_midnight)
        writer.write_int_value("systemUpdateWindowStartMinutesAfterMidnight", self.system_update_window_start_minutes_after_midnight)
        writer.write_bool_value("systemWindowsBlocked", self.system_windows_blocked)
        writer.write_bool_value("usersBlockAdd", self.users_block_add)
        writer.write_bool_value("usersBlockRemove", self.users_block_remove)
        writer.write_bool_value("volumeBlockAdjustment", self.volume_block_adjustment)
        writer.write_bool_value("vpnAlwaysOnLockdownMode", self.vpn_always_on_lockdown_mode)
        writer.write_str_value("vpnAlwaysOnPackageIdentifier", self.vpn_always_on_package_identifier)
        writer.write_bool_value("wifiBlockEditConfigurations", self.wifi_block_edit_configurations)
        writer.write_bool_value("wifiBlockEditPolicyDefinedConfigurations", self.wifi_block_edit_policy_defined_configurations)
        writer.write_int_value("workProfilePasswordExpirationDays", self.work_profile_password_expiration_days)
        writer.write_int_value("workProfilePasswordMinimumLength", self.work_profile_password_minimum_length)
        writer.write_int_value("workProfilePasswordMinimumLetterCharacters", self.work_profile_password_minimum_letter_characters)
        writer.write_int_value("workProfilePasswordMinimumLowerCaseCharacters", self.work_profile_password_minimum_lower_case_characters)
        writer.write_int_value("workProfilePasswordMinimumNonLetterCharacters", self.work_profile_password_minimum_non_letter_characters)
        writer.write_int_value("workProfilePasswordMinimumNumericCharacters", self.work_profile_password_minimum_numeric_characters)
        writer.write_int_value("workProfilePasswordMinimumSymbolCharacters", self.work_profile_password_minimum_symbol_characters)
        writer.write_int_value("workProfilePasswordMinimumUpperCaseCharacters", self.work_profile_password_minimum_upper_case_characters)
        writer.write_int_value("workProfilePasswordPreviousPasswordCountToBlock", self.work_profile_password_previous_password_count_to_block)
        writer.write_enum_value("workProfilePasswordRequiredType", self.work_profile_password_required_type)
        writer.write_enum_value("workProfilePasswordRequireUnlock", self.work_profile_password_require_unlock)
        writer.write_int_value("workProfilePasswordSignInFailureCountBeforeFactoryReset", self.work_profile_password_sign_in_failure_count_before_factory_reset)
    
    @property
    def short_help_text(self,) -> Optional[android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage]:
        """
        Gets the shortHelpText property value. Represents the customized short help text provided to users when they attempt to modify managed settings on their device.
        Returns: Optional[android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage]
        """
        return self._short_help_text
    
    @short_help_text.setter
    def short_help_text(self,value: Optional[android_device_owner_user_facing_message.AndroidDeviceOwnerUserFacingMessage] = None) -> None:
        """
        Sets the shortHelpText property value. Represents the customized short help text provided to users when they attempt to modify managed settings on their device.
        Args:
            value: Value to set for the shortHelpText property.
        """
        self._short_help_text = value
    
    @property
    def status_bar_blocked(self,) -> Optional[bool]:
        """
        Gets the statusBarBlocked property value. Indicates whether or the status bar is disabled, including notifications, quick settings and other screen overlays.
        Returns: Optional[bool]
        """
        return self._status_bar_blocked
    
    @status_bar_blocked.setter
    def status_bar_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the statusBarBlocked property value. Indicates whether or the status bar is disabled, including notifications, quick settings and other screen overlays.
        Args:
            value: Value to set for the statusBarBlocked property.
        """
        self._status_bar_blocked = value
    
    @property
    def stay_on_modes(self,) -> Optional[List[android_device_owner_battery_plugged_mode.AndroidDeviceOwnerBatteryPluggedMode]]:
        """
        Gets the stayOnModes property value. List of modes in which the device's display will stay powered-on. This collection can contain a maximum of 4 elements.
        Returns: Optional[List[android_device_owner_battery_plugged_mode.AndroidDeviceOwnerBatteryPluggedMode]]
        """
        return self._stay_on_modes
    
    @stay_on_modes.setter
    def stay_on_modes(self,value: Optional[List[android_device_owner_battery_plugged_mode.AndroidDeviceOwnerBatteryPluggedMode]] = None) -> None:
        """
        Sets the stayOnModes property value. List of modes in which the device's display will stay powered-on. This collection can contain a maximum of 4 elements.
        Args:
            value: Value to set for the stayOnModes property.
        """
        self._stay_on_modes = value
    
    @property
    def storage_allow_usb(self,) -> Optional[bool]:
        """
        Gets the storageAllowUsb property value. Indicates whether or not to allow USB mass storage.
        Returns: Optional[bool]
        """
        return self._storage_allow_usb
    
    @storage_allow_usb.setter
    def storage_allow_usb(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageAllowUsb property value. Indicates whether or not to allow USB mass storage.
        Args:
            value: Value to set for the storageAllowUsb property.
        """
        self._storage_allow_usb = value
    
    @property
    def storage_block_external_media(self,) -> Optional[bool]:
        """
        Gets the storageBlockExternalMedia property value. Indicates whether or not to block external media.
        Returns: Optional[bool]
        """
        return self._storage_block_external_media
    
    @storage_block_external_media.setter
    def storage_block_external_media(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageBlockExternalMedia property value. Indicates whether or not to block external media.
        Args:
            value: Value to set for the storageBlockExternalMedia property.
        """
        self._storage_block_external_media = value
    
    @property
    def storage_block_usb_file_transfer(self,) -> Optional[bool]:
        """
        Gets the storageBlockUsbFileTransfer property value. Indicates whether or not to block USB file transfer.
        Returns: Optional[bool]
        """
        return self._storage_block_usb_file_transfer
    
    @storage_block_usb_file_transfer.setter
    def storage_block_usb_file_transfer(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageBlockUsbFileTransfer property value. Indicates whether or not to block USB file transfer.
        Args:
            value: Value to set for the storageBlockUsbFileTransfer property.
        """
        self._storage_block_usb_file_transfer = value
    
    @property
    def system_update_freeze_periods(self,) -> Optional[List[android_device_owner_system_update_freeze_period.AndroidDeviceOwnerSystemUpdateFreezePeriod]]:
        """
        Gets the systemUpdateFreezePeriods property value. Indicates the annually repeating time periods during which system updates are postponed. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[android_device_owner_system_update_freeze_period.AndroidDeviceOwnerSystemUpdateFreezePeriod]]
        """
        return self._system_update_freeze_periods
    
    @system_update_freeze_periods.setter
    def system_update_freeze_periods(self,value: Optional[List[android_device_owner_system_update_freeze_period.AndroidDeviceOwnerSystemUpdateFreezePeriod]] = None) -> None:
        """
        Sets the systemUpdateFreezePeriods property value. Indicates the annually repeating time periods during which system updates are postponed. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the systemUpdateFreezePeriods property.
        """
        self._system_update_freeze_periods = value
    
    @property
    def system_update_install_type(self,) -> Optional[android_device_owner_system_update_install_type.AndroidDeviceOwnerSystemUpdateInstallType]:
        """
        Gets the systemUpdateInstallType property value. The type of system update configuration. Possible values are: deviceDefault, postpone, windowed, automatic.
        Returns: Optional[android_device_owner_system_update_install_type.AndroidDeviceOwnerSystemUpdateInstallType]
        """
        return self._system_update_install_type
    
    @system_update_install_type.setter
    def system_update_install_type(self,value: Optional[android_device_owner_system_update_install_type.AndroidDeviceOwnerSystemUpdateInstallType] = None) -> None:
        """
        Sets the systemUpdateInstallType property value. The type of system update configuration. Possible values are: deviceDefault, postpone, windowed, automatic.
        Args:
            value: Value to set for the systemUpdateInstallType property.
        """
        self._system_update_install_type = value
    
    @property
    def system_update_window_end_minutes_after_midnight(self,) -> Optional[int]:
        """
        Gets the systemUpdateWindowEndMinutesAfterMidnight property value. Indicates the number of minutes after midnight that the system update window ends. Valid values 0 to 1440
        Returns: Optional[int]
        """
        return self._system_update_window_end_minutes_after_midnight
    
    @system_update_window_end_minutes_after_midnight.setter
    def system_update_window_end_minutes_after_midnight(self,value: Optional[int] = None) -> None:
        """
        Sets the systemUpdateWindowEndMinutesAfterMidnight property value. Indicates the number of minutes after midnight that the system update window ends. Valid values 0 to 1440
        Args:
            value: Value to set for the systemUpdateWindowEndMinutesAfterMidnight property.
        """
        self._system_update_window_end_minutes_after_midnight = value
    
    @property
    def system_update_window_start_minutes_after_midnight(self,) -> Optional[int]:
        """
        Gets the systemUpdateWindowStartMinutesAfterMidnight property value. Indicates the number of minutes after midnight that the system update window starts. Valid values 0 to 1440
        Returns: Optional[int]
        """
        return self._system_update_window_start_minutes_after_midnight
    
    @system_update_window_start_minutes_after_midnight.setter
    def system_update_window_start_minutes_after_midnight(self,value: Optional[int] = None) -> None:
        """
        Sets the systemUpdateWindowStartMinutesAfterMidnight property value. Indicates the number of minutes after midnight that the system update window starts. Valid values 0 to 1440
        Args:
            value: Value to set for the systemUpdateWindowStartMinutesAfterMidnight property.
        """
        self._system_update_window_start_minutes_after_midnight = value
    
    @property
    def system_windows_blocked(self,) -> Optional[bool]:
        """
        Gets the systemWindowsBlocked property value. Whether or not to block Android system prompt windows, like toasts, phone activities, and system alerts.
        Returns: Optional[bool]
        """
        return self._system_windows_blocked
    
    @system_windows_blocked.setter
    def system_windows_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the systemWindowsBlocked property value. Whether or not to block Android system prompt windows, like toasts, phone activities, and system alerts.
        Args:
            value: Value to set for the systemWindowsBlocked property.
        """
        self._system_windows_blocked = value
    
    @property
    def users_block_add(self,) -> Optional[bool]:
        """
        Gets the usersBlockAdd property value. Indicates whether or not adding users and profiles is disabled.
        Returns: Optional[bool]
        """
        return self._users_block_add
    
    @users_block_add.setter
    def users_block_add(self,value: Optional[bool] = None) -> None:
        """
        Sets the usersBlockAdd property value. Indicates whether or not adding users and profiles is disabled.
        Args:
            value: Value to set for the usersBlockAdd property.
        """
        self._users_block_add = value
    
    @property
    def users_block_remove(self,) -> Optional[bool]:
        """
        Gets the usersBlockRemove property value. Indicates whether or not to disable removing other users from the device.
        Returns: Optional[bool]
        """
        return self._users_block_remove
    
    @users_block_remove.setter
    def users_block_remove(self,value: Optional[bool] = None) -> None:
        """
        Sets the usersBlockRemove property value. Indicates whether or not to disable removing other users from the device.
        Args:
            value: Value to set for the usersBlockRemove property.
        """
        self._users_block_remove = value
    
    @property
    def volume_block_adjustment(self,) -> Optional[bool]:
        """
        Gets the volumeBlockAdjustment property value. Indicates whether or not adjusting the master volume is disabled.
        Returns: Optional[bool]
        """
        return self._volume_block_adjustment
    
    @volume_block_adjustment.setter
    def volume_block_adjustment(self,value: Optional[bool] = None) -> None:
        """
        Sets the volumeBlockAdjustment property value. Indicates whether or not adjusting the master volume is disabled.
        Args:
            value: Value to set for the volumeBlockAdjustment property.
        """
        self._volume_block_adjustment = value
    
    @property
    def vpn_always_on_lockdown_mode(self,) -> Optional[bool]:
        """
        Gets the vpnAlwaysOnLockdownMode property value. If an always on VPN package name is specified, whether or not to lock network traffic when that VPN is disconnected.
        Returns: Optional[bool]
        """
        return self._vpn_always_on_lockdown_mode
    
    @vpn_always_on_lockdown_mode.setter
    def vpn_always_on_lockdown_mode(self,value: Optional[bool] = None) -> None:
        """
        Sets the vpnAlwaysOnLockdownMode property value. If an always on VPN package name is specified, whether or not to lock network traffic when that VPN is disconnected.
        Args:
            value: Value to set for the vpnAlwaysOnLockdownMode property.
        """
        self._vpn_always_on_lockdown_mode = value
    
    @property
    def vpn_always_on_package_identifier(self,) -> Optional[str]:
        """
        Gets the vpnAlwaysOnPackageIdentifier property value. Android app package name for app that will handle an always-on VPN connection.
        Returns: Optional[str]
        """
        return self._vpn_always_on_package_identifier
    
    @vpn_always_on_package_identifier.setter
    def vpn_always_on_package_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the vpnAlwaysOnPackageIdentifier property value. Android app package name for app that will handle an always-on VPN connection.
        Args:
            value: Value to set for the vpnAlwaysOnPackageIdentifier property.
        """
        self._vpn_always_on_package_identifier = value
    
    @property
    def wifi_block_edit_configurations(self,) -> Optional[bool]:
        """
        Gets the wifiBlockEditConfigurations property value. Indicates whether or not to block the user from editing the wifi connection settings.
        Returns: Optional[bool]
        """
        return self._wifi_block_edit_configurations
    
    @wifi_block_edit_configurations.setter
    def wifi_block_edit_configurations(self,value: Optional[bool] = None) -> None:
        """
        Sets the wifiBlockEditConfigurations property value. Indicates whether or not to block the user from editing the wifi connection settings.
        Args:
            value: Value to set for the wifiBlockEditConfigurations property.
        """
        self._wifi_block_edit_configurations = value
    
    @property
    def wifi_block_edit_policy_defined_configurations(self,) -> Optional[bool]:
        """
        Gets the wifiBlockEditPolicyDefinedConfigurations property value. Indicates whether or not to block the user from editing just the networks defined by the policy.
        Returns: Optional[bool]
        """
        return self._wifi_block_edit_policy_defined_configurations
    
    @wifi_block_edit_policy_defined_configurations.setter
    def wifi_block_edit_policy_defined_configurations(self,value: Optional[bool] = None) -> None:
        """
        Sets the wifiBlockEditPolicyDefinedConfigurations property value. Indicates whether or not to block the user from editing just the networks defined by the policy.
        Args:
            value: Value to set for the wifiBlockEditPolicyDefinedConfigurations property.
        """
        self._wifi_block_edit_policy_defined_configurations = value
    
    @property
    def work_profile_password_expiration_days(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordExpirationDays property value. Indicates the number of days that a work profile password can be set before it expires and a new password will be required. Valid values 1 to 365
        Returns: Optional[int]
        """
        return self._work_profile_password_expiration_days
    
    @work_profile_password_expiration_days.setter
    def work_profile_password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordExpirationDays property value. Indicates the number of days that a work profile password can be set before it expires and a new password will be required. Valid values 1 to 365
        Args:
            value: Value to set for the workProfilePasswordExpirationDays property.
        """
        self._work_profile_password_expiration_days = value
    
    @property
    def work_profile_password_minimum_length(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinimumLength property value. Indicates the minimum length of the work profile password. Valid values 4 to 16
        Returns: Optional[int]
        """
        return self._work_profile_password_minimum_length
    
    @work_profile_password_minimum_length.setter
    def work_profile_password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinimumLength property value. Indicates the minimum length of the work profile password. Valid values 4 to 16
        Args:
            value: Value to set for the workProfilePasswordMinimumLength property.
        """
        self._work_profile_password_minimum_length = value
    
    @property
    def work_profile_password_minimum_letter_characters(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinimumLetterCharacters property value. Indicates the minimum number of letter characters required for the work profile password. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._work_profile_password_minimum_letter_characters
    
    @work_profile_password_minimum_letter_characters.setter
    def work_profile_password_minimum_letter_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinimumLetterCharacters property value. Indicates the minimum number of letter characters required for the work profile password. Valid values 1 to 16
        Args:
            value: Value to set for the workProfilePasswordMinimumLetterCharacters property.
        """
        self._work_profile_password_minimum_letter_characters = value
    
    @property
    def work_profile_password_minimum_lower_case_characters(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinimumLowerCaseCharacters property value. Indicates the minimum number of lower-case characters required for the work profile password. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._work_profile_password_minimum_lower_case_characters
    
    @work_profile_password_minimum_lower_case_characters.setter
    def work_profile_password_minimum_lower_case_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinimumLowerCaseCharacters property value. Indicates the minimum number of lower-case characters required for the work profile password. Valid values 1 to 16
        Args:
            value: Value to set for the workProfilePasswordMinimumLowerCaseCharacters property.
        """
        self._work_profile_password_minimum_lower_case_characters = value
    
    @property
    def work_profile_password_minimum_non_letter_characters(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinimumNonLetterCharacters property value. Indicates the minimum number of non-letter characters required for the work profile password. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._work_profile_password_minimum_non_letter_characters
    
    @work_profile_password_minimum_non_letter_characters.setter
    def work_profile_password_minimum_non_letter_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinimumNonLetterCharacters property value. Indicates the minimum number of non-letter characters required for the work profile password. Valid values 1 to 16
        Args:
            value: Value to set for the workProfilePasswordMinimumNonLetterCharacters property.
        """
        self._work_profile_password_minimum_non_letter_characters = value
    
    @property
    def work_profile_password_minimum_numeric_characters(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinimumNumericCharacters property value. Indicates the minimum number of numeric characters required for the work profile password. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._work_profile_password_minimum_numeric_characters
    
    @work_profile_password_minimum_numeric_characters.setter
    def work_profile_password_minimum_numeric_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinimumNumericCharacters property value. Indicates the minimum number of numeric characters required for the work profile password. Valid values 1 to 16
        Args:
            value: Value to set for the workProfilePasswordMinimumNumericCharacters property.
        """
        self._work_profile_password_minimum_numeric_characters = value
    
    @property
    def work_profile_password_minimum_symbol_characters(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinimumSymbolCharacters property value. Indicates the minimum number of symbol characters required for the work profile password. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._work_profile_password_minimum_symbol_characters
    
    @work_profile_password_minimum_symbol_characters.setter
    def work_profile_password_minimum_symbol_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinimumSymbolCharacters property value. Indicates the minimum number of symbol characters required for the work profile password. Valid values 1 to 16
        Args:
            value: Value to set for the workProfilePasswordMinimumSymbolCharacters property.
        """
        self._work_profile_password_minimum_symbol_characters = value
    
    @property
    def work_profile_password_minimum_upper_case_characters(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinimumUpperCaseCharacters property value. Indicates the minimum number of upper-case letter characters required for the work profile password. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._work_profile_password_minimum_upper_case_characters
    
    @work_profile_password_minimum_upper_case_characters.setter
    def work_profile_password_minimum_upper_case_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinimumUpperCaseCharacters property value. Indicates the minimum number of upper-case letter characters required for the work profile password. Valid values 1 to 16
        Args:
            value: Value to set for the workProfilePasswordMinimumUpperCaseCharacters property.
        """
        self._work_profile_password_minimum_upper_case_characters = value
    
    @property
    def work_profile_password_previous_password_count_to_block(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordPreviousPasswordCountToBlock property value. Indicates the length of the work profile password history, where the user will not be able to enter a new password that is the same as any password in the history. Valid values 0 to 24
        Returns: Optional[int]
        """
        return self._work_profile_password_previous_password_count_to_block
    
    @work_profile_password_previous_password_count_to_block.setter
    def work_profile_password_previous_password_count_to_block(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordPreviousPasswordCountToBlock property value. Indicates the length of the work profile password history, where the user will not be able to enter a new password that is the same as any password in the history. Valid values 0 to 24
        Args:
            value: Value to set for the workProfilePasswordPreviousPasswordCountToBlock property.
        """
        self._work_profile_password_previous_password_count_to_block = value
    
    @property
    def work_profile_password_required_type(self,) -> Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType]:
        """
        Gets the workProfilePasswordRequiredType property value. Indicates the minimum password quality required on the work profile password. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
        Returns: Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType]
        """
        return self._work_profile_password_required_type
    
    @work_profile_password_required_type.setter
    def work_profile_password_required_type(self,value: Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType] = None) -> None:
        """
        Sets the workProfilePasswordRequiredType property value. Indicates the minimum password quality required on the work profile password. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
        Args:
            value: Value to set for the workProfilePasswordRequiredType property.
        """
        self._work_profile_password_required_type = value
    
    @property
    def work_profile_password_require_unlock(self,) -> Optional[android_device_owner_required_password_unlock.AndroidDeviceOwnerRequiredPasswordUnlock]:
        """
        Gets the workProfilePasswordRequireUnlock property value. Indicates the timeout period after which a work profile must be unlocked using a form of strong authentication. Possible values are: deviceDefault, daily, unkownFutureValue.
        Returns: Optional[android_device_owner_required_password_unlock.AndroidDeviceOwnerRequiredPasswordUnlock]
        """
        return self._work_profile_password_require_unlock
    
    @work_profile_password_require_unlock.setter
    def work_profile_password_require_unlock(self,value: Optional[android_device_owner_required_password_unlock.AndroidDeviceOwnerRequiredPasswordUnlock] = None) -> None:
        """
        Sets the workProfilePasswordRequireUnlock property value. Indicates the timeout period after which a work profile must be unlocked using a form of strong authentication. Possible values are: deviceDefault, daily, unkownFutureValue.
        Args:
            value: Value to set for the workProfilePasswordRequireUnlock property.
        """
        self._work_profile_password_require_unlock = value
    
    @property
    def work_profile_password_sign_in_failure_count_before_factory_reset(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordSignInFailureCountBeforeFactoryReset property value. Indicates the number of times a user can enter an incorrect work profile password before the device is wiped. Valid values 4 to 11
        Returns: Optional[int]
        """
        return self._work_profile_password_sign_in_failure_count_before_factory_reset
    
    @work_profile_password_sign_in_failure_count_before_factory_reset.setter
    def work_profile_password_sign_in_failure_count_before_factory_reset(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordSignInFailureCountBeforeFactoryReset property value. Indicates the number of times a user can enter an incorrect work profile password before the device is wiped. Valid values 4 to 11
        Args:
            value: Value to set for the workProfilePasswordSignInFailureCountBeforeFactoryReset property.
        """
        self._work_profile_password_sign_in_failure_count_before_factory_reset = value
    

