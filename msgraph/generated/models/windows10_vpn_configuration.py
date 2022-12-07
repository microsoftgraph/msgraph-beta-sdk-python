from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cryptography_suite = lazy_import('msgraph.generated.models.cryptography_suite')
extended_key_usage = lazy_import('msgraph.generated.models.extended_key_usage')
vpn_dns_rule = lazy_import('msgraph.generated.models.vpn_dns_rule')
vpn_route = lazy_import('msgraph.generated.models.vpn_route')
vpn_traffic_rule = lazy_import('msgraph.generated.models.vpn_traffic_rule')
windows_certificate_profile_base = lazy_import('msgraph.generated.models.windows_certificate_profile_base')
windows_vpn_configuration = lazy_import('msgraph.generated.models.windows_vpn_configuration')
windows10_associated_apps = lazy_import('msgraph.generated.models.windows10_associated_apps')
windows10_vpn_authentication_method = lazy_import('msgraph.generated.models.windows10_vpn_authentication_method')
windows10_vpn_connection_type = lazy_import('msgraph.generated.models.windows10_vpn_connection_type')
windows10_vpn_profile_target = lazy_import('msgraph.generated.models.windows10_vpn_profile_target')
windows10_vpn_proxy_server = lazy_import('msgraph.generated.models.windows10_vpn_proxy_server')

class Windows10VpnConfiguration(windows_vpn_configuration.WindowsVpnConfiguration):
    @property
    def associated_apps(self,) -> Optional[List[windows10_associated_apps.Windows10AssociatedApps]]:
        """
        Gets the associatedApps property value. Associated Apps. This collection can contain a maximum of 10000 elements.
        Returns: Optional[List[windows10_associated_apps.Windows10AssociatedApps]]
        """
        return self._associated_apps
    
    @associated_apps.setter
    def associated_apps(self,value: Optional[List[windows10_associated_apps.Windows10AssociatedApps]] = None) -> None:
        """
        Sets the associatedApps property value. Associated Apps. This collection can contain a maximum of 10000 elements.
        Args:
            value: Value to set for the associatedApps property.
        """
        self._associated_apps = value
    
    @property
    def authentication_method(self,) -> Optional[windows10_vpn_authentication_method.Windows10VpnAuthenticationMethod]:
        """
        Gets the authenticationMethod property value. Windows 10 VPN connection types.
        Returns: Optional[windows10_vpn_authentication_method.Windows10VpnAuthenticationMethod]
        """
        return self._authentication_method
    
    @authentication_method.setter
    def authentication_method(self,value: Optional[windows10_vpn_authentication_method.Windows10VpnAuthenticationMethod] = None) -> None:
        """
        Sets the authenticationMethod property value. Windows 10 VPN connection types.
        Args:
            value: Value to set for the authenticationMethod property.
        """
        self._authentication_method = value
    
    @property
    def connection_type(self,) -> Optional[windows10_vpn_connection_type.Windows10VpnConnectionType]:
        """
        Gets the connectionType property value. VPN connection types.
        Returns: Optional[windows10_vpn_connection_type.Windows10VpnConnectionType]
        """
        return self._connection_type
    
    @connection_type.setter
    def connection_type(self,value: Optional[windows10_vpn_connection_type.Windows10VpnConnectionType] = None) -> None:
        """
        Sets the connectionType property value. VPN connection types.
        Args:
            value: Value to set for the connectionType property.
        """
        self._connection_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10VpnConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10VpnConfiguration"
        # Associated Apps. This collection can contain a maximum of 10000 elements.
        self._associated_apps: Optional[List[windows10_associated_apps.Windows10AssociatedApps]] = None
        # Windows 10 VPN connection types.
        self._authentication_method: Optional[windows10_vpn_authentication_method.Windows10VpnAuthenticationMethod] = None
        # VPN connection types.
        self._connection_type: Optional[windows10_vpn_connection_type.Windows10VpnConnectionType] = None
        # Cryptography Suite security settings for IKEv2 VPN in Windows10 and above
        self._cryptography_suite: Optional[cryptography_suite.CryptographySuite] = None
        # DNS rules. This collection can contain a maximum of 1000 elements.
        self._dns_rules: Optional[List[vpn_dns_rule.VpnDnsRule]] = None
        # Specify DNS suffixes to add to the DNS search list to properly route short names.
        self._dns_suffixes: Optional[List[str]] = None
        # Extensible Authentication Protocol (EAP) XML. (UTF8 encoded byte array)
        self._eap_xml: Optional[bytes] = None
        # Enable Always On mode.
        self._enable_always_on: Optional[bool] = None
        # Enable conditional access.
        self._enable_conditional_access: Optional[bool] = None
        # Enable device tunnel.
        self._enable_device_tunnel: Optional[bool] = None
        # Enable IP address registration with internal DNS.
        self._enable_dns_registration: Optional[bool] = None
        # Enable single sign-on (SSO) with alternate certificate.
        self._enable_single_sign_on_with_alternate_certificate: Optional[bool] = None
        # Enable split tunneling.
        self._enable_split_tunneling: Optional[bool] = None
        # Identity certificate for client authentication when authentication method is certificate.
        self._identity_certificate: Optional[windows_certificate_profile_base.WindowsCertificateProfileBase] = None
        # ID of the Microsoft Tunnel site associated with the VPN profile.
        self._microsoft_tunnel_site_id: Optional[str] = None
        # Only associated Apps can use connection (per-app VPN).
        self._only_associated_apps_can_use_connection: Optional[bool] = None
        # Profile target type. Possible values are: user, device, autoPilotDevice.
        self._profile_target: Optional[windows10_vpn_profile_target.Windows10VpnProfileTarget] = None
        # Proxy Server.
        self._proxy_server: Optional[windows10_vpn_proxy_server.Windows10VpnProxyServer] = None
        # Remember user credentials.
        self._remember_user_credentials: Optional[bool] = None
        # Routes (optional for third-party providers). This collection can contain a maximum of 1000 elements.
        self._routes: Optional[List[vpn_route.VpnRoute]] = None
        # Single sign-on Extended Key Usage (EKU).
        self._single_sign_on_eku: Optional[extended_key_usage.ExtendedKeyUsage] = None
        # Single sign-on issuer hash.
        self._single_sign_on_issuer_hash: Optional[str] = None
        # Traffic rules. This collection can contain a maximum of 1000 elements.
        self._traffic_rules: Optional[List[vpn_traffic_rule.VpnTrafficRule]] = None
        # Trusted Network Domains
        self._trusted_network_domains: Optional[List[str]] = None
        # Windows Information Protection (WIP) domain to associate with this connection.
        self._windows_information_protection_domain: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10VpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10VpnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10VpnConfiguration()
    
    @property
    def cryptography_suite(self,) -> Optional[cryptography_suite.CryptographySuite]:
        """
        Gets the cryptographySuite property value. Cryptography Suite security settings for IKEv2 VPN in Windows10 and above
        Returns: Optional[cryptography_suite.CryptographySuite]
        """
        return self._cryptography_suite
    
    @cryptography_suite.setter
    def cryptography_suite(self,value: Optional[cryptography_suite.CryptographySuite] = None) -> None:
        """
        Sets the cryptographySuite property value. Cryptography Suite security settings for IKEv2 VPN in Windows10 and above
        Args:
            value: Value to set for the cryptographySuite property.
        """
        self._cryptography_suite = value
    
    @property
    def dns_rules(self,) -> Optional[List[vpn_dns_rule.VpnDnsRule]]:
        """
        Gets the dnsRules property value. DNS rules. This collection can contain a maximum of 1000 elements.
        Returns: Optional[List[vpn_dns_rule.VpnDnsRule]]
        """
        return self._dns_rules
    
    @dns_rules.setter
    def dns_rules(self,value: Optional[List[vpn_dns_rule.VpnDnsRule]] = None) -> None:
        """
        Sets the dnsRules property value. DNS rules. This collection can contain a maximum of 1000 elements.
        Args:
            value: Value to set for the dnsRules property.
        """
        self._dns_rules = value
    
    @property
    def dns_suffixes(self,) -> Optional[List[str]]:
        """
        Gets the dnsSuffixes property value. Specify DNS suffixes to add to the DNS search list to properly route short names.
        Returns: Optional[List[str]]
        """
        return self._dns_suffixes
    
    @dns_suffixes.setter
    def dns_suffixes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the dnsSuffixes property value. Specify DNS suffixes to add to the DNS search list to properly route short names.
        Args:
            value: Value to set for the dnsSuffixes property.
        """
        self._dns_suffixes = value
    
    @property
    def eap_xml(self,) -> Optional[bytes]:
        """
        Gets the eapXml property value. Extensible Authentication Protocol (EAP) XML. (UTF8 encoded byte array)
        Returns: Optional[bytes]
        """
        return self._eap_xml
    
    @eap_xml.setter
    def eap_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the eapXml property value. Extensible Authentication Protocol (EAP) XML. (UTF8 encoded byte array)
        Args:
            value: Value to set for the eapXml property.
        """
        self._eap_xml = value
    
    @property
    def enable_always_on(self,) -> Optional[bool]:
        """
        Gets the enableAlwaysOn property value. Enable Always On mode.
        Returns: Optional[bool]
        """
        return self._enable_always_on
    
    @enable_always_on.setter
    def enable_always_on(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableAlwaysOn property value. Enable Always On mode.
        Args:
            value: Value to set for the enableAlwaysOn property.
        """
        self._enable_always_on = value
    
    @property
    def enable_conditional_access(self,) -> Optional[bool]:
        """
        Gets the enableConditionalAccess property value. Enable conditional access.
        Returns: Optional[bool]
        """
        return self._enable_conditional_access
    
    @enable_conditional_access.setter
    def enable_conditional_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableConditionalAccess property value. Enable conditional access.
        Args:
            value: Value to set for the enableConditionalAccess property.
        """
        self._enable_conditional_access = value
    
    @property
    def enable_device_tunnel(self,) -> Optional[bool]:
        """
        Gets the enableDeviceTunnel property value. Enable device tunnel.
        Returns: Optional[bool]
        """
        return self._enable_device_tunnel
    
    @enable_device_tunnel.setter
    def enable_device_tunnel(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableDeviceTunnel property value. Enable device tunnel.
        Args:
            value: Value to set for the enableDeviceTunnel property.
        """
        self._enable_device_tunnel = value
    
    @property
    def enable_dns_registration(self,) -> Optional[bool]:
        """
        Gets the enableDnsRegistration property value. Enable IP address registration with internal DNS.
        Returns: Optional[bool]
        """
        return self._enable_dns_registration
    
    @enable_dns_registration.setter
    def enable_dns_registration(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableDnsRegistration property value. Enable IP address registration with internal DNS.
        Args:
            value: Value to set for the enableDnsRegistration property.
        """
        self._enable_dns_registration = value
    
    @property
    def enable_single_sign_on_with_alternate_certificate(self,) -> Optional[bool]:
        """
        Gets the enableSingleSignOnWithAlternateCertificate property value. Enable single sign-on (SSO) with alternate certificate.
        Returns: Optional[bool]
        """
        return self._enable_single_sign_on_with_alternate_certificate
    
    @enable_single_sign_on_with_alternate_certificate.setter
    def enable_single_sign_on_with_alternate_certificate(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableSingleSignOnWithAlternateCertificate property value. Enable single sign-on (SSO) with alternate certificate.
        Args:
            value: Value to set for the enableSingleSignOnWithAlternateCertificate property.
        """
        self._enable_single_sign_on_with_alternate_certificate = value
    
    @property
    def enable_split_tunneling(self,) -> Optional[bool]:
        """
        Gets the enableSplitTunneling property value. Enable split tunneling.
        Returns: Optional[bool]
        """
        return self._enable_split_tunneling
    
    @enable_split_tunneling.setter
    def enable_split_tunneling(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableSplitTunneling property value. Enable split tunneling.
        Args:
            value: Value to set for the enableSplitTunneling property.
        """
        self._enable_split_tunneling = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "associated_apps": lambda n : setattr(self, 'associated_apps', n.get_collection_of_object_values(windows10_associated_apps.Windows10AssociatedApps)),
            "authentication_method": lambda n : setattr(self, 'authentication_method', n.get_enum_value(windows10_vpn_authentication_method.Windows10VpnAuthenticationMethod)),
            "connection_type": lambda n : setattr(self, 'connection_type', n.get_enum_value(windows10_vpn_connection_type.Windows10VpnConnectionType)),
            "cryptography_suite": lambda n : setattr(self, 'cryptography_suite', n.get_object_value(cryptography_suite.CryptographySuite)),
            "dns_rules": lambda n : setattr(self, 'dns_rules', n.get_collection_of_object_values(vpn_dns_rule.VpnDnsRule)),
            "dns_suffixes": lambda n : setattr(self, 'dns_suffixes', n.get_collection_of_primitive_values(str)),
            "eap_xml": lambda n : setattr(self, 'eap_xml', n.get_bytes_value()),
            "enable_always_on": lambda n : setattr(self, 'enable_always_on', n.get_bool_value()),
            "enable_conditional_access": lambda n : setattr(self, 'enable_conditional_access', n.get_bool_value()),
            "enable_device_tunnel": lambda n : setattr(self, 'enable_device_tunnel', n.get_bool_value()),
            "enable_dns_registration": lambda n : setattr(self, 'enable_dns_registration', n.get_bool_value()),
            "enable_single_sign_on_with_alternate_certificate": lambda n : setattr(self, 'enable_single_sign_on_with_alternate_certificate', n.get_bool_value()),
            "enable_split_tunneling": lambda n : setattr(self, 'enable_split_tunneling', n.get_bool_value()),
            "identity_certificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(windows_certificate_profile_base.WindowsCertificateProfileBase)),
            "microsoft_tunnel_site_id": lambda n : setattr(self, 'microsoft_tunnel_site_id', n.get_str_value()),
            "only_associated_apps_can_use_connection": lambda n : setattr(self, 'only_associated_apps_can_use_connection', n.get_bool_value()),
            "profile_target": lambda n : setattr(self, 'profile_target', n.get_enum_value(windows10_vpn_profile_target.Windows10VpnProfileTarget)),
            "proxy_server": lambda n : setattr(self, 'proxy_server', n.get_object_value(windows10_vpn_proxy_server.Windows10VpnProxyServer)),
            "remember_user_credentials": lambda n : setattr(self, 'remember_user_credentials', n.get_bool_value()),
            "routes": lambda n : setattr(self, 'routes', n.get_collection_of_object_values(vpn_route.VpnRoute)),
            "single_sign_on_eku": lambda n : setattr(self, 'single_sign_on_eku', n.get_object_value(extended_key_usage.ExtendedKeyUsage)),
            "single_sign_on_issuer_hash": lambda n : setattr(self, 'single_sign_on_issuer_hash', n.get_str_value()),
            "traffic_rules": lambda n : setattr(self, 'traffic_rules', n.get_collection_of_object_values(vpn_traffic_rule.VpnTrafficRule)),
            "trusted_network_domains": lambda n : setattr(self, 'trusted_network_domains', n.get_collection_of_primitive_values(str)),
            "windows_information_protection_domain": lambda n : setattr(self, 'windows_information_protection_domain', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_certificate(self,) -> Optional[windows_certificate_profile_base.WindowsCertificateProfileBase]:
        """
        Gets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Returns: Optional[windows_certificate_profile_base.WindowsCertificateProfileBase]
        """
        return self._identity_certificate
    
    @identity_certificate.setter
    def identity_certificate(self,value: Optional[windows_certificate_profile_base.WindowsCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Args:
            value: Value to set for the identityCertificate property.
        """
        self._identity_certificate = value
    
    @property
    def microsoft_tunnel_site_id(self,) -> Optional[str]:
        """
        Gets the microsoftTunnelSiteId property value. ID of the Microsoft Tunnel site associated with the VPN profile.
        Returns: Optional[str]
        """
        return self._microsoft_tunnel_site_id
    
    @microsoft_tunnel_site_id.setter
    def microsoft_tunnel_site_id(self,value: Optional[str] = None) -> None:
        """
        Sets the microsoftTunnelSiteId property value. ID of the Microsoft Tunnel site associated with the VPN profile.
        Args:
            value: Value to set for the microsoftTunnelSiteId property.
        """
        self._microsoft_tunnel_site_id = value
    
    @property
    def only_associated_apps_can_use_connection(self,) -> Optional[bool]:
        """
        Gets the onlyAssociatedAppsCanUseConnection property value. Only associated Apps can use connection (per-app VPN).
        Returns: Optional[bool]
        """
        return self._only_associated_apps_can_use_connection
    
    @only_associated_apps_can_use_connection.setter
    def only_associated_apps_can_use_connection(self,value: Optional[bool] = None) -> None:
        """
        Sets the onlyAssociatedAppsCanUseConnection property value. Only associated Apps can use connection (per-app VPN).
        Args:
            value: Value to set for the onlyAssociatedAppsCanUseConnection property.
        """
        self._only_associated_apps_can_use_connection = value
    
    @property
    def profile_target(self,) -> Optional[windows10_vpn_profile_target.Windows10VpnProfileTarget]:
        """
        Gets the profileTarget property value. Profile target type. Possible values are: user, device, autoPilotDevice.
        Returns: Optional[windows10_vpn_profile_target.Windows10VpnProfileTarget]
        """
        return self._profile_target
    
    @profile_target.setter
    def profile_target(self,value: Optional[windows10_vpn_profile_target.Windows10VpnProfileTarget] = None) -> None:
        """
        Sets the profileTarget property value. Profile target type. Possible values are: user, device, autoPilotDevice.
        Args:
            value: Value to set for the profileTarget property.
        """
        self._profile_target = value
    
    @property
    def proxy_server(self,) -> Optional[windows10_vpn_proxy_server.Windows10VpnProxyServer]:
        """
        Gets the proxyServer property value. Proxy Server.
        Returns: Optional[windows10_vpn_proxy_server.Windows10VpnProxyServer]
        """
        return self._proxy_server
    
    @proxy_server.setter
    def proxy_server(self,value: Optional[windows10_vpn_proxy_server.Windows10VpnProxyServer] = None) -> None:
        """
        Sets the proxyServer property value. Proxy Server.
        Args:
            value: Value to set for the proxyServer property.
        """
        self._proxy_server = value
    
    @property
    def remember_user_credentials(self,) -> Optional[bool]:
        """
        Gets the rememberUserCredentials property value. Remember user credentials.
        Returns: Optional[bool]
        """
        return self._remember_user_credentials
    
    @remember_user_credentials.setter
    def remember_user_credentials(self,value: Optional[bool] = None) -> None:
        """
        Sets the rememberUserCredentials property value. Remember user credentials.
        Args:
            value: Value to set for the rememberUserCredentials property.
        """
        self._remember_user_credentials = value
    
    @property
    def routes(self,) -> Optional[List[vpn_route.VpnRoute]]:
        """
        Gets the routes property value. Routes (optional for third-party providers). This collection can contain a maximum of 1000 elements.
        Returns: Optional[List[vpn_route.VpnRoute]]
        """
        return self._routes
    
    @routes.setter
    def routes(self,value: Optional[List[vpn_route.VpnRoute]] = None) -> None:
        """
        Sets the routes property value. Routes (optional for third-party providers). This collection can contain a maximum of 1000 elements.
        Args:
            value: Value to set for the routes property.
        """
        self._routes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("associatedApps", self.associated_apps)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_object_value("cryptographySuite", self.cryptography_suite)
        writer.write_collection_of_object_values("dnsRules", self.dns_rules)
        writer.write_collection_of_primitive_values("dnsSuffixes", self.dns_suffixes)
        writer.write_object_value("eapXml", self.eap_xml)
        writer.write_bool_value("enableAlwaysOn", self.enable_always_on)
        writer.write_bool_value("enableConditionalAccess", self.enable_conditional_access)
        writer.write_bool_value("enableDeviceTunnel", self.enable_device_tunnel)
        writer.write_bool_value("enableDnsRegistration", self.enable_dns_registration)
        writer.write_bool_value("enableSingleSignOnWithAlternateCertificate", self.enable_single_sign_on_with_alternate_certificate)
        writer.write_bool_value("enableSplitTunneling", self.enable_split_tunneling)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_str_value("microsoftTunnelSiteId", self.microsoft_tunnel_site_id)
        writer.write_bool_value("onlyAssociatedAppsCanUseConnection", self.only_associated_apps_can_use_connection)
        writer.write_enum_value("profileTarget", self.profile_target)
        writer.write_object_value("proxyServer", self.proxy_server)
        writer.write_bool_value("rememberUserCredentials", self.remember_user_credentials)
        writer.write_collection_of_object_values("routes", self.routes)
        writer.write_object_value("singleSignOnEku", self.single_sign_on_eku)
        writer.write_str_value("singleSignOnIssuerHash", self.single_sign_on_issuer_hash)
        writer.write_collection_of_object_values("trafficRules", self.traffic_rules)
        writer.write_collection_of_primitive_values("trustedNetworkDomains", self.trusted_network_domains)
        writer.write_str_value("windowsInformationProtectionDomain", self.windows_information_protection_domain)
    
    @property
    def single_sign_on_eku(self,) -> Optional[extended_key_usage.ExtendedKeyUsage]:
        """
        Gets the singleSignOnEku property value. Single sign-on Extended Key Usage (EKU).
        Returns: Optional[extended_key_usage.ExtendedKeyUsage]
        """
        return self._single_sign_on_eku
    
    @single_sign_on_eku.setter
    def single_sign_on_eku(self,value: Optional[extended_key_usage.ExtendedKeyUsage] = None) -> None:
        """
        Sets the singleSignOnEku property value. Single sign-on Extended Key Usage (EKU).
        Args:
            value: Value to set for the singleSignOnEku property.
        """
        self._single_sign_on_eku = value
    
    @property
    def single_sign_on_issuer_hash(self,) -> Optional[str]:
        """
        Gets the singleSignOnIssuerHash property value. Single sign-on issuer hash.
        Returns: Optional[str]
        """
        return self._single_sign_on_issuer_hash
    
    @single_sign_on_issuer_hash.setter
    def single_sign_on_issuer_hash(self,value: Optional[str] = None) -> None:
        """
        Sets the singleSignOnIssuerHash property value. Single sign-on issuer hash.
        Args:
            value: Value to set for the singleSignOnIssuerHash property.
        """
        self._single_sign_on_issuer_hash = value
    
    @property
    def traffic_rules(self,) -> Optional[List[vpn_traffic_rule.VpnTrafficRule]]:
        """
        Gets the trafficRules property value. Traffic rules. This collection can contain a maximum of 1000 elements.
        Returns: Optional[List[vpn_traffic_rule.VpnTrafficRule]]
        """
        return self._traffic_rules
    
    @traffic_rules.setter
    def traffic_rules(self,value: Optional[List[vpn_traffic_rule.VpnTrafficRule]] = None) -> None:
        """
        Sets the trafficRules property value. Traffic rules. This collection can contain a maximum of 1000 elements.
        Args:
            value: Value to set for the trafficRules property.
        """
        self._traffic_rules = value
    
    @property
    def trusted_network_domains(self,) -> Optional[List[str]]:
        """
        Gets the trustedNetworkDomains property value. Trusted Network Domains
        Returns: Optional[List[str]]
        """
        return self._trusted_network_domains
    
    @trusted_network_domains.setter
    def trusted_network_domains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the trustedNetworkDomains property value. Trusted Network Domains
        Args:
            value: Value to set for the trustedNetworkDomains property.
        """
        self._trusted_network_domains = value
    
    @property
    def windows_information_protection_domain(self,) -> Optional[str]:
        """
        Gets the windowsInformationProtectionDomain property value. Windows Information Protection (WIP) domain to associate with this connection.
        Returns: Optional[str]
        """
        return self._windows_information_protection_domain
    
    @windows_information_protection_domain.setter
    def windows_information_protection_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the windowsInformationProtectionDomain property value. Windows Information Protection (WIP) domain to associate with this connection.
        Args:
            value: Value to set for the windowsInformationProtectionDomain property.
        """
        self._windows_information_protection_domain = value
    

