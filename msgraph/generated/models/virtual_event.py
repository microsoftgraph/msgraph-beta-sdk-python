from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import communications_identity_set, date_time_time_zone, entity, virtual_event_presenter, virtual_event_session, virtual_event_status, virtual_event_webinar

from . import entity

class VirtualEvent(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new virtualEvent and sets the default values.
        """
        super().__init__()
        # The createdBy property
        self._created_by: Optional[communications_identity_set.CommunicationsIdentitySet] = None
        # The description property
        self._description: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The endDateTime property
        self._end_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The presenters property
        self._presenters: Optional[List[virtual_event_presenter.VirtualEventPresenter]] = None
        # The sessions property
        self._sessions: Optional[List[virtual_event_session.VirtualEventSession]] = None
        # The startDateTime property
        self._start_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The status property
        self._status: Optional[virtual_event_status.VirtualEventStatus] = None
    
    @property
    def created_by(self,) -> Optional[communications_identity_set.CommunicationsIdentitySet]:
        """
        Gets the createdBy property value. The createdBy property
        Returns: Optional[communications_identity_set.CommunicationsIdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[communications_identity_set.CommunicationsIdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The createdBy property
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.virtualEventWebinar":
                from . import virtual_event_webinar

                return virtual_event_webinar.VirtualEventWebinar()
        return VirtualEvent()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def end_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the endDateTime property value. The endDateTime property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the endDateTime property value. The endDateTime property
        Args:
            value: Value to set for the end_date_time property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import communications_identity_set, date_time_time_zone, entity, virtual_event_presenter, virtual_event_session, virtual_event_status, virtual_event_webinar

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(communications_identity_set.CommunicationsIdentitySet)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "presenters": lambda n : setattr(self, 'presenters', n.get_collection_of_object_values(virtual_event_presenter.VirtualEventPresenter)),
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(virtual_event_session.VirtualEventSession)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(virtual_event_status.VirtualEventStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def presenters(self,) -> Optional[List[virtual_event_presenter.VirtualEventPresenter]]:
        """
        Gets the presenters property value. The presenters property
        Returns: Optional[List[virtual_event_presenter.VirtualEventPresenter]]
        """
        return self._presenters
    
    @presenters.setter
    def presenters(self,value: Optional[List[virtual_event_presenter.VirtualEventPresenter]] = None) -> None:
        """
        Sets the presenters property value. The presenters property
        Args:
            value: Value to set for the presenters property.
        """
        self._presenters = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("endDateTime", self.end_date_time)
        writer.write_collection_of_object_values("presenters", self.presenters)
        writer.write_collection_of_object_values("sessions", self.sessions)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
    
    @property
    def sessions(self,) -> Optional[List[virtual_event_session.VirtualEventSession]]:
        """
        Gets the sessions property value. The sessions property
        Returns: Optional[List[virtual_event_session.VirtualEventSession]]
        """
        return self._sessions
    
    @sessions.setter
    def sessions(self,value: Optional[List[virtual_event_session.VirtualEventSession]] = None) -> None:
        """
        Sets the sessions property value. The sessions property
        Args:
            value: Value to set for the sessions property.
        """
        self._sessions = value
    
    @property
    def start_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the startDateTime property value. The startDateTime property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the startDateTime property value. The startDateTime property
        Args:
            value: Value to set for the start_date_time property.
        """
        self._start_date_time = value
    
    @property
    def status(self,) -> Optional[virtual_event_status.VirtualEventStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[virtual_event_status.VirtualEventStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[virtual_event_status.VirtualEventStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

