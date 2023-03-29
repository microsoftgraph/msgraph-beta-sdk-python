from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delivery_optimization_bandwidth

from . import delivery_optimization_bandwidth

class DeliveryOptimizationBandwidthPercentage(delivery_optimization_bandwidth.DeliveryOptimizationBandwidth):
    def __init__(self,) -> None:
        """
        Instantiates a new DeliveryOptimizationBandwidthPercentage and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deliveryOptimizationBandwidthPercentage"
        # Specifies the maximum background download bandwidth that Delivery Optimization uses across all concurrent download activities as a percentage of available download bandwidth (0-100). Valid values 0 to 100
        self._maximum_background_bandwidth_percentage: Optional[int] = None
        # Specifies the maximum foreground download bandwidth that Delivery Optimization uses across all concurrent download activities as a percentage of available download bandwidth (0-100). Valid values 0 to 100
        self._maximum_foreground_bandwidth_percentage: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeliveryOptimizationBandwidthPercentage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationBandwidthPercentage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeliveryOptimizationBandwidthPercentage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import delivery_optimization_bandwidth

        fields: Dict[str, Callable[[Any], None]] = {
            "maximumBackgroundBandwidthPercentage": lambda n : setattr(self, 'maximum_background_bandwidth_percentage', n.get_int_value()),
            "maximumForegroundBandwidthPercentage": lambda n : setattr(self, 'maximum_foreground_bandwidth_percentage', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def maximum_background_bandwidth_percentage(self,) -> Optional[int]:
        """
        Gets the maximumBackgroundBandwidthPercentage property value. Specifies the maximum background download bandwidth that Delivery Optimization uses across all concurrent download activities as a percentage of available download bandwidth (0-100). Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._maximum_background_bandwidth_percentage
    
    @maximum_background_bandwidth_percentage.setter
    def maximum_background_bandwidth_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumBackgroundBandwidthPercentage property value. Specifies the maximum background download bandwidth that Delivery Optimization uses across all concurrent download activities as a percentage of available download bandwidth (0-100). Valid values 0 to 100
        Args:
            value: Value to set for the maximum_background_bandwidth_percentage property.
        """
        self._maximum_background_bandwidth_percentage = value
    
    @property
    def maximum_foreground_bandwidth_percentage(self,) -> Optional[int]:
        """
        Gets the maximumForegroundBandwidthPercentage property value. Specifies the maximum foreground download bandwidth that Delivery Optimization uses across all concurrent download activities as a percentage of available download bandwidth (0-100). Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._maximum_foreground_bandwidth_percentage
    
    @maximum_foreground_bandwidth_percentage.setter
    def maximum_foreground_bandwidth_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumForegroundBandwidthPercentage property value. Specifies the maximum foreground download bandwidth that Delivery Optimization uses across all concurrent download activities as a percentage of available download bandwidth (0-100). Valid values 0 to 100
        Args:
            value: Value to set for the maximum_foreground_bandwidth_percentage property.
        """
        self._maximum_foreground_bandwidth_percentage = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("maximumBackgroundBandwidthPercentage", self.maximum_background_bandwidth_percentage)
        writer.write_int_value("maximumForegroundBandwidthPercentage", self.maximum_foreground_bandwidth_percentage)
    

