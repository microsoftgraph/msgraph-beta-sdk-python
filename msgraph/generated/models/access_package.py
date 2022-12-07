from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_assignment_policy = lazy_import('msgraph.generated.models.access_package_assignment_policy')
access_package_catalog = lazy_import('msgraph.generated.models.access_package_catalog')
access_package_resource_role_scope = lazy_import('msgraph.generated.models.access_package_resource_role_scope')
entity = lazy_import('msgraph.generated.models.entity')
group = lazy_import('msgraph.generated.models.group')

class AccessPackage(entity.Entity):
    @property
    def access_package_assignment_policies(self,) -> Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]]:
        """
        Gets the accessPackageAssignmentPolicies property value. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]]
        """
        return self._access_package_assignment_policies
    
    @access_package_assignment_policies.setter
    def access_package_assignment_policies(self,value: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]] = None) -> None:
        """
        Sets the accessPackageAssignmentPolicies property value. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the accessPackageAssignmentPolicies property.
        """
        self._access_package_assignment_policies = value
    
    @property
    def access_package_catalog(self,) -> Optional[access_package_catalog.AccessPackageCatalog]:
        """
        Gets the accessPackageCatalog property value. The accessPackageCatalog property
        Returns: Optional[access_package_catalog.AccessPackageCatalog]
        """
        return self._access_package_catalog
    
    @access_package_catalog.setter
    def access_package_catalog(self,value: Optional[access_package_catalog.AccessPackageCatalog] = None) -> None:
        """
        Sets the accessPackageCatalog property value. The accessPackageCatalog property
        Args:
            value: Value to set for the accessPackageCatalog property.
        """
        self._access_package_catalog = value
    
    @property
    def access_package_resource_role_scopes(self,) -> Optional[List[access_package_resource_role_scope.AccessPackageResourceRoleScope]]:
        """
        Gets the accessPackageResourceRoleScopes property value. The accessPackageResourceRoleScopes property
        Returns: Optional[List[access_package_resource_role_scope.AccessPackageResourceRoleScope]]
        """
        return self._access_package_resource_role_scopes
    
    @access_package_resource_role_scopes.setter
    def access_package_resource_role_scopes(self,value: Optional[List[access_package_resource_role_scope.AccessPackageResourceRoleScope]] = None) -> None:
        """
        Sets the accessPackageResourceRoleScopes property value. The accessPackageResourceRoleScopes property
        Args:
            value: Value to set for the accessPackageResourceRoleScopes property.
        """
        self._access_package_resource_role_scopes = value
    
    @property
    def access_packages_incompatible_with(self,) -> Optional[List[AccessPackage]]:
        """
        Gets the accessPackagesIncompatibleWith property value. The access packages that are incompatible with this package. Read-only.
        Returns: Optional[List[AccessPackage]]
        """
        return self._access_packages_incompatible_with
    
    @access_packages_incompatible_with.setter
    def access_packages_incompatible_with(self,value: Optional[List[AccessPackage]] = None) -> None:
        """
        Sets the accessPackagesIncompatibleWith property value. The access packages that are incompatible with this package. Read-only.
        Args:
            value: Value to set for the accessPackagesIncompatibleWith property.
        """
        self._access_packages_incompatible_with = value
    
    @property
    def catalog_id(self,) -> Optional[str]:
        """
        Gets the catalogId property value. Identifier of the access package catalog referencing this access package. Read-only.
        Returns: Optional[str]
        """
        return self._catalog_id
    
    @catalog_id.setter
    def catalog_id(self,value: Optional[str] = None) -> None:
        """
        Sets the catalogId property value. Identifier of the access package catalog referencing this access package. Read-only.
        Args:
            value: Value to set for the catalogId property.
        """
        self._catalog_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackage and sets the default values.
        """
        super().__init__()
        # Read-only. Nullable. Supports $expand.
        self._access_package_assignment_policies: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]] = None
        # The accessPackageCatalog property
        self._access_package_catalog: Optional[access_package_catalog.AccessPackageCatalog] = None
        # The accessPackageResourceRoleScopes property
        self._access_package_resource_role_scopes: Optional[List[access_package_resource_role_scope.AccessPackageResourceRoleScope]] = None
        # The access packages that are incompatible with this package. Read-only.
        self._access_packages_incompatible_with: Optional[List[AccessPackage]] = None
        # Identifier of the access package catalog referencing this access package. Read-only.
        self._catalog_id: Optional[str] = None
        # The userPrincipalName of the user or identity of the subject who created this resource. Read-only.
        self._created_by: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The description of the access package.
        self._description: Optional[str] = None
        # The display name of the access package. Supports $filter (eq, contains).
        self._display_name: Optional[str] = None
        # The  access packages whose assigned users are ineligible to be assigned this access package.
        self._incompatible_access_packages: Optional[List[AccessPackage]] = None
        # The groups whose members are ineligible to be assigned this access package.
        self._incompatible_groups: Optional[List[group.Group]] = None
        # Whether the access package is hidden from the requestor.
        self._is_hidden: Optional[bool] = None
        # Indicates whether role scopes are visible.
        self._is_role_scopes_visible: Optional[bool] = None
        # The userPrincipalName of the user who last modified this resource. Read-only.
        self._modified_by: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[str]:
        """
        Gets the createdBy property value. The userPrincipalName of the user or identity of the subject who created this resource. Read-only.
        Returns: Optional[str]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[str] = None) -> None:
        """
        Sets the createdBy property value. The userPrincipalName of the user or identity of the subject who created this resource. Read-only.
        Args:
            value: Value to set for the createdBy property.
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
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackage()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the access package.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the access package.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the access package. Supports $filter (eq, contains).
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the access package. Supports $filter (eq, contains).
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
            "access_package_assignment_policies": lambda n : setattr(self, 'access_package_assignment_policies', n.get_collection_of_object_values(access_package_assignment_policy.AccessPackageAssignmentPolicy)),
            "access_package_catalog": lambda n : setattr(self, 'access_package_catalog', n.get_object_value(access_package_catalog.AccessPackageCatalog)),
            "access_package_resource_role_scopes": lambda n : setattr(self, 'access_package_resource_role_scopes', n.get_collection_of_object_values(access_package_resource_role_scope.AccessPackageResourceRoleScope)),
            "access_packages_incompatible_with": lambda n : setattr(self, 'access_packages_incompatible_with', n.get_collection_of_object_values(AccessPackage)),
            "catalog_id": lambda n : setattr(self, 'catalog_id', n.get_str_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "incompatible_access_packages": lambda n : setattr(self, 'incompatible_access_packages', n.get_collection_of_object_values(AccessPackage)),
            "incompatible_groups": lambda n : setattr(self, 'incompatible_groups', n.get_collection_of_object_values(group.Group)),
            "is_hidden": lambda n : setattr(self, 'is_hidden', n.get_bool_value()),
            "is_role_scopes_visible": lambda n : setattr(self, 'is_role_scopes_visible', n.get_bool_value()),
            "modified_by": lambda n : setattr(self, 'modified_by', n.get_str_value()),
            "modified_date_time": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def incompatible_access_packages(self,) -> Optional[List[AccessPackage]]:
        """
        Gets the incompatibleAccessPackages property value. The  access packages whose assigned users are ineligible to be assigned this access package.
        Returns: Optional[List[AccessPackage]]
        """
        return self._incompatible_access_packages
    
    @incompatible_access_packages.setter
    def incompatible_access_packages(self,value: Optional[List[AccessPackage]] = None) -> None:
        """
        Sets the incompatibleAccessPackages property value. The  access packages whose assigned users are ineligible to be assigned this access package.
        Args:
            value: Value to set for the incompatibleAccessPackages property.
        """
        self._incompatible_access_packages = value
    
    @property
    def incompatible_groups(self,) -> Optional[List[group.Group]]:
        """
        Gets the incompatibleGroups property value. The groups whose members are ineligible to be assigned this access package.
        Returns: Optional[List[group.Group]]
        """
        return self._incompatible_groups
    
    @incompatible_groups.setter
    def incompatible_groups(self,value: Optional[List[group.Group]] = None) -> None:
        """
        Sets the incompatibleGroups property value. The groups whose members are ineligible to be assigned this access package.
        Args:
            value: Value to set for the incompatibleGroups property.
        """
        self._incompatible_groups = value
    
    @property
    def is_hidden(self,) -> Optional[bool]:
        """
        Gets the isHidden property value. Whether the access package is hidden from the requestor.
        Returns: Optional[bool]
        """
        return self._is_hidden
    
    @is_hidden.setter
    def is_hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the isHidden property value. Whether the access package is hidden from the requestor.
        Args:
            value: Value to set for the isHidden property.
        """
        self._is_hidden = value
    
    @property
    def is_role_scopes_visible(self,) -> Optional[bool]:
        """
        Gets the isRoleScopesVisible property value. Indicates whether role scopes are visible.
        Returns: Optional[bool]
        """
        return self._is_role_scopes_visible
    
    @is_role_scopes_visible.setter
    def is_role_scopes_visible(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRoleScopesVisible property value. Indicates whether role scopes are visible.
        Args:
            value: Value to set for the isRoleScopesVisible property.
        """
        self._is_role_scopes_visible = value
    
    @property
    def modified_by(self,) -> Optional[str]:
        """
        Gets the modifiedBy property value. The userPrincipalName of the user who last modified this resource. Read-only.
        Returns: Optional[str]
        """
        return self._modified_by
    
    @modified_by.setter
    def modified_by(self,value: Optional[str] = None) -> None:
        """
        Sets the modifiedBy property value. The userPrincipalName of the user who last modified this resource. Read-only.
        Args:
            value: Value to set for the modifiedBy property.
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
            value: Value to set for the modifiedDateTime property.
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
        writer.write_collection_of_object_values("accessPackageAssignmentPolicies", self.access_package_assignment_policies)
        writer.write_object_value("accessPackageCatalog", self.access_package_catalog)
        writer.write_collection_of_object_values("accessPackageResourceRoleScopes", self.access_package_resource_role_scopes)
        writer.write_collection_of_object_values("accessPackagesIncompatibleWith", self.access_packages_incompatible_with)
        writer.write_str_value("catalogId", self.catalog_id)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("incompatibleAccessPackages", self.incompatible_access_packages)
        writer.write_collection_of_object_values("incompatibleGroups", self.incompatible_groups)
        writer.write_bool_value("isHidden", self.is_hidden)
        writer.write_bool_value("isRoleScopesVisible", self.is_role_scopes_visible)
        writer.write_str_value("modifiedBy", self.modified_by)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
    

