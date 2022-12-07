from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user_experience_analytics_health_state = lazy_import('msgraph.generated.models.user_experience_analytics_health_state')

class UserExperienceAnalyticsBatteryHealthDevicePerformance(entity.Entity):
    """
    The user experience analytics battery health device performance entity contains device level battery information.
    """
    @property
    def battery_age_in_days(self,) -> Optional[int]:
        """
        Gets the batteryAgeInDays property value. Estimated battery age. Unit in days. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._battery_age_in_days
    
    @battery_age_in_days.setter
    def battery_age_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the batteryAgeInDays property value. Estimated battery age. Unit in days. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the batteryAgeInDays property.
        """
        self._battery_age_in_days = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsBatteryHealthDevicePerformance and sets the default values.
        """
        super().__init__()
        # Estimated battery age. Unit in days. Valid values -2147483648 to 2147483647
        self._battery_age_in_days: Optional[int] = None
        # A weighted average of a device’s maximum capacity score and runtime estimate score. Values range from 0-100. Valid values -2147483648 to 2147483647
        self._device_battery_health_score: Optional[int] = None
        # The unique identifier of the device, Intune DeviceID.
        self._device_id: Optional[str] = None
        # Device friendly name.
        self._device_name: Optional[str] = None
        # The estimated runtime of the device when the battery is fully charged. Unit in minutes. Valid values -2147483648 to 2147483647
        self._estimated_runtime_in_minutes: Optional[int] = None
        # The healthStatus property
        self._health_status: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None
        # The manufacturer name of the device.
        self._manufacturer: Optional[str] = None
        # Ratio of current capacity and design capacity of the battery with the lowest capacity. Unit in percentage and values range from 0-100. Valid values -2147483648 to 2147483647
        self._max_capacity_percentage: Optional[int] = None
        # The model name of the device.
        self._model: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBatteryHealthDevicePerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthDevicePerformance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsBatteryHealthDevicePerformance()
    
    @property
    def device_battery_health_score(self,) -> Optional[int]:
        """
        Gets the deviceBatteryHealthScore property value. A weighted average of a device’s maximum capacity score and runtime estimate score. Values range from 0-100. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._device_battery_health_score
    
    @device_battery_health_score.setter
    def device_battery_health_score(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceBatteryHealthScore property value. A weighted average of a device’s maximum capacity score and runtime estimate score. Values range from 0-100. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the deviceBatteryHealthScore property.
        """
        self._device_battery_health_score = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The unique identifier of the device, Intune DeviceID.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The unique identifier of the device, Intune DeviceID.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Device friendly name.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Device friendly name.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def estimated_runtime_in_minutes(self,) -> Optional[int]:
        """
        Gets the estimatedRuntimeInMinutes property value. The estimated runtime of the device when the battery is fully charged. Unit in minutes. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._estimated_runtime_in_minutes
    
    @estimated_runtime_in_minutes.setter
    def estimated_runtime_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the estimatedRuntimeInMinutes property value. The estimated runtime of the device when the battery is fully charged. Unit in minutes. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the estimatedRuntimeInMinutes property.
        """
        self._estimated_runtime_in_minutes = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "battery_age_in_days": lambda n : setattr(self, 'battery_age_in_days', n.get_int_value()),
            "device_battery_health_score": lambda n : setattr(self, 'device_battery_health_score', n.get_int_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "estimated_runtime_in_minutes": lambda n : setattr(self, 'estimated_runtime_in_minutes', n.get_int_value()),
            "health_status": lambda n : setattr(self, 'health_status', n.get_enum_value(user_experience_analytics_health_state.UserExperienceAnalyticsHealthState)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "max_capacity_percentage": lambda n : setattr(self, 'max_capacity_percentage', n.get_int_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
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
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. The manufacturer name of the device.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. The manufacturer name of the device.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def max_capacity_percentage(self,) -> Optional[int]:
        """
        Gets the maxCapacityPercentage property value. Ratio of current capacity and design capacity of the battery with the lowest capacity. Unit in percentage and values range from 0-100. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._max_capacity_percentage
    
    @max_capacity_percentage.setter
    def max_capacity_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the maxCapacityPercentage property value. Ratio of current capacity and design capacity of the battery with the lowest capacity. Unit in percentage and values range from 0-100. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the maxCapacityPercentage property.
        """
        self._max_capacity_percentage = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. The model name of the device.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. The model name of the device.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("batteryAgeInDays", self.battery_age_in_days)
        writer.write_int_value("deviceBatteryHealthScore", self.device_battery_health_score)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_int_value("estimatedRuntimeInMinutes", self.estimated_runtime_in_minutes)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_int_value("maxCapacityPercentage", self.max_capacity_percentage)
        writer.write_str_value("model", self.model)
    

