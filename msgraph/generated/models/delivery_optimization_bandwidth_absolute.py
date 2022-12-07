from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

delivery_optimization_bandwidth = lazy_import('msgraph.generated.models.delivery_optimization_bandwidth')

class DeliveryOptimizationBandwidthAbsolute(delivery_optimization_bandwidth.DeliveryOptimizationBandwidth):
    def __init__(self,) -> None:
        """
        Instantiates a new DeliveryOptimizationBandwidthAbsolute and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deliveryOptimizationBandwidthAbsolute"
        # Specifies the maximum download bandwidth in KiloBytes/second that the device can use across all concurrent download activities using Delivery Optimization. Valid values 0 to 4294967295
        self._maximum_download_bandwidth_in_kilobytes_per_second: Optional[int] = None
        # Specifies the maximum upload bandwidth in KiloBytes/second that a device will use across all concurrent upload activity using Delivery Optimization (0-4000000). Valid values 0 to 4000000
        self._maximum_upload_bandwidth_in_kilobytes_per_second: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeliveryOptimizationBandwidthAbsolute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationBandwidthAbsolute
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeliveryOptimizationBandwidthAbsolute()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "maximum_download_bandwidth_in_kilobytes_per_second": lambda n : setattr(self, 'maximum_download_bandwidth_in_kilobytes_per_second', n.get_int_value()),
            "maximum_upload_bandwidth_in_kilobytes_per_second": lambda n : setattr(self, 'maximum_upload_bandwidth_in_kilobytes_per_second', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def maximum_download_bandwidth_in_kilobytes_per_second(self,) -> Optional[int]:
        """
        Gets the maximumDownloadBandwidthInKilobytesPerSecond property value. Specifies the maximum download bandwidth in KiloBytes/second that the device can use across all concurrent download activities using Delivery Optimization. Valid values 0 to 4294967295
        Returns: Optional[int]
        """
        return self._maximum_download_bandwidth_in_kilobytes_per_second
    
    @maximum_download_bandwidth_in_kilobytes_per_second.setter
    def maximum_download_bandwidth_in_kilobytes_per_second(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumDownloadBandwidthInKilobytesPerSecond property value. Specifies the maximum download bandwidth in KiloBytes/second that the device can use across all concurrent download activities using Delivery Optimization. Valid values 0 to 4294967295
        Args:
            value: Value to set for the maximumDownloadBandwidthInKilobytesPerSecond property.
        """
        self._maximum_download_bandwidth_in_kilobytes_per_second = value
    
    @property
    def maximum_upload_bandwidth_in_kilobytes_per_second(self,) -> Optional[int]:
        """
        Gets the maximumUploadBandwidthInKilobytesPerSecond property value. Specifies the maximum upload bandwidth in KiloBytes/second that a device will use across all concurrent upload activity using Delivery Optimization (0-4000000). Valid values 0 to 4000000
        Returns: Optional[int]
        """
        return self._maximum_upload_bandwidth_in_kilobytes_per_second
    
    @maximum_upload_bandwidth_in_kilobytes_per_second.setter
    def maximum_upload_bandwidth_in_kilobytes_per_second(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumUploadBandwidthInKilobytesPerSecond property value. Specifies the maximum upload bandwidth in KiloBytes/second that a device will use across all concurrent upload activity using Delivery Optimization (0-4000000). Valid values 0 to 4000000
        Args:
            value: Value to set for the maximumUploadBandwidthInKilobytesPerSecond property.
        """
        self._maximum_upload_bandwidth_in_kilobytes_per_second = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("maximumDownloadBandwidthInKilobytesPerSecond", self.maximum_download_bandwidth_in_kilobytes_per_second)
        writer.write_int_value("maximumUploadBandwidthInKilobytesPerSecond", self.maximum_upload_bandwidth_in_kilobytes_per_second)
    

