from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .forwarding_profile import ForwardingProfile
    from .policy_link import PolicyLink
    from .status import Status

from ..entity import Entity

@dataclass
class Profile(Entity):
    # Description.
    description: Optional[str] = None
    # Profile last modified time.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Profile name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Traffic forwarding policies associated with this profile.
    policies: Optional[List[PolicyLink]] = None
    # The state property
    state: Optional[Status] = None
    # Profile version.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Profile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Profile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingProfile".casefold():
            from .forwarding_profile import ForwardingProfile

            return ForwardingProfile()
        return Profile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .forwarding_profile import ForwardingProfile
        from .policy_link import PolicyLink
        from .status import Status

        from ..entity import Entity
        from .forwarding_profile import ForwardingProfile
        from .policy_link import PolicyLink
        from .status import Status

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(PolicyLink)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(Status)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("policies", self.policies)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("version", self.version)
    

