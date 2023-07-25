from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.item_body import ItemBody
    from .....models.key_value_pair import KeyValuePair
    from .....models.teamwork_activity_topic import TeamworkActivityTopic

@dataclass
class SendActivityNotificationPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The activityType property
    activity_type: Optional[str] = None
    # The chainId property
    chain_id: Optional[int] = None
    # The previewText property
    preview_text: Optional[ItemBody] = None
    # The templateParameters property
    template_parameters: Optional[List[KeyValuePair]] = None
    # The topic property
    topic: Optional[TeamworkActivityTopic] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SendActivityNotificationPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SendActivityNotificationPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SendActivityNotificationPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.item_body import ItemBody
        from .....models.key_value_pair import KeyValuePair
        from .....models.teamwork_activity_topic import TeamworkActivityTopic

        from .....models.item_body import ItemBody
        from .....models.key_value_pair import KeyValuePair
        from .....models.teamwork_activity_topic import TeamworkActivityTopic

        fields: Dict[str, Callable[[Any], None]] = {
            "activityType": lambda n : setattr(self, 'activity_type', n.get_str_value()),
            "chainId": lambda n : setattr(self, 'chain_id', n.get_int_value()),
            "previewText": lambda n : setattr(self, 'preview_text', n.get_object_value(ItemBody)),
            "templateParameters": lambda n : setattr(self, 'template_parameters', n.get_collection_of_object_values(KeyValuePair)),
            "topic": lambda n : setattr(self, 'topic', n.get_object_value(TeamworkActivityTopic)),
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
        writer.write_str_value("activityType", self.activity_type)
        writer.write_int_value("chainId", self.chain_id)
        writer.write_object_value("previewText", self.preview_text)
        writer.write_collection_of_object_values("templateParameters", self.template_parameters)
        writer.write_object_value("topic", self.topic)
        writer.write_additional_data_value(self.additional_data)
    

