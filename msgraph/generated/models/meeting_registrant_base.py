from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, external_meeting_registrant, meeting_registrant

from . import entity

class MeetingRegistrantBase(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new meetingRegistrantBase and sets the default values.
        """
        super().__init__()
        # A unique web URL for the registrant to join the meeting. Read-only.
        self._join_web_url: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingRegistrantBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingRegistrantBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.externalMeetingRegistrant":
                from . import external_meeting_registrant

                return external_meeting_registrant.ExternalMeetingRegistrant()
            if mapping_value == "#microsoft.graph.meetingRegistrant":
                from . import meeting_registrant

                return meeting_registrant.MeetingRegistrant()
        return MeetingRegistrantBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, external_meeting_registrant, meeting_registrant

        fields: Dict[str, Callable[[Any], None]] = {
            "joinWebUrl": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def join_web_url(self,) -> Optional[str]:
        """
        Gets the joinWebUrl property value. A unique web URL for the registrant to join the meeting. Read-only.
        Returns: Optional[str]
        """
        return self._join_web_url
    
    @join_web_url.setter
    def join_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the joinWebUrl property value. A unique web URL for the registrant to join the meeting. Read-only.
        Args:
            value: Value to set for the join_web_url property.
        """
        self._join_web_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("joinWebUrl", self.join_web_url)
    

