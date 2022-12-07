from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package = lazy_import('msgraph.generated.models.access_package')
access_package_assignment = lazy_import('msgraph.generated.models.access_package_assignment')
access_package_assignment_policy = lazy_import('msgraph.generated.models.access_package_assignment_policy')
access_package_assignment_request = lazy_import('msgraph.generated.models.access_package_assignment_request')
access_package_assignment_resource_role = lazy_import('msgraph.generated.models.access_package_assignment_resource_role')
access_package_catalog = lazy_import('msgraph.generated.models.access_package_catalog')
access_package_resource = lazy_import('msgraph.generated.models.access_package_resource')
access_package_resource_environment = lazy_import('msgraph.generated.models.access_package_resource_environment')
access_package_resource_request = lazy_import('msgraph.generated.models.access_package_resource_request')
access_package_resource_role_scope = lazy_import('msgraph.generated.models.access_package_resource_role_scope')
access_package_subject = lazy_import('msgraph.generated.models.access_package_subject')
approval = lazy_import('msgraph.generated.models.approval')
connected_organization = lazy_import('msgraph.generated.models.connected_organization')
entitlement_management_settings = lazy_import('msgraph.generated.models.entitlement_management_settings')
entity = lazy_import('msgraph.generated.models.entity')

class EntitlementManagement(entity.Entity):
    @property
    def access_package_assignment_approvals(self,) -> Optional[List[approval.Approval]]:
        """
        Gets the accessPackageAssignmentApprovals property value. The accessPackageAssignmentApprovals property
        Returns: Optional[List[approval.Approval]]
        """
        return self._access_package_assignment_approvals
    
    @access_package_assignment_approvals.setter
    def access_package_assignment_approvals(self,value: Optional[List[approval.Approval]] = None) -> None:
        """
        Sets the accessPackageAssignmentApprovals property value. The accessPackageAssignmentApprovals property
        Args:
            value: Value to set for the accessPackageAssignmentApprovals property.
        """
        self._access_package_assignment_approvals = value
    
    @property
    def access_package_assignment_policies(self,) -> Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]]:
        """
        Gets the accessPackageAssignmentPolicies property value. Represents the policy that governs which subjects can request or be assigned an access package via an access package assignment.
        Returns: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]]
        """
        return self._access_package_assignment_policies
    
    @access_package_assignment_policies.setter
    def access_package_assignment_policies(self,value: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]] = None) -> None:
        """
        Sets the accessPackageAssignmentPolicies property value. Represents the policy that governs which subjects can request or be assigned an access package via an access package assignment.
        Args:
            value: Value to set for the accessPackageAssignmentPolicies property.
        """
        self._access_package_assignment_policies = value
    
    @property
    def access_package_assignment_requests(self,) -> Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]]:
        """
        Gets the accessPackageAssignmentRequests property value. Represents access package assignment requests created by or on behalf of a user.
        Returns: Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]]
        """
        return self._access_package_assignment_requests
    
    @access_package_assignment_requests.setter
    def access_package_assignment_requests(self,value: Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]] = None) -> None:
        """
        Sets the accessPackageAssignmentRequests property value. Represents access package assignment requests created by or on behalf of a user.
        Args:
            value: Value to set for the accessPackageAssignmentRequests property.
        """
        self._access_package_assignment_requests = value
    
    @property
    def access_package_assignment_resource_roles(self,) -> Optional[List[access_package_assignment_resource_role.AccessPackageAssignmentResourceRole]]:
        """
        Gets the accessPackageAssignmentResourceRoles property value. Represents the resource-specific role which a subject has been assigned through an access package assignment.
        Returns: Optional[List[access_package_assignment_resource_role.AccessPackageAssignmentResourceRole]]
        """
        return self._access_package_assignment_resource_roles
    
    @access_package_assignment_resource_roles.setter
    def access_package_assignment_resource_roles(self,value: Optional[List[access_package_assignment_resource_role.AccessPackageAssignmentResourceRole]] = None) -> None:
        """
        Sets the accessPackageAssignmentResourceRoles property value. Represents the resource-specific role which a subject has been assigned through an access package assignment.
        Args:
            value: Value to set for the accessPackageAssignmentResourceRoles property.
        """
        self._access_package_assignment_resource_roles = value
    
    @property
    def access_package_assignments(self,) -> Optional[List[access_package_assignment.AccessPackageAssignment]]:
        """
        Gets the accessPackageAssignments property value. The assignment of an access package to a subject for a period of time.
        Returns: Optional[List[access_package_assignment.AccessPackageAssignment]]
        """
        return self._access_package_assignments
    
    @access_package_assignments.setter
    def access_package_assignments(self,value: Optional[List[access_package_assignment.AccessPackageAssignment]] = None) -> None:
        """
        Sets the accessPackageAssignments property value. The assignment of an access package to a subject for a period of time.
        Args:
            value: Value to set for the accessPackageAssignments property.
        """
        self._access_package_assignments = value
    
    @property
    def access_package_catalogs(self,) -> Optional[List[access_package_catalog.AccessPackageCatalog]]:
        """
        Gets the accessPackageCatalogs property value. A container of access packages.
        Returns: Optional[List[access_package_catalog.AccessPackageCatalog]]
        """
        return self._access_package_catalogs
    
    @access_package_catalogs.setter
    def access_package_catalogs(self,value: Optional[List[access_package_catalog.AccessPackageCatalog]] = None) -> None:
        """
        Sets the accessPackageCatalogs property value. A container of access packages.
        Args:
            value: Value to set for the accessPackageCatalogs property.
        """
        self._access_package_catalogs = value
    
    @property
    def access_package_resource_environments(self,) -> Optional[List[access_package_resource_environment.AccessPackageResourceEnvironment]]:
        """
        Gets the accessPackageResourceEnvironments property value. A reference to the geolocation environment in which a resource is located.
        Returns: Optional[List[access_package_resource_environment.AccessPackageResourceEnvironment]]
        """
        return self._access_package_resource_environments
    
    @access_package_resource_environments.setter
    def access_package_resource_environments(self,value: Optional[List[access_package_resource_environment.AccessPackageResourceEnvironment]] = None) -> None:
        """
        Sets the accessPackageResourceEnvironments property value. A reference to the geolocation environment in which a resource is located.
        Args:
            value: Value to set for the accessPackageResourceEnvironments property.
        """
        self._access_package_resource_environments = value
    
    @property
    def access_package_resource_requests(self,) -> Optional[List[access_package_resource_request.AccessPackageResourceRequest]]:
        """
        Gets the accessPackageResourceRequests property value. Represents a request to add or remove a resource to or from a catalog respectively.
        Returns: Optional[List[access_package_resource_request.AccessPackageResourceRequest]]
        """
        return self._access_package_resource_requests
    
    @access_package_resource_requests.setter
    def access_package_resource_requests(self,value: Optional[List[access_package_resource_request.AccessPackageResourceRequest]] = None) -> None:
        """
        Sets the accessPackageResourceRequests property value. Represents a request to add or remove a resource to or from a catalog respectively.
        Args:
            value: Value to set for the accessPackageResourceRequests property.
        """
        self._access_package_resource_requests = value
    
    @property
    def access_package_resource_role_scopes(self,) -> Optional[List[access_package_resource_role_scope.AccessPackageResourceRoleScope]]:
        """
        Gets the accessPackageResourceRoleScopes property value. A reference to both a scope within a resource, and a role in that resource for that scope.
        Returns: Optional[List[access_package_resource_role_scope.AccessPackageResourceRoleScope]]
        """
        return self._access_package_resource_role_scopes
    
    @access_package_resource_role_scopes.setter
    def access_package_resource_role_scopes(self,value: Optional[List[access_package_resource_role_scope.AccessPackageResourceRoleScope]] = None) -> None:
        """
        Sets the accessPackageResourceRoleScopes property value. A reference to both a scope within a resource, and a role in that resource for that scope.
        Args:
            value: Value to set for the accessPackageResourceRoleScopes property.
        """
        self._access_package_resource_role_scopes = value
    
    @property
    def access_package_resources(self,) -> Optional[List[access_package_resource.AccessPackageResource]]:
        """
        Gets the accessPackageResources property value. A reference to a resource associated with an access package catalog.
        Returns: Optional[List[access_package_resource.AccessPackageResource]]
        """
        return self._access_package_resources
    
    @access_package_resources.setter
    def access_package_resources(self,value: Optional[List[access_package_resource.AccessPackageResource]] = None) -> None:
        """
        Sets the accessPackageResources property value. A reference to a resource associated with an access package catalog.
        Args:
            value: Value to set for the accessPackageResources property.
        """
        self._access_package_resources = value
    
    @property
    def access_packages(self,) -> Optional[List[access_package.AccessPackage]]:
        """
        Gets the accessPackages property value. Represents access package objects.
        Returns: Optional[List[access_package.AccessPackage]]
        """
        return self._access_packages
    
    @access_packages.setter
    def access_packages(self,value: Optional[List[access_package.AccessPackage]] = None) -> None:
        """
        Sets the accessPackages property value. Represents access package objects.
        Args:
            value: Value to set for the accessPackages property.
        """
        self._access_packages = value
    
    @property
    def connected_organizations(self,) -> Optional[List[connected_organization.ConnectedOrganization]]:
        """
        Gets the connectedOrganizations property value. Represents references to a directory or domain of another organization whose users can request access.
        Returns: Optional[List[connected_organization.ConnectedOrganization]]
        """
        return self._connected_organizations
    
    @connected_organizations.setter
    def connected_organizations(self,value: Optional[List[connected_organization.ConnectedOrganization]] = None) -> None:
        """
        Sets the connectedOrganizations property value. Represents references to a directory or domain of another organization whose users can request access.
        Args:
            value: Value to set for the connectedOrganizations property.
        """
        self._connected_organizations = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EntitlementManagement and sets the default values.
        """
        super().__init__()
        # The accessPackageAssignmentApprovals property
        self._access_package_assignment_approvals: Optional[List[approval.Approval]] = None
        # Represents the policy that governs which subjects can request or be assigned an access package via an access package assignment.
        self._access_package_assignment_policies: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]] = None
        # Represents access package assignment requests created by or on behalf of a user.
        self._access_package_assignment_requests: Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]] = None
        # Represents the resource-specific role which a subject has been assigned through an access package assignment.
        self._access_package_assignment_resource_roles: Optional[List[access_package_assignment_resource_role.AccessPackageAssignmentResourceRole]] = None
        # The assignment of an access package to a subject for a period of time.
        self._access_package_assignments: Optional[List[access_package_assignment.AccessPackageAssignment]] = None
        # A container of access packages.
        self._access_package_catalogs: Optional[List[access_package_catalog.AccessPackageCatalog]] = None
        # A reference to the geolocation environment in which a resource is located.
        self._access_package_resource_environments: Optional[List[access_package_resource_environment.AccessPackageResourceEnvironment]] = None
        # Represents a request to add or remove a resource to or from a catalog respectively.
        self._access_package_resource_requests: Optional[List[access_package_resource_request.AccessPackageResourceRequest]] = None
        # A reference to both a scope within a resource, and a role in that resource for that scope.
        self._access_package_resource_role_scopes: Optional[List[access_package_resource_role_scope.AccessPackageResourceRoleScope]] = None
        # A reference to a resource associated with an access package catalog.
        self._access_package_resources: Optional[List[access_package_resource.AccessPackageResource]] = None
        # Represents access package objects.
        self._access_packages: Optional[List[access_package.AccessPackage]] = None
        # Represents references to a directory or domain of another organization whose users can request access.
        self._connected_organizations: Optional[List[connected_organization.ConnectedOrganization]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents the settings that control the behavior of Azure AD entitlement management.
        self._settings: Optional[entitlement_management_settings.EntitlementManagementSettings] = None
        # The subjects property
        self._subjects: Optional[List[access_package_subject.AccessPackageSubject]] = None
    
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
        fields = {
            "access_package_assignment_approvals": lambda n : setattr(self, 'access_package_assignment_approvals', n.get_collection_of_object_values(approval.Approval)),
            "access_package_assignment_policies": lambda n : setattr(self, 'access_package_assignment_policies', n.get_collection_of_object_values(access_package_assignment_policy.AccessPackageAssignmentPolicy)),
            "access_package_assignment_requests": lambda n : setattr(self, 'access_package_assignment_requests', n.get_collection_of_object_values(access_package_assignment_request.AccessPackageAssignmentRequest)),
            "access_package_assignment_resource_roles": lambda n : setattr(self, 'access_package_assignment_resource_roles', n.get_collection_of_object_values(access_package_assignment_resource_role.AccessPackageAssignmentResourceRole)),
            "access_package_assignments": lambda n : setattr(self, 'access_package_assignments', n.get_collection_of_object_values(access_package_assignment.AccessPackageAssignment)),
            "access_package_catalogs": lambda n : setattr(self, 'access_package_catalogs', n.get_collection_of_object_values(access_package_catalog.AccessPackageCatalog)),
            "access_package_resource_environments": lambda n : setattr(self, 'access_package_resource_environments', n.get_collection_of_object_values(access_package_resource_environment.AccessPackageResourceEnvironment)),
            "access_package_resource_requests": lambda n : setattr(self, 'access_package_resource_requests', n.get_collection_of_object_values(access_package_resource_request.AccessPackageResourceRequest)),
            "access_package_resource_role_scopes": lambda n : setattr(self, 'access_package_resource_role_scopes', n.get_collection_of_object_values(access_package_resource_role_scope.AccessPackageResourceRoleScope)),
            "access_package_resources": lambda n : setattr(self, 'access_package_resources', n.get_collection_of_object_values(access_package_resource.AccessPackageResource)),
            "access_packages": lambda n : setattr(self, 'access_packages', n.get_collection_of_object_values(access_package.AccessPackage)),
            "connected_organizations": lambda n : setattr(self, 'connected_organizations', n.get_collection_of_object_values(connected_organization.ConnectedOrganization)),
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
        writer.write_collection_of_object_values("connectedOrganizations", self.connected_organizations)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("subjects", self.subjects)
    
    @property
    def settings(self,) -> Optional[entitlement_management_settings.EntitlementManagementSettings]:
        """
        Gets the settings property value. Represents the settings that control the behavior of Azure AD entitlement management.
        Returns: Optional[entitlement_management_settings.EntitlementManagementSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[entitlement_management_settings.EntitlementManagementSettings] = None) -> None:
        """
        Sets the settings property value. Represents the settings that control the behavior of Azure AD entitlement management.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def subjects(self,) -> Optional[List[access_package_subject.AccessPackageSubject]]:
        """
        Gets the subjects property value. The subjects property
        Returns: Optional[List[access_package_subject.AccessPackageSubject]]
        """
        return self._subjects
    
    @subjects.setter
    def subjects(self,value: Optional[List[access_package_subject.AccessPackageSubject]] = None) -> None:
        """
        Sets the subjects property value. The subjects property
        Args:
            value: Value to set for the subjects property.
        """
        self._subjects = value
    

