from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_for_work_certificate_profile_base, android_for_work_gmail_eas_configuration, android_for_work_nine_work_eas_configuration, android_username_source, device_configuration, eas_authentication_method, email_sync_duration, user_email_source

from . import device_configuration

@dataclass
class AndroidForWorkEasEmailProfileBase(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.androidForWorkEasEmailProfileBase"
    # Exchange Active Sync authentication method.
    authentication_method: Optional[eas_authentication_method.EasAuthenticationMethod] = None
    # Possible values for email sync duration.
    duration_of_email_to_sync: Optional[email_sync_duration.EmailSyncDuration] = None
    # Possible values for username source or email source.
    email_address_source: Optional[user_email_source.UserEmailSource] = None
    # Exchange location (URL) that the mail app connects to.
    host_name: Optional[str] = None
    # Identity certificate.
    identity_certificate: Optional[android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase] = None
    # Indicates whether or not to use SSL.
    require_ssl: Optional[bool] = None
    # Android username source.
    username_source: Optional[android_username_source.AndroidUsernameSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidForWorkEasEmailProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkEasEmailProfileBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkGmailEasConfiguration".casefold():
            from . import android_for_work_gmail_eas_configuration

            return android_for_work_gmail_eas_configuration.AndroidForWorkGmailEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkNineWorkEasConfiguration".casefold():
            from . import android_for_work_nine_work_eas_configuration

            return android_for_work_nine_work_eas_configuration.AndroidForWorkNineWorkEasConfiguration()
        return AndroidForWorkEasEmailProfileBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_for_work_certificate_profile_base, android_for_work_gmail_eas_configuration, android_for_work_nine_work_eas_configuration, android_username_source, device_configuration, eas_authentication_method, email_sync_duration, user_email_source

        from . import android_for_work_certificate_profile_base, android_for_work_gmail_eas_configuration, android_for_work_nine_work_eas_configuration, android_username_source, device_configuration, eas_authentication_method, email_sync_duration, user_email_source

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(eas_authentication_method.EasAuthenticationMethod)),
            "durationOfEmailToSync": lambda n : setattr(self, 'duration_of_email_to_sync', n.get_enum_value(email_sync_duration.EmailSyncDuration)),
            "emailAddressSource": lambda n : setattr(self, 'email_address_source', n.get_enum_value(user_email_source.UserEmailSource)),
            "hostName": lambda n : setattr(self, 'host_name', n.get_str_value()),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase)),
            "requireSsl": lambda n : setattr(self, 'require_ssl', n.get_bool_value()),
            "usernameSource": lambda n : setattr(self, 'username_source', n.get_enum_value(android_username_source.AndroidUsernameSource)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_enum_value("durationOfEmailToSync", self.duration_of_email_to_sync)
        writer.write_enum_value("emailAddressSource", self.email_address_source)
        writer.write_str_value("hostName", self.host_name)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_bool_value("requireSsl", self.require_ssl)
        writer.write_enum_value("usernameSource", self.username_source)
    

