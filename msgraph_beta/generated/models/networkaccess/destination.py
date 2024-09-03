from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .networking_protocol import NetworkingProtocol
    from .traffic_type import TrafficType

@dataclass
class Destination(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The number of unique devices that were seen.
    device_count: Optional[int] = None
    # The firstAccessDateTime property
    first_access_date_time: Optional[datetime.datetime] = None
    # The fully qualified domain name (FQDN) of the destination.
    fqdn: Optional[str] = None
    # The internet protocol (IP) used to access the destination.
    ip: Optional[str] = None
    # The most recent access DateTime.
    last_access_date_time: Optional[datetime.datetime] = None
    # The networkingProtocol property
    networking_protocol: Optional[NetworkingProtocol] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The numeric identifier that is associated with a specific endpoint in a network.
    port: Optional[int] = None
    # The threatCount property
    threat_count: Optional[int] = None
    # The totalBytesReceived property
    total_bytes_received: Optional[int] = None
    # The totalBytesSent property
    total_bytes_sent: Optional[int] = None
    # The trafficType property
    traffic_type: Optional[TrafficType] = None
    # The number of transactions.
    transaction_count: Optional[int] = None
    # The number of unique Microsoft Entra ID users that were seen.
    user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Destination:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Destination
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Destination()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .networking_protocol import NetworkingProtocol
        from .traffic_type import TrafficType

        from .networking_protocol import NetworkingProtocol
        from .traffic_type import TrafficType

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "firstAccessDateTime": lambda n : setattr(self, 'first_access_date_time', n.get_datetime_value()),
            "fqdn": lambda n : setattr(self, 'fqdn', n.get_str_value()),
            "ip": lambda n : setattr(self, 'ip', n.get_str_value()),
            "lastAccessDateTime": lambda n : setattr(self, 'last_access_date_time', n.get_datetime_value()),
            "networkingProtocol": lambda n : setattr(self, 'networking_protocol', n.get_enum_value(NetworkingProtocol)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "threatCount": lambda n : setattr(self, 'threat_count', n.get_int_value()),
            "totalBytesReceived": lambda n : setattr(self, 'total_bytes_received', n.get_int_value()),
            "totalBytesSent": lambda n : setattr(self, 'total_bytes_sent', n.get_int_value()),
            "trafficType": lambda n : setattr(self, 'traffic_type', n.get_enum_value(TrafficType)),
            "transactionCount": lambda n : setattr(self, 'transaction_count', n.get_int_value()),
            "userCount": lambda n : setattr(self, 'user_count', n.get_int_value()),
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
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_datetime_value("firstAccessDateTime", self.first_access_date_time)
        writer.write_str_value("fqdn", self.fqdn)
        writer.write_str_value("ip", self.ip)
        writer.write_datetime_value("lastAccessDateTime", self.last_access_date_time)
        writer.write_enum_value("networkingProtocol", self.networking_protocol)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("port", self.port)
        writer.write_int_value("threatCount", self.threat_count)
        writer.write_int_value("totalBytesReceived", self.total_bytes_received)
        writer.write_int_value("totalBytesSent", self.total_bytes_sent)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_int_value("transactionCount", self.transaction_count)
        writer.write_int_value("userCount", self.user_count)
        writer.write_additional_data_value(self.additional_data)
    

