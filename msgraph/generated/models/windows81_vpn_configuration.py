from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows81_vpn_proxy_server, windows_phone81_vpn_configuration, windows_vpn_configuration, windows_vpn_connection_type

from . import windows_vpn_configuration

@dataclass
class Windows81VpnConfiguration(windows_vpn_configuration.WindowsVpnConfiguration):
    odata_type = "#microsoft.graph.windows81VpnConfiguration"
    # Value indicating whether this policy only applies to Windows 8.1. This property is read-only.
    apply_only_to_windows81: Optional[bool] = None
    # Windows VPN connection type.
    connection_type: Optional[windows_vpn_connection_type.WindowsVpnConnectionType] = None
    # Enable split tunneling for the VPN.
    enable_split_tunneling: Optional[bool] = None
    # Login group or domain when connection type is set to Dell SonicWALL Mobile Connection.
    login_group_or_domain: Optional[str] = None
    # Proxy Server.
    proxy_server: Optional[windows81_vpn_proxy_server.Windows81VpnProxyServer] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows81VpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows81VpnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.windowsPhone81VpnConfiguration":
                from . import windows_phone81_vpn_configuration

                return windows_phone81_vpn_configuration.WindowsPhone81VpnConfiguration()
        return Windows81VpnConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows81_vpn_proxy_server, windows_phone81_vpn_configuration, windows_vpn_configuration, windows_vpn_connection_type

        fields: Dict[str, Callable[[Any], None]] = {
            "applyOnlyToWindows81": lambda n : setattr(self, 'apply_only_to_windows81', n.get_bool_value()),
            "connectionType": lambda n : setattr(self, 'connection_type', n.get_enum_value(windows_vpn_connection_type.WindowsVpnConnectionType)),
            "enableSplitTunneling": lambda n : setattr(self, 'enable_split_tunneling', n.get_bool_value()),
            "loginGroupOrDomain": lambda n : setattr(self, 'login_group_or_domain', n.get_str_value()),
            "proxyServer": lambda n : setattr(self, 'proxy_server', n.get_object_value(windows81_vpn_proxy_server.Windows81VpnProxyServer)),
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
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_bool_value("enableSplitTunneling", self.enable_split_tunneling)
        writer.write_str_value("loginGroupOrDomain", self.login_group_or_domain)
        writer.write_object_value("proxyServer", self.proxy_server)
    

