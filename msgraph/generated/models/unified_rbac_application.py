from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, unified_rbac_resource_namespace, unified_role_assignment, unified_role_definition

from . import entity

class UnifiedRbacApplication(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new UnifiedRbacApplication and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Resource that represents a collection of related actions.
        self._resource_namespaces: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]] = None
        # Resource to grant access to users or groups.
        self._role_assignments: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None
        # The roles allowed by RBAC providers and the permissions assigned to the roles.
        self._role_definitions: Optional[List[unified_role_definition.UnifiedRoleDefinition]] = None
        # Resource to grant access to users or groups that are transitive.
        self._transitive_role_assignments: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRbacApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRbacApplication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRbacApplication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, unified_rbac_resource_namespace, unified_role_assignment, unified_role_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "resourceNamespaces": lambda n : setattr(self, 'resource_namespaces', n.get_collection_of_object_values(unified_rbac_resource_namespace.UnifiedRbacResourceNamespace)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(unified_role_assignment.UnifiedRoleAssignment)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(unified_role_definition.UnifiedRoleDefinition)),
            "transitiveRoleAssignments": lambda n : setattr(self, 'transitive_role_assignments', n.get_collection_of_object_values(unified_role_assignment.UnifiedRoleAssignment)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource_namespaces(self,) -> Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]]:
        """
        Gets the resourceNamespaces property value. Resource that represents a collection of related actions.
        Returns: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]]
        """
        return self._resource_namespaces
    
    @resource_namespaces.setter
    def resource_namespaces(self,value: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]] = None) -> None:
        """
        Sets the resourceNamespaces property value. Resource that represents a collection of related actions.
        Args:
            value: Value to set for the resource_namespaces property.
        """
        self._resource_namespaces = value
    
    @property
    def role_assignments(self,) -> Optional[List[unified_role_assignment.UnifiedRoleAssignment]]:
        """
        Gets the roleAssignments property value. Resource to grant access to users or groups.
        Returns: Optional[List[unified_role_assignment.UnifiedRoleAssignment]]
        """
        return self._role_assignments
    
    @role_assignments.setter
    def role_assignments(self,value: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None) -> None:
        """
        Sets the roleAssignments property value. Resource to grant access to users or groups.
        Args:
            value: Value to set for the role_assignments property.
        """
        self._role_assignments = value
    
    @property
    def role_definitions(self,) -> Optional[List[unified_role_definition.UnifiedRoleDefinition]]:
        """
        Gets the roleDefinitions property value. The roles allowed by RBAC providers and the permissions assigned to the roles.
        Returns: Optional[List[unified_role_definition.UnifiedRoleDefinition]]
        """
        return self._role_definitions
    
    @role_definitions.setter
    def role_definitions(self,value: Optional[List[unified_role_definition.UnifiedRoleDefinition]] = None) -> None:
        """
        Sets the roleDefinitions property value. The roles allowed by RBAC providers and the permissions assigned to the roles.
        Args:
            value: Value to set for the role_definitions property.
        """
        self._role_definitions = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("resourceNamespaces", self.resource_namespaces)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("transitiveRoleAssignments", self.transitive_role_assignments)
    
    @property
    def transitive_role_assignments(self,) -> Optional[List[unified_role_assignment.UnifiedRoleAssignment]]:
        """
        Gets the transitiveRoleAssignments property value. Resource to grant access to users or groups that are transitive.
        Returns: Optional[List[unified_role_assignment.UnifiedRoleAssignment]]
        """
        return self._transitive_role_assignments
    
    @transitive_role_assignments.setter
    def transitive_role_assignments(self,value: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None) -> None:
        """
        Sets the transitiveRoleAssignments property value. Resource to grant access to users or groups that are transitive.
        Args:
            value: Value to set for the transitive_role_assignments property.
        """
        self._transitive_role_assignments = value
    

