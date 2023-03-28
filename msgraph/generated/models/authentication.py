from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method, email_authentication_method, entity, fido2_authentication_method, long_running_operation, microsoft_authenticator_authentication_method, passwordless_microsoft_authenticator_authentication_method, password_authentication_method, phone_authentication_method, software_oath_authentication_method, temporary_access_pass_authentication_method, windows_hello_for_business_authentication_method

from . import entity

class Authentication(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new authentication and sets the default values.
        """
        super().__init__()
        # Represents the email addresses registered to a user for authentication.
        self._email_methods: Optional[List[email_authentication_method.EmailAuthenticationMethod]] = None
        # Represents the FIDO2 security keys registered to a user for authentication.
        self._fido2_methods: Optional[List[fido2_authentication_method.Fido2AuthenticationMethod]] = None
        # Represents all authentication methods registered to a user.
        self._methods: Optional[List[authentication_method.AuthenticationMethod]] = None
        # The details of the Microsoft Authenticator app registered to a user for authentication.
        self._microsoft_authenticator_methods: Optional[List[microsoft_authenticator_authentication_method.MicrosoftAuthenticatorAuthenticationMethod]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The operations property
        self._operations: Optional[List[long_running_operation.LongRunningOperation]] = None
        # Represents the details of the password authentication method registered to a user for authentication.
        self._password_methods: Optional[List[password_authentication_method.PasswordAuthenticationMethod]] = None
        # Represents the Microsoft Authenticator Passwordless Phone Sign-in methods registered to a user for authentication.
        self._passwordless_microsoft_authenticator_methods: Optional[List[passwordless_microsoft_authenticator_authentication_method.PasswordlessMicrosoftAuthenticatorAuthenticationMethod]] = None
        # Represents the phone registered to a user for authentication.
        self._phone_methods: Optional[List[phone_authentication_method.PhoneAuthenticationMethod]] = None
        # The softwareOathMethods property
        self._software_oath_methods: Optional[List[software_oath_authentication_method.SoftwareOathAuthenticationMethod]] = None
        # Represents a Temporary Access Pass registered to a user for authentication through time-limited passcodes.
        self._temporary_access_pass_methods: Optional[List[temporary_access_pass_authentication_method.TemporaryAccessPassAuthenticationMethod]] = None
        # Represents the Windows Hello for Business authentication method registered to a user for authentication.
        self._windows_hello_for_business_methods: Optional[List[windows_hello_for_business_authentication_method.WindowsHelloForBusinessAuthenticationMethod]] = None
    
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
    
    @property
    def email_methods(self,) -> Optional[List[email_authentication_method.EmailAuthenticationMethod]]:
        """
        Gets the emailMethods property value. Represents the email addresses registered to a user for authentication.
        Returns: Optional[List[email_authentication_method.EmailAuthenticationMethod]]
        """
        return self._email_methods
    
    @email_methods.setter
    def email_methods(self,value: Optional[List[email_authentication_method.EmailAuthenticationMethod]] = None) -> None:
        """
        Sets the emailMethods property value. Represents the email addresses registered to a user for authentication.
        Args:
            value: Value to set for the email_methods property.
        """
        self._email_methods = value
    
    @property
    def fido2_methods(self,) -> Optional[List[fido2_authentication_method.Fido2AuthenticationMethod]]:
        """
        Gets the fido2Methods property value. Represents the FIDO2 security keys registered to a user for authentication.
        Returns: Optional[List[fido2_authentication_method.Fido2AuthenticationMethod]]
        """
        return self._fido2_methods
    
    @fido2_methods.setter
    def fido2_methods(self,value: Optional[List[fido2_authentication_method.Fido2AuthenticationMethod]] = None) -> None:
        """
        Sets the fido2Methods property value. Represents the FIDO2 security keys registered to a user for authentication.
        Args:
            value: Value to set for the fido2_methods property.
        """
        self._fido2_methods = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method, email_authentication_method, entity, fido2_authentication_method, long_running_operation, microsoft_authenticator_authentication_method, passwordless_microsoft_authenticator_authentication_method, password_authentication_method, phone_authentication_method, software_oath_authentication_method, temporary_access_pass_authentication_method, windows_hello_for_business_authentication_method

        fields: Dict[str, Callable[[Any], None]] = {
            "emailMethods": lambda n : setattr(self, 'email_methods', n.get_collection_of_object_values(email_authentication_method.EmailAuthenticationMethod)),
            "fido2Methods": lambda n : setattr(self, 'fido2_methods', n.get_collection_of_object_values(fido2_authentication_method.Fido2AuthenticationMethod)),
            "methods": lambda n : setattr(self, 'methods', n.get_collection_of_object_values(authentication_method.AuthenticationMethod)),
            "microsoftAuthenticatorMethods": lambda n : setattr(self, 'microsoft_authenticator_methods', n.get_collection_of_object_values(microsoft_authenticator_authentication_method.MicrosoftAuthenticatorAuthenticationMethod)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(long_running_operation.LongRunningOperation)),
            "passwordlessMicrosoftAuthenticatorMethods": lambda n : setattr(self, 'passwordless_microsoft_authenticator_methods', n.get_collection_of_object_values(passwordless_microsoft_authenticator_authentication_method.PasswordlessMicrosoftAuthenticatorAuthenticationMethod)),
            "passwordMethods": lambda n : setattr(self, 'password_methods', n.get_collection_of_object_values(password_authentication_method.PasswordAuthenticationMethod)),
            "phoneMethods": lambda n : setattr(self, 'phone_methods', n.get_collection_of_object_values(phone_authentication_method.PhoneAuthenticationMethod)),
            "softwareOathMethods": lambda n : setattr(self, 'software_oath_methods', n.get_collection_of_object_values(software_oath_authentication_method.SoftwareOathAuthenticationMethod)),
            "temporaryAccessPassMethods": lambda n : setattr(self, 'temporary_access_pass_methods', n.get_collection_of_object_values(temporary_access_pass_authentication_method.TemporaryAccessPassAuthenticationMethod)),
            "windowsHelloForBusinessMethods": lambda n : setattr(self, 'windows_hello_for_business_methods', n.get_collection_of_object_values(windows_hello_for_business_authentication_method.WindowsHelloForBusinessAuthenticationMethod)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def methods(self,) -> Optional[List[authentication_method.AuthenticationMethod]]:
        """
        Gets the methods property value. Represents all authentication methods registered to a user.
        Returns: Optional[List[authentication_method.AuthenticationMethod]]
        """
        return self._methods
    
    @methods.setter
    def methods(self,value: Optional[List[authentication_method.AuthenticationMethod]] = None) -> None:
        """
        Sets the methods property value. Represents all authentication methods registered to a user.
        Args:
            value: Value to set for the methods property.
        """
        self._methods = value
    
    @property
    def microsoft_authenticator_methods(self,) -> Optional[List[microsoft_authenticator_authentication_method.MicrosoftAuthenticatorAuthenticationMethod]]:
        """
        Gets the microsoftAuthenticatorMethods property value. The details of the Microsoft Authenticator app registered to a user for authentication.
        Returns: Optional[List[microsoft_authenticator_authentication_method.MicrosoftAuthenticatorAuthenticationMethod]]
        """
        return self._microsoft_authenticator_methods
    
    @microsoft_authenticator_methods.setter
    def microsoft_authenticator_methods(self,value: Optional[List[microsoft_authenticator_authentication_method.MicrosoftAuthenticatorAuthenticationMethod]] = None) -> None:
        """
        Sets the microsoftAuthenticatorMethods property value. The details of the Microsoft Authenticator app registered to a user for authentication.
        Args:
            value: Value to set for the microsoft_authenticator_methods property.
        """
        self._microsoft_authenticator_methods = value
    
    @property
    def operations(self,) -> Optional[List[long_running_operation.LongRunningOperation]]:
        """
        Gets the operations property value. The operations property
        Returns: Optional[List[long_running_operation.LongRunningOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[long_running_operation.LongRunningOperation]] = None) -> None:
        """
        Sets the operations property value. The operations property
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def password_methods(self,) -> Optional[List[password_authentication_method.PasswordAuthenticationMethod]]:
        """
        Gets the passwordMethods property value. Represents the details of the password authentication method registered to a user for authentication.
        Returns: Optional[List[password_authentication_method.PasswordAuthenticationMethod]]
        """
        return self._password_methods
    
    @password_methods.setter
    def password_methods(self,value: Optional[List[password_authentication_method.PasswordAuthenticationMethod]] = None) -> None:
        """
        Sets the passwordMethods property value. Represents the details of the password authentication method registered to a user for authentication.
        Args:
            value: Value to set for the password_methods property.
        """
        self._password_methods = value
    
    @property
    def passwordless_microsoft_authenticator_methods(self,) -> Optional[List[passwordless_microsoft_authenticator_authentication_method.PasswordlessMicrosoftAuthenticatorAuthenticationMethod]]:
        """
        Gets the passwordlessMicrosoftAuthenticatorMethods property value. Represents the Microsoft Authenticator Passwordless Phone Sign-in methods registered to a user for authentication.
        Returns: Optional[List[passwordless_microsoft_authenticator_authentication_method.PasswordlessMicrosoftAuthenticatorAuthenticationMethod]]
        """
        return self._passwordless_microsoft_authenticator_methods
    
    @passwordless_microsoft_authenticator_methods.setter
    def passwordless_microsoft_authenticator_methods(self,value: Optional[List[passwordless_microsoft_authenticator_authentication_method.PasswordlessMicrosoftAuthenticatorAuthenticationMethod]] = None) -> None:
        """
        Sets the passwordlessMicrosoftAuthenticatorMethods property value. Represents the Microsoft Authenticator Passwordless Phone Sign-in methods registered to a user for authentication.
        Args:
            value: Value to set for the passwordless_microsoft_authenticator_methods property.
        """
        self._passwordless_microsoft_authenticator_methods = value
    
    @property
    def phone_methods(self,) -> Optional[List[phone_authentication_method.PhoneAuthenticationMethod]]:
        """
        Gets the phoneMethods property value. Represents the phone registered to a user for authentication.
        Returns: Optional[List[phone_authentication_method.PhoneAuthenticationMethod]]
        """
        return self._phone_methods
    
    @phone_methods.setter
    def phone_methods(self,value: Optional[List[phone_authentication_method.PhoneAuthenticationMethod]] = None) -> None:
        """
        Sets the phoneMethods property value. Represents the phone registered to a user for authentication.
        Args:
            value: Value to set for the phone_methods property.
        """
        self._phone_methods = value
    
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
        writer.write_collection_of_object_values("softwareOathMethods", self.software_oath_methods)
        writer.write_collection_of_object_values("temporaryAccessPassMethods", self.temporary_access_pass_methods)
        writer.write_collection_of_object_values("windowsHelloForBusinessMethods", self.windows_hello_for_business_methods)
    
    @property
    def software_oath_methods(self,) -> Optional[List[software_oath_authentication_method.SoftwareOathAuthenticationMethod]]:
        """
        Gets the softwareOathMethods property value. The softwareOathMethods property
        Returns: Optional[List[software_oath_authentication_method.SoftwareOathAuthenticationMethod]]
        """
        return self._software_oath_methods
    
    @software_oath_methods.setter
    def software_oath_methods(self,value: Optional[List[software_oath_authentication_method.SoftwareOathAuthenticationMethod]] = None) -> None:
        """
        Sets the softwareOathMethods property value. The softwareOathMethods property
        Args:
            value: Value to set for the software_oath_methods property.
        """
        self._software_oath_methods = value
    
    @property
    def temporary_access_pass_methods(self,) -> Optional[List[temporary_access_pass_authentication_method.TemporaryAccessPassAuthenticationMethod]]:
        """
        Gets the temporaryAccessPassMethods property value. Represents a Temporary Access Pass registered to a user for authentication through time-limited passcodes.
        Returns: Optional[List[temporary_access_pass_authentication_method.TemporaryAccessPassAuthenticationMethod]]
        """
        return self._temporary_access_pass_methods
    
    @temporary_access_pass_methods.setter
    def temporary_access_pass_methods(self,value: Optional[List[temporary_access_pass_authentication_method.TemporaryAccessPassAuthenticationMethod]] = None) -> None:
        """
        Sets the temporaryAccessPassMethods property value. Represents a Temporary Access Pass registered to a user for authentication through time-limited passcodes.
        Args:
            value: Value to set for the temporary_access_pass_methods property.
        """
        self._temporary_access_pass_methods = value
    
    @property
    def windows_hello_for_business_methods(self,) -> Optional[List[windows_hello_for_business_authentication_method.WindowsHelloForBusinessAuthenticationMethod]]:
        """
        Gets the windowsHelloForBusinessMethods property value. Represents the Windows Hello for Business authentication method registered to a user for authentication.
        Returns: Optional[List[windows_hello_for_business_authentication_method.WindowsHelloForBusinessAuthenticationMethod]]
        """
        return self._windows_hello_for_business_methods
    
    @windows_hello_for_business_methods.setter
    def windows_hello_for_business_methods(self,value: Optional[List[windows_hello_for_business_authentication_method.WindowsHelloForBusinessAuthenticationMethod]] = None) -> None:
        """
        Sets the windowsHelloForBusinessMethods property value. Represents the Windows Hello for Business authentication method registered to a user for authentication.
        Args:
            value: Value to set for the windows_hello_for_business_methods property.
        """
        self._windows_hello_for_business_methods = value
    

