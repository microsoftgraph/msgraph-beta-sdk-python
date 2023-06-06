from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, on_premises_agent, on_premises_publishing_type, published_resource

from . import entity

@dataclass
class OnPremisesAgentGroup(entity.Entity):
    # List of onPremisesAgent that are assigned to an onPremisesAgentGroup. Read-only. Nullable.
    agents: Optional[List[on_premises_agent.OnPremisesAgent]] = None
    # Display name of the onPremisesAgentGroup.
    display_name: Optional[str] = None
    # Indicates if the onPremisesAgentGroup is the default agent group. Only a single agent group can be the default onPremisesAgentGroup and is set by the system.
    is_default: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of publishedResource that are assigned to an onPremisesAgentGroup. Read-only. Nullable.
    published_resources: Optional[List[published_resource.PublishedResource]] = None
    # The publishingType property
    publishing_type: Optional[on_premises_publishing_type.OnPremisesPublishingType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesAgentGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesAgentGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesAgentGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, on_premises_agent, on_premises_publishing_type, published_resource

        fields: Dict[str, Callable[[Any], None]] = {
            "agents": lambda n : setattr(self, 'agents', n.get_collection_of_object_values(on_premises_agent.OnPremisesAgent)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "publishedResources": lambda n : setattr(self, 'published_resources', n.get_collection_of_object_values(published_resource.PublishedResource)),
            "publishingType": lambda n : setattr(self, 'publishing_type', n.get_enum_value(on_premises_publishing_type.OnPremisesPublishingType)),
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
        writer.write_collection_of_object_values("agents", self.agents)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_collection_of_object_values("publishedResources", self.published_resources)
        writer.write_enum_value("publishingType", self.publishing_type)
    

