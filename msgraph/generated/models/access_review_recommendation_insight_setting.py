from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_peer_outlier_recommendation_insight_settings import GroupPeerOutlierRecommendationInsightSettings
    from .user_last_sign_in_recommendation_insight_setting import UserLastSignInRecommendationInsightSetting

@dataclass
class AccessReviewRecommendationInsightSetting(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewRecommendationInsightSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewRecommendationInsightSetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPeerOutlierRecommendationInsightSettings".casefold():
            from .group_peer_outlier_recommendation_insight_settings import GroupPeerOutlierRecommendationInsightSettings

            return GroupPeerOutlierRecommendationInsightSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userLastSignInRecommendationInsightSetting".casefold():
            from .user_last_sign_in_recommendation_insight_setting import UserLastSignInRecommendationInsightSetting

            return UserLastSignInRecommendationInsightSetting()
        return AccessReviewRecommendationInsightSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .group_peer_outlier_recommendation_insight_settings import GroupPeerOutlierRecommendationInsightSettings
        from .user_last_sign_in_recommendation_insight_setting import UserLastSignInRecommendationInsightSetting

        from .group_peer_outlier_recommendation_insight_settings import GroupPeerOutlierRecommendationInsightSettings
        from .user_last_sign_in_recommendation_insight_setting import UserLastSignInRecommendationInsightSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

