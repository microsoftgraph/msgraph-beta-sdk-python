from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
long_running_operation_status = lazy_import('msgraph.generated.models.security.long_running_operation_status')
submission_admin_review = lazy_import('msgraph.generated.models.security.submission_admin_review')
submission_category = lazy_import('msgraph.generated.models.security.submission_category')
submission_client_source = lazy_import('msgraph.generated.models.security.submission_client_source')
submission_content_type = lazy_import('msgraph.generated.models.security.submission_content_type')
submission_result = lazy_import('msgraph.generated.models.security.submission_result')
submission_source = lazy_import('msgraph.generated.models.security.submission_source')
submission_user_identity = lazy_import('msgraph.generated.models.security.submission_user_identity')

class ThreatSubmission(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def admin_review(self,) -> Optional[submission_admin_review.SubmissionAdminReview]:
        """
        Gets the adminReview property value. Specifies the admin review property which constitutes of who reviewed the user submission, when and what was it identified as.
        Returns: Optional[submission_admin_review.SubmissionAdminReview]
        """
        return self._admin_review
    
    @admin_review.setter
    def admin_review(self,value: Optional[submission_admin_review.SubmissionAdminReview] = None) -> None:
        """
        Sets the adminReview property value. Specifies the admin review property which constitutes of who reviewed the user submission, when and what was it identified as.
        Args:
            value: Value to set for the adminReview property.
        """
        self._admin_review = value
    
    @property
    def category(self,) -> Optional[submission_category.SubmissionCategory]:
        """
        Gets the category property value. The category property
        Returns: Optional[submission_category.SubmissionCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[submission_category.SubmissionCategory] = None) -> None:
        """
        Sets the category property value. The category property
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    @property
    def client_source(self,) -> Optional[submission_client_source.SubmissionClientSource]:
        """
        Gets the clientSource property value. Specifies the source of the submission. The possible values are: microsoft,  other and unkownFutureValue.
        Returns: Optional[submission_client_source.SubmissionClientSource]
        """
        return self._client_source
    
    @client_source.setter
    def client_source(self,value: Optional[submission_client_source.SubmissionClientSource] = None) -> None:
        """
        Sets the clientSource property value. Specifies the source of the submission. The possible values are: microsoft,  other and unkownFutureValue.
        Args:
            value: Value to set for the clientSource property.
        """
        self._client_source = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new threatSubmission and sets the default values.
        """
        super().__init__()
        # Specifies the admin review property which constitutes of who reviewed the user submission, when and what was it identified as.
        self._admin_review: Optional[submission_admin_review.SubmissionAdminReview] = None
        # The category property
        self._category: Optional[submission_category.SubmissionCategory] = None
        # Specifies the source of the submission. The possible values are: microsoft,  other and unkownFutureValue.
        self._client_source: Optional[submission_client_source.SubmissionClientSource] = None
        # Specifies the type of content being submitted. The possible values are: email, url, file, app and unkownFutureValue.
        self._content_type: Optional[submission_content_type.SubmissionContentType] = None
        # Specifies who submitted the email as a threat. Supports $filter = createdBy/email eq 'value'.
        self._created_by: Optional[submission_user_identity.SubmissionUserIdentity] = None
        # Specifies when the threat submission was created. Supports $filter = createdDateTime ge 2022-01-01T00:00:00Z and createdDateTime lt 2022-01-02T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Specifies the result of the analysis performed by Microsoft.
        self._result: Optional[submission_result.SubmissionResult] = None
        # Specifies the role of the submitter. Supports $filter = source eq 'value'. The possible values are: administrator,  user and unkownFutureValue.
        self._source: Optional[submission_source.SubmissionSource] = None
        # Indicates whether the threat submission has been analyzed by Microsoft. Supports $filter = status eq 'value'. The possible values are: notStarted, running, succeeded, failed, skipped and unkownFutureValue.
        self._status: Optional[long_running_operation_status.LongRunningOperationStatus] = None
        # Indicates the tenant id of the submitter. Not required when created using a POST operation. It is extracted from the token of the post API call.
        self._tenant_id: Optional[str] = None
    
    @property
    def content_type(self,) -> Optional[submission_content_type.SubmissionContentType]:
        """
        Gets the contentType property value. Specifies the type of content being submitted. The possible values are: email, url, file, app and unkownFutureValue.
        Returns: Optional[submission_content_type.SubmissionContentType]
        """
        return self._content_type
    
    @content_type.setter
    def content_type(self,value: Optional[submission_content_type.SubmissionContentType] = None) -> None:
        """
        Sets the contentType property value. Specifies the type of content being submitted. The possible values are: email, url, file, app and unkownFutureValue.
        Args:
            value: Value to set for the contentType property.
        """
        self._content_type = value
    
    @property
    def created_by(self,) -> Optional[submission_user_identity.SubmissionUserIdentity]:
        """
        Gets the createdBy property value. Specifies who submitted the email as a threat. Supports $filter = createdBy/email eq 'value'.
        Returns: Optional[submission_user_identity.SubmissionUserIdentity]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[submission_user_identity.SubmissionUserIdentity] = None) -> None:
        """
        Sets the createdBy property value. Specifies who submitted the email as a threat. Supports $filter = createdBy/email eq 'value'.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Specifies when the threat submission was created. Supports $filter = createdDateTime ge 2022-01-01T00:00:00Z and createdDateTime lt 2022-01-02T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Specifies when the threat submission was created. Supports $filter = createdDateTime ge 2022-01-01T00:00:00Z and createdDateTime lt 2022-01-02T00:00:00Z.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ThreatSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ThreatSubmission
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ThreatSubmission()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "admin_review": lambda n : setattr(self, 'admin_review', n.get_object_value(submission_admin_review.SubmissionAdminReview)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(submission_category.SubmissionCategory)),
            "client_source": lambda n : setattr(self, 'client_source', n.get_enum_value(submission_client_source.SubmissionClientSource)),
            "content_type": lambda n : setattr(self, 'content_type', n.get_enum_value(submission_content_type.SubmissionContentType)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(submission_user_identity.SubmissionUserIdentity)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "result": lambda n : setattr(self, 'result', n.get_object_value(submission_result.SubmissionResult)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(submission_source.SubmissionSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(long_running_operation_status.LongRunningOperationStatus)),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def result(self,) -> Optional[submission_result.SubmissionResult]:
        """
        Gets the result property value. Specifies the result of the analysis performed by Microsoft.
        Returns: Optional[submission_result.SubmissionResult]
        """
        return self._result
    
    @result.setter
    def result(self,value: Optional[submission_result.SubmissionResult] = None) -> None:
        """
        Sets the result property value. Specifies the result of the analysis performed by Microsoft.
        Args:
            value: Value to set for the result property.
        """
        self._result = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("adminReview", self.admin_review)
        writer.write_enum_value("category", self.category)
        writer.write_enum_value("clientSource", self.client_source)
        writer.write_enum_value("contentType", self.content_type)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("result", self.result)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def source(self,) -> Optional[submission_source.SubmissionSource]:
        """
        Gets the source property value. Specifies the role of the submitter. Supports $filter = source eq 'value'. The possible values are: administrator,  user and unkownFutureValue.
        Returns: Optional[submission_source.SubmissionSource]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[submission_source.SubmissionSource] = None) -> None:
        """
        Sets the source property value. Specifies the role of the submitter. Supports $filter = source eq 'value'. The possible values are: administrator,  user and unkownFutureValue.
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    
    @property
    def status(self,) -> Optional[long_running_operation_status.LongRunningOperationStatus]:
        """
        Gets the status property value. Indicates whether the threat submission has been analyzed by Microsoft. Supports $filter = status eq 'value'. The possible values are: notStarted, running, succeeded, failed, skipped and unkownFutureValue.
        Returns: Optional[long_running_operation_status.LongRunningOperationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[long_running_operation_status.LongRunningOperationStatus] = None) -> None:
        """
        Sets the status property value. Indicates whether the threat submission has been analyzed by Microsoft. Supports $filter = status eq 'value'. The possible values are: notStarted, running, succeeded, failed, skipped and unkownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. Indicates the tenant id of the submitter. Not required when created using a POST operation. It is extracted from the token of the post API call.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. Indicates the tenant id of the submitter. Not required when created using a POST operation. It is extracted from the token of the post API call.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

