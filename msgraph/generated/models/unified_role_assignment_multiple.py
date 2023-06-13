from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_scope, directory_object, entity, unified_role_definition

from . import entity

@dataclass
class UnifiedRoleAssignmentMultiple(entity.Entity):
    # Ids of the app specific scopes when the assignment scopes are app specific. The scopes of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. App scopes are scopes that are defined and understood by this application only.
    app_scope_ids: Optional[List[str]] = None
    # Read-only collection with details of the app specific scopes when the assignment scopes are app specific. Containment entity. Read-only.
    app_scopes: Optional[List[app_scope.AppScope]] = None
    # The condition property
    condition: Optional[str] = None
    # Description of the role assignment.
    description: Optional[str] = None
    # Ids of the directory objects representing the scopes of the assignment. The scopes of an assignment determine the set of resources for which the principals have been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. App scopes are scopes that are defined and understood by this application only.
    directory_scope_ids: Optional[List[str]] = None
    # Read-only collection referencing the directory objects that are scope of the assignment. Provided so that callers can get the directory objects using $expand at the same time as getting the role assignment. Read-only.  Supports $expand.
    directory_scopes: Optional[List[directory_object.DirectoryObject]] = None
    # Name of the role assignment. Required.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Identifiers of the principals to which the assignment is granted.  Supports $filter (any operator only).
    principal_ids: Optional[List[str]] = None
    # Read-only collection referencing the assigned principals. Provided so that callers can get the principals using $expand at the same time as getting the role assignment. Read-only.  Supports $expand.
    principals: Optional[List[directory_object.DirectoryObject]] = None
    # Specifies the roleDefinition that the assignment is for. Provided so that callers can get the role definition using $expand at the same time as getting the role assignment.  Supports $filter (eq operator on id, isBuiltIn, and displayName, and startsWith operator on displayName)  and $expand.
    role_definition: Optional[unified_role_definition.UnifiedRoleDefinition] = None
    # Identifier of the unifiedRoleDefinition the assignment is for.
    role_definition_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleAssignmentMultiple:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleAssignmentMultiple
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleAssignmentMultiple()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_scope, directory_object, entity, unified_role_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "appScopes": lambda n : setattr(self, 'app_scopes', n.get_collection_of_object_values(app_scope.AppScope)),
            "appScopeIds": lambda n : setattr(self, 'app_scope_ids', n.get_collection_of_primitive_values(str)),
            "condition": lambda n : setattr(self, 'condition', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "directoryScopes": lambda n : setattr(self, 'directory_scopes', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "directoryScopeIds": lambda n : setattr(self, 'directory_scope_ids', n.get_collection_of_primitive_values(str)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "principals": lambda n : setattr(self, 'principals', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "principalIds": lambda n : setattr(self, 'principal_ids', n.get_collection_of_primitive_values(str)),
            "roleDefinition": lambda n : setattr(self, 'role_definition', n.get_object_value(unified_role_definition.UnifiedRoleDefinition)),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("appScopes", self.app_scopes)
        writer.write_collection_of_primitive_values("appScopeIds", self.app_scope_ids)
        writer.write_str_value("condition", self.condition)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("directoryScopes", self.directory_scopes)
        writer.write_collection_of_primitive_values("directoryScopeIds", self.directory_scope_ids)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("principals", self.principals)
        writer.write_collection_of_primitive_values("principalIds", self.principal_ids)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
    

