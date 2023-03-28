from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_list_item, app_list_type, device_configuration, ios_kiosk_mode_app_type, ios_network_usage_rule, media_content_rating_australia, media_content_rating_canada, media_content_rating_france, media_content_rating_germany, media_content_rating_ireland, media_content_rating_japan, media_content_rating_new_zealand, media_content_rating_united_kingdom, media_content_rating_united_states, rating_apps_type, required_password_type, web_browser_cookie_settings

from . import device_configuration

class IosGeneralDeviceConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new IosGeneralDeviceConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosGeneralDeviceConfiguration"
        # Indicates whether or not to allow account modification when the device is in supervised mode.
        self._account_block_modification: Optional[bool] = None
        # Indicates whether or not to allow activation lock when the device is in the supervised mode.
        self._activation_lock_allow_when_supervised: Optional[bool] = None
        # Indicates whether or not to allow AirDrop when the device is in supervised mode.
        self._air_drop_blocked: Optional[bool] = None
        # Indicates whether or not to cause AirDrop to be considered an unmanaged drop target (iOS 9.0 and later).
        self._air_drop_force_unmanaged_drop_target: Optional[bool] = None
        # Indicates whether or not to enforce all devices receiving AirPlay requests from this device to use a pairing password.
        self._air_play_force_pairing_password_for_outgoing_requests: Optional[bool] = None
        # Indicates whether or not keychain storage of username and password for Airprint is blocked (iOS 11.0 and later).
        self._air_print_block_credentials_storage: Optional[bool] = None
        # Indicates whether or not AirPrint is blocked (iOS 11.0 and later).
        self._air_print_blocked: Optional[bool] = None
        # Indicates whether or not iBeacon discovery of AirPrint printers is blocked. This prevents spurious AirPrint Bluetooth beacons from phishing for network traffic (iOS 11.0 and later).
        self._air_print_blocki_beacon_discovery: Optional[bool] = None
        # Indicates if trusted certificates are required for TLS printing communication (iOS 11.0 and later).
        self._air_print_force_trusted_t_l_s: Optional[bool] = None
        # Prevents a user from adding any App Clips and removes any existing App Clips on the device.
        self._app_clips_blocked: Optional[bool] = None
        # Indicates if the removal of apps is allowed.
        self._app_removal_blocked: Optional[bool] = None
        # Indicates whether or not to block the automatic downloading of apps purchased on other devices when the device is in supervised mode (iOS 9.0 and later).
        self._app_store_block_automatic_downloads: Optional[bool] = None
        # Indicates whether or not to block the user from making in app purchases.
        self._app_store_block_in_app_purchases: Optional[bool] = None
        # Indicates whether or not to block the App Store app, not restricting installation through Host apps. Applies to supervised mode only (iOS 9.0 and later).
        self._app_store_block_u_i_app_installation: Optional[bool] = None
        # Indicates whether or not to block the user from using the App Store. Requires a supervised device for iOS 13 and later.
        self._app_store_blocked: Optional[bool] = None
        # Indicates whether or not to require a password when using the app store.
        self._app_store_require_password: Optional[bool] = None
        # Indicates whether or not to block the user from using News when the device is in supervised mode (iOS 9.0 and later).
        self._apple_news_blocked: Optional[bool] = None
        # Limits Apple personalized advertising when true. Available in iOS 14 and later.
        self._apple_personalized_ads_blocked: Optional[bool] = None
        # Indicates whether or not to allow Apple Watch pairing when the device is in supervised mode (iOS 9.0 and later).
        self._apple_watch_block_pairing: Optional[bool] = None
        # Indicates whether or not to force a paired Apple Watch to use Wrist Detection (iOS 8.2 and later).
        self._apple_watch_force_wrist_detection: Optional[bool] = None
        # Gets or sets the list of iOS apps allowed to autonomously enter Single App Mode. Supervised only. iOS 7.0 and later. This collection can contain a maximum of 500 elements.
        self._apps_single_app_mode_list: Optional[List[app_list_item.AppListItem]] = None
        # List of apps in the visibility list (either visible/launchable apps list or hidden/unlaunchable apps list, controlled by AppsVisibilityListType) (iOS 9.3 and later). This collection can contain a maximum of 10000 elements.
        self._apps_visibility_list: Optional[List[app_list_item.AppListItem]] = None
        # Possible values of the compliance app list.
        self._apps_visibility_list_type: Optional[app_list_type.AppListType] = None
        # Indicates whether or not to force user authentication before autofilling passwords and credit card information in Safari and other apps on supervised devices.
        self._auto_fill_force_authentication: Optional[bool] = None
        # Blocks users from unlocking their device with Apple Watch. Available for devices running iOS and iPadOS versions 14.5 and later.
        self._auto_unlock_blocked: Optional[bool] = None
        # Indicates whether or not the removal of system apps from the device is blocked on a supervised device (iOS 11.0 and later).
        self._block_system_app_removal: Optional[bool] = None
        # Indicates whether or not to allow modification of Bluetooth settings when the device is in supervised mode (iOS 10.0 and later).
        self._bluetooth_block_modification: Optional[bool] = None
        # Indicates whether or not to block the user from accessing the camera of the device. Requires a supervised device for iOS 13 and later.
        self._camera_blocked: Optional[bool] = None
        # Indicates whether or not to block data roaming.
        self._cellular_block_data_roaming: Optional[bool] = None
        # Indicates whether or not to block global background fetch while roaming.
        self._cellular_block_global_background_fetch_while_roaming: Optional[bool] = None
        # Indicates whether or not to allow changes to cellular app data usage settings when the device is in supervised mode.
        self._cellular_block_per_app_data_modification: Optional[bool] = None
        # Indicates whether or not to block Personal Hotspot.
        self._cellular_block_personal_hotspot: Optional[bool] = None
        # Indicates whether or not to block the user from modifying the personal hotspot setting (iOS 12.2 or later).
        self._cellular_block_personal_hotspot_modification: Optional[bool] = None
        # Indicates whether or not to allow users to change the settings of the cellular plan on a supervised device.
        self._cellular_block_plan_modification: Optional[bool] = None
        # Indicates whether or not to block voice roaming.
        self._cellular_block_voice_roaming: Optional[bool] = None
        # Indicates whether or not to block untrusted TLS certificates.
        self._certificates_block_untrusted_tls_certificates: Optional[bool] = None
        # Indicates whether or not to allow remote screen observation by Classroom app when the device is in supervised mode (iOS 9.3 and later).
        self._classroom_app_block_remote_screen_observation: Optional[bool] = None
        # Indicates whether or not to automatically give permission to the teacher of a managed course on the Classroom app to view a student's screen without prompting when the device is in supervised mode.
        self._classroom_app_force_unprompted_screen_observation: Optional[bool] = None
        # Indicates whether or not to automatically give permission to the teacher's requests, without prompting the student, when the device is in supervised mode.
        self._classroom_force_automatically_join_classes: Optional[bool] = None
        # Indicates whether a student enrolled in an unmanaged course via Classroom will request permission from the teacher when attempting to leave the course (iOS 11.3 and later).
        self._classroom_force_request_permission_to_leave_classes: Optional[bool] = None
        # Indicates whether or not to allow the teacher to lock apps or the device without prompting the student. Supervised only.
        self._classroom_force_unprompted_app_and_device_lock: Optional[bool] = None
        # Possible values of the compliance app list.
        self._compliant_app_list_type: Optional[app_list_type.AppListType] = None
        # List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
        self._compliant_apps_list: Optional[List[app_list_item.AppListItem]] = None
        # Indicates whether or not to block the user from installing configuration profiles and certificates interactively when the device is in supervised mode.
        self._configuration_profile_block_changes: Optional[bool] = None
        # Indicates whether or not managed apps can write contacts to unmanaged contacts accounts (iOS 12.0 and later).
        self._contacts_allow_managed_to_unmanaged_write: Optional[bool] = None
        # Indicates whether or not unmanaged apps can read from managed contacts accounts (iOS 12.0 or later).
        self._contacts_allow_unmanaged_to_managed_read: Optional[bool] = None
        # Indicates whether or not to block the continuous path keyboard when the device is supervised (iOS 13 or later).
        self._continuous_path_keyboard_blocked: Optional[bool] = None
        # Indicates whether or not the Date and Time 'Set Automatically' feature is enabled and cannot be turned off by the user (iOS 12.0 and later).
        self._date_and_time_force_set_automatically: Optional[bool] = None
        # Indicates whether or not to block definition lookup when the device is in supervised mode (iOS 8.1.3 and later ).
        self._definition_lookup_blocked: Optional[bool] = None
        # Indicates whether or not to allow the user to enables restrictions in the device settings when the device is in supervised mode.
        self._device_block_enable_restrictions: Optional[bool] = None
        # Indicates whether or not to allow the use of the 'Erase all content and settings' option on the device when the device is in supervised mode.
        self._device_block_erase_content_and_settings: Optional[bool] = None
        # Indicates whether or not to allow device name modification when the device is in supervised mode (iOS 9.0 and later).
        self._device_block_name_modification: Optional[bool] = None
        # Indicates whether or not to block diagnostic data submission.
        self._diagnostic_data_block_submission: Optional[bool] = None
        # Indicates whether or not to allow diagnostics submission settings modification when the device is in supervised mode (iOS 9.3.2 and later).
        self._diagnostic_data_block_submission_modification: Optional[bool] = None
        # Indicates whether or not to block the user from viewing managed documents in unmanaged apps.
        self._documents_block_managed_documents_in_unmanaged_apps: Optional[bool] = None
        # Indicates whether or not to block the user from viewing unmanaged documents in managed apps.
        self._documents_block_unmanaged_documents_in_managed_apps: Optional[bool] = None
        # An email address lacking a suffix that matches any of these strings will be considered out-of-domain.
        self._email_in_domain_suffixes: Optional[List[str]] = None
        # Indicates whether or not to block the user from trusting an enterprise app.
        self._enterprise_app_block_trust: Optional[bool] = None
        # [Deprecated] Configuring this setting and setting the value to 'true' has no effect on the device.
        self._enterprise_app_block_trust_modification: Optional[bool] = None
        # Indicates whether or not Enterprise book back up is blocked.
        self._enterprise_book_block_backup: Optional[bool] = None
        # Indicates whether or not Enterprise book notes and highlights sync is blocked.
        self._enterprise_book_block_metadata_sync: Optional[bool] = None
        # Indicates whether or not to allow the addition or removal of cellular plans on the eSIM of a supervised device.
        self._esim_block_modification: Optional[bool] = None
        # Indicates whether or not to block the user from using FaceTime. Requires a supervised device for iOS 13 and later.
        self._face_time_blocked: Optional[bool] = None
        # Indicates if devices can access files or other resources on a network server using the Server Message Block (SMB) protocol. Available for devices running iOS and iPadOS, versions 13.0 and later.
        self._files_network_drive_access_blocked: Optional[bool] = None
        # Indicates if sevices with access can connect to and open files on a USB drive. Available for devices running iOS and iPadOS, versions 13.0 and later.
        self._files_usb_drive_access_blocked: Optional[bool] = None
        # Indicates whether or not to block Find My Device when the device is supervised (iOS 13 or later).
        self._find_my_device_in_find_my_app_blocked: Optional[bool] = None
        # Indicates whether or not to block changes to Find My Friends when the device is in supervised mode.
        self._find_my_friends_blocked: Optional[bool] = None
        # Indicates whether or not to block Find My Friends when the device is supervised (iOS 13 or later).
        self._find_my_friends_in_find_my_app_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from using Game Center when the device is in supervised mode.
        self._game_center_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from having friends in Game Center. Requires a supervised device for iOS 13 and later.
        self._gaming_block_game_center_friends: Optional[bool] = None
        # Indicates whether or not to block the user from using multiplayer gaming. Requires a supervised device for iOS 13 and later.
        self._gaming_block_multiplayer: Optional[bool] = None
        # indicates whether or not to allow host pairing to control the devices an iOS device can pair with when the iOS device is in supervised mode.
        self._host_pairing_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from downloading media from the iBookstore that has been tagged as erotica.
        self._i_books_store_block_erotica: Optional[bool] = None
        # Indicates whether or not to block the user from using the iBooks Store when the device is in supervised mode.
        self._i_books_store_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from continuing work they started on iOS device to another iOS or macOS device.
        self._i_cloud_block_activity_continuation: Optional[bool] = None
        # Indicates whether or not to block iCloud backup. Requires a supervised device for iOS 13 and later.
        self._i_cloud_block_backup: Optional[bool] = None
        # Indicates whether or not to block iCloud document sync. Requires a supervised device for iOS 13 and later.
        self._i_cloud_block_document_sync: Optional[bool] = None
        # Indicates whether or not to block Managed Apps Cloud Sync.
        self._i_cloud_block_managed_apps_sync: Optional[bool] = None
        # Indicates whether or not to block iCloud Photo Library.
        self._i_cloud_block_photo_library: Optional[bool] = None
        # Indicates whether or not to block iCloud Photo Stream Sync.
        self._i_cloud_block_photo_stream_sync: Optional[bool] = None
        # Indicates whether or not to block Shared Photo Stream.
        self._i_cloud_block_shared_photo_stream: Optional[bool] = None
        # iCloud private relay is an iCloud+ service that prevents networks and servers from monitoring a person's activity across the internet. By blocking iCloud private relay, Apple will not encrypt the traffic leaving the device. Available for devices running iOS 15 and later.
        self._i_cloud_private_relay_blocked: Optional[bool] = None
        # Indicates whether or not to require backups to iCloud be encrypted.
        self._i_cloud_require_encrypted_backup: Optional[bool] = None
        # Indicates whether or not to block the user from accessing explicit content in iTunes and the App Store. Requires a supervised device for iOS 13 and later.
        self._i_tunes_block_explicit_content: Optional[bool] = None
        # Indicates whether or not to block Music service and revert Music app to classic mode when the device is in supervised mode (iOS 9.3 and later and macOS 10.12 and later).
        self._i_tunes_block_music_service: Optional[bool] = None
        # Indicates whether or not to block the user from using iTunes Radio when the device is in supervised mode (iOS 9.3 and later).
        self._i_tunes_block_radio: Optional[bool] = None
        # Indicates whether or not to block the iTunes app. Requires a supervised device for iOS 13 and later.
        self._i_tunes_blocked: Optional[bool] = None
        # Indicates whether or not to block keyboard auto-correction when the device is in supervised mode (iOS 8.1.3 and later).
        self._keyboard_block_auto_correct: Optional[bool] = None
        # Indicates whether or not to block the user from using dictation input when the device is in supervised mode.
        self._keyboard_block_dictation: Optional[bool] = None
        # Indicates whether or not to block predictive keyboards when device is in supervised mode (iOS 8.1.3 and later).
        self._keyboard_block_predictive: Optional[bool] = None
        # Indicates whether or not to block keyboard shortcuts when the device is in supervised mode (iOS 9.0 and later).
        self._keyboard_block_shortcuts: Optional[bool] = None
        # Indicates whether or not to block keyboard spell-checking when the device is in supervised mode (iOS 8.1.3 and later).
        self._keyboard_block_spell_check: Optional[bool] = None
        # Indicates whether or not iCloud keychain synchronization is blocked. Requires a supervised device for iOS 13 and later.
        self._keychain_block_cloud_sync: Optional[bool] = None
        # Indicates whether or not to allow assistive speak while in kiosk mode.
        self._kiosk_mode_allow_assistive_speak: Optional[bool] = None
        # Indicates whether or not to allow access to the Assistive Touch Settings while in kiosk mode.
        self._kiosk_mode_allow_assistive_touch_settings: Optional[bool] = None
        # Indicates whether or not to allow device auto lock while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockAutoLock instead.
        self._kiosk_mode_allow_auto_lock: Optional[bool] = None
        # Indicates whether or not to allow access to the Color Inversion Settings while in kiosk mode.
        self._kiosk_mode_allow_color_inversion_settings: Optional[bool] = None
        # Indicates whether or not to allow use of the ringer switch while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockRingerSwitch instead.
        self._kiosk_mode_allow_ringer_switch: Optional[bool] = None
        # Indicates whether or not to allow screen rotation while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockScreenRotation instead.
        self._kiosk_mode_allow_screen_rotation: Optional[bool] = None
        # Indicates whether or not to allow use of the sleep button while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockSleepButton instead.
        self._kiosk_mode_allow_sleep_button: Optional[bool] = None
        # Indicates whether or not to allow use of the touchscreen while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockTouchscreen instead.
        self._kiosk_mode_allow_touchscreen: Optional[bool] = None
        # Indicates whether or not to allow the user to toggle voice control in kiosk mode.
        self._kiosk_mode_allow_voice_control_modification: Optional[bool] = None
        # Indicates whether or not to allow access to the voice over settings while in kiosk mode.
        self._kiosk_mode_allow_voice_over_settings: Optional[bool] = None
        # Indicates whether or not to allow use of the volume buttons while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockVolumeButtons instead.
        self._kiosk_mode_allow_volume_buttons: Optional[bool] = None
        # Indicates whether or not to allow access to the zoom settings while in kiosk mode.
        self._kiosk_mode_allow_zoom_settings: Optional[bool] = None
        # URL in the app store to the app to use for kiosk mode. Use if KioskModeManagedAppId is not known.
        self._kiosk_mode_app_store_url: Optional[str] = None
        # App source options for iOS kiosk mode.
        self._kiosk_mode_app_type: Optional[ios_kiosk_mode_app_type.IosKioskModeAppType] = None
        # Indicates whether or not to block device auto lock while in kiosk mode.
        self._kiosk_mode_block_auto_lock: Optional[bool] = None
        # Indicates whether or not to block use of the ringer switch while in kiosk mode.
        self._kiosk_mode_block_ringer_switch: Optional[bool] = None
        # Indicates whether or not to block screen rotation while in kiosk mode.
        self._kiosk_mode_block_screen_rotation: Optional[bool] = None
        # Indicates whether or not to block use of the sleep button while in kiosk mode.
        self._kiosk_mode_block_sleep_button: Optional[bool] = None
        # Indicates whether or not to block use of the touchscreen while in kiosk mode.
        self._kiosk_mode_block_touchscreen: Optional[bool] = None
        # Indicates whether or not to block the volume buttons while in Kiosk Mode.
        self._kiosk_mode_block_volume_buttons: Optional[bool] = None
        # ID for built-in apps to use for kiosk mode. Used when KioskModeManagedAppId and KioskModeAppStoreUrl are not set.
        self._kiosk_mode_built_in_app_id: Optional[str] = None
        # Indicates whether or not to enable voice control in kiosk mode.
        self._kiosk_mode_enable_voice_control: Optional[bool] = None
        # Managed app id of the app to use for kiosk mode. If KioskModeManagedAppId is specified then KioskModeAppStoreUrl will be ignored.
        self._kiosk_mode_managed_app_id: Optional[str] = None
        # Indicates whether or not to require assistive touch while in kiosk mode.
        self._kiosk_mode_require_assistive_touch: Optional[bool] = None
        # Indicates whether or not to require color inversion while in kiosk mode.
        self._kiosk_mode_require_color_inversion: Optional[bool] = None
        # Indicates whether or not to require mono audio while in kiosk mode.
        self._kiosk_mode_require_mono_audio: Optional[bool] = None
        # Indicates whether or not to require voice over while in kiosk mode.
        self._kiosk_mode_require_voice_over: Optional[bool] = None
        # Indicates whether or not to require zoom while in kiosk mode.
        self._kiosk_mode_require_zoom: Optional[bool] = None
        # Indicates whether or not to block the user from using control center on the lock screen.
        self._lock_screen_block_control_center: Optional[bool] = None
        # Indicates whether or not to block the user from using the notification view on the lock screen.
        self._lock_screen_block_notification_view: Optional[bool] = None
        # Indicates whether or not to block the user from using passbook when the device is locked.
        self._lock_screen_block_passbook: Optional[bool] = None
        # Indicates whether or not to block the user from using the Today View on the lock screen.
        self._lock_screen_block_today_view: Optional[bool] = None
        # Open-in management controls how people share data between unmanaged and managed apps. Setting this to true enforces copy/paste restrictions based on how you configured Block viewing corporate documents in unmanaged apps  and  Block viewing non-corporate documents in corporate apps.
        self._managed_pasteboard_required: Optional[bool] = None
        # Apps rating as in media content
        self._media_content_rating_apps: Optional[rating_apps_type.RatingAppsType] = None
        # Media content rating settings for Australia
        self._media_content_rating_australia: Optional[media_content_rating_australia.MediaContentRatingAustralia] = None
        # Media content rating settings for Canada
        self._media_content_rating_canada: Optional[media_content_rating_canada.MediaContentRatingCanada] = None
        # Media content rating settings for France
        self._media_content_rating_france: Optional[media_content_rating_france.MediaContentRatingFrance] = None
        # Media content rating settings for Germany
        self._media_content_rating_germany: Optional[media_content_rating_germany.MediaContentRatingGermany] = None
        # Media content rating settings for Ireland
        self._media_content_rating_ireland: Optional[media_content_rating_ireland.MediaContentRatingIreland] = None
        # Media content rating settings for Japan
        self._media_content_rating_japan: Optional[media_content_rating_japan.MediaContentRatingJapan] = None
        # Media content rating settings for New Zealand
        self._media_content_rating_new_zealand: Optional[media_content_rating_new_zealand.MediaContentRatingNewZealand] = None
        # Media content rating settings for United Kingdom
        self._media_content_rating_united_kingdom: Optional[media_content_rating_united_kingdom.MediaContentRatingUnitedKingdom] = None
        # Media content rating settings for United States
        self._media_content_rating_united_states: Optional[media_content_rating_united_states.MediaContentRatingUnitedStates] = None
        # Indicates whether or not to block the user from using the Messages app on the supervised device.
        self._messages_blocked: Optional[bool] = None
        # List of managed apps and the network rules that applies to them. This collection can contain a maximum of 1000 elements.
        self._network_usage_rules: Optional[List[ios_network_usage_rule.IosNetworkUsageRule]] = None
        # Disable NFC to prevent devices from pairing with other NFC-enabled devices. Available for iOS/iPadOS devices running 14.2 and later.
        self._nfc_blocked: Optional[bool] = None
        # Indicates whether or not to allow notifications settings modification (iOS 9.3 and later).
        self._notifications_block_settings_modification: Optional[bool] = None
        # Disables connections to Siri servers so that users can’t use Siri to dictate text. Available for devices running iOS and iPadOS versions 14.5 and later.
        self._on_device_only_dictation_forced: Optional[bool] = None
        # When set to TRUE, the setting disables connections to Siri servers so that users can’t use Siri to translate text. When set to FALSE, the setting allows connections to to Siri servers to users can use Siri to translate text. Available for devices running iOS and iPadOS versions 15.0 and later.
        self._on_device_only_translation_forced: Optional[bool] = None
        # Block modification of registered Touch ID fingerprints when in supervised mode.
        self._passcode_block_fingerprint_modification: Optional[bool] = None
        # Indicates whether or not to block fingerprint unlock.
        self._passcode_block_fingerprint_unlock: Optional[bool] = None
        # Indicates whether or not to allow passcode modification on the supervised device (iOS 9.0 and later).
        self._passcode_block_modification: Optional[bool] = None
        # Indicates whether or not to block simple passcodes.
        self._passcode_block_simple: Optional[bool] = None
        # Number of days before the passcode expires. Valid values 1 to 65535
        self._passcode_expiration_days: Optional[int] = None
        # Number of character sets a passcode must contain. Valid values 0 to 4
        self._passcode_minimum_character_set_count: Optional[int] = None
        # Minimum length of passcode. Valid values 4 to 14
        self._passcode_minimum_length: Optional[int] = None
        # Minutes of inactivity before a passcode is required.
        self._passcode_minutes_of_inactivity_before_lock: Optional[int] = None
        # Minutes of inactivity before the screen times out.
        self._passcode_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
        # Number of previous passcodes to block. Valid values 1 to 24
        self._passcode_previous_passcode_block_count: Optional[int] = None
        # Indicates whether or not to require a passcode.
        self._passcode_required: Optional[bool] = None
        # Possible values of required passwords.
        self._passcode_required_type: Optional[required_password_type.RequiredPasswordType] = None
        # Number of sign in failures allowed before wiping the device. Valid values 2 to 11
        self._passcode_sign_in_failure_count_before_wipe: Optional[int] = None
        # Indicates whether or not to block sharing passwords with the AirDrop passwords feature iOS 12.0 and later).
        self._password_block_air_drop_sharing: Optional[bool] = None
        # Indicates if the AutoFill passwords feature is allowed (iOS 12.0 and later).
        self._password_block_auto_fill: Optional[bool] = None
        # Indicates whether or not to block requesting passwords from nearby devices (iOS 12.0 and later).
        self._password_block_proximity_requests: Optional[bool] = None
        # Indicates whether or not over-the-air PKI updates are blocked. Setting this restriction to false does not disable CRL and OCSP checks (iOS 7.0 and later).
        self._pki_block_o_t_a_updates: Optional[bool] = None
        # Indicates whether or not to block the user from using podcasts on the supervised device (iOS 8.0 and later).
        self._podcasts_blocked: Optional[bool] = None
        # Indicates if ad tracking is limited.(iOS 7.0 and later).
        self._privacy_force_limit_ad_tracking: Optional[bool] = None
        # Indicates whether or not to enable the prompt to setup nearby devices with a supervised device.
        self._proximity_block_setup_to_new_device: Optional[bool] = None
        # Indicates whether or not to block the user from using Auto fill in Safari. Requires a supervised device for iOS 13 and later.
        self._safari_block_autofill: Optional[bool] = None
        # Indicates whether or not to block JavaScript in Safari.
        self._safari_block_java_script: Optional[bool] = None
        # Indicates whether or not to block popups in Safari.
        self._safari_block_popups: Optional[bool] = None
        # Indicates whether or not to block the user from using Safari. Requires a supervised device for iOS 13 and later.
        self._safari_blocked: Optional[bool] = None
        # Web Browser Cookie Settings.
        self._safari_cookie_settings: Optional[web_browser_cookie_settings.WebBrowserCookieSettings] = None
        # URLs matching the patterns listed here will be considered managed.
        self._safari_managed_domains: Optional[List[str]] = None
        # Users can save passwords in Safari only from URLs matching the patterns listed here. Applies to devices in supervised mode (iOS 9.3 and later).
        self._safari_password_auto_fill_domains: Optional[List[str]] = None
        # Indicates whether or not to require fraud warning in Safari.
        self._safari_require_fraud_warning: Optional[bool] = None
        # Indicates whether or not to block the user from taking Screenshots.
        self._screen_capture_blocked: Optional[bool] = None
        # Indicates whether or not to block temporary sessions on Shared iPads (iOS 13.4 or later).
        self._shared_device_block_temporary_sessions: Optional[bool] = None
        # Indicates whether or not to block Siri from querying user-generated content when used on a supervised device.
        self._siri_block_user_generated_content: Optional[bool] = None
        # Indicates whether or not to block the user from using Siri.
        self._siri_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from using Siri when locked.
        self._siri_blocked_when_locked: Optional[bool] = None
        # Indicates whether or not to prevent Siri from dictating, or speaking profane language on supervised device.
        self._siri_require_profanity_filter: Optional[bool] = None
        # Sets how many days a software update will be delyed for a supervised device. Valid values 0 to 90
        self._software_updates_enforced_delay_in_days: Optional[int] = None
        # Indicates whether or not to delay user visibility of software updates when the device is in supervised mode.
        self._software_updates_force_delayed: Optional[bool] = None
        # Indicates whether or not to block Spotlight search from returning internet results on supervised device.
        self._spotlight_block_internet_results: Optional[bool] = None
        # Allow users to boot devices into recovery mode with unpaired devices. Available for devices running iOS and iPadOS versions 14.5 and later.
        self._unpaired_external_boot_to_recovery_allowed: Optional[bool] = None
        # Indicates if connecting to USB accessories while the device is locked is allowed (iOS 11.4.1 and later).
        self._usb_restricted_mode_blocked: Optional[bool] = None
        # Indicates whether or not to block voice dialing.
        self._voice_dialing_blocked: Optional[bool] = None
        # Indicates whether or not the creation of VPN configurations is blocked (iOS 11.0 and later).
        self._vpn_block_creation: Optional[bool] = None
        # Indicates whether or not to allow wallpaper modification on supervised device (iOS 9.0 and later) .
        self._wallpaper_block_modification: Optional[bool] = None
        # Indicates whether or not to force the device to use only Wi-Fi networks from configuration profiles when the device is in supervised mode. Available for devices running iOS and iPadOS versions 14.4 and earlier. Devices running 14.5+ should use the setting, 'WiFiConnectToAllowedNetworksOnlyForced.
        self._wi_fi_connect_only_to_configured_networks: Optional[bool] = None
        # Require devices to use Wi-Fi networks set up via configuration profiles. Available for devices running iOS and iPadOS versions 14.5 and later.
        self._wi_fi_connect_to_allowed_networks_only_forced: Optional[bool] = None
        # Indicates whether or not Wi-Fi remains on, even when device is in airplane mode. Available for devices running iOS and iPadOS, versions 13.0 and later.
        self._wifi_power_on_forced: Optional[bool] = None
    
    @property
    def account_block_modification(self,) -> Optional[bool]:
        """
        Gets the accountBlockModification property value. Indicates whether or not to allow account modification when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._account_block_modification
    
    @account_block_modification.setter
    def account_block_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the accountBlockModification property value. Indicates whether or not to allow account modification when the device is in supervised mode.
        Args:
            value: Value to set for the account_block_modification property.
        """
        self._account_block_modification = value
    
    @property
    def activation_lock_allow_when_supervised(self,) -> Optional[bool]:
        """
        Gets the activationLockAllowWhenSupervised property value. Indicates whether or not to allow activation lock when the device is in the supervised mode.
        Returns: Optional[bool]
        """
        return self._activation_lock_allow_when_supervised
    
    @activation_lock_allow_when_supervised.setter
    def activation_lock_allow_when_supervised(self,value: Optional[bool] = None) -> None:
        """
        Sets the activationLockAllowWhenSupervised property value. Indicates whether or not to allow activation lock when the device is in the supervised mode.
        Args:
            value: Value to set for the activation_lock_allow_when_supervised property.
        """
        self._activation_lock_allow_when_supervised = value
    
    @property
    def air_drop_blocked(self,) -> Optional[bool]:
        """
        Gets the airDropBlocked property value. Indicates whether or not to allow AirDrop when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._air_drop_blocked
    
    @air_drop_blocked.setter
    def air_drop_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the airDropBlocked property value. Indicates whether or not to allow AirDrop when the device is in supervised mode.
        Args:
            value: Value to set for the air_drop_blocked property.
        """
        self._air_drop_blocked = value
    
    @property
    def air_drop_force_unmanaged_drop_target(self,) -> Optional[bool]:
        """
        Gets the airDropForceUnmanagedDropTarget property value. Indicates whether or not to cause AirDrop to be considered an unmanaged drop target (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._air_drop_force_unmanaged_drop_target
    
    @air_drop_force_unmanaged_drop_target.setter
    def air_drop_force_unmanaged_drop_target(self,value: Optional[bool] = None) -> None:
        """
        Sets the airDropForceUnmanagedDropTarget property value. Indicates whether or not to cause AirDrop to be considered an unmanaged drop target (iOS 9.0 and later).
        Args:
            value: Value to set for the air_drop_force_unmanaged_drop_target property.
        """
        self._air_drop_force_unmanaged_drop_target = value
    
    @property
    def air_play_force_pairing_password_for_outgoing_requests(self,) -> Optional[bool]:
        """
        Gets the airPlayForcePairingPasswordForOutgoingRequests property value. Indicates whether or not to enforce all devices receiving AirPlay requests from this device to use a pairing password.
        Returns: Optional[bool]
        """
        return self._air_play_force_pairing_password_for_outgoing_requests
    
    @air_play_force_pairing_password_for_outgoing_requests.setter
    def air_play_force_pairing_password_for_outgoing_requests(self,value: Optional[bool] = None) -> None:
        """
        Sets the airPlayForcePairingPasswordForOutgoingRequests property value. Indicates whether or not to enforce all devices receiving AirPlay requests from this device to use a pairing password.
        Args:
            value: Value to set for the air_play_force_pairing_password_for_outgoing_requests property.
        """
        self._air_play_force_pairing_password_for_outgoing_requests = value
    
    @property
    def air_print_block_credentials_storage(self,) -> Optional[bool]:
        """
        Gets the airPrintBlockCredentialsStorage property value. Indicates whether or not keychain storage of username and password for Airprint is blocked (iOS 11.0 and later).
        Returns: Optional[bool]
        """
        return self._air_print_block_credentials_storage
    
    @air_print_block_credentials_storage.setter
    def air_print_block_credentials_storage(self,value: Optional[bool] = None) -> None:
        """
        Sets the airPrintBlockCredentialsStorage property value. Indicates whether or not keychain storage of username and password for Airprint is blocked (iOS 11.0 and later).
        Args:
            value: Value to set for the air_print_block_credentials_storage property.
        """
        self._air_print_block_credentials_storage = value
    
    @property
    def air_print_blocked(self,) -> Optional[bool]:
        """
        Gets the airPrintBlocked property value. Indicates whether or not AirPrint is blocked (iOS 11.0 and later).
        Returns: Optional[bool]
        """
        return self._air_print_blocked
    
    @air_print_blocked.setter
    def air_print_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the airPrintBlocked property value. Indicates whether or not AirPrint is blocked (iOS 11.0 and later).
        Args:
            value: Value to set for the air_print_blocked property.
        """
        self._air_print_blocked = value
    
    @property
    def air_print_blocki_beacon_discovery(self,) -> Optional[bool]:
        """
        Gets the airPrintBlockiBeaconDiscovery property value. Indicates whether or not iBeacon discovery of AirPrint printers is blocked. This prevents spurious AirPrint Bluetooth beacons from phishing for network traffic (iOS 11.0 and later).
        Returns: Optional[bool]
        """
        return self._air_print_blocki_beacon_discovery
    
    @air_print_blocki_beacon_discovery.setter
    def air_print_blocki_beacon_discovery(self,value: Optional[bool] = None) -> None:
        """
        Sets the airPrintBlockiBeaconDiscovery property value. Indicates whether or not iBeacon discovery of AirPrint printers is blocked. This prevents spurious AirPrint Bluetooth beacons from phishing for network traffic (iOS 11.0 and later).
        Args:
            value: Value to set for the air_print_blocki_beacon_discovery property.
        """
        self._air_print_blocki_beacon_discovery = value
    
    @property
    def air_print_force_trusted_t_l_s(self,) -> Optional[bool]:
        """
        Gets the airPrintForceTrustedTLS property value. Indicates if trusted certificates are required for TLS printing communication (iOS 11.0 and later).
        Returns: Optional[bool]
        """
        return self._air_print_force_trusted_t_l_s
    
    @air_print_force_trusted_t_l_s.setter
    def air_print_force_trusted_t_l_s(self,value: Optional[bool] = None) -> None:
        """
        Sets the airPrintForceTrustedTLS property value. Indicates if trusted certificates are required for TLS printing communication (iOS 11.0 and later).
        Args:
            value: Value to set for the air_print_force_trusted_t_l_s property.
        """
        self._air_print_force_trusted_t_l_s = value
    
    @property
    def app_clips_blocked(self,) -> Optional[bool]:
        """
        Gets the appClipsBlocked property value. Prevents a user from adding any App Clips and removes any existing App Clips on the device.
        Returns: Optional[bool]
        """
        return self._app_clips_blocked
    
    @app_clips_blocked.setter
    def app_clips_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the appClipsBlocked property value. Prevents a user from adding any App Clips and removes any existing App Clips on the device.
        Args:
            value: Value to set for the app_clips_blocked property.
        """
        self._app_clips_blocked = value
    
    @property
    def app_removal_blocked(self,) -> Optional[bool]:
        """
        Gets the appRemovalBlocked property value. Indicates if the removal of apps is allowed.
        Returns: Optional[bool]
        """
        return self._app_removal_blocked
    
    @app_removal_blocked.setter
    def app_removal_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the appRemovalBlocked property value. Indicates if the removal of apps is allowed.
        Args:
            value: Value to set for the app_removal_blocked property.
        """
        self._app_removal_blocked = value
    
    @property
    def app_store_block_automatic_downloads(self,) -> Optional[bool]:
        """
        Gets the appStoreBlockAutomaticDownloads property value. Indicates whether or not to block the automatic downloading of apps purchased on other devices when the device is in supervised mode (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._app_store_block_automatic_downloads
    
    @app_store_block_automatic_downloads.setter
    def app_store_block_automatic_downloads(self,value: Optional[bool] = None) -> None:
        """
        Sets the appStoreBlockAutomaticDownloads property value. Indicates whether or not to block the automatic downloading of apps purchased on other devices when the device is in supervised mode (iOS 9.0 and later).
        Args:
            value: Value to set for the app_store_block_automatic_downloads property.
        """
        self._app_store_block_automatic_downloads = value
    
    @property
    def app_store_block_in_app_purchases(self,) -> Optional[bool]:
        """
        Gets the appStoreBlockInAppPurchases property value. Indicates whether or not to block the user from making in app purchases.
        Returns: Optional[bool]
        """
        return self._app_store_block_in_app_purchases
    
    @app_store_block_in_app_purchases.setter
    def app_store_block_in_app_purchases(self,value: Optional[bool] = None) -> None:
        """
        Sets the appStoreBlockInAppPurchases property value. Indicates whether or not to block the user from making in app purchases.
        Args:
            value: Value to set for the app_store_block_in_app_purchases property.
        """
        self._app_store_block_in_app_purchases = value
    
    @property
    def app_store_block_u_i_app_installation(self,) -> Optional[bool]:
        """
        Gets the appStoreBlockUIAppInstallation property value. Indicates whether or not to block the App Store app, not restricting installation through Host apps. Applies to supervised mode only (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._app_store_block_u_i_app_installation
    
    @app_store_block_u_i_app_installation.setter
    def app_store_block_u_i_app_installation(self,value: Optional[bool] = None) -> None:
        """
        Sets the appStoreBlockUIAppInstallation property value. Indicates whether or not to block the App Store app, not restricting installation through Host apps. Applies to supervised mode only (iOS 9.0 and later).
        Args:
            value: Value to set for the app_store_block_u_i_app_installation property.
        """
        self._app_store_block_u_i_app_installation = value
    
    @property
    def app_store_blocked(self,) -> Optional[bool]:
        """
        Gets the appStoreBlocked property value. Indicates whether or not to block the user from using the App Store. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._app_store_blocked
    
    @app_store_blocked.setter
    def app_store_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the appStoreBlocked property value. Indicates whether or not to block the user from using the App Store. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the app_store_blocked property.
        """
        self._app_store_blocked = value
    
    @property
    def app_store_require_password(self,) -> Optional[bool]:
        """
        Gets the appStoreRequirePassword property value. Indicates whether or not to require a password when using the app store.
        Returns: Optional[bool]
        """
        return self._app_store_require_password
    
    @app_store_require_password.setter
    def app_store_require_password(self,value: Optional[bool] = None) -> None:
        """
        Sets the appStoreRequirePassword property value. Indicates whether or not to require a password when using the app store.
        Args:
            value: Value to set for the app_store_require_password property.
        """
        self._app_store_require_password = value
    
    @property
    def apple_news_blocked(self,) -> Optional[bool]:
        """
        Gets the appleNewsBlocked property value. Indicates whether or not to block the user from using News when the device is in supervised mode (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._apple_news_blocked
    
    @apple_news_blocked.setter
    def apple_news_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the appleNewsBlocked property value. Indicates whether or not to block the user from using News when the device is in supervised mode (iOS 9.0 and later).
        Args:
            value: Value to set for the apple_news_blocked property.
        """
        self._apple_news_blocked = value
    
    @property
    def apple_personalized_ads_blocked(self,) -> Optional[bool]:
        """
        Gets the applePersonalizedAdsBlocked property value. Limits Apple personalized advertising when true. Available in iOS 14 and later.
        Returns: Optional[bool]
        """
        return self._apple_personalized_ads_blocked
    
    @apple_personalized_ads_blocked.setter
    def apple_personalized_ads_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the applePersonalizedAdsBlocked property value. Limits Apple personalized advertising when true. Available in iOS 14 and later.
        Args:
            value: Value to set for the apple_personalized_ads_blocked property.
        """
        self._apple_personalized_ads_blocked = value
    
    @property
    def apple_watch_block_pairing(self,) -> Optional[bool]:
        """
        Gets the appleWatchBlockPairing property value. Indicates whether or not to allow Apple Watch pairing when the device is in supervised mode (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._apple_watch_block_pairing
    
    @apple_watch_block_pairing.setter
    def apple_watch_block_pairing(self,value: Optional[bool] = None) -> None:
        """
        Sets the appleWatchBlockPairing property value. Indicates whether or not to allow Apple Watch pairing when the device is in supervised mode (iOS 9.0 and later).
        Args:
            value: Value to set for the apple_watch_block_pairing property.
        """
        self._apple_watch_block_pairing = value
    
    @property
    def apple_watch_force_wrist_detection(self,) -> Optional[bool]:
        """
        Gets the appleWatchForceWristDetection property value. Indicates whether or not to force a paired Apple Watch to use Wrist Detection (iOS 8.2 and later).
        Returns: Optional[bool]
        """
        return self._apple_watch_force_wrist_detection
    
    @apple_watch_force_wrist_detection.setter
    def apple_watch_force_wrist_detection(self,value: Optional[bool] = None) -> None:
        """
        Sets the appleWatchForceWristDetection property value. Indicates whether or not to force a paired Apple Watch to use Wrist Detection (iOS 8.2 and later).
        Args:
            value: Value to set for the apple_watch_force_wrist_detection property.
        """
        self._apple_watch_force_wrist_detection = value
    
    @property
    def apps_single_app_mode_list(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the appsSingleAppModeList property value. Gets or sets the list of iOS apps allowed to autonomously enter Single App Mode. Supervised only. iOS 7.0 and later. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._apps_single_app_mode_list
    
    @apps_single_app_mode_list.setter
    def apps_single_app_mode_list(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the appsSingleAppModeList property value. Gets or sets the list of iOS apps allowed to autonomously enter Single App Mode. Supervised only. iOS 7.0 and later. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the apps_single_app_mode_list property.
        """
        self._apps_single_app_mode_list = value
    
    @property
    def apps_visibility_list(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the appsVisibilityList property value. List of apps in the visibility list (either visible/launchable apps list or hidden/unlaunchable apps list, controlled by AppsVisibilityListType) (iOS 9.3 and later). This collection can contain a maximum of 10000 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._apps_visibility_list
    
    @apps_visibility_list.setter
    def apps_visibility_list(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the appsVisibilityList property value. List of apps in the visibility list (either visible/launchable apps list or hidden/unlaunchable apps list, controlled by AppsVisibilityListType) (iOS 9.3 and later). This collection can contain a maximum of 10000 elements.
        Args:
            value: Value to set for the apps_visibility_list property.
        """
        self._apps_visibility_list = value
    
    @property
    def apps_visibility_list_type(self,) -> Optional[app_list_type.AppListType]:
        """
        Gets the appsVisibilityListType property value. Possible values of the compliance app list.
        Returns: Optional[app_list_type.AppListType]
        """
        return self._apps_visibility_list_type
    
    @apps_visibility_list_type.setter
    def apps_visibility_list_type(self,value: Optional[app_list_type.AppListType] = None) -> None:
        """
        Sets the appsVisibilityListType property value. Possible values of the compliance app list.
        Args:
            value: Value to set for the apps_visibility_list_type property.
        """
        self._apps_visibility_list_type = value
    
    @property
    def auto_fill_force_authentication(self,) -> Optional[bool]:
        """
        Gets the autoFillForceAuthentication property value. Indicates whether or not to force user authentication before autofilling passwords and credit card information in Safari and other apps on supervised devices.
        Returns: Optional[bool]
        """
        return self._auto_fill_force_authentication
    
    @auto_fill_force_authentication.setter
    def auto_fill_force_authentication(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoFillForceAuthentication property value. Indicates whether or not to force user authentication before autofilling passwords and credit card information in Safari and other apps on supervised devices.
        Args:
            value: Value to set for the auto_fill_force_authentication property.
        """
        self._auto_fill_force_authentication = value
    
    @property
    def auto_unlock_blocked(self,) -> Optional[bool]:
        """
        Gets the autoUnlockBlocked property value. Blocks users from unlocking their device with Apple Watch. Available for devices running iOS and iPadOS versions 14.5 and later.
        Returns: Optional[bool]
        """
        return self._auto_unlock_blocked
    
    @auto_unlock_blocked.setter
    def auto_unlock_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoUnlockBlocked property value. Blocks users from unlocking their device with Apple Watch. Available for devices running iOS and iPadOS versions 14.5 and later.
        Args:
            value: Value to set for the auto_unlock_blocked property.
        """
        self._auto_unlock_blocked = value
    
    @property
    def block_system_app_removal(self,) -> Optional[bool]:
        """
        Gets the blockSystemAppRemoval property value. Indicates whether or not the removal of system apps from the device is blocked on a supervised device (iOS 11.0 and later).
        Returns: Optional[bool]
        """
        return self._block_system_app_removal
    
    @block_system_app_removal.setter
    def block_system_app_removal(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockSystemAppRemoval property value. Indicates whether or not the removal of system apps from the device is blocked on a supervised device (iOS 11.0 and later).
        Args:
            value: Value to set for the block_system_app_removal property.
        """
        self._block_system_app_removal = value
    
    @property
    def bluetooth_block_modification(self,) -> Optional[bool]:
        """
        Gets the bluetoothBlockModification property value. Indicates whether or not to allow modification of Bluetooth settings when the device is in supervised mode (iOS 10.0 and later).
        Returns: Optional[bool]
        """
        return self._bluetooth_block_modification
    
    @bluetooth_block_modification.setter
    def bluetooth_block_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the bluetoothBlockModification property value. Indicates whether or not to allow modification of Bluetooth settings when the device is in supervised mode (iOS 10.0 and later).
        Args:
            value: Value to set for the bluetooth_block_modification property.
        """
        self._bluetooth_block_modification = value
    
    @property
    def camera_blocked(self,) -> Optional[bool]:
        """
        Gets the cameraBlocked property value. Indicates whether or not to block the user from accessing the camera of the device. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._camera_blocked
    
    @camera_blocked.setter
    def camera_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the cameraBlocked property value. Indicates whether or not to block the user from accessing the camera of the device. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the camera_blocked property.
        """
        self._camera_blocked = value
    
    @property
    def cellular_block_data_roaming(self,) -> Optional[bool]:
        """
        Gets the cellularBlockDataRoaming property value. Indicates whether or not to block data roaming.
        Returns: Optional[bool]
        """
        return self._cellular_block_data_roaming
    
    @cellular_block_data_roaming.setter
    def cellular_block_data_roaming(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockDataRoaming property value. Indicates whether or not to block data roaming.
        Args:
            value: Value to set for the cellular_block_data_roaming property.
        """
        self._cellular_block_data_roaming = value
    
    @property
    def cellular_block_global_background_fetch_while_roaming(self,) -> Optional[bool]:
        """
        Gets the cellularBlockGlobalBackgroundFetchWhileRoaming property value. Indicates whether or not to block global background fetch while roaming.
        Returns: Optional[bool]
        """
        return self._cellular_block_global_background_fetch_while_roaming
    
    @cellular_block_global_background_fetch_while_roaming.setter
    def cellular_block_global_background_fetch_while_roaming(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockGlobalBackgroundFetchWhileRoaming property value. Indicates whether or not to block global background fetch while roaming.
        Args:
            value: Value to set for the cellular_block_global_background_fetch_while_roaming property.
        """
        self._cellular_block_global_background_fetch_while_roaming = value
    
    @property
    def cellular_block_per_app_data_modification(self,) -> Optional[bool]:
        """
        Gets the cellularBlockPerAppDataModification property value. Indicates whether or not to allow changes to cellular app data usage settings when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._cellular_block_per_app_data_modification
    
    @cellular_block_per_app_data_modification.setter
    def cellular_block_per_app_data_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockPerAppDataModification property value. Indicates whether or not to allow changes to cellular app data usage settings when the device is in supervised mode.
        Args:
            value: Value to set for the cellular_block_per_app_data_modification property.
        """
        self._cellular_block_per_app_data_modification = value
    
    @property
    def cellular_block_personal_hotspot(self,) -> Optional[bool]:
        """
        Gets the cellularBlockPersonalHotspot property value. Indicates whether or not to block Personal Hotspot.
        Returns: Optional[bool]
        """
        return self._cellular_block_personal_hotspot
    
    @cellular_block_personal_hotspot.setter
    def cellular_block_personal_hotspot(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockPersonalHotspot property value. Indicates whether or not to block Personal Hotspot.
        Args:
            value: Value to set for the cellular_block_personal_hotspot property.
        """
        self._cellular_block_personal_hotspot = value
    
    @property
    def cellular_block_personal_hotspot_modification(self,) -> Optional[bool]:
        """
        Gets the cellularBlockPersonalHotspotModification property value. Indicates whether or not to block the user from modifying the personal hotspot setting (iOS 12.2 or later).
        Returns: Optional[bool]
        """
        return self._cellular_block_personal_hotspot_modification
    
    @cellular_block_personal_hotspot_modification.setter
    def cellular_block_personal_hotspot_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockPersonalHotspotModification property value. Indicates whether or not to block the user from modifying the personal hotspot setting (iOS 12.2 or later).
        Args:
            value: Value to set for the cellular_block_personal_hotspot_modification property.
        """
        self._cellular_block_personal_hotspot_modification = value
    
    @property
    def cellular_block_plan_modification(self,) -> Optional[bool]:
        """
        Gets the cellularBlockPlanModification property value. Indicates whether or not to allow users to change the settings of the cellular plan on a supervised device.
        Returns: Optional[bool]
        """
        return self._cellular_block_plan_modification
    
    @cellular_block_plan_modification.setter
    def cellular_block_plan_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockPlanModification property value. Indicates whether or not to allow users to change the settings of the cellular plan on a supervised device.
        Args:
            value: Value to set for the cellular_block_plan_modification property.
        """
        self._cellular_block_plan_modification = value
    
    @property
    def cellular_block_voice_roaming(self,) -> Optional[bool]:
        """
        Gets the cellularBlockVoiceRoaming property value. Indicates whether or not to block voice roaming.
        Returns: Optional[bool]
        """
        return self._cellular_block_voice_roaming
    
    @cellular_block_voice_roaming.setter
    def cellular_block_voice_roaming(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockVoiceRoaming property value. Indicates whether or not to block voice roaming.
        Args:
            value: Value to set for the cellular_block_voice_roaming property.
        """
        self._cellular_block_voice_roaming = value
    
    @property
    def certificates_block_untrusted_tls_certificates(self,) -> Optional[bool]:
        """
        Gets the certificatesBlockUntrustedTlsCertificates property value. Indicates whether or not to block untrusted TLS certificates.
        Returns: Optional[bool]
        """
        return self._certificates_block_untrusted_tls_certificates
    
    @certificates_block_untrusted_tls_certificates.setter
    def certificates_block_untrusted_tls_certificates(self,value: Optional[bool] = None) -> None:
        """
        Sets the certificatesBlockUntrustedTlsCertificates property value. Indicates whether or not to block untrusted TLS certificates.
        Args:
            value: Value to set for the certificates_block_untrusted_tls_certificates property.
        """
        self._certificates_block_untrusted_tls_certificates = value
    
    @property
    def classroom_app_block_remote_screen_observation(self,) -> Optional[bool]:
        """
        Gets the classroomAppBlockRemoteScreenObservation property value. Indicates whether or not to allow remote screen observation by Classroom app when the device is in supervised mode (iOS 9.3 and later).
        Returns: Optional[bool]
        """
        return self._classroom_app_block_remote_screen_observation
    
    @classroom_app_block_remote_screen_observation.setter
    def classroom_app_block_remote_screen_observation(self,value: Optional[bool] = None) -> None:
        """
        Sets the classroomAppBlockRemoteScreenObservation property value. Indicates whether or not to allow remote screen observation by Classroom app when the device is in supervised mode (iOS 9.3 and later).
        Args:
            value: Value to set for the classroom_app_block_remote_screen_observation property.
        """
        self._classroom_app_block_remote_screen_observation = value
    
    @property
    def classroom_app_force_unprompted_screen_observation(self,) -> Optional[bool]:
        """
        Gets the classroomAppForceUnpromptedScreenObservation property value. Indicates whether or not to automatically give permission to the teacher of a managed course on the Classroom app to view a student's screen without prompting when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._classroom_app_force_unprompted_screen_observation
    
    @classroom_app_force_unprompted_screen_observation.setter
    def classroom_app_force_unprompted_screen_observation(self,value: Optional[bool] = None) -> None:
        """
        Sets the classroomAppForceUnpromptedScreenObservation property value. Indicates whether or not to automatically give permission to the teacher of a managed course on the Classroom app to view a student's screen without prompting when the device is in supervised mode.
        Args:
            value: Value to set for the classroom_app_force_unprompted_screen_observation property.
        """
        self._classroom_app_force_unprompted_screen_observation = value
    
    @property
    def classroom_force_automatically_join_classes(self,) -> Optional[bool]:
        """
        Gets the classroomForceAutomaticallyJoinClasses property value. Indicates whether or not to automatically give permission to the teacher's requests, without prompting the student, when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._classroom_force_automatically_join_classes
    
    @classroom_force_automatically_join_classes.setter
    def classroom_force_automatically_join_classes(self,value: Optional[bool] = None) -> None:
        """
        Sets the classroomForceAutomaticallyJoinClasses property value. Indicates whether or not to automatically give permission to the teacher's requests, without prompting the student, when the device is in supervised mode.
        Args:
            value: Value to set for the classroom_force_automatically_join_classes property.
        """
        self._classroom_force_automatically_join_classes = value
    
    @property
    def classroom_force_request_permission_to_leave_classes(self,) -> Optional[bool]:
        """
        Gets the classroomForceRequestPermissionToLeaveClasses property value. Indicates whether a student enrolled in an unmanaged course via Classroom will request permission from the teacher when attempting to leave the course (iOS 11.3 and later).
        Returns: Optional[bool]
        """
        return self._classroom_force_request_permission_to_leave_classes
    
    @classroom_force_request_permission_to_leave_classes.setter
    def classroom_force_request_permission_to_leave_classes(self,value: Optional[bool] = None) -> None:
        """
        Sets the classroomForceRequestPermissionToLeaveClasses property value. Indicates whether a student enrolled in an unmanaged course via Classroom will request permission from the teacher when attempting to leave the course (iOS 11.3 and later).
        Args:
            value: Value to set for the classroom_force_request_permission_to_leave_classes property.
        """
        self._classroom_force_request_permission_to_leave_classes = value
    
    @property
    def classroom_force_unprompted_app_and_device_lock(self,) -> Optional[bool]:
        """
        Gets the classroomForceUnpromptedAppAndDeviceLock property value. Indicates whether or not to allow the teacher to lock apps or the device without prompting the student. Supervised only.
        Returns: Optional[bool]
        """
        return self._classroom_force_unprompted_app_and_device_lock
    
    @classroom_force_unprompted_app_and_device_lock.setter
    def classroom_force_unprompted_app_and_device_lock(self,value: Optional[bool] = None) -> None:
        """
        Sets the classroomForceUnpromptedAppAndDeviceLock property value. Indicates whether or not to allow the teacher to lock apps or the device without prompting the student. Supervised only.
        Args:
            value: Value to set for the classroom_force_unprompted_app_and_device_lock property.
        """
        self._classroom_force_unprompted_app_and_device_lock = value
    
    @property
    def compliant_app_list_type(self,) -> Optional[app_list_type.AppListType]:
        """
        Gets the compliantAppListType property value. Possible values of the compliance app list.
        Returns: Optional[app_list_type.AppListType]
        """
        return self._compliant_app_list_type
    
    @compliant_app_list_type.setter
    def compliant_app_list_type(self,value: Optional[app_list_type.AppListType] = None) -> None:
        """
        Sets the compliantAppListType property value. Possible values of the compliance app list.
        Args:
            value: Value to set for the compliant_app_list_type property.
        """
        self._compliant_app_list_type = value
    
    @property
    def compliant_apps_list(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the compliantAppsList property value. List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._compliant_apps_list
    
    @compliant_apps_list.setter
    def compliant_apps_list(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the compliantAppsList property value. List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
        Args:
            value: Value to set for the compliant_apps_list property.
        """
        self._compliant_apps_list = value
    
    @property
    def configuration_profile_block_changes(self,) -> Optional[bool]:
        """
        Gets the configurationProfileBlockChanges property value. Indicates whether or not to block the user from installing configuration profiles and certificates interactively when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._configuration_profile_block_changes
    
    @configuration_profile_block_changes.setter
    def configuration_profile_block_changes(self,value: Optional[bool] = None) -> None:
        """
        Sets the configurationProfileBlockChanges property value. Indicates whether or not to block the user from installing configuration profiles and certificates interactively when the device is in supervised mode.
        Args:
            value: Value to set for the configuration_profile_block_changes property.
        """
        self._configuration_profile_block_changes = value
    
    @property
    def contacts_allow_managed_to_unmanaged_write(self,) -> Optional[bool]:
        """
        Gets the contactsAllowManagedToUnmanagedWrite property value. Indicates whether or not managed apps can write contacts to unmanaged contacts accounts (iOS 12.0 and later).
        Returns: Optional[bool]
        """
        return self._contacts_allow_managed_to_unmanaged_write
    
    @contacts_allow_managed_to_unmanaged_write.setter
    def contacts_allow_managed_to_unmanaged_write(self,value: Optional[bool] = None) -> None:
        """
        Sets the contactsAllowManagedToUnmanagedWrite property value. Indicates whether or not managed apps can write contacts to unmanaged contacts accounts (iOS 12.0 and later).
        Args:
            value: Value to set for the contacts_allow_managed_to_unmanaged_write property.
        """
        self._contacts_allow_managed_to_unmanaged_write = value
    
    @property
    def contacts_allow_unmanaged_to_managed_read(self,) -> Optional[bool]:
        """
        Gets the contactsAllowUnmanagedToManagedRead property value. Indicates whether or not unmanaged apps can read from managed contacts accounts (iOS 12.0 or later).
        Returns: Optional[bool]
        """
        return self._contacts_allow_unmanaged_to_managed_read
    
    @contacts_allow_unmanaged_to_managed_read.setter
    def contacts_allow_unmanaged_to_managed_read(self,value: Optional[bool] = None) -> None:
        """
        Sets the contactsAllowUnmanagedToManagedRead property value. Indicates whether or not unmanaged apps can read from managed contacts accounts (iOS 12.0 or later).
        Args:
            value: Value to set for the contacts_allow_unmanaged_to_managed_read property.
        """
        self._contacts_allow_unmanaged_to_managed_read = value
    
    @property
    def continuous_path_keyboard_blocked(self,) -> Optional[bool]:
        """
        Gets the continuousPathKeyboardBlocked property value. Indicates whether or not to block the continuous path keyboard when the device is supervised (iOS 13 or later).
        Returns: Optional[bool]
        """
        return self._continuous_path_keyboard_blocked
    
    @continuous_path_keyboard_blocked.setter
    def continuous_path_keyboard_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the continuousPathKeyboardBlocked property value. Indicates whether or not to block the continuous path keyboard when the device is supervised (iOS 13 or later).
        Args:
            value: Value to set for the continuous_path_keyboard_blocked property.
        """
        self._continuous_path_keyboard_blocked = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosGeneralDeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosGeneralDeviceConfiguration()
    
    @property
    def date_and_time_force_set_automatically(self,) -> Optional[bool]:
        """
        Gets the dateAndTimeForceSetAutomatically property value. Indicates whether or not the Date and Time 'Set Automatically' feature is enabled and cannot be turned off by the user (iOS 12.0 and later).
        Returns: Optional[bool]
        """
        return self._date_and_time_force_set_automatically
    
    @date_and_time_force_set_automatically.setter
    def date_and_time_force_set_automatically(self,value: Optional[bool] = None) -> None:
        """
        Sets the dateAndTimeForceSetAutomatically property value. Indicates whether or not the Date and Time 'Set Automatically' feature is enabled and cannot be turned off by the user (iOS 12.0 and later).
        Args:
            value: Value to set for the date_and_time_force_set_automatically property.
        """
        self._date_and_time_force_set_automatically = value
    
    @property
    def definition_lookup_blocked(self,) -> Optional[bool]:
        """
        Gets the definitionLookupBlocked property value. Indicates whether or not to block definition lookup when the device is in supervised mode (iOS 8.1.3 and later ).
        Returns: Optional[bool]
        """
        return self._definition_lookup_blocked
    
    @definition_lookup_blocked.setter
    def definition_lookup_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the definitionLookupBlocked property value. Indicates whether or not to block definition lookup when the device is in supervised mode (iOS 8.1.3 and later ).
        Args:
            value: Value to set for the definition_lookup_blocked property.
        """
        self._definition_lookup_blocked = value
    
    @property
    def device_block_enable_restrictions(self,) -> Optional[bool]:
        """
        Gets the deviceBlockEnableRestrictions property value. Indicates whether or not to allow the user to enables restrictions in the device settings when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._device_block_enable_restrictions
    
    @device_block_enable_restrictions.setter
    def device_block_enable_restrictions(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceBlockEnableRestrictions property value. Indicates whether or not to allow the user to enables restrictions in the device settings when the device is in supervised mode.
        Args:
            value: Value to set for the device_block_enable_restrictions property.
        """
        self._device_block_enable_restrictions = value
    
    @property
    def device_block_erase_content_and_settings(self,) -> Optional[bool]:
        """
        Gets the deviceBlockEraseContentAndSettings property value. Indicates whether or not to allow the use of the 'Erase all content and settings' option on the device when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._device_block_erase_content_and_settings
    
    @device_block_erase_content_and_settings.setter
    def device_block_erase_content_and_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceBlockEraseContentAndSettings property value. Indicates whether or not to allow the use of the 'Erase all content and settings' option on the device when the device is in supervised mode.
        Args:
            value: Value to set for the device_block_erase_content_and_settings property.
        """
        self._device_block_erase_content_and_settings = value
    
    @property
    def device_block_name_modification(self,) -> Optional[bool]:
        """
        Gets the deviceBlockNameModification property value. Indicates whether or not to allow device name modification when the device is in supervised mode (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._device_block_name_modification
    
    @device_block_name_modification.setter
    def device_block_name_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceBlockNameModification property value. Indicates whether or not to allow device name modification when the device is in supervised mode (iOS 9.0 and later).
        Args:
            value: Value to set for the device_block_name_modification property.
        """
        self._device_block_name_modification = value
    
    @property
    def diagnostic_data_block_submission(self,) -> Optional[bool]:
        """
        Gets the diagnosticDataBlockSubmission property value. Indicates whether or not to block diagnostic data submission.
        Returns: Optional[bool]
        """
        return self._diagnostic_data_block_submission
    
    @diagnostic_data_block_submission.setter
    def diagnostic_data_block_submission(self,value: Optional[bool] = None) -> None:
        """
        Sets the diagnosticDataBlockSubmission property value. Indicates whether or not to block diagnostic data submission.
        Args:
            value: Value to set for the diagnostic_data_block_submission property.
        """
        self._diagnostic_data_block_submission = value
    
    @property
    def diagnostic_data_block_submission_modification(self,) -> Optional[bool]:
        """
        Gets the diagnosticDataBlockSubmissionModification property value. Indicates whether or not to allow diagnostics submission settings modification when the device is in supervised mode (iOS 9.3.2 and later).
        Returns: Optional[bool]
        """
        return self._diagnostic_data_block_submission_modification
    
    @diagnostic_data_block_submission_modification.setter
    def diagnostic_data_block_submission_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the diagnosticDataBlockSubmissionModification property value. Indicates whether or not to allow diagnostics submission settings modification when the device is in supervised mode (iOS 9.3.2 and later).
        Args:
            value: Value to set for the diagnostic_data_block_submission_modification property.
        """
        self._diagnostic_data_block_submission_modification = value
    
    @property
    def documents_block_managed_documents_in_unmanaged_apps(self,) -> Optional[bool]:
        """
        Gets the documentsBlockManagedDocumentsInUnmanagedApps property value. Indicates whether or not to block the user from viewing managed documents in unmanaged apps.
        Returns: Optional[bool]
        """
        return self._documents_block_managed_documents_in_unmanaged_apps
    
    @documents_block_managed_documents_in_unmanaged_apps.setter
    def documents_block_managed_documents_in_unmanaged_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the documentsBlockManagedDocumentsInUnmanagedApps property value. Indicates whether or not to block the user from viewing managed documents in unmanaged apps.
        Args:
            value: Value to set for the documents_block_managed_documents_in_unmanaged_apps property.
        """
        self._documents_block_managed_documents_in_unmanaged_apps = value
    
    @property
    def documents_block_unmanaged_documents_in_managed_apps(self,) -> Optional[bool]:
        """
        Gets the documentsBlockUnmanagedDocumentsInManagedApps property value. Indicates whether or not to block the user from viewing unmanaged documents in managed apps.
        Returns: Optional[bool]
        """
        return self._documents_block_unmanaged_documents_in_managed_apps
    
    @documents_block_unmanaged_documents_in_managed_apps.setter
    def documents_block_unmanaged_documents_in_managed_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the documentsBlockUnmanagedDocumentsInManagedApps property value. Indicates whether or not to block the user from viewing unmanaged documents in managed apps.
        Args:
            value: Value to set for the documents_block_unmanaged_documents_in_managed_apps property.
        """
        self._documents_block_unmanaged_documents_in_managed_apps = value
    
    @property
    def email_in_domain_suffixes(self,) -> Optional[List[str]]:
        """
        Gets the emailInDomainSuffixes property value. An email address lacking a suffix that matches any of these strings will be considered out-of-domain.
        Returns: Optional[List[str]]
        """
        return self._email_in_domain_suffixes
    
    @email_in_domain_suffixes.setter
    def email_in_domain_suffixes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the emailInDomainSuffixes property value. An email address lacking a suffix that matches any of these strings will be considered out-of-domain.
        Args:
            value: Value to set for the email_in_domain_suffixes property.
        """
        self._email_in_domain_suffixes = value
    
    @property
    def enterprise_app_block_trust(self,) -> Optional[bool]:
        """
        Gets the enterpriseAppBlockTrust property value. Indicates whether or not to block the user from trusting an enterprise app.
        Returns: Optional[bool]
        """
        return self._enterprise_app_block_trust
    
    @enterprise_app_block_trust.setter
    def enterprise_app_block_trust(self,value: Optional[bool] = None) -> None:
        """
        Sets the enterpriseAppBlockTrust property value. Indicates whether or not to block the user from trusting an enterprise app.
        Args:
            value: Value to set for the enterprise_app_block_trust property.
        """
        self._enterprise_app_block_trust = value
    
    @property
    def enterprise_app_block_trust_modification(self,) -> Optional[bool]:
        """
        Gets the enterpriseAppBlockTrustModification property value. [Deprecated] Configuring this setting and setting the value to 'true' has no effect on the device.
        Returns: Optional[bool]
        """
        return self._enterprise_app_block_trust_modification
    
    @enterprise_app_block_trust_modification.setter
    def enterprise_app_block_trust_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the enterpriseAppBlockTrustModification property value. [Deprecated] Configuring this setting and setting the value to 'true' has no effect on the device.
        Args:
            value: Value to set for the enterprise_app_block_trust_modification property.
        """
        self._enterprise_app_block_trust_modification = value
    
    @property
    def enterprise_book_block_backup(self,) -> Optional[bool]:
        """
        Gets the enterpriseBookBlockBackup property value. Indicates whether or not Enterprise book back up is blocked.
        Returns: Optional[bool]
        """
        return self._enterprise_book_block_backup
    
    @enterprise_book_block_backup.setter
    def enterprise_book_block_backup(self,value: Optional[bool] = None) -> None:
        """
        Sets the enterpriseBookBlockBackup property value. Indicates whether or not Enterprise book back up is blocked.
        Args:
            value: Value to set for the enterprise_book_block_backup property.
        """
        self._enterprise_book_block_backup = value
    
    @property
    def enterprise_book_block_metadata_sync(self,) -> Optional[bool]:
        """
        Gets the enterpriseBookBlockMetadataSync property value. Indicates whether or not Enterprise book notes and highlights sync is blocked.
        Returns: Optional[bool]
        """
        return self._enterprise_book_block_metadata_sync
    
    @enterprise_book_block_metadata_sync.setter
    def enterprise_book_block_metadata_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the enterpriseBookBlockMetadataSync property value. Indicates whether or not Enterprise book notes and highlights sync is blocked.
        Args:
            value: Value to set for the enterprise_book_block_metadata_sync property.
        """
        self._enterprise_book_block_metadata_sync = value
    
    @property
    def esim_block_modification(self,) -> Optional[bool]:
        """
        Gets the esimBlockModification property value. Indicates whether or not to allow the addition or removal of cellular plans on the eSIM of a supervised device.
        Returns: Optional[bool]
        """
        return self._esim_block_modification
    
    @esim_block_modification.setter
    def esim_block_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the esimBlockModification property value. Indicates whether or not to allow the addition or removal of cellular plans on the eSIM of a supervised device.
        Args:
            value: Value to set for the esim_block_modification property.
        """
        self._esim_block_modification = value
    
    @property
    def face_time_blocked(self,) -> Optional[bool]:
        """
        Gets the faceTimeBlocked property value. Indicates whether or not to block the user from using FaceTime. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._face_time_blocked
    
    @face_time_blocked.setter
    def face_time_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the faceTimeBlocked property value. Indicates whether or not to block the user from using FaceTime. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the face_time_blocked property.
        """
        self._face_time_blocked = value
    
    @property
    def files_network_drive_access_blocked(self,) -> Optional[bool]:
        """
        Gets the filesNetworkDriveAccessBlocked property value. Indicates if devices can access files or other resources on a network server using the Server Message Block (SMB) protocol. Available for devices running iOS and iPadOS, versions 13.0 and later.
        Returns: Optional[bool]
        """
        return self._files_network_drive_access_blocked
    
    @files_network_drive_access_blocked.setter
    def files_network_drive_access_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the filesNetworkDriveAccessBlocked property value. Indicates if devices can access files or other resources on a network server using the Server Message Block (SMB) protocol. Available for devices running iOS and iPadOS, versions 13.0 and later.
        Args:
            value: Value to set for the files_network_drive_access_blocked property.
        """
        self._files_network_drive_access_blocked = value
    
    @property
    def files_usb_drive_access_blocked(self,) -> Optional[bool]:
        """
        Gets the filesUsbDriveAccessBlocked property value. Indicates if sevices with access can connect to and open files on a USB drive. Available for devices running iOS and iPadOS, versions 13.0 and later.
        Returns: Optional[bool]
        """
        return self._files_usb_drive_access_blocked
    
    @files_usb_drive_access_blocked.setter
    def files_usb_drive_access_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the filesUsbDriveAccessBlocked property value. Indicates if sevices with access can connect to and open files on a USB drive. Available for devices running iOS and iPadOS, versions 13.0 and later.
        Args:
            value: Value to set for the files_usb_drive_access_blocked property.
        """
        self._files_usb_drive_access_blocked = value
    
    @property
    def find_my_device_in_find_my_app_blocked(self,) -> Optional[bool]:
        """
        Gets the findMyDeviceInFindMyAppBlocked property value. Indicates whether or not to block Find My Device when the device is supervised (iOS 13 or later).
        Returns: Optional[bool]
        """
        return self._find_my_device_in_find_my_app_blocked
    
    @find_my_device_in_find_my_app_blocked.setter
    def find_my_device_in_find_my_app_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the findMyDeviceInFindMyAppBlocked property value. Indicates whether or not to block Find My Device when the device is supervised (iOS 13 or later).
        Args:
            value: Value to set for the find_my_device_in_find_my_app_blocked property.
        """
        self._find_my_device_in_find_my_app_blocked = value
    
    @property
    def find_my_friends_blocked(self,) -> Optional[bool]:
        """
        Gets the findMyFriendsBlocked property value. Indicates whether or not to block changes to Find My Friends when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._find_my_friends_blocked
    
    @find_my_friends_blocked.setter
    def find_my_friends_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the findMyFriendsBlocked property value. Indicates whether or not to block changes to Find My Friends when the device is in supervised mode.
        Args:
            value: Value to set for the find_my_friends_blocked property.
        """
        self._find_my_friends_blocked = value
    
    @property
    def find_my_friends_in_find_my_app_blocked(self,) -> Optional[bool]:
        """
        Gets the findMyFriendsInFindMyAppBlocked property value. Indicates whether or not to block Find My Friends when the device is supervised (iOS 13 or later).
        Returns: Optional[bool]
        """
        return self._find_my_friends_in_find_my_app_blocked
    
    @find_my_friends_in_find_my_app_blocked.setter
    def find_my_friends_in_find_my_app_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the findMyFriendsInFindMyAppBlocked property value. Indicates whether or not to block Find My Friends when the device is supervised (iOS 13 or later).
        Args:
            value: Value to set for the find_my_friends_in_find_my_app_blocked property.
        """
        self._find_my_friends_in_find_my_app_blocked = value
    
    @property
    def game_center_blocked(self,) -> Optional[bool]:
        """
        Gets the gameCenterBlocked property value. Indicates whether or not to block the user from using Game Center when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._game_center_blocked
    
    @game_center_blocked.setter
    def game_center_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the gameCenterBlocked property value. Indicates whether or not to block the user from using Game Center when the device is in supervised mode.
        Args:
            value: Value to set for the game_center_blocked property.
        """
        self._game_center_blocked = value
    
    @property
    def gaming_block_game_center_friends(self,) -> Optional[bool]:
        """
        Gets the gamingBlockGameCenterFriends property value. Indicates whether or not to block the user from having friends in Game Center. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._gaming_block_game_center_friends
    
    @gaming_block_game_center_friends.setter
    def gaming_block_game_center_friends(self,value: Optional[bool] = None) -> None:
        """
        Sets the gamingBlockGameCenterFriends property value. Indicates whether or not to block the user from having friends in Game Center. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the gaming_block_game_center_friends property.
        """
        self._gaming_block_game_center_friends = value
    
    @property
    def gaming_block_multiplayer(self,) -> Optional[bool]:
        """
        Gets the gamingBlockMultiplayer property value. Indicates whether or not to block the user from using multiplayer gaming. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._gaming_block_multiplayer
    
    @gaming_block_multiplayer.setter
    def gaming_block_multiplayer(self,value: Optional[bool] = None) -> None:
        """
        Sets the gamingBlockMultiplayer property value. Indicates whether or not to block the user from using multiplayer gaming. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the gaming_block_multiplayer property.
        """
        self._gaming_block_multiplayer = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_list_item, app_list_type, device_configuration, ios_kiosk_mode_app_type, ios_network_usage_rule, media_content_rating_australia, media_content_rating_canada, media_content_rating_france, media_content_rating_germany, media_content_rating_ireland, media_content_rating_japan, media_content_rating_new_zealand, media_content_rating_united_kingdom, media_content_rating_united_states, rating_apps_type, required_password_type, web_browser_cookie_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "accountBlockModification": lambda n : setattr(self, 'account_block_modification', n.get_bool_value()),
            "activationLockAllowWhenSupervised": lambda n : setattr(self, 'activation_lock_allow_when_supervised', n.get_bool_value()),
            "airDropBlocked": lambda n : setattr(self, 'air_drop_blocked', n.get_bool_value()),
            "airDropForceUnmanagedDropTarget": lambda n : setattr(self, 'air_drop_force_unmanaged_drop_target', n.get_bool_value()),
            "airPlayForcePairingPasswordForOutgoingRequests": lambda n : setattr(self, 'air_play_force_pairing_password_for_outgoing_requests', n.get_bool_value()),
            "airPrintBlocked": lambda n : setattr(self, 'air_print_blocked', n.get_bool_value()),
            "airPrintBlockiBeaconDiscovery": lambda n : setattr(self, 'air_print_blocki_beacon_discovery', n.get_bool_value()),
            "airPrintBlockCredentialsStorage": lambda n : setattr(self, 'air_print_block_credentials_storage', n.get_bool_value()),
            "airPrintForceTrustedTLS": lambda n : setattr(self, 'air_print_force_trusted_t_l_s', n.get_bool_value()),
            "appleNewsBlocked": lambda n : setattr(self, 'apple_news_blocked', n.get_bool_value()),
            "applePersonalizedAdsBlocked": lambda n : setattr(self, 'apple_personalized_ads_blocked', n.get_bool_value()),
            "appleWatchBlockPairing": lambda n : setattr(self, 'apple_watch_block_pairing', n.get_bool_value()),
            "appleWatchForceWristDetection": lambda n : setattr(self, 'apple_watch_force_wrist_detection', n.get_bool_value()),
            "appsSingleAppModeList": lambda n : setattr(self, 'apps_single_app_mode_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "appsVisibilityList": lambda n : setattr(self, 'apps_visibility_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "appsVisibilityListType": lambda n : setattr(self, 'apps_visibility_list_type', n.get_enum_value(app_list_type.AppListType)),
            "appClipsBlocked": lambda n : setattr(self, 'app_clips_blocked', n.get_bool_value()),
            "appRemovalBlocked": lambda n : setattr(self, 'app_removal_blocked', n.get_bool_value()),
            "appStoreBlocked": lambda n : setattr(self, 'app_store_blocked', n.get_bool_value()),
            "appStoreBlockAutomaticDownloads": lambda n : setattr(self, 'app_store_block_automatic_downloads', n.get_bool_value()),
            "appStoreBlockInAppPurchases": lambda n : setattr(self, 'app_store_block_in_app_purchases', n.get_bool_value()),
            "appStoreBlockUIAppInstallation": lambda n : setattr(self, 'app_store_block_u_i_app_installation', n.get_bool_value()),
            "appStoreRequirePassword": lambda n : setattr(self, 'app_store_require_password', n.get_bool_value()),
            "autoFillForceAuthentication": lambda n : setattr(self, 'auto_fill_force_authentication', n.get_bool_value()),
            "autoUnlockBlocked": lambda n : setattr(self, 'auto_unlock_blocked', n.get_bool_value()),
            "blockSystemAppRemoval": lambda n : setattr(self, 'block_system_app_removal', n.get_bool_value()),
            "bluetoothBlockModification": lambda n : setattr(self, 'bluetooth_block_modification', n.get_bool_value()),
            "cameraBlocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "cellularBlockDataRoaming": lambda n : setattr(self, 'cellular_block_data_roaming', n.get_bool_value()),
            "cellularBlockGlobalBackgroundFetchWhileRoaming": lambda n : setattr(self, 'cellular_block_global_background_fetch_while_roaming', n.get_bool_value()),
            "cellularBlockPersonalHotspot": lambda n : setattr(self, 'cellular_block_personal_hotspot', n.get_bool_value()),
            "cellularBlockPersonalHotspotModification": lambda n : setattr(self, 'cellular_block_personal_hotspot_modification', n.get_bool_value()),
            "cellularBlockPerAppDataModification": lambda n : setattr(self, 'cellular_block_per_app_data_modification', n.get_bool_value()),
            "cellularBlockPlanModification": lambda n : setattr(self, 'cellular_block_plan_modification', n.get_bool_value()),
            "cellularBlockVoiceRoaming": lambda n : setattr(self, 'cellular_block_voice_roaming', n.get_bool_value()),
            "certificatesBlockUntrustedTlsCertificates": lambda n : setattr(self, 'certificates_block_untrusted_tls_certificates', n.get_bool_value()),
            "classroomAppBlockRemoteScreenObservation": lambda n : setattr(self, 'classroom_app_block_remote_screen_observation', n.get_bool_value()),
            "classroomAppForceUnpromptedScreenObservation": lambda n : setattr(self, 'classroom_app_force_unprompted_screen_observation', n.get_bool_value()),
            "classroomForceAutomaticallyJoinClasses": lambda n : setattr(self, 'classroom_force_automatically_join_classes', n.get_bool_value()),
            "classroomForceRequestPermissionToLeaveClasses": lambda n : setattr(self, 'classroom_force_request_permission_to_leave_classes', n.get_bool_value()),
            "classroomForceUnpromptedAppAndDeviceLock": lambda n : setattr(self, 'classroom_force_unprompted_app_and_device_lock', n.get_bool_value()),
            "compliantAppsList": lambda n : setattr(self, 'compliant_apps_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "compliantAppListType": lambda n : setattr(self, 'compliant_app_list_type', n.get_enum_value(app_list_type.AppListType)),
            "configurationProfileBlockChanges": lambda n : setattr(self, 'configuration_profile_block_changes', n.get_bool_value()),
            "contactsAllowManagedToUnmanagedWrite": lambda n : setattr(self, 'contacts_allow_managed_to_unmanaged_write', n.get_bool_value()),
            "contactsAllowUnmanagedToManagedRead": lambda n : setattr(self, 'contacts_allow_unmanaged_to_managed_read', n.get_bool_value()),
            "continuousPathKeyboardBlocked": lambda n : setattr(self, 'continuous_path_keyboard_blocked', n.get_bool_value()),
            "dateAndTimeForceSetAutomatically": lambda n : setattr(self, 'date_and_time_force_set_automatically', n.get_bool_value()),
            "definitionLookupBlocked": lambda n : setattr(self, 'definition_lookup_blocked', n.get_bool_value()),
            "deviceBlockEnableRestrictions": lambda n : setattr(self, 'device_block_enable_restrictions', n.get_bool_value()),
            "deviceBlockEraseContentAndSettings": lambda n : setattr(self, 'device_block_erase_content_and_settings', n.get_bool_value()),
            "deviceBlockNameModification": lambda n : setattr(self, 'device_block_name_modification', n.get_bool_value()),
            "diagnosticDataBlockSubmission": lambda n : setattr(self, 'diagnostic_data_block_submission', n.get_bool_value()),
            "diagnosticDataBlockSubmissionModification": lambda n : setattr(self, 'diagnostic_data_block_submission_modification', n.get_bool_value()),
            "documentsBlockManagedDocumentsInUnmanagedApps": lambda n : setattr(self, 'documents_block_managed_documents_in_unmanaged_apps', n.get_bool_value()),
            "documentsBlockUnmanagedDocumentsInManagedApps": lambda n : setattr(self, 'documents_block_unmanaged_documents_in_managed_apps', n.get_bool_value()),
            "emailInDomainSuffixes": lambda n : setattr(self, 'email_in_domain_suffixes', n.get_collection_of_primitive_values(str)),
            "enterpriseAppBlockTrust": lambda n : setattr(self, 'enterprise_app_block_trust', n.get_bool_value()),
            "enterpriseAppBlockTrustModification": lambda n : setattr(self, 'enterprise_app_block_trust_modification', n.get_bool_value()),
            "enterpriseBookBlockBackup": lambda n : setattr(self, 'enterprise_book_block_backup', n.get_bool_value()),
            "enterpriseBookBlockMetadataSync": lambda n : setattr(self, 'enterprise_book_block_metadata_sync', n.get_bool_value()),
            "esimBlockModification": lambda n : setattr(self, 'esim_block_modification', n.get_bool_value()),
            "faceTimeBlocked": lambda n : setattr(self, 'face_time_blocked', n.get_bool_value()),
            "filesNetworkDriveAccessBlocked": lambda n : setattr(self, 'files_network_drive_access_blocked', n.get_bool_value()),
            "filesUsbDriveAccessBlocked": lambda n : setattr(self, 'files_usb_drive_access_blocked', n.get_bool_value()),
            "findMyDeviceInFindMyAppBlocked": lambda n : setattr(self, 'find_my_device_in_find_my_app_blocked', n.get_bool_value()),
            "findMyFriendsBlocked": lambda n : setattr(self, 'find_my_friends_blocked', n.get_bool_value()),
            "findMyFriendsInFindMyAppBlocked": lambda n : setattr(self, 'find_my_friends_in_find_my_app_blocked', n.get_bool_value()),
            "gameCenterBlocked": lambda n : setattr(self, 'game_center_blocked', n.get_bool_value()),
            "gamingBlockGameCenterFriends": lambda n : setattr(self, 'gaming_block_game_center_friends', n.get_bool_value()),
            "gamingBlockMultiplayer": lambda n : setattr(self, 'gaming_block_multiplayer', n.get_bool_value()),
            "hostPairingBlocked": lambda n : setattr(self, 'host_pairing_blocked', n.get_bool_value()),
            "iBooksStoreBlocked": lambda n : setattr(self, 'i_books_store_blocked', n.get_bool_value()),
            "iBooksStoreBlockErotica": lambda n : setattr(self, 'i_books_store_block_erotica', n.get_bool_value()),
            "iCloudBlockActivityContinuation": lambda n : setattr(self, 'i_cloud_block_activity_continuation', n.get_bool_value()),
            "iCloudBlockBackup": lambda n : setattr(self, 'i_cloud_block_backup', n.get_bool_value()),
            "iCloudBlockDocumentSync": lambda n : setattr(self, 'i_cloud_block_document_sync', n.get_bool_value()),
            "iCloudBlockManagedAppsSync": lambda n : setattr(self, 'i_cloud_block_managed_apps_sync', n.get_bool_value()),
            "iCloudBlockPhotoLibrary": lambda n : setattr(self, 'i_cloud_block_photo_library', n.get_bool_value()),
            "iCloudBlockPhotoStreamSync": lambda n : setattr(self, 'i_cloud_block_photo_stream_sync', n.get_bool_value()),
            "iCloudBlockSharedPhotoStream": lambda n : setattr(self, 'i_cloud_block_shared_photo_stream', n.get_bool_value()),
            "iCloudPrivateRelayBlocked": lambda n : setattr(self, 'i_cloud_private_relay_blocked', n.get_bool_value()),
            "iCloudRequireEncryptedBackup": lambda n : setattr(self, 'i_cloud_require_encrypted_backup', n.get_bool_value()),
            "iTunesBlocked": lambda n : setattr(self, 'i_tunes_blocked', n.get_bool_value()),
            "iTunesBlockExplicitContent": lambda n : setattr(self, 'i_tunes_block_explicit_content', n.get_bool_value()),
            "iTunesBlockMusicService": lambda n : setattr(self, 'i_tunes_block_music_service', n.get_bool_value()),
            "iTunesBlockRadio": lambda n : setattr(self, 'i_tunes_block_radio', n.get_bool_value()),
            "keyboardBlockAutoCorrect": lambda n : setattr(self, 'keyboard_block_auto_correct', n.get_bool_value()),
            "keyboardBlockDictation": lambda n : setattr(self, 'keyboard_block_dictation', n.get_bool_value()),
            "keyboardBlockPredictive": lambda n : setattr(self, 'keyboard_block_predictive', n.get_bool_value()),
            "keyboardBlockShortcuts": lambda n : setattr(self, 'keyboard_block_shortcuts', n.get_bool_value()),
            "keyboardBlockSpellCheck": lambda n : setattr(self, 'keyboard_block_spell_check', n.get_bool_value()),
            "keychainBlockCloudSync": lambda n : setattr(self, 'keychain_block_cloud_sync', n.get_bool_value()),
            "kioskModeAllowAssistiveSpeak": lambda n : setattr(self, 'kiosk_mode_allow_assistive_speak', n.get_bool_value()),
            "kioskModeAllowAssistiveTouchSettings": lambda n : setattr(self, 'kiosk_mode_allow_assistive_touch_settings', n.get_bool_value()),
            "kioskModeAllowAutoLock": lambda n : setattr(self, 'kiosk_mode_allow_auto_lock', n.get_bool_value()),
            "kioskModeAllowColorInversionSettings": lambda n : setattr(self, 'kiosk_mode_allow_color_inversion_settings', n.get_bool_value()),
            "kioskModeAllowRingerSwitch": lambda n : setattr(self, 'kiosk_mode_allow_ringer_switch', n.get_bool_value()),
            "kioskModeAllowScreenRotation": lambda n : setattr(self, 'kiosk_mode_allow_screen_rotation', n.get_bool_value()),
            "kioskModeAllowSleepButton": lambda n : setattr(self, 'kiosk_mode_allow_sleep_button', n.get_bool_value()),
            "kioskModeAllowTouchscreen": lambda n : setattr(self, 'kiosk_mode_allow_touchscreen', n.get_bool_value()),
            "kioskModeAllowVoiceControlModification": lambda n : setattr(self, 'kiosk_mode_allow_voice_control_modification', n.get_bool_value()),
            "kioskModeAllowVoiceOverSettings": lambda n : setattr(self, 'kiosk_mode_allow_voice_over_settings', n.get_bool_value()),
            "kioskModeAllowVolumeButtons": lambda n : setattr(self, 'kiosk_mode_allow_volume_buttons', n.get_bool_value()),
            "kioskModeAllowZoomSettings": lambda n : setattr(self, 'kiosk_mode_allow_zoom_settings', n.get_bool_value()),
            "kioskModeAppStoreUrl": lambda n : setattr(self, 'kiosk_mode_app_store_url', n.get_str_value()),
            "kioskModeAppType": lambda n : setattr(self, 'kiosk_mode_app_type', n.get_enum_value(ios_kiosk_mode_app_type.IosKioskModeAppType)),
            "kioskModeBlockAutoLock": lambda n : setattr(self, 'kiosk_mode_block_auto_lock', n.get_bool_value()),
            "kioskModeBlockRingerSwitch": lambda n : setattr(self, 'kiosk_mode_block_ringer_switch', n.get_bool_value()),
            "kioskModeBlockScreenRotation": lambda n : setattr(self, 'kiosk_mode_block_screen_rotation', n.get_bool_value()),
            "kioskModeBlockSleepButton": lambda n : setattr(self, 'kiosk_mode_block_sleep_button', n.get_bool_value()),
            "kioskModeBlockTouchscreen": lambda n : setattr(self, 'kiosk_mode_block_touchscreen', n.get_bool_value()),
            "kioskModeBlockVolumeButtons": lambda n : setattr(self, 'kiosk_mode_block_volume_buttons', n.get_bool_value()),
            "kioskModeBuiltInAppId": lambda n : setattr(self, 'kiosk_mode_built_in_app_id', n.get_str_value()),
            "kioskModeEnableVoiceControl": lambda n : setattr(self, 'kiosk_mode_enable_voice_control', n.get_bool_value()),
            "kioskModeManagedAppId": lambda n : setattr(self, 'kiosk_mode_managed_app_id', n.get_str_value()),
            "kioskModeRequireAssistiveTouch": lambda n : setattr(self, 'kiosk_mode_require_assistive_touch', n.get_bool_value()),
            "kioskModeRequireColorInversion": lambda n : setattr(self, 'kiosk_mode_require_color_inversion', n.get_bool_value()),
            "kioskModeRequireMonoAudio": lambda n : setattr(self, 'kiosk_mode_require_mono_audio', n.get_bool_value()),
            "kioskModeRequireVoiceOver": lambda n : setattr(self, 'kiosk_mode_require_voice_over', n.get_bool_value()),
            "kioskModeRequireZoom": lambda n : setattr(self, 'kiosk_mode_require_zoom', n.get_bool_value()),
            "lockScreenBlockControlCenter": lambda n : setattr(self, 'lock_screen_block_control_center', n.get_bool_value()),
            "lockScreenBlockNotificationView": lambda n : setattr(self, 'lock_screen_block_notification_view', n.get_bool_value()),
            "lockScreenBlockPassbook": lambda n : setattr(self, 'lock_screen_block_passbook', n.get_bool_value()),
            "lockScreenBlockTodayView": lambda n : setattr(self, 'lock_screen_block_today_view', n.get_bool_value()),
            "managedPasteboardRequired": lambda n : setattr(self, 'managed_pasteboard_required', n.get_bool_value()),
            "mediaContentRatingApps": lambda n : setattr(self, 'media_content_rating_apps', n.get_enum_value(rating_apps_type.RatingAppsType)),
            "mediaContentRatingAustralia": lambda n : setattr(self, 'media_content_rating_australia', n.get_object_value(media_content_rating_australia.MediaContentRatingAustralia)),
            "mediaContentRatingCanada": lambda n : setattr(self, 'media_content_rating_canada', n.get_object_value(media_content_rating_canada.MediaContentRatingCanada)),
            "mediaContentRatingFrance": lambda n : setattr(self, 'media_content_rating_france', n.get_object_value(media_content_rating_france.MediaContentRatingFrance)),
            "mediaContentRatingGermany": lambda n : setattr(self, 'media_content_rating_germany', n.get_object_value(media_content_rating_germany.MediaContentRatingGermany)),
            "mediaContentRatingIreland": lambda n : setattr(self, 'media_content_rating_ireland', n.get_object_value(media_content_rating_ireland.MediaContentRatingIreland)),
            "mediaContentRatingJapan": lambda n : setattr(self, 'media_content_rating_japan', n.get_object_value(media_content_rating_japan.MediaContentRatingJapan)),
            "mediaContentRatingNewZealand": lambda n : setattr(self, 'media_content_rating_new_zealand', n.get_object_value(media_content_rating_new_zealand.MediaContentRatingNewZealand)),
            "mediaContentRatingUnitedKingdom": lambda n : setattr(self, 'media_content_rating_united_kingdom', n.get_object_value(media_content_rating_united_kingdom.MediaContentRatingUnitedKingdom)),
            "mediaContentRatingUnitedStates": lambda n : setattr(self, 'media_content_rating_united_states', n.get_object_value(media_content_rating_united_states.MediaContentRatingUnitedStates)),
            "messagesBlocked": lambda n : setattr(self, 'messages_blocked', n.get_bool_value()),
            "networkUsageRules": lambda n : setattr(self, 'network_usage_rules', n.get_collection_of_object_values(ios_network_usage_rule.IosNetworkUsageRule)),
            "nfcBlocked": lambda n : setattr(self, 'nfc_blocked', n.get_bool_value()),
            "notificationsBlockSettingsModification": lambda n : setattr(self, 'notifications_block_settings_modification', n.get_bool_value()),
            "onDeviceOnlyDictationForced": lambda n : setattr(self, 'on_device_only_dictation_forced', n.get_bool_value()),
            "onDeviceOnlyTranslationForced": lambda n : setattr(self, 'on_device_only_translation_forced', n.get_bool_value()),
            "passcodeBlockFingerprintModification": lambda n : setattr(self, 'passcode_block_fingerprint_modification', n.get_bool_value()),
            "passcodeBlockFingerprintUnlock": lambda n : setattr(self, 'passcode_block_fingerprint_unlock', n.get_bool_value()),
            "passcodeBlockModification": lambda n : setattr(self, 'passcode_block_modification', n.get_bool_value()),
            "passcodeBlockSimple": lambda n : setattr(self, 'passcode_block_simple', n.get_bool_value()),
            "passcodeExpirationDays": lambda n : setattr(self, 'passcode_expiration_days', n.get_int_value()),
            "passcodeMinimumCharacterSetCount": lambda n : setattr(self, 'passcode_minimum_character_set_count', n.get_int_value()),
            "passcodeMinimumLength": lambda n : setattr(self, 'passcode_minimum_length', n.get_int_value()),
            "passcodeMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'passcode_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passcodeMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'passcode_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passcodePreviousPasscodeBlockCount": lambda n : setattr(self, 'passcode_previous_passcode_block_count', n.get_int_value()),
            "passcodeRequired": lambda n : setattr(self, 'passcode_required', n.get_bool_value()),
            "passcodeRequiredType": lambda n : setattr(self, 'passcode_required_type', n.get_enum_value(required_password_type.RequiredPasswordType)),
            "passcodeSignInFailureCountBeforeWipe": lambda n : setattr(self, 'passcode_sign_in_failure_count_before_wipe', n.get_int_value()),
            "passwordBlockAirDropSharing": lambda n : setattr(self, 'password_block_air_drop_sharing', n.get_bool_value()),
            "passwordBlockAutoFill": lambda n : setattr(self, 'password_block_auto_fill', n.get_bool_value()),
            "passwordBlockProximityRequests": lambda n : setattr(self, 'password_block_proximity_requests', n.get_bool_value()),
            "pkiBlockOTAUpdates": lambda n : setattr(self, 'pki_block_o_t_a_updates', n.get_bool_value()),
            "podcastsBlocked": lambda n : setattr(self, 'podcasts_blocked', n.get_bool_value()),
            "privacyForceLimitAdTracking": lambda n : setattr(self, 'privacy_force_limit_ad_tracking', n.get_bool_value()),
            "proximityBlockSetupToNewDevice": lambda n : setattr(self, 'proximity_block_setup_to_new_device', n.get_bool_value()),
            "safariBlocked": lambda n : setattr(self, 'safari_blocked', n.get_bool_value()),
            "safariBlockAutofill": lambda n : setattr(self, 'safari_block_autofill', n.get_bool_value()),
            "safariBlockJavaScript": lambda n : setattr(self, 'safari_block_java_script', n.get_bool_value()),
            "safariBlockPopups": lambda n : setattr(self, 'safari_block_popups', n.get_bool_value()),
            "safariCookieSettings": lambda n : setattr(self, 'safari_cookie_settings', n.get_enum_value(web_browser_cookie_settings.WebBrowserCookieSettings)),
            "safariManagedDomains": lambda n : setattr(self, 'safari_managed_domains', n.get_collection_of_primitive_values(str)),
            "safariPasswordAutoFillDomains": lambda n : setattr(self, 'safari_password_auto_fill_domains', n.get_collection_of_primitive_values(str)),
            "safariRequireFraudWarning": lambda n : setattr(self, 'safari_require_fraud_warning', n.get_bool_value()),
            "screenCaptureBlocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "sharedDeviceBlockTemporarySessions": lambda n : setattr(self, 'shared_device_block_temporary_sessions', n.get_bool_value()),
            "siriBlocked": lambda n : setattr(self, 'siri_blocked', n.get_bool_value()),
            "siriBlockedWhenLocked": lambda n : setattr(self, 'siri_blocked_when_locked', n.get_bool_value()),
            "siriBlockUserGeneratedContent": lambda n : setattr(self, 'siri_block_user_generated_content', n.get_bool_value()),
            "siriRequireProfanityFilter": lambda n : setattr(self, 'siri_require_profanity_filter', n.get_bool_value()),
            "softwareUpdatesEnforcedDelayInDays": lambda n : setattr(self, 'software_updates_enforced_delay_in_days', n.get_int_value()),
            "softwareUpdatesForceDelayed": lambda n : setattr(self, 'software_updates_force_delayed', n.get_bool_value()),
            "spotlightBlockInternetResults": lambda n : setattr(self, 'spotlight_block_internet_results', n.get_bool_value()),
            "unpairedExternalBootToRecoveryAllowed": lambda n : setattr(self, 'unpaired_external_boot_to_recovery_allowed', n.get_bool_value()),
            "usbRestrictedModeBlocked": lambda n : setattr(self, 'usb_restricted_mode_blocked', n.get_bool_value()),
            "voiceDialingBlocked": lambda n : setattr(self, 'voice_dialing_blocked', n.get_bool_value()),
            "vpnBlockCreation": lambda n : setattr(self, 'vpn_block_creation', n.get_bool_value()),
            "wallpaperBlockModification": lambda n : setattr(self, 'wallpaper_block_modification', n.get_bool_value()),
            "wifiPowerOnForced": lambda n : setattr(self, 'wifi_power_on_forced', n.get_bool_value()),
            "wiFiConnectOnlyToConfiguredNetworks": lambda n : setattr(self, 'wi_fi_connect_only_to_configured_networks', n.get_bool_value()),
            "wiFiConnectToAllowedNetworksOnlyForced": lambda n : setattr(self, 'wi_fi_connect_to_allowed_networks_only_forced', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def host_pairing_blocked(self,) -> Optional[bool]:
        """
        Gets the hostPairingBlocked property value. indicates whether or not to allow host pairing to control the devices an iOS device can pair with when the iOS device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._host_pairing_blocked
    
    @host_pairing_blocked.setter
    def host_pairing_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the hostPairingBlocked property value. indicates whether or not to allow host pairing to control the devices an iOS device can pair with when the iOS device is in supervised mode.
        Args:
            value: Value to set for the host_pairing_blocked property.
        """
        self._host_pairing_blocked = value
    
    @property
    def i_books_store_block_erotica(self,) -> Optional[bool]:
        """
        Gets the iBooksStoreBlockErotica property value. Indicates whether or not to block the user from downloading media from the iBookstore that has been tagged as erotica.
        Returns: Optional[bool]
        """
        return self._i_books_store_block_erotica
    
    @i_books_store_block_erotica.setter
    def i_books_store_block_erotica(self,value: Optional[bool] = None) -> None:
        """
        Sets the iBooksStoreBlockErotica property value. Indicates whether or not to block the user from downloading media from the iBookstore that has been tagged as erotica.
        Args:
            value: Value to set for the i_books_store_block_erotica property.
        """
        self._i_books_store_block_erotica = value
    
    @property
    def i_books_store_blocked(self,) -> Optional[bool]:
        """
        Gets the iBooksStoreBlocked property value. Indicates whether or not to block the user from using the iBooks Store when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._i_books_store_blocked
    
    @i_books_store_blocked.setter
    def i_books_store_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the iBooksStoreBlocked property value. Indicates whether or not to block the user from using the iBooks Store when the device is in supervised mode.
        Args:
            value: Value to set for the i_books_store_blocked property.
        """
        self._i_books_store_blocked = value
    
    @property
    def i_cloud_block_activity_continuation(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockActivityContinuation property value. Indicates whether or not to block the user from continuing work they started on iOS device to another iOS or macOS device.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_activity_continuation
    
    @i_cloud_block_activity_continuation.setter
    def i_cloud_block_activity_continuation(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockActivityContinuation property value. Indicates whether or not to block the user from continuing work they started on iOS device to another iOS or macOS device.
        Args:
            value: Value to set for the i_cloud_block_activity_continuation property.
        """
        self._i_cloud_block_activity_continuation = value
    
    @property
    def i_cloud_block_backup(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockBackup property value. Indicates whether or not to block iCloud backup. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_backup
    
    @i_cloud_block_backup.setter
    def i_cloud_block_backup(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockBackup property value. Indicates whether or not to block iCloud backup. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the i_cloud_block_backup property.
        """
        self._i_cloud_block_backup = value
    
    @property
    def i_cloud_block_document_sync(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockDocumentSync property value. Indicates whether or not to block iCloud document sync. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_document_sync
    
    @i_cloud_block_document_sync.setter
    def i_cloud_block_document_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockDocumentSync property value. Indicates whether or not to block iCloud document sync. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the i_cloud_block_document_sync property.
        """
        self._i_cloud_block_document_sync = value
    
    @property
    def i_cloud_block_managed_apps_sync(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockManagedAppsSync property value. Indicates whether or not to block Managed Apps Cloud Sync.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_managed_apps_sync
    
    @i_cloud_block_managed_apps_sync.setter
    def i_cloud_block_managed_apps_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockManagedAppsSync property value. Indicates whether or not to block Managed Apps Cloud Sync.
        Args:
            value: Value to set for the i_cloud_block_managed_apps_sync property.
        """
        self._i_cloud_block_managed_apps_sync = value
    
    @property
    def i_cloud_block_photo_library(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockPhotoLibrary property value. Indicates whether or not to block iCloud Photo Library.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_photo_library
    
    @i_cloud_block_photo_library.setter
    def i_cloud_block_photo_library(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockPhotoLibrary property value. Indicates whether or not to block iCloud Photo Library.
        Args:
            value: Value to set for the i_cloud_block_photo_library property.
        """
        self._i_cloud_block_photo_library = value
    
    @property
    def i_cloud_block_photo_stream_sync(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockPhotoStreamSync property value. Indicates whether or not to block iCloud Photo Stream Sync.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_photo_stream_sync
    
    @i_cloud_block_photo_stream_sync.setter
    def i_cloud_block_photo_stream_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockPhotoStreamSync property value. Indicates whether or not to block iCloud Photo Stream Sync.
        Args:
            value: Value to set for the i_cloud_block_photo_stream_sync property.
        """
        self._i_cloud_block_photo_stream_sync = value
    
    @property
    def i_cloud_block_shared_photo_stream(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockSharedPhotoStream property value. Indicates whether or not to block Shared Photo Stream.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_shared_photo_stream
    
    @i_cloud_block_shared_photo_stream.setter
    def i_cloud_block_shared_photo_stream(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockSharedPhotoStream property value. Indicates whether or not to block Shared Photo Stream.
        Args:
            value: Value to set for the i_cloud_block_shared_photo_stream property.
        """
        self._i_cloud_block_shared_photo_stream = value
    
    @property
    def i_cloud_private_relay_blocked(self,) -> Optional[bool]:
        """
        Gets the iCloudPrivateRelayBlocked property value. iCloud private relay is an iCloud+ service that prevents networks and servers from monitoring a person's activity across the internet. By blocking iCloud private relay, Apple will not encrypt the traffic leaving the device. Available for devices running iOS 15 and later.
        Returns: Optional[bool]
        """
        return self._i_cloud_private_relay_blocked
    
    @i_cloud_private_relay_blocked.setter
    def i_cloud_private_relay_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudPrivateRelayBlocked property value. iCloud private relay is an iCloud+ service that prevents networks and servers from monitoring a person's activity across the internet. By blocking iCloud private relay, Apple will not encrypt the traffic leaving the device. Available for devices running iOS 15 and later.
        Args:
            value: Value to set for the i_cloud_private_relay_blocked property.
        """
        self._i_cloud_private_relay_blocked = value
    
    @property
    def i_cloud_require_encrypted_backup(self,) -> Optional[bool]:
        """
        Gets the iCloudRequireEncryptedBackup property value. Indicates whether or not to require backups to iCloud be encrypted.
        Returns: Optional[bool]
        """
        return self._i_cloud_require_encrypted_backup
    
    @i_cloud_require_encrypted_backup.setter
    def i_cloud_require_encrypted_backup(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudRequireEncryptedBackup property value. Indicates whether or not to require backups to iCloud be encrypted.
        Args:
            value: Value to set for the i_cloud_require_encrypted_backup property.
        """
        self._i_cloud_require_encrypted_backup = value
    
    @property
    def i_tunes_block_explicit_content(self,) -> Optional[bool]:
        """
        Gets the iTunesBlockExplicitContent property value. Indicates whether or not to block the user from accessing explicit content in iTunes and the App Store. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._i_tunes_block_explicit_content
    
    @i_tunes_block_explicit_content.setter
    def i_tunes_block_explicit_content(self,value: Optional[bool] = None) -> None:
        """
        Sets the iTunesBlockExplicitContent property value. Indicates whether or not to block the user from accessing explicit content in iTunes and the App Store. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the i_tunes_block_explicit_content property.
        """
        self._i_tunes_block_explicit_content = value
    
    @property
    def i_tunes_block_music_service(self,) -> Optional[bool]:
        """
        Gets the iTunesBlockMusicService property value. Indicates whether or not to block Music service and revert Music app to classic mode when the device is in supervised mode (iOS 9.3 and later and macOS 10.12 and later).
        Returns: Optional[bool]
        """
        return self._i_tunes_block_music_service
    
    @i_tunes_block_music_service.setter
    def i_tunes_block_music_service(self,value: Optional[bool] = None) -> None:
        """
        Sets the iTunesBlockMusicService property value. Indicates whether or not to block Music service and revert Music app to classic mode when the device is in supervised mode (iOS 9.3 and later and macOS 10.12 and later).
        Args:
            value: Value to set for the i_tunes_block_music_service property.
        """
        self._i_tunes_block_music_service = value
    
    @property
    def i_tunes_block_radio(self,) -> Optional[bool]:
        """
        Gets the iTunesBlockRadio property value. Indicates whether or not to block the user from using iTunes Radio when the device is in supervised mode (iOS 9.3 and later).
        Returns: Optional[bool]
        """
        return self._i_tunes_block_radio
    
    @i_tunes_block_radio.setter
    def i_tunes_block_radio(self,value: Optional[bool] = None) -> None:
        """
        Sets the iTunesBlockRadio property value. Indicates whether or not to block the user from using iTunes Radio when the device is in supervised mode (iOS 9.3 and later).
        Args:
            value: Value to set for the i_tunes_block_radio property.
        """
        self._i_tunes_block_radio = value
    
    @property
    def i_tunes_blocked(self,) -> Optional[bool]:
        """
        Gets the iTunesBlocked property value. Indicates whether or not to block the iTunes app. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._i_tunes_blocked
    
    @i_tunes_blocked.setter
    def i_tunes_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the iTunesBlocked property value. Indicates whether or not to block the iTunes app. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the i_tunes_blocked property.
        """
        self._i_tunes_blocked = value
    
    @property
    def keyboard_block_auto_correct(self,) -> Optional[bool]:
        """
        Gets the keyboardBlockAutoCorrect property value. Indicates whether or not to block keyboard auto-correction when the device is in supervised mode (iOS 8.1.3 and later).
        Returns: Optional[bool]
        """
        return self._keyboard_block_auto_correct
    
    @keyboard_block_auto_correct.setter
    def keyboard_block_auto_correct(self,value: Optional[bool] = None) -> None:
        """
        Sets the keyboardBlockAutoCorrect property value. Indicates whether or not to block keyboard auto-correction when the device is in supervised mode (iOS 8.1.3 and later).
        Args:
            value: Value to set for the keyboard_block_auto_correct property.
        """
        self._keyboard_block_auto_correct = value
    
    @property
    def keyboard_block_dictation(self,) -> Optional[bool]:
        """
        Gets the keyboardBlockDictation property value. Indicates whether or not to block the user from using dictation input when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._keyboard_block_dictation
    
    @keyboard_block_dictation.setter
    def keyboard_block_dictation(self,value: Optional[bool] = None) -> None:
        """
        Sets the keyboardBlockDictation property value. Indicates whether or not to block the user from using dictation input when the device is in supervised mode.
        Args:
            value: Value to set for the keyboard_block_dictation property.
        """
        self._keyboard_block_dictation = value
    
    @property
    def keyboard_block_predictive(self,) -> Optional[bool]:
        """
        Gets the keyboardBlockPredictive property value. Indicates whether or not to block predictive keyboards when device is in supervised mode (iOS 8.1.3 and later).
        Returns: Optional[bool]
        """
        return self._keyboard_block_predictive
    
    @keyboard_block_predictive.setter
    def keyboard_block_predictive(self,value: Optional[bool] = None) -> None:
        """
        Sets the keyboardBlockPredictive property value. Indicates whether or not to block predictive keyboards when device is in supervised mode (iOS 8.1.3 and later).
        Args:
            value: Value to set for the keyboard_block_predictive property.
        """
        self._keyboard_block_predictive = value
    
    @property
    def keyboard_block_shortcuts(self,) -> Optional[bool]:
        """
        Gets the keyboardBlockShortcuts property value. Indicates whether or not to block keyboard shortcuts when the device is in supervised mode (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._keyboard_block_shortcuts
    
    @keyboard_block_shortcuts.setter
    def keyboard_block_shortcuts(self,value: Optional[bool] = None) -> None:
        """
        Sets the keyboardBlockShortcuts property value. Indicates whether or not to block keyboard shortcuts when the device is in supervised mode (iOS 9.0 and later).
        Args:
            value: Value to set for the keyboard_block_shortcuts property.
        """
        self._keyboard_block_shortcuts = value
    
    @property
    def keyboard_block_spell_check(self,) -> Optional[bool]:
        """
        Gets the keyboardBlockSpellCheck property value. Indicates whether or not to block keyboard spell-checking when the device is in supervised mode (iOS 8.1.3 and later).
        Returns: Optional[bool]
        """
        return self._keyboard_block_spell_check
    
    @keyboard_block_spell_check.setter
    def keyboard_block_spell_check(self,value: Optional[bool] = None) -> None:
        """
        Sets the keyboardBlockSpellCheck property value. Indicates whether or not to block keyboard spell-checking when the device is in supervised mode (iOS 8.1.3 and later).
        Args:
            value: Value to set for the keyboard_block_spell_check property.
        """
        self._keyboard_block_spell_check = value
    
    @property
    def keychain_block_cloud_sync(self,) -> Optional[bool]:
        """
        Gets the keychainBlockCloudSync property value. Indicates whether or not iCloud keychain synchronization is blocked. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._keychain_block_cloud_sync
    
    @keychain_block_cloud_sync.setter
    def keychain_block_cloud_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the keychainBlockCloudSync property value. Indicates whether or not iCloud keychain synchronization is blocked. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the keychain_block_cloud_sync property.
        """
        self._keychain_block_cloud_sync = value
    
    @property
    def kiosk_mode_allow_assistive_speak(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowAssistiveSpeak property value. Indicates whether or not to allow assistive speak while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_assistive_speak
    
    @kiosk_mode_allow_assistive_speak.setter
    def kiosk_mode_allow_assistive_speak(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowAssistiveSpeak property value. Indicates whether or not to allow assistive speak while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_allow_assistive_speak property.
        """
        self._kiosk_mode_allow_assistive_speak = value
    
    @property
    def kiosk_mode_allow_assistive_touch_settings(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowAssistiveTouchSettings property value. Indicates whether or not to allow access to the Assistive Touch Settings while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_assistive_touch_settings
    
    @kiosk_mode_allow_assistive_touch_settings.setter
    def kiosk_mode_allow_assistive_touch_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowAssistiveTouchSettings property value. Indicates whether or not to allow access to the Assistive Touch Settings while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_allow_assistive_touch_settings property.
        """
        self._kiosk_mode_allow_assistive_touch_settings = value
    
    @property
    def kiosk_mode_allow_auto_lock(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowAutoLock property value. Indicates whether or not to allow device auto lock while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockAutoLock instead.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_auto_lock
    
    @kiosk_mode_allow_auto_lock.setter
    def kiosk_mode_allow_auto_lock(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowAutoLock property value. Indicates whether or not to allow device auto lock while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockAutoLock instead.
        Args:
            value: Value to set for the kiosk_mode_allow_auto_lock property.
        """
        self._kiosk_mode_allow_auto_lock = value
    
    @property
    def kiosk_mode_allow_color_inversion_settings(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowColorInversionSettings property value. Indicates whether or not to allow access to the Color Inversion Settings while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_color_inversion_settings
    
    @kiosk_mode_allow_color_inversion_settings.setter
    def kiosk_mode_allow_color_inversion_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowColorInversionSettings property value. Indicates whether or not to allow access to the Color Inversion Settings while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_allow_color_inversion_settings property.
        """
        self._kiosk_mode_allow_color_inversion_settings = value
    
    @property
    def kiosk_mode_allow_ringer_switch(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowRingerSwitch property value. Indicates whether or not to allow use of the ringer switch while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockRingerSwitch instead.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_ringer_switch
    
    @kiosk_mode_allow_ringer_switch.setter
    def kiosk_mode_allow_ringer_switch(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowRingerSwitch property value. Indicates whether or not to allow use of the ringer switch while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockRingerSwitch instead.
        Args:
            value: Value to set for the kiosk_mode_allow_ringer_switch property.
        """
        self._kiosk_mode_allow_ringer_switch = value
    
    @property
    def kiosk_mode_allow_screen_rotation(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowScreenRotation property value. Indicates whether or not to allow screen rotation while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockScreenRotation instead.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_screen_rotation
    
    @kiosk_mode_allow_screen_rotation.setter
    def kiosk_mode_allow_screen_rotation(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowScreenRotation property value. Indicates whether or not to allow screen rotation while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockScreenRotation instead.
        Args:
            value: Value to set for the kiosk_mode_allow_screen_rotation property.
        """
        self._kiosk_mode_allow_screen_rotation = value
    
    @property
    def kiosk_mode_allow_sleep_button(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowSleepButton property value. Indicates whether or not to allow use of the sleep button while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockSleepButton instead.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_sleep_button
    
    @kiosk_mode_allow_sleep_button.setter
    def kiosk_mode_allow_sleep_button(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowSleepButton property value. Indicates whether or not to allow use of the sleep button while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockSleepButton instead.
        Args:
            value: Value to set for the kiosk_mode_allow_sleep_button property.
        """
        self._kiosk_mode_allow_sleep_button = value
    
    @property
    def kiosk_mode_allow_touchscreen(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowTouchscreen property value. Indicates whether or not to allow use of the touchscreen while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockTouchscreen instead.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_touchscreen
    
    @kiosk_mode_allow_touchscreen.setter
    def kiosk_mode_allow_touchscreen(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowTouchscreen property value. Indicates whether or not to allow use of the touchscreen while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockTouchscreen instead.
        Args:
            value: Value to set for the kiosk_mode_allow_touchscreen property.
        """
        self._kiosk_mode_allow_touchscreen = value
    
    @property
    def kiosk_mode_allow_voice_control_modification(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowVoiceControlModification property value. Indicates whether or not to allow the user to toggle voice control in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_voice_control_modification
    
    @kiosk_mode_allow_voice_control_modification.setter
    def kiosk_mode_allow_voice_control_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowVoiceControlModification property value. Indicates whether or not to allow the user to toggle voice control in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_allow_voice_control_modification property.
        """
        self._kiosk_mode_allow_voice_control_modification = value
    
    @property
    def kiosk_mode_allow_voice_over_settings(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowVoiceOverSettings property value. Indicates whether or not to allow access to the voice over settings while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_voice_over_settings
    
    @kiosk_mode_allow_voice_over_settings.setter
    def kiosk_mode_allow_voice_over_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowVoiceOverSettings property value. Indicates whether or not to allow access to the voice over settings while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_allow_voice_over_settings property.
        """
        self._kiosk_mode_allow_voice_over_settings = value
    
    @property
    def kiosk_mode_allow_volume_buttons(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowVolumeButtons property value. Indicates whether or not to allow use of the volume buttons while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockVolumeButtons instead.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_volume_buttons
    
    @kiosk_mode_allow_volume_buttons.setter
    def kiosk_mode_allow_volume_buttons(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowVolumeButtons property value. Indicates whether or not to allow use of the volume buttons while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockVolumeButtons instead.
        Args:
            value: Value to set for the kiosk_mode_allow_volume_buttons property.
        """
        self._kiosk_mode_allow_volume_buttons = value
    
    @property
    def kiosk_mode_allow_zoom_settings(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowZoomSettings property value. Indicates whether or not to allow access to the zoom settings while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_zoom_settings
    
    @kiosk_mode_allow_zoom_settings.setter
    def kiosk_mode_allow_zoom_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowZoomSettings property value. Indicates whether or not to allow access to the zoom settings while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_allow_zoom_settings property.
        """
        self._kiosk_mode_allow_zoom_settings = value
    
    @property
    def kiosk_mode_app_store_url(self,) -> Optional[str]:
        """
        Gets the kioskModeAppStoreUrl property value. URL in the app store to the app to use for kiosk mode. Use if KioskModeManagedAppId is not known.
        Returns: Optional[str]
        """
        return self._kiosk_mode_app_store_url
    
    @kiosk_mode_app_store_url.setter
    def kiosk_mode_app_store_url(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskModeAppStoreUrl property value. URL in the app store to the app to use for kiosk mode. Use if KioskModeManagedAppId is not known.
        Args:
            value: Value to set for the kiosk_mode_app_store_url property.
        """
        self._kiosk_mode_app_store_url = value
    
    @property
    def kiosk_mode_app_type(self,) -> Optional[ios_kiosk_mode_app_type.IosKioskModeAppType]:
        """
        Gets the kioskModeAppType property value. App source options for iOS kiosk mode.
        Returns: Optional[ios_kiosk_mode_app_type.IosKioskModeAppType]
        """
        return self._kiosk_mode_app_type
    
    @kiosk_mode_app_type.setter
    def kiosk_mode_app_type(self,value: Optional[ios_kiosk_mode_app_type.IosKioskModeAppType] = None) -> None:
        """
        Sets the kioskModeAppType property value. App source options for iOS kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_app_type property.
        """
        self._kiosk_mode_app_type = value
    
    @property
    def kiosk_mode_block_auto_lock(self,) -> Optional[bool]:
        """
        Gets the kioskModeBlockAutoLock property value. Indicates whether or not to block device auto lock while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_block_auto_lock
    
    @kiosk_mode_block_auto_lock.setter
    def kiosk_mode_block_auto_lock(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeBlockAutoLock property value. Indicates whether or not to block device auto lock while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_block_auto_lock property.
        """
        self._kiosk_mode_block_auto_lock = value
    
    @property
    def kiosk_mode_block_ringer_switch(self,) -> Optional[bool]:
        """
        Gets the kioskModeBlockRingerSwitch property value. Indicates whether or not to block use of the ringer switch while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_block_ringer_switch
    
    @kiosk_mode_block_ringer_switch.setter
    def kiosk_mode_block_ringer_switch(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeBlockRingerSwitch property value. Indicates whether or not to block use of the ringer switch while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_block_ringer_switch property.
        """
        self._kiosk_mode_block_ringer_switch = value
    
    @property
    def kiosk_mode_block_screen_rotation(self,) -> Optional[bool]:
        """
        Gets the kioskModeBlockScreenRotation property value. Indicates whether or not to block screen rotation while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_block_screen_rotation
    
    @kiosk_mode_block_screen_rotation.setter
    def kiosk_mode_block_screen_rotation(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeBlockScreenRotation property value. Indicates whether or not to block screen rotation while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_block_screen_rotation property.
        """
        self._kiosk_mode_block_screen_rotation = value
    
    @property
    def kiosk_mode_block_sleep_button(self,) -> Optional[bool]:
        """
        Gets the kioskModeBlockSleepButton property value. Indicates whether or not to block use of the sleep button while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_block_sleep_button
    
    @kiosk_mode_block_sleep_button.setter
    def kiosk_mode_block_sleep_button(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeBlockSleepButton property value. Indicates whether or not to block use of the sleep button while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_block_sleep_button property.
        """
        self._kiosk_mode_block_sleep_button = value
    
    @property
    def kiosk_mode_block_touchscreen(self,) -> Optional[bool]:
        """
        Gets the kioskModeBlockTouchscreen property value. Indicates whether or not to block use of the touchscreen while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_block_touchscreen
    
    @kiosk_mode_block_touchscreen.setter
    def kiosk_mode_block_touchscreen(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeBlockTouchscreen property value. Indicates whether or not to block use of the touchscreen while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_block_touchscreen property.
        """
        self._kiosk_mode_block_touchscreen = value
    
    @property
    def kiosk_mode_block_volume_buttons(self,) -> Optional[bool]:
        """
        Gets the kioskModeBlockVolumeButtons property value. Indicates whether or not to block the volume buttons while in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_block_volume_buttons
    
    @kiosk_mode_block_volume_buttons.setter
    def kiosk_mode_block_volume_buttons(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeBlockVolumeButtons property value. Indicates whether or not to block the volume buttons while in Kiosk Mode.
        Args:
            value: Value to set for the kiosk_mode_block_volume_buttons property.
        """
        self._kiosk_mode_block_volume_buttons = value
    
    @property
    def kiosk_mode_built_in_app_id(self,) -> Optional[str]:
        """
        Gets the kioskModeBuiltInAppId property value. ID for built-in apps to use for kiosk mode. Used when KioskModeManagedAppId and KioskModeAppStoreUrl are not set.
        Returns: Optional[str]
        """
        return self._kiosk_mode_built_in_app_id
    
    @kiosk_mode_built_in_app_id.setter
    def kiosk_mode_built_in_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskModeBuiltInAppId property value. ID for built-in apps to use for kiosk mode. Used when KioskModeManagedAppId and KioskModeAppStoreUrl are not set.
        Args:
            value: Value to set for the kiosk_mode_built_in_app_id property.
        """
        self._kiosk_mode_built_in_app_id = value
    
    @property
    def kiosk_mode_enable_voice_control(self,) -> Optional[bool]:
        """
        Gets the kioskModeEnableVoiceControl property value. Indicates whether or not to enable voice control in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_enable_voice_control
    
    @kiosk_mode_enable_voice_control.setter
    def kiosk_mode_enable_voice_control(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeEnableVoiceControl property value. Indicates whether or not to enable voice control in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_enable_voice_control property.
        """
        self._kiosk_mode_enable_voice_control = value
    
    @property
    def kiosk_mode_managed_app_id(self,) -> Optional[str]:
        """
        Gets the kioskModeManagedAppId property value. Managed app id of the app to use for kiosk mode. If KioskModeManagedAppId is specified then KioskModeAppStoreUrl will be ignored.
        Returns: Optional[str]
        """
        return self._kiosk_mode_managed_app_id
    
    @kiosk_mode_managed_app_id.setter
    def kiosk_mode_managed_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskModeManagedAppId property value. Managed app id of the app to use for kiosk mode. If KioskModeManagedAppId is specified then KioskModeAppStoreUrl will be ignored.
        Args:
            value: Value to set for the kiosk_mode_managed_app_id property.
        """
        self._kiosk_mode_managed_app_id = value
    
    @property
    def kiosk_mode_require_assistive_touch(self,) -> Optional[bool]:
        """
        Gets the kioskModeRequireAssistiveTouch property value. Indicates whether or not to require assistive touch while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_require_assistive_touch
    
    @kiosk_mode_require_assistive_touch.setter
    def kiosk_mode_require_assistive_touch(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeRequireAssistiveTouch property value. Indicates whether or not to require assistive touch while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_require_assistive_touch property.
        """
        self._kiosk_mode_require_assistive_touch = value
    
    @property
    def kiosk_mode_require_color_inversion(self,) -> Optional[bool]:
        """
        Gets the kioskModeRequireColorInversion property value. Indicates whether or not to require color inversion while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_require_color_inversion
    
    @kiosk_mode_require_color_inversion.setter
    def kiosk_mode_require_color_inversion(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeRequireColorInversion property value. Indicates whether or not to require color inversion while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_require_color_inversion property.
        """
        self._kiosk_mode_require_color_inversion = value
    
    @property
    def kiosk_mode_require_mono_audio(self,) -> Optional[bool]:
        """
        Gets the kioskModeRequireMonoAudio property value. Indicates whether or not to require mono audio while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_require_mono_audio
    
    @kiosk_mode_require_mono_audio.setter
    def kiosk_mode_require_mono_audio(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeRequireMonoAudio property value. Indicates whether or not to require mono audio while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_require_mono_audio property.
        """
        self._kiosk_mode_require_mono_audio = value
    
    @property
    def kiosk_mode_require_voice_over(self,) -> Optional[bool]:
        """
        Gets the kioskModeRequireVoiceOver property value. Indicates whether or not to require voice over while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_require_voice_over
    
    @kiosk_mode_require_voice_over.setter
    def kiosk_mode_require_voice_over(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeRequireVoiceOver property value. Indicates whether or not to require voice over while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_require_voice_over property.
        """
        self._kiosk_mode_require_voice_over = value
    
    @property
    def kiosk_mode_require_zoom(self,) -> Optional[bool]:
        """
        Gets the kioskModeRequireZoom property value. Indicates whether or not to require zoom while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_require_zoom
    
    @kiosk_mode_require_zoom.setter
    def kiosk_mode_require_zoom(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeRequireZoom property value. Indicates whether or not to require zoom while in kiosk mode.
        Args:
            value: Value to set for the kiosk_mode_require_zoom property.
        """
        self._kiosk_mode_require_zoom = value
    
    @property
    def lock_screen_block_control_center(self,) -> Optional[bool]:
        """
        Gets the lockScreenBlockControlCenter property value. Indicates whether or not to block the user from using control center on the lock screen.
        Returns: Optional[bool]
        """
        return self._lock_screen_block_control_center
    
    @lock_screen_block_control_center.setter
    def lock_screen_block_control_center(self,value: Optional[bool] = None) -> None:
        """
        Sets the lockScreenBlockControlCenter property value. Indicates whether or not to block the user from using control center on the lock screen.
        Args:
            value: Value to set for the lock_screen_block_control_center property.
        """
        self._lock_screen_block_control_center = value
    
    @property
    def lock_screen_block_notification_view(self,) -> Optional[bool]:
        """
        Gets the lockScreenBlockNotificationView property value. Indicates whether or not to block the user from using the notification view on the lock screen.
        Returns: Optional[bool]
        """
        return self._lock_screen_block_notification_view
    
    @lock_screen_block_notification_view.setter
    def lock_screen_block_notification_view(self,value: Optional[bool] = None) -> None:
        """
        Sets the lockScreenBlockNotificationView property value. Indicates whether or not to block the user from using the notification view on the lock screen.
        Args:
            value: Value to set for the lock_screen_block_notification_view property.
        """
        self._lock_screen_block_notification_view = value
    
    @property
    def lock_screen_block_passbook(self,) -> Optional[bool]:
        """
        Gets the lockScreenBlockPassbook property value. Indicates whether or not to block the user from using passbook when the device is locked.
        Returns: Optional[bool]
        """
        return self._lock_screen_block_passbook
    
    @lock_screen_block_passbook.setter
    def lock_screen_block_passbook(self,value: Optional[bool] = None) -> None:
        """
        Sets the lockScreenBlockPassbook property value. Indicates whether or not to block the user from using passbook when the device is locked.
        Args:
            value: Value to set for the lock_screen_block_passbook property.
        """
        self._lock_screen_block_passbook = value
    
    @property
    def lock_screen_block_today_view(self,) -> Optional[bool]:
        """
        Gets the lockScreenBlockTodayView property value. Indicates whether or not to block the user from using the Today View on the lock screen.
        Returns: Optional[bool]
        """
        return self._lock_screen_block_today_view
    
    @lock_screen_block_today_view.setter
    def lock_screen_block_today_view(self,value: Optional[bool] = None) -> None:
        """
        Sets the lockScreenBlockTodayView property value. Indicates whether or not to block the user from using the Today View on the lock screen.
        Args:
            value: Value to set for the lock_screen_block_today_view property.
        """
        self._lock_screen_block_today_view = value
    
    @property
    def managed_pasteboard_required(self,) -> Optional[bool]:
        """
        Gets the managedPasteboardRequired property value. Open-in management controls how people share data between unmanaged and managed apps. Setting this to true enforces copy/paste restrictions based on how you configured Block viewing corporate documents in unmanaged apps  and  Block viewing non-corporate documents in corporate apps.
        Returns: Optional[bool]
        """
        return self._managed_pasteboard_required
    
    @managed_pasteboard_required.setter
    def managed_pasteboard_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the managedPasteboardRequired property value. Open-in management controls how people share data between unmanaged and managed apps. Setting this to true enforces copy/paste restrictions based on how you configured Block viewing corporate documents in unmanaged apps  and  Block viewing non-corporate documents in corporate apps.
        Args:
            value: Value to set for the managed_pasteboard_required property.
        """
        self._managed_pasteboard_required = value
    
    @property
    def media_content_rating_apps(self,) -> Optional[rating_apps_type.RatingAppsType]:
        """
        Gets the mediaContentRatingApps property value. Apps rating as in media content
        Returns: Optional[rating_apps_type.RatingAppsType]
        """
        return self._media_content_rating_apps
    
    @media_content_rating_apps.setter
    def media_content_rating_apps(self,value: Optional[rating_apps_type.RatingAppsType] = None) -> None:
        """
        Sets the mediaContentRatingApps property value. Apps rating as in media content
        Args:
            value: Value to set for the media_content_rating_apps property.
        """
        self._media_content_rating_apps = value
    
    @property
    def media_content_rating_australia(self,) -> Optional[media_content_rating_australia.MediaContentRatingAustralia]:
        """
        Gets the mediaContentRatingAustralia property value. Media content rating settings for Australia
        Returns: Optional[media_content_rating_australia.MediaContentRatingAustralia]
        """
        return self._media_content_rating_australia
    
    @media_content_rating_australia.setter
    def media_content_rating_australia(self,value: Optional[media_content_rating_australia.MediaContentRatingAustralia] = None) -> None:
        """
        Sets the mediaContentRatingAustralia property value. Media content rating settings for Australia
        Args:
            value: Value to set for the media_content_rating_australia property.
        """
        self._media_content_rating_australia = value
    
    @property
    def media_content_rating_canada(self,) -> Optional[media_content_rating_canada.MediaContentRatingCanada]:
        """
        Gets the mediaContentRatingCanada property value. Media content rating settings for Canada
        Returns: Optional[media_content_rating_canada.MediaContentRatingCanada]
        """
        return self._media_content_rating_canada
    
    @media_content_rating_canada.setter
    def media_content_rating_canada(self,value: Optional[media_content_rating_canada.MediaContentRatingCanada] = None) -> None:
        """
        Sets the mediaContentRatingCanada property value. Media content rating settings for Canada
        Args:
            value: Value to set for the media_content_rating_canada property.
        """
        self._media_content_rating_canada = value
    
    @property
    def media_content_rating_france(self,) -> Optional[media_content_rating_france.MediaContentRatingFrance]:
        """
        Gets the mediaContentRatingFrance property value. Media content rating settings for France
        Returns: Optional[media_content_rating_france.MediaContentRatingFrance]
        """
        return self._media_content_rating_france
    
    @media_content_rating_france.setter
    def media_content_rating_france(self,value: Optional[media_content_rating_france.MediaContentRatingFrance] = None) -> None:
        """
        Sets the mediaContentRatingFrance property value. Media content rating settings for France
        Args:
            value: Value to set for the media_content_rating_france property.
        """
        self._media_content_rating_france = value
    
    @property
    def media_content_rating_germany(self,) -> Optional[media_content_rating_germany.MediaContentRatingGermany]:
        """
        Gets the mediaContentRatingGermany property value. Media content rating settings for Germany
        Returns: Optional[media_content_rating_germany.MediaContentRatingGermany]
        """
        return self._media_content_rating_germany
    
    @media_content_rating_germany.setter
    def media_content_rating_germany(self,value: Optional[media_content_rating_germany.MediaContentRatingGermany] = None) -> None:
        """
        Sets the mediaContentRatingGermany property value. Media content rating settings for Germany
        Args:
            value: Value to set for the media_content_rating_germany property.
        """
        self._media_content_rating_germany = value
    
    @property
    def media_content_rating_ireland(self,) -> Optional[media_content_rating_ireland.MediaContentRatingIreland]:
        """
        Gets the mediaContentRatingIreland property value. Media content rating settings for Ireland
        Returns: Optional[media_content_rating_ireland.MediaContentRatingIreland]
        """
        return self._media_content_rating_ireland
    
    @media_content_rating_ireland.setter
    def media_content_rating_ireland(self,value: Optional[media_content_rating_ireland.MediaContentRatingIreland] = None) -> None:
        """
        Sets the mediaContentRatingIreland property value. Media content rating settings for Ireland
        Args:
            value: Value to set for the media_content_rating_ireland property.
        """
        self._media_content_rating_ireland = value
    
    @property
    def media_content_rating_japan(self,) -> Optional[media_content_rating_japan.MediaContentRatingJapan]:
        """
        Gets the mediaContentRatingJapan property value. Media content rating settings for Japan
        Returns: Optional[media_content_rating_japan.MediaContentRatingJapan]
        """
        return self._media_content_rating_japan
    
    @media_content_rating_japan.setter
    def media_content_rating_japan(self,value: Optional[media_content_rating_japan.MediaContentRatingJapan] = None) -> None:
        """
        Sets the mediaContentRatingJapan property value. Media content rating settings for Japan
        Args:
            value: Value to set for the media_content_rating_japan property.
        """
        self._media_content_rating_japan = value
    
    @property
    def media_content_rating_new_zealand(self,) -> Optional[media_content_rating_new_zealand.MediaContentRatingNewZealand]:
        """
        Gets the mediaContentRatingNewZealand property value. Media content rating settings for New Zealand
        Returns: Optional[media_content_rating_new_zealand.MediaContentRatingNewZealand]
        """
        return self._media_content_rating_new_zealand
    
    @media_content_rating_new_zealand.setter
    def media_content_rating_new_zealand(self,value: Optional[media_content_rating_new_zealand.MediaContentRatingNewZealand] = None) -> None:
        """
        Sets the mediaContentRatingNewZealand property value. Media content rating settings for New Zealand
        Args:
            value: Value to set for the media_content_rating_new_zealand property.
        """
        self._media_content_rating_new_zealand = value
    
    @property
    def media_content_rating_united_kingdom(self,) -> Optional[media_content_rating_united_kingdom.MediaContentRatingUnitedKingdom]:
        """
        Gets the mediaContentRatingUnitedKingdom property value. Media content rating settings for United Kingdom
        Returns: Optional[media_content_rating_united_kingdom.MediaContentRatingUnitedKingdom]
        """
        return self._media_content_rating_united_kingdom
    
    @media_content_rating_united_kingdom.setter
    def media_content_rating_united_kingdom(self,value: Optional[media_content_rating_united_kingdom.MediaContentRatingUnitedKingdom] = None) -> None:
        """
        Sets the mediaContentRatingUnitedKingdom property value. Media content rating settings for United Kingdom
        Args:
            value: Value to set for the media_content_rating_united_kingdom property.
        """
        self._media_content_rating_united_kingdom = value
    
    @property
    def media_content_rating_united_states(self,) -> Optional[media_content_rating_united_states.MediaContentRatingUnitedStates]:
        """
        Gets the mediaContentRatingUnitedStates property value. Media content rating settings for United States
        Returns: Optional[media_content_rating_united_states.MediaContentRatingUnitedStates]
        """
        return self._media_content_rating_united_states
    
    @media_content_rating_united_states.setter
    def media_content_rating_united_states(self,value: Optional[media_content_rating_united_states.MediaContentRatingUnitedStates] = None) -> None:
        """
        Sets the mediaContentRatingUnitedStates property value. Media content rating settings for United States
        Args:
            value: Value to set for the media_content_rating_united_states property.
        """
        self._media_content_rating_united_states = value
    
    @property
    def messages_blocked(self,) -> Optional[bool]:
        """
        Gets the messagesBlocked property value. Indicates whether or not to block the user from using the Messages app on the supervised device.
        Returns: Optional[bool]
        """
        return self._messages_blocked
    
    @messages_blocked.setter
    def messages_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the messagesBlocked property value. Indicates whether or not to block the user from using the Messages app on the supervised device.
        Args:
            value: Value to set for the messages_blocked property.
        """
        self._messages_blocked = value
    
    @property
    def network_usage_rules(self,) -> Optional[List[ios_network_usage_rule.IosNetworkUsageRule]]:
        """
        Gets the networkUsageRules property value. List of managed apps and the network rules that applies to them. This collection can contain a maximum of 1000 elements.
        Returns: Optional[List[ios_network_usage_rule.IosNetworkUsageRule]]
        """
        return self._network_usage_rules
    
    @network_usage_rules.setter
    def network_usage_rules(self,value: Optional[List[ios_network_usage_rule.IosNetworkUsageRule]] = None) -> None:
        """
        Sets the networkUsageRules property value. List of managed apps and the network rules that applies to them. This collection can contain a maximum of 1000 elements.
        Args:
            value: Value to set for the network_usage_rules property.
        """
        self._network_usage_rules = value
    
    @property
    def nfc_blocked(self,) -> Optional[bool]:
        """
        Gets the nfcBlocked property value. Disable NFC to prevent devices from pairing with other NFC-enabled devices. Available for iOS/iPadOS devices running 14.2 and later.
        Returns: Optional[bool]
        """
        return self._nfc_blocked
    
    @nfc_blocked.setter
    def nfc_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the nfcBlocked property value. Disable NFC to prevent devices from pairing with other NFC-enabled devices. Available for iOS/iPadOS devices running 14.2 and later.
        Args:
            value: Value to set for the nfc_blocked property.
        """
        self._nfc_blocked = value
    
    @property
    def notifications_block_settings_modification(self,) -> Optional[bool]:
        """
        Gets the notificationsBlockSettingsModification property value. Indicates whether or not to allow notifications settings modification (iOS 9.3 and later).
        Returns: Optional[bool]
        """
        return self._notifications_block_settings_modification
    
    @notifications_block_settings_modification.setter
    def notifications_block_settings_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the notificationsBlockSettingsModification property value. Indicates whether or not to allow notifications settings modification (iOS 9.3 and later).
        Args:
            value: Value to set for the notifications_block_settings_modification property.
        """
        self._notifications_block_settings_modification = value
    
    @property
    def on_device_only_dictation_forced(self,) -> Optional[bool]:
        """
        Gets the onDeviceOnlyDictationForced property value. Disables connections to Siri servers so that users can’t use Siri to dictate text. Available for devices running iOS and iPadOS versions 14.5 and later.
        Returns: Optional[bool]
        """
        return self._on_device_only_dictation_forced
    
    @on_device_only_dictation_forced.setter
    def on_device_only_dictation_forced(self,value: Optional[bool] = None) -> None:
        """
        Sets the onDeviceOnlyDictationForced property value. Disables connections to Siri servers so that users can’t use Siri to dictate text. Available for devices running iOS and iPadOS versions 14.5 and later.
        Args:
            value: Value to set for the on_device_only_dictation_forced property.
        """
        self._on_device_only_dictation_forced = value
    
    @property
    def on_device_only_translation_forced(self,) -> Optional[bool]:
        """
        Gets the onDeviceOnlyTranslationForced property value. When set to TRUE, the setting disables connections to Siri servers so that users can’t use Siri to translate text. When set to FALSE, the setting allows connections to to Siri servers to users can use Siri to translate text. Available for devices running iOS and iPadOS versions 15.0 and later.
        Returns: Optional[bool]
        """
        return self._on_device_only_translation_forced
    
    @on_device_only_translation_forced.setter
    def on_device_only_translation_forced(self,value: Optional[bool] = None) -> None:
        """
        Sets the onDeviceOnlyTranslationForced property value. When set to TRUE, the setting disables connections to Siri servers so that users can’t use Siri to translate text. When set to FALSE, the setting allows connections to to Siri servers to users can use Siri to translate text. Available for devices running iOS and iPadOS versions 15.0 and later.
        Args:
            value: Value to set for the on_device_only_translation_forced property.
        """
        self._on_device_only_translation_forced = value
    
    @property
    def passcode_block_fingerprint_modification(self,) -> Optional[bool]:
        """
        Gets the passcodeBlockFingerprintModification property value. Block modification of registered Touch ID fingerprints when in supervised mode.
        Returns: Optional[bool]
        """
        return self._passcode_block_fingerprint_modification
    
    @passcode_block_fingerprint_modification.setter
    def passcode_block_fingerprint_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the passcodeBlockFingerprintModification property value. Block modification of registered Touch ID fingerprints when in supervised mode.
        Args:
            value: Value to set for the passcode_block_fingerprint_modification property.
        """
        self._passcode_block_fingerprint_modification = value
    
    @property
    def passcode_block_fingerprint_unlock(self,) -> Optional[bool]:
        """
        Gets the passcodeBlockFingerprintUnlock property value. Indicates whether or not to block fingerprint unlock.
        Returns: Optional[bool]
        """
        return self._passcode_block_fingerprint_unlock
    
    @passcode_block_fingerprint_unlock.setter
    def passcode_block_fingerprint_unlock(self,value: Optional[bool] = None) -> None:
        """
        Sets the passcodeBlockFingerprintUnlock property value. Indicates whether or not to block fingerprint unlock.
        Args:
            value: Value to set for the passcode_block_fingerprint_unlock property.
        """
        self._passcode_block_fingerprint_unlock = value
    
    @property
    def passcode_block_modification(self,) -> Optional[bool]:
        """
        Gets the passcodeBlockModification property value. Indicates whether or not to allow passcode modification on the supervised device (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._passcode_block_modification
    
    @passcode_block_modification.setter
    def passcode_block_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the passcodeBlockModification property value. Indicates whether or not to allow passcode modification on the supervised device (iOS 9.0 and later).
        Args:
            value: Value to set for the passcode_block_modification property.
        """
        self._passcode_block_modification = value
    
    @property
    def passcode_block_simple(self,) -> Optional[bool]:
        """
        Gets the passcodeBlockSimple property value. Indicates whether or not to block simple passcodes.
        Returns: Optional[bool]
        """
        return self._passcode_block_simple
    
    @passcode_block_simple.setter
    def passcode_block_simple(self,value: Optional[bool] = None) -> None:
        """
        Sets the passcodeBlockSimple property value. Indicates whether or not to block simple passcodes.
        Args:
            value: Value to set for the passcode_block_simple property.
        """
        self._passcode_block_simple = value
    
    @property
    def passcode_expiration_days(self,) -> Optional[int]:
        """
        Gets the passcodeExpirationDays property value. Number of days before the passcode expires. Valid values 1 to 65535
        Returns: Optional[int]
        """
        return self._passcode_expiration_days
    
    @passcode_expiration_days.setter
    def passcode_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeExpirationDays property value. Number of days before the passcode expires. Valid values 1 to 65535
        Args:
            value: Value to set for the passcode_expiration_days property.
        """
        self._passcode_expiration_days = value
    
    @property
    def passcode_minimum_character_set_count(self,) -> Optional[int]:
        """
        Gets the passcodeMinimumCharacterSetCount property value. Number of character sets a passcode must contain. Valid values 0 to 4
        Returns: Optional[int]
        """
        return self._passcode_minimum_character_set_count
    
    @passcode_minimum_character_set_count.setter
    def passcode_minimum_character_set_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeMinimumCharacterSetCount property value. Number of character sets a passcode must contain. Valid values 0 to 4
        Args:
            value: Value to set for the passcode_minimum_character_set_count property.
        """
        self._passcode_minimum_character_set_count = value
    
    @property
    def passcode_minimum_length(self,) -> Optional[int]:
        """
        Gets the passcodeMinimumLength property value. Minimum length of passcode. Valid values 4 to 14
        Returns: Optional[int]
        """
        return self._passcode_minimum_length
    
    @passcode_minimum_length.setter
    def passcode_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeMinimumLength property value. Minimum length of passcode. Valid values 4 to 14
        Args:
            value: Value to set for the passcode_minimum_length property.
        """
        self._passcode_minimum_length = value
    
    @property
    def passcode_minutes_of_inactivity_before_lock(self,) -> Optional[int]:
        """
        Gets the passcodeMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a passcode is required.
        Returns: Optional[int]
        """
        return self._passcode_minutes_of_inactivity_before_lock
    
    @passcode_minutes_of_inactivity_before_lock.setter
    def passcode_minutes_of_inactivity_before_lock(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a passcode is required.
        Args:
            value: Value to set for the passcode_minutes_of_inactivity_before_lock property.
        """
        self._passcode_minutes_of_inactivity_before_lock = value
    
    @property
    def passcode_minutes_of_inactivity_before_screen_timeout(self,) -> Optional[int]:
        """
        Gets the passcodeMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity before the screen times out.
        Returns: Optional[int]
        """
        return self._passcode_minutes_of_inactivity_before_screen_timeout
    
    @passcode_minutes_of_inactivity_before_screen_timeout.setter
    def passcode_minutes_of_inactivity_before_screen_timeout(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity before the screen times out.
        Args:
            value: Value to set for the passcode_minutes_of_inactivity_before_screen_timeout property.
        """
        self._passcode_minutes_of_inactivity_before_screen_timeout = value
    
    @property
    def passcode_previous_passcode_block_count(self,) -> Optional[int]:
        """
        Gets the passcodePreviousPasscodeBlockCount property value. Number of previous passcodes to block. Valid values 1 to 24
        Returns: Optional[int]
        """
        return self._passcode_previous_passcode_block_count
    
    @passcode_previous_passcode_block_count.setter
    def passcode_previous_passcode_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodePreviousPasscodeBlockCount property value. Number of previous passcodes to block. Valid values 1 to 24
        Args:
            value: Value to set for the passcode_previous_passcode_block_count property.
        """
        self._passcode_previous_passcode_block_count = value
    
    @property
    def passcode_required(self,) -> Optional[bool]:
        """
        Gets the passcodeRequired property value. Indicates whether or not to require a passcode.
        Returns: Optional[bool]
        """
        return self._passcode_required
    
    @passcode_required.setter
    def passcode_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the passcodeRequired property value. Indicates whether or not to require a passcode.
        Args:
            value: Value to set for the passcode_required property.
        """
        self._passcode_required = value
    
    @property
    def passcode_required_type(self,) -> Optional[required_password_type.RequiredPasswordType]:
        """
        Gets the passcodeRequiredType property value. Possible values of required passwords.
        Returns: Optional[required_password_type.RequiredPasswordType]
        """
        return self._passcode_required_type
    
    @passcode_required_type.setter
    def passcode_required_type(self,value: Optional[required_password_type.RequiredPasswordType] = None) -> None:
        """
        Sets the passcodeRequiredType property value. Possible values of required passwords.
        Args:
            value: Value to set for the passcode_required_type property.
        """
        self._passcode_required_type = value
    
    @property
    def passcode_sign_in_failure_count_before_wipe(self,) -> Optional[int]:
        """
        Gets the passcodeSignInFailureCountBeforeWipe property value. Number of sign in failures allowed before wiping the device. Valid values 2 to 11
        Returns: Optional[int]
        """
        return self._passcode_sign_in_failure_count_before_wipe
    
    @passcode_sign_in_failure_count_before_wipe.setter
    def passcode_sign_in_failure_count_before_wipe(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeSignInFailureCountBeforeWipe property value. Number of sign in failures allowed before wiping the device. Valid values 2 to 11
        Args:
            value: Value to set for the passcode_sign_in_failure_count_before_wipe property.
        """
        self._passcode_sign_in_failure_count_before_wipe = value
    
    @property
    def password_block_air_drop_sharing(self,) -> Optional[bool]:
        """
        Gets the passwordBlockAirDropSharing property value. Indicates whether or not to block sharing passwords with the AirDrop passwords feature iOS 12.0 and later).
        Returns: Optional[bool]
        """
        return self._password_block_air_drop_sharing
    
    @password_block_air_drop_sharing.setter
    def password_block_air_drop_sharing(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockAirDropSharing property value. Indicates whether or not to block sharing passwords with the AirDrop passwords feature iOS 12.0 and later).
        Args:
            value: Value to set for the password_block_air_drop_sharing property.
        """
        self._password_block_air_drop_sharing = value
    
    @property
    def password_block_auto_fill(self,) -> Optional[bool]:
        """
        Gets the passwordBlockAutoFill property value. Indicates if the AutoFill passwords feature is allowed (iOS 12.0 and later).
        Returns: Optional[bool]
        """
        return self._password_block_auto_fill
    
    @password_block_auto_fill.setter
    def password_block_auto_fill(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockAutoFill property value. Indicates if the AutoFill passwords feature is allowed (iOS 12.0 and later).
        Args:
            value: Value to set for the password_block_auto_fill property.
        """
        self._password_block_auto_fill = value
    
    @property
    def password_block_proximity_requests(self,) -> Optional[bool]:
        """
        Gets the passwordBlockProximityRequests property value. Indicates whether or not to block requesting passwords from nearby devices (iOS 12.0 and later).
        Returns: Optional[bool]
        """
        return self._password_block_proximity_requests
    
    @password_block_proximity_requests.setter
    def password_block_proximity_requests(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockProximityRequests property value. Indicates whether or not to block requesting passwords from nearby devices (iOS 12.0 and later).
        Args:
            value: Value to set for the password_block_proximity_requests property.
        """
        self._password_block_proximity_requests = value
    
    @property
    def pki_block_o_t_a_updates(self,) -> Optional[bool]:
        """
        Gets the pkiBlockOTAUpdates property value. Indicates whether or not over-the-air PKI updates are blocked. Setting this restriction to false does not disable CRL and OCSP checks (iOS 7.0 and later).
        Returns: Optional[bool]
        """
        return self._pki_block_o_t_a_updates
    
    @pki_block_o_t_a_updates.setter
    def pki_block_o_t_a_updates(self,value: Optional[bool] = None) -> None:
        """
        Sets the pkiBlockOTAUpdates property value. Indicates whether or not over-the-air PKI updates are blocked. Setting this restriction to false does not disable CRL and OCSP checks (iOS 7.0 and later).
        Args:
            value: Value to set for the pki_block_o_t_a_updates property.
        """
        self._pki_block_o_t_a_updates = value
    
    @property
    def podcasts_blocked(self,) -> Optional[bool]:
        """
        Gets the podcastsBlocked property value. Indicates whether or not to block the user from using podcasts on the supervised device (iOS 8.0 and later).
        Returns: Optional[bool]
        """
        return self._podcasts_blocked
    
    @podcasts_blocked.setter
    def podcasts_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the podcastsBlocked property value. Indicates whether or not to block the user from using podcasts on the supervised device (iOS 8.0 and later).
        Args:
            value: Value to set for the podcasts_blocked property.
        """
        self._podcasts_blocked = value
    
    @property
    def privacy_force_limit_ad_tracking(self,) -> Optional[bool]:
        """
        Gets the privacyForceLimitAdTracking property value. Indicates if ad tracking is limited.(iOS 7.0 and later).
        Returns: Optional[bool]
        """
        return self._privacy_force_limit_ad_tracking
    
    @privacy_force_limit_ad_tracking.setter
    def privacy_force_limit_ad_tracking(self,value: Optional[bool] = None) -> None:
        """
        Sets the privacyForceLimitAdTracking property value. Indicates if ad tracking is limited.(iOS 7.0 and later).
        Args:
            value: Value to set for the privacy_force_limit_ad_tracking property.
        """
        self._privacy_force_limit_ad_tracking = value
    
    @property
    def proximity_block_setup_to_new_device(self,) -> Optional[bool]:
        """
        Gets the proximityBlockSetupToNewDevice property value. Indicates whether or not to enable the prompt to setup nearby devices with a supervised device.
        Returns: Optional[bool]
        """
        return self._proximity_block_setup_to_new_device
    
    @proximity_block_setup_to_new_device.setter
    def proximity_block_setup_to_new_device(self,value: Optional[bool] = None) -> None:
        """
        Sets the proximityBlockSetupToNewDevice property value. Indicates whether or not to enable the prompt to setup nearby devices with a supervised device.
        Args:
            value: Value to set for the proximity_block_setup_to_new_device property.
        """
        self._proximity_block_setup_to_new_device = value
    
    @property
    def safari_block_autofill(self,) -> Optional[bool]:
        """
        Gets the safariBlockAutofill property value. Indicates whether or not to block the user from using Auto fill in Safari. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._safari_block_autofill
    
    @safari_block_autofill.setter
    def safari_block_autofill(self,value: Optional[bool] = None) -> None:
        """
        Sets the safariBlockAutofill property value. Indicates whether or not to block the user from using Auto fill in Safari. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the safari_block_autofill property.
        """
        self._safari_block_autofill = value
    
    @property
    def safari_block_java_script(self,) -> Optional[bool]:
        """
        Gets the safariBlockJavaScript property value. Indicates whether or not to block JavaScript in Safari.
        Returns: Optional[bool]
        """
        return self._safari_block_java_script
    
    @safari_block_java_script.setter
    def safari_block_java_script(self,value: Optional[bool] = None) -> None:
        """
        Sets the safariBlockJavaScript property value. Indicates whether or not to block JavaScript in Safari.
        Args:
            value: Value to set for the safari_block_java_script property.
        """
        self._safari_block_java_script = value
    
    @property
    def safari_block_popups(self,) -> Optional[bool]:
        """
        Gets the safariBlockPopups property value. Indicates whether or not to block popups in Safari.
        Returns: Optional[bool]
        """
        return self._safari_block_popups
    
    @safari_block_popups.setter
    def safari_block_popups(self,value: Optional[bool] = None) -> None:
        """
        Sets the safariBlockPopups property value. Indicates whether or not to block popups in Safari.
        Args:
            value: Value to set for the safari_block_popups property.
        """
        self._safari_block_popups = value
    
    @property
    def safari_blocked(self,) -> Optional[bool]:
        """
        Gets the safariBlocked property value. Indicates whether or not to block the user from using Safari. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._safari_blocked
    
    @safari_blocked.setter
    def safari_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the safariBlocked property value. Indicates whether or not to block the user from using Safari. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the safari_blocked property.
        """
        self._safari_blocked = value
    
    @property
    def safari_cookie_settings(self,) -> Optional[web_browser_cookie_settings.WebBrowserCookieSettings]:
        """
        Gets the safariCookieSettings property value. Web Browser Cookie Settings.
        Returns: Optional[web_browser_cookie_settings.WebBrowserCookieSettings]
        """
        return self._safari_cookie_settings
    
    @safari_cookie_settings.setter
    def safari_cookie_settings(self,value: Optional[web_browser_cookie_settings.WebBrowserCookieSettings] = None) -> None:
        """
        Sets the safariCookieSettings property value. Web Browser Cookie Settings.
        Args:
            value: Value to set for the safari_cookie_settings property.
        """
        self._safari_cookie_settings = value
    
    @property
    def safari_managed_domains(self,) -> Optional[List[str]]:
        """
        Gets the safariManagedDomains property value. URLs matching the patterns listed here will be considered managed.
        Returns: Optional[List[str]]
        """
        return self._safari_managed_domains
    
    @safari_managed_domains.setter
    def safari_managed_domains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the safariManagedDomains property value. URLs matching the patterns listed here will be considered managed.
        Args:
            value: Value to set for the safari_managed_domains property.
        """
        self._safari_managed_domains = value
    
    @property
    def safari_password_auto_fill_domains(self,) -> Optional[List[str]]:
        """
        Gets the safariPasswordAutoFillDomains property value. Users can save passwords in Safari only from URLs matching the patterns listed here. Applies to devices in supervised mode (iOS 9.3 and later).
        Returns: Optional[List[str]]
        """
        return self._safari_password_auto_fill_domains
    
    @safari_password_auto_fill_domains.setter
    def safari_password_auto_fill_domains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the safariPasswordAutoFillDomains property value. Users can save passwords in Safari only from URLs matching the patterns listed here. Applies to devices in supervised mode (iOS 9.3 and later).
        Args:
            value: Value to set for the safari_password_auto_fill_domains property.
        """
        self._safari_password_auto_fill_domains = value
    
    @property
    def safari_require_fraud_warning(self,) -> Optional[bool]:
        """
        Gets the safariRequireFraudWarning property value. Indicates whether or not to require fraud warning in Safari.
        Returns: Optional[bool]
        """
        return self._safari_require_fraud_warning
    
    @safari_require_fraud_warning.setter
    def safari_require_fraud_warning(self,value: Optional[bool] = None) -> None:
        """
        Sets the safariRequireFraudWarning property value. Indicates whether or not to require fraud warning in Safari.
        Args:
            value: Value to set for the safari_require_fraud_warning property.
        """
        self._safari_require_fraud_warning = value
    
    @property
    def screen_capture_blocked(self,) -> Optional[bool]:
        """
        Gets the screenCaptureBlocked property value. Indicates whether or not to block the user from taking Screenshots.
        Returns: Optional[bool]
        """
        return self._screen_capture_blocked
    
    @screen_capture_blocked.setter
    def screen_capture_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the screenCaptureBlocked property value. Indicates whether or not to block the user from taking Screenshots.
        Args:
            value: Value to set for the screen_capture_blocked property.
        """
        self._screen_capture_blocked = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("accountBlockModification", self.account_block_modification)
        writer.write_bool_value("activationLockAllowWhenSupervised", self.activation_lock_allow_when_supervised)
        writer.write_bool_value("airDropBlocked", self.air_drop_blocked)
        writer.write_bool_value("airDropForceUnmanagedDropTarget", self.air_drop_force_unmanaged_drop_target)
        writer.write_bool_value("airPlayForcePairingPasswordForOutgoingRequests", self.air_play_force_pairing_password_for_outgoing_requests)
        writer.write_bool_value("airPrintBlocked", self.air_print_blocked)
        writer.write_bool_value("airPrintBlockiBeaconDiscovery", self.air_print_blocki_beacon_discovery)
        writer.write_bool_value("airPrintBlockCredentialsStorage", self.air_print_block_credentials_storage)
        writer.write_bool_value("airPrintForceTrustedTLS", self.air_print_force_trusted_t_l_s)
        writer.write_bool_value("appleNewsBlocked", self.apple_news_blocked)
        writer.write_bool_value("applePersonalizedAdsBlocked", self.apple_personalized_ads_blocked)
        writer.write_bool_value("appleWatchBlockPairing", self.apple_watch_block_pairing)
        writer.write_bool_value("appleWatchForceWristDetection", self.apple_watch_force_wrist_detection)
        writer.write_collection_of_object_values("appsSingleAppModeList", self.apps_single_app_mode_list)
        writer.write_collection_of_object_values("appsVisibilityList", self.apps_visibility_list)
        writer.write_enum_value("appsVisibilityListType", self.apps_visibility_list_type)
        writer.write_bool_value("appClipsBlocked", self.app_clips_blocked)
        writer.write_bool_value("appRemovalBlocked", self.app_removal_blocked)
        writer.write_bool_value("appStoreBlocked", self.app_store_blocked)
        writer.write_bool_value("appStoreBlockAutomaticDownloads", self.app_store_block_automatic_downloads)
        writer.write_bool_value("appStoreBlockInAppPurchases", self.app_store_block_in_app_purchases)
        writer.write_bool_value("appStoreBlockUIAppInstallation", self.app_store_block_u_i_app_installation)
        writer.write_bool_value("appStoreRequirePassword", self.app_store_require_password)
        writer.write_bool_value("autoFillForceAuthentication", self.auto_fill_force_authentication)
        writer.write_bool_value("autoUnlockBlocked", self.auto_unlock_blocked)
        writer.write_bool_value("blockSystemAppRemoval", self.block_system_app_removal)
        writer.write_bool_value("bluetoothBlockModification", self.bluetooth_block_modification)
        writer.write_bool_value("cameraBlocked", self.camera_blocked)
        writer.write_bool_value("cellularBlockDataRoaming", self.cellular_block_data_roaming)
        writer.write_bool_value("cellularBlockGlobalBackgroundFetchWhileRoaming", self.cellular_block_global_background_fetch_while_roaming)
        writer.write_bool_value("cellularBlockPersonalHotspot", self.cellular_block_personal_hotspot)
        writer.write_bool_value("cellularBlockPersonalHotspotModification", self.cellular_block_personal_hotspot_modification)
        writer.write_bool_value("cellularBlockPerAppDataModification", self.cellular_block_per_app_data_modification)
        writer.write_bool_value("cellularBlockPlanModification", self.cellular_block_plan_modification)
        writer.write_bool_value("cellularBlockVoiceRoaming", self.cellular_block_voice_roaming)
        writer.write_bool_value("certificatesBlockUntrustedTlsCertificates", self.certificates_block_untrusted_tls_certificates)
        writer.write_bool_value("classroomAppBlockRemoteScreenObservation", self.classroom_app_block_remote_screen_observation)
        writer.write_bool_value("classroomAppForceUnpromptedScreenObservation", self.classroom_app_force_unprompted_screen_observation)
        writer.write_bool_value("classroomForceAutomaticallyJoinClasses", self.classroom_force_automatically_join_classes)
        writer.write_bool_value("classroomForceRequestPermissionToLeaveClasses", self.classroom_force_request_permission_to_leave_classes)
        writer.write_bool_value("classroomForceUnpromptedAppAndDeviceLock", self.classroom_force_unprompted_app_and_device_lock)
        writer.write_collection_of_object_values("compliantAppsList", self.compliant_apps_list)
        writer.write_enum_value("compliantAppListType", self.compliant_app_list_type)
        writer.write_bool_value("configurationProfileBlockChanges", self.configuration_profile_block_changes)
        writer.write_bool_value("contactsAllowManagedToUnmanagedWrite", self.contacts_allow_managed_to_unmanaged_write)
        writer.write_bool_value("contactsAllowUnmanagedToManagedRead", self.contacts_allow_unmanaged_to_managed_read)
        writer.write_bool_value("continuousPathKeyboardBlocked", self.continuous_path_keyboard_blocked)
        writer.write_bool_value("dateAndTimeForceSetAutomatically", self.date_and_time_force_set_automatically)
        writer.write_bool_value("definitionLookupBlocked", self.definition_lookup_blocked)
        writer.write_bool_value("deviceBlockEnableRestrictions", self.device_block_enable_restrictions)
        writer.write_bool_value("deviceBlockEraseContentAndSettings", self.device_block_erase_content_and_settings)
        writer.write_bool_value("deviceBlockNameModification", self.device_block_name_modification)
        writer.write_bool_value("diagnosticDataBlockSubmission", self.diagnostic_data_block_submission)
        writer.write_bool_value("diagnosticDataBlockSubmissionModification", self.diagnostic_data_block_submission_modification)
        writer.write_bool_value("documentsBlockManagedDocumentsInUnmanagedApps", self.documents_block_managed_documents_in_unmanaged_apps)
        writer.write_bool_value("documentsBlockUnmanagedDocumentsInManagedApps", self.documents_block_unmanaged_documents_in_managed_apps)
        writer.write_collection_of_primitive_values("emailInDomainSuffixes", self.email_in_domain_suffixes)
        writer.write_bool_value("enterpriseAppBlockTrust", self.enterprise_app_block_trust)
        writer.write_bool_value("enterpriseAppBlockTrustModification", self.enterprise_app_block_trust_modification)
        writer.write_bool_value("enterpriseBookBlockBackup", self.enterprise_book_block_backup)
        writer.write_bool_value("enterpriseBookBlockMetadataSync", self.enterprise_book_block_metadata_sync)
        writer.write_bool_value("esimBlockModification", self.esim_block_modification)
        writer.write_bool_value("faceTimeBlocked", self.face_time_blocked)
        writer.write_bool_value("filesNetworkDriveAccessBlocked", self.files_network_drive_access_blocked)
        writer.write_bool_value("filesUsbDriveAccessBlocked", self.files_usb_drive_access_blocked)
        writer.write_bool_value("findMyDeviceInFindMyAppBlocked", self.find_my_device_in_find_my_app_blocked)
        writer.write_bool_value("findMyFriendsBlocked", self.find_my_friends_blocked)
        writer.write_bool_value("findMyFriendsInFindMyAppBlocked", self.find_my_friends_in_find_my_app_blocked)
        writer.write_bool_value("gameCenterBlocked", self.game_center_blocked)
        writer.write_bool_value("gamingBlockGameCenterFriends", self.gaming_block_game_center_friends)
        writer.write_bool_value("gamingBlockMultiplayer", self.gaming_block_multiplayer)
        writer.write_bool_value("hostPairingBlocked", self.host_pairing_blocked)
        writer.write_bool_value("iBooksStoreBlocked", self.i_books_store_blocked)
        writer.write_bool_value("iBooksStoreBlockErotica", self.i_books_store_block_erotica)
        writer.write_bool_value("iCloudBlockActivityContinuation", self.i_cloud_block_activity_continuation)
        writer.write_bool_value("iCloudBlockBackup", self.i_cloud_block_backup)
        writer.write_bool_value("iCloudBlockDocumentSync", self.i_cloud_block_document_sync)
        writer.write_bool_value("iCloudBlockManagedAppsSync", self.i_cloud_block_managed_apps_sync)
        writer.write_bool_value("iCloudBlockPhotoLibrary", self.i_cloud_block_photo_library)
        writer.write_bool_value("iCloudBlockPhotoStreamSync", self.i_cloud_block_photo_stream_sync)
        writer.write_bool_value("iCloudBlockSharedPhotoStream", self.i_cloud_block_shared_photo_stream)
        writer.write_bool_value("iCloudPrivateRelayBlocked", self.i_cloud_private_relay_blocked)
        writer.write_bool_value("iCloudRequireEncryptedBackup", self.i_cloud_require_encrypted_backup)
        writer.write_bool_value("iTunesBlocked", self.i_tunes_blocked)
        writer.write_bool_value("iTunesBlockExplicitContent", self.i_tunes_block_explicit_content)
        writer.write_bool_value("iTunesBlockMusicService", self.i_tunes_block_music_service)
        writer.write_bool_value("iTunesBlockRadio", self.i_tunes_block_radio)
        writer.write_bool_value("keyboardBlockAutoCorrect", self.keyboard_block_auto_correct)
        writer.write_bool_value("keyboardBlockDictation", self.keyboard_block_dictation)
        writer.write_bool_value("keyboardBlockPredictive", self.keyboard_block_predictive)
        writer.write_bool_value("keyboardBlockShortcuts", self.keyboard_block_shortcuts)
        writer.write_bool_value("keyboardBlockSpellCheck", self.keyboard_block_spell_check)
        writer.write_bool_value("keychainBlockCloudSync", self.keychain_block_cloud_sync)
        writer.write_bool_value("kioskModeAllowAssistiveSpeak", self.kiosk_mode_allow_assistive_speak)
        writer.write_bool_value("kioskModeAllowAssistiveTouchSettings", self.kiosk_mode_allow_assistive_touch_settings)
        writer.write_bool_value("kioskModeAllowAutoLock", self.kiosk_mode_allow_auto_lock)
        writer.write_bool_value("kioskModeAllowColorInversionSettings", self.kiosk_mode_allow_color_inversion_settings)
        writer.write_bool_value("kioskModeAllowRingerSwitch", self.kiosk_mode_allow_ringer_switch)
        writer.write_bool_value("kioskModeAllowScreenRotation", self.kiosk_mode_allow_screen_rotation)
        writer.write_bool_value("kioskModeAllowSleepButton", self.kiosk_mode_allow_sleep_button)
        writer.write_bool_value("kioskModeAllowTouchscreen", self.kiosk_mode_allow_touchscreen)
        writer.write_bool_value("kioskModeAllowVoiceControlModification", self.kiosk_mode_allow_voice_control_modification)
        writer.write_bool_value("kioskModeAllowVoiceOverSettings", self.kiosk_mode_allow_voice_over_settings)
        writer.write_bool_value("kioskModeAllowVolumeButtons", self.kiosk_mode_allow_volume_buttons)
        writer.write_bool_value("kioskModeAllowZoomSettings", self.kiosk_mode_allow_zoom_settings)
        writer.write_str_value("kioskModeAppStoreUrl", self.kiosk_mode_app_store_url)
        writer.write_enum_value("kioskModeAppType", self.kiosk_mode_app_type)
        writer.write_bool_value("kioskModeBlockAutoLock", self.kiosk_mode_block_auto_lock)
        writer.write_bool_value("kioskModeBlockRingerSwitch", self.kiosk_mode_block_ringer_switch)
        writer.write_bool_value("kioskModeBlockScreenRotation", self.kiosk_mode_block_screen_rotation)
        writer.write_bool_value("kioskModeBlockSleepButton", self.kiosk_mode_block_sleep_button)
        writer.write_bool_value("kioskModeBlockTouchscreen", self.kiosk_mode_block_touchscreen)
        writer.write_bool_value("kioskModeBlockVolumeButtons", self.kiosk_mode_block_volume_buttons)
        writer.write_str_value("kioskModeBuiltInAppId", self.kiosk_mode_built_in_app_id)
        writer.write_bool_value("kioskModeEnableVoiceControl", self.kiosk_mode_enable_voice_control)
        writer.write_str_value("kioskModeManagedAppId", self.kiosk_mode_managed_app_id)
        writer.write_bool_value("kioskModeRequireAssistiveTouch", self.kiosk_mode_require_assistive_touch)
        writer.write_bool_value("kioskModeRequireColorInversion", self.kiosk_mode_require_color_inversion)
        writer.write_bool_value("kioskModeRequireMonoAudio", self.kiosk_mode_require_mono_audio)
        writer.write_bool_value("kioskModeRequireVoiceOver", self.kiosk_mode_require_voice_over)
        writer.write_bool_value("kioskModeRequireZoom", self.kiosk_mode_require_zoom)
        writer.write_bool_value("lockScreenBlockControlCenter", self.lock_screen_block_control_center)
        writer.write_bool_value("lockScreenBlockNotificationView", self.lock_screen_block_notification_view)
        writer.write_bool_value("lockScreenBlockPassbook", self.lock_screen_block_passbook)
        writer.write_bool_value("lockScreenBlockTodayView", self.lock_screen_block_today_view)
        writer.write_bool_value("managedPasteboardRequired", self.managed_pasteboard_required)
        writer.write_enum_value("mediaContentRatingApps", self.media_content_rating_apps)
        writer.write_object_value("mediaContentRatingAustralia", self.media_content_rating_australia)
        writer.write_object_value("mediaContentRatingCanada", self.media_content_rating_canada)
        writer.write_object_value("mediaContentRatingFrance", self.media_content_rating_france)
        writer.write_object_value("mediaContentRatingGermany", self.media_content_rating_germany)
        writer.write_object_value("mediaContentRatingIreland", self.media_content_rating_ireland)
        writer.write_object_value("mediaContentRatingJapan", self.media_content_rating_japan)
        writer.write_object_value("mediaContentRatingNewZealand", self.media_content_rating_new_zealand)
        writer.write_object_value("mediaContentRatingUnitedKingdom", self.media_content_rating_united_kingdom)
        writer.write_object_value("mediaContentRatingUnitedStates", self.media_content_rating_united_states)
        writer.write_bool_value("messagesBlocked", self.messages_blocked)
        writer.write_collection_of_object_values("networkUsageRules", self.network_usage_rules)
        writer.write_bool_value("nfcBlocked", self.nfc_blocked)
        writer.write_bool_value("notificationsBlockSettingsModification", self.notifications_block_settings_modification)
        writer.write_bool_value("onDeviceOnlyDictationForced", self.on_device_only_dictation_forced)
        writer.write_bool_value("onDeviceOnlyTranslationForced", self.on_device_only_translation_forced)
        writer.write_bool_value("passcodeBlockFingerprintModification", self.passcode_block_fingerprint_modification)
        writer.write_bool_value("passcodeBlockFingerprintUnlock", self.passcode_block_fingerprint_unlock)
        writer.write_bool_value("passcodeBlockModification", self.passcode_block_modification)
        writer.write_bool_value("passcodeBlockSimple", self.passcode_block_simple)
        writer.write_int_value("passcodeExpirationDays", self.passcode_expiration_days)
        writer.write_int_value("passcodeMinimumCharacterSetCount", self.passcode_minimum_character_set_count)
        writer.write_int_value("passcodeMinimumLength", self.passcode_minimum_length)
        writer.write_int_value("passcodeMinutesOfInactivityBeforeLock", self.passcode_minutes_of_inactivity_before_lock)
        writer.write_int_value("passcodeMinutesOfInactivityBeforeScreenTimeout", self.passcode_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("passcodePreviousPasscodeBlockCount", self.passcode_previous_passcode_block_count)
        writer.write_bool_value("passcodeRequired", self.passcode_required)
        writer.write_enum_value("passcodeRequiredType", self.passcode_required_type)
        writer.write_int_value("passcodeSignInFailureCountBeforeWipe", self.passcode_sign_in_failure_count_before_wipe)
        writer.write_bool_value("passwordBlockAirDropSharing", self.password_block_air_drop_sharing)
        writer.write_bool_value("passwordBlockAutoFill", self.password_block_auto_fill)
        writer.write_bool_value("passwordBlockProximityRequests", self.password_block_proximity_requests)
        writer.write_bool_value("pkiBlockOTAUpdates", self.pki_block_o_t_a_updates)
        writer.write_bool_value("podcastsBlocked", self.podcasts_blocked)
        writer.write_bool_value("privacyForceLimitAdTracking", self.privacy_force_limit_ad_tracking)
        writer.write_bool_value("proximityBlockSetupToNewDevice", self.proximity_block_setup_to_new_device)
        writer.write_bool_value("safariBlocked", self.safari_blocked)
        writer.write_bool_value("safariBlockAutofill", self.safari_block_autofill)
        writer.write_bool_value("safariBlockJavaScript", self.safari_block_java_script)
        writer.write_bool_value("safariBlockPopups", self.safari_block_popups)
        writer.write_enum_value("safariCookieSettings", self.safari_cookie_settings)
        writer.write_collection_of_primitive_values("safariManagedDomains", self.safari_managed_domains)
        writer.write_collection_of_primitive_values("safariPasswordAutoFillDomains", self.safari_password_auto_fill_domains)
        writer.write_bool_value("safariRequireFraudWarning", self.safari_require_fraud_warning)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_bool_value("sharedDeviceBlockTemporarySessions", self.shared_device_block_temporary_sessions)
        writer.write_bool_value("siriBlocked", self.siri_blocked)
        writer.write_bool_value("siriBlockedWhenLocked", self.siri_blocked_when_locked)
        writer.write_bool_value("siriBlockUserGeneratedContent", self.siri_block_user_generated_content)
        writer.write_bool_value("siriRequireProfanityFilter", self.siri_require_profanity_filter)
        writer.write_int_value("softwareUpdatesEnforcedDelayInDays", self.software_updates_enforced_delay_in_days)
        writer.write_bool_value("softwareUpdatesForceDelayed", self.software_updates_force_delayed)
        writer.write_bool_value("spotlightBlockInternetResults", self.spotlight_block_internet_results)
        writer.write_bool_value("unpairedExternalBootToRecoveryAllowed", self.unpaired_external_boot_to_recovery_allowed)
        writer.write_bool_value("usbRestrictedModeBlocked", self.usb_restricted_mode_blocked)
        writer.write_bool_value("voiceDialingBlocked", self.voice_dialing_blocked)
        writer.write_bool_value("vpnBlockCreation", self.vpn_block_creation)
        writer.write_bool_value("wallpaperBlockModification", self.wallpaper_block_modification)
        writer.write_bool_value("wifiPowerOnForced", self.wifi_power_on_forced)
        writer.write_bool_value("wiFiConnectOnlyToConfiguredNetworks", self.wi_fi_connect_only_to_configured_networks)
        writer.write_bool_value("wiFiConnectToAllowedNetworksOnlyForced", self.wi_fi_connect_to_allowed_networks_only_forced)
    
    @property
    def shared_device_block_temporary_sessions(self,) -> Optional[bool]:
        """
        Gets the sharedDeviceBlockTemporarySessions property value. Indicates whether or not to block temporary sessions on Shared iPads (iOS 13.4 or later).
        Returns: Optional[bool]
        """
        return self._shared_device_block_temporary_sessions
    
    @shared_device_block_temporary_sessions.setter
    def shared_device_block_temporary_sessions(self,value: Optional[bool] = None) -> None:
        """
        Sets the sharedDeviceBlockTemporarySessions property value. Indicates whether or not to block temporary sessions on Shared iPads (iOS 13.4 or later).
        Args:
            value: Value to set for the shared_device_block_temporary_sessions property.
        """
        self._shared_device_block_temporary_sessions = value
    
    @property
    def siri_block_user_generated_content(self,) -> Optional[bool]:
        """
        Gets the siriBlockUserGeneratedContent property value. Indicates whether or not to block Siri from querying user-generated content when used on a supervised device.
        Returns: Optional[bool]
        """
        return self._siri_block_user_generated_content
    
    @siri_block_user_generated_content.setter
    def siri_block_user_generated_content(self,value: Optional[bool] = None) -> None:
        """
        Sets the siriBlockUserGeneratedContent property value. Indicates whether or not to block Siri from querying user-generated content when used on a supervised device.
        Args:
            value: Value to set for the siri_block_user_generated_content property.
        """
        self._siri_block_user_generated_content = value
    
    @property
    def siri_blocked(self,) -> Optional[bool]:
        """
        Gets the siriBlocked property value. Indicates whether or not to block the user from using Siri.
        Returns: Optional[bool]
        """
        return self._siri_blocked
    
    @siri_blocked.setter
    def siri_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the siriBlocked property value. Indicates whether or not to block the user from using Siri.
        Args:
            value: Value to set for the siri_blocked property.
        """
        self._siri_blocked = value
    
    @property
    def siri_blocked_when_locked(self,) -> Optional[bool]:
        """
        Gets the siriBlockedWhenLocked property value. Indicates whether or not to block the user from using Siri when locked.
        Returns: Optional[bool]
        """
        return self._siri_blocked_when_locked
    
    @siri_blocked_when_locked.setter
    def siri_blocked_when_locked(self,value: Optional[bool] = None) -> None:
        """
        Sets the siriBlockedWhenLocked property value. Indicates whether or not to block the user from using Siri when locked.
        Args:
            value: Value to set for the siri_blocked_when_locked property.
        """
        self._siri_blocked_when_locked = value
    
    @property
    def siri_require_profanity_filter(self,) -> Optional[bool]:
        """
        Gets the siriRequireProfanityFilter property value. Indicates whether or not to prevent Siri from dictating, or speaking profane language on supervised device.
        Returns: Optional[bool]
        """
        return self._siri_require_profanity_filter
    
    @siri_require_profanity_filter.setter
    def siri_require_profanity_filter(self,value: Optional[bool] = None) -> None:
        """
        Sets the siriRequireProfanityFilter property value. Indicates whether or not to prevent Siri from dictating, or speaking profane language on supervised device.
        Args:
            value: Value to set for the siri_require_profanity_filter property.
        """
        self._siri_require_profanity_filter = value
    
    @property
    def software_updates_enforced_delay_in_days(self,) -> Optional[int]:
        """
        Gets the softwareUpdatesEnforcedDelayInDays property value. Sets how many days a software update will be delyed for a supervised device. Valid values 0 to 90
        Returns: Optional[int]
        """
        return self._software_updates_enforced_delay_in_days
    
    @software_updates_enforced_delay_in_days.setter
    def software_updates_enforced_delay_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the softwareUpdatesEnforcedDelayInDays property value. Sets how many days a software update will be delyed for a supervised device. Valid values 0 to 90
        Args:
            value: Value to set for the software_updates_enforced_delay_in_days property.
        """
        self._software_updates_enforced_delay_in_days = value
    
    @property
    def software_updates_force_delayed(self,) -> Optional[bool]:
        """
        Gets the softwareUpdatesForceDelayed property value. Indicates whether or not to delay user visibility of software updates when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._software_updates_force_delayed
    
    @software_updates_force_delayed.setter
    def software_updates_force_delayed(self,value: Optional[bool] = None) -> None:
        """
        Sets the softwareUpdatesForceDelayed property value. Indicates whether or not to delay user visibility of software updates when the device is in supervised mode.
        Args:
            value: Value to set for the software_updates_force_delayed property.
        """
        self._software_updates_force_delayed = value
    
    @property
    def spotlight_block_internet_results(self,) -> Optional[bool]:
        """
        Gets the spotlightBlockInternetResults property value. Indicates whether or not to block Spotlight search from returning internet results on supervised device.
        Returns: Optional[bool]
        """
        return self._spotlight_block_internet_results
    
    @spotlight_block_internet_results.setter
    def spotlight_block_internet_results(self,value: Optional[bool] = None) -> None:
        """
        Sets the spotlightBlockInternetResults property value. Indicates whether or not to block Spotlight search from returning internet results on supervised device.
        Args:
            value: Value to set for the spotlight_block_internet_results property.
        """
        self._spotlight_block_internet_results = value
    
    @property
    def unpaired_external_boot_to_recovery_allowed(self,) -> Optional[bool]:
        """
        Gets the unpairedExternalBootToRecoveryAllowed property value. Allow users to boot devices into recovery mode with unpaired devices. Available for devices running iOS and iPadOS versions 14.5 and later.
        Returns: Optional[bool]
        """
        return self._unpaired_external_boot_to_recovery_allowed
    
    @unpaired_external_boot_to_recovery_allowed.setter
    def unpaired_external_boot_to_recovery_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the unpairedExternalBootToRecoveryAllowed property value. Allow users to boot devices into recovery mode with unpaired devices. Available for devices running iOS and iPadOS versions 14.5 and later.
        Args:
            value: Value to set for the unpaired_external_boot_to_recovery_allowed property.
        """
        self._unpaired_external_boot_to_recovery_allowed = value
    
    @property
    def usb_restricted_mode_blocked(self,) -> Optional[bool]:
        """
        Gets the usbRestrictedModeBlocked property value. Indicates if connecting to USB accessories while the device is locked is allowed (iOS 11.4.1 and later).
        Returns: Optional[bool]
        """
        return self._usb_restricted_mode_blocked
    
    @usb_restricted_mode_blocked.setter
    def usb_restricted_mode_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the usbRestrictedModeBlocked property value. Indicates if connecting to USB accessories while the device is locked is allowed (iOS 11.4.1 and later).
        Args:
            value: Value to set for the usb_restricted_mode_blocked property.
        """
        self._usb_restricted_mode_blocked = value
    
    @property
    def voice_dialing_blocked(self,) -> Optional[bool]:
        """
        Gets the voiceDialingBlocked property value. Indicates whether or not to block voice dialing.
        Returns: Optional[bool]
        """
        return self._voice_dialing_blocked
    
    @voice_dialing_blocked.setter
    def voice_dialing_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the voiceDialingBlocked property value. Indicates whether or not to block voice dialing.
        Args:
            value: Value to set for the voice_dialing_blocked property.
        """
        self._voice_dialing_blocked = value
    
    @property
    def vpn_block_creation(self,) -> Optional[bool]:
        """
        Gets the vpnBlockCreation property value. Indicates whether or not the creation of VPN configurations is blocked (iOS 11.0 and later).
        Returns: Optional[bool]
        """
        return self._vpn_block_creation
    
    @vpn_block_creation.setter
    def vpn_block_creation(self,value: Optional[bool] = None) -> None:
        """
        Sets the vpnBlockCreation property value. Indicates whether or not the creation of VPN configurations is blocked (iOS 11.0 and later).
        Args:
            value: Value to set for the vpn_block_creation property.
        """
        self._vpn_block_creation = value
    
    @property
    def wallpaper_block_modification(self,) -> Optional[bool]:
        """
        Gets the wallpaperBlockModification property value. Indicates whether or not to allow wallpaper modification on supervised device (iOS 9.0 and later) .
        Returns: Optional[bool]
        """
        return self._wallpaper_block_modification
    
    @wallpaper_block_modification.setter
    def wallpaper_block_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the wallpaperBlockModification property value. Indicates whether or not to allow wallpaper modification on supervised device (iOS 9.0 and later) .
        Args:
            value: Value to set for the wallpaper_block_modification property.
        """
        self._wallpaper_block_modification = value
    
    @property
    def wi_fi_connect_only_to_configured_networks(self,) -> Optional[bool]:
        """
        Gets the wiFiConnectOnlyToConfiguredNetworks property value. Indicates whether or not to force the device to use only Wi-Fi networks from configuration profiles when the device is in supervised mode. Available for devices running iOS and iPadOS versions 14.4 and earlier. Devices running 14.5+ should use the setting, 'WiFiConnectToAllowedNetworksOnlyForced.
        Returns: Optional[bool]
        """
        return self._wi_fi_connect_only_to_configured_networks
    
    @wi_fi_connect_only_to_configured_networks.setter
    def wi_fi_connect_only_to_configured_networks(self,value: Optional[bool] = None) -> None:
        """
        Sets the wiFiConnectOnlyToConfiguredNetworks property value. Indicates whether or not to force the device to use only Wi-Fi networks from configuration profiles when the device is in supervised mode. Available for devices running iOS and iPadOS versions 14.4 and earlier. Devices running 14.5+ should use the setting, 'WiFiConnectToAllowedNetworksOnlyForced.
        Args:
            value: Value to set for the wi_fi_connect_only_to_configured_networks property.
        """
        self._wi_fi_connect_only_to_configured_networks = value
    
    @property
    def wi_fi_connect_to_allowed_networks_only_forced(self,) -> Optional[bool]:
        """
        Gets the wiFiConnectToAllowedNetworksOnlyForced property value. Require devices to use Wi-Fi networks set up via configuration profiles. Available for devices running iOS and iPadOS versions 14.5 and later.
        Returns: Optional[bool]
        """
        return self._wi_fi_connect_to_allowed_networks_only_forced
    
    @wi_fi_connect_to_allowed_networks_only_forced.setter
    def wi_fi_connect_to_allowed_networks_only_forced(self,value: Optional[bool] = None) -> None:
        """
        Sets the wiFiConnectToAllowedNetworksOnlyForced property value. Require devices to use Wi-Fi networks set up via configuration profiles. Available for devices running iOS and iPadOS versions 14.5 and later.
        Args:
            value: Value to set for the wi_fi_connect_to_allowed_networks_only_forced property.
        """
        self._wi_fi_connect_to_allowed_networks_only_forced = value
    
    @property
    def wifi_power_on_forced(self,) -> Optional[bool]:
        """
        Gets the wifiPowerOnForced property value. Indicates whether or not Wi-Fi remains on, even when device is in airplane mode. Available for devices running iOS and iPadOS, versions 13.0 and later.
        Returns: Optional[bool]
        """
        return self._wifi_power_on_forced
    
    @wifi_power_on_forced.setter
    def wifi_power_on_forced(self,value: Optional[bool] = None) -> None:
        """
        Sets the wifiPowerOnForced property value. Indicates whether or not Wi-Fi remains on, even when device is in airplane mode. Available for devices running iOS and iPadOS, versions 13.0 and later.
        Args:
            value: Value to set for the wifi_power_on_forced property.
        """
        self._wifi_power_on_forced = value
    

