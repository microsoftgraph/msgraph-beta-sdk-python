from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

external_authentication_type = lazy_import('msgraph.generated.models.external_authentication_type')
key_credential = lazy_import('msgraph.generated.models.key_credential')
on_premises_application_segment = lazy_import('msgraph.generated.models.on_premises_application_segment')
on_premises_publishing_single_sign_on = lazy_import('msgraph.generated.models.on_premises_publishing_single_sign_on')
password_credential = lazy_import('msgraph.generated.models.password_credential')
segment_configuration = lazy_import('msgraph.generated.models.segment_configuration')
verified_custom_domain_certificates_metadata = lazy_import('msgraph.generated.models.verified_custom_domain_certificates_metadata')

class OnPremisesPublishing(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def alternate_url(self,) -> Optional[str]:
        """
        Gets the alternateUrl property value. If you are configuring a traffic manager in front of multiple App Proxy applications, the alternateUrl is the user-friendly URL that will point to the traffic manager.
        Returns: Optional[str]
        """
        return self._alternate_url
    
    @alternate_url.setter
    def alternate_url(self,value: Optional[str] = None) -> None:
        """
        Sets the alternateUrl property value. If you are configuring a traffic manager in front of multiple App Proxy applications, the alternateUrl is the user-friendly URL that will point to the traffic manager.
        Args:
            value: Value to set for the alternateUrl property.
        """
        self._alternate_url = value
    
    @property
    def application_server_timeout(self,) -> Optional[str]:
        """
        Gets the applicationServerTimeout property value. The duration the connector will wait for a response from the backend application before closing the connection. Possible values are default, long. When set to default, the backend application timeout has a length of 85 seconds. When set to long, the backend timeout is increased to 180 seconds. Use long if your server takes more than 85 seconds to respond to requests or if you are unable to access the application and the error status is 'Backend Timeout'. Default value is default.
        Returns: Optional[str]
        """
        return self._application_server_timeout
    
    @application_server_timeout.setter
    def application_server_timeout(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationServerTimeout property value. The duration the connector will wait for a response from the backend application before closing the connection. Possible values are default, long. When set to default, the backend application timeout has a length of 85 seconds. When set to long, the backend timeout is increased to 180 seconds. Use long if your server takes more than 85 seconds to respond to requests or if you are unable to access the application and the error status is 'Backend Timeout'. Default value is default.
        Args:
            value: Value to set for the applicationServerTimeout property.
        """
        self._application_server_timeout = value
    
    @property
    def application_type(self,) -> Optional[str]:
        """
        Gets the applicationType property value. Indicates if this application is an Application Proxy configured application. This is pre-set by the system. Read-only.
        Returns: Optional[str]
        """
        return self._application_type
    
    @application_type.setter
    def application_type(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationType property value. Indicates if this application is an Application Proxy configured application. This is pre-set by the system. Read-only.
        Args:
            value: Value to set for the applicationType property.
        """
        self._application_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new onPremisesPublishing and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If you are configuring a traffic manager in front of multiple App Proxy applications, the alternateUrl is the user-friendly URL that will point to the traffic manager.
        self._alternate_url: Optional[str] = None
        # The duration the connector will wait for a response from the backend application before closing the connection. Possible values are default, long. When set to default, the backend application timeout has a length of 85 seconds. When set to long, the backend timeout is increased to 180 seconds. Use long if your server takes more than 85 seconds to respond to requests or if you are unable to access the application and the error status is 'Backend Timeout'. Default value is default.
        self._application_server_timeout: Optional[str] = None
        # Indicates if this application is an Application Proxy configured application. This is pre-set by the system. Read-only.
        self._application_type: Optional[str] = None
        # Details the pre-authentication setting for the application. Pre-authentication enforces that users must authenticate before accessing the app. Passthru does not require authentication. Possible values are: passthru, aadPreAuthentication.
        self._external_authentication_type: Optional[external_authentication_type.ExternalAuthenticationType] = None
        # The published external url for the application. For example, https://intranet-contoso.msappproxy.net/.
        self._external_url: Optional[str] = None
        # The internal url of the application. For example, https://intranet/.
        self._internal_url: Optional[str] = None
        # Indicates whether backend SSL certificate validation is enabled for the application. For all new Application Proxy apps, the property will be set to true by default. For all existing apps, the property will be set to false.
        self._is_backend_certificate_validation_enabled: Optional[bool] = None
        # Indicates if the HTTPOnly cookie flag should be set in the HTTP response headers. Set this value to true to have Application Proxy cookies include the HTTPOnly flag in the HTTP response headers. If using Remote Desktop Services, set this value to False. Default value is false.
        self._is_http_only_cookie_enabled: Optional[bool] = None
        # Indicates if the application is currently being published via Application Proxy or not. This is pre-set by the system. Read-only.
        self._is_on_prem_publishing_enabled: Optional[bool] = None
        # Indicates if the Persistent cookie flag should be set in the HTTP response headers. Keep this value set to false. Only use this setting for applications that can't share cookies between processes. For more information about cookie settings, see Cookie settings for accessing on-premises applications in Azure Active Directory. Default value is false.
        self._is_persistent_cookie_enabled: Optional[bool] = None
        # Indicates if the Secure cookie flag should be set in the HTTP response headers. Set this value to true to transmit cookies over a secure channel such as an encrypted HTTPS request. Default value is true.
        self._is_secure_cookie_enabled: Optional[bool] = None
        # Indicates whether validation of the state parameter when the client uses the OAuth 2.0 authorization code grant flow is enabled. This setting allows admins to specify whether they want to enable CSRF protection for their apps.
        self._is_state_session_enabled: Optional[bool] = None
        # Indicates if the application should translate urls in the reponse headers. Keep this value as true unless your application required the original host header in the authentication request. Default value is true.
        self._is_translate_host_header_enabled: Optional[bool] = None
        # Indicates if the application should translate urls in the application body. Keep this value as false unless you have hardcoded HTML links to other on-premises applications and don't use custom domains. For more information, see Link translation with Application Proxy. Default value is false.
        self._is_translate_links_in_body_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Represents the application segment collection for an on-premises wildcard application.
        self._on_premises_application_segments: Optional[List[on_premises_application_segment.OnPremisesApplicationSegment]] = None
        # The segmentsConfiguration property
        self._segments_configuration: Optional[segment_configuration.SegmentConfiguration] = None
        # Represents the single sign-on configuration for the on-premises application.
        self._single_sign_on_settings: Optional[on_premises_publishing_single_sign_on.OnPremisesPublishingSingleSignOn] = None
        # The useAlternateUrlForTranslationAndRedirect property
        self._use_alternate_url_for_translation_and_redirect: Optional[bool] = None
        # Details of the certificate associated with the application when a custom domain is in use. null when using the default domain. Read-only.
        self._verified_custom_domain_certificates_metadata: Optional[verified_custom_domain_certificates_metadata.VerifiedCustomDomainCertificatesMetadata] = None
        # The associated key credential for the custom domain used.
        self._verified_custom_domain_key_credential: Optional[key_credential.KeyCredential] = None
        # The associated password credential for the custom domain used.
        self._verified_custom_domain_password_credential: Optional[password_credential.PasswordCredential] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesPublishing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesPublishing
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesPublishing()
    
    @property
    def external_authentication_type(self,) -> Optional[external_authentication_type.ExternalAuthenticationType]:
        """
        Gets the externalAuthenticationType property value. Details the pre-authentication setting for the application. Pre-authentication enforces that users must authenticate before accessing the app. Passthru does not require authentication. Possible values are: passthru, aadPreAuthentication.
        Returns: Optional[external_authentication_type.ExternalAuthenticationType]
        """
        return self._external_authentication_type
    
    @external_authentication_type.setter
    def external_authentication_type(self,value: Optional[external_authentication_type.ExternalAuthenticationType] = None) -> None:
        """
        Sets the externalAuthenticationType property value. Details the pre-authentication setting for the application. Pre-authentication enforces that users must authenticate before accessing the app. Passthru does not require authentication. Possible values are: passthru, aadPreAuthentication.
        Args:
            value: Value to set for the externalAuthenticationType property.
        """
        self._external_authentication_type = value
    
    @property
    def external_url(self,) -> Optional[str]:
        """
        Gets the externalUrl property value. The published external url for the application. For example, https://intranet-contoso.msappproxy.net/.
        Returns: Optional[str]
        """
        return self._external_url
    
    @external_url.setter
    def external_url(self,value: Optional[str] = None) -> None:
        """
        Sets the externalUrl property value. The published external url for the application. For example, https://intranet-contoso.msappproxy.net/.
        Args:
            value: Value to set for the externalUrl property.
        """
        self._external_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alternate_url": lambda n : setattr(self, 'alternate_url', n.get_str_value()),
            "application_server_timeout": lambda n : setattr(self, 'application_server_timeout', n.get_str_value()),
            "application_type": lambda n : setattr(self, 'application_type', n.get_str_value()),
            "external_authentication_type": lambda n : setattr(self, 'external_authentication_type', n.get_enum_value(external_authentication_type.ExternalAuthenticationType)),
            "external_url": lambda n : setattr(self, 'external_url', n.get_str_value()),
            "internal_url": lambda n : setattr(self, 'internal_url', n.get_str_value()),
            "is_backend_certificate_validation_enabled": lambda n : setattr(self, 'is_backend_certificate_validation_enabled', n.get_bool_value()),
            "is_http_only_cookie_enabled": lambda n : setattr(self, 'is_http_only_cookie_enabled', n.get_bool_value()),
            "is_on_prem_publishing_enabled": lambda n : setattr(self, 'is_on_prem_publishing_enabled', n.get_bool_value()),
            "is_persistent_cookie_enabled": lambda n : setattr(self, 'is_persistent_cookie_enabled', n.get_bool_value()),
            "is_secure_cookie_enabled": lambda n : setattr(self, 'is_secure_cookie_enabled', n.get_bool_value()),
            "is_state_session_enabled": lambda n : setattr(self, 'is_state_session_enabled', n.get_bool_value()),
            "is_translate_host_header_enabled": lambda n : setattr(self, 'is_translate_host_header_enabled', n.get_bool_value()),
            "is_translate_links_in_body_enabled": lambda n : setattr(self, 'is_translate_links_in_body_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "on_premises_application_segments": lambda n : setattr(self, 'on_premises_application_segments', n.get_collection_of_object_values(on_premises_application_segment.OnPremisesApplicationSegment)),
            "segments_configuration": lambda n : setattr(self, 'segments_configuration', n.get_object_value(segment_configuration.SegmentConfiguration)),
            "single_sign_on_settings": lambda n : setattr(self, 'single_sign_on_settings', n.get_object_value(on_premises_publishing_single_sign_on.OnPremisesPublishingSingleSignOn)),
            "use_alternate_url_for_translation_and_redirect": lambda n : setattr(self, 'use_alternate_url_for_translation_and_redirect', n.get_bool_value()),
            "verified_custom_domain_certificates_metadata": lambda n : setattr(self, 'verified_custom_domain_certificates_metadata', n.get_object_value(verified_custom_domain_certificates_metadata.VerifiedCustomDomainCertificatesMetadata)),
            "verified_custom_domain_key_credential": lambda n : setattr(self, 'verified_custom_domain_key_credential', n.get_object_value(key_credential.KeyCredential)),
            "verified_custom_domain_password_credential": lambda n : setattr(self, 'verified_custom_domain_password_credential', n.get_object_value(password_credential.PasswordCredential)),
        }
        return fields
    
    @property
    def internal_url(self,) -> Optional[str]:
        """
        Gets the internalUrl property value. The internal url of the application. For example, https://intranet/.
        Returns: Optional[str]
        """
        return self._internal_url
    
    @internal_url.setter
    def internal_url(self,value: Optional[str] = None) -> None:
        """
        Sets the internalUrl property value. The internal url of the application. For example, https://intranet/.
        Args:
            value: Value to set for the internalUrl property.
        """
        self._internal_url = value
    
    @property
    def is_backend_certificate_validation_enabled(self,) -> Optional[bool]:
        """
        Gets the isBackendCertificateValidationEnabled property value. Indicates whether backend SSL certificate validation is enabled for the application. For all new Application Proxy apps, the property will be set to true by default. For all existing apps, the property will be set to false.
        Returns: Optional[bool]
        """
        return self._is_backend_certificate_validation_enabled
    
    @is_backend_certificate_validation_enabled.setter
    def is_backend_certificate_validation_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isBackendCertificateValidationEnabled property value. Indicates whether backend SSL certificate validation is enabled for the application. For all new Application Proxy apps, the property will be set to true by default. For all existing apps, the property will be set to false.
        Args:
            value: Value to set for the isBackendCertificateValidationEnabled property.
        """
        self._is_backend_certificate_validation_enabled = value
    
    @property
    def is_http_only_cookie_enabled(self,) -> Optional[bool]:
        """
        Gets the isHttpOnlyCookieEnabled property value. Indicates if the HTTPOnly cookie flag should be set in the HTTP response headers. Set this value to true to have Application Proxy cookies include the HTTPOnly flag in the HTTP response headers. If using Remote Desktop Services, set this value to False. Default value is false.
        Returns: Optional[bool]
        """
        return self._is_http_only_cookie_enabled
    
    @is_http_only_cookie_enabled.setter
    def is_http_only_cookie_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isHttpOnlyCookieEnabled property value. Indicates if the HTTPOnly cookie flag should be set in the HTTP response headers. Set this value to true to have Application Proxy cookies include the HTTPOnly flag in the HTTP response headers. If using Remote Desktop Services, set this value to False. Default value is false.
        Args:
            value: Value to set for the isHttpOnlyCookieEnabled property.
        """
        self._is_http_only_cookie_enabled = value
    
    @property
    def is_on_prem_publishing_enabled(self,) -> Optional[bool]:
        """
        Gets the isOnPremPublishingEnabled property value. Indicates if the application is currently being published via Application Proxy or not. This is pre-set by the system. Read-only.
        Returns: Optional[bool]
        """
        return self._is_on_prem_publishing_enabled
    
    @is_on_prem_publishing_enabled.setter
    def is_on_prem_publishing_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isOnPremPublishingEnabled property value. Indicates if the application is currently being published via Application Proxy or not. This is pre-set by the system. Read-only.
        Args:
            value: Value to set for the isOnPremPublishingEnabled property.
        """
        self._is_on_prem_publishing_enabled = value
    
    @property
    def is_persistent_cookie_enabled(self,) -> Optional[bool]:
        """
        Gets the isPersistentCookieEnabled property value. Indicates if the Persistent cookie flag should be set in the HTTP response headers. Keep this value set to false. Only use this setting for applications that can't share cookies between processes. For more information about cookie settings, see Cookie settings for accessing on-premises applications in Azure Active Directory. Default value is false.
        Returns: Optional[bool]
        """
        return self._is_persistent_cookie_enabled
    
    @is_persistent_cookie_enabled.setter
    def is_persistent_cookie_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPersistentCookieEnabled property value. Indicates if the Persistent cookie flag should be set in the HTTP response headers. Keep this value set to false. Only use this setting for applications that can't share cookies between processes. For more information about cookie settings, see Cookie settings for accessing on-premises applications in Azure Active Directory. Default value is false.
        Args:
            value: Value to set for the isPersistentCookieEnabled property.
        """
        self._is_persistent_cookie_enabled = value
    
    @property
    def is_secure_cookie_enabled(self,) -> Optional[bool]:
        """
        Gets the isSecureCookieEnabled property value. Indicates if the Secure cookie flag should be set in the HTTP response headers. Set this value to true to transmit cookies over a secure channel such as an encrypted HTTPS request. Default value is true.
        Returns: Optional[bool]
        """
        return self._is_secure_cookie_enabled
    
    @is_secure_cookie_enabled.setter
    def is_secure_cookie_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSecureCookieEnabled property value. Indicates if the Secure cookie flag should be set in the HTTP response headers. Set this value to true to transmit cookies over a secure channel such as an encrypted HTTPS request. Default value is true.
        Args:
            value: Value to set for the isSecureCookieEnabled property.
        """
        self._is_secure_cookie_enabled = value
    
    @property
    def is_state_session_enabled(self,) -> Optional[bool]:
        """
        Gets the isStateSessionEnabled property value. Indicates whether validation of the state parameter when the client uses the OAuth 2.0 authorization code grant flow is enabled. This setting allows admins to specify whether they want to enable CSRF protection for their apps.
        Returns: Optional[bool]
        """
        return self._is_state_session_enabled
    
    @is_state_session_enabled.setter
    def is_state_session_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isStateSessionEnabled property value. Indicates whether validation of the state parameter when the client uses the OAuth 2.0 authorization code grant flow is enabled. This setting allows admins to specify whether they want to enable CSRF protection for their apps.
        Args:
            value: Value to set for the isStateSessionEnabled property.
        """
        self._is_state_session_enabled = value
    
    @property
    def is_translate_host_header_enabled(self,) -> Optional[bool]:
        """
        Gets the isTranslateHostHeaderEnabled property value. Indicates if the application should translate urls in the reponse headers. Keep this value as true unless your application required the original host header in the authentication request. Default value is true.
        Returns: Optional[bool]
        """
        return self._is_translate_host_header_enabled
    
    @is_translate_host_header_enabled.setter
    def is_translate_host_header_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isTranslateHostHeaderEnabled property value. Indicates if the application should translate urls in the reponse headers. Keep this value as true unless your application required the original host header in the authentication request. Default value is true.
        Args:
            value: Value to set for the isTranslateHostHeaderEnabled property.
        """
        self._is_translate_host_header_enabled = value
    
    @property
    def is_translate_links_in_body_enabled(self,) -> Optional[bool]:
        """
        Gets the isTranslateLinksInBodyEnabled property value. Indicates if the application should translate urls in the application body. Keep this value as false unless you have hardcoded HTML links to other on-premises applications and don't use custom domains. For more information, see Link translation with Application Proxy. Default value is false.
        Returns: Optional[bool]
        """
        return self._is_translate_links_in_body_enabled
    
    @is_translate_links_in_body_enabled.setter
    def is_translate_links_in_body_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isTranslateLinksInBodyEnabled property value. Indicates if the application should translate urls in the application body. Keep this value as false unless you have hardcoded HTML links to other on-premises applications and don't use custom domains. For more information, see Link translation with Application Proxy. Default value is false.
        Args:
            value: Value to set for the isTranslateLinksInBodyEnabled property.
        """
        self._is_translate_links_in_body_enabled = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def on_premises_application_segments(self,) -> Optional[List[on_premises_application_segment.OnPremisesApplicationSegment]]:
        """
        Gets the onPremisesApplicationSegments property value. Represents the application segment collection for an on-premises wildcard application.
        Returns: Optional[List[on_premises_application_segment.OnPremisesApplicationSegment]]
        """
        return self._on_premises_application_segments
    
    @on_premises_application_segments.setter
    def on_premises_application_segments(self,value: Optional[List[on_premises_application_segment.OnPremisesApplicationSegment]] = None) -> None:
        """
        Sets the onPremisesApplicationSegments property value. Represents the application segment collection for an on-premises wildcard application.
        Args:
            value: Value to set for the onPremisesApplicationSegments property.
        """
        self._on_premises_application_segments = value
    
    @property
    def segments_configuration(self,) -> Optional[segment_configuration.SegmentConfiguration]:
        """
        Gets the segmentsConfiguration property value. The segmentsConfiguration property
        Returns: Optional[segment_configuration.SegmentConfiguration]
        """
        return self._segments_configuration
    
    @segments_configuration.setter
    def segments_configuration(self,value: Optional[segment_configuration.SegmentConfiguration] = None) -> None:
        """
        Sets the segmentsConfiguration property value. The segmentsConfiguration property
        Args:
            value: Value to set for the segmentsConfiguration property.
        """
        self._segments_configuration = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("alternateUrl", self.alternate_url)
        writer.write_str_value("applicationServerTimeout", self.application_server_timeout)
        writer.write_str_value("applicationType", self.application_type)
        writer.write_enum_value("externalAuthenticationType", self.external_authentication_type)
        writer.write_str_value("externalUrl", self.external_url)
        writer.write_str_value("internalUrl", self.internal_url)
        writer.write_bool_value("isBackendCertificateValidationEnabled", self.is_backend_certificate_validation_enabled)
        writer.write_bool_value("isHttpOnlyCookieEnabled", self.is_http_only_cookie_enabled)
        writer.write_bool_value("isOnPremPublishingEnabled", self.is_on_prem_publishing_enabled)
        writer.write_bool_value("isPersistentCookieEnabled", self.is_persistent_cookie_enabled)
        writer.write_bool_value("isSecureCookieEnabled", self.is_secure_cookie_enabled)
        writer.write_bool_value("isStateSessionEnabled", self.is_state_session_enabled)
        writer.write_bool_value("isTranslateHostHeaderEnabled", self.is_translate_host_header_enabled)
        writer.write_bool_value("isTranslateLinksInBodyEnabled", self.is_translate_links_in_body_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("onPremisesApplicationSegments", self.on_premises_application_segments)
        writer.write_object_value("segmentsConfiguration", self.segments_configuration)
        writer.write_object_value("singleSignOnSettings", self.single_sign_on_settings)
        writer.write_bool_value("useAlternateUrlForTranslationAndRedirect", self.use_alternate_url_for_translation_and_redirect)
        writer.write_object_value("verifiedCustomDomainCertificatesMetadata", self.verified_custom_domain_certificates_metadata)
        writer.write_object_value("verifiedCustomDomainKeyCredential", self.verified_custom_domain_key_credential)
        writer.write_object_value("verifiedCustomDomainPasswordCredential", self.verified_custom_domain_password_credential)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def single_sign_on_settings(self,) -> Optional[on_premises_publishing_single_sign_on.OnPremisesPublishingSingleSignOn]:
        """
        Gets the singleSignOnSettings property value. Represents the single sign-on configuration for the on-premises application.
        Returns: Optional[on_premises_publishing_single_sign_on.OnPremisesPublishingSingleSignOn]
        """
        return self._single_sign_on_settings
    
    @single_sign_on_settings.setter
    def single_sign_on_settings(self,value: Optional[on_premises_publishing_single_sign_on.OnPremisesPublishingSingleSignOn] = None) -> None:
        """
        Sets the singleSignOnSettings property value. Represents the single sign-on configuration for the on-premises application.
        Args:
            value: Value to set for the singleSignOnSettings property.
        """
        self._single_sign_on_settings = value
    
    @property
    def use_alternate_url_for_translation_and_redirect(self,) -> Optional[bool]:
        """
        Gets the useAlternateUrlForTranslationAndRedirect property value. The useAlternateUrlForTranslationAndRedirect property
        Returns: Optional[bool]
        """
        return self._use_alternate_url_for_translation_and_redirect
    
    @use_alternate_url_for_translation_and_redirect.setter
    def use_alternate_url_for_translation_and_redirect(self,value: Optional[bool] = None) -> None:
        """
        Sets the useAlternateUrlForTranslationAndRedirect property value. The useAlternateUrlForTranslationAndRedirect property
        Args:
            value: Value to set for the useAlternateUrlForTranslationAndRedirect property.
        """
        self._use_alternate_url_for_translation_and_redirect = value
    
    @property
    def verified_custom_domain_certificates_metadata(self,) -> Optional[verified_custom_domain_certificates_metadata.VerifiedCustomDomainCertificatesMetadata]:
        """
        Gets the verifiedCustomDomainCertificatesMetadata property value. Details of the certificate associated with the application when a custom domain is in use. null when using the default domain. Read-only.
        Returns: Optional[verified_custom_domain_certificates_metadata.VerifiedCustomDomainCertificatesMetadata]
        """
        return self._verified_custom_domain_certificates_metadata
    
    @verified_custom_domain_certificates_metadata.setter
    def verified_custom_domain_certificates_metadata(self,value: Optional[verified_custom_domain_certificates_metadata.VerifiedCustomDomainCertificatesMetadata] = None) -> None:
        """
        Sets the verifiedCustomDomainCertificatesMetadata property value. Details of the certificate associated with the application when a custom domain is in use. null when using the default domain. Read-only.
        Args:
            value: Value to set for the verifiedCustomDomainCertificatesMetadata property.
        """
        self._verified_custom_domain_certificates_metadata = value
    
    @property
    def verified_custom_domain_key_credential(self,) -> Optional[key_credential.KeyCredential]:
        """
        Gets the verifiedCustomDomainKeyCredential property value. The associated key credential for the custom domain used.
        Returns: Optional[key_credential.KeyCredential]
        """
        return self._verified_custom_domain_key_credential
    
    @verified_custom_domain_key_credential.setter
    def verified_custom_domain_key_credential(self,value: Optional[key_credential.KeyCredential] = None) -> None:
        """
        Sets the verifiedCustomDomainKeyCredential property value. The associated key credential for the custom domain used.
        Args:
            value: Value to set for the verifiedCustomDomainKeyCredential property.
        """
        self._verified_custom_domain_key_credential = value
    
    @property
    def verified_custom_domain_password_credential(self,) -> Optional[password_credential.PasswordCredential]:
        """
        Gets the verifiedCustomDomainPasswordCredential property value. The associated password credential for the custom domain used.
        Returns: Optional[password_credential.PasswordCredential]
        """
        return self._verified_custom_domain_password_credential
    
    @verified_custom_domain_password_credential.setter
    def verified_custom_domain_password_credential(self,value: Optional[password_credential.PasswordCredential] = None) -> None:
        """
        Sets the verifiedCustomDomainPasswordCredential property value. The associated password credential for the custom domain used.
        Args:
            value: Value to set for the verifiedCustomDomainPasswordCredential property.
        """
        self._verified_custom_domain_password_credential = value
    

