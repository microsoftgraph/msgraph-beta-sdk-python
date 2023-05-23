from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, virtual_event, virtual_event_webinar

from . import entity

class VirtualEventsRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new VirtualEventsRoot and sets the default values.
        """
        super().__init__()
        # The events property
        self._events: Optional[List[virtual_event.VirtualEvent]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The webinars property
        self._webinars: Optional[List[virtual_event_webinar.VirtualEventWebinar]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventsRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VirtualEventsRoot()
    
    @property
    def events(self,) -> Optional[List[virtual_event.VirtualEvent]]:
        """
        Gets the events property value. The events property
        Returns: Optional[List[virtual_event.VirtualEvent]]
        """
        return self._events
    
    @events.setter
    def events(self,value: Optional[List[virtual_event.VirtualEvent]] = None) -> None:
        """
        Sets the events property value. The events property
        Args:
            value: Value to set for the events property.
        """
        self._events = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, virtual_event, virtual_event_webinar

        fields: Dict[str, Callable[[Any], None]] = {
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(virtual_event.VirtualEvent)),
            "webinars": lambda n : setattr(self, 'webinars', n.get_collection_of_object_values(virtual_event_webinar.VirtualEventWebinar)),
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
        writer.write_collection_of_object_values("events", self.events)
        writer.write_collection_of_object_values("webinars", self.webinars)
    
    @property
    def webinars(self,) -> Optional[List[virtual_event_webinar.VirtualEventWebinar]]:
        """
        Gets the webinars property value. The webinars property
        Returns: Optional[List[virtual_event_webinar.VirtualEventWebinar]]
        """
        return self._webinars
    
    @webinars.setter
    def webinars(self,value: Optional[List[virtual_event_webinar.VirtualEventWebinar]] = None) -> None:
        """
        Sets the webinars property value. The webinars property
        Args:
            value: Value to set for the webinars property.
        """
        self._webinars = value
    

