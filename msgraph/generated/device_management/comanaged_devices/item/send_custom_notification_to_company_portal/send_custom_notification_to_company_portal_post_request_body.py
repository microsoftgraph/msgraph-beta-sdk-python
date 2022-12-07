from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class SendCustomNotificationToCompanyPortalPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the sendCustomNotificationToCompanyPortal method.
    """
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
        Instantiates a new sendCustomNotificationToCompanyPortalPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The notificationBody property
        self._notification_body: Optional[str] = None
        # The notificationTitle property
        self._notification_title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SendCustomNotificationToCompanyPortalPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SendCustomNotificationToCompanyPortalPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SendCustomNotificationToCompanyPortalPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "notification_body": lambda n : setattr(self, 'notification_body', n.get_str_value()),
            "notification_title": lambda n : setattr(self, 'notification_title', n.get_str_value()),
        }
        return fields
    
    @property
    def notification_body(self,) -> Optional[str]:
        """
        Gets the notificationBody property value. The notificationBody property
        Returns: Optional[str]
        """
        return self._notification_body
    
    @notification_body.setter
    def notification_body(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationBody property value. The notificationBody property
        Args:
            value: Value to set for the notificationBody property.
        """
        self._notification_body = value
    
    @property
    def notification_title(self,) -> Optional[str]:
        """
        Gets the notificationTitle property value. The notificationTitle property
        Returns: Optional[str]
        """
        return self._notification_title
    
    @notification_title.setter
    def notification_title(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationTitle property value. The notificationTitle property
        Args:
            value: Value to set for the notificationTitle property.
        """
        self._notification_title = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("notificationBody", self.notification_body)
        writer.write_str_value("notificationTitle", self.notification_title)
        writer.write_additional_data_value(self.additional_data)
    

