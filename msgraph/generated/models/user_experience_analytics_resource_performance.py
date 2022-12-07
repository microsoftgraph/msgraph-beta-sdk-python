from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsResourcePerformance(entity.Entity):
    """
    The user experience analytics resource performance entity.
    """
    @property
    def average_spike_time_score(self,) -> Optional[int]:
        """
        Gets the averageSpikeTimeScore property value. AverageSpikeTimeScore of a device or a model type. Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._average_spike_time_score
    
    @average_spike_time_score.setter
    def average_spike_time_score(self,value: Optional[int] = None) -> None:
        """
        Sets the averageSpikeTimeScore property value. AverageSpikeTimeScore of a device or a model type. Valid values 0 to 100
        Args:
            value: Value to set for the averageSpikeTimeScore property.
        """
        self._average_spike_time_score = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsResourcePerformance and sets the default values.
        """
        super().__init__()
        # AverageSpikeTimeScore of a device or a model type. Valid values 0 to 100
        self._average_spike_time_score: Optional[int] = None
        # CPU spike time in percentage. Valid values 0 to 100
        self._cpu_spike_time_percentage: Optional[float] = None
        # Threshold of cpuSpikeTimeScore. Valid values 0 to 100
        self._cpu_spike_time_percentage_threshold: Optional[float] = None
        # The user experience analytics device CPU spike time score. Valid values 0 to 100
        self._cpu_spike_time_score: Optional[int] = None
        # User experience analytics summarized device count.
        self._device_count: Optional[int] = None
        # The id of the device.
        self._device_id: Optional[str] = None
        # The name of the device.
        self._device_name: Optional[str] = None
        # Resource performance score of a specific device. Valid values 0 to 100
        self._device_resource_performance_score: Optional[int] = None
        # The user experience analytics device manufacturer.
        self._manufacturer: Optional[str] = None
        # The user experience analytics device model.
        self._model: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # RAM spike time in percentage. Valid values 0 to 100
        self._ram_spike_time_percentage: Optional[float] = None
        # Threshold of ramSpikeTimeScore. Valid values 0 to 100
        self._ram_spike_time_percentage_threshold: Optional[float] = None
        # The user experience analytics device RAM spike time score. Valid values 0 to 100
        self._ram_spike_time_score: Optional[int] = None
    
    @property
    def cpu_spike_time_percentage(self,) -> Optional[float]:
        """
        Gets the cpuSpikeTimePercentage property value. CPU spike time in percentage. Valid values 0 to 100
        Returns: Optional[float]
        """
        return self._cpu_spike_time_percentage
    
    @cpu_spike_time_percentage.setter
    def cpu_spike_time_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the cpuSpikeTimePercentage property value. CPU spike time in percentage. Valid values 0 to 100
        Args:
            value: Value to set for the cpuSpikeTimePercentage property.
        """
        self._cpu_spike_time_percentage = value
    
    @property
    def cpu_spike_time_percentage_threshold(self,) -> Optional[float]:
        """
        Gets the cpuSpikeTimePercentageThreshold property value. Threshold of cpuSpikeTimeScore. Valid values 0 to 100
        Returns: Optional[float]
        """
        return self._cpu_spike_time_percentage_threshold
    
    @cpu_spike_time_percentage_threshold.setter
    def cpu_spike_time_percentage_threshold(self,value: Optional[float] = None) -> None:
        """
        Sets the cpuSpikeTimePercentageThreshold property value. Threshold of cpuSpikeTimeScore. Valid values 0 to 100
        Args:
            value: Value to set for the cpuSpikeTimePercentageThreshold property.
        """
        self._cpu_spike_time_percentage_threshold = value
    
    @property
    def cpu_spike_time_score(self,) -> Optional[int]:
        """
        Gets the cpuSpikeTimeScore property value. The user experience analytics device CPU spike time score. Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._cpu_spike_time_score
    
    @cpu_spike_time_score.setter
    def cpu_spike_time_score(self,value: Optional[int] = None) -> None:
        """
        Sets the cpuSpikeTimeScore property value. The user experience analytics device CPU spike time score. Valid values 0 to 100
        Args:
            value: Value to set for the cpuSpikeTimeScore property.
        """
        self._cpu_spike_time_score = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsResourcePerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsResourcePerformance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsResourcePerformance()
    
    @property
    def device_count(self,) -> Optional[int]:
        """
        Gets the deviceCount property value. User experience analytics summarized device count.
        Returns: Optional[int]
        """
        return self._device_count
    
    @device_count.setter
    def device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceCount property value. User experience analytics summarized device count.
        Args:
            value: Value to set for the deviceCount property.
        """
        self._device_count = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The id of the device.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The id of the device.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The name of the device.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The name of the device.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def device_resource_performance_score(self,) -> Optional[int]:
        """
        Gets the deviceResourcePerformanceScore property value. Resource performance score of a specific device. Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._device_resource_performance_score
    
    @device_resource_performance_score.setter
    def device_resource_performance_score(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceResourcePerformanceScore property value. Resource performance score of a specific device. Valid values 0 to 100
        Args:
            value: Value to set for the deviceResourcePerformanceScore property.
        """
        self._device_resource_performance_score = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "average_spike_time_score": lambda n : setattr(self, 'average_spike_time_score', n.get_int_value()),
            "cpu_spike_time_percentage": lambda n : setattr(self, 'cpu_spike_time_percentage', n.get_float_value()),
            "cpu_spike_time_percentage_threshold": lambda n : setattr(self, 'cpu_spike_time_percentage_threshold', n.get_float_value()),
            "cpu_spike_time_score": lambda n : setattr(self, 'cpu_spike_time_score', n.get_int_value()),
            "device_count": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "device_resource_performance_score": lambda n : setattr(self, 'device_resource_performance_score', n.get_int_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "ram_spike_time_percentage": lambda n : setattr(self, 'ram_spike_time_percentage', n.get_float_value()),
            "ram_spike_time_percentage_threshold": lambda n : setattr(self, 'ram_spike_time_percentage_threshold', n.get_float_value()),
            "ram_spike_time_score": lambda n : setattr(self, 'ram_spike_time_score', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. The user experience analytics device manufacturer.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. The user experience analytics device manufacturer.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. The user experience analytics device model.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. The user experience analytics device model.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def ram_spike_time_percentage(self,) -> Optional[float]:
        """
        Gets the ramSpikeTimePercentage property value. RAM spike time in percentage. Valid values 0 to 100
        Returns: Optional[float]
        """
        return self._ram_spike_time_percentage
    
    @ram_spike_time_percentage.setter
    def ram_spike_time_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the ramSpikeTimePercentage property value. RAM spike time in percentage. Valid values 0 to 100
        Args:
            value: Value to set for the ramSpikeTimePercentage property.
        """
        self._ram_spike_time_percentage = value
    
    @property
    def ram_spike_time_percentage_threshold(self,) -> Optional[float]:
        """
        Gets the ramSpikeTimePercentageThreshold property value. Threshold of ramSpikeTimeScore. Valid values 0 to 100
        Returns: Optional[float]
        """
        return self._ram_spike_time_percentage_threshold
    
    @ram_spike_time_percentage_threshold.setter
    def ram_spike_time_percentage_threshold(self,value: Optional[float] = None) -> None:
        """
        Sets the ramSpikeTimePercentageThreshold property value. Threshold of ramSpikeTimeScore. Valid values 0 to 100
        Args:
            value: Value to set for the ramSpikeTimePercentageThreshold property.
        """
        self._ram_spike_time_percentage_threshold = value
    
    @property
    def ram_spike_time_score(self,) -> Optional[int]:
        """
        Gets the ramSpikeTimeScore property value. The user experience analytics device RAM spike time score. Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._ram_spike_time_score
    
    @ram_spike_time_score.setter
    def ram_spike_time_score(self,value: Optional[int] = None) -> None:
        """
        Sets the ramSpikeTimeScore property value. The user experience analytics device RAM spike time score. Valid values 0 to 100
        Args:
            value: Value to set for the ramSpikeTimeScore property.
        """
        self._ram_spike_time_score = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    

