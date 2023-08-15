from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_resource import AccessPackageResource
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageResourceScope(Entity):
    # The accessPackageResource property
    access_package_resource: Optional[AccessPackageResource] = None
    # The description of the scope.
    description: Optional[str] = None
    # The display name of the scope.
    display_name: Optional[str] = None
    # True if the scopes are arranged in a hierarchy and this is the top or root scope of the resource.
    is_root_scope: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier for the scope in the resource as defined in the origin system.
    origin_id: Optional[str] = None
    # The origin system for the scope.
    origin_system: Optional[str] = None
    # The origin system for the role, if different.
    role_origin_id: Optional[str] = None
    # A resource locator for the scope.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageResourceScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceScope
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResourceScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_resource import AccessPackageResource
        from .entity import Entity

        from .access_package_resource import AccessPackageResource
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessPackageResource": lambda n : setattr(self, 'access_package_resource', n.get_object_value(AccessPackageResource)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isRootScope": lambda n : setattr(self, 'is_root_scope', n.get_bool_value()),
            "originId": lambda n : setattr(self, 'origin_id', n.get_str_value()),
            "originSystem": lambda n : setattr(self, 'origin_system', n.get_str_value()),
            "roleOriginId": lambda n : setattr(self, 'role_origin_id', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_object_value("accessPackageResource", self.access_package_resource)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isRootScope", self.is_root_scope)
        writer.write_str_value("originId", self.origin_id)
        writer.write_str_value("originSystem", self.origin_system)
        writer.write_str_value("roleOriginId", self.role_origin_id)
        writer.write_str_value("url", self.url)
    

