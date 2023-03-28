from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .. import entity

from .. import entity

class DeviceHealthStatus(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new deviceHealthStatus and sets the default values.
        """
        super().__init__()
        # The blueScreenCount property
        self._blue_screen_count: Optional[int] = None
        # The bootTotalDurationInSeconds property
        self._boot_total_duration_in_seconds: Optional[float] = None
        # The deviceId property
        self._device_id: Optional[str] = None
        # The deviceMake property
        self._device_make: Optional[str] = None
        # The deviceModel property
        self._device_model: Optional[str] = None
        # The deviceName property
        self._device_name: Optional[str] = None
        # The healthStatus property
        self._health_status: Optional[str] = None
        # The lastUpdatedDateTime property
        self._last_updated_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The osVersion property
        self._os_version: Optional[str] = None
        # The primaryDiskType property
        self._primary_disk_type: Optional[str] = None
        # The restartCount property
        self._restart_count: Optional[int] = None
        # The startupPerformanceScore property
        self._startup_performance_score: Optional[float] = None
        # The tenantDisplayName property
        self._tenant_display_name: Optional[str] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
        # The topProcesses property
        self._top_processes: Optional[str] = None
    
    @property
    def blue_screen_count(self,) -> Optional[int]:
        """
        Gets the blueScreenCount property value. The blueScreenCount property
        Returns: Optional[int]
        """
        return self._blue_screen_count
    
    @blue_screen_count.setter
    def blue_screen_count(self,value: Optional[int] = None) -> None:
        """
        Sets the blueScreenCount property value. The blueScreenCount property
        Args:
            value: Value to set for the blue_screen_count property.
        """
        self._blue_screen_count = value
    
    @property
    def boot_total_duration_in_seconds(self,) -> Optional[float]:
        """
        Gets the bootTotalDurationInSeconds property value. The bootTotalDurationInSeconds property
        Returns: Optional[float]
        """
        return self._boot_total_duration_in_seconds
    
    @boot_total_duration_in_seconds.setter
    def boot_total_duration_in_seconds(self,value: Optional[float] = None) -> None:
        """
        Sets the bootTotalDurationInSeconds property value. The bootTotalDurationInSeconds property
        Args:
            value: Value to set for the boot_total_duration_in_seconds property.
        """
        self._boot_total_duration_in_seconds = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceHealthStatus()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The deviceId property
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The deviceId property
        Args:
            value: Value to set for the device_id property.
        """
        self._device_id = value
    
    @property
    def device_make(self,) -> Optional[str]:
        """
        Gets the deviceMake property value. The deviceMake property
        Returns: Optional[str]
        """
        return self._device_make
    
    @device_make.setter
    def device_make(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceMake property value. The deviceMake property
        Args:
            value: Value to set for the device_make property.
        """
        self._device_make = value
    
    @property
    def device_model(self,) -> Optional[str]:
        """
        Gets the deviceModel property value. The deviceModel property
        Returns: Optional[str]
        """
        return self._device_model
    
    @device_model.setter
    def device_model(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceModel property value. The deviceModel property
        Args:
            value: Value to set for the device_model property.
        """
        self._device_model = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The deviceName property
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The deviceName property
        Args:
            value: Value to set for the device_name property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "blueScreenCount": lambda n : setattr(self, 'blue_screen_count', n.get_int_value()),
            "bootTotalDurationInSeconds": lambda n : setattr(self, 'boot_total_duration_in_seconds', n.get_float_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceMake": lambda n : setattr(self, 'device_make', n.get_str_value()),
            "deviceModel": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "primaryDiskType": lambda n : setattr(self, 'primary_disk_type', n.get_str_value()),
            "restartCount": lambda n : setattr(self, 'restart_count', n.get_int_value()),
            "startupPerformanceScore": lambda n : setattr(self, 'startup_performance_score', n.get_float_value()),
            "tenantDisplayName": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "topProcesses": lambda n : setattr(self, 'top_processes', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def health_status(self,) -> Optional[str]:
        """
        Gets the healthStatus property value. The healthStatus property
        Returns: Optional[str]
        """
        return self._health_status
    
    @health_status.setter
    def health_status(self,value: Optional[str] = None) -> None:
        """
        Sets the healthStatus property value. The healthStatus property
        Args:
            value: Value to set for the health_status property.
        """
        self._health_status = value
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. The lastUpdatedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. The lastUpdatedDateTime property
        Args:
            value: Value to set for the last_updated_date_time property.
        """
        self._last_updated_date_time = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. The osVersion property
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. The osVersion property
        Args:
            value: Value to set for the os_version property.
        """
        self._os_version = value
    
    @property
    def primary_disk_type(self,) -> Optional[str]:
        """
        Gets the primaryDiskType property value. The primaryDiskType property
        Returns: Optional[str]
        """
        return self._primary_disk_type
    
    @primary_disk_type.setter
    def primary_disk_type(self,value: Optional[str] = None) -> None:
        """
        Sets the primaryDiskType property value. The primaryDiskType property
        Args:
            value: Value to set for the primary_disk_type property.
        """
        self._primary_disk_type = value
    
    @property
    def restart_count(self,) -> Optional[int]:
        """
        Gets the restartCount property value. The restartCount property
        Returns: Optional[int]
        """
        return self._restart_count
    
    @restart_count.setter
    def restart_count(self,value: Optional[int] = None) -> None:
        """
        Sets the restartCount property value. The restartCount property
        Args:
            value: Value to set for the restart_count property.
        """
        self._restart_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("blueScreenCount", self.blue_screen_count)
        writer.write_float_value("bootTotalDurationInSeconds", self.boot_total_duration_in_seconds)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceMake", self.device_make)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("healthStatus", self.health_status)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("primaryDiskType", self.primary_disk_type)
        writer.write_int_value("restartCount", self.restart_count)
        writer.write_float_value("startupPerformanceScore", self.startup_performance_score)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("topProcesses", self.top_processes)
    
    @property
    def startup_performance_score(self,) -> Optional[float]:
        """
        Gets the startupPerformanceScore property value. The startupPerformanceScore property
        Returns: Optional[float]
        """
        return self._startup_performance_score
    
    @startup_performance_score.setter
    def startup_performance_score(self,value: Optional[float] = None) -> None:
        """
        Sets the startupPerformanceScore property value. The startupPerformanceScore property
        Args:
            value: Value to set for the startup_performance_score property.
        """
        self._startup_performance_score = value
    
    @property
    def tenant_display_name(self,) -> Optional[str]:
        """
        Gets the tenantDisplayName property value. The tenantDisplayName property
        Returns: Optional[str]
        """
        return self._tenant_display_name
    
    @tenant_display_name.setter
    def tenant_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantDisplayName property value. The tenantDisplayName property
        Args:
            value: Value to set for the tenant_display_name property.
        """
        self._tenant_display_name = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    
    @property
    def top_processes(self,) -> Optional[str]:
        """
        Gets the topProcesses property value. The topProcesses property
        Returns: Optional[str]
        """
        return self._top_processes
    
    @top_processes.setter
    def top_processes(self,value: Optional[str] = None) -> None:
        """
        Sets the topProcesses property value. The topProcesses property
        Args:
            value: Value to set for the top_processes property.
        """
        self._top_processes = value
    

