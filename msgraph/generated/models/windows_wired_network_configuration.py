from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
eap_type = lazy_import('msgraph.generated.models.eap_type')
non_eap_authentication_method_for_eap_ttls_type = lazy_import('msgraph.generated.models.non_eap_authentication_method_for_eap_ttls_type')
windows_certificate_profile_base = lazy_import('msgraph.generated.models.windows_certificate_profile_base')
windows81_trusted_root_certificate = lazy_import('msgraph.generated.models.windows81_trusted_root_certificate')
wired_network_authentication_method = lazy_import('msgraph.generated.models.wired_network_authentication_method')
wired_network_authentication_type = lazy_import('msgraph.generated.models.wired_network_authentication_type')

class WindowsWiredNetworkConfiguration(device_configuration.DeviceConfiguration):
    @property
    def authentication_block_period_in_minutes(self,) -> Optional[int]:
        """
        Gets the authenticationBlockPeriodInMinutes property value. Specify the duration for which automatic authentication attempts will be blocked from occuring after a failed authentication attempt.
        Returns: Optional[int]
        """
        return self._authentication_block_period_in_minutes
    
    @authentication_block_period_in_minutes.setter
    def authentication_block_period_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the authenticationBlockPeriodInMinutes property value. Specify the duration for which automatic authentication attempts will be blocked from occuring after a failed authentication attempt.
        Args:
            value: Value to set for the authenticationBlockPeriodInMinutes property.
        """
        self._authentication_block_period_in_minutes = value
    
    @property
    def authentication_method(self,) -> Optional[wired_network_authentication_method.WiredNetworkAuthenticationMethod]:
        """
        Gets the authenticationMethod property value. Specify the authentication method. Possible values are: certificate, usernameAndPassword, derivedCredential. Possible values are: certificate, usernameAndPassword, derivedCredential, unknownFutureValue.
        Returns: Optional[wired_network_authentication_method.WiredNetworkAuthenticationMethod]
        """
        return self._authentication_method
    
    @authentication_method.setter
    def authentication_method(self,value: Optional[wired_network_authentication_method.WiredNetworkAuthenticationMethod] = None) -> None:
        """
        Sets the authenticationMethod property value. Specify the authentication method. Possible values are: certificate, usernameAndPassword, derivedCredential. Possible values are: certificate, usernameAndPassword, derivedCredential, unknownFutureValue.
        Args:
            value: Value to set for the authenticationMethod property.
        """
        self._authentication_method = value
    
    @property
    def authentication_period_in_seconds(self,) -> Optional[int]:
        """
        Gets the authenticationPeriodInSeconds property value. Specify the number of seconds for the client to wait after an authentication attempt before failing. Valid range 1-3600.
        Returns: Optional[int]
        """
        return self._authentication_period_in_seconds
    
    @authentication_period_in_seconds.setter
    def authentication_period_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the authenticationPeriodInSeconds property value. Specify the number of seconds for the client to wait after an authentication attempt before failing. Valid range 1-3600.
        Args:
            value: Value to set for the authenticationPeriodInSeconds property.
        """
        self._authentication_period_in_seconds = value
    
    @property
    def authentication_retry_delay_period_in_seconds(self,) -> Optional[int]:
        """
        Gets the authenticationRetryDelayPeriodInSeconds property value. Specify the number of seconds between a failed authentication and the next authentication attempt. Valid range 1-3600.
        Returns: Optional[int]
        """
        return self._authentication_retry_delay_period_in_seconds
    
    @authentication_retry_delay_period_in_seconds.setter
    def authentication_retry_delay_period_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the authenticationRetryDelayPeriodInSeconds property value. Specify the number of seconds between a failed authentication and the next authentication attempt. Valid range 1-3600.
        Args:
            value: Value to set for the authenticationRetryDelayPeriodInSeconds property.
        """
        self._authentication_retry_delay_period_in_seconds = value
    
    @property
    def authentication_type(self,) -> Optional[wired_network_authentication_type.WiredNetworkAuthenticationType]:
        """
        Gets the authenticationType property value. Specify whether to authenticate the user, the device, either, or to use guest authentication (none). If you're using certificate authentication, make sure the certificate type matches the authentication type. Possible values are: none, user, machine, machineOrUser, guest. Possible values are: none, user, machine, machineOrUser, guest, unknownFutureValue.
        Returns: Optional[wired_network_authentication_type.WiredNetworkAuthenticationType]
        """
        return self._authentication_type
    
    @authentication_type.setter
    def authentication_type(self,value: Optional[wired_network_authentication_type.WiredNetworkAuthenticationType] = None) -> None:
        """
        Sets the authenticationType property value. Specify whether to authenticate the user, the device, either, or to use guest authentication (none). If you're using certificate authentication, make sure the certificate type matches the authentication type. Possible values are: none, user, machine, machineOrUser, guest. Possible values are: none, user, machine, machineOrUser, guest, unknownFutureValue.
        Args:
            value: Value to set for the authenticationType property.
        """
        self._authentication_type = value
    
    @property
    def cache_credentials(self,) -> Optional[bool]:
        """
        Gets the cacheCredentials property value. When TRUE, caches user credentials on the device so that users don't need to keep entering them each time they connect. When FALSE, do not cache credentials. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._cache_credentials
    
    @cache_credentials.setter
    def cache_credentials(self,value: Optional[bool] = None) -> None:
        """
        Sets the cacheCredentials property value. When TRUE, caches user credentials on the device so that users don't need to keep entering them each time they connect. When FALSE, do not cache credentials. Default value is FALSE.
        Args:
            value: Value to set for the cacheCredentials property.
        """
        self._cache_credentials = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsWiredNetworkConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsWiredNetworkConfiguration"
        # Specify the duration for which automatic authentication attempts will be blocked from occuring after a failed authentication attempt.
        self._authentication_block_period_in_minutes: Optional[int] = None
        # Specify the authentication method. Possible values are: certificate, usernameAndPassword, derivedCredential. Possible values are: certificate, usernameAndPassword, derivedCredential, unknownFutureValue.
        self._authentication_method: Optional[wired_network_authentication_method.WiredNetworkAuthenticationMethod] = None
        # Specify the number of seconds for the client to wait after an authentication attempt before failing. Valid range 1-3600.
        self._authentication_period_in_seconds: Optional[int] = None
        # Specify the number of seconds between a failed authentication and the next authentication attempt. Valid range 1-3600.
        self._authentication_retry_delay_period_in_seconds: Optional[int] = None
        # Specify whether to authenticate the user, the device, either, or to use guest authentication (none). If you're using certificate authentication, make sure the certificate type matches the authentication type. Possible values are: none, user, machine, machineOrUser, guest. Possible values are: none, user, machine, machineOrUser, guest, unknownFutureValue.
        self._authentication_type: Optional[wired_network_authentication_type.WiredNetworkAuthenticationType] = None
        # When TRUE, caches user credentials on the device so that users don't need to keep entering them each time they connect. When FALSE, do not cache credentials. Default value is FALSE.
        self._cache_credentials: Optional[bool] = None
        # When TRUE, prevents the user from being prompted to authorize new servers for trusted certification authorities when EAP type is selected as PEAP. When FALSE, does not prevent the user from being prompted. Default value is FALSE.
        self._disable_user_prompt_for_server_validation: Optional[bool] = None
        # Specify the number of seconds to wait before sending an EAPOL (Extensible Authentication Protocol over LAN) Start message. Valid range 1-3600.
        self._eapol_start_period_in_seconds: Optional[int] = None
        # Extensible Authentication Protocol (EAP) configuration types.
        self._eap_type: Optional[eap_type.EapType] = None
        # When TRUE, the automatic configuration service for wired networks requires the use of 802.1X for port authentication. When FALSE, 802.1X is not required. Default value is FALSE.
        self._enforce8021_x: Optional[bool] = None
        # When TRUE, forces FIPS compliance. When FALSE, does not enable FIPS compliance. Default value is FALSE.
        self._force_f_i_p_s_compliance: Optional[bool] = None
        # Specify identity certificate for client authentication.
        self._identity_certificate_for_client_authentication: Optional[windows_certificate_profile_base.WindowsCertificateProfileBase] = None
        # Specify inner authentication protocol for EAP TTLS. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
        self._inner_authentication_protocol_for_e_a_p_t_t_l_s: Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType] = None
        # Specify the maximum authentication failures allowed for a set of credentials. Valid range 1-100.
        self._maximum_authentication_failures: Optional[int] = None
        # Specify the maximum number of EAPOL (Extensible Authentication Protocol over LAN) Start messages to be sent before returning failure. Valid range 1-100.
        self._maximum_e_a_p_o_l_start_messages: Optional[int] = None
        # Specify the string to replace usernames for privacy when using EAP TTLS or PEAP.
        self._outer_identity_privacy_temporary_value: Optional[str] = None
        # When TRUE, enables verification of server's identity by validating the certificate when EAP type is selected as PEAP. When FALSE, the certificate is not validated. Default value is TRUE.
        self._perform_server_validation: Optional[bool] = None
        # When TRUE, enables cryptographic binding when EAP type is selected as PEAP. When FALSE, does not enable cryptogrpahic binding. Default value is TRUE.
        self._require_cryptographic_binding: Optional[bool] = None
        # Specify root certificate for client validation.
        self._root_certificate_for_client_validation: Optional[windows81_trusted_root_certificate.Windows81TrustedRootCertificate] = None
        # Specify root certificates for server validation. This collection can contain a maximum of 500 elements.
        self._root_certificates_for_server_validation: Optional[List[windows81_trusted_root_certificate.Windows81TrustedRootCertificate]] = None
        # Specify the secondary authentication method. Possible values are: certificate, usernameAndPassword, derivedCredential. Possible values are: certificate, usernameAndPassword, derivedCredential, unknownFutureValue.
        self._secondary_authentication_method: Optional[wired_network_authentication_method.WiredNetworkAuthenticationMethod] = None
        # Specify secondary identity certificate for client authentication.
        self._secondary_identity_certificate_for_client_authentication: Optional[windows_certificate_profile_base.WindowsCertificateProfileBase] = None
        # Specify secondary root certificate for client validation.
        self._secondary_root_certificate_for_client_validation: Optional[windows81_trusted_root_certificate.Windows81TrustedRootCertificate] = None
        # Specify trusted server certificate names.
        self._trusted_server_certificate_names: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsWiredNetworkConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsWiredNetworkConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsWiredNetworkConfiguration()
    
    @property
    def disable_user_prompt_for_server_validation(self,) -> Optional[bool]:
        """
        Gets the disableUserPromptForServerValidation property value. When TRUE, prevents the user from being prompted to authorize new servers for trusted certification authorities when EAP type is selected as PEAP. When FALSE, does not prevent the user from being prompted. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._disable_user_prompt_for_server_validation
    
    @disable_user_prompt_for_server_validation.setter
    def disable_user_prompt_for_server_validation(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableUserPromptForServerValidation property value. When TRUE, prevents the user from being prompted to authorize new servers for trusted certification authorities when EAP type is selected as PEAP. When FALSE, does not prevent the user from being prompted. Default value is FALSE.
        Args:
            value: Value to set for the disableUserPromptForServerValidation property.
        """
        self._disable_user_prompt_for_server_validation = value
    
    @property
    def eapol_start_period_in_seconds(self,) -> Optional[int]:
        """
        Gets the eapolStartPeriodInSeconds property value. Specify the number of seconds to wait before sending an EAPOL (Extensible Authentication Protocol over LAN) Start message. Valid range 1-3600.
        Returns: Optional[int]
        """
        return self._eapol_start_period_in_seconds
    
    @eapol_start_period_in_seconds.setter
    def eapol_start_period_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the eapolStartPeriodInSeconds property value. Specify the number of seconds to wait before sending an EAPOL (Extensible Authentication Protocol over LAN) Start message. Valid range 1-3600.
        Args:
            value: Value to set for the eapolStartPeriodInSeconds property.
        """
        self._eapol_start_period_in_seconds = value
    
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
    def enforce8021_x(self,) -> Optional[bool]:
        """
        Gets the enforce8021X property value. When TRUE, the automatic configuration service for wired networks requires the use of 802.1X for port authentication. When FALSE, 802.1X is not required. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._enforce8021_x
    
    @enforce8021_x.setter
    def enforce8021_x(self,value: Optional[bool] = None) -> None:
        """
        Sets the enforce8021X property value. When TRUE, the automatic configuration service for wired networks requires the use of 802.1X for port authentication. When FALSE, 802.1X is not required. Default value is FALSE.
        Args:
            value: Value to set for the enforce8021X property.
        """
        self._enforce8021_x = value
    
    @property
    def force_f_i_p_s_compliance(self,) -> Optional[bool]:
        """
        Gets the forceFIPSCompliance property value. When TRUE, forces FIPS compliance. When FALSE, does not enable FIPS compliance. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._force_f_i_p_s_compliance
    
    @force_f_i_p_s_compliance.setter
    def force_f_i_p_s_compliance(self,value: Optional[bool] = None) -> None:
        """
        Sets the forceFIPSCompliance property value. When TRUE, forces FIPS compliance. When FALSE, does not enable FIPS compliance. Default value is FALSE.
        Args:
            value: Value to set for the forceFIPSCompliance property.
        """
        self._force_f_i_p_s_compliance = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_block_period_in_minutes": lambda n : setattr(self, 'authentication_block_period_in_minutes', n.get_int_value()),
            "authentication_method": lambda n : setattr(self, 'authentication_method', n.get_enum_value(wired_network_authentication_method.WiredNetworkAuthenticationMethod)),
            "authentication_period_in_seconds": lambda n : setattr(self, 'authentication_period_in_seconds', n.get_int_value()),
            "authentication_retry_delay_period_in_seconds": lambda n : setattr(self, 'authentication_retry_delay_period_in_seconds', n.get_int_value()),
            "authentication_type": lambda n : setattr(self, 'authentication_type', n.get_enum_value(wired_network_authentication_type.WiredNetworkAuthenticationType)),
            "cache_credentials": lambda n : setattr(self, 'cache_credentials', n.get_bool_value()),
            "disable_user_prompt_for_server_validation": lambda n : setattr(self, 'disable_user_prompt_for_server_validation', n.get_bool_value()),
            "eapol_start_period_in_seconds": lambda n : setattr(self, 'eapol_start_period_in_seconds', n.get_int_value()),
            "eap_type": lambda n : setattr(self, 'eap_type', n.get_enum_value(eap_type.EapType)),
            "enforce8021_x": lambda n : setattr(self, 'enforce8021_x', n.get_bool_value()),
            "force_f_i_p_s_compliance": lambda n : setattr(self, 'force_f_i_p_s_compliance', n.get_bool_value()),
            "identity_certificate_for_client_authentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(windows_certificate_profile_base.WindowsCertificateProfileBase)),
            "inner_authentication_protocol_for_e_a_p_t_t_l_s": lambda n : setattr(self, 'inner_authentication_protocol_for_e_a_p_t_t_l_s', n.get_enum_value(non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType)),
            "maximum_authentication_failures": lambda n : setattr(self, 'maximum_authentication_failures', n.get_int_value()),
            "maximum_e_a_p_o_l_start_messages": lambda n : setattr(self, 'maximum_e_a_p_o_l_start_messages', n.get_int_value()),
            "outer_identity_privacy_temporary_value": lambda n : setattr(self, 'outer_identity_privacy_temporary_value', n.get_str_value()),
            "perform_server_validation": lambda n : setattr(self, 'perform_server_validation', n.get_bool_value()),
            "require_cryptographic_binding": lambda n : setattr(self, 'require_cryptographic_binding', n.get_bool_value()),
            "root_certificate_for_client_validation": lambda n : setattr(self, 'root_certificate_for_client_validation', n.get_object_value(windows81_trusted_root_certificate.Windows81TrustedRootCertificate)),
            "root_certificates_for_server_validation": lambda n : setattr(self, 'root_certificates_for_server_validation', n.get_collection_of_object_values(windows81_trusted_root_certificate.Windows81TrustedRootCertificate)),
            "secondary_authentication_method": lambda n : setattr(self, 'secondary_authentication_method', n.get_enum_value(wired_network_authentication_method.WiredNetworkAuthenticationMethod)),
            "secondary_identity_certificate_for_client_authentication": lambda n : setattr(self, 'secondary_identity_certificate_for_client_authentication', n.get_object_value(windows_certificate_profile_base.WindowsCertificateProfileBase)),
            "secondary_root_certificate_for_client_validation": lambda n : setattr(self, 'secondary_root_certificate_for_client_validation', n.get_object_value(windows81_trusted_root_certificate.Windows81TrustedRootCertificate)),
            "trusted_server_certificate_names": lambda n : setattr(self, 'trusted_server_certificate_names', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_certificate_for_client_authentication(self,) -> Optional[windows_certificate_profile_base.WindowsCertificateProfileBase]:
        """
        Gets the identityCertificateForClientAuthentication property value. Specify identity certificate for client authentication.
        Returns: Optional[windows_certificate_profile_base.WindowsCertificateProfileBase]
        """
        return self._identity_certificate_for_client_authentication
    
    @identity_certificate_for_client_authentication.setter
    def identity_certificate_for_client_authentication(self,value: Optional[windows_certificate_profile_base.WindowsCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificateForClientAuthentication property value. Specify identity certificate for client authentication.
        Args:
            value: Value to set for the identityCertificateForClientAuthentication property.
        """
        self._identity_certificate_for_client_authentication = value
    
    @property
    def inner_authentication_protocol_for_e_a_p_t_t_l_s(self,) -> Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType]:
        """
        Gets the innerAuthenticationProtocolForEAPTTLS property value. Specify inner authentication protocol for EAP TTLS. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
        Returns: Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType]
        """
        return self._inner_authentication_protocol_for_e_a_p_t_t_l_s
    
    @inner_authentication_protocol_for_e_a_p_t_t_l_s.setter
    def inner_authentication_protocol_for_e_a_p_t_t_l_s(self,value: Optional[non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType] = None) -> None:
        """
        Sets the innerAuthenticationProtocolForEAPTTLS property value. Specify inner authentication protocol for EAP TTLS. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
        Args:
            value: Value to set for the innerAuthenticationProtocolForEAPTTLS property.
        """
        self._inner_authentication_protocol_for_e_a_p_t_t_l_s = value
    
    @property
    def maximum_authentication_failures(self,) -> Optional[int]:
        """
        Gets the maximumAuthenticationFailures property value. Specify the maximum authentication failures allowed for a set of credentials. Valid range 1-100.
        Returns: Optional[int]
        """
        return self._maximum_authentication_failures
    
    @maximum_authentication_failures.setter
    def maximum_authentication_failures(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumAuthenticationFailures property value. Specify the maximum authentication failures allowed for a set of credentials. Valid range 1-100.
        Args:
            value: Value to set for the maximumAuthenticationFailures property.
        """
        self._maximum_authentication_failures = value
    
    @property
    def maximum_e_a_p_o_l_start_messages(self,) -> Optional[int]:
        """
        Gets the maximumEAPOLStartMessages property value. Specify the maximum number of EAPOL (Extensible Authentication Protocol over LAN) Start messages to be sent before returning failure. Valid range 1-100.
        Returns: Optional[int]
        """
        return self._maximum_e_a_p_o_l_start_messages
    
    @maximum_e_a_p_o_l_start_messages.setter
    def maximum_e_a_p_o_l_start_messages(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumEAPOLStartMessages property value. Specify the maximum number of EAPOL (Extensible Authentication Protocol over LAN) Start messages to be sent before returning failure. Valid range 1-100.
        Args:
            value: Value to set for the maximumEAPOLStartMessages property.
        """
        self._maximum_e_a_p_o_l_start_messages = value
    
    @property
    def outer_identity_privacy_temporary_value(self,) -> Optional[str]:
        """
        Gets the outerIdentityPrivacyTemporaryValue property value. Specify the string to replace usernames for privacy when using EAP TTLS or PEAP.
        Returns: Optional[str]
        """
        return self._outer_identity_privacy_temporary_value
    
    @outer_identity_privacy_temporary_value.setter
    def outer_identity_privacy_temporary_value(self,value: Optional[str] = None) -> None:
        """
        Sets the outerIdentityPrivacyTemporaryValue property value. Specify the string to replace usernames for privacy when using EAP TTLS or PEAP.
        Args:
            value: Value to set for the outerIdentityPrivacyTemporaryValue property.
        """
        self._outer_identity_privacy_temporary_value = value
    
    @property
    def perform_server_validation(self,) -> Optional[bool]:
        """
        Gets the performServerValidation property value. When TRUE, enables verification of server's identity by validating the certificate when EAP type is selected as PEAP. When FALSE, the certificate is not validated. Default value is TRUE.
        Returns: Optional[bool]
        """
        return self._perform_server_validation
    
    @perform_server_validation.setter
    def perform_server_validation(self,value: Optional[bool] = None) -> None:
        """
        Sets the performServerValidation property value. When TRUE, enables verification of server's identity by validating the certificate when EAP type is selected as PEAP. When FALSE, the certificate is not validated. Default value is TRUE.
        Args:
            value: Value to set for the performServerValidation property.
        """
        self._perform_server_validation = value
    
    @property
    def require_cryptographic_binding(self,) -> Optional[bool]:
        """
        Gets the requireCryptographicBinding property value. When TRUE, enables cryptographic binding when EAP type is selected as PEAP. When FALSE, does not enable cryptogrpahic binding. Default value is TRUE.
        Returns: Optional[bool]
        """
        return self._require_cryptographic_binding
    
    @require_cryptographic_binding.setter
    def require_cryptographic_binding(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireCryptographicBinding property value. When TRUE, enables cryptographic binding when EAP type is selected as PEAP. When FALSE, does not enable cryptogrpahic binding. Default value is TRUE.
        Args:
            value: Value to set for the requireCryptographicBinding property.
        """
        self._require_cryptographic_binding = value
    
    @property
    def root_certificate_for_client_validation(self,) -> Optional[windows81_trusted_root_certificate.Windows81TrustedRootCertificate]:
        """
        Gets the rootCertificateForClientValidation property value. Specify root certificate for client validation.
        Returns: Optional[windows81_trusted_root_certificate.Windows81TrustedRootCertificate]
        """
        return self._root_certificate_for_client_validation
    
    @root_certificate_for_client_validation.setter
    def root_certificate_for_client_validation(self,value: Optional[windows81_trusted_root_certificate.Windows81TrustedRootCertificate] = None) -> None:
        """
        Sets the rootCertificateForClientValidation property value. Specify root certificate for client validation.
        Args:
            value: Value to set for the rootCertificateForClientValidation property.
        """
        self._root_certificate_for_client_validation = value
    
    @property
    def root_certificates_for_server_validation(self,) -> Optional[List[windows81_trusted_root_certificate.Windows81TrustedRootCertificate]]:
        """
        Gets the rootCertificatesForServerValidation property value. Specify root certificates for server validation. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[windows81_trusted_root_certificate.Windows81TrustedRootCertificate]]
        """
        return self._root_certificates_for_server_validation
    
    @root_certificates_for_server_validation.setter
    def root_certificates_for_server_validation(self,value: Optional[List[windows81_trusted_root_certificate.Windows81TrustedRootCertificate]] = None) -> None:
        """
        Sets the rootCertificatesForServerValidation property value. Specify root certificates for server validation. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the rootCertificatesForServerValidation property.
        """
        self._root_certificates_for_server_validation = value
    
    @property
    def secondary_authentication_method(self,) -> Optional[wired_network_authentication_method.WiredNetworkAuthenticationMethod]:
        """
        Gets the secondaryAuthenticationMethod property value. Specify the secondary authentication method. Possible values are: certificate, usernameAndPassword, derivedCredential. Possible values are: certificate, usernameAndPassword, derivedCredential, unknownFutureValue.
        Returns: Optional[wired_network_authentication_method.WiredNetworkAuthenticationMethod]
        """
        return self._secondary_authentication_method
    
    @secondary_authentication_method.setter
    def secondary_authentication_method(self,value: Optional[wired_network_authentication_method.WiredNetworkAuthenticationMethod] = None) -> None:
        """
        Sets the secondaryAuthenticationMethod property value. Specify the secondary authentication method. Possible values are: certificate, usernameAndPassword, derivedCredential. Possible values are: certificate, usernameAndPassword, derivedCredential, unknownFutureValue.
        Args:
            value: Value to set for the secondaryAuthenticationMethod property.
        """
        self._secondary_authentication_method = value
    
    @property
    def secondary_identity_certificate_for_client_authentication(self,) -> Optional[windows_certificate_profile_base.WindowsCertificateProfileBase]:
        """
        Gets the secondaryIdentityCertificateForClientAuthentication property value. Specify secondary identity certificate for client authentication.
        Returns: Optional[windows_certificate_profile_base.WindowsCertificateProfileBase]
        """
        return self._secondary_identity_certificate_for_client_authentication
    
    @secondary_identity_certificate_for_client_authentication.setter
    def secondary_identity_certificate_for_client_authentication(self,value: Optional[windows_certificate_profile_base.WindowsCertificateProfileBase] = None) -> None:
        """
        Sets the secondaryIdentityCertificateForClientAuthentication property value. Specify secondary identity certificate for client authentication.
        Args:
            value: Value to set for the secondaryIdentityCertificateForClientAuthentication property.
        """
        self._secondary_identity_certificate_for_client_authentication = value
    
    @property
    def secondary_root_certificate_for_client_validation(self,) -> Optional[windows81_trusted_root_certificate.Windows81TrustedRootCertificate]:
        """
        Gets the secondaryRootCertificateForClientValidation property value. Specify secondary root certificate for client validation.
        Returns: Optional[windows81_trusted_root_certificate.Windows81TrustedRootCertificate]
        """
        return self._secondary_root_certificate_for_client_validation
    
    @secondary_root_certificate_for_client_validation.setter
    def secondary_root_certificate_for_client_validation(self,value: Optional[windows81_trusted_root_certificate.Windows81TrustedRootCertificate] = None) -> None:
        """
        Sets the secondaryRootCertificateForClientValidation property value. Specify secondary root certificate for client validation.
        Args:
            value: Value to set for the secondaryRootCertificateForClientValidation property.
        """
        self._secondary_root_certificate_for_client_validation = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("authenticationBlockPeriodInMinutes", self.authentication_block_period_in_minutes)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_int_value("authenticationPeriodInSeconds", self.authentication_period_in_seconds)
        writer.write_int_value("authenticationRetryDelayPeriodInSeconds", self.authentication_retry_delay_period_in_seconds)
        writer.write_enum_value("authenticationType", self.authentication_type)
        writer.write_bool_value("cacheCredentials", self.cache_credentials)
        writer.write_bool_value("disableUserPromptForServerValidation", self.disable_user_prompt_for_server_validation)
        writer.write_int_value("eapolStartPeriodInSeconds", self.eapol_start_period_in_seconds)
        writer.write_enum_value("eapType", self.eap_type)
        writer.write_bool_value("enforce8021X", self.enforce8021_x)
        writer.write_bool_value("forceFIPSCompliance", self.force_f_i_p_s_compliance)
        writer.write_object_value("identityCertificateForClientAuthentication", self.identity_certificate_for_client_authentication)
        writer.write_enum_value("innerAuthenticationProtocolForEAPTTLS", self.inner_authentication_protocol_for_e_a_p_t_t_l_s)
        writer.write_int_value("maximumAuthenticationFailures", self.maximum_authentication_failures)
        writer.write_int_value("maximumEAPOLStartMessages", self.maximum_e_a_p_o_l_start_messages)
        writer.write_str_value("outerIdentityPrivacyTemporaryValue", self.outer_identity_privacy_temporary_value)
        writer.write_bool_value("performServerValidation", self.perform_server_validation)
        writer.write_bool_value("requireCryptographicBinding", self.require_cryptographic_binding)
        writer.write_object_value("rootCertificateForClientValidation", self.root_certificate_for_client_validation)
        writer.write_collection_of_object_values("rootCertificatesForServerValidation", self.root_certificates_for_server_validation)
        writer.write_enum_value("secondaryAuthenticationMethod", self.secondary_authentication_method)
        writer.write_object_value("secondaryIdentityCertificateForClientAuthentication", self.secondary_identity_certificate_for_client_authentication)
        writer.write_object_value("secondaryRootCertificateForClientValidation", self.secondary_root_certificate_for_client_validation)
        writer.write_collection_of_primitive_values("trustedServerCertificateNames", self.trusted_server_certificate_names)
    
    @property
    def trusted_server_certificate_names(self,) -> Optional[List[str]]:
        """
        Gets the trustedServerCertificateNames property value. Specify trusted server certificate names.
        Returns: Optional[List[str]]
        """
        return self._trusted_server_certificate_names
    
    @trusted_server_certificate_names.setter
    def trusted_server_certificate_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the trustedServerCertificateNames property value. Specify trusted server certificate names.
        Args:
            value: Value to set for the trustedServerCertificateNames property.
        """
        self._trusted_server_certificate_names = value
    

