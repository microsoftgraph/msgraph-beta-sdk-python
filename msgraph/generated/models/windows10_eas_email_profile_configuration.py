from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import eas_email_profile_configuration_base, email_sync_duration, email_sync_schedule, user_email_source

from . import eas_email_profile_configuration_base

@dataclass
class Windows10EasEmailProfileConfiguration(eas_email_profile_configuration_base.EasEmailProfileConfigurationBase):
    odata_type = "#microsoft.graph.windows10EasEmailProfileConfiguration"
    # Account name.
    account_name: Optional[str] = None
    # Possible values for email sync duration.
    duration_of_email_to_sync: Optional[email_sync_duration.EmailSyncDuration] = None
    # Possible values for username source or email source.
    email_address_source: Optional[user_email_source.UserEmailSource] = None
    # Possible values for email sync schedule.
    email_sync_schedule: Optional[email_sync_schedule.EmailSyncSchedule] = None
    # Exchange location that (URL) that the native mail app connects to.
    host_name: Optional[str] = None
    # Indicates whether or not to use SSL.
    require_ssl: Optional[bool] = None
    # Whether or not to sync the calendar.
    sync_calendar: Optional[bool] = None
    # Whether or not to sync contacts.
    sync_contacts: Optional[bool] = None
    # Whether or not to sync tasks.
    sync_tasks: Optional[bool] = None
    
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
    

