from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_work_profile_eas_email_profile_base

from . import android_work_profile_eas_email_profile_base

class AndroidWorkProfileNineWorkEasConfiguration(android_work_profile_eas_email_profile_base.AndroidWorkProfileEasEmailProfileBase):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidWorkProfileNineWorkEasConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidWorkProfileNineWorkEasConfiguration"
        # Toggles syncing the calendar. If set to false the calendar is turned off on the device.
        self._sync_calendar: Optional[bool] = None
        # Toggles syncing contacts. If set to false contacts are turned off on the device.
        self._sync_contacts: Optional[bool] = None
        # Toggles syncing tasks. If set to false tasks are turned off on the device.
        self._sync_tasks: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidWorkProfileNineWorkEasConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidWorkProfileNineWorkEasConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidWorkProfileNineWorkEasConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_work_profile_eas_email_profile_base

        fields: Dict[str, Callable[[Any], None]] = {
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
            value: Value to set for the sync_calendar property.
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
            value: Value to set for the sync_contacts property.
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
            value: Value to set for the sync_tasks property.
        """
        self._sync_tasks = value
    

