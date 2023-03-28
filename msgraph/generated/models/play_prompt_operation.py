from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import comms_operation, play_prompt_completion_reason

from . import comms_operation

class PlayPromptOperation(comms_operation.CommsOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new PlayPromptOperation and sets the default values.
        """
        super().__init__()
        # Possible values are: unknown, completedSuccessfully, mediaOperationCanceled.
        self._completion_reason: Optional[play_prompt_completion_reason.PlayPromptCompletionReason] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def completion_reason(self,) -> Optional[play_prompt_completion_reason.PlayPromptCompletionReason]:
        """
        Gets the completionReason property value. Possible values are: unknown, completedSuccessfully, mediaOperationCanceled.
        Returns: Optional[play_prompt_completion_reason.PlayPromptCompletionReason]
        """
        return self._completion_reason
    
    @completion_reason.setter
    def completion_reason(self,value: Optional[play_prompt_completion_reason.PlayPromptCompletionReason] = None) -> None:
        """
        Sets the completionReason property value. Possible values are: unknown, completedSuccessfully, mediaOperationCanceled.
        Args:
            value: Value to set for the completion_reason property.
        """
        self._completion_reason = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlayPromptOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlayPromptOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlayPromptOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import comms_operation, play_prompt_completion_reason

        fields: Dict[str, Callable[[Any], None]] = {
            "completionReason": lambda n : setattr(self, 'completion_reason', n.get_enum_value(play_prompt_completion_reason.PlayPromptCompletionReason)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("completionReason", self.completion_reason)
    

