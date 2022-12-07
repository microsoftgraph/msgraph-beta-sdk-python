from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
on_premises_agent = lazy_import('msgraph.generated.models.on_premises_agent')
on_premises_publishing_type = lazy_import('msgraph.generated.models.on_premises_publishing_type')
published_resource = lazy_import('msgraph.generated.models.published_resource')

class OnPremisesAgentGroup(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def agents(self,) -> Optional[List[on_premises_agent.OnPremisesAgent]]:
        """
        Gets the agents property value. List of onPremisesAgent that are assigned to an onPremisesAgentGroup. Read-only. Nullable.
        Returns: Optional[List[on_premises_agent.OnPremisesAgent]]
        """
        return self._agents
    
    @agents.setter
    def agents(self,value: Optional[List[on_premises_agent.OnPremisesAgent]] = None) -> None:
        """
        Sets the agents property value. List of onPremisesAgent that are assigned to an onPremisesAgentGroup. Read-only. Nullable.
        Args:
            value: Value to set for the agents property.
        """
        self._agents = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new onPremisesAgentGroup and sets the default values.
        """
        super().__init__()
        # List of onPremisesAgent that are assigned to an onPremisesAgentGroup. Read-only. Nullable.
        self._agents: Optional[List[on_premises_agent.OnPremisesAgent]] = None
        # Display name of the onPremisesAgentGroup.
        self._display_name: Optional[str] = None
        # Indicates if the onPremisesAgentGroup is the default agent group. Only a single agent group can be the default onPremisesAgentGroup and is set by the system.
        self._is_default: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of publishedResource that are assigned to an onPremisesAgentGroup. Read-only. Nullable.
        self._published_resources: Optional[List[published_resource.PublishedResource]] = None
        # The publishingType property
        self._publishing_type: Optional[on_premises_publishing_type.OnPremisesPublishingType] = None
    
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
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the onPremisesAgentGroup.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the onPremisesAgentGroup.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "agents": lambda n : setattr(self, 'agents', n.get_collection_of_object_values(on_premises_agent.OnPremisesAgent)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "published_resources": lambda n : setattr(self, 'published_resources', n.get_collection_of_object_values(published_resource.PublishedResource)),
            "publishing_type": lambda n : setattr(self, 'publishing_type', n.get_enum_value(on_premises_publishing_type.OnPremisesPublishingType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. Indicates if the onPremisesAgentGroup is the default agent group. Only a single agent group can be the default onPremisesAgentGroup and is set by the system.
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. Indicates if the onPremisesAgentGroup is the default agent group. Only a single agent group can be the default onPremisesAgentGroup and is set by the system.
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def published_resources(self,) -> Optional[List[published_resource.PublishedResource]]:
        """
        Gets the publishedResources property value. List of publishedResource that are assigned to an onPremisesAgentGroup. Read-only. Nullable.
        Returns: Optional[List[published_resource.PublishedResource]]
        """
        return self._published_resources
    
    @published_resources.setter
    def published_resources(self,value: Optional[List[published_resource.PublishedResource]] = None) -> None:
        """
        Sets the publishedResources property value. List of publishedResource that are assigned to an onPremisesAgentGroup. Read-only. Nullable.
        Args:
            value: Value to set for the publishedResources property.
        """
        self._published_resources = value
    
    @property
    def publishing_type(self,) -> Optional[on_premises_publishing_type.OnPremisesPublishingType]:
        """
        Gets the publishingType property value. The publishingType property
        Returns: Optional[on_premises_publishing_type.OnPremisesPublishingType]
        """
        return self._publishing_type
    
    @publishing_type.setter
    def publishing_type(self,value: Optional[on_premises_publishing_type.OnPremisesPublishingType] = None) -> None:
        """
        Sets the publishingType property value. The publishingType property
        Args:
            value: Value to set for the publishingType property.
        """
        self._publishing_type = value
    
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
    

