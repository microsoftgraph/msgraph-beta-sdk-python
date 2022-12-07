from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

connector = lazy_import('msgraph.generated.models.connector')
connector_group = lazy_import('msgraph.generated.models.connector_group')
entity = lazy_import('msgraph.generated.models.entity')
hybrid_agent_updater_configuration = lazy_import('msgraph.generated.models.hybrid_agent_updater_configuration')
on_premises_agent = lazy_import('msgraph.generated.models.on_premises_agent')
on_premises_agent_group = lazy_import('msgraph.generated.models.on_premises_agent_group')
published_resource = lazy_import('msgraph.generated.models.published_resource')

class OnPremisesPublishingProfile(entity.Entity):
    @property
    def agent_groups(self,) -> Optional[List[on_premises_agent_group.OnPremisesAgentGroup]]:
        """
        Gets the agentGroups property value. List of existing onPremisesAgentGroup objects. Read-only. Nullable.
        Returns: Optional[List[on_premises_agent_group.OnPremisesAgentGroup]]
        """
        return self._agent_groups
    
    @agent_groups.setter
    def agent_groups(self,value: Optional[List[on_premises_agent_group.OnPremisesAgentGroup]] = None) -> None:
        """
        Sets the agentGroups property value. List of existing onPremisesAgentGroup objects. Read-only. Nullable.
        Args:
            value: Value to set for the agentGroups property.
        """
        self._agent_groups = value
    
    @property
    def agents(self,) -> Optional[List[on_premises_agent.OnPremisesAgent]]:
        """
        Gets the agents property value. List of existing onPremisesAgent objects. Read-only. Nullable.
        Returns: Optional[List[on_premises_agent.OnPremisesAgent]]
        """
        return self._agents
    
    @agents.setter
    def agents(self,value: Optional[List[on_premises_agent.OnPremisesAgent]] = None) -> None:
        """
        Sets the agents property value. List of existing onPremisesAgent objects. Read-only. Nullable.
        Args:
            value: Value to set for the agents property.
        """
        self._agents = value
    
    @property
    def connector_groups(self,) -> Optional[List[connector_group.ConnectorGroup]]:
        """
        Gets the connectorGroups property value. List of existing connectorGroup objects for applications published through Application Proxy. Read-only. Nullable.
        Returns: Optional[List[connector_group.ConnectorGroup]]
        """
        return self._connector_groups
    
    @connector_groups.setter
    def connector_groups(self,value: Optional[List[connector_group.ConnectorGroup]] = None) -> None:
        """
        Sets the connectorGroups property value. List of existing connectorGroup objects for applications published through Application Proxy. Read-only. Nullable.
        Args:
            value: Value to set for the connectorGroups property.
        """
        self._connector_groups = value
    
    @property
    def connectors(self,) -> Optional[List[connector.Connector]]:
        """
        Gets the connectors property value. List of existing connector objects for applications published through Application Proxy. Read-only. Nullable.
        Returns: Optional[List[connector.Connector]]
        """
        return self._connectors
    
    @connectors.setter
    def connectors(self,value: Optional[List[connector.Connector]] = None) -> None:
        """
        Sets the connectors property value. List of existing connector objects for applications published through Application Proxy. Read-only. Nullable.
        Args:
            value: Value to set for the connectors property.
        """
        self._connectors = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new OnPremisesPublishingProfile and sets the default values.
        """
        super().__init__()
        # List of existing onPremisesAgentGroup objects. Read-only. Nullable.
        self._agent_groups: Optional[List[on_premises_agent_group.OnPremisesAgentGroup]] = None
        # List of existing onPremisesAgent objects. Read-only. Nullable.
        self._agents: Optional[List[on_premises_agent.OnPremisesAgent]] = None
        # List of existing connectorGroup objects for applications published through Application Proxy. Read-only. Nullable.
        self._connector_groups: Optional[List[connector_group.ConnectorGroup]] = None
        # List of existing connector objects for applications published through Application Proxy. Read-only. Nullable.
        self._connectors: Optional[List[connector.Connector]] = None
        # Represents a hybridAgentUpdaterConfiguration object.
        self._hybrid_agent_updater_configuration: Optional[hybrid_agent_updater_configuration.HybridAgentUpdaterConfiguration] = None
        # The isDefaultAccessEnabled property
        self._is_default_access_enabled: Optional[bool] = None
        # Represents if Azure AD Application Proxy is enabled for the tenant.
        self._is_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of existing publishedResource objects. Read-only. Nullable.
        self._published_resources: Optional[List[published_resource.PublishedResource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesPublishingProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesPublishingProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesPublishingProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "agent_groups": lambda n : setattr(self, 'agent_groups', n.get_collection_of_object_values(on_premises_agent_group.OnPremisesAgentGroup)),
            "agents": lambda n : setattr(self, 'agents', n.get_collection_of_object_values(on_premises_agent.OnPremisesAgent)),
            "connector_groups": lambda n : setattr(self, 'connector_groups', n.get_collection_of_object_values(connector_group.ConnectorGroup)),
            "connectors": lambda n : setattr(self, 'connectors', n.get_collection_of_object_values(connector.Connector)),
            "hybrid_agent_updater_configuration": lambda n : setattr(self, 'hybrid_agent_updater_configuration', n.get_object_value(hybrid_agent_updater_configuration.HybridAgentUpdaterConfiguration)),
            "is_default_access_enabled": lambda n : setattr(self, 'is_default_access_enabled', n.get_bool_value()),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "published_resources": lambda n : setattr(self, 'published_resources', n.get_collection_of_object_values(published_resource.PublishedResource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hybrid_agent_updater_configuration(self,) -> Optional[hybrid_agent_updater_configuration.HybridAgentUpdaterConfiguration]:
        """
        Gets the hybridAgentUpdaterConfiguration property value. Represents a hybridAgentUpdaterConfiguration object.
        Returns: Optional[hybrid_agent_updater_configuration.HybridAgentUpdaterConfiguration]
        """
        return self._hybrid_agent_updater_configuration
    
    @hybrid_agent_updater_configuration.setter
    def hybrid_agent_updater_configuration(self,value: Optional[hybrid_agent_updater_configuration.HybridAgentUpdaterConfiguration] = None) -> None:
        """
        Sets the hybridAgentUpdaterConfiguration property value. Represents a hybridAgentUpdaterConfiguration object.
        Args:
            value: Value to set for the hybridAgentUpdaterConfiguration property.
        """
        self._hybrid_agent_updater_configuration = value
    
    @property
    def is_default_access_enabled(self,) -> Optional[bool]:
        """
        Gets the isDefaultAccessEnabled property value. The isDefaultAccessEnabled property
        Returns: Optional[bool]
        """
        return self._is_default_access_enabled
    
    @is_default_access_enabled.setter
    def is_default_access_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefaultAccessEnabled property value. The isDefaultAccessEnabled property
        Args:
            value: Value to set for the isDefaultAccessEnabled property.
        """
        self._is_default_access_enabled = value
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Represents if Azure AD Application Proxy is enabled for the tenant.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Represents if Azure AD Application Proxy is enabled for the tenant.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    @property
    def published_resources(self,) -> Optional[List[published_resource.PublishedResource]]:
        """
        Gets the publishedResources property value. List of existing publishedResource objects. Read-only. Nullable.
        Returns: Optional[List[published_resource.PublishedResource]]
        """
        return self._published_resources
    
    @published_resources.setter
    def published_resources(self,value: Optional[List[published_resource.PublishedResource]] = None) -> None:
        """
        Sets the publishedResources property value. List of existing publishedResource objects. Read-only. Nullable.
        Args:
            value: Value to set for the publishedResources property.
        """
        self._published_resources = value
    
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
        writer.write_collection_of_object_values("agents", self.agents)
        writer.write_collection_of_object_values("connectorGroups", self.connector_groups)
        writer.write_collection_of_object_values("connectors", self.connectors)
        writer.write_object_value("hybridAgentUpdaterConfiguration", self.hybrid_agent_updater_configuration)
        writer.write_bool_value("isDefaultAccessEnabled", self.is_default_access_enabled)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_collection_of_object_values("publishedResources", self.published_resources)
    

