from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_resource_attribute import AccessPackageResourceAttribute
    from .access_package_resource_environment import AccessPackageResourceEnvironment
    from .access_package_resource_role import AccessPackageResourceRole
    from .access_package_resource_scope import AccessPackageResourceScope
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageResource(Entity):
    # Contains the environment information for the resource. This can be set using either the @odata.bind annotation or the environment's originId.Supports $expand.
    access_package_resource_environment: Optional[AccessPackageResourceEnvironment] = None
    # Read-only. Nullable. Supports $expand.
    access_package_resource_roles: Optional[List[AccessPackageResourceRole]] = None
    # Read-only. Nullable. Supports $expand.
    access_package_resource_scopes: Optional[List[AccessPackageResourceScope]] = None
    # The name of the user or application that first added this resource. Read-only.
    added_by: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    added_on: Optional[datetime.datetime] = None
    # Contains information about the attributes to be collected from the requestor and sent to the resource application.
    attributes: Optional[List[AccessPackageResourceAttribute]] = None
    # A description for the resource.
    description: Optional[str] = None
    # The display name of the resource, such as the application name, group name or site name.
    display_name: Optional[str] = None
    # True if the resource is not yet available for assignment. Read-only.
    is_pending_onboarding: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier of the resource in the origin system. In the case of a Microsoft Entra group, this is the identifier of the group.
    origin_id: Optional[str] = None
    # The type of the resource in the origin system, such as SharePointOnline, AadApplication or AadGroup.
    origin_system: Optional[str] = None
    # The type of the resource, such as Application if it is a Microsoft Entra connected application, or SharePoint Online Site for a SharePoint Online site.
    resource_type: Optional[str] = None
    # A unique resource locator for the resource, such as the URL for signing a user into an application.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_resource_attribute import AccessPackageResourceAttribute
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .entity import Entity

        from .access_package_resource_attribute import AccessPackageResourceAttribute
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessPackageResourceEnvironment": lambda n : setattr(self, 'access_package_resource_environment', n.get_object_value(AccessPackageResourceEnvironment)),
            "accessPackageResourceRoles": lambda n : setattr(self, 'access_package_resource_roles', n.get_collection_of_object_values(AccessPackageResourceRole)),
            "accessPackageResourceScopes": lambda n : setattr(self, 'access_package_resource_scopes', n.get_collection_of_object_values(AccessPackageResourceScope)),
            "addedBy": lambda n : setattr(self, 'added_by', n.get_str_value()),
            "addedOn": lambda n : setattr(self, 'added_on', n.get_datetime_value()),
            "attributes": lambda n : setattr(self, 'attributes', n.get_collection_of_object_values(AccessPackageResourceAttribute)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isPendingOnboarding": lambda n : setattr(self, 'is_pending_onboarding', n.get_bool_value()),
            "originId": lambda n : setattr(self, 'origin_id', n.get_str_value()),
            "originSystem": lambda n : setattr(self, 'origin_system', n.get_str_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
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
        writer.write_object_value("accessPackageResourceEnvironment", self.access_package_resource_environment)
        writer.write_collection_of_object_values("accessPackageResourceRoles", self.access_package_resource_roles)
        writer.write_collection_of_object_values("accessPackageResourceScopes", self.access_package_resource_scopes)
        writer.write_str_value("addedBy", self.added_by)
        writer.write_datetime_value("addedOn", self.added_on)
        writer.write_collection_of_object_values("attributes", self.attributes)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isPendingOnboarding", self.is_pending_onboarding)
        writer.write_str_value("originId", self.origin_id)
        writer.write_str_value("originSystem", self.origin_system)
        writer.write_str_value("resourceType", self.resource_type)
        writer.write_str_value("url", self.url)
    

