from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_health_script_daily_schedule, device_health_script_hourly_schedule, device_health_script_run_once_schedule, device_health_script_time_schedule

class DeviceHealthScriptRunSchedule(AdditionalDataHolder, Parsable):
    """
    Base type of Device health script run schedule.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceHealthScriptRunSchedule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The x value of every x hours for hourly schedule, every x days for Daily Schedule, every x weeks for weekly schedule, every x months for Monthly Schedule. Valid values 1 to 23
        self._interval: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptRunSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptRunSchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceHealthScriptDailySchedule":
                from . import device_health_script_daily_schedule

                return device_health_script_daily_schedule.DeviceHealthScriptDailySchedule()
            if mapping_value == "#microsoft.graph.deviceHealthScriptHourlySchedule":
                from . import device_health_script_hourly_schedule

                return device_health_script_hourly_schedule.DeviceHealthScriptHourlySchedule()
            if mapping_value == "#microsoft.graph.deviceHealthScriptRunOnceSchedule":
                from . import device_health_script_run_once_schedule

                return device_health_script_run_once_schedule.DeviceHealthScriptRunOnceSchedule()
            if mapping_value == "#microsoft.graph.deviceHealthScriptTimeSchedule":
                from . import device_health_script_time_schedule

                return device_health_script_time_schedule.DeviceHealthScriptTimeSchedule()
        return DeviceHealthScriptRunSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_health_script_daily_schedule, device_health_script_hourly_schedule, device_health_script_run_once_schedule, device_health_script_time_schedule

        fields: Dict[str, Callable[[Any], None]] = {
            "interval": lambda n : setattr(self, 'interval', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def interval(self,) -> Optional[int]:
        """
        Gets the interval property value. The x value of every x hours for hourly schedule, every x days for Daily Schedule, every x weeks for weekly schedule, every x months for Monthly Schedule. Valid values 1 to 23
        Returns: Optional[int]
        """
        return self._interval
    
    @interval.setter
    def interval(self,value: Optional[int] = None) -> None:
        """
        Sets the interval property value. The x value of every x hours for hourly schedule, every x days for Daily Schedule, every x weeks for weekly schedule, every x months for Monthly Schedule. Valid values 1 to 23
        Args:
            value: Value to set for the interval property.
        """
        self._interval = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("interval", self.interval)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

