from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_eap_type, android_for_work_certificate_profile_base, android_for_work_trusted_root_certificate, android_for_work_wi_fi_configuration, non_eap_authentication_method_for_eap_ttls_type, non_eap_authentication_method_for_peap, wi_fi_authentication_method

from . import android_for_work_wi_fi_configuration

class AndroidForWorkEnterpriseWiFiConfiguration(android_for_work_wi_fi_configuration.AndroidForWorkWiFiConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidForWorkEnterpriseWiFiConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidForWorkEnterpriseWiFiConfiguration"
        # Indicates the Authentication Method the client (device) needs to use when the EAP Type is configured to PEAP or EAP-TTLS. Possible values are: certificate, usernameAndPassword, derivedCredential.
        self._authentication_method: Optional[wi_fi_authentication_method.WiFiAuthenticationMethod] = None
        # Extensible Authentication Protocol (EAP) Configuration Types.
        self._eap_type: Optional[android_eap_type.AndroidEapType] = None
        # Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication). This is the certificate presented by client to the Wi-Fi endpoint. The authentication server sitting behind the Wi-Fi endpoint must accept this certificate to successfully establish a Wi-Fi connection.
        self._identity_certificate_for_client_authentication: Optional[android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase] = None
        # Non-EAP Method for Authentication (Inner Identity) when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
        self._inner_authentication_protocol_for_eap_ttls: Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType] = None
        # Non-EAP Method for Authentication (Inner Identity) when EAP Type is PEAP and Authenticationmethod is Username and Password. Possible values are: none, microsoftChapVersionTwo.
        self._inner_authentication_protocol_for_peap: Optional[non_eap_authentication_method_for_peap.NonEapAuthenticationMethodForPeap] = None
        # Enable identity privacy (Outer Identity) when EAP Type is configured to EAP-TTLS or PEAP. The String provided here is used to mask the username of individual users when they attempt to connect to Wi-Fi network.
        self._outer_identity_privacy_temporary_value: Optional[str] = None
        # Trusted Root Certificate for Server Validation when EAP Type is configured to EAP-TLS, EAP-TTLS or PEAP. This is the certificate presented by the Wi-Fi endpoint when the device attempts to connect to Wi-Fi endpoint. The device (or user) must accept this certificate to continue the connection attempt.
        self._root_certificate_for_server_validation: Optional[android_for_work_trusted_root_certificate.AndroidForWorkTrustedRootCertificate] = None
        # Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users' devices when they connect to this Wi-Fi network.
        self._trusted_server_certificate_names: Optional[List[str]] = None
    
    @property
    def authentication_method(self,) -> Optional[wi_fi_authentication_method.WiFiAuthenticationMethod]:
        """
        Gets the authenticationMethod property value. Indicates the Authentication Method the client (device) needs to use when the EAP Type is configured to PEAP or EAP-TTLS. Possible values are: certificate, usernameAndPassword, derivedCredential.
        Returns: Optional[wi_fi_authentication_method.WiFiAuthenticationMethod]
        """
        return self._authentication_method
    
    @authentication_method.setter
    def authentication_method(self,value: Optional[wi_fi_authentication_method.WiFiAuthenticationMethod] = None) -> None:
        """
        Sets the authenticationMethod property value. Indicates the Authentication Method the client (device) needs to use when the EAP Type is configured to PEAP or EAP-TTLS. Possible values are: certificate, usernameAndPassword, derivedCredential.
        Args:
            value: Value to set for the authentication_method property.
        """
        self._authentication_method = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidForWorkEnterpriseWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkEnterpriseWiFiConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidForWorkEnterpriseWiFiConfiguration()
    
    @property
    def eap_type(self,) -> Optional[android_eap_type.AndroidEapType]:
        """
        Gets the eapType property value. Extensible Authentication Protocol (EAP) Configuration Types.
        Returns: Optional[android_eap_type.AndroidEapType]
        """
        return self._eap_type
    
    @eap_type.setter
    def eap_type(self,value: Optional[android_eap_type.AndroidEapType] = None) -> None:
        """
        Sets the eapType property value. Extensible Authentication Protocol (EAP) Configuration Types.
        Args:
            value: Value to set for the eap_type property.
        """
        self._eap_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_eap_type, android_for_work_certificate_profile_base, android_for_work_trusted_root_certificate, android_for_work_wi_fi_configuration, non_eap_authentication_method_for_eap_ttls_type, non_eap_authentication_method_for_peap, wi_fi_authentication_method

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(wi_fi_authentication_method.WiFiAuthenticationMethod)),
            "eapType": lambda n : setattr(self, 'eap_type', n.get_enum_value(android_eap_type.AndroidEapType)),
            "identityCertificateForClientAuthentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase)),
            "innerAuthenticationProtocolForEapTtls": lambda n : setattr(self, 'inner_authentication_protocol_for_eap_ttls', n.get_enum_value(non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType)),
            "innerAuthenticationProtocolForPeap": lambda n : setattr(self, 'inner_authentication_protocol_for_peap', n.get_enum_value(non_eap_authentication_method_for_peap.NonEapAuthenticationMethodForPeap)),
            "outerIdentityPrivacyTemporaryValue": lambda n : setattr(self, 'outer_identity_privacy_temporary_value', n.get_str_value()),
            "rootCertificateForServerValidation": lambda n : setattr(self, 'root_certificate_for_server_validation', n.get_object_value(android_for_work_trusted_root_certificate.AndroidForWorkTrustedRootCertificate)),
            "trustedServerCertificateNames": lambda n : setattr(self, 'trusted_server_certificate_names', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_certificate_for_client_authentication(self,) -> Optional[android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase]:
        """
        Gets the identityCertificateForClientAuthentication property value. Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication). This is the certificate presented by client to the Wi-Fi endpoint. The authentication server sitting behind the Wi-Fi endpoint must accept this certificate to successfully establish a Wi-Fi connection.
        Returns: Optional[android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase]
        """
        return self._identity_certificate_for_client_authentication
    
    @identity_certificate_for_client_authentication.setter
    def identity_certificate_for_client_authentication(self,value: Optional[android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificateForClientAuthentication property value. Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication). This is the certificate presented by client to the Wi-Fi endpoint. The authentication server sitting behind the Wi-Fi endpoint must accept this certificate to successfully establish a Wi-Fi connection.
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
    def inner_authentication_protocol_for_peap(self,) -> Optional[non_eap_authentication_method_for_peap.NonEapAuthenticationMethodForPeap]:
        """
        Gets the innerAuthenticationProtocolForPeap property value. Non-EAP Method for Authentication (Inner Identity) when EAP Type is PEAP and Authenticationmethod is Username and Password. Possible values are: none, microsoftChapVersionTwo.
        Returns: Optional[non_eap_authentication_method_for_peap.NonEapAuthenticationMethodForPeap]
        """
        return self._inner_authentication_protocol_for_peap
    
    @inner_authentication_protocol_for_peap.setter
    def inner_authentication_protocol_for_peap(self,value: Optional[non_eap_authentication_method_for_peap.NonEapAuthenticationMethodForPeap] = None) -> None:
        """
        Sets the innerAuthenticationProtocolForPeap property value. Non-EAP Method for Authentication (Inner Identity) when EAP Type is PEAP and Authenticationmethod is Username and Password. Possible values are: none, microsoftChapVersionTwo.
        Args:
            value: Value to set for the inner_authentication_protocol_for_peap property.
        """
        self._inner_authentication_protocol_for_peap = value
    
    @property
    def outer_identity_privacy_temporary_value(self,) -> Optional[str]:
        """
        Gets the outerIdentityPrivacyTemporaryValue property value. Enable identity privacy (Outer Identity) when EAP Type is configured to EAP-TTLS or PEAP. The String provided here is used to mask the username of individual users when they attempt to connect to Wi-Fi network.
        Returns: Optional[str]
        """
        return self._outer_identity_privacy_temporary_value
    
    @outer_identity_privacy_temporary_value.setter
    def outer_identity_privacy_temporary_value(self,value: Optional[str] = None) -> None:
        """
        Sets the outerIdentityPrivacyTemporaryValue property value. Enable identity privacy (Outer Identity) when EAP Type is configured to EAP-TTLS or PEAP. The String provided here is used to mask the username of individual users when they attempt to connect to Wi-Fi network.
        Args:
            value: Value to set for the outer_identity_privacy_temporary_value property.
        """
        self._outer_identity_privacy_temporary_value = value
    
    @property
    def root_certificate_for_server_validation(self,) -> Optional[android_for_work_trusted_root_certificate.AndroidForWorkTrustedRootCertificate]:
        """
        Gets the rootCertificateForServerValidation property value. Trusted Root Certificate for Server Validation when EAP Type is configured to EAP-TLS, EAP-TTLS or PEAP. This is the certificate presented by the Wi-Fi endpoint when the device attempts to connect to Wi-Fi endpoint. The device (or user) must accept this certificate to continue the connection attempt.
        Returns: Optional[android_for_work_trusted_root_certificate.AndroidForWorkTrustedRootCertificate]
        """
        return self._root_certificate_for_server_validation
    
    @root_certificate_for_server_validation.setter
    def root_certificate_for_server_validation(self,value: Optional[android_for_work_trusted_root_certificate.AndroidForWorkTrustedRootCertificate] = None) -> None:
        """
        Sets the rootCertificateForServerValidation property value. Trusted Root Certificate for Server Validation when EAP Type is configured to EAP-TLS, EAP-TTLS or PEAP. This is the certificate presented by the Wi-Fi endpoint when the device attempts to connect to Wi-Fi endpoint. The device (or user) must accept this certificate to continue the connection attempt.
        Args:
            value: Value to set for the root_certificate_for_server_validation property.
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
        writer.write_enum_value("eapType", self.eap_type)
        writer.write_object_value("identityCertificateForClientAuthentication", self.identity_certificate_for_client_authentication)
        writer.write_enum_value("innerAuthenticationProtocolForEapTtls", self.inner_authentication_protocol_for_eap_ttls)
        writer.write_enum_value("innerAuthenticationProtocolForPeap", self.inner_authentication_protocol_for_peap)
        writer.write_str_value("outerIdentityPrivacyTemporaryValue", self.outer_identity_privacy_temporary_value)
        writer.write_object_value("rootCertificateForServerValidation", self.root_certificate_for_server_validation)
        writer.write_collection_of_primitive_values("trustedServerCertificateNames", self.trusted_server_certificate_names)
    
    @property
    def trusted_server_certificate_names(self,) -> Optional[List[str]]:
        """
        Gets the trustedServerCertificateNames property value. Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users' devices when they connect to this Wi-Fi network.
        Returns: Optional[List[str]]
        """
        return self._trusted_server_certificate_names
    
    @trusted_server_certificate_names.setter
    def trusted_server_certificate_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the trustedServerCertificateNames property value. Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users' devices when they connect to this Wi-Fi network.
        Args:
            value: Value to set for the trusted_server_certificate_names property.
        """
        self._trusted_server_certificate_names = value
    

