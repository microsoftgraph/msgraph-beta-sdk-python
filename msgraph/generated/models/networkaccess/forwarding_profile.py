from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .association import Association
    from .profile import Profile
    from .traffic_forwarding_type import TrafficForwardingType

from .profile import Profile

@dataclass
class ForwardingProfile(Profile):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.forwardingProfile"
    # Specifies the users, groups, devices, and branch locations whose traffic is associated with the given traffic forwarding profile.
    associations: Optional[List[Association]] = None
    # Profile priority.
    priority: Optional[int] = None
    # The trafficForwardingType property
    traffic_forwarding_type: Optional[TrafficForwardingType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ForwardingProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ForwardingProfile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ForwardingProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .association import Association
        from .profile import Profile
        from .traffic_forwarding_type import TrafficForwardingType

        from .association import Association
        from .profile import Profile
        from .traffic_forwarding_type import TrafficForwardingType

        fields: Dict[str, Callable[[Any], None]] = {
            "associations": lambda n : setattr(self, 'associations', n.get_collection_of_object_values(Association)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "trafficForwardingType": lambda n : setattr(self, 'traffic_forwarding_type', n.get_enum_value(TrafficForwardingType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("associations", self.associations)
        writer.write_int_value("priority", self.priority)
        writer.write_enum_value("trafficForwardingType", self.traffic_forwarding_type)
    

