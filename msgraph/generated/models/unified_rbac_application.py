from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_app_scope import CustomAppScope
    from .entity import Entity
    from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
    from .unified_role_assignment import UnifiedRoleAssignment
    from .unified_role_definition import UnifiedRoleDefinition

from .entity import Entity

@dataclass
class UnifiedRbacApplication(Entity):
    # Workload-specific scope object that represents the resources for which the principal has been granted access.
    custom_app_scopes: Optional[List[CustomAppScope]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Resource that represents a collection of related actions.
    resource_namespaces: Optional[List[UnifiedRbacResourceNamespace]] = None
    # Resource to grant access to users or groups.
    role_assignments: Optional[List[UnifiedRoleAssignment]] = None
    # The roles allowed by RBAC providers and the permissions assigned to the roles.
    role_definitions: Optional[List[UnifiedRoleDefinition]] = None
    # Resource to grant access to users or groups that are transitive.
    transitive_role_assignments: Optional[List[UnifiedRoleAssignment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRbacApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRbacApplication
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRbacApplication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_app_scope import CustomAppScope
        from .entity import Entity
        from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
        from .unified_role_assignment import UnifiedRoleAssignment
        from .unified_role_definition import UnifiedRoleDefinition

        from .custom_app_scope import CustomAppScope
        from .entity import Entity
        from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
        from .unified_role_assignment import UnifiedRoleAssignment
        from .unified_role_definition import UnifiedRoleDefinition

        fields: Dict[str, Callable[[Any], None]] = {
            "customAppScopes": lambda n : setattr(self, 'custom_app_scopes', n.get_collection_of_object_values(CustomAppScope)),
            "resourceNamespaces": lambda n : setattr(self, 'resource_namespaces', n.get_collection_of_object_values(UnifiedRbacResourceNamespace)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(UnifiedRoleAssignment)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(UnifiedRoleDefinition)),
            "transitiveRoleAssignments": lambda n : setattr(self, 'transitive_role_assignments', n.get_collection_of_object_values(UnifiedRoleAssignment)),
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
        writer.write_collection_of_object_values("customAppScopes", self.custom_app_scopes)
        writer.write_collection_of_object_values("resourceNamespaces", self.resource_namespaces)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("transitiveRoleAssignments", self.transitive_role_assignments)
    

