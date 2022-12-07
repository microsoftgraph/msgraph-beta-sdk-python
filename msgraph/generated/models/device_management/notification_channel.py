from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

notification_channel_type = lazy_import('msgraph.generated.models.device_management.notification_channel_type')
notification_receiver = lazy_import('msgraph.generated.models.device_management.notification_receiver')

class NotificationChannel(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new notificationChannel and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The type of the notification channel. The possible values are: portal, email, phoneCall, sms, unknownFutureValue.
        self._notification_channel_type: Optional[notification_channel_type.NotificationChannelType] = None
        # Information about the notification receivers, such as locale and contact information. For example, en-us for locale and serena.davis@contoso.com for contact information.
        self._notification_receivers: Optional[List[notification_receiver.NotificationReceiver]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The contact information about the notification receivers, such as email addresses. For portal notifications, receivers can be left blank. For email notifications, receivers consists of email addresses such as serena.davis@contoso.com.
        self._receivers: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NotificationChannel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NotificationChannel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NotificationChannel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "notification_channel_type": lambda n : setattr(self, 'notification_channel_type', n.get_enum_value(notification_channel_type.NotificationChannelType)),
            "notification_receivers": lambda n : setattr(self, 'notification_receivers', n.get_collection_of_object_values(notification_receiver.NotificationReceiver)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "receivers": lambda n : setattr(self, 'receivers', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def notification_channel_type(self,) -> Optional[notification_channel_type.NotificationChannelType]:
        """
        Gets the notificationChannelType property value. The type of the notification channel. The possible values are: portal, email, phoneCall, sms, unknownFutureValue.
        Returns: Optional[notification_channel_type.NotificationChannelType]
        """
        return self._notification_channel_type
    
    @notification_channel_type.setter
    def notification_channel_type(self,value: Optional[notification_channel_type.NotificationChannelType] = None) -> None:
        """
        Sets the notificationChannelType property value. The type of the notification channel. The possible values are: portal, email, phoneCall, sms, unknownFutureValue.
        Args:
            value: Value to set for the notificationChannelType property.
        """
        self._notification_channel_type = value
    
    @property
    def notification_receivers(self,) -> Optional[List[notification_receiver.NotificationReceiver]]:
        """
        Gets the notificationReceivers property value. Information about the notification receivers, such as locale and contact information. For example, en-us for locale and serena.davis@contoso.com for contact information.
        Returns: Optional[List[notification_receiver.NotificationReceiver]]
        """
        return self._notification_receivers
    
    @notification_receivers.setter
    def notification_receivers(self,value: Optional[List[notification_receiver.NotificationReceiver]] = None) -> None:
        """
        Sets the notificationReceivers property value. Information about the notification receivers, such as locale and contact information. For example, en-us for locale and serena.davis@contoso.com for contact information.
        Args:
            value: Value to set for the notificationReceivers property.
        """
        self._notification_receivers = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def receivers(self,) -> Optional[List[str]]:
        """
        Gets the receivers property value. The contact information about the notification receivers, such as email addresses. For portal notifications, receivers can be left blank. For email notifications, receivers consists of email addresses such as serena.davis@contoso.com.
        Returns: Optional[List[str]]
        """
        return self._receivers
    
    @receivers.setter
    def receivers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the receivers property value. The contact information about the notification receivers, such as email addresses. For portal notifications, receivers can be left blank. For email notifications, receivers consists of email addresses such as serena.davis@contoso.com.
        Args:
            value: Value to set for the receivers property.
        """
        self._receivers = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("notificationChannelType", self.notification_channel_type)
        writer.write_collection_of_object_values("notificationReceivers", self.notification_receivers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("receivers", self.receivers)
        writer.write_additional_data_value(self.additional_data)
    

