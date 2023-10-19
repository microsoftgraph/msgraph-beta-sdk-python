from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .inactive_users_metric_base import InactiveUsersMetricBase

from .inactive_users_metric_base import InactiveUsersMetricBase

@dataclass
class DailyInactiveUsersMetric(InactiveUsersMetricBase):
    # The inactive1DayCount property
    inactive1_day_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DailyInactiveUsersMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DailyInactiveUsersMetric
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DailyInactiveUsersMetric()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .inactive_users_metric_base import InactiveUsersMetricBase

        from .inactive_users_metric_base import InactiveUsersMetricBase

        fields: Dict[str, Callable[[Any], None]] = {
            "inactive1DayCount": lambda n : setattr(self, 'inactive1_day_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("inactive1DayCount", self.inactive1_day_count)
    

