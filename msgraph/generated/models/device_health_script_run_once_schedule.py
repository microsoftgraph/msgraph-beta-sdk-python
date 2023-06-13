from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_health_script_time_schedule

from . import device_health_script_time_schedule

@dataclass
class DeviceHealthScriptRunOnceSchedule(device_health_script_time_schedule.DeviceHealthScriptTimeSchedule):
    odata_type = "#microsoft.graph.deviceHealthScriptRunOnceSchedule"
    # The date the script is scheduled to run. This collection can contain a maximum of 20 elements.
    date: Optional[date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptRunOnceSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptRunOnceSchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceHealthScriptRunOnceSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_health_script_time_schedule

        fields: Dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_date_value()),
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
        writer.write_date_value("date", self.date)
    

