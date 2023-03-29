from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, unified_rbac_resource_namespace, unified_role_assignment_multiple, unified_role_definition

from . import entity

class RbacApplicationMultiple(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new RbacApplicationMultiple and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The resourceNamespaces property
        self._resource_namespaces: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]] = None
        # The roleAssignments property
        self._role_assignments: Optional[List[unified_role_assignment_multiple.UnifiedRoleAssignmentMultiple]] = None
        # The roleDefinitions property
        self._role_definitions: Optional[List[unified_role_definition.UnifiedRoleDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RbacApplicationMultiple:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RbacApplicationMultiple
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RbacApplicationMultiple()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, unified_rbac_resource_namespace, unified_role_assignment_multiple, unified_role_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "resourceNamespaces": lambda n : setattr(self, 'resource_namespaces', n.get_collection_of_object_values(unified_rbac_resource_namespace.UnifiedRbacResourceNamespace)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(unified_role_assignment_multiple.UnifiedRoleAssignmentMultiple)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(unified_role_definition.UnifiedRoleDefinition)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource_namespaces(self,) -> Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]]:
        """
        Gets the resourceNamespaces property value. The resourceNamespaces property
        Returns: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]]
        """
        return self._resource_namespaces
    
    @resource_namespaces.setter
    def resource_namespaces(self,value: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]] = None) -> None:
        """
        Sets the resourceNamespaces property value. The resourceNamespaces property
        Args:
            value: Value to set for the resource_namespaces property.
        """
        self._resource_namespaces = value
    
    @property
    def role_assignments(self,) -> Optional[List[unified_role_assignment_multiple.UnifiedRoleAssignmentMultiple]]:
        """
        Gets the roleAssignments property value. The roleAssignments property
        Returns: Optional[List[unified_role_assignment_multiple.UnifiedRoleAssignmentMultiple]]
        """
        return self._role_assignments
    
    @role_assignments.setter
    def role_assignments(self,value: Optional[List[unified_role_assignment_multiple.UnifiedRoleAssignmentMultiple]] = None) -> None:
        """
        Sets the roleAssignments property value. The roleAssignments property
        Args:
            value: Value to set for the role_assignments property.
        """
        self._role_assignments = value
    
    @property
    def role_definitions(self,) -> Optional[List[unified_role_definition.UnifiedRoleDefinition]]:
        """
        Gets the roleDefinitions property value. The roleDefinitions property
        Returns: Optional[List[unified_role_definition.UnifiedRoleDefinition]]
        """
        return self._role_definitions
    
    @role_definitions.setter
    def role_definitions(self,value: Optional[List[unified_role_definition.UnifiedRoleDefinition]] = None) -> None:
        """
        Sets the roleDefinitions property value. The roleDefinitions property
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
    

