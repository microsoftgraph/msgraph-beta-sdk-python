from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_apply_action, access_review_recommendation_insight_setting, patterned_recurrence

class AccessReviewScheduleSettings(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new accessReviewScheduleSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Optional field. Describes the  actions to take once a review is complete. There are two types that are currently supported: removeAccessApplyAction (default) and disableAndDeleteUserApplyAction. Field only needs to be specified in the case of disableAndDeleteUserApplyAction.
        self._apply_actions: Optional[List[access_review_apply_action.AccessReviewApplyAction]] = None
        # Indicates whether decisions are automatically applied. When set to false, an admin must apply the decisions manually once the reviewer completes the access review. When set to true, decisions are applied automatically after the access review instance duration ends, whether or not the reviewers have responded. Default value is false.  CAUTION: If both autoApplyDecisionsEnabled and defaultDecisionEnabled are true, all access for the principals to the resource risks being revoked if the reviewers fail to respond.
        self._auto_apply_decisions_enabled: Optional[bool] = None
        # Indicates whether decisions on previous access review stages are available for reviewers on an accessReviewInstance with multiple subsequent stages. If not provided, the default is disabled (false).
        self._decision_histories_for_reviewers_enabled: Optional[bool] = None
        # Decision chosen if defaultDecisionEnabled is enabled. Can be one of Approve, Deny, or Recommendation.
        self._default_decision: Optional[str] = None
        # Indicates whether the default decision is enabled or disabled when reviewers do not respond. Default value is false.  CAUTION: If both autoApplyDecisionsEnabled and defaultDecisionEnabled are true, all access for the principals to the resource risks being revoked if the reviewers fail to respond.
        self._default_decision_enabled: Optional[bool] = None
        # Duration of each recurrence of review (accessReviewInstance) in number of days. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its durationInDays setting will be used instead of the value of this property.
        self._instance_duration_in_days: Optional[int] = None
        # Indicates whether reviewers are required to provide justification with their decision. Default value is false.
        self._justification_required_on_approval: Optional[bool] = None
        # Indicates whether emails are enabled or disabled. Default value is false.
        self._mail_notifications_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Optional. Describes the types of insights that aid reviewers to make access review decisions. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its recommendationInsightSettings setting will be used instead of the value of this property.
        self._recommendation_insight_settings: Optional[List[access_review_recommendation_insight_setting.AccessReviewRecommendationInsightSetting]] = None
        # Optional field. Indicates the period of inactivity (with respect to the start date of the review instance) that recommendations will be configured from. The recommendation will be to deny if the user is inactive during the look-back duration. For reviews of groups and Azure AD roles, any duration is accepted. For reviews of applications, 30 days is the maximum duration. If not specified, the duration is 30 days. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its recommendationLookBackDuration setting will be used instead of the value of this property.
        self._recommendation_look_back_duration: Optional[timedelta] = None
        # Indicates whether decision recommendations are enabled or disabled. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its recommendationsEnabled setting will be used instead of the value of this property.
        self._recommendations_enabled: Optional[bool] = None
        # Detailed settings for recurrence using the standard Outlook recurrence object. Note: Only dayOfMonth, interval, and type (weekly, absoluteMonthly) properties are supported. Use the property startDate on recurrenceRange to determine the day the review starts.
        self._recurrence: Optional[patterned_recurrence.PatternedRecurrence] = None
        # Indicates whether reminders are enabled or disabled. Default value is false.
        self._reminder_notifications_enabled: Optional[bool] = None
    
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
    def apply_actions(self,) -> Optional[List[access_review_apply_action.AccessReviewApplyAction]]:
        """
        Gets the applyActions property value. Optional field. Describes the  actions to take once a review is complete. There are two types that are currently supported: removeAccessApplyAction (default) and disableAndDeleteUserApplyAction. Field only needs to be specified in the case of disableAndDeleteUserApplyAction.
        Returns: Optional[List[access_review_apply_action.AccessReviewApplyAction]]
        """
        return self._apply_actions
    
    @apply_actions.setter
    def apply_actions(self,value: Optional[List[access_review_apply_action.AccessReviewApplyAction]] = None) -> None:
        """
        Sets the applyActions property value. Optional field. Describes the  actions to take once a review is complete. There are two types that are currently supported: removeAccessApplyAction (default) and disableAndDeleteUserApplyAction. Field only needs to be specified in the case of disableAndDeleteUserApplyAction.
        Args:
            value: Value to set for the apply_actions property.
        """
        self._apply_actions = value
    
    @property
    def auto_apply_decisions_enabled(self,) -> Optional[bool]:
        """
        Gets the autoApplyDecisionsEnabled property value. Indicates whether decisions are automatically applied. When set to false, an admin must apply the decisions manually once the reviewer completes the access review. When set to true, decisions are applied automatically after the access review instance duration ends, whether or not the reviewers have responded. Default value is false.  CAUTION: If both autoApplyDecisionsEnabled and defaultDecisionEnabled are true, all access for the principals to the resource risks being revoked if the reviewers fail to respond.
        Returns: Optional[bool]
        """
        return self._auto_apply_decisions_enabled
    
    @auto_apply_decisions_enabled.setter
    def auto_apply_decisions_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoApplyDecisionsEnabled property value. Indicates whether decisions are automatically applied. When set to false, an admin must apply the decisions manually once the reviewer completes the access review. When set to true, decisions are applied automatically after the access review instance duration ends, whether or not the reviewers have responded. Default value is false.  CAUTION: If both autoApplyDecisionsEnabled and defaultDecisionEnabled are true, all access for the principals to the resource risks being revoked if the reviewers fail to respond.
        Args:
            value: Value to set for the auto_apply_decisions_enabled property.
        """
        self._auto_apply_decisions_enabled = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewScheduleSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewScheduleSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewScheduleSettings()
    
    @property
    def decision_histories_for_reviewers_enabled(self,) -> Optional[bool]:
        """
        Gets the decisionHistoriesForReviewersEnabled property value. Indicates whether decisions on previous access review stages are available for reviewers on an accessReviewInstance with multiple subsequent stages. If not provided, the default is disabled (false).
        Returns: Optional[bool]
        """
        return self._decision_histories_for_reviewers_enabled
    
    @decision_histories_for_reviewers_enabled.setter
    def decision_histories_for_reviewers_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the decisionHistoriesForReviewersEnabled property value. Indicates whether decisions on previous access review stages are available for reviewers on an accessReviewInstance with multiple subsequent stages. If not provided, the default is disabled (false).
        Args:
            value: Value to set for the decision_histories_for_reviewers_enabled property.
        """
        self._decision_histories_for_reviewers_enabled = value
    
    @property
    def default_decision(self,) -> Optional[str]:
        """
        Gets the defaultDecision property value. Decision chosen if defaultDecisionEnabled is enabled. Can be one of Approve, Deny, or Recommendation.
        Returns: Optional[str]
        """
        return self._default_decision
    
    @default_decision.setter
    def default_decision(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultDecision property value. Decision chosen if defaultDecisionEnabled is enabled. Can be one of Approve, Deny, or Recommendation.
        Args:
            value: Value to set for the default_decision property.
        """
        self._default_decision = value
    
    @property
    def default_decision_enabled(self,) -> Optional[bool]:
        """
        Gets the defaultDecisionEnabled property value. Indicates whether the default decision is enabled or disabled when reviewers do not respond. Default value is false.  CAUTION: If both autoApplyDecisionsEnabled and defaultDecisionEnabled are true, all access for the principals to the resource risks being revoked if the reviewers fail to respond.
        Returns: Optional[bool]
        """
        return self._default_decision_enabled
    
    @default_decision_enabled.setter
    def default_decision_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the defaultDecisionEnabled property value. Indicates whether the default decision is enabled or disabled when reviewers do not respond. Default value is false.  CAUTION: If both autoApplyDecisionsEnabled and defaultDecisionEnabled are true, all access for the principals to the resource risks being revoked if the reviewers fail to respond.
        Args:
            value: Value to set for the default_decision_enabled property.
        """
        self._default_decision_enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_apply_action, access_review_recommendation_insight_setting, patterned_recurrence

        fields: Dict[str, Callable[[Any], None]] = {
            "applyActions": lambda n : setattr(self, 'apply_actions', n.get_collection_of_object_values(access_review_apply_action.AccessReviewApplyAction)),
            "autoApplyDecisionsEnabled": lambda n : setattr(self, 'auto_apply_decisions_enabled', n.get_bool_value()),
            "decisionHistoriesForReviewersEnabled": lambda n : setattr(self, 'decision_histories_for_reviewers_enabled', n.get_bool_value()),
            "defaultDecision": lambda n : setattr(self, 'default_decision', n.get_str_value()),
            "defaultDecisionEnabled": lambda n : setattr(self, 'default_decision_enabled', n.get_bool_value()),
            "instanceDurationInDays": lambda n : setattr(self, 'instance_duration_in_days', n.get_int_value()),
            "justificationRequiredOnApproval": lambda n : setattr(self, 'justification_required_on_approval', n.get_bool_value()),
            "mailNotificationsEnabled": lambda n : setattr(self, 'mail_notifications_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommendationsEnabled": lambda n : setattr(self, 'recommendations_enabled', n.get_bool_value()),
            "recommendationInsightSettings": lambda n : setattr(self, 'recommendation_insight_settings', n.get_collection_of_object_values(access_review_recommendation_insight_setting.AccessReviewRecommendationInsightSetting)),
            "recommendationLookBackDuration": lambda n : setattr(self, 'recommendation_look_back_duration', n.get_timedelta_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(patterned_recurrence.PatternedRecurrence)),
            "reminderNotificationsEnabled": lambda n : setattr(self, 'reminder_notifications_enabled', n.get_bool_value()),
        }
        return fields
    
    @property
    def instance_duration_in_days(self,) -> Optional[int]:
        """
        Gets the instanceDurationInDays property value. Duration of each recurrence of review (accessReviewInstance) in number of days. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its durationInDays setting will be used instead of the value of this property.
        Returns: Optional[int]
        """
        return self._instance_duration_in_days
    
    @instance_duration_in_days.setter
    def instance_duration_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the instanceDurationInDays property value. Duration of each recurrence of review (accessReviewInstance) in number of days. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its durationInDays setting will be used instead of the value of this property.
        Args:
            value: Value to set for the instance_duration_in_days property.
        """
        self._instance_duration_in_days = value
    
    @property
    def justification_required_on_approval(self,) -> Optional[bool]:
        """
        Gets the justificationRequiredOnApproval property value. Indicates whether reviewers are required to provide justification with their decision. Default value is false.
        Returns: Optional[bool]
        """
        return self._justification_required_on_approval
    
    @justification_required_on_approval.setter
    def justification_required_on_approval(self,value: Optional[bool] = None) -> None:
        """
        Sets the justificationRequiredOnApproval property value. Indicates whether reviewers are required to provide justification with their decision. Default value is false.
        Args:
            value: Value to set for the justification_required_on_approval property.
        """
        self._justification_required_on_approval = value
    
    @property
    def mail_notifications_enabled(self,) -> Optional[bool]:
        """
        Gets the mailNotificationsEnabled property value. Indicates whether emails are enabled or disabled. Default value is false.
        Returns: Optional[bool]
        """
        return self._mail_notifications_enabled
    
    @mail_notifications_enabled.setter
    def mail_notifications_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the mailNotificationsEnabled property value. Indicates whether emails are enabled or disabled. Default value is false.
        Args:
            value: Value to set for the mail_notifications_enabled property.
        """
        self._mail_notifications_enabled = value
    
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
        Gets the recommendationInsightSettings property value. Optional. Describes the types of insights that aid reviewers to make access review decisions. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its recommendationInsightSettings setting will be used instead of the value of this property.
        Returns: Optional[List[access_review_recommendation_insight_setting.AccessReviewRecommendationInsightSetting]]
        """
        return self._recommendation_insight_settings
    
    @recommendation_insight_settings.setter
    def recommendation_insight_settings(self,value: Optional[List[access_review_recommendation_insight_setting.AccessReviewRecommendationInsightSetting]] = None) -> None:
        """
        Sets the recommendationInsightSettings property value. Optional. Describes the types of insights that aid reviewers to make access review decisions. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its recommendationInsightSettings setting will be used instead of the value of this property.
        Args:
            value: Value to set for the recommendation_insight_settings property.
        """
        self._recommendation_insight_settings = value
    
    @property
    def recommendation_look_back_duration(self,) -> Optional[timedelta]:
        """
        Gets the recommendationLookBackDuration property value. Optional field. Indicates the period of inactivity (with respect to the start date of the review instance) that recommendations will be configured from. The recommendation will be to deny if the user is inactive during the look-back duration. For reviews of groups and Azure AD roles, any duration is accepted. For reviews of applications, 30 days is the maximum duration. If not specified, the duration is 30 days. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its recommendationLookBackDuration setting will be used instead of the value of this property.
        Returns: Optional[timedelta]
        """
        return self._recommendation_look_back_duration
    
    @recommendation_look_back_duration.setter
    def recommendation_look_back_duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the recommendationLookBackDuration property value. Optional field. Indicates the period of inactivity (with respect to the start date of the review instance) that recommendations will be configured from. The recommendation will be to deny if the user is inactive during the look-back duration. For reviews of groups and Azure AD roles, any duration is accepted. For reviews of applications, 30 days is the maximum duration. If not specified, the duration is 30 days. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its recommendationLookBackDuration setting will be used instead of the value of this property.
        Args:
            value: Value to set for the recommendation_look_back_duration property.
        """
        self._recommendation_look_back_duration = value
    
    @property
    def recommendations_enabled(self,) -> Optional[bool]:
        """
        Gets the recommendationsEnabled property value. Indicates whether decision recommendations are enabled or disabled. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its recommendationsEnabled setting will be used instead of the value of this property.
        Returns: Optional[bool]
        """
        return self._recommendations_enabled
    
    @recommendations_enabled.setter
    def recommendations_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the recommendationsEnabled property value. Indicates whether decision recommendations are enabled or disabled. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its recommendationsEnabled setting will be used instead of the value of this property.
        Args:
            value: Value to set for the recommendations_enabled property.
        """
        self._recommendations_enabled = value
    
    @property
    def recurrence(self,) -> Optional[patterned_recurrence.PatternedRecurrence]:
        """
        Gets the recurrence property value. Detailed settings for recurrence using the standard Outlook recurrence object. Note: Only dayOfMonth, interval, and type (weekly, absoluteMonthly) properties are supported. Use the property startDate on recurrenceRange to determine the day the review starts.
        Returns: Optional[patterned_recurrence.PatternedRecurrence]
        """
        return self._recurrence
    
    @recurrence.setter
    def recurrence(self,value: Optional[patterned_recurrence.PatternedRecurrence] = None) -> None:
        """
        Sets the recurrence property value. Detailed settings for recurrence using the standard Outlook recurrence object. Note: Only dayOfMonth, interval, and type (weekly, absoluteMonthly) properties are supported. Use the property startDate on recurrenceRange to determine the day the review starts.
        Args:
            value: Value to set for the recurrence property.
        """
        self._recurrence = value
    
    @property
    def reminder_notifications_enabled(self,) -> Optional[bool]:
        """
        Gets the reminderNotificationsEnabled property value. Indicates whether reminders are enabled or disabled. Default value is false.
        Returns: Optional[bool]
        """
        return self._reminder_notifications_enabled
    
    @reminder_notifications_enabled.setter
    def reminder_notifications_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the reminderNotificationsEnabled property value. Indicates whether reminders are enabled or disabled. Default value is false.
        Args:
            value: Value to set for the reminder_notifications_enabled property.
        """
        self._reminder_notifications_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("applyActions", self.apply_actions)
        writer.write_bool_value("autoApplyDecisionsEnabled", self.auto_apply_decisions_enabled)
        writer.write_bool_value("decisionHistoriesForReviewersEnabled", self.decision_histories_for_reviewers_enabled)
        writer.write_str_value("defaultDecision", self.default_decision)
        writer.write_bool_value("defaultDecisionEnabled", self.default_decision_enabled)
        writer.write_int_value("instanceDurationInDays", self.instance_duration_in_days)
        writer.write_bool_value("justificationRequiredOnApproval", self.justification_required_on_approval)
        writer.write_bool_value("mailNotificationsEnabled", self.mail_notifications_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("recommendationsEnabled", self.recommendations_enabled)
        writer.write_collection_of_object_values("recommendationInsightSettings", self.recommendation_insight_settings)
        writer.write_timedelta_value("recommendationLookBackDuration", self.recommendation_look_back_duration)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_bool_value("reminderNotificationsEnabled", self.reminder_notifications_enabled)
        writer.write_additional_data_value(self.additional_data)
    

