from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_certificate_profile_base, android_vpn_connection_type, device_configuration, key_value, key_value_pair, vpn_authentication_method, vpn_server

from . import device_configuration

class AndroidVpnConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidVpnConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidVpnConfiguration"
        # VPN Authentication Method.
        self._authentication_method: Optional[vpn_authentication_method.VpnAuthenticationMethod] = None
        # Connection name displayed to the user.
        self._connection_name: Optional[str] = None
        # Android VPN connection type.
        self._connection_type: Optional[android_vpn_connection_type.AndroidVpnConnectionType] = None
        # Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
        self._custom_data: Optional[List[key_value.KeyValue]] = None
        # Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
        self._custom_key_value_data: Optional[List[key_value_pair.KeyValuePair]] = None
        # Fingerprint is a string that will be used to verify the VPN server can be trusted, which is only applicable when connection type is Check Point Capsule VPN.
        self._fingerprint: Optional[str] = None
        # Identity certificate for client authentication when authentication method is certificate.
        self._identity_certificate: Optional[android_certificate_profile_base.AndroidCertificateProfileBase] = None
        # Realm when connection type is set to Pulse Secure.
        self._realm: Optional[str] = None
        # Role when connection type is set to Pulse Secure.
        self._role: Optional[str] = None
        # List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
        self._servers: Optional[List[vpn_server.VpnServer]] = None
    
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
            value: Value to set for the authentication_method property.
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
            value: Value to set for the connection_name property.
        """
        self._connection_name = value
    
    @property
    def connection_type(self,) -> Optional[android_vpn_connection_type.AndroidVpnConnectionType]:
        """
        Gets the connectionType property value. Android VPN connection type.
        Returns: Optional[android_vpn_connection_type.AndroidVpnConnectionType]
        """
        return self._connection_type
    
    @connection_type.setter
    def connection_type(self,value: Optional[android_vpn_connection_type.AndroidVpnConnectionType] = None) -> None:
        """
        Sets the connectionType property value. Android VPN connection type.
        Args:
            value: Value to set for the connection_type property.
        """
        self._connection_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidVpnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidVpnConfiguration()
    
    @property
    def custom_data(self,) -> Optional[List[key_value.KeyValue]]:
        """
        Gets the customData property value. Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
        Returns: Optional[List[key_value.KeyValue]]
        """
        return self._custom_data
    
    @custom_data.setter
    def custom_data(self,value: Optional[List[key_value.KeyValue]] = None) -> None:
        """
        Sets the customData property value. Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
        Args:
            value: Value to set for the custom_data property.
        """
        self._custom_data = value
    
    @property
    def custom_key_value_data(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the customKeyValueData property value. Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._custom_key_value_data
    
    @custom_key_value_data.setter
    def custom_key_value_data(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the customKeyValueData property value. Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
        Args:
            value: Value to set for the custom_key_value_data property.
        """
        self._custom_key_value_data = value
    
    @property
    def fingerprint(self,) -> Optional[str]:
        """
        Gets the fingerprint property value. Fingerprint is a string that will be used to verify the VPN server can be trusted, which is only applicable when connection type is Check Point Capsule VPN.
        Returns: Optional[str]
        """
        return self._fingerprint
    
    @fingerprint.setter
    def fingerprint(self,value: Optional[str] = None) -> None:
        """
        Sets the fingerprint property value. Fingerprint is a string that will be used to verify the VPN server can be trusted, which is only applicable when connection type is Check Point Capsule VPN.
        Args:
            value: Value to set for the fingerprint property.
        """
        self._fingerprint = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def identity_certificate(self,) -> Optional[android_certificate_profile_base.AndroidCertificateProfileBase]:
        """
        Gets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Returns: Optional[android_certificate_profile_base.AndroidCertificateProfileBase]
        """
        return self._identity_certificate
    
    @identity_certificate.setter
    def identity_certificate(self,value: Optional[android_certificate_profile_base.AndroidCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Args:
            value: Value to set for the identity_certificate property.
        """
        self._identity_certificate = value
    
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
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_collection_of_object_values("customData", self.custom_data)
        writer.write_collection_of_object_values("customKeyValueData", self.custom_key_value_data)
        writer.write_str_value("fingerprint", self.fingerprint)
        writer.write_object_value("identityCertificate", self.identity_certificate)
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
    

