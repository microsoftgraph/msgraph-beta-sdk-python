from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

submission_result_category = lazy_import('msgraph.generated.models.security.submission_result_category')

class SubmissionAdminReview(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new submissionAdminReview and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies who reviewed the email. The identification is an email ID or other identity strings.
        self._review_by: Optional[str] = None
        # Specifies the date time when the review occurred.
        self._review_date_time: Optional[datetime] = None
        # Specifies what the review result was. The possible values are: notJunk, spam, phishing, malware, allowedByPolicy, blockedByPolicy, spoof, unknown, noResultAvailable, and unknownFutureValue.
        self._review_result: Optional[submission_result_category.SubmissionResultCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubmissionAdminReview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubmissionAdminReview
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SubmissionAdminReview()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "review_by": lambda n : setattr(self, 'review_by', n.get_str_value()),
            "review_date_time": lambda n : setattr(self, 'review_date_time', n.get_datetime_value()),
            "review_result": lambda n : setattr(self, 'review_result', n.get_enum_value(submission_result_category.SubmissionResultCategory)),
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
    
    @property
    def review_by(self,) -> Optional[str]:
        """
        Gets the reviewBy property value. Specifies who reviewed the email. The identification is an email ID or other identity strings.
        Returns: Optional[str]
        """
        return self._review_by
    
    @review_by.setter
    def review_by(self,value: Optional[str] = None) -> None:
        """
        Sets the reviewBy property value. Specifies who reviewed the email. The identification is an email ID or other identity strings.
        Args:
            value: Value to set for the reviewBy property.
        """
        self._review_by = value
    
    @property
    def review_date_time(self,) -> Optional[datetime]:
        """
        Gets the reviewDateTime property value. Specifies the date time when the review occurred.
        Returns: Optional[datetime]
        """
        return self._review_date_time
    
    @review_date_time.setter
    def review_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the reviewDateTime property value. Specifies the date time when the review occurred.
        Args:
            value: Value to set for the reviewDateTime property.
        """
        self._review_date_time = value
    
    @property
    def review_result(self,) -> Optional[submission_result_category.SubmissionResultCategory]:
        """
        Gets the reviewResult property value. Specifies what the review result was. The possible values are: notJunk, spam, phishing, malware, allowedByPolicy, blockedByPolicy, spoof, unknown, noResultAvailable, and unknownFutureValue.
        Returns: Optional[submission_result_category.SubmissionResultCategory]
        """
        return self._review_result
    
    @review_result.setter
    def review_result(self,value: Optional[submission_result_category.SubmissionResultCategory] = None) -> None:
        """
        Sets the reviewResult property value. Specifies what the review result was. The possible values are: notJunk, spam, phishing, malware, allowedByPolicy, blockedByPolicy, spoof, unknown, noResultAvailable, and unknownFutureValue.
        Args:
            value: Value to set for the reviewResult property.
        """
        self._review_result = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("reviewBy", self.review_by)
        writer.write_datetime_value("reviewDateTime", self.review_date_time)
        writer.write_enum_value("reviewResult", self.review_result)
        writer.write_additional_data_value(self.additional_data)
    

