from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UsageProfilingPoint(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The count of traffic requests directed to general internet destinations.
    internet_access_traffic_count: Optional[int] = None
    # The count of traffic requests directed to Microsoft 365 services.
    microsoft365_access_traffic_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The count of traffic requests directed to internal private network destinations.
    private_access_traffic_count: Optional[int] = None
    # The date and time of this data point.
    time_stamp_date_time: Optional[datetime.datetime] = None
    # The total count of all traffic requests across all access types.
    total_traffic_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UsageProfilingPoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UsageProfilingPoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UsageProfilingPoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "internetAccessTrafficCount": lambda n : setattr(self, 'internet_access_traffic_count', n.get_int_value()),
            "microsoft365AccessTrafficCount": lambda n : setattr(self, 'microsoft365_access_traffic_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "privateAccessTrafficCount": lambda n : setattr(self, 'private_access_traffic_count', n.get_int_value()),
            "timeStampDateTime": lambda n : setattr(self, 'time_stamp_date_time', n.get_datetime_value()),
            "totalTrafficCount": lambda n : setattr(self, 'total_traffic_count', n.get_int_value()),
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
        writer.write_int_value("internetAccessTrafficCount", self.internet_access_traffic_count)
        writer.write_int_value("microsoft365AccessTrafficCount", self.microsoft365_access_traffic_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("privateAccessTrafficCount", self.private_access_traffic_count)
        writer.write_datetime_value("timeStampDateTime", self.time_stamp_date_time)
        writer.write_int_value("totalTrafficCount", self.total_traffic_count)
        writer.write_additional_data_value(self.additional_data)
    

