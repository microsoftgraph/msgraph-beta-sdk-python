from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
role_assignment = lazy_import('msgraph.generated.models.role_assignment')
role_permission = lazy_import('msgraph.generated.models.role_permission')

class RoleDefinition(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new roleDefinition and sets the default values.
        """
        super().__init__()
        # Description of the Role definition.
        self._description: Optional[str] = None
        # Display Name of the Role definition.
        self._display_name: Optional[str] = None
        # Type of Role. Set to True if it is built-in, or set to False if it is a custom role definition.
        self._is_built_in: Optional[bool] = None
        # Type of Role. Set to True if it is built-in, or set to False if it is a custom role definition.
        self._is_built_in_role_definition: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of Role Permissions this role is allowed to perform. These must match the actionName that is defined as part of the rolePermission.
        self._permissions: Optional[List[role_permission.RolePermission]] = None
        # List of Role assignments for this role definition.
        self._role_assignments: Optional[List[role_assignment.RoleAssignment]] = None
        # List of Role Permissions this role is allowed to perform. These must match the actionName that is defined as part of the rolePermission.
        self._role_permissions: Optional[List[role_permission.RolePermission]] = None
        # List of Scope Tags for this Entity instance.
        self._role_scope_tag_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoleDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RoleDefinition()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the Role definition.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the Role definition.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display Name of the Role definition.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display Name of the Role definition.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_built_in": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
            "is_built_in_role_definition": lambda n : setattr(self, 'is_built_in_role_definition', n.get_bool_value()),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_object_values(role_permission.RolePermission)),
            "role_assignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(role_assignment.RoleAssignment)),
            "role_permissions": lambda n : setattr(self, 'role_permissions', n.get_collection_of_object_values(role_permission.RolePermission)),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_built_in(self,) -> Optional[bool]:
        """
        Gets the isBuiltIn property value. Type of Role. Set to True if it is built-in, or set to False if it is a custom role definition.
        Returns: Optional[bool]
        """
        return self._is_built_in
    
    @is_built_in.setter
    def is_built_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the isBuiltIn property value. Type of Role. Set to True if it is built-in, or set to False if it is a custom role definition.
        Args:
            value: Value to set for the isBuiltIn property.
        """
        self._is_built_in = value
    
    @property
    def is_built_in_role_definition(self,) -> Optional[bool]:
        """
        Gets the isBuiltInRoleDefinition property value. Type of Role. Set to True if it is built-in, or set to False if it is a custom role definition.
        Returns: Optional[bool]
        """
        return self._is_built_in_role_definition
    
    @is_built_in_role_definition.setter
    def is_built_in_role_definition(self,value: Optional[bool] = None) -> None:
        """
        Sets the isBuiltInRoleDefinition property value. Type of Role. Set to True if it is built-in, or set to False if it is a custom role definition.
        Args:
            value: Value to set for the isBuiltInRoleDefinition property.
        """
        self._is_built_in_role_definition = value
    
    @property
    def permissions(self,) -> Optional[List[role_permission.RolePermission]]:
        """
        Gets the permissions property value. List of Role Permissions this role is allowed to perform. These must match the actionName that is defined as part of the rolePermission.
        Returns: Optional[List[role_permission.RolePermission]]
        """
        return self._permissions
    
    @permissions.setter
    def permissions(self,value: Optional[List[role_permission.RolePermission]] = None) -> None:
        """
        Sets the permissions property value. List of Role Permissions this role is allowed to perform. These must match the actionName that is defined as part of the rolePermission.
        Args:
            value: Value to set for the permissions property.
        """
        self._permissions = value
    
    @property
    def role_assignments(self,) -> Optional[List[role_assignment.RoleAssignment]]:
        """
        Gets the roleAssignments property value. List of Role assignments for this role definition.
        Returns: Optional[List[role_assignment.RoleAssignment]]
        """
        return self._role_assignments
    
    @role_assignments.setter
    def role_assignments(self,value: Optional[List[role_assignment.RoleAssignment]] = None) -> None:
        """
        Sets the roleAssignments property value. List of Role assignments for this role definition.
        Args:
            value: Value to set for the roleAssignments property.
        """
        self._role_assignments = value
    
    @property
    def role_permissions(self,) -> Optional[List[role_permission.RolePermission]]:
        """
        Gets the rolePermissions property value. List of Role Permissions this role is allowed to perform. These must match the actionName that is defined as part of the rolePermission.
        Returns: Optional[List[role_permission.RolePermission]]
        """
        return self._role_permissions
    
    @role_permissions.setter
    def role_permissions(self,value: Optional[List[role_permission.RolePermission]] = None) -> None:
        """
        Sets the rolePermissions property value. List of Role Permissions this role is allowed to perform. These must match the actionName that is defined as part of the rolePermission.
        Args:
            value: Value to set for the rolePermissions property.
        """
        self._role_permissions = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
        Args:
            value: Value to set for the roleScopeTagIds property.
        """
        self._role_scope_tag_ids = value
    
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
        writer.write_bool_value("isBuiltIn", self.is_built_in)
        writer.write_bool_value("isBuiltInRoleDefinition", self.is_built_in_role_definition)
        writer.write_collection_of_object_values("permissions", self.permissions)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("rolePermissions", self.role_permissions)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

