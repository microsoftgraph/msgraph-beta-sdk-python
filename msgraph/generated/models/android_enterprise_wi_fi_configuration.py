from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_certificate_profile_base import AndroidCertificateProfileBase
    from .android_eap_type import AndroidEapType
    from .android_trusted_root_certificate import AndroidTrustedRootCertificate
    from .android_wi_fi_configuration import AndroidWiFiConfiguration
    from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
    from .non_eap_authentication_method_for_peap import NonEapAuthenticationMethodForPeap
    from .wi_fi_authentication_method import WiFiAuthenticationMethod

from .android_wi_fi_configuration import AndroidWiFiConfiguration

@dataclass
class AndroidEnterpriseWiFiConfiguration(AndroidWiFiConfiguration):
    """
    By providing the configurations in this profile you can instruct the Android device to connect to desired Wi-Fi endpoint. By specifying the authentication method and security types expected by Wi-Fi endpoint you can make the Wi-Fi connection seamless for end user.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidEnterpriseWiFiConfiguration"
    # Indicates the Authentication Method the client (device) needs to use when the EAP Type is configured to PEAP or EAP-TTLS. Possible values are: certificate, usernameAndPassword, derivedCredential.
    authentication_method: Optional[WiFiAuthenticationMethod] = None
    # Extensible Authentication Protocol (EAP) Configuration Types.
    eap_type: Optional[AndroidEapType] = None
    # Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication). This is the certificate presented by client to the Wi-Fi endpoint. The authentication server sitting behind the Wi-Fi endpoint must accept this certificate to successfully establish a Wi-Fi connection.
    identity_certificate_for_client_authentication: Optional[AndroidCertificateProfileBase] = None
    # Non-EAP Method for Authentication (Inner Identity) when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
    inner_authentication_protocol_for_eap_ttls: Optional[NonEapAuthenticationMethodForEapTtlsType] = None
    # Non-EAP Method for Authentication (Inner Identity) when EAP Type is PEAP and Authenticationmethod is Username and Password. Possible values are: none, microsoftChapVersionTwo.
    inner_authentication_protocol_for_peap: Optional[NonEapAuthenticationMethodForPeap] = None
    # Enable identity privacy (Outer Identity) when EAP Type is configured to EAP-TTLS or PEAP. The String provided here is used to mask the username of individual users when they attempt to connect to Wi-Fi network.
    outer_identity_privacy_temporary_value: Optional[str] = None
    # Password format string used to build the password to connect to wifi
    password_format_string: Optional[str] = None
    # PreSharedKey used to build the password to connect to wifi
    pre_shared_key: Optional[str] = None
    # Trusted Root Certificate for Server Validation when EAP Type is configured to EAP-TLS, EAP-TTLS or PEAP. This is the certificate presented by the Wi-Fi endpoint when the device attempts to connect to Wi-Fi endpoint. The device (or user) must accept this certificate to continue the connection attempt.
    root_certificate_for_server_validation: Optional[AndroidTrustedRootCertificate] = None
    # Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users' devices when they connect to this Wi-Fi network.
    trusted_server_certificate_names: Optional[List[str]] = None
    # Username format string used to build the username to connect to wifi
    username_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidEnterpriseWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidEnterpriseWiFiConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidEnterpriseWiFiConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_certificate_profile_base import AndroidCertificateProfileBase
        from .android_eap_type import AndroidEapType
        from .android_trusted_root_certificate import AndroidTrustedRootCertificate
        from .android_wi_fi_configuration import AndroidWiFiConfiguration
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .non_eap_authentication_method_for_peap import NonEapAuthenticationMethodForPeap
        from .wi_fi_authentication_method import WiFiAuthenticationMethod

        from .android_certificate_profile_base import AndroidCertificateProfileBase
        from .android_eap_type import AndroidEapType
        from .android_trusted_root_certificate import AndroidTrustedRootCertificate
        from .android_wi_fi_configuration import AndroidWiFiConfiguration
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .non_eap_authentication_method_for_peap import NonEapAuthenticationMethodForPeap
        from .wi_fi_authentication_method import WiFiAuthenticationMethod

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(WiFiAuthenticationMethod)),
            "eapType": lambda n : setattr(self, 'eap_type', n.get_enum_value(AndroidEapType)),
            "identityCertificateForClientAuthentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(AndroidCertificateProfileBase)),
            "innerAuthenticationProtocolForEapTtls": lambda n : setattr(self, 'inner_authentication_protocol_for_eap_ttls', n.get_enum_value(NonEapAuthenticationMethodForEapTtlsType)),
            "innerAuthenticationProtocolForPeap": lambda n : setattr(self, 'inner_authentication_protocol_for_peap', n.get_enum_value(NonEapAuthenticationMethodForPeap)),
            "outerIdentityPrivacyTemporaryValue": lambda n : setattr(self, 'outer_identity_privacy_temporary_value', n.get_str_value()),
            "passwordFormatString": lambda n : setattr(self, 'password_format_string', n.get_str_value()),
            "preSharedKey": lambda n : setattr(self, 'pre_shared_key', n.get_str_value()),
            "rootCertificateForServerValidation": lambda n : setattr(self, 'root_certificate_for_server_validation', n.get_object_value(AndroidTrustedRootCertificate)),
            "trustedServerCertificateNames": lambda n : setattr(self, 'trusted_server_certificate_names', n.get_collection_of_primitive_values(str)),
            "usernameFormatString": lambda n : setattr(self, 'username_format_string', n.get_str_value()),
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
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_enum_value("eapType", self.eap_type)
        writer.write_object_value("identityCertificateForClientAuthentication", self.identity_certificate_for_client_authentication)
        writer.write_enum_value("innerAuthenticationProtocolForEapTtls", self.inner_authentication_protocol_for_eap_ttls)
        writer.write_enum_value("innerAuthenticationProtocolForPeap", self.inner_authentication_protocol_for_peap)
        writer.write_str_value("outerIdentityPrivacyTemporaryValue", self.outer_identity_privacy_temporary_value)
        writer.write_str_value("passwordFormatString", self.password_format_string)
        writer.write_str_value("preSharedKey", self.pre_shared_key)
        writer.write_object_value("rootCertificateForServerValidation", self.root_certificate_for_server_validation)
        writer.write_collection_of_primitive_values("trustedServerCertificateNames", self.trusted_server_certificate_names)
        writer.write_str_value("usernameFormatString", self.username_format_string)
    

