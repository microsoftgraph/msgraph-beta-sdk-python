from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_health_script_time_schedule = lazy_import('msgraph.generated.models.device_health_script_time_schedule')

class DeviceHealthScriptRunOnceSchedule(device_health_script_time_schedule.DeviceHealthScriptTimeSchedule):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceHealthScriptRunOnceSchedule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceHealthScriptRunOnceSchedule"
        # The date the script is scheduled to run. This collection can contain a maximum of 20 elements.
        self._date: Optional[Date] = None
    
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
    
    @property
    def date(self,) -> Optional[Date]:
        """
        Gets the date property value. The date the script is scheduled to run. This collection can contain a maximum of 20 elements.
        Returns: Optional[Date]
        """
        return self._date
    
    @date.setter
    def date(self,value: Optional[Date] = None) -> None:
        """
        Sets the date property value. The date the script is scheduled to run. This collection can contain a maximum of 20 elements.
        Args:
            value: Value to set for the date property.
        """
        self._date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "date": lambda n : setattr(self, 'date', n.get_object_value(Date)),
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
        writer.write_object_value("date", self.date)
    

