from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
on_premises_agent_group = lazy_import('msgraph.generated.models.on_premises_agent_group')
on_premises_publishing_type = lazy_import('msgraph.generated.models.on_premises_publishing_type')

class PublishedResource(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def agent_groups(self,) -> Optional[List[on_premises_agent_group.OnPremisesAgentGroup]]:
        """
        Gets the agentGroups property value. List of onPremisesAgentGroups that a publishedResource is assigned to. Read-only. Nullable.
        Returns: Optional[List[on_premises_agent_group.OnPremisesAgentGroup]]
        """
        return self._agent_groups
    
    @agent_groups.setter
    def agent_groups(self,value: Optional[List[on_premises_agent_group.OnPremisesAgentGroup]] = None) -> None:
        """
        Sets the agentGroups property value. List of onPremisesAgentGroups that a publishedResource is assigned to. Read-only. Nullable.
        Args:
            value: Value to set for the agentGroups property.
        """
        self._agent_groups = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new publishedResource and sets the default values.
        """
        super().__init__()
        # List of onPremisesAgentGroups that a publishedResource is assigned to. Read-only. Nullable.
        self._agent_groups: Optional[List[on_premises_agent_group.OnPremisesAgentGroup]] = None
        # Display Name of the publishedResource.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The publishingType property
        self._publishing_type: Optional[on_premises_publishing_type.OnPremisesPublishingType] = None
        # Name of the publishedResource.
        self._resource_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PublishedResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PublishedResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PublishedResource()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display Name of the publishedResource.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display Name of the publishedResource.
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
            "agent_groups": lambda n : setattr(self, 'agent_groups', n.get_collection_of_object_values(on_premises_agent_group.OnPremisesAgentGroup)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "publishing_type": lambda n : setattr(self, 'publishing_type', n.get_enum_value(on_premises_publishing_type.OnPremisesPublishingType)),
            "resource_name": lambda n : setattr(self, 'resource_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    
    @property
    def resource_name(self,) -> Optional[str]:
        """
        Gets the resourceName property value. Name of the publishedResource.
        Returns: Optional[str]
        """
        return self._resource_name
    
    @resource_name.setter
    def resource_name(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceName property value. Name of the publishedResource.
        Args:
            value: Value to set for the resourceName property.
        """
        self._resource_name = value
    
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("publishingType", self.publishing_type)
        writer.write_str_value("resourceName", self.resource_name)
    

