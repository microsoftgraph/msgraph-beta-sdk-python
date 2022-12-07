from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_work_profile_certificate_profile_base = lazy_import('msgraph.generated.models.android_work_profile_certificate_profile_base')
android_work_profile_vpn_connection_type = lazy_import('msgraph.generated.models.android_work_profile_vpn_connection_type')
app_list_item = lazy_import('msgraph.generated.models.app_list_item')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
key_value = lazy_import('msgraph.generated.models.key_value')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
vpn_authentication_method = lazy_import('msgraph.generated.models.vpn_authentication_method')
vpn_proxy_server = lazy_import('msgraph.generated.models.vpn_proxy_server')
vpn_server = lazy_import('msgraph.generated.models.vpn_server')

class AndroidWorkProfileVpnConfiguration(device_configuration.DeviceConfiguration):
    @property
    def always_on(self,) -> Optional[bool]:
        """
        Gets the alwaysOn property value. Whether or not to enable always-on VPN connection.
        Returns: Optional[bool]
        """
        return self._always_on
    
    @always_on.setter
    def always_on(self,value: Optional[bool] = None) -> None:
        """
        Sets the alwaysOn property value. Whether or not to enable always-on VPN connection.
        Args:
            value: Value to set for the alwaysOn property.
        """
        self._always_on = value
    
    @property
    def always_on_lockdown(self,) -> Optional[bool]:
        """
        Gets the alwaysOnLockdown property value. If always-on VPN connection is enabled, whether or not to lock network traffic when that VPN is disconnected.
        Returns: Optional[bool]
        """
        return self._always_on_lockdown
    
    @always_on_lockdown.setter
    def always_on_lockdown(self,value: Optional[bool] = None) -> None:
        """
        Sets the alwaysOnLockdown property value. If always-on VPN connection is enabled, whether or not to lock network traffic when that VPN is disconnected.
        Args:
            value: Value to set for the alwaysOnLockdown property.
        """
        self._always_on_lockdown = value
    
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
    
    @property
    def connection_type(self,) -> Optional[android_work_profile_vpn_connection_type.AndroidWorkProfileVpnConnectionType]:
        """
        Gets the connectionType property value. Android Work Profile VPN connection type.
        Returns: Optional[android_work_profile_vpn_connection_type.AndroidWorkProfileVpnConnectionType]
        """
        return self._connection_type
    
    @connection_type.setter
    def connection_type(self,value: Optional[android_work_profile_vpn_connection_type.AndroidWorkProfileVpnConnectionType] = None) -> None:
        """
        Sets the connectionType property value. Android Work Profile VPN connection type.
        Args:
            value: Value to set for the connectionType property.
        """
        self._connection_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidWorkProfileVpnConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidWorkProfileVpnConfiguration"
        # Whether or not to enable always-on VPN connection.
        self._always_on: Optional[bool] = None
        # If always-on VPN connection is enabled, whether or not to lock network traffic when that VPN is disconnected.
        self._always_on_lockdown: Optional[bool] = None
        # VPN Authentication Method.
        self._authentication_method: Optional[vpn_authentication_method.VpnAuthenticationMethod] = None
        # Connection name displayed to the user.
        self._connection_name: Optional[str] = None
        # Android Work Profile VPN connection type.
        self._connection_type: Optional[android_work_profile_vpn_connection_type.AndroidWorkProfileVpnConnectionType] = None
        # Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
        self._custom_data: Optional[List[key_value.KeyValue]] = None
        # Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
        self._custom_key_value_data: Optional[List[key_value_pair.KeyValuePair]] = None
        # Fingerprint is a string that will be used to verify the VPN server can be trusted, which is only applicable when connection type is Check Point Capsule VPN.
        self._fingerprint: Optional[str] = None
        # Identity certificate for client authentication when authentication method is certificate.
        self._identity_certificate: Optional[android_work_profile_certificate_profile_base.AndroidWorkProfileCertificateProfileBase] = None
        # Microsoft Tunnel site ID.
        self._microsoft_tunnel_site_id: Optional[str] = None
        # Proxy server.
        self._proxy_server: Optional[vpn_proxy_server.VpnProxyServer] = None
        # Realm when connection type is set to Pulse Secure.
        self._realm: Optional[str] = None
        # Role when connection type is set to Pulse Secure.
        self._role: Optional[str] = None
        # List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
        self._servers: Optional[List[vpn_server.VpnServer]] = None
        # Targeted mobile apps. This collection can contain a maximum of 500 elements.
        self._targeted_mobile_apps: Optional[List[app_list_item.AppListItem]] = None
        # Targeted App package IDs.
        self._targeted_package_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidWorkProfileVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidWorkProfileVpnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidWorkProfileVpnConfiguration()
    
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
            value: Value to set for the customData property.
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
            value: Value to set for the customKeyValueData property.
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
        fields = {
            "always_on": lambda n : setattr(self, 'always_on', n.get_bool_value()),
            "always_on_lockdown": lambda n : setattr(self, 'always_on_lockdown', n.get_bool_value()),
            "authentication_method": lambda n : setattr(self, 'authentication_method', n.get_enum_value(vpn_authentication_method.VpnAuthenticationMethod)),
            "connection_name": lambda n : setattr(self, 'connection_name', n.get_str_value()),
            "connection_type": lambda n : setattr(self, 'connection_type', n.get_enum_value(android_work_profile_vpn_connection_type.AndroidWorkProfileVpnConnectionType)),
            "custom_data": lambda n : setattr(self, 'custom_data', n.get_collection_of_object_values(key_value.KeyValue)),
            "custom_key_value_data": lambda n : setattr(self, 'custom_key_value_data', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "fingerprint": lambda n : setattr(self, 'fingerprint', n.get_str_value()),
            "identity_certificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(android_work_profile_certificate_profile_base.AndroidWorkProfileCertificateProfileBase)),
            "microsoft_tunnel_site_id": lambda n : setattr(self, 'microsoft_tunnel_site_id', n.get_str_value()),
            "proxy_server": lambda n : setattr(self, 'proxy_server', n.get_object_value(vpn_proxy_server.VpnProxyServer)),
            "realm": lambda n : setattr(self, 'realm', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "servers": lambda n : setattr(self, 'servers', n.get_collection_of_object_values(vpn_server.VpnServer)),
            "targeted_mobile_apps": lambda n : setattr(self, 'targeted_mobile_apps', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "targeted_package_ids": lambda n : setattr(self, 'targeted_package_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_certificate(self,) -> Optional[android_work_profile_certificate_profile_base.AndroidWorkProfileCertificateProfileBase]:
        """
        Gets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Returns: Optional[android_work_profile_certificate_profile_base.AndroidWorkProfileCertificateProfileBase]
        """
        return self._identity_certificate
    
    @identity_certificate.setter
    def identity_certificate(self,value: Optional[android_work_profile_certificate_profile_base.AndroidWorkProfileCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Args:
            value: Value to set for the identityCertificate property.
        """
        self._identity_certificate = value
    
    @property
    def microsoft_tunnel_site_id(self,) -> Optional[str]:
        """
        Gets the microsoftTunnelSiteId property value. Microsoft Tunnel site ID.
        Returns: Optional[str]
        """
        return self._microsoft_tunnel_site_id
    
    @microsoft_tunnel_site_id.setter
    def microsoft_tunnel_site_id(self,value: Optional[str] = None) -> None:
        """
        Sets the microsoftTunnelSiteId property value. Microsoft Tunnel site ID.
        Args:
            value: Value to set for the microsoftTunnelSiteId property.
        """
        self._microsoft_tunnel_site_id = value
    
    @property
    def proxy_server(self,) -> Optional[vpn_proxy_server.VpnProxyServer]:
        """
        Gets the proxyServer property value. Proxy server.
        Returns: Optional[vpn_proxy_server.VpnProxyServer]
        """
        return self._proxy_server
    
    @proxy_server.setter
    def proxy_server(self,value: Optional[vpn_proxy_server.VpnProxyServer] = None) -> None:
        """
        Sets the proxyServer property value. Proxy server.
        Args:
            value: Value to set for the proxyServer property.
        """
        self._proxy_server = value
    
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
        writer.write_object_value("proxyServer", self.proxy_server)
        writer.write_str_value("realm", self.realm)
        writer.write_str_value("role", self.role)
        writer.write_collection_of_object_values("servers", self.servers)
        writer.write_collection_of_object_values("targetedMobileApps", self.targeted_mobile_apps)
        writer.write_collection_of_primitive_values("targetedPackageIds", self.targeted_package_ids)
    
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
    
    @property
    def targeted_mobile_apps(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the targetedMobileApps property value. Targeted mobile apps. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._targeted_mobile_apps
    
    @targeted_mobile_apps.setter
    def targeted_mobile_apps(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the targetedMobileApps property value. Targeted mobile apps. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the targetedMobileApps property.
        """
        self._targeted_mobile_apps = value
    
    @property
    def targeted_package_ids(self,) -> Optional[List[str]]:
        """
        Gets the targetedPackageIds property value. Targeted App package IDs.
        Returns: Optional[List[str]]
        """
        return self._targeted_package_ids
    
    @targeted_package_ids.setter
    def targeted_package_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the targetedPackageIds property value. Targeted App package IDs.
        Args:
            value: Value to set for the targetedPackageIds property.
        """
        self._targeted_package_ids = value
    

