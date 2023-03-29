from __future__ import annotations
from datetime import date, timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import analytics_activity_type, call_activity_statistics, chat_activity_statistics, email_activity_statistics, entity, focus_activity_statistics, meeting_activity_statistics

from . import entity

class ActivityStatistics(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new activityStatistics and sets the default values.
        """
        super().__init__()
        # The type of activity for which statistics are returned. The possible values are: call, chat, email, focus, and meeting.
        self._activity: Optional[analytics_activity_type.AnalyticsActivityType] = None
        # Total hours spent on the activity. The value is represented in ISO 8601 format for durations.
        self._duration: Optional[timedelta] = None
        # Date when the activity ended, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-03' that follows the YYYY-MM-DD format.
        self._end_date: Optional[date] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Date when the activity started, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-04' that follows the YYYY-MM-DD format.
        self._start_date: Optional[date] = None
        # The time zone that the user sets in Microsoft Outlook is used for the computation. For example, the property value could be 'Pacific Standard Time.'
        self._time_zone_used: Optional[str] = None
    
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
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.callActivityStatistics":
                from . import call_activity_statistics

                return call_activity_statistics.CallActivityStatistics()
            if mapping_value == "#microsoft.graph.chatActivityStatistics":
                from . import chat_activity_statistics

                return chat_activity_statistics.ChatActivityStatistics()
            if mapping_value == "#microsoft.graph.emailActivityStatistics":
                from . import email_activity_statistics

                return email_activity_statistics.EmailActivityStatistics()
            if mapping_value == "#microsoft.graph.focusActivityStatistics":
                from . import focus_activity_statistics

                return focus_activity_statistics.FocusActivityStatistics()
            if mapping_value == "#microsoft.graph.meetingActivityStatistics":
                from . import meeting_activity_statistics

                return meeting_activity_statistics.MeetingActivityStatistics()
        return ActivityStatistics()
    
    @property
    def duration(self,) -> Optional[timedelta]:
        """
        Gets the duration property value. Total hours spent on the activity. The value is represented in ISO 8601 format for durations.
        Returns: Optional[timedelta]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the duration property value. Total hours spent on the activity. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    @property
    def end_date(self,) -> Optional[date]:
        """
        Gets the endDate property value. Date when the activity ended, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-03' that follows the YYYY-MM-DD format.
        Returns: Optional[date]
        """
        return self._end_date
    
    @end_date.setter
    def end_date(self,value: Optional[date] = None) -> None:
        """
        Sets the endDate property value. Date when the activity ended, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-03' that follows the YYYY-MM-DD format.
        Args:
            value: Value to set for the end_date property.
        """
        self._end_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import analytics_activity_type, call_activity_statistics, chat_activity_statistics, email_activity_statistics, entity, focus_activity_statistics, meeting_activity_statistics

        fields: Dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_enum_value(analytics_activity_type.AnalyticsActivityType)),
            "duration": lambda n : setattr(self, 'duration', n.get_timedelta_value()),
            "endDate": lambda n : setattr(self, 'end_date', n.get_date_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
            "timeZoneUsed": lambda n : setattr(self, 'time_zone_used', n.get_str_value()),
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
        writer.write_timedelta_value("duration", self.duration)
        writer.write_date_value("endDate", self.end_date)
        writer.write_date_value("startDate", self.start_date)
        writer.write_str_value("timeZoneUsed", self.time_zone_used)
    
    @property
    def start_date(self,) -> Optional[date]:
        """
        Gets the startDate property value. Date when the activity started, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-04' that follows the YYYY-MM-DD format.
        Returns: Optional[date]
        """
        return self._start_date
    
    @start_date.setter
    def start_date(self,value: Optional[date] = None) -> None:
        """
        Sets the startDate property value. Date when the activity started, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-04' that follows the YYYY-MM-DD format.
        Args:
            value: Value to set for the start_date property.
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
            value: Value to set for the time_zone_used property.
        """
        self._time_zone_used = value
    

