from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_object, extension, scoped_role_membership

from . import directory_object

@dataclass
class AdministrativeUnit(directory_object.DirectoryObject):
    odata_type = "#microsoft.graph.administrativeUnit"
    # An optional description for the administrative unit. Supports $filter (eq, ne, in, startsWith), $search.
    description: Optional[str] = None
    # Display name for the administrative unit. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
    display_name: Optional[str] = None
    # The collection of open extensions defined for this administrative unit. Nullable.
    extensions: Optional[List[extension.Extension]] = None
    # true if members of this administrative unit should be treated as sensitive, which requires specific permissions to manage. Default value is false. Use this property to define administrative units whose roles don't inherit from tenant-level administrators, and management of individual member objects is limited to administrators scoped to a restricted management administrative unit. Immutable, so cannot be changed later.
    is_member_management_restricted: Optional[bool] = None
    # Users and groups that are members of this administrative unit. Supports $expand.
    members: Optional[List[directory_object.DirectoryObject]] = None
    # Scoped-role members of this administrative unit.
    scoped_role_members: Optional[List[scoped_role_membership.ScopedRoleMembership]] = None
    # Controls whether the administrative unit and its members are hidden or public. Can be set to HiddenMembership or Public. If not set, the default behavior is Public. When set to HiddenMembership, only members of the administrative unit can list other members of the administrative unit.
    visibility: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AdministrativeUnit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AdministrativeUnit
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AdministrativeUnit()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_object, extension, scoped_role_membership

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "isMemberManagementRestricted": lambda n : setattr(self, 'is_member_management_restricted', n.get_bool_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "scopedRoleMembers": lambda n : setattr(self, 'scoped_role_members', n.get_collection_of_object_values(scoped_role_membership.ScopedRoleMembership)),
            "visibility": lambda n : setattr(self, 'visibility', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_bool_value("isMemberManagementRestricted", self.is_member_management_restricted)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_collection_of_object_values("scopedRoleMembers", self.scoped_role_members)
        writer.write_str_value("visibility", self.visibility)
    

