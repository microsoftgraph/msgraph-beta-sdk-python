from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

delivery_optimization_max_cache_size = lazy_import('msgraph.generated.models.delivery_optimization_max_cache_size')

class DeliveryOptimizationMaxCacheSizePercentage(delivery_optimization_max_cache_size.DeliveryOptimizationMaxCacheSize):
    def __init__(self,) -> None:
        """
        Instantiates a new DeliveryOptimizationMaxCacheSizePercentage and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deliveryOptimizationMaxCacheSizePercentage"
        # Specifies the maximum cache size that Delivery Optimization can utilize, as a percentage of disk size (1-100). Valid values 1 to 100
        self._maximum_cache_size_percentage: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeliveryOptimizationMaxCacheSizePercentage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationMaxCacheSizePercentage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeliveryOptimizationMaxCacheSizePercentage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "maximum_cache_size_percentage": lambda n : setattr(self, 'maximum_cache_size_percentage', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def maximum_cache_size_percentage(self,) -> Optional[int]:
        """
        Gets the maximumCacheSizePercentage property value. Specifies the maximum cache size that Delivery Optimization can utilize, as a percentage of disk size (1-100). Valid values 1 to 100
        Returns: Optional[int]
        """
        return self._maximum_cache_size_percentage
    
    @maximum_cache_size_percentage.setter
    def maximum_cache_size_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumCacheSizePercentage property value. Specifies the maximum cache size that Delivery Optimization can utilize, as a percentage of disk size (1-100). Valid values 1 to 100
        Args:
            value: Value to set for the maximumCacheSizePercentage property.
        """
        self._maximum_cache_size_percentage = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("maximumCacheSizePercentage", self.maximum_cache_size_percentage)
    

