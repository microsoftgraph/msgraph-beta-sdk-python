from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows10_vpn_proxy_server, windows81_vpn_proxy_server

class VpnProxyServer(AdditionalDataHolder, Parsable):
    """
    VPN Proxy Server.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new vpnProxyServer and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Address.
        self._address: Optional[str] = None
        # Proxy's automatic configuration script url.
        self._automatic_configuration_script_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Port. Valid values 0 to 65535
        self._port: Optional[int] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def address(self,) -> Optional[str]:
        """
        Gets the address property value. Address.
        Returns: Optional[str]
        """
        return self._address
    
    @address.setter
    def address(self,value: Optional[str] = None) -> None:
        """
        Sets the address property value. Address.
        Args:
            value: Value to set for the address property.
        """
        self._address = value
    
    @property
    def automatic_configuration_script_url(self,) -> Optional[str]:
        """
        Gets the automaticConfigurationScriptUrl property value. Proxy's automatic configuration script url.
        Returns: Optional[str]
        """
        return self._automatic_configuration_script_url
    
    @automatic_configuration_script_url.setter
    def automatic_configuration_script_url(self,value: Optional[str] = None) -> None:
        """
        Sets the automaticConfigurationScriptUrl property value. Proxy's automatic configuration script url.
        Args:
            value: Value to set for the automatic_configuration_script_url property.
        """
        self._automatic_configuration_script_url = value
    
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
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def port(self,) -> Optional[int]:
        """
        Gets the port property value. Port. Valid values 0 to 65535
        Returns: Optional[int]
        """
        return self._port
    
    @port.setter
    def port(self,value: Optional[int] = None) -> None:
        """
        Sets the port property value. Port. Valid values 0 to 65535
        Args:
            value: Value to set for the port property.
        """
        self._port = value
    
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
    

