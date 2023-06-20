from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import email_content_threat_submission, email_threat_submission, email_url_threat_submission, file_content_threat_submission, file_threat_submission, file_url_threat_submission, long_running_operation_status, submission_admin_review, submission_category, submission_client_source, submission_content_type, submission_result, submission_source, submission_user_identity, url_threat_submission
    from .. import entity

from .. import entity

@dataclass
class ThreatSubmission(entity.Entity):
    # Specifies the admin review property which constitutes of who reviewed the user submission, when and what was it identified as.
    admin_review: Optional[submission_admin_review.SubmissionAdminReview] = None
    # The category property
    category: Optional[submission_category.SubmissionCategory] = None
    # Specifies the source of the submission. The possible values are: microsoft,  other and unkownFutureValue.
    client_source: Optional[submission_client_source.SubmissionClientSource] = None
    # Specifies the type of content being submitted. The possible values are: email, url, file, app and unkownFutureValue.
    content_type: Optional[submission_content_type.SubmissionContentType] = None
    # Specifies who submitted the email as a threat. Supports $filter = createdBy/email eq 'value'.
    created_by: Optional[submission_user_identity.SubmissionUserIdentity] = None
    # Specifies when the threat submission was created. Supports $filter = createdDateTime ge 2022-01-01T00:00:00Z and createdDateTime lt 2022-01-02T00:00:00Z.
    created_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the result of the analysis performed by Microsoft.
    result: Optional[submission_result.SubmissionResult] = None
    # Specifies the role of the submitter. Supports $filter = source eq 'value'. The possible values are: administrator,  user and unkownFutureValue.
    source: Optional[submission_source.SubmissionSource] = None
    # Indicates whether the threat submission has been analyzed by Microsoft. Supports $filter = status eq 'value'. The possible values are: notStarted, running, succeeded, failed, skipped and unkownFutureValue.
    status: Optional[long_running_operation_status.LongRunningOperationStatus] = None
    # Indicates the tenant id of the submitter. Not required when created using a POST operation. It is extracted from the token of the post API call.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ThreatSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ThreatSubmission
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.emailContentThreatSubmission".casefold():
            from . import email_content_threat_submission

            return email_content_threat_submission.EmailContentThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.emailThreatSubmission".casefold():
            from . import email_threat_submission

            return email_threat_submission.EmailThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.emailUrlThreatSubmission".casefold():
            from . import email_url_threat_submission

            return email_url_threat_submission.EmailUrlThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileContentThreatSubmission".casefold():
            from . import file_content_threat_submission

            return file_content_threat_submission.FileContentThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileThreatSubmission".casefold():
            from . import file_threat_submission

            return file_threat_submission.FileThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileUrlThreatSubmission".casefold():
            from . import file_url_threat_submission

            return file_url_threat_submission.FileUrlThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.urlThreatSubmission".casefold():
            from . import url_threat_submission

            return url_threat_submission.UrlThreatSubmission()
        return ThreatSubmission()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import email_content_threat_submission, email_threat_submission, email_url_threat_submission, file_content_threat_submission, file_threat_submission, file_url_threat_submission, long_running_operation_status, submission_admin_review, submission_category, submission_client_source, submission_content_type, submission_result, submission_source, submission_user_identity, url_threat_submission
        from .. import entity

        from . import email_content_threat_submission, email_threat_submission, email_url_threat_submission, file_content_threat_submission, file_threat_submission, file_url_threat_submission, long_running_operation_status, submission_admin_review, submission_category, submission_client_source, submission_content_type, submission_result, submission_source, submission_user_identity, url_threat_submission
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "adminReview": lambda n : setattr(self, 'admin_review', n.get_object_value(submission_admin_review.SubmissionAdminReview)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(submission_category.SubmissionCategory)),
            "clientSource": lambda n : setattr(self, 'client_source', n.get_enum_value(submission_client_source.SubmissionClientSource)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_enum_value(submission_content_type.SubmissionContentType)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(submission_user_identity.SubmissionUserIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "result": lambda n : setattr(self, 'result', n.get_object_value(submission_result.SubmissionResult)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(submission_source.SubmissionSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(long_running_operation_status.LongRunningOperationStatus)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
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
    

