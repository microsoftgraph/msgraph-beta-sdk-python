from __future__ import annotations
from dataclasses import dataclass, field
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_health_script_daily_schedule, device_health_script_run_once_schedule, device_health_script_run_schedule

from . import device_health_script_run_schedule

@dataclass
class DeviceHealthScriptTimeSchedule(device_health_script_run_schedule.DeviceHealthScriptRunSchedule):
    odata_type = "#microsoft.graph.deviceHealthScriptTimeSchedule"
    # At what time the script is scheduled to run. This collection can contain a maximum of 20 elements.
    time: Optional[time] = None
    # Indicate if the time is Utc or client local time.
    use_utc: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptTimeSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptTimeSchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceHealthScriptDailySchedule":
                from . import device_health_script_daily_schedule

                return device_health_script_daily_schedule.DeviceHealthScriptDailySchedule()
            if mapping_value == "#microsoft.graph.deviceHealthScriptRunOnceSchedule":
                from . import device_health_script_run_once_schedule

                return device_health_script_run_once_schedule.DeviceHealthScriptRunOnceSchedule()
        return DeviceHealthScriptTimeSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_health_script_daily_schedule, device_health_script_run_once_schedule, device_health_script_run_schedule

        fields: Dict[str, Callable[[Any], None]] = {
            "time": lambda n : setattr(self, 'time', n.get_time_value()),
            "useUtc": lambda n : setattr(self, 'use_utc', n.get_bool_value()),
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
        writer.write_time_value("time", self.time)
        writer.write_bool_value("useUtc", self.use_utc)
    

