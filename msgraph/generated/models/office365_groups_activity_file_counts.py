from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class Office365GroupsActivityFileCounts(entity.Entity):
    @property
    def active(self,) -> Optional[int]:
        """
        Gets the active property value. The number of files that were viewed, edited, shared, or synced in the group's SharePoint document library.
        Returns: Optional[int]
        """
        return self._active
    
    @active.setter
    def active(self,value: Optional[int] = None) -> None:
        """
        Sets the active property value. The number of files that were viewed, edited, shared, or synced in the group's SharePoint document library.
        Args:
            value: Value to set for the active property.
        """
        self._active = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Office365GroupsActivityFileCounts and sets the default values.
        """
        super().__init__()
        # The number of files that were viewed, edited, shared, or synced in the group's SharePoint document library.
        self._active: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The date on which a number of files were active in the group's SharePoint site.
        self._report_date: Optional[Date] = None
        # The number of days the report covers.
        self._report_period: Optional[str] = None
        # The latest date of the content.
        self._report_refresh_date: Optional[Date] = None
        # The total number of files in the group's SharePoint document library.
        self._total: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Office365GroupsActivityFileCounts:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Office365GroupsActivityFileCounts
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Office365GroupsActivityFileCounts()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active": lambda n : setattr(self, 'active', n.get_int_value()),
            "report_date": lambda n : setattr(self, 'report_date', n.get_object_value(Date)),
            "report_period": lambda n : setattr(self, 'report_period', n.get_str_value()),
            "report_refresh_date": lambda n : setattr(self, 'report_refresh_date', n.get_object_value(Date)),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def report_date(self,) -> Optional[Date]:
        """
        Gets the reportDate property value. The date on which a number of files were active in the group's SharePoint site.
        Returns: Optional[Date]
        """
        return self._report_date
    
    @report_date.setter
    def report_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the reportDate property value. The date on which a number of files were active in the group's SharePoint site.
        Args:
            value: Value to set for the reportDate property.
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
            value: Value to set for the reportPeriod property.
        """
        self._report_period = value
    
    @property
    def report_refresh_date(self,) -> Optional[Date]:
        """
        Gets the reportRefreshDate property value. The latest date of the content.
        Returns: Optional[Date]
        """
        return self._report_refresh_date
    
    @report_refresh_date.setter
    def report_refresh_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the reportRefreshDate property value. The latest date of the content.
        Args:
            value: Value to set for the reportRefreshDate property.
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
        writer.write_int_value("active", self.active)
        writer.write_object_value("reportDate", self.report_date)
        writer.write_str_value("reportPeriod", self.report_period)
        writer.write_object_value("reportRefreshDate", self.report_refresh_date)
        writer.write_int_value("total", self.total)
    
    @property
    def total(self,) -> Optional[int]:
        """
        Gets the total property value. The total number of files in the group's SharePoint document library.
        Returns: Optional[int]
        """
        return self._total
    
    @total.setter
    def total(self,value: Optional[int] = None) -> None:
        """
        Sets the total property value. The total number of files in the group's SharePoint document library.
        Args:
            value: Value to set for the total property.
        """
        self._total = value
    

