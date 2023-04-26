from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package, access_package_answer, access_package_assignment, access_package_subject, custom_extension_callout_instance, custom_extension_handler_instance, entity, request_schedule, verified_credential_data

from . import entity

class AccessPackageAssignmentRequest(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAssignmentRequest and sets the default values.
        """
        super().__init__()
        # The access package associated with the accessPackageAssignmentRequest. An access package defines the collections of resource roles and the policies for how one or more users can get access to those resources. Read-only. Nullable. Supports $expand.
        self._access_package: Optional[access_package.AccessPackage] = None
        # For a requestType of UserAdd or AdminAdd, this is an access package assignment requested to be created.  For a requestType of UserRemove, AdminRemove or SystemRemove, this has the id property of an existing assignment to be removed.  Supports $expand.
        self._access_package_assignment: Optional[access_package_assignment.AccessPackageAssignment] = None
        # Answers provided by the requestor to accessPackageQuestions asked of them at the time of request.
        self._answers: Optional[List[access_package_answer.AccessPackageAnswer]] = None
        # The date of the end of processing, either successful or failure, of a request. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._completed_date: Optional[datetime] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._created_date_time: Optional[datetime] = None
        # Information about all the custom extension calls that were made during the access package assignment request workflow.
        self._custom_extension_callout_instances: Optional[List[custom_extension_callout_instance.CustomExtensionCalloutInstance]] = None
        # A collection of custom workflow extension instances being run on an assignment request. Read-only.
        self._custom_extension_handler_instances: Optional[List[custom_extension_handler_instance.CustomExtensionHandlerInstance]] = None
        # The expirationDateTime property
        self._expiration_date_time: Optional[datetime] = None
        # True if the request is not to be processed for assignment.
        self._is_validation_only: Optional[bool] = None
        # The requestor's supplied justification.
        self._justification: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # One of PendingApproval, Canceled,  Denied, Delivering, Delivered, PartiallyDelivered, DeliveryFailed, Submitted or Scheduled. Read-only.
        self._request_state: Optional[str] = None
        # More information on the request processing status. Read-only.
        self._request_status: Optional[str] = None
        # One of UserAdd, UserExtend, UserUpdate, UserRemove, AdminAdd, AdminRemove or SystemRemove. A request from the user themselves would have requestType of UserAdd, UserUpdate or UserRemove. Read-only.
        self._request_type: Optional[str] = None
        # The subject who requested or, if a direct assignment, was assigned. Read-only. Nullable. Supports $expand.
        self._requestor: Optional[access_package_subject.AccessPackageSubject] = None
        # The range of dates that access is to be assigned to the requestor. Read-only.
        self._schedule: Optional[request_schedule.RequestSchedule] = None
        # The details of the verifiable credential that was presented by the requestor, such as the issuer and claims. Read-only.
        self._verified_credentials_data: Optional[List[verified_credential_data.VerifiedCredentialData]] = None
    
    @property
    def access_package(self,) -> Optional[access_package.AccessPackage]:
        """
        Gets the accessPackage property value. The access package associated with the accessPackageAssignmentRequest. An access package defines the collections of resource roles and the policies for how one or more users can get access to those resources. Read-only. Nullable. Supports $expand.
        Returns: Optional[access_package.AccessPackage]
        """
        return self._access_package
    
    @access_package.setter
    def access_package(self,value: Optional[access_package.AccessPackage] = None) -> None:
        """
        Sets the accessPackage property value. The access package associated with the accessPackageAssignmentRequest. An access package defines the collections of resource roles and the policies for how one or more users can get access to those resources. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the access_package property.
        """
        self._access_package = value
    
    @property
    def access_package_assignment(self,) -> Optional[access_package_assignment.AccessPackageAssignment]:
        """
        Gets the accessPackageAssignment property value. For a requestType of UserAdd or AdminAdd, this is an access package assignment requested to be created.  For a requestType of UserRemove, AdminRemove or SystemRemove, this has the id property of an existing assignment to be removed.  Supports $expand.
        Returns: Optional[access_package_assignment.AccessPackageAssignment]
        """
        return self._access_package_assignment
    
    @access_package_assignment.setter
    def access_package_assignment(self,value: Optional[access_package_assignment.AccessPackageAssignment] = None) -> None:
        """
        Sets the accessPackageAssignment property value. For a requestType of UserAdd or AdminAdd, this is an access package assignment requested to be created.  For a requestType of UserRemove, AdminRemove or SystemRemove, this has the id property of an existing assignment to be removed.  Supports $expand.
        Args:
            value: Value to set for the access_package_assignment property.
        """
        self._access_package_assignment = value
    
    @property
    def answers(self,) -> Optional[List[access_package_answer.AccessPackageAnswer]]:
        """
        Gets the answers property value. Answers provided by the requestor to accessPackageQuestions asked of them at the time of request.
        Returns: Optional[List[access_package_answer.AccessPackageAnswer]]
        """
        return self._answers
    
    @answers.setter
    def answers(self,value: Optional[List[access_package_answer.AccessPackageAnswer]] = None) -> None:
        """
        Sets the answers property value. Answers provided by the requestor to accessPackageQuestions asked of them at the time of request.
        Args:
            value: Value to set for the answers property.
        """
        self._answers = value
    
    @property
    def completed_date(self,) -> Optional[datetime]:
        """
        Gets the completedDate property value. The date of the end of processing, either successful or failure, of a request. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._completed_date
    
    @completed_date.setter
    def completed_date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDate property value. The date of the end of processing, either successful or failure, of a request. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the completed_date property.
        """
        self._completed_date = value
    
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
    
    @property
    def custom_extension_callout_instances(self,) -> Optional[List[custom_extension_callout_instance.CustomExtensionCalloutInstance]]:
        """
        Gets the customExtensionCalloutInstances property value. Information about all the custom extension calls that were made during the access package assignment request workflow.
        Returns: Optional[List[custom_extension_callout_instance.CustomExtensionCalloutInstance]]
        """
        return self._custom_extension_callout_instances
    
    @custom_extension_callout_instances.setter
    def custom_extension_callout_instances(self,value: Optional[List[custom_extension_callout_instance.CustomExtensionCalloutInstance]] = None) -> None:
        """
        Sets the customExtensionCalloutInstances property value. Information about all the custom extension calls that were made during the access package assignment request workflow.
        Args:
            value: Value to set for the custom_extension_callout_instances property.
        """
        self._custom_extension_callout_instances = value
    
    @property
    def custom_extension_handler_instances(self,) -> Optional[List[custom_extension_handler_instance.CustomExtensionHandlerInstance]]:
        """
        Gets the customExtensionHandlerInstances property value. A collection of custom workflow extension instances being run on an assignment request. Read-only.
        Returns: Optional[List[custom_extension_handler_instance.CustomExtensionHandlerInstance]]
        """
        return self._custom_extension_handler_instances
    
    @custom_extension_handler_instances.setter
    def custom_extension_handler_instances(self,value: Optional[List[custom_extension_handler_instance.CustomExtensionHandlerInstance]] = None) -> None:
        """
        Sets the customExtensionHandlerInstances property value. A collection of custom workflow extension instances being run on an assignment request. Read-only.
        Args:
            value: Value to set for the custom_extension_handler_instances property.
        """
        self._custom_extension_handler_instances = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The expirationDateTime property
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The expirationDateTime property
        Args:
            value: Value to set for the expiration_date_time property.
        """
        self._expiration_date_time = value
    
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
    
    @property
    def is_validation_only(self,) -> Optional[bool]:
        """
        Gets the isValidationOnly property value. True if the request is not to be processed for assignment.
        Returns: Optional[bool]
        """
        return self._is_validation_only
    
    @is_validation_only.setter
    def is_validation_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the isValidationOnly property value. True if the request is not to be processed for assignment.
        Args:
            value: Value to set for the is_validation_only property.
        """
        self._is_validation_only = value
    
    @property
    def justification(self,) -> Optional[str]:
        """
        Gets the justification property value. The requestor's supplied justification.
        Returns: Optional[str]
        """
        return self._justification
    
    @justification.setter
    def justification(self,value: Optional[str] = None) -> None:
        """
        Sets the justification property value. The requestor's supplied justification.
        Args:
            value: Value to set for the justification property.
        """
        self._justification = value
    
    @property
    def request_state(self,) -> Optional[str]:
        """
        Gets the requestState property value. One of PendingApproval, Canceled,  Denied, Delivering, Delivered, PartiallyDelivered, DeliveryFailed, Submitted or Scheduled. Read-only.
        Returns: Optional[str]
        """
        return self._request_state
    
    @request_state.setter
    def request_state(self,value: Optional[str] = None) -> None:
        """
        Sets the requestState property value. One of PendingApproval, Canceled,  Denied, Delivering, Delivered, PartiallyDelivered, DeliveryFailed, Submitted or Scheduled. Read-only.
        Args:
            value: Value to set for the request_state property.
        """
        self._request_state = value
    
    @property
    def request_status(self,) -> Optional[str]:
        """
        Gets the requestStatus property value. More information on the request processing status. Read-only.
        Returns: Optional[str]
        """
        return self._request_status
    
    @request_status.setter
    def request_status(self,value: Optional[str] = None) -> None:
        """
        Sets the requestStatus property value. More information on the request processing status. Read-only.
        Args:
            value: Value to set for the request_status property.
        """
        self._request_status = value
    
    @property
    def request_type(self,) -> Optional[str]:
        """
        Gets the requestType property value. One of UserAdd, UserExtend, UserUpdate, UserRemove, AdminAdd, AdminRemove or SystemRemove. A request from the user themselves would have requestType of UserAdd, UserUpdate or UserRemove. Read-only.
        Returns: Optional[str]
        """
        return self._request_type
    
    @request_type.setter
    def request_type(self,value: Optional[str] = None) -> None:
        """
        Sets the requestType property value. One of UserAdd, UserExtend, UserUpdate, UserRemove, AdminAdd, AdminRemove or SystemRemove. A request from the user themselves would have requestType of UserAdd, UserUpdate or UserRemove. Read-only.
        Args:
            value: Value to set for the request_type property.
        """
        self._request_type = value
    
    @property
    def requestor(self,) -> Optional[access_package_subject.AccessPackageSubject]:
        """
        Gets the requestor property value. The subject who requested or, if a direct assignment, was assigned. Read-only. Nullable. Supports $expand.
        Returns: Optional[access_package_subject.AccessPackageSubject]
        """
        return self._requestor
    
    @requestor.setter
    def requestor(self,value: Optional[access_package_subject.AccessPackageSubject] = None) -> None:
        """
        Sets the requestor property value. The subject who requested or, if a direct assignment, was assigned. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the requestor property.
        """
        self._requestor = value
    
    @property
    def schedule(self,) -> Optional[request_schedule.RequestSchedule]:
        """
        Gets the schedule property value. The range of dates that access is to be assigned to the requestor. Read-only.
        Returns: Optional[request_schedule.RequestSchedule]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[request_schedule.RequestSchedule] = None) -> None:
        """
        Sets the schedule property value. The range of dates that access is to be assigned to the requestor. Read-only.
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
    
    @property
    def verified_credentials_data(self,) -> Optional[List[verified_credential_data.VerifiedCredentialData]]:
        """
        Gets the verifiedCredentialsData property value. The details of the verifiable credential that was presented by the requestor, such as the issuer and claims. Read-only.
        Returns: Optional[List[verified_credential_data.VerifiedCredentialData]]
        """
        return self._verified_credentials_data
    
    @verified_credentials_data.setter
    def verified_credentials_data(self,value: Optional[List[verified_credential_data.VerifiedCredentialData]] = None) -> None:
        """
        Sets the verifiedCredentialsData property value. The details of the verifiable credential that was presented by the requestor, such as the issuer and claims. Read-only.
        Args:
            value: Value to set for the verified_credentials_data property.
        """
        self._verified_credentials_data = value
    

