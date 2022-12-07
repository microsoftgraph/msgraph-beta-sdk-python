from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_health_script_run_schedule = lazy_import('msgraph.generated.models.device_health_script_run_schedule')

class DeviceHealthScriptTimeSchedule(device_health_script_run_schedule.DeviceHealthScriptRunSchedule):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceHealthScriptTimeSchedule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceHealthScriptTimeSchedule"
        # At what time the script is scheduled to run. This collection can contain a maximum of 20 elements.
        self._time: Optional[Time] = None
        # Indicate if the time is Utc or client local time.
        self._use_utc: Optional[bool] = None
    
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
        return DeviceHealthScriptTimeSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "time": lambda n : setattr(self, 'time', n.get_object_value(Time)),
            "use_utc": lambda n : setattr(self, 'use_utc', n.get_bool_value()),
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
        writer.write_object_value("time", self.time)
        writer.write_bool_value("useUtc", self.use_utc)
    
    @property
    def time(self,) -> Optional[Time]:
        """
        Gets the time property value. At what time the script is scheduled to run. This collection can contain a maximum of 20 elements.
        Returns: Optional[Time]
        """
        return self._time
    
    @time.setter
    def time(self,value: Optional[Time] = None) -> None:
        """
        Sets the time property value. At what time the script is scheduled to run. This collection can contain a maximum of 20 elements.
        Args:
            value: Value to set for the time property.
        """
        self._time = value
    
    @property
    def use_utc(self,) -> Optional[bool]:
        """
        Gets the useUtc property value. Indicate if the time is Utc or client local time.
        Returns: Optional[bool]
        """
        return self._use_utc
    
    @use_utc.setter
    def use_utc(self,value: Optional[bool] = None) -> None:
        """
        Sets the useUtc property value. Indicate if the time is Utc or client local time.
        Args:
            value: Value to set for the useUtc property.
        """
        self._use_utc = value
    

