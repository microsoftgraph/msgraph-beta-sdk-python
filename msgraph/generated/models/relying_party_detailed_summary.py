from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
migration_status = lazy_import('msgraph.generated.models.migration_status')

class RelyingPartyDetailedSummary(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new RelyingPartyDetailedSummary and sets the default values.
        """
        super().__init__()
        # Number of failed sign in on Active Directory Federation Service in the period specified.
        self._failed_sign_in_count: Optional[int] = None
        # The migrationStatus property
        self._migration_status: Optional[migration_status.MigrationStatus] = None
        # Specifies all the validations check done on applications configuration details to evaluate if the application is ready to be moved to Azure AD.
        self._migration_validation_details: Optional[List[key_value_pair.KeyValuePair]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # This identifier is used to identify the relying party to this Federation Service. It is used when issuing claims to the relying party.
        self._relying_party_id: Optional[str] = None
        # Name of application or other entity on the internet that uses an identity provider to authenticate a user who wants to log in.
        self._relying_party_name: Optional[str] = None
        # Specifies where the relying party expects to receive the token.
        self._reply_urls: Optional[List[str]] = None
        # Uniquely identifies the Active Directory forest.
        self._service_id: Optional[str] = None
        # Number of successful / (number of successful + number of failed sign ins) on Active Directory Federation Service in the period specified.
        self._sign_in_success_rate: Optional[float] = None
        # Number of successful sign ins on Active Directory Federation Service.
        self._successful_sign_in_count: Optional[int] = None
        # Number of successful + failed sign ins failed sign ins on Active Directory Federation Service in the period specified.
        self._total_sign_in_count: Optional[int] = None
        # Number of unique users that have signed into the application.
        self._unique_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RelyingPartyDetailedSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RelyingPartyDetailedSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RelyingPartyDetailedSummary()
    
    @property
    def failed_sign_in_count(self,) -> Optional[int]:
        """
        Gets the failedSignInCount property value. Number of failed sign in on Active Directory Federation Service in the period specified.
        Returns: Optional[int]
        """
        return self._failed_sign_in_count
    
    @failed_sign_in_count.setter
    def failed_sign_in_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedSignInCount property value. Number of failed sign in on Active Directory Federation Service in the period specified.
        Args:
            value: Value to set for the failedSignInCount property.
        """
        self._failed_sign_in_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "failed_sign_in_count": lambda n : setattr(self, 'failed_sign_in_count', n.get_int_value()),
            "migration_status": lambda n : setattr(self, 'migration_status', n.get_enum_value(migration_status.MigrationStatus)),
            "migration_validation_details": lambda n : setattr(self, 'migration_validation_details', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "relying_party_id": lambda n : setattr(self, 'relying_party_id', n.get_str_value()),
            "relying_party_name": lambda n : setattr(self, 'relying_party_name', n.get_str_value()),
            "reply_urls": lambda n : setattr(self, 'reply_urls', n.get_collection_of_primitive_values(str)),
            "service_id": lambda n : setattr(self, 'service_id', n.get_str_value()),
            "sign_in_success_rate": lambda n : setattr(self, 'sign_in_success_rate', n.get_float_value()),
            "successful_sign_in_count": lambda n : setattr(self, 'successful_sign_in_count', n.get_int_value()),
            "total_sign_in_count": lambda n : setattr(self, 'total_sign_in_count', n.get_int_value()),
            "unique_user_count": lambda n : setattr(self, 'unique_user_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def migration_status(self,) -> Optional[migration_status.MigrationStatus]:
        """
        Gets the migrationStatus property value. The migrationStatus property
        Returns: Optional[migration_status.MigrationStatus]
        """
        return self._migration_status
    
    @migration_status.setter
    def migration_status(self,value: Optional[migration_status.MigrationStatus] = None) -> None:
        """
        Sets the migrationStatus property value. The migrationStatus property
        Args:
            value: Value to set for the migrationStatus property.
        """
        self._migration_status = value
    
    @property
    def migration_validation_details(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the migrationValidationDetails property value. Specifies all the validations check done on applications configuration details to evaluate if the application is ready to be moved to Azure AD.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._migration_validation_details
    
    @migration_validation_details.setter
    def migration_validation_details(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the migrationValidationDetails property value. Specifies all the validations check done on applications configuration details to evaluate if the application is ready to be moved to Azure AD.
        Args:
            value: Value to set for the migrationValidationDetails property.
        """
        self._migration_validation_details = value
    
    @property
    def relying_party_id(self,) -> Optional[str]:
        """
        Gets the relyingPartyId property value. This identifier is used to identify the relying party to this Federation Service. It is used when issuing claims to the relying party.
        Returns: Optional[str]
        """
        return self._relying_party_id
    
    @relying_party_id.setter
    def relying_party_id(self,value: Optional[str] = None) -> None:
        """
        Sets the relyingPartyId property value. This identifier is used to identify the relying party to this Federation Service. It is used when issuing claims to the relying party.
        Args:
            value: Value to set for the relyingPartyId property.
        """
        self._relying_party_id = value
    
    @property
    def relying_party_name(self,) -> Optional[str]:
        """
        Gets the relyingPartyName property value. Name of application or other entity on the internet that uses an identity provider to authenticate a user who wants to log in.
        Returns: Optional[str]
        """
        return self._relying_party_name
    
    @relying_party_name.setter
    def relying_party_name(self,value: Optional[str] = None) -> None:
        """
        Sets the relyingPartyName property value. Name of application or other entity on the internet that uses an identity provider to authenticate a user who wants to log in.
        Args:
            value: Value to set for the relyingPartyName property.
        """
        self._relying_party_name = value
    
    @property
    def reply_urls(self,) -> Optional[List[str]]:
        """
        Gets the replyUrls property value. Specifies where the relying party expects to receive the token.
        Returns: Optional[List[str]]
        """
        return self._reply_urls
    
    @reply_urls.setter
    def reply_urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the replyUrls property value. Specifies where the relying party expects to receive the token.
        Args:
            value: Value to set for the replyUrls property.
        """
        self._reply_urls = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def service_id(self,) -> Optional[str]:
        """
        Gets the serviceId property value. Uniquely identifies the Active Directory forest.
        Returns: Optional[str]
        """
        return self._service_id
    
    @service_id.setter
    def service_id(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceId property value. Uniquely identifies the Active Directory forest.
        Args:
            value: Value to set for the serviceId property.
        """
        self._service_id = value
    
    @property
    def sign_in_success_rate(self,) -> Optional[float]:
        """
        Gets the signInSuccessRate property value. Number of successful / (number of successful + number of failed sign ins) on Active Directory Federation Service in the period specified.
        Returns: Optional[float]
        """
        return self._sign_in_success_rate
    
    @sign_in_success_rate.setter
    def sign_in_success_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the signInSuccessRate property value. Number of successful / (number of successful + number of failed sign ins) on Active Directory Federation Service in the period specified.
        Args:
            value: Value to set for the signInSuccessRate property.
        """
        self._sign_in_success_rate = value
    
    @property
    def successful_sign_in_count(self,) -> Optional[int]:
        """
        Gets the successfulSignInCount property value. Number of successful sign ins on Active Directory Federation Service.
        Returns: Optional[int]
        """
        return self._successful_sign_in_count
    
    @successful_sign_in_count.setter
    def successful_sign_in_count(self,value: Optional[int] = None) -> None:
        """
        Sets the successfulSignInCount property value. Number of successful sign ins on Active Directory Federation Service.
        Args:
            value: Value to set for the successfulSignInCount property.
        """
        self._successful_sign_in_count = value
    
    @property
    def total_sign_in_count(self,) -> Optional[int]:
        """
        Gets the totalSignInCount property value. Number of successful + failed sign ins failed sign ins on Active Directory Federation Service in the period specified.
        Returns: Optional[int]
        """
        return self._total_sign_in_count
    
    @total_sign_in_count.setter
    def total_sign_in_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalSignInCount property value. Number of successful + failed sign ins failed sign ins on Active Directory Federation Service in the period specified.
        Args:
            value: Value to set for the totalSignInCount property.
        """
        self._total_sign_in_count = value
    
    @property
    def unique_user_count(self,) -> Optional[int]:
        """
        Gets the uniqueUserCount property value. Number of unique users that have signed into the application.
        Returns: Optional[int]
        """
        return self._unique_user_count
    
    @unique_user_count.setter
    def unique_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the uniqueUserCount property value. Number of unique users that have signed into the application.
        Args:
            value: Value to set for the uniqueUserCount property.
        """
        self._unique_user_count = value
    

