from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class ValidatePropertiesPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The displayName property
    display_name: Optional[str] = None
    # The entityType property
    entity_type: Optional[str] = None
    # The mailNickname property
    mail_nickname: Optional[str] = None
    # The onBehalfOfUserId property
    on_behalf_of_user_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ValidatePropertiesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ValidatePropertiesPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ValidatePropertiesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "entityType": lambda n : setattr(self, 'entity_type', n.get_str_value()),
            "mailNickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "onBehalfOfUserId": lambda n : setattr(self, 'on_behalf_of_user_id', n.get_uuid_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("entityType", self.entity_type)
        writer.write_str_value("mailNickname", self.mail_nickname)
        writer.write_uuid_value("onBehalfOfUserId", self.on_behalf_of_user_id)
        writer.write_additional_data_value(self.additional_data)
    

