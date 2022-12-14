from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
unified_rbac_resource_scope = lazy_import('msgraph.generated.models.unified_rbac_resource_scope')

class UnifiedRbacResourceAction(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def action_verb(self,) -> Optional[str]:
        """
        Gets the actionVerb property value. HTTP method for the action, such as DELETE, GET, PATCH, POST, PUT, or null. Supports $filter (eq) but not for null values.
        Returns: Optional[str]
        """
        return self._action_verb
    
    @action_verb.setter
    def action_verb(self,value: Optional[str] = None) -> None:
        """
        Sets the actionVerb property value. HTTP method for the action, such as DELETE, GET, PATCH, POST, PUT, or null. Supports $filter (eq) but not for null values.
        Args:
            value: Value to set for the actionVerb property.
        """
        self._action_verb = value
    
    @property
    def authentication_context_id(self,) -> Optional[str]:
        """
        Gets the authenticationContextId property value. The authenticationContextId property
        Returns: Optional[str]
        """
        return self._authentication_context_id
    
    @authentication_context_id.setter
    def authentication_context_id(self,value: Optional[str] = None) -> None:
        """
        Sets the authenticationContextId property value. The authenticationContextId property
        Args:
            value: Value to set for the authenticationContextId property.
        """
        self._authentication_context_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRbacResourceAction and sets the default values.
        """
        super().__init__()
        # HTTP method for the action, such as DELETE, GET, PATCH, POST, PUT, or null. Supports $filter (eq) but not for null values.
        self._action_verb: Optional[str] = None
        # The authenticationContextId property
        self._authentication_context_id: Optional[str] = None
        # Description for the action. Supports $filter (eq).
        self._description: Optional[str] = None
        # The isAuthenticationContextSettable property
        self._is_authentication_context_settable: Optional[bool] = None
        # Name for the action within the resource namespace, such as microsoft.insights/programs/update. Can include slash character (/). Case insensitive. Required. Supports $filter (eq).
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The resourceScope property
        self._resource_scope: Optional[unified_rbac_resource_scope.UnifiedRbacResourceScope] = None
        # Not implemented.
        self._resource_scope_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRbacResourceAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRbacResourceAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRbacResourceAction()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description for the action. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description for the action. Supports $filter (eq).
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_verb": lambda n : setattr(self, 'action_verb', n.get_str_value()),
            "authentication_context_id": lambda n : setattr(self, 'authentication_context_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "is_authentication_context_settable": lambda n : setattr(self, 'is_authentication_context_settable', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "resource_scope": lambda n : setattr(self, 'resource_scope', n.get_object_value(unified_rbac_resource_scope.UnifiedRbacResourceScope)),
            "resource_scope_id": lambda n : setattr(self, 'resource_scope_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_authentication_context_settable(self,) -> Optional[bool]:
        """
        Gets the isAuthenticationContextSettable property value. The isAuthenticationContextSettable property
        Returns: Optional[bool]
        """
        return self._is_authentication_context_settable
    
    @is_authentication_context_settable.setter
    def is_authentication_context_settable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAuthenticationContextSettable property value. The isAuthenticationContextSettable property
        Args:
            value: Value to set for the isAuthenticationContextSettable property.
        """
        self._is_authentication_context_settable = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name for the action within the resource namespace, such as microsoft.insights/programs/update. Can include slash character (/). Case insensitive. Required. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name for the action within the resource namespace, such as microsoft.insights/programs/update. Can include slash character (/). Case insensitive. Required. Supports $filter (eq).
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def resource_scope(self,) -> Optional[unified_rbac_resource_scope.UnifiedRbacResourceScope]:
        """
        Gets the resourceScope property value. The resourceScope property
        Returns: Optional[unified_rbac_resource_scope.UnifiedRbacResourceScope]
        """
        return self._resource_scope
    
    @resource_scope.setter
    def resource_scope(self,value: Optional[unified_rbac_resource_scope.UnifiedRbacResourceScope] = None) -> None:
        """
        Sets the resourceScope property value. The resourceScope property
        Args:
            value: Value to set for the resourceScope property.
        """
        self._resource_scope = value
    
    @property
    def resource_scope_id(self,) -> Optional[str]:
        """
        Gets the resourceScopeId property value. Not implemented.
        Returns: Optional[str]
        """
        return self._resource_scope_id
    
    @resource_scope_id.setter
    def resource_scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceScopeId property value. Not implemented.
        Args:
            value: Value to set for the resourceScopeId property.
        """
        self._resource_scope_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("actionVerb", self.action_verb)
        writer.write_str_value("authenticationContextId", self.authentication_context_id)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("isAuthenticationContextSettable", self.is_authentication_context_settable)
        writer.write_str_value("name", self.name)
        writer.write_object_value("resourceScope", self.resource_scope)
        writer.write_str_value("resourceScopeId", self.resource_scope_id)
    

