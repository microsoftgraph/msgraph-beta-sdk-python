from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class DateTimeTimeZone(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new dateTimeTimeZone and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A single point of time in a combined date and time representation ({date}T{time}). For example, '2019-04-16T09:00:00'.
        self._date_time: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Represents a time zone, for example, 'Pacific Standard Time'. See below for possible values.
        self._time_zone: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DateTimeTimeZone:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DateTimeTimeZone
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DateTimeTimeZone()
    
    @property
    def date_time(self,) -> Optional[str]:
        """
        Gets the dateTime property value. A single point of time in a combined date and time representation ({date}T{time}). For example, '2019-04-16T09:00:00'.
        Returns: Optional[str]
        """
        return self._date_time
    
    @date_time.setter
    def date_time(self,value: Optional[str] = None) -> None:
        """
        Sets the dateTime property value. A single point of time in a combined date and time representation ({date}T{time}). For example, '2019-04-16T09:00:00'.
        Args:
            value: Value to set for the date_time property.
        """
        self._date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "dateTime": lambda n : setattr(self, 'date_time', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("dateTime", self.date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def time_zone(self,) -> Optional[str]:
        """
        Gets the timeZone property value. Represents a time zone, for example, 'Pacific Standard Time'. See below for possible values.
        Returns: Optional[str]
        """
        return self._time_zone
    
    @time_zone.setter
    def time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the timeZone property value. Represents a time zone, for example, 'Pacific Standard Time'. See below for possible values.
        Args:
            value: Value to set for the time_zone property.
        """
        self._time_zone = value
    

