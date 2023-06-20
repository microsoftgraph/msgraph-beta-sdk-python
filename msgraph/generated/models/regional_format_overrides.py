from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class RegionalFormatOverrides(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The calendar to use, e.g., Gregorian Calendar.Returned by default.
    calendar: Optional[str] = None
    # The first day of the week to use, e.g., Sunday.Returned by default.
    first_day_of_week: Optional[str] = None
    # The long date time format to be used for displaying dates.Returned by default.
    long_date_format: Optional[str] = None
    # The long time format to be used for displaying time.Returned by default.
    long_time_format: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The short date time format to be used for displaying dates.Returned by default.
    short_date_format: Optional[str] = None
    # The short time format to be used for displaying time.Returned by default.
    short_time_format: Optional[str] = None
    # The timezone to be used for displaying time.Returned by default.
    time_zone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RegionalFormatOverrides:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RegionalFormatOverrides
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RegionalFormatOverrides()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "calendar": lambda n : setattr(self, 'calendar', n.get_str_value()),
            "firstDayOfWeek": lambda n : setattr(self, 'first_day_of_week', n.get_str_value()),
            "longDateFormat": lambda n : setattr(self, 'long_date_format', n.get_str_value()),
            "longTimeFormat": lambda n : setattr(self, 'long_time_format', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "shortDateFormat": lambda n : setattr(self, 'short_date_format', n.get_str_value()),
            "shortTimeFormat": lambda n : setattr(self, 'short_time_format', n.get_str_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("calendar", self.calendar)
        writer.write_str_value("firstDayOfWeek", self.first_day_of_week)
        writer.write_str_value("longDateFormat", self.long_date_format)
        writer.write_str_value("longTimeFormat", self.long_time_format)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("shortDateFormat", self.short_date_format)
        writer.write_str_value("shortTimeFormat", self.short_time_format)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_additional_data_value(self.additional_data)
    

