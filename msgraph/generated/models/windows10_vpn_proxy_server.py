from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import vpn_proxy_server

from . import vpn_proxy_server

@dataclass
class Windows10VpnProxyServer(vpn_proxy_server.VpnProxyServer):
    odata_type = "#microsoft.graph.windows10VpnProxyServer"
    # Bypass proxy server for local address.
    bypass_proxy_server_for_local_address: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10VpnProxyServer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10VpnProxyServer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10VpnProxyServer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import vpn_proxy_server

        fields: Dict[str, Callable[[Any], None]] = {
            "bypassProxyServerForLocalAddress": lambda n : setattr(self, 'bypass_proxy_server_for_local_address', n.get_bool_value()),
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
        writer.write_bool_value("bypassProxyServerForLocalAddress", self.bypass_proxy_server_for_local_address)
    

