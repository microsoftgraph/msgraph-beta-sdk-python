from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

day_of_week = lazy_import('msgraph.generated.models.day_of_week')
windows10_apps_update_recurrence = lazy_import('msgraph.generated.models.windows10_apps_update_recurrence')

class WindowsKioskForceUpdateSchedule(AdditionalDataHolder, Parsable):
    """
    Windows 10 force update schedule for Kiosk devices.
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsKioskForceUpdateSchedule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Day of month. Valid values 1 to 31
        self._dayof_month: Optional[int] = None
        # The dayofWeek property
        self._dayof_week: Optional[day_of_week.DayOfWeek] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Possible values for App update on Windows10 recurrence.
        self._recurrence: Optional[windows10_apps_update_recurrence.Windows10AppsUpdateRecurrence] = None
        # If true, runs the task immediately if StartDateTime is in the past, else, runs at the next recurrence.
        self._run_immediately_if_after_start_date_time: Optional[bool] = None
        # The start time for the force restart.
        self._start_date_time: Optional[datetime] = None
    
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
    
    @property
    def dayof_month(self,) -> Optional[int]:
        """
        Gets the dayofMonth property value. Day of month. Valid values 1 to 31
        Returns: Optional[int]
        """
        return self._dayof_month
    
    @dayof_month.setter
    def dayof_month(self,value: Optional[int] = None) -> None:
        """
        Sets the dayofMonth property value. Day of month. Valid values 1 to 31
        Args:
            value: Value to set for the dayofMonth property.
        """
        self._dayof_month = value
    
    @property
    def dayof_week(self,) -> Optional[day_of_week.DayOfWeek]:
        """
        Gets the dayofWeek property value. The dayofWeek property
        Returns: Optional[day_of_week.DayOfWeek]
        """
        return self._dayof_week
    
    @dayof_week.setter
    def dayof_week(self,value: Optional[day_of_week.DayOfWeek] = None) -> None:
        """
        Sets the dayofWeek property value. The dayofWeek property
        Args:
            value: Value to set for the dayofWeek property.
        """
        self._dayof_week = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "dayof_month": lambda n : setattr(self, 'dayof_month', n.get_int_value()),
            "dayof_week": lambda n : setattr(self, 'dayof_week', n.get_enum_value(day_of_week.DayOfWeek)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_enum_value(windows10_apps_update_recurrence.Windows10AppsUpdateRecurrence)),
            "run_immediately_if_after_start_date_time": lambda n : setattr(self, 'run_immediately_if_after_start_date_time', n.get_bool_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        return fields
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def recurrence(self,) -> Optional[windows10_apps_update_recurrence.Windows10AppsUpdateRecurrence]:
        """
        Gets the recurrence property value. Possible values for App update on Windows10 recurrence.
        Returns: Optional[windows10_apps_update_recurrence.Windows10AppsUpdateRecurrence]
        """
        return self._recurrence
    
    @recurrence.setter
    def recurrence(self,value: Optional[windows10_apps_update_recurrence.Windows10AppsUpdateRecurrence] = None) -> None:
        """
        Sets the recurrence property value. Possible values for App update on Windows10 recurrence.
        Args:
            value: Value to set for the recurrence property.
        """
        self._recurrence = value
    
    @property
    def run_immediately_if_after_start_date_time(self,) -> Optional[bool]:
        """
        Gets the runImmediatelyIfAfterStartDateTime property value. If true, runs the task immediately if StartDateTime is in the past, else, runs at the next recurrence.
        Returns: Optional[bool]
        """
        return self._run_immediately_if_after_start_date_time
    
    @run_immediately_if_after_start_date_time.setter
    def run_immediately_if_after_start_date_time(self,value: Optional[bool] = None) -> None:
        """
        Sets the runImmediatelyIfAfterStartDateTime property value. If true, runs the task immediately if StartDateTime is in the past, else, runs at the next recurrence.
        Args:
            value: Value to set for the runImmediatelyIfAfterStartDateTime property.
        """
        self._run_immediately_if_after_start_date_time = value
    
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
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The start time for the force restart.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The start time for the force restart.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    

