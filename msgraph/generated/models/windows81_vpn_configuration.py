from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows81_vpn_proxy_server, windows_phone81_vpn_configuration, windows_vpn_configuration, windows_vpn_connection_type

from . import windows_vpn_configuration

class Windows81VpnConfiguration(windows_vpn_configuration.WindowsVpnConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new Windows81VpnConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows81VpnConfiguration"
        # Value indicating whether this policy only applies to Windows 8.1. This property is read-only.
        self._apply_only_to_windows81: Optional[bool] = None
        # Windows VPN connection type.
        self._connection_type: Optional[windows_vpn_connection_type.WindowsVpnConnectionType] = None
        # Enable split tunneling for the VPN.
        self._enable_split_tunneling: Optional[bool] = None
        # Login group or domain when connection type is set to Dell SonicWALL Mobile Connection.
        self._login_group_or_domain: Optional[str] = None
        # Proxy Server.
        self._proxy_server: Optional[windows81_vpn_proxy_server.Windows81VpnProxyServer] = None
    
    @property
    def apply_only_to_windows81(self,) -> Optional[bool]:
        """
        Gets the applyOnlyToWindows81 property value. Value indicating whether this policy only applies to Windows 8.1. This property is read-only.
        Returns: Optional[bool]
        """
        return self._apply_only_to_windows81
    
    @apply_only_to_windows81.setter
    def apply_only_to_windows81(self,value: Optional[bool] = None) -> None:
        """
        Sets the applyOnlyToWindows81 property value. Value indicating whether this policy only applies to Windows 8.1. This property is read-only.
        Args:
            value: Value to set for the apply_only_to_windows81 property.
        """
        self._apply_only_to_windows81 = value
    
    @property
    def connection_type(self,) -> Optional[windows_vpn_connection_type.WindowsVpnConnectionType]:
        """
        Gets the connectionType property value. Windows VPN connection type.
        Returns: Optional[windows_vpn_connection_type.WindowsVpnConnectionType]
        """
        return self._connection_type
    
    @connection_type.setter
    def connection_type(self,value: Optional[windows_vpn_connection_type.WindowsVpnConnectionType] = None) -> None:
        """
        Sets the connectionType property value. Windows VPN connection type.
        Args:
            value: Value to set for the connection_type property.
        """
        self._connection_type = value
    
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
    
    @property
    def enable_split_tunneling(self,) -> Optional[bool]:
        """
        Gets the enableSplitTunneling property value. Enable split tunneling for the VPN.
        Returns: Optional[bool]
        """
        return self._enable_split_tunneling
    
    @enable_split_tunneling.setter
    def enable_split_tunneling(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableSplitTunneling property value. Enable split tunneling for the VPN.
        Args:
            value: Value to set for the enable_split_tunneling property.
        """
        self._enable_split_tunneling = value
    
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
    
    @property
    def login_group_or_domain(self,) -> Optional[str]:
        """
        Gets the loginGroupOrDomain property value. Login group or domain when connection type is set to Dell SonicWALL Mobile Connection.
        Returns: Optional[str]
        """
        return self._login_group_or_domain
    
    @login_group_or_domain.setter
    def login_group_or_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the loginGroupOrDomain property value. Login group or domain when connection type is set to Dell SonicWALL Mobile Connection.
        Args:
            value: Value to set for the login_group_or_domain property.
        """
        self._login_group_or_domain = value
    
    @property
    def proxy_server(self,) -> Optional[windows81_vpn_proxy_server.Windows81VpnProxyServer]:
        """
        Gets the proxyServer property value. Proxy Server.
        Returns: Optional[windows81_vpn_proxy_server.Windows81VpnProxyServer]
        """
        return self._proxy_server
    
    @proxy_server.setter
    def proxy_server(self,value: Optional[windows81_vpn_proxy_server.Windows81VpnProxyServer] = None) -> None:
        """
        Sets the proxyServer property value. Proxy Server.
        Args:
            value: Value to set for the proxy_server property.
        """
        self._proxy_server = value
    
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
    

