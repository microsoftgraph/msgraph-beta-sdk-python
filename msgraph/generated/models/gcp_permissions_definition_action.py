from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .gcp_action_permissions_definition_action import GcpActionPermissionsDefinitionAction
    from .gcp_role_permissions_definition_action import GcpRolePermissionsDefinitionAction
    from .permissions_definition_action import PermissionsDefinitionAction

from .permissions_definition_action import PermissionsDefinitionAction

@dataclass
class GcpPermissionsDefinitionAction(PermissionsDefinitionAction):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.gcpPermissionsDefinitionAction"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GcpPermissionsDefinitionAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GcpPermissionsDefinitionAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpActionPermissionsDefinitionAction".casefold():
            from .gcp_action_permissions_definition_action import GcpActionPermissionsDefinitionAction

            return GcpActionPermissionsDefinitionAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpRolePermissionsDefinitionAction".casefold():
            from .gcp_role_permissions_definition_action import GcpRolePermissionsDefinitionAction

            return GcpRolePermissionsDefinitionAction()
        return GcpPermissionsDefinitionAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .gcp_action_permissions_definition_action import GcpActionPermissionsDefinitionAction
        from .gcp_role_permissions_definition_action import GcpRolePermissionsDefinitionAction
        from .permissions_definition_action import PermissionsDefinitionAction

        from .gcp_action_permissions_definition_action import GcpActionPermissionsDefinitionAction
        from .gcp_role_permissions_definition_action import GcpRolePermissionsDefinitionAction
        from .permissions_definition_action import PermissionsDefinitionAction

        fields: Dict[str, Callable[[Any], None]] = {
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
    

