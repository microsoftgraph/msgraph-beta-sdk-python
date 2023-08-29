from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsBatteryHealthRuntimeDetails(Entity):
    """
    The user experience analytics battery health runtime entity contains count of devices broken down into 3 categories - devices with runtime > 5 hours, devices with runtime 3-5 hours and devices with runtime < 3 hours.This API provides the count of devices in these 3 categories.
    """
    # Number of active devices within the tenant. Valid values 0 to 2147483647
    active_devices: Optional[int] = None
    # Number of devices whose active runtime is greater than 3 hours but lesser than 5 hours. Valid values 0 to 2147483647
    battery_runtime_fair: Optional[int] = None
    # Number of devices  whose active runtime is greater than 5 hours. Valid values 0 to 2147483647
    battery_runtime_good: Optional[int] = None
    # Number of devices whose active runtime is lesser than 3 hours. Valid values 0 to 2147483647
    battery_runtime_poor: Optional[int] = None
    # Recorded date time of this runtime details instance.
    last_refreshed_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBatteryHealthRuntimeDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthRuntimeDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsBatteryHealthRuntimeDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "activeDevices": lambda n : setattr(self, 'active_devices', n.get_int_value()),
            "batteryRuntimeFair": lambda n : setattr(self, 'battery_runtime_fair', n.get_int_value()),
            "batteryRuntimeGood": lambda n : setattr(self, 'battery_runtime_good', n.get_int_value()),
            "batteryRuntimePoor": lambda n : setattr(self, 'battery_runtime_poor', n.get_int_value()),
            "lastRefreshedDateTime": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("activeDevices", self.active_devices)
        writer.write_int_value("batteryRuntimeFair", self.battery_runtime_fair)
        writer.write_int_value("batteryRuntimeGood", self.battery_runtime_good)
        writer.write_int_value("batteryRuntimePoor", self.battery_runtime_poor)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
    

