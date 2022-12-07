from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

eas_email_profile_configuration_base = lazy_import('msgraph.generated.models.eas_email_profile_configuration_base')
email_sync_duration = lazy_import('msgraph.generated.models.email_sync_duration')
email_sync_schedule = lazy_import('msgraph.generated.models.email_sync_schedule')
user_email_source = lazy_import('msgraph.generated.models.user_email_source')

class WindowsPhoneEASEmailProfileConfiguration(eas_email_profile_configuration_base.EasEmailProfileConfigurationBase):
    @property
    def account_name(self,) -> Optional[str]:
        """
        Gets the accountName property value. Account name.
        Returns: Optional[str]
        """
        return self._account_name
    
    @account_name.setter
    def account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the accountName property value. Account name.
        Args:
            value: Value to set for the accountName property.
        """
        self._account_name = value
    
    @property
    def apply_only_to_windows_phone81(self,) -> Optional[bool]:
        """
        Gets the applyOnlyToWindowsPhone81 property value. Value indicating whether this policy only applies to Windows 8.1. This property is read-only.
        Returns: Optional[bool]
        """
        return self._apply_only_to_windows_phone81
    
    @apply_only_to_windows_phone81.setter
    def apply_only_to_windows_phone81(self,value: Optional[bool] = None) -> None:
        """
        Sets the applyOnlyToWindowsPhone81 property value. Value indicating whether this policy only applies to Windows 8.1. This property is read-only.
        Args:
            value: Value to set for the applyOnlyToWindowsPhone81 property.
        """
        self._apply_only_to_windows_phone81 = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsPhoneEASEmailProfileConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsPhoneEASEmailProfileConfiguration"
        # Account name.
        self._account_name: Optional[str] = None
        # Value indicating whether this policy only applies to Windows 8.1. This property is read-only.
        self._apply_only_to_windows_phone81: Optional[bool] = None
        # Possible values for email sync duration.
        self._duration_of_email_to_sync: Optional[email_sync_duration.EmailSyncDuration] = None
        # Email attribute that is picked from AAD and injected into this profile before installing on the device. Possible values are: userPrincipalName, primarySmtpAddress.
        self._email_address_source: Optional[user_email_source.UserEmailSource] = None
        # Possible values for email sync schedule.
        self._email_sync_schedule: Optional[email_sync_schedule.EmailSyncSchedule] = None
        # Exchange location that (URL) that the native mail app connects to.
        self._host_name: Optional[str] = None
        # Indicates whether or not to use SSL.
        self._require_ssl: Optional[bool] = None
        # Whether or not to sync the calendar.
        self._sync_calendar: Optional[bool] = None
        # Whether or not to sync contacts.
        self._sync_contacts: Optional[bool] = None
        # Whether or not to sync tasks.
        self._sync_tasks: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPhoneEASEmailProfileConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhoneEASEmailProfileConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsPhoneEASEmailProfileConfiguration()
    
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
        Gets the emailAddressSource property value. Email attribute that is picked from AAD and injected into this profile before installing on the device. Possible values are: userPrincipalName, primarySmtpAddress.
        Returns: Optional[user_email_source.UserEmailSource]
        """
        return self._email_address_source
    
    @email_address_source.setter
    def email_address_source(self,value: Optional[user_email_source.UserEmailSource] = None) -> None:
        """
        Sets the emailAddressSource property value. Email attribute that is picked from AAD and injected into this profile before installing on the device. Possible values are: userPrincipalName, primarySmtpAddress.
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
            "apply_only_to_windows_phone81": lambda n : setattr(self, 'apply_only_to_windows_phone81', n.get_bool_value()),
            "duration_of_email_to_sync": lambda n : setattr(self, 'duration_of_email_to_sync', n.get_enum_value(email_sync_duration.EmailSyncDuration)),
            "email_address_source": lambda n : setattr(self, 'email_address_source', n.get_enum_value(user_email_source.UserEmailSource)),
            "email_sync_schedule": lambda n : setattr(self, 'email_sync_schedule', n.get_enum_value(email_sync_schedule.EmailSyncSchedule)),
            "host_name": lambda n : setattr(self, 'host_name', n.get_str_value()),
            "require_ssl": lambda n : setattr(self, 'require_ssl', n.get_bool_value()),
            "sync_calendar": lambda n : setattr(self, 'sync_calendar', n.get_bool_value()),
            "sync_contacts": lambda n : setattr(self, 'sync_contacts', n.get_bool_value()),
            "sync_tasks": lambda n : setattr(self, 'sync_tasks', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def host_name(self,) -> Optional[str]:
        """
        Gets the hostName property value. Exchange location that (URL) that the native mail app connects to.
        Returns: Optional[str]
        """
        return self._host_name
    
    @host_name.setter
    def host_name(self,value: Optional[str] = None) -> None:
        """
        Sets the hostName property value. Exchange location that (URL) that the native mail app connects to.
        Args:
            value: Value to set for the hostName property.
        """
        self._host_name = value
    
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
        writer.write_enum_value("durationOfEmailToSync", self.duration_of_email_to_sync)
        writer.write_enum_value("emailAddressSource", self.email_address_source)
        writer.write_enum_value("emailSyncSchedule", self.email_sync_schedule)
        writer.write_str_value("hostName", self.host_name)
        writer.write_bool_value("requireSsl", self.require_ssl)
        writer.write_bool_value("syncCalendar", self.sync_calendar)
        writer.write_bool_value("syncContacts", self.sync_contacts)
        writer.write_bool_value("syncTasks", self.sync_tasks)
    
    @property
    def sync_calendar(self,) -> Optional[bool]:
        """
        Gets the syncCalendar property value. Whether or not to sync the calendar.
        Returns: Optional[bool]
        """
        return self._sync_calendar
    
    @sync_calendar.setter
    def sync_calendar(self,value: Optional[bool] = None) -> None:
        """
        Sets the syncCalendar property value. Whether or not to sync the calendar.
        Args:
            value: Value to set for the syncCalendar property.
        """
        self._sync_calendar = value
    
    @property
    def sync_contacts(self,) -> Optional[bool]:
        """
        Gets the syncContacts property value. Whether or not to sync contacts.
        Returns: Optional[bool]
        """
        return self._sync_contacts
    
    @sync_contacts.setter
    def sync_contacts(self,value: Optional[bool] = None) -> None:
        """
        Sets the syncContacts property value. Whether or not to sync contacts.
        Args:
            value: Value to set for the syncContacts property.
        """
        self._sync_contacts = value
    
    @property
    def sync_tasks(self,) -> Optional[bool]:
        """
        Gets the syncTasks property value. Whether or not to sync tasks.
        Returns: Optional[bool]
        """
        return self._sync_tasks
    
    @sync_tasks.setter
    def sync_tasks(self,value: Optional[bool] = None) -> None:
        """
        Sets the syncTasks property value. Whether or not to sync tasks.
        Args:
            value: Value to set for the syncTasks property.
        """
        self._sync_tasks = value
    

