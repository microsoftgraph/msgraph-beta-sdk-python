from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UserExperienceAnalyticsAnomalySeverityOverview(AdditionalDataHolder, Parsable):
    """
    The user experience analytics anomaly severity overview entity contains the count information for each severity of anomaly.
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
        Instantiates a new userExperienceAnalyticsAnomalySeverityOverview and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number of high severity anomalies which have been detected. Valid values -2147483648 to 2147483647
        self._high_severity_anomaly_count: Optional[int] = None
        # The number of informational severity anomalies which have been detected. Valid values -2147483648 to 2147483647
        self._informational_severity_anomaly_count: Optional[int] = None
        # The number of low severity anomalies which have been detected. Valid values -2147483648 to 2147483647
        self._low_severity_anomaly_count: Optional[int] = None
        # The number of medium severity anomalies which have been detected. Valid values -2147483648 to 2147483647
        self._medium_severity_anomaly_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsAnomalySeverityOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAnomalySeverityOverview
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsAnomalySeverityOverview()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "high_severity_anomaly_count": lambda n : setattr(self, 'high_severity_anomaly_count', n.get_int_value()),
            "informational_severity_anomaly_count": lambda n : setattr(self, 'informational_severity_anomaly_count', n.get_int_value()),
            "low_severity_anomaly_count": lambda n : setattr(self, 'low_severity_anomaly_count', n.get_int_value()),
            "medium_severity_anomaly_count": lambda n : setattr(self, 'medium_severity_anomaly_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def high_severity_anomaly_count(self,) -> Optional[int]:
        """
        Gets the highSeverityAnomalyCount property value. The number of high severity anomalies which have been detected. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._high_severity_anomaly_count
    
    @high_severity_anomaly_count.setter
    def high_severity_anomaly_count(self,value: Optional[int] = None) -> None:
        """
        Sets the highSeverityAnomalyCount property value. The number of high severity anomalies which have been detected. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the highSeverityAnomalyCount property.
        """
        self._high_severity_anomaly_count = value
    
    @property
    def informational_severity_anomaly_count(self,) -> Optional[int]:
        """
        Gets the informationalSeverityAnomalyCount property value. The number of informational severity anomalies which have been detected. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._informational_severity_anomaly_count
    
    @informational_severity_anomaly_count.setter
    def informational_severity_anomaly_count(self,value: Optional[int] = None) -> None:
        """
        Sets the informationalSeverityAnomalyCount property value. The number of informational severity anomalies which have been detected. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the informationalSeverityAnomalyCount property.
        """
        self._informational_severity_anomaly_count = value
    
    @property
    def low_severity_anomaly_count(self,) -> Optional[int]:
        """
        Gets the lowSeverityAnomalyCount property value. The number of low severity anomalies which have been detected. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._low_severity_anomaly_count
    
    @low_severity_anomaly_count.setter
    def low_severity_anomaly_count(self,value: Optional[int] = None) -> None:
        """
        Sets the lowSeverityAnomalyCount property value. The number of low severity anomalies which have been detected. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the lowSeverityAnomalyCount property.
        """
        self._low_severity_anomaly_count = value
    
    @property
    def medium_severity_anomaly_count(self,) -> Optional[int]:
        """
        Gets the mediumSeverityAnomalyCount property value. The number of medium severity anomalies which have been detected. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._medium_severity_anomaly_count
    
    @medium_severity_anomaly_count.setter
    def medium_severity_anomaly_count(self,value: Optional[int] = None) -> None:
        """
        Sets the mediumSeverityAnomalyCount property value. The number of medium severity anomalies which have been detected. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the mediumSeverityAnomalyCount property.
        """
        self._medium_severity_anomaly_count = value
    
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
        writer.write_int_value("highSeverityAnomalyCount", self.high_severity_anomaly_count)
        writer.write_int_value("informationalSeverityAnomalyCount", self.informational_severity_anomaly_count)
        writer.write_int_value("lowSeverityAnomalyCount", self.low_severity_anomaly_count)
        writer.write_int_value("mediumSeverityAnomalyCount", self.medium_severity_anomaly_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

