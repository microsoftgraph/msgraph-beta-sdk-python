from __future__ import annotations
from dataclasses import dataclass, field
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import custom_update_time_window, day_of_week, device_configuration, ios_software_update_schedule_type

from . import device_configuration

@dataclass
class IosUpdateConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.iosUpdateConfiguration"
    # Active Hours End (active hours mean the time window when updates install should not happen)
    active_hours_end: Optional[time] = None
    # Active Hours Start (active hours mean the time window when updates install should not happen)
    active_hours_start: Optional[time] = None
    # If update schedule type is set to use time window scheduling, custom time windows when updates will be scheduled. This collection can contain a maximum of 20 elements.
    custom_update_time_windows: Optional[List[custom_update_time_window.CustomUpdateTimeWindow]] = None
    # If left unspecified, devices will update to the latest version of the OS.
    desired_os_version: Optional[str] = None
    # Days before software updates are visible to iOS devices ranging from 0 to 90 inclusive
    enforced_software_update_delay_in_days: Optional[int] = None
    # Is setting enabled in UI
    is_enabled: Optional[bool] = None
    # Days in week for which active hours are configured. This collection can contain a maximum of 7 elements.
    scheduled_install_days: Optional[List[day_of_week.DayOfWeek]] = None
    # Update schedule type for iOS software updates.
    update_schedule_type: Optional[ios_software_update_schedule_type.IosSoftwareUpdateScheduleType] = None
    # UTC Time Offset indicated in minutes
    utc_time_offset_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosUpdateConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosUpdateConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosUpdateConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import custom_update_time_window, day_of_week, device_configuration, ios_software_update_schedule_type

        from . import custom_update_time_window, day_of_week, device_configuration, ios_software_update_schedule_type

        fields: Dict[str, Callable[[Any], None]] = {
            "activeHoursEnd": lambda n : setattr(self, 'active_hours_end', n.get_time_value()),
            "activeHoursStart": lambda n : setattr(self, 'active_hours_start', n.get_time_value()),
            "customUpdateTimeWindows": lambda n : setattr(self, 'custom_update_time_windows', n.get_collection_of_object_values(custom_update_time_window.CustomUpdateTimeWindow)),
            "desiredOsVersion": lambda n : setattr(self, 'desired_os_version', n.get_str_value()),
            "enforcedSoftwareUpdateDelayInDays": lambda n : setattr(self, 'enforced_software_update_delay_in_days', n.get_int_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "scheduledInstallDays": lambda n : setattr(self, 'scheduled_install_days', n.get_collection_of_enum_values(day_of_week.DayOfWeek)),
            "updateScheduleType": lambda n : setattr(self, 'update_schedule_type', n.get_enum_value(ios_software_update_schedule_type.IosSoftwareUpdateScheduleType)),
            "utcTimeOffsetInMinutes": lambda n : setattr(self, 'utc_time_offset_in_minutes', n.get_int_value()),
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
        writer.write_time_value("activeHoursEnd", self.active_hours_end)
        writer.write_time_value("activeHoursStart", self.active_hours_start)
        writer.write_collection_of_object_values("customUpdateTimeWindows", self.custom_update_time_windows)
        writer.write_str_value("desiredOsVersion", self.desired_os_version)
        writer.write_int_value("enforcedSoftwareUpdateDelayInDays", self.enforced_software_update_delay_in_days)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_collection_of_enum_values("scheduledInstallDays", self.scheduled_install_days)
        writer.write_enum_value("updateScheduleType", self.update_schedule_type)
        writer.write_int_value("utcTimeOffsetInMinutes", self.utc_time_offset_in_minutes)
    

