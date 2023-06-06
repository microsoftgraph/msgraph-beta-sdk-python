from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows10_vpn_proxy_server, windows81_vpn_proxy_server

@dataclass
class VpnProxyServer(AdditionalDataHolder, Parsable):
    """
    VPN Proxy Server.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Address.
    address: Optional[str] = None
    # Proxy's automatic configuration script url.
    automatic_configuration_script_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Port. Valid values 0 to 65535
    port: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VpnProxyServer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VpnProxyServer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.windows10VpnProxyServer":
                from . import windows10_vpn_proxy_server

                return windows10_vpn_proxy_server.Windows10VpnProxyServer()
            if mapping_value == "#microsoft.graph.windows81VpnProxyServer":
                from . import windows81_vpn_proxy_server

                return windows81_vpn_proxy_server.Windows81VpnProxyServer()
        return VpnProxyServer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows10_vpn_proxy_server, windows81_vpn_proxy_server

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "automaticConfigurationScriptUrl": lambda n : setattr(self, 'automatic_configuration_script_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("address", self.address)
        writer.write_str_value("automaticConfigurationScriptUrl", self.automatic_configuration_script_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("port", self.port)
        writer.write_additional_data_value(self.additional_data)
    

