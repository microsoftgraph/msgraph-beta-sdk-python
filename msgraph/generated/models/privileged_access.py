from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, governance_resource, governance_role_assignment, governance_role_assignment_request, governance_role_definition, governance_role_setting

from . import entity

@dataclass
class PrivilegedAccess(entity.Entity):
    # The display name of the provider managed by PIM.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of resources for the provider.
    resources: Optional[List[governance_resource.GovernanceResource]] = None
    # A collection of role assignment requests for the provider.
    role_assignment_requests: Optional[List[governance_role_assignment_request.GovernanceRoleAssignmentRequest]] = None
    # A collection of role assignments for the provider.
    role_assignments: Optional[List[governance_role_assignment.GovernanceRoleAssignment]] = None
    # A collection of role defintions for the provider.
    role_definitions: Optional[List[governance_role_definition.GovernanceRoleDefinition]] = None
    # A collection of role settings for the provider.
    role_settings: Optional[List[governance_role_setting.GovernanceRoleSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccess:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccess
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedAccess()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, governance_resource, governance_role_assignment, governance_role_assignment_request, governance_role_definition, governance_role_setting

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(governance_resource.GovernanceResource)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(governance_role_assignment.GovernanceRoleAssignment)),
            "roleAssignmentRequests": lambda n : setattr(self, 'role_assignment_requests', n.get_collection_of_object_values(governance_role_assignment_request.GovernanceRoleAssignmentRequest)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(governance_role_definition.GovernanceRoleDefinition)),
            "roleSettings": lambda n : setattr(self, 'role_settings', n.get_collection_of_object_values(governance_role_setting.GovernanceRoleSetting)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleAssignmentRequests", self.role_assignment_requests)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("roleSettings", self.role_settings)
    

