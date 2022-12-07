from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TeamworkDateTimeConfiguration(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkDateTimeConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The date format for the device.
        self._date_format: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The time of the day when the device is turned off.
        self._office_hours_end_time: Optional[Time] = None
        # The time of the day when the device is turned on.
        self._office_hours_start_time: Optional[Time] = None
        # The time format for the device.
        self._time_format: Optional[str] = None
        # The time zone to which the office hours apply.
        self._time_zone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkDateTimeConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDateTimeConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkDateTimeConfiguration()
    
    @property
    def date_format(self,) -> Optional[str]:
        """
        Gets the dateFormat property value. The date format for the device.
        Returns: Optional[str]
        """
        return self._date_format
    
    @date_format.setter
    def date_format(self,value: Optional[str] = None) -> None:
        """
        Sets the dateFormat property value. The date format for the device.
        Args:
            value: Value to set for the dateFormat property.
        """
        self._date_format = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "date_format": lambda n : setattr(self, 'date_format', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "office_hours_end_time": lambda n : setattr(self, 'office_hours_end_time', n.get_object_value(Time)),
            "office_hours_start_time": lambda n : setattr(self, 'office_hours_start_time', n.get_object_value(Time)),
            "time_format": lambda n : setattr(self, 'time_format', n.get_str_value()),
            "time_zone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
        }
        return fields
    
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
    
    @property
    def office_hours_end_time(self,) -> Optional[Time]:
        """
        Gets the officeHoursEndTime property value. The time of the day when the device is turned off.
        Returns: Optional[Time]
        """
        return self._office_hours_end_time
    
    @office_hours_end_time.setter
    def office_hours_end_time(self,value: Optional[Time] = None) -> None:
        """
        Sets the officeHoursEndTime property value. The time of the day when the device is turned off.
        Args:
            value: Value to set for the officeHoursEndTime property.
        """
        self._office_hours_end_time = value
    
    @property
    def office_hours_start_time(self,) -> Optional[Time]:
        """
        Gets the officeHoursStartTime property value. The time of the day when the device is turned on.
        Returns: Optional[Time]
        """
        return self._office_hours_start_time
    
    @office_hours_start_time.setter
    def office_hours_start_time(self,value: Optional[Time] = None) -> None:
        """
        Sets the officeHoursStartTime property value. The time of the day when the device is turned on.
        Args:
            value: Value to set for the officeHoursStartTime property.
        """
        self._office_hours_start_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("dateFormat", self.date_format)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("officeHoursEndTime", self.office_hours_end_time)
        writer.write_object_value("officeHoursStartTime", self.office_hours_start_time)
        writer.write_str_value("timeFormat", self.time_format)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def time_format(self,) -> Optional[str]:
        """
        Gets the timeFormat property value. The time format for the device.
        Returns: Optional[str]
        """
        return self._time_format
    
    @time_format.setter
    def time_format(self,value: Optional[str] = None) -> None:
        """
        Sets the timeFormat property value. The time format for the device.
        Args:
            value: Value to set for the timeFormat property.
        """
        self._time_format = value
    
    @property
    def time_zone(self,) -> Optional[str]:
        """
        Gets the timeZone property value. The time zone to which the office hours apply.
        Returns: Optional[str]
        """
        return self._time_zone
    
    @time_zone.setter
    def time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the timeZone property value. The time zone to which the office hours apply.
        Args:
            value: Value to set for the timeZone property.
        """
        self._time_zone = value
    

