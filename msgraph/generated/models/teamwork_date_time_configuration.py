from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TeamworkDateTimeConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The date format for the device.
    date_format: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The time of the day when the device is turned off.
    office_hours_end_time: Optional[datetime.time] = None
    # The time of the day when the device is turned on.
    office_hours_start_time: Optional[datetime.time] = None
    # The time format for the device.
    time_format: Optional[str] = None
    # The time zone to which the office hours apply.
    time_zone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkDateTimeConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDateTimeConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkDateTimeConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "dateFormat": lambda n : setattr(self, 'date_format', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "officeHoursEndTime": lambda n : setattr(self, 'office_hours_end_time', n.get_time_value()),
            "officeHoursStartTime": lambda n : setattr(self, 'office_hours_start_time', n.get_time_value()),
            "timeFormat": lambda n : setattr(self, 'time_format', n.get_str_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("dateFormat", self.date_format)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_time_value("officeHoursEndTime", self.office_hours_end_time)
        writer.write_time_value("officeHoursStartTime", self.office_hours_start_time)
        writer.write_str_value("timeFormat", self.time_format)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_additional_data_value(self.additional_data)
    

