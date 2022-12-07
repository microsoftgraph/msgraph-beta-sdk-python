from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
vpn_authentication_method = lazy_import('msgraph.generated.models.vpn_authentication_method')
vpn_server = lazy_import('msgraph.generated.models.vpn_server')

class VpnConfiguration(device_configuration.DeviceConfiguration):
    @property
    def authentication_method(self,) -> Optional[vpn_authentication_method.VpnAuthenticationMethod]:
        """
        Gets the authenticationMethod property value. VPN Authentication Method.
        Returns: Optional[vpn_authentication_method.VpnAuthenticationMethod]
        """
        return self._authentication_method
    
    @authentication_method.setter
    def authentication_method(self,value: Optional[vpn_authentication_method.VpnAuthenticationMethod] = None) -> None:
        """
        Sets the authenticationMethod property value. VPN Authentication Method.
        Args:
            value: Value to set for the authenticationMethod property.
        """
        self._authentication_method = value
    
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
        Instantiates a new VpnConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.vpnConfiguration"
        # VPN Authentication Method.
        self._authentication_method: Optional[vpn_authentication_method.VpnAuthenticationMethod] = None
        # Connection name displayed to the user.
        self._connection_name: Optional[str] = None
        # Realm when connection type is set to Pulse Secure.
        self._realm: Optional[str] = None
        # Role when connection type is set to Pulse Secure.
        self._role: Optional[str] = None
        # List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
        self._servers: Optional[List[vpn_server.VpnServer]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VpnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VpnConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_method": lambda n : setattr(self, 'authentication_method', n.get_enum_value(vpn_authentication_method.VpnAuthenticationMethod)),
            "connection_name": lambda n : setattr(self, 'connection_name', n.get_str_value()),
            "realm": lambda n : setattr(self, 'realm', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "servers": lambda n : setattr(self, 'servers', n.get_collection_of_object_values(vpn_server.VpnServer)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def realm(self,) -> Optional[str]:
        """
        Gets the realm property value. Realm when connection type is set to Pulse Secure.
        Returns: Optional[str]
        """
        return self._realm
    
    @realm.setter
    def realm(self,value: Optional[str] = None) -> None:
        """
        Sets the realm property value. Realm when connection type is set to Pulse Secure.
        Args:
            value: Value to set for the realm property.
        """
        self._realm = value
    
    @property
    def role(self,) -> Optional[str]:
        """
        Gets the role property value. Role when connection type is set to Pulse Secure.
        Returns: Optional[str]
        """
        return self._role
    
    @role.setter
    def role(self,value: Optional[str] = None) -> None:
        """
        Sets the role property value. Role when connection type is set to Pulse Secure.
        Args:
            value: Value to set for the role property.
        """
        self._role = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_str_value("connectionName", self.connection_name)
        writer.write_str_value("realm", self.realm)
        writer.write_str_value("role", self.role)
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
    

