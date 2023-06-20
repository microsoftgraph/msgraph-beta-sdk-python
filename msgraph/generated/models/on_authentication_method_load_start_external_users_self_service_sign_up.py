from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_provider_base, on_authentication_method_load_start_handler

from . import on_authentication_method_load_start_handler

@dataclass
class OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp(on_authentication_method_load_start_handler.OnAuthenticationMethodLoadStartHandler):
    odata_type = "#microsoft.graph.onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp"
    # The identityProviders property
    identity_providers: Optional[List[identity_provider_base.IdentityProviderBase]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_provider_base, on_authentication_method_load_start_handler

        from . import identity_provider_base, on_authentication_method_load_start_handler

        fields: Dict[str, Callable[[Any], None]] = {
            "identityProviders": lambda n : setattr(self, 'identity_providers', n.get_collection_of_object_values(identity_provider_base.IdentityProviderBase)),
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
        writer.write_collection_of_object_values("identityProviders", self.identity_providers)
    

