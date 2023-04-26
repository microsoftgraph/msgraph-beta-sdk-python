from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_event_level, entity

from . import entity

class UserExperienceAnalyticsDeviceTimelineEvent(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new UserExperienceAnalyticsDeviceTimelineEvent and sets the default values.
        """
        super().__init__()
        # The id of the device where the event occurred.
        self._device_id: Optional[str] = None
        # The time the event occured.
        self._event_date_time: Optional[datetime] = None
        # The details provided by the event, format depends on event type.
        self._event_details: Optional[str] = None
        # Indicates device event level. Possible values are: None, Verbose, Information, Warning, Error, Critical
        self._event_level: Optional[device_event_level.DeviceEventLevel] = None
        # The name of the event. Examples include: BootEvent, LogonEvent, AppCrashEvent, AppHangEvent.
        self._event_name: Optional[str] = None
        # The source of the event. Examples include: Intune, Sccm.
        self._event_source: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDeviceTimelineEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceTimelineEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsDeviceTimelineEvent()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The id of the device where the event occurred.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The id of the device where the event occurred.
        Args:
            value: Value to set for the device_id property.
        """
        self._device_id = value
    
    @property
    def event_date_time(self,) -> Optional[datetime]:
        """
        Gets the eventDateTime property value. The time the event occured.
        Returns: Optional[datetime]
        """
        return self._event_date_time
    
    @event_date_time.setter
    def event_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the eventDateTime property value. The time the event occured.
        Args:
            value: Value to set for the event_date_time property.
        """
        self._event_date_time = value
    
    @property
    def event_details(self,) -> Optional[str]:
        """
        Gets the eventDetails property value. The details provided by the event, format depends on event type.
        Returns: Optional[str]
        """
        return self._event_details
    
    @event_details.setter
    def event_details(self,value: Optional[str] = None) -> None:
        """
        Sets the eventDetails property value. The details provided by the event, format depends on event type.
        Args:
            value: Value to set for the event_details property.
        """
        self._event_details = value
    
    @property
    def event_level(self,) -> Optional[device_event_level.DeviceEventLevel]:
        """
        Gets the eventLevel property value. Indicates device event level. Possible values are: None, Verbose, Information, Warning, Error, Critical
        Returns: Optional[device_event_level.DeviceEventLevel]
        """
        return self._event_level
    
    @event_level.setter
    def event_level(self,value: Optional[device_event_level.DeviceEventLevel] = None) -> None:
        """
        Sets the eventLevel property value. Indicates device event level. Possible values are: None, Verbose, Information, Warning, Error, Critical
        Args:
            value: Value to set for the event_level property.
        """
        self._event_level = value
    
    @property
    def event_name(self,) -> Optional[str]:
        """
        Gets the eventName property value. The name of the event. Examples include: BootEvent, LogonEvent, AppCrashEvent, AppHangEvent.
        Returns: Optional[str]
        """
        return self._event_name
    
    @event_name.setter
    def event_name(self,value: Optional[str] = None) -> None:
        """
        Sets the eventName property value. The name of the event. Examples include: BootEvent, LogonEvent, AppCrashEvent, AppHangEvent.
        Args:
            value: Value to set for the event_name property.
        """
        self._event_name = value
    
    @property
    def event_source(self,) -> Optional[str]:
        """
        Gets the eventSource property value. The source of the event. Examples include: Intune, Sccm.
        Returns: Optional[str]
        """
        return self._event_source
    
    @event_source.setter
    def event_source(self,value: Optional[str] = None) -> None:
        """
        Sets the eventSource property value. The source of the event. Examples include: Intune, Sccm.
        Args:
            value: Value to set for the event_source property.
        """
        self._event_source = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_event_level, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "eventDetails": lambda n : setattr(self, 'event_details', n.get_str_value()),
            "eventLevel": lambda n : setattr(self, 'event_level', n.get_enum_value(device_event_level.DeviceEventLevel)),
            "eventName": lambda n : setattr(self, 'event_name', n.get_str_value()),
            "eventSource": lambda n : setattr(self, 'event_source', n.get_str_value()),
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
        writer.write_str_value("deviceId", self.device_id)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("eventDetails", self.event_details)
        writer.write_enum_value("eventLevel", self.event_level)
        writer.write_str_value("eventName", self.event_name)
        writer.write_str_value("eventSource", self.event_source)
    

