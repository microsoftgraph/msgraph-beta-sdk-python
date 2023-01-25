from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_decision = lazy_import('msgraph.generated.models.access_review_decision')
access_review_reviewer = lazy_import('msgraph.generated.models.access_review_reviewer')
access_review_settings = lazy_import('msgraph.generated.models.access_review_settings')
entity = lazy_import('msgraph.generated.models.entity')
identity = lazy_import('msgraph.generated.models.identity')
user_identity = lazy_import('msgraph.generated.models.user_identity')

class AccessReview(entity.Entity):
    @property
    def business_flow_template_id(self,) -> Optional[str]:
        """
        Gets the businessFlowTemplateId property value. The business flow template identifier. Required on create.  This value is case sensitive.
        Returns: Optional[str]
        """
        return self._business_flow_template_id
    
    @business_flow_template_id.setter
    def business_flow_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the businessFlowTemplateId property value. The business flow template identifier. Required on create.  This value is case sensitive.
        Args:
            value: Value to set for the businessFlowTemplateId property.
        """
        self._business_flow_template_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AccessReview and sets the default values.
        """
        super().__init__()
        # The business flow template identifier. Required on create.  This value is case sensitive.
        self._business_flow_template_id: Optional[str] = None
        # The user who created this review.
        self._created_by: Optional[user_identity.UserIdentity] = None
        # The collection of decisions for this access review.
        self._decisions: Optional[List[access_review_decision.AccessReviewDecision]] = None
        # The description provided by the access review creator, to show to the reviewers.
        self._description: Optional[str] = None
        # The access review name. Required on create.
        self._display_name: Optional[str] = None
        # The DateTime when the review is scheduled to end. This must be at least one day later than the start date.  Required on create.
        self._end_date_time: Optional[datetime] = None
        # The collection of access reviews instances past, present and future, if this object is a recurring access review.
        self._instances: Optional[List[access_review.AccessReview]] = None
        # The collection of decisions for the caller, if the caller is a reviewer.
        self._my_decisions: Optional[List[access_review_decision.AccessReviewDecision]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The object for which the access reviews is reviewing the access rights assignments. This can be the group for the review of memberships of users in a group, or the app for a review of assignments of users to an application. Required on create.
        self._reviewed_entity: Optional[identity.Identity] = None
        # The collection of reviewers for an access review, if access review reviewerType is of type delegated.
        self._reviewers: Optional[List[access_review_reviewer.AccessReviewReviewer]] = None
        # The relationship type of reviewer to the target object, one of self, delegated or entityOwners. Required on create.
        self._reviewer_type: Optional[str] = None
        # The settings of an accessReview, see type definition below.
        self._settings: Optional[access_review_settings.AccessReviewSettings] = None
        # The DateTime when the review is scheduled to be start.  This could be a date in the future.  Required on create.
        self._start_date_time: Optional[datetime] = None
        # This read-only field specifies the status of an accessReview. The typical states include Initializing, NotStarted, Starting,InProgress, Completing, Completed, AutoReviewing, and AutoReviewed.
        self._status: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[user_identity.UserIdentity]:
        """
        Gets the createdBy property value. The user who created this review.
        Returns: Optional[user_identity.UserIdentity]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[user_identity.UserIdentity] = None) -> None:
        """
        Sets the createdBy property value. The user who created this review.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReview
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReview()
    
    @property
    def decisions(self,) -> Optional[List[access_review_decision.AccessReviewDecision]]:
        """
        Gets the decisions property value. The collection of decisions for this access review.
        Returns: Optional[List[access_review_decision.AccessReviewDecision]]
        """
        return self._decisions
    
    @decisions.setter
    def decisions(self,value: Optional[List[access_review_decision.AccessReviewDecision]] = None) -> None:
        """
        Sets the decisions property value. The collection of decisions for this access review.
        Args:
            value: Value to set for the decisions property.
        """
        self._decisions = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description provided by the access review creator, to show to the reviewers.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description provided by the access review creator, to show to the reviewers.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The access review name. Required on create.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The access review name. Required on create.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The DateTime when the review is scheduled to end. This must be at least one day later than the start date.  Required on create.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The DateTime when the review is scheduled to end. This must be at least one day later than the start date.  Required on create.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "business_flow_template_id": lambda n : setattr(self, 'business_flow_template_id', n.get_str_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(user_identity.UserIdentity)),
            "decisions": lambda n : setattr(self, 'decisions', n.get_collection_of_object_values(access_review_decision.AccessReviewDecision)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "instances": lambda n : setattr(self, 'instances', n.get_collection_of_object_values(access_review.AccessReview)),
            "my_decisions": lambda n : setattr(self, 'my_decisions', n.get_collection_of_object_values(access_review_decision.AccessReviewDecision)),
            "reviewed_entity": lambda n : setattr(self, 'reviewed_entity', n.get_object_value(identity.Identity)),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(access_review_reviewer.AccessReviewReviewer)),
            "reviewer_type": lambda n : setattr(self, 'reviewer_type', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(access_review_settings.AccessReviewSettings)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def instances(self,) -> Optional[List[access_review.AccessReview]]:
        """
        Gets the instances property value. The collection of access reviews instances past, present and future, if this object is a recurring access review.
        Returns: Optional[List[access_review.AccessReview]]
        """
        return self._instances
    
    @instances.setter
    def instances(self,value: Optional[List[access_review.AccessReview]] = None) -> None:
        """
        Sets the instances property value. The collection of access reviews instances past, present and future, if this object is a recurring access review.
        Args:
            value: Value to set for the instances property.
        """
        self._instances = value
    
    @property
    def my_decisions(self,) -> Optional[List[access_review_decision.AccessReviewDecision]]:
        """
        Gets the myDecisions property value. The collection of decisions for the caller, if the caller is a reviewer.
        Returns: Optional[List[access_review_decision.AccessReviewDecision]]
        """
        return self._my_decisions
    
    @my_decisions.setter
    def my_decisions(self,value: Optional[List[access_review_decision.AccessReviewDecision]] = None) -> None:
        """
        Sets the myDecisions property value. The collection of decisions for the caller, if the caller is a reviewer.
        Args:
            value: Value to set for the myDecisions property.
        """
        self._my_decisions = value
    
    @property
    def reviewed_entity(self,) -> Optional[identity.Identity]:
        """
        Gets the reviewedEntity property value. The object for which the access reviews is reviewing the access rights assignments. This can be the group for the review of memberships of users in a group, or the app for a review of assignments of users to an application. Required on create.
        Returns: Optional[identity.Identity]
        """
        return self._reviewed_entity
    
    @reviewed_entity.setter
    def reviewed_entity(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the reviewedEntity property value. The object for which the access reviews is reviewing the access rights assignments. This can be the group for the review of memberships of users in a group, or the app for a review of assignments of users to an application. Required on create.
        Args:
            value: Value to set for the reviewedEntity property.
        """
        self._reviewed_entity = value
    
    @property
    def reviewers(self,) -> Optional[List[access_review_reviewer.AccessReviewReviewer]]:
        """
        Gets the reviewers property value. The collection of reviewers for an access review, if access review reviewerType is of type delegated.
        Returns: Optional[List[access_review_reviewer.AccessReviewReviewer]]
        """
        return self._reviewers
    
    @reviewers.setter
    def reviewers(self,value: Optional[List[access_review_reviewer.AccessReviewReviewer]] = None) -> None:
        """
        Sets the reviewers property value. The collection of reviewers for an access review, if access review reviewerType is of type delegated.
        Args:
            value: Value to set for the reviewers property.
        """
        self._reviewers = value
    
    @property
    def reviewer_type(self,) -> Optional[str]:
        """
        Gets the reviewerType property value. The relationship type of reviewer to the target object, one of self, delegated or entityOwners. Required on create.
        Returns: Optional[str]
        """
        return self._reviewer_type
    
    @reviewer_type.setter
    def reviewer_type(self,value: Optional[str] = None) -> None:
        """
        Sets the reviewerType property value. The relationship type of reviewer to the target object, one of self, delegated or entityOwners. Required on create.
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
        super().serialize(writer)
        writer.write_str_value("businessFlowTemplateId", self.business_flow_template_id)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_collection_of_object_values("decisions", self.decisions)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_collection_of_object_values("instances", self.instances)
        writer.write_collection_of_object_values("myDecisions", self.my_decisions)
        writer.write_object_value("reviewedEntity", self.reviewed_entity)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_str_value("reviewerType", self.reviewer_type)
        writer.write_object_value("settings", self.settings)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("status", self.status)
    
    @property
    def settings(self,) -> Optional[access_review_settings.AccessReviewSettings]:
        """
        Gets the settings property value. The settings of an accessReview, see type definition below.
        Returns: Optional[access_review_settings.AccessReviewSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[access_review_settings.AccessReviewSettings] = None) -> None:
        """
        Sets the settings property value. The settings of an accessReview, see type definition below.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The DateTime when the review is scheduled to be start.  This could be a date in the future.  Required on create.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The DateTime when the review is scheduled to be start.  This could be a date in the future.  Required on create.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. This read-only field specifies the status of an accessReview. The typical states include Initializing, NotStarted, Starting,InProgress, Completing, Completed, AutoReviewing, and AutoReviewed.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. This read-only field specifies the status of an accessReview. The typical states include Initializing, NotStarted, Starting,InProgress, Completing, Completed, AutoReviewing, and AutoReviewed.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

