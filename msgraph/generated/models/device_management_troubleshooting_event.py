from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_troubleshooting_error_details = lazy_import('msgraph.generated.models.device_management_troubleshooting_error_details')
entity = lazy_import('msgraph.generated.models.entity')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')

class DeviceManagementTroubleshootingEvent(entity.Entity):
    """
    Event representing an general failure.
    """
    @property
    def additional_information(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the additionalInformation property value. A set of string key and string value pairs which provides additional information on the Troubleshooting event
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._additional_information
    
    @additional_information.setter
    def additional_information(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the additionalInformation property value. A set of string key and string value pairs which provides additional information on the Troubleshooting event
        Args:
            value: Value to set for the additionalInformation property.
        """
        self._additional_information = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementTroubleshootingEvent and sets the default values.
        """
        super().__init__()
        # A set of string key and string value pairs which provides additional information on the Troubleshooting event
        self._additional_information: Optional[List[key_value_pair.KeyValuePair]] = None
        # Id used for tracing the failure in the service.
        self._correlation_id: Optional[str] = None
        # Time when the event occurred .
        self._event_date_time: Optional[datetime] = None
        # Event Name corresponding to the Troubleshooting Event. It is an Optional field
        self._event_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Object containing detailed information about the error and its remediation.
        self._troubleshooting_error_details: Optional[device_management_troubleshooting_error_details.DeviceManagementTroubleshootingErrorDetails] = None
    
    @property
    def correlation_id(self,) -> Optional[str]:
        """
        Gets the correlationId property value. Id used for tracing the failure in the service.
        Returns: Optional[str]
        """
        return self._correlation_id
    
    @correlation_id.setter
    def correlation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the correlationId property value. Id used for tracing the failure in the service.
        Args:
            value: Value to set for the correlationId property.
        """
        self._correlation_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementTroubleshootingEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementTroubleshootingEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementTroubleshootingEvent()
    
    @property
    def event_date_time(self,) -> Optional[datetime]:
        """
        Gets the eventDateTime property value. Time when the event occurred .
        Returns: Optional[datetime]
        """
        return self._event_date_time
    
    @event_date_time.setter
    def event_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the eventDateTime property value. Time when the event occurred .
        Args:
            value: Value to set for the eventDateTime property.
        """
        self._event_date_time = value
    
    @property
    def event_name(self,) -> Optional[str]:
        """
        Gets the eventName property value. Event Name corresponding to the Troubleshooting Event. It is an Optional field
        Returns: Optional[str]
        """
        return self._event_name
    
    @event_name.setter
    def event_name(self,value: Optional[str] = None) -> None:
        """
        Sets the eventName property value. Event Name corresponding to the Troubleshooting Event. It is an Optional field
        Args:
            value: Value to set for the eventName property.
        """
        self._event_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "additional_information": lambda n : setattr(self, 'additional_information', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "correlation_id": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "event_date_time": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "event_name": lambda n : setattr(self, 'event_name', n.get_str_value()),
            "troubleshooting_error_details": lambda n : setattr(self, 'troubleshooting_error_details', n.get_object_value(device_management_troubleshooting_error_details.DeviceManagementTroubleshootingErrorDetails)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("additionalInformation", self.additional_information)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("eventName", self.event_name)
        writer.write_object_value("troubleshootingErrorDetails", self.troubleshooting_error_details)
    
    @property
    def troubleshooting_error_details(self,) -> Optional[device_management_troubleshooting_error_details.DeviceManagementTroubleshootingErrorDetails]:
        """
        Gets the troubleshootingErrorDetails property value. Object containing detailed information about the error and its remediation.
        Returns: Optional[device_management_troubleshooting_error_details.DeviceManagementTroubleshootingErrorDetails]
        """
        return self._troubleshooting_error_details
    
    @troubleshooting_error_details.setter
    def troubleshooting_error_details(self,value: Optional[device_management_troubleshooting_error_details.DeviceManagementTroubleshootingErrorDetails] = None) -> None:
        """
        Sets the troubleshootingErrorDetails property value. Object containing detailed information about the error and its remediation.
        Args:
            value: Value to set for the troubleshootingErrorDetails property.
        """
        self._troubleshooting_error_details = value
    

