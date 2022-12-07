from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_timeout_behavior = lazy_import('msgraph.generated.models.access_review_timeout_behavior')
user_set = lazy_import('msgraph.generated.models.user_set')

class AssignmentReviewSettings(AdditionalDataHolder, Parsable):
    @property
    def access_review_timeout_behavior(self,) -> Optional[access_review_timeout_behavior.AccessReviewTimeoutBehavior]:
        """
        Gets the accessReviewTimeoutBehavior property value. The default decision to apply if the request is not reviewed within the period specified in durationInDays. The possible values are: acceptAccessRecommendation, keepAccess, removeAccess, and unknownFutureValue.
        Returns: Optional[access_review_timeout_behavior.AccessReviewTimeoutBehavior]
        """
        return self._access_review_timeout_behavior
    
    @access_review_timeout_behavior.setter
    def access_review_timeout_behavior(self,value: Optional[access_review_timeout_behavior.AccessReviewTimeoutBehavior] = None) -> None:
        """
        Sets the accessReviewTimeoutBehavior property value. The default decision to apply if the request is not reviewed within the period specified in durationInDays. The possible values are: acceptAccessRecommendation, keepAccess, removeAccess, and unknownFutureValue.
        Args:
            value: Value to set for the accessReviewTimeoutBehavior property.
        """
        self._access_review_timeout_behavior = value
    
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
        Instantiates a new assignmentReviewSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The default decision to apply if the request is not reviewed within the period specified in durationInDays. The possible values are: acceptAccessRecommendation, keepAccess, removeAccess, and unknownFutureValue.
        self._access_review_timeout_behavior: Optional[access_review_timeout_behavior.AccessReviewTimeoutBehavior] = None
        # The number of days within which reviewers should provide input.
        self._duration_in_days: Optional[int] = None
        # Specifies whether to display recommendations to the reviewer. The default value is true
        self._is_access_recommendation_enabled: Optional[bool] = None
        # Specifies whether the reviewer must provide justification for the approval. The default value is true.
        self._is_approval_justification_required: Optional[bool] = None
        # If true, access reviews are required for assignments from this policy.
        self._is_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The interval for recurrence, such as monthly or quarterly.
        self._recurrence_type: Optional[str] = None
        # If the reviewerType is Reviewers, this collection specifies the users who will be reviewers, either by ID or as members of a group, using a collection of singleUser and groupMembers.
        self._reviewers: Optional[List[user_set.UserSet]] = None
        # Who should be asked to do the review, either Self or Reviewers.
        self._reviewer_type: Optional[str] = None
        # When the first review should start.
        self._start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignmentReviewSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentReviewSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignmentReviewSettings()
    
    @property
    def duration_in_days(self,) -> Optional[int]:
        """
        Gets the durationInDays property value. The number of days within which reviewers should provide input.
        Returns: Optional[int]
        """
        return self._duration_in_days
    
    @duration_in_days.setter
    def duration_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the durationInDays property value. The number of days within which reviewers should provide input.
        Args:
            value: Value to set for the durationInDays property.
        """
        self._duration_in_days = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_review_timeout_behavior": lambda n : setattr(self, 'access_review_timeout_behavior', n.get_enum_value(access_review_timeout_behavior.AccessReviewTimeoutBehavior)),
            "duration_in_days": lambda n : setattr(self, 'duration_in_days', n.get_int_value()),
            "is_access_recommendation_enabled": lambda n : setattr(self, 'is_access_recommendation_enabled', n.get_bool_value()),
            "is_approval_justification_required": lambda n : setattr(self, 'is_approval_justification_required', n.get_bool_value()),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrence_type": lambda n : setattr(self, 'recurrence_type', n.get_str_value()),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(user_set.UserSet)),
            "reviewer_type": lambda n : setattr(self, 'reviewer_type', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        return fields
    
    @property
    def is_access_recommendation_enabled(self,) -> Optional[bool]:
        """
        Gets the isAccessRecommendationEnabled property value. Specifies whether to display recommendations to the reviewer. The default value is true
        Returns: Optional[bool]
        """
        return self._is_access_recommendation_enabled
    
    @is_access_recommendation_enabled.setter
    def is_access_recommendation_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAccessRecommendationEnabled property value. Specifies whether to display recommendations to the reviewer. The default value is true
        Args:
            value: Value to set for the isAccessRecommendationEnabled property.
        """
        self._is_access_recommendation_enabled = value
    
    @property
    def is_approval_justification_required(self,) -> Optional[bool]:
        """
        Gets the isApprovalJustificationRequired property value. Specifies whether the reviewer must provide justification for the approval. The default value is true.
        Returns: Optional[bool]
        """
        return self._is_approval_justification_required
    
    @is_approval_justification_required.setter
    def is_approval_justification_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isApprovalJustificationRequired property value. Specifies whether the reviewer must provide justification for the approval. The default value is true.
        Args:
            value: Value to set for the isApprovalJustificationRequired property.
        """
        self._is_approval_justification_required = value
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. If true, access reviews are required for assignments from this policy.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. If true, access reviews are required for assignments from this policy.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
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
    def recurrence_type(self,) -> Optional[str]:
        """
        Gets the recurrenceType property value. The interval for recurrence, such as monthly or quarterly.
        Returns: Optional[str]
        """
        return self._recurrence_type
    
    @recurrence_type.setter
    def recurrence_type(self,value: Optional[str] = None) -> None:
        """
        Sets the recurrenceType property value. The interval for recurrence, such as monthly or quarterly.
        Args:
            value: Value to set for the recurrenceType property.
        """
        self._recurrence_type = value
    
    @property
    def reviewers(self,) -> Optional[List[user_set.UserSet]]:
        """
        Gets the reviewers property value. If the reviewerType is Reviewers, this collection specifies the users who will be reviewers, either by ID or as members of a group, using a collection of singleUser and groupMembers.
        Returns: Optional[List[user_set.UserSet]]
        """
        return self._reviewers
    
    @reviewers.setter
    def reviewers(self,value: Optional[List[user_set.UserSet]] = None) -> None:
        """
        Sets the reviewers property value. If the reviewerType is Reviewers, this collection specifies the users who will be reviewers, either by ID or as members of a group, using a collection of singleUser and groupMembers.
        Args:
            value: Value to set for the reviewers property.
        """
        self._reviewers = value
    
    @property
    def reviewer_type(self,) -> Optional[str]:
        """
        Gets the reviewerType property value. Who should be asked to do the review, either Self or Reviewers.
        Returns: Optional[str]
        """
        return self._reviewer_type
    
    @reviewer_type.setter
    def reviewer_type(self,value: Optional[str] = None) -> None:
        """
        Sets the reviewerType property value. Who should be asked to do the review, either Self or Reviewers.
        Args:
            value: Value to set for the reviewerType property.
        """
        self._reviewer_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("accessReviewTimeoutBehavior", self.access_review_timeout_behavior)
        writer.write_int_value("durationInDays", self.duration_in_days)
        writer.write_bool_value("isAccessRecommendationEnabled", self.is_access_recommendation_enabled)
        writer.write_bool_value("isApprovalJustificationRequired", self.is_approval_justification_required)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("recurrenceType", self.recurrence_type)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_str_value("reviewerType", self.reviewer_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. When the first review should start.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. When the first review should start.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    

