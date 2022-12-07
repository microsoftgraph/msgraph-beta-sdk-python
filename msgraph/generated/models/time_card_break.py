from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_body = lazy_import('msgraph.generated.models.item_body')
time_card_event = lazy_import('msgraph.generated.models.time_card_event')

class TimeCardBreak(AdditionalDataHolder, Parsable):
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
    def break_id(self,) -> Optional[str]:
        """
        Gets the breakId property value. ID of the timeCardBreak.
        Returns: Optional[str]
        """
        return self._break_id
    
    @break_id.setter
    def break_id(self,value: Optional[str] = None) -> None:
        """
        Sets the breakId property value. ID of the timeCardBreak.
        Args:
            value: Value to set for the breakId property.
        """
        self._break_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new timeCardBreak and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # ID of the timeCardBreak.
        self._break_id: Optional[str] = None
        # The start event of the timeCardBreak.
        self._end: Optional[time_card_event.TimeCardEvent] = None
        # Notes about the timeCardBreak.
        self._notes: Optional[item_body.ItemBody] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The start property
        self._start: Optional[time_card_event.TimeCardEvent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeCardBreak:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TimeCardBreak
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TimeCardBreak()
    
    @property
    def end(self,) -> Optional[time_card_event.TimeCardEvent]:
        """
        Gets the end property value. The start event of the timeCardBreak.
        Returns: Optional[time_card_event.TimeCardEvent]
        """
        return self._end
    
    @end.setter
    def end(self,value: Optional[time_card_event.TimeCardEvent] = None) -> None:
        """
        Sets the end property value. The start event of the timeCardBreak.
        Args:
            value: Value to set for the end property.
        """
        self._end = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "break_id": lambda n : setattr(self, 'break_id', n.get_str_value()),
            "end": lambda n : setattr(self, 'end', n.get_object_value(time_card_event.TimeCardEvent)),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(item_body.ItemBody)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start": lambda n : setattr(self, 'start', n.get_object_value(time_card_event.TimeCardEvent)),
        }
        return fields
    
    @property
    def notes(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the notes property value. Notes about the timeCardBreak.
        Returns: Optional[item_body.ItemBody]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the notes property value. Notes about the timeCardBreak.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
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
        writer.write_str_value("breakId", self.break_id)
        writer.write_object_value("end", self.end)
        writer.write_object_value("notes", self.notes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("start", self.start)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start(self,) -> Optional[time_card_event.TimeCardEvent]:
        """
        Gets the start property value. The start property
        Returns: Optional[time_card_event.TimeCardEvent]
        """
        return self._start
    
    @start.setter
    def start(self,value: Optional[time_card_event.TimeCardEvent] = None) -> None:
        """
        Sets the start property value. The start property
        Args:
            value: Value to set for the start property.
        """
        self._start = value
    

