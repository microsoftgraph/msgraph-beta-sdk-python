from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

configuration_usage = lazy_import('msgraph.generated.models.configuration_usage')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class WindowsIdentityProtectionConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsIdentityProtectionConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsIdentityProtectionConfiguration"
        # Boolean value used to enable enhanced anti-spoofing for facial feature recognition on Windows Hello face authentication.
        self._enhanced_anti_spoofing_for_facial_features_enabled: Optional[bool] = None
        # Integer value specifies the period (in days) that a PIN can be used before the system requires the user to change it. Valid values are 0 to 730 inclusive. Valid values 0 to 730
        self._pin_expiration_in_days: Optional[int] = None
        # Possible values of the ConfigurationUsage list.
        self._pin_lowercase_characters_usage: Optional[configuration_usage.ConfigurationUsage] = None
        # Integer value that sets the maximum number of characters allowed for the work PIN. Valid values are 4 to 127 inclusive and greater than or equal to the value set for the minimum PIN. Valid values 4 to 127
        self._pin_maximum_length: Optional[int] = None
        # Integer value that sets the minimum number of characters required for the Windows Hello for Business PIN. Valid values are 4 to 127 inclusive and less than or equal to the value set for the maximum PIN. Valid values 4 to 127
        self._pin_minimum_length: Optional[int] = None
        # Controls the ability to prevent users from using past PINs. This must be set between 0 and 50, inclusive, and the current PIN of the user is included in that count. If set to 0, previous PINs are not stored. PIN history is not preserved through a PIN reset. Valid values 0 to 50
        self._pin_previous_block_count: Optional[int] = None
        # Boolean value that enables a user to change their PIN by using the Windows Hello for Business PIN recovery service.
        self._pin_recovery_enabled: Optional[bool] = None
        # Possible values of the ConfigurationUsage list.
        self._pin_special_characters_usage: Optional[configuration_usage.ConfigurationUsage] = None
        # Possible values of the ConfigurationUsage list.
        self._pin_uppercase_characters_usage: Optional[configuration_usage.ConfigurationUsage] = None
        # Controls whether to require a Trusted Platform Module (TPM) for provisioning Windows Hello for Business. A TPM provides an additional security benefit in that data stored on it cannot be used on other devices. If set to False, all devices can provision Windows Hello for Business even if there is not a usable TPM.
        self._security_device_required: Optional[bool] = None
        # Controls the use of biometric gestures, such as face and fingerprint, as an alternative to the Windows Hello for Business PIN.  If set to False, biometric gestures are not allowed. Users must still configure a PIN as a backup in case of failures.
        self._unlock_with_biometrics_enabled: Optional[bool] = None
        # Boolean value that enables Windows Hello for Business to use certificates to authenticate on-premise resources.
        self._use_certificates_for_on_premises_auth_enabled: Optional[bool] = None
        # Boolean value used to enable the Windows Hello security key as a logon credential.
        self._use_security_key_for_signin: Optional[bool] = None
        # Boolean value that blocks Windows Hello for Business as a method for signing into Windows.
        self._windows_hello_for_business_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsIdentityProtectionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsIdentityProtectionConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsIdentityProtectionConfiguration()
    
    @property
    def enhanced_anti_spoofing_for_facial_features_enabled(self,) -> Optional[bool]:
        """
        Gets the enhancedAntiSpoofingForFacialFeaturesEnabled property value. Boolean value used to enable enhanced anti-spoofing for facial feature recognition on Windows Hello face authentication.
        Returns: Optional[bool]
        """
        return self._enhanced_anti_spoofing_for_facial_features_enabled
    
    @enhanced_anti_spoofing_for_facial_features_enabled.setter
    def enhanced_anti_spoofing_for_facial_features_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enhancedAntiSpoofingForFacialFeaturesEnabled property value. Boolean value used to enable enhanced anti-spoofing for facial feature recognition on Windows Hello face authentication.
        Args:
            value: Value to set for the enhancedAntiSpoofingForFacialFeaturesEnabled property.
        """
        self._enhanced_anti_spoofing_for_facial_features_enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enhanced_anti_spoofing_for_facial_features_enabled": lambda n : setattr(self, 'enhanced_anti_spoofing_for_facial_features_enabled', n.get_bool_value()),
            "pin_expiration_in_days": lambda n : setattr(self, 'pin_expiration_in_days', n.get_int_value()),
            "pin_lowercase_characters_usage": lambda n : setattr(self, 'pin_lowercase_characters_usage', n.get_enum_value(configuration_usage.ConfigurationUsage)),
            "pin_maximum_length": lambda n : setattr(self, 'pin_maximum_length', n.get_int_value()),
            "pin_minimum_length": lambda n : setattr(self, 'pin_minimum_length', n.get_int_value()),
            "pin_previous_block_count": lambda n : setattr(self, 'pin_previous_block_count', n.get_int_value()),
            "pin_recovery_enabled": lambda n : setattr(self, 'pin_recovery_enabled', n.get_bool_value()),
            "pin_special_characters_usage": lambda n : setattr(self, 'pin_special_characters_usage', n.get_enum_value(configuration_usage.ConfigurationUsage)),
            "pin_uppercase_characters_usage": lambda n : setattr(self, 'pin_uppercase_characters_usage', n.get_enum_value(configuration_usage.ConfigurationUsage)),
            "security_device_required": lambda n : setattr(self, 'security_device_required', n.get_bool_value()),
            "unlock_with_biometrics_enabled": lambda n : setattr(self, 'unlock_with_biometrics_enabled', n.get_bool_value()),
            "use_certificates_for_on_premises_auth_enabled": lambda n : setattr(self, 'use_certificates_for_on_premises_auth_enabled', n.get_bool_value()),
            "use_security_key_for_signin": lambda n : setattr(self, 'use_security_key_for_signin', n.get_bool_value()),
            "windows_hello_for_business_blocked": lambda n : setattr(self, 'windows_hello_for_business_blocked', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def pin_expiration_in_days(self,) -> Optional[int]:
        """
        Gets the pinExpirationInDays property value. Integer value specifies the period (in days) that a PIN can be used before the system requires the user to change it. Valid values are 0 to 730 inclusive. Valid values 0 to 730
        Returns: Optional[int]
        """
        return self._pin_expiration_in_days
    
    @pin_expiration_in_days.setter
    def pin_expiration_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the pinExpirationInDays property value. Integer value specifies the period (in days) that a PIN can be used before the system requires the user to change it. Valid values are 0 to 730 inclusive. Valid values 0 to 730
        Args:
            value: Value to set for the pinExpirationInDays property.
        """
        self._pin_expiration_in_days = value
    
    @property
    def pin_lowercase_characters_usage(self,) -> Optional[configuration_usage.ConfigurationUsage]:
        """
        Gets the pinLowercaseCharactersUsage property value. Possible values of the ConfigurationUsage list.
        Returns: Optional[configuration_usage.ConfigurationUsage]
        """
        return self._pin_lowercase_characters_usage
    
    @pin_lowercase_characters_usage.setter
    def pin_lowercase_characters_usage(self,value: Optional[configuration_usage.ConfigurationUsage] = None) -> None:
        """
        Sets the pinLowercaseCharactersUsage property value. Possible values of the ConfigurationUsage list.
        Args:
            value: Value to set for the pinLowercaseCharactersUsage property.
        """
        self._pin_lowercase_characters_usage = value
    
    @property
    def pin_maximum_length(self,) -> Optional[int]:
        """
        Gets the pinMaximumLength property value. Integer value that sets the maximum number of characters allowed for the work PIN. Valid values are 4 to 127 inclusive and greater than or equal to the value set for the minimum PIN. Valid values 4 to 127
        Returns: Optional[int]
        """
        return self._pin_maximum_length
    
    @pin_maximum_length.setter
    def pin_maximum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the pinMaximumLength property value. Integer value that sets the maximum number of characters allowed for the work PIN. Valid values are 4 to 127 inclusive and greater than or equal to the value set for the minimum PIN. Valid values 4 to 127
        Args:
            value: Value to set for the pinMaximumLength property.
        """
        self._pin_maximum_length = value
    
    @property
    def pin_minimum_length(self,) -> Optional[int]:
        """
        Gets the pinMinimumLength property value. Integer value that sets the minimum number of characters required for the Windows Hello for Business PIN. Valid values are 4 to 127 inclusive and less than or equal to the value set for the maximum PIN. Valid values 4 to 127
        Returns: Optional[int]
        """
        return self._pin_minimum_length
    
    @pin_minimum_length.setter
    def pin_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the pinMinimumLength property value. Integer value that sets the minimum number of characters required for the Windows Hello for Business PIN. Valid values are 4 to 127 inclusive and less than or equal to the value set for the maximum PIN. Valid values 4 to 127
        Args:
            value: Value to set for the pinMinimumLength property.
        """
        self._pin_minimum_length = value
    
    @property
    def pin_previous_block_count(self,) -> Optional[int]:
        """
        Gets the pinPreviousBlockCount property value. Controls the ability to prevent users from using past PINs. This must be set between 0 and 50, inclusive, and the current PIN of the user is included in that count. If set to 0, previous PINs are not stored. PIN history is not preserved through a PIN reset. Valid values 0 to 50
        Returns: Optional[int]
        """
        return self._pin_previous_block_count
    
    @pin_previous_block_count.setter
    def pin_previous_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the pinPreviousBlockCount property value. Controls the ability to prevent users from using past PINs. This must be set between 0 and 50, inclusive, and the current PIN of the user is included in that count. If set to 0, previous PINs are not stored. PIN history is not preserved through a PIN reset. Valid values 0 to 50
        Args:
            value: Value to set for the pinPreviousBlockCount property.
        """
        self._pin_previous_block_count = value
    
    @property
    def pin_recovery_enabled(self,) -> Optional[bool]:
        """
        Gets the pinRecoveryEnabled property value. Boolean value that enables a user to change their PIN by using the Windows Hello for Business PIN recovery service.
        Returns: Optional[bool]
        """
        return self._pin_recovery_enabled
    
    @pin_recovery_enabled.setter
    def pin_recovery_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the pinRecoveryEnabled property value. Boolean value that enables a user to change their PIN by using the Windows Hello for Business PIN recovery service.
        Args:
            value: Value to set for the pinRecoveryEnabled property.
        """
        self._pin_recovery_enabled = value
    
    @property
    def pin_special_characters_usage(self,) -> Optional[configuration_usage.ConfigurationUsage]:
        """
        Gets the pinSpecialCharactersUsage property value. Possible values of the ConfigurationUsage list.
        Returns: Optional[configuration_usage.ConfigurationUsage]
        """
        return self._pin_special_characters_usage
    
    @pin_special_characters_usage.setter
    def pin_special_characters_usage(self,value: Optional[configuration_usage.ConfigurationUsage] = None) -> None:
        """
        Sets the pinSpecialCharactersUsage property value. Possible values of the ConfigurationUsage list.
        Args:
            value: Value to set for the pinSpecialCharactersUsage property.
        """
        self._pin_special_characters_usage = value
    
    @property
    def pin_uppercase_characters_usage(self,) -> Optional[configuration_usage.ConfigurationUsage]:
        """
        Gets the pinUppercaseCharactersUsage property value. Possible values of the ConfigurationUsage list.
        Returns: Optional[configuration_usage.ConfigurationUsage]
        """
        return self._pin_uppercase_characters_usage
    
    @pin_uppercase_characters_usage.setter
    def pin_uppercase_characters_usage(self,value: Optional[configuration_usage.ConfigurationUsage] = None) -> None:
        """
        Sets the pinUppercaseCharactersUsage property value. Possible values of the ConfigurationUsage list.
        Args:
            value: Value to set for the pinUppercaseCharactersUsage property.
        """
        self._pin_uppercase_characters_usage = value
    
    @property
    def security_device_required(self,) -> Optional[bool]:
        """
        Gets the securityDeviceRequired property value. Controls whether to require a Trusted Platform Module (TPM) for provisioning Windows Hello for Business. A TPM provides an additional security benefit in that data stored on it cannot be used on other devices. If set to False, all devices can provision Windows Hello for Business even if there is not a usable TPM.
        Returns: Optional[bool]
        """
        return self._security_device_required
    
    @security_device_required.setter
    def security_device_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityDeviceRequired property value. Controls whether to require a Trusted Platform Module (TPM) for provisioning Windows Hello for Business. A TPM provides an additional security benefit in that data stored on it cannot be used on other devices. If set to False, all devices can provision Windows Hello for Business even if there is not a usable TPM.
        Args:
            value: Value to set for the securityDeviceRequired property.
        """
        self._security_device_required = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("enhancedAntiSpoofingForFacialFeaturesEnabled", self.enhanced_anti_spoofing_for_facial_features_enabled)
        writer.write_int_value("pinExpirationInDays", self.pin_expiration_in_days)
        writer.write_enum_value("pinLowercaseCharactersUsage", self.pin_lowercase_characters_usage)
        writer.write_int_value("pinMaximumLength", self.pin_maximum_length)
        writer.write_int_value("pinMinimumLength", self.pin_minimum_length)
        writer.write_int_value("pinPreviousBlockCount", self.pin_previous_block_count)
        writer.write_bool_value("pinRecoveryEnabled", self.pin_recovery_enabled)
        writer.write_enum_value("pinSpecialCharactersUsage", self.pin_special_characters_usage)
        writer.write_enum_value("pinUppercaseCharactersUsage", self.pin_uppercase_characters_usage)
        writer.write_bool_value("securityDeviceRequired", self.security_device_required)
        writer.write_bool_value("unlockWithBiometricsEnabled", self.unlock_with_biometrics_enabled)
        writer.write_bool_value("useCertificatesForOnPremisesAuthEnabled", self.use_certificates_for_on_premises_auth_enabled)
        writer.write_bool_value("useSecurityKeyForSignin", self.use_security_key_for_signin)
        writer.write_bool_value("windowsHelloForBusinessBlocked", self.windows_hello_for_business_blocked)
    
    @property
    def unlock_with_biometrics_enabled(self,) -> Optional[bool]:
        """
        Gets the unlockWithBiometricsEnabled property value. Controls the use of biometric gestures, such as face and fingerprint, as an alternative to the Windows Hello for Business PIN.  If set to False, biometric gestures are not allowed. Users must still configure a PIN as a backup in case of failures.
        Returns: Optional[bool]
        """
        return self._unlock_with_biometrics_enabled
    
    @unlock_with_biometrics_enabled.setter
    def unlock_with_biometrics_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the unlockWithBiometricsEnabled property value. Controls the use of biometric gestures, such as face and fingerprint, as an alternative to the Windows Hello for Business PIN.  If set to False, biometric gestures are not allowed. Users must still configure a PIN as a backup in case of failures.
        Args:
            value: Value to set for the unlockWithBiometricsEnabled property.
        """
        self._unlock_with_biometrics_enabled = value
    
    @property
    def use_certificates_for_on_premises_auth_enabled(self,) -> Optional[bool]:
        """
        Gets the useCertificatesForOnPremisesAuthEnabled property value. Boolean value that enables Windows Hello for Business to use certificates to authenticate on-premise resources.
        Returns: Optional[bool]
        """
        return self._use_certificates_for_on_premises_auth_enabled
    
    @use_certificates_for_on_premises_auth_enabled.setter
    def use_certificates_for_on_premises_auth_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the useCertificatesForOnPremisesAuthEnabled property value. Boolean value that enables Windows Hello for Business to use certificates to authenticate on-premise resources.
        Args:
            value: Value to set for the useCertificatesForOnPremisesAuthEnabled property.
        """
        self._use_certificates_for_on_premises_auth_enabled = value
    
    @property
    def use_security_key_for_signin(self,) -> Optional[bool]:
        """
        Gets the useSecurityKeyForSignin property value. Boolean value used to enable the Windows Hello security key as a logon credential.
        Returns: Optional[bool]
        """
        return self._use_security_key_for_signin
    
    @use_security_key_for_signin.setter
    def use_security_key_for_signin(self,value: Optional[bool] = None) -> None:
        """
        Sets the useSecurityKeyForSignin property value. Boolean value used to enable the Windows Hello security key as a logon credential.
        Args:
            value: Value to set for the useSecurityKeyForSignin property.
        """
        self._use_security_key_for_signin = value
    
    @property
    def windows_hello_for_business_blocked(self,) -> Optional[bool]:
        """
        Gets the windowsHelloForBusinessBlocked property value. Boolean value that blocks Windows Hello for Business as a method for signing into Windows.
        Returns: Optional[bool]
        """
        return self._windows_hello_for_business_blocked
    
    @windows_hello_for_business_blocked.setter
    def windows_hello_for_business_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsHelloForBusinessBlocked property value. Boolean value that blocks Windows Hello for Business as a method for signing into Windows.
        Args:
            value: Value to set for the windowsHelloForBusinessBlocked property.
        """
        self._windows_hello_for_business_blocked = value
    

