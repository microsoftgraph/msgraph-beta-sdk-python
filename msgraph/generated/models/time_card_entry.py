from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

time_card_break = lazy_import('msgraph.generated.models.time_card_break')
time_card_event = lazy_import('msgraph.generated.models.time_card_event')

class TimeCardEntry(AdditionalDataHolder, Parsable):
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
    def breaks(self,) -> Optional[List[time_card_break.TimeCardBreak]]:
        """
        Gets the breaks property value. The list of breaks associated with the timeCard.
        Returns: Optional[List[time_card_break.TimeCardBreak]]
        """
        return self._breaks
    
    @breaks.setter
    def breaks(self,value: Optional[List[time_card_break.TimeCardBreak]] = None) -> None:
        """
        Sets the breaks property value. The list of breaks associated with the timeCard.
        Args:
            value: Value to set for the breaks property.
        """
        self._breaks = value
    
    @property
    def clock_in_event(self,) -> Optional[time_card_event.TimeCardEvent]:
        """
        Gets the clockInEvent property value. The clock-in event of the timeCard.
        Returns: Optional[time_card_event.TimeCardEvent]
        """
        return self._clock_in_event
    
    @clock_in_event.setter
    def clock_in_event(self,value: Optional[time_card_event.TimeCardEvent] = None) -> None:
        """
        Sets the clockInEvent property value. The clock-in event of the timeCard.
        Args:
            value: Value to set for the clockInEvent property.
        """
        self._clock_in_event = value
    
    @property
    def clock_out_event(self,) -> Optional[time_card_event.TimeCardEvent]:
        """
        Gets the clockOutEvent property value. The clock-out event of the timeCard.
        Returns: Optional[time_card_event.TimeCardEvent]
        """
        return self._clock_out_event
    
    @clock_out_event.setter
    def clock_out_event(self,value: Optional[time_card_event.TimeCardEvent] = None) -> None:
        """
        Sets the clockOutEvent property value. The clock-out event of the timeCard.
        Args:
            value: Value to set for the clockOutEvent property.
        """
        self._clock_out_event = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new timeCardEntry and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The list of breaks associated with the timeCard.
        self._breaks: Optional[List[time_card_break.TimeCardBreak]] = None
        # The clock-in event of the timeCard.
        self._clock_in_event: Optional[time_card_event.TimeCardEvent] = None
        # The clock-out event of the timeCard.
        self._clock_out_event: Optional[time_card_event.TimeCardEvent] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeCardEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TimeCardEntry
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TimeCardEntry()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "breaks": lambda n : setattr(self, 'breaks', n.get_collection_of_object_values(time_card_break.TimeCardBreak)),
            "clock_in_event": lambda n : setattr(self, 'clock_in_event', n.get_object_value(time_card_event.TimeCardEvent)),
            "clock_out_event": lambda n : setattr(self, 'clock_out_event', n.get_object_value(time_card_event.TimeCardEvent)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("breaks", self.breaks)
        writer.write_object_value("clockInEvent", self.clock_in_event)
        writer.write_object_value("clockOutEvent", self.clock_out_event)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

