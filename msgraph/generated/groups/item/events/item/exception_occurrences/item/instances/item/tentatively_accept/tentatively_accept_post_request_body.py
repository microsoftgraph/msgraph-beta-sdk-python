from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..........models.time_slot import TimeSlot

@dataclass
class TentativelyAcceptPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Comment property
    comment: Optional[str] = None
    # The ProposedNewTime property
    proposed_new_time: Optional[TimeSlot] = None
    # The SendResponse property
    send_response: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TentativelyAcceptPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TentativelyAcceptPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TentativelyAcceptPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..........models.time_slot import TimeSlot

        from ..........models.time_slot import TimeSlot

        fields: Dict[str, Callable[[Any], None]] = {
            "Comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "ProposedNewTime": lambda n : setattr(self, 'proposed_new_time', n.get_object_value(TimeSlot)),
            "SendResponse": lambda n : setattr(self, 'send_response', n.get_bool_value()),
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
        writer.write_str_value("Comment", self.comment)
        writer.write_object_value("ProposedNewTime", self.proposed_new_time)
        writer.write_bool_value("SendResponse", self.send_response)
        writer.write_additional_data_value(self.additional_data)
    

