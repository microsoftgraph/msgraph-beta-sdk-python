from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import eas_email_profile_configuration_base, email_sync_duration, email_sync_schedule, user_email_source

from . import eas_email_profile_configuration_base

class Windows10EasEmailProfileConfiguration(eas_email_profile_configuration_base.EasEmailProfileConfigurationBase):
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10EasEmailProfileConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10EasEmailProfileConfiguration"
        # Account name.
        self._account_name: Optional[str] = None
        # Possible values for email sync duration.
        self._duration_of_email_to_sync: Optional[email_sync_duration.EmailSyncDuration] = None
        # Possible values for username source or email source.
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
            value: Value to set for the account_name property.
        """
        self._account_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10EasEmailProfileConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10EasEmailProfileConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10EasEmailProfileConfiguration()
    
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
            value: Value to set for the email_sync_schedule property.
        """
        self._email_sync_schedule = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import eas_email_profile_configuration_base, email_sync_duration, email_sync_schedule, user_email_source

        fields: Dict[str, Callable[[Any], None]] = {
            "accountName": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "durationOfEmailToSync": lambda n : setattr(self, 'duration_of_email_to_sync', n.get_enum_value(email_sync_duration.EmailSyncDuration)),
            "emailAddressSource": lambda n : setattr(self, 'email_address_source', n.get_enum_value(user_email_source.UserEmailSource)),
            "emailSyncSchedule": lambda n : setattr(self, 'email_sync_schedule', n.get_enum_value(email_sync_schedule.EmailSyncSchedule)),
            "hostName": lambda n : setattr(self, 'host_name', n.get_str_value()),
            "requireSsl": lambda n : setattr(self, 'require_ssl', n.get_bool_value()),
            "syncCalendar": lambda n : setattr(self, 'sync_calendar', n.get_bool_value()),
            "syncContacts": lambda n : setattr(self, 'sync_contacts', n.get_bool_value()),
            "syncTasks": lambda n : setattr(self, 'sync_tasks', n.get_bool_value()),
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
            value: Value to set for the host_name property.
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
            value: Value to set for the sync_calendar property.
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
            value: Value to set for the sync_contacts property.
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
            value: Value to set for the sync_tasks property.
        """
        self._sync_tasks = value
    

