from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsResourcePerformance(Entity):
    """
    The user experience analytics resource performance entity.
    """
    # AverageSpikeTimeScore of a device or a model type. Valid values 0 to 100
    average_spike_time_score: Optional[int] = None
    # CPU spike time in percentage. Valid values 0 to 100
    cpu_spike_time_percentage: Optional[float] = None
    # Threshold of cpuSpikeTimeScore. Valid values 0 to 100
    cpu_spike_time_percentage_threshold: Optional[float] = None
    # The user experience analytics device CPU spike time score. Valid values 0 to 100
    cpu_spike_time_score: Optional[int] = None
    # User experience analytics summarized device count.
    device_count: Optional[int] = None
    # The id of the device.
    device_id: Optional[str] = None
    # The name of the device.
    device_name: Optional[str] = None
    # Resource performance score of a specific device. Valid values 0 to 100
    device_resource_performance_score: Optional[int] = None
    # The user experience analytics device manufacturer.
    manufacturer: Optional[str] = None
    # The user experience analytics device model.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # RAM spike time in percentage. Valid values 0 to 100
    ram_spike_time_percentage: Optional[float] = None
    # Threshold of ramSpikeTimeScore. Valid values 0 to 100
    ram_spike_time_percentage_threshold: Optional[float] = None
    # The user experience analytics device RAM spike time score. Valid values 0 to 100
    ram_spike_time_score: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsResourcePerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsResourcePerformance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsResourcePerformance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "averageSpikeTimeScore": lambda n : setattr(self, 'average_spike_time_score', n.get_int_value()),
            "cpuSpikeTimePercentage": lambda n : setattr(self, 'cpu_spike_time_percentage', n.get_float_value()),
            "cpuSpikeTimePercentageThreshold": lambda n : setattr(self, 'cpu_spike_time_percentage_threshold', n.get_float_value()),
            "cpuSpikeTimeScore": lambda n : setattr(self, 'cpu_spike_time_score', n.get_int_value()),
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "deviceResourcePerformanceScore": lambda n : setattr(self, 'device_resource_performance_score', n.get_int_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "ramSpikeTimePercentage": lambda n : setattr(self, 'ram_spike_time_percentage', n.get_float_value()),
            "ramSpikeTimePercentageThreshold": lambda n : setattr(self, 'ram_spike_time_percentage_threshold', n.get_float_value()),
            "ramSpikeTimeScore": lambda n : setattr(self, 'ram_spike_time_score', n.get_int_value()),
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
        writer.write_int_value("averageSpikeTimeScore", self.average_spike_time_score)
        writer.write_float_value("cpuSpikeTimePercentage", self.cpu_spike_time_percentage)
        writer.write_float_value("cpuSpikeTimePercentageThreshold", self.cpu_spike_time_percentage_threshold)
        writer.write_int_value("cpuSpikeTimeScore", self.cpu_spike_time_score)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_int_value("deviceResourcePerformanceScore", self.device_resource_performance_score)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_float_value("ramSpikeTimePercentage", self.ram_spike_time_percentage)
        writer.write_float_value("ramSpikeTimePercentageThreshold", self.ram_spike_time_percentage_threshold)
        writer.write_int_value("ramSpikeTimeScore", self.ram_spike_time_score)
    

