from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_and_app_management_role_definition, entity, role_assignment, role_permission

from . import entity

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
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceAndAppManagementRoleDefinition":
                from . import device_and_app_management_role_definition

                return device_and_app_management_role_definition.DeviceAndAppManagementRoleDefinition()
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
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_and_app_management_role_definition, entity, role_assignment, role_permission

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isBuiltIn": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
            "isBuiltInRoleDefinition": lambda n : setattr(self, 'is_built_in_role_definition', n.get_bool_value()),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_object_values(role_permission.RolePermission)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(role_assignment.RoleAssignment)),
            "rolePermissions": lambda n : setattr(self, 'role_permissions', n.get_collection_of_object_values(role_permission.RolePermission)),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
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
            value: Value to set for the is_built_in property.
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
            value: Value to set for the is_built_in_role_definition property.
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
            value: Value to set for the role_assignments property.
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
            value: Value to set for the role_permissions property.
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
            value: Value to set for the role_scope_tag_ids property.
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
    

