from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

agent_status = lazy_import('msgraph.generated.models.agent_status')
entity = lazy_import('msgraph.generated.models.entity')
on_premises_agent_group = lazy_import('msgraph.generated.models.on_premises_agent_group')
on_premises_publishing_type = lazy_import('msgraph.generated.models.on_premises_publishing_type')

class OnPremisesAgent(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def agent_groups(self,) -> Optional[List[on_premises_agent_group.OnPremisesAgentGroup]]:
        """
        Gets the agentGroups property value. List of onPremisesAgentGroups that an onPremisesAgent is assigned to. Read-only. Nullable.
        Returns: Optional[List[on_premises_agent_group.OnPremisesAgentGroup]]
        """
        return self._agent_groups
    
    @agent_groups.setter
    def agent_groups(self,value: Optional[List[on_premises_agent_group.OnPremisesAgentGroup]] = None) -> None:
        """
        Sets the agentGroups property value. List of onPremisesAgentGroups that an onPremisesAgent is assigned to. Read-only. Nullable.
        Args:
            value: Value to set for the agentGroups property.
        """
        self._agent_groups = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new onPremisesAgent and sets the default values.
        """
        super().__init__()
        # List of onPremisesAgentGroups that an onPremisesAgent is assigned to. Read-only. Nullable.
        self._agent_groups: Optional[List[on_premises_agent_group.OnPremisesAgentGroup]] = None
        # The external IP address as detected by the service for the agent machine. Read-only
        self._external_ip: Optional[str] = None
        # The name of the machine that the aggent is running on. Read-only
        self._machine_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[agent_status.AgentStatus] = None
        # The supportedPublishingTypes property
        self._supported_publishing_types: Optional[List[on_premises_publishing_type.OnPremisesPublishingType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesAgent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesAgent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesAgent()
    
    @property
    def external_ip(self,) -> Optional[str]:
        """
        Gets the externalIp property value. The external IP address as detected by the service for the agent machine. Read-only
        Returns: Optional[str]
        """
        return self._external_ip
    
    @external_ip.setter
    def external_ip(self,value: Optional[str] = None) -> None:
        """
        Sets the externalIp property value. The external IP address as detected by the service for the agent machine. Read-only
        Args:
            value: Value to set for the externalIp property.
        """
        self._external_ip = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "agent_groups": lambda n : setattr(self, 'agent_groups', n.get_collection_of_object_values(on_premises_agent_group.OnPremisesAgentGroup)),
            "external_ip": lambda n : setattr(self, 'external_ip', n.get_str_value()),
            "machine_name": lambda n : setattr(self, 'machine_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(agent_status.AgentStatus)),
            "supported_publishing_types": lambda n : setattr(self, 'supported_publishing_types', n.get_collection_of_enum_values(on_premises_publishing_type.OnPremisesPublishingType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def machine_name(self,) -> Optional[str]:
        """
        Gets the machineName property value. The name of the machine that the aggent is running on. Read-only
        Returns: Optional[str]
        """
        return self._machine_name
    
    @machine_name.setter
    def machine_name(self,value: Optional[str] = None) -> None:
        """
        Sets the machineName property value. The name of the machine that the aggent is running on. Read-only
        Args:
            value: Value to set for the machineName property.
        """
        self._machine_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("agentGroups", self.agent_groups)
        writer.write_str_value("externalIp", self.external_ip)
        writer.write_str_value("machineName", self.machine_name)
        writer.write_enum_value("status", self.status)
        writer.write_enum_value("supportedPublishingTypes", self.supported_publishing_types)
    
    @property
    def status(self,) -> Optional[agent_status.AgentStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[agent_status.AgentStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[agent_status.AgentStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def supported_publishing_types(self,) -> Optional[List[on_premises_publishing_type.OnPremisesPublishingType]]:
        """
        Gets the supportedPublishingTypes property value. The supportedPublishingTypes property
        Returns: Optional[List[on_premises_publishing_type.OnPremisesPublishingType]]
        """
        return self._supported_publishing_types
    
    @supported_publishing_types.setter
    def supported_publishing_types(self,value: Optional[List[on_premises_publishing_type.OnPremisesPublishingType]] = None) -> None:
        """
        Sets the supportedPublishingTypes property value. The supportedPublishingTypes property
        Args:
            value: Value to set for the supportedPublishingTypes property.
        """
        self._supported_publishing_types = value
    

