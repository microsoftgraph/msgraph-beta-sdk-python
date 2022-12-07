from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsAppHealthApplicationPerformance(entity.Entity):
    """
    The user experience analytics application performance entity contains app performance details.
    """
    @property
    def active_device_count(self,) -> Optional[int]:
        """
        Gets the activeDeviceCount property value. The number of devices where the app has been active. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._active_device_count
    
    @active_device_count.setter
    def active_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the activeDeviceCount property value. The number of devices where the app has been active. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the activeDeviceCount property.
        """
        self._active_device_count = value
    
    @property
    def app_crash_count(self,) -> Optional[int]:
        """
        Gets the appCrashCount property value. The number of crashes for the app. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._app_crash_count
    
    @app_crash_count.setter
    def app_crash_count(self,value: Optional[int] = None) -> None:
        """
        Sets the appCrashCount property value. The number of crashes for the app. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the appCrashCount property.
        """
        self._app_crash_count = value
    
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. The friendly name of the application.
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. The friendly name of the application.
        Args:
            value: Value to set for the appDisplayName property.
        """
        self._app_display_name = value
    
    @property
    def app_hang_count(self,) -> Optional[int]:
        """
        Gets the appHangCount property value. The number of hangs for the app. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._app_hang_count
    
    @app_hang_count.setter
    def app_hang_count(self,value: Optional[int] = None) -> None:
        """
        Sets the appHangCount property value. The number of hangs for the app. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the appHangCount property.
        """
        self._app_hang_count = value
    
    @property
    def app_health_score(self,) -> Optional[float]:
        """
        Gets the appHealthScore property value. The health score of the app. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._app_health_score
    
    @app_health_score.setter
    def app_health_score(self,value: Optional[float] = None) -> None:
        """
        Sets the appHealthScore property value. The health score of the app. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the appHealthScore property.
        """
        self._app_health_score = value
    
    @property
    def app_health_status(self,) -> Optional[str]:
        """
        Gets the appHealthStatus property value. The overall health status of the app.
        Returns: Optional[str]
        """
        return self._app_health_status
    
    @app_health_status.setter
    def app_health_status(self,value: Optional[str] = None) -> None:
        """
        Sets the appHealthStatus property value. The overall health status of the app.
        Args:
            value: Value to set for the appHealthStatus property.
        """
        self._app_health_status = value
    
    @property
    def app_name(self,) -> Optional[str]:
        """
        Gets the appName property value. The name of the application.
        Returns: Optional[str]
        """
        return self._app_name
    
    @app_name.setter
    def app_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appName property value. The name of the application.
        Args:
            value: Value to set for the appName property.
        """
        self._app_name = value
    
    @property
    def app_publisher(self,) -> Optional[str]:
        """
        Gets the appPublisher property value. The publisher of the application.
        Returns: Optional[str]
        """
        return self._app_publisher
    
    @app_publisher.setter
    def app_publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the appPublisher property value. The publisher of the application.
        Args:
            value: Value to set for the appPublisher property.
        """
        self._app_publisher = value
    
    @property
    def app_usage_duration(self,) -> Optional[int]:
        """
        Gets the appUsageDuration property value. The total usage time of the application in minutes. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._app_usage_duration
    
    @app_usage_duration.setter
    def app_usage_duration(self,value: Optional[int] = None) -> None:
        """
        Sets the appUsageDuration property value. The total usage time of the application in minutes. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the appUsageDuration property.
        """
        self._app_usage_duration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsAppHealthApplicationPerformance and sets the default values.
        """
        super().__init__()
        # The number of devices where the app has been active. Valid values -2147483648 to 2147483647
        self._active_device_count: Optional[int] = None
        # The number of crashes for the app. Valid values -2147483648 to 2147483647
        self._app_crash_count: Optional[int] = None
        # The friendly name of the application.
        self._app_display_name: Optional[str] = None
        # The number of hangs for the app. Valid values -2147483648 to 2147483647
        self._app_hang_count: Optional[int] = None
        # The health score of the app. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._app_health_score: Optional[float] = None
        # The overall health status of the app.
        self._app_health_status: Optional[str] = None
        # The name of the application.
        self._app_name: Optional[str] = None
        # The publisher of the application.
        self._app_publisher: Optional[str] = None
        # The total usage time of the application in minutes. Valid values -2147483648 to 2147483647
        self._app_usage_duration: Optional[int] = None
        # The mean time to failure for the app in minutes. Valid values -2147483648 to 2147483647
        self._mean_time_to_failure_in_minutes: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsAppHealthApplicationPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAppHealthApplicationPerformance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsAppHealthApplicationPerformance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_device_count": lambda n : setattr(self, 'active_device_count', n.get_int_value()),
            "app_crash_count": lambda n : setattr(self, 'app_crash_count', n.get_int_value()),
            "app_display_name": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "app_hang_count": lambda n : setattr(self, 'app_hang_count', n.get_int_value()),
            "app_health_score": lambda n : setattr(self, 'app_health_score', n.get_float_value()),
            "app_health_status": lambda n : setattr(self, 'app_health_status', n.get_str_value()),
            "app_name": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "app_publisher": lambda n : setattr(self, 'app_publisher', n.get_str_value()),
            "app_usage_duration": lambda n : setattr(self, 'app_usage_duration', n.get_int_value()),
            "mean_time_to_failure_in_minutes": lambda n : setattr(self, 'mean_time_to_failure_in_minutes', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def mean_time_to_failure_in_minutes(self,) -> Optional[int]:
        """
        Gets the meanTimeToFailureInMinutes property value. The mean time to failure for the app in minutes. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._mean_time_to_failure_in_minutes
    
    @mean_time_to_failure_in_minutes.setter
    def mean_time_to_failure_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the meanTimeToFailureInMinutes property value. The mean time to failure for the app in minutes. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the meanTimeToFailureInMinutes property.
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
        writer.write_int_value("activeDeviceCount", self.active_device_count)
        writer.write_int_value("appCrashCount", self.app_crash_count)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_int_value("appHangCount", self.app_hang_count)
        writer.write_float_value("appHealthScore", self.app_health_score)
        writer.write_str_value("appHealthStatus", self.app_health_status)
        writer.write_str_value("appName", self.app_name)
        writer.write_str_value("appPublisher", self.app_publisher)
        writer.write_int_value("appUsageDuration", self.app_usage_duration)
        writer.write_int_value("meanTimeToFailureInMinutes", self.mean_time_to_failure_in_minutes)
    

