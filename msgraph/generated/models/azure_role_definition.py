from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .azure_role_definition_type import AzureRoleDefinitionType
    from .entity import Entity

from .entity import Entity

@dataclass
class AzureRoleDefinition(Entity):
    # The assignableScopes property
    assignable_scopes: Optional[List[str]] = None
    # The azureRoleDefinitionType property
    azure_role_definition_type: Optional[AzureRoleDefinitionType] = None
    # The displayName property
    display_name: Optional[str] = None
    # The externalId property
    external_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AzureRoleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureRoleDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AzureRoleDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .azure_role_definition_type import AzureRoleDefinitionType
        from .entity import Entity

        from .azure_role_definition_type import AzureRoleDefinitionType
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignableScopes": lambda n : setattr(self, 'assignable_scopes', n.get_collection_of_primitive_values(str)),
            "azureRoleDefinitionType": lambda n : setattr(self, 'azure_role_definition_type', n.get_enum_value(AzureRoleDefinitionType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("assignableScopes", self.assignable_scopes)
        writer.write_enum_value("azureRoleDefinitionType", self.azure_role_definition_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
    

