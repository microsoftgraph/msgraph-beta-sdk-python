from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_provider_base, identity_provider_state

from . import identity_provider_base

class BuiltInIdentityProvider(identity_provider_base.IdentityProviderBase):
    def __init__(self,) -> None:
        """
        Instantiates a new BuiltInIdentityProvider and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.builtInIdentityProvider"
        # The identity provider type. For a B2B scenario, possible values: AADSignup, MicrosoftAccount, EmailOTP. Required.
        self._identity_provider_type: Optional[str] = None
        # The state property
        self._state: Optional[identity_provider_state.IdentityProviderState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BuiltInIdentityProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BuiltInIdentityProvider
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BuiltInIdentityProvider()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_provider_base, identity_provider_state

        fields: Dict[str, Callable[[Any], None]] = {
            "identityProviderType": lambda n : setattr(self, 'identity_provider_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(identity_provider_state.IdentityProviderState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_provider_type(self,) -> Optional[str]:
        """
        Gets the identityProviderType property value. The identity provider type. For a B2B scenario, possible values: AADSignup, MicrosoftAccount, EmailOTP. Required.
        Returns: Optional[str]
        """
        return self._identity_provider_type
    
    @identity_provider_type.setter
    def identity_provider_type(self,value: Optional[str] = None) -> None:
        """
        Sets the identityProviderType property value. The identity provider type. For a B2B scenario, possible values: AADSignup, MicrosoftAccount, EmailOTP. Required.
        Args:
            value: Value to set for the identity_provider_type property.
        """
        self._identity_provider_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("identityProviderType", self.identity_provider_type)
        writer.write_enum_value("state", self.state)
    
    @property
    def state(self,) -> Optional[identity_provider_state.IdentityProviderState]:
        """
        Gets the state property value. The state property
        Returns: Optional[identity_provider_state.IdentityProviderState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[identity_provider_state.IdentityProviderState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

