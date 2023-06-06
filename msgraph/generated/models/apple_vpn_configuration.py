from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_vpn_connection_type, device_configuration, iosik_ev2_vpn_configuration, ios_vpn_configuration, key_value, key_value_pair, mac_o_s_vpn_configuration, vpn_authentication_method, vpn_on_demand_rule, vpn_provider_type, vpn_proxy_server, vpn_server

from . import device_configuration

@dataclass
class AppleVpnConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.appleVpnConfiguration"
    # Associated Domains
    associated_domains: Optional[List[str]] = None
    # VPN Authentication Method.
    authentication_method: Optional[vpn_authentication_method.VpnAuthenticationMethod] = None
    # Connection name displayed to the user.
    connection_name: Optional[str] = None
    # Apple VPN connection type.
    connection_type: Optional[apple_vpn_connection_type.AppleVpnConnectionType] = None
    # Custom data when connection type is set to Custom VPN. Use this field to enable functionality not supported by Intune, but available in your VPN solution. Contact your VPN vendor to learn how to add these key/value pairs. This collection can contain a maximum of 25 elements.
    custom_data: Optional[List[key_value.KeyValue]] = None
    # Custom data when connection type is set to Custom VPN. Use this field to enable functionality not supported by Intune, but available in your VPN solution. Contact your VPN vendor to learn how to add these key/value pairs. This collection can contain a maximum of 25 elements.
    custom_key_value_data: Optional[List[key_value_pair.KeyValuePair]] = None
    # Toggle to prevent user from disabling automatic VPN in the Settings app
    disable_on_demand_user_override: Optional[bool] = None
    # Whether to disconnect after on-demand connection idles
    disconnect_on_idle: Optional[bool] = None
    # The length of time in seconds to wait before disconnecting an on-demand connection. Valid values 0 to 65535
    disconnect_on_idle_timer_in_seconds: Optional[int] = None
    # Setting this to true creates Per-App VPN payload which can later be associated with Apps that can trigger this VPN conneciton on the end user's iOS device.
    enable_per_app: Optional[bool] = None
    # Send all network traffic through VPN.
    enable_split_tunneling: Optional[bool] = None
    # Domains that are accessed through the public internet instead of through VPN, even when per-app VPN is activated
    excluded_domains: Optional[List[str]] = None
    # Identifier provided by VPN vendor when connection type is set to Custom VPN. For example: Cisco AnyConnect uses an identifier of the form com.cisco.anyconnect.applevpn.plugin
    identifier: Optional[str] = None
    # Login group or domain when connection type is set to Dell SonicWALL Mobile Connection.
    login_group_or_domain: Optional[str] = None
    # On-Demand Rules. This collection can contain a maximum of 500 elements.
    on_demand_rules: Optional[List[vpn_on_demand_rule.VpnOnDemandRule]] = None
    # Opt-In to sharing the device's Id to third-party vpn clients for use during network access control validation.
    opt_in_to_device_id_sharing: Optional[bool] = None
    # Provider type for per-app VPN. Possible values are: notConfigured, appProxy, packetTunnel.
    provider_type: Optional[vpn_provider_type.VpnProviderType] = None
    # Proxy Server.
    proxy_server: Optional[vpn_proxy_server.VpnProxyServer] = None
    # Realm when connection type is set to Pulse Secure.
    realm: Optional[str] = None
    # Role when connection type is set to Pulse Secure.
    role: Optional[str] = None
    # Safari domains when this VPN per App setting is enabled. In addition to the apps associated with this VPN, Safari domains specified here will also be able to trigger this VPN connection.
    safari_domains: Optional[List[str]] = None
    # VPN Server definition.
    server: Optional[vpn_server.VpnServer] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppleVpnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.iosikEv2VpnConfiguration":
                from . import iosik_ev2_vpn_configuration

                return iosik_ev2_vpn_configuration.IosikEv2VpnConfiguration()
            if mapping_value == "#microsoft.graph.iosVpnConfiguration":
                from . import ios_vpn_configuration

                return ios_vpn_configuration.IosVpnConfiguration()
            if mapping_value == "#microsoft.graph.macOSVpnConfiguration":
                from . import mac_o_s_vpn_configuration

                return mac_o_s_vpn_configuration.MacOSVpnConfiguration()
        return AppleVpnConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_vpn_connection_type, device_configuration, iosik_ev2_vpn_configuration, ios_vpn_configuration, key_value, key_value_pair, mac_o_s_vpn_configuration, vpn_authentication_method, vpn_on_demand_rule, vpn_provider_type, vpn_proxy_server, vpn_server

        fields: Dict[str, Callable[[Any], None]] = {
            "associatedDomains": lambda n : setattr(self, 'associated_domains', n.get_collection_of_primitive_values(str)),
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(vpn_authentication_method.VpnAuthenticationMethod)),
            "connectionName": lambda n : setattr(self, 'connection_name', n.get_str_value()),
            "connectionType": lambda n : setattr(self, 'connection_type', n.get_enum_value(apple_vpn_connection_type.AppleVpnConnectionType)),
            "customData": lambda n : setattr(self, 'custom_data', n.get_collection_of_object_values(key_value.KeyValue)),
            "customKeyValueData": lambda n : setattr(self, 'custom_key_value_data', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "disableOnDemandUserOverride": lambda n : setattr(self, 'disable_on_demand_user_override', n.get_bool_value()),
            "disconnectOnIdle": lambda n : setattr(self, 'disconnect_on_idle', n.get_bool_value()),
            "disconnectOnIdleTimerInSeconds": lambda n : setattr(self, 'disconnect_on_idle_timer_in_seconds', n.get_int_value()),
            "enablePerApp": lambda n : setattr(self, 'enable_per_app', n.get_bool_value()),
            "enableSplitTunneling": lambda n : setattr(self, 'enable_split_tunneling', n.get_bool_value()),
            "excludedDomains": lambda n : setattr(self, 'excluded_domains', n.get_collection_of_primitive_values(str)),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "loginGroupOrDomain": lambda n : setattr(self, 'login_group_or_domain', n.get_str_value()),
            "onDemandRules": lambda n : setattr(self, 'on_demand_rules', n.get_collection_of_object_values(vpn_on_demand_rule.VpnOnDemandRule)),
            "optInToDeviceIdSharing": lambda n : setattr(self, 'opt_in_to_device_id_sharing', n.get_bool_value()),
            "providerType": lambda n : setattr(self, 'provider_type', n.get_enum_value(vpn_provider_type.VpnProviderType)),
            "proxyServer": lambda n : setattr(self, 'proxy_server', n.get_object_value(vpn_proxy_server.VpnProxyServer)),
            "realm": lambda n : setattr(self, 'realm', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "safariDomains": lambda n : setattr(self, 'safari_domains', n.get_collection_of_primitive_values(str)),
            "server": lambda n : setattr(self, 'server', n.get_object_value(vpn_server.VpnServer)),
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
        writer.write_collection_of_primitive_values("associatedDomains", self.associated_domains)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_str_value("connectionName", self.connection_name)
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_collection_of_object_values("customData", self.custom_data)
        writer.write_collection_of_object_values("customKeyValueData", self.custom_key_value_data)
        writer.write_bool_value("disableOnDemandUserOverride", self.disable_on_demand_user_override)
        writer.write_bool_value("disconnectOnIdle", self.disconnect_on_idle)
        writer.write_int_value("disconnectOnIdleTimerInSeconds", self.disconnect_on_idle_timer_in_seconds)
        writer.write_bool_value("enablePerApp", self.enable_per_app)
        writer.write_bool_value("enableSplitTunneling", self.enable_split_tunneling)
        writer.write_collection_of_primitive_values("excludedDomains", self.excluded_domains)
        writer.write_str_value("identifier", self.identifier)
        writer.write_str_value("loginGroupOrDomain", self.login_group_or_domain)
        writer.write_collection_of_object_values("onDemandRules", self.on_demand_rules)
        writer.write_bool_value("optInToDeviceIdSharing", self.opt_in_to_device_id_sharing)
        writer.write_enum_value("providerType", self.provider_type)
        writer.write_object_value("proxyServer", self.proxy_server)
        writer.write_str_value("realm", self.realm)
        writer.write_str_value("role", self.role)
        writer.write_collection_of_primitive_values("safariDomains", self.safari_domains)
        writer.write_object_value("server", self.server)
    

