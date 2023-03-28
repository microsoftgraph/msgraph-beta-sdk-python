from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_protocol, identity_provider_base, internal_domain_federation, saml_or_ws_fed_external_domain_federation

from . import identity_provider_base

class SamlOrWsFedProvider(identity_provider_base.IdentityProviderBase):
    def __init__(self,) -> None:
        """
        Instantiates a new SamlOrWsFedProvider and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.samlOrWsFedProvider"
        # Issuer URI of the federation server.
        self._issuer_uri: Optional[str] = None
        # URI of the metadata exchange endpoint used for authentication from rich client applications.
        self._metadata_exchange_uri: Optional[str] = None
        # URI that web-based clients are directed to when signing in to Azure Active Directory (Azure AD) services.
        self._passive_sign_in_uri: Optional[str] = None
        # Preferred authentication protocol. Supported values include saml or wsfed.
        self._preferred_authentication_protocol: Optional[authentication_protocol.AuthenticationProtocol] = None
        # Current certificate used to sign tokens passed to the Microsoft identity platform. The certificate is formatted as a Base64 encoded string of the public portion of the federated IdP's token signing certificate and must be compatible with the X509Certificate2 class.   This property is used in the following scenarios:  if a rollover is required outside of the autorollover update a new federation service is being set up  if the new token signing certificate isn't present in the federation properties after the federation service certificate has been updated.   Azure AD updates certificates via an autorollover process in which it attempts to retrieve a new certificate from the federation service metadata, 30 days before expiry of the current certificate. If a new certificate isn't available, Azure AD monitors the metadata daily and will update the federation settings for the domain when a new certificate is available.
        self._signing_certificate: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SamlOrWsFedProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SamlOrWsFedProvider
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.internalDomainFederation":
                from . import internal_domain_federation

                return internal_domain_federation.InternalDomainFederation()
            if mapping_value == "#microsoft.graph.samlOrWsFedExternalDomainFederation":
                from . import saml_or_ws_fed_external_domain_federation

                return saml_or_ws_fed_external_domain_federation.SamlOrWsFedExternalDomainFederation()
        return SamlOrWsFedProvider()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_protocol, identity_provider_base, internal_domain_federation, saml_or_ws_fed_external_domain_federation

        fields: Dict[str, Callable[[Any], None]] = {
            "issuerUri": lambda n : setattr(self, 'issuer_uri', n.get_str_value()),
            "metadataExchangeUri": lambda n : setattr(self, 'metadata_exchange_uri', n.get_str_value()),
            "passiveSignInUri": lambda n : setattr(self, 'passive_sign_in_uri', n.get_str_value()),
            "preferredAuthenticationProtocol": lambda n : setattr(self, 'preferred_authentication_protocol', n.get_enum_value(authentication_protocol.AuthenticationProtocol)),
            "signingCertificate": lambda n : setattr(self, 'signing_certificate', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def issuer_uri(self,) -> Optional[str]:
        """
        Gets the issuerUri property value. Issuer URI of the federation server.
        Returns: Optional[str]
        """
        return self._issuer_uri
    
    @issuer_uri.setter
    def issuer_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the issuerUri property value. Issuer URI of the federation server.
        Args:
            value: Value to set for the issuer_uri property.
        """
        self._issuer_uri = value
    
    @property
    def metadata_exchange_uri(self,) -> Optional[str]:
        """
        Gets the metadataExchangeUri property value. URI of the metadata exchange endpoint used for authentication from rich client applications.
        Returns: Optional[str]
        """
        return self._metadata_exchange_uri
    
    @metadata_exchange_uri.setter
    def metadata_exchange_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the metadataExchangeUri property value. URI of the metadata exchange endpoint used for authentication from rich client applications.
        Args:
            value: Value to set for the metadata_exchange_uri property.
        """
        self._metadata_exchange_uri = value
    
    @property
    def passive_sign_in_uri(self,) -> Optional[str]:
        """
        Gets the passiveSignInUri property value. URI that web-based clients are directed to when signing in to Azure Active Directory (Azure AD) services.
        Returns: Optional[str]
        """
        return self._passive_sign_in_uri
    
    @passive_sign_in_uri.setter
    def passive_sign_in_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the passiveSignInUri property value. URI that web-based clients are directed to when signing in to Azure Active Directory (Azure AD) services.
        Args:
            value: Value to set for the passive_sign_in_uri property.
        """
        self._passive_sign_in_uri = value
    
    @property
    def preferred_authentication_protocol(self,) -> Optional[authentication_protocol.AuthenticationProtocol]:
        """
        Gets the preferredAuthenticationProtocol property value. Preferred authentication protocol. Supported values include saml or wsfed.
        Returns: Optional[authentication_protocol.AuthenticationProtocol]
        """
        return self._preferred_authentication_protocol
    
    @preferred_authentication_protocol.setter
    def preferred_authentication_protocol(self,value: Optional[authentication_protocol.AuthenticationProtocol] = None) -> None:
        """
        Sets the preferredAuthenticationProtocol property value. Preferred authentication protocol. Supported values include saml or wsfed.
        Args:
            value: Value to set for the preferred_authentication_protocol property.
        """
        self._preferred_authentication_protocol = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("issuerUri", self.issuer_uri)
        writer.write_str_value("metadataExchangeUri", self.metadata_exchange_uri)
        writer.write_str_value("passiveSignInUri", self.passive_sign_in_uri)
        writer.write_enum_value("preferredAuthenticationProtocol", self.preferred_authentication_protocol)
        writer.write_str_value("signingCertificate", self.signing_certificate)
    
    @property
    def signing_certificate(self,) -> Optional[str]:
        """
        Gets the signingCertificate property value. Current certificate used to sign tokens passed to the Microsoft identity platform. The certificate is formatted as a Base64 encoded string of the public portion of the federated IdP's token signing certificate and must be compatible with the X509Certificate2 class.   This property is used in the following scenarios:  if a rollover is required outside of the autorollover update a new federation service is being set up  if the new token signing certificate isn't present in the federation properties after the federation service certificate has been updated.   Azure AD updates certificates via an autorollover process in which it attempts to retrieve a new certificate from the federation service metadata, 30 days before expiry of the current certificate. If a new certificate isn't available, Azure AD monitors the metadata daily and will update the federation settings for the domain when a new certificate is available.
        Returns: Optional[str]
        """
        return self._signing_certificate
    
    @signing_certificate.setter
    def signing_certificate(self,value: Optional[str] = None) -> None:
        """
        Sets the signingCertificate property value. Current certificate used to sign tokens passed to the Microsoft identity platform. The certificate is formatted as a Base64 encoded string of the public portion of the federated IdP's token signing certificate and must be compatible with the X509Certificate2 class.   This property is used in the following scenarios:  if a rollover is required outside of the autorollover update a new federation service is being set up  if the new token signing certificate isn't present in the federation properties after the federation service certificate has been updated.   Azure AD updates certificates via an autorollover process in which it attempts to retrieve a new certificate from the federation service metadata, 30 days before expiry of the current certificate. If a new certificate isn't available, Azure AD monitors the metadata daily and will update the federation settings for the domain when a new certificate is available.
        Args:
            value: Value to set for the signing_certificate property.
        """
        self._signing_certificate = value
    

