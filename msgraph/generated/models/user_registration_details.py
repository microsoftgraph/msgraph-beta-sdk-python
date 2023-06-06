from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import default_mfa_method_type, entity, sign_in_user_type

from . import entity

@dataclass
class UserRegistrationDetails(entity.Entity):
    # The method the user or admin selected as default for performing multi-factor authentication for the user. The possible values are: none, mobilePhone, alternateMobilePhone, officePhone, microsoftAuthenticatorPush, softwareOneTimePasscode, unknownFutureValue.
    default_mfa_method: Optional[default_mfa_method_type.DefaultMfaMethodType] = None
    # Whether the user has an admin role in the tenant. This value can be used to check the authentication methods that privileged accounts are registered for and capable of.
    is_admin: Optional[bool] = None
    # Whether the user has registered a strong authentication method for multi-factor authentication. The method must be allowed by the authentication methods policy. Supports $filter (eq).
    is_mfa_capable: Optional[bool] = None
    # Whether the user has registered a strong authentication method for multi-factor authentication. The method may not necessarily be allowed by the authentication methods policy.  Supports $filter (eq).
    is_mfa_registered: Optional[bool] = None
    # Whether the user has registered a passwordless strong authentication method (including FIDO2, Windows Hello for Business, and Microsoft Authenticator (Passwordless)) that is allowed by the authentication methods policy. Supports $filter (eq).
    is_passwordless_capable: Optional[bool] = None
    # Whether the user has registered the required number of authentication methods for self-service password reset and the user is allowed to perform self-service password reset by policy. Supports $filter (eq).
    is_sspr_capable: Optional[bool] = None
    # Whether the user is allowed to perform self-service password reset by policy. The user may not necessarily have registered the required number of authentication methods for self-service password reset. Supports $filter (eq).
    is_sspr_enabled: Optional[bool] = None
    # Whether the user has registered the required number of authentication methods for self-service password reset. The user may not necessarily be allowed to perform self-service password reset by policy. Supports $filter (eq).
    is_sspr_registered: Optional[bool] = None
    # The lastUpdatedDateTime property
    last_updated_date_time: Optional[datetime] = None
    # Collection of authentication methods registered, such as mobilePhone, email, fido2. Supports $filter (any with eq).
    methods_registered: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user display name, such as Adele Vance. Supports $filter (eq, startsWith) and $orderBy.
    user_display_name: Optional[str] = None
    # The user principal name, such as AdeleV@contoso.com. Supports $filter (eq, startsWith) and $orderBy.
    user_principal_name: Optional[str] = None
    # Identifies whether the user is a member or guest in the tenant. The possible values are: member, guest, unknownFutureValue.
    user_type: Optional[sign_in_user_type.SignInUserType] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import default_mfa_method_type, entity, sign_in_user_type

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultMfaMethod": lambda n : setattr(self, 'default_mfa_method', n.get_enum_value(default_mfa_method_type.DefaultMfaMethodType)),
            "isAdmin": lambda n : setattr(self, 'is_admin', n.get_bool_value()),
            "isMfaCapable": lambda n : setattr(self, 'is_mfa_capable', n.get_bool_value()),
            "isMfaRegistered": lambda n : setattr(self, 'is_mfa_registered', n.get_bool_value()),
            "isPasswordlessCapable": lambda n : setattr(self, 'is_passwordless_capable', n.get_bool_value()),
            "isSsprCapable": lambda n : setattr(self, 'is_sspr_capable', n.get_bool_value()),
            "isSsprEnabled": lambda n : setattr(self, 'is_sspr_enabled', n.get_bool_value()),
            "isSsprRegistered": lambda n : setattr(self, 'is_sspr_registered', n.get_bool_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "methodsRegistered": lambda n : setattr(self, 'methods_registered', n.get_collection_of_primitive_values(str)),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(sign_in_user_type.SignInUserType)),
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
        writer.write_enum_value("defaultMfaMethod", self.default_mfa_method)
        writer.write_bool_value("isAdmin", self.is_admin)
        writer.write_bool_value("isMfaCapable", self.is_mfa_capable)
        writer.write_bool_value("isMfaRegistered", self.is_mfa_registered)
        writer.write_bool_value("isPasswordlessCapable", self.is_passwordless_capable)
        writer.write_bool_value("isSsprCapable", self.is_sspr_capable)
        writer.write_bool_value("isSsprEnabled", self.is_sspr_enabled)
        writer.write_bool_value("isSsprRegistered", self.is_sspr_registered)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_collection_of_primitive_values("methodsRegistered", self.methods_registered)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_enum_value("userType", self.user_type)
    

