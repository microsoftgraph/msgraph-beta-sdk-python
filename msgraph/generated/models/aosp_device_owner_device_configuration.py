from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_owner_required_password_type, device_configuration

from . import device_configuration

class AospDeviceOwnerDeviceConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new AospDeviceOwnerDeviceConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.aospDeviceOwnerDeviceConfiguration"
        # Indicates whether or not the user is allowed to enable unknown sources setting. When set to true, user is not allowed to enable unknown sources settings.
        self._apps_block_install_from_unknown_sources: Optional[bool] = None
        # Indicates whether or not to block a user from configuring bluetooth.
        self._bluetooth_block_configuration: Optional[bool] = None
        # Indicates whether or not to disable the use of bluetooth. When set to true, bluetooth cannot be enabled on the device.
        self._bluetooth_blocked: Optional[bool] = None
        # Indicates whether or not to disable the use of the camera.
        self._camera_blocked: Optional[bool] = None
        # Indicates whether or not the factory reset option in settings is disabled.
        self._factory_reset_blocked: Optional[bool] = None
        # Indicates the minimum length of the password required on the device. Valid values 4 to 16
        self._password_minimum_length: Optional[int] = None
        # Minutes of inactivity before the screen times out.
        self._password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
        # Indicates the minimum password quality required on the device. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
        self._password_required_type: Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType] = None
        # Indicates the number of times a user can enter an incorrect password before the device is wiped. Valid values 4 to 11
        self._password_sign_in_failure_count_before_factory_reset: Optional[int] = None
        # Indicates whether or not to disable the capability to take screenshots.
        self._screen_capture_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from enabling debugging features on the device.
        self._security_allow_debugging_features: Optional[bool] = None
        # Indicates whether or not to block external media.
        self._storage_block_external_media: Optional[bool] = None
        # Indicates whether or not to block USB file transfer.
        self._storage_block_usb_file_transfer: Optional[bool] = None
        # Indicates whether or not to block the user from editing the wifi connection settings.
        self._wifi_block_edit_configurations: Optional[bool] = None
    
    @property
    def apps_block_install_from_unknown_sources(self,) -> Optional[bool]:
        """
        Gets the appsBlockInstallFromUnknownSources property value. Indicates whether or not the user is allowed to enable unknown sources setting. When set to true, user is not allowed to enable unknown sources settings.
        Returns: Optional[bool]
        """
        return self._apps_block_install_from_unknown_sources
    
    @apps_block_install_from_unknown_sources.setter
    def apps_block_install_from_unknown_sources(self,value: Optional[bool] = None) -> None:
        """
        Sets the appsBlockInstallFromUnknownSources property value. Indicates whether or not the user is allowed to enable unknown sources setting. When set to true, user is not allowed to enable unknown sources settings.
        Args:
            value: Value to set for the apps_block_install_from_unknown_sources property.
        """
        self._apps_block_install_from_unknown_sources = value
    
    @property
    def bluetooth_block_configuration(self,) -> Optional[bool]:
        """
        Gets the bluetoothBlockConfiguration property value. Indicates whether or not to block a user from configuring bluetooth.
        Returns: Optional[bool]
        """
        return self._bluetooth_block_configuration
    
    @bluetooth_block_configuration.setter
    def bluetooth_block_configuration(self,value: Optional[bool] = None) -> None:
        """
        Sets the bluetoothBlockConfiguration property value. Indicates whether or not to block a user from configuring bluetooth.
        Args:
            value: Value to set for the bluetooth_block_configuration property.
        """
        self._bluetooth_block_configuration = value
    
    @property
    def bluetooth_blocked(self,) -> Optional[bool]:
        """
        Gets the bluetoothBlocked property value. Indicates whether or not to disable the use of bluetooth. When set to true, bluetooth cannot be enabled on the device.
        Returns: Optional[bool]
        """
        return self._bluetooth_blocked
    
    @bluetooth_blocked.setter
    def bluetooth_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the bluetoothBlocked property value. Indicates whether or not to disable the use of bluetooth. When set to true, bluetooth cannot be enabled on the device.
        Args:
            value: Value to set for the bluetooth_blocked property.
        """
        self._bluetooth_blocked = value
    
    @property
    def camera_blocked(self,) -> Optional[bool]:
        """
        Gets the cameraBlocked property value. Indicates whether or not to disable the use of the camera.
        Returns: Optional[bool]
        """
        return self._camera_blocked
    
    @camera_blocked.setter
    def camera_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the cameraBlocked property value. Indicates whether or not to disable the use of the camera.
        Args:
            value: Value to set for the camera_blocked property.
        """
        self._camera_blocked = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AospDeviceOwnerDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AospDeviceOwnerDeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AospDeviceOwnerDeviceConfiguration()
    
    @property
    def factory_reset_blocked(self,) -> Optional[bool]:
        """
        Gets the factoryResetBlocked property value. Indicates whether or not the factory reset option in settings is disabled.
        Returns: Optional[bool]
        """
        return self._factory_reset_blocked
    
    @factory_reset_blocked.setter
    def factory_reset_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the factoryResetBlocked property value. Indicates whether or not the factory reset option in settings is disabled.
        Args:
            value: Value to set for the factory_reset_blocked property.
        """
        self._factory_reset_blocked = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_device_owner_required_password_type, device_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "appsBlockInstallFromUnknownSources": lambda n : setattr(self, 'apps_block_install_from_unknown_sources', n.get_bool_value()),
            "bluetoothBlocked": lambda n : setattr(self, 'bluetooth_blocked', n.get_bool_value()),
            "bluetoothBlockConfiguration": lambda n : setattr(self, 'bluetooth_block_configuration', n.get_bool_value()),
            "cameraBlocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "factoryResetBlocked": lambda n : setattr(self, 'factory_reset_blocked', n.get_bool_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType)),
            "passwordSignInFailureCountBeforeFactoryReset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "screenCaptureBlocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "securityAllowDebuggingFeatures": lambda n : setattr(self, 'security_allow_debugging_features', n.get_bool_value()),
            "storageBlockExternalMedia": lambda n : setattr(self, 'storage_block_external_media', n.get_bool_value()),
            "storageBlockUsbFileTransfer": lambda n : setattr(self, 'storage_block_usb_file_transfer', n.get_bool_value()),
            "wifiBlockEditConfigurations": lambda n : setattr(self, 'wifi_block_edit_configurations', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def password_minimum_length(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLength property value. Indicates the minimum length of the password required on the device. Valid values 4 to 16
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. Indicates the minimum length of the password required on the device. Valid values 4 to 16
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
    def password_required_type(self,) -> Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType]:
        """
        Gets the passwordRequiredType property value. Indicates the minimum password quality required on the device. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
        Returns: Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType]
        """
        return self._password_required_type
    
    @password_required_type.setter
    def password_required_type(self,value: Optional[android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType] = None) -> None:
        """
        Sets the passwordRequiredType property value. Indicates the minimum password quality required on the device. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
        Args:
            value: Value to set for the password_required_type property.
        """
        self._password_required_type = value
    
    @property
    def password_sign_in_failure_count_before_factory_reset(self,) -> Optional[int]:
        """
        Gets the passwordSignInFailureCountBeforeFactoryReset property value. Indicates the number of times a user can enter an incorrect password before the device is wiped. Valid values 4 to 11
        Returns: Optional[int]
        """
        return self._password_sign_in_failure_count_before_factory_reset
    
    @password_sign_in_failure_count_before_factory_reset.setter
    def password_sign_in_failure_count_before_factory_reset(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordSignInFailureCountBeforeFactoryReset property value. Indicates the number of times a user can enter an incorrect password before the device is wiped. Valid values 4 to 11
        Args:
            value: Value to set for the password_sign_in_failure_count_before_factory_reset property.
        """
        self._password_sign_in_failure_count_before_factory_reset = value
    
    @property
    def screen_capture_blocked(self,) -> Optional[bool]:
        """
        Gets the screenCaptureBlocked property value. Indicates whether or not to disable the capability to take screenshots.
        Returns: Optional[bool]
        """
        return self._screen_capture_blocked
    
    @screen_capture_blocked.setter
    def screen_capture_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the screenCaptureBlocked property value. Indicates whether or not to disable the capability to take screenshots.
        Args:
            value: Value to set for the screen_capture_blocked property.
        """
        self._screen_capture_blocked = value
    
    @property
    def security_allow_debugging_features(self,) -> Optional[bool]:
        """
        Gets the securityAllowDebuggingFeatures property value. Indicates whether or not to block the user from enabling debugging features on the device.
        Returns: Optional[bool]
        """
        return self._security_allow_debugging_features
    
    @security_allow_debugging_features.setter
    def security_allow_debugging_features(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityAllowDebuggingFeatures property value. Indicates whether or not to block the user from enabling debugging features on the device.
        Args:
            value: Value to set for the security_allow_debugging_features property.
        """
        self._security_allow_debugging_features = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("appsBlockInstallFromUnknownSources", self.apps_block_install_from_unknown_sources)
        writer.write_bool_value("bluetoothBlocked", self.bluetooth_blocked)
        writer.write_bool_value("bluetoothBlockConfiguration", self.bluetooth_block_configuration)
        writer.write_bool_value("cameraBlocked", self.camera_blocked)
        writer.write_bool_value("factoryResetBlocked", self.factory_reset_blocked)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeScreenTimeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_int_value("passwordSignInFailureCountBeforeFactoryReset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_bool_value("securityAllowDebuggingFeatures", self.security_allow_debugging_features)
        writer.write_bool_value("storageBlockExternalMedia", self.storage_block_external_media)
        writer.write_bool_value("storageBlockUsbFileTransfer", self.storage_block_usb_file_transfer)
        writer.write_bool_value("wifiBlockEditConfigurations", self.wifi_block_edit_configurations)
    
    @property
    def storage_block_external_media(self,) -> Optional[bool]:
        """
        Gets the storageBlockExternalMedia property value. Indicates whether or not to block external media.
        Returns: Optional[bool]
        """
        return self._storage_block_external_media
    
    @storage_block_external_media.setter
    def storage_block_external_media(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageBlockExternalMedia property value. Indicates whether or not to block external media.
        Args:
            value: Value to set for the storage_block_external_media property.
        """
        self._storage_block_external_media = value
    
    @property
    def storage_block_usb_file_transfer(self,) -> Optional[bool]:
        """
        Gets the storageBlockUsbFileTransfer property value. Indicates whether or not to block USB file transfer.
        Returns: Optional[bool]
        """
        return self._storage_block_usb_file_transfer
    
    @storage_block_usb_file_transfer.setter
    def storage_block_usb_file_transfer(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageBlockUsbFileTransfer property value. Indicates whether or not to block USB file transfer.
        Args:
            value: Value to set for the storage_block_usb_file_transfer property.
        """
        self._storage_block_usb_file_transfer = value
    
    @property
    def wifi_block_edit_configurations(self,) -> Optional[bool]:
        """
        Gets the wifiBlockEditConfigurations property value. Indicates whether or not to block the user from editing the wifi connection settings.
        Returns: Optional[bool]
        """
        return self._wifi_block_edit_configurations
    
    @wifi_block_edit_configurations.setter
    def wifi_block_edit_configurations(self,value: Optional[bool] = None) -> None:
        """
        Sets the wifiBlockEditConfigurations property value. Indicates whether or not to block the user from editing the wifi connection settings.
        Args:
            value: Value to set for the wifi_block_edit_configurations property.
        """
        self._wifi_block_edit_configurations = value
    

