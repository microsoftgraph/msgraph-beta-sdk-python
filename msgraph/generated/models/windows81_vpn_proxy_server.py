from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

vpn_proxy_server = lazy_import('msgraph.generated.models.vpn_proxy_server')

class Windows81VpnProxyServer(vpn_proxy_server.VpnProxyServer):
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
            value: Value to set for the automaticallyDetectProxySettings property.
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
            value: Value to set for the bypassProxyServerForLocalAddress property.
        """
        self._bypass_proxy_server_for_local_address = value
    
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
        fields = {
            "automatically_detect_proxy_settings": lambda n : setattr(self, 'automatically_detect_proxy_settings', n.get_bool_value()),
            "bypass_proxy_server_for_local_address": lambda n : setattr(self, 'bypass_proxy_server_for_local_address', n.get_bool_value()),
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
    

