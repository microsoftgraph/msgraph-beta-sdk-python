from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
vpn_server = lazy_import('msgraph.generated.models.vpn_server')

class WindowsVpnConfiguration(device_configuration.DeviceConfiguration):
    @property
    def connection_name(self,) -> Optional[str]:
        """
        Gets the connectionName property value. Connection name displayed to the user.
        Returns: Optional[str]
        """
        return self._connection_name
    
    @connection_name.setter
    def connection_name(self,value: Optional[str] = None) -> None:
        """
        Sets the connectionName property value. Connection name displayed to the user.
        Args:
            value: Value to set for the connectionName property.
        """
        self._connection_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsVpnConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsVpnConfiguration"
        # Connection name displayed to the user.
        self._connection_name: Optional[str] = None
        # Custom XML commands that configures the VPN connection. (UTF8 encoded byte array)
        self._custom_xml: Optional[bytes] = None
        # List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
        self._servers: Optional[List[vpn_server.VpnServer]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsVpnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsVpnConfiguration()
    
    @property
    def custom_xml(self,) -> Optional[bytes]:
        """
        Gets the customXml property value. Custom XML commands that configures the VPN connection. (UTF8 encoded byte array)
        Returns: Optional[bytes]
        """
        return self._custom_xml
    
    @custom_xml.setter
    def custom_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the customXml property value. Custom XML commands that configures the VPN connection. (UTF8 encoded byte array)
        Args:
            value: Value to set for the customXml property.
        """
        self._custom_xml = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connection_name": lambda n : setattr(self, 'connection_name', n.get_str_value()),
            "custom_xml": lambda n : setattr(self, 'custom_xml', n.get_bytes_value()),
            "servers": lambda n : setattr(self, 'servers', n.get_collection_of_object_values(vpn_server.VpnServer)),
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
        writer.write_str_value("connectionName", self.connection_name)
        writer.write_object_value("customXml", self.custom_xml)
        writer.write_collection_of_object_values("servers", self.servers)
    
    @property
    def servers(self,) -> Optional[List[vpn_server.VpnServer]]:
        """
        Gets the servers property value. List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[vpn_server.VpnServer]]
        """
        return self._servers
    
    @servers.setter
    def servers(self,value: Optional[List[vpn_server.VpnServer]] = None) -> None:
        """
        Sets the servers property value. List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the servers property.
        """
        self._servers = value
    

