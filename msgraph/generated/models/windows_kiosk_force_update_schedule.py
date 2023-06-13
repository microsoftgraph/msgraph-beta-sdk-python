from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import day_of_week, windows10_apps_update_recurrence

@dataclass
class WindowsKioskForceUpdateSchedule(AdditionalDataHolder, Parsable):
    """
    Windows 10 force update schedule for Kiosk devices.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Day of month. Valid values 1 to 31
    dayof_month: Optional[int] = None
    # The dayofWeek property
    dayof_week: Optional[day_of_week.DayOfWeek] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Possible values for App update on Windows10 recurrence.
    recurrence: Optional[windows10_apps_update_recurrence.Windows10AppsUpdateRecurrence] = None
    # If true, runs the task immediately if StartDateTime is in the past, else, runs at the next recurrence.
    run_immediately_if_after_start_date_time: Optional[bool] = None
    # The start time for the force restart.
    start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskForceUpdateSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskForceUpdateSchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskForceUpdateSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import day_of_week, windows10_apps_update_recurrence

        fields: Dict[str, Callable[[Any], None]] = {
            "dayofMonth": lambda n : setattr(self, 'dayof_month', n.get_int_value()),
            "dayofWeek": lambda n : setattr(self, 'dayof_week', n.get_enum_value(day_of_week.DayOfWeek)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_enum_value(windows10_apps_update_recurrence.Windows10AppsUpdateRecurrence)),
            "runImmediatelyIfAfterStartDateTime": lambda n : setattr(self, 'run_immediately_if_after_start_date_time', n.get_bool_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("dayofMonth", self.dayof_month)
        writer.write_enum_value("dayofWeek", self.dayof_week)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("recurrence", self.recurrence)
        writer.write_bool_value("runImmediatelyIfAfterStartDateTime", self.run_immediately_if_after_start_date_time)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

