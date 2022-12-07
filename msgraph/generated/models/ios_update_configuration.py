from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

custom_update_time_window = lazy_import('msgraph.generated.models.custom_update_time_window')
day_of_week = lazy_import('msgraph.generated.models.day_of_week')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
ios_software_update_schedule_type = lazy_import('msgraph.generated.models.ios_software_update_schedule_type')

class IosUpdateConfiguration(device_configuration.DeviceConfiguration):
    @property
    def active_hours_end(self,) -> Optional[Time]:
        """
        Gets the activeHoursEnd property value. Active Hours End (active hours mean the time window when updates install should not happen)
        Returns: Optional[Time]
        """
        return self._active_hours_end
    
    @active_hours_end.setter
    def active_hours_end(self,value: Optional[Time] = None) -> None:
        """
        Sets the activeHoursEnd property value. Active Hours End (active hours mean the time window when updates install should not happen)
        Args:
            value: Value to set for the activeHoursEnd property.
        """
        self._active_hours_end = value
    
    @property
    def active_hours_start(self,) -> Optional[Time]:
        """
        Gets the activeHoursStart property value. Active Hours Start (active hours mean the time window when updates install should not happen)
        Returns: Optional[Time]
        """
        return self._active_hours_start
    
    @active_hours_start.setter
    def active_hours_start(self,value: Optional[Time] = None) -> None:
        """
        Sets the activeHoursStart property value. Active Hours Start (active hours mean the time window when updates install should not happen)
        Args:
            value: Value to set for the activeHoursStart property.
        """
        self._active_hours_start = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosUpdateConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosUpdateConfiguration"
        # Active Hours End (active hours mean the time window when updates install should not happen)
        self._active_hours_end: Optional[Time] = None
        # Active Hours Start (active hours mean the time window when updates install should not happen)
        self._active_hours_start: Optional[Time] = None
        # If update schedule type is set to use time window scheduling, custom time windows when updates will be scheduled. This collection can contain a maximum of 20 elements.
        self._custom_update_time_windows: Optional[List[custom_update_time_window.CustomUpdateTimeWindow]] = None
        # If left unspecified, devices will update to the latest version of the OS.
        self._desired_os_version: Optional[str] = None
        # Days before software updates are visible to iOS devices ranging from 0 to 90 inclusive
        self._enforced_software_update_delay_in_days: Optional[int] = None
        # Is setting enabled in UI
        self._is_enabled: Optional[bool] = None
        # Days in week for which active hours are configured. This collection can contain a maximum of 7 elements.
        self._scheduled_install_days: Optional[List[day_of_week.DayOfWeek]] = None
        # Update schedule type for iOS software updates.
        self._update_schedule_type: Optional[ios_software_update_schedule_type.IosSoftwareUpdateScheduleType] = None
        # UTC Time Offset indicated in minutes
        self._utc_time_offset_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosUpdateConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosUpdateConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosUpdateConfiguration()
    
    @property
    def custom_update_time_windows(self,) -> Optional[List[custom_update_time_window.CustomUpdateTimeWindow]]:
        """
        Gets the customUpdateTimeWindows property value. If update schedule type is set to use time window scheduling, custom time windows when updates will be scheduled. This collection can contain a maximum of 20 elements.
        Returns: Optional[List[custom_update_time_window.CustomUpdateTimeWindow]]
        """
        return self._custom_update_time_windows
    
    @custom_update_time_windows.setter
    def custom_update_time_windows(self,value: Optional[List[custom_update_time_window.CustomUpdateTimeWindow]] = None) -> None:
        """
        Sets the customUpdateTimeWindows property value. If update schedule type is set to use time window scheduling, custom time windows when updates will be scheduled. This collection can contain a maximum of 20 elements.
        Args:
            value: Value to set for the customUpdateTimeWindows property.
        """
        self._custom_update_time_windows = value
    
    @property
    def desired_os_version(self,) -> Optional[str]:
        """
        Gets the desiredOsVersion property value. If left unspecified, devices will update to the latest version of the OS.
        Returns: Optional[str]
        """
        return self._desired_os_version
    
    @desired_os_version.setter
    def desired_os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the desiredOsVersion property value. If left unspecified, devices will update to the latest version of the OS.
        Args:
            value: Value to set for the desiredOsVersion property.
        """
        self._desired_os_version = value
    
    @property
    def enforced_software_update_delay_in_days(self,) -> Optional[int]:
        """
        Gets the enforcedSoftwareUpdateDelayInDays property value. Days before software updates are visible to iOS devices ranging from 0 to 90 inclusive
        Returns: Optional[int]
        """
        return self._enforced_software_update_delay_in_days
    
    @enforced_software_update_delay_in_days.setter
    def enforced_software_update_delay_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the enforcedSoftwareUpdateDelayInDays property value. Days before software updates are visible to iOS devices ranging from 0 to 90 inclusive
        Args:
            value: Value to set for the enforcedSoftwareUpdateDelayInDays property.
        """
        self._enforced_software_update_delay_in_days = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_hours_end": lambda n : setattr(self, 'active_hours_end', n.get_object_value(Time)),
            "active_hours_start": lambda n : setattr(self, 'active_hours_start', n.get_object_value(Time)),
            "custom_update_time_windows": lambda n : setattr(self, 'custom_update_time_windows', n.get_collection_of_object_values(custom_update_time_window.CustomUpdateTimeWindow)),
            "desired_os_version": lambda n : setattr(self, 'desired_os_version', n.get_str_value()),
            "enforced_software_update_delay_in_days": lambda n : setattr(self, 'enforced_software_update_delay_in_days', n.get_int_value()),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "scheduled_install_days": lambda n : setattr(self, 'scheduled_install_days', n.get_collection_of_enum_values(day_of_week.DayOfWeek)),
            "update_schedule_type": lambda n : setattr(self, 'update_schedule_type', n.get_enum_value(ios_software_update_schedule_type.IosSoftwareUpdateScheduleType)),
            "utc_time_offset_in_minutes": lambda n : setattr(self, 'utc_time_offset_in_minutes', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Is setting enabled in UI
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Is setting enabled in UI
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    @property
    def scheduled_install_days(self,) -> Optional[List[day_of_week.DayOfWeek]]:
        """
        Gets the scheduledInstallDays property value. Days in week for which active hours are configured. This collection can contain a maximum of 7 elements.
        Returns: Optional[List[day_of_week.DayOfWeek]]
        """
        return self._scheduled_install_days
    
    @scheduled_install_days.setter
    def scheduled_install_days(self,value: Optional[List[day_of_week.DayOfWeek]] = None) -> None:
        """
        Sets the scheduledInstallDays property value. Days in week for which active hours are configured. This collection can contain a maximum of 7 elements.
        Args:
            value: Value to set for the scheduledInstallDays property.
        """
        self._scheduled_install_days = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("activeHoursEnd", self.active_hours_end)
        writer.write_object_value("activeHoursStart", self.active_hours_start)
        writer.write_collection_of_object_values("customUpdateTimeWindows", self.custom_update_time_windows)
        writer.write_str_value("desiredOsVersion", self.desired_os_version)
        writer.write_int_value("enforcedSoftwareUpdateDelayInDays", self.enforced_software_update_delay_in_days)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_enum_value("scheduledInstallDays", self.scheduled_install_days)
        writer.write_enum_value("updateScheduleType", self.update_schedule_type)
        writer.write_int_value("utcTimeOffsetInMinutes", self.utc_time_offset_in_minutes)
    
    @property
    def update_schedule_type(self,) -> Optional[ios_software_update_schedule_type.IosSoftwareUpdateScheduleType]:
        """
        Gets the updateScheduleType property value. Update schedule type for iOS software updates.
        Returns: Optional[ios_software_update_schedule_type.IosSoftwareUpdateScheduleType]
        """
        return self._update_schedule_type
    
    @update_schedule_type.setter
    def update_schedule_type(self,value: Optional[ios_software_update_schedule_type.IosSoftwareUpdateScheduleType] = None) -> None:
        """
        Sets the updateScheduleType property value. Update schedule type for iOS software updates.
        Args:
            value: Value to set for the updateScheduleType property.
        """
        self._update_schedule_type = value
    
    @property
    def utc_time_offset_in_minutes(self,) -> Optional[int]:
        """
        Gets the utcTimeOffsetInMinutes property value. UTC Time Offset indicated in minutes
        Returns: Optional[int]
        """
        return self._utc_time_offset_in_minutes
    
    @utc_time_offset_in_minutes.setter
    def utc_time_offset_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the utcTimeOffsetInMinutes property value. UTC Time Offset indicated in minutes
        Args:
            value: Value to set for the utcTimeOffsetInMinutes property.
        """
        self._utc_time_offset_in_minutes = value
    

