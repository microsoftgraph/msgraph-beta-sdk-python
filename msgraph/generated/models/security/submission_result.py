from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

submission_detected_file = lazy_import('msgraph.generated.models.security.submission_detected_file')
submission_result_category = lazy_import('msgraph.generated.models.security.submission_result_category')
submission_result_detail = lazy_import('msgraph.generated.models.security.submission_result_detail')
user_mailbox_setting = lazy_import('msgraph.generated.models.security.user_mailbox_setting')

class SubmissionResult(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def category(self,) -> Optional[submission_result_category.SubmissionResultCategory]:
        """
        Gets the category property value. The submission result category. The possible values are: notJunk, spam, phishing, malware, allowedByPolicy, blockedByPolicy, spoof, unknown, noResultAvailable and unkownFutureValue.
        Returns: Optional[submission_result_category.SubmissionResultCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[submission_result_category.SubmissionResultCategory] = None) -> None:
        """
        Sets the category property value. The submission result category. The possible values are: notJunk, spam, phishing, malware, allowedByPolicy, blockedByPolicy, spoof, unknown, noResultAvailable and unkownFutureValue.
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new submissionResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The submission result category. The possible values are: notJunk, spam, phishing, malware, allowedByPolicy, blockedByPolicy, spoof, unknown, noResultAvailable and unkownFutureValue.
        self._category: Optional[submission_result_category.SubmissionResultCategory] = None
        # Specifies the additional details provided by Microsoft to substantiate their analysis result.
        self._detail: Optional[submission_result_detail.SubmissionResultDetail] = None
        # Specifies the files detected by Microsoft in the submitted emails.
        self._detected_files: Optional[List[submission_detected_file.SubmissionDetectedFile]] = None
        # Specifes the URLs detected by Microsoft in the submitted email.
        self._detected_urls: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies the setting for user mailbox denoted by a comma-separated string.
        self._user_mailbox_setting: Optional[user_mailbox_setting.UserMailboxSetting] = None
    
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
    
    @property
    def detail(self,) -> Optional[submission_result_detail.SubmissionResultDetail]:
        """
        Gets the detail property value. Specifies the additional details provided by Microsoft to substantiate their analysis result.
        Returns: Optional[submission_result_detail.SubmissionResultDetail]
        """
        return self._detail
    
    @detail.setter
    def detail(self,value: Optional[submission_result_detail.SubmissionResultDetail] = None) -> None:
        """
        Sets the detail property value. Specifies the additional details provided by Microsoft to substantiate their analysis result.
        Args:
            value: Value to set for the detail property.
        """
        self._detail = value
    
    @property
    def detected_files(self,) -> Optional[List[submission_detected_file.SubmissionDetectedFile]]:
        """
        Gets the detectedFiles property value. Specifies the files detected by Microsoft in the submitted emails.
        Returns: Optional[List[submission_detected_file.SubmissionDetectedFile]]
        """
        return self._detected_files
    
    @detected_files.setter
    def detected_files(self,value: Optional[List[submission_detected_file.SubmissionDetectedFile]] = None) -> None:
        """
        Sets the detectedFiles property value. Specifies the files detected by Microsoft in the submitted emails.
        Args:
            value: Value to set for the detectedFiles property.
        """
        self._detected_files = value
    
    @property
    def detected_urls(self,) -> Optional[List[str]]:
        """
        Gets the detectedUrls property value. Specifes the URLs detected by Microsoft in the submitted email.
        Returns: Optional[List[str]]
        """
        return self._detected_urls
    
    @detected_urls.setter
    def detected_urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the detectedUrls property value. Specifes the URLs detected by Microsoft in the submitted email.
        Args:
            value: Value to set for the detectedUrls property.
        """
        self._detected_urls = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(submission_result_category.SubmissionResultCategory)),
            "detail": lambda n : setattr(self, 'detail', n.get_enum_value(submission_result_detail.SubmissionResultDetail)),
            "detected_files": lambda n : setattr(self, 'detected_files', n.get_collection_of_object_values(submission_detected_file.SubmissionDetectedFile)),
            "detected_urls": lambda n : setattr(self, 'detected_urls', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user_mailbox_setting": lambda n : setattr(self, 'user_mailbox_setting', n.get_enum_value(user_mailbox_setting.UserMailboxSetting)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
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
    
    @property
    def user_mailbox_setting(self,) -> Optional[user_mailbox_setting.UserMailboxSetting]:
        """
        Gets the userMailboxSetting property value. Specifies the setting for user mailbox denoted by a comma-separated string.
        Returns: Optional[user_mailbox_setting.UserMailboxSetting]
        """
        return self._user_mailbox_setting
    
    @user_mailbox_setting.setter
    def user_mailbox_setting(self,value: Optional[user_mailbox_setting.UserMailboxSetting] = None) -> None:
        """
        Sets the userMailboxSetting property value. Specifies the setting for user mailbox denoted by a comma-separated string.
        Args:
            value: Value to set for the userMailboxSetting property.
        """
        self._user_mailbox_setting = value
    

