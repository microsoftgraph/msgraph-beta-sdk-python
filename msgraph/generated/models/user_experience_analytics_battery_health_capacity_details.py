from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsBatteryHealthCapacityDetails(entity.Entity):
    @property
    def active_devices(self,) -> Optional[int]:
        """
        Gets the activeDevices property value. Number of active devices within the tenant. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._active_devices
    
    @active_devices.setter
    def active_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the activeDevices property value. Number of active devices within the tenant. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the activeDevices property.
        """
        self._active_devices = value
    
    @property
    def battery_capacity_fair(self,) -> Optional[int]:
        """
        Gets the batteryCapacityFair property value. Number of devices whose battery maximum capacity is greater than 50% but lesser than 80%. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._battery_capacity_fair
    
    @battery_capacity_fair.setter
    def battery_capacity_fair(self,value: Optional[int] = None) -> None:
        """
        Sets the batteryCapacityFair property value. Number of devices whose battery maximum capacity is greater than 50% but lesser than 80%. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the batteryCapacityFair property.
        """
        self._battery_capacity_fair = value
    
    @property
    def battery_capacity_good(self,) -> Optional[int]:
        """
        Gets the batteryCapacityGood property value. Number of devices whose battery maximum capacity is greater than 80%. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._battery_capacity_good
    
    @battery_capacity_good.setter
    def battery_capacity_good(self,value: Optional[int] = None) -> None:
        """
        Sets the batteryCapacityGood property value. Number of devices whose battery maximum capacity is greater than 80%. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the batteryCapacityGood property.
        """
        self._battery_capacity_good = value
    
    @property
    def battery_capacity_poor(self,) -> Optional[int]:
        """
        Gets the batteryCapacityPoor property value. Number of devices whose battery maximum capacity is lesser than 50%. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._battery_capacity_poor
    
    @battery_capacity_poor.setter
    def battery_capacity_poor(self,value: Optional[int] = None) -> None:
        """
        Sets the batteryCapacityPoor property value. Number of devices whose battery maximum capacity is lesser than 50%. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the batteryCapacityPoor property.
        """
        self._battery_capacity_poor = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsBatteryHealthCapacityDetails and sets the default values.
        """
        super().__init__()
        # Number of active devices within the tenant. Valid values -2147483648 to 2147483647
        self._active_devices: Optional[int] = None
        # Number of devices whose battery maximum capacity is greater than 50% but lesser than 80%. Valid values -2147483648 to 2147483647
        self._battery_capacity_fair: Optional[int] = None
        # Number of devices whose battery maximum capacity is greater than 80%. Valid values -2147483648 to 2147483647
        self._battery_capacity_good: Optional[int] = None
        # Number of devices whose battery maximum capacity is lesser than 50%. Valid values -2147483648 to 2147483647
        self._battery_capacity_poor: Optional[int] = None
        # Recorded date time of this capacity details instance.
        self._last_refreshed_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
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
        fields = {
            "active_devices": lambda n : setattr(self, 'active_devices', n.get_int_value()),
            "battery_capacity_fair": lambda n : setattr(self, 'battery_capacity_fair', n.get_int_value()),
            "battery_capacity_good": lambda n : setattr(self, 'battery_capacity_good', n.get_int_value()),
            "battery_capacity_poor": lambda n : setattr(self, 'battery_capacity_poor', n.get_int_value()),
            "last_refreshed_date_time": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_refreshed_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastRefreshedDateTime property value. Recorded date time of this capacity details instance.
        Returns: Optional[datetime]
        """
        return self._last_refreshed_date_time
    
    @last_refreshed_date_time.setter
    def last_refreshed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRefreshedDateTime property value. Recorded date time of this capacity details instance.
        Args:
            value: Value to set for the lastRefreshedDateTime property.
        """
        self._last_refreshed_date_time = value
    
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
    

