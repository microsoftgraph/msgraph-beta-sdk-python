from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_for_work_certificate_profile_base, android_for_work_gmail_eas_configuration, android_for_work_nine_work_eas_configuration, android_username_source, device_configuration, eas_authentication_method, email_sync_duration, user_email_source

from . import device_configuration

class AndroidForWorkEasEmailProfileBase(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidForWorkEasEmailProfileBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidForWorkEasEmailProfileBase"
        # Exchange Active Sync authentication method.
        self._authentication_method: Optional[eas_authentication_method.EasAuthenticationMethod] = None
        # Possible values for email sync duration.
        self._duration_of_email_to_sync: Optional[email_sync_duration.EmailSyncDuration] = None
        # Possible values for username source or email source.
        self._email_address_source: Optional[user_email_source.UserEmailSource] = None
        # Exchange location (URL) that the mail app connects to.
        self._host_name: Optional[str] = None
        # Identity certificate.
        self._identity_certificate: Optional[android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase] = None
        # Indicates whether or not to use SSL.
        self._require_ssl: Optional[bool] = None
        # Android username source.
        self._username_source: Optional[android_username_source.AndroidUsernameSource] = None
    
    @property
    def authentication_method(self,) -> Optional[eas_authentication_method.EasAuthenticationMethod]:
        """
        Gets the authenticationMethod property value. Exchange Active Sync authentication method.
        Returns: Optional[eas_authentication_method.EasAuthenticationMethod]
        """
        return self._authentication_method
    
    @authentication_method.setter
    def authentication_method(self,value: Optional[eas_authentication_method.EasAuthenticationMethod] = None) -> None:
        """
        Sets the authenticationMethod property value. Exchange Active Sync authentication method.
        Args:
            value: Value to set for the authentication_method property.
        """
        self._authentication_method = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidForWorkEasEmailProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkEasEmailProfileBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.androidForWorkGmailEasConfiguration":
                from . import android_for_work_gmail_eas_configuration

                return android_for_work_gmail_eas_configuration.AndroidForWorkGmailEasConfiguration()
            if mapping_value == "#microsoft.graph.androidForWorkNineWorkEasConfiguration":
                from . import android_for_work_nine_work_eas_configuration

                return android_for_work_nine_work_eas_configuration.AndroidForWorkNineWorkEasConfiguration()
        return AndroidForWorkEasEmailProfileBase()
    
    @property
    def duration_of_email_to_sync(self,) -> Optional[email_sync_duration.EmailSyncDuration]:
        """
        Gets the durationOfEmailToSync property value. Possible values for email sync duration.
        Returns: Optional[email_sync_duration.EmailSyncDuration]
        """
        return self._duration_of_email_to_sync
    
    @duration_of_email_to_sync.setter
    def duration_of_email_to_sync(self,value: Optional[email_sync_duration.EmailSyncDuration] = None) -> None:
        """
        Sets the durationOfEmailToSync property value. Possible values for email sync duration.
        Args:
            value: Value to set for the duration_of_email_to_sync property.
        """
        self._duration_of_email_to_sync = value
    
    @property
    def email_address_source(self,) -> Optional[user_email_source.UserEmailSource]:
        """
        Gets the emailAddressSource property value. Possible values for username source or email source.
        Returns: Optional[user_email_source.UserEmailSource]
        """
        return self._email_address_source
    
    @email_address_source.setter
    def email_address_source(self,value: Optional[user_email_source.UserEmailSource] = None) -> None:
        """
        Sets the emailAddressSource property value. Possible values for username source or email source.
        Args:
            value: Value to set for the email_address_source property.
        """
        self._email_address_source = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def host_name(self,) -> Optional[str]:
        """
        Gets the hostName property value. Exchange location (URL) that the mail app connects to.
        Returns: Optional[str]
        """
        return self._host_name
    
    @host_name.setter
    def host_name(self,value: Optional[str] = None) -> None:
        """
        Sets the hostName property value. Exchange location (URL) that the mail app connects to.
        Args:
            value: Value to set for the host_name property.
        """
        self._host_name = value
    
    @property
    def identity_certificate(self,) -> Optional[android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase]:
        """
        Gets the identityCertificate property value. Identity certificate.
        Returns: Optional[android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase]
        """
        return self._identity_certificate
    
    @identity_certificate.setter
    def identity_certificate(self,value: Optional[android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificate property value. Identity certificate.
        Args:
            value: Value to set for the identity_certificate property.
        """
        self._identity_certificate = value
    
    @property
    def require_ssl(self,) -> Optional[bool]:
        """
        Gets the requireSsl property value. Indicates whether or not to use SSL.
        Returns: Optional[bool]
        """
        return self._require_ssl
    
    @require_ssl.setter
    def require_ssl(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireSsl property value. Indicates whether or not to use SSL.
        Args:
            value: Value to set for the require_ssl property.
        """
        self._require_ssl = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_enum_value("durationOfEmailToSync", self.duration_of_email_to_sync)
        writer.write_enum_value("emailAddressSource", self.email_address_source)
        writer.write_str_value("hostName", self.host_name)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_bool_value("requireSsl", self.require_ssl)
        writer.write_enum_value("usernameSource", self.username_source)
    
    @property
    def username_source(self,) -> Optional[android_username_source.AndroidUsernameSource]:
        """
        Gets the usernameSource property value. Android username source.
        Returns: Optional[android_username_source.AndroidUsernameSource]
        """
        return self._username_source
    
    @username_source.setter
    def username_source(self,value: Optional[android_username_source.AndroidUsernameSource] = None) -> None:
        """
        Sets the usernameSource property value. Android username source.
        Args:
            value: Value to set for the username_source property.
        """
        self._username_source = value
    

