from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_certificate_profile_base = lazy_import('msgraph.generated.models.android_certificate_profile_base')
android_username_source = lazy_import('msgraph.generated.models.android_username_source')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
domain_name_source = lazy_import('msgraph.generated.models.domain_name_source')
eas_authentication_method = lazy_import('msgraph.generated.models.eas_authentication_method')
email_sync_duration = lazy_import('msgraph.generated.models.email_sync_duration')
email_sync_schedule = lazy_import('msgraph.generated.models.email_sync_schedule')
user_email_source = lazy_import('msgraph.generated.models.user_email_source')

class AndroidEasEmailProfileConfiguration(device_configuration.DeviceConfiguration):
    @property
    def account_name(self,) -> Optional[str]:
        """
        Gets the accountName property value. Exchange ActiveSync account name, displayed to users as name of EAS (this) profile.
        Returns: Optional[str]
        """
        return self._account_name
    
    @account_name.setter
    def account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the accountName property value. Exchange ActiveSync account name, displayed to users as name of EAS (this) profile.
        Args:
            value: Value to set for the accountName property.
        """
        self._account_name = value
    
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
            value: Value to set for the authenticationMethod property.
        """
        self._authentication_method = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidEasEmailProfileConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidEasEmailProfileConfiguration"
        # Exchange ActiveSync account name, displayed to users as name of EAS (this) profile.
        self._account_name: Optional[str] = None
        # Exchange Active Sync authentication method.
        self._authentication_method: Optional[eas_authentication_method.EasAuthenticationMethod] = None
        # Custom domain name value used while generating an email profile before installing on the device.
        self._custom_domain_name: Optional[str] = None
        # Possible values for email sync duration.
        self._duration_of_email_to_sync: Optional[email_sync_duration.EmailSyncDuration] = None
        # Possible values for username source or email source.
        self._email_address_source: Optional[user_email_source.UserEmailSource] = None
        # Possible values for email sync schedule.
        self._email_sync_schedule: Optional[email_sync_schedule.EmailSyncSchedule] = None
        # Exchange location (URL) that the native mail app connects to.
        self._host_name: Optional[str] = None
        # Identity certificate.
        self._identity_certificate: Optional[android_certificate_profile_base.AndroidCertificateProfileBase] = None
        # Indicates whether or not to use S/MIME certificate.
        self._require_smime: Optional[bool] = None
        # Indicates whether or not to use SSL.
        self._require_ssl: Optional[bool] = None
        # S/MIME signing certificate.
        self._smime_signing_certificate: Optional[android_certificate_profile_base.AndroidCertificateProfileBase] = None
        # Toggles syncing the calendar. If set to false calendar is turned off on the device.
        self._sync_calendar: Optional[bool] = None
        # Toggles syncing contacts. If set to false contacts are turned off on the device.
        self._sync_contacts: Optional[bool] = None
        # Toggles syncing notes. If set to false notes are turned off on the device.
        self._sync_notes: Optional[bool] = None
        # Toggles syncing tasks. If set to false tasks are turned off on the device.
        self._sync_tasks: Optional[bool] = None
        # UserDomainname attribute that is picked from AAD and injected into this profile before installing on the device. Possible values are: fullDomainName, netBiosDomainName.
        self._user_domain_name_source: Optional[domain_name_source.DomainNameSource] = None
        # Android username source.
        self._username_source: Optional[android_username_source.AndroidUsernameSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidEasEmailProfileConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidEasEmailProfileConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidEasEmailProfileConfiguration()
    
    @property
    def custom_domain_name(self,) -> Optional[str]:
        """
        Gets the customDomainName property value. Custom domain name value used while generating an email profile before installing on the device.
        Returns: Optional[str]
        """
        return self._custom_domain_name
    
    @custom_domain_name.setter
    def custom_domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the customDomainName property value. Custom domain name value used while generating an email profile before installing on the device.
        Args:
            value: Value to set for the customDomainName property.
        """
        self._custom_domain_name = value
    
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
            value: Value to set for the durationOfEmailToSync property.
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
            value: Value to set for the emailAddressSource property.
        """
        self._email_address_source = value
    
    @property
    def email_sync_schedule(self,) -> Optional[email_sync_schedule.EmailSyncSchedule]:
        """
        Gets the emailSyncSchedule property value. Possible values for email sync schedule.
        Returns: Optional[email_sync_schedule.EmailSyncSchedule]
        """
        return self._email_sync_schedule
    
    @email_sync_schedule.setter
    def email_sync_schedule(self,value: Optional[email_sync_schedule.EmailSyncSchedule] = None) -> None:
        """
        Sets the emailSyncSchedule property value. Possible values for email sync schedule.
        Args:
            value: Value to set for the emailSyncSchedule property.
        """
        self._email_sync_schedule = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_name": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "authentication_method": lambda n : setattr(self, 'authentication_method', n.get_enum_value(eas_authentication_method.EasAuthenticationMethod)),
            "custom_domain_name": lambda n : setattr(self, 'custom_domain_name', n.get_str_value()),
            "duration_of_email_to_sync": lambda n : setattr(self, 'duration_of_email_to_sync', n.get_enum_value(email_sync_duration.EmailSyncDuration)),
            "email_address_source": lambda n : setattr(self, 'email_address_source', n.get_enum_value(user_email_source.UserEmailSource)),
            "email_sync_schedule": lambda n : setattr(self, 'email_sync_schedule', n.get_enum_value(email_sync_schedule.EmailSyncSchedule)),
            "host_name": lambda n : setattr(self, 'host_name', n.get_str_value()),
            "identity_certificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(android_certificate_profile_base.AndroidCertificateProfileBase)),
            "require_smime": lambda n : setattr(self, 'require_smime', n.get_bool_value()),
            "require_ssl": lambda n : setattr(self, 'require_ssl', n.get_bool_value()),
            "smime_signing_certificate": lambda n : setattr(self, 'smime_signing_certificate', n.get_object_value(android_certificate_profile_base.AndroidCertificateProfileBase)),
            "sync_calendar": lambda n : setattr(self, 'sync_calendar', n.get_bool_value()),
            "sync_contacts": lambda n : setattr(self, 'sync_contacts', n.get_bool_value()),
            "sync_notes": lambda n : setattr(self, 'sync_notes', n.get_bool_value()),
            "sync_tasks": lambda n : setattr(self, 'sync_tasks', n.get_bool_value()),
            "user_domain_name_source": lambda n : setattr(self, 'user_domain_name_source', n.get_enum_value(domain_name_source.DomainNameSource)),
            "username_source": lambda n : setattr(self, 'username_source', n.get_enum_value(android_username_source.AndroidUsernameSource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def host_name(self,) -> Optional[str]:
        """
        Gets the hostName property value. Exchange location (URL) that the native mail app connects to.
        Returns: Optional[str]
        """
        return self._host_name
    
    @host_name.setter
    def host_name(self,value: Optional[str] = None) -> None:
        """
        Sets the hostName property value. Exchange location (URL) that the native mail app connects to.
        Args:
            value: Value to set for the hostName property.
        """
        self._host_name = value
    
    @property
    def identity_certificate(self,) -> Optional[android_certificate_profile_base.AndroidCertificateProfileBase]:
        """
        Gets the identityCertificate property value. Identity certificate.
        Returns: Optional[android_certificate_profile_base.AndroidCertificateProfileBase]
        """
        return self._identity_certificate
    
    @identity_certificate.setter
    def identity_certificate(self,value: Optional[android_certificate_profile_base.AndroidCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificate property value. Identity certificate.
        Args:
            value: Value to set for the identityCertificate property.
        """
        self._identity_certificate = value
    
    @property
    def require_smime(self,) -> Optional[bool]:
        """
        Gets the requireSmime property value. Indicates whether or not to use S/MIME certificate.
        Returns: Optional[bool]
        """
        return self._require_smime
    
    @require_smime.setter
    def require_smime(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireSmime property value. Indicates whether or not to use S/MIME certificate.
        Args:
            value: Value to set for the requireSmime property.
        """
        self._require_smime = value
    
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
            value: Value to set for the requireSsl property.
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
        writer.write_str_value("accountName", self.account_name)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_str_value("customDomainName", self.custom_domain_name)
        writer.write_enum_value("durationOfEmailToSync", self.duration_of_email_to_sync)
        writer.write_enum_value("emailAddressSource", self.email_address_source)
        writer.write_enum_value("emailSyncSchedule", self.email_sync_schedule)
        writer.write_str_value("hostName", self.host_name)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_bool_value("requireSmime", self.require_smime)
        writer.write_bool_value("requireSsl", self.require_ssl)
        writer.write_object_value("smimeSigningCertificate", self.smime_signing_certificate)
        writer.write_bool_value("syncCalendar", self.sync_calendar)
        writer.write_bool_value("syncContacts", self.sync_contacts)
        writer.write_bool_value("syncNotes", self.sync_notes)
        writer.write_bool_value("syncTasks", self.sync_tasks)
        writer.write_enum_value("userDomainNameSource", self.user_domain_name_source)
        writer.write_enum_value("usernameSource", self.username_source)
    
    @property
    def smime_signing_certificate(self,) -> Optional[android_certificate_profile_base.AndroidCertificateProfileBase]:
        """
        Gets the smimeSigningCertificate property value. S/MIME signing certificate.
        Returns: Optional[android_certificate_profile_base.AndroidCertificateProfileBase]
        """
        return self._smime_signing_certificate
    
    @smime_signing_certificate.setter
    def smime_signing_certificate(self,value: Optional[android_certificate_profile_base.AndroidCertificateProfileBase] = None) -> None:
        """
        Sets the smimeSigningCertificate property value. S/MIME signing certificate.
        Args:
            value: Value to set for the smimeSigningCertificate property.
        """
        self._smime_signing_certificate = value
    
    @property
    def sync_calendar(self,) -> Optional[bool]:
        """
        Gets the syncCalendar property value. Toggles syncing the calendar. If set to false calendar is turned off on the device.
        Returns: Optional[bool]
        """
        return self._sync_calendar
    
    @sync_calendar.setter
    def sync_calendar(self,value: Optional[bool] = None) -> None:
        """
        Sets the syncCalendar property value. Toggles syncing the calendar. If set to false calendar is turned off on the device.
        Args:
            value: Value to set for the syncCalendar property.
        """
        self._sync_calendar = value
    
    @property
    def sync_contacts(self,) -> Optional[bool]:
        """
        Gets the syncContacts property value. Toggles syncing contacts. If set to false contacts are turned off on the device.
        Returns: Optional[bool]
        """
        return self._sync_contacts
    
    @sync_contacts.setter
    def sync_contacts(self,value: Optional[bool] = None) -> None:
        """
        Sets the syncContacts property value. Toggles syncing contacts. If set to false contacts are turned off on the device.
        Args:
            value: Value to set for the syncContacts property.
        """
        self._sync_contacts = value
    
    @property
    def sync_notes(self,) -> Optional[bool]:
        """
        Gets the syncNotes property value. Toggles syncing notes. If set to false notes are turned off on the device.
        Returns: Optional[bool]
        """
        return self._sync_notes
    
    @sync_notes.setter
    def sync_notes(self,value: Optional[bool] = None) -> None:
        """
        Sets the syncNotes property value. Toggles syncing notes. If set to false notes are turned off on the device.
        Args:
            value: Value to set for the syncNotes property.
        """
        self._sync_notes = value
    
    @property
    def sync_tasks(self,) -> Optional[bool]:
        """
        Gets the syncTasks property value. Toggles syncing tasks. If set to false tasks are turned off on the device.
        Returns: Optional[bool]
        """
        return self._sync_tasks
    
    @sync_tasks.setter
    def sync_tasks(self,value: Optional[bool] = None) -> None:
        """
        Sets the syncTasks property value. Toggles syncing tasks. If set to false tasks are turned off on the device.
        Args:
            value: Value to set for the syncTasks property.
        """
        self._sync_tasks = value
    
    @property
    def user_domain_name_source(self,) -> Optional[domain_name_source.DomainNameSource]:
        """
        Gets the userDomainNameSource property value. UserDomainname attribute that is picked from AAD and injected into this profile before installing on the device. Possible values are: fullDomainName, netBiosDomainName.
        Returns: Optional[domain_name_source.DomainNameSource]
        """
        return self._user_domain_name_source
    
    @user_domain_name_source.setter
    def user_domain_name_source(self,value: Optional[domain_name_source.DomainNameSource] = None) -> None:
        """
        Sets the userDomainNameSource property value. UserDomainname attribute that is picked from AAD and injected into this profile before installing on the device. Possible values are: fullDomainName, netBiosDomainName.
        Args:
            value: Value to set for the userDomainNameSource property.
        """
        self._user_domain_name_source = value
    
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
            value: Value to set for the usernameSource property.
        """
        self._username_source = value
    

