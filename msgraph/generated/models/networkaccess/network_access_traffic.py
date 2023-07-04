from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_category import DeviceCategory
    from .headers import Headers
    from .networking_protocol import NetworkingProtocol
    from .traffic_type import TrafficType

@dataclass
class NetworkAccessTraffic(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The agentVersion property
    agent_version: Optional[str] = None
    # The connectionId property
    connection_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The destinationFQDN property
    destination_f_q_d_n: Optional[str] = None
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
    # The headers property
    headers: Optional[Headers] = None
    # The networkProtocol property
    network_protocol: Optional[NetworkingProtocol] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyId property
    policy_id: Optional[str] = None
    # The policyRuleId property
    policy_rule_id: Optional[str] = None
    # The receivedBytes property
    received_bytes: Optional[int] = None
    # The sentBytes property
    sent_bytes: Optional[int] = None
    # The sessionId property
    session_id: Optional[str] = None
    # The sourceIp property
    source_ip: Optional[str] = None
    # The sourcePort property
    source_port: Optional[int] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The trafficType property
    traffic_type: Optional[TrafficType] = None
    # The transactionId property
    transaction_id: Optional[str] = None
    # The transportProtocol property
    transport_protocol: Optional[NetworkingProtocol] = None
    # The userId property
    user_id: Optional[str] = None
    # The userPrincipalName property
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NetworkAccessTraffic:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NetworkAccessTraffic
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return NetworkAccessTraffic()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_category import DeviceCategory
        from .headers import Headers
        from .networking_protocol import NetworkingProtocol
        from .traffic_type import TrafficType

        from .device_category import DeviceCategory
        from .headers import Headers
        from .networking_protocol import NetworkingProtocol
        from .traffic_type import TrafficType

        fields: Dict[str, Callable[[Any], None]] = {
            "agentVersion": lambda n : setattr(self, 'agent_version', n.get_str_value()),
            "connectionId": lambda n : setattr(self, 'connection_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "destinationFQDN": lambda n : setattr(self, 'destination_f_q_d_n', n.get_str_value()),
            "destinationIp": lambda n : setattr(self, 'destination_ip', n.get_str_value()),
            "destinationPort": lambda n : setattr(self, 'destination_port', n.get_int_value()),
            "deviceCategory": lambda n : setattr(self, 'device_category', n.get_enum_value(DeviceCategory)),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceOperatingSystem": lambda n : setattr(self, 'device_operating_system', n.get_str_value()),
            "deviceOperatingSystemVersion": lambda n : setattr(self, 'device_operating_system_version', n.get_str_value()),
            "headers": lambda n : setattr(self, 'headers', n.get_object_value(Headers)),
            "networkProtocol": lambda n : setattr(self, 'network_protocol', n.get_enum_value(NetworkingProtocol)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policyRuleId": lambda n : setattr(self, 'policy_rule_id', n.get_str_value()),
            "receivedBytes": lambda n : setattr(self, 'received_bytes', n.get_int_value()),
            "sentBytes": lambda n : setattr(self, 'sent_bytes', n.get_int_value()),
            "sessionId": lambda n : setattr(self, 'session_id', n.get_str_value()),
            "sourceIp": lambda n : setattr(self, 'source_ip', n.get_str_value()),
            "sourcePort": lambda n : setattr(self, 'source_port', n.get_int_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "trafficType": lambda n : setattr(self, 'traffic_type', n.get_enum_value(TrafficType)),
            "transactionId": lambda n : setattr(self, 'transaction_id', n.get_str_value()),
            "transportProtocol": lambda n : setattr(self, 'transport_protocol', n.get_enum_value(NetworkingProtocol)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("agentVersion", self.agent_version)
        writer.write_str_value("connectionId", self.connection_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("destinationFQDN", self.destination_f_q_d_n)
        writer.write_str_value("destinationIp", self.destination_ip)
        writer.write_int_value("destinationPort", self.destination_port)
        writer.write_enum_value("deviceCategory", self.device_category)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceOperatingSystem", self.device_operating_system)
        writer.write_str_value("deviceOperatingSystemVersion", self.device_operating_system_version)
        writer.write_object_value("headers", self.headers)
        writer.write_enum_value("networkProtocol", self.network_protocol)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("policyRuleId", self.policy_rule_id)
        writer.write_int_value("receivedBytes", self.received_bytes)
        writer.write_int_value("sentBytes", self.sent_bytes)
        writer.write_str_value("sessionId", self.session_id)
        writer.write_str_value("sourceIp", self.source_ip)
        writer.write_int_value("sourcePort", self.source_port)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_str_value("transactionId", self.transaction_id)
        writer.write_enum_value("transportProtocol", self.transport_protocol)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

