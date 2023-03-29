from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import vpn_proxy_server

from . import vpn_proxy_server

class Windows81VpnProxyServer(vpn_proxy_server.VpnProxyServer):
    def __init__(self,) -> None:
        """
        Instantiates a new Windows81VpnProxyServer and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows81VpnProxyServer"
        # Automatically detect proxy settings.
        self._automatically_detect_proxy_settings: Optional[bool] = None
        # Bypass proxy server for local address.
        self._bypass_proxy_server_for_local_address: Optional[bool] = None
    
    @property
    def automatically_detect_proxy_settings(self,) -> Optional[bool]:
        """
        Gets the automaticallyDetectProxySettings property value. Automatically detect proxy settings.
        Returns: Optional[bool]
        """
        return self._automatically_detect_proxy_settings
    
    @automatically_detect_proxy_settings.setter
    def automatically_detect_proxy_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the automaticallyDetectProxySettings property value. Automatically detect proxy settings.
        Args:
            value: Value to set for the automatically_detect_proxy_settings property.
        """
        self._automatically_detect_proxy_settings = value
    
    @property
    def bypass_proxy_server_for_local_address(self,) -> Optional[bool]:
        """
        Gets the bypassProxyServerForLocalAddress property value. Bypass proxy server for local address.
        Returns: Optional[bool]
        """
        return self._bypass_proxy_server_for_local_address
    
    @bypass_proxy_server_for_local_address.setter
    def bypass_proxy_server_for_local_address(self,value: Optional[bool] = None) -> None:
        """
        Sets the bypassProxyServerForLocalAddress property value. Bypass proxy server for local address.
        Args:
            value: Value to set for the bypass_proxy_server_for_local_address property.
        """
        self._bypass_proxy_server_for_local_address = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows81VpnProxyServer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows81VpnProxyServer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows81VpnProxyServer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import vpn_proxy_server

        fields: Dict[str, Callable[[Any], None]] = {
            "automaticallyDetectProxySettings": lambda n : setattr(self, 'automatically_detect_proxy_settings', n.get_bool_value()),
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
        writer.write_bool_value("automaticallyDetectProxySettings", self.automatically_detect_proxy_settings)
        writer.write_bool_value("bypassProxyServerForLocalAddress", self.bypass_proxy_server_for_local_address)
    

