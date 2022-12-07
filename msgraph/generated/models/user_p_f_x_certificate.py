from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user_pfx_intended_purpose = lazy_import('msgraph.generated.models.user_pfx_intended_purpose')
user_pfx_padding_scheme = lazy_import('msgraph.generated.models.user_pfx_padding_scheme')

class UserPFXCertificate(entity.Entity):
    """
    Entity that encapsulates all information required for a user's PFX certificates.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new userPFXCertificate and sets the default values.
        """
        super().__init__()
        # Date/time when this PFX certificate was imported.
        self._created_date_time: Optional[datetime] = None
        # Encrypted PFX blob.
        self._encrypted_pfx_blob: Optional[bytes] = None
        # Encrypted PFX password.
        self._encrypted_pfx_password: Optional[str] = None
        # Certificate's validity expiration date/time.
        self._expiration_date_time: Optional[datetime] = None
        # Supported values for the intended purpose of a user PFX certificate.
        self._intended_purpose: Optional[user_pfx_intended_purpose.UserPfxIntendedPurpose] = None
        # Name of the key (within the provider) used to encrypt the blob.
        self._key_name: Optional[str] = None
        # Date/time when this PFX certificate was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Supported values for the padding scheme used by encryption provider.
        self._padding_scheme: Optional[user_pfx_padding_scheme.UserPfxPaddingScheme] = None
        # Crypto provider used to encrypt this blob.
        self._provider_name: Optional[str] = None
        # Certificate's validity start date/time.
        self._start_date_time: Optional[datetime] = None
        # SHA-1 thumbprint of the PFX certificate.
        self._thumbprint: Optional[str] = None
        # User Principal Name of the PFX certificate.
        self._user_principal_name: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date/time when this PFX certificate was imported.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date/time when this PFX certificate was imported.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserPFXCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserPFXCertificate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserPFXCertificate()
    
    @property
    def encrypted_pfx_blob(self,) -> Optional[bytes]:
        """
        Gets the encryptedPfxBlob property value. Encrypted PFX blob.
        Returns: Optional[bytes]
        """
        return self._encrypted_pfx_blob
    
    @encrypted_pfx_blob.setter
    def encrypted_pfx_blob(self,value: Optional[bytes] = None) -> None:
        """
        Sets the encryptedPfxBlob property value. Encrypted PFX blob.
        Args:
            value: Value to set for the encryptedPfxBlob property.
        """
        self._encrypted_pfx_blob = value
    
    @property
    def encrypted_pfx_password(self,) -> Optional[str]:
        """
        Gets the encryptedPfxPassword property value. Encrypted PFX password.
        Returns: Optional[str]
        """
        return self._encrypted_pfx_password
    
    @encrypted_pfx_password.setter
    def encrypted_pfx_password(self,value: Optional[str] = None) -> None:
        """
        Sets the encryptedPfxPassword property value. Encrypted PFX password.
        Args:
            value: Value to set for the encryptedPfxPassword property.
        """
        self._encrypted_pfx_password = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. Certificate's validity expiration date/time.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. Certificate's validity expiration date/time.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "encrypted_pfx_blob": lambda n : setattr(self, 'encrypted_pfx_blob', n.get_bytes_value()),
            "encrypted_pfx_password": lambda n : setattr(self, 'encrypted_pfx_password', n.get_str_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "intended_purpose": lambda n : setattr(self, 'intended_purpose', n.get_enum_value(user_pfx_intended_purpose.UserPfxIntendedPurpose)),
            "key_name": lambda n : setattr(self, 'key_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "padding_scheme": lambda n : setattr(self, 'padding_scheme', n.get_enum_value(user_pfx_padding_scheme.UserPfxPaddingScheme)),
            "provider_name": lambda n : setattr(self, 'provider_name', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "thumbprint": lambda n : setattr(self, 'thumbprint', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def intended_purpose(self,) -> Optional[user_pfx_intended_purpose.UserPfxIntendedPurpose]:
        """
        Gets the intendedPurpose property value. Supported values for the intended purpose of a user PFX certificate.
        Returns: Optional[user_pfx_intended_purpose.UserPfxIntendedPurpose]
        """
        return self._intended_purpose
    
    @intended_purpose.setter
    def intended_purpose(self,value: Optional[user_pfx_intended_purpose.UserPfxIntendedPurpose] = None) -> None:
        """
        Sets the intendedPurpose property value. Supported values for the intended purpose of a user PFX certificate.
        Args:
            value: Value to set for the intendedPurpose property.
        """
        self._intended_purpose = value
    
    @property
    def key_name(self,) -> Optional[str]:
        """
        Gets the keyName property value. Name of the key (within the provider) used to encrypt the blob.
        Returns: Optional[str]
        """
        return self._key_name
    
    @key_name.setter
    def key_name(self,value: Optional[str] = None) -> None:
        """
        Sets the keyName property value. Name of the key (within the provider) used to encrypt the blob.
        Args:
            value: Value to set for the keyName property.
        """
        self._key_name = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Date/time when this PFX certificate was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Date/time when this PFX certificate was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def padding_scheme(self,) -> Optional[user_pfx_padding_scheme.UserPfxPaddingScheme]:
        """
        Gets the paddingScheme property value. Supported values for the padding scheme used by encryption provider.
        Returns: Optional[user_pfx_padding_scheme.UserPfxPaddingScheme]
        """
        return self._padding_scheme
    
    @padding_scheme.setter
    def padding_scheme(self,value: Optional[user_pfx_padding_scheme.UserPfxPaddingScheme] = None) -> None:
        """
        Sets the paddingScheme property value. Supported values for the padding scheme used by encryption provider.
        Args:
            value: Value to set for the paddingScheme property.
        """
        self._padding_scheme = value
    
    @property
    def provider_name(self,) -> Optional[str]:
        """
        Gets the providerName property value. Crypto provider used to encrypt this blob.
        Returns: Optional[str]
        """
        return self._provider_name
    
    @provider_name.setter
    def provider_name(self,value: Optional[str] = None) -> None:
        """
        Sets the providerName property value. Crypto provider used to encrypt this blob.
        Args:
            value: Value to set for the providerName property.
        """
        self._provider_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("encryptedPfxBlob", self.encrypted_pfx_blob)
        writer.write_str_value("encryptedPfxPassword", self.encrypted_pfx_password)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_enum_value("intendedPurpose", self.intended_purpose)
        writer.write_str_value("keyName", self.key_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("paddingScheme", self.padding_scheme)
        writer.write_str_value("providerName", self.provider_name)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("thumbprint", self.thumbprint)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. Certificate's validity start date/time.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. Certificate's validity start date/time.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def thumbprint(self,) -> Optional[str]:
        """
        Gets the thumbprint property value. SHA-1 thumbprint of the PFX certificate.
        Returns: Optional[str]
        """
        return self._thumbprint
    
    @thumbprint.setter
    def thumbprint(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbprint property value. SHA-1 thumbprint of the PFX certificate.
        Args:
            value: Value to set for the thumbprint property.
        """
        self._thumbprint = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User Principal Name of the PFX certificate.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User Principal Name of the PFX certificate.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

