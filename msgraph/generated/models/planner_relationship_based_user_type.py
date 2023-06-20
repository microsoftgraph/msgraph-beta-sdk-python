from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import planner_relationship_user_roles, planner_task_configuration_role_base

from . import planner_task_configuration_role_base

@dataclass
class PlannerRelationshipBasedUserType(planner_task_configuration_role_base.PlannerTaskConfigurationRoleBase):
    odata_type = "#microsoft.graph.plannerRelationshipBasedUserType"
    # The role property
    role: Optional[planner_relationship_user_roles.PlannerRelationshipUserRoles] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerRelationshipBasedUserType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerRelationshipBasedUserType
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PlannerRelationshipBasedUserType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import planner_relationship_user_roles, planner_task_configuration_role_base

        from . import planner_relationship_user_roles, planner_task_configuration_role_base

        fields: Dict[str, Callable[[Any], None]] = {
            "role": lambda n : setattr(self, 'role', n.get_enum_value(planner_relationship_user_roles.PlannerRelationshipUserRoles)),
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
        writer.write_enum_value("role", self.role)
    

