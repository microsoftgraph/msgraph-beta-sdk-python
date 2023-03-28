from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import eap_fast_configuration, eap_type, mac_o_s_certificate_profile_base, mac_o_s_trusted_root_certificate, mac_o_s_wi_fi_configuration, non_eap_authentication_method_for_eap_ttls_type, wi_fi_authentication_method

from . import mac_o_s_wi_fi_configuration

class MacOSEnterpriseWiFiConfiguration(mac_o_s_wi_fi_configuration.MacOSWiFiConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSEnterpriseWiFiConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSEnterpriseWiFiConfiguration"
        # Authentication Method when EAP Type is configured to PEAP or EAP-TTLS. Possible values are: certificate, usernameAndPassword, derivedCredential.
        self._authentication_method: Optional[wi_fi_authentication_method.WiFiAuthenticationMethod] = None
        # EAP-FAST Configuration Option when EAP-FAST is the selected EAP Type. Possible values are: noProtectedAccessCredential, useProtectedAccessCredential, useProtectedAccessCredentialAndProvision, useProtectedAccessCredentialAndProvisionAnonymously.
        self._eap_fast_configuration: Optional[eap_fast_configuration.EapFastConfiguration] = None
        # Extensible Authentication Protocol (EAP) configuration types.
        self._eap_type: Optional[eap_type.EapType] = None
        # Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication).
        self._identity_certificate_for_client_authentication: Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase] = None
        # Non-EAP Method for Authentication (Inner Identity) when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
        self._inner_authentication_protocol_for_eap_ttls: Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType] = None
        # Enable identity privacy (Outer Identity) when EAP Type is configured to EAP-TTLS, EAP-FAST or PEAP. This property masks usernames with the text you enter. For example, if you use 'anonymous', each user that authenticates with this Wi-Fi connection using their real username is displayed as 'anonymous'.
        self._outer_identity_privacy_temporary_value: Optional[str] = None
        # Trusted Root Certificate for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP.
        self._root_certificate_for_server_validation: Optional[mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate] = None
        # Trusted Root Certificates for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. If you provide this value you do not need to provide trustedServerCertificateNames, and vice versa. This collection can contain a maximum of 500 elements.
        self._root_certificates_for_server_validation: Optional[List[mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate]] = None
        # Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users devices when they connect to this Wi-Fi network.
        self._trusted_server_certificate_names: Optional[List[str]] = None
    
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
            value: Value to set for the authentication_method property.
        """
        self._authentication_method = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSEnterpriseWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSEnterpriseWiFiConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSEnterpriseWiFiConfiguration()
    
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
            value: Value to set for the eap_fast_configuration property.
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
            value: Value to set for the eap_type property.
        """
        self._eap_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import eap_fast_configuration, eap_type, mac_o_s_certificate_profile_base, mac_o_s_trusted_root_certificate, mac_o_s_wi_fi_configuration, non_eap_authentication_method_for_eap_ttls_type, wi_fi_authentication_method

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(wi_fi_authentication_method.WiFiAuthenticationMethod)),
            "eapFastConfiguration": lambda n : setattr(self, 'eap_fast_configuration', n.get_enum_value(eap_fast_configuration.EapFastConfiguration)),
            "eapType": lambda n : setattr(self, 'eap_type', n.get_enum_value(eap_type.EapType)),
            "identityCertificateForClientAuthentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(mac_o_s_certificate_profile_base.MacOSCertificateProfileBase)),
            "innerAuthenticationProtocolForEapTtls": lambda n : setattr(self, 'inner_authentication_protocol_for_eap_ttls', n.get_enum_value(non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType)),
            "outerIdentityPrivacyTemporaryValue": lambda n : setattr(self, 'outer_identity_privacy_temporary_value', n.get_str_value()),
            "rootCertificatesForServerValidation": lambda n : setattr(self, 'root_certificates_for_server_validation', n.get_collection_of_object_values(mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate)),
            "rootCertificateForServerValidation": lambda n : setattr(self, 'root_certificate_for_server_validation', n.get_object_value(mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate)),
            "trustedServerCertificateNames": lambda n : setattr(self, 'trusted_server_certificate_names', n.get_collection_of_primitive_values(str)),
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
            value: Value to set for the identity_certificate_for_client_authentication property.
        """
        self._identity_certificate_for_client_authentication = value
    
    @property
    def inner_authentication_protocol_for_eap_ttls(self,) -> Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType]:
        """
        Gets the innerAuthenticationProtocolForEapTtls property value. Non-EAP Method for Authentication (Inner Identity) when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
        Returns: Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType]
        """
        return self._inner_authentication_protocol_for_eap_ttls
    
    @inner_authentication_protocol_for_eap_ttls.setter
    def inner_authentication_protocol_for_eap_ttls(self,value: Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType] = None) -> None:
        """
        Sets the innerAuthenticationProtocolForEapTtls property value. Non-EAP Method for Authentication (Inner Identity) when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
        Args:
            value: Value to set for the inner_authentication_protocol_for_eap_ttls property.
        """
        self._inner_authentication_protocol_for_eap_ttls = value
    
    @property
    def outer_identity_privacy_temporary_value(self,) -> Optional[str]:
        """
        Gets the outerIdentityPrivacyTemporaryValue property value. Enable identity privacy (Outer Identity) when EAP Type is configured to EAP-TTLS, EAP-FAST or PEAP. This property masks usernames with the text you enter. For example, if you use 'anonymous', each user that authenticates with this Wi-Fi connection using their real username is displayed as 'anonymous'.
        Returns: Optional[str]
        """
        return self._outer_identity_privacy_temporary_value
    
    @outer_identity_privacy_temporary_value.setter
    def outer_identity_privacy_temporary_value(self,value: Optional[str] = None) -> None:
        """
        Sets the outerIdentityPrivacyTemporaryValue property value. Enable identity privacy (Outer Identity) when EAP Type is configured to EAP-TTLS, EAP-FAST or PEAP. This property masks usernames with the text you enter. For example, if you use 'anonymous', each user that authenticates with this Wi-Fi connection using their real username is displayed as 'anonymous'.
        Args:
            value: Value to set for the outer_identity_privacy_temporary_value property.
        """
        self._outer_identity_privacy_temporary_value = value
    
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
            value: Value to set for the root_certificate_for_server_validation property.
        """
        self._root_certificate_for_server_validation = value
    
    @property
    def root_certificates_for_server_validation(self,) -> Optional[List[mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate]]:
        """
        Gets the rootCertificatesForServerValidation property value. Trusted Root Certificates for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. If you provide this value you do not need to provide trustedServerCertificateNames, and vice versa. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate]]
        """
        return self._root_certificates_for_server_validation
    
    @root_certificates_for_server_validation.setter
    def root_certificates_for_server_validation(self,value: Optional[List[mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate]] = None) -> None:
        """
        Sets the rootCertificatesForServerValidation property value. Trusted Root Certificates for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. If you provide this value you do not need to provide trustedServerCertificateNames, and vice versa. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the root_certificates_for_server_validation property.
        """
        self._root_certificates_for_server_validation = value
    
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
        writer.write_object_value("identityCertificateForClientAuthentication", self.identity_certificate_for_client_authentication)
        writer.write_enum_value("innerAuthenticationProtocolForEapTtls", self.inner_authentication_protocol_for_eap_ttls)
        writer.write_str_value("outerIdentityPrivacyTemporaryValue", self.outer_identity_privacy_temporary_value)
        writer.write_collection_of_object_values("rootCertificatesForServerValidation", self.root_certificates_for_server_validation)
        writer.write_object_value("rootCertificateForServerValidation", self.root_certificate_for_server_validation)
        writer.write_collection_of_primitive_values("trustedServerCertificateNames", self.trusted_server_certificate_names)
    
    @property
    def trusted_server_certificate_names(self,) -> Optional[List[str]]:
        """
        Gets the trustedServerCertificateNames property value. Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users devices when they connect to this Wi-Fi network.
        Returns: Optional[List[str]]
        """
        return self._trusted_server_certificate_names
    
    @trusted_server_certificate_names.setter
    def trusted_server_certificate_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the trustedServerCertificateNames property value. Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users devices when they connect to this Wi-Fi network.
        Args:
            value: Value to set for the trusted_server_certificate_names property.
        """
        self._trusted_server_certificate_names = value
    

