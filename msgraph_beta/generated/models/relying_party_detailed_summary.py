from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .key_value_pair import KeyValuePair
    from .migration_status import MigrationStatus

from .entity import Entity

@dataclass
class RelyingPartyDetailedSummary(Entity):
    # Number of failed sign in on Active Directory Federation Service in the period specified.
    failed_sign_in_count: Optional[int] = None
    # The migrationStatus property
    migration_status: Optional[MigrationStatus] = None
    # Specifies all the validations check done on applications configuration details to evaluate if the application is ready to be moved to Microsoft Entra ID.
    migration_validation_details: Optional[List[KeyValuePair]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This identifier is used to identify the relying party to this Federation Service. It's used when issuing claims to the relying party.
    relying_party_id: Optional[str] = None
    # Name of application or other entity on the internet that uses an identity provider to authenticate a user who wants to sign in.
    relying_party_name: Optional[str] = None
    # Specifies where the relying party expects to receive the token.
    reply_urls: Optional[List[str]] = None
    # Uniquely identifies the Active Directory forest.
    service_id: Optional[str] = None
    # Number of successful / (number of successful + number of failed sign ins) on Active Directory Federation Service in the period specified.
    sign_in_success_rate: Optional[float] = None
    # Number of successful sign ins on Active Directory Federation Service.
    successful_sign_in_count: Optional[int] = None
    # Number of successful + failed sign ins on Active Directory Federation Service in the period specified.
    total_sign_in_count: Optional[int] = None
    # Number of unique users that have signed into the application.
    unique_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RelyingPartyDetailedSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RelyingPartyDetailedSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RelyingPartyDetailedSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .key_value_pair import KeyValuePair
        from .migration_status import MigrationStatus

        from .entity import Entity
        from .key_value_pair import KeyValuePair
        from .migration_status import MigrationStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "failedSignInCount": lambda n : setattr(self, 'failed_sign_in_count', n.get_int_value()),
            "migrationStatus": lambda n : setattr(self, 'migration_status', n.get_enum_value(MigrationStatus)),
            "migrationValidationDetails": lambda n : setattr(self, 'migration_validation_details', n.get_collection_of_object_values(KeyValuePair)),
            "relyingPartyId": lambda n : setattr(self, 'relying_party_id', n.get_str_value()),
            "relyingPartyName": lambda n : setattr(self, 'relying_party_name', n.get_str_value()),
            "replyUrls": lambda n : setattr(self, 'reply_urls', n.get_collection_of_primitive_values(str)),
            "serviceId": lambda n : setattr(self, 'service_id', n.get_str_value()),
            "signInSuccessRate": lambda n : setattr(self, 'sign_in_success_rate', n.get_float_value()),
            "successfulSignInCount": lambda n : setattr(self, 'successful_sign_in_count', n.get_int_value()),
            "totalSignInCount": lambda n : setattr(self, 'total_sign_in_count', n.get_int_value()),
            "uniqueUserCount": lambda n : setattr(self, 'unique_user_count', n.get_int_value()),
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
        writer.write_int_value("failedSignInCount", self.failed_sign_in_count)
        writer.write_enum_value("migrationStatus", self.migration_status)
        writer.write_collection_of_object_values("migrationValidationDetails", self.migration_validation_details)
        writer.write_str_value("relyingPartyId", self.relying_party_id)
        writer.write_str_value("relyingPartyName", self.relying_party_name)
        writer.write_collection_of_primitive_values("replyUrls", self.reply_urls)
        writer.write_str_value("serviceId", self.service_id)
        writer.write_float_value("signInSuccessRate", self.sign_in_success_rate)
        writer.write_int_value("successfulSignInCount", self.successful_sign_in_count)
        writer.write_int_value("totalSignInCount", self.total_sign_in_count)
        writer.write_int_value("uniqueUserCount", self.unique_user_count)
    

