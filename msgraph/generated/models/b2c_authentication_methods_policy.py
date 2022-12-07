from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class B2cAuthenticationMethodsPolicy(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new B2cAuthenticationMethodsPolicy and sets the default values.
        """
        super().__init__()
        # The tenant admin can configure local accounts using email if the email and password authentication method is enabled.
        self._is_email_password_authentication_enabled: Optional[bool] = None
        # The tenant admin can configure local accounts using phone number if the phone number and one-time password authentication method is enabled.
        self._is_phone_one_time_password_authentication_enabled: Optional[bool] = None
        # The tenant admin can configure local accounts using username if the username and password authentication method is enabled.
        self._is_user_name_authentication_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> B2cAuthenticationMethodsPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: B2cAuthenticationMethodsPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return B2cAuthenticationMethodsPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_email_password_authentication_enabled": lambda n : setattr(self, 'is_email_password_authentication_enabled', n.get_bool_value()),
            "is_phone_one_time_password_authentication_enabled": lambda n : setattr(self, 'is_phone_one_time_password_authentication_enabled', n.get_bool_value()),
            "is_user_name_authentication_enabled": lambda n : setattr(self, 'is_user_name_authentication_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_email_password_authentication_enabled(self,) -> Optional[bool]:
        """
        Gets the isEmailPasswordAuthenticationEnabled property value. The tenant admin can configure local accounts using email if the email and password authentication method is enabled.
        Returns: Optional[bool]
        """
        return self._is_email_password_authentication_enabled
    
    @is_email_password_authentication_enabled.setter
    def is_email_password_authentication_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEmailPasswordAuthenticationEnabled property value. The tenant admin can configure local accounts using email if the email and password authentication method is enabled.
        Args:
            value: Value to set for the isEmailPasswordAuthenticationEnabled property.
        """
        self._is_email_password_authentication_enabled = value
    
    @property
    def is_phone_one_time_password_authentication_enabled(self,) -> Optional[bool]:
        """
        Gets the isPhoneOneTimePasswordAuthenticationEnabled property value. The tenant admin can configure local accounts using phone number if the phone number and one-time password authentication method is enabled.
        Returns: Optional[bool]
        """
        return self._is_phone_one_time_password_authentication_enabled
    
    @is_phone_one_time_password_authentication_enabled.setter
    def is_phone_one_time_password_authentication_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPhoneOneTimePasswordAuthenticationEnabled property value. The tenant admin can configure local accounts using phone number if the phone number and one-time password authentication method is enabled.
        Args:
            value: Value to set for the isPhoneOneTimePasswordAuthenticationEnabled property.
        """
        self._is_phone_one_time_password_authentication_enabled = value
    
    @property
    def is_user_name_authentication_enabled(self,) -> Optional[bool]:
        """
        Gets the isUserNameAuthenticationEnabled property value. The tenant admin can configure local accounts using username if the username and password authentication method is enabled.
        Returns: Optional[bool]
        """
        return self._is_user_name_authentication_enabled
    
    @is_user_name_authentication_enabled.setter
    def is_user_name_authentication_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isUserNameAuthenticationEnabled property value. The tenant admin can configure local accounts using username if the username and password authentication method is enabled.
        Args:
            value: Value to set for the isUserNameAuthenticationEnabled property.
        """
        self._is_user_name_authentication_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isEmailPasswordAuthenticationEnabled", self.is_email_password_authentication_enabled)
        writer.write_bool_value("isPhoneOneTimePasswordAuthenticationEnabled", self.is_phone_one_time_password_authentication_enabled)
        writer.write_bool_value("isUserNameAuthenticationEnabled", self.is_user_name_authentication_enabled)
    

