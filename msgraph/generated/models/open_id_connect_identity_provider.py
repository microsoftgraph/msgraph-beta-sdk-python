from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import claims_mapping, identity_provider_base, open_id_connect_response_mode, open_id_connect_response_types

from . import identity_provider_base

@dataclass
class OpenIdConnectIdentityProvider(identity_provider_base.IdentityProviderBase):
    odata_type = "#microsoft.graph.openIdConnectIdentityProvider"
    # After the OIDC provider sends an ID token back to Azure AD, Azure AD needs to be able to map the claims from the received token to the claims that Azure AD recognizes and uses. This complex type captures that mapping. Required.
    claims_mapping: Optional[claims_mapping.ClaimsMapping] = None
    # The client identifier for the application obtained when registering the application with the identity provider. Required.
    client_id: Optional[str] = None
    # The client secret for the application obtained when registering the application with the identity provider. The clientSecret has a dependency on responseType. When responseType is code, a secret is required for the auth code exchange.When responseType is id_token the secret is not required because there is no code exchange. The id_token is returned directly from the authorization response. This is write-only. A read operation returns ****.
    client_secret: Optional[str] = None
    # The domain hint can be used to skip directly to the sign-in page of the specified identity provider, instead of having the user make a selection among the list of available identity providers.
    domain_hint: Optional[str] = None
    # The URL for the metadata document of the OpenID Connect identity provider. Every OpenID Connect identity provider describes a metadata document that contains most of the information required to perform sign-in. This includes information such as the URLs to use and the location of the service's public signing keys. The OpenID Connect metadata document is always located at an endpoint that ends in .well-known/openid-configuration. Provide the metadata URL for the OpenID Connect identity provider you add. Read-only. Required.
    metadata_url: Optional[str] = None
    # The responseMode property
    response_mode: Optional[open_id_connect_response_mode.OpenIdConnectResponseMode] = None
    # The responseType property
    response_type: Optional[open_id_connect_response_types.OpenIdConnectResponseTypes] = None
    # Scope defines the information and permissions you are looking to gather from your custom identity provider. OpenID Connect requests must contain the openid scope value in order to receive the ID token from the identity provider. Without the ID token, users are not able to sign in to Azure AD B2C using the custom identity provider. Other scopes can be appended, separated by a space. For more details about the scope limitations see RFC6749 Section 3.3. Required.
    scope: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OpenIdConnectIdentityProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OpenIdConnectIdentityProvider
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OpenIdConnectIdentityProvider()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import claims_mapping, identity_provider_base, open_id_connect_response_mode, open_id_connect_response_types

        from . import claims_mapping, identity_provider_base, open_id_connect_response_mode, open_id_connect_response_types

        fields: Dict[str, Callable[[Any], None]] = {
            "claimsMapping": lambda n : setattr(self, 'claims_mapping', n.get_object_value(claims_mapping.ClaimsMapping)),
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "clientSecret": lambda n : setattr(self, 'client_secret', n.get_str_value()),
            "domainHint": lambda n : setattr(self, 'domain_hint', n.get_str_value()),
            "metadataUrl": lambda n : setattr(self, 'metadata_url', n.get_str_value()),
            "responseMode": lambda n : setattr(self, 'response_mode', n.get_enum_value(open_id_connect_response_mode.OpenIdConnectResponseMode)),
            "responseType": lambda n : setattr(self, 'response_type', n.get_enum_value(open_id_connect_response_types.OpenIdConnectResponseTypes)),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("claimsMapping", self.claims_mapping)
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("clientSecret", self.client_secret)
        writer.write_str_value("domainHint", self.domain_hint)
        writer.write_str_value("metadataUrl", self.metadata_url)
        writer.write_enum_value("responseMode", self.response_mode)
        writer.write_enum_value("responseType", self.response_type)
        writer.write_str_value("scope", self.scope)
    

