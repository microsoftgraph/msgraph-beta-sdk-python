from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import industry_data_run_activity, industry_data_run_status
    from .. import entity, public_error

from .. import entity

class IndustryDataRun(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new industryDataRun and sets the default values.
        """
        super().__init__()
        # The set of activities performed during the run.
        self._activities: Optional[List[industry_data_run_activity.IndustryDataRunActivity]] = None
        # An error object to diagnose critical failures in the run.
        self._blocking_error: Optional[public_error.PublicError] = None
        # The name of the run for rendering in a user interface.
        self._display_name: Optional[str] = None
        # The date and time when the run finished or null if the run is still in-progress. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._end_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The date and time when the run started. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._start_date_time: Optional[datetime] = None
        # The status property
        self._status: Optional[industry_data_run_status.IndustryDataRunStatus] = None
    
    @property
    def activities(self,) -> Optional[List[industry_data_run_activity.IndustryDataRunActivity]]:
        """
        Gets the activities property value. The set of activities performed during the run.
        Returns: Optional[List[industry_data_run_activity.IndustryDataRunActivity]]
        """
        return self._activities
    
    @activities.setter
    def activities(self,value: Optional[List[industry_data_run_activity.IndustryDataRunActivity]] = None) -> None:
        """
        Sets the activities property value. The set of activities performed during the run.
        Args:
            value: Value to set for the activities property.
        """
        self._activities = value
    
    @property
    def blocking_error(self,) -> Optional[public_error.PublicError]:
        """
        Gets the blockingError property value. An error object to diagnose critical failures in the run.
        Returns: Optional[public_error.PublicError]
        """
        return self._blocking_error
    
    @blocking_error.setter
    def blocking_error(self,value: Optional[public_error.PublicError] = None) -> None:
        """
        Sets the blockingError property value. An error object to diagnose critical failures in the run.
        Args:
            value: Value to set for the blocking_error property.
        """
        self._blocking_error = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IndustryDataRun:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataRun
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IndustryDataRun()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the run for rendering in a user interface.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the run for rendering in a user interface.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The date and time when the run finished or null if the run is still in-progress. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The date and time when the run finished or null if the run is still in-progress. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the end_date_time property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import industry_data_run_activity, industry_data_run_status
        from .. import entity, public_error

        fields: Dict[str, Callable[[Any], None]] = {
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(industry_data_run_activity.IndustryDataRunActivity)),
            "blockingError": lambda n : setattr(self, 'blocking_error', n.get_object_value(public_error.PublicError)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(industry_data_run_status.IndustryDataRunStatus)),
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
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_enum_value("status", self.status)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The date and time when the run started. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The date and time when the run started. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the start_date_time property.
        """
        self._start_date_time = value
    
    @property
    def status(self,) -> Optional[industry_data_run_status.IndustryDataRunStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[industry_data_run_status.IndustryDataRunStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[industry_data_run_status.IndustryDataRunStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

