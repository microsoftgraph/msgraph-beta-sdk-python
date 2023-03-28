from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_compliance_policy, device_threat_protection_level, mac_o_s_gatekeeper_app_sources, required_password_type

from . import device_compliance_policy

class MacOSCompliancePolicy(device_compliance_policy.DeviceCompliancePolicy):
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSCompliancePolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSCompliancePolicy"
        # Device threat protection levels for the Device Threat Protection API.
        self._advanced_threat_protection_required_security_level: Optional[device_threat_protection_level.DeviceThreatProtectionLevel] = None
        # Require that devices have enabled device threat protection.
        self._device_threat_protection_enabled: Optional[bool] = None
        # Device threat protection levels for the Device Threat Protection API.
        self._device_threat_protection_required_security_level: Optional[device_threat_protection_level.DeviceThreatProtectionLevel] = None
        # Corresponds to the 'Block all incoming connections' option.
        self._firewall_block_all_incoming: Optional[bool] = None
        # Corresponds to 'Enable stealth mode.'
        self._firewall_enable_stealth_mode: Optional[bool] = None
        # Whether the firewall should be enabled or not.
        self._firewall_enabled: Optional[bool] = None
        # App source options for macOS Gatekeeper.
        self._gatekeeper_allowed_app_source: Optional[mac_o_s_gatekeeper_app_sources.MacOSGatekeeperAppSources] = None
        # Maximum MacOS build version.
        self._os_maximum_build_version: Optional[str] = None
        # Maximum MacOS version.
        self._os_maximum_version: Optional[str] = None
        # Minimum MacOS build version.
        self._os_minimum_build_version: Optional[str] = None
        # Minimum MacOS version.
        self._os_minimum_version: Optional[str] = None
        # Indicates whether or not to block simple passwords.
        self._password_block_simple: Optional[bool] = None
        # Number of days before the password expires. Valid values 1 to 65535
        self._password_expiration_days: Optional[int] = None
        # The number of character sets required in the password.
        self._password_minimum_character_set_count: Optional[int] = None
        # Minimum length of password. Valid values 4 to 14
        self._password_minimum_length: Optional[int] = None
        # Minutes of inactivity before a password is required.
        self._password_minutes_of_inactivity_before_lock: Optional[int] = None
        # Number of previous passwords to block. Valid values 1 to 24
        self._password_previous_password_block_count: Optional[int] = None
        # Whether or not to require a password.
        self._password_required: Optional[bool] = None
        # Possible values of required passwords.
        self._password_required_type: Optional[required_password_type.RequiredPasswordType] = None
        # Require encryption on Mac OS devices.
        self._storage_require_encryption: Optional[bool] = None
        # Require that devices have enabled system integrity protection.
        self._system_integrity_protection_enabled: Optional[bool] = None
    
    @property
    def advanced_threat_protection_required_security_level(self,) -> Optional[device_threat_protection_level.DeviceThreatProtectionLevel]:
        """
        Gets the advancedThreatProtectionRequiredSecurityLevel property value. Device threat protection levels for the Device Threat Protection API.
        Returns: Optional[device_threat_protection_level.DeviceThreatProtectionLevel]
        """
        return self._advanced_threat_protection_required_security_level
    
    @advanced_threat_protection_required_security_level.setter
    def advanced_threat_protection_required_security_level(self,value: Optional[device_threat_protection_level.DeviceThreatProtectionLevel] = None) -> None:
        """
        Sets the advancedThreatProtectionRequiredSecurityLevel property value. Device threat protection levels for the Device Threat Protection API.
        Args:
            value: Value to set for the advanced_threat_protection_required_security_level property.
        """
        self._advanced_threat_protection_required_security_level = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSCompliancePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSCompliancePolicy()
    
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
            value: Value to set for the device_threat_protection_enabled property.
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
            value: Value to set for the device_threat_protection_required_security_level property.
        """
        self._device_threat_protection_required_security_level = value
    
    @property
    def firewall_block_all_incoming(self,) -> Optional[bool]:
        """
        Gets the firewallBlockAllIncoming property value. Corresponds to the 'Block all incoming connections' option.
        Returns: Optional[bool]
        """
        return self._firewall_block_all_incoming
    
    @firewall_block_all_incoming.setter
    def firewall_block_all_incoming(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallBlockAllIncoming property value. Corresponds to the 'Block all incoming connections' option.
        Args:
            value: Value to set for the firewall_block_all_incoming property.
        """
        self._firewall_block_all_incoming = value
    
    @property
    def firewall_enable_stealth_mode(self,) -> Optional[bool]:
        """
        Gets the firewallEnableStealthMode property value. Corresponds to 'Enable stealth mode.'
        Returns: Optional[bool]
        """
        return self._firewall_enable_stealth_mode
    
    @firewall_enable_stealth_mode.setter
    def firewall_enable_stealth_mode(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallEnableStealthMode property value. Corresponds to 'Enable stealth mode.'
        Args:
            value: Value to set for the firewall_enable_stealth_mode property.
        """
        self._firewall_enable_stealth_mode = value
    
    @property
    def firewall_enabled(self,) -> Optional[bool]:
        """
        Gets the firewallEnabled property value. Whether the firewall should be enabled or not.
        Returns: Optional[bool]
        """
        return self._firewall_enabled
    
    @firewall_enabled.setter
    def firewall_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallEnabled property value. Whether the firewall should be enabled or not.
        Args:
            value: Value to set for the firewall_enabled property.
        """
        self._firewall_enabled = value
    
    @property
    def gatekeeper_allowed_app_source(self,) -> Optional[mac_o_s_gatekeeper_app_sources.MacOSGatekeeperAppSources]:
        """
        Gets the gatekeeperAllowedAppSource property value. App source options for macOS Gatekeeper.
        Returns: Optional[mac_o_s_gatekeeper_app_sources.MacOSGatekeeperAppSources]
        """
        return self._gatekeeper_allowed_app_source
    
    @gatekeeper_allowed_app_source.setter
    def gatekeeper_allowed_app_source(self,value: Optional[mac_o_s_gatekeeper_app_sources.MacOSGatekeeperAppSources] = None) -> None:
        """
        Sets the gatekeeperAllowedAppSource property value. App source options for macOS Gatekeeper.
        Args:
            value: Value to set for the gatekeeper_allowed_app_source property.
        """
        self._gatekeeper_allowed_app_source = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_compliance_policy, device_threat_protection_level, mac_o_s_gatekeeper_app_sources, required_password_type

        fields: Dict[str, Callable[[Any], None]] = {
            "advancedThreatProtectionRequiredSecurityLevel": lambda n : setattr(self, 'advanced_threat_protection_required_security_level', n.get_enum_value(device_threat_protection_level.DeviceThreatProtectionLevel)),
            "deviceThreatProtectionEnabled": lambda n : setattr(self, 'device_threat_protection_enabled', n.get_bool_value()),
            "deviceThreatProtectionRequiredSecurityLevel": lambda n : setattr(self, 'device_threat_protection_required_security_level', n.get_enum_value(device_threat_protection_level.DeviceThreatProtectionLevel)),
            "firewallBlockAllIncoming": lambda n : setattr(self, 'firewall_block_all_incoming', n.get_bool_value()),
            "firewallEnabled": lambda n : setattr(self, 'firewall_enabled', n.get_bool_value()),
            "firewallEnableStealthMode": lambda n : setattr(self, 'firewall_enable_stealth_mode', n.get_bool_value()),
            "gatekeeperAllowedAppSource": lambda n : setattr(self, 'gatekeeper_allowed_app_source', n.get_enum_value(mac_o_s_gatekeeper_app_sources.MacOSGatekeeperAppSources)),
            "osMaximumBuildVersion": lambda n : setattr(self, 'os_maximum_build_version', n.get_str_value()),
            "osMaximumVersion": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "osMinimumBuildVersion": lambda n : setattr(self, 'os_minimum_build_version', n.get_str_value()),
            "osMinimumVersion": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "passwordBlockSimple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumCharacterSetCount": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequired": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(required_password_type.RequiredPasswordType)),
            "storageRequireEncryption": lambda n : setattr(self, 'storage_require_encryption', n.get_bool_value()),
            "systemIntegrityProtectionEnabled": lambda n : setattr(self, 'system_integrity_protection_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def os_maximum_build_version(self,) -> Optional[str]:
        """
        Gets the osMaximumBuildVersion property value. Maximum MacOS build version.
        Returns: Optional[str]
        """
        return self._os_maximum_build_version
    
    @os_maximum_build_version.setter
    def os_maximum_build_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMaximumBuildVersion property value. Maximum MacOS build version.
        Args:
            value: Value to set for the os_maximum_build_version property.
        """
        self._os_maximum_build_version = value
    
    @property
    def os_maximum_version(self,) -> Optional[str]:
        """
        Gets the osMaximumVersion property value. Maximum MacOS version.
        Returns: Optional[str]
        """
        return self._os_maximum_version
    
    @os_maximum_version.setter
    def os_maximum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMaximumVersion property value. Maximum MacOS version.
        Args:
            value: Value to set for the os_maximum_version property.
        """
        self._os_maximum_version = value
    
    @property
    def os_minimum_build_version(self,) -> Optional[str]:
        """
        Gets the osMinimumBuildVersion property value. Minimum MacOS build version.
        Returns: Optional[str]
        """
        return self._os_minimum_build_version
    
    @os_minimum_build_version.setter
    def os_minimum_build_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMinimumBuildVersion property value. Minimum MacOS build version.
        Args:
            value: Value to set for the os_minimum_build_version property.
        """
        self._os_minimum_build_version = value
    
    @property
    def os_minimum_version(self,) -> Optional[str]:
        """
        Gets the osMinimumVersion property value. Minimum MacOS version.
        Returns: Optional[str]
        """
        return self._os_minimum_version
    
    @os_minimum_version.setter
    def os_minimum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMinimumVersion property value. Minimum MacOS version.
        Args:
            value: Value to set for the os_minimum_version property.
        """
        self._os_minimum_version = value
    
    @property
    def password_block_simple(self,) -> Optional[bool]:
        """
        Gets the passwordBlockSimple property value. Indicates whether or not to block simple passwords.
        Returns: Optional[bool]
        """
        return self._password_block_simple
    
    @password_block_simple.setter
    def password_block_simple(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockSimple property value. Indicates whether or not to block simple passwords.
        Args:
            value: Value to set for the password_block_simple property.
        """
        self._password_block_simple = value
    
    @property
    def password_expiration_days(self,) -> Optional[int]:
        """
        Gets the passwordExpirationDays property value. Number of days before the password expires. Valid values 1 to 65535
        Returns: Optional[int]
        """
        return self._password_expiration_days
    
    @password_expiration_days.setter
    def password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordExpirationDays property value. Number of days before the password expires. Valid values 1 to 65535
        Args:
            value: Value to set for the password_expiration_days property.
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
            value: Value to set for the password_minimum_character_set_count property.
        """
        self._password_minimum_character_set_count = value
    
    @property
    def password_minimum_length(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLength property value. Minimum length of password. Valid values 4 to 14
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. Minimum length of password. Valid values 4 to 14
        Args:
            value: Value to set for the password_minimum_length property.
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
            value: Value to set for the password_minutes_of_inactivity_before_lock property.
        """
        self._password_minutes_of_inactivity_before_lock = value
    
    @property
    def password_previous_password_block_count(self,) -> Optional[int]:
        """
        Gets the passwordPreviousPasswordBlockCount property value. Number of previous passwords to block. Valid values 1 to 24
        Returns: Optional[int]
        """
        return self._password_previous_password_block_count
    
    @password_previous_password_block_count.setter
    def password_previous_password_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordPreviousPasswordBlockCount property value. Number of previous passwords to block. Valid values 1 to 24
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("advancedThreatProtectionRequiredSecurityLevel", self.advanced_threat_protection_required_security_level)
        writer.write_bool_value("deviceThreatProtectionEnabled", self.device_threat_protection_enabled)
        writer.write_enum_value("deviceThreatProtectionRequiredSecurityLevel", self.device_threat_protection_required_security_level)
        writer.write_bool_value("firewallBlockAllIncoming", self.firewall_block_all_incoming)
        writer.write_bool_value("firewallEnabled", self.firewall_enabled)
        writer.write_bool_value("firewallEnableStealthMode", self.firewall_enable_stealth_mode)
        writer.write_enum_value("gatekeeperAllowedAppSource", self.gatekeeper_allowed_app_source)
        writer.write_str_value("osMaximumBuildVersion", self.os_maximum_build_version)
        writer.write_str_value("osMaximumVersion", self.os_maximum_version)
        writer.write_str_value("osMinimumBuildVersion", self.os_minimum_build_version)
        writer.write_str_value("osMinimumVersion", self.os_minimum_version)
        writer.write_bool_value("passwordBlockSimple", self.password_block_simple)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumCharacterSetCount", self.password_minimum_character_set_count)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeLock", self.password_minutes_of_inactivity_before_lock)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_bool_value("storageRequireEncryption", self.storage_require_encryption)
        writer.write_bool_value("systemIntegrityProtectionEnabled", self.system_integrity_protection_enabled)
    
    @property
    def storage_require_encryption(self,) -> Optional[bool]:
        """
        Gets the storageRequireEncryption property value. Require encryption on Mac OS devices.
        Returns: Optional[bool]
        """
        return self._storage_require_encryption
    
    @storage_require_encryption.setter
    def storage_require_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageRequireEncryption property value. Require encryption on Mac OS devices.
        Args:
            value: Value to set for the storage_require_encryption property.
        """
        self._storage_require_encryption = value
    
    @property
    def system_integrity_protection_enabled(self,) -> Optional[bool]:
        """
        Gets the systemIntegrityProtectionEnabled property value. Require that devices have enabled system integrity protection.
        Returns: Optional[bool]
        """
        return self._system_integrity_protection_enabled
    
    @system_integrity_protection_enabled.setter
    def system_integrity_protection_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the systemIntegrityProtectionEnabled property value. Require that devices have enabled system integrity protection.
        Args:
            value: Value to set for the system_integrity_protection_enabled property.
        """
        self._system_integrity_protection_enabled = value
    

