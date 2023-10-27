from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .daily_user_insight_metrics_root import DailyUserInsightMetricsRoot
    from .entity import Entity
    from .monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot

from .entity import Entity

@dataclass
class UserInsightsRoot(Entity):
    # The daily property
    daily: Optional[DailyUserInsightMetricsRoot] = None
    # The monthly property
    monthly: Optional[MonthlyUserInsightMetricsRoot] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserInsightsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserInsightsRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserInsightsRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .daily_user_insight_metrics_root import DailyUserInsightMetricsRoot
        from .entity import Entity
        from .monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot

        from .daily_user_insight_metrics_root import DailyUserInsightMetricsRoot
        from .entity import Entity
        from .monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot

        fields: Dict[str, Callable[[Any], None]] = {
            "daily": lambda n : setattr(self, 'daily', n.get_object_value(DailyUserInsightMetricsRoot)),
            "monthly": lambda n : setattr(self, 'monthly', n.get_object_value(MonthlyUserInsightMetricsRoot)),
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
        writer.write_object_value("daily", self.daily)
        writer.write_object_value("monthly", self.monthly)
    

