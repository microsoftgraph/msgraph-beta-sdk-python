from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user_experience_analytics_insight = lazy_import('msgraph.generated.models.user_experience_analytics_insight')

class UserExperienceAnalyticsOverview(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsOverview and sets the default values.
        """
        super().__init__()
        # The user experience analytics insights.
        self._insights: Optional[List[user_experience_analytics_insight.UserExperienceAnalyticsInsight]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsOverview
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsOverview()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "insights": lambda n : setattr(self, 'insights', n.get_collection_of_object_values(user_experience_analytics_insight.UserExperienceAnalyticsInsight)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def insights(self,) -> Optional[List[user_experience_analytics_insight.UserExperienceAnalyticsInsight]]:
        """
        Gets the insights property value. The user experience analytics insights.
        Returns: Optional[List[user_experience_analytics_insight.UserExperienceAnalyticsInsight]]
        """
        return self._insights
    
    @insights.setter
    def insights(self,value: Optional[List[user_experience_analytics_insight.UserExperienceAnalyticsInsight]] = None) -> None:
        """
        Sets the insights property value. The user experience analytics insights.
        Args:
            value: Value to set for the insights property.
        """
        self._insights = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("insights", self.insights)
    

