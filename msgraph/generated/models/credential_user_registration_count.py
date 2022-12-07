from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user_registration_count = lazy_import('msgraph.generated.models.user_registration_count')

class CredentialUserRegistrationCount(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new CredentialUserRegistrationCount and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Provides the total user count in the tenant.
        self._total_user_count: Optional[int] = None
        # A collection of registration count and status information for users in your tenant.
        self._user_registration_counts: Optional[List[user_registration_count.UserRegistrationCount]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CredentialUserRegistrationCount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CredentialUserRegistrationCount
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CredentialUserRegistrationCount()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "total_user_count": lambda n : setattr(self, 'total_user_count', n.get_int_value()),
            "user_registration_counts": lambda n : setattr(self, 'user_registration_counts', n.get_collection_of_object_values(user_registration_count.UserRegistrationCount)),
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
        writer.write_int_value("totalUserCount", self.total_user_count)
        writer.write_collection_of_object_values("userRegistrationCounts", self.user_registration_counts)
    
    @property
    def total_user_count(self,) -> Optional[int]:
        """
        Gets the totalUserCount property value. Provides the total user count in the tenant.
        Returns: Optional[int]
        """
        return self._total_user_count
    
    @total_user_count.setter
    def total_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalUserCount property value. Provides the total user count in the tenant.
        Args:
            value: Value to set for the totalUserCount property.
        """
        self._total_user_count = value
    
    @property
    def user_registration_counts(self,) -> Optional[List[user_registration_count.UserRegistrationCount]]:
        """
        Gets the userRegistrationCounts property value. A collection of registration count and status information for users in your tenant.
        Returns: Optional[List[user_registration_count.UserRegistrationCount]]
        """
        return self._user_registration_counts
    
    @user_registration_counts.setter
    def user_registration_counts(self,value: Optional[List[user_registration_count.UserRegistrationCount]] = None) -> None:
        """
        Sets the userRegistrationCounts property value. A collection of registration count and status information for users in your tenant.
        Args:
            value: Value to set for the userRegistrationCounts property.
        """
        self._user_registration_counts = value
    

