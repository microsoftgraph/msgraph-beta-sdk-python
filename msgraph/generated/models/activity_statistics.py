from __future__ import annotations
from datetime import date, timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

analytics_activity_type = lazy_import('msgraph.generated.models.analytics_activity_type')
entity = lazy_import('msgraph.generated.models.entity')

class ActivityStatistics(entity.Entity):
    """
    Provides operations to manage the collection of activityStatistics entities.
    """
    @property
    def activity(self,) -> Optional[analytics_activity_type.AnalyticsActivityType]:
        """
        Gets the activity property value. The type of activity for which statistics are returned. The possible values are: call, chat, email, focus, and meeting.
        Returns: Optional[analytics_activity_type.AnalyticsActivityType]
        """
        return self._activity
    
    @activity.setter
    def activity(self,value: Optional[analytics_activity_type.AnalyticsActivityType] = None) -> None:
        """
        Sets the activity property value. The type of activity for which statistics are returned. The possible values are: call, chat, email, focus, and meeting.
        Args:
            value: Value to set for the activity property.
        """
        self._activity = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new activityStatistics and sets the default values.
        """
        super().__init__()
        # The type of activity for which statistics are returned. The possible values are: call, chat, email, focus, and meeting.
        self._activity: Optional[analytics_activity_type.AnalyticsActivityType] = None
        # Total hours spent on the activity. The value is represented in ISO 8601 format for durations.
        self._duration: Optional[Timedelta] = None
        # Date when the activity ended, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-03' that follows the YYYY-MM-DD format.
        self._end_date: Optional[Date] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Date when the activity started, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-04' that follows the YYYY-MM-DD format.
        self._start_date: Optional[Date] = None
        # The time zone that the user sets in Microsoft Outlook is used for the computation. For example, the property value could be 'Pacific Standard Time.'
        self._time_zone_used: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ActivityStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ActivityStatistics
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ActivityStatistics()
    
    @property
    def duration(self,) -> Optional[Timedelta]:
        """
        Gets the duration property value. Total hours spent on the activity. The value is represented in ISO 8601 format for durations.
        Returns: Optional[Timedelta]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the duration property value. Total hours spent on the activity. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    @property
    def end_date(self,) -> Optional[Date]:
        """
        Gets the endDate property value. Date when the activity ended, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-03' that follows the YYYY-MM-DD format.
        Returns: Optional[Date]
        """
        return self._end_date
    
    @end_date.setter
    def end_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the endDate property value. Date when the activity ended, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-03' that follows the YYYY-MM-DD format.
        Args:
            value: Value to set for the endDate property.
        """
        self._end_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity": lambda n : setattr(self, 'activity', n.get_enum_value(analytics_activity_type.AnalyticsActivityType)),
            "duration": lambda n : setattr(self, 'duration', n.get_object_value(Timedelta)),
            "end_date": lambda n : setattr(self, 'end_date', n.get_object_value(Date)),
            "start_date": lambda n : setattr(self, 'start_date', n.get_object_value(Date)),
            "time_zone_used": lambda n : setattr(self, 'time_zone_used', n.get_str_value()),
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
        writer.write_enum_value("activity", self.activity)
        writer.write_object_value("duration", self.duration)
        writer.write_object_value("endDate", self.end_date)
        writer.write_object_value("startDate", self.start_date)
        writer.write_str_value("timeZoneUsed", self.time_zone_used)
    
    @property
    def start_date(self,) -> Optional[Date]:
        """
        Gets the startDate property value. Date when the activity started, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-04' that follows the YYYY-MM-DD format.
        Returns: Optional[Date]
        """
        return self._start_date
    
    @start_date.setter
    def start_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the startDate property value. Date when the activity started, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-04' that follows the YYYY-MM-DD format.
        Args:
            value: Value to set for the startDate property.
        """
        self._start_date = value
    
    @property
    def time_zone_used(self,) -> Optional[str]:
        """
        Gets the timeZoneUsed property value. The time zone that the user sets in Microsoft Outlook is used for the computation. For example, the property value could be 'Pacific Standard Time.'
        Returns: Optional[str]
        """
        return self._time_zone_used
    
    @time_zone_used.setter
    def time_zone_used(self,value: Optional[str] = None) -> None:
        """
        Sets the timeZoneUsed property value. The time zone that the user sets in Microsoft Outlook is used for the computation. For example, the property value could be 'Pacific Standard Time.'
        Args:
            value: Value to set for the timeZoneUsed property.
        """
        self._time_zone_used = value
    

