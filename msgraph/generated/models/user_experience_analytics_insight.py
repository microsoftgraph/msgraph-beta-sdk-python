from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

user_experience_analytics_insight_severity = lazy_import('msgraph.generated.models.user_experience_analytics_insight_severity')
user_experience_analytics_insight_value = lazy_import('msgraph.generated.models.user_experience_analytics_insight_value')

class UserExperienceAnalyticsInsight(AdditionalDataHolder, Parsable):
    """
    The user experience analytics insight is the recomendation to improve the user experience analytics score.
    """
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
        Instantiates a new userExperienceAnalyticsInsight and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The unique identifier of the user experience analytics insight.
        self._insight_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The severity property
        self._severity: Optional[user_experience_analytics_insight_severity.UserExperienceAnalyticsInsightSeverity] = None
        # The unique identifier of the user experience analytics insight.
        self._user_experience_analytics_metric_id: Optional[str] = None
        # The value of the user experience analytics insight.
        self._values: Optional[List[user_experience_analytics_insight_value.UserExperienceAnalyticsInsightValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsInsight
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsInsight()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "insight_id": lambda n : setattr(self, 'insight_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(user_experience_analytics_insight_severity.UserExperienceAnalyticsInsightSeverity)),
            "user_experience_analytics_metric_id": lambda n : setattr(self, 'user_experience_analytics_metric_id', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_collection_of_object_values(user_experience_analytics_insight_value.UserExperienceAnalyticsInsightValue)),
        }
        return fields
    
    @property
    def insight_id(self,) -> Optional[str]:
        """
        Gets the insightId property value. The unique identifier of the user experience analytics insight.
        Returns: Optional[str]
        """
        return self._insight_id
    
    @insight_id.setter
    def insight_id(self,value: Optional[str] = None) -> None:
        """
        Sets the insightId property value. The unique identifier of the user experience analytics insight.
        Args:
            value: Value to set for the insightId property.
        """
        self._insight_id = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("insightId", self.insight_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("severity", self.severity)
        writer.write_str_value("userExperienceAnalyticsMetricId", self.user_experience_analytics_metric_id)
        writer.write_collection_of_object_values("values", self.values)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def severity(self,) -> Optional[user_experience_analytics_insight_severity.UserExperienceAnalyticsInsightSeverity]:
        """
        Gets the severity property value. The severity property
        Returns: Optional[user_experience_analytics_insight_severity.UserExperienceAnalyticsInsightSeverity]
        """
        return self._severity
    
    @severity.setter
    def severity(self,value: Optional[user_experience_analytics_insight_severity.UserExperienceAnalyticsInsightSeverity] = None) -> None:
        """
        Sets the severity property value. The severity property
        Args:
            value: Value to set for the severity property.
        """
        self._severity = value
    
    @property
    def user_experience_analytics_metric_id(self,) -> Optional[str]:
        """
        Gets the userExperienceAnalyticsMetricId property value. The unique identifier of the user experience analytics insight.
        Returns: Optional[str]
        """
        return self._user_experience_analytics_metric_id
    
    @user_experience_analytics_metric_id.setter
    def user_experience_analytics_metric_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userExperienceAnalyticsMetricId property value. The unique identifier of the user experience analytics insight.
        Args:
            value: Value to set for the userExperienceAnalyticsMetricId property.
        """
        self._user_experience_analytics_metric_id = value
    
    @property
    def values(self,) -> Optional[List[user_experience_analytics_insight_value.UserExperienceAnalyticsInsightValue]]:
        """
        Gets the values property value. The value of the user experience analytics insight.
        Returns: Optional[List[user_experience_analytics_insight_value.UserExperienceAnalyticsInsightValue]]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[List[user_experience_analytics_insight_value.UserExperienceAnalyticsInsightValue]] = None) -> None:
        """
        Sets the values property value. The value of the user experience analytics insight.
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    

