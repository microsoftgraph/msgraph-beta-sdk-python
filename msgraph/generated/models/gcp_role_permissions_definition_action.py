from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .gcp_permissions_definition_action import GcpPermissionsDefinitionAction
    from .permissions_definition_gcp_role import PermissionsDefinitionGcpRole

from .gcp_permissions_definition_action import GcpPermissionsDefinitionAction

@dataclass
class GcpRolePermissionsDefinitionAction(GcpPermissionsDefinitionAction):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.gcpRolePermissionsDefinitionAction"
    # The roles property
    roles: Optional[List[PermissionsDefinitionGcpRole]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GcpRolePermissionsDefinitionAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GcpRolePermissionsDefinitionAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GcpRolePermissionsDefinitionAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .gcp_permissions_definition_action import GcpPermissionsDefinitionAction
        from .permissions_definition_gcp_role import PermissionsDefinitionGcpRole

        from .gcp_permissions_definition_action import GcpPermissionsDefinitionAction
        from .permissions_definition_gcp_role import PermissionsDefinitionGcpRole

        fields: Dict[str, Callable[[Any], None]] = {
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_object_values(PermissionsDefinitionGcpRole)),
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
        writer.write_collection_of_object_values("roles", self.roles)
    

