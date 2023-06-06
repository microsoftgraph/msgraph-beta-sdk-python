from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_connectivity_event_result, cloud_pc_connectivity_event_type

@dataclass
class CloudPcConnectivityEvent(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Indicates the date and time when this event was created. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
    event_date_time: Optional[datetime] = None
    # Name of the event.
    event_name: Optional[str] = None
    # The eventResult property
    event_result: Optional[cloud_pc_connectivity_event_result.CloudPcConnectivityEventResult] = None
    # The eventType property
    event_type: Optional[cloud_pc_connectivity_event_type.CloudPcConnectivityEventType] = None
    # Additional message for this event.
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcConnectivityEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcConnectivityEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcConnectivityEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_connectivity_event_result, cloud_pc_connectivity_event_type

        fields: Dict[str, Callable[[Any], None]] = {
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "eventName": lambda n : setattr(self, 'event_name', n.get_str_value()),
            "eventResult": lambda n : setattr(self, 'event_result', n.get_enum_value(cloud_pc_connectivity_event_result.CloudPcConnectivityEventResult)),
            "eventType": lambda n : setattr(self, 'event_type', n.get_enum_value(cloud_pc_connectivity_event_type.CloudPcConnectivityEventType)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("eventName", self.event_name)
        writer.write_enum_value("eventResult", self.event_result)
        writer.write_enum_value("eventType", self.event_type)
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

