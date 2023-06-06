from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class UserExperienceAnalyticsDeviceStartupProcessPerformance(entity.Entity):
    """
    The user experience analytics device startup process performance.
    """
    # User experience analytics device startup process summarized count.
    device_count: Optional[int] = None
    # User experience analytics device startup process median impact in milliseconds.
    median_impact_in_ms: Optional[int] = None
    # User experience analytics device startup process median impact in milliseconds.
    median_impact_in_ms2: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # User experience analytics device startup process name.
    process_name: Optional[str] = None
    # The user experience analytics device startup process product name.
    product_name: Optional[str] = None
    # The User experience analytics device startup process publisher.
    publisher: Optional[str] = None
    # User experience analytics device startup process total impact in milliseconds.
    total_impact_in_ms: Optional[int] = None
    # User experience analytics device startup process total impact in milliseconds.
    total_impact_in_ms2: Optional[int] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "medianImpactInMs": lambda n : setattr(self, 'median_impact_in_ms', n.get_int_value()),
            "medianImpactInMs2": lambda n : setattr(self, 'median_impact_in_ms2', n.get_int_value()),
            "processName": lambda n : setattr(self, 'process_name', n.get_str_value()),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "totalImpactInMs": lambda n : setattr(self, 'total_impact_in_ms', n.get_int_value()),
            "totalImpactInMs2": lambda n : setattr(self, 'total_impact_in_ms2', n.get_int_value()),
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
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_int_value("medianImpactInMs", self.median_impact_in_ms)
        writer.write_int_value("medianImpactInMs2", self.median_impact_in_ms2)
        writer.write_str_value("processName", self.process_name)
        writer.write_str_value("productName", self.product_name)
        writer.write_str_value("publisher", self.publisher)
        writer.write_int_value("totalImpactInMs", self.total_impact_in_ms)
        writer.write_int_value("totalImpactInMs2", self.total_impact_in_ms2)
    

