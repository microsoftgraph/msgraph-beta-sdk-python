from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .active_users_metric import ActiveUsersMetric
    from .authentications_metric import AuthenticationsMetric
    from .entity import Entity
    from .insight_summary import InsightSummary
    from .mfa_completion_metric import MfaCompletionMetric
    from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric
    from .monthly_inactive_users_metric import MonthlyInactiveUsersMetric
    from .user_requests_metric import UserRequestsMetric
    from .user_sign_up_metric import UserSignUpMetric

from .entity import Entity

@dataclass
class MonthlyUserInsightMetricsRoot(Entity):
    # Insights for active users on apps registered in the tenant for a specified period.
    active_users: Optional[List[ActiveUsersMetric]] = None
    # Insights for authentications on apps registered in the tenant for a specified period.
    authentications: Optional[List[AuthenticationsMetric]] = None
    # The inactiveUsers property
    inactive_users: Optional[List[MonthlyInactiveUsersMetric]] = None
    # The inactiveUsersByApplication property
    inactive_users_by_application: Optional[List[MonthlyInactiveUsersByApplicationMetric]] = None
    # Insights for MFA usage on apps registered in the tenant for a specified period.
    mfa_completions: Optional[List[MfaCompletionMetric]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Insights for all user requests on apps registered in the tenant for a specified period.
    requests: Optional[List[UserRequestsMetric]] = None
    # Total sign-ups on apps registered in the tenant for a specified period.
    sign_ups: Optional[List[UserSignUpMetric]] = None
    # Summary of all usage insights on apps registered in the tenant for a specified period.
    summary: Optional[List[InsightSummary]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MonthlyUserInsightMetricsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MonthlyUserInsightMetricsRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MonthlyUserInsightMetricsRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .active_users_metric import ActiveUsersMetric
        from .authentications_metric import AuthenticationsMetric
        from .entity import Entity
        from .insight_summary import InsightSummary
        from .mfa_completion_metric import MfaCompletionMetric
        from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric
        from .monthly_inactive_users_metric import MonthlyInactiveUsersMetric
        from .user_requests_metric import UserRequestsMetric
        from .user_sign_up_metric import UserSignUpMetric

        from .active_users_metric import ActiveUsersMetric
        from .authentications_metric import AuthenticationsMetric
        from .entity import Entity
        from .insight_summary import InsightSummary
        from .mfa_completion_metric import MfaCompletionMetric
        from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric
        from .monthly_inactive_users_metric import MonthlyInactiveUsersMetric
        from .user_requests_metric import UserRequestsMetric
        from .user_sign_up_metric import UserSignUpMetric

        fields: Dict[str, Callable[[Any], None]] = {
            "activeUsers": lambda n : setattr(self, 'active_users', n.get_collection_of_object_values(ActiveUsersMetric)),
            "authentications": lambda n : setattr(self, 'authentications', n.get_collection_of_object_values(AuthenticationsMetric)),
            "inactiveUsers": lambda n : setattr(self, 'inactive_users', n.get_collection_of_object_values(MonthlyInactiveUsersMetric)),
            "inactiveUsersByApplication": lambda n : setattr(self, 'inactive_users_by_application', n.get_collection_of_object_values(MonthlyInactiveUsersByApplicationMetric)),
            "mfaCompletions": lambda n : setattr(self, 'mfa_completions', n.get_collection_of_object_values(MfaCompletionMetric)),
            "requests": lambda n : setattr(self, 'requests', n.get_collection_of_object_values(UserRequestsMetric)),
            "signUps": lambda n : setattr(self, 'sign_ups', n.get_collection_of_object_values(UserSignUpMetric)),
            "summary": lambda n : setattr(self, 'summary', n.get_collection_of_object_values(InsightSummary)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("activeUsers", self.active_users)
        writer.write_collection_of_object_values("authentications", self.authentications)
        writer.write_collection_of_object_values("inactiveUsers", self.inactive_users)
        writer.write_collection_of_object_values("inactiveUsersByApplication", self.inactive_users_by_application)
        writer.write_collection_of_object_values("mfaCompletions", self.mfa_completions)
        writer.write_collection_of_object_values("requests", self.requests)
        writer.write_collection_of_object_values("signUps", self.sign_ups)
        writer.write_collection_of_object_values("summary", self.summary)
    

