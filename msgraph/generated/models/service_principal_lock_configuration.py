from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ServicePrincipalLockConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new servicePrincipalLockConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Enables locking all sensitive properties. The sensitive properties are keyCredentials, passwordCredentials, and tokenEncryptionKeyId.
        self._all_properties: Optional[bool] = None
        # Locks the keyCredentials and passwordCredentials properties for modification where credential usage type is Sign.
        self._credentials_with_usage_sign: Optional[bool] = None
        # Locks the keyCredentials and passwordCredentials properties for modification where credential usage type is Verify. This locks OAuth service principals.
        self._credentials_with_usage_verify: Optional[bool] = None
        # Enables or disables service principal lock configuration. To allow the sensitive properties to be updated, update this property to false to disable the lock on the service principal.
        self._is_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Locks the tokenEncryptionKeyId property for modification on the service principal.
        self._token_encryption_key_id: Optional[bool] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def all_properties(self,) -> Optional[bool]:
        """
        Gets the allProperties property value. Enables locking all sensitive properties. The sensitive properties are keyCredentials, passwordCredentials, and tokenEncryptionKeyId.
        Returns: Optional[bool]
        """
        return self._all_properties
    
    @all_properties.setter
    def all_properties(self,value: Optional[bool] = None) -> None:
        """
        Sets the allProperties property value. Enables locking all sensitive properties. The sensitive properties are keyCredentials, passwordCredentials, and tokenEncryptionKeyId.
        Args:
            value: Value to set for the all_properties property.
        """
        self._all_properties = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServicePrincipalLockConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalLockConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServicePrincipalLockConfiguration()
    
    @property
    def credentials_with_usage_sign(self,) -> Optional[bool]:
        """
        Gets the credentialsWithUsageSign property value. Locks the keyCredentials and passwordCredentials properties for modification where credential usage type is Sign.
        Returns: Optional[bool]
        """
        return self._credentials_with_usage_sign
    
    @credentials_with_usage_sign.setter
    def credentials_with_usage_sign(self,value: Optional[bool] = None) -> None:
        """
        Sets the credentialsWithUsageSign property value. Locks the keyCredentials and passwordCredentials properties for modification where credential usage type is Sign.
        Args:
            value: Value to set for the credentials_with_usage_sign property.
        """
        self._credentials_with_usage_sign = value
    
    @property
    def credentials_with_usage_verify(self,) -> Optional[bool]:
        """
        Gets the credentialsWithUsageVerify property value. Locks the keyCredentials and passwordCredentials properties for modification where credential usage type is Verify. This locks OAuth service principals.
        Returns: Optional[bool]
        """
        return self._credentials_with_usage_verify
    
    @credentials_with_usage_verify.setter
    def credentials_with_usage_verify(self,value: Optional[bool] = None) -> None:
        """
        Sets the credentialsWithUsageVerify property value. Locks the keyCredentials and passwordCredentials properties for modification where credential usage type is Verify. This locks OAuth service principals.
        Args:
            value: Value to set for the credentials_with_usage_verify property.
        """
        self._credentials_with_usage_verify = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "allProperties": lambda n : setattr(self, 'all_properties', n.get_bool_value()),
            "credentialsWithUsageSign": lambda n : setattr(self, 'credentials_with_usage_sign', n.get_bool_value()),
            "credentialsWithUsageVerify": lambda n : setattr(self, 'credentials_with_usage_verify', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tokenEncryptionKeyId": lambda n : setattr(self, 'token_encryption_key_id', n.get_bool_value()),
        }
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Enables or disables service principal lock configuration. To allow the sensitive properties to be updated, update this property to false to disable the lock on the service principal.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Enables or disables service principal lock configuration. To allow the sensitive properties to be updated, update this property to false to disable the lock on the service principal.
        Args:
            value: Value to set for the is_enabled property.
        """
        self._is_enabled = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allProperties", self.all_properties)
        writer.write_bool_value("credentialsWithUsageSign", self.credentials_with_usage_sign)
        writer.write_bool_value("credentialsWithUsageVerify", self.credentials_with_usage_verify)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("tokenEncryptionKeyId", self.token_encryption_key_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def token_encryption_key_id(self,) -> Optional[bool]:
        """
        Gets the tokenEncryptionKeyId property value. Locks the tokenEncryptionKeyId property for modification on the service principal.
        Returns: Optional[bool]
        """
        return self._token_encryption_key_id
    
    @token_encryption_key_id.setter
    def token_encryption_key_id(self,value: Optional[bool] = None) -> None:
        """
        Sets the tokenEncryptionKeyId property value. Locks the tokenEncryptionKeyId property for modification on the service principal.
        Args:
            value: Value to set for the token_encryption_key_id property.
        """
        self._token_encryption_key_id = value
    

