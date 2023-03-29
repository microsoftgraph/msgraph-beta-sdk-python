from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_event_handler_result

from . import authentication_event_handler_result

class CustomExtensionCalloutResult(authentication_event_handler_result.AuthenticationEventHandlerResult):
    def __init__(self,) -> None:
        """
        Instantiates a new CustomExtensionCalloutResult and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.customExtensionCalloutResult"
        # When the API transaction was initiated, the date and time information uses ISO 8601 format and is always in UTC time. Example: midnight on Jan 1, 2014, is reported as 2014-01-01T00:00:00Z.
        self._callout_date_time: Optional[datetime] = None
        # Identifier of the custom extension that was called.
        self._custom_extension_id: Optional[str] = None
        # Error code that was returned when the last API attempt failed.
        self._error_code: Optional[int] = None
        # The HTTP status code that was returned by the target API endpoint after the last API attempt.
        self._http_status: Optional[int] = None
        # The number of API calls to the customer's API.
        self._number_of_attempts: Optional[int] = None
    
    @property
    def callout_date_time(self,) -> Optional[datetime]:
        """
        Gets the calloutDateTime property value. When the API transaction was initiated, the date and time information uses ISO 8601 format and is always in UTC time. Example: midnight on Jan 1, 2014, is reported as 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._callout_date_time
    
    @callout_date_time.setter
    def callout_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the calloutDateTime property value. When the API transaction was initiated, the date and time information uses ISO 8601 format and is always in UTC time. Example: midnight on Jan 1, 2014, is reported as 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the callout_date_time property.
        """
        self._callout_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomExtensionCalloutResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionCalloutResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomExtensionCalloutResult()
    
    @property
    def custom_extension_id(self,) -> Optional[str]:
        """
        Gets the customExtensionId property value. Identifier of the custom extension that was called.
        Returns: Optional[str]
        """
        return self._custom_extension_id
    
    @custom_extension_id.setter
    def custom_extension_id(self,value: Optional[str] = None) -> None:
        """
        Sets the customExtensionId property value. Identifier of the custom extension that was called.
        Args:
            value: Value to set for the custom_extension_id property.
        """
        self._custom_extension_id = value
    
    @property
    def error_code(self,) -> Optional[int]:
        """
        Gets the errorCode property value. Error code that was returned when the last API attempt failed.
        Returns: Optional[int]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCode property value. Error code that was returned when the last API attempt failed.
        Args:
            value: Value to set for the error_code property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_event_handler_result

        fields: Dict[str, Callable[[Any], None]] = {
            "calloutDateTime": lambda n : setattr(self, 'callout_date_time', n.get_datetime_value()),
            "customExtensionId": lambda n : setattr(self, 'custom_extension_id', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "httpStatus": lambda n : setattr(self, 'http_status', n.get_int_value()),
            "numberOfAttempts": lambda n : setattr(self, 'number_of_attempts', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def http_status(self,) -> Optional[int]:
        """
        Gets the httpStatus property value. The HTTP status code that was returned by the target API endpoint after the last API attempt.
        Returns: Optional[int]
        """
        return self._http_status
    
    @http_status.setter
    def http_status(self,value: Optional[int] = None) -> None:
        """
        Sets the httpStatus property value. The HTTP status code that was returned by the target API endpoint after the last API attempt.
        Args:
            value: Value to set for the http_status property.
        """
        self._http_status = value
    
    @property
    def number_of_attempts(self,) -> Optional[int]:
        """
        Gets the numberOfAttempts property value. The number of API calls to the customer's API.
        Returns: Optional[int]
        """
        return self._number_of_attempts
    
    @number_of_attempts.setter
    def number_of_attempts(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfAttempts property value. The number of API calls to the customer's API.
        Args:
            value: Value to set for the number_of_attempts property.
        """
        self._number_of_attempts = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("calloutDateTime", self.callout_date_time)
        writer.write_str_value("customExtensionId", self.custom_extension_id)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_int_value("httpStatus", self.http_status)
        writer.write_int_value("numberOfAttempts", self.number_of_attempts)
    

