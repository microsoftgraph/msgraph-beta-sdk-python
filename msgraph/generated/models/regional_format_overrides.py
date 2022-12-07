from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class RegionalFormatOverrides(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def calendar(self,) -> Optional[str]:
        """
        Gets the calendar property value. The calendar to use, e.g., Gregorian Calendar.Returned by default.
        Returns: Optional[str]
        """
        return self._calendar
    
    @calendar.setter
    def calendar(self,value: Optional[str] = None) -> None:
        """
        Sets the calendar property value. The calendar to use, e.g., Gregorian Calendar.Returned by default.
        Args:
            value: Value to set for the calendar property.
        """
        self._calendar = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new regionalFormatOverrides and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The calendar to use, e.g., Gregorian Calendar.Returned by default.
        self._calendar: Optional[str] = None
        # The first day of the week to use, e.g., Sunday.Returned by default.
        self._first_day_of_week: Optional[str] = None
        # The long date time format to be used for displaying dates.Returned by default.
        self._long_date_format: Optional[str] = None
        # The long time format to be used for displaying time.Returned by default.
        self._long_time_format: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The short date time format to be used for displaying dates.Returned by default.
        self._short_date_format: Optional[str] = None
        # The short time format to be used for displaying time.Returned by default.
        self._short_time_format: Optional[str] = None
        # The timezone to be used for displaying time.Returned by default.
        self._time_zone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RegionalFormatOverrides:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RegionalFormatOverrides
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RegionalFormatOverrides()
    
    @property
    def first_day_of_week(self,) -> Optional[str]:
        """
        Gets the firstDayOfWeek property value. The first day of the week to use, e.g., Sunday.Returned by default.
        Returns: Optional[str]
        """
        return self._first_day_of_week
    
    @first_day_of_week.setter
    def first_day_of_week(self,value: Optional[str] = None) -> None:
        """
        Sets the firstDayOfWeek property value. The first day of the week to use, e.g., Sunday.Returned by default.
        Args:
            value: Value to set for the firstDayOfWeek property.
        """
        self._first_day_of_week = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "calendar": lambda n : setattr(self, 'calendar', n.get_str_value()),
            "first_day_of_week": lambda n : setattr(self, 'first_day_of_week', n.get_str_value()),
            "long_date_format": lambda n : setattr(self, 'long_date_format', n.get_str_value()),
            "long_time_format": lambda n : setattr(self, 'long_time_format', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "short_date_format": lambda n : setattr(self, 'short_date_format', n.get_str_value()),
            "short_time_format": lambda n : setattr(self, 'short_time_format', n.get_str_value()),
            "time_zone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
        }
        return fields
    
    @property
    def long_date_format(self,) -> Optional[str]:
        """
        Gets the longDateFormat property value. The long date time format to be used for displaying dates.Returned by default.
        Returns: Optional[str]
        """
        return self._long_date_format
    
    @long_date_format.setter
    def long_date_format(self,value: Optional[str] = None) -> None:
        """
        Sets the longDateFormat property value. The long date time format to be used for displaying dates.Returned by default.
        Args:
            value: Value to set for the longDateFormat property.
        """
        self._long_date_format = value
    
    @property
    def long_time_format(self,) -> Optional[str]:
        """
        Gets the longTimeFormat property value. The long time format to be used for displaying time.Returned by default.
        Returns: Optional[str]
        """
        return self._long_time_format
    
    @long_time_format.setter
    def long_time_format(self,value: Optional[str] = None) -> None:
        """
        Sets the longTimeFormat property value. The long time format to be used for displaying time.Returned by default.
        Args:
            value: Value to set for the longTimeFormat property.
        """
        self._long_time_format = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("calendar", self.calendar)
        writer.write_str_value("firstDayOfWeek", self.first_day_of_week)
        writer.write_str_value("longDateFormat", self.long_date_format)
        writer.write_str_value("longTimeFormat", self.long_time_format)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("shortDateFormat", self.short_date_format)
        writer.write_str_value("shortTimeFormat", self.short_time_format)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def short_date_format(self,) -> Optional[str]:
        """
        Gets the shortDateFormat property value. The short date time format to be used for displaying dates.Returned by default.
        Returns: Optional[str]
        """
        return self._short_date_format
    
    @short_date_format.setter
    def short_date_format(self,value: Optional[str] = None) -> None:
        """
        Sets the shortDateFormat property value. The short date time format to be used for displaying dates.Returned by default.
        Args:
            value: Value to set for the shortDateFormat property.
        """
        self._short_date_format = value
    
    @property
    def short_time_format(self,) -> Optional[str]:
        """
        Gets the shortTimeFormat property value. The short time format to be used for displaying time.Returned by default.
        Returns: Optional[str]
        """
        return self._short_time_format
    
    @short_time_format.setter
    def short_time_format(self,value: Optional[str] = None) -> None:
        """
        Sets the shortTimeFormat property value. The short time format to be used for displaying time.Returned by default.
        Args:
            value: Value to set for the shortTimeFormat property.
        """
        self._short_time_format = value
    
    @property
    def time_zone(self,) -> Optional[str]:
        """
        Gets the timeZone property value. The timezone to be used for displaying time.Returned by default.
        Returns: Optional[str]
        """
        return self._time_zone
    
    @time_zone.setter
    def time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the timeZone property value. The timezone to be used for displaying time.Returned by default.
        Args:
            value: Value to set for the timeZone property.
        """
        self._time_zone = value
    

