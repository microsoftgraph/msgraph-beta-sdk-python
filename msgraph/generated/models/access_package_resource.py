from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_resource_attribute = lazy_import('msgraph.generated.models.access_package_resource_attribute')
access_package_resource_environment = lazy_import('msgraph.generated.models.access_package_resource_environment')
access_package_resource_role = lazy_import('msgraph.generated.models.access_package_resource_role')
access_package_resource_scope = lazy_import('msgraph.generated.models.access_package_resource_scope')
entity = lazy_import('msgraph.generated.models.entity')

class AccessPackageResource(entity.Entity):
    @property
    def access_package_resource_environment(self,) -> Optional[access_package_resource_environment.AccessPackageResourceEnvironment]:
        """
        Gets the accessPackageResourceEnvironment property value. Contains the environment information for the resource. This can be set using either the @odata.bind annotation or the environment's originId.Supports $expand.
        Returns: Optional[access_package_resource_environment.AccessPackageResourceEnvironment]
        """
        return self._access_package_resource_environment
    
    @access_package_resource_environment.setter
    def access_package_resource_environment(self,value: Optional[access_package_resource_environment.AccessPackageResourceEnvironment] = None) -> None:
        """
        Sets the accessPackageResourceEnvironment property value. Contains the environment information for the resource. This can be set using either the @odata.bind annotation or the environment's originId.Supports $expand.
        Args:
            value: Value to set for the accessPackageResourceEnvironment property.
        """
        self._access_package_resource_environment = value
    
    @property
    def access_package_resource_roles(self,) -> Optional[List[access_package_resource_role.AccessPackageResourceRole]]:
        """
        Gets the accessPackageResourceRoles property value. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[access_package_resource_role.AccessPackageResourceRole]]
        """
        return self._access_package_resource_roles
    
    @access_package_resource_roles.setter
    def access_package_resource_roles(self,value: Optional[List[access_package_resource_role.AccessPackageResourceRole]] = None) -> None:
        """
        Sets the accessPackageResourceRoles property value. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the accessPackageResourceRoles property.
        """
        self._access_package_resource_roles = value
    
    @property
    def access_package_resource_scopes(self,) -> Optional[List[access_package_resource_scope.AccessPackageResourceScope]]:
        """
        Gets the accessPackageResourceScopes property value. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[access_package_resource_scope.AccessPackageResourceScope]]
        """
        return self._access_package_resource_scopes
    
    @access_package_resource_scopes.setter
    def access_package_resource_scopes(self,value: Optional[List[access_package_resource_scope.AccessPackageResourceScope]] = None) -> None:
        """
        Sets the accessPackageResourceScopes property value. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the accessPackageResourceScopes property.
        """
        self._access_package_resource_scopes = value
    
    @property
    def added_by(self,) -> Optional[str]:
        """
        Gets the addedBy property value. The name of the user or application that first added this resource. Read-only.
        Returns: Optional[str]
        """
        return self._added_by
    
    @added_by.setter
    def added_by(self,value: Optional[str] = None) -> None:
        """
        Sets the addedBy property value. The name of the user or application that first added this resource. Read-only.
        Args:
            value: Value to set for the addedBy property.
        """
        self._added_by = value
    
    @property
    def added_on(self,) -> Optional[datetime]:
        """
        Gets the addedOn property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._added_on
    
    @added_on.setter
    def added_on(self,value: Optional[datetime] = None) -> None:
        """
        Sets the addedOn property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the addedOn property.
        """
        self._added_on = value
    
    @property
    def attributes(self,) -> Optional[List[access_package_resource_attribute.AccessPackageResourceAttribute]]:
        """
        Gets the attributes property value. Contains information about the attributes to be collected from the requestor and sent to the resource application.
        Returns: Optional[List[access_package_resource_attribute.AccessPackageResourceAttribute]]
        """
        return self._attributes
    
    @attributes.setter
    def attributes(self,value: Optional[List[access_package_resource_attribute.AccessPackageResourceAttribute]] = None) -> None:
        """
        Sets the attributes property value. Contains information about the attributes to be collected from the requestor and sent to the resource application.
        Args:
            value: Value to set for the attributes property.
        """
        self._attributes = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageResource and sets the default values.
        """
        super().__init__()
        # Contains the environment information for the resource. This can be set using either the @odata.bind annotation or the environment's originId.Supports $expand.
        self._access_package_resource_environment: Optional[access_package_resource_environment.AccessPackageResourceEnvironment] = None
        # Read-only. Nullable. Supports $expand.
        self._access_package_resource_roles: Optional[List[access_package_resource_role.AccessPackageResourceRole]] = None
        # Read-only. Nullable. Supports $expand.
        self._access_package_resource_scopes: Optional[List[access_package_resource_scope.AccessPackageResourceScope]] = None
        # The name of the user or application that first added this resource. Read-only.
        self._added_by: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._added_on: Optional[datetime] = None
        # Contains information about the attributes to be collected from the requestor and sent to the resource application.
        self._attributes: Optional[List[access_package_resource_attribute.AccessPackageResourceAttribute]] = None
        # A description for the resource.
        self._description: Optional[str] = None
        # The display name of the resource, such as the application name, group name or site name.
        self._display_name: Optional[str] = None
        # True if the resource is not yet available for assignment. Read-only.
        self._is_pending_onboarding: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The unique identifier of the resource in the origin system. In the case of an Azure AD group, this is the identifier of the group.
        self._origin_id: Optional[str] = None
        # The type of the resource in the origin system, such as SharePointOnline, AadApplication or AadGroup.
        self._origin_system: Optional[str] = None
        # The type of the resource, such as Application if it is an Azure AD connected application, or SharePoint Online Site for a SharePoint Online site.
        self._resource_type: Optional[str] = None
        # A unique resource locator for the resource, such as the URL for signing a user into an application.
        self._url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageResource()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. A description for the resource.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. A description for the resource.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the resource, such as the application name, group name or site name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the resource, such as the application name, group name or site name.
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
            "access_package_resource_environment": lambda n : setattr(self, 'access_package_resource_environment', n.get_object_value(access_package_resource_environment.AccessPackageResourceEnvironment)),
            "access_package_resource_roles": lambda n : setattr(self, 'access_package_resource_roles', n.get_collection_of_object_values(access_package_resource_role.AccessPackageResourceRole)),
            "access_package_resource_scopes": lambda n : setattr(self, 'access_package_resource_scopes', n.get_collection_of_object_values(access_package_resource_scope.AccessPackageResourceScope)),
            "added_by": lambda n : setattr(self, 'added_by', n.get_str_value()),
            "added_on": lambda n : setattr(self, 'added_on', n.get_datetime_value()),
            "attributes": lambda n : setattr(self, 'attributes', n.get_collection_of_object_values(access_package_resource_attribute.AccessPackageResourceAttribute)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_pending_onboarding": lambda n : setattr(self, 'is_pending_onboarding', n.get_bool_value()),
            "origin_id": lambda n : setattr(self, 'origin_id', n.get_str_value()),
            "origin_system": lambda n : setattr(self, 'origin_system', n.get_str_value()),
            "resource_type": lambda n : setattr(self, 'resource_type', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_pending_onboarding(self,) -> Optional[bool]:
        """
        Gets the isPendingOnboarding property value. True if the resource is not yet available for assignment. Read-only.
        Returns: Optional[bool]
        """
        return self._is_pending_onboarding
    
    @is_pending_onboarding.setter
    def is_pending_onboarding(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPendingOnboarding property value. True if the resource is not yet available for assignment. Read-only.
        Args:
            value: Value to set for the isPendingOnboarding property.
        """
        self._is_pending_onboarding = value
    
    @property
    def origin_id(self,) -> Optional[str]:
        """
        Gets the originId property value. The unique identifier of the resource in the origin system. In the case of an Azure AD group, this is the identifier of the group.
        Returns: Optional[str]
        """
        return self._origin_id
    
    @origin_id.setter
    def origin_id(self,value: Optional[str] = None) -> None:
        """
        Sets the originId property value. The unique identifier of the resource in the origin system. In the case of an Azure AD group, this is the identifier of the group.
        Args:
            value: Value to set for the originId property.
        """
        self._origin_id = value
    
    @property
    def origin_system(self,) -> Optional[str]:
        """
        Gets the originSystem property value. The type of the resource in the origin system, such as SharePointOnline, AadApplication or AadGroup.
        Returns: Optional[str]
        """
        return self._origin_system
    
    @origin_system.setter
    def origin_system(self,value: Optional[str] = None) -> None:
        """
        Sets the originSystem property value. The type of the resource in the origin system, such as SharePointOnline, AadApplication or AadGroup.
        Args:
            value: Value to set for the originSystem property.
        """
        self._origin_system = value
    
    @property
    def resource_type(self,) -> Optional[str]:
        """
        Gets the resourceType property value. The type of the resource, such as Application if it is an Azure AD connected application, or SharePoint Online Site for a SharePoint Online site.
        Returns: Optional[str]
        """
        return self._resource_type
    
    @resource_type.setter
    def resource_type(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceType property value. The type of the resource, such as Application if it is an Azure AD connected application, or SharePoint Online Site for a SharePoint Online site.
        Args:
            value: Value to set for the resourceType property.
        """
        self._resource_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def url(self,) -> Optional[str]:
        """
        Gets the url property value. A unique resource locator for the resource, such as the URL for signing a user into an application.
        Returns: Optional[str]
        """
        return self._url
    
    @url.setter
    def url(self,value: Optional[str] = None) -> None:
        """
        Sets the url property value. A unique resource locator for the resource, such as the URL for signing a user into an application.
        Args:
            value: Value to set for the url property.
        """
        self._url = value
    

