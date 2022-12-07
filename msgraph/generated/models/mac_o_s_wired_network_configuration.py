from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
eap_fast_configuration = lazy_import('msgraph.generated.models.eap_fast_configuration')
eap_type = lazy_import('msgraph.generated.models.eap_type')
mac_o_s_certificate_profile_base = lazy_import('msgraph.generated.models.mac_o_s_certificate_profile_base')
mac_o_s_trusted_root_certificate = lazy_import('msgraph.generated.models.mac_o_s_trusted_root_certificate')
non_eap_authentication_method_for_eap_ttls_type = lazy_import('msgraph.generated.models.non_eap_authentication_method_for_eap_ttls_type')
wi_fi_authentication_method = lazy_import('msgraph.generated.models.wi_fi_authentication_method')
wired_network_interface = lazy_import('msgraph.generated.models.wired_network_interface')

class MacOSWiredNetworkConfiguration(device_configuration.DeviceConfiguration):
    @property
    def authentication_method(self,) -> Optional[wi_fi_authentication_method.WiFiAuthenticationMethod]:
        """
        Gets the authenticationMethod property value. Authentication Method when EAP Type is configured to PEAP or EAP-TTLS. Possible values are: certificate, usernameAndPassword, derivedCredential.
        Returns: Optional[wi_fi_authentication_method.WiFiAuthenticationMethod]
        """
        return self._authentication_method
    
    @authentication_method.setter
    def authentication_method(self,value: Optional[wi_fi_authentication_method.WiFiAuthenticationMethod] = None) -> None:
        """
        Sets the authenticationMethod property value. Authentication Method when EAP Type is configured to PEAP or EAP-TTLS. Possible values are: certificate, usernameAndPassword, derivedCredential.
        Args:
            value: Value to set for the authenticationMethod property.
        """
        self._authentication_method = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSWiredNetworkConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSWiredNetworkConfiguration"
        # Authentication Method when EAP Type is configured to PEAP or EAP-TTLS. Possible values are: certificate, usernameAndPassword, derivedCredential.
        self._authentication_method: Optional[wi_fi_authentication_method.WiFiAuthenticationMethod] = None
        # EAP-FAST Configuration Option when EAP-FAST is the selected EAP Type. Possible values are: noProtectedAccessCredential, useProtectedAccessCredential, useProtectedAccessCredentialAndProvision, useProtectedAccessCredentialAndProvisionAnonymously.
        self._eap_fast_configuration: Optional[eap_fast_configuration.EapFastConfiguration] = None
        # Extensible Authentication Protocol (EAP) configuration types.
        self._eap_type: Optional[eap_type.EapType] = None
        # Enable identity privacy (Outer Identity) when EAP Type is configured to EAP-TTLS, EAP-FAST or PEAP. This property masks usernames with the text you enter. For example, if you use 'anonymous', each user that authenticates with this wired network using their real username is displayed as 'anonymous'.
        self._enable_outer_identity_privacy: Optional[str] = None
        # Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication).
        self._identity_certificate_for_client_authentication: Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase] = None
        # Apple network interface type.
        self._network_interface: Optional[wired_network_interface.WiredNetworkInterface] = None
        # Network Name
        self._network_name: Optional[str] = None
        # Non-EAP Method for Authentication (Inner Identity) when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
        self._non_eap_authentication_method_for_eap_ttls: Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType] = None
        # Trusted Root Certificate for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP.
        self._root_certificate_for_server_validation: Optional[mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate] = None
        # Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users devices when they connect to this wired network.
        self._trusted_server_certificate_names: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSWiredNetworkConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSWiredNetworkConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSWiredNetworkConfiguration()
    
    @property
    def eap_fast_configuration(self,) -> Optional[eap_fast_configuration.EapFastConfiguration]:
        """
        Gets the eapFastConfiguration property value. EAP-FAST Configuration Option when EAP-FAST is the selected EAP Type. Possible values are: noProtectedAccessCredential, useProtectedAccessCredential, useProtectedAccessCredentialAndProvision, useProtectedAccessCredentialAndProvisionAnonymously.
        Returns: Optional[eap_fast_configuration.EapFastConfiguration]
        """
        return self._eap_fast_configuration
    
    @eap_fast_configuration.setter
    def eap_fast_configuration(self,value: Optional[eap_fast_configuration.EapFastConfiguration] = None) -> None:
        """
        Sets the eapFastConfiguration property value. EAP-FAST Configuration Option when EAP-FAST is the selected EAP Type. Possible values are: noProtectedAccessCredential, useProtectedAccessCredential, useProtectedAccessCredentialAndProvision, useProtectedAccessCredentialAndProvisionAnonymously.
        Args:
            value: Value to set for the eapFastConfiguration property.
        """
        self._eap_fast_configuration = value
    
    @property
    def eap_type(self,) -> Optional[eap_type.EapType]:
        """
        Gets the eapType property value. Extensible Authentication Protocol (EAP) configuration types.
        Returns: Optional[eap_type.EapType]
        """
        return self._eap_type
    
    @eap_type.setter
    def eap_type(self,value: Optional[eap_type.EapType] = None) -> None:
        """
        Sets the eapType property value. Extensible Authentication Protocol (EAP) configuration types.
        Args:
            value: Value to set for the eapType property.
        """
        self._eap_type = value
    
    @property
    def enable_outer_identity_privacy(self,) -> Optional[str]:
        """
        Gets the enableOuterIdentityPrivacy property value. Enable identity privacy (Outer Identity) when EAP Type is configured to EAP-TTLS, EAP-FAST or PEAP. This property masks usernames with the text you enter. For example, if you use 'anonymous', each user that authenticates with this wired network using their real username is displayed as 'anonymous'.
        Returns: Optional[str]
        """
        return self._enable_outer_identity_privacy
    
    @enable_outer_identity_privacy.setter
    def enable_outer_identity_privacy(self,value: Optional[str] = None) -> None:
        """
        Sets the enableOuterIdentityPrivacy property value. Enable identity privacy (Outer Identity) when EAP Type is configured to EAP-TTLS, EAP-FAST or PEAP. This property masks usernames with the text you enter. For example, if you use 'anonymous', each user that authenticates with this wired network using their real username is displayed as 'anonymous'.
        Args:
            value: Value to set for the enableOuterIdentityPrivacy property.
        """
        self._enable_outer_identity_privacy = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_method": lambda n : setattr(self, 'authentication_method', n.get_enum_value(wi_fi_authentication_method.WiFiAuthenticationMethod)),
            "eap_fast_configuration": lambda n : setattr(self, 'eap_fast_configuration', n.get_enum_value(eap_fast_configuration.EapFastConfiguration)),
            "eap_type": lambda n : setattr(self, 'eap_type', n.get_enum_value(eap_type.EapType)),
            "enable_outer_identity_privacy": lambda n : setattr(self, 'enable_outer_identity_privacy', n.get_str_value()),
            "identity_certificate_for_client_authentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(mac_o_s_certificate_profile_base.MacOSCertificateProfileBase)),
            "network_interface": lambda n : setattr(self, 'network_interface', n.get_enum_value(wired_network_interface.WiredNetworkInterface)),
            "network_name": lambda n : setattr(self, 'network_name', n.get_str_value()),
            "non_eap_authentication_method_for_eap_ttls": lambda n : setattr(self, 'non_eap_authentication_method_for_eap_ttls', n.get_enum_value(non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType)),
            "root_certificate_for_server_validation": lambda n : setattr(self, 'root_certificate_for_server_validation', n.get_object_value(mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate)),
            "trusted_server_certificate_names": lambda n : setattr(self, 'trusted_server_certificate_names', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_certificate_for_client_authentication(self,) -> Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase]:
        """
        Gets the identityCertificateForClientAuthentication property value. Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication).
        Returns: Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase]
        """
        return self._identity_certificate_for_client_authentication
    
    @identity_certificate_for_client_authentication.setter
    def identity_certificate_for_client_authentication(self,value: Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificateForClientAuthentication property value. Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication).
        Args:
            value: Value to set for the identityCertificateForClientAuthentication property.
        """
        self._identity_certificate_for_client_authentication = value
    
    @property
    def network_interface(self,) -> Optional[wired_network_interface.WiredNetworkInterface]:
        """
        Gets the networkInterface property value. Apple network interface type.
        Returns: Optional[wired_network_interface.WiredNetworkInterface]
        """
        return self._network_interface
    
    @network_interface.setter
    def network_interface(self,value: Optional[wired_network_interface.WiredNetworkInterface] = None) -> None:
        """
        Sets the networkInterface property value. Apple network interface type.
        Args:
            value: Value to set for the networkInterface property.
        """
        self._network_interface = value
    
    @property
    def network_name(self,) -> Optional[str]:
        """
        Gets the networkName property value. Network Name
        Returns: Optional[str]
        """
        return self._network_name
    
    @network_name.setter
    def network_name(self,value: Optional[str] = None) -> None:
        """
        Sets the networkName property value. Network Name
        Args:
            value: Value to set for the networkName property.
        """
        self._network_name = value
    
    @property
    def non_eap_authentication_method_for_eap_ttls(self,) -> Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType]:
        """
        Gets the nonEapAuthenticationMethodForEapTtls property value. Non-EAP Method for Authentication (Inner Identity) when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
        Returns: Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType]
        """
        return self._non_eap_authentication_method_for_eap_ttls
    
    @non_eap_authentication_method_for_eap_ttls.setter
    def non_eap_authentication_method_for_eap_ttls(self,value: Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType] = None) -> None:
        """
        Sets the nonEapAuthenticationMethodForEapTtls property value. Non-EAP Method for Authentication (Inner Identity) when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
        Args:
            value: Value to set for the nonEapAuthenticationMethodForEapTtls property.
        """
        self._non_eap_authentication_method_for_eap_ttls = value
    
    @property
    def root_certificate_for_server_validation(self,) -> Optional[mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate]:
        """
        Gets the rootCertificateForServerValidation property value. Trusted Root Certificate for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP.
        Returns: Optional[mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate]
        """
        return self._root_certificate_for_server_validation
    
    @root_certificate_for_server_validation.setter
    def root_certificate_for_server_validation(self,value: Optional[mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate] = None) -> None:
        """
        Sets the rootCertificateForServerValidation property value. Trusted Root Certificate for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP.
        Args:
            value: Value to set for the rootCertificateForServerValidation property.
        """
        self._root_certificate_for_server_validation = value
    
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
        writer.write_enum_value("eapFastConfiguration", self.eap_fast_configuration)
        writer.write_enum_value("eapType", self.eap_type)
        writer.write_str_value("enableOuterIdentityPrivacy", self.enable_outer_identity_privacy)
        writer.write_object_value("identityCertificateForClientAuthentication", self.identity_certificate_for_client_authentication)
        writer.write_enum_value("networkInterface", self.network_interface)
        writer.write_str_value("networkName", self.network_name)
        writer.write_enum_value("nonEapAuthenticationMethodForEapTtls", self.non_eap_authentication_method_for_eap_ttls)
        writer.write_object_value("rootCertificateForServerValidation", self.root_certificate_for_server_validation)
        writer.write_collection_of_primitive_values("trustedServerCertificateNames", self.trusted_server_certificate_names)
    
    @property
    def trusted_server_certificate_names(self,) -> Optional[List[str]]:
        """
        Gets the trustedServerCertificateNames property value. Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users devices when they connect to this wired network.
        Returns: Optional[List[str]]
        """
        return self._trusted_server_certificate_names
    
    @trusted_server_certificate_names.setter
    def trusted_server_certificate_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the trustedServerCertificateNames property value. Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users devices when they connect to this wired network.
        Args:
            value: Value to set for the trustedServerCertificateNames property.
        """
        self._trusted_server_certificate_names = value
    

