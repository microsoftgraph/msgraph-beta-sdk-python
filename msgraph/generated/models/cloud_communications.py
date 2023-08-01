from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .call import Call
    from .call_records.call_record import CallRecord
    from .online_meeting import OnlineMeeting
    from .presence import Presence

@dataclass
class CloudCommunications(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The callRecords property
    call_records: Optional[List[CallRecord]] = None
    # The calls property
    calls: Optional[List[Call]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The onlineMeetings property
    online_meetings: Optional[List[OnlineMeeting]] = None
    # The presences property
    presences: Optional[List[Presence]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudCommunications:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudCommunications
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudCommunications()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .call import Call
        from .call_records.call_record import CallRecord
        from .online_meeting import OnlineMeeting
        from .presence import Presence

        from .call import Call
        from .call_records.call_record import CallRecord
        from .online_meeting import OnlineMeeting
        from .presence import Presence

        fields: Dict[str, Callable[[Any], None]] = {
            "callRecords": lambda n : setattr(self, 'call_records', n.get_collection_of_object_values(CallRecord)),
            "calls": lambda n : setattr(self, 'calls', n.get_collection_of_object_values(Call)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "onlineMeetings": lambda n : setattr(self, 'online_meetings', n.get_collection_of_object_values(OnlineMeeting)),
            "presences": lambda n : setattr(self, 'presences', n.get_collection_of_object_values(Presence)),
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
        writer.write_collection_of_object_values("callRecords", self.call_records)
        writer.write_collection_of_object_values("calls", self.calls)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("onlineMeetings", self.online_meetings)
        writer.write_collection_of_object_values("presences", self.presences)
        writer.write_additional_data_value(self.additional_data)
    

