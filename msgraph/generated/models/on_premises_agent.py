from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import agent_status, entity, on_premises_agent_group, on_premises_publishing_type

from . import entity

@dataclass
class OnPremisesAgent(entity.Entity):
    # List of onPremisesAgentGroups that an onPremisesAgent is assigned to. Read-only. Nullable.
    agent_groups: Optional[List[on_premises_agent_group.OnPremisesAgentGroup]] = None
    # The external IP address as detected by the service for the agent machine. Read-only
    external_ip: Optional[str] = None
    # The name of the machine that the aggent is running on. Read-only
    machine_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[agent_status.AgentStatus] = None
    # The supportedPublishingTypes property
    supported_publishing_types: Optional[List[on_premises_publishing_type.OnPremisesPublishingType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesAgent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesAgent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesAgent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import agent_status, entity, on_premises_agent_group, on_premises_publishing_type

        from . import agent_status, entity, on_premises_agent_group, on_premises_publishing_type

        fields: Dict[str, Callable[[Any], None]] = {
            "agentGroups": lambda n : setattr(self, 'agent_groups', n.get_collection_of_object_values(on_premises_agent_group.OnPremisesAgentGroup)),
            "externalIp": lambda n : setattr(self, 'external_ip', n.get_str_value()),
            "machineName": lambda n : setattr(self, 'machine_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(agent_status.AgentStatus)),
            "supportedPublishingTypes": lambda n : setattr(self, 'supported_publishing_types', n.get_collection_of_enum_values(on_premises_publishing_type.OnPremisesPublishingType)),
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
        writer.write_str_value("externalIp", self.external_ip)
        writer.write_str_value("machineName", self.machine_name)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_enum_values("supportedPublishingTypes", self.supported_publishing_types)
    

