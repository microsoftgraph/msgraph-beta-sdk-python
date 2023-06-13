from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package, access_package_answer, access_package_assignment, access_package_subject, custom_extension_callout_instance, custom_extension_handler_instance, entity, request_schedule, verified_credential_data

from . import entity

@dataclass
class AccessPackageAssignmentRequest(entity.Entity):
    # The access package associated with the accessPackageAssignmentRequest. An access package defines the collections of resource roles and the policies for how one or more users can get access to those resources. Read-only. Nullable. Supports $expand.
    access_package: Optional[access_package.AccessPackage] = None
    # For a requestType of UserAdd or AdminAdd, this is an access package assignment requested to be created.  For a requestType of UserRemove, AdminRemove or SystemRemove, this has the id property of an existing assignment to be removed.  Supports $expand.
    access_package_assignment: Optional[access_package_assignment.AccessPackageAssignment] = None
    # Answers provided by the requestor to accessPackageQuestions asked of them at the time of request.
    answers: Optional[List[access_package_answer.AccessPackageAnswer]] = None
    # The date of the end of processing, either successful or failure, of a request. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    completed_date: Optional[datetime] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime] = None
    # Information about all the custom extension calls that were made during the access package assignment request workflow.
    custom_extension_callout_instances: Optional[List[custom_extension_callout_instance.CustomExtensionCalloutInstance]] = None
    # A collection of custom workflow extension instances being run on an assignment request. Read-only.
    custom_extension_handler_instances: Optional[List[custom_extension_handler_instance.CustomExtensionHandlerInstance]] = None
    # The expirationDateTime property
    expiration_date_time: Optional[datetime] = None
    # True if the request is not to be processed for assignment.
    is_validation_only: Optional[bool] = None
    # The requestor's supplied justification.
    justification: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # One of PendingApproval, Canceled,  Denied, Delivering, Delivered, PartiallyDelivered, DeliveryFailed, Submitted or Scheduled. Read-only.
    request_state: Optional[str] = None
    # More information on the request processing status. Read-only.
    request_status: Optional[str] = None
    # One of UserAdd, UserExtend, UserUpdate, UserRemove, AdminAdd, AdminRemove or SystemRemove. A request from the user themselves would have requestType of UserAdd, UserUpdate or UserRemove. Read-only.
    request_type: Optional[str] = None
    # The subject who requested or, if a direct assignment, was assigned. Read-only. Nullable. Supports $expand.
    requestor: Optional[access_package_subject.AccessPackageSubject] = None
    # The range of dates that access is to be assigned to the requestor. Read-only.
    schedule: Optional[request_schedule.RequestSchedule] = None
    # The details of the verifiable credential that was presented by the requestor, such as the issuer and claims. Read-only.
    verified_credentials_data: Optional[List[verified_credential_data.VerifiedCredentialData]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignmentRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package, access_package_answer, access_package_assignment, access_package_subject, custom_extension_callout_instance, custom_extension_handler_instance, entity, request_schedule, verified_credential_data

        fields: Dict[str, Callable[[Any], None]] = {
            "accessPackage": lambda n : setattr(self, 'access_package', n.get_object_value(access_package.AccessPackage)),
            "accessPackageAssignment": lambda n : setattr(self, 'access_package_assignment', n.get_object_value(access_package_assignment.AccessPackageAssignment)),
            "answers": lambda n : setattr(self, 'answers', n.get_collection_of_object_values(access_package_answer.AccessPackageAnswer)),
            "completedDate": lambda n : setattr(self, 'completed_date', n.get_datetime_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customExtensionCalloutInstances": lambda n : setattr(self, 'custom_extension_callout_instances', n.get_collection_of_object_values(custom_extension_callout_instance.CustomExtensionCalloutInstance)),
            "customExtensionHandlerInstances": lambda n : setattr(self, 'custom_extension_handler_instances', n.get_collection_of_object_values(custom_extension_handler_instance.CustomExtensionHandlerInstance)),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "isValidationOnly": lambda n : setattr(self, 'is_validation_only', n.get_bool_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "requestor": lambda n : setattr(self, 'requestor', n.get_object_value(access_package_subject.AccessPackageSubject)),
            "requestState": lambda n : setattr(self, 'request_state', n.get_str_value()),
            "requestStatus": lambda n : setattr(self, 'request_status', n.get_str_value()),
            "requestType": lambda n : setattr(self, 'request_type', n.get_str_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(request_schedule.RequestSchedule)),
            "verifiedCredentialsData": lambda n : setattr(self, 'verified_credentials_data', n.get_collection_of_object_values(verified_credential_data.VerifiedCredentialData)),
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
        writer.write_object_value("accessPackage", self.access_package)
        writer.write_object_value("accessPackageAssignment", self.access_package_assignment)
        writer.write_collection_of_object_values("answers", self.answers)
        writer.write_datetime_value("completedDate", self.completed_date)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("customExtensionCalloutInstances", self.custom_extension_callout_instances)
        writer.write_collection_of_object_values("customExtensionHandlerInstances", self.custom_extension_handler_instances)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_bool_value("isValidationOnly", self.is_validation_only)
        writer.write_str_value("justification", self.justification)
        writer.write_object_value("requestor", self.requestor)
        writer.write_str_value("requestState", self.request_state)
        writer.write_str_value("requestStatus", self.request_status)
        writer.write_str_value("requestType", self.request_type)
        writer.write_object_value("schedule", self.schedule)
        writer.write_collection_of_object_values("verifiedCredentialsData", self.verified_credentials_data)
    

