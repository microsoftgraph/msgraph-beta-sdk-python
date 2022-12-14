from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
oath_token_metadata = lazy_import('msgraph.generated.models.oath_token_metadata')

class StrongAuthenticationPhoneAppDetail(entity.Entity):
    @property
    def authentication_type(self,) -> Optional[str]:
        """
        Gets the authenticationType property value. The authenticationType property
        Returns: Optional[str]
        """
        return self._authentication_type
    
    @authentication_type.setter
    def authentication_type(self,value: Optional[str] = None) -> None:
        """
        Sets the authenticationType property value. The authenticationType property
        Args:
            value: Value to set for the authenticationType property.
        """
        self._authentication_type = value
    
    @property
    def authenticator_flavor(self,) -> Optional[str]:
        """
        Gets the authenticatorFlavor property value. The authenticatorFlavor property
        Returns: Optional[str]
        """
        return self._authenticator_flavor
    
    @authenticator_flavor.setter
    def authenticator_flavor(self,value: Optional[str] = None) -> None:
        """
        Sets the authenticatorFlavor property value. The authenticatorFlavor property
        Args:
            value: Value to set for the authenticatorFlavor property.
        """
        self._authenticator_flavor = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new StrongAuthenticationPhoneAppDetail and sets the default values.
        """
        super().__init__()
        # The authenticationType property
        self._authentication_type: Optional[str] = None
        # The authenticatorFlavor property
        self._authenticator_flavor: Optional[str] = None
        # The deviceId property
        self._device_id: Optional[Guid] = None
        # The deviceName property
        self._device_name: Optional[str] = None
        # The deviceTag property
        self._device_tag: Optional[str] = None
        # The deviceToken property
        self._device_token: Optional[str] = None
        # The hashFunction property
        self._hash_function: Optional[str] = None
        # The lastAuthenticatedDateTime property
        self._last_authenticated_date_time: Optional[datetime] = None
        # The notificationType property
        self._notification_type: Optional[str] = None
        # The oathSecretKey property
        self._oath_secret_key: Optional[str] = None
        # The oathTokenMetadata property
        self._oath_token_metadata: Optional[oath_token_metadata.OathTokenMetadata] = None
        # The oathTokenTimeDriftInSeconds property
        self._oath_token_time_drift_in_seconds: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The phoneAppVersion property
        self._phone_app_version: Optional[str] = None
        # The tenantDeviceId property
        self._tenant_device_id: Optional[str] = None
        # The tokenGenerationIntervalInSeconds property
        self._token_generation_interval_in_seconds: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StrongAuthenticationPhoneAppDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: StrongAuthenticationPhoneAppDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return StrongAuthenticationPhoneAppDetail()
    
    @property
    def device_id(self,) -> Optional[Guid]:
        """
        Gets the deviceId property value. The deviceId property
        Returns: Optional[Guid]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the deviceId property value. The deviceId property
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The deviceName property
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The deviceName property
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def device_tag(self,) -> Optional[str]:
        """
        Gets the deviceTag property value. The deviceTag property
        Returns: Optional[str]
        """
        return self._device_tag
    
    @device_tag.setter
    def device_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceTag property value. The deviceTag property
        Args:
            value: Value to set for the deviceTag property.
        """
        self._device_tag = value
    
    @property
    def device_token(self,) -> Optional[str]:
        """
        Gets the deviceToken property value. The deviceToken property
        Returns: Optional[str]
        """
        return self._device_token
    
    @device_token.setter
    def device_token(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceToken property value. The deviceToken property
        Args:
            value: Value to set for the deviceToken property.
        """
        self._device_token = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_type": lambda n : setattr(self, 'authentication_type', n.get_str_value()),
            "authenticator_flavor": lambda n : setattr(self, 'authenticator_flavor', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_object_value(Guid)),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "device_tag": lambda n : setattr(self, 'device_tag', n.get_str_value()),
            "device_token": lambda n : setattr(self, 'device_token', n.get_str_value()),
            "hash_function": lambda n : setattr(self, 'hash_function', n.get_str_value()),
            "last_authenticated_date_time": lambda n : setattr(self, 'last_authenticated_date_time', n.get_datetime_value()),
            "notification_type": lambda n : setattr(self, 'notification_type', n.get_str_value()),
            "oath_secret_key": lambda n : setattr(self, 'oath_secret_key', n.get_str_value()),
            "oath_token_metadata": lambda n : setattr(self, 'oath_token_metadata', n.get_object_value(oath_token_metadata.OathTokenMetadata)),
            "oath_token_time_drift_in_seconds": lambda n : setattr(self, 'oath_token_time_drift_in_seconds', n.get_int_value()),
            "phone_app_version": lambda n : setattr(self, 'phone_app_version', n.get_str_value()),
            "tenant_device_id": lambda n : setattr(self, 'tenant_device_id', n.get_str_value()),
            "token_generation_interval_in_seconds": lambda n : setattr(self, 'token_generation_interval_in_seconds', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hash_function(self,) -> Optional[str]:
        """
        Gets the hashFunction property value. The hashFunction property
        Returns: Optional[str]
        """
        return self._hash_function
    
    @hash_function.setter
    def hash_function(self,value: Optional[str] = None) -> None:
        """
        Sets the hashFunction property value. The hashFunction property
        Args:
            value: Value to set for the hashFunction property.
        """
        self._hash_function = value
    
    @property
    def last_authenticated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastAuthenticatedDateTime property value. The lastAuthenticatedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_authenticated_date_time
    
    @last_authenticated_date_time.setter
    def last_authenticated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastAuthenticatedDateTime property value. The lastAuthenticatedDateTime property
        Args:
            value: Value to set for the lastAuthenticatedDateTime property.
        """
        self._last_authenticated_date_time = value
    
    @property
    def notification_type(self,) -> Optional[str]:
        """
        Gets the notificationType property value. The notificationType property
        Returns: Optional[str]
        """
        return self._notification_type
    
    @notification_type.setter
    def notification_type(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationType property value. The notificationType property
        Args:
            value: Value to set for the notificationType property.
        """
        self._notification_type = value
    
    @property
    def oath_secret_key(self,) -> Optional[str]:
        """
        Gets the oathSecretKey property value. The oathSecretKey property
        Returns: Optional[str]
        """
        return self._oath_secret_key
    
    @oath_secret_key.setter
    def oath_secret_key(self,value: Optional[str] = None) -> None:
        """
        Sets the oathSecretKey property value. The oathSecretKey property
        Args:
            value: Value to set for the oathSecretKey property.
        """
        self._oath_secret_key = value
    
    @property
    def oath_token_metadata(self,) -> Optional[oath_token_metadata.OathTokenMetadata]:
        """
        Gets the oathTokenMetadata property value. The oathTokenMetadata property
        Returns: Optional[oath_token_metadata.OathTokenMetadata]
        """
        return self._oath_token_metadata
    
    @oath_token_metadata.setter
    def oath_token_metadata(self,value: Optional[oath_token_metadata.OathTokenMetadata] = None) -> None:
        """
        Sets the oathTokenMetadata property value. The oathTokenMetadata property
        Args:
            value: Value to set for the oathTokenMetadata property.
        """
        self._oath_token_metadata = value
    
    @property
    def oath_token_time_drift_in_seconds(self,) -> Optional[int]:
        """
        Gets the oathTokenTimeDriftInSeconds property value. The oathTokenTimeDriftInSeconds property
        Returns: Optional[int]
        """
        return self._oath_token_time_drift_in_seconds
    
    @oath_token_time_drift_in_seconds.setter
    def oath_token_time_drift_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the oathTokenTimeDriftInSeconds property value. The oathTokenTimeDriftInSeconds property
        Args:
            value: Value to set for the oathTokenTimeDriftInSeconds property.
        """
        self._oath_token_time_drift_in_seconds = value
    
    @property
    def phone_app_version(self,) -> Optional[str]:
        """
        Gets the phoneAppVersion property value. The phoneAppVersion property
        Returns: Optional[str]
        """
        return self._phone_app_version
    
    @phone_app_version.setter
    def phone_app_version(self,value: Optional[str] = None) -> None:
        """
        Sets the phoneAppVersion property value. The phoneAppVersion property
        Args:
            value: Value to set for the phoneAppVersion property.
        """
        self._phone_app_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("authenticationType", self.authentication_type)
        writer.write_str_value("authenticatorFlavor", self.authenticator_flavor)
        writer.write_object_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("deviceTag", self.device_tag)
        writer.write_str_value("deviceToken", self.device_token)
        writer.write_str_value("hashFunction", self.hash_function)
        writer.write_datetime_value("lastAuthenticatedDateTime", self.last_authenticated_date_time)
        writer.write_str_value("notificationType", self.notification_type)
        writer.write_str_value("oathSecretKey", self.oath_secret_key)
        writer.write_object_value("oathTokenMetadata", self.oath_token_metadata)
        writer.write_int_value("oathTokenTimeDriftInSeconds", self.oath_token_time_drift_in_seconds)
        writer.write_str_value("phoneAppVersion", self.phone_app_version)
        writer.write_str_value("tenantDeviceId", self.tenant_device_id)
        writer.write_int_value("tokenGenerationIntervalInSeconds", self.token_generation_interval_in_seconds)
    
    @property
    def tenant_device_id(self,) -> Optional[str]:
        """
        Gets the tenantDeviceId property value. The tenantDeviceId property
        Returns: Optional[str]
        """
        return self._tenant_device_id
    
    @tenant_device_id.setter
    def tenant_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantDeviceId property value. The tenantDeviceId property
        Args:
            value: Value to set for the tenantDeviceId property.
        """
        self._tenant_device_id = value
    
    @property
    def token_generation_interval_in_seconds(self,) -> Optional[int]:
        """
        Gets the tokenGenerationIntervalInSeconds property value. The tokenGenerationIntervalInSeconds property
        Returns: Optional[int]
        """
        return self._token_generation_interval_in_seconds
    
    @token_generation_interval_in_seconds.setter
    def token_generation_interval_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the tokenGenerationIntervalInSeconds property value. The tokenGenerationIntervalInSeconds property
        Args:
            value: Value to set for the tokenGenerationIntervalInSeconds property.
        """
        self._token_generation_interval_in_seconds = value
    

