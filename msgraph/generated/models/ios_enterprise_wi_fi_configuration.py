from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_derived_credential_settings = lazy_import('msgraph.generated.models.device_management_derived_credential_settings')
eap_fast_configuration = lazy_import('msgraph.generated.models.eap_fast_configuration')
eap_type = lazy_import('msgraph.generated.models.eap_type')
ios_certificate_profile_base = lazy_import('msgraph.generated.models.ios_certificate_profile_base')
ios_trusted_root_certificate = lazy_import('msgraph.generated.models.ios_trusted_root_certificate')
ios_wi_fi_configuration = lazy_import('msgraph.generated.models.ios_wi_fi_configuration')
non_eap_authentication_method_for_eap_ttls_type = lazy_import('msgraph.generated.models.non_eap_authentication_method_for_eap_ttls_type')
wi_fi_authentication_method = lazy_import('msgraph.generated.models.wi_fi_authentication_method')

class IosEnterpriseWiFiConfiguration(ios_wi_fi_configuration.IosWiFiConfiguration):
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
        Instantiates a new IosEnterpriseWiFiConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosEnterpriseWiFiConfiguration"
        # Authentication Method when EAP Type is configured to PEAP or EAP-TTLS. Possible values are: certificate, usernameAndPassword, derivedCredential.
        self._authentication_method: Optional[wi_fi_authentication_method.WiFiAuthenticationMethod] = None
        # Tenant level settings for the Derived Credentials to be used for authentication.
        self._derived_credential_settings: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None
        # EAP-FAST Configuration Option when EAP-FAST is the selected EAP Type. Possible values are: noProtectedAccessCredential, useProtectedAccessCredential, useProtectedAccessCredentialAndProvision, useProtectedAccessCredentialAndProvisionAnonymously.
        self._eap_fast_configuration: Optional[eap_fast_configuration.EapFastConfiguration] = None
        # Extensible Authentication Protocol (EAP) configuration types.
        self._eap_type: Optional[eap_type.EapType] = None
        # Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication).
        self._identity_certificate_for_client_authentication: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None
        # Non-EAP Method for Authentication when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
        self._inner_authentication_protocol_for_eap_ttls: Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType] = None
        # Enable identity privacy (Outer Identity) when EAP Type is configured to EAP - TTLS, EAP - FAST or PEAP. This property masks usernames with the text you enter. For example, if you use 'anonymous', each user that authenticates with this Wi-Fi connection using their real username is displayed as 'anonymous'.
        self._outer_identity_privacy_temporary_value: Optional[str] = None
        # Password format string used to build the password to connect to wifi
        self._password_format_string: Optional[str] = None
        # Trusted Root Certificates for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. If you provide this value you do not need to provide trustedServerCertificateNames, and vice versa. This collection can contain a maximum of 500 elements.
        self._root_certificates_for_server_validation: Optional[List[ios_trusted_root_certificate.IosTrustedRootCertificate]] = None
        # Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users' devices when they connect to this Wi-Fi network.
        self._trusted_server_certificate_names: Optional[List[str]] = None
        # Username format string used to build the username to connect to wifi
        self._username_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosEnterpriseWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosEnterpriseWiFiConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosEnterpriseWiFiConfiguration()
    
    @property
    def derived_credential_settings(self,) -> Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]:
        """
        Gets the derivedCredentialSettings property value. Tenant level settings for the Derived Credentials to be used for authentication.
        Returns: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]
        """
        return self._derived_credential_settings
    
    @derived_credential_settings.setter
    def derived_credential_settings(self,value: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None) -> None:
        """
        Sets the derivedCredentialSettings property value. Tenant level settings for the Derived Credentials to be used for authentication.
        Args:
            value: Value to set for the derivedCredentialSettings property.
        """
        self._derived_credential_settings = value
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_method": lambda n : setattr(self, 'authentication_method', n.get_enum_value(wi_fi_authentication_method.WiFiAuthenticationMethod)),
            "derived_credential_settings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings)),
            "eap_fast_configuration": lambda n : setattr(self, 'eap_fast_configuration', n.get_enum_value(eap_fast_configuration.EapFastConfiguration)),
            "eap_type": lambda n : setattr(self, 'eap_type', n.get_enum_value(eap_type.EapType)),
            "identity_certificate_for_client_authentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(ios_certificate_profile_base.IosCertificateProfileBase)),
            "inner_authentication_protocol_for_eap_ttls": lambda n : setattr(self, 'inner_authentication_protocol_for_eap_ttls', n.get_enum_value(non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType)),
            "outer_identity_privacy_temporary_value": lambda n : setattr(self, 'outer_identity_privacy_temporary_value', n.get_str_value()),
            "password_format_string": lambda n : setattr(self, 'password_format_string', n.get_str_value()),
            "root_certificates_for_server_validation": lambda n : setattr(self, 'root_certificates_for_server_validation', n.get_collection_of_object_values(ios_trusted_root_certificate.IosTrustedRootCertificate)),
            "trusted_server_certificate_names": lambda n : setattr(self, 'trusted_server_certificate_names', n.get_collection_of_primitive_values(str)),
            "username_format_string": lambda n : setattr(self, 'username_format_string', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_certificate_for_client_authentication(self,) -> Optional[ios_certificate_profile_base.IosCertificateProfileBase]:
        """
        Gets the identityCertificateForClientAuthentication property value. Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication).
        Returns: Optional[ios_certificate_profile_base.IosCertificateProfileBase]
        """
        return self._identity_certificate_for_client_authentication
    
    @identity_certificate_for_client_authentication.setter
    def identity_certificate_for_client_authentication(self,value: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificateForClientAuthentication property value. Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication).
        Args:
            value: Value to set for the identityCertificateForClientAuthentication property.
        """
        self._identity_certificate_for_client_authentication = value
    
    @property
    def inner_authentication_protocol_for_eap_ttls(self,) -> Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType]:
        """
        Gets the innerAuthenticationProtocolForEapTtls property value. Non-EAP Method for Authentication when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
        Returns: Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType]
        """
        return self._inner_authentication_protocol_for_eap_ttls
    
    @inner_authentication_protocol_for_eap_ttls.setter
    def inner_authentication_protocol_for_eap_ttls(self,value: Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType] = None) -> None:
        """
        Sets the innerAuthenticationProtocolForEapTtls property value. Non-EAP Method for Authentication when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
        Args:
            value: Value to set for the innerAuthenticationProtocolForEapTtls property.
        """
        self._inner_authentication_protocol_for_eap_ttls = value
    
    @property
    def outer_identity_privacy_temporary_value(self,) -> Optional[str]:
        """
        Gets the outerIdentityPrivacyTemporaryValue property value. Enable identity privacy (Outer Identity) when EAP Type is configured to EAP - TTLS, EAP - FAST or PEAP. This property masks usernames with the text you enter. For example, if you use 'anonymous', each user that authenticates with this Wi-Fi connection using their real username is displayed as 'anonymous'.
        Returns: Optional[str]
        """
        return self._outer_identity_privacy_temporary_value
    
    @outer_identity_privacy_temporary_value.setter
    def outer_identity_privacy_temporary_value(self,value: Optional[str] = None) -> None:
        """
        Sets the outerIdentityPrivacyTemporaryValue property value. Enable identity privacy (Outer Identity) when EAP Type is configured to EAP - TTLS, EAP - FAST or PEAP. This property masks usernames with the text you enter. For example, if you use 'anonymous', each user that authenticates with this Wi-Fi connection using their real username is displayed as 'anonymous'.
        Args:
            value: Value to set for the outerIdentityPrivacyTemporaryValue property.
        """
        self._outer_identity_privacy_temporary_value = value
    
    @property
    def password_format_string(self,) -> Optional[str]:
        """
        Gets the passwordFormatString property value. Password format string used to build the password to connect to wifi
        Returns: Optional[str]
        """
        return self._password_format_string
    
    @password_format_string.setter
    def password_format_string(self,value: Optional[str] = None) -> None:
        """
        Sets the passwordFormatString property value. Password format string used to build the password to connect to wifi
        Args:
            value: Value to set for the passwordFormatString property.
        """
        self._password_format_string = value
    
    @property
    def root_certificates_for_server_validation(self,) -> Optional[List[ios_trusted_root_certificate.IosTrustedRootCertificate]]:
        """
        Gets the rootCertificatesForServerValidation property value. Trusted Root Certificates for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. If you provide this value you do not need to provide trustedServerCertificateNames, and vice versa. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ios_trusted_root_certificate.IosTrustedRootCertificate]]
        """
        return self._root_certificates_for_server_validation
    
    @root_certificates_for_server_validation.setter
    def root_certificates_for_server_validation(self,value: Optional[List[ios_trusted_root_certificate.IosTrustedRootCertificate]] = None) -> None:
        """
        Sets the rootCertificatesForServerValidation property value. Trusted Root Certificates for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. If you provide this value you do not need to provide trustedServerCertificateNames, and vice versa. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the rootCertificatesForServerValidation property.
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
        writer.write_object_value("derivedCredentialSettings", self.derived_credential_settings)
        writer.write_enum_value("eapFastConfiguration", self.eap_fast_configuration)
        writer.write_enum_value("eapType", self.eap_type)
        writer.write_object_value("identityCertificateForClientAuthentication", self.identity_certificate_for_client_authentication)
        writer.write_enum_value("innerAuthenticationProtocolForEapTtls", self.inner_authentication_protocol_for_eap_ttls)
        writer.write_str_value("outerIdentityPrivacyTemporaryValue", self.outer_identity_privacy_temporary_value)
        writer.write_str_value("passwordFormatString", self.password_format_string)
        writer.write_collection_of_object_values("rootCertificatesForServerValidation", self.root_certificates_for_server_validation)
        writer.write_collection_of_primitive_values("trustedServerCertificateNames", self.trusted_server_certificate_names)
        writer.write_str_value("usernameFormatString", self.username_format_string)
    
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
            value: Value to set for the trustedServerCertificateNames property.
        """
        self._trusted_server_certificate_names = value
    
    @property
    def username_format_string(self,) -> Optional[str]:
        """
        Gets the usernameFormatString property value. Username format string used to build the username to connect to wifi
        Returns: Optional[str]
        """
        return self._username_format_string
    
    @username_format_string.setter
    def username_format_string(self,value: Optional[str] = None) -> None:
        """
        Sets the usernameFormatString property value. Username format string used to build the username to connect to wifi
        Args:
            value: Value to set for the usernameFormatString property.
        """
        self._username_format_string = value
    

