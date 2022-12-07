from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_recurrence_settings = lazy_import('msgraph.generated.models.access_review_recurrence_settings')
auto_review_settings = lazy_import('msgraph.generated.models.auto_review_settings')

class AccessReviewSettings(AdditionalDataHolder, Parsable):
    @property
    def access_recommendations_enabled(self,) -> Optional[bool]:
        """
        Gets the accessRecommendationsEnabled property value. Indicates whether showing recommendations to reviewers is enabled.
        Returns: Optional[bool]
        """
        return self._access_recommendations_enabled
    
    @access_recommendations_enabled.setter
    def access_recommendations_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the accessRecommendationsEnabled property value. Indicates whether showing recommendations to reviewers is enabled.
        Args:
            value: Value to set for the accessRecommendationsEnabled property.
        """
        self._access_recommendations_enabled = value
    
    @property
    def activity_duration_in_days(self,) -> Optional[int]:
        """
        Gets the activityDurationInDays property value. The number of days of user activities to show to reviewers.
        Returns: Optional[int]
        """
        return self._activity_duration_in_days
    
    @activity_duration_in_days.setter
    def activity_duration_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the activityDurationInDays property value. The number of days of user activities to show to reviewers.
        Args:
            value: Value to set for the activityDurationInDays property.
        """
        self._activity_duration_in_days = value
    
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
    def auto_apply_review_results_enabled(self,) -> Optional[bool]:
        """
        Gets the autoApplyReviewResultsEnabled property value. Indicates whether the auto-apply capability, to automatically change the target object access resource, is enabled.  If not enabled, a user must, after the review completes, apply the access review.
        Returns: Optional[bool]
        """
        return self._auto_apply_review_results_enabled
    
    @auto_apply_review_results_enabled.setter
    def auto_apply_review_results_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoApplyReviewResultsEnabled property value. Indicates whether the auto-apply capability, to automatically change the target object access resource, is enabled.  If not enabled, a user must, after the review completes, apply the access review.
        Args:
            value: Value to set for the autoApplyReviewResultsEnabled property.
        """
        self._auto_apply_review_results_enabled = value
    
    @property
    def auto_review_enabled(self,) -> Optional[bool]:
        """
        Gets the autoReviewEnabled property value. Indicates whether a decision should be set if the reviewer did not supply one. For use when auto-apply is enabled. If you don't want to have a review decision recorded unless the reviewer makes an explicit choice, set it to false.
        Returns: Optional[bool]
        """
        return self._auto_review_enabled
    
    @auto_review_enabled.setter
    def auto_review_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoReviewEnabled property value. Indicates whether a decision should be set if the reviewer did not supply one. For use when auto-apply is enabled. If you don't want to have a review decision recorded unless the reviewer makes an explicit choice, set it to false.
        Args:
            value: Value to set for the autoReviewEnabled property.
        """
        self._auto_review_enabled = value
    
    @property
    def auto_review_settings(self,) -> Optional[auto_review_settings.AutoReviewSettings]:
        """
        Gets the autoReviewSettings property value. Detailed settings for how the feature should set the review decision. For use when auto-apply is enabled.
        Returns: Optional[auto_review_settings.AutoReviewSettings]
        """
        return self._auto_review_settings
    
    @auto_review_settings.setter
    def auto_review_settings(self,value: Optional[auto_review_settings.AutoReviewSettings] = None) -> None:
        """
        Sets the autoReviewSettings property value. Detailed settings for how the feature should set the review decision. For use when auto-apply is enabled.
        Args:
            value: Value to set for the autoReviewSettings property.
        """
        self._auto_review_settings = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessReviewSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether showing recommendations to reviewers is enabled.
        self._access_recommendations_enabled: Optional[bool] = None
        # The number of days of user activities to show to reviewers.
        self._activity_duration_in_days: Optional[int] = None
        # Indicates whether the auto-apply capability, to automatically change the target object access resource, is enabled.  If not enabled, a user must, after the review completes, apply the access review.
        self._auto_apply_review_results_enabled: Optional[bool] = None
        # Indicates whether a decision should be set if the reviewer did not supply one. For use when auto-apply is enabled. If you don't want to have a review decision recorded unless the reviewer makes an explicit choice, set it to false.
        self._auto_review_enabled: Optional[bool] = None
        # Detailed settings for how the feature should set the review decision. For use when auto-apply is enabled.
        self._auto_review_settings: Optional[auto_review_settings.AutoReviewSettings] = None
        # Indicates whether reviewers are required to provide a justification when reviewing access.
        self._justification_required_on_approval: Optional[bool] = None
        # Indicates whether sending mails to reviewers and the review creator is enabled.
        self._mail_notifications_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Detailed settings for recurrence.
        self._recurrence_settings: Optional[access_review_recurrence_settings.AccessReviewRecurrenceSettings] = None
        # Indicates whether sending reminder emails to reviewers is enabled.
        self._reminders_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_recommendations_enabled": lambda n : setattr(self, 'access_recommendations_enabled', n.get_bool_value()),
            "activity_duration_in_days": lambda n : setattr(self, 'activity_duration_in_days', n.get_int_value()),
            "auto_apply_review_results_enabled": lambda n : setattr(self, 'auto_apply_review_results_enabled', n.get_bool_value()),
            "auto_review_enabled": lambda n : setattr(self, 'auto_review_enabled', n.get_bool_value()),
            "auto_review_settings": lambda n : setattr(self, 'auto_review_settings', n.get_object_value(auto_review_settings.AutoReviewSettings)),
            "justification_required_on_approval": lambda n : setattr(self, 'justification_required_on_approval', n.get_bool_value()),
            "mail_notifications_enabled": lambda n : setattr(self, 'mail_notifications_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrence_settings": lambda n : setattr(self, 'recurrence_settings', n.get_object_value(access_review_recurrence_settings.AccessReviewRecurrenceSettings)),
            "reminders_enabled": lambda n : setattr(self, 'reminders_enabled', n.get_bool_value()),
        }
        return fields
    
    @property
    def justification_required_on_approval(self,) -> Optional[bool]:
        """
        Gets the justificationRequiredOnApproval property value. Indicates whether reviewers are required to provide a justification when reviewing access.
        Returns: Optional[bool]
        """
        return self._justification_required_on_approval
    
    @justification_required_on_approval.setter
    def justification_required_on_approval(self,value: Optional[bool] = None) -> None:
        """
        Sets the justificationRequiredOnApproval property value. Indicates whether reviewers are required to provide a justification when reviewing access.
        Args:
            value: Value to set for the justificationRequiredOnApproval property.
        """
        self._justification_required_on_approval = value
    
    @property
    def mail_notifications_enabled(self,) -> Optional[bool]:
        """
        Gets the mailNotificationsEnabled property value. Indicates whether sending mails to reviewers and the review creator is enabled.
        Returns: Optional[bool]
        """
        return self._mail_notifications_enabled
    
    @mail_notifications_enabled.setter
    def mail_notifications_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the mailNotificationsEnabled property value. Indicates whether sending mails to reviewers and the review creator is enabled.
        Args:
            value: Value to set for the mailNotificationsEnabled property.
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def recurrence_settings(self,) -> Optional[access_review_recurrence_settings.AccessReviewRecurrenceSettings]:
        """
        Gets the recurrenceSettings property value. Detailed settings for recurrence.
        Returns: Optional[access_review_recurrence_settings.AccessReviewRecurrenceSettings]
        """
        return self._recurrence_settings
    
    @recurrence_settings.setter
    def recurrence_settings(self,value: Optional[access_review_recurrence_settings.AccessReviewRecurrenceSettings] = None) -> None:
        """
        Sets the recurrenceSettings property value. Detailed settings for recurrence.
        Args:
            value: Value to set for the recurrenceSettings property.
        """
        self._recurrence_settings = value
    
    @property
    def reminders_enabled(self,) -> Optional[bool]:
        """
        Gets the remindersEnabled property value. Indicates whether sending reminder emails to reviewers is enabled.
        Returns: Optional[bool]
        """
        return self._reminders_enabled
    
    @reminders_enabled.setter
    def reminders_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the remindersEnabled property value. Indicates whether sending reminder emails to reviewers is enabled.
        Args:
            value: Value to set for the remindersEnabled property.
        """
        self._reminders_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("accessRecommendationsEnabled", self.access_recommendations_enabled)
        writer.write_int_value("activityDurationInDays", self.activity_duration_in_days)
        writer.write_bool_value("autoApplyReviewResultsEnabled", self.auto_apply_review_results_enabled)
        writer.write_bool_value("autoReviewEnabled", self.auto_review_enabled)
        writer.write_object_value("autoReviewSettings", self.auto_review_settings)
        writer.write_bool_value("justificationRequiredOnApproval", self.justification_required_on_approval)
        writer.write_bool_value("mailNotificationsEnabled", self.mail_notifications_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("recurrenceSettings", self.recurrence_settings)
        writer.write_bool_value("remindersEnabled", self.reminders_enabled)
        writer.write_additional_data_value(self.additional_data)
    

