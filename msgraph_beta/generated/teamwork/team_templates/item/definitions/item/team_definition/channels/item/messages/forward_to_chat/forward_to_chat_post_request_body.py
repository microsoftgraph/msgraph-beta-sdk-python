from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...........models.chat_message import ChatMessage

@dataclass
class ForwardToChatPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The additionalMessage property
    additional_message: Optional[ChatMessage] = None
    # The messageIds property
    message_ids: Optional[list[str]] = None
    # The targetChatIds property
    target_chat_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ForwardToChatPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ForwardToChatPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ForwardToChatPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...........models.chat_message import ChatMessage

        from ...........models.chat_message import ChatMessage

        fields: dict[str, Callable[[Any], None]] = {
            "additionalMessage": lambda n : setattr(self, 'additional_message', n.get_object_value(ChatMessage)),
            "messageIds": lambda n : setattr(self, 'message_ids', n.get_collection_of_primitive_values(str)),
            "targetChatIds": lambda n : setattr(self, 'target_chat_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("additionalMessage", self.additional_message)
        writer.write_collection_of_primitive_values("messageIds", self.message_ids)
        writer.write_collection_of_primitive_values("targetChatIds", self.target_chat_ids)
        writer.write_additional_data_value(self.additional_data)
    

