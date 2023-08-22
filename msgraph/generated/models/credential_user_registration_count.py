from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_registration_count import UserRegistrationCount

from .entity import Entity

@dataclass
class CredentialUserRegistrationCount(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # Provides the count of users with accountEnabled set to true in the tenant.
    total_user_count: Optional[int] = None
    # A collection of registration count and status information for users in your tenant.
    user_registration_counts: Optional[List[UserRegistrationCount]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CredentialUserRegistrationCount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CredentialUserRegistrationCount
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CredentialUserRegistrationCount()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_registration_count import UserRegistrationCount

        from .entity import Entity
        from .user_registration_count import UserRegistrationCount

        fields: Dict[str, Callable[[Any], None]] = {
            "totalUserCount": lambda n : setattr(self, 'total_user_count', n.get_int_value()),
            "userRegistrationCounts": lambda n : setattr(self, 'user_registration_counts', n.get_collection_of_object_values(UserRegistrationCount)),
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
        writer.write_int_value("totalUserCount", self.total_user_count)
        writer.write_collection_of_object_values("userRegistrationCounts", self.user_registration_counts)
    

