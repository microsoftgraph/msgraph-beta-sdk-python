from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_scope = lazy_import('msgraph.generated.models.app_scope')
directory_object = lazy_import('msgraph.generated.models.directory_object')
entity = lazy_import('msgraph.generated.models.entity')
unified_role_definition = lazy_import('msgraph.generated.models.unified_role_definition')

class UnifiedRoleAssignment(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def app_scope(self,) -> Optional[app_scope.AppScope]:
        """
        Gets the appScope property value. Details of the app specific scope when the assignment scope is app specific. Containment entity.
        Returns: Optional[app_scope.AppScope]
        """
        return self._app_scope
    
    @app_scope.setter
    def app_scope(self,value: Optional[app_scope.AppScope] = None) -> None:
        """
        Sets the appScope property value. Details of the app specific scope when the assignment scope is app specific. Containment entity.
        Args:
            value: Value to set for the appScope property.
        """
        self._app_scope = value
    
    @property
    def app_scope_id(self,) -> Optional[str]:
        """
        Gets the appScopeId property value. Identifier of the app specific scope when the assignment scope is app specific. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. App scopes are scopes that are defined and understood by this application only.  For the entitlement management provider, use app scopes to specify a catalog, for example /AccessPackageCatalog/beedadfe-01d5-4025-910b-84abb9369997.
        Returns: Optional[str]
        """
        return self._app_scope_id
    
    @app_scope_id.setter
    def app_scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appScopeId property value. Identifier of the app specific scope when the assignment scope is app specific. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. App scopes are scopes that are defined and understood by this application only.  For the entitlement management provider, use app scopes to specify a catalog, for example /AccessPackageCatalog/beedadfe-01d5-4025-910b-84abb9369997.
        Args:
            value: Value to set for the appScopeId property.
        """
        self._app_scope_id = value
    
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
        Instantiates a new unifiedRoleAssignment and sets the default values.
        """
        super().__init__()
        # Details of the app specific scope when the assignment scope is app specific. Containment entity.
        self._app_scope: Optional[app_scope.AppScope] = None
        # Identifier of the app specific scope when the assignment scope is app specific. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. App scopes are scopes that are defined and understood by this application only.  For the entitlement management provider, use app scopes to specify a catalog, for example /AccessPackageCatalog/beedadfe-01d5-4025-910b-84abb9369997.
        self._app_scope_id: Optional[str] = None
        # The condition property
        self._condition: Optional[str] = None
        # The directory object that is the scope of the assignment. Provided so that callers can get the directory object using $expand at the same time as getting the role assignment. Read-only. Supports $expand.
        self._directory_scope: Optional[directory_object.DirectoryObject] = None
        # Identifier of the directory object representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. App scopes are scopes that are defined and understood by this application only.
        self._directory_scope_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The assigned principal. Provided so that callers can get the principal using $expand at the same time as getting the role assignment. Read-only. Supports $expand.
        self._principal: Optional[directory_object.DirectoryObject] = None
        # Identifier of the principal to which the assignment is granted. Supports $filter (eq operator only).
        self._principal_id: Optional[str] = None
        # The principalOrganizationId property
        self._principal_organization_id: Optional[str] = None
        # The scope at which the unifiedRoleAssignment applies. This is / for service-wide. DO NOT USE. This property will be deprecated soon.
        self._resource_scope: Optional[str] = None
        # The roleDefinition the assignment is for. Provided so that callers can get the role definition using $expand at the same time as getting the role assignment. roleDefinition.id will be auto expanded. Supports $expand.
        self._role_definition: Optional[unified_role_definition.UnifiedRoleDefinition] = None
        # Identifier of the unifiedRoleDefinition the assignment is for. Read-only. Supports $filter (eq operator only).
        self._role_definition_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleAssignment()
    
    @property
    def directory_scope(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the directoryScope property value. The directory object that is the scope of the assignment. Provided so that callers can get the directory object using $expand at the same time as getting the role assignment. Read-only. Supports $expand.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._directory_scope
    
    @directory_scope.setter
    def directory_scope(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the directoryScope property value. The directory object that is the scope of the assignment. Provided so that callers can get the directory object using $expand at the same time as getting the role assignment. Read-only. Supports $expand.
        Args:
            value: Value to set for the directoryScope property.
        """
        self._directory_scope = value
    
    @property
    def directory_scope_id(self,) -> Optional[str]:
        """
        Gets the directoryScopeId property value. Identifier of the directory object representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. App scopes are scopes that are defined and understood by this application only.
        Returns: Optional[str]
        """
        return self._directory_scope_id
    
    @directory_scope_id.setter
    def directory_scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the directoryScopeId property value. Identifier of the directory object representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. App scopes are scopes that are defined and understood by this application only.
        Args:
            value: Value to set for the directoryScopeId property.
        """
        self._directory_scope_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_scope": lambda n : setattr(self, 'app_scope', n.get_object_value(app_scope.AppScope)),
            "app_scope_id": lambda n : setattr(self, 'app_scope_id', n.get_str_value()),
            "condition": lambda n : setattr(self, 'condition', n.get_str_value()),
            "directory_scope": lambda n : setattr(self, 'directory_scope', n.get_object_value(directory_object.DirectoryObject)),
            "directory_scope_id": lambda n : setattr(self, 'directory_scope_id', n.get_str_value()),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(directory_object.DirectoryObject)),
            "principal_id": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "principal_organization_id": lambda n : setattr(self, 'principal_organization_id', n.get_str_value()),
            "resource_scope": lambda n : setattr(self, 'resource_scope', n.get_str_value()),
            "role_definition": lambda n : setattr(self, 'role_definition', n.get_object_value(unified_role_definition.UnifiedRoleDefinition)),
            "role_definition_id": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def principal(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the principal property value. The assigned principal. Provided so that callers can get the principal using $expand at the same time as getting the role assignment. Read-only. Supports $expand.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._principal
    
    @principal.setter
    def principal(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the principal property value. The assigned principal. Provided so that callers can get the principal using $expand at the same time as getting the role assignment. Read-only. Supports $expand.
        Args:
            value: Value to set for the principal property.
        """
        self._principal = value
    
    @property
    def principal_id(self,) -> Optional[str]:
        """
        Gets the principalId property value. Identifier of the principal to which the assignment is granted. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._principal_id
    
    @principal_id.setter
    def principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the principalId property value. Identifier of the principal to which the assignment is granted. Supports $filter (eq operator only).
        Args:
            value: Value to set for the principalId property.
        """
        self._principal_id = value
    
    @property
    def principal_organization_id(self,) -> Optional[str]:
        """
        Gets the principalOrganizationId property value. The principalOrganizationId property
        Returns: Optional[str]
        """
        return self._principal_organization_id
    
    @principal_organization_id.setter
    def principal_organization_id(self,value: Optional[str] = None) -> None:
        """
        Sets the principalOrganizationId property value. The principalOrganizationId property
        Args:
            value: Value to set for the principalOrganizationId property.
        """
        self._principal_organization_id = value
    
    @property
    def resource_scope(self,) -> Optional[str]:
        """
        Gets the resourceScope property value. The scope at which the unifiedRoleAssignment applies. This is / for service-wide. DO NOT USE. This property will be deprecated soon.
        Returns: Optional[str]
        """
        return self._resource_scope
    
    @resource_scope.setter
    def resource_scope(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceScope property value. The scope at which the unifiedRoleAssignment applies. This is / for service-wide. DO NOT USE. This property will be deprecated soon.
        Args:
            value: Value to set for the resourceScope property.
        """
        self._resource_scope = value
    
    @property
    def role_definition(self,) -> Optional[unified_role_definition.UnifiedRoleDefinition]:
        """
        Gets the roleDefinition property value. The roleDefinition the assignment is for. Provided so that callers can get the role definition using $expand at the same time as getting the role assignment. roleDefinition.id will be auto expanded. Supports $expand.
        Returns: Optional[unified_role_definition.UnifiedRoleDefinition]
        """
        return self._role_definition
    
    @role_definition.setter
    def role_definition(self,value: Optional[unified_role_definition.UnifiedRoleDefinition] = None) -> None:
        """
        Sets the roleDefinition property value. The roleDefinition the assignment is for. Provided so that callers can get the role definition using $expand at the same time as getting the role assignment. roleDefinition.id will be auto expanded. Supports $expand.
        Args:
            value: Value to set for the roleDefinition property.
        """
        self._role_definition = value
    
    @property
    def role_definition_id(self,) -> Optional[str]:
        """
        Gets the roleDefinitionId property value. Identifier of the unifiedRoleDefinition the assignment is for. Read-only. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._role_definition_id
    
    @role_definition_id.setter
    def role_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleDefinitionId property value. Identifier of the unifiedRoleDefinition the assignment is for. Read-only. Supports $filter (eq operator only).
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
    

