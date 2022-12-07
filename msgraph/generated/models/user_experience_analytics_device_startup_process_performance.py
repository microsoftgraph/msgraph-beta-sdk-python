from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsDeviceStartupProcessPerformance(entity.Entity):
    """
    The user experience analytics device startup process performance.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsDeviceStartupProcessPerformance and sets the default values.
        """
        super().__init__()
        # User experience analytics device startup process summarized count.
        self._device_count: Optional[int] = None
        # User experience analytics device startup process median impact in milliseconds.
        self._median_impact_in_ms: Optional[int] = None
        # User experience analytics device startup process median impact in milliseconds.
        self._median_impact_in_ms2: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # User experience analytics device startup process name.
        self._process_name: Optional[str] = None
        # The user experience analytics device startup process product name.
        self._product_name: Optional[str] = None
        # The User experience analytics device startup process publisher.
        self._publisher: Optional[str] = None
        # User experience analytics device startup process total impact in milliseconds.
        self._total_impact_in_ms: Optional[int] = None
        # User experience analytics device startup process total impact in milliseconds.
        self._total_impact_in_ms2: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDeviceStartupProcessPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceStartupProcessPerformance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsDeviceStartupProcessPerformance()
    
    @property
    def device_count(self,) -> Optional[int]:
        """
        Gets the deviceCount property value. User experience analytics device startup process summarized count.
        Returns: Optional[int]
        """
        return self._device_count
    
    @device_count.setter
    def device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceCount property value. User experience analytics device startup process summarized count.
        Args:
            value: Value to set for the deviceCount property.
        """
        self._device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_count": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "median_impact_in_ms": lambda n : setattr(self, 'median_impact_in_ms', n.get_int_value()),
            "median_impact_in_ms2": lambda n : setattr(self, 'median_impact_in_ms2', n.get_int_value()),
            "process_name": lambda n : setattr(self, 'process_name', n.get_str_value()),
            "product_name": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "total_impact_in_ms": lambda n : setattr(self, 'total_impact_in_ms', n.get_int_value()),
            "total_impact_in_ms2": lambda n : setattr(self, 'total_impact_in_ms2', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def median_impact_in_ms(self,) -> Optional[int]:
        """
        Gets the medianImpactInMs property value. User experience analytics device startup process median impact in milliseconds.
        Returns: Optional[int]
        """
        return self._median_impact_in_ms
    
    @median_impact_in_ms.setter
    def median_impact_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the medianImpactInMs property value. User experience analytics device startup process median impact in milliseconds.
        Args:
            value: Value to set for the medianImpactInMs property.
        """
        self._median_impact_in_ms = value
    
    @property
    def median_impact_in_ms2(self,) -> Optional[int]:
        """
        Gets the medianImpactInMs2 property value. User experience analytics device startup process median impact in milliseconds.
        Returns: Optional[int]
        """
        return self._median_impact_in_ms2
    
    @median_impact_in_ms2.setter
    def median_impact_in_ms2(self,value: Optional[int] = None) -> None:
        """
        Sets the medianImpactInMs2 property value. User experience analytics device startup process median impact in milliseconds.
        Args:
            value: Value to set for the medianImpactInMs2 property.
        """
        self._median_impact_in_ms2 = value
    
    @property
    def process_name(self,) -> Optional[str]:
        """
        Gets the processName property value. User experience analytics device startup process name.
        Returns: Optional[str]
        """
        return self._process_name
    
    @process_name.setter
    def process_name(self,value: Optional[str] = None) -> None:
        """
        Sets the processName property value. User experience analytics device startup process name.
        Args:
            value: Value to set for the processName property.
        """
        self._process_name = value
    
    @property
    def product_name(self,) -> Optional[str]:
        """
        Gets the productName property value. The user experience analytics device startup process product name.
        Returns: Optional[str]
        """
        return self._product_name
    
    @product_name.setter
    def product_name(self,value: Optional[str] = None) -> None:
        """
        Sets the productName property value. The user experience analytics device startup process product name.
        Args:
            value: Value to set for the productName property.
        """
        self._product_name = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. The User experience analytics device startup process publisher.
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. The User experience analytics device startup process publisher.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_int_value("medianImpactInMs", self.median_impact_in_ms)
        writer.write_int_value("medianImpactInMs2", self.median_impact_in_ms2)
        writer.write_str_value("processName", self.process_name)
        writer.write_str_value("productName", self.product_name)
        writer.write_str_value("publisher", self.publisher)
        writer.write_int_value("totalImpactInMs", self.total_impact_in_ms)
        writer.write_int_value("totalImpactInMs2", self.total_impact_in_ms2)
    
    @property
    def total_impact_in_ms(self,) -> Optional[int]:
        """
        Gets the totalImpactInMs property value. User experience analytics device startup process total impact in milliseconds.
        Returns: Optional[int]
        """
        return self._total_impact_in_ms
    
    @total_impact_in_ms.setter
    def total_impact_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the totalImpactInMs property value. User experience analytics device startup process total impact in milliseconds.
        Args:
            value: Value to set for the totalImpactInMs property.
        """
        self._total_impact_in_ms = value
    
    @property
    def total_impact_in_ms2(self,) -> Optional[int]:
        """
        Gets the totalImpactInMs2 property value. User experience analytics device startup process total impact in milliseconds.
        Returns: Optional[int]
        """
        return self._total_impact_in_ms2
    
    @total_impact_in_ms2.setter
    def total_impact_in_ms2(self,value: Optional[int] = None) -> None:
        """
        Sets the totalImpactInMs2 property value. User experience analytics device startup process total impact in milliseconds.
        Args:
            value: Value to set for the totalImpactInMs2 property.
        """
        self._total_impact_in_ms2 = value
    

