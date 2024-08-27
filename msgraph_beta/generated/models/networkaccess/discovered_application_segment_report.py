from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_type import AccessType
    from .networking_protocol import NetworkingProtocol

@dataclass
class DiscoveredApplicationSegmentReport(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The accessType property
    access_type: Optional[AccessType] = None
    # The deviceCount property
    device_count: Optional[int] = None
    # The discoveredApplicationSegmentId property
    discovered_application_segment_id: Optional[str] = None
    # The firstAccessDateTime property
    first_access_date_time: Optional[datetime.datetime] = None
    # The fqdn property
    fqdn: Optional[str] = None
    # The ip property
    ip: Optional[str] = None
    # The lastAccessDateTime property
    last_access_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The port property
    port: Optional[int] = None
    # The totalBytesReceived property
    total_bytes_received: Optional[int] = None
    # The totalBytesSent property
    total_bytes_sent: Optional[int] = None
    # The transactionCount property
    transaction_count: Optional[int] = None
    # The transportProtocol property
    transport_protocol: Optional[NetworkingProtocol] = None
    # The userCount property
    user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DiscoveredApplicationSegmentReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DiscoveredApplicationSegmentReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DiscoveredApplicationSegmentReport()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_type import AccessType
        from .networking_protocol import NetworkingProtocol

        from .access_type import AccessType
        from .networking_protocol import NetworkingProtocol

        fields: Dict[str, Callable[[Any], None]] = {
            "accessType": lambda n : setattr(self, 'access_type', n.get_enum_value(AccessType)),
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "discoveredApplicationSegmentId": lambda n : setattr(self, 'discovered_application_segment_id', n.get_str_value()),
            "firstAccessDateTime": lambda n : setattr(self, 'first_access_date_time', n.get_datetime_value()),
            "fqdn": lambda n : setattr(self, 'fqdn', n.get_str_value()),
            "ip": lambda n : setattr(self, 'ip', n.get_str_value()),
            "lastAccessDateTime": lambda n : setattr(self, 'last_access_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "totalBytesReceived": lambda n : setattr(self, 'total_bytes_received', n.get_int_value()),
            "totalBytesSent": lambda n : setattr(self, 'total_bytes_sent', n.get_int_value()),
            "transactionCount": lambda n : setattr(self, 'transaction_count', n.get_int_value()),
            "transportProtocol": lambda n : setattr(self, 'transport_protocol', n.get_enum_value(NetworkingProtocol)),
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
        writer.write_enum_value("accessType", self.access_type)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_str_value("discoveredApplicationSegmentId", self.discovered_application_segment_id)
        writer.write_datetime_value("firstAccessDateTime", self.first_access_date_time)
        writer.write_str_value("fqdn", self.fqdn)
        writer.write_str_value("ip", self.ip)
        writer.write_datetime_value("lastAccessDateTime", self.last_access_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("port", self.port)
        writer.write_int_value("totalBytesReceived", self.total_bytes_received)
        writer.write_int_value("totalBytesSent", self.total_bytes_sent)
        writer.write_int_value("transactionCount", self.transaction_count)
        writer.write_enum_value("transportProtocol", self.transport_protocol)
        writer.write_int_value("userCount", self.user_count)
        writer.write_additional_data_value(self.additional_data)
    

