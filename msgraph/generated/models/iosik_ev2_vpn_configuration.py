from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

apple_vpn_always_on_configuration = lazy_import('msgraph.generated.models.apple_vpn_always_on_configuration')
ios_vpn_configuration = lazy_import('msgraph.generated.models.ios_vpn_configuration')
ios_vpn_security_association_parameters = lazy_import('msgraph.generated.models.ios_vpn_security_association_parameters')
vpn_client_authentication_type = lazy_import('msgraph.generated.models.vpn_client_authentication_type')
vpn_dead_peer_detection_rate = lazy_import('msgraph.generated.models.vpn_dead_peer_detection_rate')
vpn_local_identifier = lazy_import('msgraph.generated.models.vpn_local_identifier')
vpn_server_certificate_type = lazy_import('msgraph.generated.models.vpn_server_certificate_type')

class IosikEv2VpnConfiguration(ios_vpn_configuration.IosVpnConfiguration):
    @property
    def allow_default_child_security_association_parameters(self,) -> Optional[bool]:
        """
        Gets the allowDefaultChildSecurityAssociationParameters property value. Allows the use of child security association parameters by setting all parameters to the device's default unless explicitly specified.
        Returns: Optional[bool]
        """
        return self._allow_default_child_security_association_parameters
    
    @allow_default_child_security_association_parameters.setter
    def allow_default_child_security_association_parameters(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowDefaultChildSecurityAssociationParameters property value. Allows the use of child security association parameters by setting all parameters to the device's default unless explicitly specified.
        Args:
            value: Value to set for the allowDefaultChildSecurityAssociationParameters property.
        """
        self._allow_default_child_security_association_parameters = value
    
    @property
    def allow_default_security_association_parameters(self,) -> Optional[bool]:
        """
        Gets the allowDefaultSecurityAssociationParameters property value. Allows the use of security association parameters by setting all parameters to the device's default unless explicitly specified.
        Returns: Optional[bool]
        """
        return self._allow_default_security_association_parameters
    
    @allow_default_security_association_parameters.setter
    def allow_default_security_association_parameters(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowDefaultSecurityAssociationParameters property value. Allows the use of security association parameters by setting all parameters to the device's default unless explicitly specified.
        Args:
            value: Value to set for the allowDefaultSecurityAssociationParameters property.
        """
        self._allow_default_security_association_parameters = value
    
    @property
    def always_on_configuration(self,) -> Optional[apple_vpn_always_on_configuration.AppleVpnAlwaysOnConfiguration]:
        """
        Gets the alwaysOnConfiguration property value. AlwaysOn Configuration
        Returns: Optional[apple_vpn_always_on_configuration.AppleVpnAlwaysOnConfiguration]
        """
        return self._always_on_configuration
    
    @always_on_configuration.setter
    def always_on_configuration(self,value: Optional[apple_vpn_always_on_configuration.AppleVpnAlwaysOnConfiguration] = None) -> None:
        """
        Sets the alwaysOnConfiguration property value. AlwaysOn Configuration
        Args:
            value: Value to set for the alwaysOnConfiguration property.
        """
        self._always_on_configuration = value
    
    @property
    def child_security_association_parameters(self,) -> Optional[ios_vpn_security_association_parameters.IosVpnSecurityAssociationParameters]:
        """
        Gets the childSecurityAssociationParameters property value. Child Security Association Parameters
        Returns: Optional[ios_vpn_security_association_parameters.IosVpnSecurityAssociationParameters]
        """
        return self._child_security_association_parameters
    
    @child_security_association_parameters.setter
    def child_security_association_parameters(self,value: Optional[ios_vpn_security_association_parameters.IosVpnSecurityAssociationParameters] = None) -> None:
        """
        Sets the childSecurityAssociationParameters property value. Child Security Association Parameters
        Args:
            value: Value to set for the childSecurityAssociationParameters property.
        """
        self._child_security_association_parameters = value
    
    @property
    def client_authentication_type(self,) -> Optional[vpn_client_authentication_type.VpnClientAuthenticationType]:
        """
        Gets the clientAuthenticationType property value. The type of VPN client authentication type
        Returns: Optional[vpn_client_authentication_type.VpnClientAuthenticationType]
        """
        return self._client_authentication_type
    
    @client_authentication_type.setter
    def client_authentication_type(self,value: Optional[vpn_client_authentication_type.VpnClientAuthenticationType] = None) -> None:
        """
        Sets the clientAuthenticationType property value. The type of VPN client authentication type
        Args:
            value: Value to set for the clientAuthenticationType property.
        """
        self._client_authentication_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosikEv2VpnConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosikEv2VpnConfiguration"
        # Allows the use of child security association parameters by setting all parameters to the device's default unless explicitly specified.
        self._allow_default_child_security_association_parameters: Optional[bool] = None
        # Allows the use of security association parameters by setting all parameters to the device's default unless explicitly specified.
        self._allow_default_security_association_parameters: Optional[bool] = None
        # AlwaysOn Configuration
        self._always_on_configuration: Optional[apple_vpn_always_on_configuration.AppleVpnAlwaysOnConfiguration] = None
        # Child Security Association Parameters
        self._child_security_association_parameters: Optional[ios_vpn_security_association_parameters.IosVpnSecurityAssociationParameters] = None
        # The type of VPN client authentication type
        self._client_authentication_type: Optional[vpn_client_authentication_type.VpnClientAuthenticationType] = None
        # Determine how often to check if a peer connection is still active. . Possible values are: medium, none, low, high.
        self._dead_peer_detection_rate: Optional[vpn_dead_peer_detection_rate.VpnDeadPeerDetectionRate] = None
        # Disable MOBIKE
        self._disable_mobility_and_multihoming: Optional[bool] = None
        # Disable Redirect
        self._disable_redirect: Optional[bool] = None
        # Determines if Always on VPN is enabled
        self._enable_always_on_configuration: Optional[bool] = None
        # Enables a best-effort revocation check; server response timeouts will not cause it to fail
        self._enable_certificate_revocation_check: Optional[bool] = None
        # Enables EAP only authentication
        self._enable_e_a_p: Optional[bool] = None
        # Enable Perfect Forward Secrecy (PFS).
        self._enable_perfect_forward_secrecy: Optional[bool] = None
        # Enable Use Internal Subnet Attributes.
        self._enable_use_internal_subnet_attributes: Optional[bool] = None
        # The type of VPN local identifier
        self._local_identifier: Optional[vpn_local_identifier.VpnLocalIdentifier] = None
        # Maximum transmission unit. Valid values 1280 to 1400
        self._mtu_size_in_bytes: Optional[int] = None
        # Address of the IKEv2 server. Must be a FQDN, UserFQDN, network address, or ASN1DN
        self._remote_identifier: Optional[str] = None
        # Security Association Parameters
        self._security_association_parameters: Optional[ios_vpn_security_association_parameters.IosVpnSecurityAssociationParameters] = None
        # Common name of the IKEv2 Server Certificate used in Server Authentication
        self._server_certificate_common_name: Optional[str] = None
        # Issuer Common name of the IKEv2 Server Certificate issuer used in Authentication
        self._server_certificate_issuer_common_name: Optional[str] = None
        # The type of certificate the VPN server will present to the VPN client for authentication. Possible values are: rsa, ecdsa256, ecdsa384, ecdsa521.
        self._server_certificate_type: Optional[vpn_server_certificate_type.VpnServerCertificateType] = None
        # Used when Shared Secret Authentication is selected
        self._shared_secret: Optional[str] = None
        # The maximum TLS version to be used with EAP-TLS authentication
        self._tls_maximum_version: Optional[str] = None
        # The minimum TLS version to be used with EAP-TLS authentication
        self._tls_minimum_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosikEv2VpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosikEv2VpnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosikEv2VpnConfiguration()
    
    @property
    def dead_peer_detection_rate(self,) -> Optional[vpn_dead_peer_detection_rate.VpnDeadPeerDetectionRate]:
        """
        Gets the deadPeerDetectionRate property value. Determine how often to check if a peer connection is still active. . Possible values are: medium, none, low, high.
        Returns: Optional[vpn_dead_peer_detection_rate.VpnDeadPeerDetectionRate]
        """
        return self._dead_peer_detection_rate
    
    @dead_peer_detection_rate.setter
    def dead_peer_detection_rate(self,value: Optional[vpn_dead_peer_detection_rate.VpnDeadPeerDetectionRate] = None) -> None:
        """
        Sets the deadPeerDetectionRate property value. Determine how often to check if a peer connection is still active. . Possible values are: medium, none, low, high.
        Args:
            value: Value to set for the deadPeerDetectionRate property.
        """
        self._dead_peer_detection_rate = value
    
    @property
    def disable_mobility_and_multihoming(self,) -> Optional[bool]:
        """
        Gets the disableMobilityAndMultihoming property value. Disable MOBIKE
        Returns: Optional[bool]
        """
        return self._disable_mobility_and_multihoming
    
    @disable_mobility_and_multihoming.setter
    def disable_mobility_and_multihoming(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableMobilityAndMultihoming property value. Disable MOBIKE
        Args:
            value: Value to set for the disableMobilityAndMultihoming property.
        """
        self._disable_mobility_and_multihoming = value
    
    @property
    def disable_redirect(self,) -> Optional[bool]:
        """
        Gets the disableRedirect property value. Disable Redirect
        Returns: Optional[bool]
        """
        return self._disable_redirect
    
    @disable_redirect.setter
    def disable_redirect(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableRedirect property value. Disable Redirect
        Args:
            value: Value to set for the disableRedirect property.
        """
        self._disable_redirect = value
    
    @property
    def enable_always_on_configuration(self,) -> Optional[bool]:
        """
        Gets the enableAlwaysOnConfiguration property value. Determines if Always on VPN is enabled
        Returns: Optional[bool]
        """
        return self._enable_always_on_configuration
    
    @enable_always_on_configuration.setter
    def enable_always_on_configuration(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableAlwaysOnConfiguration property value. Determines if Always on VPN is enabled
        Args:
            value: Value to set for the enableAlwaysOnConfiguration property.
        """
        self._enable_always_on_configuration = value
    
    @property
    def enable_certificate_revocation_check(self,) -> Optional[bool]:
        """
        Gets the enableCertificateRevocationCheck property value. Enables a best-effort revocation check; server response timeouts will not cause it to fail
        Returns: Optional[bool]
        """
        return self._enable_certificate_revocation_check
    
    @enable_certificate_revocation_check.setter
    def enable_certificate_revocation_check(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableCertificateRevocationCheck property value. Enables a best-effort revocation check; server response timeouts will not cause it to fail
        Args:
            value: Value to set for the enableCertificateRevocationCheck property.
        """
        self._enable_certificate_revocation_check = value
    
    @property
    def enable_e_a_p(self,) -> Optional[bool]:
        """
        Gets the enableEAP property value. Enables EAP only authentication
        Returns: Optional[bool]
        """
        return self._enable_e_a_p
    
    @enable_e_a_p.setter
    def enable_e_a_p(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableEAP property value. Enables EAP only authentication
        Args:
            value: Value to set for the enableEAP property.
        """
        self._enable_e_a_p = value
    
    @property
    def enable_perfect_forward_secrecy(self,) -> Optional[bool]:
        """
        Gets the enablePerfectForwardSecrecy property value. Enable Perfect Forward Secrecy (PFS).
        Returns: Optional[bool]
        """
        return self._enable_perfect_forward_secrecy
    
    @enable_perfect_forward_secrecy.setter
    def enable_perfect_forward_secrecy(self,value: Optional[bool] = None) -> None:
        """
        Sets the enablePerfectForwardSecrecy property value. Enable Perfect Forward Secrecy (PFS).
        Args:
            value: Value to set for the enablePerfectForwardSecrecy property.
        """
        self._enable_perfect_forward_secrecy = value
    
    @property
    def enable_use_internal_subnet_attributes(self,) -> Optional[bool]:
        """
        Gets the enableUseInternalSubnetAttributes property value. Enable Use Internal Subnet Attributes.
        Returns: Optional[bool]
        """
        return self._enable_use_internal_subnet_attributes
    
    @enable_use_internal_subnet_attributes.setter
    def enable_use_internal_subnet_attributes(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableUseInternalSubnetAttributes property value. Enable Use Internal Subnet Attributes.
        Args:
            value: Value to set for the enableUseInternalSubnetAttributes property.
        """
        self._enable_use_internal_subnet_attributes = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_default_child_security_association_parameters": lambda n : setattr(self, 'allow_default_child_security_association_parameters', n.get_bool_value()),
            "allow_default_security_association_parameters": lambda n : setattr(self, 'allow_default_security_association_parameters', n.get_bool_value()),
            "always_on_configuration": lambda n : setattr(self, 'always_on_configuration', n.get_object_value(apple_vpn_always_on_configuration.AppleVpnAlwaysOnConfiguration)),
            "child_security_association_parameters": lambda n : setattr(self, 'child_security_association_parameters', n.get_object_value(ios_vpn_security_association_parameters.IosVpnSecurityAssociationParameters)),
            "client_authentication_type": lambda n : setattr(self, 'client_authentication_type', n.get_enum_value(vpn_client_authentication_type.VpnClientAuthenticationType)),
            "dead_peer_detection_rate": lambda n : setattr(self, 'dead_peer_detection_rate', n.get_enum_value(vpn_dead_peer_detection_rate.VpnDeadPeerDetectionRate)),
            "disable_mobility_and_multihoming": lambda n : setattr(self, 'disable_mobility_and_multihoming', n.get_bool_value()),
            "disable_redirect": lambda n : setattr(self, 'disable_redirect', n.get_bool_value()),
            "enable_always_on_configuration": lambda n : setattr(self, 'enable_always_on_configuration', n.get_bool_value()),
            "enable_certificate_revocation_check": lambda n : setattr(self, 'enable_certificate_revocation_check', n.get_bool_value()),
            "enable_e_a_p": lambda n : setattr(self, 'enable_e_a_p', n.get_bool_value()),
            "enable_perfect_forward_secrecy": lambda n : setattr(self, 'enable_perfect_forward_secrecy', n.get_bool_value()),
            "enable_use_internal_subnet_attributes": lambda n : setattr(self, 'enable_use_internal_subnet_attributes', n.get_bool_value()),
            "local_identifier": lambda n : setattr(self, 'local_identifier', n.get_enum_value(vpn_local_identifier.VpnLocalIdentifier)),
            "mtu_size_in_bytes": lambda n : setattr(self, 'mtu_size_in_bytes', n.get_int_value()),
            "remote_identifier": lambda n : setattr(self, 'remote_identifier', n.get_str_value()),
            "security_association_parameters": lambda n : setattr(self, 'security_association_parameters', n.get_object_value(ios_vpn_security_association_parameters.IosVpnSecurityAssociationParameters)),
            "server_certificate_common_name": lambda n : setattr(self, 'server_certificate_common_name', n.get_str_value()),
            "server_certificate_issuer_common_name": lambda n : setattr(self, 'server_certificate_issuer_common_name', n.get_str_value()),
            "server_certificate_type": lambda n : setattr(self, 'server_certificate_type', n.get_enum_value(vpn_server_certificate_type.VpnServerCertificateType)),
            "shared_secret": lambda n : setattr(self, 'shared_secret', n.get_str_value()),
            "tls_maximum_version": lambda n : setattr(self, 'tls_maximum_version', n.get_str_value()),
            "tls_minimum_version": lambda n : setattr(self, 'tls_minimum_version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def local_identifier(self,) -> Optional[vpn_local_identifier.VpnLocalIdentifier]:
        """
        Gets the localIdentifier property value. The type of VPN local identifier
        Returns: Optional[vpn_local_identifier.VpnLocalIdentifier]
        """
        return self._local_identifier
    
    @local_identifier.setter
    def local_identifier(self,value: Optional[vpn_local_identifier.VpnLocalIdentifier] = None) -> None:
        """
        Sets the localIdentifier property value. The type of VPN local identifier
        Args:
            value: Value to set for the localIdentifier property.
        """
        self._local_identifier = value
    
    @property
    def mtu_size_in_bytes(self,) -> Optional[int]:
        """
        Gets the mtuSizeInBytes property value. Maximum transmission unit. Valid values 1280 to 1400
        Returns: Optional[int]
        """
        return self._mtu_size_in_bytes
    
    @mtu_size_in_bytes.setter
    def mtu_size_in_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the mtuSizeInBytes property value. Maximum transmission unit. Valid values 1280 to 1400
        Args:
            value: Value to set for the mtuSizeInBytes property.
        """
        self._mtu_size_in_bytes = value
    
    @property
    def remote_identifier(self,) -> Optional[str]:
        """
        Gets the remoteIdentifier property value. Address of the IKEv2 server. Must be a FQDN, UserFQDN, network address, or ASN1DN
        Returns: Optional[str]
        """
        return self._remote_identifier
    
    @remote_identifier.setter
    def remote_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the remoteIdentifier property value. Address of the IKEv2 server. Must be a FQDN, UserFQDN, network address, or ASN1DN
        Args:
            value: Value to set for the remoteIdentifier property.
        """
        self._remote_identifier = value
    
    @property
    def security_association_parameters(self,) -> Optional[ios_vpn_security_association_parameters.IosVpnSecurityAssociationParameters]:
        """
        Gets the securityAssociationParameters property value. Security Association Parameters
        Returns: Optional[ios_vpn_security_association_parameters.IosVpnSecurityAssociationParameters]
        """
        return self._security_association_parameters
    
    @security_association_parameters.setter
    def security_association_parameters(self,value: Optional[ios_vpn_security_association_parameters.IosVpnSecurityAssociationParameters] = None) -> None:
        """
        Sets the securityAssociationParameters property value. Security Association Parameters
        Args:
            value: Value to set for the securityAssociationParameters property.
        """
        self._security_association_parameters = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowDefaultChildSecurityAssociationParameters", self.allow_default_child_security_association_parameters)
        writer.write_bool_value("allowDefaultSecurityAssociationParameters", self.allow_default_security_association_parameters)
        writer.write_object_value("alwaysOnConfiguration", self.always_on_configuration)
        writer.write_object_value("childSecurityAssociationParameters", self.child_security_association_parameters)
        writer.write_enum_value("clientAuthenticationType", self.client_authentication_type)
        writer.write_enum_value("deadPeerDetectionRate", self.dead_peer_detection_rate)
        writer.write_bool_value("disableMobilityAndMultihoming", self.disable_mobility_and_multihoming)
        writer.write_bool_value("disableRedirect", self.disable_redirect)
        writer.write_bool_value("enableAlwaysOnConfiguration", self.enable_always_on_configuration)
        writer.write_bool_value("enableCertificateRevocationCheck", self.enable_certificate_revocation_check)
        writer.write_bool_value("enableEAP", self.enable_e_a_p)
        writer.write_bool_value("enablePerfectForwardSecrecy", self.enable_perfect_forward_secrecy)
        writer.write_bool_value("enableUseInternalSubnetAttributes", self.enable_use_internal_subnet_attributes)
        writer.write_enum_value("localIdentifier", self.local_identifier)
        writer.write_int_value("mtuSizeInBytes", self.mtu_size_in_bytes)
        writer.write_str_value("remoteIdentifier", self.remote_identifier)
        writer.write_object_value("securityAssociationParameters", self.security_association_parameters)
        writer.write_str_value("serverCertificateCommonName", self.server_certificate_common_name)
        writer.write_str_value("serverCertificateIssuerCommonName", self.server_certificate_issuer_common_name)
        writer.write_enum_value("serverCertificateType", self.server_certificate_type)
        writer.write_str_value("sharedSecret", self.shared_secret)
        writer.write_str_value("tlsMaximumVersion", self.tls_maximum_version)
        writer.write_str_value("tlsMinimumVersion", self.tls_minimum_version)
    
    @property
    def server_certificate_common_name(self,) -> Optional[str]:
        """
        Gets the serverCertificateCommonName property value. Common name of the IKEv2 Server Certificate used in Server Authentication
        Returns: Optional[str]
        """
        return self._server_certificate_common_name
    
    @server_certificate_common_name.setter
    def server_certificate_common_name(self,value: Optional[str] = None) -> None:
        """
        Sets the serverCertificateCommonName property value. Common name of the IKEv2 Server Certificate used in Server Authentication
        Args:
            value: Value to set for the serverCertificateCommonName property.
        """
        self._server_certificate_common_name = value
    
    @property
    def server_certificate_issuer_common_name(self,) -> Optional[str]:
        """
        Gets the serverCertificateIssuerCommonName property value. Issuer Common name of the IKEv2 Server Certificate issuer used in Authentication
        Returns: Optional[str]
        """
        return self._server_certificate_issuer_common_name
    
    @server_certificate_issuer_common_name.setter
    def server_certificate_issuer_common_name(self,value: Optional[str] = None) -> None:
        """
        Sets the serverCertificateIssuerCommonName property value. Issuer Common name of the IKEv2 Server Certificate issuer used in Authentication
        Args:
            value: Value to set for the serverCertificateIssuerCommonName property.
        """
        self._server_certificate_issuer_common_name = value
    
    @property
    def server_certificate_type(self,) -> Optional[vpn_server_certificate_type.VpnServerCertificateType]:
        """
        Gets the serverCertificateType property value. The type of certificate the VPN server will present to the VPN client for authentication. Possible values are: rsa, ecdsa256, ecdsa384, ecdsa521.
        Returns: Optional[vpn_server_certificate_type.VpnServerCertificateType]
        """
        return self._server_certificate_type
    
    @server_certificate_type.setter
    def server_certificate_type(self,value: Optional[vpn_server_certificate_type.VpnServerCertificateType] = None) -> None:
        """
        Sets the serverCertificateType property value. The type of certificate the VPN server will present to the VPN client for authentication. Possible values are: rsa, ecdsa256, ecdsa384, ecdsa521.
        Args:
            value: Value to set for the serverCertificateType property.
        """
        self._server_certificate_type = value
    
    @property
    def shared_secret(self,) -> Optional[str]:
        """
        Gets the sharedSecret property value. Used when Shared Secret Authentication is selected
        Returns: Optional[str]
        """
        return self._shared_secret
    
    @shared_secret.setter
    def shared_secret(self,value: Optional[str] = None) -> None:
        """
        Sets the sharedSecret property value. Used when Shared Secret Authentication is selected
        Args:
            value: Value to set for the sharedSecret property.
        """
        self._shared_secret = value
    
    @property
    def tls_maximum_version(self,) -> Optional[str]:
        """
        Gets the tlsMaximumVersion property value. The maximum TLS version to be used with EAP-TLS authentication
        Returns: Optional[str]
        """
        return self._tls_maximum_version
    
    @tls_maximum_version.setter
    def tls_maximum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the tlsMaximumVersion property value. The maximum TLS version to be used with EAP-TLS authentication
        Args:
            value: Value to set for the tlsMaximumVersion property.
        """
        self._tls_maximum_version = value
    
    @property
    def tls_minimum_version(self,) -> Optional[str]:
        """
        Gets the tlsMinimumVersion property value. The minimum TLS version to be used with EAP-TLS authentication
        Returns: Optional[str]
        """
        return self._tls_minimum_version
    
    @tls_minimum_version.setter
    def tls_minimum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the tlsMinimumVersion property value. The minimum TLS version to be used with EAP-TLS authentication
        Args:
            value: Value to set for the tlsMinimumVersion property.
        """
        self._tls_minimum_version = value
    

