from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_scope = lazy_import('msgraph.generated.models.app_scope')
directory_object = lazy_import('msgraph.generated.models.directory_object')
entity = lazy_import('msgraph.generated.models.entity')
unified_role_definition = lazy_import('msgraph.generated.models.unified_role_definition')

class UnifiedRoleAssignmentMultiple(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def app_scope_ids(self,) -> Optional[List[str]]:
        """
        Gets the appScopeIds property value. Ids of the app specific scopes when the assignment scopes are app specific. The scopes of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. App scopes are scopes that are defined and understood by this application only.
        Returns: Optional[List[str]]
        """
        return self._app_scope_ids
    
    @app_scope_ids.setter
    def app_scope_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the appScopeIds property value. Ids of the app specific scopes when the assignment scopes are app specific. The scopes of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. App scopes are scopes that are defined and understood by this application only.
        Args:
            value: Value to set for the appScopeIds property.
        """
        self._app_scope_ids = value
    
    @property
    def app_scopes(self,) -> Optional[List[app_scope.AppScope]]:
        """
        Gets the appScopes property value. Read-only collection with details of the app specific scopes when the assignment scopes are app specific. Containment entity. Read-only.
        Returns: Optional[List[app_scope.AppScope]]
        """
        return self._app_scopes
    
    @app_scopes.setter
    def app_scopes(self,value: Optional[List[app_scope.AppScope]] = None) -> None:
        """
        Sets the appScopes property value. Read-only collection with details of the app specific scopes when the assignment scopes are app specific. Containment entity. Read-only.
        Args:
            value: Value to set for the appScopes property.
        """
        self._app_scopes = value
    
    @property
    def condition(self,) -> Optional[str]:
        """
        Gets the condition property value. The condition property
        Returns: Optional[str]
        """
        return self._condition
    
    @condition.setter
    def condition(self,value: Optional[str] = None) -> None:
        """
        Sets the condition property value. The condition property
        Args:
            value: Value to set for the condition property.
        """
        self._condition = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRoleAssignmentMultiple and sets the default values.
        """
        super().__init__()
        # Ids of the app specific scopes when the assignment scopes are app specific. The scopes of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. App scopes are scopes that are defined and understood by this application only.
        self._app_scope_ids: Optional[List[str]] = None
        # Read-only collection with details of the app specific scopes when the assignment scopes are app specific. Containment entity. Read-only.
        self._app_scopes: Optional[List[app_scope.AppScope]] = None
        # The condition property
        self._condition: Optional[str] = None
        # Description of the role assignment.
        self._description: Optional[str] = None
        # Ids of the directory objects representing the scopes of the assignment. The scopes of an assignment determine the set of resources for which the principals have been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. App scopes are scopes that are defined and understood by this application only.
        self._directory_scope_ids: Optional[List[str]] = None
        # Read-only collection referencing the directory objects that are scope of the assignment. Provided so that callers can get the directory objects using $expand at the same time as getting the role assignment. Read-only.  Supports $expand.
        self._directory_scopes: Optional[List[directory_object.DirectoryObject]] = None
        # Name of the role assignment. Required.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Identifiers of the principals to which the assignment is granted.  Supports $filter (any operator only).
        self._principal_ids: Optional[List[str]] = None
        # Read-only collection referencing the assigned principals. Provided so that callers can get the principals using $expand at the same time as getting the role assignment. Read-only.  Supports $expand.
        self._principals: Optional[List[directory_object.DirectoryObject]] = None
        # Specifies the roleDefinition that the assignment is for. Provided so that callers can get the role definition using $expand at the same time as getting the role assignment.  Supports $filter (eq operator on id, isBuiltIn, and displayName, and startsWith operator on displayName)  and $expand.
        self._role_definition: Optional[unified_role_definition.UnifiedRoleDefinition] = None
        # Identifier of the unifiedRoleDefinition the assignment is for.
        self._role_definition_id: Optional[str] = None
    
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
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the role assignment.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the role assignment.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def directory_scope_ids(self,) -> Optional[List[str]]:
        """
        Gets the directoryScopeIds property value. Ids of the directory objects representing the scopes of the assignment. The scopes of an assignment determine the set of resources for which the principals have been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. App scopes are scopes that are defined and understood by this application only.
        Returns: Optional[List[str]]
        """
        return self._directory_scope_ids
    
    @directory_scope_ids.setter
    def directory_scope_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the directoryScopeIds property value. Ids of the directory objects representing the scopes of the assignment. The scopes of an assignment determine the set of resources for which the principals have been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. App scopes are scopes that are defined and understood by this application only.
        Args:
            value: Value to set for the directoryScopeIds property.
        """
        self._directory_scope_ids = value
    
    @property
    def directory_scopes(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the directoryScopes property value. Read-only collection referencing the directory objects that are scope of the assignment. Provided so that callers can get the directory objects using $expand at the same time as getting the role assignment. Read-only.  Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._directory_scopes
    
    @directory_scopes.setter
    def directory_scopes(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the directoryScopes property value. Read-only collection referencing the directory objects that are scope of the assignment. Provided so that callers can get the directory objects using $expand at the same time as getting the role assignment. Read-only.  Supports $expand.
        Args:
            value: Value to set for the directoryScopes property.
        """
        self._directory_scopes = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the role assignment. Required.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the role assignment. Required.
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
            "app_scope_ids": lambda n : setattr(self, 'app_scope_ids', n.get_collection_of_primitive_values(str)),
            "app_scopes": lambda n : setattr(self, 'app_scopes', n.get_collection_of_object_values(app_scope.AppScope)),
            "condition": lambda n : setattr(self, 'condition', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "directory_scope_ids": lambda n : setattr(self, 'directory_scope_ids', n.get_collection_of_primitive_values(str)),
            "directory_scopes": lambda n : setattr(self, 'directory_scopes', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "principal_ids": lambda n : setattr(self, 'principal_ids', n.get_collection_of_primitive_values(str)),
            "principals": lambda n : setattr(self, 'principals', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "role_definition": lambda n : setattr(self, 'role_definition', n.get_object_value(unified_role_definition.UnifiedRoleDefinition)),
            "role_definition_id": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def principal_ids(self,) -> Optional[List[str]]:
        """
        Gets the principalIds property value. Identifiers of the principals to which the assignment is granted.  Supports $filter (any operator only).
        Returns: Optional[List[str]]
        """
        return self._principal_ids
    
    @principal_ids.setter
    def principal_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the principalIds property value. Identifiers of the principals to which the assignment is granted.  Supports $filter (any operator only).
        Args:
            value: Value to set for the principalIds property.
        """
        self._principal_ids = value
    
    @property
    def principals(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the principals property value. Read-only collection referencing the assigned principals. Provided so that callers can get the principals using $expand at the same time as getting the role assignment. Read-only.  Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._principals
    
    @principals.setter
    def principals(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the principals property value. Read-only collection referencing the assigned principals. Provided so that callers can get the principals using $expand at the same time as getting the role assignment. Read-only.  Supports $expand.
        Args:
            value: Value to set for the principals property.
        """
        self._principals = value
    
    @property
    def role_definition(self,) -> Optional[unified_role_definition.UnifiedRoleDefinition]:
        """
        Gets the roleDefinition property value. Specifies the roleDefinition that the assignment is for. Provided so that callers can get the role definition using $expand at the same time as getting the role assignment.  Supports $filter (eq operator on id, isBuiltIn, and displayName, and startsWith operator on displayName)  and $expand.
        Returns: Optional[unified_role_definition.UnifiedRoleDefinition]
        """
        return self._role_definition
    
    @role_definition.setter
    def role_definition(self,value: Optional[unified_role_definition.UnifiedRoleDefinition] = None) -> None:
        """
        Sets the roleDefinition property value. Specifies the roleDefinition that the assignment is for. Provided so that callers can get the role definition using $expand at the same time as getting the role assignment.  Supports $filter (eq operator on id, isBuiltIn, and displayName, and startsWith operator on displayName)  and $expand.
        Args:
            value: Value to set for the roleDefinition property.
        """
        self._role_definition = value
    
    @property
    def role_definition_id(self,) -> Optional[str]:
        """
        Gets the roleDefinitionId property value. Identifier of the unifiedRoleDefinition the assignment is for.
        Returns: Optional[str]
        """
        return self._role_definition_id
    
    @role_definition_id.setter
    def role_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleDefinitionId property value. Identifier of the unifiedRoleDefinition the assignment is for.
        Args:
            value: Value to set for the roleDefinitionId property.
        """
        self._role_definition_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("appScopeIds", self.app_scope_ids)
        writer.write_collection_of_object_values("appScopes", self.app_scopes)
        writer.write_str_value("condition", self.condition)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_primitive_values("directoryScopeIds", self.directory_scope_ids)
        writer.write_collection_of_object_values("directoryScopes", self.directory_scopes)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("principalIds", self.principal_ids)
        writer.write_collection_of_object_values("principals", self.principals)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
    

