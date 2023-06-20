from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_health_script_daily_schedule, device_health_script_hourly_schedule, device_health_script_run_once_schedule, device_health_script_time_schedule

@dataclass
class DeviceHealthScriptRunSchedule(AdditionalDataHolder, Parsable):
    """
    Base type of Device health script run schedule.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The x value of every x hours for hourly schedule, every x days for Daily Schedule, every x weeks for weekly schedule, every x months for Monthly Schedule. Valid values 1 to 23
    interval: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptRunSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptRunSchedule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceHealthScriptDailySchedule".casefold():
            from . import device_health_script_daily_schedule

            return device_health_script_daily_schedule.DeviceHealthScriptDailySchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceHealthScriptHourlySchedule".casefold():
            from . import device_health_script_hourly_schedule

            return device_health_script_hourly_schedule.DeviceHealthScriptHourlySchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceHealthScriptRunOnceSchedule".casefold():
            from . import device_health_script_run_once_schedule

            return device_health_script_run_once_schedule.DeviceHealthScriptRunOnceSchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceHealthScriptTimeSchedule".casefold():
            from . import device_health_script_time_schedule

            return device_health_script_time_schedule.DeviceHealthScriptTimeSchedule()
        return DeviceHealthScriptRunSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_health_script_daily_schedule, device_health_script_hourly_schedule, device_health_script_run_once_schedule, device_health_script_time_schedule

        from . import device_health_script_daily_schedule, device_health_script_hourly_schedule, device_health_script_run_once_schedule, device_health_script_time_schedule

        fields: Dict[str, Callable[[Any], None]] = {
            "interval": lambda n : setattr(self, 'interval', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("interval", self.interval)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

