from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_event_handler_result = lazy_import('msgraph.generated.models.authentication_event_handler_result')

class CustomExtensionCalloutResult(authentication_event_handler_result.AuthenticationEventHandlerResult):
    @property
    def callout_date_time(self,) -> Optional[datetime]:
        """
        Gets the calloutDateTime property value. The calloutDateTime property
        Returns: Optional[datetime]
        """
        return self._callout_date_time
    
    @callout_date_time.setter
    def callout_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the calloutDateTime property value. The calloutDateTime property
        Args:
            value: Value to set for the calloutDateTime property.
        """
        self._callout_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CustomExtensionCalloutResult and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.customExtensionCalloutResult"
        # The calloutDateTime property
        self._callout_date_time: Optional[datetime] = None
        # The customExtensionId property
        self._custom_extension_id: Optional[str] = None
        # The errorCode property
        self._error_code: Optional[int] = None
        # The httpStatus property
        self._http_status: Optional[int] = None
        # The numberOfAttempts property
        self._number_of_attempts: Optional[int] = None
    
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
        Gets the customExtensionId property value. The customExtensionId property
        Returns: Optional[str]
        """
        return self._custom_extension_id
    
    @custom_extension_id.setter
    def custom_extension_id(self,value: Optional[str] = None) -> None:
        """
        Sets the customExtensionId property value. The customExtensionId property
        Args:
            value: Value to set for the customExtensionId property.
        """
        self._custom_extension_id = value
    
    @property
    def error_code(self,) -> Optional[int]:
        """
        Gets the errorCode property value. The errorCode property
        Returns: Optional[int]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCode property value. The errorCode property
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "callout_date_time": lambda n : setattr(self, 'callout_date_time', n.get_datetime_value()),
            "custom_extension_id": lambda n : setattr(self, 'custom_extension_id', n.get_str_value()),
            "error_code": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "http_status": lambda n : setattr(self, 'http_status', n.get_int_value()),
            "number_of_attempts": lambda n : setattr(self, 'number_of_attempts', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def http_status(self,) -> Optional[int]:
        """
        Gets the httpStatus property value. The httpStatus property
        Returns: Optional[int]
        """
        return self._http_status
    
    @http_status.setter
    def http_status(self,value: Optional[int] = None) -> None:
        """
        Sets the httpStatus property value. The httpStatus property
        Args:
            value: Value to set for the httpStatus property.
        """
        self._http_status = value
    
    @property
    def number_of_attempts(self,) -> Optional[int]:
        """
        Gets the numberOfAttempts property value. The numberOfAttempts property
        Returns: Optional[int]
        """
        return self._number_of_attempts
    
    @number_of_attempts.setter
    def number_of_attempts(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfAttempts property value. The numberOfAttempts property
        Args:
            value: Value to set for the numberOfAttempts property.
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
    

