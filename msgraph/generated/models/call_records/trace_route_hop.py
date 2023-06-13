from __future__ import annotations
from dataclasses import dataclass, field
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TraceRouteHop(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The network path count of this hop that was used to compute the round-trip time.
    hop_count: Optional[int] = None
    # IP address used for this hop in the network trace.
    ip_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The time from when the trace route packet was sent from the client to this hop and back to the client, denoted in [ISO 8601][] format. For example, 1 second is denoted as PT1S, where P is the duration designator, T is the time designator, and S is the second designator.
    round_trip_time: Optional[timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TraceRouteHop:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TraceRouteHop
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TraceRouteHop()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "hopCount": lambda n : setattr(self, 'hop_count', n.get_int_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "roundTripTime": lambda n : setattr(self, 'round_trip_time', n.get_timedelta_value()),
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
        writer.write_int_value("hopCount", self.hop_count)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_timedelta_value("roundTripTime", self.round_trip_time)
        writer.write_additional_data_value(self.additional_data)
    

