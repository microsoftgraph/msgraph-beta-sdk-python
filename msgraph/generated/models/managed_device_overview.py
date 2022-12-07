from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_exchange_access_state_summary = lazy_import('msgraph.generated.models.device_exchange_access_state_summary')
device_operating_system_summary = lazy_import('msgraph.generated.models.device_operating_system_summary')
entity = lazy_import('msgraph.generated.models.entity')
managed_device_models_and_manufacturers = lazy_import('msgraph.generated.models.managed_device_models_and_manufacturers')

class ManagedDeviceOverview(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new managedDeviceOverview and sets the default values.
        """
        super().__init__()
        # Distribution of Exchange Access State in Intune
        self._device_exchange_access_state_summary: Optional[device_exchange_access_state_summary.DeviceExchangeAccessStateSummary] = None
        # Device operating system summary.
        self._device_operating_system_summary: Optional[device_operating_system_summary.DeviceOperatingSystemSummary] = None
        # The number of devices enrolled in both MDM and EAS
        self._dual_enrolled_device_count: Optional[int] = None
        # Total enrolled device count. Does not include PC devices managed via Intune PC Agent
        self._enrolled_device_count: Optional[int] = None
        # Last modified date time of device overview
        self._last_modified_date_time: Optional[datetime] = None
        # Models and Manufactures meatadata for managed devices in the account
        self._managed_device_models_and_manufacturers: Optional[managed_device_models_and_manufacturers.ManagedDeviceModelsAndManufacturers] = None
        # The number of devices enrolled in MDM
        self._mdm_enrolled_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceOverview
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDeviceOverview()
    
    @property
    def device_exchange_access_state_summary(self,) -> Optional[device_exchange_access_state_summary.DeviceExchangeAccessStateSummary]:
        """
        Gets the deviceExchangeAccessStateSummary property value. Distribution of Exchange Access State in Intune
        Returns: Optional[device_exchange_access_state_summary.DeviceExchangeAccessStateSummary]
        """
        return self._device_exchange_access_state_summary
    
    @device_exchange_access_state_summary.setter
    def device_exchange_access_state_summary(self,value: Optional[device_exchange_access_state_summary.DeviceExchangeAccessStateSummary] = None) -> None:
        """
        Sets the deviceExchangeAccessStateSummary property value. Distribution of Exchange Access State in Intune
        Args:
            value: Value to set for the deviceExchangeAccessStateSummary property.
        """
        self._device_exchange_access_state_summary = value
    
    @property
    def device_operating_system_summary(self,) -> Optional[device_operating_system_summary.DeviceOperatingSystemSummary]:
        """
        Gets the deviceOperatingSystemSummary property value. Device operating system summary.
        Returns: Optional[device_operating_system_summary.DeviceOperatingSystemSummary]
        """
        return self._device_operating_system_summary
    
    @device_operating_system_summary.setter
    def device_operating_system_summary(self,value: Optional[device_operating_system_summary.DeviceOperatingSystemSummary] = None) -> None:
        """
        Sets the deviceOperatingSystemSummary property value. Device operating system summary.
        Args:
            value: Value to set for the deviceOperatingSystemSummary property.
        """
        self._device_operating_system_summary = value
    
    @property
    def dual_enrolled_device_count(self,) -> Optional[int]:
        """
        Gets the dualEnrolledDeviceCount property value. The number of devices enrolled in both MDM and EAS
        Returns: Optional[int]
        """
        return self._dual_enrolled_device_count
    
    @dual_enrolled_device_count.setter
    def dual_enrolled_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the dualEnrolledDeviceCount property value. The number of devices enrolled in both MDM and EAS
        Args:
            value: Value to set for the dualEnrolledDeviceCount property.
        """
        self._dual_enrolled_device_count = value
    
    @property
    def enrolled_device_count(self,) -> Optional[int]:
        """
        Gets the enrolledDeviceCount property value. Total enrolled device count. Does not include PC devices managed via Intune PC Agent
        Returns: Optional[int]
        """
        return self._enrolled_device_count
    
    @enrolled_device_count.setter
    def enrolled_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the enrolledDeviceCount property value. Total enrolled device count. Does not include PC devices managed via Intune PC Agent
        Args:
            value: Value to set for the enrolledDeviceCount property.
        """
        self._enrolled_device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_exchange_access_state_summary": lambda n : setattr(self, 'device_exchange_access_state_summary', n.get_object_value(device_exchange_access_state_summary.DeviceExchangeAccessStateSummary)),
            "device_operating_system_summary": lambda n : setattr(self, 'device_operating_system_summary', n.get_object_value(device_operating_system_summary.DeviceOperatingSystemSummary)),
            "dual_enrolled_device_count": lambda n : setattr(self, 'dual_enrolled_device_count', n.get_int_value()),
            "enrolled_device_count": lambda n : setattr(self, 'enrolled_device_count', n.get_int_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "managed_device_models_and_manufacturers": lambda n : setattr(self, 'managed_device_models_and_manufacturers', n.get_object_value(managed_device_models_and_manufacturers.ManagedDeviceModelsAndManufacturers)),
            "mdm_enrolled_count": lambda n : setattr(self, 'mdm_enrolled_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Last modified date time of device overview
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Last modified date time of device overview
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def managed_device_models_and_manufacturers(self,) -> Optional[managed_device_models_and_manufacturers.ManagedDeviceModelsAndManufacturers]:
        """
        Gets the managedDeviceModelsAndManufacturers property value. Models and Manufactures meatadata for managed devices in the account
        Returns: Optional[managed_device_models_and_manufacturers.ManagedDeviceModelsAndManufacturers]
        """
        return self._managed_device_models_and_manufacturers
    
    @managed_device_models_and_manufacturers.setter
    def managed_device_models_and_manufacturers(self,value: Optional[managed_device_models_and_manufacturers.ManagedDeviceModelsAndManufacturers] = None) -> None:
        """
        Sets the managedDeviceModelsAndManufacturers property value. Models and Manufactures meatadata for managed devices in the account
        Args:
            value: Value to set for the managedDeviceModelsAndManufacturers property.
        """
        self._managed_device_models_and_manufacturers = value
    
    @property
    def mdm_enrolled_count(self,) -> Optional[int]:
        """
        Gets the mdmEnrolledCount property value. The number of devices enrolled in MDM
        Returns: Optional[int]
        """
        return self._mdm_enrolled_count
    
    @mdm_enrolled_count.setter
    def mdm_enrolled_count(self,value: Optional[int] = None) -> None:
        """
        Sets the mdmEnrolledCount property value. The number of devices enrolled in MDM
        Args:
            value: Value to set for the mdmEnrolledCount property.
        """
        self._mdm_enrolled_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("deviceExchangeAccessStateSummary", self.device_exchange_access_state_summary)
        writer.write_object_value("deviceOperatingSystemSummary", self.device_operating_system_summary)
        writer.write_int_value("dualEnrolledDeviceCount", self.dual_enrolled_device_count)
        writer.write_int_value("enrolledDeviceCount", self.enrolled_device_count)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("managedDeviceModelsAndManufacturers", self.managed_device_models_and_manufacturers)
        writer.write_int_value("mdmEnrolledCount", self.mdm_enrolled_count)
    

