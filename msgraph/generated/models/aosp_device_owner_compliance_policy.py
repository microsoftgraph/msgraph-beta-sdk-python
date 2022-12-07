from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_device_owner_required_password_type = lazy_import('msgraph.generated.models.android_device_owner_required_password_type')
device_compliance_policy = lazy_import('msgraph.generated.models.device_compliance_policy')

class AospDeviceOwnerCompliancePolicy(device_compliance_policy.DeviceCompliancePolicy):
    def __init__(self,) -> None:
        """
        Instantiates a new AospDeviceOwnerCompliancePolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.aospDeviceOwnerCompliancePolicy"
        # Minimum Android security patch level.
        self._min_android_security_patch_level: Optional[str] = None
        # Maximum Android version.
        self._os_maximum_version: Optional[str] = None
        # Minimum Android version.
        self._os_minimum_version: Optional[str] = None
        # Minimum password length. Valid values 4 to 16
        self._password_minimum_length: Optional[int] = None
        # Minutes of inactivity before a password is required. Valid values 1 to 8640
        self._password_minutes_of_inactivity_before_lock: Optional[int] = None
        # Require a password to unlock device.
        self._password_required: Optional[bool] = None
        # Type of characters in password. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
        self._password_required_type: Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType] = None
        # Devices must not be jailbroken or rooted.
        self._security_block_jailbroken_devices: Optional[bool] = None
        # Require encryption on Android devices.
        self._storage_require_encryption: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AospDeviceOwnerCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AospDeviceOwnerCompliancePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AospDeviceOwnerCompliancePolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "min_android_security_patch_level": lambda n : setattr(self, 'min_android_security_patch_level', n.get_str_value()),
            "os_maximum_version": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "os_minimum_version": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "password_minimum_length": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "password_minutes_of_inactivity_before_lock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "password_required": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType)),
            "security_block_jailbroken_devices": lambda n : setattr(self, 'security_block_jailbroken_devices', n.get_bool_value()),
            "storage_require_encryption": lambda n : setattr(self, 'storage_require_encryption', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def min_android_security_patch_level(self,) -> Optional[str]:
        """
        Gets the minAndroidSecurityPatchLevel property value. Minimum Android security patch level.
        Returns: Optional[str]
        """
        return self._min_android_security_patch_level
    
    @min_android_security_patch_level.setter
    def min_android_security_patch_level(self,value: Optional[str] = None) -> None:
        """
        Sets the minAndroidSecurityPatchLevel property value. Minimum Android security patch level.
        Args:
            value: Value to set for the minAndroidSecurityPatchLevel property.
        """
        self._min_android_security_patch_level = value
    
    @property
    def os_maximum_version(self,) -> Optional[str]:
        """
        Gets the osMaximumVersion property value. Maximum Android version.
        Returns: Optional[str]
        """
        return self._os_maximum_version
    
    @os_maximum_version.setter
    def os_maximum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMaximumVersion property value. Maximum Android version.
        Args:
            value: Value to set for the osMaximumVersion property.
        """
        self._os_maximum_version = value
    
    @property
    def os_minimum_version(self,) -> Optional[str]:
        """
        Gets the osMinimumVersion property value. Minimum Android version.
        Returns: Optional[str]
        """
        return self._os_minimum_version
    
    @os_minimum_version.setter
    def os_minimum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMinimumVersion property value. Minimum Android version.
        Args:
            value: Value to set for the osMinimumVersion property.
        """
        self._os_minimum_version = value
    
    @property
    def password_minimum_length(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLength property value. Minimum password length. Valid values 4 to 16
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. Minimum password length. Valid values 4 to 16
        Args:
            value: Value to set for the passwordMinimumLength property.
        """
        self._password_minimum_length = value
    
    @property
    def password_minutes_of_inactivity_before_lock(self,) -> Optional[int]:
        """
        Gets the passwordMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a password is required. Valid values 1 to 8640
        Returns: Optional[int]
        """
        return self._password_minutes_of_inactivity_before_lock
    
    @password_minutes_of_inactivity_before_lock.setter
    def password_minutes_of_inactivity_before_lock(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a password is required. Valid values 1 to 8640
        Args:
            value: Value to set for the passwordMinutesOfInactivityBeforeLock property.
        """
        self._password_minutes_of_inactivity_before_lock = value
    
    @property
    def password_required(self,) -> Optional[bool]:
        """
        Gets the passwordRequired property value. Require a password to unlock device.
        Returns: Optional[bool]
        """
        return self._password_required
    
    @password_required.setter
    def password_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRequired property value. Require a password to unlock device.
        Args:
            value: Value to set for the passwordRequired property.
        """
        self._password_required = value
    
    @property
    def password_required_type(self,) -> Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType]:
        """
        Gets the passwordRequiredType property value. Type of characters in password. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
        Returns: Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType]
        """
        return self._password_required_type
    
    @password_required_type.setter
    def password_required_type(self,value: Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType] = None) -> None:
        """
        Sets the passwordRequiredType property value. Type of characters in password. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
        Args:
            value: Value to set for the passwordRequiredType property.
        """
        self._password_required_type = value
    
    @property
    def security_block_jailbroken_devices(self,) -> Optional[bool]:
        """
        Gets the securityBlockJailbrokenDevices property value. Devices must not be jailbroken or rooted.
        Returns: Optional[bool]
        """
        return self._security_block_jailbroken_devices
    
    @security_block_jailbroken_devices.setter
    def security_block_jailbroken_devices(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityBlockJailbrokenDevices property value. Devices must not be jailbroken or rooted.
        Args:
            value: Value to set for the securityBlockJailbrokenDevices property.
        """
        self._security_block_jailbroken_devices = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("minAndroidSecurityPatchLevel", self.min_android_security_patch_level)
        writer.write_str_value("osMaximumVersion", self.os_maximum_version)
        writer.write_str_value("osMinimumVersion", self.os_minimum_version)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeLock", self.password_minutes_of_inactivity_before_lock)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_bool_value("securityBlockJailbrokenDevices", self.security_block_jailbroken_devices)
        writer.write_bool_value("storageRequireEncryption", self.storage_require_encryption)
    
    @property
    def storage_require_encryption(self,) -> Optional[bool]:
        """
        Gets the storageRequireEncryption property value. Require encryption on Android devices.
        Returns: Optional[bool]
        """
        return self._storage_require_encryption
    
    @storage_require_encryption.setter
    def storage_require_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageRequireEncryption property value. Require encryption on Android devices.
        Args:
            value: Value to set for the storageRequireEncryption property.
        """
        self._storage_require_encryption = value
    

