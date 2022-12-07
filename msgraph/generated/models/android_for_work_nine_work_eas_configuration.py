from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_for_work_eas_email_profile_base = lazy_import('msgraph.generated.models.android_for_work_eas_email_profile_base')

class AndroidForWorkNineWorkEasConfiguration(android_for_work_eas_email_profile_base.AndroidForWorkEasEmailProfileBase):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidForWorkNineWorkEasConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidForWorkNineWorkEasConfiguration"
        # Toggles syncing the calendar. If set to false the calendar is turned off on the device.
        self._sync_calendar: Optional[bool] = None
        # Toggles syncing contacts. If set to false contacts are turned off on the device.
        self._sync_contacts: Optional[bool] = None
        # Toggles syncing tasks. If set to false tasks are turned off on the device.
        self._sync_tasks: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidForWorkNineWorkEasConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkNineWorkEasConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidForWorkNineWorkEasConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "sync_calendar": lambda n : setattr(self, 'sync_calendar', n.get_bool_value()),
            "sync_contacts": lambda n : setattr(self, 'sync_contacts', n.get_bool_value()),
            "sync_tasks": lambda n : setattr(self, 'sync_tasks', n.get_bool_value()),
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
        writer.write_bool_value("syncCalendar", self.sync_calendar)
        writer.write_bool_value("syncContacts", self.sync_contacts)
        writer.write_bool_value("syncTasks", self.sync_tasks)
    
    @property
    def sync_calendar(self,) -> Optional[bool]:
        """
        Gets the syncCalendar property value. Toggles syncing the calendar. If set to false the calendar is turned off on the device.
        Returns: Optional[bool]
        """
        return self._sync_calendar
    
    @sync_calendar.setter
    def sync_calendar(self,value: Optional[bool] = None) -> None:
        """
        Sets the syncCalendar property value. Toggles syncing the calendar. If set to false the calendar is turned off on the device.
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
    

