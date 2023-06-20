from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_managed_identity_provider, built_in_identity_provider, entity, internal_domain_federation, open_id_connect_identity_provider, saml_or_ws_fed_external_domain_federation, saml_or_ws_fed_provider, social_identity_provider

from . import entity

@dataclass
class IdentityProviderBase(entity.Entity):
    # The display name of the identity provider.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityProviderBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityProviderBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleManagedIdentityProvider".casefold():
            from . import apple_managed_identity_provider

            return apple_managed_identity_provider.AppleManagedIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.builtInIdentityProvider".casefold():
            from . import built_in_identity_provider

            return built_in_identity_provider.BuiltInIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.internalDomainFederation".casefold():
            from . import internal_domain_federation

            return internal_domain_federation.InternalDomainFederation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openIdConnectIdentityProvider".casefold():
            from . import open_id_connect_identity_provider

            return open_id_connect_identity_provider.OpenIdConnectIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.samlOrWsFedExternalDomainFederation".casefold():
            from . import saml_or_ws_fed_external_domain_federation

            return saml_or_ws_fed_external_domain_federation.SamlOrWsFedExternalDomainFederation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.samlOrWsFedProvider".casefold():
            from . import saml_or_ws_fed_provider

            return saml_or_ws_fed_provider.SamlOrWsFedProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.socialIdentityProvider".casefold():
            from . import social_identity_provider

            return social_identity_provider.SocialIdentityProvider()
        return IdentityProviderBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_managed_identity_provider, built_in_identity_provider, entity, internal_domain_federation, open_id_connect_identity_provider, saml_or_ws_fed_external_domain_federation, saml_or_ws_fed_provider, social_identity_provider

        from . import apple_managed_identity_provider, built_in_identity_provider, entity, internal_domain_federation, open_id_connect_identity_provider, saml_or_ws_fed_external_domain_federation, saml_or_ws_fed_provider, social_identity_provider

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
    

