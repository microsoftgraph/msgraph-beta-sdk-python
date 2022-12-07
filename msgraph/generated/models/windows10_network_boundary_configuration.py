from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
windows_network_isolation_policy = lazy_import('msgraph.generated.models.windows_network_isolation_policy')

class Windows10NetworkBoundaryConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10NetworkBoundaryConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10NetworkBoundaryConfiguration"
        # Windows Network Isolation Policy
        self._windows_network_isolation_policy: Optional[windows_network_isolation_policy.WindowsNetworkIsolationPolicy] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10NetworkBoundaryConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10NetworkBoundaryConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10NetworkBoundaryConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "windows_network_isolation_policy": lambda n : setattr(self, 'windows_network_isolation_policy', n.get_object_value(windows_network_isolation_policy.WindowsNetworkIsolationPolicy)),
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
        writer.write_object_value("windowsNetworkIsolationPolicy", self.windows_network_isolation_policy)
    
    @property
    def windows_network_isolation_policy(self,) -> Optional[windows_network_isolation_policy.WindowsNetworkIsolationPolicy]:
        """
        Gets the windowsNetworkIsolationPolicy property value. Windows Network Isolation Policy
        Returns: Optional[windows_network_isolation_policy.WindowsNetworkIsolationPolicy]
        """
        return self._windows_network_isolation_policy
    
    @windows_network_isolation_policy.setter
    def windows_network_isolation_policy(self,value: Optional[windows_network_isolation_policy.WindowsNetworkIsolationPolicy] = None) -> None:
        """
        Sets the windowsNetworkIsolationPolicy property value. Windows Network Isolation Policy
        Args:
            value: Value to set for the windowsNetworkIsolationPolicy property.
        """
        self._windows_network_isolation_policy = value
    

