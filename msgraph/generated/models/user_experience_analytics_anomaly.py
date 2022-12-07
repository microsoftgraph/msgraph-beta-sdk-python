from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user_experience_analytics_anomaly_severity = lazy_import('msgraph.generated.models.user_experience_analytics_anomaly_severity')
user_experience_analytics_anomaly_state = lazy_import('msgraph.generated.models.user_experience_analytics_anomaly_state')
user_experience_analytics_anomaly_type = lazy_import('msgraph.generated.models.user_experience_analytics_anomaly_type')

class UserExperienceAnalyticsAnomaly(entity.Entity):
    """
    The user experience analytics anomaly entity contains anomaly details.
    """
    @property
    def anomaly_first_occurrence_date_time(self,) -> Optional[datetime]:
        """
        Gets the anomalyFirstOccurrenceDateTime property value. Indicates the first occurrence date and time for the anomaly.
        Returns: Optional[datetime]
        """
        return self._anomaly_first_occurrence_date_time
    
    @anomaly_first_occurrence_date_time.setter
    def anomaly_first_occurrence_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the anomalyFirstOccurrenceDateTime property value. Indicates the first occurrence date and time for the anomaly.
        Args:
            value: Value to set for the anomalyFirstOccurrenceDateTime property.
        """
        self._anomaly_first_occurrence_date_time = value
    
    @property
    def anomaly_id(self,) -> Optional[str]:
        """
        Gets the anomalyId property value. The unique identifier of the anomaly.
        Returns: Optional[str]
        """
        return self._anomaly_id
    
    @anomaly_id.setter
    def anomaly_id(self,value: Optional[str] = None) -> None:
        """
        Sets the anomalyId property value. The unique identifier of the anomaly.
        Args:
            value: Value to set for the anomalyId property.
        """
        self._anomaly_id = value
    
    @property
    def anomaly_latest_occurrence_date_time(self,) -> Optional[datetime]:
        """
        Gets the anomalyLatestOccurrenceDateTime property value. Indicates the latest occurrence date and time for the anomaly.
        Returns: Optional[datetime]
        """
        return self._anomaly_latest_occurrence_date_time
    
    @anomaly_latest_occurrence_date_time.setter
    def anomaly_latest_occurrence_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the anomalyLatestOccurrenceDateTime property value. Indicates the latest occurrence date and time for the anomaly.
        Args:
            value: Value to set for the anomalyLatestOccurrenceDateTime property.
        """
        self._anomaly_latest_occurrence_date_time = value
    
    @property
    def anomaly_name(self,) -> Optional[str]:
        """
        Gets the anomalyName property value. The name of the anomaly.
        Returns: Optional[str]
        """
        return self._anomaly_name
    
    @anomaly_name.setter
    def anomaly_name(self,value: Optional[str] = None) -> None:
        """
        Sets the anomalyName property value. The name of the anomaly.
        Args:
            value: Value to set for the anomalyName property.
        """
        self._anomaly_name = value
    
    @property
    def anomaly_type(self,) -> Optional[user_experience_analytics_anomaly_type.UserExperienceAnalyticsAnomalyType]:
        """
        Gets the anomalyType property value. Indicates the category of the anomaly. Eg: anomaly type can be device, application, stop error, driver or other.
        Returns: Optional[user_experience_analytics_anomaly_type.UserExperienceAnalyticsAnomalyType]
        """
        return self._anomaly_type
    
    @anomaly_type.setter
    def anomaly_type(self,value: Optional[user_experience_analytics_anomaly_type.UserExperienceAnalyticsAnomalyType] = None) -> None:
        """
        Sets the anomalyType property value. Indicates the category of the anomaly. Eg: anomaly type can be device, application, stop error, driver or other.
        Args:
            value: Value to set for the anomalyType property.
        """
        self._anomaly_type = value
    
    @property
    def asset_name(self,) -> Optional[str]:
        """
        Gets the assetName property value. The name of the application or module that caused the anomaly.
        Returns: Optional[str]
        """
        return self._asset_name
    
    @asset_name.setter
    def asset_name(self,value: Optional[str] = None) -> None:
        """
        Sets the assetName property value. The name of the application or module that caused the anomaly.
        Args:
            value: Value to set for the assetName property.
        """
        self._asset_name = value
    
    @property
    def asset_publisher(self,) -> Optional[str]:
        """
        Gets the assetPublisher property value. The publisher of the application or module that caused the anomaly.
        Returns: Optional[str]
        """
        return self._asset_publisher
    
    @asset_publisher.setter
    def asset_publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the assetPublisher property value. The publisher of the application or module that caused the anomaly.
        Args:
            value: Value to set for the assetPublisher property.
        """
        self._asset_publisher = value
    
    @property
    def asset_version(self,) -> Optional[str]:
        """
        Gets the assetVersion property value. The version of the application or module that caused the anomaly.
        Returns: Optional[str]
        """
        return self._asset_version
    
    @asset_version.setter
    def asset_version(self,value: Optional[str] = None) -> None:
        """
        Sets the assetVersion property value. The version of the application or module that caused the anomaly.
        Args:
            value: Value to set for the assetVersion property.
        """
        self._asset_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsAnomaly and sets the default values.
        """
        super().__init__()
        # Indicates the first occurrence date and time for the anomaly.
        self._anomaly_first_occurrence_date_time: Optional[datetime] = None
        # The unique identifier of the anomaly.
        self._anomaly_id: Optional[str] = None
        # Indicates the latest occurrence date and time for the anomaly.
        self._anomaly_latest_occurrence_date_time: Optional[datetime] = None
        # The name of the anomaly.
        self._anomaly_name: Optional[str] = None
        # Indicates the category of the anomaly. Eg: anomaly type can be device, application, stop error, driver or other.
        self._anomaly_type: Optional[user_experience_analytics_anomaly_type.UserExperienceAnalyticsAnomalyType] = None
        # The name of the application or module that caused the anomaly.
        self._asset_name: Optional[str] = None
        # The publisher of the application or module that caused the anomaly.
        self._asset_publisher: Optional[str] = None
        # The version of the application or module that caused the anomaly.
        self._asset_version: Optional[str] = None
        # The unique identifier of the anomaly detection model.
        self._detection_model_id: Optional[str] = None
        # The number of devices impacted by the anomaly. Valid values -2147483648 to 2147483647
        self._device_impacted_count: Optional[int] = None
        # The unique identifier of the anomaly detection model.
        self._issue_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates the severity of the anomaly. Eg: anomaly severity can be high, medium, low, informational or other.
        self._severity: Optional[user_experience_analytics_anomaly_severity.UserExperienceAnalyticsAnomalySeverity] = None
        # Indicates the state of the anomaly. Eg: anomaly severity can be new, active, disabled, removed or other.
        self._state: Optional[user_experience_analytics_anomaly_state.UserExperienceAnalyticsAnomalyState] = None
    
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
    
    @property
    def detection_model_id(self,) -> Optional[str]:
        """
        Gets the detectionModelId property value. The unique identifier of the anomaly detection model.
        Returns: Optional[str]
        """
        return self._detection_model_id
    
    @detection_model_id.setter
    def detection_model_id(self,value: Optional[str] = None) -> None:
        """
        Sets the detectionModelId property value. The unique identifier of the anomaly detection model.
        Args:
            value: Value to set for the detectionModelId property.
        """
        self._detection_model_id = value
    
    @property
    def device_impacted_count(self,) -> Optional[int]:
        """
        Gets the deviceImpactedCount property value. The number of devices impacted by the anomaly. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._device_impacted_count
    
    @device_impacted_count.setter
    def device_impacted_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceImpactedCount property value. The number of devices impacted by the anomaly. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the deviceImpactedCount property.
        """
        self._device_impacted_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "anomaly_first_occurrence_date_time": lambda n : setattr(self, 'anomaly_first_occurrence_date_time', n.get_datetime_value()),
            "anomaly_id": lambda n : setattr(self, 'anomaly_id', n.get_str_value()),
            "anomaly_latest_occurrence_date_time": lambda n : setattr(self, 'anomaly_latest_occurrence_date_time', n.get_datetime_value()),
            "anomaly_name": lambda n : setattr(self, 'anomaly_name', n.get_str_value()),
            "anomaly_type": lambda n : setattr(self, 'anomaly_type', n.get_enum_value(user_experience_analytics_anomaly_type.UserExperienceAnalyticsAnomalyType)),
            "asset_name": lambda n : setattr(self, 'asset_name', n.get_str_value()),
            "asset_publisher": lambda n : setattr(self, 'asset_publisher', n.get_str_value()),
            "asset_version": lambda n : setattr(self, 'asset_version', n.get_str_value()),
            "detection_model_id": lambda n : setattr(self, 'detection_model_id', n.get_str_value()),
            "device_impacted_count": lambda n : setattr(self, 'device_impacted_count', n.get_int_value()),
            "issue_id": lambda n : setattr(self, 'issue_id', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(user_experience_analytics_anomaly_severity.UserExperienceAnalyticsAnomalySeverity)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(user_experience_analytics_anomaly_state.UserExperienceAnalyticsAnomalyState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def issue_id(self,) -> Optional[str]:
        """
        Gets the issueId property value. The unique identifier of the anomaly detection model.
        Returns: Optional[str]
        """
        return self._issue_id
    
    @issue_id.setter
    def issue_id(self,value: Optional[str] = None) -> None:
        """
        Sets the issueId property value. The unique identifier of the anomaly detection model.
        Args:
            value: Value to set for the issueId property.
        """
        self._issue_id = value
    
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
    
    @property
    def severity(self,) -> Optional[user_experience_analytics_anomaly_severity.UserExperienceAnalyticsAnomalySeverity]:
        """
        Gets the severity property value. Indicates the severity of the anomaly. Eg: anomaly severity can be high, medium, low, informational or other.
        Returns: Optional[user_experience_analytics_anomaly_severity.UserExperienceAnalyticsAnomalySeverity]
        """
        return self._severity
    
    @severity.setter
    def severity(self,value: Optional[user_experience_analytics_anomaly_severity.UserExperienceAnalyticsAnomalySeverity] = None) -> None:
        """
        Sets the severity property value. Indicates the severity of the anomaly. Eg: anomaly severity can be high, medium, low, informational or other.
        Args:
            value: Value to set for the severity property.
        """
        self._severity = value
    
    @property
    def state(self,) -> Optional[user_experience_analytics_anomaly_state.UserExperienceAnalyticsAnomalyState]:
        """
        Gets the state property value. Indicates the state of the anomaly. Eg: anomaly severity can be new, active, disabled, removed or other.
        Returns: Optional[user_experience_analytics_anomaly_state.UserExperienceAnalyticsAnomalyState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[user_experience_analytics_anomaly_state.UserExperienceAnalyticsAnomalyState] = None) -> None:
        """
        Sets the state property value. Indicates the state of the anomaly. Eg: anomaly severity can be new, active, disabled, removed or other.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

