from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_managed_app_safety_net_apps_verification_type = lazy_import('msgraph.generated.models.android_managed_app_safety_net_apps_verification_type')
android_managed_app_safety_net_device_attestation_type = lazy_import('msgraph.generated.models.android_managed_app_safety_net_device_attestation_type')
android_managed_app_safety_net_evaluation_type = lazy_import('msgraph.generated.models.android_managed_app_safety_net_evaluation_type')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
managed_app_policy_deployment_summary = lazy_import('msgraph.generated.models.managed_app_policy_deployment_summary')
managed_app_remediation_action = lazy_import('msgraph.generated.models.managed_app_remediation_action')
managed_mobile_app = lazy_import('msgraph.generated.models.managed_mobile_app')
targeted_managed_app_protection = lazy_import('msgraph.generated.models.targeted_managed_app_protection')

class AndroidManagedAppProtection(targeted_managed_app_protection.TargetedManagedAppProtection):
    @property
    def allowed_android_device_manufacturers(self,) -> Optional[str]:
        """
        Gets the allowedAndroidDeviceManufacturers property value. Semicolon seperated list of device manufacturers allowed, as a string, for the managed app to work.
        Returns: Optional[str]
        """
        return self._allowed_android_device_manufacturers
    
    @allowed_android_device_manufacturers.setter
    def allowed_android_device_manufacturers(self,value: Optional[str] = None) -> None:
        """
        Sets the allowedAndroidDeviceManufacturers property value. Semicolon seperated list of device manufacturers allowed, as a string, for the managed app to work.
        Args:
            value: Value to set for the allowedAndroidDeviceManufacturers property.
        """
        self._allowed_android_device_manufacturers = value
    
    @property
    def allowed_android_device_models(self,) -> Optional[List[str]]:
        """
        Gets the allowedAndroidDeviceModels property value. List of device models allowed, as a string, for the managed app to work.
        Returns: Optional[List[str]]
        """
        return self._allowed_android_device_models
    
    @allowed_android_device_models.setter
    def allowed_android_device_models(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedAndroidDeviceModels property value. List of device models allowed, as a string, for the managed app to work.
        Args:
            value: Value to set for the allowedAndroidDeviceModels property.
        """
        self._allowed_android_device_models = value
    
    @property
    def app_action_if_android_device_manufacturer_not_allowed(self,) -> Optional[managed_app_remediation_action.ManagedAppRemediationAction]:
        """
        Gets the appActionIfAndroidDeviceManufacturerNotAllowed property value. An admin initiated action to be applied on a managed app.
        Returns: Optional[managed_app_remediation_action.ManagedAppRemediationAction]
        """
        return self._app_action_if_android_device_manufacturer_not_allowed
    
    @app_action_if_android_device_manufacturer_not_allowed.setter
    def app_action_if_android_device_manufacturer_not_allowed(self,value: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None) -> None:
        """
        Sets the appActionIfAndroidDeviceManufacturerNotAllowed property value. An admin initiated action to be applied on a managed app.
        Args:
            value: Value to set for the appActionIfAndroidDeviceManufacturerNotAllowed property.
        """
        self._app_action_if_android_device_manufacturer_not_allowed = value
    
    @property
    def app_action_if_android_device_model_not_allowed(self,) -> Optional[managed_app_remediation_action.ManagedAppRemediationAction]:
        """
        Gets the appActionIfAndroidDeviceModelNotAllowed property value. An admin initiated action to be applied on a managed app.
        Returns: Optional[managed_app_remediation_action.ManagedAppRemediationAction]
        """
        return self._app_action_if_android_device_model_not_allowed
    
    @app_action_if_android_device_model_not_allowed.setter
    def app_action_if_android_device_model_not_allowed(self,value: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None) -> None:
        """
        Sets the appActionIfAndroidDeviceModelNotAllowed property value. An admin initiated action to be applied on a managed app.
        Args:
            value: Value to set for the appActionIfAndroidDeviceModelNotAllowed property.
        """
        self._app_action_if_android_device_model_not_allowed = value
    
    @property
    def app_action_if_android_safety_net_apps_verification_failed(self,) -> Optional[managed_app_remediation_action.ManagedAppRemediationAction]:
        """
        Gets the appActionIfAndroidSafetyNetAppsVerificationFailed property value. An admin initiated action to be applied on a managed app.
        Returns: Optional[managed_app_remediation_action.ManagedAppRemediationAction]
        """
        return self._app_action_if_android_safety_net_apps_verification_failed
    
    @app_action_if_android_safety_net_apps_verification_failed.setter
    def app_action_if_android_safety_net_apps_verification_failed(self,value: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None) -> None:
        """
        Sets the appActionIfAndroidSafetyNetAppsVerificationFailed property value. An admin initiated action to be applied on a managed app.
        Args:
            value: Value to set for the appActionIfAndroidSafetyNetAppsVerificationFailed property.
        """
        self._app_action_if_android_safety_net_apps_verification_failed = value
    
    @property
    def app_action_if_android_safety_net_device_attestation_failed(self,) -> Optional[managed_app_remediation_action.ManagedAppRemediationAction]:
        """
        Gets the appActionIfAndroidSafetyNetDeviceAttestationFailed property value. An admin initiated action to be applied on a managed app.
        Returns: Optional[managed_app_remediation_action.ManagedAppRemediationAction]
        """
        return self._app_action_if_android_safety_net_device_attestation_failed
    
    @app_action_if_android_safety_net_device_attestation_failed.setter
    def app_action_if_android_safety_net_device_attestation_failed(self,value: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None) -> None:
        """
        Sets the appActionIfAndroidSafetyNetDeviceAttestationFailed property value. An admin initiated action to be applied on a managed app.
        Args:
            value: Value to set for the appActionIfAndroidSafetyNetDeviceAttestationFailed property.
        """
        self._app_action_if_android_safety_net_device_attestation_failed = value
    
    @property
    def app_action_if_device_lock_not_set(self,) -> Optional[managed_app_remediation_action.ManagedAppRemediationAction]:
        """
        Gets the appActionIfDeviceLockNotSet property value. An admin initiated action to be applied on a managed app.
        Returns: Optional[managed_app_remediation_action.ManagedAppRemediationAction]
        """
        return self._app_action_if_device_lock_not_set
    
    @app_action_if_device_lock_not_set.setter
    def app_action_if_device_lock_not_set(self,value: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None) -> None:
        """
        Sets the appActionIfDeviceLockNotSet property value. An admin initiated action to be applied on a managed app.
        Args:
            value: Value to set for the appActionIfDeviceLockNotSet property.
        """
        self._app_action_if_device_lock_not_set = value
    
    @property
    def app_action_if_device_passcode_complexity_less_than_high(self,) -> Optional[managed_app_remediation_action.ManagedAppRemediationAction]:
        """
        Gets the appActionIfDevicePasscodeComplexityLessThanHigh property value. If the device does not have a passcode of high complexity or higher, trigger the stored action.
        Returns: Optional[managed_app_remediation_action.ManagedAppRemediationAction]
        """
        return self._app_action_if_device_passcode_complexity_less_than_high
    
    @app_action_if_device_passcode_complexity_less_than_high.setter
    def app_action_if_device_passcode_complexity_less_than_high(self,value: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None) -> None:
        """
        Sets the appActionIfDevicePasscodeComplexityLessThanHigh property value. If the device does not have a passcode of high complexity or higher, trigger the stored action.
        Args:
            value: Value to set for the appActionIfDevicePasscodeComplexityLessThanHigh property.
        """
        self._app_action_if_device_passcode_complexity_less_than_high = value
    
    @property
    def app_action_if_device_passcode_complexity_less_than_low(self,) -> Optional[managed_app_remediation_action.ManagedAppRemediationAction]:
        """
        Gets the appActionIfDevicePasscodeComplexityLessThanLow property value. If the device does not have a passcode of low complexity or higher, trigger the stored action.
        Returns: Optional[managed_app_remediation_action.ManagedAppRemediationAction]
        """
        return self._app_action_if_device_passcode_complexity_less_than_low
    
    @app_action_if_device_passcode_complexity_less_than_low.setter
    def app_action_if_device_passcode_complexity_less_than_low(self,value: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None) -> None:
        """
        Sets the appActionIfDevicePasscodeComplexityLessThanLow property value. If the device does not have a passcode of low complexity or higher, trigger the stored action.
        Args:
            value: Value to set for the appActionIfDevicePasscodeComplexityLessThanLow property.
        """
        self._app_action_if_device_passcode_complexity_less_than_low = value
    
    @property
    def app_action_if_device_passcode_complexity_less_than_medium(self,) -> Optional[managed_app_remediation_action.ManagedAppRemediationAction]:
        """
        Gets the appActionIfDevicePasscodeComplexityLessThanMedium property value. If the device does not have a passcode of medium complexity or higher, trigger the stored action.
        Returns: Optional[managed_app_remediation_action.ManagedAppRemediationAction]
        """
        return self._app_action_if_device_passcode_complexity_less_than_medium
    
    @app_action_if_device_passcode_complexity_less_than_medium.setter
    def app_action_if_device_passcode_complexity_less_than_medium(self,value: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None) -> None:
        """
        Sets the appActionIfDevicePasscodeComplexityLessThanMedium property value. If the device does not have a passcode of medium complexity or higher, trigger the stored action.
        Args:
            value: Value to set for the appActionIfDevicePasscodeComplexityLessThanMedium property.
        """
        self._app_action_if_device_passcode_complexity_less_than_medium = value
    
    @property
    def approved_keyboards(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the approvedKeyboards property value. If Keyboard Restriction is enabled, only keyboards in this approved list will be allowed. A key should be Android package id for a keyboard and value should be a friendly name
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._approved_keyboards
    
    @approved_keyboards.setter
    def approved_keyboards(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the approvedKeyboards property value. If Keyboard Restriction is enabled, only keyboards in this approved list will be allowed. A key should be Android package id for a keyboard and value should be a friendly name
        Args:
            value: Value to set for the approvedKeyboards property.
        """
        self._approved_keyboards = value
    
    @property
    def apps(self,) -> Optional[List[managed_mobile_app.ManagedMobileApp]]:
        """
        Gets the apps property value. List of apps to which the policy is deployed.
        Returns: Optional[List[managed_mobile_app.ManagedMobileApp]]
        """
        return self._apps
    
    @apps.setter
    def apps(self,value: Optional[List[managed_mobile_app.ManagedMobileApp]] = None) -> None:
        """
        Sets the apps property value. List of apps to which the policy is deployed.
        Args:
            value: Value to set for the apps property.
        """
        self._apps = value
    
    @property
    def biometric_authentication_blocked(self,) -> Optional[bool]:
        """
        Gets the biometricAuthenticationBlocked property value. Indicates whether use of the biometric authentication is allowed in place of a pin if PinRequired is set to True.
        Returns: Optional[bool]
        """
        return self._biometric_authentication_blocked
    
    @biometric_authentication_blocked.setter
    def biometric_authentication_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the biometricAuthenticationBlocked property value. Indicates whether use of the biometric authentication is allowed in place of a pin if PinRequired is set to True.
        Args:
            value: Value to set for the biometricAuthenticationBlocked property.
        """
        self._biometric_authentication_blocked = value
    
    @property
    def block_after_company_portal_update_deferral_in_days(self,) -> Optional[int]:
        """
        Gets the blockAfterCompanyPortalUpdateDeferralInDays property value. Maximum number of days Company Portal update can be deferred on the device or app access will be blocked.
        Returns: Optional[int]
        """
        return self._block_after_company_portal_update_deferral_in_days
    
    @block_after_company_portal_update_deferral_in_days.setter
    def block_after_company_portal_update_deferral_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the blockAfterCompanyPortalUpdateDeferralInDays property value. Maximum number of days Company Portal update can be deferred on the device or app access will be blocked.
        Args:
            value: Value to set for the blockAfterCompanyPortalUpdateDeferralInDays property.
        """
        self._block_after_company_portal_update_deferral_in_days = value
    
    @property
    def connect_to_vpn_on_launch(self,) -> Optional[bool]:
        """
        Gets the connectToVpnOnLaunch property value. Whether the app should connect to the configured VPN on launch.
        Returns: Optional[bool]
        """
        return self._connect_to_vpn_on_launch
    
    @connect_to_vpn_on_launch.setter
    def connect_to_vpn_on_launch(self,value: Optional[bool] = None) -> None:
        """
        Sets the connectToVpnOnLaunch property value. Whether the app should connect to the configured VPN on launch.
        Args:
            value: Value to set for the connectToVpnOnLaunch property.
        """
        self._connect_to_vpn_on_launch = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidManagedAppProtection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidManagedAppProtection"
        # Semicolon seperated list of device manufacturers allowed, as a string, for the managed app to work.
        self._allowed_android_device_manufacturers: Optional[str] = None
        # List of device models allowed, as a string, for the managed app to work.
        self._allowed_android_device_models: Optional[List[str]] = None
        # An admin initiated action to be applied on a managed app.
        self._app_action_if_android_device_manufacturer_not_allowed: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None
        # An admin initiated action to be applied on a managed app.
        self._app_action_if_android_device_model_not_allowed: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None
        # An admin initiated action to be applied on a managed app.
        self._app_action_if_android_safety_net_apps_verification_failed: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None
        # An admin initiated action to be applied on a managed app.
        self._app_action_if_android_safety_net_device_attestation_failed: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None
        # An admin initiated action to be applied on a managed app.
        self._app_action_if_device_lock_not_set: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None
        # If the device does not have a passcode of high complexity or higher, trigger the stored action.
        self._app_action_if_device_passcode_complexity_less_than_high: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None
        # If the device does not have a passcode of low complexity or higher, trigger the stored action.
        self._app_action_if_device_passcode_complexity_less_than_low: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None
        # If the device does not have a passcode of medium complexity or higher, trigger the stored action.
        self._app_action_if_device_passcode_complexity_less_than_medium: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None
        # If Keyboard Restriction is enabled, only keyboards in this approved list will be allowed. A key should be Android package id for a keyboard and value should be a friendly name
        self._approved_keyboards: Optional[List[key_value_pair.KeyValuePair]] = None
        # List of apps to which the policy is deployed.
        self._apps: Optional[List[managed_mobile_app.ManagedMobileApp]] = None
        # Indicates whether use of the biometric authentication is allowed in place of a pin if PinRequired is set to True.
        self._biometric_authentication_blocked: Optional[bool] = None
        # Maximum number of days Company Portal update can be deferred on the device or app access will be blocked.
        self._block_after_company_portal_update_deferral_in_days: Optional[int] = None
        # Whether the app should connect to the configured VPN on launch.
        self._connect_to_vpn_on_launch: Optional[bool] = None
        # Friendly name of the preferred custom browser to open weblink on Android.
        self._custom_browser_display_name: Optional[str] = None
        # Unique identifier of a custom browser to open weblink on Android.
        self._custom_browser_package_id: Optional[str] = None
        # Friendly name of a custom dialer app to click-to-open a phone number on Android.
        self._custom_dialer_app_display_name: Optional[str] = None
        # PackageId of a custom dialer app to click-to-open a phone number on Android.
        self._custom_dialer_app_package_id: Optional[str] = None
        # Count of apps to which the current policy is deployed.
        self._deployed_app_count: Optional[int] = None
        # Navigation property to deployment summary of the configuration.
        self._deployment_summary: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary] = None
        # Defines if any kind of lock must be required on android device
        self._device_lock_required: Optional[bool] = None
        # When this setting is enabled, app level encryption is disabled if device level encryption is enabled
        self._disable_app_encryption_if_device_encryption_is_enabled: Optional[bool] = None
        # Indicates whether application data for managed apps should be encrypted
        self._encrypt_app_data: Optional[bool] = None
        # App packages in this list will be exempt from the policy and will be able to receive data from managed apps.
        self._exempted_app_packages: Optional[List[key_value_pair.KeyValuePair]] = None
        # If null, this setting will be ignored. If false both fingerprints and biometrics will not be enabled. If true, both fingerprints and biometrics will be enabled.
        self._fingerprint_and_biometric_enabled: Optional[bool] = None
        # Indicates if keyboard restriction is enabled. If enabled list of approved keyboards must be provided as well.
        self._keyboards_restricted: Optional[bool] = None
        # Minimum version of the Company portal that must be installed on the device or app access will be blocked
        self._minimum_required_company_portal_version: Optional[str] = None
        # Define the oldest required Android security patch level a user can have to gain secure access to the app.
        self._minimum_required_patch_version: Optional[str] = None
        # Minimum version of the Company portal that must be installed on the device or the user will receive a warning
        self._minimum_warning_company_portal_version: Optional[str] = None
        # Define the oldest recommended Android security patch level a user can have for secure access to the app.
        self._minimum_warning_patch_version: Optional[str] = None
        # Minimum version of the Company portal that must be installed on the device or the company data on the app will be wiped
        self._minimum_wipe_company_portal_version: Optional[str] = None
        # Android security patch level  less than or equal to the specified value will wipe the managed app and the associated company data.
        self._minimum_wipe_patch_version: Optional[str] = None
        # Require user to apply Class 3 Biometrics on their Android device.
        self._require_class3_biometrics: Optional[bool] = None
        # An admin enforced Android SafetyNet Device Attestation requirement on a managed app.
        self._required_android_safety_net_apps_verification_type: Optional[android_managed_app_safety_net_apps_verification_type.AndroidManagedAppSafetyNetAppsVerificationType] = None
        # An admin enforced Android SafetyNet Device Attestation requirement on a managed app.
        self._required_android_safety_net_device_attestation_type: Optional[android_managed_app_safety_net_device_attestation_type.AndroidManagedAppSafetyNetDeviceAttestationType] = None
        # An admin enforced Android SafetyNet evaluation type requirement on a managed app.
        self._required_android_safety_net_evaluation_type: Optional[android_managed_app_safety_net_evaluation_type.AndroidManagedAppSafetyNetEvaluationType] = None
        # A PIN prompt will override biometric prompts if class 3 biometrics are updated on the device.
        self._require_pin_after_biometric_change: Optional[bool] = None
        # Indicates whether a managed user can take screen captures of managed apps
        self._screen_capture_blocked: Optional[bool] = None
        # Maximum number of days Company Portal update can be deferred on the device or the user will receive the warning
        self._warn_after_company_portal_update_deferral_in_days: Optional[int] = None
        # Maximum number of days Company Portal update can be deferred on the device or the company data on the app will be wiped
        self._wipe_after_company_portal_update_deferral_in_days: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedAppProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidManagedAppProtection()
    
    @property
    def custom_browser_display_name(self,) -> Optional[str]:
        """
        Gets the customBrowserDisplayName property value. Friendly name of the preferred custom browser to open weblink on Android.
        Returns: Optional[str]
        """
        return self._custom_browser_display_name
    
    @custom_browser_display_name.setter
    def custom_browser_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the customBrowserDisplayName property value. Friendly name of the preferred custom browser to open weblink on Android.
        Args:
            value: Value to set for the customBrowserDisplayName property.
        """
        self._custom_browser_display_name = value
    
    @property
    def custom_browser_package_id(self,) -> Optional[str]:
        """
        Gets the customBrowserPackageId property value. Unique identifier of a custom browser to open weblink on Android.
        Returns: Optional[str]
        """
        return self._custom_browser_package_id
    
    @custom_browser_package_id.setter
    def custom_browser_package_id(self,value: Optional[str] = None) -> None:
        """
        Sets the customBrowserPackageId property value. Unique identifier of a custom browser to open weblink on Android.
        Args:
            value: Value to set for the customBrowserPackageId property.
        """
        self._custom_browser_package_id = value
    
    @property
    def custom_dialer_app_display_name(self,) -> Optional[str]:
        """
        Gets the customDialerAppDisplayName property value. Friendly name of a custom dialer app to click-to-open a phone number on Android.
        Returns: Optional[str]
        """
        return self._custom_dialer_app_display_name
    
    @custom_dialer_app_display_name.setter
    def custom_dialer_app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the customDialerAppDisplayName property value. Friendly name of a custom dialer app to click-to-open a phone number on Android.
        Args:
            value: Value to set for the customDialerAppDisplayName property.
        """
        self._custom_dialer_app_display_name = value
    
    @property
    def custom_dialer_app_package_id(self,) -> Optional[str]:
        """
        Gets the customDialerAppPackageId property value. PackageId of a custom dialer app to click-to-open a phone number on Android.
        Returns: Optional[str]
        """
        return self._custom_dialer_app_package_id
    
    @custom_dialer_app_package_id.setter
    def custom_dialer_app_package_id(self,value: Optional[str] = None) -> None:
        """
        Sets the customDialerAppPackageId property value. PackageId of a custom dialer app to click-to-open a phone number on Android.
        Args:
            value: Value to set for the customDialerAppPackageId property.
        """
        self._custom_dialer_app_package_id = value
    
    @property
    def deployed_app_count(self,) -> Optional[int]:
        """
        Gets the deployedAppCount property value. Count of apps to which the current policy is deployed.
        Returns: Optional[int]
        """
        return self._deployed_app_count
    
    @deployed_app_count.setter
    def deployed_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deployedAppCount property value. Count of apps to which the current policy is deployed.
        Args:
            value: Value to set for the deployedAppCount property.
        """
        self._deployed_app_count = value
    
    @property
    def deployment_summary(self,) -> Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary]:
        """
        Gets the deploymentSummary property value. Navigation property to deployment summary of the configuration.
        Returns: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary]
        """
        return self._deployment_summary
    
    @deployment_summary.setter
    def deployment_summary(self,value: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary] = None) -> None:
        """
        Sets the deploymentSummary property value. Navigation property to deployment summary of the configuration.
        Args:
            value: Value to set for the deploymentSummary property.
        """
        self._deployment_summary = value
    
    @property
    def device_lock_required(self,) -> Optional[bool]:
        """
        Gets the deviceLockRequired property value. Defines if any kind of lock must be required on android device
        Returns: Optional[bool]
        """
        return self._device_lock_required
    
    @device_lock_required.setter
    def device_lock_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceLockRequired property value. Defines if any kind of lock must be required on android device
        Args:
            value: Value to set for the deviceLockRequired property.
        """
        self._device_lock_required = value
    
    @property
    def disable_app_encryption_if_device_encryption_is_enabled(self,) -> Optional[bool]:
        """
        Gets the disableAppEncryptionIfDeviceEncryptionIsEnabled property value. When this setting is enabled, app level encryption is disabled if device level encryption is enabled
        Returns: Optional[bool]
        """
        return self._disable_app_encryption_if_device_encryption_is_enabled
    
    @disable_app_encryption_if_device_encryption_is_enabled.setter
    def disable_app_encryption_if_device_encryption_is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableAppEncryptionIfDeviceEncryptionIsEnabled property value. When this setting is enabled, app level encryption is disabled if device level encryption is enabled
        Args:
            value: Value to set for the disableAppEncryptionIfDeviceEncryptionIsEnabled property.
        """
        self._disable_app_encryption_if_device_encryption_is_enabled = value
    
    @property
    def encrypt_app_data(self,) -> Optional[bool]:
        """
        Gets the encryptAppData property value. Indicates whether application data for managed apps should be encrypted
        Returns: Optional[bool]
        """
        return self._encrypt_app_data
    
    @encrypt_app_data.setter
    def encrypt_app_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the encryptAppData property value. Indicates whether application data for managed apps should be encrypted
        Args:
            value: Value to set for the encryptAppData property.
        """
        self._encrypt_app_data = value
    
    @property
    def exempted_app_packages(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the exemptedAppPackages property value. App packages in this list will be exempt from the policy and will be able to receive data from managed apps.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._exempted_app_packages
    
    @exempted_app_packages.setter
    def exempted_app_packages(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the exemptedAppPackages property value. App packages in this list will be exempt from the policy and will be able to receive data from managed apps.
        Args:
            value: Value to set for the exemptedAppPackages property.
        """
        self._exempted_app_packages = value
    
    @property
    def fingerprint_and_biometric_enabled(self,) -> Optional[bool]:
        """
        Gets the fingerprintAndBiometricEnabled property value. If null, this setting will be ignored. If false both fingerprints and biometrics will not be enabled. If true, both fingerprints and biometrics will be enabled.
        Returns: Optional[bool]
        """
        return self._fingerprint_and_biometric_enabled
    
    @fingerprint_and_biometric_enabled.setter
    def fingerprint_and_biometric_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the fingerprintAndBiometricEnabled property value. If null, this setting will be ignored. If false both fingerprints and biometrics will not be enabled. If true, both fingerprints and biometrics will be enabled.
        Args:
            value: Value to set for the fingerprintAndBiometricEnabled property.
        """
        self._fingerprint_and_biometric_enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_android_device_manufacturers": lambda n : setattr(self, 'allowed_android_device_manufacturers', n.get_str_value()),
            "allowed_android_device_models": lambda n : setattr(self, 'allowed_android_device_models', n.get_collection_of_primitive_values(str)),
            "app_action_if_android_device_manufacturer_not_allowed": lambda n : setattr(self, 'app_action_if_android_device_manufacturer_not_allowed', n.get_enum_value(managed_app_remediation_action.ManagedAppRemediationAction)),
            "app_action_if_android_device_model_not_allowed": lambda n : setattr(self, 'app_action_if_android_device_model_not_allowed', n.get_enum_value(managed_app_remediation_action.ManagedAppRemediationAction)),
            "app_action_if_android_safety_net_apps_verification_failed": lambda n : setattr(self, 'app_action_if_android_safety_net_apps_verification_failed', n.get_enum_value(managed_app_remediation_action.ManagedAppRemediationAction)),
            "app_action_if_android_safety_net_device_attestation_failed": lambda n : setattr(self, 'app_action_if_android_safety_net_device_attestation_failed', n.get_enum_value(managed_app_remediation_action.ManagedAppRemediationAction)),
            "app_action_if_device_lock_not_set": lambda n : setattr(self, 'app_action_if_device_lock_not_set', n.get_enum_value(managed_app_remediation_action.ManagedAppRemediationAction)),
            "app_action_if_device_passcode_complexity_less_than_high": lambda n : setattr(self, 'app_action_if_device_passcode_complexity_less_than_high', n.get_enum_value(managed_app_remediation_action.ManagedAppRemediationAction)),
            "app_action_if_device_passcode_complexity_less_than_low": lambda n : setattr(self, 'app_action_if_device_passcode_complexity_less_than_low', n.get_enum_value(managed_app_remediation_action.ManagedAppRemediationAction)),
            "app_action_if_device_passcode_complexity_less_than_medium": lambda n : setattr(self, 'app_action_if_device_passcode_complexity_less_than_medium', n.get_enum_value(managed_app_remediation_action.ManagedAppRemediationAction)),
            "approved_keyboards": lambda n : setattr(self, 'approved_keyboards', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(managed_mobile_app.ManagedMobileApp)),
            "biometric_authentication_blocked": lambda n : setattr(self, 'biometric_authentication_blocked', n.get_bool_value()),
            "block_after_company_portal_update_deferral_in_days": lambda n : setattr(self, 'block_after_company_portal_update_deferral_in_days', n.get_int_value()),
            "connect_to_vpn_on_launch": lambda n : setattr(self, 'connect_to_vpn_on_launch', n.get_bool_value()),
            "custom_browser_display_name": lambda n : setattr(self, 'custom_browser_display_name', n.get_str_value()),
            "custom_browser_package_id": lambda n : setattr(self, 'custom_browser_package_id', n.get_str_value()),
            "custom_dialer_app_display_name": lambda n : setattr(self, 'custom_dialer_app_display_name', n.get_str_value()),
            "custom_dialer_app_package_id": lambda n : setattr(self, 'custom_dialer_app_package_id', n.get_str_value()),
            "deployed_app_count": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deployment_summary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary)),
            "device_lock_required": lambda n : setattr(self, 'device_lock_required', n.get_bool_value()),
            "disable_app_encryption_if_device_encryption_is_enabled": lambda n : setattr(self, 'disable_app_encryption_if_device_encryption_is_enabled', n.get_bool_value()),
            "encrypt_app_data": lambda n : setattr(self, 'encrypt_app_data', n.get_bool_value()),
            "exempted_app_packages": lambda n : setattr(self, 'exempted_app_packages', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "fingerprint_and_biometric_enabled": lambda n : setattr(self, 'fingerprint_and_biometric_enabled', n.get_bool_value()),
            "keyboards_restricted": lambda n : setattr(self, 'keyboards_restricted', n.get_bool_value()),
            "minimum_required_company_portal_version": lambda n : setattr(self, 'minimum_required_company_portal_version', n.get_str_value()),
            "minimum_required_patch_version": lambda n : setattr(self, 'minimum_required_patch_version', n.get_str_value()),
            "minimum_warning_company_portal_version": lambda n : setattr(self, 'minimum_warning_company_portal_version', n.get_str_value()),
            "minimum_warning_patch_version": lambda n : setattr(self, 'minimum_warning_patch_version', n.get_str_value()),
            "minimum_wipe_company_portal_version": lambda n : setattr(self, 'minimum_wipe_company_portal_version', n.get_str_value()),
            "minimum_wipe_patch_version": lambda n : setattr(self, 'minimum_wipe_patch_version', n.get_str_value()),
            "require_class3_biometrics": lambda n : setattr(self, 'require_class3_biometrics', n.get_bool_value()),
            "required_android_safety_net_apps_verification_type": lambda n : setattr(self, 'required_android_safety_net_apps_verification_type', n.get_enum_value(android_managed_app_safety_net_apps_verification_type.AndroidManagedAppSafetyNetAppsVerificationType)),
            "required_android_safety_net_device_attestation_type": lambda n : setattr(self, 'required_android_safety_net_device_attestation_type', n.get_enum_value(android_managed_app_safety_net_device_attestation_type.AndroidManagedAppSafetyNetDeviceAttestationType)),
            "required_android_safety_net_evaluation_type": lambda n : setattr(self, 'required_android_safety_net_evaluation_type', n.get_enum_value(android_managed_app_safety_net_evaluation_type.AndroidManagedAppSafetyNetEvaluationType)),
            "require_pin_after_biometric_change": lambda n : setattr(self, 'require_pin_after_biometric_change', n.get_bool_value()),
            "screen_capture_blocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "warn_after_company_portal_update_deferral_in_days": lambda n : setattr(self, 'warn_after_company_portal_update_deferral_in_days', n.get_int_value()),
            "wipe_after_company_portal_update_deferral_in_days": lambda n : setattr(self, 'wipe_after_company_portal_update_deferral_in_days', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def keyboards_restricted(self,) -> Optional[bool]:
        """
        Gets the keyboardsRestricted property value. Indicates if keyboard restriction is enabled. If enabled list of approved keyboards must be provided as well.
        Returns: Optional[bool]
        """
        return self._keyboards_restricted
    
    @keyboards_restricted.setter
    def keyboards_restricted(self,value: Optional[bool] = None) -> None:
        """
        Sets the keyboardsRestricted property value. Indicates if keyboard restriction is enabled. If enabled list of approved keyboards must be provided as well.
        Args:
            value: Value to set for the keyboardsRestricted property.
        """
        self._keyboards_restricted = value
    
    @property
    def minimum_required_company_portal_version(self,) -> Optional[str]:
        """
        Gets the minimumRequiredCompanyPortalVersion property value. Minimum version of the Company portal that must be installed on the device or app access will be blocked
        Returns: Optional[str]
        """
        return self._minimum_required_company_portal_version
    
    @minimum_required_company_portal_version.setter
    def minimum_required_company_portal_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumRequiredCompanyPortalVersion property value. Minimum version of the Company portal that must be installed on the device or app access will be blocked
        Args:
            value: Value to set for the minimumRequiredCompanyPortalVersion property.
        """
        self._minimum_required_company_portal_version = value
    
    @property
    def minimum_required_patch_version(self,) -> Optional[str]:
        """
        Gets the minimumRequiredPatchVersion property value. Define the oldest required Android security patch level a user can have to gain secure access to the app.
        Returns: Optional[str]
        """
        return self._minimum_required_patch_version
    
    @minimum_required_patch_version.setter
    def minimum_required_patch_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumRequiredPatchVersion property value. Define the oldest required Android security patch level a user can have to gain secure access to the app.
        Args:
            value: Value to set for the minimumRequiredPatchVersion property.
        """
        self._minimum_required_patch_version = value
    
    @property
    def minimum_warning_company_portal_version(self,) -> Optional[str]:
        """
        Gets the minimumWarningCompanyPortalVersion property value. Minimum version of the Company portal that must be installed on the device or the user will receive a warning
        Returns: Optional[str]
        """
        return self._minimum_warning_company_portal_version
    
    @minimum_warning_company_portal_version.setter
    def minimum_warning_company_portal_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWarningCompanyPortalVersion property value. Minimum version of the Company portal that must be installed on the device or the user will receive a warning
        Args:
            value: Value to set for the minimumWarningCompanyPortalVersion property.
        """
        self._minimum_warning_company_portal_version = value
    
    @property
    def minimum_warning_patch_version(self,) -> Optional[str]:
        """
        Gets the minimumWarningPatchVersion property value. Define the oldest recommended Android security patch level a user can have for secure access to the app.
        Returns: Optional[str]
        """
        return self._minimum_warning_patch_version
    
    @minimum_warning_patch_version.setter
    def minimum_warning_patch_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWarningPatchVersion property value. Define the oldest recommended Android security patch level a user can have for secure access to the app.
        Args:
            value: Value to set for the minimumWarningPatchVersion property.
        """
        self._minimum_warning_patch_version = value
    
    @property
    def minimum_wipe_company_portal_version(self,) -> Optional[str]:
        """
        Gets the minimumWipeCompanyPortalVersion property value. Minimum version of the Company portal that must be installed on the device or the company data on the app will be wiped
        Returns: Optional[str]
        """
        return self._minimum_wipe_company_portal_version
    
    @minimum_wipe_company_portal_version.setter
    def minimum_wipe_company_portal_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWipeCompanyPortalVersion property value. Minimum version of the Company portal that must be installed on the device or the company data on the app will be wiped
        Args:
            value: Value to set for the minimumWipeCompanyPortalVersion property.
        """
        self._minimum_wipe_company_portal_version = value
    
    @property
    def minimum_wipe_patch_version(self,) -> Optional[str]:
        """
        Gets the minimumWipePatchVersion property value. Android security patch level  less than or equal to the specified value will wipe the managed app and the associated company data.
        Returns: Optional[str]
        """
        return self._minimum_wipe_patch_version
    
    @minimum_wipe_patch_version.setter
    def minimum_wipe_patch_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWipePatchVersion property value. Android security patch level  less than or equal to the specified value will wipe the managed app and the associated company data.
        Args:
            value: Value to set for the minimumWipePatchVersion property.
        """
        self._minimum_wipe_patch_version = value
    
    @property
    def require_class3_biometrics(self,) -> Optional[bool]:
        """
        Gets the requireClass3Biometrics property value. Require user to apply Class 3 Biometrics on their Android device.
        Returns: Optional[bool]
        """
        return self._require_class3_biometrics
    
    @require_class3_biometrics.setter
    def require_class3_biometrics(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireClass3Biometrics property value. Require user to apply Class 3 Biometrics on their Android device.
        Args:
            value: Value to set for the requireClass3Biometrics property.
        """
        self._require_class3_biometrics = value
    
    @property
    def required_android_safety_net_apps_verification_type(self,) -> Optional[android_managed_app_safety_net_apps_verification_type.AndroidManagedAppSafetyNetAppsVerificationType]:
        """
        Gets the requiredAndroidSafetyNetAppsVerificationType property value. An admin enforced Android SafetyNet Device Attestation requirement on a managed app.
        Returns: Optional[android_managed_app_safety_net_apps_verification_type.AndroidManagedAppSafetyNetAppsVerificationType]
        """
        return self._required_android_safety_net_apps_verification_type
    
    @required_android_safety_net_apps_verification_type.setter
    def required_android_safety_net_apps_verification_type(self,value: Optional[android_managed_app_safety_net_apps_verification_type.AndroidManagedAppSafetyNetAppsVerificationType] = None) -> None:
        """
        Sets the requiredAndroidSafetyNetAppsVerificationType property value. An admin enforced Android SafetyNet Device Attestation requirement on a managed app.
        Args:
            value: Value to set for the requiredAndroidSafetyNetAppsVerificationType property.
        """
        self._required_android_safety_net_apps_verification_type = value
    
    @property
    def required_android_safety_net_device_attestation_type(self,) -> Optional[android_managed_app_safety_net_device_attestation_type.AndroidManagedAppSafetyNetDeviceAttestationType]:
        """
        Gets the requiredAndroidSafetyNetDeviceAttestationType property value. An admin enforced Android SafetyNet Device Attestation requirement on a managed app.
        Returns: Optional[android_managed_app_safety_net_device_attestation_type.AndroidManagedAppSafetyNetDeviceAttestationType]
        """
        return self._required_android_safety_net_device_attestation_type
    
    @required_android_safety_net_device_attestation_type.setter
    def required_android_safety_net_device_attestation_type(self,value: Optional[android_managed_app_safety_net_device_attestation_type.AndroidManagedAppSafetyNetDeviceAttestationType] = None) -> None:
        """
        Sets the requiredAndroidSafetyNetDeviceAttestationType property value. An admin enforced Android SafetyNet Device Attestation requirement on a managed app.
        Args:
            value: Value to set for the requiredAndroidSafetyNetDeviceAttestationType property.
        """
        self._required_android_safety_net_device_attestation_type = value
    
    @property
    def required_android_safety_net_evaluation_type(self,) -> Optional[android_managed_app_safety_net_evaluation_type.AndroidManagedAppSafetyNetEvaluationType]:
        """
        Gets the requiredAndroidSafetyNetEvaluationType property value. An admin enforced Android SafetyNet evaluation type requirement on a managed app.
        Returns: Optional[android_managed_app_safety_net_evaluation_type.AndroidManagedAppSafetyNetEvaluationType]
        """
        return self._required_android_safety_net_evaluation_type
    
    @required_android_safety_net_evaluation_type.setter
    def required_android_safety_net_evaluation_type(self,value: Optional[android_managed_app_safety_net_evaluation_type.AndroidManagedAppSafetyNetEvaluationType] = None) -> None:
        """
        Sets the requiredAndroidSafetyNetEvaluationType property value. An admin enforced Android SafetyNet evaluation type requirement on a managed app.
        Args:
            value: Value to set for the requiredAndroidSafetyNetEvaluationType property.
        """
        self._required_android_safety_net_evaluation_type = value
    
    @property
    def require_pin_after_biometric_change(self,) -> Optional[bool]:
        """
        Gets the requirePinAfterBiometricChange property value. A PIN prompt will override biometric prompts if class 3 biometrics are updated on the device.
        Returns: Optional[bool]
        """
        return self._require_pin_after_biometric_change
    
    @require_pin_after_biometric_change.setter
    def require_pin_after_biometric_change(self,value: Optional[bool] = None) -> None:
        """
        Sets the requirePinAfterBiometricChange property value. A PIN prompt will override biometric prompts if class 3 biometrics are updated on the device.
        Args:
            value: Value to set for the requirePinAfterBiometricChange property.
        """
        self._require_pin_after_biometric_change = value
    
    @property
    def screen_capture_blocked(self,) -> Optional[bool]:
        """
        Gets the screenCaptureBlocked property value. Indicates whether a managed user can take screen captures of managed apps
        Returns: Optional[bool]
        """
        return self._screen_capture_blocked
    
    @screen_capture_blocked.setter
    def screen_capture_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the screenCaptureBlocked property value. Indicates whether a managed user can take screen captures of managed apps
        Args:
            value: Value to set for the screenCaptureBlocked property.
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
        writer.write_str_value("allowedAndroidDeviceManufacturers", self.allowed_android_device_manufacturers)
        writer.write_collection_of_primitive_values("allowedAndroidDeviceModels", self.allowed_android_device_models)
        writer.write_enum_value("appActionIfAndroidDeviceManufacturerNotAllowed", self.app_action_if_android_device_manufacturer_not_allowed)
        writer.write_enum_value("appActionIfAndroidDeviceModelNotAllowed", self.app_action_if_android_device_model_not_allowed)
        writer.write_enum_value("appActionIfAndroidSafetyNetAppsVerificationFailed", self.app_action_if_android_safety_net_apps_verification_failed)
        writer.write_enum_value("appActionIfAndroidSafetyNetDeviceAttestationFailed", self.app_action_if_android_safety_net_device_attestation_failed)
        writer.write_enum_value("appActionIfDeviceLockNotSet", self.app_action_if_device_lock_not_set)
        writer.write_enum_value("appActionIfDevicePasscodeComplexityLessThanHigh", self.app_action_if_device_passcode_complexity_less_than_high)
        writer.write_enum_value("appActionIfDevicePasscodeComplexityLessThanLow", self.app_action_if_device_passcode_complexity_less_than_low)
        writer.write_enum_value("appActionIfDevicePasscodeComplexityLessThanMedium", self.app_action_if_device_passcode_complexity_less_than_medium)
        writer.write_collection_of_object_values("approvedKeyboards", self.approved_keyboards)
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_bool_value("biometricAuthenticationBlocked", self.biometric_authentication_blocked)
        writer.write_int_value("blockAfterCompanyPortalUpdateDeferralInDays", self.block_after_company_portal_update_deferral_in_days)
        writer.write_bool_value("connectToVpnOnLaunch", self.connect_to_vpn_on_launch)
        writer.write_str_value("customBrowserDisplayName", self.custom_browser_display_name)
        writer.write_str_value("customBrowserPackageId", self.custom_browser_package_id)
        writer.write_str_value("customDialerAppDisplayName", self.custom_dialer_app_display_name)
        writer.write_str_value("customDialerAppPackageId", self.custom_dialer_app_package_id)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_object_value("deploymentSummary", self.deployment_summary)
        writer.write_bool_value("deviceLockRequired", self.device_lock_required)
        writer.write_bool_value("disableAppEncryptionIfDeviceEncryptionIsEnabled", self.disable_app_encryption_if_device_encryption_is_enabled)
        writer.write_bool_value("encryptAppData", self.encrypt_app_data)
        writer.write_collection_of_object_values("exemptedAppPackages", self.exempted_app_packages)
        writer.write_bool_value("fingerprintAndBiometricEnabled", self.fingerprint_and_biometric_enabled)
        writer.write_bool_value("keyboardsRestricted", self.keyboards_restricted)
        writer.write_str_value("minimumRequiredCompanyPortalVersion", self.minimum_required_company_portal_version)
        writer.write_str_value("minimumRequiredPatchVersion", self.minimum_required_patch_version)
        writer.write_str_value("minimumWarningCompanyPortalVersion", self.minimum_warning_company_portal_version)
        writer.write_str_value("minimumWarningPatchVersion", self.minimum_warning_patch_version)
        writer.write_str_value("minimumWipeCompanyPortalVersion", self.minimum_wipe_company_portal_version)
        writer.write_str_value("minimumWipePatchVersion", self.minimum_wipe_patch_version)
        writer.write_bool_value("requireClass3Biometrics", self.require_class3_biometrics)
        writer.write_enum_value("requiredAndroidSafetyNetAppsVerificationType", self.required_android_safety_net_apps_verification_type)
        writer.write_enum_value("requiredAndroidSafetyNetDeviceAttestationType", self.required_android_safety_net_device_attestation_type)
        writer.write_enum_value("requiredAndroidSafetyNetEvaluationType", self.required_android_safety_net_evaluation_type)
        writer.write_bool_value("requirePinAfterBiometricChange", self.require_pin_after_biometric_change)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_int_value("warnAfterCompanyPortalUpdateDeferralInDays", self.warn_after_company_portal_update_deferral_in_days)
        writer.write_int_value("wipeAfterCompanyPortalUpdateDeferralInDays", self.wipe_after_company_portal_update_deferral_in_days)
    
    @property
    def warn_after_company_portal_update_deferral_in_days(self,) -> Optional[int]:
        """
        Gets the warnAfterCompanyPortalUpdateDeferralInDays property value. Maximum number of days Company Portal update can be deferred on the device or the user will receive the warning
        Returns: Optional[int]
        """
        return self._warn_after_company_portal_update_deferral_in_days
    
    @warn_after_company_portal_update_deferral_in_days.setter
    def warn_after_company_portal_update_deferral_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the warnAfterCompanyPortalUpdateDeferralInDays property value. Maximum number of days Company Portal update can be deferred on the device or the user will receive the warning
        Args:
            value: Value to set for the warnAfterCompanyPortalUpdateDeferralInDays property.
        """
        self._warn_after_company_portal_update_deferral_in_days = value
    
    @property
    def wipe_after_company_portal_update_deferral_in_days(self,) -> Optional[int]:
        """
        Gets the wipeAfterCompanyPortalUpdateDeferralInDays property value. Maximum number of days Company Portal update can be deferred on the device or the company data on the app will be wiped
        Returns: Optional[int]
        """
        return self._wipe_after_company_portal_update_deferral_in_days
    
    @wipe_after_company_portal_update_deferral_in_days.setter
    def wipe_after_company_portal_update_deferral_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the wipeAfterCompanyPortalUpdateDeferralInDays property value. Maximum number of days Company Portal update can be deferred on the device or the company data on the app will be wiped
        Args:
            value: Value to set for the wipeAfterCompanyPortalUpdateDeferralInDays property.
        """
        self._wipe_after_company_portal_update_deferral_in_days = value
    

