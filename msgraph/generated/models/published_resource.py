from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, on_premises_agent_group, on_premises_publishing_type

from . import entity

@dataclass
class PublishedResource(entity.Entity):
    # List of onPremisesAgentGroups that a publishedResource is assigned to. Read-only. Nullable.
    agent_groups: Optional[List[on_premises_agent_group.OnPremisesAgentGroup]] = None
    # Display Name of the publishedResource.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The publishingType property
    publishing_type: Optional[on_premises_publishing_type.OnPremisesPublishingType] = None
    # Name of the publishedResource.
    resource_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PublishedResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PublishedResource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PublishedResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, on_premises_agent_group, on_premises_publishing_type

        from . import entity, on_premises_agent_group, on_premises_publishing_type

        fields: Dict[str, Callable[[Any], None]] = {
            "agentGroups": lambda n : setattr(self, 'agent_groups', n.get_collection_of_object_values(on_premises_agent_group.OnPremisesAgentGroup)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "publishingType": lambda n : setattr(self, 'publishing_type', n.get_enum_value(on_premises_publishing_type.OnPremisesPublishingType)),
            "resourceName": lambda n : setattr(self, 'resource_name', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("agentGroups", self.agent_groups)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("publishingType", self.publishing_type)
        writer.write_str_value("resourceName", self.resource_name)
    

