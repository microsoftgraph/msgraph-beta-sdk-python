from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_required_password_complexity = lazy_import('msgraph.generated.models.android_required_password_complexity')
android_work_profile_cross_profile_data_sharing_type = lazy_import('msgraph.generated.models.android_work_profile_cross_profile_data_sharing_type')
android_work_profile_default_app_permission_policy_type = lazy_import('msgraph.generated.models.android_work_profile_default_app_permission_policy_type')
android_work_profile_required_password_type = lazy_import('msgraph.generated.models.android_work_profile_required_password_type')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class AndroidWorkProfileGeneralDeviceConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidWorkProfileGeneralDeviceConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration"
        # Indicates whether or not to block face unlock.
        self._password_block_face_unlock: Optional[bool] = None
        # Indicates whether or not to block fingerprint unlock.
        self._password_block_fingerprint_unlock: Optional[bool] = None
        # Indicates whether or not to block iris unlock.
        self._password_block_iris_unlock: Optional[bool] = None
        # Indicates whether or not to block Smart Lock and other trust agents.
        self._password_block_trust_agents: Optional[bool] = None
        # Number of days before the password expires. Valid values 1 to 365
        self._password_expiration_days: Optional[int] = None
        # Minimum length of passwords. Valid values 4 to 16
        self._password_minimum_length: Optional[int] = None
        # Minutes of inactivity before the screen times out.
        self._password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
        # Number of previous passwords to block. Valid values 0 to 24
        self._password_previous_password_block_count: Optional[int] = None
        # Android Work Profile required password type.
        self._password_required_type: Optional[android_work_profile_required_password_type.AndroidWorkProfileRequiredPasswordType] = None
        # Number of sign in failures allowed before factory reset. Valid values 1 to 16
        self._password_sign_in_failure_count_before_factory_reset: Optional[int] = None
        # The password complexity types that can be set on Android. One of: NONE, LOW, MEDIUM, HIGH. This is an API targeted to Android 11+.
        self._required_password_complexity: Optional[android_required_password_complexity.AndroidRequiredPasswordComplexity] = None
        # Require the Android Verify apps feature is turned on.
        self._security_require_verify_apps: Optional[bool] = None
        # Enable lockdown mode for always-on VPN.
        self._vpn_always_on_package_identifier: Optional[str] = None
        # Enable lockdown mode for always-on VPN.
        self._vpn_enable_always_on_lockdown_mode: Optional[bool] = None
        # Indicates whether to allow installation of apps from unknown sources.
        self._work_profile_allow_app_installs_from_unknown_sources: Optional[bool] = None
        # Allow widgets from work profile apps.
        self._work_profile_allow_widgets: Optional[bool] = None
        # Block users from adding/removing accounts in work profile.
        self._work_profile_block_adding_accounts: Optional[bool] = None
        # Block work profile camera.
        self._work_profile_block_camera: Optional[bool] = None
        # Block display work profile caller ID in personal profile.
        self._work_profile_block_cross_profile_caller_id: Optional[bool] = None
        # Block work profile contacts availability in personal profile.
        self._work_profile_block_cross_profile_contacts_search: Optional[bool] = None
        # Boolean that indicates if the setting disallow cross profile copy/paste is enabled.
        self._work_profile_block_cross_profile_copy_paste: Optional[bool] = None
        # Indicates whether or not to block notifications while device locked.
        self._work_profile_block_notifications_while_device_locked: Optional[bool] = None
        # Prevent app installations from unknown sources in the personal profile.
        self._work_profile_block_personal_app_installs_from_unknown_sources: Optional[bool] = None
        # Block screen capture in work profile.
        self._work_profile_block_screen_capture: Optional[bool] = None
        # Allow bluetooth devices to access enterprise contacts.
        self._work_profile_bluetooth_enable_contact_sharing: Optional[bool] = None
        # Android Work Profile cross profile data sharing type.
        self._work_profile_data_sharing_type: Optional[android_work_profile_cross_profile_data_sharing_type.AndroidWorkProfileCrossProfileDataSharingType] = None
        # Android Work Profile default app permission policy type.
        self._work_profile_default_app_permission_policy: Optional[android_work_profile_default_app_permission_policy_type.AndroidWorkProfileDefaultAppPermissionPolicyType] = None
        # Indicates whether or not to block face unlock for work profile.
        self._work_profile_password_block_face_unlock: Optional[bool] = None
        # Indicates whether or not to block fingerprint unlock for work profile.
        self._work_profile_password_block_fingerprint_unlock: Optional[bool] = None
        # Indicates whether or not to block iris unlock for work profile.
        self._work_profile_password_block_iris_unlock: Optional[bool] = None
        # Indicates whether or not to block Smart Lock and other trust agents for work profile.
        self._work_profile_password_block_trust_agents: Optional[bool] = None
        # Number of days before the work profile password expires. Valid values 1 to 365
        self._work_profile_password_expiration_days: Optional[int] = None
        # Minimum # of letter characters required in work profile password. Valid values 1 to 10
        self._work_profile_password_min_letter_characters: Optional[int] = None
        # Minimum # of lower-case characters required in work profile password. Valid values 1 to 10
        self._work_profile_password_min_lower_case_characters: Optional[int] = None
        # Minimum # of non-letter characters required in work profile password. Valid values 1 to 10
        self._work_profile_password_min_non_letter_characters: Optional[int] = None
        # Minimum # of numeric characters required in work profile password. Valid values 1 to 10
        self._work_profile_password_min_numeric_characters: Optional[int] = None
        # Minimum # of symbols required in work profile password. Valid values 1 to 10
        self._work_profile_password_min_symbol_characters: Optional[int] = None
        # Minimum # of upper-case characters required in work profile password. Valid values 1 to 10
        self._work_profile_password_min_upper_case_characters: Optional[int] = None
        # Minimum length of work profile password. Valid values 4 to 16
        self._work_profile_password_minimum_length: Optional[int] = None
        # Minutes of inactivity before the screen times out.
        self._work_profile_password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
        # Number of previous work profile passwords to block. Valid values 0 to 24
        self._work_profile_password_previous_password_block_count: Optional[int] = None
        # Android Work Profile required password type.
        self._work_profile_password_required_type: Optional[android_work_profile_required_password_type.AndroidWorkProfileRequiredPasswordType] = None
        # Number of sign in failures allowed before work profile is removed and all corporate data deleted. Valid values 1 to 16
        self._work_profile_password_sign_in_failure_count_before_factory_reset: Optional[int] = None
        # Password is required or not for work profile
        self._work_profile_require_password: Optional[bool] = None
        # The password complexity types that can be set on Android. One of: NONE, LOW, MEDIUM, HIGH. This is an API targeted to Android 11+.
        self._work_profile_required_password_complexity: Optional[android_required_password_complexity.AndroidRequiredPasswordComplexity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidWorkProfileGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidWorkProfileGeneralDeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidWorkProfileGeneralDeviceConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "passwordBlockFaceUnlock": lambda n : setattr(self, 'password_block_face_unlock', n.get_bool_value()),
            "passwordBlockFingerprintUnlock": lambda n : setattr(self, 'password_block_fingerprint_unlock', n.get_bool_value()),
            "passwordBlockIrisUnlock": lambda n : setattr(self, 'password_block_iris_unlock', n.get_bool_value()),
            "passwordBlockTrustAgents": lambda n : setattr(self, 'password_block_trust_agents', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(android_work_profile_required_password_type.AndroidWorkProfileRequiredPasswordType)),
            "passwordSignInFailureCountBeforeFactoryReset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "requiredPasswordComplexity": lambda n : setattr(self, 'required_password_complexity', n.get_enum_value(android_required_password_complexity.AndroidRequiredPasswordComplexity)),
            "securityRequireVerifyApps": lambda n : setattr(self, 'security_require_verify_apps', n.get_bool_value()),
            "vpnAlwaysOnPackageIdentifier": lambda n : setattr(self, 'vpn_always_on_package_identifier', n.get_str_value()),
            "vpnEnableAlwaysOnLockdownMode": lambda n : setattr(self, 'vpn_enable_always_on_lockdown_mode', n.get_bool_value()),
            "workProfileAllowAppInstallsFromUnknownSources": lambda n : setattr(self, 'work_profile_allow_app_installs_from_unknown_sources', n.get_bool_value()),
            "workProfileAllowWidgets": lambda n : setattr(self, 'work_profile_allow_widgets', n.get_bool_value()),
            "workProfileBlockAddingAccounts": lambda n : setattr(self, 'work_profile_block_adding_accounts', n.get_bool_value()),
            "workProfileBlockCamera": lambda n : setattr(self, 'work_profile_block_camera', n.get_bool_value()),
            "workProfileBlockCrossProfileCallerId": lambda n : setattr(self, 'work_profile_block_cross_profile_caller_id', n.get_bool_value()),
            "workProfileBlockCrossProfileContactsSearch": lambda n : setattr(self, 'work_profile_block_cross_profile_contacts_search', n.get_bool_value()),
            "workProfileBlockCrossProfileCopyPaste": lambda n : setattr(self, 'work_profile_block_cross_profile_copy_paste', n.get_bool_value()),
            "workProfileBlockNotificationsWhileDeviceLocked": lambda n : setattr(self, 'work_profile_block_notifications_while_device_locked', n.get_bool_value()),
            "workProfileBlockPersonalAppInstallsFromUnknownSources": lambda n : setattr(self, 'work_profile_block_personal_app_installs_from_unknown_sources', n.get_bool_value()),
            "workProfileBlockScreenCapture": lambda n : setattr(self, 'work_profile_block_screen_capture', n.get_bool_value()),
            "workProfileBluetoothEnableContactSharing": lambda n : setattr(self, 'work_profile_bluetooth_enable_contact_sharing', n.get_bool_value()),
            "workProfileDataSharingType": lambda n : setattr(self, 'work_profile_data_sharing_type', n.get_enum_value(android_work_profile_cross_profile_data_sharing_type.AndroidWorkProfileCrossProfileDataSharingType)),
            "workProfileDefaultAppPermissionPolicy": lambda n : setattr(self, 'work_profile_default_app_permission_policy', n.get_enum_value(android_work_profile_default_app_permission_policy_type.AndroidWorkProfileDefaultAppPermissionPolicyType)),
            "workProfilePasswordBlockFaceUnlock": lambda n : setattr(self, 'work_profile_password_block_face_unlock', n.get_bool_value()),
            "workProfilePasswordBlockFingerprintUnlock": lambda n : setattr(self, 'work_profile_password_block_fingerprint_unlock', n.get_bool_value()),
            "workProfilePasswordBlockIrisUnlock": lambda n : setattr(self, 'work_profile_password_block_iris_unlock', n.get_bool_value()),
            "workProfilePasswordBlockTrustAgents": lambda n : setattr(self, 'work_profile_password_block_trust_agents', n.get_bool_value()),
            "workProfilePasswordExpirationDays": lambda n : setattr(self, 'work_profile_password_expiration_days', n.get_int_value()),
            "workProfilePasswordMinimumLength": lambda n : setattr(self, 'work_profile_password_minimum_length', n.get_int_value()),
            "workProfilePasswordMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'work_profile_password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "workProfilePasswordMinLetterCharacters": lambda n : setattr(self, 'work_profile_password_min_letter_characters', n.get_int_value()),
            "workProfilePasswordMinLowerCaseCharacters": lambda n : setattr(self, 'work_profile_password_min_lower_case_characters', n.get_int_value()),
            "workProfilePasswordMinNonLetterCharacters": lambda n : setattr(self, 'work_profile_password_min_non_letter_characters', n.get_int_value()),
            "workProfilePasswordMinNumericCharacters": lambda n : setattr(self, 'work_profile_password_min_numeric_characters', n.get_int_value()),
            "workProfilePasswordMinSymbolCharacters": lambda n : setattr(self, 'work_profile_password_min_symbol_characters', n.get_int_value()),
            "workProfilePasswordMinUpperCaseCharacters": lambda n : setattr(self, 'work_profile_password_min_upper_case_characters', n.get_int_value()),
            "workProfilePasswordPreviousPasswordBlockCount": lambda n : setattr(self, 'work_profile_password_previous_password_block_count', n.get_int_value()),
            "workProfilePasswordRequiredType": lambda n : setattr(self, 'work_profile_password_required_type', n.get_enum_value(android_work_profile_required_password_type.AndroidWorkProfileRequiredPasswordType)),
            "workProfilePasswordSignInFailureCountBeforeFactoryReset": lambda n : setattr(self, 'work_profile_password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "workProfileRequiredPasswordComplexity": lambda n : setattr(self, 'work_profile_required_password_complexity', n.get_enum_value(android_required_password_complexity.AndroidRequiredPasswordComplexity)),
            "workProfileRequirePassword": lambda n : setattr(self, 'work_profile_require_password', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def password_block_face_unlock(self,) -> Optional[bool]:
        """
        Gets the passwordBlockFaceUnlock property value. Indicates whether or not to block face unlock.
        Returns: Optional[bool]
        """
        return self._password_block_face_unlock
    
    @password_block_face_unlock.setter
    def password_block_face_unlock(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockFaceUnlock property value. Indicates whether or not to block face unlock.
        Args:
            value: Value to set for the password_block_face_unlock property.
        """
        self._password_block_face_unlock = value
    
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
    def password_block_iris_unlock(self,) -> Optional[bool]:
        """
        Gets the passwordBlockIrisUnlock property value. Indicates whether or not to block iris unlock.
        Returns: Optional[bool]
        """
        return self._password_block_iris_unlock
    
    @password_block_iris_unlock.setter
    def password_block_iris_unlock(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockIrisUnlock property value. Indicates whether or not to block iris unlock.
        Args:
            value: Value to set for the password_block_iris_unlock property.
        """
        self._password_block_iris_unlock = value
    
    @property
    def password_block_trust_agents(self,) -> Optional[bool]:
        """
        Gets the passwordBlockTrustAgents property value. Indicates whether or not to block Smart Lock and other trust agents.
        Returns: Optional[bool]
        """
        return self._password_block_trust_agents
    
    @password_block_trust_agents.setter
    def password_block_trust_agents(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockTrustAgents property value. Indicates whether or not to block Smart Lock and other trust agents.
        Args:
            value: Value to set for the password_block_trust_agents property.
        """
        self._password_block_trust_agents = value
    
    @property
    def password_expiration_days(self,) -> Optional[int]:
        """
        Gets the passwordExpirationDays property value. Number of days before the password expires. Valid values 1 to 365
        Returns: Optional[int]
        """
        return self._password_expiration_days
    
    @password_expiration_days.setter
    def password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordExpirationDays property value. Number of days before the password expires. Valid values 1 to 365
        Args:
            value: Value to set for the password_expiration_days property.
        """
        self._password_expiration_days = value
    
    @property
    def password_minimum_length(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLength property value. Minimum length of passwords. Valid values 4 to 16
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. Minimum length of passwords. Valid values 4 to 16
        Args:
            value: Value to set for the password_minimum_length property.
        """
        self._password_minimum_length = value
    
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
            value: Value to set for the password_minutes_of_inactivity_before_screen_timeout property.
        """
        self._password_minutes_of_inactivity_before_screen_timeout = value
    
    @property
    def password_previous_password_block_count(self,) -> Optional[int]:
        """
        Gets the passwordPreviousPasswordBlockCount property value. Number of previous passwords to block. Valid values 0 to 24
        Returns: Optional[int]
        """
        return self._password_previous_password_block_count
    
    @password_previous_password_block_count.setter
    def password_previous_password_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordPreviousPasswordBlockCount property value. Number of previous passwords to block. Valid values 0 to 24
        Args:
            value: Value to set for the password_previous_password_block_count property.
        """
        self._password_previous_password_block_count = value
    
    @property
    def password_required_type(self,) -> Optional[android_work_profile_required_password_type.AndroidWorkProfileRequiredPasswordType]:
        """
        Gets the passwordRequiredType property value. Android Work Profile required password type.
        Returns: Optional[android_work_profile_required_password_type.AndroidWorkProfileRequiredPasswordType]
        """
        return self._password_required_type
    
    @password_required_type.setter
    def password_required_type(self,value: Optional[android_work_profile_required_password_type.AndroidWorkProfileRequiredPasswordType] = None) -> None:
        """
        Sets the passwordRequiredType property value. Android Work Profile required password type.
        Args:
            value: Value to set for the password_required_type property.
        """
        self._password_required_type = value
    
    @property
    def password_sign_in_failure_count_before_factory_reset(self,) -> Optional[int]:
        """
        Gets the passwordSignInFailureCountBeforeFactoryReset property value. Number of sign in failures allowed before factory reset. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._password_sign_in_failure_count_before_factory_reset
    
    @password_sign_in_failure_count_before_factory_reset.setter
    def password_sign_in_failure_count_before_factory_reset(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordSignInFailureCountBeforeFactoryReset property value. Number of sign in failures allowed before factory reset. Valid values 1 to 16
        Args:
            value: Value to set for the password_sign_in_failure_count_before_factory_reset property.
        """
        self._password_sign_in_failure_count_before_factory_reset = value
    
    @property
    def required_password_complexity(self,) -> Optional[android_required_password_complexity.AndroidRequiredPasswordComplexity]:
        """
        Gets the requiredPasswordComplexity property value. The password complexity types that can be set on Android. One of: NONE, LOW, MEDIUM, HIGH. This is an API targeted to Android 11+.
        Returns: Optional[android_required_password_complexity.AndroidRequiredPasswordComplexity]
        """
        return self._required_password_complexity
    
    @required_password_complexity.setter
    def required_password_complexity(self,value: Optional[android_required_password_complexity.AndroidRequiredPasswordComplexity] = None) -> None:
        """
        Sets the requiredPasswordComplexity property value. The password complexity types that can be set on Android. One of: NONE, LOW, MEDIUM, HIGH. This is an API targeted to Android 11+.
        Args:
            value: Value to set for the required_password_complexity property.
        """
        self._required_password_complexity = value
    
    @property
    def security_require_verify_apps(self,) -> Optional[bool]:
        """
        Gets the securityRequireVerifyApps property value. Require the Android Verify apps feature is turned on.
        Returns: Optional[bool]
        """
        return self._security_require_verify_apps
    
    @security_require_verify_apps.setter
    def security_require_verify_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityRequireVerifyApps property value. Require the Android Verify apps feature is turned on.
        Args:
            value: Value to set for the security_require_verify_apps property.
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
        writer.write_bool_value("passwordBlockFaceUnlock", self.password_block_face_unlock)
        writer.write_bool_value("passwordBlockFingerprintUnlock", self.password_block_fingerprint_unlock)
        writer.write_bool_value("passwordBlockIrisUnlock", self.password_block_iris_unlock)
        writer.write_bool_value("passwordBlockTrustAgents", self.password_block_trust_agents)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeScreenTimeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_int_value("passwordSignInFailureCountBeforeFactoryReset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_enum_value("requiredPasswordComplexity", self.required_password_complexity)
        writer.write_bool_value("securityRequireVerifyApps", self.security_require_verify_apps)
        writer.write_str_value("vpnAlwaysOnPackageIdentifier", self.vpn_always_on_package_identifier)
        writer.write_bool_value("vpnEnableAlwaysOnLockdownMode", self.vpn_enable_always_on_lockdown_mode)
        writer.write_bool_value("workProfileAllowAppInstallsFromUnknownSources", self.work_profile_allow_app_installs_from_unknown_sources)
        writer.write_bool_value("workProfileAllowWidgets", self.work_profile_allow_widgets)
        writer.write_bool_value("workProfileBlockAddingAccounts", self.work_profile_block_adding_accounts)
        writer.write_bool_value("workProfileBlockCamera", self.work_profile_block_camera)
        writer.write_bool_value("workProfileBlockCrossProfileCallerId", self.work_profile_block_cross_profile_caller_id)
        writer.write_bool_value("workProfileBlockCrossProfileContactsSearch", self.work_profile_block_cross_profile_contacts_search)
        writer.write_bool_value("workProfileBlockCrossProfileCopyPaste", self.work_profile_block_cross_profile_copy_paste)
        writer.write_bool_value("workProfileBlockNotificationsWhileDeviceLocked", self.work_profile_block_notifications_while_device_locked)
        writer.write_bool_value("workProfileBlockPersonalAppInstallsFromUnknownSources", self.work_profile_block_personal_app_installs_from_unknown_sources)
        writer.write_bool_value("workProfileBlockScreenCapture", self.work_profile_block_screen_capture)
        writer.write_bool_value("workProfileBluetoothEnableContactSharing", self.work_profile_bluetooth_enable_contact_sharing)
        writer.write_enum_value("workProfileDataSharingType", self.work_profile_data_sharing_type)
        writer.write_enum_value("workProfileDefaultAppPermissionPolicy", self.work_profile_default_app_permission_policy)
        writer.write_bool_value("workProfilePasswordBlockFaceUnlock", self.work_profile_password_block_face_unlock)
        writer.write_bool_value("workProfilePasswordBlockFingerprintUnlock", self.work_profile_password_block_fingerprint_unlock)
        writer.write_bool_value("workProfilePasswordBlockIrisUnlock", self.work_profile_password_block_iris_unlock)
        writer.write_bool_value("workProfilePasswordBlockTrustAgents", self.work_profile_password_block_trust_agents)
        writer.write_int_value("workProfilePasswordExpirationDays", self.work_profile_password_expiration_days)
        writer.write_int_value("workProfilePasswordMinimumLength", self.work_profile_password_minimum_length)
        writer.write_int_value("workProfilePasswordMinutesOfInactivityBeforeScreenTimeout", self.work_profile_password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("workProfilePasswordMinLetterCharacters", self.work_profile_password_min_letter_characters)
        writer.write_int_value("workProfilePasswordMinLowerCaseCharacters", self.work_profile_password_min_lower_case_characters)
        writer.write_int_value("workProfilePasswordMinNonLetterCharacters", self.work_profile_password_min_non_letter_characters)
        writer.write_int_value("workProfilePasswordMinNumericCharacters", self.work_profile_password_min_numeric_characters)
        writer.write_int_value("workProfilePasswordMinSymbolCharacters", self.work_profile_password_min_symbol_characters)
        writer.write_int_value("workProfilePasswordMinUpperCaseCharacters", self.work_profile_password_min_upper_case_characters)
        writer.write_int_value("workProfilePasswordPreviousPasswordBlockCount", self.work_profile_password_previous_password_block_count)
        writer.write_enum_value("workProfilePasswordRequiredType", self.work_profile_password_required_type)
        writer.write_int_value("workProfilePasswordSignInFailureCountBeforeFactoryReset", self.work_profile_password_sign_in_failure_count_before_factory_reset)
        writer.write_enum_value("workProfileRequiredPasswordComplexity", self.work_profile_required_password_complexity)
        writer.write_bool_value("workProfileRequirePassword", self.work_profile_require_password)
    
    @property
    def vpn_always_on_package_identifier(self,) -> Optional[str]:
        """
        Gets the vpnAlwaysOnPackageIdentifier property value. Enable lockdown mode for always-on VPN.
        Returns: Optional[str]
        """
        return self._vpn_always_on_package_identifier
    
    @vpn_always_on_package_identifier.setter
    def vpn_always_on_package_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the vpnAlwaysOnPackageIdentifier property value. Enable lockdown mode for always-on VPN.
        Args:
            value: Value to set for the vpn_always_on_package_identifier property.
        """
        self._vpn_always_on_package_identifier = value
    
    @property
    def vpn_enable_always_on_lockdown_mode(self,) -> Optional[bool]:
        """
        Gets the vpnEnableAlwaysOnLockdownMode property value. Enable lockdown mode for always-on VPN.
        Returns: Optional[bool]
        """
        return self._vpn_enable_always_on_lockdown_mode
    
    @vpn_enable_always_on_lockdown_mode.setter
    def vpn_enable_always_on_lockdown_mode(self,value: Optional[bool] = None) -> None:
        """
        Sets the vpnEnableAlwaysOnLockdownMode property value. Enable lockdown mode for always-on VPN.
        Args:
            value: Value to set for the vpn_enable_always_on_lockdown_mode property.
        """
        self._vpn_enable_always_on_lockdown_mode = value
    
    @property
    def work_profile_allow_app_installs_from_unknown_sources(self,) -> Optional[bool]:
        """
        Gets the workProfileAllowAppInstallsFromUnknownSources property value. Indicates whether to allow installation of apps from unknown sources.
        Returns: Optional[bool]
        """
        return self._work_profile_allow_app_installs_from_unknown_sources
    
    @work_profile_allow_app_installs_from_unknown_sources.setter
    def work_profile_allow_app_installs_from_unknown_sources(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfileAllowAppInstallsFromUnknownSources property value. Indicates whether to allow installation of apps from unknown sources.
        Args:
            value: Value to set for the work_profile_allow_app_installs_from_unknown_sources property.
        """
        self._work_profile_allow_app_installs_from_unknown_sources = value
    
    @property
    def work_profile_allow_widgets(self,) -> Optional[bool]:
        """
        Gets the workProfileAllowWidgets property value. Allow widgets from work profile apps.
        Returns: Optional[bool]
        """
        return self._work_profile_allow_widgets
    
    @work_profile_allow_widgets.setter
    def work_profile_allow_widgets(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfileAllowWidgets property value. Allow widgets from work profile apps.
        Args:
            value: Value to set for the work_profile_allow_widgets property.
        """
        self._work_profile_allow_widgets = value
    
    @property
    def work_profile_block_adding_accounts(self,) -> Optional[bool]:
        """
        Gets the workProfileBlockAddingAccounts property value. Block users from adding/removing accounts in work profile.
        Returns: Optional[bool]
        """
        return self._work_profile_block_adding_accounts
    
    @work_profile_block_adding_accounts.setter
    def work_profile_block_adding_accounts(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfileBlockAddingAccounts property value. Block users from adding/removing accounts in work profile.
        Args:
            value: Value to set for the work_profile_block_adding_accounts property.
        """
        self._work_profile_block_adding_accounts = value
    
    @property
    def work_profile_block_camera(self,) -> Optional[bool]:
        """
        Gets the workProfileBlockCamera property value. Block work profile camera.
        Returns: Optional[bool]
        """
        return self._work_profile_block_camera
    
    @work_profile_block_camera.setter
    def work_profile_block_camera(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfileBlockCamera property value. Block work profile camera.
        Args:
            value: Value to set for the work_profile_block_camera property.
        """
        self._work_profile_block_camera = value
    
    @property
    def work_profile_block_cross_profile_caller_id(self,) -> Optional[bool]:
        """
        Gets the workProfileBlockCrossProfileCallerId property value. Block display work profile caller ID in personal profile.
        Returns: Optional[bool]
        """
        return self._work_profile_block_cross_profile_caller_id
    
    @work_profile_block_cross_profile_caller_id.setter
    def work_profile_block_cross_profile_caller_id(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfileBlockCrossProfileCallerId property value. Block display work profile caller ID in personal profile.
        Args:
            value: Value to set for the work_profile_block_cross_profile_caller_id property.
        """
        self._work_profile_block_cross_profile_caller_id = value
    
    @property
    def work_profile_block_cross_profile_contacts_search(self,) -> Optional[bool]:
        """
        Gets the workProfileBlockCrossProfileContactsSearch property value. Block work profile contacts availability in personal profile.
        Returns: Optional[bool]
        """
        return self._work_profile_block_cross_profile_contacts_search
    
    @work_profile_block_cross_profile_contacts_search.setter
    def work_profile_block_cross_profile_contacts_search(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfileBlockCrossProfileContactsSearch property value. Block work profile contacts availability in personal profile.
        Args:
            value: Value to set for the work_profile_block_cross_profile_contacts_search property.
        """
        self._work_profile_block_cross_profile_contacts_search = value
    
    @property
    def work_profile_block_cross_profile_copy_paste(self,) -> Optional[bool]:
        """
        Gets the workProfileBlockCrossProfileCopyPaste property value. Boolean that indicates if the setting disallow cross profile copy/paste is enabled.
        Returns: Optional[bool]
        """
        return self._work_profile_block_cross_profile_copy_paste
    
    @work_profile_block_cross_profile_copy_paste.setter
    def work_profile_block_cross_profile_copy_paste(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfileBlockCrossProfileCopyPaste property value. Boolean that indicates if the setting disallow cross profile copy/paste is enabled.
        Args:
            value: Value to set for the work_profile_block_cross_profile_copy_paste property.
        """
        self._work_profile_block_cross_profile_copy_paste = value
    
    @property
    def work_profile_block_notifications_while_device_locked(self,) -> Optional[bool]:
        """
        Gets the workProfileBlockNotificationsWhileDeviceLocked property value. Indicates whether or not to block notifications while device locked.
        Returns: Optional[bool]
        """
        return self._work_profile_block_notifications_while_device_locked
    
    @work_profile_block_notifications_while_device_locked.setter
    def work_profile_block_notifications_while_device_locked(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfileBlockNotificationsWhileDeviceLocked property value. Indicates whether or not to block notifications while device locked.
        Args:
            value: Value to set for the work_profile_block_notifications_while_device_locked property.
        """
        self._work_profile_block_notifications_while_device_locked = value
    
    @property
    def work_profile_block_personal_app_installs_from_unknown_sources(self,) -> Optional[bool]:
        """
        Gets the workProfileBlockPersonalAppInstallsFromUnknownSources property value. Prevent app installations from unknown sources in the personal profile.
        Returns: Optional[bool]
        """
        return self._work_profile_block_personal_app_installs_from_unknown_sources
    
    @work_profile_block_personal_app_installs_from_unknown_sources.setter
    def work_profile_block_personal_app_installs_from_unknown_sources(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfileBlockPersonalAppInstallsFromUnknownSources property value. Prevent app installations from unknown sources in the personal profile.
        Args:
            value: Value to set for the work_profile_block_personal_app_installs_from_unknown_sources property.
        """
        self._work_profile_block_personal_app_installs_from_unknown_sources = value
    
    @property
    def work_profile_block_screen_capture(self,) -> Optional[bool]:
        """
        Gets the workProfileBlockScreenCapture property value. Block screen capture in work profile.
        Returns: Optional[bool]
        """
        return self._work_profile_block_screen_capture
    
    @work_profile_block_screen_capture.setter
    def work_profile_block_screen_capture(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfileBlockScreenCapture property value. Block screen capture in work profile.
        Args:
            value: Value to set for the work_profile_block_screen_capture property.
        """
        self._work_profile_block_screen_capture = value
    
    @property
    def work_profile_bluetooth_enable_contact_sharing(self,) -> Optional[bool]:
        """
        Gets the workProfileBluetoothEnableContactSharing property value. Allow bluetooth devices to access enterprise contacts.
        Returns: Optional[bool]
        """
        return self._work_profile_bluetooth_enable_contact_sharing
    
    @work_profile_bluetooth_enable_contact_sharing.setter
    def work_profile_bluetooth_enable_contact_sharing(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfileBluetoothEnableContactSharing property value. Allow bluetooth devices to access enterprise contacts.
        Args:
            value: Value to set for the work_profile_bluetooth_enable_contact_sharing property.
        """
        self._work_profile_bluetooth_enable_contact_sharing = value
    
    @property
    def work_profile_data_sharing_type(self,) -> Optional[android_work_profile_cross_profile_data_sharing_type.AndroidWorkProfileCrossProfileDataSharingType]:
        """
        Gets the workProfileDataSharingType property value. Android Work Profile cross profile data sharing type.
        Returns: Optional[android_work_profile_cross_profile_data_sharing_type.AndroidWorkProfileCrossProfileDataSharingType]
        """
        return self._work_profile_data_sharing_type
    
    @work_profile_data_sharing_type.setter
    def work_profile_data_sharing_type(self,value: Optional[android_work_profile_cross_profile_data_sharing_type.AndroidWorkProfileCrossProfileDataSharingType] = None) -> None:
        """
        Sets the workProfileDataSharingType property value. Android Work Profile cross profile data sharing type.
        Args:
            value: Value to set for the work_profile_data_sharing_type property.
        """
        self._work_profile_data_sharing_type = value
    
    @property
    def work_profile_default_app_permission_policy(self,) -> Optional[android_work_profile_default_app_permission_policy_type.AndroidWorkProfileDefaultAppPermissionPolicyType]:
        """
        Gets the workProfileDefaultAppPermissionPolicy property value. Android Work Profile default app permission policy type.
        Returns: Optional[android_work_profile_default_app_permission_policy_type.AndroidWorkProfileDefaultAppPermissionPolicyType]
        """
        return self._work_profile_default_app_permission_policy
    
    @work_profile_default_app_permission_policy.setter
    def work_profile_default_app_permission_policy(self,value: Optional[android_work_profile_default_app_permission_policy_type.AndroidWorkProfileDefaultAppPermissionPolicyType] = None) -> None:
        """
        Sets the workProfileDefaultAppPermissionPolicy property value. Android Work Profile default app permission policy type.
        Args:
            value: Value to set for the work_profile_default_app_permission_policy property.
        """
        self._work_profile_default_app_permission_policy = value
    
    @property
    def work_profile_password_block_face_unlock(self,) -> Optional[bool]:
        """
        Gets the workProfilePasswordBlockFaceUnlock property value. Indicates whether or not to block face unlock for work profile.
        Returns: Optional[bool]
        """
        return self._work_profile_password_block_face_unlock
    
    @work_profile_password_block_face_unlock.setter
    def work_profile_password_block_face_unlock(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfilePasswordBlockFaceUnlock property value. Indicates whether or not to block face unlock for work profile.
        Args:
            value: Value to set for the work_profile_password_block_face_unlock property.
        """
        self._work_profile_password_block_face_unlock = value
    
    @property
    def work_profile_password_block_fingerprint_unlock(self,) -> Optional[bool]:
        """
        Gets the workProfilePasswordBlockFingerprintUnlock property value. Indicates whether or not to block fingerprint unlock for work profile.
        Returns: Optional[bool]
        """
        return self._work_profile_password_block_fingerprint_unlock
    
    @work_profile_password_block_fingerprint_unlock.setter
    def work_profile_password_block_fingerprint_unlock(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfilePasswordBlockFingerprintUnlock property value. Indicates whether or not to block fingerprint unlock for work profile.
        Args:
            value: Value to set for the work_profile_password_block_fingerprint_unlock property.
        """
        self._work_profile_password_block_fingerprint_unlock = value
    
    @property
    def work_profile_password_block_iris_unlock(self,) -> Optional[bool]:
        """
        Gets the workProfilePasswordBlockIrisUnlock property value. Indicates whether or not to block iris unlock for work profile.
        Returns: Optional[bool]
        """
        return self._work_profile_password_block_iris_unlock
    
    @work_profile_password_block_iris_unlock.setter
    def work_profile_password_block_iris_unlock(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfilePasswordBlockIrisUnlock property value. Indicates whether or not to block iris unlock for work profile.
        Args:
            value: Value to set for the work_profile_password_block_iris_unlock property.
        """
        self._work_profile_password_block_iris_unlock = value
    
    @property
    def work_profile_password_block_trust_agents(self,) -> Optional[bool]:
        """
        Gets the workProfilePasswordBlockTrustAgents property value. Indicates whether or not to block Smart Lock and other trust agents for work profile.
        Returns: Optional[bool]
        """
        return self._work_profile_password_block_trust_agents
    
    @work_profile_password_block_trust_agents.setter
    def work_profile_password_block_trust_agents(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfilePasswordBlockTrustAgents property value. Indicates whether or not to block Smart Lock and other trust agents for work profile.
        Args:
            value: Value to set for the work_profile_password_block_trust_agents property.
        """
        self._work_profile_password_block_trust_agents = value
    
    @property
    def work_profile_password_expiration_days(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordExpirationDays property value. Number of days before the work profile password expires. Valid values 1 to 365
        Returns: Optional[int]
        """
        return self._work_profile_password_expiration_days
    
    @work_profile_password_expiration_days.setter
    def work_profile_password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordExpirationDays property value. Number of days before the work profile password expires. Valid values 1 to 365
        Args:
            value: Value to set for the work_profile_password_expiration_days property.
        """
        self._work_profile_password_expiration_days = value
    
    @property
    def work_profile_password_min_letter_characters(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinLetterCharacters property value. Minimum # of letter characters required in work profile password. Valid values 1 to 10
        Returns: Optional[int]
        """
        return self._work_profile_password_min_letter_characters
    
    @work_profile_password_min_letter_characters.setter
    def work_profile_password_min_letter_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinLetterCharacters property value. Minimum # of letter characters required in work profile password. Valid values 1 to 10
        Args:
            value: Value to set for the work_profile_password_min_letter_characters property.
        """
        self._work_profile_password_min_letter_characters = value
    
    @property
    def work_profile_password_min_lower_case_characters(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinLowerCaseCharacters property value. Minimum # of lower-case characters required in work profile password. Valid values 1 to 10
        Returns: Optional[int]
        """
        return self._work_profile_password_min_lower_case_characters
    
    @work_profile_password_min_lower_case_characters.setter
    def work_profile_password_min_lower_case_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinLowerCaseCharacters property value. Minimum # of lower-case characters required in work profile password. Valid values 1 to 10
        Args:
            value: Value to set for the work_profile_password_min_lower_case_characters property.
        """
        self._work_profile_password_min_lower_case_characters = value
    
    @property
    def work_profile_password_min_non_letter_characters(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinNonLetterCharacters property value. Minimum # of non-letter characters required in work profile password. Valid values 1 to 10
        Returns: Optional[int]
        """
        return self._work_profile_password_min_non_letter_characters
    
    @work_profile_password_min_non_letter_characters.setter
    def work_profile_password_min_non_letter_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinNonLetterCharacters property value. Minimum # of non-letter characters required in work profile password. Valid values 1 to 10
        Args:
            value: Value to set for the work_profile_password_min_non_letter_characters property.
        """
        self._work_profile_password_min_non_letter_characters = value
    
    @property
    def work_profile_password_min_numeric_characters(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinNumericCharacters property value. Minimum # of numeric characters required in work profile password. Valid values 1 to 10
        Returns: Optional[int]
        """
        return self._work_profile_password_min_numeric_characters
    
    @work_profile_password_min_numeric_characters.setter
    def work_profile_password_min_numeric_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinNumericCharacters property value. Minimum # of numeric characters required in work profile password. Valid values 1 to 10
        Args:
            value: Value to set for the work_profile_password_min_numeric_characters property.
        """
        self._work_profile_password_min_numeric_characters = value
    
    @property
    def work_profile_password_min_symbol_characters(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinSymbolCharacters property value. Minimum # of symbols required in work profile password. Valid values 1 to 10
        Returns: Optional[int]
        """
        return self._work_profile_password_min_symbol_characters
    
    @work_profile_password_min_symbol_characters.setter
    def work_profile_password_min_symbol_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinSymbolCharacters property value. Minimum # of symbols required in work profile password. Valid values 1 to 10
        Args:
            value: Value to set for the work_profile_password_min_symbol_characters property.
        """
        self._work_profile_password_min_symbol_characters = value
    
    @property
    def work_profile_password_min_upper_case_characters(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinUpperCaseCharacters property value. Minimum # of upper-case characters required in work profile password. Valid values 1 to 10
        Returns: Optional[int]
        """
        return self._work_profile_password_min_upper_case_characters
    
    @work_profile_password_min_upper_case_characters.setter
    def work_profile_password_min_upper_case_characters(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinUpperCaseCharacters property value. Minimum # of upper-case characters required in work profile password. Valid values 1 to 10
        Args:
            value: Value to set for the work_profile_password_min_upper_case_characters property.
        """
        self._work_profile_password_min_upper_case_characters = value
    
    @property
    def work_profile_password_minimum_length(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinimumLength property value. Minimum length of work profile password. Valid values 4 to 16
        Returns: Optional[int]
        """
        return self._work_profile_password_minimum_length
    
    @work_profile_password_minimum_length.setter
    def work_profile_password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinimumLength property value. Minimum length of work profile password. Valid values 4 to 16
        Args:
            value: Value to set for the work_profile_password_minimum_length property.
        """
        self._work_profile_password_minimum_length = value
    
    @property
    def work_profile_password_minutes_of_inactivity_before_screen_timeout(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity before the screen times out.
        Returns: Optional[int]
        """
        return self._work_profile_password_minutes_of_inactivity_before_screen_timeout
    
    @work_profile_password_minutes_of_inactivity_before_screen_timeout.setter
    def work_profile_password_minutes_of_inactivity_before_screen_timeout(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity before the screen times out.
        Args:
            value: Value to set for the work_profile_password_minutes_of_inactivity_before_screen_timeout property.
        """
        self._work_profile_password_minutes_of_inactivity_before_screen_timeout = value
    
    @property
    def work_profile_password_previous_password_block_count(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordPreviousPasswordBlockCount property value. Number of previous work profile passwords to block. Valid values 0 to 24
        Returns: Optional[int]
        """
        return self._work_profile_password_previous_password_block_count
    
    @work_profile_password_previous_password_block_count.setter
    def work_profile_password_previous_password_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordPreviousPasswordBlockCount property value. Number of previous work profile passwords to block. Valid values 0 to 24
        Args:
            value: Value to set for the work_profile_password_previous_password_block_count property.
        """
        self._work_profile_password_previous_password_block_count = value
    
    @property
    def work_profile_password_required_type(self,) -> Optional[android_work_profile_required_password_type.AndroidWorkProfileRequiredPasswordType]:
        """
        Gets the workProfilePasswordRequiredType property value. Android Work Profile required password type.
        Returns: Optional[android_work_profile_required_password_type.AndroidWorkProfileRequiredPasswordType]
        """
        return self._work_profile_password_required_type
    
    @work_profile_password_required_type.setter
    def work_profile_password_required_type(self,value: Optional[android_work_profile_required_password_type.AndroidWorkProfileRequiredPasswordType] = None) -> None:
        """
        Sets the workProfilePasswordRequiredType property value. Android Work Profile required password type.
        Args:
            value: Value to set for the work_profile_password_required_type property.
        """
        self._work_profile_password_required_type = value
    
    @property
    def work_profile_password_sign_in_failure_count_before_factory_reset(self,) -> Optional[int]:
        """
        Gets the workProfilePasswordSignInFailureCountBeforeFactoryReset property value. Number of sign in failures allowed before work profile is removed and all corporate data deleted. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._work_profile_password_sign_in_failure_count_before_factory_reset
    
    @work_profile_password_sign_in_failure_count_before_factory_reset.setter
    def work_profile_password_sign_in_failure_count_before_factory_reset(self,value: Optional[int] = None) -> None:
        """
        Sets the workProfilePasswordSignInFailureCountBeforeFactoryReset property value. Number of sign in failures allowed before work profile is removed and all corporate data deleted. Valid values 1 to 16
        Args:
            value: Value to set for the work_profile_password_sign_in_failure_count_before_factory_reset property.
        """
        self._work_profile_password_sign_in_failure_count_before_factory_reset = value
    
    @property
    def work_profile_require_password(self,) -> Optional[bool]:
        """
        Gets the workProfileRequirePassword property value. Password is required or not for work profile
        Returns: Optional[bool]
        """
        return self._work_profile_require_password
    
    @work_profile_require_password.setter
    def work_profile_require_password(self,value: Optional[bool] = None) -> None:
        """
        Sets the workProfileRequirePassword property value. Password is required or not for work profile
        Args:
            value: Value to set for the work_profile_require_password property.
        """
        self._work_profile_require_password = value
    
    @property
    def work_profile_required_password_complexity(self,) -> Optional[android_required_password_complexity.AndroidRequiredPasswordComplexity]:
        """
        Gets the workProfileRequiredPasswordComplexity property value. The password complexity types that can be set on Android. One of: NONE, LOW, MEDIUM, HIGH. This is an API targeted to Android 11+.
        Returns: Optional[android_required_password_complexity.AndroidRequiredPasswordComplexity]
        """
        return self._work_profile_required_password_complexity
    
    @work_profile_required_password_complexity.setter
    def work_profile_required_password_complexity(self,value: Optional[android_required_password_complexity.AndroidRequiredPasswordComplexity] = None) -> None:
        """
        Sets the workProfileRequiredPasswordComplexity property value. The password complexity types that can be set on Android. One of: NONE, LOW, MEDIUM, HIGH. This is an API targeted to Android 11+.
        Args:
            value: Value to set for the work_profile_required_password_complexity property.
        """
        self._work_profile_required_password_complexity = value
    

