from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

delivery_optimization_bandwidth = lazy_import('msgraph.generated.models.delivery_optimization_bandwidth')
delivery_optimization_bandwidth_business_hours_limit = lazy_import('msgraph.generated.models.delivery_optimization_bandwidth_business_hours_limit')

class DeliveryOptimizationBandwidthHoursWithPercentage(delivery_optimization_bandwidth.DeliveryOptimizationBandwidth):
    @property
    def bandwidth_background_percentage_hours(self,) -> Optional[delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit]:
        """
        Gets the bandwidthBackgroundPercentageHours property value. Background download percentage hours.
        Returns: Optional[delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit]
        """
        return self._bandwidth_background_percentage_hours
    
    @bandwidth_background_percentage_hours.setter
    def bandwidth_background_percentage_hours(self,value: Optional[delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit] = None) -> None:
        """
        Sets the bandwidthBackgroundPercentageHours property value. Background download percentage hours.
        Args:
            value: Value to set for the bandwidthBackgroundPercentageHours property.
        """
        self._bandwidth_background_percentage_hours = value
    
    @property
    def bandwidth_foreground_percentage_hours(self,) -> Optional[delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit]:
        """
        Gets the bandwidthForegroundPercentageHours property value. Foreground download percentage hours.
        Returns: Optional[delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit]
        """
        return self._bandwidth_foreground_percentage_hours
    
    @bandwidth_foreground_percentage_hours.setter
    def bandwidth_foreground_percentage_hours(self,value: Optional[delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit] = None) -> None:
        """
        Sets the bandwidthForegroundPercentageHours property value. Foreground download percentage hours.
        Args:
            value: Value to set for the bandwidthForegroundPercentageHours property.
        """
        self._bandwidth_foreground_percentage_hours = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeliveryOptimizationBandwidthHoursWithPercentage and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deliveryOptimizationBandwidthHoursWithPercentage"
        # Background download percentage hours.
        self._bandwidth_background_percentage_hours: Optional[delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit] = None
        # Foreground download percentage hours.
        self._bandwidth_foreground_percentage_hours: Optional[delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeliveryOptimizationBandwidthHoursWithPercentage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationBandwidthHoursWithPercentage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeliveryOptimizationBandwidthHoursWithPercentage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bandwidth_background_percentage_hours": lambda n : setattr(self, 'bandwidth_background_percentage_hours', n.get_object_value(delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit)),
            "bandwidth_foreground_percentage_hours": lambda n : setattr(self, 'bandwidth_foreground_percentage_hours', n.get_object_value(delivery_optimization_bandwidth_business_hours_limit.DeliveryOptimizationBandwidthBusinessHoursLimit)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("bandwidthBackgroundPercentageHours", self.bandwidth_background_percentage_hours)
        writer.write_object_value("bandwidthForegroundPercentageHours", self.bandwidth_foreground_percentage_hours)
    

