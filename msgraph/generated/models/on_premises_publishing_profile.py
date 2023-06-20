from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import connector, connector_group, entity, hybrid_agent_updater_configuration, on_premises_agent, on_premises_agent_group, published_resource

from . import entity

@dataclass
class OnPremisesPublishingProfile(entity.Entity):
    # List of existing onPremisesAgentGroup objects. Read-only. Nullable.
    agent_groups: Optional[List[on_premises_agent_group.OnPremisesAgentGroup]] = None
    # List of existing onPremisesAgent objects. Read-only. Nullable.
    agents: Optional[List[on_premises_agent.OnPremisesAgent]] = None
    # List of existing connectorGroup objects for applications published through Application Proxy. Read-only. Nullable.
    connector_groups: Optional[List[connector_group.ConnectorGroup]] = None
    # List of existing connector objects for applications published through Application Proxy. Read-only. Nullable.
    connectors: Optional[List[connector.Connector]] = None
    # Represents a hybridAgentUpdaterConfiguration object.
    hybrid_agent_updater_configuration: Optional[hybrid_agent_updater_configuration.HybridAgentUpdaterConfiguration] = None
    # The isDefaultAccessEnabled property
    is_default_access_enabled: Optional[bool] = None
    # Represents if Azure AD Application Proxy is enabled for the tenant.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of existing publishedResource objects. Read-only. Nullable.
    published_resources: Optional[List[published_resource.PublishedResource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesPublishingProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesPublishingProfile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesPublishingProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import connector, connector_group, entity, hybrid_agent_updater_configuration, on_premises_agent, on_premises_agent_group, published_resource

        from . import connector, connector_group, entity, hybrid_agent_updater_configuration, on_premises_agent, on_premises_agent_group, published_resource

        fields: Dict[str, Callable[[Any], None]] = {
            "agentGroups": lambda n : setattr(self, 'agent_groups', n.get_collection_of_object_values(on_premises_agent_group.OnPremisesAgentGroup)),
            "agents": lambda n : setattr(self, 'agents', n.get_collection_of_object_values(on_premises_agent.OnPremisesAgent)),
            "connectorGroups": lambda n : setattr(self, 'connector_groups', n.get_collection_of_object_values(connector_group.ConnectorGroup)),
            "connectors": lambda n : setattr(self, 'connectors', n.get_collection_of_object_values(connector.Connector)),
            "hybridAgentUpdaterConfiguration": lambda n : setattr(self, 'hybrid_agent_updater_configuration', n.get_object_value(hybrid_agent_updater_configuration.HybridAgentUpdaterConfiguration)),
            "isDefaultAccessEnabled": lambda n : setattr(self, 'is_default_access_enabled', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "publishedResources": lambda n : setattr(self, 'published_resources', n.get_collection_of_object_values(published_resource.PublishedResource)),
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
        writer.write_collection_of_object_values("agents", self.agents)
        writer.write_collection_of_object_values("connectorGroups", self.connector_groups)
        writer.write_collection_of_object_values("connectors", self.connectors)
        writer.write_object_value("hybridAgentUpdaterConfiguration", self.hybrid_agent_updater_configuration)
        writer.write_bool_value("isDefaultAccessEnabled", self.is_default_access_enabled)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_collection_of_object_values("publishedResources", self.published_resources)
    

