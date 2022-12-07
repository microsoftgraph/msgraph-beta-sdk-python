from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsBatteryHealthModelPerformance(entity.Entity):
    """
    The user experience analytics battery health model performance entity contains battery related information for all unique device models in their organization.
    """
    @property
    def active_devices(self,) -> Optional[int]:
        """
        Gets the activeDevices property value. Number of active devices for that model. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._active_devices
    
    @active_devices.setter
    def active_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the activeDevices property value. Number of active devices for that model. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the activeDevices property.
        """
        self._active_devices = value
    
    @property
    def average_battery_age_in_days(self,) -> Optional[int]:
        """
        Gets the averageBatteryAgeInDays property value. The mean of the battery age for all devices of a given model in a tenant. Unit in days. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._average_battery_age_in_days
    
    @average_battery_age_in_days.setter
    def average_battery_age_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the averageBatteryAgeInDays property value. The mean of the battery age for all devices of a given model in a tenant. Unit in days. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the averageBatteryAgeInDays property.
        """
        self._average_battery_age_in_days = value
    
    @property
    def average_estimated_runtime_in_minutes(self,) -> Optional[int]:
        """
        Gets the averageEstimatedRuntimeInMinutes property value. The mean of the estimated runtimes on full charge for all devices of a given model. Unit in minutes. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._average_estimated_runtime_in_minutes
    
    @average_estimated_runtime_in_minutes.setter
    def average_estimated_runtime_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the averageEstimatedRuntimeInMinutes property value. The mean of the estimated runtimes on full charge for all devices of a given model. Unit in minutes. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the averageEstimatedRuntimeInMinutes property.
        """
        self._average_estimated_runtime_in_minutes = value
    
    @property
    def average_max_capacity_percentage(self,) -> Optional[int]:
        """
        Gets the averageMaxCapacityPercentage property value. The mean of the maximum capacity for all devices of a given model. Maximum capacity measures the full charge vs. design capacity for a device’s batteries.. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._average_max_capacity_percentage
    
    @average_max_capacity_percentage.setter
    def average_max_capacity_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the averageMaxCapacityPercentage property value. The mean of the maximum capacity for all devices of a given model. Maximum capacity measures the full charge vs. design capacity for a device’s batteries.. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the averageMaxCapacityPercentage property.
        """
        self._average_max_capacity_percentage = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsBatteryHealthModelPerformance and sets the default values.
        """
        super().__init__()
        # Number of active devices for that model. Valid values -2147483648 to 2147483647
        self._active_devices: Optional[int] = None
        # The mean of the battery age for all devices of a given model in a tenant. Unit in days. Valid values -2147483648 to 2147483647
        self._average_battery_age_in_days: Optional[int] = None
        # The mean of the estimated runtimes on full charge for all devices of a given model. Unit in minutes. Valid values -2147483648 to 2147483647
        self._average_estimated_runtime_in_minutes: Optional[int] = None
        # The mean of the maximum capacity for all devices of a given model. Maximum capacity measures the full charge vs. design capacity for a device’s batteries.. Valid values -2147483648 to 2147483647
        self._average_max_capacity_percentage: Optional[int] = None
        # Name of the device manufacturer.
        self._manufacturer: Optional[str] = None
        # The model name of the device.
        self._model: Optional[str] = None
        # A weighted average of a model’s maximum capacity score and runtime estimate score. Values range from 0-100. Valid values -2147483648 to 2147483647
        self._model_battery_health_score: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBatteryHealthModelPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthModelPerformance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsBatteryHealthModelPerformance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_devices": lambda n : setattr(self, 'active_devices', n.get_int_value()),
            "average_battery_age_in_days": lambda n : setattr(self, 'average_battery_age_in_days', n.get_int_value()),
            "average_estimated_runtime_in_minutes": lambda n : setattr(self, 'average_estimated_runtime_in_minutes', n.get_int_value()),
            "average_max_capacity_percentage": lambda n : setattr(self, 'average_max_capacity_percentage', n.get_int_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "model_battery_health_score": lambda n : setattr(self, 'model_battery_health_score', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. Name of the device manufacturer.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. Name of the device manufacturer.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
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
    
    @property
    def model_battery_health_score(self,) -> Optional[int]:
        """
        Gets the modelBatteryHealthScore property value. A weighted average of a model’s maximum capacity score and runtime estimate score. Values range from 0-100. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._model_battery_health_score
    
    @model_battery_health_score.setter
    def model_battery_health_score(self,value: Optional[int] = None) -> None:
        """
        Sets the modelBatteryHealthScore property value. A weighted average of a model’s maximum capacity score and runtime estimate score. Values range from 0-100. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the modelBatteryHealthScore property.
        """
        self._model_battery_health_score = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("activeDevices", self.active_devices)
        writer.write_int_value("averageBatteryAgeInDays", self.average_battery_age_in_days)
        writer.write_int_value("averageEstimatedRuntimeInMinutes", self.average_estimated_runtime_in_minutes)
        writer.write_int_value("averageMaxCapacityPercentage", self.average_max_capacity_percentage)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_int_value("modelBatteryHealthScore", self.model_battery_health_score)
    

