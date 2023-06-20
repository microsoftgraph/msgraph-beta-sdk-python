from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, user_experience_analytics_health_state

from . import entity

@dataclass
class UserExperienceAnalyticsDeviceScores(entity.Entity):
    """
    The user experience analytics device scores entity consolidates the various Endpoint Analytics scores.
    """
    # The user experience analytics device app reliability score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    app_reliability_score: Optional[float] = None
    # The user experience analytics device battery health score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    battery_health_score: Optional[float] = None
    # The user experience analytics device name.
    device_name: Optional[str] = None
    # The user experience analytics device score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    endpoint_analytics_score: Optional[float] = None
    # The healthStatus property
    health_status: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None
    # The user experience analytics device manufacturer.
    manufacturer: Optional[str] = None
    # The user experience analytics device model.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user experience analytics device startup performance score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    startup_performance_score: Optional[float] = None
    # The user experience analytics device work From anywhere score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    work_from_anywhere_score: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDeviceScores:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceScores
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsDeviceScores()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, user_experience_analytics_health_state

        from . import entity, user_experience_analytics_health_state

        fields: Dict[str, Callable[[Any], None]] = {
            "appReliabilityScore": lambda n : setattr(self, 'app_reliability_score', n.get_float_value()),
            "batteryHealthScore": lambda n : setattr(self, 'battery_health_score', n.get_float_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "endpointAnalyticsScore": lambda n : setattr(self, 'endpoint_analytics_score', n.get_float_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(user_experience_analytics_health_state.UserExperienceAnalyticsHealthState)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "startupPerformanceScore": lambda n : setattr(self, 'startup_performance_score', n.get_float_value()),
            "workFromAnywhereScore": lambda n : setattr(self, 'work_from_anywhere_score', n.get_float_value()),
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
        writer.write_float_value("appReliabilityScore", self.app_reliability_score)
        writer.write_float_value("batteryHealthScore", self.battery_health_score)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_float_value("endpointAnalyticsScore", self.endpoint_analytics_score)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_float_value("startupPerformanceScore", self.startup_performance_score)
        writer.write_float_value("workFromAnywhereScore", self.work_from_anywhere_score)
    

