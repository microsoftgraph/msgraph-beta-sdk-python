from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import custom_update_time_window, device_configuration, mac_o_s_priority, mac_o_s_software_update_behavior, mac_o_s_software_update_schedule_type

from . import device_configuration

@dataclass
class MacOSSoftwareUpdateConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.macOSSoftwareUpdateConfiguration"
    # Update behavior options for macOS software updates.
    all_other_update_behavior: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior] = None
    # Update behavior options for macOS software updates.
    config_data_update_behavior: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior] = None
    # Update behavior options for macOS software updates.
    critical_update_behavior: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior] = None
    # Custom Time windows when updates will be allowed or blocked. This collection can contain a maximum of 20 elements.
    custom_update_time_windows: Optional[List[custom_update_time_window.CustomUpdateTimeWindow]] = None
    # Update behavior options for macOS software updates.
    firmware_update_behavior: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior] = None
    # The maximum number of times the system allows the user to postpone an update before it’s installed. Supported values: 0 - 366. Valid values 0 to 365
    max_user_deferrals_count: Optional[int] = None
    # The scheduling priority for downloading and preparing the requested update. Default: Low. Possible values: Null, Low, High. Possible values are: low, high, unknownFutureValue.
    priority: Optional[mac_o_s_priority.MacOSPriority] = None
    # Update schedule type for macOS software updates.
    update_schedule_type: Optional[mac_o_s_software_update_schedule_type.MacOSSoftwareUpdateScheduleType] = None
    # Minutes indicating UTC offset for each update time window
    update_time_window_utc_offset_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSSoftwareUpdateConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSoftwareUpdateConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSSoftwareUpdateConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import custom_update_time_window, device_configuration, mac_o_s_priority, mac_o_s_software_update_behavior, mac_o_s_software_update_schedule_type

        fields: Dict[str, Callable[[Any], None]] = {
            "allOtherUpdateBehavior": lambda n : setattr(self, 'all_other_update_behavior', n.get_enum_value(mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior)),
            "configDataUpdateBehavior": lambda n : setattr(self, 'config_data_update_behavior', n.get_enum_value(mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior)),
            "criticalUpdateBehavior": lambda n : setattr(self, 'critical_update_behavior', n.get_enum_value(mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior)),
            "customUpdateTimeWindows": lambda n : setattr(self, 'custom_update_time_windows', n.get_collection_of_object_values(custom_update_time_window.CustomUpdateTimeWindow)),
            "firmwareUpdateBehavior": lambda n : setattr(self, 'firmware_update_behavior', n.get_enum_value(mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior)),
            "maxUserDeferralsCount": lambda n : setattr(self, 'max_user_deferrals_count', n.get_int_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(mac_o_s_priority.MacOSPriority)),
            "updateScheduleType": lambda n : setattr(self, 'update_schedule_type', n.get_enum_value(mac_o_s_software_update_schedule_type.MacOSSoftwareUpdateScheduleType)),
            "updateTimeWindowUtcOffsetInMinutes": lambda n : setattr(self, 'update_time_window_utc_offset_in_minutes', n.get_int_value()),
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
        writer.write_enum_value("allOtherUpdateBehavior", self.all_other_update_behavior)
        writer.write_enum_value("configDataUpdateBehavior", self.config_data_update_behavior)
        writer.write_enum_value("criticalUpdateBehavior", self.critical_update_behavior)
        writer.write_collection_of_object_values("customUpdateTimeWindows", self.custom_update_time_windows)
        writer.write_enum_value("firmwareUpdateBehavior", self.firmware_update_behavior)
        writer.write_int_value("maxUserDeferralsCount", self.max_user_deferrals_count)
        writer.write_enum_value("priority", self.priority)
        writer.write_enum_value("updateScheduleType", self.update_schedule_type)
        writer.write_int_value("updateTimeWindowUtcOffsetInMinutes", self.update_time_window_utc_offset_in_minutes)
    

