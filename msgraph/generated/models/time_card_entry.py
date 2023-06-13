from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import time_card_break, time_card_event

@dataclass
class TimeCardEntry(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The list of breaks associated with the timeCard.
    breaks: Optional[List[time_card_break.TimeCardBreak]] = None
    # The clock-in event of the timeCard.
    clock_in_event: Optional[time_card_event.TimeCardEvent] = None
    # The clock-out event of the timeCard.
    clock_out_event: Optional[time_card_event.TimeCardEvent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
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
        from . import time_card_break, time_card_event

        fields: Dict[str, Callable[[Any], None]] = {
            "breaks": lambda n : setattr(self, 'breaks', n.get_collection_of_object_values(time_card_break.TimeCardBreak)),
            "clockInEvent": lambda n : setattr(self, 'clock_in_event', n.get_object_value(time_card_event.TimeCardEvent)),
            "clockOutEvent": lambda n : setattr(self, 'clock_out_event', n.get_object_value(time_card_event.TimeCardEvent)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
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
    

