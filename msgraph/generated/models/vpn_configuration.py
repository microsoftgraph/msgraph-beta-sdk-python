from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_owner_vpn_configuration, device_configuration, vpn_authentication_method, vpn_server

from . import device_configuration

@dataclass
class VpnConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.vpnConfiguration"
    # VPN Authentication Method.
    authentication_method: Optional[vpn_authentication_method.VpnAuthenticationMethod] = None
    # Connection name displayed to the user.
    connection_name: Optional[str] = None
    # Realm when connection type is set to Pulse Secure.
    realm: Optional[str] = None
    # Role when connection type is set to Pulse Secure.
    role: Optional[str] = None
    # List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
    servers: Optional[List[vpn_server.VpnServer]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VpnConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerVpnConfiguration".casefold():
            from . import android_device_owner_vpn_configuration

            return android_device_owner_vpn_configuration.AndroidDeviceOwnerVpnConfiguration()
        return VpnConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_device_owner_vpn_configuration, device_configuration, vpn_authentication_method, vpn_server

        from . import android_device_owner_vpn_configuration, device_configuration, vpn_authentication_method, vpn_server

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(vpn_authentication_method.VpnAuthenticationMethod)),
            "connectionName": lambda n : setattr(self, 'connection_name', n.get_str_value()),
            "realm": lambda n : setattr(self, 'realm', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_str_value("connectionName", self.connection_name)
        writer.write_str_value("realm", self.realm)
        writer.write_str_value("role", self.role)
        writer.write_collection_of_object_values("servers", self.servers)
    

