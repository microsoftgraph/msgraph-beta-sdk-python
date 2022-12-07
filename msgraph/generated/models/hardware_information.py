from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_guard_local_system_authority_credential_guard_state = lazy_import('msgraph.generated.models.device_guard_local_system_authority_credential_guard_state')
device_guard_virtualization_based_security_hardware_requirement_state = lazy_import('msgraph.generated.models.device_guard_virtualization_based_security_hardware_requirement_state')
device_guard_virtualization_based_security_state = lazy_import('msgraph.generated.models.device_guard_virtualization_based_security_state')
device_licensing_status = lazy_import('msgraph.generated.models.device_licensing_status')
shared_apple_device_user = lazy_import('msgraph.generated.models.shared_apple_device_user')

class HardwareInformation(AdditionalDataHolder, Parsable):
    """
    Hardware information of a given device.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def battery_charge_cycles(self,) -> Optional[int]:
        """
        Gets the batteryChargeCycles property value. The number of charge cycles the device’s current battery has gone through. Valid values 0 to 2147483647
        Returns: Optional[int]
        """
        return self._battery_charge_cycles
    
    @battery_charge_cycles.setter
    def battery_charge_cycles(self,value: Optional[int] = None) -> None:
        """
        Sets the batteryChargeCycles property value. The number of charge cycles the device’s current battery has gone through. Valid values 0 to 2147483647
        Args:
            value: Value to set for the batteryChargeCycles property.
        """
        self._battery_charge_cycles = value
    
    @property
    def battery_health_percentage(self,) -> Optional[int]:
        """
        Gets the batteryHealthPercentage property value. The device’s current battery’s health percentage. Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._battery_health_percentage
    
    @battery_health_percentage.setter
    def battery_health_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the batteryHealthPercentage property value. The device’s current battery’s health percentage. Valid values 0 to 100
        Args:
            value: Value to set for the batteryHealthPercentage property.
        """
        self._battery_health_percentage = value
    
    @property
    def battery_level_percentage(self,) -> Optional[float]:
        """
        Gets the batteryLevelPercentage property value. The battery level, between 0.0 and 100, or null if the battery level cannot be determined. The update frequency of this property is per-checkin. Note this property is currently supported only on devices running iOS 5.0 and later, and is available only when Device Information access right is obtained. Valid values 0 to 100
        Returns: Optional[float]
        """
        return self._battery_level_percentage
    
    @battery_level_percentage.setter
    def battery_level_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the batteryLevelPercentage property value. The battery level, between 0.0 and 100, or null if the battery level cannot be determined. The update frequency of this property is per-checkin. Note this property is currently supported only on devices running iOS 5.0 and later, and is available only when Device Information access right is obtained. Valid values 0 to 100
        Args:
            value: Value to set for the batteryLevelPercentage property.
        """
        self._battery_level_percentage = value
    
    @property
    def battery_serial_number(self,) -> Optional[str]:
        """
        Gets the batterySerialNumber property value. The serial number of the device’s current battery
        Returns: Optional[str]
        """
        return self._battery_serial_number
    
    @battery_serial_number.setter
    def battery_serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the batterySerialNumber property value. The serial number of the device’s current battery
        Args:
            value: Value to set for the batterySerialNumber property.
        """
        self._battery_serial_number = value
    
    @property
    def cellular_technology(self,) -> Optional[str]:
        """
        Gets the cellularTechnology property value. Cellular technology of the device
        Returns: Optional[str]
        """
        return self._cellular_technology
    
    @cellular_technology.setter
    def cellular_technology(self,value: Optional[str] = None) -> None:
        """
        Sets the cellularTechnology property value. Cellular technology of the device
        Args:
            value: Value to set for the cellularTechnology property.
        """
        self._cellular_technology = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new hardwareInformation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number of charge cycles the device’s current battery has gone through. Valid values 0 to 2147483647
        self._battery_charge_cycles: Optional[int] = None
        # The device’s current battery’s health percentage. Valid values 0 to 100
        self._battery_health_percentage: Optional[int] = None
        # The battery level, between 0.0 and 100, or null if the battery level cannot be determined. The update frequency of this property is per-checkin. Note this property is currently supported only on devices running iOS 5.0 and later, and is available only when Device Information access right is obtained. Valid values 0 to 100
        self._battery_level_percentage: Optional[float] = None
        # The serial number of the device’s current battery
        self._battery_serial_number: Optional[str] = None
        # Cellular technology of the device
        self._cellular_technology: Optional[str] = None
        # Returns the fully qualified domain name of the device (if any). If the device is not domain-joined, it returns an empty string.
        self._device_full_qualified_domain_name: Optional[str] = None
        # The deviceGuardLocalSystemAuthorityCredentialGuardState property
        self._device_guard_local_system_authority_credential_guard_state: Optional[device_guard_local_system_authority_credential_guard_state.DeviceGuardLocalSystemAuthorityCredentialGuardState] = None
        # The deviceGuardVirtualizationBasedSecurityHardwareRequirementState property
        self._device_guard_virtualization_based_security_hardware_requirement_state: Optional[device_guard_virtualization_based_security_hardware_requirement_state.DeviceGuardVirtualizationBasedSecurityHardwareRequirementState] = None
        # The deviceGuardVirtualizationBasedSecurityState property
        self._device_guard_virtualization_based_security_state: Optional[device_guard_virtualization_based_security_state.DeviceGuardVirtualizationBasedSecurityState] = None
        # A standard error code indicating the last error, or 0 indicating no error (default). The update frequency of this property is daily. Note this property is currently supported only for Windows based Device based subscription licensing. Valid values 0 to 2147483647
        self._device_licensing_last_error_code: Optional[int] = None
        # Error text message as a descripition for deviceLicensingLastErrorCode. The update frequency of this property is daily. Note this property is currently supported only for Windows based Device based subscription licensing.
        self._device_licensing_last_error_description: Optional[str] = None
        # Indicates the device licensing status after Windows device based subscription has been enabled.
        self._device_licensing_status: Optional[device_licensing_status.DeviceLicensingStatus] = None
        # eSIM identifier
        self._esim_identifier: Optional[str] = None
        # Free storage space of the device.
        self._free_storage_space: Optional[int] = None
        # IMEI
        self._imei: Optional[str] = None
        # IPAddressV4
        self._ip_address_v4: Optional[str] = None
        # Encryption status of the device
        self._is_encrypted: Optional[bool] = None
        # Shared iPad
        self._is_shared_device: Optional[bool] = None
        # Supervised mode of the device
        self._is_supervised: Optional[bool] = None
        # Manufacturer of the device
        self._manufacturer: Optional[str] = None
        # MEID
        self._meid: Optional[str] = None
        # Model of the device
        self._model: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # String that specifies the OS edition.
        self._operating_system_edition: Optional[str] = None
        # Operating system language of the device
        self._operating_system_language: Optional[str] = None
        # Int that specifies the Windows Operating System ProductType. More details here https://go.microsoft.com/fwlink/?linkid=2126950. Valid values 0 to 2147483647
        self._operating_system_product_type: Optional[int] = None
        # Operating System Build Number on Android device
        self._os_build_number: Optional[str] = None
        # Phone number of the device
        self._phone_number: Optional[str] = None
        # The product name, e.g. iPad8,12 etc. The update frequency of this property is weekly. Note this property is currently supported only on iOS/MacOS devices, and is available only when Device Information access right is obtained.
        self._product_name: Optional[str] = None
        # The number of users currently on this device, or null (default) if the value of this property cannot be determined. The update frequency of this property is per-checkin. Note this property is currently supported only on devices running iOS 13.4 and later, and is available only when Device Information access right is obtained. Valid values 0 to 2147483647
        self._resident_users_count: Optional[int] = None
        # Serial number.
        self._serial_number: Optional[str] = None
        # All users on the shared Apple device
        self._shared_device_cached_users: Optional[List[shared_apple_device_user.SharedAppleDeviceUser]] = None
        # SubnetAddress
        self._subnet_address: Optional[str] = None
        # Subscriber carrier of the device
        self._subscriber_carrier: Optional[str] = None
        # BIOS version as reported by SMBIOS
        self._system_management_b_i_o_s_version: Optional[str] = None
        # Total storage space of the device.
        self._total_storage_space: Optional[int] = None
        # The identifying information that uniquely names the TPM manufacturer
        self._tpm_manufacturer: Optional[str] = None
        # String that specifies the specification version.
        self._tpm_specification_version: Optional[str] = None
        # The version of the TPM, as specified by the manufacturer
        self._tpm_version: Optional[str] = None
        # WiFi MAC address of the device
        self._wifi_mac: Optional[str] = None
        # A list of wired IPv4 addresses. The update frequency (the maximum delay for the change of property value to be synchronized from the device to the cloud storage) of this property is daily. Note this property is currently supported only on devices running on Windows.
        self._wired_i_pv4_addresses: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HardwareInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HardwareInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HardwareInformation()
    
    @property
    def device_full_qualified_domain_name(self,) -> Optional[str]:
        """
        Gets the deviceFullQualifiedDomainName property value. Returns the fully qualified domain name of the device (if any). If the device is not domain-joined, it returns an empty string.
        Returns: Optional[str]
        """
        return self._device_full_qualified_domain_name
    
    @device_full_qualified_domain_name.setter
    def device_full_qualified_domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceFullQualifiedDomainName property value. Returns the fully qualified domain name of the device (if any). If the device is not domain-joined, it returns an empty string.
        Args:
            value: Value to set for the deviceFullQualifiedDomainName property.
        """
        self._device_full_qualified_domain_name = value
    
    @property
    def device_guard_local_system_authority_credential_guard_state(self,) -> Optional[device_guard_local_system_authority_credential_guard_state.DeviceGuardLocalSystemAuthorityCredentialGuardState]:
        """
        Gets the deviceGuardLocalSystemAuthorityCredentialGuardState property value. The deviceGuardLocalSystemAuthorityCredentialGuardState property
        Returns: Optional[device_guard_local_system_authority_credential_guard_state.DeviceGuardLocalSystemAuthorityCredentialGuardState]
        """
        return self._device_guard_local_system_authority_credential_guard_state
    
    @device_guard_local_system_authority_credential_guard_state.setter
    def device_guard_local_system_authority_credential_guard_state(self,value: Optional[device_guard_local_system_authority_credential_guard_state.DeviceGuardLocalSystemAuthorityCredentialGuardState] = None) -> None:
        """
        Sets the deviceGuardLocalSystemAuthorityCredentialGuardState property value. The deviceGuardLocalSystemAuthorityCredentialGuardState property
        Args:
            value: Value to set for the deviceGuardLocalSystemAuthorityCredentialGuardState property.
        """
        self._device_guard_local_system_authority_credential_guard_state = value
    
    @property
    def device_guard_virtualization_based_security_hardware_requirement_state(self,) -> Optional[device_guard_virtualization_based_security_hardware_requirement_state.DeviceGuardVirtualizationBasedSecurityHardwareRequirementState]:
        """
        Gets the deviceGuardVirtualizationBasedSecurityHardwareRequirementState property value. The deviceGuardVirtualizationBasedSecurityHardwareRequirementState property
        Returns: Optional[device_guard_virtualization_based_security_hardware_requirement_state.DeviceGuardVirtualizationBasedSecurityHardwareRequirementState]
        """
        return self._device_guard_virtualization_based_security_hardware_requirement_state
    
    @device_guard_virtualization_based_security_hardware_requirement_state.setter
    def device_guard_virtualization_based_security_hardware_requirement_state(self,value: Optional[device_guard_virtualization_based_security_hardware_requirement_state.DeviceGuardVirtualizationBasedSecurityHardwareRequirementState] = None) -> None:
        """
        Sets the deviceGuardVirtualizationBasedSecurityHardwareRequirementState property value. The deviceGuardVirtualizationBasedSecurityHardwareRequirementState property
        Args:
            value: Value to set for the deviceGuardVirtualizationBasedSecurityHardwareRequirementState property.
        """
        self._device_guard_virtualization_based_security_hardware_requirement_state = value
    
    @property
    def device_guard_virtualization_based_security_state(self,) -> Optional[device_guard_virtualization_based_security_state.DeviceGuardVirtualizationBasedSecurityState]:
        """
        Gets the deviceGuardVirtualizationBasedSecurityState property value. The deviceGuardVirtualizationBasedSecurityState property
        Returns: Optional[device_guard_virtualization_based_security_state.DeviceGuardVirtualizationBasedSecurityState]
        """
        return self._device_guard_virtualization_based_security_state
    
    @device_guard_virtualization_based_security_state.setter
    def device_guard_virtualization_based_security_state(self,value: Optional[device_guard_virtualization_based_security_state.DeviceGuardVirtualizationBasedSecurityState] = None) -> None:
        """
        Sets the deviceGuardVirtualizationBasedSecurityState property value. The deviceGuardVirtualizationBasedSecurityState property
        Args:
            value: Value to set for the deviceGuardVirtualizationBasedSecurityState property.
        """
        self._device_guard_virtualization_based_security_state = value
    
    @property
    def device_licensing_last_error_code(self,) -> Optional[int]:
        """
        Gets the deviceLicensingLastErrorCode property value. A standard error code indicating the last error, or 0 indicating no error (default). The update frequency of this property is daily. Note this property is currently supported only for Windows based Device based subscription licensing. Valid values 0 to 2147483647
        Returns: Optional[int]
        """
        return self._device_licensing_last_error_code
    
    @device_licensing_last_error_code.setter
    def device_licensing_last_error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceLicensingLastErrorCode property value. A standard error code indicating the last error, or 0 indicating no error (default). The update frequency of this property is daily. Note this property is currently supported only for Windows based Device based subscription licensing. Valid values 0 to 2147483647
        Args:
            value: Value to set for the deviceLicensingLastErrorCode property.
        """
        self._device_licensing_last_error_code = value
    
    @property
    def device_licensing_last_error_description(self,) -> Optional[str]:
        """
        Gets the deviceLicensingLastErrorDescription property value. Error text message as a descripition for deviceLicensingLastErrorCode. The update frequency of this property is daily. Note this property is currently supported only for Windows based Device based subscription licensing.
        Returns: Optional[str]
        """
        return self._device_licensing_last_error_description
    
    @device_licensing_last_error_description.setter
    def device_licensing_last_error_description(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceLicensingLastErrorDescription property value. Error text message as a descripition for deviceLicensingLastErrorCode. The update frequency of this property is daily. Note this property is currently supported only for Windows based Device based subscription licensing.
        Args:
            value: Value to set for the deviceLicensingLastErrorDescription property.
        """
        self._device_licensing_last_error_description = value
    
    @property
    def device_licensing_status(self,) -> Optional[device_licensing_status.DeviceLicensingStatus]:
        """
        Gets the deviceLicensingStatus property value. Indicates the device licensing status after Windows device based subscription has been enabled.
        Returns: Optional[device_licensing_status.DeviceLicensingStatus]
        """
        return self._device_licensing_status
    
    @device_licensing_status.setter
    def device_licensing_status(self,value: Optional[device_licensing_status.DeviceLicensingStatus] = None) -> None:
        """
        Sets the deviceLicensingStatus property value. Indicates the device licensing status after Windows device based subscription has been enabled.
        Args:
            value: Value to set for the deviceLicensingStatus property.
        """
        self._device_licensing_status = value
    
    @property
    def esim_identifier(self,) -> Optional[str]:
        """
        Gets the esimIdentifier property value. eSIM identifier
        Returns: Optional[str]
        """
        return self._esim_identifier
    
    @esim_identifier.setter
    def esim_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the esimIdentifier property value. eSIM identifier
        Args:
            value: Value to set for the esimIdentifier property.
        """
        self._esim_identifier = value
    
    @property
    def free_storage_space(self,) -> Optional[int]:
        """
        Gets the freeStorageSpace property value. Free storage space of the device.
        Returns: Optional[int]
        """
        return self._free_storage_space
    
    @free_storage_space.setter
    def free_storage_space(self,value: Optional[int] = None) -> None:
        """
        Sets the freeStorageSpace property value. Free storage space of the device.
        Args:
            value: Value to set for the freeStorageSpace property.
        """
        self._free_storage_space = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "battery_charge_cycles": lambda n : setattr(self, 'battery_charge_cycles', n.get_int_value()),
            "battery_health_percentage": lambda n : setattr(self, 'battery_health_percentage', n.get_int_value()),
            "battery_level_percentage": lambda n : setattr(self, 'battery_level_percentage', n.get_float_value()),
            "battery_serial_number": lambda n : setattr(self, 'battery_serial_number', n.get_str_value()),
            "cellular_technology": lambda n : setattr(self, 'cellular_technology', n.get_str_value()),
            "device_full_qualified_domain_name": lambda n : setattr(self, 'device_full_qualified_domain_name', n.get_str_value()),
            "device_guard_local_system_authority_credential_guard_state": lambda n : setattr(self, 'device_guard_local_system_authority_credential_guard_state', n.get_enum_value(device_guard_local_system_authority_credential_guard_state.DeviceGuardLocalSystemAuthorityCredentialGuardState)),
            "device_guard_virtualization_based_security_hardware_requirement_state": lambda n : setattr(self, 'device_guard_virtualization_based_security_hardware_requirement_state', n.get_enum_value(device_guard_virtualization_based_security_hardware_requirement_state.DeviceGuardVirtualizationBasedSecurityHardwareRequirementState)),
            "device_guard_virtualization_based_security_state": lambda n : setattr(self, 'device_guard_virtualization_based_security_state', n.get_enum_value(device_guard_virtualization_based_security_state.DeviceGuardVirtualizationBasedSecurityState)),
            "device_licensing_last_error_code": lambda n : setattr(self, 'device_licensing_last_error_code', n.get_int_value()),
            "device_licensing_last_error_description": lambda n : setattr(self, 'device_licensing_last_error_description', n.get_str_value()),
            "device_licensing_status": lambda n : setattr(self, 'device_licensing_status', n.get_enum_value(device_licensing_status.DeviceLicensingStatus)),
            "esim_identifier": lambda n : setattr(self, 'esim_identifier', n.get_str_value()),
            "free_storage_space": lambda n : setattr(self, 'free_storage_space', n.get_int_value()),
            "imei": lambda n : setattr(self, 'imei', n.get_str_value()),
            "ip_address_v4": lambda n : setattr(self, 'ip_address_v4', n.get_str_value()),
            "is_encrypted": lambda n : setattr(self, 'is_encrypted', n.get_bool_value()),
            "is_shared_device": lambda n : setattr(self, 'is_shared_device', n.get_bool_value()),
            "is_supervised": lambda n : setattr(self, 'is_supervised', n.get_bool_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "meid": lambda n : setattr(self, 'meid', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operating_system_edition": lambda n : setattr(self, 'operating_system_edition', n.get_str_value()),
            "operating_system_language": lambda n : setattr(self, 'operating_system_language', n.get_str_value()),
            "operating_system_product_type": lambda n : setattr(self, 'operating_system_product_type', n.get_int_value()),
            "os_build_number": lambda n : setattr(self, 'os_build_number', n.get_str_value()),
            "phone_number": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "product_name": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "resident_users_count": lambda n : setattr(self, 'resident_users_count', n.get_int_value()),
            "serial_number": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "shared_device_cached_users": lambda n : setattr(self, 'shared_device_cached_users', n.get_collection_of_object_values(shared_apple_device_user.SharedAppleDeviceUser)),
            "subnet_address": lambda n : setattr(self, 'subnet_address', n.get_str_value()),
            "subscriber_carrier": lambda n : setattr(self, 'subscriber_carrier', n.get_str_value()),
            "system_management_b_i_o_s_version": lambda n : setattr(self, 'system_management_b_i_o_s_version', n.get_str_value()),
            "total_storage_space": lambda n : setattr(self, 'total_storage_space', n.get_int_value()),
            "tpm_manufacturer": lambda n : setattr(self, 'tpm_manufacturer', n.get_str_value()),
            "tpm_specification_version": lambda n : setattr(self, 'tpm_specification_version', n.get_str_value()),
            "tpm_version": lambda n : setattr(self, 'tpm_version', n.get_str_value()),
            "wifi_mac": lambda n : setattr(self, 'wifi_mac', n.get_str_value()),
            "wired_i_pv4_addresses": lambda n : setattr(self, 'wired_i_pv4_addresses', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def imei(self,) -> Optional[str]:
        """
        Gets the imei property value. IMEI
        Returns: Optional[str]
        """
        return self._imei
    
    @imei.setter
    def imei(self,value: Optional[str] = None) -> None:
        """
        Sets the imei property value. IMEI
        Args:
            value: Value to set for the imei property.
        """
        self._imei = value
    
    @property
    def ip_address_v4(self,) -> Optional[str]:
        """
        Gets the ipAddressV4 property value. IPAddressV4
        Returns: Optional[str]
        """
        return self._ip_address_v4
    
    @ip_address_v4.setter
    def ip_address_v4(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddressV4 property value. IPAddressV4
        Args:
            value: Value to set for the ipAddressV4 property.
        """
        self._ip_address_v4 = value
    
    @property
    def is_encrypted(self,) -> Optional[bool]:
        """
        Gets the isEncrypted property value. Encryption status of the device
        Returns: Optional[bool]
        """
        return self._is_encrypted
    
    @is_encrypted.setter
    def is_encrypted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEncrypted property value. Encryption status of the device
        Args:
            value: Value to set for the isEncrypted property.
        """
        self._is_encrypted = value
    
    @property
    def is_shared_device(self,) -> Optional[bool]:
        """
        Gets the isSharedDevice property value. Shared iPad
        Returns: Optional[bool]
        """
        return self._is_shared_device
    
    @is_shared_device.setter
    def is_shared_device(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSharedDevice property value. Shared iPad
        Args:
            value: Value to set for the isSharedDevice property.
        """
        self._is_shared_device = value
    
    @property
    def is_supervised(self,) -> Optional[bool]:
        """
        Gets the isSupervised property value. Supervised mode of the device
        Returns: Optional[bool]
        """
        return self._is_supervised
    
    @is_supervised.setter
    def is_supervised(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSupervised property value. Supervised mode of the device
        Args:
            value: Value to set for the isSupervised property.
        """
        self._is_supervised = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. Manufacturer of the device
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. Manufacturer of the device
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def meid(self,) -> Optional[str]:
        """
        Gets the meid property value. MEID
        Returns: Optional[str]
        """
        return self._meid
    
    @meid.setter
    def meid(self,value: Optional[str] = None) -> None:
        """
        Sets the meid property value. MEID
        Args:
            value: Value to set for the meid property.
        """
        self._meid = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. Model of the device
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. Model of the device
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def operating_system_edition(self,) -> Optional[str]:
        """
        Gets the operatingSystemEdition property value. String that specifies the OS edition.
        Returns: Optional[str]
        """
        return self._operating_system_edition
    
    @operating_system_edition.setter
    def operating_system_edition(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystemEdition property value. String that specifies the OS edition.
        Args:
            value: Value to set for the operatingSystemEdition property.
        """
        self._operating_system_edition = value
    
    @property
    def operating_system_language(self,) -> Optional[str]:
        """
        Gets the operatingSystemLanguage property value. Operating system language of the device
        Returns: Optional[str]
        """
        return self._operating_system_language
    
    @operating_system_language.setter
    def operating_system_language(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystemLanguage property value. Operating system language of the device
        Args:
            value: Value to set for the operatingSystemLanguage property.
        """
        self._operating_system_language = value
    
    @property
    def operating_system_product_type(self,) -> Optional[int]:
        """
        Gets the operatingSystemProductType property value. Int that specifies the Windows Operating System ProductType. More details here https://go.microsoft.com/fwlink/?linkid=2126950. Valid values 0 to 2147483647
        Returns: Optional[int]
        """
        return self._operating_system_product_type
    
    @operating_system_product_type.setter
    def operating_system_product_type(self,value: Optional[int] = None) -> None:
        """
        Sets the operatingSystemProductType property value. Int that specifies the Windows Operating System ProductType. More details here https://go.microsoft.com/fwlink/?linkid=2126950. Valid values 0 to 2147483647
        Args:
            value: Value to set for the operatingSystemProductType property.
        """
        self._operating_system_product_type = value
    
    @property
    def os_build_number(self,) -> Optional[str]:
        """
        Gets the osBuildNumber property value. Operating System Build Number on Android device
        Returns: Optional[str]
        """
        return self._os_build_number
    
    @os_build_number.setter
    def os_build_number(self,value: Optional[str] = None) -> None:
        """
        Sets the osBuildNumber property value. Operating System Build Number on Android device
        Args:
            value: Value to set for the osBuildNumber property.
        """
        self._os_build_number = value
    
    @property
    def phone_number(self,) -> Optional[str]:
        """
        Gets the phoneNumber property value. Phone number of the device
        Returns: Optional[str]
        """
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the phoneNumber property value. Phone number of the device
        Args:
            value: Value to set for the phoneNumber property.
        """
        self._phone_number = value
    
    @property
    def product_name(self,) -> Optional[str]:
        """
        Gets the productName property value. The product name, e.g. iPad8,12 etc. The update frequency of this property is weekly. Note this property is currently supported only on iOS/MacOS devices, and is available only when Device Information access right is obtained.
        Returns: Optional[str]
        """
        return self._product_name
    
    @product_name.setter
    def product_name(self,value: Optional[str] = None) -> None:
        """
        Sets the productName property value. The product name, e.g. iPad8,12 etc. The update frequency of this property is weekly. Note this property is currently supported only on iOS/MacOS devices, and is available only when Device Information access right is obtained.
        Args:
            value: Value to set for the productName property.
        """
        self._product_name = value
    
    @property
    def resident_users_count(self,) -> Optional[int]:
        """
        Gets the residentUsersCount property value. The number of users currently on this device, or null (default) if the value of this property cannot be determined. The update frequency of this property is per-checkin. Note this property is currently supported only on devices running iOS 13.4 and later, and is available only when Device Information access right is obtained. Valid values 0 to 2147483647
        Returns: Optional[int]
        """
        return self._resident_users_count
    
    @resident_users_count.setter
    def resident_users_count(self,value: Optional[int] = None) -> None:
        """
        Sets the residentUsersCount property value. The number of users currently on this device, or null (default) if the value of this property cannot be determined. The update frequency of this property is per-checkin. Note this property is currently supported only on devices running iOS 13.4 and later, and is available only when Device Information access right is obtained. Valid values 0 to 2147483647
        Args:
            value: Value to set for the residentUsersCount property.
        """
        self._resident_users_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("batteryChargeCycles", self.battery_charge_cycles)
        writer.write_int_value("batteryHealthPercentage", self.battery_health_percentage)
        writer.write_float_value("batteryLevelPercentage", self.battery_level_percentage)
        writer.write_str_value("batterySerialNumber", self.battery_serial_number)
        writer.write_str_value("cellularTechnology", self.cellular_technology)
        writer.write_str_value("deviceFullQualifiedDomainName", self.device_full_qualified_domain_name)
        writer.write_enum_value("deviceGuardLocalSystemAuthorityCredentialGuardState", self.device_guard_local_system_authority_credential_guard_state)
        writer.write_enum_value("deviceGuardVirtualizationBasedSecurityHardwareRequirementState", self.device_guard_virtualization_based_security_hardware_requirement_state)
        writer.write_enum_value("deviceGuardVirtualizationBasedSecurityState", self.device_guard_virtualization_based_security_state)
        writer.write_int_value("deviceLicensingLastErrorCode", self.device_licensing_last_error_code)
        writer.write_str_value("deviceLicensingLastErrorDescription", self.device_licensing_last_error_description)
        writer.write_enum_value("deviceLicensingStatus", self.device_licensing_status)
        writer.write_str_value("esimIdentifier", self.esim_identifier)
        writer.write_int_value("freeStorageSpace", self.free_storage_space)
        writer.write_str_value("imei", self.imei)
        writer.write_str_value("ipAddressV4", self.ip_address_v4)
        writer.write_bool_value("isEncrypted", self.is_encrypted)
        writer.write_bool_value("isSharedDevice", self.is_shared_device)
        writer.write_bool_value("isSupervised", self.is_supervised)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("meid", self.meid)
        writer.write_str_value("model", self.model)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatingSystemEdition", self.operating_system_edition)
        writer.write_str_value("operatingSystemLanguage", self.operating_system_language)
        writer.write_int_value("operatingSystemProductType", self.operating_system_product_type)
        writer.write_str_value("osBuildNumber", self.os_build_number)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("productName", self.product_name)
        writer.write_int_value("residentUsersCount", self.resident_users_count)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_collection_of_object_values("sharedDeviceCachedUsers", self.shared_device_cached_users)
        writer.write_str_value("subnetAddress", self.subnet_address)
        writer.write_str_value("subscriberCarrier", self.subscriber_carrier)
        writer.write_str_value("systemManagementBIOSVersion", self.system_management_b_i_o_s_version)
        writer.write_int_value("totalStorageSpace", self.total_storage_space)
        writer.write_str_value("tpmManufacturer", self.tpm_manufacturer)
        writer.write_str_value("tpmSpecificationVersion", self.tpm_specification_version)
        writer.write_str_value("tpmVersion", self.tpm_version)
        writer.write_str_value("wifiMac", self.wifi_mac)
        writer.write_collection_of_primitive_values("wiredIPv4Addresses", self.wired_i_pv4_addresses)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def serial_number(self,) -> Optional[str]:
        """
        Gets the serialNumber property value. Serial number.
        Returns: Optional[str]
        """
        return self._serial_number
    
    @serial_number.setter
    def serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the serialNumber property value. Serial number.
        Args:
            value: Value to set for the serialNumber property.
        """
        self._serial_number = value
    
    @property
    def shared_device_cached_users(self,) -> Optional[List[shared_apple_device_user.SharedAppleDeviceUser]]:
        """
        Gets the sharedDeviceCachedUsers property value. All users on the shared Apple device
        Returns: Optional[List[shared_apple_device_user.SharedAppleDeviceUser]]
        """
        return self._shared_device_cached_users
    
    @shared_device_cached_users.setter
    def shared_device_cached_users(self,value: Optional[List[shared_apple_device_user.SharedAppleDeviceUser]] = None) -> None:
        """
        Sets the sharedDeviceCachedUsers property value. All users on the shared Apple device
        Args:
            value: Value to set for the sharedDeviceCachedUsers property.
        """
        self._shared_device_cached_users = value
    
    @property
    def subnet_address(self,) -> Optional[str]:
        """
        Gets the subnetAddress property value. SubnetAddress
        Returns: Optional[str]
        """
        return self._subnet_address
    
    @subnet_address.setter
    def subnet_address(self,value: Optional[str] = None) -> None:
        """
        Sets the subnetAddress property value. SubnetAddress
        Args:
            value: Value to set for the subnetAddress property.
        """
        self._subnet_address = value
    
    @property
    def subscriber_carrier(self,) -> Optional[str]:
        """
        Gets the subscriberCarrier property value. Subscriber carrier of the device
        Returns: Optional[str]
        """
        return self._subscriber_carrier
    
    @subscriber_carrier.setter
    def subscriber_carrier(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriberCarrier property value. Subscriber carrier of the device
        Args:
            value: Value to set for the subscriberCarrier property.
        """
        self._subscriber_carrier = value
    
    @property
    def system_management_b_i_o_s_version(self,) -> Optional[str]:
        """
        Gets the systemManagementBIOSVersion property value. BIOS version as reported by SMBIOS
        Returns: Optional[str]
        """
        return self._system_management_b_i_o_s_version
    
    @system_management_b_i_o_s_version.setter
    def system_management_b_i_o_s_version(self,value: Optional[str] = None) -> None:
        """
        Sets the systemManagementBIOSVersion property value. BIOS version as reported by SMBIOS
        Args:
            value: Value to set for the systemManagementBIOSVersion property.
        """
        self._system_management_b_i_o_s_version = value
    
    @property
    def total_storage_space(self,) -> Optional[int]:
        """
        Gets the totalStorageSpace property value. Total storage space of the device.
        Returns: Optional[int]
        """
        return self._total_storage_space
    
    @total_storage_space.setter
    def total_storage_space(self,value: Optional[int] = None) -> None:
        """
        Sets the totalStorageSpace property value. Total storage space of the device.
        Args:
            value: Value to set for the totalStorageSpace property.
        """
        self._total_storage_space = value
    
    @property
    def tpm_manufacturer(self,) -> Optional[str]:
        """
        Gets the tpmManufacturer property value. The identifying information that uniquely names the TPM manufacturer
        Returns: Optional[str]
        """
        return self._tpm_manufacturer
    
    @tpm_manufacturer.setter
    def tpm_manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the tpmManufacturer property value. The identifying information that uniquely names the TPM manufacturer
        Args:
            value: Value to set for the tpmManufacturer property.
        """
        self._tpm_manufacturer = value
    
    @property
    def tpm_specification_version(self,) -> Optional[str]:
        """
        Gets the tpmSpecificationVersion property value. String that specifies the specification version.
        Returns: Optional[str]
        """
        return self._tpm_specification_version
    
    @tpm_specification_version.setter
    def tpm_specification_version(self,value: Optional[str] = None) -> None:
        """
        Sets the tpmSpecificationVersion property value. String that specifies the specification version.
        Args:
            value: Value to set for the tpmSpecificationVersion property.
        """
        self._tpm_specification_version = value
    
    @property
    def tpm_version(self,) -> Optional[str]:
        """
        Gets the tpmVersion property value. The version of the TPM, as specified by the manufacturer
        Returns: Optional[str]
        """
        return self._tpm_version
    
    @tpm_version.setter
    def tpm_version(self,value: Optional[str] = None) -> None:
        """
        Sets the tpmVersion property value. The version of the TPM, as specified by the manufacturer
        Args:
            value: Value to set for the tpmVersion property.
        """
        self._tpm_version = value
    
    @property
    def wifi_mac(self,) -> Optional[str]:
        """
        Gets the wifiMac property value. WiFi MAC address of the device
        Returns: Optional[str]
        """
        return self._wifi_mac
    
    @wifi_mac.setter
    def wifi_mac(self,value: Optional[str] = None) -> None:
        """
        Sets the wifiMac property value. WiFi MAC address of the device
        Args:
            value: Value to set for the wifiMac property.
        """
        self._wifi_mac = value
    
    @property
    def wired_i_pv4_addresses(self,) -> Optional[List[str]]:
        """
        Gets the wiredIPv4Addresses property value. A list of wired IPv4 addresses. The update frequency (the maximum delay for the change of property value to be synchronized from the device to the cloud storage) of this property is daily. Note this property is currently supported only on devices running on Windows.
        Returns: Optional[List[str]]
        """
        return self._wired_i_pv4_addresses
    
    @wired_i_pv4_addresses.setter
    def wired_i_pv4_addresses(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the wiredIPv4Addresses property value. A list of wired IPv4 addresses. The update frequency (the maximum delay for the change of property value to be synchronized from the device to the cloud storage) of this property is daily. Note this property is currently supported only on devices running on Windows.
        Args:
            value: Value to set for the wiredIPv4Addresses property.
        """
        self._wired_i_pv4_addresses = value
    

