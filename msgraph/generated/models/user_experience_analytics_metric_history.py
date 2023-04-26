from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class UserExperienceAnalyticsMetricHistory(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new UserExperienceAnalyticsMetricHistory and sets the default values.
        """
        super().__init__()
        # The user experience analytics device id.
        self._device_id: Optional[str] = None
        # The user experience analytics metric date time.
        self._metric_date_time: Optional[datetime] = None
        # The user experience analytics metric type.
        self._metric_type: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsMetricHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsMetricHistory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsMetricHistory()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The user experience analytics device id.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The user experience analytics device id.
        Args:
            value: Value to set for the device_id property.
        """
        self._device_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "metricDateTime": lambda n : setattr(self, 'metric_date_time', n.get_datetime_value()),
            "metricType": lambda n : setattr(self, 'metric_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def metric_date_time(self,) -> Optional[datetime]:
        """
        Gets the metricDateTime property value. The user experience analytics metric date time.
        Returns: Optional[datetime]
        """
        return self._metric_date_time
    
    @metric_date_time.setter
    def metric_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the metricDateTime property value. The user experience analytics metric date time.
        Args:
            value: Value to set for the metric_date_time property.
        """
        self._metric_date_time = value
    
    @property
    def metric_type(self,) -> Optional[str]:
        """
        Gets the metricType property value. The user experience analytics metric type.
        Returns: Optional[str]
        """
        return self._metric_type
    
    @metric_type.setter
    def metric_type(self,value: Optional[str] = None) -> None:
        """
        Sets the metricType property value. The user experience analytics metric type.
        Args:
            value: Value to set for the metric_type property.
        """
        self._metric_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_datetime_value("metricDateTime", self.metric_date_time)
        writer.write_str_value("metricType", self.metric_type)
    

