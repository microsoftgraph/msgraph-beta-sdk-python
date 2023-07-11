from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .date_time_time_zone import DateTimeTimeZone
    from .item_body import ItemBody

@dataclass
class PresenceStatusMessage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Time in which the status message expires.If not provided, the status message does not expire.expiryDateTime.dateTime should not include time zone.expiryDateTime is not available when requesting presence of another user.
    expiry_date_time: Optional[DateTimeTimeZone] = None
    # Status message item. The only supported format currently is message.contentType = 'text'.
    message: Optional[ItemBody] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Time in which the status message was published.Read-only.publishedDateTime is not available when requesting presence of another user.
    published_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PresenceStatusMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PresenceStatusMessage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PresenceStatusMessage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .date_time_time_zone import DateTimeTimeZone
        from .item_body import ItemBody

        from .date_time_time_zone import DateTimeTimeZone
        from .item_body import ItemBody

        fields: Dict[str, Callable[[Any], None]] = {
            "expiryDateTime": lambda n : setattr(self, 'expiry_date_time', n.get_object_value(DateTimeTimeZone)),
            "message": lambda n : setattr(self, 'message', n.get_object_value(ItemBody)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "publishedDateTime": lambda n : setattr(self, 'published_date_time', n.get_datetime_value()),
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
        writer.write_object_value("expiryDateTime", self.expiry_date_time)
        writer.write_object_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("publishedDateTime", self.published_date_time)
        writer.write_additional_data_value(self.additional_data)
    

