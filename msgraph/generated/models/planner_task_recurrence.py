from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import planner_recurrence_schedule

class PlannerTaskRecurrence(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerTaskRecurrence and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The nextInSeriesTaskId property
        self._next_in_series_task_id: Optional[str] = None
        # The occurrenceId property
        self._occurrence_id: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The previousInSeriesTaskId property
        self._previous_in_series_task_id: Optional[str] = None
        # The recurrenceStartDateTime property
        self._recurrence_start_date_time: Optional[datetime] = None
        # The schedule property
        self._schedule: Optional[planner_recurrence_schedule.PlannerRecurrenceSchedule] = None
        # The seriesId property
        self._series_id: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTaskRecurrence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskRecurrence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerTaskRecurrence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import planner_recurrence_schedule

        fields: Dict[str, Callable[[Any], None]] = {
            "nextInSeriesTaskId": lambda n : setattr(self, 'next_in_series_task_id', n.get_str_value()),
            "occurrenceId": lambda n : setattr(self, 'occurrence_id', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "previousInSeriesTaskId": lambda n : setattr(self, 'previous_in_series_task_id', n.get_str_value()),
            "recurrenceStartDateTime": lambda n : setattr(self, 'recurrence_start_date_time', n.get_datetime_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(planner_recurrence_schedule.PlannerRecurrenceSchedule)),
            "seriesId": lambda n : setattr(self, 'series_id', n.get_str_value()),
        }
        return fields
    
    @property
    def next_in_series_task_id(self,) -> Optional[str]:
        """
        Gets the nextInSeriesTaskId property value. The nextInSeriesTaskId property
        Returns: Optional[str]
        """
        return self._next_in_series_task_id
    
    @next_in_series_task_id.setter
    def next_in_series_task_id(self,value: Optional[str] = None) -> None:
        """
        Sets the nextInSeriesTaskId property value. The nextInSeriesTaskId property
        Args:
            value: Value to set for the next_in_series_task_id property.
        """
        self._next_in_series_task_id = value
    
    @property
    def occurrence_id(self,) -> Optional[int]:
        """
        Gets the occurrenceId property value. The occurrenceId property
        Returns: Optional[int]
        """
        return self._occurrence_id
    
    @occurrence_id.setter
    def occurrence_id(self,value: Optional[int] = None) -> None:
        """
        Sets the occurrenceId property value. The occurrenceId property
        Args:
            value: Value to set for the occurrence_id property.
        """
        self._occurrence_id = value
    
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
    
    @property
    def previous_in_series_task_id(self,) -> Optional[str]:
        """
        Gets the previousInSeriesTaskId property value. The previousInSeriesTaskId property
        Returns: Optional[str]
        """
        return self._previous_in_series_task_id
    
    @previous_in_series_task_id.setter
    def previous_in_series_task_id(self,value: Optional[str] = None) -> None:
        """
        Sets the previousInSeriesTaskId property value. The previousInSeriesTaskId property
        Args:
            value: Value to set for the previous_in_series_task_id property.
        """
        self._previous_in_series_task_id = value
    
    @property
    def recurrence_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the recurrenceStartDateTime property value. The recurrenceStartDateTime property
        Returns: Optional[datetime]
        """
        return self._recurrence_start_date_time
    
    @recurrence_start_date_time.setter
    def recurrence_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the recurrenceStartDateTime property value. The recurrenceStartDateTime property
        Args:
            value: Value to set for the recurrence_start_date_time property.
        """
        self._recurrence_start_date_time = value
    
    @property
    def schedule(self,) -> Optional[planner_recurrence_schedule.PlannerRecurrenceSchedule]:
        """
        Gets the schedule property value. The schedule property
        Returns: Optional[planner_recurrence_schedule.PlannerRecurrenceSchedule]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[planner_recurrence_schedule.PlannerRecurrenceSchedule] = None) -> None:
        """
        Sets the schedule property value. The schedule property
        Args:
            value: Value to set for the schedule property.
        """
        self._schedule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("nextInSeriesTaskId", self.next_in_series_task_id)
        writer.write_int_value("occurrenceId", self.occurrence_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("previousInSeriesTaskId", self.previous_in_series_task_id)
        writer.write_datetime_value("recurrenceStartDateTime", self.recurrence_start_date_time)
        writer.write_object_value("schedule", self.schedule)
        writer.write_str_value("seriesId", self.series_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def series_id(self,) -> Optional[str]:
        """
        Gets the seriesId property value. The seriesId property
        Returns: Optional[str]
        """
        return self._series_id
    
    @series_id.setter
    def series_id(self,value: Optional[str] = None) -> None:
        """
        Sets the seriesId property value. The seriesId property
        Args:
            value: Value to set for the series_id property.
        """
        self._series_id = value
    

