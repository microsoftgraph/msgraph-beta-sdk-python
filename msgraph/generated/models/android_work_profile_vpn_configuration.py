from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
    from .android_work_profile_vpn_connection_type import AndroidWorkProfileVpnConnectionType
    from .app_list_item import AppListItem
    from .device_configuration import DeviceConfiguration
    from .key_value import KeyValue
    from .key_value_pair import KeyValuePair
    from .vpn_authentication_method import VpnAuthenticationMethod
    from .vpn_proxy_server import VpnProxyServer
    from .vpn_server import VpnServer

from .device_configuration import DeviceConfiguration

@dataclass
class AndroidWorkProfileVpnConfiguration(DeviceConfiguration):
    """
    By providing the configurations in this profile you can instruct the Android Work Profile device to connect to desired VPN endpoint. By specifying the authentication method and security types expected by VPN endpoint you can make the VPN connection seamless for end user.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidWorkProfileVpnConfiguration"
    # Whether or not to enable always-on VPN connection.
    always_on: Optional[bool] = None
    # If always-on VPN connection is enabled, whether or not to lock network traffic when that VPN is disconnected.
    always_on_lockdown: Optional[bool] = None
    # VPN Authentication Method.
    authentication_method: Optional[VpnAuthenticationMethod] = None
    # Connection name displayed to the user.
    connection_name: Optional[str] = None
    # Android Work Profile VPN connection type.
    connection_type: Optional[AndroidWorkProfileVpnConnectionType] = None
    # Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
    custom_data: Optional[List[KeyValue]] = None
    # Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
    custom_key_value_data: Optional[List[KeyValuePair]] = None
    # Fingerprint is a string that will be used to verify the VPN server can be trusted, which is only applicable when connection type is Check Point Capsule VPN.
    fingerprint: Optional[str] = None
    # Identity certificate for client authentication when authentication method is certificate.
    identity_certificate: Optional[AndroidWorkProfileCertificateProfileBase] = None
    # Microsoft Tunnel site ID.
    microsoft_tunnel_site_id: Optional[str] = None
    # List of hosts to exclude using the proxy on connections for. These hosts can use wildcards such as .example.com.
    proxy_exclusion_list: Optional[List[str]] = None
    # Proxy server.
    proxy_server: Optional[VpnProxyServer] = None
    # Realm when connection type is set to Pulse Secure.
    realm: Optional[str] = None
    # Role when connection type is set to Pulse Secure.
    role: Optional[str] = None
    # List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
    servers: Optional[List[VpnServer]] = None
    # Targeted mobile apps. This collection can contain a maximum of 500 elements.
    targeted_mobile_apps: Optional[List[AppListItem]] = None
    # Targeted App package IDs.
    targeted_package_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidWorkProfileVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidWorkProfileVpnConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidWorkProfileVpnConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
        from .android_work_profile_vpn_connection_type import AndroidWorkProfileVpnConnectionType
        from .app_list_item import AppListItem
        from .device_configuration import DeviceConfiguration
        from .key_value import KeyValue
        from .key_value_pair import KeyValuePair
        from .vpn_authentication_method import VpnAuthenticationMethod
        from .vpn_proxy_server import VpnProxyServer
        from .vpn_server import VpnServer

        from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
        from .android_work_profile_vpn_connection_type import AndroidWorkProfileVpnConnectionType
        from .app_list_item import AppListItem
        from .device_configuration import DeviceConfiguration
        from .key_value import KeyValue
        from .key_value_pair import KeyValuePair
        from .vpn_authentication_method import VpnAuthenticationMethod
        from .vpn_proxy_server import VpnProxyServer
        from .vpn_server import VpnServer

        fields: Dict[str, Callable[[Any], None]] = {
            "alwaysOn": lambda n : setattr(self, 'always_on', n.get_bool_value()),
            "alwaysOnLockdown": lambda n : setattr(self, 'always_on_lockdown', n.get_bool_value()),
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(VpnAuthenticationMethod)),
            "connectionName": lambda n : setattr(self, 'connection_name', n.get_str_value()),
            "connectionType": lambda n : setattr(self, 'connection_type', n.get_enum_value(AndroidWorkProfileVpnConnectionType)),
            "customData": lambda n : setattr(self, 'custom_data', n.get_collection_of_object_values(KeyValue)),
            "customKeyValueData": lambda n : setattr(self, 'custom_key_value_data', n.get_collection_of_object_values(KeyValuePair)),
            "fingerprint": lambda n : setattr(self, 'fingerprint', n.get_str_value()),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(AndroidWorkProfileCertificateProfileBase)),
            "microsoftTunnelSiteId": lambda n : setattr(self, 'microsoft_tunnel_site_id', n.get_str_value()),
            "proxyExclusionList": lambda n : setattr(self, 'proxy_exclusion_list', n.get_collection_of_primitive_values(str)),
            "proxyServer": lambda n : setattr(self, 'proxy_server', n.get_object_value(VpnProxyServer)),
            "realm": lambda n : setattr(self, 'realm', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "servers": lambda n : setattr(self, 'servers', n.get_collection_of_object_values(VpnServer)),
            "targetedMobileApps": lambda n : setattr(self, 'targeted_mobile_apps', n.get_collection_of_object_values(AppListItem)),
            "targetedPackageIds": lambda n : setattr(self, 'targeted_package_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("alwaysOn", self.always_on)
        writer.write_bool_value("alwaysOnLockdown", self.always_on_lockdown)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_str_value("connectionName", self.connection_name)
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_collection_of_object_values("customData", self.custom_data)
        writer.write_collection_of_object_values("customKeyValueData", self.custom_key_value_data)
        writer.write_str_value("fingerprint", self.fingerprint)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_str_value("microsoftTunnelSiteId", self.microsoft_tunnel_site_id)
        writer.write_collection_of_primitive_values("proxyExclusionList", self.proxy_exclusion_list)
        writer.write_object_value("proxyServer", self.proxy_server)
        writer.write_str_value("realm", self.realm)
        writer.write_str_value("role", self.role)
        writer.write_collection_of_object_values("servers", self.servers)
        writer.write_collection_of_object_values("targetedMobileApps", self.targeted_mobile_apps)
        writer.write_collection_of_primitive_values("targetedPackageIds", self.targeted_package_ids)
    

