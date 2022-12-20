from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
status = lazy_import('msgraph.generated.models.status')
user_activity = lazy_import('msgraph.generated.models.user_activity')

class ActivityHistoryItem(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def active_duration_seconds(self,) -> Optional[int]:
        """
        Gets the activeDurationSeconds property value. The activeDurationSeconds property
        Returns: Optional[int]
        """
        return self._active_duration_seconds
    
    @active_duration_seconds.setter
    def active_duration_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the activeDurationSeconds property value. The activeDurationSeconds property
        Args:
            value: Value to set for the activeDurationSeconds property.
        """
        self._active_duration_seconds = value
    
    @property
    def activity(self,) -> Optional[user_activity.UserActivity]:
        """
        Gets the activity property value. The activity property
        Returns: Optional[user_activity.UserActivity]
        """
        return self._activity
    
    @activity.setter
    def activity(self,value: Optional[user_activity.UserActivity] = None) -> None:
        """
        Sets the activity property value. The activity property
        Args:
            value: Value to set for the activity property.
        """
        self._activity = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new activityHistoryItem and sets the default values.
        """
        super().__init__()
        # The activeDurationSeconds property
        self._active_duration_seconds: Optional[int] = None
        # The activity property
        self._activity: Optional[user_activity.UserActivity] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The expirationDateTime property
        self._expiration_date_time: Optional[datetime] = None
        # The lastActiveDateTime property
        self._last_active_date_time: Optional[datetime] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The startedDateTime property
        self._started_date_time: Optional[datetime] = None
        # The status property
        self._status: Optional[status.Status] = None
        # The userTimezone property
        self._user_timezone: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ActivityHistoryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ActivityHistoryItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ActivityHistoryItem()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The expirationDateTime property
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The expirationDateTime property
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_duration_seconds": lambda n : setattr(self, 'active_duration_seconds', n.get_int_value()),
            "activity": lambda n : setattr(self, 'activity', n.get_object_value(user_activity.UserActivity)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "last_active_date_time": lambda n : setattr(self, 'last_active_date_time', n.get_datetime_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "started_date_time": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(status.Status)),
            "user_timezone": lambda n : setattr(self, 'user_timezone', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_active_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActiveDateTime property value. The lastActiveDateTime property
        Returns: Optional[datetime]
        """
        return self._last_active_date_time
    
    @last_active_date_time.setter
    def last_active_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActiveDateTime property value. The lastActiveDateTime property
        Args:
            value: Value to set for the lastActiveDateTime property.
        """
        self._last_active_date_time = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("activeDurationSeconds", self.active_duration_seconds)
        writer.write_object_value("activity", self.activity)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("lastActiveDateTime", self.last_active_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userTimezone", self.user_timezone)
    
    @property
    def started_date_time(self,) -> Optional[datetime]:
        """
        Gets the startedDateTime property value. The startedDateTime property
        Returns: Optional[datetime]
        """
        return self._started_date_time
    
    @started_date_time.setter
    def started_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startedDateTime property value. The startedDateTime property
        Args:
            value: Value to set for the startedDateTime property.
        """
        self._started_date_time = value
    
    @property
    def status(self,) -> Optional[status.Status]:
        """
        Gets the status property value. The status property
        Returns: Optional[status.Status]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[status.Status] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def user_timezone(self,) -> Optional[str]:
        """
        Gets the userTimezone property value. The userTimezone property
        Returns: Optional[str]
        """
        return self._user_timezone
    
    @user_timezone.setter
    def user_timezone(self,value: Optional[str] = None) -> None:
        """
        Sets the userTimezone property value. The userTimezone property
        Args:
            value: Value to set for the userTimezone property.
        """
        self._user_timezone = value
    

