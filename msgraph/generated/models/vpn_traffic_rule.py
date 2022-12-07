from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

i_pv4_range = lazy_import('msgraph.generated.models.i_pv4_range')
number_range = lazy_import('msgraph.generated.models.number_range')
vpn_traffic_rule_app_type = lazy_import('msgraph.generated.models.vpn_traffic_rule_app_type')
vpn_traffic_rule_routing_policy_type = lazy_import('msgraph.generated.models.vpn_traffic_rule_routing_policy_type')

class VpnTrafficRule(AdditionalDataHolder, Parsable):
    """
    VPN Traffic Rule definition.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. App identifier, if this traffic rule is triggered by an app.
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. App identifier, if this traffic rule is triggered by an app.
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    @property
    def app_type(self,) -> Optional[vpn_traffic_rule_app_type.VpnTrafficRuleAppType]:
        """
        Gets the appType property value. Indicates the type of app that a VPN traffic rule is associated with.
        Returns: Optional[vpn_traffic_rule_app_type.VpnTrafficRuleAppType]
        """
        return self._app_type
    
    @app_type.setter
    def app_type(self,value: Optional[vpn_traffic_rule_app_type.VpnTrafficRuleAppType] = None) -> None:
        """
        Sets the appType property value. Indicates the type of app that a VPN traffic rule is associated with.
        Args:
            value: Value to set for the appType property.
        """
        self._app_type = value
    
    @property
    def claims(self,) -> Optional[str]:
        """
        Gets the claims property value. Claims associated with this traffic rule.
        Returns: Optional[str]
        """
        return self._claims
    
    @claims.setter
    def claims(self,value: Optional[str] = None) -> None:
        """
        Sets the claims property value. Claims associated with this traffic rule.
        Args:
            value: Value to set for the claims property.
        """
        self._claims = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new vpnTrafficRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # App identifier, if this traffic rule is triggered by an app.
        self._app_id: Optional[str] = None
        # Indicates the type of app that a VPN traffic rule is associated with.
        self._app_type: Optional[vpn_traffic_rule_app_type.VpnTrafficRuleAppType] = None
        # Claims associated with this traffic rule.
        self._claims: Optional[str] = None
        # Local address range. This collection can contain a maximum of 500 elements.
        self._local_address_ranges: Optional[List[i_pv4_range.IPv4Range]] = None
        # Local port range can be set only when protocol is either TCP or UDP (6 or 17). This collection can contain a maximum of 500 elements.
        self._local_port_ranges: Optional[List[number_range.NumberRange]] = None
        # Name.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Protocols (0-255). Valid values 0 to 255
        self._protocols: Optional[int] = None
        # Remote address range. This collection can contain a maximum of 500 elements.
        self._remote_address_ranges: Optional[List[i_pv4_range.IPv4Range]] = None
        # Remote port range can be set only when protocol is either TCP or UDP (6 or 17). This collection can contain a maximum of 500 elements.
        self._remote_port_ranges: Optional[List[number_range.NumberRange]] = None
        # Specifies the routing policy for a VPN traffic rule.
        self._routing_policy_type: Optional[vpn_traffic_rule_routing_policy_type.VpnTrafficRuleRoutingPolicyType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VpnTrafficRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VpnTrafficRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VpnTrafficRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "app_type": lambda n : setattr(self, 'app_type', n.get_enum_value(vpn_traffic_rule_app_type.VpnTrafficRuleAppType)),
            "claims": lambda n : setattr(self, 'claims', n.get_str_value()),
            "local_address_ranges": lambda n : setattr(self, 'local_address_ranges', n.get_collection_of_object_values(i_pv4_range.IPv4Range)),
            "local_port_ranges": lambda n : setattr(self, 'local_port_ranges', n.get_collection_of_object_values(number_range.NumberRange)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "protocols": lambda n : setattr(self, 'protocols', n.get_int_value()),
            "remote_address_ranges": lambda n : setattr(self, 'remote_address_ranges', n.get_collection_of_object_values(i_pv4_range.IPv4Range)),
            "remote_port_ranges": lambda n : setattr(self, 'remote_port_ranges', n.get_collection_of_object_values(number_range.NumberRange)),
            "routing_policy_type": lambda n : setattr(self, 'routing_policy_type', n.get_enum_value(vpn_traffic_rule_routing_policy_type.VpnTrafficRuleRoutingPolicyType)),
        }
        return fields
    
    @property
    def local_address_ranges(self,) -> Optional[List[i_pv4_range.IPv4Range]]:
        """
        Gets the localAddressRanges property value. Local address range. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[i_pv4_range.IPv4Range]]
        """
        return self._local_address_ranges
    
    @local_address_ranges.setter
    def local_address_ranges(self,value: Optional[List[i_pv4_range.IPv4Range]] = None) -> None:
        """
        Sets the localAddressRanges property value. Local address range. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the localAddressRanges property.
        """
        self._local_address_ranges = value
    
    @property
    def local_port_ranges(self,) -> Optional[List[number_range.NumberRange]]:
        """
        Gets the localPortRanges property value. Local port range can be set only when protocol is either TCP or UDP (6 or 17). This collection can contain a maximum of 500 elements.
        Returns: Optional[List[number_range.NumberRange]]
        """
        return self._local_port_ranges
    
    @local_port_ranges.setter
    def local_port_ranges(self,value: Optional[List[number_range.NumberRange]] = None) -> None:
        """
        Sets the localPortRanges property value. Local port range can be set only when protocol is either TCP or UDP (6 or 17). This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the localPortRanges property.
        """
        self._local_port_ranges = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def protocols(self,) -> Optional[int]:
        """
        Gets the protocols property value. Protocols (0-255). Valid values 0 to 255
        Returns: Optional[int]
        """
        return self._protocols
    
    @protocols.setter
    def protocols(self,value: Optional[int] = None) -> None:
        """
        Sets the protocols property value. Protocols (0-255). Valid values 0 to 255
        Args:
            value: Value to set for the protocols property.
        """
        self._protocols = value
    
    @property
    def remote_address_ranges(self,) -> Optional[List[i_pv4_range.IPv4Range]]:
        """
        Gets the remoteAddressRanges property value. Remote address range. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[i_pv4_range.IPv4Range]]
        """
        return self._remote_address_ranges
    
    @remote_address_ranges.setter
    def remote_address_ranges(self,value: Optional[List[i_pv4_range.IPv4Range]] = None) -> None:
        """
        Sets the remoteAddressRanges property value. Remote address range. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the remoteAddressRanges property.
        """
        self._remote_address_ranges = value
    
    @property
    def remote_port_ranges(self,) -> Optional[List[number_range.NumberRange]]:
        """
        Gets the remotePortRanges property value. Remote port range can be set only when protocol is either TCP or UDP (6 or 17). This collection can contain a maximum of 500 elements.
        Returns: Optional[List[number_range.NumberRange]]
        """
        return self._remote_port_ranges
    
    @remote_port_ranges.setter
    def remote_port_ranges(self,value: Optional[List[number_range.NumberRange]] = None) -> None:
        """
        Sets the remotePortRanges property value. Remote port range can be set only when protocol is either TCP or UDP (6 or 17). This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the remotePortRanges property.
        """
        self._remote_port_ranges = value
    
    @property
    def routing_policy_type(self,) -> Optional[vpn_traffic_rule_routing_policy_type.VpnTrafficRuleRoutingPolicyType]:
        """
        Gets the routingPolicyType property value. Specifies the routing policy for a VPN traffic rule.
        Returns: Optional[vpn_traffic_rule_routing_policy_type.VpnTrafficRuleRoutingPolicyType]
        """
        return self._routing_policy_type
    
    @routing_policy_type.setter
    def routing_policy_type(self,value: Optional[vpn_traffic_rule_routing_policy_type.VpnTrafficRuleRoutingPolicyType] = None) -> None:
        """
        Sets the routingPolicyType property value. Specifies the routing policy for a VPN traffic rule.
        Args:
            value: Value to set for the routingPolicyType property.
        """
        self._routing_policy_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("appId", self.app_id)
        writer.write_enum_value("appType", self.app_type)
        writer.write_str_value("claims", self.claims)
        writer.write_collection_of_object_values("localAddressRanges", self.local_address_ranges)
        writer.write_collection_of_object_values("localPortRanges", self.local_port_ranges)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("protocols", self.protocols)
        writer.write_collection_of_object_values("remoteAddressRanges", self.remote_address_ranges)
        writer.write_collection_of_object_values("remotePortRanges", self.remote_port_ranges)
        writer.write_enum_value("routingPolicyType", self.routing_policy_type)
        writer.write_additional_data_value(self.additional_data)
    

