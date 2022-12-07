from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_compliance_policy = lazy_import('msgraph.generated.models.device_compliance_policy')
device_compliance_policy_script = lazy_import('msgraph.generated.models.device_compliance_policy_script')
device_threat_protection_level = lazy_import('msgraph.generated.models.device_threat_protection_level')
operating_system_version_range = lazy_import('msgraph.generated.models.operating_system_version_range')
required_password_type = lazy_import('msgraph.generated.models.required_password_type')

class Windows10CompliancePolicy(device_compliance_policy.DeviceCompliancePolicy):
    @property
    def active_firewall_required(self,) -> Optional[bool]:
        """
        Gets the activeFirewallRequired property value. Require active firewall on Windows devices.
        Returns: Optional[bool]
        """
        return self._active_firewall_required
    
    @active_firewall_required.setter
    def active_firewall_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the activeFirewallRequired property value. Require active firewall on Windows devices.
        Args:
            value: Value to set for the activeFirewallRequired property.
        """
        self._active_firewall_required = value
    
    @property
    def anti_spyware_required(self,) -> Optional[bool]:
        """
        Gets the antiSpywareRequired property value. Require any AntiSpyware solution registered with Windows Decurity Center to be on and monitoring (e.g. Symantec, Windows Defender).
        Returns: Optional[bool]
        """
        return self._anti_spyware_required
    
    @anti_spyware_required.setter
    def anti_spyware_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the antiSpywareRequired property value. Require any AntiSpyware solution registered with Windows Decurity Center to be on and monitoring (e.g. Symantec, Windows Defender).
        Args:
            value: Value to set for the antiSpywareRequired property.
        """
        self._anti_spyware_required = value
    
    @property
    def antivirus_required(self,) -> Optional[bool]:
        """
        Gets the antivirusRequired property value. Require any Antivirus solution registered with Windows Decurity Center to be on and monitoring (e.g. Symantec, Windows Defender).
        Returns: Optional[bool]
        """
        return self._antivirus_required
    
    @antivirus_required.setter
    def antivirus_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the antivirusRequired property value. Require any Antivirus solution registered with Windows Decurity Center to be on and monitoring (e.g. Symantec, Windows Defender).
        Args:
            value: Value to set for the antivirusRequired property.
        """
        self._antivirus_required = value
    
    @property
    def bit_locker_enabled(self,) -> Optional[bool]:
        """
        Gets the bitLockerEnabled property value. Require devices to be reported healthy by Windows Device Health Attestation - bit locker is enabled
        Returns: Optional[bool]
        """
        return self._bit_locker_enabled
    
    @bit_locker_enabled.setter
    def bit_locker_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the bitLockerEnabled property value. Require devices to be reported healthy by Windows Device Health Attestation - bit locker is enabled
        Args:
            value: Value to set for the bitLockerEnabled property.
        """
        self._bit_locker_enabled = value
    
    @property
    def code_integrity_enabled(self,) -> Optional[bool]:
        """
        Gets the codeIntegrityEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation.
        Returns: Optional[bool]
        """
        return self._code_integrity_enabled
    
    @code_integrity_enabled.setter
    def code_integrity_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the codeIntegrityEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation.
        Args:
            value: Value to set for the codeIntegrityEnabled property.
        """
        self._code_integrity_enabled = value
    
    @property
    def configuration_manager_compliance_required(self,) -> Optional[bool]:
        """
        Gets the configurationManagerComplianceRequired property value. Require to consider SCCM Compliance state into consideration for Intune Compliance State.
        Returns: Optional[bool]
        """
        return self._configuration_manager_compliance_required
    
    @configuration_manager_compliance_required.setter
    def configuration_manager_compliance_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the configurationManagerComplianceRequired property value. Require to consider SCCM Compliance state into consideration for Intune Compliance State.
        Args:
            value: Value to set for the configurationManagerComplianceRequired property.
        """
        self._configuration_manager_compliance_required = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10CompliancePolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10CompliancePolicy"
        # Require active firewall on Windows devices.
        self._active_firewall_required: Optional[bool] = None
        # Require any AntiSpyware solution registered with Windows Decurity Center to be on and monitoring (e.g. Symantec, Windows Defender).
        self._anti_spyware_required: Optional[bool] = None
        # Require any Antivirus solution registered with Windows Decurity Center to be on and monitoring (e.g. Symantec, Windows Defender).
        self._antivirus_required: Optional[bool] = None
        # Require devices to be reported healthy by Windows Device Health Attestation - bit locker is enabled
        self._bit_locker_enabled: Optional[bool] = None
        # Require devices to be reported as healthy by Windows Device Health Attestation.
        self._code_integrity_enabled: Optional[bool] = None
        # Require to consider SCCM Compliance state into consideration for Intune Compliance State.
        self._configuration_manager_compliance_required: Optional[bool] = None
        # Require Windows Defender Antimalware on Windows devices.
        self._defender_enabled: Optional[bool] = None
        # Require Windows Defender Antimalware minimum version on Windows devices.
        self._defender_version: Optional[str] = None
        # Not yet documented
        self._device_compliance_policy_script: Optional[device_compliance_policy_script.DeviceCompliancePolicyScript] = None
        # Require that devices have enabled device threat protection.
        self._device_threat_protection_enabled: Optional[bool] = None
        # Device threat protection levels for the Device Threat Protection API.
        self._device_threat_protection_required_security_level: Optional[device_threat_protection_level.DeviceThreatProtectionLevel] = None
        # Require devices to be reported as healthy by Windows Device Health Attestation - early launch antimalware driver is enabled.
        self._early_launch_anti_malware_driver_enabled: Optional[bool] = None
        # Maximum Windows Phone version.
        self._mobile_os_maximum_version: Optional[str] = None
        # Minimum Windows Phone version.
        self._mobile_os_minimum_version: Optional[str] = None
        # Maximum Windows 10 version.
        self._os_maximum_version: Optional[str] = None
        # Minimum Windows 10 version.
        self._os_minimum_version: Optional[str] = None
        # Indicates whether or not to block simple password.
        self._password_block_simple: Optional[bool] = None
        # The password expiration in days.
        self._password_expiration_days: Optional[int] = None
        # The number of character sets required in the password.
        self._password_minimum_character_set_count: Optional[int] = None
        # The minimum password length.
        self._password_minimum_length: Optional[int] = None
        # Minutes of inactivity before a password is required.
        self._password_minutes_of_inactivity_before_lock: Optional[int] = None
        # The number of previous passwords to prevent re-use of.
        self._password_previous_password_block_count: Optional[int] = None
        # Require a password to unlock Windows device.
        self._password_required: Optional[bool] = None
        # Require a password to unlock an idle device.
        self._password_required_to_unlock_from_idle: Optional[bool] = None
        # Possible values of required passwords.
        self._password_required_type: Optional[required_password_type.RequiredPasswordType] = None
        # Require devices to be reported as healthy by Windows Device Health Attestation.
        self._require_healthy_device_report: Optional[bool] = None
        # Require Windows Defender Antimalware Real-Time Protection on Windows devices.
        self._rtp_enabled: Optional[bool] = None
        # Require devices to be reported as healthy by Windows Device Health Attestation - secure boot is enabled.
        self._secure_boot_enabled: Optional[bool] = None
        # Require Windows Defender Antimalware Signature to be up to date on Windows devices.
        self._signature_out_of_date: Optional[bool] = None
        # Require encryption on windows devices.
        self._storage_require_encryption: Optional[bool] = None
        # Require Trusted Platform Module(TPM) to be present.
        self._tpm_required: Optional[bool] = None
        # The valid operating system build ranges on Windows devices. This collection can contain a maximum of 10000 elements.
        self._valid_operating_system_build_ranges: Optional[List[operating_system_version_range.OperatingSystemVersionRange]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10CompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10CompliancePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10CompliancePolicy()
    
    @property
    def defender_enabled(self,) -> Optional[bool]:
        """
        Gets the defenderEnabled property value. Require Windows Defender Antimalware on Windows devices.
        Returns: Optional[bool]
        """
        return self._defender_enabled
    
    @defender_enabled.setter
    def defender_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderEnabled property value. Require Windows Defender Antimalware on Windows devices.
        Args:
            value: Value to set for the defenderEnabled property.
        """
        self._defender_enabled = value
    
    @property
    def defender_version(self,) -> Optional[str]:
        """
        Gets the defenderVersion property value. Require Windows Defender Antimalware minimum version on Windows devices.
        Returns: Optional[str]
        """
        return self._defender_version
    
    @defender_version.setter
    def defender_version(self,value: Optional[str] = None) -> None:
        """
        Sets the defenderVersion property value. Require Windows Defender Antimalware minimum version on Windows devices.
        Args:
            value: Value to set for the defenderVersion property.
        """
        self._defender_version = value
    
    @property
    def device_compliance_policy_script(self,) -> Optional[device_compliance_policy_script.DeviceCompliancePolicyScript]:
        """
        Gets the deviceCompliancePolicyScript property value. Not yet documented
        Returns: Optional[device_compliance_policy_script.DeviceCompliancePolicyScript]
        """
        return self._device_compliance_policy_script
    
    @device_compliance_policy_script.setter
    def device_compliance_policy_script(self,value: Optional[device_compliance_policy_script.DeviceCompliancePolicyScript] = None) -> None:
        """
        Sets the deviceCompliancePolicyScript property value. Not yet documented
        Args:
            value: Value to set for the deviceCompliancePolicyScript property.
        """
        self._device_compliance_policy_script = value
    
    @property
    def device_threat_protection_enabled(self,) -> Optional[bool]:
        """
        Gets the deviceThreatProtectionEnabled property value. Require that devices have enabled device threat protection.
        Returns: Optional[bool]
        """
        return self._device_threat_protection_enabled
    
    @device_threat_protection_enabled.setter
    def device_threat_protection_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceThreatProtectionEnabled property value. Require that devices have enabled device threat protection.
        Args:
            value: Value to set for the deviceThreatProtectionEnabled property.
        """
        self._device_threat_protection_enabled = value
    
    @property
    def device_threat_protection_required_security_level(self,) -> Optional[device_threat_protection_level.DeviceThreatProtectionLevel]:
        """
        Gets the deviceThreatProtectionRequiredSecurityLevel property value. Device threat protection levels for the Device Threat Protection API.
        Returns: Optional[device_threat_protection_level.DeviceThreatProtectionLevel]
        """
        return self._device_threat_protection_required_security_level
    
    @device_threat_protection_required_security_level.setter
    def device_threat_protection_required_security_level(self,value: Optional[device_threat_protection_level.DeviceThreatProtectionLevel] = None) -> None:
        """
        Sets the deviceThreatProtectionRequiredSecurityLevel property value. Device threat protection levels for the Device Threat Protection API.
        Args:
            value: Value to set for the deviceThreatProtectionRequiredSecurityLevel property.
        """
        self._device_threat_protection_required_security_level = value
    
    @property
    def early_launch_anti_malware_driver_enabled(self,) -> Optional[bool]:
        """
        Gets the earlyLaunchAntiMalwareDriverEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation - early launch antimalware driver is enabled.
        Returns: Optional[bool]
        """
        return self._early_launch_anti_malware_driver_enabled
    
    @early_launch_anti_malware_driver_enabled.setter
    def early_launch_anti_malware_driver_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the earlyLaunchAntiMalwareDriverEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation - early launch antimalware driver is enabled.
        Args:
            value: Value to set for the earlyLaunchAntiMalwareDriverEnabled property.
        """
        self._early_launch_anti_malware_driver_enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_firewall_required": lambda n : setattr(self, 'active_firewall_required', n.get_bool_value()),
            "anti_spyware_required": lambda n : setattr(self, 'anti_spyware_required', n.get_bool_value()),
            "antivirus_required": lambda n : setattr(self, 'antivirus_required', n.get_bool_value()),
            "bit_locker_enabled": lambda n : setattr(self, 'bit_locker_enabled', n.get_bool_value()),
            "code_integrity_enabled": lambda n : setattr(self, 'code_integrity_enabled', n.get_bool_value()),
            "configuration_manager_compliance_required": lambda n : setattr(self, 'configuration_manager_compliance_required', n.get_bool_value()),
            "defender_enabled": lambda n : setattr(self, 'defender_enabled', n.get_bool_value()),
            "defender_version": lambda n : setattr(self, 'defender_version', n.get_str_value()),
            "device_compliance_policy_script": lambda n : setattr(self, 'device_compliance_policy_script', n.get_object_value(device_compliance_policy_script.DeviceCompliancePolicyScript)),
            "device_threat_protection_enabled": lambda n : setattr(self, 'device_threat_protection_enabled', n.get_bool_value()),
            "device_threat_protection_required_security_level": lambda n : setattr(self, 'device_threat_protection_required_security_level', n.get_enum_value(device_threat_protection_level.DeviceThreatProtectionLevel)),
            "early_launch_anti_malware_driver_enabled": lambda n : setattr(self, 'early_launch_anti_malware_driver_enabled', n.get_bool_value()),
            "mobile_os_maximum_version": lambda n : setattr(self, 'mobile_os_maximum_version', n.get_str_value()),
            "mobile_os_minimum_version": lambda n : setattr(self, 'mobile_os_minimum_version', n.get_str_value()),
            "os_maximum_version": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "os_minimum_version": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "password_block_simple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "password_expiration_days": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "password_minimum_character_set_count": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "password_minimum_length": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "password_minutes_of_inactivity_before_lock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "password_previous_password_block_count": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "password_required": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "password_required_to_unlock_from_idle": lambda n : setattr(self, 'password_required_to_unlock_from_idle', n.get_bool_value()),
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(required_password_type.RequiredPasswordType)),
            "require_healthy_device_report": lambda n : setattr(self, 'require_healthy_device_report', n.get_bool_value()),
            "rtp_enabled": lambda n : setattr(self, 'rtp_enabled', n.get_bool_value()),
            "secure_boot_enabled": lambda n : setattr(self, 'secure_boot_enabled', n.get_bool_value()),
            "signature_out_of_date": lambda n : setattr(self, 'signature_out_of_date', n.get_bool_value()),
            "storage_require_encryption": lambda n : setattr(self, 'storage_require_encryption', n.get_bool_value()),
            "tpm_required": lambda n : setattr(self, 'tpm_required', n.get_bool_value()),
            "valid_operating_system_build_ranges": lambda n : setattr(self, 'valid_operating_system_build_ranges', n.get_collection_of_object_values(operating_system_version_range.OperatingSystemVersionRange)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def mobile_os_maximum_version(self,) -> Optional[str]:
        """
        Gets the mobileOsMaximumVersion property value. Maximum Windows Phone version.
        Returns: Optional[str]
        """
        return self._mobile_os_maximum_version
    
    @mobile_os_maximum_version.setter
    def mobile_os_maximum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the mobileOsMaximumVersion property value. Maximum Windows Phone version.
        Args:
            value: Value to set for the mobileOsMaximumVersion property.
        """
        self._mobile_os_maximum_version = value
    
    @property
    def mobile_os_minimum_version(self,) -> Optional[str]:
        """
        Gets the mobileOsMinimumVersion property value. Minimum Windows Phone version.
        Returns: Optional[str]
        """
        return self._mobile_os_minimum_version
    
    @mobile_os_minimum_version.setter
    def mobile_os_minimum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the mobileOsMinimumVersion property value. Minimum Windows Phone version.
        Args:
            value: Value to set for the mobileOsMinimumVersion property.
        """
        self._mobile_os_minimum_version = value
    
    @property
    def os_maximum_version(self,) -> Optional[str]:
        """
        Gets the osMaximumVersion property value. Maximum Windows 10 version.
        Returns: Optional[str]
        """
        return self._os_maximum_version
    
    @os_maximum_version.setter
    def os_maximum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMaximumVersion property value. Maximum Windows 10 version.
        Args:
            value: Value to set for the osMaximumVersion property.
        """
        self._os_maximum_version = value
    
    @property
    def os_minimum_version(self,) -> Optional[str]:
        """
        Gets the osMinimumVersion property value. Minimum Windows 10 version.
        Returns: Optional[str]
        """
        return self._os_minimum_version
    
    @os_minimum_version.setter
    def os_minimum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMinimumVersion property value. Minimum Windows 10 version.
        Args:
            value: Value to set for the osMinimumVersion property.
        """
        self._os_minimum_version = value
    
    @property
    def password_block_simple(self,) -> Optional[bool]:
        """
        Gets the passwordBlockSimple property value. Indicates whether or not to block simple password.
        Returns: Optional[bool]
        """
        return self._password_block_simple
    
    @password_block_simple.setter
    def password_block_simple(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockSimple property value. Indicates whether or not to block simple password.
        Args:
            value: Value to set for the passwordBlockSimple property.
        """
        self._password_block_simple = value
    
    @property
    def password_expiration_days(self,) -> Optional[int]:
        """
        Gets the passwordExpirationDays property value. The password expiration in days.
        Returns: Optional[int]
        """
        return self._password_expiration_days
    
    @password_expiration_days.setter
    def password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordExpirationDays property value. The password expiration in days.
        Args:
            value: Value to set for the passwordExpirationDays property.
        """
        self._password_expiration_days = value
    
    @property
    def password_minimum_character_set_count(self,) -> Optional[int]:
        """
        Gets the passwordMinimumCharacterSetCount property value. The number of character sets required in the password.
        Returns: Optional[int]
        """
        return self._password_minimum_character_set_count
    
    @password_minimum_character_set_count.setter
    def password_minimum_character_set_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumCharacterSetCount property value. The number of character sets required in the password.
        Args:
            value: Value to set for the passwordMinimumCharacterSetCount property.
        """
        self._password_minimum_character_set_count = value
    
    @property
    def password_minimum_length(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLength property value. The minimum password length.
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. The minimum password length.
        Args:
            value: Value to set for the passwordMinimumLength property.
        """
        self._password_minimum_length = value
    
    @property
    def password_minutes_of_inactivity_before_lock(self,) -> Optional[int]:
        """
        Gets the passwordMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a password is required.
        Returns: Optional[int]
        """
        return self._password_minutes_of_inactivity_before_lock
    
    @password_minutes_of_inactivity_before_lock.setter
    def password_minutes_of_inactivity_before_lock(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a password is required.
        Args:
            value: Value to set for the passwordMinutesOfInactivityBeforeLock property.
        """
        self._password_minutes_of_inactivity_before_lock = value
    
    @property
    def password_previous_password_block_count(self,) -> Optional[int]:
        """
        Gets the passwordPreviousPasswordBlockCount property value. The number of previous passwords to prevent re-use of.
        Returns: Optional[int]
        """
        return self._password_previous_password_block_count
    
    @password_previous_password_block_count.setter
    def password_previous_password_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordPreviousPasswordBlockCount property value. The number of previous passwords to prevent re-use of.
        Args:
            value: Value to set for the passwordPreviousPasswordBlockCount property.
        """
        self._password_previous_password_block_count = value
    
    @property
    def password_required(self,) -> Optional[bool]:
        """
        Gets the passwordRequired property value. Require a password to unlock Windows device.
        Returns: Optional[bool]
        """
        return self._password_required
    
    @password_required.setter
    def password_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRequired property value. Require a password to unlock Windows device.
        Args:
            value: Value to set for the passwordRequired property.
        """
        self._password_required = value
    
    @property
    def password_required_to_unlock_from_idle(self,) -> Optional[bool]:
        """
        Gets the passwordRequiredToUnlockFromIdle property value. Require a password to unlock an idle device.
        Returns: Optional[bool]
        """
        return self._password_required_to_unlock_from_idle
    
    @password_required_to_unlock_from_idle.setter
    def password_required_to_unlock_from_idle(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRequiredToUnlockFromIdle property value. Require a password to unlock an idle device.
        Args:
            value: Value to set for the passwordRequiredToUnlockFromIdle property.
        """
        self._password_required_to_unlock_from_idle = value
    
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
            value: Value to set for the passwordRequiredType property.
        """
        self._password_required_type = value
    
    @property
    def require_healthy_device_report(self,) -> Optional[bool]:
        """
        Gets the requireHealthyDeviceReport property value. Require devices to be reported as healthy by Windows Device Health Attestation.
        Returns: Optional[bool]
        """
        return self._require_healthy_device_report
    
    @require_healthy_device_report.setter
    def require_healthy_device_report(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireHealthyDeviceReport property value. Require devices to be reported as healthy by Windows Device Health Attestation.
        Args:
            value: Value to set for the requireHealthyDeviceReport property.
        """
        self._require_healthy_device_report = value
    
    @property
    def rtp_enabled(self,) -> Optional[bool]:
        """
        Gets the rtpEnabled property value. Require Windows Defender Antimalware Real-Time Protection on Windows devices.
        Returns: Optional[bool]
        """
        return self._rtp_enabled
    
    @rtp_enabled.setter
    def rtp_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the rtpEnabled property value. Require Windows Defender Antimalware Real-Time Protection on Windows devices.
        Args:
            value: Value to set for the rtpEnabled property.
        """
        self._rtp_enabled = value
    
    @property
    def secure_boot_enabled(self,) -> Optional[bool]:
        """
        Gets the secureBootEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation - secure boot is enabled.
        Returns: Optional[bool]
        """
        return self._secure_boot_enabled
    
    @secure_boot_enabled.setter
    def secure_boot_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the secureBootEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation - secure boot is enabled.
        Args:
            value: Value to set for the secureBootEnabled property.
        """
        self._secure_boot_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("activeFirewallRequired", self.active_firewall_required)
        writer.write_bool_value("antiSpywareRequired", self.anti_spyware_required)
        writer.write_bool_value("antivirusRequired", self.antivirus_required)
        writer.write_bool_value("bitLockerEnabled", self.bit_locker_enabled)
        writer.write_bool_value("codeIntegrityEnabled", self.code_integrity_enabled)
        writer.write_bool_value("configurationManagerComplianceRequired", self.configuration_manager_compliance_required)
        writer.write_bool_value("defenderEnabled", self.defender_enabled)
        writer.write_str_value("defenderVersion", self.defender_version)
        writer.write_object_value("deviceCompliancePolicyScript", self.device_compliance_policy_script)
        writer.write_bool_value("deviceThreatProtectionEnabled", self.device_threat_protection_enabled)
        writer.write_enum_value("deviceThreatProtectionRequiredSecurityLevel", self.device_threat_protection_required_security_level)
        writer.write_bool_value("earlyLaunchAntiMalwareDriverEnabled", self.early_launch_anti_malware_driver_enabled)
        writer.write_str_value("mobileOsMaximumVersion", self.mobile_os_maximum_version)
        writer.write_str_value("mobileOsMinimumVersion", self.mobile_os_minimum_version)
        writer.write_str_value("osMaximumVersion", self.os_maximum_version)
        writer.write_str_value("osMinimumVersion", self.os_minimum_version)
        writer.write_bool_value("passwordBlockSimple", self.password_block_simple)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumCharacterSetCount", self.password_minimum_character_set_count)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeLock", self.password_minutes_of_inactivity_before_lock)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_bool_value("passwordRequiredToUnlockFromIdle", self.password_required_to_unlock_from_idle)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_bool_value("requireHealthyDeviceReport", self.require_healthy_device_report)
        writer.write_bool_value("rtpEnabled", self.rtp_enabled)
        writer.write_bool_value("secureBootEnabled", self.secure_boot_enabled)
        writer.write_bool_value("signatureOutOfDate", self.signature_out_of_date)
        writer.write_bool_value("storageRequireEncryption", self.storage_require_encryption)
        writer.write_bool_value("tpmRequired", self.tpm_required)
        writer.write_collection_of_object_values("validOperatingSystemBuildRanges", self.valid_operating_system_build_ranges)
    
    @property
    def signature_out_of_date(self,) -> Optional[bool]:
        """
        Gets the signatureOutOfDate property value. Require Windows Defender Antimalware Signature to be up to date on Windows devices.
        Returns: Optional[bool]
        """
        return self._signature_out_of_date
    
    @signature_out_of_date.setter
    def signature_out_of_date(self,value: Optional[bool] = None) -> None:
        """
        Sets the signatureOutOfDate property value. Require Windows Defender Antimalware Signature to be up to date on Windows devices.
        Args:
            value: Value to set for the signatureOutOfDate property.
        """
        self._signature_out_of_date = value
    
    @property
    def storage_require_encryption(self,) -> Optional[bool]:
        """
        Gets the storageRequireEncryption property value. Require encryption on windows devices.
        Returns: Optional[bool]
        """
        return self._storage_require_encryption
    
    @storage_require_encryption.setter
    def storage_require_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageRequireEncryption property value. Require encryption on windows devices.
        Args:
            value: Value to set for the storageRequireEncryption property.
        """
        self._storage_require_encryption = value
    
    @property
    def tpm_required(self,) -> Optional[bool]:
        """
        Gets the tpmRequired property value. Require Trusted Platform Module(TPM) to be present.
        Returns: Optional[bool]
        """
        return self._tpm_required
    
    @tpm_required.setter
    def tpm_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the tpmRequired property value. Require Trusted Platform Module(TPM) to be present.
        Args:
            value: Value to set for the tpmRequired property.
        """
        self._tpm_required = value
    
    @property
    def valid_operating_system_build_ranges(self,) -> Optional[List[operating_system_version_range.OperatingSystemVersionRange]]:
        """
        Gets the validOperatingSystemBuildRanges property value. The valid operating system build ranges on Windows devices. This collection can contain a maximum of 10000 elements.
        Returns: Optional[List[operating_system_version_range.OperatingSystemVersionRange]]
        """
        return self._valid_operating_system_build_ranges
    
    @valid_operating_system_build_ranges.setter
    def valid_operating_system_build_ranges(self,value: Optional[List[operating_system_version_range.OperatingSystemVersionRange]] = None) -> None:
        """
        Sets the validOperatingSystemBuildRanges property value. The valid operating system build ranges on Windows devices. This collection can contain a maximum of 10000 elements.
        Args:
            value: Value to set for the validOperatingSystemBuildRanges property.
        """
        self._valid_operating_system_build_ranges = value
    

