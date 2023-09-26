from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .b2b_identity_providers_type import B2bIdentityProvidersType
    from .default_invitation_redemption_identity_provider_configuration import DefaultInvitationRedemptionIdentityProviderConfiguration

@dataclass
class InvitationRedemptionIdentityProviderConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The fallbackIdentityProvider property
    fallback_identity_provider: Optional[B2bIdentityProvidersType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The primaryIdentityProviderPrecedenceOrder property
    primary_identity_provider_precedence_order: Optional[List[B2bIdentityProvidersType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InvitationRedemptionIdentityProviderConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvitationRedemptionIdentityProviderConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.defaultInvitationRedemptionIdentityProviderConfiguration".casefold():
            from .default_invitation_redemption_identity_provider_configuration import DefaultInvitationRedemptionIdentityProviderConfiguration

            return DefaultInvitationRedemptionIdentityProviderConfiguration()
        return InvitationRedemptionIdentityProviderConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .b2b_identity_providers_type import B2bIdentityProvidersType
        from .default_invitation_redemption_identity_provider_configuration import DefaultInvitationRedemptionIdentityProviderConfiguration

        from .b2b_identity_providers_type import B2bIdentityProvidersType
        from .default_invitation_redemption_identity_provider_configuration import DefaultInvitationRedemptionIdentityProviderConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "fallbackIdentityProvider": lambda n : setattr(self, 'fallback_identity_provider', n.get_enum_value(B2bIdentityProvidersType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primaryIdentityProviderPrecedenceOrder": lambda n : setattr(self, 'primary_identity_provider_precedence_order', n.get_collection_of_enum_values(B2bIdentityProvidersType)),
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
        writer.write_enum_value("fallbackIdentityProvider", self.fallback_identity_provider)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_enum_values("primaryIdentityProviderPrecedenceOrder", self.primary_identity_provider_precedence_order)
        writer.write_additional_data_value(self.additional_data)
    

