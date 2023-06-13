from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import submission_detected_file, submission_result_category, submission_result_detail, user_mailbox_setting

@dataclass
class SubmissionResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The submission result category. The possible values are: notJunk, spam, phishing, malware, allowedByPolicy, blockedByPolicy, spoof, unknown, noResultAvailable and unkownFutureValue.
    category: Optional[submission_result_category.SubmissionResultCategory] = None
    # Specifies the additional details provided by Microsoft to substantiate their analysis result.
    detail: Optional[submission_result_detail.SubmissionResultDetail] = None
    # Specifies the files detected by Microsoft in the submitted emails.
    detected_files: Optional[List[submission_detected_file.SubmissionDetectedFile]] = None
    # Specifes the URLs detected by Microsoft in the submitted email.
    detected_urls: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the setting for user mailbox denoted by a comma-separated string.
    user_mailbox_setting: Optional[user_mailbox_setting.UserMailboxSetting] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubmissionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubmissionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SubmissionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import submission_detected_file, submission_result_category, submission_result_detail, user_mailbox_setting

        fields: Dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(submission_result_category.SubmissionResultCategory)),
            "detail": lambda n : setattr(self, 'detail', n.get_enum_value(submission_result_detail.SubmissionResultDetail)),
            "detectedFiles": lambda n : setattr(self, 'detected_files', n.get_collection_of_object_values(submission_detected_file.SubmissionDetectedFile)),
            "detectedUrls": lambda n : setattr(self, 'detected_urls', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userMailboxSetting": lambda n : setattr(self, 'user_mailbox_setting', n.get_enum_value(user_mailbox_setting.UserMailboxSetting)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("category", self.category)
        writer.write_enum_value("detail", self.detail)
        writer.write_collection_of_object_values("detectedFiles", self.detected_files)
        writer.write_collection_of_primitive_values("detectedUrls", self.detected_urls)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("userMailboxSetting", self.user_mailbox_setting)
        writer.write_additional_data_value(self.additional_data)
    

