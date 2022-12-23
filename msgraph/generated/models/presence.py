from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
out_of_office_settings = lazy_import('msgraph.generated.models.out_of_office_settings')
presence_status_message = lazy_import('msgraph.generated.models.presence_status_message')

class Presence(entity.Entity):
    @property
    def activity(self,) -> Optional[str]:
        """
        Gets the activity property value. The supplemental information to a user's availability. Possible values are Available, Away, BeRightBack, Busy, DoNotDisturb, InACall, InAConferenceCall, Inactive,InAMeeting, Offline, OffWork,OutOfOffice, PresenceUnknown,Presenting, UrgentInterruptionsOnly.
        Returns: Optional[str]
        """
        return self._activity
    
    @activity.setter
    def activity(self,value: Optional[str] = None) -> None:
        """
        Sets the activity property value. The supplemental information to a user's availability. Possible values are Available, Away, BeRightBack, Busy, DoNotDisturb, InACall, InAConferenceCall, Inactive,InAMeeting, Offline, OffWork,OutOfOffice, PresenceUnknown,Presenting, UrgentInterruptionsOnly.
        Args:
            value: Value to set for the activity property.
        """
        self._activity = value
    
    @property
    def availability(self,) -> Optional[str]:
        """
        Gets the availability property value. The base presence information for a user. Possible values are Available, AvailableIdle,  Away, BeRightBack, Busy, BusyIdle, DoNotDisturb, Offline, PresenceUnknown
        Returns: Optional[str]
        """
        return self._availability
    
    @availability.setter
    def availability(self,value: Optional[str] = None) -> None:
        """
        Sets the availability property value. The base presence information for a user. Possible values are Available, AvailableIdle,  Away, BeRightBack, Busy, BusyIdle, DoNotDisturb, Offline, PresenceUnknown
        Args:
            value: Value to set for the availability property.
        """
        self._availability = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new presence and sets the default values.
        """
        super().__init__()
        # The supplemental information to a user's availability. Possible values are Available, Away, BeRightBack, Busy, DoNotDisturb, InACall, InAConferenceCall, Inactive,InAMeeting, Offline, OffWork,OutOfOffice, PresenceUnknown,Presenting, UrgentInterruptionsOnly.
        self._activity: Optional[str] = None
        # The base presence information for a user. Possible values are Available, AvailableIdle,  Away, BeRightBack, Busy, BusyIdle, DoNotDisturb, Offline, PresenceUnknown
        self._availability: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The out of office settings for a user.
        self._out_of_office_settings: Optional[out_of_office_settings.OutOfOfficeSettings] = None
        # The presence status message of a user.
        self._status_message: Optional[presence_status_message.PresenceStatusMessage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Presence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Presence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Presence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity": lambda n : setattr(self, 'activity', n.get_str_value()),
            "availability": lambda n : setattr(self, 'availability', n.get_str_value()),
            "out_of_office_settings": lambda n : setattr(self, 'out_of_office_settings', n.get_object_value(out_of_office_settings.OutOfOfficeSettings)),
            "status_message": lambda n : setattr(self, 'status_message', n.get_object_value(presence_status_message.PresenceStatusMessage)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def out_of_office_settings(self,) -> Optional[out_of_office_settings.OutOfOfficeSettings]:
        """
        Gets the outOfOfficeSettings property value. The out of office settings for a user.
        Returns: Optional[out_of_office_settings.OutOfOfficeSettings]
        """
        return self._out_of_office_settings
    
    @out_of_office_settings.setter
    def out_of_office_settings(self,value: Optional[out_of_office_settings.OutOfOfficeSettings] = None) -> None:
        """
        Sets the outOfOfficeSettings property value. The out of office settings for a user.
        Args:
            value: Value to set for the outOfOfficeSettings property.
        """
        self._out_of_office_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("activity", self.activity)
        writer.write_str_value("availability", self.availability)
        writer.write_object_value("outOfOfficeSettings", self.out_of_office_settings)
        writer.write_object_value("statusMessage", self.status_message)
    
    @property
    def status_message(self,) -> Optional[presence_status_message.PresenceStatusMessage]:
        """
        Gets the statusMessage property value. The presence status message of a user.
        Returns: Optional[presence_status_message.PresenceStatusMessage]
        """
        return self._status_message
    
    @status_message.setter
    def status_message(self,value: Optional[presence_status_message.PresenceStatusMessage] = None) -> None:
        """
        Sets the statusMessage property value. The presence status message of a user.
        Args:
            value: Value to set for the statusMessage property.
        """
        self._status_message = value
    

