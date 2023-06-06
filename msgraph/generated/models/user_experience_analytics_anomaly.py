from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, user_experience_analytics_anomaly_severity, user_experience_analytics_anomaly_state, user_experience_analytics_anomaly_type

from . import entity

@dataclass
class UserExperienceAnalyticsAnomaly(entity.Entity):
    """
    The user experience analytics anomaly entity contains anomaly details.
    """
    # Indicates the first occurrence date and time for the anomaly.
    anomaly_first_occurrence_date_time: Optional[datetime] = None
    # The unique identifier of the anomaly.
    anomaly_id: Optional[str] = None
    # Indicates the latest occurrence date and time for the anomaly.
    anomaly_latest_occurrence_date_time: Optional[datetime] = None
    # The name of the anomaly.
    anomaly_name: Optional[str] = None
    # Indicates the category of the anomaly. Eg: anomaly type can be device, application, stop error, driver or other.
    anomaly_type: Optional[user_experience_analytics_anomaly_type.UserExperienceAnalyticsAnomalyType] = None
    # The name of the application or module that caused the anomaly.
    asset_name: Optional[str] = None
    # The publisher of the application or module that caused the anomaly.
    asset_publisher: Optional[str] = None
    # The version of the application or module that caused the anomaly.
    asset_version: Optional[str] = None
    # The unique identifier of the anomaly detection model.
    detection_model_id: Optional[str] = None
    # The number of devices impacted by the anomaly. Valid values -2147483648 to 2147483647
    device_impacted_count: Optional[int] = None
    # The unique identifier of the anomaly detection model.
    issue_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the severity of the anomaly. Eg: anomaly severity can be high, medium, low, informational or other.
    severity: Optional[user_experience_analytics_anomaly_severity.UserExperienceAnalyticsAnomalySeverity] = None
    # Indicates the state of the anomaly. Eg: anomaly severity can be new, active, disabled, removed or other.
    state: Optional[user_experience_analytics_anomaly_state.UserExperienceAnalyticsAnomalyState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsAnomaly:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAnomaly
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsAnomaly()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, user_experience_analytics_anomaly_severity, user_experience_analytics_anomaly_state, user_experience_analytics_anomaly_type

        fields: Dict[str, Callable[[Any], None]] = {
            "anomalyFirstOccurrenceDateTime": lambda n : setattr(self, 'anomaly_first_occurrence_date_time', n.get_datetime_value()),
            "anomalyId": lambda n : setattr(self, 'anomaly_id', n.get_str_value()),
            "anomalyLatestOccurrenceDateTime": lambda n : setattr(self, 'anomaly_latest_occurrence_date_time', n.get_datetime_value()),
            "anomalyName": lambda n : setattr(self, 'anomaly_name', n.get_str_value()),
            "anomalyType": lambda n : setattr(self, 'anomaly_type', n.get_enum_value(user_experience_analytics_anomaly_type.UserExperienceAnalyticsAnomalyType)),
            "assetName": lambda n : setattr(self, 'asset_name', n.get_str_value()),
            "assetPublisher": lambda n : setattr(self, 'asset_publisher', n.get_str_value()),
            "assetVersion": lambda n : setattr(self, 'asset_version', n.get_str_value()),
            "detectionModelId": lambda n : setattr(self, 'detection_model_id', n.get_str_value()),
            "deviceImpactedCount": lambda n : setattr(self, 'device_impacted_count', n.get_int_value()),
            "issueId": lambda n : setattr(self, 'issue_id', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(user_experience_analytics_anomaly_severity.UserExperienceAnalyticsAnomalySeverity)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(user_experience_analytics_anomaly_state.UserExperienceAnalyticsAnomalyState)),
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
        writer.write_datetime_value("anomalyFirstOccurrenceDateTime", self.anomaly_first_occurrence_date_time)
        writer.write_str_value("anomalyId", self.anomaly_id)
        writer.write_datetime_value("anomalyLatestOccurrenceDateTime", self.anomaly_latest_occurrence_date_time)
        writer.write_str_value("anomalyName", self.anomaly_name)
        writer.write_enum_value("anomalyType", self.anomaly_type)
        writer.write_str_value("assetName", self.asset_name)
        writer.write_str_value("assetPublisher", self.asset_publisher)
        writer.write_str_value("assetVersion", self.asset_version)
        writer.write_str_value("detectionModelId", self.detection_model_id)
        writer.write_int_value("deviceImpactedCount", self.device_impacted_count)
        writer.write_str_value("issueId", self.issue_id)
        writer.write_enum_value("severity", self.severity)
        writer.write_enum_value("state", self.state)
    

