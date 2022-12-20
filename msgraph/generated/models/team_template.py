from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
team_template_definition = lazy_import('msgraph.generated.models.team_template_definition')

class TeamTemplate(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new teamTemplate and sets the default values.
        """
        super().__init__()
        # The definitions property
        self._definitions: Optional[List[team_template_definition.TeamTemplateDefinition]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamTemplate()
    
    @property
    def definitions(self,) -> Optional[List[team_template_definition.TeamTemplateDefinition]]:
        """
        Gets the definitions property value. The definitions property
        Returns: Optional[List[team_template_definition.TeamTemplateDefinition]]
        """
        return self._definitions
    
    @definitions.setter
    def definitions(self,value: Optional[List[team_template_definition.TeamTemplateDefinition]] = None) -> None:
        """
        Sets the definitions property value. The definitions property
        Args:
            value: Value to set for the definitions property.
        """
        self._definitions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "definitions": lambda n : setattr(self, 'definitions', n.get_collection_of_object_values(team_template_definition.TeamTemplateDefinition)),
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
        writer.write_collection_of_object_values("definitions", self.definitions)
    

