from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_event_level, entity

from . import entity

@dataclass
class UserExperienceAnalyticsDeviceTimelineEvent(entity.Entity):
    """
    The user experience analytics device event entity contains NRT device event details.
    """
    # The id of the device where the event occurred.
    device_id: Optional[str] = None
    # The time the event occured.
    event_date_time: Optional[datetime] = None
    # The details provided by the event, format depends on event type.
    event_details: Optional[str] = None
    # Indicates device event level. Possible values are: None, Verbose, Information, Warning, Error, Critical
    event_level: Optional[device_event_level.DeviceEventLevel] = None
    # The name of the event. Examples include: BootEvent, LogonEvent, AppCrashEvent, AppHangEvent.
    event_name: Optional[str] = None
    # The source of the event. Examples include: Intune, Sccm.
    event_source: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
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
    

