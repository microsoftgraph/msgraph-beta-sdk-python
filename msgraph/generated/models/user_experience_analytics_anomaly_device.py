from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsAnomalyDevice(entity.Entity):
    """
    The user experience analytics anomaly entity contains device details.
    """
    @property
    def anomaly_id(self,) -> Optional[str]:
        """
        Gets the anomalyId property value. The unique identifier of the anomaly.
        Returns: Optional[str]
        """
        return self._anomaly_id
    
    @anomaly_id.setter
    def anomaly_id(self,value: Optional[str] = None) -> None:
        """
        Sets the anomalyId property value. The unique identifier of the anomaly.
        Args:
            value: Value to set for the anomalyId property.
        """
        self._anomaly_id = value
    
    @property
    def anomaly_on_device_first_occurrence_date_time(self,) -> Optional[datetime]:
        """
        Gets the anomalyOnDeviceFirstOccurrenceDateTime property value. Indicates the first occurance date and time for the anomaly on the device.
        Returns: Optional[datetime]
        """
        return self._anomaly_on_device_first_occurrence_date_time
    
    @anomaly_on_device_first_occurrence_date_time.setter
    def anomaly_on_device_first_occurrence_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the anomalyOnDeviceFirstOccurrenceDateTime property value. Indicates the first occurance date and time for the anomaly on the device.
        Args:
            value: Value to set for the anomalyOnDeviceFirstOccurrenceDateTime property.
        """
        self._anomaly_on_device_first_occurrence_date_time = value
    
    @property
    def anomaly_on_device_latest_occurrence_date_time(self,) -> Optional[datetime]:
        """
        Gets the anomalyOnDeviceLatestOccurrenceDateTime property value. Indicates the latest occurance date and time for the anomaly on the device.
        Returns: Optional[datetime]
        """
        return self._anomaly_on_device_latest_occurrence_date_time
    
    @anomaly_on_device_latest_occurrence_date_time.setter
    def anomaly_on_device_latest_occurrence_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the anomalyOnDeviceLatestOccurrenceDateTime property value. Indicates the latest occurance date and time for the anomaly on the device.
        Args:
            value: Value to set for the anomalyOnDeviceLatestOccurrenceDateTime property.
        """
        self._anomaly_on_device_latest_occurrence_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsAnomalyDevice and sets the default values.
        """
        super().__init__()
        # The unique identifier of the anomaly.
        self._anomaly_id: Optional[str] = None
        # Indicates the first occurance date and time for the anomaly on the device.
        self._anomaly_on_device_first_occurrence_date_time: Optional[datetime] = None
        # Indicates the latest occurance date and time for the anomaly on the device.
        self._anomaly_on_device_latest_occurrence_date_time: Optional[datetime] = None
        # The unique identifier of the device.
        self._device_id: Optional[str] = None
        # The manufacturer name of the device.
        self._device_manufacturer: Optional[str] = None
        # The model name of the device.
        self._device_model: Optional[str] = None
        # The name of the device.
        self._device_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The name of the OS installed on the device.
        self._os_name: Optional[str] = None
        # The OS version installed on the device.
        self._os_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsAnomalyDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAnomalyDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsAnomalyDevice()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The unique identifier of the device.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The unique identifier of the device.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_manufacturer(self,) -> Optional[str]:
        """
        Gets the deviceManufacturer property value. The manufacturer name of the device.
        Returns: Optional[str]
        """
        return self._device_manufacturer
    
    @device_manufacturer.setter
    def device_manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceManufacturer property value. The manufacturer name of the device.
        Args:
            value: Value to set for the deviceManufacturer property.
        """
        self._device_manufacturer = value
    
    @property
    def device_model(self,) -> Optional[str]:
        """
        Gets the deviceModel property value. The model name of the device.
        Returns: Optional[str]
        """
        return self._device_model
    
    @device_model.setter
    def device_model(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceModel property value. The model name of the device.
        Args:
            value: Value to set for the deviceModel property.
        """
        self._device_model = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The name of the device.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The name of the device.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "anomaly_id": lambda n : setattr(self, 'anomaly_id', n.get_str_value()),
            "anomaly_on_device_first_occurrence_date_time": lambda n : setattr(self, 'anomaly_on_device_first_occurrence_date_time', n.get_datetime_value()),
            "anomaly_on_device_latest_occurrence_date_time": lambda n : setattr(self, 'anomaly_on_device_latest_occurrence_date_time', n.get_datetime_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_manufacturer": lambda n : setattr(self, 'device_manufacturer', n.get_str_value()),
            "device_model": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "os_name": lambda n : setattr(self, 'os_name', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def os_name(self,) -> Optional[str]:
        """
        Gets the osName property value. The name of the OS installed on the device.
        Returns: Optional[str]
        """
        return self._os_name
    
    @os_name.setter
    def os_name(self,value: Optional[str] = None) -> None:
        """
        Sets the osName property value. The name of the OS installed on the device.
        Args:
            value: Value to set for the osName property.
        """
        self._os_name = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. The OS version installed on the device.
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. The OS version installed on the device.
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("anomalyId", self.anomaly_id)
        writer.write_datetime_value("anomalyOnDeviceFirstOccurrenceDateTime", self.anomaly_on_device_first_occurrence_date_time)
        writer.write_datetime_value("anomalyOnDeviceLatestOccurrenceDateTime", self.anomaly_on_device_latest_occurrence_date_time)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceManufacturer", self.device_manufacturer)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("osName", self.os_name)
        writer.write_str_value("osVersion", self.os_version)
    

