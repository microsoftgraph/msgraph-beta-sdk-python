from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class UserExperienceAnalyticsAnomalySeverityOverview(AdditionalDataHolder, BackedModel, Parsable):
    """
    The user experience analytics anomaly severity overview entity contains the count information for each severity of anomaly.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates count of high severity anomalies which have been detected. Valid values -2147483648 to 2147483647
    high_severity_anomaly_count: Optional[int] = None
    # Indicates count of informational severity anomalies which have been detected. Valid values -2147483648 to 2147483647
    informational_severity_anomaly_count: Optional[int] = None
    # Indicates count of low severity anomalies which have been detected. Valid values -2147483648 to 2147483647
    low_severity_anomaly_count: Optional[int] = None
    # Indicates count of medium severity anomalies which have been detected. Valid values -2147483648 to 2147483647
    medium_severity_anomaly_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsAnomalySeverityOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAnomalySeverityOverview
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsAnomalySeverityOverview()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "highSeverityAnomalyCount": lambda n : setattr(self, 'high_severity_anomaly_count', n.get_int_value()),
            "informationalSeverityAnomalyCount": lambda n : setattr(self, 'informational_severity_anomaly_count', n.get_int_value()),
            "lowSeverityAnomalyCount": lambda n : setattr(self, 'low_severity_anomaly_count', n.get_int_value()),
            "mediumSeverityAnomalyCount": lambda n : setattr(self, 'medium_severity_anomaly_count', n.get_int_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("highSeverityAnomalyCount", self.high_severity_anomaly_count)
        writer.write_int_value("informationalSeverityAnomalyCount", self.informational_severity_anomaly_count)
        writer.write_int_value("lowSeverityAnomalyCount", self.low_severity_anomaly_count)
        writer.write_int_value("mediumSeverityAnomalyCount", self.medium_severity_anomaly_count)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

