from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_provider_base import IdentityProviderBase
    from .identity_provider_state import IdentityProviderState

from .identity_provider_base import IdentityProviderBase

@dataclass
class BuiltInIdentityProvider(IdentityProviderBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.builtInIdentityProvider"
    # The identity provider type. For a B2B scenario, possible values: AADSignup, MicrosoftAccount, EmailOTP. Required.
    identity_provider_type: Optional[str] = None
    # The state property
    state: Optional[IdentityProviderState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BuiltInIdentityProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
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
        from .identity_provider_base import IdentityProviderBase
        from .identity_provider_state import IdentityProviderState

        from .identity_provider_base import IdentityProviderBase
        from .identity_provider_state import IdentityProviderState

        fields: Dict[str, Callable[[Any], None]] = {
            "identityProviderType": lambda n : setattr(self, 'identity_provider_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(IdentityProviderState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("identityProviderType", self.identity_provider_type)
        writer.write_enum_value("state", self.state)
    

