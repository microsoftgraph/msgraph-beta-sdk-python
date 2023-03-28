from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class Office365GroupsActivityStorage(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Office365GroupsActivityStorage and sets the default values.
        """
        super().__init__()
        # The storage used in group mailbox.
        self._mailbox_storage_used_in_bytes: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The snapshot date for Exchange and SharePoint used storage.
        self._report_date: Optional[date] = None
        # The number of days the report covers.
        self._report_period: Optional[str] = None
        # The latest date of the content.
        self._report_refresh_date: Optional[date] = None
        # The storage used in SharePoint document library.
        self._site_storage_used_in_bytes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Office365GroupsActivityStorage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Office365GroupsActivityStorage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Office365GroupsActivityStorage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "mailboxStorageUsedInBytes": lambda n : setattr(self, 'mailbox_storage_used_in_bytes', n.get_int_value()),
            "reportDate": lambda n : setattr(self, 'report_date', n.get_date_value()),
            "reportPeriod": lambda n : setattr(self, 'report_period', n.get_str_value()),
            "reportRefreshDate": lambda n : setattr(self, 'report_refresh_date', n.get_date_value()),
            "siteStorageUsedInBytes": lambda n : setattr(self, 'site_storage_used_in_bytes', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def mailbox_storage_used_in_bytes(self,) -> Optional[int]:
        """
        Gets the mailboxStorageUsedInBytes property value. The storage used in group mailbox.
        Returns: Optional[int]
        """
        return self._mailbox_storage_used_in_bytes
    
    @mailbox_storage_used_in_bytes.setter
    def mailbox_storage_used_in_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the mailboxStorageUsedInBytes property value. The storage used in group mailbox.
        Args:
            value: Value to set for the mailbox_storage_used_in_bytes property.
        """
        self._mailbox_storage_used_in_bytes = value
    
    @property
    def report_date(self,) -> Optional[date]:
        """
        Gets the reportDate property value. The snapshot date for Exchange and SharePoint used storage.
        Returns: Optional[date]
        """
        return self._report_date
    
    @report_date.setter
    def report_date(self,value: Optional[date] = None) -> None:
        """
        Sets the reportDate property value. The snapshot date for Exchange and SharePoint used storage.
        Args:
            value: Value to set for the report_date property.
        """
        self._report_date = value
    
    @property
    def report_period(self,) -> Optional[str]:
        """
        Gets the reportPeriod property value. The number of days the report covers.
        Returns: Optional[str]
        """
        return self._report_period
    
    @report_period.setter
    def report_period(self,value: Optional[str] = None) -> None:
        """
        Sets the reportPeriod property value. The number of days the report covers.
        Args:
            value: Value to set for the report_period property.
        """
        self._report_period = value
    
    @property
    def report_refresh_date(self,) -> Optional[date]:
        """
        Gets the reportRefreshDate property value. The latest date of the content.
        Returns: Optional[date]
        """
        return self._report_refresh_date
    
    @report_refresh_date.setter
    def report_refresh_date(self,value: Optional[date] = None) -> None:
        """
        Sets the reportRefreshDate property value. The latest date of the content.
        Args:
            value: Value to set for the report_refresh_date property.
        """
        self._report_refresh_date = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("mailboxStorageUsedInBytes", self.mailbox_storage_used_in_bytes)
        writer.write_date_value("reportDate", self.report_date)
        writer.write_str_value("reportPeriod", self.report_period)
        writer.write_date_value("reportRefreshDate", self.report_refresh_date)
        writer.write_int_value("siteStorageUsedInBytes", self.site_storage_used_in_bytes)
    
    @property
    def site_storage_used_in_bytes(self,) -> Optional[int]:
        """
        Gets the siteStorageUsedInBytes property value. The storage used in SharePoint document library.
        Returns: Optional[int]
        """
        return self._site_storage_used_in_bytes
    
    @site_storage_used_in_bytes.setter
    def site_storage_used_in_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the siteStorageUsedInBytes property value. The storage used in SharePoint document library.
        Args:
            value: Value to set for the site_storage_used_in_bytes property.
        """
        self._site_storage_used_in_bytes = value
    

