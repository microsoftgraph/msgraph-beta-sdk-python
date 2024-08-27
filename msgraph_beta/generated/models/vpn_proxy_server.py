from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows10_vpn_proxy_server import Windows10VpnProxyServer
    from .windows81_vpn_proxy_server import Windows81VpnProxyServer

@dataclass
class VpnProxyServer(AdditionalDataHolder, BackedModel, Parsable):
    """
    VPN Proxy Server.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

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
    def create_from_discriminator_value(parse_node: ParseNode) -> VpnProxyServer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VpnProxyServer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10VpnProxyServer".casefold():
            from .windows10_vpn_proxy_server import Windows10VpnProxyServer

            return Windows10VpnProxyServer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81VpnProxyServer".casefold():
            from .windows81_vpn_proxy_server import Windows81VpnProxyServer

            return Windows81VpnProxyServer()
        return VpnProxyServer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .windows10_vpn_proxy_server import Windows10VpnProxyServer
        from .windows81_vpn_proxy_server import Windows81VpnProxyServer

        from .windows10_vpn_proxy_server import Windows10VpnProxyServer
        from .windows81_vpn_proxy_server import Windows81VpnProxyServer

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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("address", self.address)
        writer.write_str_value("automaticConfigurationScriptUrl", self.automatic_configuration_script_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("port", self.port)
        writer.write_additional_data_value(self.additional_data)
    

