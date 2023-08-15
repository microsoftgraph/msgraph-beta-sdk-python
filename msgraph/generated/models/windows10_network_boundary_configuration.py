from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .windows_network_isolation_policy import WindowsNetworkIsolationPolicy

from .device_configuration import DeviceConfiguration

@dataclass
class Windows10NetworkBoundaryConfiguration(DeviceConfiguration):
    """
    Windows10 Network Boundary Configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10NetworkBoundaryConfiguration"
    # Windows Network Isolation Policy
    windows_network_isolation_policy: Optional[WindowsNetworkIsolationPolicy] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10NetworkBoundaryConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10NetworkBoundaryConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Windows10NetworkBoundaryConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .windows_network_isolation_policy import WindowsNetworkIsolationPolicy

        from .device_configuration import DeviceConfiguration
        from .windows_network_isolation_policy import WindowsNetworkIsolationPolicy

        fields: Dict[str, Callable[[Any], None]] = {
            "windowsNetworkIsolationPolicy": lambda n : setattr(self, 'windows_network_isolation_policy', n.get_object_value(WindowsNetworkIsolationPolicy)),
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
        writer.write_object_value("windowsNetworkIsolationPolicy", self.windows_network_isolation_policy)
    

