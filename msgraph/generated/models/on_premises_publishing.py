from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .external_authentication_type import ExternalAuthenticationType
    from .key_credential import KeyCredential
    from .on_premises_application_segment import OnPremisesApplicationSegment
    from .on_premises_publishing_single_sign_on import OnPremisesPublishingSingleSignOn
    from .password_credential import PasswordCredential
    from .segment_configuration import SegmentConfiguration
    from .verified_custom_domain_certificates_metadata import VerifiedCustomDomainCertificatesMetadata

@dataclass
class OnPremisesPublishing(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # If you're configuring a traffic manager in front of multiple App Proxy applications, the alternateUrl is the user-friendly URL that points to the traffic manager.
    alternate_url: Optional[str] = None
    # The duration the connector waits for a response from the backend application before closing the connection. Possible values are default, long. When set to default, the backend application timeout has a length of 85 seconds. When set to long, the backend timeout is increased to 180 seconds. Use long if your server takes more than 85 seconds to respond to requests or if you are unable to access the application and the error status is 'Backend Timeout'. Default value is default.
    application_server_timeout: Optional[str] = None
    # Indicates if this application is an Application Proxy configured application. This is pre-set by the system. Read-only.
    application_type: Optional[str] = None
    # Details the pre-authentication setting for the application. Pre-authentication enforces that users must authenticate before accessing the app. Pass through doesn't require authentication. Possible values are: passthru, aadPreAuthentication.
    external_authentication_type: Optional[ExternalAuthenticationType] = None
    # The published external url for the application. For example, https://intranet-contoso.msappproxy.net/.
    external_url: Optional[str] = None
    # The internal url of the application. For example, https://intranet/.
    internal_url: Optional[str] = None
    # The isAccessibleViaZTNAClient property
    is_accessible_via_z_t_n_a_client: Optional[bool] = None
    # Indicates whether backend SSL certificate validation is enabled for the application. For all new Application Proxy apps, the property is set to true by default. For all existing apps, the property is set to false.
    is_backend_certificate_validation_enabled: Optional[bool] = None
    # Indicates if the HTTPOnly cookie flag should be set in the HTTP response headers. Set this value to true to have Application Proxy cookies include the HTTPOnly flag in the HTTP response headers. If using Remote Desktop Services, set this value to False. Default value is false.
    is_http_only_cookie_enabled: Optional[bool] = None
    # Indicates if the application is currently being published via Application Proxy or not. This is preset by the system. Read-only.
    is_on_prem_publishing_enabled: Optional[bool] = None
    # Indicates if the Persistent cookie flag should be set in the HTTP response headers. Keep this value set to false. Only use this setting for applications that can't share cookies between processes. For more information about cookie settings, see Cookie settings for accessing on-premises applications in Microsoft Entra ID. Default value is false.
    is_persistent_cookie_enabled: Optional[bool] = None
    # Indicates if the Secure cookie flag should be set in the HTTP response headers. Set this value to true to transmit cookies over a secure channel such as an encrypted HTTPS request. Default value is true.
    is_secure_cookie_enabled: Optional[bool] = None
    # Indicates whether validation of the state parameter when the client uses the OAuth 2.0 authorization code grant flow is enabled. This setting allows admins to specify whether they want to enable CSRF protection for their apps.
    is_state_session_enabled: Optional[bool] = None
    # Indicates if the application should translate urls in the response headers. Keep this value as true unless your application required the original host header in the authentication request. Default value is true.
    is_translate_host_header_enabled: Optional[bool] = None
    # Indicates if the application should translate urls in the application body. Keep this value as false unless you have hardcoded HTML links to other on-premises applications and don't use custom domains. For more information, see Link translation with Application Proxy. Default value is false.
    is_translate_links_in_body_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The onPremisesApplicationSegments property
    on_premises_application_segments: Optional[List[OnPremisesApplicationSegment]] = None
    # Represents the collection of application segments for an on-premises wildcard application that's published through Microsoft Entra application proxy.
    segments_configuration: Optional[SegmentConfiguration] = None
    # Represents the single sign-on configuration for the on-premises application.
    single_sign_on_settings: Optional[OnPremisesPublishingSingleSignOn] = None
    # The useAlternateUrlForTranslationAndRedirect property
    use_alternate_url_for_translation_and_redirect: Optional[bool] = None
    # Details of the certificate associated with the application when a custom domain is in use. null when using the default domain. Read-only.
    verified_custom_domain_certificates_metadata: Optional[VerifiedCustomDomainCertificatesMetadata] = None
    # The associated key credential for the custom domain used.
    verified_custom_domain_key_credential: Optional[KeyCredential] = None
    # The associated password credential for the custom domain used.
    verified_custom_domain_password_credential: Optional[PasswordCredential] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesPublishing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesPublishing
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesPublishing()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .external_authentication_type import ExternalAuthenticationType
        from .key_credential import KeyCredential
        from .on_premises_application_segment import OnPremisesApplicationSegment
        from .on_premises_publishing_single_sign_on import OnPremisesPublishingSingleSignOn
        from .password_credential import PasswordCredential
        from .segment_configuration import SegmentConfiguration
        from .verified_custom_domain_certificates_metadata import VerifiedCustomDomainCertificatesMetadata

        from .external_authentication_type import ExternalAuthenticationType
        from .key_credential import KeyCredential
        from .on_premises_application_segment import OnPremisesApplicationSegment
        from .on_premises_publishing_single_sign_on import OnPremisesPublishingSingleSignOn
        from .password_credential import PasswordCredential
        from .segment_configuration import SegmentConfiguration
        from .verified_custom_domain_certificates_metadata import VerifiedCustomDomainCertificatesMetadata

        fields: Dict[str, Callable[[Any], None]] = {
            "alternateUrl": lambda n : setattr(self, 'alternate_url', n.get_str_value()),
            "applicationServerTimeout": lambda n : setattr(self, 'application_server_timeout', n.get_str_value()),
            "applicationType": lambda n : setattr(self, 'application_type', n.get_str_value()),
            "externalAuthenticationType": lambda n : setattr(self, 'external_authentication_type', n.get_enum_value(ExternalAuthenticationType)),
            "externalUrl": lambda n : setattr(self, 'external_url', n.get_str_value()),
            "internalUrl": lambda n : setattr(self, 'internal_url', n.get_str_value()),
            "isAccessibleViaZTNAClient": lambda n : setattr(self, 'is_accessible_via_z_t_n_a_client', n.get_bool_value()),
            "isBackendCertificateValidationEnabled": lambda n : setattr(self, 'is_backend_certificate_validation_enabled', n.get_bool_value()),
            "isHttpOnlyCookieEnabled": lambda n : setattr(self, 'is_http_only_cookie_enabled', n.get_bool_value()),
            "isOnPremPublishingEnabled": lambda n : setattr(self, 'is_on_prem_publishing_enabled', n.get_bool_value()),
            "isPersistentCookieEnabled": lambda n : setattr(self, 'is_persistent_cookie_enabled', n.get_bool_value()),
            "isSecureCookieEnabled": lambda n : setattr(self, 'is_secure_cookie_enabled', n.get_bool_value()),
            "isStateSessionEnabled": lambda n : setattr(self, 'is_state_session_enabled', n.get_bool_value()),
            "isTranslateHostHeaderEnabled": lambda n : setattr(self, 'is_translate_host_header_enabled', n.get_bool_value()),
            "isTranslateLinksInBodyEnabled": lambda n : setattr(self, 'is_translate_links_in_body_enabled', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "onPremisesApplicationSegments": lambda n : setattr(self, 'on_premises_application_segments', n.get_collection_of_object_values(OnPremisesApplicationSegment)),
            "segmentsConfiguration": lambda n : setattr(self, 'segments_configuration', n.get_object_value(SegmentConfiguration)),
            "singleSignOnSettings": lambda n : setattr(self, 'single_sign_on_settings', n.get_object_value(OnPremisesPublishingSingleSignOn)),
            "useAlternateUrlForTranslationAndRedirect": lambda n : setattr(self, 'use_alternate_url_for_translation_and_redirect', n.get_bool_value()),
            "verifiedCustomDomainCertificatesMetadata": lambda n : setattr(self, 'verified_custom_domain_certificates_metadata', n.get_object_value(VerifiedCustomDomainCertificatesMetadata)),
            "verifiedCustomDomainKeyCredential": lambda n : setattr(self, 'verified_custom_domain_key_credential', n.get_object_value(KeyCredential)),
            "verifiedCustomDomainPasswordCredential": lambda n : setattr(self, 'verified_custom_domain_password_credential', n.get_object_value(PasswordCredential)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("alternateUrl", self.alternate_url)
        writer.write_str_value("applicationServerTimeout", self.application_server_timeout)
        writer.write_str_value("applicationType", self.application_type)
        writer.write_enum_value("externalAuthenticationType", self.external_authentication_type)
        writer.write_str_value("externalUrl", self.external_url)
        writer.write_str_value("internalUrl", self.internal_url)
        writer.write_bool_value("isAccessibleViaZTNAClient", self.is_accessible_via_z_t_n_a_client)
        writer.write_bool_value("isBackendCertificateValidationEnabled", self.is_backend_certificate_validation_enabled)
        writer.write_bool_value("isHttpOnlyCookieEnabled", self.is_http_only_cookie_enabled)
        writer.write_bool_value("isOnPremPublishingEnabled", self.is_on_prem_publishing_enabled)
        writer.write_bool_value("isPersistentCookieEnabled", self.is_persistent_cookie_enabled)
        writer.write_bool_value("isSecureCookieEnabled", self.is_secure_cookie_enabled)
        writer.write_bool_value("isStateSessionEnabled", self.is_state_session_enabled)
        writer.write_bool_value("isTranslateHostHeaderEnabled", self.is_translate_host_header_enabled)
        writer.write_bool_value("isTranslateLinksInBodyEnabled", self.is_translate_links_in_body_enabled)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_collection_of_object_values("onPremisesApplicationSegments", self.on_premises_application_segments)
        writer.write_object_value("segmentsConfiguration", self.segments_configuration)
        writer.write_object_value("singleSignOnSettings", self.single_sign_on_settings)
        writer.write_bool_value("useAlternateUrlForTranslationAndRedirect", self.use_alternate_url_for_translation_and_redirect)
        writer.write_object_value("verifiedCustomDomainCertificatesMetadata", self.verified_custom_domain_certificates_metadata)
        writer.write_object_value("verifiedCustomDomainKeyCredential", self.verified_custom_domain_key_credential)
        writer.write_object_value("verifiedCustomDomainPasswordCredential", self.verified_custom_domain_password_credential)
        writer.write_additional_data_value(self.additional_data)
    

