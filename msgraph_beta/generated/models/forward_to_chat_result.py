from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_result_part import ActionResultPart

from .action_result_part import ActionResultPart

@dataclass
class ForwardToChatResult(ActionResultPart, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.forwardToChatResult"
    # The chatMessage ID generated after a message is successfully forwarded to the target chat ID.
    forwarded_message_id: Optional[str] = None
    # The target chat ID where the message was forwarded.
    target_chat_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ForwardToChatResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ForwardToChatResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ForwardToChatResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .action_result_part import ActionResultPart

        from .action_result_part import ActionResultPart

        fields: dict[str, Callable[[Any], None]] = {
            "forwardedMessageId": lambda n : setattr(self, 'forwarded_message_id', n.get_str_value()),
            "targetChatId": lambda n : setattr(self, 'target_chat_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("forwardedMessageId", self.forwarded_message_id)
        writer.write_str_value("targetChatId", self.target_chat_id)
    

