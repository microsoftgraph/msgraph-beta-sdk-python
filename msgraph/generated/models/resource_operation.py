from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ResourceOperation(entity.Entity):
    """
    Describes the resourceOperation resource (entity) of the Microsoft Graph API (REST), which supports Intune workflows related to role-based access control (RBAC).
    """
    @property
    def action_name(self,) -> Optional[str]:
        """
        Gets the actionName property value. Type of action this operation is going to perform. The actionName should be concise and limited to as few words as possible.
        Returns: Optional[str]
        """
        return self._action_name
    
    @action_name.setter
    def action_name(self,value: Optional[str] = None) -> None:
        """
        Sets the actionName property value. Type of action this operation is going to perform. The actionName should be concise and limited to as few words as possible.
        Args:
            value: Value to set for the actionName property.
        """
        self._action_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new resourceOperation and sets the default values.
        """
        super().__init__()
        # Type of action this operation is going to perform. The actionName should be concise and limited to as few words as possible.
        self._action_name: Optional[str] = None
        # Description of the resource operation. The description is used in mouse-over text for the operation when shown in the Azure Portal.
        self._description: Optional[str] = None
        # Determines whether the Permission is validated for Scopes defined per Role Assignment. This property is read-only.
        self._enabled_for_scope_validation: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Resource category to which this Operation belongs. This property is read-only.
        self._resource: Optional[str] = None
        # Name of the Resource this operation is performed on.
        self._resource_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ResourceOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ResourceOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ResourceOperation()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the resource operation. The description is used in mouse-over text for the operation when shown in the Azure Portal.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the resource operation. The description is used in mouse-over text for the operation when shown in the Azure Portal.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def enabled_for_scope_validation(self,) -> Optional[bool]:
        """
        Gets the enabledForScopeValidation property value. Determines whether the Permission is validated for Scopes defined per Role Assignment. This property is read-only.
        Returns: Optional[bool]
        """
        return self._enabled_for_scope_validation
    
    @enabled_for_scope_validation.setter
    def enabled_for_scope_validation(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabledForScopeValidation property value. Determines whether the Permission is validated for Scopes defined per Role Assignment. This property is read-only.
        Args:
            value: Value to set for the enabledForScopeValidation property.
        """
        self._enabled_for_scope_validation = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_name": lambda n : setattr(self, 'action_name', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "enabled_for_scope_validation": lambda n : setattr(self, 'enabled_for_scope_validation', n.get_bool_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_str_value()),
            "resource_name": lambda n : setattr(self, 'resource_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource(self,) -> Optional[str]:
        """
        Gets the resource property value. Resource category to which this Operation belongs. This property is read-only.
        Returns: Optional[str]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[str] = None) -> None:
        """
        Sets the resource property value. Resource category to which this Operation belongs. This property is read-only.
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    @property
    def resource_name(self,) -> Optional[str]:
        """
        Gets the resourceName property value. Name of the Resource this operation is performed on.
        Returns: Optional[str]
        """
        return self._resource_name
    
    @resource_name.setter
    def resource_name(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceName property value. Name of the Resource this operation is performed on.
        Args:
            value: Value to set for the resourceName property.
        """
        self._resource_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("actionName", self.action_name)
        writer.write_str_value("description", self.description)
        writer.write_str_value("resourceName", self.resource_name)
    

