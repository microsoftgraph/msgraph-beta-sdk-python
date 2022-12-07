from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_recommendation_insight_setting = lazy_import('msgraph.generated.models.access_review_recommendation_insight_setting')
user_sign_in_recommendation_scope = lazy_import('msgraph.generated.models.user_sign_in_recommendation_scope')

class UserLastSignInRecommendationInsightSetting(access_review_recommendation_insight_setting.AccessReviewRecommendationInsightSetting):
    def __init__(self,) -> None:
        """
        Instantiates a new UserLastSignInRecommendationInsightSetting and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.userLastSignInRecommendationInsightSetting"
        # Optional. Indicates the time period of inactivity (with respect to the start date of the review instance) that recommendations will be configured from. The recommendation will be to deny if the user is inactive during the look-back duration. For reviews of groups and Azure AD roles, any duration is accepted. For reviews of applications, 30 days is the maximum duration. If not specified, the duration is 30 days.
        self._recommendation_look_back_duration: Optional[Timedelta] = None
        # Indicates whether inactivity is calculated based on the user's inactivity in the tenant or in the application. The possible values are tenant, application, unknownFutureValue. application is only relevant when the access review is a review of an assignment to an application.
        self._sign_in_scope: Optional[user_sign_in_recommendation_scope.UserSignInRecommendationScope] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserLastSignInRecommendationInsightSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserLastSignInRecommendationInsightSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserLastSignInRecommendationInsightSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "recommendation_look_back_duration": lambda n : setattr(self, 'recommendation_look_back_duration', n.get_object_value(Timedelta)),
            "sign_in_scope": lambda n : setattr(self, 'sign_in_scope', n.get_enum_value(user_sign_in_recommendation_scope.UserSignInRecommendationScope)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def recommendation_look_back_duration(self,) -> Optional[Timedelta]:
        """
        Gets the recommendationLookBackDuration property value. Optional. Indicates the time period of inactivity (with respect to the start date of the review instance) that recommendations will be configured from. The recommendation will be to deny if the user is inactive during the look-back duration. For reviews of groups and Azure AD roles, any duration is accepted. For reviews of applications, 30 days is the maximum duration. If not specified, the duration is 30 days.
        Returns: Optional[Timedelta]
        """
        return self._recommendation_look_back_duration
    
    @recommendation_look_back_duration.setter
    def recommendation_look_back_duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the recommendationLookBackDuration property value. Optional. Indicates the time period of inactivity (with respect to the start date of the review instance) that recommendations will be configured from. The recommendation will be to deny if the user is inactive during the look-back duration. For reviews of groups and Azure AD roles, any duration is accepted. For reviews of applications, 30 days is the maximum duration. If not specified, the duration is 30 days.
        Args:
            value: Value to set for the recommendationLookBackDuration property.
        """
        self._recommendation_look_back_duration = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("recommendationLookBackDuration", self.recommendation_look_back_duration)
        writer.write_enum_value("signInScope", self.sign_in_scope)
    
    @property
    def sign_in_scope(self,) -> Optional[user_sign_in_recommendation_scope.UserSignInRecommendationScope]:
        """
        Gets the signInScope property value. Indicates whether inactivity is calculated based on the user's inactivity in the tenant or in the application. The possible values are tenant, application, unknownFutureValue. application is only relevant when the access review is a review of an assignment to an application.
        Returns: Optional[user_sign_in_recommendation_scope.UserSignInRecommendationScope]
        """
        return self._sign_in_scope
    
    @sign_in_scope.setter
    def sign_in_scope(self,value: Optional[user_sign_in_recommendation_scope.UserSignInRecommendationScope] = None) -> None:
        """
        Sets the signInScope property value. Indicates whether inactivity is calculated based on the user's inactivity in the tenant or in the application. The possible values are tenant, application, unknownFutureValue. application is only relevant when the access review is a review of an assignment to an application.
        Args:
            value: Value to set for the signInScope property.
        """
        self._sign_in_scope = value
    

