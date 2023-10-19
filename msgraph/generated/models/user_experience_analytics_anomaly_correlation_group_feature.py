from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_experience_analytics_anomaly_device_feature_type import UserExperienceAnalyticsAnomalyDeviceFeatureType

@dataclass
class UserExperienceAnalyticsAnomalyCorrelationGroupFeature(AdditionalDataHolder, BackedModel, Parsable):
    """
    Describes the features of a device that are shared between all devices in a correlation group.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates the device's feature type. Possible values are: manufacturer, model, osVersion, application or driver.
    device_feature_type: Optional[UserExperienceAnalyticsAnomalyDeviceFeatureType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specific metric values that describe the features of the given device feature type.
    values: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsAnomalyCorrelationGroupFeature:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAnomalyCorrelationGroupFeature
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsAnomalyCorrelationGroupFeature()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .user_experience_analytics_anomaly_device_feature_type import UserExperienceAnalyticsAnomalyDeviceFeatureType

        from .user_experience_analytics_anomaly_device_feature_type import UserExperienceAnalyticsAnomalyDeviceFeatureType

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceFeatureType": lambda n : setattr(self, 'device_feature_type', n.get_enum_value(UserExperienceAnalyticsAnomalyDeviceFeatureType)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_collection_of_primitive_values(str)),
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
        writer.write_enum_value("deviceFeatureType", self.device_feature_type)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_collection_of_primitive_values("values", self.values)
        writer.write_additional_data_value(self.additional_data)
    

