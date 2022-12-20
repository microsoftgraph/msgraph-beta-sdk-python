from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package = lazy_import('msgraph.generated.models.access_package')
access_package_catalog = lazy_import('msgraph.generated.models.access_package_catalog')
access_package_question = lazy_import('msgraph.generated.models.access_package_question')
approval_settings = lazy_import('msgraph.generated.models.approval_settings')
assignment_review_settings = lazy_import('msgraph.generated.models.assignment_review_settings')
custom_extension_handler = lazy_import('msgraph.generated.models.custom_extension_handler')
entity = lazy_import('msgraph.generated.models.entity')
requestor_settings = lazy_import('msgraph.generated.models.requestor_settings')

class AccessPackageAssignmentPolicy(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def access_package(self,) -> Optional[access_package.AccessPackage]:
        """
        Gets the accessPackage property value. The access package with this policy. Read-only. Nullable. Supports $expand.
        Returns: Optional[access_package.AccessPackage]
        """
        return self._access_package
    
    @access_package.setter
    def access_package(self,value: Optional[access_package.AccessPackage] = None) -> None:
        """
        Sets the accessPackage property value. The access package with this policy. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the accessPackage property.
        """
        self._access_package = value
    
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
    def access_package_id(self,) -> Optional[str]:
        """
        Gets the accessPackageId property value. Identifier of the access package.
        Returns: Optional[str]
        """
        return self._access_package_id
    
    @access_package_id.setter
    def access_package_id(self,value: Optional[str] = None) -> None:
        """
        Sets the accessPackageId property value. Identifier of the access package.
        Args:
            value: Value to set for the accessPackageId property.
        """
        self._access_package_id = value
    
    @property
    def access_review_settings(self,) -> Optional[assignment_review_settings.AssignmentReviewSettings]:
        """
        Gets the accessReviewSettings property value. Who must review, and how often, the assignments to the access package from this policy. This property is null if reviews are not required.
        Returns: Optional[assignment_review_settings.AssignmentReviewSettings]
        """
        return self._access_review_settings
    
    @access_review_settings.setter
    def access_review_settings(self,value: Optional[assignment_review_settings.AssignmentReviewSettings] = None) -> None:
        """
        Sets the accessReviewSettings property value. Who must review, and how often, the assignments to the access package from this policy. This property is null if reviews are not required.
        Args:
            value: Value to set for the accessReviewSettings property.
        """
        self._access_review_settings = value
    
    @property
    def can_extend(self,) -> Optional[bool]:
        """
        Gets the canExtend property value. Indicates whether a user can extend the access package assignment duration after approval.
        Returns: Optional[bool]
        """
        return self._can_extend
    
    @can_extend.setter
    def can_extend(self,value: Optional[bool] = None) -> None:
        """
        Sets the canExtend property value. Indicates whether a user can extend the access package assignment duration after approval.
        Args:
            value: Value to set for the canExtend property.
        """
        self._can_extend = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAssignmentPolicy and sets the default values.
        """
        super().__init__()
        # The access package with this policy. Read-only. Nullable. Supports $expand.
        self._access_package: Optional[access_package.AccessPackage] = None
        # The accessPackageCatalog property
        self._access_package_catalog: Optional[access_package_catalog.AccessPackageCatalog] = None
        # Identifier of the access package.
        self._access_package_id: Optional[str] = None
        # Who must review, and how often, the assignments to the access package from this policy. This property is null if reviews are not required.
        self._access_review_settings: Optional[assignment_review_settings.AssignmentReviewSettings] = None
        # Indicates whether a user can extend the access package assignment duration after approval.
        self._can_extend: Optional[bool] = None
        # The createdBy property
        self._created_by: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._created_date_time: Optional[datetime] = None
        # The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.
        self._custom_extension_handlers: Optional[List[custom_extension_handler.CustomExtensionHandler]] = None
        # The description of the policy.
        self._description: Optional[str] = None
        # The display name of the policy. Supports $filter (eq).
        self._display_name: Optional[str] = None
        # The number of days in which assignments from this policy last until they are expired.
        self._duration_in_days: Optional[int] = None
        # The expiration date for assignments created in this policy. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._expiration_date_time: Optional[datetime] = None
        # The modifiedBy property
        self._modified_by: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Questions that are posed to the  requestor.
        self._questions: Optional[List[access_package_question.AccessPackageQuestion]] = None
        # Who must approve requests for access package in this policy.
        self._request_approval_settings: Optional[approval_settings.ApprovalSettings] = None
        # Who can request this access package from this policy.
        self._requestor_settings: Optional[requestor_settings.RequestorSettings] = None
    
    @property
    def created_by(self,) -> Optional[str]:
        """
        Gets the createdBy property value. The createdBy property
        Returns: Optional[str]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[str] = None) -> None:
        """
        Sets the createdBy property value. The createdBy property
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignmentPolicy()
    
    @property
    def custom_extension_handlers(self,) -> Optional[List[custom_extension_handler.CustomExtensionHandler]]:
        """
        Gets the customExtensionHandlers property value. The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.
        Returns: Optional[List[custom_extension_handler.CustomExtensionHandler]]
        """
        return self._custom_extension_handlers
    
    @custom_extension_handlers.setter
    def custom_extension_handlers(self,value: Optional[List[custom_extension_handler.CustomExtensionHandler]] = None) -> None:
        """
        Sets the customExtensionHandlers property value. The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.
        Args:
            value: Value to set for the customExtensionHandlers property.
        """
        self._custom_extension_handlers = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the policy.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the policy.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the policy. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the policy. Supports $filter (eq).
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def duration_in_days(self,) -> Optional[int]:
        """
        Gets the durationInDays property value. The number of days in which assignments from this policy last until they are expired.
        Returns: Optional[int]
        """
        return self._duration_in_days
    
    @duration_in_days.setter
    def duration_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the durationInDays property value. The number of days in which assignments from this policy last until they are expired.
        Args:
            value: Value to set for the durationInDays property.
        """
        self._duration_in_days = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The expiration date for assignments created in this policy. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The expiration date for assignments created in this policy. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_package": lambda n : setattr(self, 'access_package', n.get_object_value(access_package.AccessPackage)),
            "access_package_catalog": lambda n : setattr(self, 'access_package_catalog', n.get_object_value(access_package_catalog.AccessPackageCatalog)),
            "access_package_id": lambda n : setattr(self, 'access_package_id', n.get_str_value()),
            "access_review_settings": lambda n : setattr(self, 'access_review_settings', n.get_object_value(assignment_review_settings.AssignmentReviewSettings)),
            "can_extend": lambda n : setattr(self, 'can_extend', n.get_bool_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "custom_extension_handlers": lambda n : setattr(self, 'custom_extension_handlers', n.get_collection_of_object_values(custom_extension_handler.CustomExtensionHandler)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "duration_in_days": lambda n : setattr(self, 'duration_in_days', n.get_int_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "modified_by": lambda n : setattr(self, 'modified_by', n.get_str_value()),
            "modified_date_time": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "questions": lambda n : setattr(self, 'questions', n.get_collection_of_object_values(access_package_question.AccessPackageQuestion)),
            "request_approval_settings": lambda n : setattr(self, 'request_approval_settings', n.get_object_value(approval_settings.ApprovalSettings)),
            "requestor_settings": lambda n : setattr(self, 'requestor_settings', n.get_object_value(requestor_settings.RequestorSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def modified_by(self,) -> Optional[str]:
        """
        Gets the modifiedBy property value. The modifiedBy property
        Returns: Optional[str]
        """
        return self._modified_by
    
    @modified_by.setter
    def modified_by(self,value: Optional[str] = None) -> None:
        """
        Sets the modifiedBy property value. The modifiedBy property
        Args:
            value: Value to set for the modifiedBy property.
        """
        self._modified_by = value
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the modifiedDateTime property.
        """
        self._modified_date_time = value
    
    @property
    def questions(self,) -> Optional[List[access_package_question.AccessPackageQuestion]]:
        """
        Gets the questions property value. Questions that are posed to the  requestor.
        Returns: Optional[List[access_package_question.AccessPackageQuestion]]
        """
        return self._questions
    
    @questions.setter
    def questions(self,value: Optional[List[access_package_question.AccessPackageQuestion]] = None) -> None:
        """
        Sets the questions property value. Questions that are posed to the  requestor.
        Args:
            value: Value to set for the questions property.
        """
        self._questions = value
    
    @property
    def request_approval_settings(self,) -> Optional[approval_settings.ApprovalSettings]:
        """
        Gets the requestApprovalSettings property value. Who must approve requests for access package in this policy.
        Returns: Optional[approval_settings.ApprovalSettings]
        """
        return self._request_approval_settings
    
    @request_approval_settings.setter
    def request_approval_settings(self,value: Optional[approval_settings.ApprovalSettings] = None) -> None:
        """
        Sets the requestApprovalSettings property value. Who must approve requests for access package in this policy.
        Args:
            value: Value to set for the requestApprovalSettings property.
        """
        self._request_approval_settings = value
    
    @property
    def requestor_settings(self,) -> Optional[requestor_settings.RequestorSettings]:
        """
        Gets the requestorSettings property value. Who can request this access package from this policy.
        Returns: Optional[requestor_settings.RequestorSettings]
        """
        return self._requestor_settings
    
    @requestor_settings.setter
    def requestor_settings(self,value: Optional[requestor_settings.RequestorSettings] = None) -> None:
        """
        Sets the requestorSettings property value. Who can request this access package from this policy.
        Args:
            value: Value to set for the requestorSettings property.
        """
        self._requestor_settings = value
    
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
        writer.write_object_value("accessPackageCatalog", self.access_package_catalog)
        writer.write_str_value("accessPackageId", self.access_package_id)
        writer.write_object_value("accessReviewSettings", self.access_review_settings)
        writer.write_bool_value("canExtend", self.can_extend)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("customExtensionHandlers", self.custom_extension_handlers)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("durationInDays", self.duration_in_days)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("modifiedBy", self.modified_by)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_collection_of_object_values("questions", self.questions)
        writer.write_object_value("requestApprovalSettings", self.request_approval_settings)
        writer.write_object_value("requestorSettings", self.requestor_settings)
    

