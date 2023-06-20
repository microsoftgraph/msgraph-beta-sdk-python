from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import role_assignment, role_scope_tag

from . import role_assignment

@dataclass
class DeviceAndAppManagementRoleAssignment(role_assignment.RoleAssignment):
    # The list of ids of role member security groups. These are IDs from Azure Active Directory.
    members: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The set of Role Scope Tags defined on the Role Assignment.
    role_scope_tags: Optional[List[role_scope_tag.RoleScopeTag]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAndAppManagementRoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAndAppManagementRoleAssignment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceAndAppManagementRoleAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import role_assignment, role_scope_tag

        from . import role_assignment, role_scope_tag

        fields: Dict[str, Callable[[Any], None]] = {
            "members": lambda n : setattr(self, 'members', n.get_collection_of_primitive_values(str)),
            "roleScopeTags": lambda n : setattr(self, 'role_scope_tags', n.get_collection_of_object_values(role_scope_tag.RoleScopeTag)),
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
        writer.write_collection_of_primitive_values("members", self.members)
        writer.write_collection_of_object_values("roleScopeTags", self.role_scope_tags)
    

