from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .notification_channel_type import NotificationChannelType
    from .notification_receiver import NotificationReceiver

@dataclass
class NotificationChannel(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The type of the notification channel. The possible values are: portal, email, phoneCall, sms, unknownFutureValue.
    notification_channel_type: Optional[NotificationChannelType] = None
    # Information about the notification receivers, such as locale and contact information. For example, en-us for locale and serena.davis@contoso.com for contact information.
    notification_receivers: Optional[List[NotificationReceiver]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The contact information about the notification receivers, such as email addresses. For portal notifications, receivers can be left blank. For email notifications, receivers consists of email addresses such as serena.davis@contoso.com.
    receivers: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NotificationChannel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NotificationChannel
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return NotificationChannel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .notification_channel_type import NotificationChannelType
        from .notification_receiver import NotificationReceiver

        from .notification_channel_type import NotificationChannelType
        from .notification_receiver import NotificationReceiver

        fields: Dict[str, Callable[[Any], None]] = {
            "notificationChannelType": lambda n : setattr(self, 'notification_channel_type', n.get_enum_value(NotificationChannelType)),
            "notificationReceivers": lambda n : setattr(self, 'notification_receivers', n.get_collection_of_object_values(NotificationReceiver)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "receivers": lambda n : setattr(self, 'receivers', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("notificationChannelType", self.notification_channel_type)
        writer.write_collection_of_object_values("notificationReceivers", self.notification_receivers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("receivers", self.receivers)
        writer.write_additional_data_value(self.additional_data)
    

