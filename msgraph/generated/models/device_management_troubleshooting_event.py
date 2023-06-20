from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_vpp_token_troubleshooting_event, device_management_troubleshooting_error_details, enrollment_troubleshooting_event, entity, key_value_pair, mobile_app_troubleshooting_event

from . import entity

@dataclass
class DeviceManagementTroubleshootingEvent(entity.Entity):
    # A set of string key and string value pairs which provides additional information on the Troubleshooting event
    additional_information: Optional[List[key_value_pair.KeyValuePair]] = None
    # Id used for tracing the failure in the service.
    correlation_id: Optional[str] = None
    # Time when the event occurred .
    event_date_time: Optional[datetime] = None
    # Event Name corresponding to the Troubleshooting Event. It is an Optional field
    event_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Object containing detailed information about the error and its remediation.
    troubleshooting_error_details: Optional[device_management_troubleshooting_error_details.DeviceManagementTroubleshootingErrorDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementTroubleshootingEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementTroubleshootingEvent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleVppTokenTroubleshootingEvent".casefold():
            from . import apple_vpp_token_troubleshooting_event

            return apple_vpp_token_troubleshooting_event.AppleVppTokenTroubleshootingEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enrollmentTroubleshootingEvent".casefold():
            from . import enrollment_troubleshooting_event

            return enrollment_troubleshooting_event.EnrollmentTroubleshootingEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppTroubleshootingEvent".casefold():
            from . import mobile_app_troubleshooting_event

            return mobile_app_troubleshooting_event.MobileAppTroubleshootingEvent()
        return DeviceManagementTroubleshootingEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_vpp_token_troubleshooting_event, device_management_troubleshooting_error_details, enrollment_troubleshooting_event, entity, key_value_pair, mobile_app_troubleshooting_event

        from . import apple_vpp_token_troubleshooting_event, device_management_troubleshooting_error_details, enrollment_troubleshooting_event, entity, key_value_pair, mobile_app_troubleshooting_event

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "eventName": lambda n : setattr(self, 'event_name', n.get_str_value()),
            "troubleshootingErrorDetails": lambda n : setattr(self, 'troubleshooting_error_details', n.get_object_value(device_management_troubleshooting_error_details.DeviceManagementTroubleshootingErrorDetails)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("additionalInformation", self.additional_information)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("eventName", self.event_name)
        writer.write_object_value("troubleshootingErrorDetails", self.troubleshooting_error_details)
    

