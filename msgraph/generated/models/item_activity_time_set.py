from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ItemActivityTimeSet(AdditionalDataHolder, Parsable):
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
        Instantiates a new itemActivityTimeSet and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The lastRecordedDateTime property
        self._last_recorded_date_time: Optional[datetime] = None
        # When the activity was observed to take place.
        self._observed_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # When the observation was recorded on the service.
        self._recorded_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemActivityTimeSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemActivityTimeSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemActivityTimeSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_recorded_date_time": lambda n : setattr(self, 'last_recorded_date_time', n.get_datetime_value()),
            "observed_date_time": lambda n : setattr(self, 'observed_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recorded_date_time": lambda n : setattr(self, 'recorded_date_time', n.get_datetime_value()),
        }
        return fields
    
    @property
    def last_recorded_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastRecordedDateTime property value. The lastRecordedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_recorded_date_time
    
    @last_recorded_date_time.setter
    def last_recorded_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRecordedDateTime property value. The lastRecordedDateTime property
        Args:
            value: Value to set for the lastRecordedDateTime property.
        """
        self._last_recorded_date_time = value
    
    @property
    def observed_date_time(self,) -> Optional[datetime]:
        """
        Gets the observedDateTime property value. When the activity was observed to take place.
        Returns: Optional[datetime]
        """
        return self._observed_date_time
    
    @observed_date_time.setter
    def observed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the observedDateTime property value. When the activity was observed to take place.
        Args:
            value: Value to set for the observedDateTime property.
        """
        self._observed_date_time = value
    
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
    def recorded_date_time(self,) -> Optional[datetime]:
        """
        Gets the recordedDateTime property value. When the observation was recorded on the service.
        Returns: Optional[datetime]
        """
        return self._recorded_date_time
    
    @recorded_date_time.setter
    def recorded_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the recordedDateTime property value. When the observation was recorded on the service.
        Args:
            value: Value to set for the recordedDateTime property.
        """
        self._recorded_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("lastRecordedDateTime", self.last_recorded_date_time)
        writer.write_datetime_value("observedDateTime", self.observed_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("recordedDateTime", self.recorded_date_time)
        writer.write_additional_data_value(self.additional_data)
    

