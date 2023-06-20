from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class UserExperienceAnalyticsMetricHistory(entity.Entity):
    """
    The user experience analytics metric history.
    """
    # The user experience analytics device id.
    device_id: Optional[str] = None
    # The user experience analytics metric date time.
    metric_date_time: Optional[datetime] = None
    # The user experience analytics metric type.
    metric_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsMetricHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsMetricHistory
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsMetricHistory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "metricDateTime": lambda n : setattr(self, 'metric_date_time', n.get_datetime_value()),
            "metricType": lambda n : setattr(self, 'metric_type', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_datetime_value("metricDateTime", self.metric_date_time)
        writer.write_str_value("metricType", self.metric_type)
    

