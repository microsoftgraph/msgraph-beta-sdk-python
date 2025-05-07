from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .application_snapshot import ApplicationSnapshot
    from .connection_status import ConnectionStatus
    from .device_category import DeviceCategory
    from .networking_protocol import NetworkingProtocol
    from .private_access_details import PrivateAccessDetails
    from .traffic_type import TrafficType

from ..entity import Entity

@dataclass
class Connection(Entity, Parsable):
    # The agentVersion property
    agent_version: Optional[str] = None
    # The applicationSnapshot property
    application_snapshot: Optional[ApplicationSnapshot] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The destinationFqdn property
    destination_fqdn: Optional[str] = None
    # The destinationIp property
    destination_ip: Optional[str] = None
    # The destinationPort property
    destination_port: Optional[int] = None
    # The deviceCategory property
    device_category: Optional[DeviceCategory] = None
    # The deviceId property
    device_id: Optional[str] = None
    # The deviceOperatingSystem property
    device_operating_system: Optional[str] = None
    # The deviceOperatingSystemVersion property
    device_operating_system_version: Optional[str] = None
    # The endDateTime property
    end_date_time: Optional[datetime.datetime] = None
    # The initiatingProcessName property
    initiating_process_name: Optional[str] = None
    # The lastUpdateDateTime property
    last_update_date_time: Optional[datetime.datetime] = None
    # The networkProtocol property
    network_protocol: Optional[NetworkingProtocol] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The popProcessingRegion property
    pop_processing_region: Optional[str] = None
    # The privateAccessDetails property
    private_access_details: Optional[PrivateAccessDetails] = None
    # The receivedBytes property
    received_bytes: Optional[int] = None
    # The sentBytes property
    sent_bytes: Optional[int] = None
    # The sourceIp property
    source_ip: Optional[str] = None
    # The sourcePort property
    source_port: Optional[int] = None
    # The status property
    status: Optional[ConnectionStatus] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The trafficType property
    traffic_type: Optional[TrafficType] = None
    # The transactionBlockCount property
    transaction_block_count: Optional[int] = None
    # The transactionCount property
    transaction_count: Optional[int] = None
    # The transportProtocol property
    transport_protocol: Optional[NetworkingProtocol] = None
    # The userId property
    user_id: Optional[str] = None
    # The userPrincipalName property
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Connection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Connection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Connection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .application_snapshot import ApplicationSnapshot
        from .connection_status import ConnectionStatus
        from .device_category import DeviceCategory
        from .networking_protocol import NetworkingProtocol
        from .private_access_details import PrivateAccessDetails
        from .traffic_type import TrafficType

        from ..entity import Entity
        from .application_snapshot import ApplicationSnapshot
        from .connection_status import ConnectionStatus
        from .device_category import DeviceCategory
        from .networking_protocol import NetworkingProtocol
        from .private_access_details import PrivateAccessDetails
        from .traffic_type import TrafficType

        fields: dict[str, Callable[[Any], None]] = {
            "agentVersion": lambda n : setattr(self, 'agent_version', n.get_str_value()),
            "applicationSnapshot": lambda n : setattr(self, 'application_snapshot', n.get_object_value(ApplicationSnapshot)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "destinationFqdn": lambda n : setattr(self, 'destination_fqdn', n.get_str_value()),
            "destinationIp": lambda n : setattr(self, 'destination_ip', n.get_str_value()),
            "destinationPort": lambda n : setattr(self, 'destination_port', n.get_int_value()),
            "deviceCategory": lambda n : setattr(self, 'device_category', n.get_enum_value(DeviceCategory)),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceOperatingSystem": lambda n : setattr(self, 'device_operating_system', n.get_str_value()),
            "deviceOperatingSystemVersion": lambda n : setattr(self, 'device_operating_system_version', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "initiatingProcessName": lambda n : setattr(self, 'initiating_process_name', n.get_str_value()),
            "lastUpdateDateTime": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "networkProtocol": lambda n : setattr(self, 'network_protocol', n.get_enum_value(NetworkingProtocol)),
            "popProcessingRegion": lambda n : setattr(self, 'pop_processing_region', n.get_str_value()),
            "privateAccessDetails": lambda n : setattr(self, 'private_access_details', n.get_object_value(PrivateAccessDetails)),
            "receivedBytes": lambda n : setattr(self, 'received_bytes', n.get_int_value()),
            "sentBytes": lambda n : setattr(self, 'sent_bytes', n.get_int_value()),
            "sourceIp": lambda n : setattr(self, 'source_ip', n.get_str_value()),
            "sourcePort": lambda n : setattr(self, 'source_port', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ConnectionStatus)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "trafficType": lambda n : setattr(self, 'traffic_type', n.get_enum_value(TrafficType)),
            "transactionBlockCount": lambda n : setattr(self, 'transaction_block_count', n.get_int_value()),
            "transactionCount": lambda n : setattr(self, 'transaction_count', n.get_int_value()),
            "transportProtocol": lambda n : setattr(self, 'transport_protocol', n.get_enum_value(NetworkingProtocol)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("agentVersion", self.agent_version)
        writer.write_object_value("applicationSnapshot", self.application_snapshot)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("destinationFqdn", self.destination_fqdn)
        writer.write_str_value("destinationIp", self.destination_ip)
        writer.write_int_value("destinationPort", self.destination_port)
        writer.write_enum_value("deviceCategory", self.device_category)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceOperatingSystem", self.device_operating_system)
        writer.write_str_value("deviceOperatingSystemVersion", self.device_operating_system_version)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("initiatingProcessName", self.initiating_process_name)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_enum_value("networkProtocol", self.network_protocol)
        writer.write_str_value("popProcessingRegion", self.pop_processing_region)
        writer.write_object_value("privateAccessDetails", self.private_access_details)
        writer.write_int_value("receivedBytes", self.received_bytes)
        writer.write_int_value("sentBytes", self.sent_bytes)
        writer.write_str_value("sourceIp", self.source_ip)
        writer.write_int_value("sourcePort", self.source_port)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_int_value("transactionBlockCount", self.transaction_block_count)
        writer.write_int_value("transactionCount", self.transaction_count)
        writer.write_enum_value("transportProtocol", self.transport_protocol)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

