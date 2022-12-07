from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
role_assignment_scope_type = lazy_import('msgraph.generated.models.role_assignment_scope_type')
role_definition = lazy_import('msgraph.generated.models.role_definition')

class RoleAssignment(entity.Entity):
    """
    The Role Assignment resource. Role assignments tie together a role definition with members and scopes. There can be one or more role assignments per role. This applies to custom and built-in roles.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new roleAssignment and sets the default values.
        """
        super().__init__()
        # Description of the Role Assignment.
        self._description: Optional[str] = None
        # The display or friendly name of the role Assignment.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of ids of role scope member security groups.  These are IDs from Azure Active Directory.
        self._resource_scopes: Optional[List[str]] = None
        # Role definition this assignment is part of.
        self._role_definition: Optional[role_definition.RoleDefinition] = None
        # List of ids of role scope member security groups.  These are IDs from Azure Active Directory.
        self._scope_members: Optional[List[str]] = None
        # Specifies the type of scope for a Role Assignment.
        self._scope_type: Optional[role_assignment_scope_type.RoleAssignmentScopeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoleAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RoleAssignment()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the Role Assignment.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the Role Assignment.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display or friendly name of the role Assignment.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display or friendly name of the role Assignment.
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
            "resource_scopes": lambda n : setattr(self, 'resource_scopes', n.get_collection_of_primitive_values(str)),
            "role_definition": lambda n : setattr(self, 'role_definition', n.get_object_value(role_definition.RoleDefinition)),
            "scope_members": lambda n : setattr(self, 'scope_members', n.get_collection_of_primitive_values(str)),
            "scope_type": lambda n : setattr(self, 'scope_type', n.get_enum_value(role_assignment_scope_type.RoleAssignmentScopeType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource_scopes(self,) -> Optional[List[str]]:
        """
        Gets the resourceScopes property value. List of ids of role scope member security groups.  These are IDs from Azure Active Directory.
        Returns: Optional[List[str]]
        """
        return self._resource_scopes
    
    @resource_scopes.setter
    def resource_scopes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the resourceScopes property value. List of ids of role scope member security groups.  These are IDs from Azure Active Directory.
        Args:
            value: Value to set for the resourceScopes property.
        """
        self._resource_scopes = value
    
    @property
    def role_definition(self,) -> Optional[role_definition.RoleDefinition]:
        """
        Gets the roleDefinition property value. Role definition this assignment is part of.
        Returns: Optional[role_definition.RoleDefinition]
        """
        return self._role_definition
    
    @role_definition.setter
    def role_definition(self,value: Optional[role_definition.RoleDefinition] = None) -> None:
        """
        Sets the roleDefinition property value. Role definition this assignment is part of.
        Args:
            value: Value to set for the roleDefinition property.
        """
        self._role_definition = value
    
    @property
    def scope_members(self,) -> Optional[List[str]]:
        """
        Gets the scopeMembers property value. List of ids of role scope member security groups.  These are IDs from Azure Active Directory.
        Returns: Optional[List[str]]
        """
        return self._scope_members
    
    @scope_members.setter
    def scope_members(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the scopeMembers property value. List of ids of role scope member security groups.  These are IDs from Azure Active Directory.
        Args:
            value: Value to set for the scopeMembers property.
        """
        self._scope_members = value
    
    @property
    def scope_type(self,) -> Optional[role_assignment_scope_type.RoleAssignmentScopeType]:
        """
        Gets the scopeType property value. Specifies the type of scope for a Role Assignment.
        Returns: Optional[role_assignment_scope_type.RoleAssignmentScopeType]
        """
        return self._scope_type
    
    @scope_type.setter
    def scope_type(self,value: Optional[role_assignment_scope_type.RoleAssignmentScopeType] = None) -> None:
        """
        Sets the scopeType property value. Specifies the type of scope for a Role Assignment.
        Args:
            value: Value to set for the scopeType property.
        """
        self._scope_type = value
    
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
        writer.write_collection_of_primitive_values("resourceScopes", self.resource_scopes)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_collection_of_primitive_values("scopeMembers", self.scope_members)
        writer.write_enum_value("scopeType", self.scope_type)
    

