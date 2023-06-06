from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, user_experience_analytics_health_state

from . import entity

@dataclass
class UserExperienceAnalyticsAppHealthDevicePerformance(entity.Entity):
    """
    The user experience analytics device performance entity contains device performance details.
    """
    # The number of app crashes for the device. Valid values -2147483648 to 2147483647
    app_crash_count: Optional[int] = None
    # The number of app hangs for the device. Valid values -2147483648 to 2147483647
    app_hang_count: Optional[int] = None
    # The number of distinct app crashes for the device. Valid values -2147483648 to 2147483647
    crashed_app_count: Optional[int] = None
    # The app health score of the device. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    device_app_health_score: Optional[float] = None
    # The overall app health status of the device.
    device_app_health_status: Optional[str] = None
    # The name of the device.
    device_display_name: Optional[str] = None
    # The id of the device.
    device_id: Optional[str] = None
    # The manufacturer name of the device.
    device_manufacturer: Optional[str] = None
    # The model name of the device.
    device_model: Optional[str] = None
    # The healthStatus property
    health_status: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None
    # The mean time to failure for the device in minutes. Valid values -2147483648 to 2147483647
    mean_time_to_failure_in_minutes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the statistics were last computed.
    processed_date_time: Optional[datetime] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, user_experience_analytics_health_state

        fields: Dict[str, Callable[[Any], None]] = {
            "appCrashCount": lambda n : setattr(self, 'app_crash_count', n.get_int_value()),
            "appHangCount": lambda n : setattr(self, 'app_hang_count', n.get_int_value()),
            "crashedAppCount": lambda n : setattr(self, 'crashed_app_count', n.get_int_value()),
            "deviceAppHealthScore": lambda n : setattr(self, 'device_app_health_score', n.get_float_value()),
            "deviceAppHealthStatus": lambda n : setattr(self, 'device_app_health_status', n.get_str_value()),
            "deviceDisplayName": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceManufacturer": lambda n : setattr(self, 'device_manufacturer', n.get_str_value()),
            "deviceModel": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(user_experience_analytics_health_state.UserExperienceAnalyticsHealthState)),
            "meanTimeToFailureInMinutes": lambda n : setattr(self, 'mean_time_to_failure_in_minutes', n.get_int_value()),
            "processedDateTime": lambda n : setattr(self, 'processed_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    

