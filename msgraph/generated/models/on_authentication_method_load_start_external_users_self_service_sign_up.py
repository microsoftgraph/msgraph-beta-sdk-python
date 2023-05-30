from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_provider_base, on_authentication_method_load_start_handler

from . import on_authentication_method_load_start_handler

class OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp(on_authentication_method_load_start_handler.OnAuthenticationMethodLoadStartHandler):
    def __init__(self,) -> None:
        """
        Instantiates a new OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp"
        # The identityProviders property
        self._identity_providers: Optional[List[identity_provider_base.IdentityProviderBase]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_provider_base, on_authentication_method_load_start_handler

        fields: Dict[str, Callable[[Any], None]] = {
            "identityProviders": lambda n : setattr(self, 'identity_providers', n.get_collection_of_object_values(identity_provider_base.IdentityProviderBase)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_providers(self,) -> Optional[List[identity_provider_base.IdentityProviderBase]]:
        """
        Gets the identityProviders property value. The identityProviders property
        Returns: Optional[List[identity_provider_base.IdentityProviderBase]]
        """
        return self._identity_providers
    
    @identity_providers.setter
    def identity_providers(self,value: Optional[List[identity_provider_base.IdentityProviderBase]] = None) -> None:
        """
        Sets the identityProviders property value. The identityProviders property
        Args:
            value: Value to set for the identity_providers property.
        """
        self._identity_providers = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("identityProviders", self.identity_providers)
    

