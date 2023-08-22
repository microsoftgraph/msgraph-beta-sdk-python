from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class ResourceOperation(Entity):
    """
    Describes the resourceOperation resource (entity) of the Microsoft Graph API (REST), which supports Intune workflows related to role-based access control (RBAC).
    """
    # Type of action this operation is going to perform. The actionName should be concise and limited to as few words as possible.
    action_name: Optional[str] = None
    # Description of the resource operation. The description is used in mouse-over text for the operation when shown in the Azure Portal.
    description: Optional[str] = None
    # Determines whether the Permission is validated for Scopes defined per Role Assignment. This property is read-only.
    enabled_for_scope_validation: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Resource category to which this Operation belongs. This property is read-only.
    resource: Optional[str] = None
    # Name of the Resource this operation is performed on.
    resource_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ResourceOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResourceOperation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ResourceOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "actionName": lambda n : setattr(self, 'action_name', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "enabledForScopeValidation": lambda n : setattr(self, 'enabled_for_scope_validation', n.get_bool_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_str_value()),
            "resourceName": lambda n : setattr(self, 'resource_name', n.get_str_value()),
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
        writer.write_str_value("actionName", self.action_name)
        writer.write_str_value("description", self.description)
        writer.write_str_value("resourceName", self.resource_name)
    

