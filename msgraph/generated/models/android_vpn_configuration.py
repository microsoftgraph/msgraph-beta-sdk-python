from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_certificate_profile_base, android_vpn_connection_type, device_configuration, key_value, key_value_pair, vpn_authentication_method, vpn_server

from . import device_configuration

@dataclass
class AndroidVpnConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.androidVpnConfiguration"
    # VPN Authentication Method.
    authentication_method: Optional[vpn_authentication_method.VpnAuthenticationMethod] = None
    # Connection name displayed to the user.
    connection_name: Optional[str] = None
    # Android VPN connection type.
    connection_type: Optional[android_vpn_connection_type.AndroidVpnConnectionType] = None
    # Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
    custom_data: Optional[List[key_value.KeyValue]] = None
    # Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
    custom_key_value_data: Optional[List[key_value_pair.KeyValuePair]] = None
    # Fingerprint is a string that will be used to verify the VPN server can be trusted, which is only applicable when connection type is Check Point Capsule VPN.
    fingerprint: Optional[str] = None
    # Identity certificate for client authentication when authentication method is certificate.
    identity_certificate: Optional[android_certificate_profile_base.AndroidCertificateProfileBase] = None
    # Realm when connection type is set to Pulse Secure.
    realm: Optional[str] = None
    # Role when connection type is set to Pulse Secure.
    role: Optional[str] = None
    # List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
    servers: Optional[List[vpn_server.VpnServer]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidVpnConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidVpnConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_certificate_profile_base, android_vpn_connection_type, device_configuration, key_value, key_value_pair, vpn_authentication_method, vpn_server

        from . import android_certificate_profile_base, android_vpn_connection_type, device_configuration, key_value, key_value_pair, vpn_authentication_method, vpn_server

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(vpn_authentication_method.VpnAuthenticationMethod)),
            "connectionName": lambda n : setattr(self, 'connection_name', n.get_str_value()),
            "connectionType": lambda n : setattr(self, 'connection_type', n.get_enum_value(android_vpn_connection_type.AndroidVpnConnectionType)),
            "customData": lambda n : setattr(self, 'custom_data', n.get_collection_of_object_values(key_value.KeyValue)),
            "customKeyValueData": lambda n : setattr(self, 'custom_key_value_data', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "fingerprint": lambda n : setattr(self, 'fingerprint', n.get_str_value()),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(android_certificate_profile_base.AndroidCertificateProfileBase)),
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
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_collection_of_object_values("customData", self.custom_data)
        writer.write_collection_of_object_values("customKeyValueData", self.custom_key_value_data)
        writer.write_str_value("fingerprint", self.fingerprint)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_str_value("realm", self.realm)
        writer.write_str_value("role", self.role)
        writer.write_collection_of_object_values("servers", self.servers)
    

