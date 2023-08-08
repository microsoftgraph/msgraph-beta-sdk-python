from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.incoming_call_options import IncomingCallOptions
    from .....models.media_config import MediaConfig
    from .....models.modality import Modality

@dataclass
class AnswerPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The acceptedModalities property
    accepted_modalities: Optional[List[Modality]] = None
    # The callOptions property
    call_options: Optional[IncomingCallOptions] = None
    # The callbackUri property
    callback_uri: Optional[str] = None
    # The mediaConfig property
    media_config: Optional[MediaConfig] = None
    # The participantCapacity property
    participant_capacity: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AnswerPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnswerPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AnswerPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.incoming_call_options import IncomingCallOptions
        from .....models.media_config import MediaConfig
        from .....models.modality import Modality

        from .....models.incoming_call_options import IncomingCallOptions
        from .....models.media_config import MediaConfig
        from .....models.modality import Modality

        fields: Dict[str, Callable[[Any], None]] = {
            "acceptedModalities": lambda n : setattr(self, 'accepted_modalities', n.get_collection_of_enum_values(Modality)),
            "callOptions": lambda n : setattr(self, 'call_options', n.get_object_value(IncomingCallOptions)),
            "callbackUri": lambda n : setattr(self, 'callback_uri', n.get_str_value()),
            "mediaConfig": lambda n : setattr(self, 'media_config', n.get_object_value(MediaConfig)),
            "participantCapacity": lambda n : setattr(self, 'participant_capacity', n.get_int_value()),
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
        writer.write_collection_of_enum_values("acceptedModalities", self.accepted_modalities)
        writer.write_object_value("callOptions", self.call_options)
        writer.write_str_value("callbackUri", self.callback_uri)
        writer.write_object_value("mediaConfig", self.media_config)
        writer.write_int_value("participantCapacity", self.participant_capacity)
        writer.write_additional_data_value(self.additional_data)
    

