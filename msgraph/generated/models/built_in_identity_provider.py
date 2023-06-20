from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_provider_base, identity_provider_state

from . import identity_provider_base

@dataclass
class BuiltInIdentityProvider(identity_provider_base.IdentityProviderBase):
    odata_type = "#microsoft.graph.builtInIdentityProvider"
    # The identity provider type. For a B2B scenario, possible values: AADSignup, MicrosoftAccount, EmailOTP. Required.
    identity_provider_type: Optional[str] = None
    # The state property
    state: Optional[identity_provider_state.IdentityProviderState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BuiltInIdentityProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BuiltInIdentityProvider
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BuiltInIdentityProvider()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_provider_base, identity_provider_state

        from . import identity_provider_base, identity_provider_state

        fields: Dict[str, Callable[[Any], None]] = {
            "identityProviderType": lambda n : setattr(self, 'identity_provider_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(identity_provider_state.IdentityProviderState)),
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
        writer.write_str_value("identityProviderType", self.identity_provider_type)
        writer.write_enum_value("state", self.state)
    

