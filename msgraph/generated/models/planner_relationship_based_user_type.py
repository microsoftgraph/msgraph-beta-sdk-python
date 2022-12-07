from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

planner_relationship_user_roles = lazy_import('msgraph.generated.models.planner_relationship_user_roles')
planner_task_configuration_role_base = lazy_import('msgraph.generated.models.planner_task_configuration_role_base')

class PlannerRelationshipBasedUserType(planner_task_configuration_role_base.PlannerTaskConfigurationRoleBase):
    def __init__(self,) -> None:
        """
        Instantiates a new PlannerRelationshipBasedUserType and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.plannerRelationshipBasedUserType"
        # The role property
        self._role: Optional[planner_relationship_user_roles.PlannerRelationshipUserRoles] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerRelationshipBasedUserType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerRelationshipBasedUserType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerRelationshipBasedUserType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "role": lambda n : setattr(self, 'role', n.get_enum_value(planner_relationship_user_roles.PlannerRelationshipUserRoles)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def role(self,) -> Optional[planner_relationship_user_roles.PlannerRelationshipUserRoles]:
        """
        Gets the role property value. The role property
        Returns: Optional[planner_relationship_user_roles.PlannerRelationshipUserRoles]
        """
        return self._role
    
    @role.setter
    def role(self,value: Optional[planner_relationship_user_roles.PlannerRelationshipUserRoles] = None) -> None:
        """
        Sets the role property value. The role property
        Args:
            value: Value to set for the role property.
        """
        self._role = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("role", self.role)
    

