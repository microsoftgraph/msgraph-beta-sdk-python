from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_assignment = lazy_import('msgraph.generated.models.access_package_assignment')
access_package_resource_role = lazy_import('msgraph.generated.models.access_package_resource_role')
access_package_resource_scope = lazy_import('msgraph.generated.models.access_package_resource_scope')
access_package_subject = lazy_import('msgraph.generated.models.access_package_subject')
entity = lazy_import('msgraph.generated.models.entity')

class AccessPackageAssignmentResourceRole(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def access_package_assignments(self,) -> Optional[List[access_package_assignment.AccessPackageAssignment]]:
        """
        Gets the accessPackageAssignments property value. The access package assignments resulting in this role assignment. Read-only. Nullable.
        Returns: Optional[List[access_package_assignment.AccessPackageAssignment]]
        """
        return self._access_package_assignments
    
    @access_package_assignments.setter
    def access_package_assignments(self,value: Optional[List[access_package_assignment.AccessPackageAssignment]] = None) -> None:
        """
        Sets the accessPackageAssignments property value. The access package assignments resulting in this role assignment. Read-only. Nullable.
        Args:
            value: Value to set for the accessPackageAssignments property.
        """
        self._access_package_assignments = value
    
    @property
    def access_package_resource_role(self,) -> Optional[access_package_resource_role.AccessPackageResourceRole]:
        """
        Gets the accessPackageResourceRole property value. The accessPackageResourceRole property
        Returns: Optional[access_package_resource_role.AccessPackageResourceRole]
        """
        return self._access_package_resource_role
    
    @access_package_resource_role.setter
    def access_package_resource_role(self,value: Optional[access_package_resource_role.AccessPackageResourceRole] = None) -> None:
        """
        Sets the accessPackageResourceRole property value. The accessPackageResourceRole property
        Args:
            value: Value to set for the accessPackageResourceRole property.
        """
        self._access_package_resource_role = value
    
    @property
    def access_package_resource_scope(self,) -> Optional[access_package_resource_scope.AccessPackageResourceScope]:
        """
        Gets the accessPackageResourceScope property value. The accessPackageResourceScope property
        Returns: Optional[access_package_resource_scope.AccessPackageResourceScope]
        """
        return self._access_package_resource_scope
    
    @access_package_resource_scope.setter
    def access_package_resource_scope(self,value: Optional[access_package_resource_scope.AccessPackageResourceScope] = None) -> None:
        """
        Sets the accessPackageResourceScope property value. The accessPackageResourceScope property
        Args:
            value: Value to set for the accessPackageResourceScope property.
        """
        self._access_package_resource_scope = value
    
    @property
    def access_package_subject(self,) -> Optional[access_package_subject.AccessPackageSubject]:
        """
        Gets the accessPackageSubject property value. Read-only. Nullable. Supports $filter (eq) on objectId and $expand query parameters.
        Returns: Optional[access_package_subject.AccessPackageSubject]
        """
        return self._access_package_subject
    
    @access_package_subject.setter
    def access_package_subject(self,value: Optional[access_package_subject.AccessPackageSubject] = None) -> None:
        """
        Sets the accessPackageSubject property value. Read-only. Nullable. Supports $filter (eq) on objectId and $expand query parameters.
        Args:
            value: Value to set for the accessPackageSubject property.
        """
        self._access_package_subject = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAssignmentResourceRole and sets the default values.
        """
        super().__init__()
        # The access package assignments resulting in this role assignment. Read-only. Nullable.
        self._access_package_assignments: Optional[List[access_package_assignment.AccessPackageAssignment]] = None
        # The accessPackageResourceRole property
        self._access_package_resource_role: Optional[access_package_resource_role.AccessPackageResourceRole] = None
        # The accessPackageResourceScope property
        self._access_package_resource_scope: Optional[access_package_resource_scope.AccessPackageResourceScope] = None
        # Read-only. Nullable. Supports $filter (eq) on objectId and $expand query parameters.
        self._access_package_subject: Optional[access_package_subject.AccessPackageSubject] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A unique identifier relative to the origin system, corresponding to the originId property of the accessPackageResourceRole.
        self._origin_id: Optional[str] = None
        # The system where the role assignment is to be created or has been created for an access package assignment, such as SharePointOnline, AadGroup or AadApplication, corresponding to the originSystem property of the accessPackageResourceRole.
        self._origin_system: Optional[str] = None
        # The value is PendingFulfillment when the access package assignment has not yet been delivered to the origin system, and Fulfilled when the access package assignment has been delivered to the origin system.
        self._status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentResourceRole:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentResourceRole
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignmentResourceRole()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_package_assignments": lambda n : setattr(self, 'access_package_assignments', n.get_collection_of_object_values(access_package_assignment.AccessPackageAssignment)),
            "access_package_resource_role": lambda n : setattr(self, 'access_package_resource_role', n.get_object_value(access_package_resource_role.AccessPackageResourceRole)),
            "access_package_resource_scope": lambda n : setattr(self, 'access_package_resource_scope', n.get_object_value(access_package_resource_scope.AccessPackageResourceScope)),
            "access_package_subject": lambda n : setattr(self, 'access_package_subject', n.get_object_value(access_package_subject.AccessPackageSubject)),
            "origin_id": lambda n : setattr(self, 'origin_id', n.get_str_value()),
            "origin_system": lambda n : setattr(self, 'origin_system', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def origin_id(self,) -> Optional[str]:
        """
        Gets the originId property value. A unique identifier relative to the origin system, corresponding to the originId property of the accessPackageResourceRole.
        Returns: Optional[str]
        """
        return self._origin_id
    
    @origin_id.setter
    def origin_id(self,value: Optional[str] = None) -> None:
        """
        Sets the originId property value. A unique identifier relative to the origin system, corresponding to the originId property of the accessPackageResourceRole.
        Args:
            value: Value to set for the originId property.
        """
        self._origin_id = value
    
    @property
    def origin_system(self,) -> Optional[str]:
        """
        Gets the originSystem property value. The system where the role assignment is to be created or has been created for an access package assignment, such as SharePointOnline, AadGroup or AadApplication, corresponding to the originSystem property of the accessPackageResourceRole.
        Returns: Optional[str]
        """
        return self._origin_system
    
    @origin_system.setter
    def origin_system(self,value: Optional[str] = None) -> None:
        """
        Sets the originSystem property value. The system where the role assignment is to be created or has been created for an access package assignment, such as SharePointOnline, AadGroup or AadApplication, corresponding to the originSystem property of the accessPackageResourceRole.
        Args:
            value: Value to set for the originSystem property.
        """
        self._origin_system = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("accessPackageAssignments", self.access_package_assignments)
        writer.write_object_value("accessPackageResourceRole", self.access_package_resource_role)
        writer.write_object_value("accessPackageResourceScope", self.access_package_resource_scope)
        writer.write_object_value("accessPackageSubject", self.access_package_subject)
        writer.write_str_value("originId", self.origin_id)
        writer.write_str_value("originSystem", self.origin_system)
        writer.write_str_value("status", self.status)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The value is PendingFulfillment when the access package assignment has not yet been delivered to the origin system, and Fulfilled when the access package assignment has been delivered to the origin system.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The value is PendingFulfillment when the access package assignment has not yet been delivered to the origin system, and Fulfilled when the access package assignment has been delivered to the origin system.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

