from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class AndroidDeviceOwnerSystemUpdateFreezePeriod(AdditionalDataHolder, Parsable):
    """
    Represents one item in the list of freeze periods for Android Device Owner system updates
    """
    def __init__(self,) -> None:
        """
        Instantiates a new androidDeviceOwnerSystemUpdateFreezePeriod and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The day of the end date of the freeze period. Valid values 1 to 31
        self._end_day: Optional[int] = None
        # The month of the end date of the freeze period. Valid values 1 to 12
        self._end_month: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The day of the start date of the freeze period. Valid values 1 to 31
        self._start_day: Optional[int] = None
        # The month of the start date of the freeze period. Valid values 1 to 12
        self._start_month: Optional[int] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerSystemUpdateFreezePeriod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerSystemUpdateFreezePeriod
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerSystemUpdateFreezePeriod()
    
    @property
    def end_day(self,) -> Optional[int]:
        """
        Gets the endDay property value. The day of the end date of the freeze period. Valid values 1 to 31
        Returns: Optional[int]
        """
        return self._end_day
    
    @end_day.setter
    def end_day(self,value: Optional[int] = None) -> None:
        """
        Sets the endDay property value. The day of the end date of the freeze period. Valid values 1 to 31
        Args:
            value: Value to set for the end_day property.
        """
        self._end_day = value
    
    @property
    def end_month(self,) -> Optional[int]:
        """
        Gets the endMonth property value. The month of the end date of the freeze period. Valid values 1 to 12
        Returns: Optional[int]
        """
        return self._end_month
    
    @end_month.setter
    def end_month(self,value: Optional[int] = None) -> None:
        """
        Sets the endMonth property value. The month of the end date of the freeze period. Valid values 1 to 12
        Args:
            value: Value to set for the end_month property.
        """
        self._end_month = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "endDay": lambda n : setattr(self, 'end_day', n.get_int_value()),
            "endMonth": lambda n : setattr(self, 'end_month', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDay": lambda n : setattr(self, 'start_day', n.get_int_value()),
            "startMonth": lambda n : setattr(self, 'start_month', n.get_int_value()),
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
        writer.write_int_value("endDay", self.end_day)
        writer.write_int_value("endMonth", self.end_month)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("startDay", self.start_day)
        writer.write_int_value("startMonth", self.start_month)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_day(self,) -> Optional[int]:
        """
        Gets the startDay property value. The day of the start date of the freeze period. Valid values 1 to 31
        Returns: Optional[int]
        """
        return self._start_day
    
    @start_day.setter
    def start_day(self,value: Optional[int] = None) -> None:
        """
        Sets the startDay property value. The day of the start date of the freeze period. Valid values 1 to 31
        Args:
            value: Value to set for the start_day property.
        """
        self._start_day = value
    
    @property
    def start_month(self,) -> Optional[int]:
        """
        Gets the startMonth property value. The month of the start date of the freeze period. Valid values 1 to 12
        Returns: Optional[int]
        """
        return self._start_month
    
    @start_month.setter
    def start_month(self,value: Optional[int] = None) -> None:
        """
        Sets the startMonth property value. The month of the start date of the freeze period. Valid values 1 to 12
        Args:
            value: Value to set for the start_month property.
        """
        self._start_month = value
    

