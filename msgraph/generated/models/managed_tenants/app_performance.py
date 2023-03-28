from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .. import entity

from .. import entity

class AppPerformance(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new appPerformance and sets the default values.
        """
        super().__init__()
        # The appFriendlyName property
        self._app_friendly_name: Optional[str] = None
        # The appName property
        self._app_name: Optional[str] = None
        # The appPublisher property
        self._app_publisher: Optional[str] = None
        # The lastUpdatedDateTime property
        self._last_updated_date_time: Optional[datetime] = None
        # The meanTimeToFailureInMinutes property
        self._mean_time_to_failure_in_minutes: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The tenantDisplayName property
        self._tenant_display_name: Optional[str] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
        # The totalActiveDeviceCount property
        self._total_active_device_count: Optional[int] = None
        # The totalAppCrashCount property
        self._total_app_crash_count: Optional[int] = None
        # The totalAppFreezeCount property
        self._total_app_freeze_count: Optional[int] = None
    
    @property
    def app_friendly_name(self,) -> Optional[str]:
        """
        Gets the appFriendlyName property value. The appFriendlyName property
        Returns: Optional[str]
        """
        return self._app_friendly_name
    
    @app_friendly_name.setter
    def app_friendly_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appFriendlyName property value. The appFriendlyName property
        Args:
            value: Value to set for the app_friendly_name property.
        """
        self._app_friendly_name = value
    
    @property
    def app_name(self,) -> Optional[str]:
        """
        Gets the appName property value. The appName property
        Returns: Optional[str]
        """
        return self._app_name
    
    @app_name.setter
    def app_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appName property value. The appName property
        Args:
            value: Value to set for the app_name property.
        """
        self._app_name = value
    
    @property
    def app_publisher(self,) -> Optional[str]:
        """
        Gets the appPublisher property value. The appPublisher property
        Returns: Optional[str]
        """
        return self._app_publisher
    
    @app_publisher.setter
    def app_publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the appPublisher property value. The appPublisher property
        Args:
            value: Value to set for the app_publisher property.
        """
        self._app_publisher = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppPerformance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppPerformance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "appFriendlyName": lambda n : setattr(self, 'app_friendly_name', n.get_str_value()),
            "appName": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "appPublisher": lambda n : setattr(self, 'app_publisher', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "meanTimeToFailureInMinutes": lambda n : setattr(self, 'mean_time_to_failure_in_minutes', n.get_int_value()),
            "tenantDisplayName": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "totalActiveDeviceCount": lambda n : setattr(self, 'total_active_device_count', n.get_int_value()),
            "totalAppCrashCount": lambda n : setattr(self, 'total_app_crash_count', n.get_int_value()),
            "totalAppFreezeCount": lambda n : setattr(self, 'total_app_freeze_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    def mean_time_to_failure_in_minutes(self,) -> Optional[int]:
        """
        Gets the meanTimeToFailureInMinutes property value. The meanTimeToFailureInMinutes property
        Returns: Optional[int]
        """
        return self._mean_time_to_failure_in_minutes
    
    @mean_time_to_failure_in_minutes.setter
    def mean_time_to_failure_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the meanTimeToFailureInMinutes property value. The meanTimeToFailureInMinutes property
        Args:
            value: Value to set for the mean_time_to_failure_in_minutes property.
        """
        self._mean_time_to_failure_in_minutes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appFriendlyName", self.app_friendly_name)
        writer.write_str_value("appName", self.app_name)
        writer.write_str_value("appPublisher", self.app_publisher)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_int_value("meanTimeToFailureInMinutes", self.mean_time_to_failure_in_minutes)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_int_value("totalActiveDeviceCount", self.total_active_device_count)
        writer.write_int_value("totalAppCrashCount", self.total_app_crash_count)
        writer.write_int_value("totalAppFreezeCount", self.total_app_freeze_count)
    
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
    def total_active_device_count(self,) -> Optional[int]:
        """
        Gets the totalActiveDeviceCount property value. The totalActiveDeviceCount property
        Returns: Optional[int]
        """
        return self._total_active_device_count
    
    @total_active_device_count.setter
    def total_active_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalActiveDeviceCount property value. The totalActiveDeviceCount property
        Args:
            value: Value to set for the total_active_device_count property.
        """
        self._total_active_device_count = value
    
    @property
    def total_app_crash_count(self,) -> Optional[int]:
        """
        Gets the totalAppCrashCount property value. The totalAppCrashCount property
        Returns: Optional[int]
        """
        return self._total_app_crash_count
    
    @total_app_crash_count.setter
    def total_app_crash_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalAppCrashCount property value. The totalAppCrashCount property
        Args:
            value: Value to set for the total_app_crash_count property.
        """
        self._total_app_crash_count = value
    
    @property
    def total_app_freeze_count(self,) -> Optional[int]:
        """
        Gets the totalAppFreezeCount property value. The totalAppFreezeCount property
        Returns: Optional[int]
        """
        return self._total_app_freeze_count
    
    @total_app_freeze_count.setter
    def total_app_freeze_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalAppFreezeCount property value. The totalAppFreezeCount property
        Args:
            value: Value to set for the total_app_freeze_count property.
        """
        self._total_app_freeze_count = value
    

