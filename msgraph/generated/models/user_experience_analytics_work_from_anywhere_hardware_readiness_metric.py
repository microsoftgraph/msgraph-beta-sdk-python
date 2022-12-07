from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The percentage of devices for which OS check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._os_check_failed_percentage: Optional[float] = None
        # The percentage of devices for which processor hardware 64-bit architecture check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._processor64_bit_check_failed_percentage: Optional[float] = None
        # The percentage of devices for which processor hardware core count check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._processor_core_count_check_failed_percentage: Optional[float] = None
        # The percentage of devices for which processor hardware family check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._processor_family_check_failed_percentage: Optional[float] = None
        # The percentage of devices for which processor hardware speed check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._processor_speed_check_failed_percentage: Optional[float] = None
        # The percentage of devices for which RAM hardware check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._ram_check_failed_percentage: Optional[float] = None
        # The percentage of devices for which secure boot hardware check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._secure_boot_check_failed_percentage: Optional[float] = None
        # The percentage of devices for which storage hardware check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._storage_check_failed_percentage: Optional[float] = None
        # The count of total devices in an organization. Valid values -2147483648 to 2147483647
        self._total_device_count: Optional[int] = None
        # The percentage of devices for which Trusted Platform Module (TPM) hardware check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._tpm_check_failed_percentage: Optional[float] = None
        # The count of devices in an organization eligible for windows upgrade. Valid values -2147483648 to 2147483647
        self._upgrade_eligible_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "os_check_failed_percentage": lambda n : setattr(self, 'os_check_failed_percentage', n.get_float_value()),
            "processor64_bit_check_failed_percentage": lambda n : setattr(self, 'processor64_bit_check_failed_percentage', n.get_float_value()),
            "processor_core_count_check_failed_percentage": lambda n : setattr(self, 'processor_core_count_check_failed_percentage', n.get_float_value()),
            "processor_family_check_failed_percentage": lambda n : setattr(self, 'processor_family_check_failed_percentage', n.get_float_value()),
            "processor_speed_check_failed_percentage": lambda n : setattr(self, 'processor_speed_check_failed_percentage', n.get_float_value()),
            "ram_check_failed_percentage": lambda n : setattr(self, 'ram_check_failed_percentage', n.get_float_value()),
            "secure_boot_check_failed_percentage": lambda n : setattr(self, 'secure_boot_check_failed_percentage', n.get_float_value()),
            "storage_check_failed_percentage": lambda n : setattr(self, 'storage_check_failed_percentage', n.get_float_value()),
            "total_device_count": lambda n : setattr(self, 'total_device_count', n.get_int_value()),
            "tpm_check_failed_percentage": lambda n : setattr(self, 'tpm_check_failed_percentage', n.get_float_value()),
            "upgrade_eligible_device_count": lambda n : setattr(self, 'upgrade_eligible_device_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def os_check_failed_percentage(self,) -> Optional[float]:
        """
        Gets the osCheckFailedPercentage property value. The percentage of devices for which OS check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._os_check_failed_percentage
    
    @os_check_failed_percentage.setter
    def os_check_failed_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the osCheckFailedPercentage property value. The percentage of devices for which OS check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the osCheckFailedPercentage property.
        """
        self._os_check_failed_percentage = value
    
    @property
    def processor64_bit_check_failed_percentage(self,) -> Optional[float]:
        """
        Gets the processor64BitCheckFailedPercentage property value. The percentage of devices for which processor hardware 64-bit architecture check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._processor64_bit_check_failed_percentage
    
    @processor64_bit_check_failed_percentage.setter
    def processor64_bit_check_failed_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the processor64BitCheckFailedPercentage property value. The percentage of devices for which processor hardware 64-bit architecture check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the processor64BitCheckFailedPercentage property.
        """
        self._processor64_bit_check_failed_percentage = value
    
    @property
    def processor_core_count_check_failed_percentage(self,) -> Optional[float]:
        """
        Gets the processorCoreCountCheckFailedPercentage property value. The percentage of devices for which processor hardware core count check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._processor_core_count_check_failed_percentage
    
    @processor_core_count_check_failed_percentage.setter
    def processor_core_count_check_failed_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the processorCoreCountCheckFailedPercentage property value. The percentage of devices for which processor hardware core count check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the processorCoreCountCheckFailedPercentage property.
        """
        self._processor_core_count_check_failed_percentage = value
    
    @property
    def processor_family_check_failed_percentage(self,) -> Optional[float]:
        """
        Gets the processorFamilyCheckFailedPercentage property value. The percentage of devices for which processor hardware family check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._processor_family_check_failed_percentage
    
    @processor_family_check_failed_percentage.setter
    def processor_family_check_failed_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the processorFamilyCheckFailedPercentage property value. The percentage of devices for which processor hardware family check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the processorFamilyCheckFailedPercentage property.
        """
        self._processor_family_check_failed_percentage = value
    
    @property
    def processor_speed_check_failed_percentage(self,) -> Optional[float]:
        """
        Gets the processorSpeedCheckFailedPercentage property value. The percentage of devices for which processor hardware speed check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._processor_speed_check_failed_percentage
    
    @processor_speed_check_failed_percentage.setter
    def processor_speed_check_failed_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the processorSpeedCheckFailedPercentage property value. The percentage of devices for which processor hardware speed check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the processorSpeedCheckFailedPercentage property.
        """
        self._processor_speed_check_failed_percentage = value
    
    @property
    def ram_check_failed_percentage(self,) -> Optional[float]:
        """
        Gets the ramCheckFailedPercentage property value. The percentage of devices for which RAM hardware check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._ram_check_failed_percentage
    
    @ram_check_failed_percentage.setter
    def ram_check_failed_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the ramCheckFailedPercentage property value. The percentage of devices for which RAM hardware check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the ramCheckFailedPercentage property.
        """
        self._ram_check_failed_percentage = value
    
    @property
    def secure_boot_check_failed_percentage(self,) -> Optional[float]:
        """
        Gets the secureBootCheckFailedPercentage property value. The percentage of devices for which secure boot hardware check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._secure_boot_check_failed_percentage
    
    @secure_boot_check_failed_percentage.setter
    def secure_boot_check_failed_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the secureBootCheckFailedPercentage property value. The percentage of devices for which secure boot hardware check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the secureBootCheckFailedPercentage property.
        """
        self._secure_boot_check_failed_percentage = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_float_value("osCheckFailedPercentage", self.os_check_failed_percentage)
        writer.write_float_value("processor64BitCheckFailedPercentage", self.processor64_bit_check_failed_percentage)
        writer.write_float_value("processorCoreCountCheckFailedPercentage", self.processor_core_count_check_failed_percentage)
        writer.write_float_value("processorFamilyCheckFailedPercentage", self.processor_family_check_failed_percentage)
        writer.write_float_value("processorSpeedCheckFailedPercentage", self.processor_speed_check_failed_percentage)
        writer.write_float_value("ramCheckFailedPercentage", self.ram_check_failed_percentage)
        writer.write_float_value("secureBootCheckFailedPercentage", self.secure_boot_check_failed_percentage)
        writer.write_float_value("storageCheckFailedPercentage", self.storage_check_failed_percentage)
        writer.write_int_value("totalDeviceCount", self.total_device_count)
        writer.write_float_value("tpmCheckFailedPercentage", self.tpm_check_failed_percentage)
        writer.write_int_value("upgradeEligibleDeviceCount", self.upgrade_eligible_device_count)
    
    @property
    def storage_check_failed_percentage(self,) -> Optional[float]:
        """
        Gets the storageCheckFailedPercentage property value. The percentage of devices for which storage hardware check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._storage_check_failed_percentage
    
    @storage_check_failed_percentage.setter
    def storage_check_failed_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the storageCheckFailedPercentage property value. The percentage of devices for which storage hardware check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the storageCheckFailedPercentage property.
        """
        self._storage_check_failed_percentage = value
    
    @property
    def total_device_count(self,) -> Optional[int]:
        """
        Gets the totalDeviceCount property value. The count of total devices in an organization. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._total_device_count
    
    @total_device_count.setter
    def total_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalDeviceCount property value. The count of total devices in an organization. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the totalDeviceCount property.
        """
        self._total_device_count = value
    
    @property
    def tpm_check_failed_percentage(self,) -> Optional[float]:
        """
        Gets the tpmCheckFailedPercentage property value. The percentage of devices for which Trusted Platform Module (TPM) hardware check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._tpm_check_failed_percentage
    
    @tpm_check_failed_percentage.setter
    def tpm_check_failed_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the tpmCheckFailedPercentage property value. The percentage of devices for which Trusted Platform Module (TPM) hardware check has failed. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the tpmCheckFailedPercentage property.
        """
        self._tpm_check_failed_percentage = value
    
    @property
    def upgrade_eligible_device_count(self,) -> Optional[int]:
        """
        Gets the upgradeEligibleDeviceCount property value. The count of devices in an organization eligible for windows upgrade. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._upgrade_eligible_device_count
    
    @upgrade_eligible_device_count.setter
    def upgrade_eligible_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the upgradeEligibleDeviceCount property value. The count of devices in an organization eligible for windows upgrade. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the upgradeEligibleDeviceCount property.
        """
        self._upgrade_eligible_device_count = value
    

