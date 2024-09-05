from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package import AccessPackage
    from .access_package_assignment import AccessPackageAssignment
    from .access_package_assignment_policy import AccessPackageAssignmentPolicy
    from .access_package_assignment_request import AccessPackageAssignmentRequest
    from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
    from .access_package_catalog import AccessPackageCatalog
    from .access_package_resource import AccessPackageResource
    from .access_package_resource_environment import AccessPackageResourceEnvironment
    from .access_package_resource_request import AccessPackageResourceRequest
    from .access_package_resource_role_scope import AccessPackageResourceRoleScope
    from .access_package_subject import AccessPackageSubject
    from .approval import Approval
    from .connected_organization import ConnectedOrganization
    from .entitlement_management_settings import EntitlementManagementSettings
    from .entity import Entity

from .entity import Entity

@dataclass
class EntitlementManagement(Entity):
    # The accessPackageAssignmentApprovals property
    access_package_assignment_approvals: Optional[List[Approval]] = None
    # Represents the policy that governs which subjects can request or be assigned an access package via an access package assignment.
    access_package_assignment_policies: Optional[List[AccessPackageAssignmentPolicy]] = None
    # Represents access package assignment requests created by or on behalf of a user. DO NOT USE. TO BE RETIRED SOON. Use the assignmentRequests relationship instead.
    access_package_assignment_requests: Optional[List[AccessPackageAssignmentRequest]] = None
    # Represents the resource-specific role which a subject has been assigned through an access package assignment.
    access_package_assignment_resource_roles: Optional[List[AccessPackageAssignmentResourceRole]] = None
    # The assignment of an access package to a subject for a period of time.
    access_package_assignments: Optional[List[AccessPackageAssignment]] = None
    # A container of access packages.
    access_package_catalogs: Optional[List[AccessPackageCatalog]] = None
    # A reference to the geolocation environment in which a resource is located.
    access_package_resource_environments: Optional[List[AccessPackageResourceEnvironment]] = None
    # Represents a request to add or remove a resource to or from a catalog respectively.
    access_package_resource_requests: Optional[List[AccessPackageResourceRequest]] = None
    # A reference to both a scope within a resource, and a role in that resource for that scope.
    access_package_resource_role_scopes: Optional[List[AccessPackageResourceRoleScope]] = None
    # A reference to a resource associated with an access package catalog.
    access_package_resources: Optional[List[AccessPackageResource]] = None
    # Represents access package objects.
    access_packages: Optional[List[AccessPackage]] = None
    # Represents access package assignment requests created by or on behalf of a user.
    assignment_requests: Optional[List[AccessPackageAssignmentRequest]] = None
    # Represents references to a directory or domain of another organization whose users can request access.
    connected_organizations: Optional[List[ConnectedOrganization]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the settings that control the behavior of Microsoft Entra entitlement management.
    settings: Optional[EntitlementManagementSettings] = None
    # Represents the subjects within entitlement management.
    subjects: Optional[List[AccessPackageSubject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EntitlementManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EntitlementManagement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EntitlementManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package import AccessPackage
        from .access_package_assignment import AccessPackageAssignment
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_request import AccessPackageResourceRequest
        from .access_package_resource_role_scope import AccessPackageResourceRoleScope
        from .access_package_subject import AccessPackageSubject
        from .approval import Approval
        from .connected_organization import ConnectedOrganization
        from .entitlement_management_settings import EntitlementManagementSettings
        from .entity import Entity

        from .access_package import AccessPackage
        from .access_package_assignment import AccessPackageAssignment
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_request import AccessPackageResourceRequest
        from .access_package_resource_role_scope import AccessPackageResourceRoleScope
        from .access_package_subject import AccessPackageSubject
        from .approval import Approval
        from .connected_organization import ConnectedOrganization
        from .entitlement_management_settings import EntitlementManagementSettings
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessPackageAssignmentApprovals": lambda n : setattr(self, 'access_package_assignment_approvals', n.get_collection_of_object_values(Approval)),
            "accessPackageAssignmentPolicies": lambda n : setattr(self, 'access_package_assignment_policies', n.get_collection_of_object_values(AccessPackageAssignmentPolicy)),
            "accessPackageAssignmentRequests": lambda n : setattr(self, 'access_package_assignment_requests', n.get_collection_of_object_values(AccessPackageAssignmentRequest)),
            "accessPackageAssignmentResourceRoles": lambda n : setattr(self, 'access_package_assignment_resource_roles', n.get_collection_of_object_values(AccessPackageAssignmentResourceRole)),
            "accessPackageAssignments": lambda n : setattr(self, 'access_package_assignments', n.get_collection_of_object_values(AccessPackageAssignment)),
            "accessPackageCatalogs": lambda n : setattr(self, 'access_package_catalogs', n.get_collection_of_object_values(AccessPackageCatalog)),
            "accessPackageResourceEnvironments": lambda n : setattr(self, 'access_package_resource_environments', n.get_collection_of_object_values(AccessPackageResourceEnvironment)),
            "accessPackageResourceRequests": lambda n : setattr(self, 'access_package_resource_requests', n.get_collection_of_object_values(AccessPackageResourceRequest)),
            "accessPackageResourceRoleScopes": lambda n : setattr(self, 'access_package_resource_role_scopes', n.get_collection_of_object_values(AccessPackageResourceRoleScope)),
            "accessPackageResources": lambda n : setattr(self, 'access_package_resources', n.get_collection_of_object_values(AccessPackageResource)),
            "accessPackages": lambda n : setattr(self, 'access_packages', n.get_collection_of_object_values(AccessPackage)),
            "assignmentRequests": lambda n : setattr(self, 'assignment_requests', n.get_collection_of_object_values(AccessPackageAssignmentRequest)),
            "connectedOrganizations": lambda n : setattr(self, 'connected_organizations', n.get_collection_of_object_values(ConnectedOrganization)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(EntitlementManagementSettings)),
            "subjects": lambda n : setattr(self, 'subjects', n.get_collection_of_object_values(AccessPackageSubject)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("accessPackageAssignmentApprovals", self.access_package_assignment_approvals)
        writer.write_collection_of_object_values("accessPackageAssignmentPolicies", self.access_package_assignment_policies)
        writer.write_collection_of_object_values("accessPackageAssignmentRequests", self.access_package_assignment_requests)
        writer.write_collection_of_object_values("accessPackageAssignmentResourceRoles", self.access_package_assignment_resource_roles)
        writer.write_collection_of_object_values("accessPackageAssignments", self.access_package_assignments)
        writer.write_collection_of_object_values("accessPackageCatalogs", self.access_package_catalogs)
        writer.write_collection_of_object_values("accessPackageResourceEnvironments", self.access_package_resource_environments)
        writer.write_collection_of_object_values("accessPackageResourceRequests", self.access_package_resource_requests)
        writer.write_collection_of_object_values("accessPackageResourceRoleScopes", self.access_package_resource_role_scopes)
        writer.write_collection_of_object_values("accessPackageResources", self.access_package_resources)
        writer.write_collection_of_object_values("accessPackages", self.access_packages)
        writer.write_collection_of_object_values("assignmentRequests", self.assignment_requests)
        writer.write_collection_of_object_values("connectedOrganizations", self.connected_organizations)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("subjects", self.subjects)
    

