from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

delivery_optimization_max_cache_size = lazy_import('msgraph.generated.models.delivery_optimization_max_cache_size')

class DeliveryOptimizationMaxCacheSizeAbsolute(delivery_optimization_max_cache_size.DeliveryOptimizationMaxCacheSize):
    def __init__(self,) -> None:
        """
        Instantiates a new DeliveryOptimizationMaxCacheSizeAbsolute and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deliveryOptimizationMaxCacheSizeAbsolute"
        # Specifies the maximum size in GB of Delivery Optimization cache. Valid values 0 to 4294967295
        self._maximum_cache_size_in_gigabytes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeliveryOptimizationMaxCacheSizeAbsolute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationMaxCacheSizeAbsolute
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeliveryOptimizationMaxCacheSizeAbsolute()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "maximum_cache_size_in_gigabytes": lambda n : setattr(self, 'maximum_cache_size_in_gigabytes', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def maximum_cache_size_in_gigabytes(self,) -> Optional[int]:
        """
        Gets the maximumCacheSizeInGigabytes property value. Specifies the maximum size in GB of Delivery Optimization cache. Valid values 0 to 4294967295
        Returns: Optional[int]
        """
        return self._maximum_cache_size_in_gigabytes
    
    @maximum_cache_size_in_gigabytes.setter
    def maximum_cache_size_in_gigabytes(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumCacheSizeInGigabytes property value. Specifies the maximum size in GB of Delivery Optimization cache. Valid values 0 to 4294967295
        Args:
            value: Value to set for the maximumCacheSizeInGigabytes property.
        """
        self._maximum_cache_size_in_gigabytes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("maximumCacheSizeInGigabytes", self.maximum_cache_size_in_gigabytes)
    

