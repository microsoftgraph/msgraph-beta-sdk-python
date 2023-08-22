from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delivery_optimization_max_cache_size import DeliveryOptimizationMaxCacheSize

from .delivery_optimization_max_cache_size import DeliveryOptimizationMaxCacheSize

@dataclass
class DeliveryOptimizationMaxCacheSizeAbsolute(DeliveryOptimizationMaxCacheSize):
    """
    Delivery Optimization max cache size absolute type.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deliveryOptimizationMaxCacheSizeAbsolute"
    # Specifies the maximum size in GB of Delivery Optimization cache. Valid values 0 to 4294967295
    maximum_cache_size_in_gigabytes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeliveryOptimizationMaxCacheSizeAbsolute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationMaxCacheSizeAbsolute
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeliveryOptimizationMaxCacheSizeAbsolute()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .delivery_optimization_max_cache_size import DeliveryOptimizationMaxCacheSize

        from .delivery_optimization_max_cache_size import DeliveryOptimizationMaxCacheSize

        fields: Dict[str, Callable[[Any], None]] = {
            "maximumCacheSizeInGigabytes": lambda n : setattr(self, 'maximum_cache_size_in_gigabytes', n.get_int_value()),
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
        writer.write_int_value("maximumCacheSizeInGigabytes", self.maximum_cache_size_in_gigabytes)
    

