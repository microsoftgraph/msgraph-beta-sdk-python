from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import meeting_participant_info, virtual_event_presenter_details

from . import meeting_participant_info

class VirtualEventPresenterInfo(meeting_participant_info.MeetingParticipantInfo):
    def __init__(self,) -> None:
        """
        Instantiates a new VirtualEventPresenterInfo and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.virtualEventPresenterInfo"
        # The presenterDetails property
        self._presenter_details: Optional[virtual_event_presenter_details.VirtualEventPresenterDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventPresenterInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventPresenterInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VirtualEventPresenterInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import meeting_participant_info, virtual_event_presenter_details

        fields: Dict[str, Callable[[Any], None]] = {
            "presenterDetails": lambda n : setattr(self, 'presenter_details', n.get_object_value(virtual_event_presenter_details.VirtualEventPresenterDetails)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def presenter_details(self,) -> Optional[virtual_event_presenter_details.VirtualEventPresenterDetails]:
        """
        Gets the presenterDetails property value. The presenterDetails property
        Returns: Optional[virtual_event_presenter_details.VirtualEventPresenterDetails]
        """
        return self._presenter_details
    
    @presenter_details.setter
    def presenter_details(self,value: Optional[virtual_event_presenter_details.VirtualEventPresenterDetails] = None) -> None:
        """
        Sets the presenterDetails property value. The presenterDetails property
        Args:
            value: Value to set for the presenter_details property.
        """
        self._presenter_details = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("presenterDetails", self.presenter_details)
    

