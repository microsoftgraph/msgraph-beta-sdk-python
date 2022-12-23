from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

default_mfa_method_type = lazy_import('msgraph.generated.models.default_mfa_method_type')
entity = lazy_import('msgraph.generated.models.entity')
sign_in_user_type = lazy_import('msgraph.generated.models.sign_in_user_type')

class UserRegistrationDetails(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new userRegistrationDetails and sets the default values.
        """
        super().__init__()
        # The method the user or admin selected as default for performing multi-factor authentication for the user. The possible values are: none, mobilePhone, alternateMobilePhone, officePhone, microsoftAuthenticatorPush, softwareOneTimePasscode, unknownFutureValue.
        self._default_mfa_method: Optional[default_mfa_method_type.DefaultMfaMethodType] = None
        # Whether the user has an admin role in the tenant. This value can be used to check the authentication methods that privileged accounts are registered for and capable of.
        self._is_admin: Optional[bool] = None
        # Whether the user has registered a strong authentication method for multi-factor authentication. The method must be allowed by the authentication methods policy. Supports $filter (eq).
        self._is_mfa_capable: Optional[bool] = None
        # Whether the user has registered a strong authentication method for multi-factor authentication. The method may not necessarily be allowed by the authentication methods policy.  Supports $filter (eq).
        self._is_mfa_registered: Optional[bool] = None
        # Whether the user has registered a passwordless strong authentication method (including FIDO2, Windows Hello for Business, and Microsoft Authenticator (Passwordless)) that is allowed by the authentication methods policy. Supports $filter (eq).
        self._is_passwordless_capable: Optional[bool] = None
        # Whether the user has registered the required number of authentication methods for self-service password reset and the user is allowed to perform self-service password reset by policy. Supports $filter (eq).
        self._is_sspr_capable: Optional[bool] = None
        # Whether the user is allowed to perform self-service password reset by policy. The user may not necessarily have registered the required number of authentication methods for self-service password reset. Supports $filter (eq).
        self._is_sspr_enabled: Optional[bool] = None
        # Whether the user has registered the required number of authentication methods for self-service password reset. The user may not necessarily be allowed to perform self-service password reset by policy. Supports $filter (eq).
        self._is_sspr_registered: Optional[bool] = None
        # Collection of authentication methods registered, such as mobilePhone, email, fido2. Supports $filter (any with eq).
        self._methods_registered: Optional[List[str]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user display name, such as Adele Vance. Supports $filter (eq, startsWith) and $orderBy.
        self._user_display_name: Optional[str] = None
        # The user principal name, such as AdeleV@contoso.com. Supports $filter (eq, startsWith) and $orderBy.
        self._user_principal_name: Optional[str] = None
        # Identifies whether the user is a member or guest in the tenant. The possible values are: member, guest, unknownFutureValue.
        self._user_type: Optional[sign_in_user_type.SignInUserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserRegistrationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserRegistrationDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserRegistrationDetails()
    
    @property
    def default_mfa_method(self,) -> Optional[default_mfa_method_type.DefaultMfaMethodType]:
        """
        Gets the defaultMfaMethod property value. The method the user or admin selected as default for performing multi-factor authentication for the user. The possible values are: none, mobilePhone, alternateMobilePhone, officePhone, microsoftAuthenticatorPush, softwareOneTimePasscode, unknownFutureValue.
        Returns: Optional[default_mfa_method_type.DefaultMfaMethodType]
        """
        return self._default_mfa_method
    
    @default_mfa_method.setter
    def default_mfa_method(self,value: Optional[default_mfa_method_type.DefaultMfaMethodType] = None) -> None:
        """
        Sets the defaultMfaMethod property value. The method the user or admin selected as default for performing multi-factor authentication for the user. The possible values are: none, mobilePhone, alternateMobilePhone, officePhone, microsoftAuthenticatorPush, softwareOneTimePasscode, unknownFutureValue.
        Args:
            value: Value to set for the defaultMfaMethod property.
        """
        self._default_mfa_method = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_mfa_method": lambda n : setattr(self, 'default_mfa_method', n.get_enum_value(default_mfa_method_type.DefaultMfaMethodType)),
            "is_admin": lambda n : setattr(self, 'is_admin', n.get_bool_value()),
            "is_mfa_capable": lambda n : setattr(self, 'is_mfa_capable', n.get_bool_value()),
            "is_mfa_registered": lambda n : setattr(self, 'is_mfa_registered', n.get_bool_value()),
            "is_passwordless_capable": lambda n : setattr(self, 'is_passwordless_capable', n.get_bool_value()),
            "is_sspr_capable": lambda n : setattr(self, 'is_sspr_capable', n.get_bool_value()),
            "is_sspr_enabled": lambda n : setattr(self, 'is_sspr_enabled', n.get_bool_value()),
            "is_sspr_registered": lambda n : setattr(self, 'is_sspr_registered', n.get_bool_value()),
            "methods_registered": lambda n : setattr(self, 'methods_registered', n.get_collection_of_primitive_values(str)),
            "user_display_name": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "user_type": lambda n : setattr(self, 'user_type', n.get_enum_value(sign_in_user_type.SignInUserType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_admin(self,) -> Optional[bool]:
        """
        Gets the isAdmin property value. Whether the user has an admin role in the tenant. This value can be used to check the authentication methods that privileged accounts are registered for and capable of.
        Returns: Optional[bool]
        """
        return self._is_admin
    
    @is_admin.setter
    def is_admin(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAdmin property value. Whether the user has an admin role in the tenant. This value can be used to check the authentication methods that privileged accounts are registered for and capable of.
        Args:
            value: Value to set for the isAdmin property.
        """
        self._is_admin = value
    
    @property
    def is_mfa_capable(self,) -> Optional[bool]:
        """
        Gets the isMfaCapable property value. Whether the user has registered a strong authentication method for multi-factor authentication. The method must be allowed by the authentication methods policy. Supports $filter (eq).
        Returns: Optional[bool]
        """
        return self._is_mfa_capable
    
    @is_mfa_capable.setter
    def is_mfa_capable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMfaCapable property value. Whether the user has registered a strong authentication method for multi-factor authentication. The method must be allowed by the authentication methods policy. Supports $filter (eq).
        Args:
            value: Value to set for the isMfaCapable property.
        """
        self._is_mfa_capable = value
    
    @property
    def is_mfa_registered(self,) -> Optional[bool]:
        """
        Gets the isMfaRegistered property value. Whether the user has registered a strong authentication method for multi-factor authentication. The method may not necessarily be allowed by the authentication methods policy.  Supports $filter (eq).
        Returns: Optional[bool]
        """
        return self._is_mfa_registered
    
    @is_mfa_registered.setter
    def is_mfa_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMfaRegistered property value. Whether the user has registered a strong authentication method for multi-factor authentication. The method may not necessarily be allowed by the authentication methods policy.  Supports $filter (eq).
        Args:
            value: Value to set for the isMfaRegistered property.
        """
        self._is_mfa_registered = value
    
    @property
    def is_passwordless_capable(self,) -> Optional[bool]:
        """
        Gets the isPasswordlessCapable property value. Whether the user has registered a passwordless strong authentication method (including FIDO2, Windows Hello for Business, and Microsoft Authenticator (Passwordless)) that is allowed by the authentication methods policy. Supports $filter (eq).
        Returns: Optional[bool]
        """
        return self._is_passwordless_capable
    
    @is_passwordless_capable.setter
    def is_passwordless_capable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPasswordlessCapable property value. Whether the user has registered a passwordless strong authentication method (including FIDO2, Windows Hello for Business, and Microsoft Authenticator (Passwordless)) that is allowed by the authentication methods policy. Supports $filter (eq).
        Args:
            value: Value to set for the isPasswordlessCapable property.
        """
        self._is_passwordless_capable = value
    
    @property
    def is_sspr_capable(self,) -> Optional[bool]:
        """
        Gets the isSsprCapable property value. Whether the user has registered the required number of authentication methods for self-service password reset and the user is allowed to perform self-service password reset by policy. Supports $filter (eq).
        Returns: Optional[bool]
        """
        return self._is_sspr_capable
    
    @is_sspr_capable.setter
    def is_sspr_capable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSsprCapable property value. Whether the user has registered the required number of authentication methods for self-service password reset and the user is allowed to perform self-service password reset by policy. Supports $filter (eq).
        Args:
            value: Value to set for the isSsprCapable property.
        """
        self._is_sspr_capable = value
    
    @property
    def is_sspr_enabled(self,) -> Optional[bool]:
        """
        Gets the isSsprEnabled property value. Whether the user is allowed to perform self-service password reset by policy. The user may not necessarily have registered the required number of authentication methods for self-service password reset. Supports $filter (eq).
        Returns: Optional[bool]
        """
        return self._is_sspr_enabled
    
    @is_sspr_enabled.setter
    def is_sspr_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSsprEnabled property value. Whether the user is allowed to perform self-service password reset by policy. The user may not necessarily have registered the required number of authentication methods for self-service password reset. Supports $filter (eq).
        Args:
            value: Value to set for the isSsprEnabled property.
        """
        self._is_sspr_enabled = value
    
    @property
    def is_sspr_registered(self,) -> Optional[bool]:
        """
        Gets the isSsprRegistered property value. Whether the user has registered the required number of authentication methods for self-service password reset. The user may not necessarily be allowed to perform self-service password reset by policy. Supports $filter (eq).
        Returns: Optional[bool]
        """
        return self._is_sspr_registered
    
    @is_sspr_registered.setter
    def is_sspr_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSsprRegistered property value. Whether the user has registered the required number of authentication methods for self-service password reset. The user may not necessarily be allowed to perform self-service password reset by policy. Supports $filter (eq).
        Args:
            value: Value to set for the isSsprRegistered property.
        """
        self._is_sspr_registered = value
    
    @property
    def methods_registered(self,) -> Optional[List[str]]:
        """
        Gets the methodsRegistered property value. Collection of authentication methods registered, such as mobilePhone, email, fido2. Supports $filter (any with eq).
        Returns: Optional[List[str]]
        """
        return self._methods_registered
    
    @methods_registered.setter
    def methods_registered(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the methodsRegistered property value. Collection of authentication methods registered, such as mobilePhone, email, fido2. Supports $filter (any with eq).
        Args:
            value: Value to set for the methodsRegistered property.
        """
        self._methods_registered = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("defaultMfaMethod", self.default_mfa_method)
        writer.write_bool_value("isAdmin", self.is_admin)
        writer.write_bool_value("isMfaCapable", self.is_mfa_capable)
        writer.write_bool_value("isMfaRegistered", self.is_mfa_registered)
        writer.write_bool_value("isPasswordlessCapable", self.is_passwordless_capable)
        writer.write_bool_value("isSsprCapable", self.is_sspr_capable)
        writer.write_bool_value("isSsprEnabled", self.is_sspr_enabled)
        writer.write_bool_value("isSsprRegistered", self.is_sspr_registered)
        writer.write_collection_of_primitive_values("methodsRegistered", self.methods_registered)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_enum_value("userType", self.user_type)
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. The user display name, such as Adele Vance. Supports $filter (eq, startsWith) and $orderBy.
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. The user display name, such as Adele Vance. Supports $filter (eq, startsWith) and $orderBy.
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name, such as AdeleV@contoso.com. Supports $filter (eq, startsWith) and $orderBy.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name, such as AdeleV@contoso.com. Supports $filter (eq, startsWith) and $orderBy.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    
    @property
    def user_type(self,) -> Optional[sign_in_user_type.SignInUserType]:
        """
        Gets the userType property value. Identifies whether the user is a member or guest in the tenant. The possible values are: member, guest, unknownFutureValue.
        Returns: Optional[sign_in_user_type.SignInUserType]
        """
        return self._user_type
    
    @user_type.setter
    def user_type(self,value: Optional[sign_in_user_type.SignInUserType] = None) -> None:
        """
        Sets the userType property value. Identifies whether the user is a member or guest in the tenant. The possible values are: member, guest, unknownFutureValue.
        Args:
            value: Value to set for the userType property.
        """
        self._user_type = value
    

