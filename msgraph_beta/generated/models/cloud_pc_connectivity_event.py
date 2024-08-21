from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_connectivity_event_result import CloudPcConnectivityEventResult
    from .cloud_pc_connectivity_event_type import CloudPcConnectivityEventType

@dataclass
class CloudPcConnectivityEvent(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates the date and time when this event was created. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
    event_date_time: Optional[datetime.datetime] = None
    # Name of the event.
    event_name: Optional[str] = None
    # The eventResult property
    event_result: Optional[CloudPcConnectivityEventResult] = None
    # The eventType property
    event_type: Optional[CloudPcConnectivityEventType] = None
    # Additional message for this event.
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcConnectivityEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcConnectivityEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcConnectivityEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_connectivity_event_result import CloudPcConnectivityEventResult
        from .cloud_pc_connectivity_event_type import CloudPcConnectivityEventType

        from .cloud_pc_connectivity_event_result import CloudPcConnectivityEventResult
        from .cloud_pc_connectivity_event_type import CloudPcConnectivityEventType

        fields: Dict[str, Callable[[Any], None]] = {
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "eventName": lambda n : setattr(self, 'event_name', n.get_str_value()),
            "eventResult": lambda n : setattr(self, 'event_result', n.get_enum_value(CloudPcConnectivityEventResult)),
            "eventType": lambda n : setattr(self, 'event_type', n.get_enum_value(CloudPcConnectivityEventType)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("eventName", self.event_name)
        writer.write_enum_value("eventResult", self.event_result)
        writer.write_enum_value("eventType", self.event_type)
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

