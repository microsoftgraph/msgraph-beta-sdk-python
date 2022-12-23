from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

date_time_time_zone = lazy_import('msgraph.generated.models.date_time_time_zone')
item_body = lazy_import('msgraph.generated.models.item_body')

class PresenceStatusMessage(AdditionalDataHolder, Parsable):
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
        Instantiates a new presenceStatusMessage and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Time in which the status message expires.If not provided, the status message does not expire.expiryDateTime.dateTime should not include time zone.expiryDateTime is not available when requesting presence of another user.
        self._expiry_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # Status message item. The only supported format currently is message.contentType = 'text'.
        self._message: Optional[item_body.ItemBody] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Time in which the status message was published.Read-only.publishedDateTime is not available when requesting presence of another user.
        self._published_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PresenceStatusMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PresenceStatusMessage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PresenceStatusMessage()
    
    @property
    def expiry_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the expiryDateTime property value. Time in which the status message expires.If not provided, the status message does not expire.expiryDateTime.dateTime should not include time zone.expiryDateTime is not available when requesting presence of another user.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._expiry_date_time
    
    @expiry_date_time.setter
    def expiry_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the expiryDateTime property value. Time in which the status message expires.If not provided, the status message does not expire.expiryDateTime.dateTime should not include time zone.expiryDateTime is not available when requesting presence of another user.
        Args:
            value: Value to set for the expiryDateTime property.
        """
        self._expiry_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "expiry_date_time": lambda n : setattr(self, 'expiry_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "message": lambda n : setattr(self, 'message', n.get_object_value(item_body.ItemBody)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "published_date_time": lambda n : setattr(self, 'published_date_time', n.get_datetime_value()),
        }
        return fields
    
    @property
    def message(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the message property value. Status message item. The only supported format currently is message.contentType = 'text'.
        Returns: Optional[item_body.ItemBody]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the message property value. Status message item. The only supported format currently is message.contentType = 'text'.
        Args:
            value: Value to set for the message property.
        """
        self._message = value
    
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
    def published_date_time(self,) -> Optional[datetime]:
        """
        Gets the publishedDateTime property value. Time in which the status message was published.Read-only.publishedDateTime is not available when requesting presence of another user.
        Returns: Optional[datetime]
        """
        return self._published_date_time
    
    @published_date_time.setter
    def published_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the publishedDateTime property value. Time in which the status message was published.Read-only.publishedDateTime is not available when requesting presence of another user.
        Args:
            value: Value to set for the publishedDateTime property.
        """
        self._published_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("expiryDateTime", self.expiry_date_time)
        writer.write_object_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("publishedDateTime", self.published_date_time)
        writer.write_additional_data_value(self.additional_data)
    

