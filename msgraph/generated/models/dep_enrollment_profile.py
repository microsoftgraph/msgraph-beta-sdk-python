from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

enrollment_profile = lazy_import('msgraph.generated.models.enrollment_profile')
i_tunes_pairing_mode = lazy_import('msgraph.generated.models.i_tunes_pairing_mode')
management_certificate_with_thumbprint = lazy_import('msgraph.generated.models.management_certificate_with_thumbprint')

class DepEnrollmentProfile(enrollment_profile.EnrollmentProfile):
    @property
    def apple_id_disabled(self,) -> Optional[bool]:
        """
        Gets the appleIdDisabled property value. Indicates if Apple id setup pane is disabled
        Returns: Optional[bool]
        """
        return self._apple_id_disabled
    
    @apple_id_disabled.setter
    def apple_id_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the appleIdDisabled property value. Indicates if Apple id setup pane is disabled
        Args:
            value: Value to set for the appleIdDisabled property.
        """
        self._apple_id_disabled = value
    
    @property
    def apple_pay_disabled(self,) -> Optional[bool]:
        """
        Gets the applePayDisabled property value. Indicates if Apple pay setup pane is disabled
        Returns: Optional[bool]
        """
        return self._apple_pay_disabled
    
    @apple_pay_disabled.setter
    def apple_pay_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the applePayDisabled property value. Indicates if Apple pay setup pane is disabled
        Args:
            value: Value to set for the applePayDisabled property.
        """
        self._apple_pay_disabled = value
    
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new DepEnrollmentProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.depEnrollmentProfile"
        # Indicates if Apple id setup pane is disabled
        self._apple_id_disabled: Optional[bool] = None
        # Indicates if Apple pay setup pane is disabled
        self._apple_pay_disabled: Optional[bool] = None
        # Indicates if the device will need to wait for configured confirmation
        self._await_device_configured_confirmation: Optional[bool] = None
        # Indicates if diagnostics setup pane is disabled
        self._diagnostics_disabled: Optional[bool] = None
        # This indicates whether the device is to be enrolled in a mode which enables multi user scenarios. Only applicable in shared iPads.
        self._enable_shared_i_pad: Optional[bool] = None
        # Indicates if this is the default profile
        self._is_default: Optional[bool] = None
        # Indicates if the profile is mandatory
        self._is_mandatory: Optional[bool] = None
        # The iTunesPairingMode property
        self._i_tunes_pairing_mode: Optional[i_tunes_pairing_mode.ITunesPairingMode] = None
        # Indicates if Location service setup pane is disabled
        self._location_disabled: Optional[bool] = None
        # Indicates if Mac OS file vault is disabled
        self._mac_o_s_file_vault_disabled: Optional[bool] = None
        # Indicates if Mac OS registration is disabled
        self._mac_o_s_registration_disabled: Optional[bool] = None
        # Management certificates for Apple Configurator
        self._management_certificates: Optional[List[management_certificate_with_thumbprint.ManagementCertificateWithThumbprint]] = None
        # Indicates if Passcode setup pane is disabled
        self._pass_code_disabled: Optional[bool] = None
        # Indicates if the profile removal option is disabled
        self._profile_removal_disabled: Optional[bool] = None
        # Indicates if Restore setup pane is blocked
        self._restore_blocked: Optional[bool] = None
        # Indicates if Restore from Android is disabled
        self._restore_from_android_disabled: Optional[bool] = None
        # This specifies the maximum number of users that can use a shared iPad. Only applicable in shared iPad mode.
        self._shared_i_pad_maximum_user_count: Optional[int] = None
        # Indicates if siri setup pane is disabled
        self._siri_disabled: Optional[bool] = None
        # Supervised mode, True to enable, false otherwise. See https://learn.microsoft.com/intune/deploy-use/enroll-devices-in-microsoft-intune for additional information.
        self._supervised_mode_enabled: Optional[bool] = None
        # Support department information
        self._support_department: Optional[str] = None
        # Support phone number
        self._support_phone_number: Optional[str] = None
        # Indicates if 'Terms and Conditions' setup pane is disabled
        self._terms_and_conditions_disabled: Optional[bool] = None
        # Indicates if touch id setup pane is disabled
        self._touch_id_disabled: Optional[bool] = None
        # Indicates if zoom setup pane is disabled
        self._zoom_disabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DepEnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DepEnrollmentProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DepEnrollmentProfile()
    
    @property
    def diagnostics_disabled(self,) -> Optional[bool]:
        """
        Gets the diagnosticsDisabled property value. Indicates if diagnostics setup pane is disabled
        Returns: Optional[bool]
        """
        return self._diagnostics_disabled
    
    @diagnostics_disabled.setter
    def diagnostics_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the diagnosticsDisabled property value. Indicates if diagnostics setup pane is disabled
        Args:
            value: Value to set for the diagnosticsDisabled property.
        """
        self._diagnostics_disabled = value
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "apple_id_disabled": lambda n : setattr(self, 'apple_id_disabled', n.get_bool_value()),
            "apple_pay_disabled": lambda n : setattr(self, 'apple_pay_disabled', n.get_bool_value()),
            "await_device_configured_confirmation": lambda n : setattr(self, 'await_device_configured_confirmation', n.get_bool_value()),
            "diagnostics_disabled": lambda n : setattr(self, 'diagnostics_disabled', n.get_bool_value()),
            "enable_shared_i_pad": lambda n : setattr(self, 'enable_shared_i_pad', n.get_bool_value()),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "is_mandatory": lambda n : setattr(self, 'is_mandatory', n.get_bool_value()),
            "i_tunes_pairing_mode": lambda n : setattr(self, 'i_tunes_pairing_mode', n.get_enum_value(i_tunes_pairing_mode.ITunesPairingMode)),
            "location_disabled": lambda n : setattr(self, 'location_disabled', n.get_bool_value()),
            "mac_o_s_file_vault_disabled": lambda n : setattr(self, 'mac_o_s_file_vault_disabled', n.get_bool_value()),
            "mac_o_s_registration_disabled": lambda n : setattr(self, 'mac_o_s_registration_disabled', n.get_bool_value()),
            "management_certificates": lambda n : setattr(self, 'management_certificates', n.get_collection_of_object_values(management_certificate_with_thumbprint.ManagementCertificateWithThumbprint)),
            "pass_code_disabled": lambda n : setattr(self, 'pass_code_disabled', n.get_bool_value()),
            "profile_removal_disabled": lambda n : setattr(self, 'profile_removal_disabled', n.get_bool_value()),
            "restore_blocked": lambda n : setattr(self, 'restore_blocked', n.get_bool_value()),
            "restore_from_android_disabled": lambda n : setattr(self, 'restore_from_android_disabled', n.get_bool_value()),
            "shared_i_pad_maximum_user_count": lambda n : setattr(self, 'shared_i_pad_maximum_user_count', n.get_int_value()),
            "siri_disabled": lambda n : setattr(self, 'siri_disabled', n.get_bool_value()),
            "supervised_mode_enabled": lambda n : setattr(self, 'supervised_mode_enabled', n.get_bool_value()),
            "support_department": lambda n : setattr(self, 'support_department', n.get_str_value()),
            "support_phone_number": lambda n : setattr(self, 'support_phone_number', n.get_str_value()),
            "terms_and_conditions_disabled": lambda n : setattr(self, 'terms_and_conditions_disabled', n.get_bool_value()),
            "touch_id_disabled": lambda n : setattr(self, 'touch_id_disabled', n.get_bool_value()),
            "zoom_disabled": lambda n : setattr(self, 'zoom_disabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. Indicates if this is the default profile
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. Indicates if this is the default profile
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def is_mandatory(self,) -> Optional[bool]:
        """
        Gets the isMandatory property value. Indicates if the profile is mandatory
        Returns: Optional[bool]
        """
        return self._is_mandatory
    
    @is_mandatory.setter
    def is_mandatory(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMandatory property value. Indicates if the profile is mandatory
        Args:
            value: Value to set for the isMandatory property.
        """
        self._is_mandatory = value
    
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
    def location_disabled(self,) -> Optional[bool]:
        """
        Gets the locationDisabled property value. Indicates if Location service setup pane is disabled
        Returns: Optional[bool]
        """
        return self._location_disabled
    
    @location_disabled.setter
    def location_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the locationDisabled property value. Indicates if Location service setup pane is disabled
        Args:
            value: Value to set for the locationDisabled property.
        """
        self._location_disabled = value
    
    @property
    def mac_o_s_file_vault_disabled(self,) -> Optional[bool]:
        """
        Gets the macOSFileVaultDisabled property value. Indicates if Mac OS file vault is disabled
        Returns: Optional[bool]
        """
        return self._mac_o_s_file_vault_disabled
    
    @mac_o_s_file_vault_disabled.setter
    def mac_o_s_file_vault_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the macOSFileVaultDisabled property value. Indicates if Mac OS file vault is disabled
        Args:
            value: Value to set for the macOSFileVaultDisabled property.
        """
        self._mac_o_s_file_vault_disabled = value
    
    @property
    def mac_o_s_registration_disabled(self,) -> Optional[bool]:
        """
        Gets the macOSRegistrationDisabled property value. Indicates if Mac OS registration is disabled
        Returns: Optional[bool]
        """
        return self._mac_o_s_registration_disabled
    
    @mac_o_s_registration_disabled.setter
    def mac_o_s_registration_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the macOSRegistrationDisabled property value. Indicates if Mac OS registration is disabled
        Args:
            value: Value to set for the macOSRegistrationDisabled property.
        """
        self._mac_o_s_registration_disabled = value
    
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
    def profile_removal_disabled(self,) -> Optional[bool]:
        """
        Gets the profileRemovalDisabled property value. Indicates if the profile removal option is disabled
        Returns: Optional[bool]
        """
        return self._profile_removal_disabled
    
    @profile_removal_disabled.setter
    def profile_removal_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the profileRemovalDisabled property value. Indicates if the profile removal option is disabled
        Args:
            value: Value to set for the profileRemovalDisabled property.
        """
        self._profile_removal_disabled = value
    
    @property
    def restore_blocked(self,) -> Optional[bool]:
        """
        Gets the restoreBlocked property value. Indicates if Restore setup pane is blocked
        Returns: Optional[bool]
        """
        return self._restore_blocked
    
    @restore_blocked.setter
    def restore_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the restoreBlocked property value. Indicates if Restore setup pane is blocked
        Args:
            value: Value to set for the restoreBlocked property.
        """
        self._restore_blocked = value
    
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
        writer.write_bool_value("appleIdDisabled", self.apple_id_disabled)
        writer.write_bool_value("applePayDisabled", self.apple_pay_disabled)
        writer.write_bool_value("awaitDeviceConfiguredConfirmation", self.await_device_configured_confirmation)
        writer.write_bool_value("diagnosticsDisabled", self.diagnostics_disabled)
        writer.write_bool_value("enableSharedIPad", self.enable_shared_i_pad)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isMandatory", self.is_mandatory)
        writer.write_enum_value("iTunesPairingMode", self.i_tunes_pairing_mode)
        writer.write_bool_value("locationDisabled", self.location_disabled)
        writer.write_bool_value("macOSFileVaultDisabled", self.mac_o_s_file_vault_disabled)
        writer.write_bool_value("macOSRegistrationDisabled", self.mac_o_s_registration_disabled)
        writer.write_collection_of_object_values("managementCertificates", self.management_certificates)
        writer.write_bool_value("passCodeDisabled", self.pass_code_disabled)
        writer.write_bool_value("profileRemovalDisabled", self.profile_removal_disabled)
        writer.write_bool_value("restoreBlocked", self.restore_blocked)
        writer.write_bool_value("restoreFromAndroidDisabled", self.restore_from_android_disabled)
        writer.write_int_value("sharedIPadMaximumUserCount", self.shared_i_pad_maximum_user_count)
        writer.write_bool_value("siriDisabled", self.siri_disabled)
        writer.write_bool_value("supervisedModeEnabled", self.supervised_mode_enabled)
        writer.write_str_value("supportDepartment", self.support_department)
        writer.write_str_value("supportPhoneNumber", self.support_phone_number)
        writer.write_bool_value("termsAndConditionsDisabled", self.terms_and_conditions_disabled)
        writer.write_bool_value("touchIdDisabled", self.touch_id_disabled)
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
    def siri_disabled(self,) -> Optional[bool]:
        """
        Gets the siriDisabled property value. Indicates if siri setup pane is disabled
        Returns: Optional[bool]
        """
        return self._siri_disabled
    
    @siri_disabled.setter
    def siri_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the siriDisabled property value. Indicates if siri setup pane is disabled
        Args:
            value: Value to set for the siriDisabled property.
        """
        self._siri_disabled = value
    
    @property
    def supervised_mode_enabled(self,) -> Optional[bool]:
        """
        Gets the supervisedModeEnabled property value. Supervised mode, True to enable, false otherwise. See https://learn.microsoft.com/intune/deploy-use/enroll-devices-in-microsoft-intune for additional information.
        Returns: Optional[bool]
        """
        return self._supervised_mode_enabled
    
    @supervised_mode_enabled.setter
    def supervised_mode_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the supervisedModeEnabled property value. Supervised mode, True to enable, false otherwise. See https://learn.microsoft.com/intune/deploy-use/enroll-devices-in-microsoft-intune for additional information.
        Args:
            value: Value to set for the supervisedModeEnabled property.
        """
        self._supervised_mode_enabled = value
    
    @property
    def support_department(self,) -> Optional[str]:
        """
        Gets the supportDepartment property value. Support department information
        Returns: Optional[str]
        """
        return self._support_department
    
    @support_department.setter
    def support_department(self,value: Optional[str] = None) -> None:
        """
        Sets the supportDepartment property value. Support department information
        Args:
            value: Value to set for the supportDepartment property.
        """
        self._support_department = value
    
    @property
    def support_phone_number(self,) -> Optional[str]:
        """
        Gets the supportPhoneNumber property value. Support phone number
        Returns: Optional[str]
        """
        return self._support_phone_number
    
    @support_phone_number.setter
    def support_phone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the supportPhoneNumber property value. Support phone number
        Args:
            value: Value to set for the supportPhoneNumber property.
        """
        self._support_phone_number = value
    
    @property
    def terms_and_conditions_disabled(self,) -> Optional[bool]:
        """
        Gets the termsAndConditionsDisabled property value. Indicates if 'Terms and Conditions' setup pane is disabled
        Returns: Optional[bool]
        """
        return self._terms_and_conditions_disabled
    
    @terms_and_conditions_disabled.setter
    def terms_and_conditions_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the termsAndConditionsDisabled property value. Indicates if 'Terms and Conditions' setup pane is disabled
        Args:
            value: Value to set for the termsAndConditionsDisabled property.
        """
        self._terms_and_conditions_disabled = value
    
    @property
    def touch_id_disabled(self,) -> Optional[bool]:
        """
        Gets the touchIdDisabled property value. Indicates if touch id setup pane is disabled
        Returns: Optional[bool]
        """
        return self._touch_id_disabled
    
    @touch_id_disabled.setter
    def touch_id_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the touchIdDisabled property value. Indicates if touch id setup pane is disabled
        Args:
            value: Value to set for the touchIdDisabled property.
        """
        self._touch_id_disabled = value
    
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
    

