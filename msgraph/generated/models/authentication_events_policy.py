from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_listener, entity

from . import entity

class AuthenticationEventsPolicy(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AuthenticationEventsPolicy and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A list of applicable actions to be taken on sign-up.
        self._on_signup_start: Optional[List[authentication_listener.AuthenticationListener]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationEventsPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationEventsPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationEventsPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_listener, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "onSignupStart": lambda n : setattr(self, 'on_signup_start', n.get_collection_of_object_values(authentication_listener.AuthenticationListener)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def on_signup_start(self,) -> Optional[List[authentication_listener.AuthenticationListener]]:
        """
        Gets the onSignupStart property value. A list of applicable actions to be taken on sign-up.
        Returns: Optional[List[authentication_listener.AuthenticationListener]]
        """
        return self._on_signup_start
    
    @on_signup_start.setter
    def on_signup_start(self,value: Optional[List[authentication_listener.AuthenticationListener]] = None) -> None:
        """
        Sets the onSignupStart property value. A list of applicable actions to be taken on sign-up.
        Args:
            value: Value to set for the on_signup_start property.
        """
        self._on_signup_start = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("onSignupStart", self.on_signup_start)
    

