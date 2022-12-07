from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user_experience_analytics_health_state = lazy_import('msgraph.generated.models.user_experience_analytics_health_state')

class UserExperienceAnalyticsAppHealthDevicePerformance(entity.Entity):
    """
    The user experience analytics device performance entity contains device performance details.
    """
    @property
    def app_crash_count(self,) -> Optional[int]:
        """
        Gets the appCrashCount property value. The number of app crashes for the device. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._app_crash_count
    
    @app_crash_count.setter
    def app_crash_count(self,value: Optional[int] = None) -> None:
        """
        Sets the appCrashCount property value. The number of app crashes for the device. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the appCrashCount property.
        """
        self._app_crash_count = value
    
    @property
    def app_hang_count(self,) -> Optional[int]:
        """
        Gets the appHangCount property value. The number of app hangs for the device. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._app_hang_count
    
    @app_hang_count.setter
    def app_hang_count(self,value: Optional[int] = None) -> None:
        """
        Sets the appHangCount property value. The number of app hangs for the device. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the appHangCount property.
        """
        self._app_hang_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsAppHealthDevicePerformance and sets the default values.
        """
        super().__init__()
        # The number of app crashes for the device. Valid values -2147483648 to 2147483647
        self._app_crash_count: Optional[int] = None
        # The number of app hangs for the device. Valid values -2147483648 to 2147483647
        self._app_hang_count: Optional[int] = None
        # The number of distinct app crashes for the device. Valid values -2147483648 to 2147483647
        self._crashed_app_count: Optional[int] = None
        # The app health score of the device. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._device_app_health_score: Optional[float] = None
        # The overall app health status of the device.
        self._device_app_health_status: Optional[str] = None
        # The name of the device.
        self._device_display_name: Optional[str] = None
        # The id of the device.
        self._device_id: Optional[str] = None
        # The manufacturer name of the device.
        self._device_manufacturer: Optional[str] = None
        # The model name of the device.
        self._device_model: Optional[str] = None
        # The healthStatus property
        self._health_status: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None
        # The mean time to failure for the device in minutes. Valid values -2147483648 to 2147483647
        self._mean_time_to_failure_in_minutes: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The date and time when the statistics were last computed.
        self._processed_date_time: Optional[datetime] = None
    
    @property
    def crashed_app_count(self,) -> Optional[int]:
        """
        Gets the crashedAppCount property value. The number of distinct app crashes for the device. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._crashed_app_count
    
    @crashed_app_count.setter
    def crashed_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the crashedAppCount property value. The number of distinct app crashes for the device. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the crashedAppCount property.
        """
        self._crashed_app_count = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsAppHealthDevicePerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAppHealthDevicePerformance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsAppHealthDevicePerformance()
    
    @property
    def device_app_health_score(self,) -> Optional[float]:
        """
        Gets the deviceAppHealthScore property value. The app health score of the device. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._device_app_health_score
    
    @device_app_health_score.setter
    def device_app_health_score(self,value: Optional[float] = None) -> None:
        """
        Sets the deviceAppHealthScore property value. The app health score of the device. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the deviceAppHealthScore property.
        """
        self._device_app_health_score = value
    
    @property
    def device_app_health_status(self,) -> Optional[str]:
        """
        Gets the deviceAppHealthStatus property value. The overall app health status of the device.
        Returns: Optional[str]
        """
        return self._device_app_health_status
    
    @device_app_health_status.setter
    def device_app_health_status(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceAppHealthStatus property value. The overall app health status of the device.
        Args:
            value: Value to set for the deviceAppHealthStatus property.
        """
        self._device_app_health_status = value
    
    @property
    def device_display_name(self,) -> Optional[str]:
        """
        Gets the deviceDisplayName property value. The name of the device.
        Returns: Optional[str]
        """
        return self._device_display_name
    
    @device_display_name.setter
    def device_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceDisplayName property value. The name of the device.
        Args:
            value: Value to set for the deviceDisplayName property.
        """
        self._device_display_name = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The id of the device.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The id of the device.
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_crash_count": lambda n : setattr(self, 'app_crash_count', n.get_int_value()),
            "app_hang_count": lambda n : setattr(self, 'app_hang_count', n.get_int_value()),
            "crashed_app_count": lambda n : setattr(self, 'crashed_app_count', n.get_int_value()),
            "device_app_health_score": lambda n : setattr(self, 'device_app_health_score', n.get_float_value()),
            "device_app_health_status": lambda n : setattr(self, 'device_app_health_status', n.get_str_value()),
            "device_display_name": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_manufacturer": lambda n : setattr(self, 'device_manufacturer', n.get_str_value()),
            "device_model": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "health_status": lambda n : setattr(self, 'health_status', n.get_enum_value(user_experience_analytics_health_state.UserExperienceAnalyticsHealthState)),
            "mean_time_to_failure_in_minutes": lambda n : setattr(self, 'mean_time_to_failure_in_minutes', n.get_int_value()),
            "processed_date_time": lambda n : setattr(self, 'processed_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def health_status(self,) -> Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState]:
        """
        Gets the healthStatus property value. The healthStatus property
        Returns: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState]
        """
        return self._health_status
    
    @health_status.setter
    def health_status(self,value: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None) -> None:
        """
        Sets the healthStatus property value. The healthStatus property
        Args:
            value: Value to set for the healthStatus property.
        """
        self._health_status = value
    
    @property
    def mean_time_to_failure_in_minutes(self,) -> Optional[int]:
        """
        Gets the meanTimeToFailureInMinutes property value. The mean time to failure for the device in minutes. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._mean_time_to_failure_in_minutes
    
    @mean_time_to_failure_in_minutes.setter
    def mean_time_to_failure_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the meanTimeToFailureInMinutes property value. The mean time to failure for the device in minutes. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the meanTimeToFailureInMinutes property.
        """
        self._mean_time_to_failure_in_minutes = value
    
    @property
    def processed_date_time(self,) -> Optional[datetime]:
        """
        Gets the processedDateTime property value. The date and time when the statistics were last computed.
        Returns: Optional[datetime]
        """
        return self._processed_date_time
    
    @processed_date_time.setter
    def processed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the processedDateTime property value. The date and time when the statistics were last computed.
        Args:
            value: Value to set for the processedDateTime property.
        """
        self._processed_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("appCrashCount", self.app_crash_count)
        writer.write_int_value("appHangCount", self.app_hang_count)
        writer.write_int_value("crashedAppCount", self.crashed_app_count)
        writer.write_float_value("deviceAppHealthScore", self.device_app_health_score)
        writer.write_str_value("deviceAppHealthStatus", self.device_app_health_status)
        writer.write_str_value("deviceDisplayName", self.device_display_name)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceManufacturer", self.device_manufacturer)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_int_value("meanTimeToFailureInMinutes", self.mean_time_to_failure_in_minutes)
        writer.write_datetime_value("processedDateTime", self.processed_date_time)
    

