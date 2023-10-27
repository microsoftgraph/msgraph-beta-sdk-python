from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_category import DeviceCategory
    from .headers import Headers
    from .networking_protocol import NetworkingProtocol
    from .traffic_type import TrafficType

@dataclass
class NetworkAccessTraffic(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Represents the version of the Global Secure Access client agent software. Supports $filter (eq) and $orderby.
    agent_version: Optional[str] = None
    # Represents a unique identifier assigned to a connection. Supports $filter (eq) and $orderby.
    connection_id: Optional[str] = None
    # Represents the date and time when a network access traffic log entry was created. Supports $filter (eq) and $orderby.
    created_date_time: Optional[datetime.datetime] = None
    # Represents the Fully Qualified Domain Name (FQDN) of the destination host or server in a network communication. Supports $filter (eq) and $orderby.
    destination_f_q_d_n: Optional[str] = None
    # Represents the IP address of the destination host or server in a network communication. Supports $filter (eq) and $orderby.
    destination_ip: Optional[str] = None
    # Represents the network port number on the destination host or server in a network communication. Supports $filter (eq) and $orderby.
    destination_port: Optional[int] = None
    # Represents the category classification of a device within a network infrastructure. The possible values are: client, branch, unknownFutureValue. Supports $filter (eq) and $orderby.
    device_category: Optional[DeviceCategory] = None
    # Represents a unique identifier assigned to a device within a network infrastructure. Supports $filter (eq) and $orderby.
    device_id: Optional[str] = None
    # Represents the operating system installed on a device within a network infrastructure. Supports $filter (eq) and $orderby.
    device_operating_system: Optional[str] = None
    # Represents the version or release number of the operating system installed on a device within a network infrastructure. Supports $filter (eq) and $orderby.
    device_operating_system_version: Optional[str] = None
    # The filteringProfileId property
    filtering_profile_id: Optional[str] = None
    # The filteringProfileName property
    filtering_profile_name: Optional[str] = None
    # Represents the headers included in a network request or response. Supports $filter (eq) and $orderby.
    headers: Optional[Headers] = None
    # The initiatingProcessName property
    initiating_process_name: Optional[str] = None
    # Represents the networking protocol used for communication.The possible values are: ip, icmp, igmp, ggp, ipv4, tcp, pup, udp, idp, ipv6, ipv6RoutingHeader, ipv6FragmentHeader, ipSecEncapsulatingSecurityPayload, ipSecAuthenticationHeader, icmpV6, ipv6NoNextHeader, ipv6DestinationOptions, nd, raw, ipx, spx, spxII, unknownFutureValue. Supports $filter (eq) and $orderby.
    network_protocol: Optional[NetworkingProtocol] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a unique identifier assigned to a policy. Supports $filter (eq) and $orderby.
    policy_id: Optional[str] = None
    # The policyName property
    policy_name: Optional[str] = None
    # Represents a unique identifier assigned to a policy rule. Supports $filter (eq) and $orderby.
    policy_rule_id: Optional[str] = None
    # The policyRuleName property
    policy_rule_name: Optional[str] = None
    # Represents the total number of bytes received in a network communication or data transfer. Supports $filter (eq) and $orderby.
    received_bytes: Optional[int] = None
    # The resourceTenantId property
    resource_tenant_id: Optional[str] = None
    # Represents the total number of bytes sent in a network communication or data transfer. Supports $filter (eq) and $orderby.
    sent_bytes: Optional[int] = None
    # Represents a unique identifier assigned to a session or connection within a network infrastructure. Supports $filter (eq) and $orderby.
    session_id: Optional[str] = None
    # Represents the source IP address in a network communication. Supports $filter (eq) and $orderby.
    source_ip: Optional[str] = None
    # Represents the network port number on the source host or device in a network communication. Supports $filter (eq) and $orderby.
    source_port: Optional[int] = None
    # Represents a unique identifier assigned to a tenant within a network infrastructure. Supports $filter (eq) and $orderby.
    tenant_id: Optional[str] = None
    # The trafficType property
    traffic_type: Optional[TrafficType] = None
    # Represents a unique identifier assigned to a specific transaction or operation. Key. Supports $filter (eq) and $orderby.
    transaction_id: Optional[str] = None
    # Represents the transport protocol used for communication.The possible values are: ip, icmp, igmp, ggp, ipv4, tcp, pup, udp, idp, ipv6, ipv6RoutingHeader, ipv6FragmentHeader, ipSecEncapsulatingSecurityPayload, ipSecAuthenticationHeader, icmpV6, ipv6NoNextHeader, ipv6DestinationOptions, nd, raw, ipx, spx, spxII, unknownFutureValue. Supports $filter (eq) and $orderby.
    transport_protocol: Optional[NetworkingProtocol] = None
    # Represents a unique identifier assigned to a user. Supports $filter (eq) and $orderby.
    user_id: Optional[str] = None
    # Represents the user principal name (UPN) associated with a user. Supports $filter (eq) and $orderby.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NetworkAccessTraffic:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
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
            "filteringProfileId": lambda n : setattr(self, 'filtering_profile_id', n.get_str_value()),
            "filteringProfileName": lambda n : setattr(self, 'filtering_profile_name', n.get_str_value()),
            "headers": lambda n : setattr(self, 'headers', n.get_object_value(Headers)),
            "initiatingProcessName": lambda n : setattr(self, 'initiating_process_name', n.get_str_value()),
            "networkProtocol": lambda n : setattr(self, 'network_protocol', n.get_enum_value(NetworkingProtocol)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "policyRuleId": lambda n : setattr(self, 'policy_rule_id', n.get_str_value()),
            "policyRuleName": lambda n : setattr(self, 'policy_rule_name', n.get_str_value()),
            "receivedBytes": lambda n : setattr(self, 'received_bytes', n.get_int_value()),
            "resourceTenantId": lambda n : setattr(self, 'resource_tenant_id', n.get_str_value()),
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
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
        writer.write_str_value("filteringProfileId", self.filtering_profile_id)
        writer.write_str_value("filteringProfileName", self.filtering_profile_name)
        writer.write_object_value("headers", self.headers)
        writer.write_str_value("initiatingProcessName", self.initiating_process_name)
        writer.write_enum_value("networkProtocol", self.network_protocol)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_str_value("policyRuleId", self.policy_rule_id)
        writer.write_str_value("policyRuleName", self.policy_rule_name)
        writer.write_int_value("receivedBytes", self.received_bytes)
        writer.write_str_value("resourceTenantId", self.resource_tenant_id)
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
    

