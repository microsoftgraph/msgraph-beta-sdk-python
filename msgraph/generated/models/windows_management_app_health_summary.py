from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class WindowsManagementAppHealthSummary(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsManagementAppHealthSummary and sets the default values.
        """
        super().__init__()
        # Healthy device count.
        self._healthy_device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Unhealthy device count.
        self._unhealthy_device_count: Optional[int] = None
        # Unknown device count.
        self._unknown_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsManagementAppHealthSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsManagementAppHealthSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsManagementAppHealthSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "healthy_device_count": lambda n : setattr(self, 'healthy_device_count', n.get_int_value()),
            "unhealthy_device_count": lambda n : setattr(self, 'unhealthy_device_count', n.get_int_value()),
            "unknown_device_count": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def healthy_device_count(self,) -> Optional[int]:
        """
        Gets the healthyDeviceCount property value. Healthy device count.
        Returns: Optional[int]
        """
        return self._healthy_device_count
    
    @healthy_device_count.setter
    def healthy_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the healthyDeviceCount property value. Healthy device count.
        Args:
            value: Value to set for the healthyDeviceCount property.
        """
        self._healthy_device_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("healthyDeviceCount", self.healthy_device_count)
        writer.write_int_value("unhealthyDeviceCount", self.unhealthy_device_count)
        writer.write_int_value("unknownDeviceCount", self.unknown_device_count)
    
    @property
    def unhealthy_device_count(self,) -> Optional[int]:
        """
        Gets the unhealthyDeviceCount property value. Unhealthy device count.
        Returns: Optional[int]
        """
        return self._unhealthy_device_count
    
    @unhealthy_device_count.setter
    def unhealthy_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unhealthyDeviceCount property value. Unhealthy device count.
        Args:
            value: Value to set for the unhealthyDeviceCount property.
        """
        self._unhealthy_device_count = value
    
    @property
    def unknown_device_count(self,) -> Optional[int]:
        """
        Gets the unknownDeviceCount property value. Unknown device count.
        Returns: Optional[int]
        """
        return self._unknown_device_count
    
    @unknown_device_count.setter
    def unknown_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unknownDeviceCount property value. Unknown device count.
        Args:
            value: Value to set for the unknownDeviceCount property.
        """
        self._unknown_device_count = value
    

