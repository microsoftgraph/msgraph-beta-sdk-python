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
    # The deviceCount property
    device_count: Optional[int] = None
    # The fqdn property
    fqdn: Optional[str] = None
    # The ip property
    ip: Optional[str] = None
    # The lastAccessDateTime property
    last_access_date_time: Optional[datetime.datetime] = None
    # The networkingProtocol property
    networking_protocol: Optional[NetworkingProtocol] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The port property
    port: Optional[int] = None
    # The trafficType property
    traffic_type: Optional[TrafficType] = None
    # The transactionCount property
    transaction_count: Optional[int] = None
    # The userCount property
    user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Destination:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Destination
        """
        if not parse_node:
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
            "fqdn": lambda n : setattr(self, 'fqdn', n.get_str_value()),
            "ip": lambda n : setattr(self, 'ip', n.get_str_value()),
            "lastAccessDateTime": lambda n : setattr(self, 'last_access_date_time', n.get_datetime_value()),
            "networkingProtocol": lambda n : setattr(self, 'networking_protocol', n.get_enum_value(NetworkingProtocol)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_str_value("fqdn", self.fqdn)
        writer.write_str_value("ip", self.ip)
        writer.write_datetime_value("lastAccessDateTime", self.last_access_date_time)
        writer.write_enum_value("networkingProtocol", self.networking_protocol)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_int_value("port", self.port)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_int_value("transactionCount", self.transaction_count)
        writer.write_int_value("userCount", self.user_count)
        writer.write_additional_data_value(self.additional_data)
    

