from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import user_experience_analytics_insight_severity, user_experience_analytics_insight_value

@dataclass
class UserExperienceAnalyticsInsight(AdditionalDataHolder, Parsable):
    """
    The user experience analytics insight is the recomendation to improve the user experience analytics score.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The unique identifier of the user experience analytics insight.
    insight_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates severity of insights. Possible values are: None, Informational, Warning, Error.
    severity: Optional[user_experience_analytics_insight_severity.UserExperienceAnalyticsInsightSeverity] = None
    # The unique identifier of the user experience analytics insight.
    user_experience_analytics_metric_id: Optional[str] = None
    # The value of the user experience analytics insight.
    values: Optional[List[user_experience_analytics_insight_value.UserExperienceAnalyticsInsightValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsInsight
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsInsight()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import user_experience_analytics_insight_severity, user_experience_analytics_insight_value

        from . import user_experience_analytics_insight_severity, user_experience_analytics_insight_value

        fields: Dict[str, Callable[[Any], None]] = {
            "insightId": lambda n : setattr(self, 'insight_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(user_experience_analytics_insight_severity.UserExperienceAnalyticsInsightSeverity)),
            "userExperienceAnalyticsMetricId": lambda n : setattr(self, 'user_experience_analytics_metric_id', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_collection_of_object_values(user_experience_analytics_insight_value.UserExperienceAnalyticsInsightValue)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("insightId", self.insight_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("severity", self.severity)
        writer.write_str_value("userExperienceAnalyticsMetricId", self.user_experience_analytics_metric_id)
        writer.write_collection_of_object_values("values", self.values)
        writer.write_additional_data_value(self.additional_data)
    

