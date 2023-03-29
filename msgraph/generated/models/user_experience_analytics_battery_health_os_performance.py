from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class UserExperienceAnalyticsBatteryHealthOsPerformance(entity.Entity):
    """
    The user experience analytics battery health os performance entity contains battery related information for all operating system versions in their organization.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsBatteryHealthOsPerformance and sets the default values.
        """
        super().__init__()
        # Number of active devices for that os version. Valid values -2147483648 to 2147483647
        self._active_devices: Optional[int] = None
        # The mean of the battery age for all devices running a particular operating system version in a tenant. Unit in days. Valid values -2147483648 to 2147483647
        self._average_battery_age_in_days: Optional[int] = None
        # The mean of the estimated runtimes on full charge for all devices running a particular operating system version. Unit in minutes. Valid values -2147483648 to 2147483647
        self._average_estimated_runtime_in_minutes: Optional[int] = None
        # The mean of the maximum capacity for all devices running a particular operating system version. Maximum capacity measures the full charge vs. design capacity for a device’s batteries.. Valid values -2147483648 to 2147483647
        self._average_max_capacity_percentage: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Build number of the operating system.
        self._os_build_number: Optional[str] = None
        # Version of the operating system.
        self._os_version: Optional[str] = None
    
    @property
    def active_devices(self,) -> Optional[int]:
        """
        Gets the activeDevices property value. Number of active devices for that os version. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._active_devices
    
    @active_devices.setter
    def active_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the activeDevices property value. Number of active devices for that os version. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the active_devices property.
        """
        self._active_devices = value
    
    @property
    def average_battery_age_in_days(self,) -> Optional[int]:
        """
        Gets the averageBatteryAgeInDays property value. The mean of the battery age for all devices running a particular operating system version in a tenant. Unit in days. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._average_battery_age_in_days
    
    @average_battery_age_in_days.setter
    def average_battery_age_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the averageBatteryAgeInDays property value. The mean of the battery age for all devices running a particular operating system version in a tenant. Unit in days. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the average_battery_age_in_days property.
        """
        self._average_battery_age_in_days = value
    
    @property
    def average_estimated_runtime_in_minutes(self,) -> Optional[int]:
        """
        Gets the averageEstimatedRuntimeInMinutes property value. The mean of the estimated runtimes on full charge for all devices running a particular operating system version. Unit in minutes. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._average_estimated_runtime_in_minutes
    
    @average_estimated_runtime_in_minutes.setter
    def average_estimated_runtime_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the averageEstimatedRuntimeInMinutes property value. The mean of the estimated runtimes on full charge for all devices running a particular operating system version. Unit in minutes. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the average_estimated_runtime_in_minutes property.
        """
        self._average_estimated_runtime_in_minutes = value
    
    @property
    def average_max_capacity_percentage(self,) -> Optional[int]:
        """
        Gets the averageMaxCapacityPercentage property value. The mean of the maximum capacity for all devices running a particular operating system version. Maximum capacity measures the full charge vs. design capacity for a device’s batteries.. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._average_max_capacity_percentage
    
    @average_max_capacity_percentage.setter
    def average_max_capacity_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the averageMaxCapacityPercentage property value. The mean of the maximum capacity for all devices running a particular operating system version. Maximum capacity measures the full charge vs. design capacity for a device’s batteries.. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the average_max_capacity_percentage property.
        """
        self._average_max_capacity_percentage = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBatteryHealthOsPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthOsPerformance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsBatteryHealthOsPerformance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "activeDevices": lambda n : setattr(self, 'active_devices', n.get_int_value()),
            "averageBatteryAgeInDays": lambda n : setattr(self, 'average_battery_age_in_days', n.get_int_value()),
            "averageEstimatedRuntimeInMinutes": lambda n : setattr(self, 'average_estimated_runtime_in_minutes', n.get_int_value()),
            "averageMaxCapacityPercentage": lambda n : setattr(self, 'average_max_capacity_percentage', n.get_int_value()),
            "osBuildNumber": lambda n : setattr(self, 'os_build_number', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def os_build_number(self,) -> Optional[str]:
        """
        Gets the osBuildNumber property value. Build number of the operating system.
        Returns: Optional[str]
        """
        return self._os_build_number
    
    @os_build_number.setter
    def os_build_number(self,value: Optional[str] = None) -> None:
        """
        Sets the osBuildNumber property value. Build number of the operating system.
        Args:
            value: Value to set for the os_build_number property.
        """
        self._os_build_number = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. Version of the operating system.
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. Version of the operating system.
        Args:
            value: Value to set for the os_version property.
        """
        self._os_version = value
    
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
        writer.write_str_value("osBuildNumber", self.os_build_number)
        writer.write_str_value("osVersion", self.os_version)
    

