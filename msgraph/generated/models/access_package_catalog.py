from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package, access_package_resource, access_package_resource_role, access_package_resource_scope, custom_access_package_workflow_extension, custom_callout_extension, entity

from . import entity

@dataclass
class AccessPackageCatalog(entity.Entity):
    # The attributes of a logic app, which can be called at various stages of an access package request and assignment cycle.
    access_package_custom_workflow_extensions: Optional[List[custom_callout_extension.CustomCalloutExtension]] = None
    # The roles in each resource in a catalog. Read-only.
    access_package_resource_roles: Optional[List[access_package_resource_role.AccessPackageResourceRole]] = None
    # The accessPackageResourceScopes property
    access_package_resource_scopes: Optional[List[access_package_resource_scope.AccessPackageResourceScope]] = None
    # The accessPackageResources property
    access_package_resources: Optional[List[access_package_resource.AccessPackageResource]] = None
    # The access packages in this catalog. Read-only. Nullable. Supports $expand.
    access_packages: Optional[List[access_package.AccessPackage]] = None
    # Has the value Published if the access packages are available for management.
    catalog_status: Optional[str] = None
    # One of UserManaged or ServiceDefault.
    catalog_type: Optional[str] = None
    # UPN of the user who created this resource. Read-only.
    created_by: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime] = None
    # The customAccessPackageWorkflowExtensions property
    custom_access_package_workflow_extensions: Optional[List[custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension]] = None
    # The description of the access package catalog.
    description: Optional[str] = None
    # The display name of the access package catalog. Supports $filter (eq, contains).
    display_name: Optional[str] = None
    # Whether the access packages in this catalog can be requested by users outside of the tenant.
    is_externally_visible: Optional[bool] = None
    # The UPN of the user who last modified this resource. Read-only.
    modified_by: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
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
    

