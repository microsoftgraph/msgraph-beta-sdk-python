from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_owner_global_proxy

from . import android_device_owner_global_proxy

@dataclass
class AndroidDeviceOwnerGlobalProxyAutoConfig(android_device_owner_global_proxy.AndroidDeviceOwnerGlobalProxy):
    odata_type = "#microsoft.graph.androidDeviceOwnerGlobalProxyAutoConfig"
    # The proxy auto-config URL
    proxy_auto_config_u_r_l: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerGlobalProxyAutoConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerGlobalProxyAutoConfig
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerGlobalProxyAutoConfig()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_device_owner_global_proxy

        fields: Dict[str, Callable[[Any], None]] = {
            "proxyAutoConfigURL": lambda n : setattr(self, 'proxy_auto_config_u_r_l', n.get_str_value()),
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
        writer.write_str_value("proxyAutoConfigURL", self.proxy_auto_config_u_r_l)
    

