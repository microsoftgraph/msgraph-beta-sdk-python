from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

dep_enrollment_base_profile = lazy_import('msgraph.generated.models.dep_enrollment_base_profile')
i_tunes_pairing_mode = lazy_import('msgraph.generated.models.i_tunes_pairing_mode')
management_certificate_with_thumbprint = lazy_import('msgraph.generated.models.management_certificate_with_thumbprint')

class DepIOSEnrollmentProfile(dep_enrollment_base_profile.DepEnrollmentBaseProfile):
    @property
    def appearance_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the appearanceScreenDisabled property value. Indicates if Apperance screen is disabled
        Returns: Optional[bool]
        """
        return self._appearance_screen_disabled
    
    @appearance_screen_disabled.setter
    def appearance_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the appearanceScreenDisabled property value. Indicates if Apperance screen is disabled
        Args:
            value: Value to set for the appearanceScreenDisabled property.
        """
        self._appearance_screen_disabled = value
    
    @property
    def await_device_configured_confirmation(self,) -> Optional[bool]:
        """
        Gets the awaitDeviceConfiguredConfirmation property value. Indicates if the device will need to wait for configured confirmation
        Returns: Optional[bool]
        """
        return self._await_device_configured_confirmation
    
    @await_device_configured_confirmation.setter
    def await_device_configured_confirmation(self,value: Optional[bool] = None) -> None:
        """
        Sets the awaitDeviceConfiguredConfirmation property value. Indicates if the device will need to wait for configured confirmation
        Args:
            value: Value to set for the awaitDeviceConfiguredConfirmation property.
        """
        self._await_device_configured_confirmation = value
    
    @property
    def carrier_activation_url(self,) -> Optional[str]:
        """
        Gets the carrierActivationUrl property value. Carrier URL for activating device eSIM.
        Returns: Optional[str]
        """
        return self._carrier_activation_url
    
    @carrier_activation_url.setter
    def carrier_activation_url(self,value: Optional[str] = None) -> None:
        """
        Sets the carrierActivationUrl property value. Carrier URL for activating device eSIM.
        Args:
            value: Value to set for the carrierActivationUrl property.
        """
        self._carrier_activation_url = value
    
    @property
    def company_portal_vpp_token_id(self,) -> Optional[str]:
        """
        Gets the companyPortalVppTokenId property value. If set, indicates which Vpp token should be used to deploy the Company Portal w/ device licensing. 'enableAuthenticationViaCompanyPortal' must be set in order for this property to be set.
        Returns: Optional[str]
        """
        return self._company_portal_vpp_token_id
    
    @company_portal_vpp_token_id.setter
    def company_portal_vpp_token_id(self,value: Optional[str] = None) -> None:
        """
        Sets the companyPortalVppTokenId property value. If set, indicates which Vpp token should be used to deploy the Company Portal w/ device licensing. 'enableAuthenticationViaCompanyPortal' must be set in order for this property to be set.
        Args:
            value: Value to set for the companyPortalVppTokenId property.
        """
        self._company_portal_vpp_token_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DepIOSEnrollmentProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.depIOSEnrollmentProfile"
        # Indicates if Apperance screen is disabled
        self._appearance_screen_disabled: Optional[bool] = None
        # Indicates if the device will need to wait for configured confirmation
        self._await_device_configured_confirmation: Optional[bool] = None
        # Carrier URL for activating device eSIM.
        self._carrier_activation_url: Optional[str] = None
        # If set, indicates which Vpp token should be used to deploy the Company Portal w/ device licensing. 'enableAuthenticationViaCompanyPortal' must be set in order for this property to be set.
        self._company_portal_vpp_token_id: Optional[str] = None
        # Indicates if Device To Device Migration is disabled
        self._device_to_device_migration_disabled: Optional[bool] = None
        # This indicates whether the device is to be enrolled in a mode which enables multi user scenarios. Only applicable in shared iPads.
        self._enable_shared_i_pad: Optional[bool] = None
        # Tells the device to enable single app mode and apply app-lock during enrollment. Default is false. 'enableAuthenticationViaCompanyPortal' and 'companyPortalVppTokenId' must be set for this property to be set.
        self._enable_single_app_enrollment_mode: Optional[bool] = None
        # Indicates if Express Language screen is disabled
        self._express_language_screen_disabled: Optional[bool] = None
        # Indicates if temporary sessions is enabled
        self._force_temporary_session: Optional[bool] = None
        # Indicates if home button sensitivity screen is disabled
        self._home_button_screen_disabled: Optional[bool] = None
        # Indicates if iMessage and FaceTime screen is disabled
        self._i_message_and_face_time_screen_disabled: Optional[bool] = None
        # The iTunesPairingMode property
        self._i_tunes_pairing_mode: Optional[i_tunes_pairing_mode.ITunesPairingMode] = None
        # Management certificates for Apple Configurator
        self._management_certificates: Optional[List[management_certificate_with_thumbprint.ManagementCertificateWithThumbprint]] = None
        # Indicates if onboarding setup screen is disabled
        self._on_boarding_screen_disabled: Optional[bool] = None
        # Indicates if Passcode setup pane is disabled
        self._pass_code_disabled: Optional[bool] = None
        # Indicates timeout before locked screen requires the user to enter the device passocde to unlock it
        self._passcode_lock_grace_period_in_seconds: Optional[int] = None
        # Indicates if Preferred language screen is disabled
        self._preferred_language_screen_disabled: Optional[bool] = None
        # Indicates if Weclome screen is disabled
        self._restore_completed_screen_disabled: Optional[bool] = None
        # Indicates if Restore from Android is disabled
        self._restore_from_android_disabled: Optional[bool] = None
        # This specifies the maximum number of users that can use a shared iPad. Only applicable in shared iPad mode.
        self._shared_i_pad_maximum_user_count: Optional[int] = None
        # Indicates if the SIMSetup screen is disabled
        self._sim_setup_screen_disabled: Optional[bool] = None
        # Indicates if the mandatory sofware update screen is disabled
        self._software_update_screen_disabled: Optional[bool] = None
        # Indicates timeout of temporary session
        self._temporary_session_timeout_in_seconds: Optional[int] = None
        # Indicates if Weclome screen is disabled
        self._update_complete_screen_disabled: Optional[bool] = None
        # Indicates that this apple device is designated to support 'shared device mode' scenarios. This is distinct from the 'shared iPad' scenario. See https://learn.microsoft.com/mem/intune/enrollment/device-enrollment-shared-ios
        self._userless_shared_aad_mode_enabled: Optional[bool] = None
        # Indicates timeout of temporary session
        self._user_session_timeout_in_seconds: Optional[int] = None
        # Indicates if the watch migration screen is disabled
        self._watch_migration_screen_disabled: Optional[bool] = None
        # Indicates if Weclome screen is disabled
        self._welcome_screen_disabled: Optional[bool] = None
        # Indicates if zoom setup pane is disabled
        self._zoom_disabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DepIOSEnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DepIOSEnrollmentProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DepIOSEnrollmentProfile()
    
    @property
    def device_to_device_migration_disabled(self,) -> Optional[bool]:
        """
        Gets the deviceToDeviceMigrationDisabled property value. Indicates if Device To Device Migration is disabled
        Returns: Optional[bool]
        """
        return self._device_to_device_migration_disabled
    
    @device_to_device_migration_disabled.setter
    def device_to_device_migration_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceToDeviceMigrationDisabled property value. Indicates if Device To Device Migration is disabled
        Args:
            value: Value to set for the deviceToDeviceMigrationDisabled property.
        """
        self._device_to_device_migration_disabled = value
    
    @property
    def enable_shared_i_pad(self,) -> Optional[bool]:
        """
        Gets the enableSharedIPad property value. This indicates whether the device is to be enrolled in a mode which enables multi user scenarios. Only applicable in shared iPads.
        Returns: Optional[bool]
        """
        return self._enable_shared_i_pad
    
    @enable_shared_i_pad.setter
    def enable_shared_i_pad(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableSharedIPad property value. This indicates whether the device is to be enrolled in a mode which enables multi user scenarios. Only applicable in shared iPads.
        Args:
            value: Value to set for the enableSharedIPad property.
        """
        self._enable_shared_i_pad = value
    
    @property
    def enable_single_app_enrollment_mode(self,) -> Optional[bool]:
        """
        Gets the enableSingleAppEnrollmentMode property value. Tells the device to enable single app mode and apply app-lock during enrollment. Default is false. 'enableAuthenticationViaCompanyPortal' and 'companyPortalVppTokenId' must be set for this property to be set.
        Returns: Optional[bool]
        """
        return self._enable_single_app_enrollment_mode
    
    @enable_single_app_enrollment_mode.setter
    def enable_single_app_enrollment_mode(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableSingleAppEnrollmentMode property value. Tells the device to enable single app mode and apply app-lock during enrollment. Default is false. 'enableAuthenticationViaCompanyPortal' and 'companyPortalVppTokenId' must be set for this property to be set.
        Args:
            value: Value to set for the enableSingleAppEnrollmentMode property.
        """
        self._enable_single_app_enrollment_mode = value
    
    @property
    def express_language_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the expressLanguageScreenDisabled property value. Indicates if Express Language screen is disabled
        Returns: Optional[bool]
        """
        return self._express_language_screen_disabled
    
    @express_language_screen_disabled.setter
    def express_language_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the expressLanguageScreenDisabled property value. Indicates if Express Language screen is disabled
        Args:
            value: Value to set for the expressLanguageScreenDisabled property.
        """
        self._express_language_screen_disabled = value
    
    @property
    def force_temporary_session(self,) -> Optional[bool]:
        """
        Gets the forceTemporarySession property value. Indicates if temporary sessions is enabled
        Returns: Optional[bool]
        """
        return self._force_temporary_session
    
    @force_temporary_session.setter
    def force_temporary_session(self,value: Optional[bool] = None) -> None:
        """
        Sets the forceTemporarySession property value. Indicates if temporary sessions is enabled
        Args:
            value: Value to set for the forceTemporarySession property.
        """
        self._force_temporary_session = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "appearance_screen_disabled": lambda n : setattr(self, 'appearance_screen_disabled', n.get_bool_value()),
            "await_device_configured_confirmation": lambda n : setattr(self, 'await_device_configured_confirmation', n.get_bool_value()),
            "carrier_activation_url": lambda n : setattr(self, 'carrier_activation_url', n.get_str_value()),
            "company_portal_vpp_token_id": lambda n : setattr(self, 'company_portal_vpp_token_id', n.get_str_value()),
            "device_to_device_migration_disabled": lambda n : setattr(self, 'device_to_device_migration_disabled', n.get_bool_value()),
            "enable_shared_i_pad": lambda n : setattr(self, 'enable_shared_i_pad', n.get_bool_value()),
            "enable_single_app_enrollment_mode": lambda n : setattr(self, 'enable_single_app_enrollment_mode', n.get_bool_value()),
            "express_language_screen_disabled": lambda n : setattr(self, 'express_language_screen_disabled', n.get_bool_value()),
            "force_temporary_session": lambda n : setattr(self, 'force_temporary_session', n.get_bool_value()),
            "home_button_screen_disabled": lambda n : setattr(self, 'home_button_screen_disabled', n.get_bool_value()),
            "i_message_and_face_time_screen_disabled": lambda n : setattr(self, 'i_message_and_face_time_screen_disabled', n.get_bool_value()),
            "i_tunes_pairing_mode": lambda n : setattr(self, 'i_tunes_pairing_mode', n.get_enum_value(i_tunes_pairing_mode.ITunesPairingMode)),
            "management_certificates": lambda n : setattr(self, 'management_certificates', n.get_collection_of_object_values(management_certificate_with_thumbprint.ManagementCertificateWithThumbprint)),
            "on_boarding_screen_disabled": lambda n : setattr(self, 'on_boarding_screen_disabled', n.get_bool_value()),
            "pass_code_disabled": lambda n : setattr(self, 'pass_code_disabled', n.get_bool_value()),
            "passcode_lock_grace_period_in_seconds": lambda n : setattr(self, 'passcode_lock_grace_period_in_seconds', n.get_int_value()),
            "preferred_language_screen_disabled": lambda n : setattr(self, 'preferred_language_screen_disabled', n.get_bool_value()),
            "restore_completed_screen_disabled": lambda n : setattr(self, 'restore_completed_screen_disabled', n.get_bool_value()),
            "restore_from_android_disabled": lambda n : setattr(self, 'restore_from_android_disabled', n.get_bool_value()),
            "shared_i_pad_maximum_user_count": lambda n : setattr(self, 'shared_i_pad_maximum_user_count', n.get_int_value()),
            "sim_setup_screen_disabled": lambda n : setattr(self, 'sim_setup_screen_disabled', n.get_bool_value()),
            "software_update_screen_disabled": lambda n : setattr(self, 'software_update_screen_disabled', n.get_bool_value()),
            "temporary_session_timeout_in_seconds": lambda n : setattr(self, 'temporary_session_timeout_in_seconds', n.get_int_value()),
            "update_complete_screen_disabled": lambda n : setattr(self, 'update_complete_screen_disabled', n.get_bool_value()),
            "userless_shared_aad_mode_enabled": lambda n : setattr(self, 'userless_shared_aad_mode_enabled', n.get_bool_value()),
            "user_session_timeout_in_seconds": lambda n : setattr(self, 'user_session_timeout_in_seconds', n.get_int_value()),
            "watch_migration_screen_disabled": lambda n : setattr(self, 'watch_migration_screen_disabled', n.get_bool_value()),
            "welcome_screen_disabled": lambda n : setattr(self, 'welcome_screen_disabled', n.get_bool_value()),
            "zoom_disabled": lambda n : setattr(self, 'zoom_disabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def home_button_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the homeButtonScreenDisabled property value. Indicates if home button sensitivity screen is disabled
        Returns: Optional[bool]
        """
        return self._home_button_screen_disabled
    
    @home_button_screen_disabled.setter
    def home_button_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the homeButtonScreenDisabled property value. Indicates if home button sensitivity screen is disabled
        Args:
            value: Value to set for the homeButtonScreenDisabled property.
        """
        self._home_button_screen_disabled = value
    
    @property
    def i_message_and_face_time_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the iMessageAndFaceTimeScreenDisabled property value. Indicates if iMessage and FaceTime screen is disabled
        Returns: Optional[bool]
        """
        return self._i_message_and_face_time_screen_disabled
    
    @i_message_and_face_time_screen_disabled.setter
    def i_message_and_face_time_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the iMessageAndFaceTimeScreenDisabled property value. Indicates if iMessage and FaceTime screen is disabled
        Args:
            value: Value to set for the iMessageAndFaceTimeScreenDisabled property.
        """
        self._i_message_and_face_time_screen_disabled = value
    
    @property
    def i_tunes_pairing_mode(self,) -> Optional[i_tunes_pairing_mode.ITunesPairingMode]:
        """
        Gets the iTunesPairingMode property value. The iTunesPairingMode property
        Returns: Optional[i_tunes_pairing_mode.ITunesPairingMode]
        """
        return self._i_tunes_pairing_mode
    
    @i_tunes_pairing_mode.setter
    def i_tunes_pairing_mode(self,value: Optional[i_tunes_pairing_mode.ITunesPairingMode] = None) -> None:
        """
        Sets the iTunesPairingMode property value. The iTunesPairingMode property
        Args:
            value: Value to set for the iTunesPairingMode property.
        """
        self._i_tunes_pairing_mode = value
    
    @property
    def management_certificates(self,) -> Optional[List[management_certificate_with_thumbprint.ManagementCertificateWithThumbprint]]:
        """
        Gets the managementCertificates property value. Management certificates for Apple Configurator
        Returns: Optional[List[management_certificate_with_thumbprint.ManagementCertificateWithThumbprint]]
        """
        return self._management_certificates
    
    @management_certificates.setter
    def management_certificates(self,value: Optional[List[management_certificate_with_thumbprint.ManagementCertificateWithThumbprint]] = None) -> None:
        """
        Sets the managementCertificates property value. Management certificates for Apple Configurator
        Args:
            value: Value to set for the managementCertificates property.
        """
        self._management_certificates = value
    
    @property
    def on_boarding_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the onBoardingScreenDisabled property value. Indicates if onboarding setup screen is disabled
        Returns: Optional[bool]
        """
        return self._on_boarding_screen_disabled
    
    @on_boarding_screen_disabled.setter
    def on_boarding_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the onBoardingScreenDisabled property value. Indicates if onboarding setup screen is disabled
        Args:
            value: Value to set for the onBoardingScreenDisabled property.
        """
        self._on_boarding_screen_disabled = value
    
    @property
    def pass_code_disabled(self,) -> Optional[bool]:
        """
        Gets the passCodeDisabled property value. Indicates if Passcode setup pane is disabled
        Returns: Optional[bool]
        """
        return self._pass_code_disabled
    
    @pass_code_disabled.setter
    def pass_code_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the passCodeDisabled property value. Indicates if Passcode setup pane is disabled
        Args:
            value: Value to set for the passCodeDisabled property.
        """
        self._pass_code_disabled = value
    
    @property
    def passcode_lock_grace_period_in_seconds(self,) -> Optional[int]:
        """
        Gets the passcodeLockGracePeriodInSeconds property value. Indicates timeout before locked screen requires the user to enter the device passocde to unlock it
        Returns: Optional[int]
        """
        return self._passcode_lock_grace_period_in_seconds
    
    @passcode_lock_grace_period_in_seconds.setter
    def passcode_lock_grace_period_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeLockGracePeriodInSeconds property value. Indicates timeout before locked screen requires the user to enter the device passocde to unlock it
        Args:
            value: Value to set for the passcodeLockGracePeriodInSeconds property.
        """
        self._passcode_lock_grace_period_in_seconds = value
    
    @property
    def preferred_language_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the preferredLanguageScreenDisabled property value. Indicates if Preferred language screen is disabled
        Returns: Optional[bool]
        """
        return self._preferred_language_screen_disabled
    
    @preferred_language_screen_disabled.setter
    def preferred_language_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the preferredLanguageScreenDisabled property value. Indicates if Preferred language screen is disabled
        Args:
            value: Value to set for the preferredLanguageScreenDisabled property.
        """
        self._preferred_language_screen_disabled = value
    
    @property
    def restore_completed_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the restoreCompletedScreenDisabled property value. Indicates if Weclome screen is disabled
        Returns: Optional[bool]
        """
        return self._restore_completed_screen_disabled
    
    @restore_completed_screen_disabled.setter
    def restore_completed_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the restoreCompletedScreenDisabled property value. Indicates if Weclome screen is disabled
        Args:
            value: Value to set for the restoreCompletedScreenDisabled property.
        """
        self._restore_completed_screen_disabled = value
    
    @property
    def restore_from_android_disabled(self,) -> Optional[bool]:
        """
        Gets the restoreFromAndroidDisabled property value. Indicates if Restore from Android is disabled
        Returns: Optional[bool]
        """
        return self._restore_from_android_disabled
    
    @restore_from_android_disabled.setter
    def restore_from_android_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the restoreFromAndroidDisabled property value. Indicates if Restore from Android is disabled
        Args:
            value: Value to set for the restoreFromAndroidDisabled property.
        """
        self._restore_from_android_disabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("appearanceScreenDisabled", self.appearance_screen_disabled)
        writer.write_bool_value("awaitDeviceConfiguredConfirmation", self.await_device_configured_confirmation)
        writer.write_str_value("carrierActivationUrl", self.carrier_activation_url)
        writer.write_str_value("companyPortalVppTokenId", self.company_portal_vpp_token_id)
        writer.write_bool_value("deviceToDeviceMigrationDisabled", self.device_to_device_migration_disabled)
        writer.write_bool_value("enableSharedIPad", self.enable_shared_i_pad)
        writer.write_bool_value("enableSingleAppEnrollmentMode", self.enable_single_app_enrollment_mode)
        writer.write_bool_value("expressLanguageScreenDisabled", self.express_language_screen_disabled)
        writer.write_bool_value("forceTemporarySession", self.force_temporary_session)
        writer.write_bool_value("homeButtonScreenDisabled", self.home_button_screen_disabled)
        writer.write_bool_value("iMessageAndFaceTimeScreenDisabled", self.i_message_and_face_time_screen_disabled)
        writer.write_enum_value("iTunesPairingMode", self.i_tunes_pairing_mode)
        writer.write_collection_of_object_values("managementCertificates", self.management_certificates)
        writer.write_bool_value("onBoardingScreenDisabled", self.on_boarding_screen_disabled)
        writer.write_bool_value("passCodeDisabled", self.pass_code_disabled)
        writer.write_int_value("passcodeLockGracePeriodInSeconds", self.passcode_lock_grace_period_in_seconds)
        writer.write_bool_value("preferredLanguageScreenDisabled", self.preferred_language_screen_disabled)
        writer.write_bool_value("restoreCompletedScreenDisabled", self.restore_completed_screen_disabled)
        writer.write_bool_value("restoreFromAndroidDisabled", self.restore_from_android_disabled)
        writer.write_int_value("sharedIPadMaximumUserCount", self.shared_i_pad_maximum_user_count)
        writer.write_bool_value("simSetupScreenDisabled", self.sim_setup_screen_disabled)
        writer.write_bool_value("softwareUpdateScreenDisabled", self.software_update_screen_disabled)
        writer.write_int_value("temporarySessionTimeoutInSeconds", self.temporary_session_timeout_in_seconds)
        writer.write_bool_value("updateCompleteScreenDisabled", self.update_complete_screen_disabled)
        writer.write_bool_value("userlessSharedAadModeEnabled", self.userless_shared_aad_mode_enabled)
        writer.write_int_value("userSessionTimeoutInSeconds", self.user_session_timeout_in_seconds)
        writer.write_bool_value("watchMigrationScreenDisabled", self.watch_migration_screen_disabled)
        writer.write_bool_value("welcomeScreenDisabled", self.welcome_screen_disabled)
        writer.write_bool_value("zoomDisabled", self.zoom_disabled)
    
    @property
    def shared_i_pad_maximum_user_count(self,) -> Optional[int]:
        """
        Gets the sharedIPadMaximumUserCount property value. This specifies the maximum number of users that can use a shared iPad. Only applicable in shared iPad mode.
        Returns: Optional[int]
        """
        return self._shared_i_pad_maximum_user_count
    
    @shared_i_pad_maximum_user_count.setter
    def shared_i_pad_maximum_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the sharedIPadMaximumUserCount property value. This specifies the maximum number of users that can use a shared iPad. Only applicable in shared iPad mode.
        Args:
            value: Value to set for the sharedIPadMaximumUserCount property.
        """
        self._shared_i_pad_maximum_user_count = value
    
    @property
    def sim_setup_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the simSetupScreenDisabled property value. Indicates if the SIMSetup screen is disabled
        Returns: Optional[bool]
        """
        return self._sim_setup_screen_disabled
    
    @sim_setup_screen_disabled.setter
    def sim_setup_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the simSetupScreenDisabled property value. Indicates if the SIMSetup screen is disabled
        Args:
            value: Value to set for the simSetupScreenDisabled property.
        """
        self._sim_setup_screen_disabled = value
    
    @property
    def software_update_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the softwareUpdateScreenDisabled property value. Indicates if the mandatory sofware update screen is disabled
        Returns: Optional[bool]
        """
        return self._software_update_screen_disabled
    
    @software_update_screen_disabled.setter
    def software_update_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the softwareUpdateScreenDisabled property value. Indicates if the mandatory sofware update screen is disabled
        Args:
            value: Value to set for the softwareUpdateScreenDisabled property.
        """
        self._software_update_screen_disabled = value
    
    @property
    def temporary_session_timeout_in_seconds(self,) -> Optional[int]:
        """
        Gets the temporarySessionTimeoutInSeconds property value. Indicates timeout of temporary session
        Returns: Optional[int]
        """
        return self._temporary_session_timeout_in_seconds
    
    @temporary_session_timeout_in_seconds.setter
    def temporary_session_timeout_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the temporarySessionTimeoutInSeconds property value. Indicates timeout of temporary session
        Args:
            value: Value to set for the temporarySessionTimeoutInSeconds property.
        """
        self._temporary_session_timeout_in_seconds = value
    
    @property
    def update_complete_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the updateCompleteScreenDisabled property value. Indicates if Weclome screen is disabled
        Returns: Optional[bool]
        """
        return self._update_complete_screen_disabled
    
    @update_complete_screen_disabled.setter
    def update_complete_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the updateCompleteScreenDisabled property value. Indicates if Weclome screen is disabled
        Args:
            value: Value to set for the updateCompleteScreenDisabled property.
        """
        self._update_complete_screen_disabled = value
    
    @property
    def userless_shared_aad_mode_enabled(self,) -> Optional[bool]:
        """
        Gets the userlessSharedAadModeEnabled property value. Indicates that this apple device is designated to support 'shared device mode' scenarios. This is distinct from the 'shared iPad' scenario. See https://learn.microsoft.com/mem/intune/enrollment/device-enrollment-shared-ios
        Returns: Optional[bool]
        """
        return self._userless_shared_aad_mode_enabled
    
    @userless_shared_aad_mode_enabled.setter
    def userless_shared_aad_mode_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the userlessSharedAadModeEnabled property value. Indicates that this apple device is designated to support 'shared device mode' scenarios. This is distinct from the 'shared iPad' scenario. See https://learn.microsoft.com/mem/intune/enrollment/device-enrollment-shared-ios
        Args:
            value: Value to set for the userlessSharedAadModeEnabled property.
        """
        self._userless_shared_aad_mode_enabled = value
    
    @property
    def user_session_timeout_in_seconds(self,) -> Optional[int]:
        """
        Gets the userSessionTimeoutInSeconds property value. Indicates timeout of temporary session
        Returns: Optional[int]
        """
        return self._user_session_timeout_in_seconds
    
    @user_session_timeout_in_seconds.setter
    def user_session_timeout_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the userSessionTimeoutInSeconds property value. Indicates timeout of temporary session
        Args:
            value: Value to set for the userSessionTimeoutInSeconds property.
        """
        self._user_session_timeout_in_seconds = value
    
    @property
    def watch_migration_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the watchMigrationScreenDisabled property value. Indicates if the watch migration screen is disabled
        Returns: Optional[bool]
        """
        return self._watch_migration_screen_disabled
    
    @watch_migration_screen_disabled.setter
    def watch_migration_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the watchMigrationScreenDisabled property value. Indicates if the watch migration screen is disabled
        Args:
            value: Value to set for the watchMigrationScreenDisabled property.
        """
        self._watch_migration_screen_disabled = value
    
    @property
    def welcome_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the welcomeScreenDisabled property value. Indicates if Weclome screen is disabled
        Returns: Optional[bool]
        """
        return self._welcome_screen_disabled
    
    @welcome_screen_disabled.setter
    def welcome_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the welcomeScreenDisabled property value. Indicates if Weclome screen is disabled
        Args:
            value: Value to set for the welcomeScreenDisabled property.
        """
        self._welcome_screen_disabled = value
    
    @property
    def zoom_disabled(self,) -> Optional[bool]:
        """
        Gets the zoomDisabled property value. Indicates if zoom setup pane is disabled
        Returns: Optional[bool]
        """
        return self._zoom_disabled
    
    @zoom_disabled.setter
    def zoom_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the zoomDisabled property value. Indicates if zoom setup pane is disabled
        Args:
            value: Value to set for the zoomDisabled property.
        """
        self._zoom_disabled = value
    

