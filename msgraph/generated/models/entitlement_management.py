from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package, access_package_assignment, access_package_assignment_policy, access_package_assignment_request, access_package_assignment_resource_role, access_package_catalog, access_package_resource, access_package_resource_environment, access_package_resource_request, access_package_resource_role_scope, access_package_subject, approval, connected_organization, entitlement_management_settings, entity

from . import entity

@dataclass
class EntitlementManagement(entity.Entity):
    # The accessPackageAssignmentApprovals property
    access_package_assignment_approvals: Optional[List[approval.Approval]] = None
    # Represents the policy that governs which subjects can request or be assigned an access package via an access package assignment.
    access_package_assignment_policies: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]] = None
    # Represents access package assignment requests created by or on behalf of a user.
    access_package_assignment_requests: Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]] = None
    # Represents the resource-specific role which a subject has been assigned through an access package assignment.
    access_package_assignment_resource_roles: Optional[List[access_package_assignment_resource_role.AccessPackageAssignmentResourceRole]] = None
    # The assignment of an access package to a subject for a period of time.
    access_package_assignments: Optional[List[access_package_assignment.AccessPackageAssignment]] = None
    # A container of access packages.
    access_package_catalogs: Optional[List[access_package_catalog.AccessPackageCatalog]] = None
    # A reference to the geolocation environment in which a resource is located.
    access_package_resource_environments: Optional[List[access_package_resource_environment.AccessPackageResourceEnvironment]] = None
    # Represents a request to add or remove a resource to or from a catalog respectively.
    access_package_resource_requests: Optional[List[access_package_resource_request.AccessPackageResourceRequest]] = None
    # A reference to both a scope within a resource, and a role in that resource for that scope.
    access_package_resource_role_scopes: Optional[List[access_package_resource_role_scope.AccessPackageResourceRoleScope]] = None
    # A reference to a resource associated with an access package catalog.
    access_package_resources: Optional[List[access_package_resource.AccessPackageResource]] = None
    # Represents access package objects.
    access_packages: Optional[List[access_package.AccessPackage]] = None
    # Represents references to a directory or domain of another organization whose users can request access.
    connected_organizations: Optional[List[connected_organization.ConnectedOrganization]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the settings that control the behavior of Azure AD entitlement management.
    settings: Optional[entitlement_management_settings.EntitlementManagementSettings] = None
    # The subjects property
    subjects: Optional[List[access_package_subject.AccessPackageSubject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EntitlementManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EntitlementManagement
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EntitlementManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package, access_package_assignment, access_package_assignment_policy, access_package_assignment_request, access_package_assignment_resource_role, access_package_catalog, access_package_resource, access_package_resource_environment, access_package_resource_request, access_package_resource_role_scope, access_package_subject, approval, connected_organization, entitlement_management_settings, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessPackages": lambda n : setattr(self, 'access_packages', n.get_collection_of_object_values(access_package.AccessPackage)),
            "accessPackageAssignments": lambda n : setattr(self, 'access_package_assignments', n.get_collection_of_object_values(access_package_assignment.AccessPackageAssignment)),
            "accessPackageAssignmentApprovals": lambda n : setattr(self, 'access_package_assignment_approvals', n.get_collection_of_object_values(approval.Approval)),
            "accessPackageAssignmentPolicies": lambda n : setattr(self, 'access_package_assignment_policies', n.get_collection_of_object_values(access_package_assignment_policy.AccessPackageAssignmentPolicy)),
            "accessPackageAssignmentRequests": lambda n : setattr(self, 'access_package_assignment_requests', n.get_collection_of_object_values(access_package_assignment_request.AccessPackageAssignmentRequest)),
            "accessPackageAssignmentResourceRoles": lambda n : setattr(self, 'access_package_assignment_resource_roles', n.get_collection_of_object_values(access_package_assignment_resource_role.AccessPackageAssignmentResourceRole)),
            "accessPackageCatalogs": lambda n : setattr(self, 'access_package_catalogs', n.get_collection_of_object_values(access_package_catalog.AccessPackageCatalog)),
            "accessPackageResources": lambda n : setattr(self, 'access_package_resources', n.get_collection_of_object_values(access_package_resource.AccessPackageResource)),
            "accessPackageResourceEnvironments": lambda n : setattr(self, 'access_package_resource_environments', n.get_collection_of_object_values(access_package_resource_environment.AccessPackageResourceEnvironment)),
            "accessPackageResourceRequests": lambda n : setattr(self, 'access_package_resource_requests', n.get_collection_of_object_values(access_package_resource_request.AccessPackageResourceRequest)),
            "accessPackageResourceRoleScopes": lambda n : setattr(self, 'access_package_resource_role_scopes', n.get_collection_of_object_values(access_package_resource_role_scope.AccessPackageResourceRoleScope)),
            "connectedOrganizations": lambda n : setattr(self, 'connected_organizations', n.get_collection_of_object_values(connected_organization.ConnectedOrganization)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(entitlement_management_settings.EntitlementManagementSettings)),
            "subjects": lambda n : setattr(self, 'subjects', n.get_collection_of_object_values(access_package_subject.AccessPackageSubject)),
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
        writer.write_collection_of_object_values("accessPackageAssignments", self.access_package_assignments)
        writer.write_collection_of_object_values("accessPackageAssignmentApprovals", self.access_package_assignment_approvals)
        writer.write_collection_of_object_values("accessPackageAssignmentPolicies", self.access_package_assignment_policies)
        writer.write_collection_of_object_values("accessPackageAssignmentRequests", self.access_package_assignment_requests)
        writer.write_collection_of_object_values("accessPackageAssignmentResourceRoles", self.access_package_assignment_resource_roles)
        writer.write_collection_of_object_values("accessPackageCatalogs", self.access_package_catalogs)
        writer.write_collection_of_object_values("accessPackageResources", self.access_package_resources)
        writer.write_collection_of_object_values("accessPackageResourceEnvironments", self.access_package_resource_environments)
        writer.write_collection_of_object_values("accessPackageResourceRequests", self.access_package_resource_requests)
        writer.write_collection_of_object_values("accessPackageResourceRoleScopes", self.access_package_resource_role_scopes)
        writer.write_collection_of_object_values("connectedOrganizations", self.connected_organizations)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("subjects", self.subjects)
    

