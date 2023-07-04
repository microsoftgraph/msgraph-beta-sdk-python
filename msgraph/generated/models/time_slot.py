from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .date_time_time_zone import DateTimeTimeZone

@dataclass
class TimeSlot(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The end property
    end: Optional[DateTimeTimeZone] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The start property
    start: Optional[DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeSlot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimeSlot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TimeSlot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .date_time_time_zone import DateTimeTimeZone

        from .date_time_time_zone import DateTimeTimeZone

        fields: Dict[str, Callable[[Any], None]] = {
            "end": lambda n : setattr(self, 'end', n.get_object_value(DateTimeTimeZone)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start": lambda n : setattr(self, 'start', n.get_object_value(DateTimeTimeZone)),
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
        writer.write_object_value("end", self.end)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("start", self.start)
        writer.write_additional_data_value(self.additional_data)
    

