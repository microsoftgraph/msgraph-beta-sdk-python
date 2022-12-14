from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user_identity = lazy_import('msgraph.generated.models.user_identity')

class AccessReviewDecision(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def access_recommendation(self,) -> Optional[str]:
        """
        Gets the accessRecommendation property value. The feature- generated recommendation shown to the reviewer, one of Approve, Deny or NotAvailable.
        Returns: Optional[str]
        """
        return self._access_recommendation
    
    @access_recommendation.setter
    def access_recommendation(self,value: Optional[str] = None) -> None:
        """
        Sets the accessRecommendation property value. The feature- generated recommendation shown to the reviewer, one of Approve, Deny or NotAvailable.
        Args:
            value: Value to set for the accessRecommendation property.
        """
        self._access_recommendation = value
    
    @property
    def access_review_id(self,) -> Optional[str]:
        """
        Gets the accessReviewId property value. The feature-generated id of the access review.
        Returns: Optional[str]
        """
        return self._access_review_id
    
    @access_review_id.setter
    def access_review_id(self,value: Optional[str] = None) -> None:
        """
        Sets the accessReviewId property value. The feature-generated id of the access review.
        Args:
            value: Value to set for the accessReviewId property.
        """
        self._access_review_id = value
    
    @property
    def applied_by(self,) -> Optional[user_identity.UserIdentity]:
        """
        Gets the appliedBy property value. When the review completes, if the results were manually applied, the user identity of the user who applied the decision. If the review was auto-applied, the userPrincipalName is empty.
        Returns: Optional[user_identity.UserIdentity]
        """
        return self._applied_by
    
    @applied_by.setter
    def applied_by(self,value: Optional[user_identity.UserIdentity] = None) -> None:
        """
        Sets the appliedBy property value. When the review completes, if the results were manually applied, the user identity of the user who applied the decision. If the review was auto-applied, the userPrincipalName is empty.
        Args:
            value: Value to set for the appliedBy property.
        """
        self._applied_by = value
    
    @property
    def applied_date_time(self,) -> Optional[datetime]:
        """
        Gets the appliedDateTime property value. The date and time when the review decision was applied.
        Returns: Optional[datetime]
        """
        return self._applied_date_time
    
    @applied_date_time.setter
    def applied_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the appliedDateTime property value. The date and time when the review decision was applied.
        Args:
            value: Value to set for the appliedDateTime property.
        """
        self._applied_date_time = value
    
    @property
    def apply_result(self,) -> Optional[str]:
        """
        Gets the applyResult property value. The outcome of applying the decision, one of NotApplied, Success, Failed, NotFound or NotSupported.
        Returns: Optional[str]
        """
        return self._apply_result
    
    @apply_result.setter
    def apply_result(self,value: Optional[str] = None) -> None:
        """
        Sets the applyResult property value. The outcome of applying the decision, one of NotApplied, Success, Failed, NotFound or NotSupported.
        Args:
            value: Value to set for the applyResult property.
        """
        self._apply_result = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessReviewDecision and sets the default values.
        """
        super().__init__()
        # The feature- generated recommendation shown to the reviewer, one of Approve, Deny or NotAvailable.
        self._access_recommendation: Optional[str] = None
        # The feature-generated id of the access review.
        self._access_review_id: Optional[str] = None
        # When the review completes, if the results were manually applied, the user identity of the user who applied the decision. If the review was auto-applied, the userPrincipalName is empty.
        self._applied_by: Optional[user_identity.UserIdentity] = None
        # The date and time when the review decision was applied.
        self._applied_date_time: Optional[datetime] = None
        # The outcome of applying the decision, one of NotApplied, Success, Failed, NotFound or NotSupported.
        self._apply_result: Optional[str] = None
        # The reviewer's business justification, if supplied.
        self._justification: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The identity of the reviewer. If the recommendation was used as the review, the userPrincipalName is empty.
        self._reviewed_by: Optional[user_identity.UserIdentity] = None
        # The reviewedDateTime property
        self._reviewed_date_time: Optional[datetime] = None
        # The result of the review, one of NotReviewed, Deny, DontKnow or Approve.
        self._review_result: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewDecision:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewDecision
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewDecision()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_recommendation": lambda n : setattr(self, 'access_recommendation', n.get_str_value()),
            "access_review_id": lambda n : setattr(self, 'access_review_id', n.get_str_value()),
            "applied_by": lambda n : setattr(self, 'applied_by', n.get_object_value(user_identity.UserIdentity)),
            "applied_date_time": lambda n : setattr(self, 'applied_date_time', n.get_datetime_value()),
            "apply_result": lambda n : setattr(self, 'apply_result', n.get_str_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "reviewed_by": lambda n : setattr(self, 'reviewed_by', n.get_object_value(user_identity.UserIdentity)),
            "reviewed_date_time": lambda n : setattr(self, 'reviewed_date_time', n.get_datetime_value()),
            "review_result": lambda n : setattr(self, 'review_result', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def justification(self,) -> Optional[str]:
        """
        Gets the justification property value. The reviewer's business justification, if supplied.
        Returns: Optional[str]
        """
        return self._justification
    
    @justification.setter
    def justification(self,value: Optional[str] = None) -> None:
        """
        Sets the justification property value. The reviewer's business justification, if supplied.
        Args:
            value: Value to set for the justification property.
        """
        self._justification = value
    
    @property
    def reviewed_by(self,) -> Optional[user_identity.UserIdentity]:
        """
        Gets the reviewedBy property value. The identity of the reviewer. If the recommendation was used as the review, the userPrincipalName is empty.
        Returns: Optional[user_identity.UserIdentity]
        """
        return self._reviewed_by
    
    @reviewed_by.setter
    def reviewed_by(self,value: Optional[user_identity.UserIdentity] = None) -> None:
        """
        Sets the reviewedBy property value. The identity of the reviewer. If the recommendation was used as the review, the userPrincipalName is empty.
        Args:
            value: Value to set for the reviewedBy property.
        """
        self._reviewed_by = value
    
    @property
    def reviewed_date_time(self,) -> Optional[datetime]:
        """
        Gets the reviewedDateTime property value. The reviewedDateTime property
        Returns: Optional[datetime]
        """
        return self._reviewed_date_time
    
    @reviewed_date_time.setter
    def reviewed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the reviewedDateTime property value. The reviewedDateTime property
        Args:
            value: Value to set for the reviewedDateTime property.
        """
        self._reviewed_date_time = value
    
    @property
    def review_result(self,) -> Optional[str]:
        """
        Gets the reviewResult property value. The result of the review, one of NotReviewed, Deny, DontKnow or Approve.
        Returns: Optional[str]
        """
        return self._review_result
    
    @review_result.setter
    def review_result(self,value: Optional[str] = None) -> None:
        """
        Sets the reviewResult property value. The result of the review, one of NotReviewed, Deny, DontKnow or Approve.
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
        super().serialize(writer)
        writer.write_str_value("accessRecommendation", self.access_recommendation)
        writer.write_str_value("accessReviewId", self.access_review_id)
        writer.write_object_value("appliedBy", self.applied_by)
        writer.write_datetime_value("appliedDateTime", self.applied_date_time)
        writer.write_str_value("applyResult", self.apply_result)
        writer.write_str_value("justification", self.justification)
        writer.write_object_value("reviewedBy", self.reviewed_by)
        writer.write_datetime_value("reviewedDateTime", self.reviewed_date_time)
        writer.write_str_value("reviewResult", self.review_result)
    

