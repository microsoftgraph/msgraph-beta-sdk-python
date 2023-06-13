from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method, email_authentication_method, entity, fido2_authentication_method, long_running_operation, microsoft_authenticator_authentication_method, passwordless_microsoft_authenticator_authentication_method, password_authentication_method, phone_authentication_method, sign_in_preferences, software_oath_authentication_method, temporary_access_pass_authentication_method, windows_hello_for_business_authentication_method

from . import entity

@dataclass
class Authentication(entity.Entity):
    # Represents the email addresses registered to a user for authentication.
    email_methods: Optional[List[email_authentication_method.EmailAuthenticationMethod]] = None
    # Represents the FIDO2 security keys registered to a user for authentication.
    fido2_methods: Optional[List[fido2_authentication_method.Fido2AuthenticationMethod]] = None
    # Represents all authentication methods registered to a user.
    methods: Optional[List[authentication_method.AuthenticationMethod]] = None
    # The details of the Microsoft Authenticator app registered to a user for authentication.
    microsoft_authenticator_methods: Optional[List[microsoft_authenticator_authentication_method.MicrosoftAuthenticatorAuthenticationMethod]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operations property
    operations: Optional[List[long_running_operation.LongRunningOperation]] = None
    # Represents the details of the password authentication method registered to a user for authentication.
    password_methods: Optional[List[password_authentication_method.PasswordAuthenticationMethod]] = None
    # Represents the Microsoft Authenticator Passwordless Phone Sign-in methods registered to a user for authentication.
    passwordless_microsoft_authenticator_methods: Optional[List[passwordless_microsoft_authenticator_authentication_method.PasswordlessMicrosoftAuthenticatorAuthenticationMethod]] = None
    # Represents the phone registered to a user for authentication.
    phone_methods: Optional[List[phone_authentication_method.PhoneAuthenticationMethod]] = None
    # The settings and preferences for to the sign-in experience of a user.
    sign_in_preferences: Optional[sign_in_preferences.SignInPreferences] = None
    # The softwareOathMethods property
    software_oath_methods: Optional[List[software_oath_authentication_method.SoftwareOathAuthenticationMethod]] = None
    # Represents a Temporary Access Pass registered to a user for authentication through time-limited passcodes.
    temporary_access_pass_methods: Optional[List[temporary_access_pass_authentication_method.TemporaryAccessPassAuthenticationMethod]] = None
    # Represents the Windows Hello for Business authentication method registered to a user for authentication.
    windows_hello_for_business_methods: Optional[List[windows_hello_for_business_authentication_method.WindowsHelloForBusinessAuthenticationMethod]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Authentication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Authentication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Authentication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method, email_authentication_method, entity, fido2_authentication_method, long_running_operation, microsoft_authenticator_authentication_method, passwordless_microsoft_authenticator_authentication_method, password_authentication_method, phone_authentication_method, sign_in_preferences, software_oath_authentication_method, temporary_access_pass_authentication_method, windows_hello_for_business_authentication_method

        fields: Dict[str, Callable[[Any], None]] = {
            "emailMethods": lambda n : setattr(self, 'email_methods', n.get_collection_of_object_values(email_authentication_method.EmailAuthenticationMethod)),
            "fido2Methods": lambda n : setattr(self, 'fido2_methods', n.get_collection_of_object_values(fido2_authentication_method.Fido2AuthenticationMethod)),
            "methods": lambda n : setattr(self, 'methods', n.get_collection_of_object_values(authentication_method.AuthenticationMethod)),
            "microsoftAuthenticatorMethods": lambda n : setattr(self, 'microsoft_authenticator_methods', n.get_collection_of_object_values(microsoft_authenticator_authentication_method.MicrosoftAuthenticatorAuthenticationMethod)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(long_running_operation.LongRunningOperation)),
            "passwordlessMicrosoftAuthenticatorMethods": lambda n : setattr(self, 'passwordless_microsoft_authenticator_methods', n.get_collection_of_object_values(passwordless_microsoft_authenticator_authentication_method.PasswordlessMicrosoftAuthenticatorAuthenticationMethod)),
            "passwordMethods": lambda n : setattr(self, 'password_methods', n.get_collection_of_object_values(password_authentication_method.PasswordAuthenticationMethod)),
            "phoneMethods": lambda n : setattr(self, 'phone_methods', n.get_collection_of_object_values(phone_authentication_method.PhoneAuthenticationMethod)),
            "signInPreferences": lambda n : setattr(self, 'sign_in_preferences', n.get_object_value(sign_in_preferences.SignInPreferences)),
            "softwareOathMethods": lambda n : setattr(self, 'software_oath_methods', n.get_collection_of_object_values(software_oath_authentication_method.SoftwareOathAuthenticationMethod)),
            "temporaryAccessPassMethods": lambda n : setattr(self, 'temporary_access_pass_methods', n.get_collection_of_object_values(temporary_access_pass_authentication_method.TemporaryAccessPassAuthenticationMethod)),
            "windowsHelloForBusinessMethods": lambda n : setattr(self, 'windows_hello_for_business_methods', n.get_collection_of_object_values(windows_hello_for_business_authentication_method.WindowsHelloForBusinessAuthenticationMethod)),
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
        writer.write_collection_of_object_values("emailMethods", self.email_methods)
        writer.write_collection_of_object_values("fido2Methods", self.fido2_methods)
        writer.write_collection_of_object_values("methods", self.methods)
        writer.write_collection_of_object_values("microsoftAuthenticatorMethods", self.microsoft_authenticator_methods)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("passwordlessMicrosoftAuthenticatorMethods", self.passwordless_microsoft_authenticator_methods)
        writer.write_collection_of_object_values("passwordMethods", self.password_methods)
        writer.write_collection_of_object_values("phoneMethods", self.phone_methods)
        writer.write_object_value("signInPreferences", self.sign_in_preferences)
        writer.write_collection_of_object_values("softwareOathMethods", self.software_oath_methods)
        writer.write_collection_of_object_values("temporaryAccessPassMethods", self.temporary_access_pass_methods)
        writer.write_collection_of_object_values("windowsHelloForBusinessMethods", self.windows_hello_for_business_methods)
    

