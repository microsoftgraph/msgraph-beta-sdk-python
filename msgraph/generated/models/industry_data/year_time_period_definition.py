from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import year_reference_value
    from .. import entity

from .. import entity

class YearTimePeriodDefinition(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new yearTimePeriodDefinition and sets the default values.
        """
        super().__init__()
        # The name of the year. Maximum supported length is 100 characters.
        self._display_name: Optional[str] = None
        # The last day of the year using ISO 8601 format for date.
        self._end_date: Optional[date] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The first day of the year using ISO 8601 format for date.
        self._start_date: Optional[date] = None
        # The year property
        self._year: Optional[year_reference_value.YearReferenceValue] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> YearTimePeriodDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: YearTimePeriodDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return YearTimePeriodDefinition()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the year. Maximum supported length is 100 characters.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the year. Maximum supported length is 100 characters.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def end_date(self,) -> Optional[date]:
        """
        Gets the endDate property value. The last day of the year using ISO 8601 format for date.
        Returns: Optional[date]
        """
        return self._end_date
    
    @end_date.setter
    def end_date(self,value: Optional[date] = None) -> None:
        """
        Sets the endDate property value. The last day of the year using ISO 8601 format for date.
        Args:
            value: Value to set for the end_date property.
        """
        self._end_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import year_reference_value
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDate": lambda n : setattr(self, 'end_date', n.get_date_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
            "year": lambda n : setattr(self, 'year', n.get_object_value(year_reference_value.YearReferenceValue)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_date_value("endDate", self.end_date)
        writer.write_date_value("startDate", self.start_date)
        writer.write_object_value("year", self.year)
    
    @property
    def start_date(self,) -> Optional[date]:
        """
        Gets the startDate property value. The first day of the year using ISO 8601 format for date.
        Returns: Optional[date]
        """
        return self._start_date
    
    @start_date.setter
    def start_date(self,value: Optional[date] = None) -> None:
        """
        Sets the startDate property value. The first day of the year using ISO 8601 format for date.
        Args:
            value: Value to set for the start_date property.
        """
        self._start_date = value
    
    @property
    def year(self,) -> Optional[year_reference_value.YearReferenceValue]:
        """
        Gets the year property value. The year property
        Returns: Optional[year_reference_value.YearReferenceValue]
        """
        return self._year
    
    @year.setter
    def year(self,value: Optional[year_reference_value.YearReferenceValue] = None) -> None:
        """
        Sets the year property value. The year property
        Args:
            value: Value to set for the year property.
        """
        self._year = value
    

