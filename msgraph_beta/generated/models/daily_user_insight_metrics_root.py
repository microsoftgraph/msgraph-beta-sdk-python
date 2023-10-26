from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .active_users_breakdown_metric import ActiveUsersBreakdownMetric
    from .active_users_metric import ActiveUsersMetric
    from .authentications_metric import AuthenticationsMetric
    from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
    from .daily_inactive_users_metric import DailyInactiveUsersMetric
    from .entity import Entity
    from .insight_summary import InsightSummary
    from .mfa_completion_metric import MfaCompletionMetric
    from .user_count_metric import UserCountMetric
    from .user_sign_up_metric import UserSignUpMetric

from .entity import Entity

@dataclass
class DailyUserInsightMetricsRoot(Entity):
    # The activeUsers property
    active_users: Optional[List[ActiveUsersMetric]] = None
    # The activeUsersBreakdown property
    active_users_breakdown: Optional[List[ActiveUsersBreakdownMetric]] = None
    # The authentications property
    authentications: Optional[List[AuthenticationsMetric]] = None
    # The inactiveUsers property
    inactive_users: Optional[List[DailyInactiveUsersMetric]] = None
    # The inactiveUsersByApplication property
    inactive_users_by_application: Optional[List[DailyInactiveUsersByApplicationMetric]] = None
    # The mfaCompletions property
    mfa_completions: Optional[List[MfaCompletionMetric]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The signUps property
    sign_ups: Optional[List[UserSignUpMetric]] = None
    # The summary property
    summary: Optional[List[InsightSummary]] = None
    # The userCount property
    user_count: Optional[List[UserCountMetric]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DailyUserInsightMetricsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DailyUserInsightMetricsRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DailyUserInsightMetricsRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .active_users_breakdown_metric import ActiveUsersBreakdownMetric
        from .active_users_metric import ActiveUsersMetric
        from .authentications_metric import AuthenticationsMetric
        from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
        from .daily_inactive_users_metric import DailyInactiveUsersMetric
        from .entity import Entity
        from .insight_summary import InsightSummary
        from .mfa_completion_metric import MfaCompletionMetric
        from .user_count_metric import UserCountMetric
        from .user_sign_up_metric import UserSignUpMetric

        from .active_users_breakdown_metric import ActiveUsersBreakdownMetric
        from .active_users_metric import ActiveUsersMetric
        from .authentications_metric import AuthenticationsMetric
        from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
        from .daily_inactive_users_metric import DailyInactiveUsersMetric
        from .entity import Entity
        from .insight_summary import InsightSummary
        from .mfa_completion_metric import MfaCompletionMetric
        from .user_count_metric import UserCountMetric
        from .user_sign_up_metric import UserSignUpMetric

        fields: Dict[str, Callable[[Any], None]] = {
            "activeUsers": lambda n : setattr(self, 'active_users', n.get_collection_of_object_values(ActiveUsersMetric)),
            "activeUsersBreakdown": lambda n : setattr(self, 'active_users_breakdown', n.get_collection_of_object_values(ActiveUsersBreakdownMetric)),
            "authentications": lambda n : setattr(self, 'authentications', n.get_collection_of_object_values(AuthenticationsMetric)),
            "inactiveUsers": lambda n : setattr(self, 'inactive_users', n.get_collection_of_object_values(DailyInactiveUsersMetric)),
            "inactiveUsersByApplication": lambda n : setattr(self, 'inactive_users_by_application', n.get_collection_of_object_values(DailyInactiveUsersByApplicationMetric)),
            "mfaCompletions": lambda n : setattr(self, 'mfa_completions', n.get_collection_of_object_values(MfaCompletionMetric)),
            "signUps": lambda n : setattr(self, 'sign_ups', n.get_collection_of_object_values(UserSignUpMetric)),
            "summary": lambda n : setattr(self, 'summary', n.get_collection_of_object_values(InsightSummary)),
            "userCount": lambda n : setattr(self, 'user_count', n.get_collection_of_object_values(UserCountMetric)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("activeUsers", self.active_users)
        writer.write_collection_of_object_values("activeUsersBreakdown", self.active_users_breakdown)
        writer.write_collection_of_object_values("authentications", self.authentications)
        writer.write_collection_of_object_values("inactiveUsers", self.inactive_users)
        writer.write_collection_of_object_values("inactiveUsersByApplication", self.inactive_users_by_application)
        writer.write_collection_of_object_values("mfaCompletions", self.mfa_completions)
        writer.write_collection_of_object_values("signUps", self.sign_ups)
        writer.write_collection_of_object_values("summary", self.summary)
        writer.write_collection_of_object_values("userCount", self.user_count)
    

