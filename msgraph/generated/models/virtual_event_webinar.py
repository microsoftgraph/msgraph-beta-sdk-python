from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import communications_user_identity, meeting_audience, virtual_event, virtual_event_registration

from . import virtual_event

class VirtualEventWebinar(virtual_event.VirtualEvent):
    def __init__(self,) -> None:
        """
        Instantiates a new VirtualEventWebinar and sets the default values.
        """
        super().__init__()
        # The audience property
        self._audience: Optional[meeting_audience.MeetingAudience] = None
        # The coOrganizers property
        self._co_organizers: Optional[List[communications_user_identity.CommunicationsUserIdentity]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The registration property
        self._registration: Optional[virtual_event_registration.VirtualEventRegistration] = None
    
    @property
    def audience(self,) -> Optional[meeting_audience.MeetingAudience]:
        """
        Gets the audience property value. The audience property
        Returns: Optional[meeting_audience.MeetingAudience]
        """
        return self._audience
    
    @audience.setter
    def audience(self,value: Optional[meeting_audience.MeetingAudience] = None) -> None:
        """
        Sets the audience property value. The audience property
        Args:
            value: Value to set for the audience property.
        """
        self._audience = value
    
    @property
    def co_organizers(self,) -> Optional[List[communications_user_identity.CommunicationsUserIdentity]]:
        """
        Gets the coOrganizers property value. The coOrganizers property
        Returns: Optional[List[communications_user_identity.CommunicationsUserIdentity]]
        """
        return self._co_organizers
    
    @co_organizers.setter
    def co_organizers(self,value: Optional[List[communications_user_identity.CommunicationsUserIdentity]] = None) -> None:
        """
        Sets the coOrganizers property value. The coOrganizers property
        Args:
            value: Value to set for the co_organizers property.
        """
        self._co_organizers = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventWebinar:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventWebinar
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VirtualEventWebinar()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import communications_user_identity, meeting_audience, virtual_event, virtual_event_registration

        fields: Dict[str, Callable[[Any], None]] = {
            "audience": lambda n : setattr(self, 'audience', n.get_enum_value(meeting_audience.MeetingAudience)),
            "coOrganizers": lambda n : setattr(self, 'co_organizers', n.get_collection_of_object_values(communications_user_identity.CommunicationsUserIdentity)),
            "registration": lambda n : setattr(self, 'registration', n.get_object_value(virtual_event_registration.VirtualEventRegistration)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def registration(self,) -> Optional[virtual_event_registration.VirtualEventRegistration]:
        """
        Gets the registration property value. The registration property
        Returns: Optional[virtual_event_registration.VirtualEventRegistration]
        """
        return self._registration
    
    @registration.setter
    def registration(self,value: Optional[virtual_event_registration.VirtualEventRegistration] = None) -> None:
        """
        Sets the registration property value. The registration property
        Args:
            value: Value to set for the registration property.
        """
        self._registration = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("audience", self.audience)
        writer.write_collection_of_object_values("coOrganizers", self.co_organizers)
        writer.write_object_value("registration", self.registration)
    

