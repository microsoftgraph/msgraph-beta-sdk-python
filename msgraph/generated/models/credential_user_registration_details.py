from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
registration_auth_method = lazy_import('msgraph.generated.models.registration_auth_method')

class CredentialUserRegistrationDetails(entity.Entity):
    @property
    def auth_methods(self,) -> Optional[List[registration_auth_method.RegistrationAuthMethod]]:
        """
        Gets the authMethods property value. Represents the authentication method that the user has registered. Possible values are: email, mobilePhone, officePhone,  securityQuestion (only used for self-service password reset), appNotification,  appCode, alternateMobilePhone (supported only in registration),  fido,  appPassword,  unknownFutureValue.
        Returns: Optional[List[registration_auth_method.RegistrationAuthMethod]]
        """
        return self._auth_methods
    
    @auth_methods.setter
    def auth_methods(self,value: Optional[List[registration_auth_method.RegistrationAuthMethod]] = None) -> None:
        """
        Sets the authMethods property value. Represents the authentication method that the user has registered. Possible values are: email, mobilePhone, officePhone,  securityQuestion (only used for self-service password reset), appNotification,  appCode, alternateMobilePhone (supported only in registration),  fido,  appPassword,  unknownFutureValue.
        Args:
            value: Value to set for the authMethods property.
        """
        self._auth_methods = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CredentialUserRegistrationDetails and sets the default values.
        """
        super().__init__()
        # Represents the authentication method that the user has registered. Possible values are: email, mobilePhone, officePhone,  securityQuestion (only used for self-service password reset), appNotification,  appCode, alternateMobilePhone (supported only in registration),  fido,  appPassword,  unknownFutureValue.
        self._auth_methods: Optional[List[registration_auth_method.RegistrationAuthMethod]] = None
        # Indicates whether the user is ready to perform self-service password reset or MFA.
        self._is_capable: Optional[bool] = None
        # Indicates whether the user enabled to perform self-service password reset.
        self._is_enabled: Optional[bool] = None
        # Indicates whether the user is registered for MFA.
        self._is_mfa_registered: Optional[bool] = None
        # Indicates whether the user has registered any authentication methods for self-service password reset.
        self._is_registered: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Provides the user name of the corresponding user.
        self._user_display_name: Optional[str] = None
        # Provides the user principal name of the corresponding user.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CredentialUserRegistrationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CredentialUserRegistrationDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CredentialUserRegistrationDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "auth_methods": lambda n : setattr(self, 'auth_methods', n.get_collection_of_enum_values(registration_auth_method.RegistrationAuthMethod)),
            "is_capable": lambda n : setattr(self, 'is_capable', n.get_bool_value()),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "is_mfa_registered": lambda n : setattr(self, 'is_mfa_registered', n.get_bool_value()),
            "is_registered": lambda n : setattr(self, 'is_registered', n.get_bool_value()),
            "user_display_name": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_capable(self,) -> Optional[bool]:
        """
        Gets the isCapable property value. Indicates whether the user is ready to perform self-service password reset or MFA.
        Returns: Optional[bool]
        """
        return self._is_capable
    
    @is_capable.setter
    def is_capable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCapable property value. Indicates whether the user is ready to perform self-service password reset or MFA.
        Args:
            value: Value to set for the isCapable property.
        """
        self._is_capable = value
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Indicates whether the user enabled to perform self-service password reset.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Indicates whether the user enabled to perform self-service password reset.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    @property
    def is_mfa_registered(self,) -> Optional[bool]:
        """
        Gets the isMfaRegistered property value. Indicates whether the user is registered for MFA.
        Returns: Optional[bool]
        """
        return self._is_mfa_registered
    
    @is_mfa_registered.setter
    def is_mfa_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMfaRegistered property value. Indicates whether the user is registered for MFA.
        Args:
            value: Value to set for the isMfaRegistered property.
        """
        self._is_mfa_registered = value
    
    @property
    def is_registered(self,) -> Optional[bool]:
        """
        Gets the isRegistered property value. Indicates whether the user has registered any authentication methods for self-service password reset.
        Returns: Optional[bool]
        """
        return self._is_registered
    
    @is_registered.setter
    def is_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRegistered property value. Indicates whether the user has registered any authentication methods for self-service password reset.
        Args:
            value: Value to set for the isRegistered property.
        """
        self._is_registered = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("authMethods", self.auth_methods)
        writer.write_bool_value("isCapable", self.is_capable)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("isMfaRegistered", self.is_mfa_registered)
        writer.write_bool_value("isRegistered", self.is_registered)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. Provides the user name of the corresponding user.
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. Provides the user name of the corresponding user.
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. Provides the user principal name of the corresponding user.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. Provides the user principal name of the corresponding user.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

