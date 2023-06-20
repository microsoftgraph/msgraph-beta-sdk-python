from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class UserExperienceAnalyticsBatteryHealthModelPerformance(entity.Entity):
    """
    The user experience analytics battery health model performance entity contains battery related information for all unique device models in their organization.
    """
    # Number of active devices for that model. Valid values -2147483648 to 2147483647
    active_devices: Optional[int] = None
    # The mean of the battery age for all devices of a given model in a tenant. Unit in days. Valid values -2147483648 to 2147483647
    average_battery_age_in_days: Optional[int] = None
    # The mean of the estimated runtimes on full charge for all devices of a given model. Unit in minutes. Valid values -2147483648 to 2147483647
    average_estimated_runtime_in_minutes: Optional[int] = None
    # The mean of the maximum capacity for all devices of a given model. Maximum capacity measures the full charge vs. design capacity for a device’s batteries.. Valid values -2147483648 to 2147483647
    average_max_capacity_percentage: Optional[int] = None
    # Name of the device manufacturer.
    manufacturer: Optional[str] = None
    # The model name of the device.
    model: Optional[str] = None
    # A weighted average of a model’s maximum capacity score and runtime estimate score. Values range from 0-100. Valid values -2147483648 to 2147483647
    model_battery_health_score: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBatteryHealthModelPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthModelPerformance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsBatteryHealthModelPerformance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "activeDevices": lambda n : setattr(self, 'active_devices', n.get_int_value()),
            "averageBatteryAgeInDays": lambda n : setattr(self, 'average_battery_age_in_days', n.get_int_value()),
            "averageEstimatedRuntimeInMinutes": lambda n : setattr(self, 'average_estimated_runtime_in_minutes', n.get_int_value()),
            "averageMaxCapacityPercentage": lambda n : setattr(self, 'average_max_capacity_percentage', n.get_int_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "modelBatteryHealthScore": lambda n : setattr(self, 'model_battery_health_score', n.get_int_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("activeDevices", self.active_devices)
        writer.write_int_value("averageBatteryAgeInDays", self.average_battery_age_in_days)
        writer.write_int_value("averageEstimatedRuntimeInMinutes", self.average_estimated_runtime_in_minutes)
        writer.write_int_value("averageMaxCapacityPercentage", self.average_max_capacity_percentage)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_int_value("modelBatteryHealthScore", self.model_battery_health_score)
    

