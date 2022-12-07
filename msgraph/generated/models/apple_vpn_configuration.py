from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

apple_vpn_connection_type = lazy_import('msgraph.generated.models.apple_vpn_connection_type')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
key_value = lazy_import('msgraph.generated.models.key_value')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
vpn_authentication_method = lazy_import('msgraph.generated.models.vpn_authentication_method')
vpn_on_demand_rule = lazy_import('msgraph.generated.models.vpn_on_demand_rule')
vpn_provider_type = lazy_import('msgraph.generated.models.vpn_provider_type')
vpn_proxy_server = lazy_import('msgraph.generated.models.vpn_proxy_server')
vpn_server = lazy_import('msgraph.generated.models.vpn_server')

class AppleVpnConfiguration(device_configuration.DeviceConfiguration):
    @property
    def associated_domains(self,) -> Optional[List[str]]:
        """
        Gets the associatedDomains property value. Associated Domains
        Returns: Optional[List[str]]
        """
        return self._associated_domains
    
    @associated_domains.setter
    def associated_domains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the associatedDomains property value. Associated Domains
        Args:
            value: Value to set for the associatedDomains property.
        """
        self._associated_domains = value
    
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
    def connection_type(self,) -> Optional[apple_vpn_connection_type.AppleVpnConnectionType]:
        """
        Gets the connectionType property value. Apple VPN connection type.
        Returns: Optional[apple_vpn_connection_type.AppleVpnConnectionType]
        """
        return self._connection_type
    
    @connection_type.setter
    def connection_type(self,value: Optional[apple_vpn_connection_type.AppleVpnConnectionType] = None) -> None:
        """
        Sets the connectionType property value. Apple VPN connection type.
        Args:
            value: Value to set for the connectionType property.
        """
        self._connection_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AppleVpnConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.appleVpnConfiguration"
        # Associated Domains
        self._associated_domains: Optional[List[str]] = None
        # VPN Authentication Method.
        self._authentication_method: Optional[vpn_authentication_method.VpnAuthenticationMethod] = None
        # Connection name displayed to the user.
        self._connection_name: Optional[str] = None
        # Apple VPN connection type.
        self._connection_type: Optional[apple_vpn_connection_type.AppleVpnConnectionType] = None
        # Custom data when connection type is set to Custom VPN. Use this field to enable functionality not supported by Intune, but available in your VPN solution. Contact your VPN vendor to learn how to add these key/value pairs. This collection can contain a maximum of 25 elements.
        self._custom_data: Optional[List[key_value.KeyValue]] = None
        # Custom data when connection type is set to Custom VPN. Use this field to enable functionality not supported by Intune, but available in your VPN solution. Contact your VPN vendor to learn how to add these key/value pairs. This collection can contain a maximum of 25 elements.
        self._custom_key_value_data: Optional[List[key_value_pair.KeyValuePair]] = None
        # Toggle to prevent user from disabling automatic VPN in the Settings app
        self._disable_on_demand_user_override: Optional[bool] = None
        # Whether to disconnect after on-demand connection idles
        self._disconnect_on_idle: Optional[bool] = None
        # The length of time in seconds to wait before disconnecting an on-demand connection. Valid values 0 to 65535
        self._disconnect_on_idle_timer_in_seconds: Optional[int] = None
        # Setting this to true creates Per-App VPN payload which can later be associated with Apps that can trigger this VPN conneciton on the end user's iOS device.
        self._enable_per_app: Optional[bool] = None
        # Send all network traffic through VPN.
        self._enable_split_tunneling: Optional[bool] = None
        # Domains that are accessed through the public internet instead of through VPN, even when per-app VPN is activated
        self._excluded_domains: Optional[List[str]] = None
        # Identifier provided by VPN vendor when connection type is set to Custom VPN. For example: Cisco AnyConnect uses an identifier of the form com.cisco.anyconnect.applevpn.plugin
        self._identifier: Optional[str] = None
        # Login group or domain when connection type is set to Dell SonicWALL Mobile Connection.
        self._login_group_or_domain: Optional[str] = None
        # On-Demand Rules. This collection can contain a maximum of 500 elements.
        self._on_demand_rules: Optional[List[vpn_on_demand_rule.VpnOnDemandRule]] = None
        # Opt-In to sharing the device's Id to third-party vpn clients for use during network access control validation.
        self._opt_in_to_device_id_sharing: Optional[bool] = None
        # Provider type for per-app VPN. Possible values are: notConfigured, appProxy, packetTunnel.
        self._provider_type: Optional[vpn_provider_type.VpnProviderType] = None
        # Proxy Server.
        self._proxy_server: Optional[vpn_proxy_server.VpnProxyServer] = None
        # Realm when connection type is set to Pulse Secure.
        self._realm: Optional[str] = None
        # Role when connection type is set to Pulse Secure.
        self._role: Optional[str] = None
        # Safari domains when this VPN per App setting is enabled. In addition to the apps associated with this VPN, Safari domains specified here will also be able to trigger this VPN connection.
        self._safari_domains: Optional[List[str]] = None
        # VPN Server definition.
        self._server: Optional[vpn_server.VpnServer] = None
    
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
        return AppleVpnConfiguration()
    
    @property
    def custom_data(self,) -> Optional[List[key_value.KeyValue]]:
        """
        Gets the customData property value. Custom data when connection type is set to Custom VPN. Use this field to enable functionality not supported by Intune, but available in your VPN solution. Contact your VPN vendor to learn how to add these key/value pairs. This collection can contain a maximum of 25 elements.
        Returns: Optional[List[key_value.KeyValue]]
        """
        return self._custom_data
    
    @custom_data.setter
    def custom_data(self,value: Optional[List[key_value.KeyValue]] = None) -> None:
        """
        Sets the customData property value. Custom data when connection type is set to Custom VPN. Use this field to enable functionality not supported by Intune, but available in your VPN solution. Contact your VPN vendor to learn how to add these key/value pairs. This collection can contain a maximum of 25 elements.
        Args:
            value: Value to set for the customData property.
        """
        self._custom_data = value
    
    @property
    def custom_key_value_data(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the customKeyValueData property value. Custom data when connection type is set to Custom VPN. Use this field to enable functionality not supported by Intune, but available in your VPN solution. Contact your VPN vendor to learn how to add these key/value pairs. This collection can contain a maximum of 25 elements.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._custom_key_value_data
    
    @custom_key_value_data.setter
    def custom_key_value_data(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the customKeyValueData property value. Custom data when connection type is set to Custom VPN. Use this field to enable functionality not supported by Intune, but available in your VPN solution. Contact your VPN vendor to learn how to add these key/value pairs. This collection can contain a maximum of 25 elements.
        Args:
            value: Value to set for the customKeyValueData property.
        """
        self._custom_key_value_data = value
    
    @property
    def disable_on_demand_user_override(self,) -> Optional[bool]:
        """
        Gets the disableOnDemandUserOverride property value. Toggle to prevent user from disabling automatic VPN in the Settings app
        Returns: Optional[bool]
        """
        return self._disable_on_demand_user_override
    
    @disable_on_demand_user_override.setter
    def disable_on_demand_user_override(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableOnDemandUserOverride property value. Toggle to prevent user from disabling automatic VPN in the Settings app
        Args:
            value: Value to set for the disableOnDemandUserOverride property.
        """
        self._disable_on_demand_user_override = value
    
    @property
    def disconnect_on_idle(self,) -> Optional[bool]:
        """
        Gets the disconnectOnIdle property value. Whether to disconnect after on-demand connection idles
        Returns: Optional[bool]
        """
        return self._disconnect_on_idle
    
    @disconnect_on_idle.setter
    def disconnect_on_idle(self,value: Optional[bool] = None) -> None:
        """
        Sets the disconnectOnIdle property value. Whether to disconnect after on-demand connection idles
        Args:
            value: Value to set for the disconnectOnIdle property.
        """
        self._disconnect_on_idle = value
    
    @property
    def disconnect_on_idle_timer_in_seconds(self,) -> Optional[int]:
        """
        Gets the disconnectOnIdleTimerInSeconds property value. The length of time in seconds to wait before disconnecting an on-demand connection. Valid values 0 to 65535
        Returns: Optional[int]
        """
        return self._disconnect_on_idle_timer_in_seconds
    
    @disconnect_on_idle_timer_in_seconds.setter
    def disconnect_on_idle_timer_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the disconnectOnIdleTimerInSeconds property value. The length of time in seconds to wait before disconnecting an on-demand connection. Valid values 0 to 65535
        Args:
            value: Value to set for the disconnectOnIdleTimerInSeconds property.
        """
        self._disconnect_on_idle_timer_in_seconds = value
    
    @property
    def enable_per_app(self,) -> Optional[bool]:
        """
        Gets the enablePerApp property value. Setting this to true creates Per-App VPN payload which can later be associated with Apps that can trigger this VPN conneciton on the end user's iOS device.
        Returns: Optional[bool]
        """
        return self._enable_per_app
    
    @enable_per_app.setter
    def enable_per_app(self,value: Optional[bool] = None) -> None:
        """
        Sets the enablePerApp property value. Setting this to true creates Per-App VPN payload which can later be associated with Apps that can trigger this VPN conneciton on the end user's iOS device.
        Args:
            value: Value to set for the enablePerApp property.
        """
        self._enable_per_app = value
    
    @property
    def enable_split_tunneling(self,) -> Optional[bool]:
        """
        Gets the enableSplitTunneling property value. Send all network traffic through VPN.
        Returns: Optional[bool]
        """
        return self._enable_split_tunneling
    
    @enable_split_tunneling.setter
    def enable_split_tunneling(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableSplitTunneling property value. Send all network traffic through VPN.
        Args:
            value: Value to set for the enableSplitTunneling property.
        """
        self._enable_split_tunneling = value
    
    @property
    def excluded_domains(self,) -> Optional[List[str]]:
        """
        Gets the excludedDomains property value. Domains that are accessed through the public internet instead of through VPN, even when per-app VPN is activated
        Returns: Optional[List[str]]
        """
        return self._excluded_domains
    
    @excluded_domains.setter
    def excluded_domains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludedDomains property value. Domains that are accessed through the public internet instead of through VPN, even when per-app VPN is activated
        Args:
            value: Value to set for the excludedDomains property.
        """
        self._excluded_domains = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "associated_domains": lambda n : setattr(self, 'associated_domains', n.get_collection_of_primitive_values(str)),
            "authentication_method": lambda n : setattr(self, 'authentication_method', n.get_enum_value(vpn_authentication_method.VpnAuthenticationMethod)),
            "connection_name": lambda n : setattr(self, 'connection_name', n.get_str_value()),
            "connection_type": lambda n : setattr(self, 'connection_type', n.get_enum_value(apple_vpn_connection_type.AppleVpnConnectionType)),
            "custom_data": lambda n : setattr(self, 'custom_data', n.get_collection_of_object_values(key_value.KeyValue)),
            "custom_key_value_data": lambda n : setattr(self, 'custom_key_value_data', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "disable_on_demand_user_override": lambda n : setattr(self, 'disable_on_demand_user_override', n.get_bool_value()),
            "disconnect_on_idle": lambda n : setattr(self, 'disconnect_on_idle', n.get_bool_value()),
            "disconnect_on_idle_timer_in_seconds": lambda n : setattr(self, 'disconnect_on_idle_timer_in_seconds', n.get_int_value()),
            "enable_per_app": lambda n : setattr(self, 'enable_per_app', n.get_bool_value()),
            "enable_split_tunneling": lambda n : setattr(self, 'enable_split_tunneling', n.get_bool_value()),
            "excluded_domains": lambda n : setattr(self, 'excluded_domains', n.get_collection_of_primitive_values(str)),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "login_group_or_domain": lambda n : setattr(self, 'login_group_or_domain', n.get_str_value()),
            "on_demand_rules": lambda n : setattr(self, 'on_demand_rules', n.get_collection_of_object_values(vpn_on_demand_rule.VpnOnDemandRule)),
            "opt_in_to_device_id_sharing": lambda n : setattr(self, 'opt_in_to_device_id_sharing', n.get_bool_value()),
            "provider_type": lambda n : setattr(self, 'provider_type', n.get_enum_value(vpn_provider_type.VpnProviderType)),
            "proxy_server": lambda n : setattr(self, 'proxy_server', n.get_object_value(vpn_proxy_server.VpnProxyServer)),
            "realm": lambda n : setattr(self, 'realm', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "safari_domains": lambda n : setattr(self, 'safari_domains', n.get_collection_of_primitive_values(str)),
            "server": lambda n : setattr(self, 'server', n.get_object_value(vpn_server.VpnServer)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identifier(self,) -> Optional[str]:
        """
        Gets the identifier property value. Identifier provided by VPN vendor when connection type is set to Custom VPN. For example: Cisco AnyConnect uses an identifier of the form com.cisco.anyconnect.applevpn.plugin
        Returns: Optional[str]
        """
        return self._identifier
    
    @identifier.setter
    def identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the identifier property value. Identifier provided by VPN vendor when connection type is set to Custom VPN. For example: Cisco AnyConnect uses an identifier of the form com.cisco.anyconnect.applevpn.plugin
        Args:
            value: Value to set for the identifier property.
        """
        self._identifier = value
    
    @property
    def login_group_or_domain(self,) -> Optional[str]:
        """
        Gets the loginGroupOrDomain property value. Login group or domain when connection type is set to Dell SonicWALL Mobile Connection.
        Returns: Optional[str]
        """
        return self._login_group_or_domain
    
    @login_group_or_domain.setter
    def login_group_or_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the loginGroupOrDomain property value. Login group or domain when connection type is set to Dell SonicWALL Mobile Connection.
        Args:
            value: Value to set for the loginGroupOrDomain property.
        """
        self._login_group_or_domain = value
    
    @property
    def on_demand_rules(self,) -> Optional[List[vpn_on_demand_rule.VpnOnDemandRule]]:
        """
        Gets the onDemandRules property value. On-Demand Rules. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[vpn_on_demand_rule.VpnOnDemandRule]]
        """
        return self._on_demand_rules
    
    @on_demand_rules.setter
    def on_demand_rules(self,value: Optional[List[vpn_on_demand_rule.VpnOnDemandRule]] = None) -> None:
        """
        Sets the onDemandRules property value. On-Demand Rules. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the onDemandRules property.
        """
        self._on_demand_rules = value
    
    @property
    def opt_in_to_device_id_sharing(self,) -> Optional[bool]:
        """
        Gets the optInToDeviceIdSharing property value. Opt-In to sharing the device's Id to third-party vpn clients for use during network access control validation.
        Returns: Optional[bool]
        """
        return self._opt_in_to_device_id_sharing
    
    @opt_in_to_device_id_sharing.setter
    def opt_in_to_device_id_sharing(self,value: Optional[bool] = None) -> None:
        """
        Sets the optInToDeviceIdSharing property value. Opt-In to sharing the device's Id to third-party vpn clients for use during network access control validation.
        Args:
            value: Value to set for the optInToDeviceIdSharing property.
        """
        self._opt_in_to_device_id_sharing = value
    
    @property
    def provider_type(self,) -> Optional[vpn_provider_type.VpnProviderType]:
        """
        Gets the providerType property value. Provider type for per-app VPN. Possible values are: notConfigured, appProxy, packetTunnel.
        Returns: Optional[vpn_provider_type.VpnProviderType]
        """
        return self._provider_type
    
    @provider_type.setter
    def provider_type(self,value: Optional[vpn_provider_type.VpnProviderType] = None) -> None:
        """
        Sets the providerType property value. Provider type for per-app VPN. Possible values are: notConfigured, appProxy, packetTunnel.
        Args:
            value: Value to set for the providerType property.
        """
        self._provider_type = value
    
    @property
    def proxy_server(self,) -> Optional[vpn_proxy_server.VpnProxyServer]:
        """
        Gets the proxyServer property value. Proxy Server.
        Returns: Optional[vpn_proxy_server.VpnProxyServer]
        """
        return self._proxy_server
    
    @proxy_server.setter
    def proxy_server(self,value: Optional[vpn_proxy_server.VpnProxyServer] = None) -> None:
        """
        Sets the proxyServer property value. Proxy Server.
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
    
    @property
    def safari_domains(self,) -> Optional[List[str]]:
        """
        Gets the safariDomains property value. Safari domains when this VPN per App setting is enabled. In addition to the apps associated with this VPN, Safari domains specified here will also be able to trigger this VPN connection.
        Returns: Optional[List[str]]
        """
        return self._safari_domains
    
    @safari_domains.setter
    def safari_domains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the safariDomains property value. Safari domains when this VPN per App setting is enabled. In addition to the apps associated with this VPN, Safari domains specified here will also be able to trigger this VPN connection.
        Args:
            value: Value to set for the safariDomains property.
        """
        self._safari_domains = value
    
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
    
    @property
    def server(self,) -> Optional[vpn_server.VpnServer]:
        """
        Gets the server property value. VPN Server definition.
        Returns: Optional[vpn_server.VpnServer]
        """
        return self._server
    
    @server.setter
    def server(self,value: Optional[vpn_server.VpnServer] = None) -> None:
        """
        Sets the server property value. VPN Server definition.
        Args:
            value: Value to set for the server property.
        """
        self._server = value
    

