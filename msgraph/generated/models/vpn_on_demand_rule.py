from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

vpn_on_demand_rule_connection_action = lazy_import('msgraph.generated.models.vpn_on_demand_rule_connection_action')
vpn_on_demand_rule_connection_domain_action = lazy_import('msgraph.generated.models.vpn_on_demand_rule_connection_domain_action')
vpn_on_demand_rule_interface_type_match = lazy_import('msgraph.generated.models.vpn_on_demand_rule_interface_type_match')

class VpnOnDemandRule(AdditionalDataHolder, Parsable):
    """
    VPN On-Demand Rule definition.
    """
    @property
    def action(self,) -> Optional[vpn_on_demand_rule_connection_action.VpnOnDemandRuleConnectionAction]:
        """
        Gets the action property value. VPN On-Demand Rule Connection Action.
        Returns: Optional[vpn_on_demand_rule_connection_action.VpnOnDemandRuleConnectionAction]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[vpn_on_demand_rule_connection_action.VpnOnDemandRuleConnectionAction] = None) -> None:
        """
        Sets the action property value. VPN On-Demand Rule Connection Action.
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new vpnOnDemandRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # VPN On-Demand Rule Connection Action.
        self._action: Optional[vpn_on_demand_rule_connection_action.VpnOnDemandRuleConnectionAction] = None
        # DNS Search Domains.
        self._dns_search_domains: Optional[List[str]] = None
        # DNS Search Server Address.
        self._dns_server_address_match: Optional[List[str]] = None
        # VPN On-Demand Rule Connection Domain Action.
        self._domain_action: Optional[vpn_on_demand_rule_connection_domain_action.VpnOnDemandRuleConnectionDomainAction] = None
        # Domains (Only applicable when Action is evaluate connection).
        self._domains: Optional[List[str]] = None
        # VPN On-Demand Rule Connection network interface type.
        self._interface_type_match: Optional[vpn_on_demand_rule_interface_type_match.VpnOnDemandRuleInterfaceTypeMatch] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Probe Required Url (Only applicable when Action is evaluate connection and DomainAction is connect if needed).
        self._probe_required_url: Optional[str] = None
        # A URL to probe. If this URL is successfully fetched (returning a 200 HTTP status code) without redirection, this rule matches.
        self._probe_url: Optional[str] = None
        # Network Service Set Identifiers (SSIDs).
        self._ssids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VpnOnDemandRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VpnOnDemandRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VpnOnDemandRule()
    
    @property
    def dns_search_domains(self,) -> Optional[List[str]]:
        """
        Gets the dnsSearchDomains property value. DNS Search Domains.
        Returns: Optional[List[str]]
        """
        return self._dns_search_domains
    
    @dns_search_domains.setter
    def dns_search_domains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the dnsSearchDomains property value. DNS Search Domains.
        Args:
            value: Value to set for the dnsSearchDomains property.
        """
        self._dns_search_domains = value
    
    @property
    def dns_server_address_match(self,) -> Optional[List[str]]:
        """
        Gets the dnsServerAddressMatch property value. DNS Search Server Address.
        Returns: Optional[List[str]]
        """
        return self._dns_server_address_match
    
    @dns_server_address_match.setter
    def dns_server_address_match(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the dnsServerAddressMatch property value. DNS Search Server Address.
        Args:
            value: Value to set for the dnsServerAddressMatch property.
        """
        self._dns_server_address_match = value
    
    @property
    def domain_action(self,) -> Optional[vpn_on_demand_rule_connection_domain_action.VpnOnDemandRuleConnectionDomainAction]:
        """
        Gets the domainAction property value. VPN On-Demand Rule Connection Domain Action.
        Returns: Optional[vpn_on_demand_rule_connection_domain_action.VpnOnDemandRuleConnectionDomainAction]
        """
        return self._domain_action
    
    @domain_action.setter
    def domain_action(self,value: Optional[vpn_on_demand_rule_connection_domain_action.VpnOnDemandRuleConnectionDomainAction] = None) -> None:
        """
        Sets the domainAction property value. VPN On-Demand Rule Connection Domain Action.
        Args:
            value: Value to set for the domainAction property.
        """
        self._domain_action = value
    
    @property
    def domains(self,) -> Optional[List[str]]:
        """
        Gets the domains property value. Domains (Only applicable when Action is evaluate connection).
        Returns: Optional[List[str]]
        """
        return self._domains
    
    @domains.setter
    def domains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the domains property value. Domains (Only applicable when Action is evaluate connection).
        Args:
            value: Value to set for the domains property.
        """
        self._domains = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(vpn_on_demand_rule_connection_action.VpnOnDemandRuleConnectionAction)),
            "dns_search_domains": lambda n : setattr(self, 'dns_search_domains', n.get_collection_of_primitive_values(str)),
            "dns_server_address_match": lambda n : setattr(self, 'dns_server_address_match', n.get_collection_of_primitive_values(str)),
            "domain_action": lambda n : setattr(self, 'domain_action', n.get_enum_value(vpn_on_demand_rule_connection_domain_action.VpnOnDemandRuleConnectionDomainAction)),
            "domains": lambda n : setattr(self, 'domains', n.get_collection_of_primitive_values(str)),
            "interface_type_match": lambda n : setattr(self, 'interface_type_match', n.get_enum_value(vpn_on_demand_rule_interface_type_match.VpnOnDemandRuleInterfaceTypeMatch)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "probe_required_url": lambda n : setattr(self, 'probe_required_url', n.get_str_value()),
            "probe_url": lambda n : setattr(self, 'probe_url', n.get_str_value()),
            "ssids": lambda n : setattr(self, 'ssids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def interface_type_match(self,) -> Optional[vpn_on_demand_rule_interface_type_match.VpnOnDemandRuleInterfaceTypeMatch]:
        """
        Gets the interfaceTypeMatch property value. VPN On-Demand Rule Connection network interface type.
        Returns: Optional[vpn_on_demand_rule_interface_type_match.VpnOnDemandRuleInterfaceTypeMatch]
        """
        return self._interface_type_match
    
    @interface_type_match.setter
    def interface_type_match(self,value: Optional[vpn_on_demand_rule_interface_type_match.VpnOnDemandRuleInterfaceTypeMatch] = None) -> None:
        """
        Sets the interfaceTypeMatch property value. VPN On-Demand Rule Connection network interface type.
        Args:
            value: Value to set for the interfaceTypeMatch property.
        """
        self._interface_type_match = value
    
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
    def probe_required_url(self,) -> Optional[str]:
        """
        Gets the probeRequiredUrl property value. Probe Required Url (Only applicable when Action is evaluate connection and DomainAction is connect if needed).
        Returns: Optional[str]
        """
        return self._probe_required_url
    
    @probe_required_url.setter
    def probe_required_url(self,value: Optional[str] = None) -> None:
        """
        Sets the probeRequiredUrl property value. Probe Required Url (Only applicable when Action is evaluate connection and DomainAction is connect if needed).
        Args:
            value: Value to set for the probeRequiredUrl property.
        """
        self._probe_required_url = value
    
    @property
    def probe_url(self,) -> Optional[str]:
        """
        Gets the probeUrl property value. A URL to probe. If this URL is successfully fetched (returning a 200 HTTP status code) without redirection, this rule matches.
        Returns: Optional[str]
        """
        return self._probe_url
    
    @probe_url.setter
    def probe_url(self,value: Optional[str] = None) -> None:
        """
        Sets the probeUrl property value. A URL to probe. If this URL is successfully fetched (returning a 200 HTTP status code) without redirection, this rule matches.
        Args:
            value: Value to set for the probeUrl property.
        """
        self._probe_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("action", self.action)
        writer.write_collection_of_primitive_values("dnsSearchDomains", self.dns_search_domains)
        writer.write_collection_of_primitive_values("dnsServerAddressMatch", self.dns_server_address_match)
        writer.write_enum_value("domainAction", self.domain_action)
        writer.write_collection_of_primitive_values("domains", self.domains)
        writer.write_enum_value("interfaceTypeMatch", self.interface_type_match)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("probeRequiredUrl", self.probe_required_url)
        writer.write_str_value("probeUrl", self.probe_url)
        writer.write_collection_of_primitive_values("ssids", self.ssids)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def ssids(self,) -> Optional[List[str]]:
        """
        Gets the ssids property value. Network Service Set Identifiers (SSIDs).
        Returns: Optional[List[str]]
        """
        return self._ssids
    
    @ssids.setter
    def ssids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the ssids property value. Network Service Set Identifiers (SSIDs).
        Args:
            value: Value to set for the ssids property.
        """
        self._ssids = value
    

