from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delivery_optimization_bandwidth, delivery_optimization_bandwidth_business_hours_limit

from . import delivery_optimization_bandwidth

@dataclass
class DeliveryOptimizationBandwidthHoursWithPercentage(delivery_optimization_bandwidth.DeliveryOptimizationBandwidth):
    odata_type = "#microsoft.graph.deliveryOptimizationBandwidthHoursWithPercentage"
    # Background download percentage hours.
    bandwidth_background_percentage_hours: Optional[delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit] = None
    # Foreground download percentage hours.
    bandwidth_foreground_percentage_hours: Optional[delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeliveryOptimizationBandwidthHoursWithPercentage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationBandwidthHoursWithPercentage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeliveryOptimizationBandwidthHoursWithPercentage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import delivery_optimization_bandwidth, delivery_optimization_bandwidth_business_hours_limit

        from . import delivery_optimization_bandwidth, delivery_optimization_bandwidth_business_hours_limit

        fields: Dict[str, Callable[[Any], None]] = {
            "bandwidthBackgroundPercentageHours": lambda n : setattr(self, 'bandwidth_background_percentage_hours', n.get_object_value(delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit)),
            "bandwidthForegroundPercentageHours": lambda n : setattr(self, 'bandwidth_foreground_percentage_hours', n.get_object_value(delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit)),
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
        writer.write_object_value("bandwidthBackgroundPercentageHours", self.bandwidth_background_percentage_hours)
        writer.write_object_value("bandwidthForegroundPercentageHours", self.bandwidth_foreground_percentage_hours)
    

