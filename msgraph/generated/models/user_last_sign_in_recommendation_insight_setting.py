from __future__ import annotations
from dataclasses import dataclass, field
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_recommendation_insight_setting, user_sign_in_recommendation_scope

from . import access_review_recommendation_insight_setting

@dataclass
class UserLastSignInRecommendationInsightSetting(access_review_recommendation_insight_setting.AccessReviewRecommendationInsightSetting):
    odata_type = "#microsoft.graph.userLastSignInRecommendationInsightSetting"
    # Optional. Indicates the time period of inactivity (with respect to the start date of the review instance) that recommendations will be configured from. The recommendation will be to deny if the user is inactive during the look-back duration. For reviews of groups and Azure AD roles, any duration is accepted. For reviews of applications, 30 days is the maximum duration. If not specified, the duration is 30 days.
    recommendation_look_back_duration: Optional[timedelta] = None
    # Indicates whether inactivity is calculated based on the user's inactivity in the tenant or in the application. The possible values are tenant, application, unknownFutureValue. application is only relevant when the access review is a review of an assignment to an application.
    sign_in_scope: Optional[user_sign_in_recommendation_scope.UserSignInRecommendationScope] = None
    
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
        from . import access_review_recommendation_insight_setting, user_sign_in_recommendation_scope

        fields: Dict[str, Callable[[Any], None]] = {
            "recommendationLookBackDuration": lambda n : setattr(self, 'recommendation_look_back_duration', n.get_timedelta_value()),
            "signInScope": lambda n : setattr(self, 'sign_in_scope', n.get_enum_value(user_sign_in_recommendation_scope.UserSignInRecommendationScope)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_timedelta_value("recommendationLookBackDuration", self.recommendation_look_back_duration)
        writer.write_enum_value("signInScope", self.sign_in_scope)
    

