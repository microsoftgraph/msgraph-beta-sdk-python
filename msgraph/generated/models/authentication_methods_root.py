from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, user_registration_details

from . import entity

class AuthenticationMethodsRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AuthenticationMethodsRoot and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents the state of a user's authentication methods, including which methods are registered and which features the user is registered and capable of (such as multi-factor authentication, self-service password reset, and passwordless authentication).
        self._user_registration_details: Optional[List[user_registration_details.UserRegistrationDetails]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodsRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationMethodsRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, user_registration_details

        fields: Dict[str, Callable[[Any], None]] = {
            "userRegistrationDetails": lambda n : setattr(self, 'user_registration_details', n.get_collection_of_object_values(user_registration_details.UserRegistrationDetails)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("userRegistrationDetails", self.user_registration_details)
    
    @property
    def user_registration_details(self,) -> Optional[List[user_registration_details.UserRegistrationDetails]]:
        """
        Gets the userRegistrationDetails property value. Represents the state of a user's authentication methods, including which methods are registered and which features the user is registered and capable of (such as multi-factor authentication, self-service password reset, and passwordless authentication).
        Returns: Optional[List[user_registration_details.UserRegistrationDetails]]
        """
        return self._user_registration_details
    
    @user_registration_details.setter
    def user_registration_details(self,value: Optional[List[user_registration_details.UserRegistrationDetails]] = None) -> None:
        """
        Sets the userRegistrationDetails property value. Represents the state of a user's authentication methods, including which methods are registered and which features the user is registered and capable of (such as multi-factor authentication, self-service password reset, and passwordless authentication).
        Args:
            value: Value to set for the user_registration_details property.
        """
        self._user_registration_details = value
    

