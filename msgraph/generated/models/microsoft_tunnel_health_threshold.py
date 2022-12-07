from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class MicrosoftTunnelHealthThreshold(entity.Entity):
    """
    Entity that represents the health thresholds of a health metric
    """
    def __init__(self,) -> None:
        """
        Instantiates a new microsoftTunnelHealthThreshold and sets the default values.
        """
        super().__init__()
        # The threshold for being healthy based on default health status metrics: CPU usage healthy < 50%, Memory usage healthy < 50%, Disk space healthy > 5GB, Latency healthy < 10ms, health metrics can be customized. Read-only.
        self._default_healthy_threshold: Optional[int] = None
        # The threshold for being unhealthy based on default health status metrics: CPU usage unhealthy > 75%, Memory usage unhealthy > 75%, Disk space < 3GB, Latency unhealthy > 20ms, health metrics can be customized. Read-only.
        self._default_unhealthy_threshold: Optional[int] = None
        # The threshold for being healthy based on default health status metrics: CPU usage healthy < 50%, Memory usage healthy < 50%, Disk space healthy > 5GB, Latency healthy < 10ms, health metrics can be customized.
        self._healthy_threshold: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The threshold for being unhealthy based on default health status metrics: CPU usage unhealthy > 75%, Memory usage unhealthy > 75%, Disk space < 3GB, Latency Unhealthy > 20ms, health metrics can be customized.
        self._unhealthy_threshold: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftTunnelHealthThreshold:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftTunnelHealthThreshold
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftTunnelHealthThreshold()
    
    @property
    def default_healthy_threshold(self,) -> Optional[int]:
        """
        Gets the defaultHealthyThreshold property value. The threshold for being healthy based on default health status metrics: CPU usage healthy < 50%, Memory usage healthy < 50%, Disk space healthy > 5GB, Latency healthy < 10ms, health metrics can be customized. Read-only.
        Returns: Optional[int]
        """
        return self._default_healthy_threshold
    
    @default_healthy_threshold.setter
    def default_healthy_threshold(self,value: Optional[int] = None) -> None:
        """
        Sets the defaultHealthyThreshold property value. The threshold for being healthy based on default health status metrics: CPU usage healthy < 50%, Memory usage healthy < 50%, Disk space healthy > 5GB, Latency healthy < 10ms, health metrics can be customized. Read-only.
        Args:
            value: Value to set for the defaultHealthyThreshold property.
        """
        self._default_healthy_threshold = value
    
    @property
    def default_unhealthy_threshold(self,) -> Optional[int]:
        """
        Gets the defaultUnhealthyThreshold property value. The threshold for being unhealthy based on default health status metrics: CPU usage unhealthy > 75%, Memory usage unhealthy > 75%, Disk space < 3GB, Latency unhealthy > 20ms, health metrics can be customized. Read-only.
        Returns: Optional[int]
        """
        return self._default_unhealthy_threshold
    
    @default_unhealthy_threshold.setter
    def default_unhealthy_threshold(self,value: Optional[int] = None) -> None:
        """
        Sets the defaultUnhealthyThreshold property value. The threshold for being unhealthy based on default health status metrics: CPU usage unhealthy > 75%, Memory usage unhealthy > 75%, Disk space < 3GB, Latency unhealthy > 20ms, health metrics can be customized. Read-only.
        Args:
            value: Value to set for the defaultUnhealthyThreshold property.
        """
        self._default_unhealthy_threshold = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_healthy_threshold": lambda n : setattr(self, 'default_healthy_threshold', n.get_int_value()),
            "default_unhealthy_threshold": lambda n : setattr(self, 'default_unhealthy_threshold', n.get_int_value()),
            "healthy_threshold": lambda n : setattr(self, 'healthy_threshold', n.get_int_value()),
            "unhealthy_threshold": lambda n : setattr(self, 'unhealthy_threshold', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def healthy_threshold(self,) -> Optional[int]:
        """
        Gets the healthyThreshold property value. The threshold for being healthy based on default health status metrics: CPU usage healthy < 50%, Memory usage healthy < 50%, Disk space healthy > 5GB, Latency healthy < 10ms, health metrics can be customized.
        Returns: Optional[int]
        """
        return self._healthy_threshold
    
    @healthy_threshold.setter
    def healthy_threshold(self,value: Optional[int] = None) -> None:
        """
        Sets the healthyThreshold property value. The threshold for being healthy based on default health status metrics: CPU usage healthy < 50%, Memory usage healthy < 50%, Disk space healthy > 5GB, Latency healthy < 10ms, health metrics can be customized.
        Args:
            value: Value to set for the healthyThreshold property.
        """
        self._healthy_threshold = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("defaultHealthyThreshold", self.default_healthy_threshold)
        writer.write_int_value("defaultUnhealthyThreshold", self.default_unhealthy_threshold)
        writer.write_int_value("healthyThreshold", self.healthy_threshold)
        writer.write_int_value("unhealthyThreshold", self.unhealthy_threshold)
    
    @property
    def unhealthy_threshold(self,) -> Optional[int]:
        """
        Gets the unhealthyThreshold property value. The threshold for being unhealthy based on default health status metrics: CPU usage unhealthy > 75%, Memory usage unhealthy > 75%, Disk space < 3GB, Latency Unhealthy > 20ms, health metrics can be customized.
        Returns: Optional[int]
        """
        return self._unhealthy_threshold
    
    @unhealthy_threshold.setter
    def unhealthy_threshold(self,value: Optional[int] = None) -> None:
        """
        Sets the unhealthyThreshold property value. The threshold for being unhealthy based on default health status metrics: CPU usage unhealthy > 75%, Memory usage unhealthy > 75%, Disk space < 3GB, Latency Unhealthy > 20ms, health metrics can be customized.
        Args:
            value: Value to set for the unhealthyThreshold property.
        """
        self._unhealthy_threshold = value
    

