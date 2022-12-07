from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package = lazy_import('msgraph.generated.models.access_package')
access_package_assignment_policy = lazy_import('msgraph.generated.models.access_package_assignment_policy')
access_package_assignment_request = lazy_import('msgraph.generated.models.access_package_assignment_request')
access_package_assignment_resource_role = lazy_import('msgraph.generated.models.access_package_assignment_resource_role')
access_package_subject = lazy_import('msgraph.generated.models.access_package_subject')
entity = lazy_import('msgraph.generated.models.entity')
request_schedule = lazy_import('msgraph.generated.models.request_schedule')

class AccessPackageAssignment(entity.Entity):
    @property
    def access_package(self,) -> Optional[access_package.AccessPackage]:
        """
        Gets the accessPackage property value. Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.
        Returns: Optional[access_package.AccessPackage]
        """
        return self._access_package
    
    @access_package.setter
    def access_package(self,value: Optional[access_package.AccessPackage] = None) -> None:
        """
        Sets the accessPackage property value. Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.
        Args:
            value: Value to set for the accessPackage property.
        """
        self._access_package = value
    
    @property
    def access_package_assignment_policy(self,) -> Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy]:
        """
        Gets the accessPackageAssignmentPolicy property value. Read-only. Nullable. Supports $filter (eq) on the id property
        Returns: Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy]
        """
        return self._access_package_assignment_policy
    
    @access_package_assignment_policy.setter
    def access_package_assignment_policy(self,value: Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy] = None) -> None:
        """
        Sets the accessPackageAssignmentPolicy property value. Read-only. Nullable. Supports $filter (eq) on the id property
        Args:
            value: Value to set for the accessPackageAssignmentPolicy property.
        """
        self._access_package_assignment_policy = value
    
    @property
    def access_package_assignment_requests(self,) -> Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]]:
        """
        Gets the accessPackageAssignmentRequests property value. The accessPackageAssignmentRequests property
        Returns: Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]]
        """
        return self._access_package_assignment_requests
    
    @access_package_assignment_requests.setter
    def access_package_assignment_requests(self,value: Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]] = None) -> None:
        """
        Sets the accessPackageAssignmentRequests property value. The accessPackageAssignmentRequests property
        Args:
            value: Value to set for the accessPackageAssignmentRequests property.
        """
        self._access_package_assignment_requests = value
    
    @property
    def access_package_assignment_resource_roles(self,) -> Optional[List[access_package_assignment_resource_role.AccessPackageAssignmentResourceRole]]:
        """
        Gets the accessPackageAssignmentResourceRoles property value. The resource roles delivered to the target user for this assignment. Read-only. Nullable.
        Returns: Optional[List[access_package_assignment_resource_role.AccessPackageAssignmentResourceRole]]
        """
        return self._access_package_assignment_resource_roles
    
    @access_package_assignment_resource_roles.setter
    def access_package_assignment_resource_roles(self,value: Optional[List[access_package_assignment_resource_role.AccessPackageAssignmentResourceRole]] = None) -> None:
        """
        Sets the accessPackageAssignmentResourceRoles property value. The resource roles delivered to the target user for this assignment. Read-only. Nullable.
        Args:
            value: Value to set for the accessPackageAssignmentResourceRoles property.
        """
        self._access_package_assignment_resource_roles = value
    
    @property
    def access_package_id(self,) -> Optional[str]:
        """
        Gets the accessPackageId property value. The identifier of the access package. Read-only.
        Returns: Optional[str]
        """
        return self._access_package_id
    
    @access_package_id.setter
    def access_package_id(self,value: Optional[str] = None) -> None:
        """
        Sets the accessPackageId property value. The identifier of the access package. Read-only.
        Args:
            value: Value to set for the accessPackageId property.
        """
        self._access_package_id = value
    
    @property
    def assignment_policy_id(self,) -> Optional[str]:
        """
        Gets the assignmentPolicyId property value. The identifier of the access package assignment policy. Read-only.
        Returns: Optional[str]
        """
        return self._assignment_policy_id
    
    @assignment_policy_id.setter
    def assignment_policy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the assignmentPolicyId property value. The identifier of the access package assignment policy. Read-only.
        Args:
            value: Value to set for the assignmentPolicyId property.
        """
        self._assignment_policy_id = value
    
    @property
    def assignment_state(self,) -> Optional[str]:
        """
        Gets the assignmentState property value. The state of the access package assignment. Possible values are Delivering, Delivered, or Expired. Read-only. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._assignment_state
    
    @assignment_state.setter
    def assignment_state(self,value: Optional[str] = None) -> None:
        """
        Sets the assignmentState property value. The state of the access package assignment. Possible values are Delivering, Delivered, or Expired. Read-only. Supports $filter (eq).
        Args:
            value: Value to set for the assignmentState property.
        """
        self._assignment_state = value
    
    @property
    def assignment_status(self,) -> Optional[str]:
        """
        Gets the assignmentStatus property value. More information about the assignment lifecycle.  Possible values include Delivering, Delivered, NearExpiry1DayNotificationTriggered, or ExpiredNotificationTriggered.  Read-only.
        Returns: Optional[str]
        """
        return self._assignment_status
    
    @assignment_status.setter
    def assignment_status(self,value: Optional[str] = None) -> None:
        """
        Sets the assignmentStatus property value. More information about the assignment lifecycle.  Possible values include Delivering, Delivered, NearExpiry1DayNotificationTriggered, or ExpiredNotificationTriggered.  Read-only.
        Args:
            value: Value to set for the assignmentStatus property.
        """
        self._assignment_status = value
    
    @property
    def catalog_id(self,) -> Optional[str]:
        """
        Gets the catalogId property value. The identifier of the catalog containing the access package. Read-only.
        Returns: Optional[str]
        """
        return self._catalog_id
    
    @catalog_id.setter
    def catalog_id(self,value: Optional[str] = None) -> None:
        """
        Sets the catalogId property value. The identifier of the catalog containing the access package. Read-only.
        Args:
            value: Value to set for the catalogId property.
        """
        self._catalog_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAssignment and sets the default values.
        """
        super().__init__()
        # Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.
        self._access_package: Optional[access_package.AccessPackage] = None
        # Read-only. Nullable. Supports $filter (eq) on the id property
        self._access_package_assignment_policy: Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy] = None
        # The accessPackageAssignmentRequests property
        self._access_package_assignment_requests: Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]] = None
        # The resource roles delivered to the target user for this assignment. Read-only. Nullable.
        self._access_package_assignment_resource_roles: Optional[List[access_package_assignment_resource_role.AccessPackageAssignmentResourceRole]] = None
        # The identifier of the access package. Read-only.
        self._access_package_id: Optional[str] = None
        # The identifier of the access package assignment policy. Read-only.
        self._assignment_policy_id: Optional[str] = None
        # The state of the access package assignment. Possible values are Delivering, Delivered, or Expired. Read-only. Supports $filter (eq).
        self._assignment_state: Optional[str] = None
        # More information about the assignment lifecycle.  Possible values include Delivering, Delivered, NearExpiry1DayNotificationTriggered, or ExpiredNotificationTriggered.  Read-only.
        self._assignment_status: Optional[str] = None
        # The identifier of the catalog containing the access package. Read-only.
        self._catalog_id: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._expired_date_time: Optional[datetime] = None
        # Indicates whether the access package assignment is extended. Read-only.
        self._is_extended: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # When the access assignment is to be in place. Read-only.
        self._schedule: Optional[request_schedule.RequestSchedule] = None
        # The subject of the access package assignment. Read-only. Nullable. Supports $expand. Supports $filter (eq) on objectId.
        self._target: Optional[access_package_subject.AccessPackageSubject] = None
        # The ID of the subject with the assignment. Read-only.
        self._target_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignment()
    
    @property
    def expired_date_time(self,) -> Optional[datetime]:
        """
        Gets the expiredDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._expired_date_time
    
    @expired_date_time.setter
    def expired_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expiredDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the expiredDateTime property.
        """
        self._expired_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_package": lambda n : setattr(self, 'access_package', n.get_object_value(access_package.AccessPackage)),
            "access_package_assignment_policy": lambda n : setattr(self, 'access_package_assignment_policy', n.get_object_value(access_package_assignment_policy.AccessPackageAssignmentPolicy)),
            "access_package_assignment_requests": lambda n : setattr(self, 'access_package_assignment_requests', n.get_collection_of_object_values(access_package_assignment_request.AccessPackageAssignmentRequest)),
            "access_package_assignment_resource_roles": lambda n : setattr(self, 'access_package_assignment_resource_roles', n.get_collection_of_object_values(access_package_assignment_resource_role.AccessPackageAssignmentResourceRole)),
            "access_package_id": lambda n : setattr(self, 'access_package_id', n.get_str_value()),
            "assignment_policy_id": lambda n : setattr(self, 'assignment_policy_id', n.get_str_value()),
            "assignment_state": lambda n : setattr(self, 'assignment_state', n.get_str_value()),
            "assignment_status": lambda n : setattr(self, 'assignment_status', n.get_str_value()),
            "catalog_id": lambda n : setattr(self, 'catalog_id', n.get_str_value()),
            "expired_date_time": lambda n : setattr(self, 'expired_date_time', n.get_datetime_value()),
            "is_extended": lambda n : setattr(self, 'is_extended', n.get_bool_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(request_schedule.RequestSchedule)),
            "target": lambda n : setattr(self, 'target', n.get_object_value(access_package_subject.AccessPackageSubject)),
            "target_id": lambda n : setattr(self, 'target_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_extended(self,) -> Optional[bool]:
        """
        Gets the isExtended property value. Indicates whether the access package assignment is extended. Read-only.
        Returns: Optional[bool]
        """
        return self._is_extended
    
    @is_extended.setter
    def is_extended(self,value: Optional[bool] = None) -> None:
        """
        Sets the isExtended property value. Indicates whether the access package assignment is extended. Read-only.
        Args:
            value: Value to set for the isExtended property.
        """
        self._is_extended = value
    
    @property
    def schedule(self,) -> Optional[request_schedule.RequestSchedule]:
        """
        Gets the schedule property value. When the access assignment is to be in place. Read-only.
        Returns: Optional[request_schedule.RequestSchedule]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[request_schedule.RequestSchedule] = None) -> None:
        """
        Sets the schedule property value. When the access assignment is to be in place. Read-only.
        Args:
            value: Value to set for the schedule property.
        """
        self._schedule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("accessPackage", self.access_package)
        writer.write_object_value("accessPackageAssignmentPolicy", self.access_package_assignment_policy)
        writer.write_collection_of_object_values("accessPackageAssignmentRequests", self.access_package_assignment_requests)
        writer.write_collection_of_object_values("accessPackageAssignmentResourceRoles", self.access_package_assignment_resource_roles)
        writer.write_str_value("accessPackageId", self.access_package_id)
        writer.write_str_value("assignmentPolicyId", self.assignment_policy_id)
        writer.write_str_value("assignmentState", self.assignment_state)
        writer.write_str_value("assignmentStatus", self.assignment_status)
        writer.write_str_value("catalogId", self.catalog_id)
        writer.write_datetime_value("expiredDateTime", self.expired_date_time)
        writer.write_bool_value("isExtended", self.is_extended)
        writer.write_object_value("schedule", self.schedule)
        writer.write_object_value("target", self.target)
        writer.write_str_value("targetId", self.target_id)
    
    @property
    def target(self,) -> Optional[access_package_subject.AccessPackageSubject]:
        """
        Gets the target property value. The subject of the access package assignment. Read-only. Nullable. Supports $expand. Supports $filter (eq) on objectId.
        Returns: Optional[access_package_subject.AccessPackageSubject]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[access_package_subject.AccessPackageSubject] = None) -> None:
        """
        Sets the target property value. The subject of the access package assignment. Read-only. Nullable. Supports $expand. Supports $filter (eq) on objectId.
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    
    @property
    def target_id(self,) -> Optional[str]:
        """
        Gets the targetId property value. The ID of the subject with the assignment. Read-only.
        Returns: Optional[str]
        """
        return self._target_id
    
    @target_id.setter
    def target_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetId property value. The ID of the subject with the assignment. Read-only.
        Args:
            value: Value to set for the targetId property.
        """
        self._target_id = value
    

