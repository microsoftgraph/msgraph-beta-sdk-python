from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_scope import AppScope
    from .directory_object import DirectoryObject
    from .entity import Entity
    from .unified_role_definition import UnifiedRoleDefinition

from .entity import Entity

@dataclass
class UnifiedRoleAssignment(Entity):
    # Details of the app specific scope when the assignment scope is app specific. Containment entity.
    app_scope: Optional[AppScope] = None
    # Identifier of the app specific scope when the assignment scope is app specific. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. App scopes are scopes that are defined and understood by this application only.  For the entitlement management provider, use app scopes to specify a catalog, for example /AccessPackageCatalog/beedadfe-01d5-4025-910b-84abb9369997.
    app_scope_id: Optional[str] = None
    # The condition property
    condition: Optional[str] = None
    # The directory object that is the scope of the assignment. Provided so that callers can get the directory object using $expand at the same time as getting the role assignment. Read-only. Supports $expand.
    directory_scope: Optional[DirectoryObject] = None
    # Identifier of the directory object representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. App scopes are scopes that are defined and understood by this application only.
    directory_scope_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The assigned principal. Provided so that callers can get the principal using $expand at the same time as getting the role assignment. Read-only. Supports $expand.
    principal: Optional[DirectoryObject] = None
    # Identifier of the principal to which the assignment is granted. Supports $filter (eq operator only).
    principal_id: Optional[str] = None
    # The principalOrganizationId property
    principal_organization_id: Optional[str] = None
    # The scope at which the unifiedRoleAssignment applies. This is / for service-wide. DO NOT USE. This property will be deprecated soon.
    resource_scope: Optional[str] = None
    # The roleDefinition the assignment is for. Provided so that callers can get the role definition using $expand at the same time as getting the role assignment. roleDefinition.id will be auto expanded. Supports $expand.
    role_definition: Optional[UnifiedRoleDefinition] = None
    # Identifier of the unifiedRoleDefinition the assignment is for. Read-only. Supports $filter (eq operator only).
    role_definition_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleAssignment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_scope import AppScope
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .unified_role_definition import UnifiedRoleDefinition

        from .app_scope import AppScope
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .unified_role_definition import UnifiedRoleDefinition

        fields: Dict[str, Callable[[Any], None]] = {
            "appScope": lambda n : setattr(self, 'app_scope', n.get_object_value(AppScope)),
            "appScopeId": lambda n : setattr(self, 'app_scope_id', n.get_str_value()),
            "condition": lambda n : setattr(self, 'condition', n.get_str_value()),
            "directoryScope": lambda n : setattr(self, 'directory_scope', n.get_object_value(DirectoryObject)),
            "directoryScopeId": lambda n : setattr(self, 'directory_scope_id', n.get_str_value()),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(DirectoryObject)),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "principalOrganizationId": lambda n : setattr(self, 'principal_organization_id', n.get_str_value()),
            "resourceScope": lambda n : setattr(self, 'resource_scope', n.get_str_value()),
            "roleDefinition": lambda n : setattr(self, 'role_definition', n.get_object_value(UnifiedRoleDefinition)),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
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
        writer.write_object_value("appScope", self.app_scope)
        writer.write_str_value("appScopeId", self.app_scope_id)
        writer.write_str_value("condition", self.condition)
        writer.write_object_value("directoryScope", self.directory_scope)
        writer.write_str_value("directoryScopeId", self.directory_scope_id)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_str_value("principalOrganizationId", self.principal_organization_id)
        writer.write_str_value("resourceScope", self.resource_scope)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
    

