from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

claims_mapping = lazy_import('msgraph.generated.models.claims_mapping')
identity_provider = lazy_import('msgraph.generated.models.identity_provider')
open_id_connect_response_mode = lazy_import('msgraph.generated.models.open_id_connect_response_mode')
open_id_connect_response_types = lazy_import('msgraph.generated.models.open_id_connect_response_types')

class OpenIdConnectProvider(identity_provider.IdentityProvider):
    @property
    def claims_mapping(self,) -> Optional[claims_mapping.ClaimsMapping]:
        """
        Gets the claimsMapping property value. After the OIDC provider sends an ID token back to Azure AD, Azure AD needs to be able to map the claims from the received token to the claims that Azure AD recognizes and uses. This complex type captures that mapping. It is a required property.
        Returns: Optional[claims_mapping.ClaimsMapping]
        """
        return self._claims_mapping
    
    @claims_mapping.setter
    def claims_mapping(self,value: Optional[claims_mapping.ClaimsMapping] = None) -> None:
        """
        Sets the claimsMapping property value. After the OIDC provider sends an ID token back to Azure AD, Azure AD needs to be able to map the claims from the received token to the claims that Azure AD recognizes and uses. This complex type captures that mapping. It is a required property.
        Args:
            value: Value to set for the claimsMapping property.
        """
        self._claims_mapping = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new OpenIdConnectProvider and sets the default values.
        """
        super().__init__()
        # After the OIDC provider sends an ID token back to Azure AD, Azure AD needs to be able to map the claims from the received token to the claims that Azure AD recognizes and uses. This complex type captures that mapping. It is a required property.
        self._claims_mapping: Optional[claims_mapping.ClaimsMapping] = None
        # The domain hint can be used to skip directly to the sign-in page of the specified identity provider, instead of having the user make a selection among the list of available identity providers.
        self._domain_hint: Optional[str] = None
        # The URL for the metadata document of the OpenID Connect identity provider. Every OpenID Connect identity provider describes a metadata document that contains most of the information required to perform sign-in. This includes information such as the URLs to use and the location of the service's public signing keys. The OpenID Connect metadata document is always located at an endpoint that ends in .well-known/openid-configuration . For the OpenID Connect identity provider you are looking to add, you will need to provide the metadata URL. It is a required property and is read only after creation.
        self._metadata_url: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The responseMode property
        self._response_mode: Optional[open_id_connect_response_mode.OpenIdConnectResponseMode] = None
        # The responseType property
        self._response_type: Optional[open_id_connect_response_types.OpenIdConnectResponseTypes] = None
        # Scope defines the information and permissions you are looking to gather from your custom identity provider. OpenID Connect requests must contain the openid scope value in order to receive the ID token from the identity provider. Without the ID token, users are not able to sign in to Azure AD B2C using the custom identity provider. Other scopes can be appended separated by space. For more details about the scope limitations see RFC6749 Section 3.3. It is a required property.
        self._scope: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OpenIdConnectProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OpenIdConnectProvider
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OpenIdConnectProvider()
    
    @property
    def domain_hint(self,) -> Optional[str]:
        """
        Gets the domainHint property value. The domain hint can be used to skip directly to the sign-in page of the specified identity provider, instead of having the user make a selection among the list of available identity providers.
        Returns: Optional[str]
        """
        return self._domain_hint
    
    @domain_hint.setter
    def domain_hint(self,value: Optional[str] = None) -> None:
        """
        Sets the domainHint property value. The domain hint can be used to skip directly to the sign-in page of the specified identity provider, instead of having the user make a selection among the list of available identity providers.
        Args:
            value: Value to set for the domainHint property.
        """
        self._domain_hint = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "claims_mapping": lambda n : setattr(self, 'claims_mapping', n.get_object_value(claims_mapping.ClaimsMapping)),
            "domain_hint": lambda n : setattr(self, 'domain_hint', n.get_str_value()),
            "metadata_url": lambda n : setattr(self, 'metadata_url', n.get_str_value()),
            "response_mode": lambda n : setattr(self, 'response_mode', n.get_enum_value(open_id_connect_response_mode.OpenIdConnectResponseMode)),
            "response_type": lambda n : setattr(self, 'response_type', n.get_enum_value(open_id_connect_response_types.OpenIdConnectResponseTypes)),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def metadata_url(self,) -> Optional[str]:
        """
        Gets the metadataUrl property value. The URL for the metadata document of the OpenID Connect identity provider. Every OpenID Connect identity provider describes a metadata document that contains most of the information required to perform sign-in. This includes information such as the URLs to use and the location of the service's public signing keys. The OpenID Connect metadata document is always located at an endpoint that ends in .well-known/openid-configuration . For the OpenID Connect identity provider you are looking to add, you will need to provide the metadata URL. It is a required property and is read only after creation.
        Returns: Optional[str]
        """
        return self._metadata_url
    
    @metadata_url.setter
    def metadata_url(self,value: Optional[str] = None) -> None:
        """
        Sets the metadataUrl property value. The URL for the metadata document of the OpenID Connect identity provider. Every OpenID Connect identity provider describes a metadata document that contains most of the information required to perform sign-in. This includes information such as the URLs to use and the location of the service's public signing keys. The OpenID Connect metadata document is always located at an endpoint that ends in .well-known/openid-configuration . For the OpenID Connect identity provider you are looking to add, you will need to provide the metadata URL. It is a required property and is read only after creation.
        Args:
            value: Value to set for the metadataUrl property.
        """
        self._metadata_url = value
    
    @property
    def response_mode(self,) -> Optional[open_id_connect_response_mode.OpenIdConnectResponseMode]:
        """
        Gets the responseMode property value. The responseMode property
        Returns: Optional[open_id_connect_response_mode.OpenIdConnectResponseMode]
        """
        return self._response_mode
    
    @response_mode.setter
    def response_mode(self,value: Optional[open_id_connect_response_mode.OpenIdConnectResponseMode] = None) -> None:
        """
        Sets the responseMode property value. The responseMode property
        Args:
            value: Value to set for the responseMode property.
        """
        self._response_mode = value
    
    @property
    def response_type(self,) -> Optional[open_id_connect_response_types.OpenIdConnectResponseTypes]:
        """
        Gets the responseType property value. The responseType property
        Returns: Optional[open_id_connect_response_types.OpenIdConnectResponseTypes]
        """
        return self._response_type
    
    @response_type.setter
    def response_type(self,value: Optional[open_id_connect_response_types.OpenIdConnectResponseTypes] = None) -> None:
        """
        Sets the responseType property value. The responseType property
        Args:
            value: Value to set for the responseType property.
        """
        self._response_type = value
    
    @property
    def scope(self,) -> Optional[str]:
        """
        Gets the scope property value. Scope defines the information and permissions you are looking to gather from your custom identity provider. OpenID Connect requests must contain the openid scope value in order to receive the ID token from the identity provider. Without the ID token, users are not able to sign in to Azure AD B2C using the custom identity provider. Other scopes can be appended separated by space. For more details about the scope limitations see RFC6749 Section 3.3. It is a required property.
        Returns: Optional[str]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[str] = None) -> None:
        """
        Sets the scope property value. Scope defines the information and permissions you are looking to gather from your custom identity provider. OpenID Connect requests must contain the openid scope value in order to receive the ID token from the identity provider. Without the ID token, users are not able to sign in to Azure AD B2C using the custom identity provider. Other scopes can be appended separated by space. For more details about the scope limitations see RFC6749 Section 3.3. It is a required property.
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("claimsMapping", self.claims_mapping)
        writer.write_str_value("domainHint", self.domain_hint)
        writer.write_str_value("metadataUrl", self.metadata_url)
        writer.write_enum_value("responseMode", self.response_mode)
        writer.write_enum_value("responseType", self.response_type)
        writer.write_str_value("scope", self.scope)
    

