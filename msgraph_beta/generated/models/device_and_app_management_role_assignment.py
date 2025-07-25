from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .role_assignment import RoleAssignment
    from .role_scope_tag import RoleScopeTag

from .role_assignment import RoleAssignment

@dataclass
class DeviceAndAppManagementRoleAssignment(RoleAssignment, Parsable):
    """
    The Role Assignment resource. Role assignments tie together a role definition with members and scopes. There can be one or more role assignments per role. This applies to custom and built-in roles.
    """
    # Indicates the list of role member security group Entra IDs. For example: {dec942f4-6777-4998-96b4-522e383b08e2}.
    members: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the set of role scope tag IDs for the role assignment. These scope tags will limit the visibility of any Intune resources to those that match any of the scope tags in this collection.
    role_scope_tag_ids: Optional[list[str]] = None
    # Indicates the set of scope tags for the role assignment. These scope tags will limit the visibility of any Intune resources to those that match any of the scope tags in this collection.
    role_scope_tags: Optional[list[RoleScopeTag]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceAndAppManagementRoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAndAppManagementRoleAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceAndAppManagementRoleAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .role_assignment import RoleAssignment
        from .role_scope_tag import RoleScopeTag

        from .role_assignment import RoleAssignment
        from .role_scope_tag import RoleScopeTag

        fields: dict[str, Callable[[Any], None]] = {
            "members": lambda n : setattr(self, 'members', n.get_collection_of_primitive_values(str)),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "roleScopeTags": lambda n : setattr(self, 'role_scope_tags', n.get_collection_of_object_values(RoleScopeTag)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("members", self.members)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_collection_of_object_values("roleScopeTags", self.role_scope_tags)
    

