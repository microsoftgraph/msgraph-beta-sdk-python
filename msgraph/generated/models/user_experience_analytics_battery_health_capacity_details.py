from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class UserExperienceAnalyticsBatteryHealthCapacityDetails(entity.Entity):
    # Number of active devices within the tenant. Valid values -2147483648 to 2147483647
    active_devices: Optional[int] = None
    # Number of devices whose battery maximum capacity is greater than 50% but lesser than 80%. Valid values -2147483648 to 2147483647
    battery_capacity_fair: Optional[int] = None
    # Number of devices whose battery maximum capacity is greater than 80%. Valid values -2147483648 to 2147483647
    battery_capacity_good: Optional[int] = None
    # Number of devices whose battery maximum capacity is lesser than 50%. Valid values -2147483648 to 2147483647
    battery_capacity_poor: Optional[int] = None
    # Recorded date time of this capacity details instance.
    last_refreshed_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBatteryHealthCapacityDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthCapacityDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsBatteryHealthCapacityDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "activeDevices": lambda n : setattr(self, 'active_devices', n.get_int_value()),
            "batteryCapacityFair": lambda n : setattr(self, 'battery_capacity_fair', n.get_int_value()),
            "batteryCapacityGood": lambda n : setattr(self, 'battery_capacity_good', n.get_int_value()),
            "batteryCapacityPoor": lambda n : setattr(self, 'battery_capacity_poor', n.get_int_value()),
            "lastRefreshedDateTime": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
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
        writer.write_int_value("activeDevices", self.active_devices)
        writer.write_int_value("batteryCapacityFair", self.battery_capacity_fair)
        writer.write_int_value("batteryCapacityGood", self.battery_capacity_good)
        writer.write_int_value("batteryCapacityPoor", self.battery_capacity_poor)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
    

