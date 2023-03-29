from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_list_item, app_list_type, device_configuration, mac_o_s_privacy_access_control_item, mac_o_s_software_update_delay_policy, required_password_type

from . import device_configuration

class MacOSGeneralDeviceConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSGeneralDeviceConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSGeneralDeviceConfiguration"
        # When TRUE, activation lock is allowed when the devices is in the supervised mode. When FALSE, activation lock is not allowed. Default is false.
        self._activation_lock_when_supervised_allowed: Optional[bool] = None
        # Yes prevents users from adding friends to Game Center. Available for devices running macOS versions 10.13 and later.
        self._adding_game_center_friends_blocked: Optional[bool] = None
        # Indicates whether or not to allow AirDrop.
        self._air_drop_blocked: Optional[bool] = None
        # Indicates whether or to block users from unlocking their Mac with Apple Watch.
        self._apple_watch_block_auto_unlock: Optional[bool] = None
        # Indicates whether or not to block the user from accessing the camera of the device.
        self._camera_blocked: Optional[bool] = None
        # Indicates whether or not to allow remote screen observation by Classroom app. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        self._classroom_app_block_remote_screen_observation: Optional[bool] = None
        # Indicates whether or not to automatically give permission to the teacher of a managed course on the Classroom app to view a student's screen without prompting. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        self._classroom_app_force_unprompted_screen_observation: Optional[bool] = None
        # Indicates whether or not to automatically give permission to the teacher's requests, without prompting the student. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        self._classroom_force_automatically_join_classes: Optional[bool] = None
        # Indicates whether a student enrolled in an unmanaged course via Classroom will be required to request permission from the teacher when attempting to leave the course. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        self._classroom_force_request_permission_to_leave_classes: Optional[bool] = None
        # Indicates whether or not to allow the teacher to lock apps or the device without prompting the student. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        self._classroom_force_unprompted_app_and_device_lock: Optional[bool] = None
        # Possible values of the compliance app list.
        self._compliant_app_list_type: Optional[app_list_type.AppListType] = None
        # List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
        self._compliant_apps_list: Optional[List[app_list_item.AppListItem]] = None
        # Indicates whether or not to allow content caching.
        self._content_caching_blocked: Optional[bool] = None
        # Indicates whether or not to block definition lookup.
        self._definition_lookup_blocked: Optional[bool] = None
        # An email address lacking a suffix that matches any of these strings will be considered out-of-domain.
        self._email_in_domain_suffixes: Optional[List[str]] = None
        # TRUE disables the reset option on supervised devices. FALSE enables the reset option on supervised devices. Available for devices running macOS versions 12.0 and later.
        self._erase_content_and_settings_blocked: Optional[bool] = None
        # Yes disables Game Center, and the Game Center icon is removed from the Home screen. Available for devices running macOS versions 10.13 and later.
        self._game_center_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from continuing work that they started on a MacOS device on another iOS or MacOS device (MacOS 10.15 or later).
        self._i_cloud_block_activity_continuation: Optional[bool] = None
        # Indicates whether or not to block iCloud from syncing contacts.
        self._i_cloud_block_address_book: Optional[bool] = None
        # Indicates whether or not to block iCloud from syncing bookmarks.
        self._i_cloud_block_bookmarks: Optional[bool] = None
        # Indicates whether or not to block iCloud from syncing calendars.
        self._i_cloud_block_calendar: Optional[bool] = None
        # Indicates whether or not to block iCloud document sync.
        self._i_cloud_block_document_sync: Optional[bool] = None
        # Indicates whether or not to block iCloud from syncing mail.
        self._i_cloud_block_mail: Optional[bool] = None
        # Indicates whether or not to block iCloud from syncing notes.
        self._i_cloud_block_notes: Optional[bool] = None
        # Indicates whether or not to block iCloud Photo Library.
        self._i_cloud_block_photo_library: Optional[bool] = None
        # Indicates whether or not to block iCloud from syncing reminders.
        self._i_cloud_block_reminders: Optional[bool] = None
        # When TRUE the synchronization of cloud desktop and documents is blocked. When FALSE, synchronization of the cloud desktop and documents are allowed. Available for devices running macOS 10.12.4 and later.
        self._i_cloud_desktop_and_documents_blocked: Optional[bool] = None
        # iCloud private relay is an iCloud+ service that prevents networks and servers from monitoring a person's activity across the internet. By blocking iCloud private relay, Apple will not encrypt the traffic leaving the device. Available for devices running macOS 12 and later.
        self._i_cloud_private_relay_blocked: Optional[bool] = None
        # Indicates whether or not to block files from being transferred using iTunes.
        self._i_tunes_block_file_sharing: Optional[bool] = None
        # Indicates whether or not to block Music service and revert Music app to classic mode.
        self._i_tunes_block_music_service: Optional[bool] = None
        # Indicates whether or not to block the user from using dictation input.
        self._keyboard_block_dictation: Optional[bool] = None
        # Indicates whether or not iCloud keychain synchronization is blocked (macOS 10.12 and later).
        self._keychain_block_cloud_sync: Optional[bool] = None
        # TRUE prevents multiplayer gaming when using Game Center. FALSE allows multiplayer gaming when using Game Center. Available for devices running macOS versions 10.13 and later.
        self._multiplayer_gaming_blocked: Optional[bool] = None
        # Indicates whether or not to block sharing passwords with the AirDrop passwords feature.
        self._password_block_air_drop_sharing: Optional[bool] = None
        # Indicates whether or not to block the AutoFill Passwords feature.
        self._password_block_auto_fill: Optional[bool] = None
        # Indicates whether or not to block fingerprint unlock.
        self._password_block_fingerprint_unlock: Optional[bool] = None
        # Indicates whether or not to allow passcode modification.
        self._password_block_modification: Optional[bool] = None
        # Indicates whether or not to block requesting passwords from nearby devices.
        self._password_block_proximity_requests: Optional[bool] = None
        # Block simple passwords.
        self._password_block_simple: Optional[bool] = None
        # Number of days before the password expires.
        self._password_expiration_days: Optional[int] = None
        # The number of allowed failed attempts to enter the passcode at the device's lock screen. Valid values 2 to 11
        self._password_maximum_attempt_count: Optional[int] = None
        # Number of character sets a password must contain. Valid values 0 to 4
        self._password_minimum_character_set_count: Optional[int] = None
        # Minimum length of passwords.
        self._password_minimum_length: Optional[int] = None
        # Minutes of inactivity required before a password is required.
        self._password_minutes_of_inactivity_before_lock: Optional[int] = None
        # Minutes of inactivity required before the screen times out.
        self._password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
        # The number of minutes before the login is reset after the maximum number of unsuccessful login attempts is reached.
        self._password_minutes_until_failed_login_reset: Optional[int] = None
        # Number of previous passwords to block.
        self._password_previous_password_block_count: Optional[int] = None
        # Whether or not to require a password.
        self._password_required: Optional[bool] = None
        # Possible values of required passwords.
        self._password_required_type: Optional[required_password_type.RequiredPasswordType] = None
        # List of privacy preference policy controls. This collection can contain a maximum of 10000 elements.
        self._privacy_access_controls: Optional[List[mac_o_s_privacy_access_control_item.MacOSPrivacyAccessControlItem]] = None
        # Indicates whether or not to block the user from using Auto fill in Safari.
        self._safari_block_autofill: Optional[bool] = None
        # Indicates whether or not to block the user from taking Screenshots.
        self._screen_capture_blocked: Optional[bool] = None
        # Specify the number of days (1-90) to delay visibility of major OS software updates. Available for devices running macOS versions 11.3 and later. Valid values 0 to 90
        self._software_update_major_o_s_deferred_install_delay_in_days: Optional[int] = None
        # Specify the number of days (1-90) to delay visibility of minor OS software updates. Available for devices running macOS versions 11.3 and later. Valid values 0 to 90
        self._software_update_minor_o_s_deferred_install_delay_in_days: Optional[int] = None
        # Specify the number of days (1-90) to delay visibility of non-OS software updates. Available for devices running macOS versions 11.3 and later. Valid values 0 to 90
        self._software_update_non_o_s_deferred_install_delay_in_days: Optional[int] = None
        # Sets how many days a software update will be delyed for a supervised device. Valid values 0 to 90
        self._software_updates_enforced_delay_in_days: Optional[int] = None
        # Indicates whether or not to block Spotlight from returning any results from an Internet search.
        self._spotlight_block_internet_results: Optional[bool] = None
        # Maximum hours after which the user must enter their password to unlock the device instead of using Touch ID. Available for devices running macOS 12 and later. Valid values 0 to 2147483647
        self._touch_id_timeout_in_hours: Optional[int] = None
        # Determines whether to delay OS and/or app updates for macOS. Possible values are: none, delayOSUpdateVisibility, delayAppUpdateVisibility, unknownFutureValue, delayMajorOsUpdateVisibility.
        self._update_delay_policy: Optional[mac_o_s_software_update_delay_policy.MacOSSoftwareUpdateDelayPolicy] = None
        # TRUE prevents the wallpaper from being changed. FALSE allows the wallpaper to be changed. Available for devices running macOS versions 10.13 and later.
        self._wallpaper_modification_blocked: Optional[bool] = None
    
    @property
    def activation_lock_when_supervised_allowed(self,) -> Optional[bool]:
        """
        Gets the activationLockWhenSupervisedAllowed property value. When TRUE, activation lock is allowed when the devices is in the supervised mode. When FALSE, activation lock is not allowed. Default is false.
        Returns: Optional[bool]
        """
        return self._activation_lock_when_supervised_allowed
    
    @activation_lock_when_supervised_allowed.setter
    def activation_lock_when_supervised_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the activationLockWhenSupervisedAllowed property value. When TRUE, activation lock is allowed when the devices is in the supervised mode. When FALSE, activation lock is not allowed. Default is false.
        Args:
            value: Value to set for the activation_lock_when_supervised_allowed property.
        """
        self._activation_lock_when_supervised_allowed = value
    
    @property
    def adding_game_center_friends_blocked(self,) -> Optional[bool]:
        """
        Gets the addingGameCenterFriendsBlocked property value. Yes prevents users from adding friends to Game Center. Available for devices running macOS versions 10.13 and later.
        Returns: Optional[bool]
        """
        return self._adding_game_center_friends_blocked
    
    @adding_game_center_friends_blocked.setter
    def adding_game_center_friends_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the addingGameCenterFriendsBlocked property value. Yes prevents users from adding friends to Game Center. Available for devices running macOS versions 10.13 and later.
        Args:
            value: Value to set for the adding_game_center_friends_blocked property.
        """
        self._adding_game_center_friends_blocked = value
    
    @property
    def air_drop_blocked(self,) -> Optional[bool]:
        """
        Gets the airDropBlocked property value. Indicates whether or not to allow AirDrop.
        Returns: Optional[bool]
        """
        return self._air_drop_blocked
    
    @air_drop_blocked.setter
    def air_drop_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the airDropBlocked property value. Indicates whether or not to allow AirDrop.
        Args:
            value: Value to set for the air_drop_blocked property.
        """
        self._air_drop_blocked = value
    
    @property
    def apple_watch_block_auto_unlock(self,) -> Optional[bool]:
        """
        Gets the appleWatchBlockAutoUnlock property value. Indicates whether or to block users from unlocking their Mac with Apple Watch.
        Returns: Optional[bool]
        """
        return self._apple_watch_block_auto_unlock
    
    @apple_watch_block_auto_unlock.setter
    def apple_watch_block_auto_unlock(self,value: Optional[bool] = None) -> None:
        """
        Sets the appleWatchBlockAutoUnlock property value. Indicates whether or to block users from unlocking their Mac with Apple Watch.
        Args:
            value: Value to set for the apple_watch_block_auto_unlock property.
        """
        self._apple_watch_block_auto_unlock = value
    
    @property
    def camera_blocked(self,) -> Optional[bool]:
        """
        Gets the cameraBlocked property value. Indicates whether or not to block the user from accessing the camera of the device.
        Returns: Optional[bool]
        """
        return self._camera_blocked
    
    @camera_blocked.setter
    def camera_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the cameraBlocked property value. Indicates whether or not to block the user from accessing the camera of the device.
        Args:
            value: Value to set for the camera_blocked property.
        """
        self._camera_blocked = value
    
    @property
    def classroom_app_block_remote_screen_observation(self,) -> Optional[bool]:
        """
        Gets the classroomAppBlockRemoteScreenObservation property value. Indicates whether or not to allow remote screen observation by Classroom app. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        Returns: Optional[bool]
        """
        return self._classroom_app_block_remote_screen_observation
    
    @classroom_app_block_remote_screen_observation.setter
    def classroom_app_block_remote_screen_observation(self,value: Optional[bool] = None) -> None:
        """
        Sets the classroomAppBlockRemoteScreenObservation property value. Indicates whether or not to allow remote screen observation by Classroom app. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        Args:
            value: Value to set for the classroom_app_block_remote_screen_observation property.
        """
        self._classroom_app_block_remote_screen_observation = value
    
    @property
    def classroom_app_force_unprompted_screen_observation(self,) -> Optional[bool]:
        """
        Gets the classroomAppForceUnpromptedScreenObservation property value. Indicates whether or not to automatically give permission to the teacher of a managed course on the Classroom app to view a student's screen without prompting. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        Returns: Optional[bool]
        """
        return self._classroom_app_force_unprompted_screen_observation
    
    @classroom_app_force_unprompted_screen_observation.setter
    def classroom_app_force_unprompted_screen_observation(self,value: Optional[bool] = None) -> None:
        """
        Sets the classroomAppForceUnpromptedScreenObservation property value. Indicates whether or not to automatically give permission to the teacher of a managed course on the Classroom app to view a student's screen without prompting. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        Args:
            value: Value to set for the classroom_app_force_unprompted_screen_observation property.
        """
        self._classroom_app_force_unprompted_screen_observation = value
    
    @property
    def classroom_force_automatically_join_classes(self,) -> Optional[bool]:
        """
        Gets the classroomForceAutomaticallyJoinClasses property value. Indicates whether or not to automatically give permission to the teacher's requests, without prompting the student. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        Returns: Optional[bool]
        """
        return self._classroom_force_automatically_join_classes
    
    @classroom_force_automatically_join_classes.setter
    def classroom_force_automatically_join_classes(self,value: Optional[bool] = None) -> None:
        """
        Sets the classroomForceAutomaticallyJoinClasses property value. Indicates whether or not to automatically give permission to the teacher's requests, without prompting the student. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        Args:
            value: Value to set for the classroom_force_automatically_join_classes property.
        """
        self._classroom_force_automatically_join_classes = value
    
    @property
    def classroom_force_request_permission_to_leave_classes(self,) -> Optional[bool]:
        """
        Gets the classroomForceRequestPermissionToLeaveClasses property value. Indicates whether a student enrolled in an unmanaged course via Classroom will be required to request permission from the teacher when attempting to leave the course. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        Returns: Optional[bool]
        """
        return self._classroom_force_request_permission_to_leave_classes
    
    @classroom_force_request_permission_to_leave_classes.setter
    def classroom_force_request_permission_to_leave_classes(self,value: Optional[bool] = None) -> None:
        """
        Sets the classroomForceRequestPermissionToLeaveClasses property value. Indicates whether a student enrolled in an unmanaged course via Classroom will be required to request permission from the teacher when attempting to leave the course. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        Args:
            value: Value to set for the classroom_force_request_permission_to_leave_classes property.
        """
        self._classroom_force_request_permission_to_leave_classes = value
    
    @property
    def classroom_force_unprompted_app_and_device_lock(self,) -> Optional[bool]:
        """
        Gets the classroomForceUnpromptedAppAndDeviceLock property value. Indicates whether or not to allow the teacher to lock apps or the device without prompting the student. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
        Returns: Optional[bool]
        """
        return self._classroom_force_unprompted_app_and_device_lock
    
    @classroom_force_unprompted_app_and_device_lock.setter
    def classroom_force_unprompted_app_and_device_lock(self,value: Optional[bool] = None) -> None:
        """
        Sets the classroomForceUnpromptedAppAndDeviceLock property value. Indicates whether or not to allow the teacher to lock apps or the device without prompting the student. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
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
    def content_caching_blocked(self,) -> Optional[bool]:
        """
        Gets the contentCachingBlocked property value. Indicates whether or not to allow content caching.
        Returns: Optional[bool]
        """
        return self._content_caching_blocked
    
    @content_caching_blocked.setter
    def content_caching_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the contentCachingBlocked property value. Indicates whether or not to allow content caching.
        Args:
            value: Value to set for the content_caching_blocked property.
        """
        self._content_caching_blocked = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSGeneralDeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSGeneralDeviceConfiguration()
    
    @property
    def definition_lookup_blocked(self,) -> Optional[bool]:
        """
        Gets the definitionLookupBlocked property value. Indicates whether or not to block definition lookup.
        Returns: Optional[bool]
        """
        return self._definition_lookup_blocked
    
    @definition_lookup_blocked.setter
    def definition_lookup_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the definitionLookupBlocked property value. Indicates whether or not to block definition lookup.
        Args:
            value: Value to set for the definition_lookup_blocked property.
        """
        self._definition_lookup_blocked = value
    
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
    def erase_content_and_settings_blocked(self,) -> Optional[bool]:
        """
        Gets the eraseContentAndSettingsBlocked property value. TRUE disables the reset option on supervised devices. FALSE enables the reset option on supervised devices. Available for devices running macOS versions 12.0 and later.
        Returns: Optional[bool]
        """
        return self._erase_content_and_settings_blocked
    
    @erase_content_and_settings_blocked.setter
    def erase_content_and_settings_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the eraseContentAndSettingsBlocked property value. TRUE disables the reset option on supervised devices. FALSE enables the reset option on supervised devices. Available for devices running macOS versions 12.0 and later.
        Args:
            value: Value to set for the erase_content_and_settings_blocked property.
        """
        self._erase_content_and_settings_blocked = value
    
    @property
    def game_center_blocked(self,) -> Optional[bool]:
        """
        Gets the gameCenterBlocked property value. Yes disables Game Center, and the Game Center icon is removed from the Home screen. Available for devices running macOS versions 10.13 and later.
        Returns: Optional[bool]
        """
        return self._game_center_blocked
    
    @game_center_blocked.setter
    def game_center_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the gameCenterBlocked property value. Yes disables Game Center, and the Game Center icon is removed from the Home screen. Available for devices running macOS versions 10.13 and later.
        Args:
            value: Value to set for the game_center_blocked property.
        """
        self._game_center_blocked = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_list_item, app_list_type, device_configuration, mac_o_s_privacy_access_control_item, mac_o_s_software_update_delay_policy, required_password_type

        fields: Dict[str, Callable[[Any], None]] = {
            "activationLockWhenSupervisedAllowed": lambda n : setattr(self, 'activation_lock_when_supervised_allowed', n.get_bool_value()),
            "addingGameCenterFriendsBlocked": lambda n : setattr(self, 'adding_game_center_friends_blocked', n.get_bool_value()),
            "airDropBlocked": lambda n : setattr(self, 'air_drop_blocked', n.get_bool_value()),
            "appleWatchBlockAutoUnlock": lambda n : setattr(self, 'apple_watch_block_auto_unlock', n.get_bool_value()),
            "cameraBlocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "classroomAppBlockRemoteScreenObservation": lambda n : setattr(self, 'classroom_app_block_remote_screen_observation', n.get_bool_value()),
            "classroomAppForceUnpromptedScreenObservation": lambda n : setattr(self, 'classroom_app_force_unprompted_screen_observation', n.get_bool_value()),
            "classroomForceAutomaticallyJoinClasses": lambda n : setattr(self, 'classroom_force_automatically_join_classes', n.get_bool_value()),
            "classroomForceRequestPermissionToLeaveClasses": lambda n : setattr(self, 'classroom_force_request_permission_to_leave_classes', n.get_bool_value()),
            "classroomForceUnpromptedAppAndDeviceLock": lambda n : setattr(self, 'classroom_force_unprompted_app_and_device_lock', n.get_bool_value()),
            "compliantAppsList": lambda n : setattr(self, 'compliant_apps_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "compliantAppListType": lambda n : setattr(self, 'compliant_app_list_type', n.get_enum_value(app_list_type.AppListType)),
            "contentCachingBlocked": lambda n : setattr(self, 'content_caching_blocked', n.get_bool_value()),
            "definitionLookupBlocked": lambda n : setattr(self, 'definition_lookup_blocked', n.get_bool_value()),
            "emailInDomainSuffixes": lambda n : setattr(self, 'email_in_domain_suffixes', n.get_collection_of_primitive_values(str)),
            "eraseContentAndSettingsBlocked": lambda n : setattr(self, 'erase_content_and_settings_blocked', n.get_bool_value()),
            "gameCenterBlocked": lambda n : setattr(self, 'game_center_blocked', n.get_bool_value()),
            "iCloudBlockActivityContinuation": lambda n : setattr(self, 'i_cloud_block_activity_continuation', n.get_bool_value()),
            "iCloudBlockAddressBook": lambda n : setattr(self, 'i_cloud_block_address_book', n.get_bool_value()),
            "iCloudBlockBookmarks": lambda n : setattr(self, 'i_cloud_block_bookmarks', n.get_bool_value()),
            "iCloudBlockCalendar": lambda n : setattr(self, 'i_cloud_block_calendar', n.get_bool_value()),
            "iCloudBlockDocumentSync": lambda n : setattr(self, 'i_cloud_block_document_sync', n.get_bool_value()),
            "iCloudBlockMail": lambda n : setattr(self, 'i_cloud_block_mail', n.get_bool_value()),
            "iCloudBlockNotes": lambda n : setattr(self, 'i_cloud_block_notes', n.get_bool_value()),
            "iCloudBlockPhotoLibrary": lambda n : setattr(self, 'i_cloud_block_photo_library', n.get_bool_value()),
            "iCloudBlockReminders": lambda n : setattr(self, 'i_cloud_block_reminders', n.get_bool_value()),
            "iCloudDesktopAndDocumentsBlocked": lambda n : setattr(self, 'i_cloud_desktop_and_documents_blocked', n.get_bool_value()),
            "iCloudPrivateRelayBlocked": lambda n : setattr(self, 'i_cloud_private_relay_blocked', n.get_bool_value()),
            "iTunesBlockFileSharing": lambda n : setattr(self, 'i_tunes_block_file_sharing', n.get_bool_value()),
            "iTunesBlockMusicService": lambda n : setattr(self, 'i_tunes_block_music_service', n.get_bool_value()),
            "keyboardBlockDictation": lambda n : setattr(self, 'keyboard_block_dictation', n.get_bool_value()),
            "keychainBlockCloudSync": lambda n : setattr(self, 'keychain_block_cloud_sync', n.get_bool_value()),
            "multiplayerGamingBlocked": lambda n : setattr(self, 'multiplayer_gaming_blocked', n.get_bool_value()),
            "passwordBlockAirDropSharing": lambda n : setattr(self, 'password_block_air_drop_sharing', n.get_bool_value()),
            "passwordBlockAutoFill": lambda n : setattr(self, 'password_block_auto_fill', n.get_bool_value()),
            "passwordBlockFingerprintUnlock": lambda n : setattr(self, 'password_block_fingerprint_unlock', n.get_bool_value()),
            "passwordBlockModification": lambda n : setattr(self, 'password_block_modification', n.get_bool_value()),
            "passwordBlockProximityRequests": lambda n : setattr(self, 'password_block_proximity_requests', n.get_bool_value()),
            "passwordBlockSimple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMaximumAttemptCount": lambda n : setattr(self, 'password_maximum_attempt_count', n.get_int_value()),
            "passwordMinimumCharacterSetCount": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passwordMinutesUntilFailedLoginReset": lambda n : setattr(self, 'password_minutes_until_failed_login_reset', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequired": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(required_password_type.RequiredPasswordType)),
            "privacyAccessControls": lambda n : setattr(self, 'privacy_access_controls', n.get_collection_of_object_values(mac_o_s_privacy_access_control_item.MacOSPrivacyAccessControlItem)),
            "safariBlockAutofill": lambda n : setattr(self, 'safari_block_autofill', n.get_bool_value()),
            "screenCaptureBlocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "softwareUpdatesEnforcedDelayInDays": lambda n : setattr(self, 'software_updates_enforced_delay_in_days', n.get_int_value()),
            "softwareUpdateMajorOSDeferredInstallDelayInDays": lambda n : setattr(self, 'software_update_major_o_s_deferred_install_delay_in_days', n.get_int_value()),
            "softwareUpdateMinorOSDeferredInstallDelayInDays": lambda n : setattr(self, 'software_update_minor_o_s_deferred_install_delay_in_days', n.get_int_value()),
            "softwareUpdateNonOSDeferredInstallDelayInDays": lambda n : setattr(self, 'software_update_non_o_s_deferred_install_delay_in_days', n.get_int_value()),
            "spotlightBlockInternetResults": lambda n : setattr(self, 'spotlight_block_internet_results', n.get_bool_value()),
            "touchIdTimeoutInHours": lambda n : setattr(self, 'touch_id_timeout_in_hours', n.get_int_value()),
            "updateDelayPolicy": lambda n : setattr(self, 'update_delay_policy', n.get_enum_value(mac_o_s_software_update_delay_policy.MacOSSoftwareUpdateDelayPolicy)),
            "wallpaperModificationBlocked": lambda n : setattr(self, 'wallpaper_modification_blocked', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def i_cloud_block_activity_continuation(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockActivityContinuation property value. Indicates whether or not to block the user from continuing work that they started on a MacOS device on another iOS or MacOS device (MacOS 10.15 or later).
        Returns: Optional[bool]
        """
        return self._i_cloud_block_activity_continuation
    
    @i_cloud_block_activity_continuation.setter
    def i_cloud_block_activity_continuation(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockActivityContinuation property value. Indicates whether or not to block the user from continuing work that they started on a MacOS device on another iOS or MacOS device (MacOS 10.15 or later).
        Args:
            value: Value to set for the i_cloud_block_activity_continuation property.
        """
        self._i_cloud_block_activity_continuation = value
    
    @property
    def i_cloud_block_address_book(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockAddressBook property value. Indicates whether or not to block iCloud from syncing contacts.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_address_book
    
    @i_cloud_block_address_book.setter
    def i_cloud_block_address_book(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockAddressBook property value. Indicates whether or not to block iCloud from syncing contacts.
        Args:
            value: Value to set for the i_cloud_block_address_book property.
        """
        self._i_cloud_block_address_book = value
    
    @property
    def i_cloud_block_bookmarks(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockBookmarks property value. Indicates whether or not to block iCloud from syncing bookmarks.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_bookmarks
    
    @i_cloud_block_bookmarks.setter
    def i_cloud_block_bookmarks(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockBookmarks property value. Indicates whether or not to block iCloud from syncing bookmarks.
        Args:
            value: Value to set for the i_cloud_block_bookmarks property.
        """
        self._i_cloud_block_bookmarks = value
    
    @property
    def i_cloud_block_calendar(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockCalendar property value. Indicates whether or not to block iCloud from syncing calendars.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_calendar
    
    @i_cloud_block_calendar.setter
    def i_cloud_block_calendar(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockCalendar property value. Indicates whether or not to block iCloud from syncing calendars.
        Args:
            value: Value to set for the i_cloud_block_calendar property.
        """
        self._i_cloud_block_calendar = value
    
    @property
    def i_cloud_block_document_sync(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockDocumentSync property value. Indicates whether or not to block iCloud document sync.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_document_sync
    
    @i_cloud_block_document_sync.setter
    def i_cloud_block_document_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockDocumentSync property value. Indicates whether or not to block iCloud document sync.
        Args:
            value: Value to set for the i_cloud_block_document_sync property.
        """
        self._i_cloud_block_document_sync = value
    
    @property
    def i_cloud_block_mail(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockMail property value. Indicates whether or not to block iCloud from syncing mail.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_mail
    
    @i_cloud_block_mail.setter
    def i_cloud_block_mail(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockMail property value. Indicates whether or not to block iCloud from syncing mail.
        Args:
            value: Value to set for the i_cloud_block_mail property.
        """
        self._i_cloud_block_mail = value
    
    @property
    def i_cloud_block_notes(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockNotes property value. Indicates whether or not to block iCloud from syncing notes.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_notes
    
    @i_cloud_block_notes.setter
    def i_cloud_block_notes(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockNotes property value. Indicates whether or not to block iCloud from syncing notes.
        Args:
            value: Value to set for the i_cloud_block_notes property.
        """
        self._i_cloud_block_notes = value
    
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
    def i_cloud_block_reminders(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockReminders property value. Indicates whether or not to block iCloud from syncing reminders.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_reminders
    
    @i_cloud_block_reminders.setter
    def i_cloud_block_reminders(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockReminders property value. Indicates whether or not to block iCloud from syncing reminders.
        Args:
            value: Value to set for the i_cloud_block_reminders property.
        """
        self._i_cloud_block_reminders = value
    
    @property
    def i_cloud_desktop_and_documents_blocked(self,) -> Optional[bool]:
        """
        Gets the iCloudDesktopAndDocumentsBlocked property value. When TRUE the synchronization of cloud desktop and documents is blocked. When FALSE, synchronization of the cloud desktop and documents are allowed. Available for devices running macOS 10.12.4 and later.
        Returns: Optional[bool]
        """
        return self._i_cloud_desktop_and_documents_blocked
    
    @i_cloud_desktop_and_documents_blocked.setter
    def i_cloud_desktop_and_documents_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudDesktopAndDocumentsBlocked property value. When TRUE the synchronization of cloud desktop and documents is blocked. When FALSE, synchronization of the cloud desktop and documents are allowed. Available for devices running macOS 10.12.4 and later.
        Args:
            value: Value to set for the i_cloud_desktop_and_documents_blocked property.
        """
        self._i_cloud_desktop_and_documents_blocked = value
    
    @property
    def i_cloud_private_relay_blocked(self,) -> Optional[bool]:
        """
        Gets the iCloudPrivateRelayBlocked property value. iCloud private relay is an iCloud+ service that prevents networks and servers from monitoring a person's activity across the internet. By blocking iCloud private relay, Apple will not encrypt the traffic leaving the device. Available for devices running macOS 12 and later.
        Returns: Optional[bool]
        """
        return self._i_cloud_private_relay_blocked
    
    @i_cloud_private_relay_blocked.setter
    def i_cloud_private_relay_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudPrivateRelayBlocked property value. iCloud private relay is an iCloud+ service that prevents networks and servers from monitoring a person's activity across the internet. By blocking iCloud private relay, Apple will not encrypt the traffic leaving the device. Available for devices running macOS 12 and later.
        Args:
            value: Value to set for the i_cloud_private_relay_blocked property.
        """
        self._i_cloud_private_relay_blocked = value
    
    @property
    def i_tunes_block_file_sharing(self,) -> Optional[bool]:
        """
        Gets the iTunesBlockFileSharing property value. Indicates whether or not to block files from being transferred using iTunes.
        Returns: Optional[bool]
        """
        return self._i_tunes_block_file_sharing
    
    @i_tunes_block_file_sharing.setter
    def i_tunes_block_file_sharing(self,value: Optional[bool] = None) -> None:
        """
        Sets the iTunesBlockFileSharing property value. Indicates whether or not to block files from being transferred using iTunes.
        Args:
            value: Value to set for the i_tunes_block_file_sharing property.
        """
        self._i_tunes_block_file_sharing = value
    
    @property
    def i_tunes_block_music_service(self,) -> Optional[bool]:
        """
        Gets the iTunesBlockMusicService property value. Indicates whether or not to block Music service and revert Music app to classic mode.
        Returns: Optional[bool]
        """
        return self._i_tunes_block_music_service
    
    @i_tunes_block_music_service.setter
    def i_tunes_block_music_service(self,value: Optional[bool] = None) -> None:
        """
        Sets the iTunesBlockMusicService property value. Indicates whether or not to block Music service and revert Music app to classic mode.
        Args:
            value: Value to set for the i_tunes_block_music_service property.
        """
        self._i_tunes_block_music_service = value
    
    @property
    def keyboard_block_dictation(self,) -> Optional[bool]:
        """
        Gets the keyboardBlockDictation property value. Indicates whether or not to block the user from using dictation input.
        Returns: Optional[bool]
        """
        return self._keyboard_block_dictation
    
    @keyboard_block_dictation.setter
    def keyboard_block_dictation(self,value: Optional[bool] = None) -> None:
        """
        Sets the keyboardBlockDictation property value. Indicates whether or not to block the user from using dictation input.
        Args:
            value: Value to set for the keyboard_block_dictation property.
        """
        self._keyboard_block_dictation = value
    
    @property
    def keychain_block_cloud_sync(self,) -> Optional[bool]:
        """
        Gets the keychainBlockCloudSync property value. Indicates whether or not iCloud keychain synchronization is blocked (macOS 10.12 and later).
        Returns: Optional[bool]
        """
        return self._keychain_block_cloud_sync
    
    @keychain_block_cloud_sync.setter
    def keychain_block_cloud_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the keychainBlockCloudSync property value. Indicates whether or not iCloud keychain synchronization is blocked (macOS 10.12 and later).
        Args:
            value: Value to set for the keychain_block_cloud_sync property.
        """
        self._keychain_block_cloud_sync = value
    
    @property
    def multiplayer_gaming_blocked(self,) -> Optional[bool]:
        """
        Gets the multiplayerGamingBlocked property value. TRUE prevents multiplayer gaming when using Game Center. FALSE allows multiplayer gaming when using Game Center. Available for devices running macOS versions 10.13 and later.
        Returns: Optional[bool]
        """
        return self._multiplayer_gaming_blocked
    
    @multiplayer_gaming_blocked.setter
    def multiplayer_gaming_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the multiplayerGamingBlocked property value. TRUE prevents multiplayer gaming when using Game Center. FALSE allows multiplayer gaming when using Game Center. Available for devices running macOS versions 10.13 and later.
        Args:
            value: Value to set for the multiplayer_gaming_blocked property.
        """
        self._multiplayer_gaming_blocked = value
    
    @property
    def password_block_air_drop_sharing(self,) -> Optional[bool]:
        """
        Gets the passwordBlockAirDropSharing property value. Indicates whether or not to block sharing passwords with the AirDrop passwords feature.
        Returns: Optional[bool]
        """
        return self._password_block_air_drop_sharing
    
    @password_block_air_drop_sharing.setter
    def password_block_air_drop_sharing(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockAirDropSharing property value. Indicates whether or not to block sharing passwords with the AirDrop passwords feature.
        Args:
            value: Value to set for the password_block_air_drop_sharing property.
        """
        self._password_block_air_drop_sharing = value
    
    @property
    def password_block_auto_fill(self,) -> Optional[bool]:
        """
        Gets the passwordBlockAutoFill property value. Indicates whether or not to block the AutoFill Passwords feature.
        Returns: Optional[bool]
        """
        return self._password_block_auto_fill
    
    @password_block_auto_fill.setter
    def password_block_auto_fill(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockAutoFill property value. Indicates whether or not to block the AutoFill Passwords feature.
        Args:
            value: Value to set for the password_block_auto_fill property.
        """
        self._password_block_auto_fill = value
    
    @property
    def password_block_fingerprint_unlock(self,) -> Optional[bool]:
        """
        Gets the passwordBlockFingerprintUnlock property value. Indicates whether or not to block fingerprint unlock.
        Returns: Optional[bool]
        """
        return self._password_block_fingerprint_unlock
    
    @password_block_fingerprint_unlock.setter
    def password_block_fingerprint_unlock(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockFingerprintUnlock property value. Indicates whether or not to block fingerprint unlock.
        Args:
            value: Value to set for the password_block_fingerprint_unlock property.
        """
        self._password_block_fingerprint_unlock = value
    
    @property
    def password_block_modification(self,) -> Optional[bool]:
        """
        Gets the passwordBlockModification property value. Indicates whether or not to allow passcode modification.
        Returns: Optional[bool]
        """
        return self._password_block_modification
    
    @password_block_modification.setter
    def password_block_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockModification property value. Indicates whether or not to allow passcode modification.
        Args:
            value: Value to set for the password_block_modification property.
        """
        self._password_block_modification = value
    
    @property
    def password_block_proximity_requests(self,) -> Optional[bool]:
        """
        Gets the passwordBlockProximityRequests property value. Indicates whether or not to block requesting passwords from nearby devices.
        Returns: Optional[bool]
        """
        return self._password_block_proximity_requests
    
    @password_block_proximity_requests.setter
    def password_block_proximity_requests(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockProximityRequests property value. Indicates whether or not to block requesting passwords from nearby devices.
        Args:
            value: Value to set for the password_block_proximity_requests property.
        """
        self._password_block_proximity_requests = value
    
    @property
    def password_block_simple(self,) -> Optional[bool]:
        """
        Gets the passwordBlockSimple property value. Block simple passwords.
        Returns: Optional[bool]
        """
        return self._password_block_simple
    
    @password_block_simple.setter
    def password_block_simple(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockSimple property value. Block simple passwords.
        Args:
            value: Value to set for the password_block_simple property.
        """
        self._password_block_simple = value
    
    @property
    def password_expiration_days(self,) -> Optional[int]:
        """
        Gets the passwordExpirationDays property value. Number of days before the password expires.
        Returns: Optional[int]
        """
        return self._password_expiration_days
    
    @password_expiration_days.setter
    def password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordExpirationDays property value. Number of days before the password expires.
        Args:
            value: Value to set for the password_expiration_days property.
        """
        self._password_expiration_days = value
    
    @property
    def password_maximum_attempt_count(self,) -> Optional[int]:
        """
        Gets the passwordMaximumAttemptCount property value. The number of allowed failed attempts to enter the passcode at the device's lock screen. Valid values 2 to 11
        Returns: Optional[int]
        """
        return self._password_maximum_attempt_count
    
    @password_maximum_attempt_count.setter
    def password_maximum_attempt_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMaximumAttemptCount property value. The number of allowed failed attempts to enter the passcode at the device's lock screen. Valid values 2 to 11
        Args:
            value: Value to set for the password_maximum_attempt_count property.
        """
        self._password_maximum_attempt_count = value
    
    @property
    def password_minimum_character_set_count(self,) -> Optional[int]:
        """
        Gets the passwordMinimumCharacterSetCount property value. Number of character sets a password must contain. Valid values 0 to 4
        Returns: Optional[int]
        """
        return self._password_minimum_character_set_count
    
    @password_minimum_character_set_count.setter
    def password_minimum_character_set_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumCharacterSetCount property value. Number of character sets a password must contain. Valid values 0 to 4
        Args:
            value: Value to set for the password_minimum_character_set_count property.
        """
        self._password_minimum_character_set_count = value
    
    @property
    def password_minimum_length(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLength property value. Minimum length of passwords.
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. Minimum length of passwords.
        Args:
            value: Value to set for the password_minimum_length property.
        """
        self._password_minimum_length = value
    
    @property
    def password_minutes_of_inactivity_before_lock(self,) -> Optional[int]:
        """
        Gets the passwordMinutesOfInactivityBeforeLock property value. Minutes of inactivity required before a password is required.
        Returns: Optional[int]
        """
        return self._password_minutes_of_inactivity_before_lock
    
    @password_minutes_of_inactivity_before_lock.setter
    def password_minutes_of_inactivity_before_lock(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinutesOfInactivityBeforeLock property value. Minutes of inactivity required before a password is required.
        Args:
            value: Value to set for the password_minutes_of_inactivity_before_lock property.
        """
        self._password_minutes_of_inactivity_before_lock = value
    
    @property
    def password_minutes_of_inactivity_before_screen_timeout(self,) -> Optional[int]:
        """
        Gets the passwordMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity required before the screen times out.
        Returns: Optional[int]
        """
        return self._password_minutes_of_inactivity_before_screen_timeout
    
    @password_minutes_of_inactivity_before_screen_timeout.setter
    def password_minutes_of_inactivity_before_screen_timeout(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity required before the screen times out.
        Args:
            value: Value to set for the password_minutes_of_inactivity_before_screen_timeout property.
        """
        self._password_minutes_of_inactivity_before_screen_timeout = value
    
    @property
    def password_minutes_until_failed_login_reset(self,) -> Optional[int]:
        """
        Gets the passwordMinutesUntilFailedLoginReset property value. The number of minutes before the login is reset after the maximum number of unsuccessful login attempts is reached.
        Returns: Optional[int]
        """
        return self._password_minutes_until_failed_login_reset
    
    @password_minutes_until_failed_login_reset.setter
    def password_minutes_until_failed_login_reset(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinutesUntilFailedLoginReset property value. The number of minutes before the login is reset after the maximum number of unsuccessful login attempts is reached.
        Args:
            value: Value to set for the password_minutes_until_failed_login_reset property.
        """
        self._password_minutes_until_failed_login_reset = value
    
    @property
    def password_previous_password_block_count(self,) -> Optional[int]:
        """
        Gets the passwordPreviousPasswordBlockCount property value. Number of previous passwords to block.
        Returns: Optional[int]
        """
        return self._password_previous_password_block_count
    
    @password_previous_password_block_count.setter
    def password_previous_password_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordPreviousPasswordBlockCount property value. Number of previous passwords to block.
        Args:
            value: Value to set for the password_previous_password_block_count property.
        """
        self._password_previous_password_block_count = value
    
    @property
    def password_required(self,) -> Optional[bool]:
        """
        Gets the passwordRequired property value. Whether or not to require a password.
        Returns: Optional[bool]
        """
        return self._password_required
    
    @password_required.setter
    def password_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRequired property value. Whether or not to require a password.
        Args:
            value: Value to set for the password_required property.
        """
        self._password_required = value
    
    @property
    def password_required_type(self,) -> Optional[required_password_type.RequiredPasswordType]:
        """
        Gets the passwordRequiredType property value. Possible values of required passwords.
        Returns: Optional[required_password_type.RequiredPasswordType]
        """
        return self._password_required_type
    
    @password_required_type.setter
    def password_required_type(self,value: Optional[required_password_type.RequiredPasswordType] = None) -> None:
        """
        Sets the passwordRequiredType property value. Possible values of required passwords.
        Args:
            value: Value to set for the password_required_type property.
        """
        self._password_required_type = value
    
    @property
    def privacy_access_controls(self,) -> Optional[List[mac_o_s_privacy_access_control_item.MacOSPrivacyAccessControlItem]]:
        """
        Gets the privacyAccessControls property value. List of privacy preference policy controls. This collection can contain a maximum of 10000 elements.
        Returns: Optional[List[mac_o_s_privacy_access_control_item.MacOSPrivacyAccessControlItem]]
        """
        return self._privacy_access_controls
    
    @privacy_access_controls.setter
    def privacy_access_controls(self,value: Optional[List[mac_o_s_privacy_access_control_item.MacOSPrivacyAccessControlItem]] = None) -> None:
        """
        Sets the privacyAccessControls property value. List of privacy preference policy controls. This collection can contain a maximum of 10000 elements.
        Args:
            value: Value to set for the privacy_access_controls property.
        """
        self._privacy_access_controls = value
    
    @property
    def safari_block_autofill(self,) -> Optional[bool]:
        """
        Gets the safariBlockAutofill property value. Indicates whether or not to block the user from using Auto fill in Safari.
        Returns: Optional[bool]
        """
        return self._safari_block_autofill
    
    @safari_block_autofill.setter
    def safari_block_autofill(self,value: Optional[bool] = None) -> None:
        """
        Sets the safariBlockAutofill property value. Indicates whether or not to block the user from using Auto fill in Safari.
        Args:
            value: Value to set for the safari_block_autofill property.
        """
        self._safari_block_autofill = value
    
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
        writer.write_bool_value("activationLockWhenSupervisedAllowed", self.activation_lock_when_supervised_allowed)
        writer.write_bool_value("addingGameCenterFriendsBlocked", self.adding_game_center_friends_blocked)
        writer.write_bool_value("airDropBlocked", self.air_drop_blocked)
        writer.write_bool_value("appleWatchBlockAutoUnlock", self.apple_watch_block_auto_unlock)
        writer.write_bool_value("cameraBlocked", self.camera_blocked)
        writer.write_bool_value("classroomAppBlockRemoteScreenObservation", self.classroom_app_block_remote_screen_observation)
        writer.write_bool_value("classroomAppForceUnpromptedScreenObservation", self.classroom_app_force_unprompted_screen_observation)
        writer.write_bool_value("classroomForceAutomaticallyJoinClasses", self.classroom_force_automatically_join_classes)
        writer.write_bool_value("classroomForceRequestPermissionToLeaveClasses", self.classroom_force_request_permission_to_leave_classes)
        writer.write_bool_value("classroomForceUnpromptedAppAndDeviceLock", self.classroom_force_unprompted_app_and_device_lock)
        writer.write_collection_of_object_values("compliantAppsList", self.compliant_apps_list)
        writer.write_enum_value("compliantAppListType", self.compliant_app_list_type)
        writer.write_bool_value("contentCachingBlocked", self.content_caching_blocked)
        writer.write_bool_value("definitionLookupBlocked", self.definition_lookup_blocked)
        writer.write_collection_of_primitive_values("emailInDomainSuffixes", self.email_in_domain_suffixes)
        writer.write_bool_value("eraseContentAndSettingsBlocked", self.erase_content_and_settings_blocked)
        writer.write_bool_value("gameCenterBlocked", self.game_center_blocked)
        writer.write_bool_value("iCloudBlockActivityContinuation", self.i_cloud_block_activity_continuation)
        writer.write_bool_value("iCloudBlockAddressBook", self.i_cloud_block_address_book)
        writer.write_bool_value("iCloudBlockBookmarks", self.i_cloud_block_bookmarks)
        writer.write_bool_value("iCloudBlockCalendar", self.i_cloud_block_calendar)
        writer.write_bool_value("iCloudBlockDocumentSync", self.i_cloud_block_document_sync)
        writer.write_bool_value("iCloudBlockMail", self.i_cloud_block_mail)
        writer.write_bool_value("iCloudBlockNotes", self.i_cloud_block_notes)
        writer.write_bool_value("iCloudBlockPhotoLibrary", self.i_cloud_block_photo_library)
        writer.write_bool_value("iCloudBlockReminders", self.i_cloud_block_reminders)
        writer.write_bool_value("iCloudDesktopAndDocumentsBlocked", self.i_cloud_desktop_and_documents_blocked)
        writer.write_bool_value("iCloudPrivateRelayBlocked", self.i_cloud_private_relay_blocked)
        writer.write_bool_value("iTunesBlockFileSharing", self.i_tunes_block_file_sharing)
        writer.write_bool_value("iTunesBlockMusicService", self.i_tunes_block_music_service)
        writer.write_bool_value("keyboardBlockDictation", self.keyboard_block_dictation)
        writer.write_bool_value("keychainBlockCloudSync", self.keychain_block_cloud_sync)
        writer.write_bool_value("multiplayerGamingBlocked", self.multiplayer_gaming_blocked)
        writer.write_bool_value("passwordBlockAirDropSharing", self.password_block_air_drop_sharing)
        writer.write_bool_value("passwordBlockAutoFill", self.password_block_auto_fill)
        writer.write_bool_value("passwordBlockFingerprintUnlock", self.password_block_fingerprint_unlock)
        writer.write_bool_value("passwordBlockModification", self.password_block_modification)
        writer.write_bool_value("passwordBlockProximityRequests", self.password_block_proximity_requests)
        writer.write_bool_value("passwordBlockSimple", self.password_block_simple)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMaximumAttemptCount", self.password_maximum_attempt_count)
        writer.write_int_value("passwordMinimumCharacterSetCount", self.password_minimum_character_set_count)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeLock", self.password_minutes_of_inactivity_before_lock)
        writer.write_int_value("passwordMinutesOfInactivityBeforeScreenTimeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("passwordMinutesUntilFailedLoginReset", self.password_minutes_until_failed_login_reset)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_collection_of_object_values("privacyAccessControls", self.privacy_access_controls)
        writer.write_bool_value("safariBlockAutofill", self.safari_block_autofill)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_int_value("softwareUpdatesEnforcedDelayInDays", self.software_updates_enforced_delay_in_days)
        writer.write_int_value("softwareUpdateMajorOSDeferredInstallDelayInDays", self.software_update_major_o_s_deferred_install_delay_in_days)
        writer.write_int_value("softwareUpdateMinorOSDeferredInstallDelayInDays", self.software_update_minor_o_s_deferred_install_delay_in_days)
        writer.write_int_value("softwareUpdateNonOSDeferredInstallDelayInDays", self.software_update_non_o_s_deferred_install_delay_in_days)
        writer.write_bool_value("spotlightBlockInternetResults", self.spotlight_block_internet_results)
        writer.write_int_value("touchIdTimeoutInHours", self.touch_id_timeout_in_hours)
        writer.write_enum_value("updateDelayPolicy", self.update_delay_policy)
        writer.write_bool_value("wallpaperModificationBlocked", self.wallpaper_modification_blocked)
    
    @property
    def software_update_major_o_s_deferred_install_delay_in_days(self,) -> Optional[int]:
        """
        Gets the softwareUpdateMajorOSDeferredInstallDelayInDays property value. Specify the number of days (1-90) to delay visibility of major OS software updates. Available for devices running macOS versions 11.3 and later. Valid values 0 to 90
        Returns: Optional[int]
        """
        return self._software_update_major_o_s_deferred_install_delay_in_days
    
    @software_update_major_o_s_deferred_install_delay_in_days.setter
    def software_update_major_o_s_deferred_install_delay_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the softwareUpdateMajorOSDeferredInstallDelayInDays property value. Specify the number of days (1-90) to delay visibility of major OS software updates. Available for devices running macOS versions 11.3 and later. Valid values 0 to 90
        Args:
            value: Value to set for the software_update_major_o_s_deferred_install_delay_in_days property.
        """
        self._software_update_major_o_s_deferred_install_delay_in_days = value
    
    @property
    def software_update_minor_o_s_deferred_install_delay_in_days(self,) -> Optional[int]:
        """
        Gets the softwareUpdateMinorOSDeferredInstallDelayInDays property value. Specify the number of days (1-90) to delay visibility of minor OS software updates. Available for devices running macOS versions 11.3 and later. Valid values 0 to 90
        Returns: Optional[int]
        """
        return self._software_update_minor_o_s_deferred_install_delay_in_days
    
    @software_update_minor_o_s_deferred_install_delay_in_days.setter
    def software_update_minor_o_s_deferred_install_delay_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the softwareUpdateMinorOSDeferredInstallDelayInDays property value. Specify the number of days (1-90) to delay visibility of minor OS software updates. Available for devices running macOS versions 11.3 and later. Valid values 0 to 90
        Args:
            value: Value to set for the software_update_minor_o_s_deferred_install_delay_in_days property.
        """
        self._software_update_minor_o_s_deferred_install_delay_in_days = value
    
    @property
    def software_update_non_o_s_deferred_install_delay_in_days(self,) -> Optional[int]:
        """
        Gets the softwareUpdateNonOSDeferredInstallDelayInDays property value. Specify the number of days (1-90) to delay visibility of non-OS software updates. Available for devices running macOS versions 11.3 and later. Valid values 0 to 90
        Returns: Optional[int]
        """
        return self._software_update_non_o_s_deferred_install_delay_in_days
    
    @software_update_non_o_s_deferred_install_delay_in_days.setter
    def software_update_non_o_s_deferred_install_delay_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the softwareUpdateNonOSDeferredInstallDelayInDays property value. Specify the number of days (1-90) to delay visibility of non-OS software updates. Available for devices running macOS versions 11.3 and later. Valid values 0 to 90
        Args:
            value: Value to set for the software_update_non_o_s_deferred_install_delay_in_days property.
        """
        self._software_update_non_o_s_deferred_install_delay_in_days = value
    
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
    def spotlight_block_internet_results(self,) -> Optional[bool]:
        """
        Gets the spotlightBlockInternetResults property value. Indicates whether or not to block Spotlight from returning any results from an Internet search.
        Returns: Optional[bool]
        """
        return self._spotlight_block_internet_results
    
    @spotlight_block_internet_results.setter
    def spotlight_block_internet_results(self,value: Optional[bool] = None) -> None:
        """
        Sets the spotlightBlockInternetResults property value. Indicates whether or not to block Spotlight from returning any results from an Internet search.
        Args:
            value: Value to set for the spotlight_block_internet_results property.
        """
        self._spotlight_block_internet_results = value
    
    @property
    def touch_id_timeout_in_hours(self,) -> Optional[int]:
        """
        Gets the touchIdTimeoutInHours property value. Maximum hours after which the user must enter their password to unlock the device instead of using Touch ID. Available for devices running macOS 12 and later. Valid values 0 to 2147483647
        Returns: Optional[int]
        """
        return self._touch_id_timeout_in_hours
    
    @touch_id_timeout_in_hours.setter
    def touch_id_timeout_in_hours(self,value: Optional[int] = None) -> None:
        """
        Sets the touchIdTimeoutInHours property value. Maximum hours after which the user must enter their password to unlock the device instead of using Touch ID. Available for devices running macOS 12 and later. Valid values 0 to 2147483647
        Args:
            value: Value to set for the touch_id_timeout_in_hours property.
        """
        self._touch_id_timeout_in_hours = value
    
    @property
    def update_delay_policy(self,) -> Optional[mac_o_s_software_update_delay_policy.MacOSSoftwareUpdateDelayPolicy]:
        """
        Gets the updateDelayPolicy property value. Determines whether to delay OS and/or app updates for macOS. Possible values are: none, delayOSUpdateVisibility, delayAppUpdateVisibility, unknownFutureValue, delayMajorOsUpdateVisibility.
        Returns: Optional[mac_o_s_software_update_delay_policy.MacOSSoftwareUpdateDelayPolicy]
        """
        return self._update_delay_policy
    
    @update_delay_policy.setter
    def update_delay_policy(self,value: Optional[mac_o_s_software_update_delay_policy.MacOSSoftwareUpdateDelayPolicy] = None) -> None:
        """
        Sets the updateDelayPolicy property value. Determines whether to delay OS and/or app updates for macOS. Possible values are: none, delayOSUpdateVisibility, delayAppUpdateVisibility, unknownFutureValue, delayMajorOsUpdateVisibility.
        Args:
            value: Value to set for the update_delay_policy property.
        """
        self._update_delay_policy = value
    
    @property
    def wallpaper_modification_blocked(self,) -> Optional[bool]:
        """
        Gets the wallpaperModificationBlocked property value. TRUE prevents the wallpaper from being changed. FALSE allows the wallpaper to be changed. Available for devices running macOS versions 10.13 and later.
        Returns: Optional[bool]
        """
        return self._wallpaper_modification_blocked
    
    @wallpaper_modification_blocked.setter
    def wallpaper_modification_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the wallpaperModificationBlocked property value. TRUE prevents the wallpaper from being changed. FALSE allows the wallpaper to be changed. Available for devices running macOS versions 10.13 and later.
        Args:
            value: Value to set for the wallpaper_modification_blocked property.
        """
        self._wallpaper_modification_blocked = value
    

