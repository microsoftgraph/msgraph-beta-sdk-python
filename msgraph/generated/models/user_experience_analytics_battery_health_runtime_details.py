from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsBatteryHealthRuntimeDetails(entity.Entity):
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
    def battery_runtime_fair(self,) -> Optional[int]:
        """
        Gets the batteryRuntimeFair property value. Number of devices whose active runtime is greater than 3 hours but lesser than 5 hours. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._battery_runtime_fair
    
    @battery_runtime_fair.setter
    def battery_runtime_fair(self,value: Optional[int] = None) -> None:
        """
        Sets the batteryRuntimeFair property value. Number of devices whose active runtime is greater than 3 hours but lesser than 5 hours. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the batteryRuntimeFair property.
        """
        self._battery_runtime_fair = value
    
    @property
    def battery_runtime_good(self,) -> Optional[int]:
        """
        Gets the batteryRuntimeGood property value. Number of devices  whose active runtime is greater than 5 hours. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._battery_runtime_good
    
    @battery_runtime_good.setter
    def battery_runtime_good(self,value: Optional[int] = None) -> None:
        """
        Sets the batteryRuntimeGood property value. Number of devices  whose active runtime is greater than 5 hours. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the batteryRuntimeGood property.
        """
        self._battery_runtime_good = value
    
    @property
    def battery_runtime_poor(self,) -> Optional[int]:
        """
        Gets the batteryRuntimePoor property value. Number of devices whose active runtime is lesser than 3 hours. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._battery_runtime_poor
    
    @battery_runtime_poor.setter
    def battery_runtime_poor(self,value: Optional[int] = None) -> None:
        """
        Sets the batteryRuntimePoor property value. Number of devices whose active runtime is lesser than 3 hours. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the batteryRuntimePoor property.
        """
        self._battery_runtime_poor = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsBatteryHealthRuntimeDetails and sets the default values.
        """
        super().__init__()
        # Number of active devices within the tenant. Valid values -2147483648 to 2147483647
        self._active_devices: Optional[int] = None
        # Number of devices whose active runtime is greater than 3 hours but lesser than 5 hours. Valid values -2147483648 to 2147483647
        self._battery_runtime_fair: Optional[int] = None
        # Number of devices  whose active runtime is greater than 5 hours. Valid values -2147483648 to 2147483647
        self._battery_runtime_good: Optional[int] = None
        # Number of devices whose active runtime is lesser than 3 hours. Valid values -2147483648 to 2147483647
        self._battery_runtime_poor: Optional[int] = None
        # Recorded date time of this runtime details instance.
        self._last_refreshed_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBatteryHealthRuntimeDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthRuntimeDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsBatteryHealthRuntimeDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_devices": lambda n : setattr(self, 'active_devices', n.get_int_value()),
            "battery_runtime_fair": lambda n : setattr(self, 'battery_runtime_fair', n.get_int_value()),
            "battery_runtime_good": lambda n : setattr(self, 'battery_runtime_good', n.get_int_value()),
            "battery_runtime_poor": lambda n : setattr(self, 'battery_runtime_poor', n.get_int_value()),
            "last_refreshed_date_time": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_refreshed_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastRefreshedDateTime property value. Recorded date time of this runtime details instance.
        Returns: Optional[datetime]
        """
        return self._last_refreshed_date_time
    
    @last_refreshed_date_time.setter
    def last_refreshed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRefreshedDateTime property value. Recorded date time of this runtime details instance.
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
        writer.write_int_value("batteryRuntimeFair", self.battery_runtime_fair)
        writer.write_int_value("batteryRuntimeGood", self.battery_runtime_good)
        writer.write_int_value("batteryRuntimePoor", self.battery_runtime_poor)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
    

