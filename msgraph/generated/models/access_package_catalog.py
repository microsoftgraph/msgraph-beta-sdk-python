from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package, access_package_resource, access_package_resource_role, access_package_resource_scope, custom_access_package_workflow_extension, custom_callout_extension, entity

from . import entity

class AccessPackageCatalog(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageCatalog and sets the default values.
        """
        super().__init__()
        # The attributes of a logic app, which can be called at various stages of an access package request and assignment cycle.
        self._access_package_custom_workflow_extensions: Optional[List[custom_callout_extension.CustomCalloutExtension]] = None
        # The roles in each resource in a catalog. Read-only.
        self._access_package_resource_roles: Optional[List[access_package_resource_role.AccessPackageResourceRole]] = None
        # The accessPackageResourceScopes property
        self._access_package_resource_scopes: Optional[List[access_package_resource_scope.AccessPackageResourceScope]] = None
        # The accessPackageResources property
        self._access_package_resources: Optional[List[access_package_resource.AccessPackageResource]] = None
        # The access packages in this catalog. Read-only. Nullable. Supports $expand.
        self._access_packages: Optional[List[access_package.AccessPackage]] = None
        # Has the value Published if the access packages are available for management.
        self._catalog_status: Optional[str] = None
        # One of UserManaged or ServiceDefault.
        self._catalog_type: Optional[str] = None
        # UPN of the user who created this resource. Read-only.
        self._created_by: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The customAccessPackageWorkflowExtensions property
        self._custom_access_package_workflow_extensions: Optional[List[custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension]] = None
        # The description of the access package catalog.
        self._description: Optional[str] = None
        # The display name of the access package catalog. Supports $filter (eq, contains).
        self._display_name: Optional[str] = None
        # Whether the access packages in this catalog can be requested by users outside of the tenant.
        self._is_externally_visible: Optional[bool] = None
        # The UPN of the user who last modified this resource. Read-only.
        self._modified_by: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def access_package_custom_workflow_extensions(self,) -> Optional[List[custom_callout_extension.CustomCalloutExtension]]:
        """
        Gets the accessPackageCustomWorkflowExtensions property value. The attributes of a logic app, which can be called at various stages of an access package request and assignment cycle.
        Returns: Optional[List[custom_callout_extension.CustomCalloutExtension]]
        """
        return self._access_package_custom_workflow_extensions
    
    @access_package_custom_workflow_extensions.setter
    def access_package_custom_workflow_extensions(self,value: Optional[List[custom_callout_extension.CustomCalloutExtension]] = None) -> None:
        """
        Sets the accessPackageCustomWorkflowExtensions property value. The attributes of a logic app, which can be called at various stages of an access package request and assignment cycle.
        Args:
            value: Value to set for the access_package_custom_workflow_extensions property.
        """
        self._access_package_custom_workflow_extensions = value
    
    @property
    def access_package_resource_roles(self,) -> Optional[List[access_package_resource_role.AccessPackageResourceRole]]:
        """
        Gets the accessPackageResourceRoles property value. The roles in each resource in a catalog. Read-only.
        Returns: Optional[List[access_package_resource_role.AccessPackageResourceRole]]
        """
        return self._access_package_resource_roles
    
    @access_package_resource_roles.setter
    def access_package_resource_roles(self,value: Optional[List[access_package_resource_role.AccessPackageResourceRole]] = None) -> None:
        """
        Sets the accessPackageResourceRoles property value. The roles in each resource in a catalog. Read-only.
        Args:
            value: Value to set for the access_package_resource_roles property.
        """
        self._access_package_resource_roles = value
    
    @property
    def access_package_resource_scopes(self,) -> Optional[List[access_package_resource_scope.AccessPackageResourceScope]]:
        """
        Gets the accessPackageResourceScopes property value. The accessPackageResourceScopes property
        Returns: Optional[List[access_package_resource_scope.AccessPackageResourceScope]]
        """
        return self._access_package_resource_scopes
    
    @access_package_resource_scopes.setter
    def access_package_resource_scopes(self,value: Optional[List[access_package_resource_scope.AccessPackageResourceScope]] = None) -> None:
        """
        Sets the accessPackageResourceScopes property value. The accessPackageResourceScopes property
        Args:
            value: Value to set for the access_package_resource_scopes property.
        """
        self._access_package_resource_scopes = value
    
    @property
    def access_package_resources(self,) -> Optional[List[access_package_resource.AccessPackageResource]]:
        """
        Gets the accessPackageResources property value. The accessPackageResources property
        Returns: Optional[List[access_package_resource.AccessPackageResource]]
        """
        return self._access_package_resources
    
    @access_package_resources.setter
    def access_package_resources(self,value: Optional[List[access_package_resource.AccessPackageResource]] = None) -> None:
        """
        Sets the accessPackageResources property value. The accessPackageResources property
        Args:
            value: Value to set for the access_package_resources property.
        """
        self._access_package_resources = value
    
    @property
    def access_packages(self,) -> Optional[List[access_package.AccessPackage]]:
        """
        Gets the accessPackages property value. The access packages in this catalog. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[access_package.AccessPackage]]
        """
        return self._access_packages
    
    @access_packages.setter
    def access_packages(self,value: Optional[List[access_package.AccessPackage]] = None) -> None:
        """
        Sets the accessPackages property value. The access packages in this catalog. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the access_packages property.
        """
        self._access_packages = value
    
    @property
    def catalog_status(self,) -> Optional[str]:
        """
        Gets the catalogStatus property value. Has the value Published if the access packages are available for management.
        Returns: Optional[str]
        """
        return self._catalog_status
    
    @catalog_status.setter
    def catalog_status(self,value: Optional[str] = None) -> None:
        """
        Sets the catalogStatus property value. Has the value Published if the access packages are available for management.
        Args:
            value: Value to set for the catalog_status property.
        """
        self._catalog_status = value
    
    @property
    def catalog_type(self,) -> Optional[str]:
        """
        Gets the catalogType property value. One of UserManaged or ServiceDefault.
        Returns: Optional[str]
        """
        return self._catalog_type
    
    @catalog_type.setter
    def catalog_type(self,value: Optional[str] = None) -> None:
        """
        Sets the catalogType property value. One of UserManaged or ServiceDefault.
        Args:
            value: Value to set for the catalog_type property.
        """
        self._catalog_type = value
    
    @property
    def created_by(self,) -> Optional[str]:
        """
        Gets the createdBy property value. UPN of the user who created this resource. Read-only.
        Returns: Optional[str]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[str] = None) -> None:
        """
        Sets the createdBy property value. UPN of the user who created this resource. Read-only.
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageCatalog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageCatalog
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageCatalog()
    
    @property
    def custom_access_package_workflow_extensions(self,) -> Optional[List[custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension]]:
        """
        Gets the customAccessPackageWorkflowExtensions property value. The customAccessPackageWorkflowExtensions property
        Returns: Optional[List[custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension]]
        """
        return self._custom_access_package_workflow_extensions
    
    @custom_access_package_workflow_extensions.setter
    def custom_access_package_workflow_extensions(self,value: Optional[List[custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension]] = None) -> None:
        """
        Sets the customAccessPackageWorkflowExtensions property value. The customAccessPackageWorkflowExtensions property
        Args:
            value: Value to set for the custom_access_package_workflow_extensions property.
        """
        self._custom_access_package_workflow_extensions = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the access package catalog.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the access package catalog.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the access package catalog. Supports $filter (eq, contains).
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the access package catalog. Supports $filter (eq, contains).
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package, access_package_resource, access_package_resource_role, access_package_resource_scope, custom_access_package_workflow_extension, custom_callout_extension, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessPackages": lambda n : setattr(self, 'access_packages', n.get_collection_of_object_values(access_package.AccessPackage)),
            "accessPackageCustomWorkflowExtensions": lambda n : setattr(self, 'access_package_custom_workflow_extensions', n.get_collection_of_object_values(custom_callout_extension.CustomCalloutExtension)),
            "accessPackageResources": lambda n : setattr(self, 'access_package_resources', n.get_collection_of_object_values(access_package_resource.AccessPackageResource)),
            "accessPackageResourceRoles": lambda n : setattr(self, 'access_package_resource_roles', n.get_collection_of_object_values(access_package_resource_role.AccessPackageResourceRole)),
            "accessPackageResourceScopes": lambda n : setattr(self, 'access_package_resource_scopes', n.get_collection_of_object_values(access_package_resource_scope.AccessPackageResourceScope)),
            "catalogStatus": lambda n : setattr(self, 'catalog_status', n.get_str_value()),
            "catalogType": lambda n : setattr(self, 'catalog_type', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customAccessPackageWorkflowExtensions": lambda n : setattr(self, 'custom_access_package_workflow_extensions', n.get_collection_of_object_values(custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isExternallyVisible": lambda n : setattr(self, 'is_externally_visible', n.get_bool_value()),
            "modifiedBy": lambda n : setattr(self, 'modified_by', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_externally_visible(self,) -> Optional[bool]:
        """
        Gets the isExternallyVisible property value. Whether the access packages in this catalog can be requested by users outside of the tenant.
        Returns: Optional[bool]
        """
        return self._is_externally_visible
    
    @is_externally_visible.setter
    def is_externally_visible(self,value: Optional[bool] = None) -> None:
        """
        Sets the isExternallyVisible property value. Whether the access packages in this catalog can be requested by users outside of the tenant.
        Args:
            value: Value to set for the is_externally_visible property.
        """
        self._is_externally_visible = value
    
    @property
    def modified_by(self,) -> Optional[str]:
        """
        Gets the modifiedBy property value. The UPN of the user who last modified this resource. Read-only.
        Returns: Optional[str]
        """
        return self._modified_by
    
    @modified_by.setter
    def modified_by(self,value: Optional[str] = None) -> None:
        """
        Sets the modifiedBy property value. The UPN of the user who last modified this resource. Read-only.
        Args:
            value: Value to set for the modified_by property.
        """
        self._modified_by = value
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the modified_date_time property.
        """
        self._modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("accessPackages", self.access_packages)
        writer.write_collection_of_object_values("accessPackageCustomWorkflowExtensions", self.access_package_custom_workflow_extensions)
        writer.write_collection_of_object_values("accessPackageResources", self.access_package_resources)
        writer.write_collection_of_object_values("accessPackageResourceRoles", self.access_package_resource_roles)
        writer.write_collection_of_object_values("accessPackageResourceScopes", self.access_package_resource_scopes)
        writer.write_str_value("catalogStatus", self.catalog_status)
        writer.write_str_value("catalogType", self.catalog_type)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("customAccessPackageWorkflowExtensions", self.custom_access_package_workflow_extensions)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isExternallyVisible", self.is_externally_visible)
        writer.write_str_value("modifiedBy", self.modified_by)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
    

