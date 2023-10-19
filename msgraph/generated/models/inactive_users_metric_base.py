from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .daily_inactive_users_metric import DailyInactiveUsersMetric
    from .entity import Entity
    from .monthly_inactive_users_metric import MonthlyInactiveUsersMetric

from .entity import Entity

@dataclass
class InactiveUsersMetricBase(Entity):
    # The factDate property
    fact_date: Optional[datetime.date] = None
    # The inactive30DayCount property
    inactive30_day_count: Optional[int] = None
    # The inactive60DayCount property
    inactive60_day_count: Optional[int] = None
    # The inactive90DayCount property
    inactive90_day_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InactiveUsersMetricBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InactiveUsersMetricBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dailyInactiveUsersMetric".casefold():
            from .daily_inactive_users_metric import DailyInactiveUsersMetric

            return DailyInactiveUsersMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.monthlyInactiveUsersMetric".casefold():
            from .monthly_inactive_users_metric import MonthlyInactiveUsersMetric

            return MonthlyInactiveUsersMetric()
        return InactiveUsersMetricBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .daily_inactive_users_metric import DailyInactiveUsersMetric
        from .entity import Entity
        from .monthly_inactive_users_metric import MonthlyInactiveUsersMetric

        from .daily_inactive_users_metric import DailyInactiveUsersMetric
        from .entity import Entity
        from .monthly_inactive_users_metric import MonthlyInactiveUsersMetric

        fields: Dict[str, Callable[[Any], None]] = {
            "factDate": lambda n : setattr(self, 'fact_date', n.get_date_value()),
            "inactive30DayCount": lambda n : setattr(self, 'inactive30_day_count', n.get_int_value()),
            "inactive60DayCount": lambda n : setattr(self, 'inactive60_day_count', n.get_int_value()),
            "inactive90DayCount": lambda n : setattr(self, 'inactive90_day_count', n.get_int_value()),
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
        writer.write_date_value("factDate", self.fact_date)
        writer.write_int_value("inactive30DayCount", self.inactive30_day_count)
        writer.write_int_value("inactive60DayCount", self.inactive60_day_count)
        writer.write_int_value("inactive90DayCount", self.inactive90_day_count)
    

