from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_recommendation_insight_setting = lazy_import('msgraph.generated.models.access_review_recommendation_insight_setting')
access_review_reviewer_scope = lazy_import('msgraph.generated.models.access_review_reviewer_scope')

class AccessReviewStageSettings(AdditionalDataHolder, Parsable):
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
        Instantiates a new accessReviewStageSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicate which decisions will go to the next stage. Can be a sub-set of Approve, Deny, Recommendation, or NotReviewed. If not provided, all decisions will go to the next stage. Optional.
        self._decisions_that_will_move_to_next_stage: Optional[List[str]] = None
        # Defines the sequential or parallel order of the stages and depends on the stageId. Only sequential stages are currently supported. For example, if stageId is 2, then dependsOn must be 1. If stageId is 1, do not specify dependsOn. Required if stageId is not 1.
        self._depends_on: Optional[List[str]] = None
        # The duration of the stage. Required.  NOTE: The cumulative value of this property across all stages  1. Will override the instanceDurationInDays setting on the accessReviewScheduleDefinition object. 2. Cannot exceed the length of one recurrence. That is, if the review recurs weekly, the cumulative durationInDays cannot exceed 7.
        self._duration_in_days: Optional[int] = None
        # If provided, the fallback reviewers are asked to complete a review if the primary reviewers do not exist. For example, if managers are selected as reviewers and a principal under review does not have a manager in Azure AD, the fallback reviewers are asked to review that principal. NOTE: The value of this property will override the corresponding setting on the accessReviewScheduleDefinition object.
        self._fallback_reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The recommendationInsightSettings property
        self._recommendation_insight_settings: Optional[List[access_review_recommendation_insight_setting.AccessReviewRecommendationInsightSetting]] = None
        # Optional field. Indicates the time period of inactivity (with respect to the start date of the review instance) that recommendations will be configured from. The recommendation will be to deny if the user is inactive during the look back duration. For reviews of groups and Azure AD roles, any duration is accepted. For reviews of applications, 30 days is the maximum duration. If not specified, the duration is 30 days. NOTE: The value of this property will override the corresponding setting on the accessReviewScheduleDefinition object.
        self._recommendation_look_back_duration: Optional[Timedelta] = None
        # Indicates whether showing recommendations to reviewers is enabled. Required. NOTE: The value of this property will override override the corresponding setting on the accessReviewScheduleDefinition object.
        self._recommendations_enabled: Optional[bool] = None
        # Defines who the reviewers are. If none are specified, the review is a self-review (users review their own access).  For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API. NOTE: The value of this property will override the corresponding setting on the accessReviewScheduleDefinition.
        self._reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
        # Unique identifier of the accessReviewStageSettings. The stageId will be used in dependsOn property to indicate the stage relationship. Required.
        self._stage_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewStageSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewStageSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewStageSettings()
    
    @property
    def decisions_that_will_move_to_next_stage(self,) -> Optional[List[str]]:
        """
        Gets the decisionsThatWillMoveToNextStage property value. Indicate which decisions will go to the next stage. Can be a sub-set of Approve, Deny, Recommendation, or NotReviewed. If not provided, all decisions will go to the next stage. Optional.
        Returns: Optional[List[str]]
        """
        return self._decisions_that_will_move_to_next_stage
    
    @decisions_that_will_move_to_next_stage.setter
    def decisions_that_will_move_to_next_stage(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the decisionsThatWillMoveToNextStage property value. Indicate which decisions will go to the next stage. Can be a sub-set of Approve, Deny, Recommendation, or NotReviewed. If not provided, all decisions will go to the next stage. Optional.
        Args:
            value: Value to set for the decisions_that_will_move_to_next_stage property.
        """
        self._decisions_that_will_move_to_next_stage = value
    
    @property
    def depends_on(self,) -> Optional[List[str]]:
        """
        Gets the dependsOn property value. Defines the sequential or parallel order of the stages and depends on the stageId. Only sequential stages are currently supported. For example, if stageId is 2, then dependsOn must be 1. If stageId is 1, do not specify dependsOn. Required if stageId is not 1.
        Returns: Optional[List[str]]
        """
        return self._depends_on
    
    @depends_on.setter
    def depends_on(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the dependsOn property value. Defines the sequential or parallel order of the stages and depends on the stageId. Only sequential stages are currently supported. For example, if stageId is 2, then dependsOn must be 1. If stageId is 1, do not specify dependsOn. Required if stageId is not 1.
        Args:
            value: Value to set for the depends_on property.
        """
        self._depends_on = value
    
    @property
    def duration_in_days(self,) -> Optional[int]:
        """
        Gets the durationInDays property value. The duration of the stage. Required.  NOTE: The cumulative value of this property across all stages  1. Will override the instanceDurationInDays setting on the accessReviewScheduleDefinition object. 2. Cannot exceed the length of one recurrence. That is, if the review recurs weekly, the cumulative durationInDays cannot exceed 7.
        Returns: Optional[int]
        """
        return self._duration_in_days
    
    @duration_in_days.setter
    def duration_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the durationInDays property value. The duration of the stage. Required.  NOTE: The cumulative value of this property across all stages  1. Will override the instanceDurationInDays setting on the accessReviewScheduleDefinition object. 2. Cannot exceed the length of one recurrence. That is, if the review recurs weekly, the cumulative durationInDays cannot exceed 7.
        Args:
            value: Value to set for the duration_in_days property.
        """
        self._duration_in_days = value
    
    @property
    def fallback_reviewers(self,) -> Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]:
        """
        Gets the fallbackReviewers property value. If provided, the fallback reviewers are asked to complete a review if the primary reviewers do not exist. For example, if managers are selected as reviewers and a principal under review does not have a manager in Azure AD, the fallback reviewers are asked to review that principal. NOTE: The value of this property will override the corresponding setting on the accessReviewScheduleDefinition object.
        Returns: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]
        """
        return self._fallback_reviewers
    
    @fallback_reviewers.setter
    def fallback_reviewers(self,value: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None) -> None:
        """
        Sets the fallbackReviewers property value. If provided, the fallback reviewers are asked to complete a review if the primary reviewers do not exist. For example, if managers are selected as reviewers and a principal under review does not have a manager in Azure AD, the fallback reviewers are asked to review that principal. NOTE: The value of this property will override the corresponding setting on the accessReviewScheduleDefinition object.
        Args:
            value: Value to set for the fallback_reviewers property.
        """
        self._fallback_reviewers = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "decisionsThatWillMoveToNextStage": lambda n : setattr(self, 'decisions_that_will_move_to_next_stage', n.get_collection_of_primitive_values(str)),
            "dependsOn": lambda n : setattr(self, 'depends_on', n.get_collection_of_primitive_values(str)),
            "durationInDays": lambda n : setattr(self, 'duration_in_days', n.get_int_value()),
            "fallbackReviewers": lambda n : setattr(self, 'fallback_reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommendationsEnabled": lambda n : setattr(self, 'recommendations_enabled', n.get_bool_value()),
            "recommendationInsightSettings": lambda n : setattr(self, 'recommendation_insight_settings', n.get_collection_of_object_values(access_review_recommendation_insight_setting.AccessReviewRecommendationInsightSetting)),
            "recommendationLookBackDuration": lambda n : setattr(self, 'recommendation_look_back_duration', n.get_object_value(Timedelta)),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "stageId": lambda n : setattr(self, 'stage_id', n.get_str_value()),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def recommendation_insight_settings(self,) -> Optional[List[access_review_recommendation_insight_setting.AccessReviewRecommendationInsightSetting]]:
        """
        Gets the recommendationInsightSettings property value. The recommendationInsightSettings property
        Returns: Optional[List[access_review_recommendation_insight_setting.AccessReviewRecommendationInsightSetting]]
        """
        return self._recommendation_insight_settings
    
    @recommendation_insight_settings.setter
    def recommendation_insight_settings(self,value: Optional[List[access_review_recommendation_insight_setting.AccessReviewRecommendationInsightSetting]] = None) -> None:
        """
        Sets the recommendationInsightSettings property value. The recommendationInsightSettings property
        Args:
            value: Value to set for the recommendation_insight_settings property.
        """
        self._recommendation_insight_settings = value
    
    @property
    def recommendation_look_back_duration(self,) -> Optional[Timedelta]:
        """
        Gets the recommendationLookBackDuration property value. Optional field. Indicates the time period of inactivity (with respect to the start date of the review instance) that recommendations will be configured from. The recommendation will be to deny if the user is inactive during the look back duration. For reviews of groups and Azure AD roles, any duration is accepted. For reviews of applications, 30 days is the maximum duration. If not specified, the duration is 30 days. NOTE: The value of this property will override the corresponding setting on the accessReviewScheduleDefinition object.
        Returns: Optional[Timedelta]
        """
        return self._recommendation_look_back_duration
    
    @recommendation_look_back_duration.setter
    def recommendation_look_back_duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the recommendationLookBackDuration property value. Optional field. Indicates the time period of inactivity (with respect to the start date of the review instance) that recommendations will be configured from. The recommendation will be to deny if the user is inactive during the look back duration. For reviews of groups and Azure AD roles, any duration is accepted. For reviews of applications, 30 days is the maximum duration. If not specified, the duration is 30 days. NOTE: The value of this property will override the corresponding setting on the accessReviewScheduleDefinition object.
        Args:
            value: Value to set for the recommendation_look_back_duration property.
        """
        self._recommendation_look_back_duration = value
    
    @property
    def recommendations_enabled(self,) -> Optional[bool]:
        """
        Gets the recommendationsEnabled property value. Indicates whether showing recommendations to reviewers is enabled. Required. NOTE: The value of this property will override override the corresponding setting on the accessReviewScheduleDefinition object.
        Returns: Optional[bool]
        """
        return self._recommendations_enabled
    
    @recommendations_enabled.setter
    def recommendations_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the recommendationsEnabled property value. Indicates whether showing recommendations to reviewers is enabled. Required. NOTE: The value of this property will override override the corresponding setting on the accessReviewScheduleDefinition object.
        Args:
            value: Value to set for the recommendations_enabled property.
        """
        self._recommendations_enabled = value
    
    @property
    def reviewers(self,) -> Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]:
        """
        Gets the reviewers property value. Defines who the reviewers are. If none are specified, the review is a self-review (users review their own access).  For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API. NOTE: The value of this property will override the corresponding setting on the accessReviewScheduleDefinition.
        Returns: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]
        """
        return self._reviewers
    
    @reviewers.setter
    def reviewers(self,value: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None) -> None:
        """
        Sets the reviewers property value. Defines who the reviewers are. If none are specified, the review is a self-review (users review their own access).  For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API. NOTE: The value of this property will override the corresponding setting on the accessReviewScheduleDefinition.
        Args:
            value: Value to set for the reviewers property.
        """
        self._reviewers = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("decisionsThatWillMoveToNextStage", self.decisions_that_will_move_to_next_stage)
        writer.write_collection_of_primitive_values("dependsOn", self.depends_on)
        writer.write_int_value("durationInDays", self.duration_in_days)
        writer.write_collection_of_object_values("fallbackReviewers", self.fallback_reviewers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("recommendationsEnabled", self.recommendations_enabled)
        writer.write_collection_of_object_values("recommendationInsightSettings", self.recommendation_insight_settings)
        writer.write_object_value("recommendationLookBackDuration", self.recommendation_look_back_duration)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_str_value("stageId", self.stage_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def stage_id(self,) -> Optional[str]:
        """
        Gets the stageId property value. Unique identifier of the accessReviewStageSettings. The stageId will be used in dependsOn property to indicate the stage relationship. Required.
        Returns: Optional[str]
        """
        return self._stage_id
    
    @stage_id.setter
    def stage_id(self,value: Optional[str] = None) -> None:
        """
        Sets the stageId property value. Unique identifier of the accessReviewStageSettings. The stageId will be used in dependsOn property to indicate the stage relationship. Required.
        Args:
            value: Value to set for the stage_id property.
        """
        self._stage_id = value
    

