from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SetPresencePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The activity property
    activity: Optional[str] = None
    # The availability property
    availability: Optional[str] = None
    # The expirationDuration property
    expiration_duration: Optional[datetime.timedelta] = None
    # The sessionId property
    session_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SetPresencePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SetPresencePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SetPresencePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_str_value()),
            "availability": lambda n : setattr(self, 'availability', n.get_str_value()),
            "expirationDuration": lambda n : setattr(self, 'expiration_duration', n.get_timedelta_value()),
            "sessionId": lambda n : setattr(self, 'session_id', n.get_str_value()),
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
        writer.write_str_value("activity", self.activity)
        writer.write_str_value("availability", self.availability)
        writer.write_timedelta_value("expirationDuration", self.expiration_duration)
        writer.write_str_value("sessionId", self.session_id)
        writer.write_additional_data_value(self.additional_data)
    

