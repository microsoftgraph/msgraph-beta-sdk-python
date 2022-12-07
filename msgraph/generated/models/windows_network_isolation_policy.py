from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ip_range = lazy_import('msgraph.generated.models.ip_range')
proxied_domain = lazy_import('msgraph.generated.models.proxied_domain')

class WindowsNetworkIsolationPolicy(AdditionalDataHolder, Parsable):
    """
    Windows Network Isolation Policy
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsNetworkIsolationPolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Contains a list of enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy. This collection can contain a maximum of 500 elements.
        self._enterprise_cloud_resources: Optional[List[proxied_domain.ProxiedDomain]] = None
        # This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseCloudResources policy to force traffic to the matched cloud resources through these proxies.
        self._enterprise_internal_proxy_servers: Optional[List[str]] = None
        # Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to. This collection can contain a maximum of 500 elements.
        self._enterprise_i_p_ranges: Optional[List[ip_range.IpRange]] = None
        # Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false.
        self._enterprise_i_p_ranges_are_authoritative: Optional[bool] = None
        # This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected. These locations will be considered a safe destination for enterprise data to be shared to.
        self._enterprise_network_domain_names: Optional[List[str]] = None
        # This is a list of proxy servers. Any server not on this list is considered non-enterprise.
        self._enterprise_proxy_servers: Optional[List[str]] = None
        # Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false
        self._enterprise_proxy_servers_are_authoritative: Optional[bool] = None
        # List of domain names that can used for work or personal resource.
        self._neutral_domain_resources: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsNetworkIsolationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsNetworkIsolationPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsNetworkIsolationPolicy()
    
    @property
    def enterprise_cloud_resources(self,) -> Optional[List[proxied_domain.ProxiedDomain]]:
        """
        Gets the enterpriseCloudResources property value. Contains a list of enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[proxied_domain.ProxiedDomain]]
        """
        return self._enterprise_cloud_resources
    
    @enterprise_cloud_resources.setter
    def enterprise_cloud_resources(self,value: Optional[List[proxied_domain.ProxiedDomain]] = None) -> None:
        """
        Sets the enterpriseCloudResources property value. Contains a list of enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the enterpriseCloudResources property.
        """
        self._enterprise_cloud_resources = value
    
    @property
    def enterprise_internal_proxy_servers(self,) -> Optional[List[str]]:
        """
        Gets the enterpriseInternalProxyServers property value. This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseCloudResources policy to force traffic to the matched cloud resources through these proxies.
        Returns: Optional[List[str]]
        """
        return self._enterprise_internal_proxy_servers
    
    @enterprise_internal_proxy_servers.setter
    def enterprise_internal_proxy_servers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enterpriseInternalProxyServers property value. This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseCloudResources policy to force traffic to the matched cloud resources through these proxies.
        Args:
            value: Value to set for the enterpriseInternalProxyServers property.
        """
        self._enterprise_internal_proxy_servers = value
    
    @property
    def enterprise_i_p_ranges(self,) -> Optional[List[ip_range.IpRange]]:
        """
        Gets the enterpriseIPRanges property value. Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ip_range.IpRange]]
        """
        return self._enterprise_i_p_ranges
    
    @enterprise_i_p_ranges.setter
    def enterprise_i_p_ranges(self,value: Optional[List[ip_range.IpRange]] = None) -> None:
        """
        Sets the enterpriseIPRanges property value. Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the enterpriseIPRanges property.
        """
        self._enterprise_i_p_ranges = value
    
    @property
    def enterprise_i_p_ranges_are_authoritative(self,) -> Optional[bool]:
        """
        Gets the enterpriseIPRangesAreAuthoritative property value. Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false.
        Returns: Optional[bool]
        """
        return self._enterprise_i_p_ranges_are_authoritative
    
    @enterprise_i_p_ranges_are_authoritative.setter
    def enterprise_i_p_ranges_are_authoritative(self,value: Optional[bool] = None) -> None:
        """
        Sets the enterpriseIPRangesAreAuthoritative property value. Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false.
        Args:
            value: Value to set for the enterpriseIPRangesAreAuthoritative property.
        """
        self._enterprise_i_p_ranges_are_authoritative = value
    
    @property
    def enterprise_network_domain_names(self,) -> Optional[List[str]]:
        """
        Gets the enterpriseNetworkDomainNames property value. This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected. These locations will be considered a safe destination for enterprise data to be shared to.
        Returns: Optional[List[str]]
        """
        return self._enterprise_network_domain_names
    
    @enterprise_network_domain_names.setter
    def enterprise_network_domain_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enterpriseNetworkDomainNames property value. This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected. These locations will be considered a safe destination for enterprise data to be shared to.
        Args:
            value: Value to set for the enterpriseNetworkDomainNames property.
        """
        self._enterprise_network_domain_names = value
    
    @property
    def enterprise_proxy_servers(self,) -> Optional[List[str]]:
        """
        Gets the enterpriseProxyServers property value. This is a list of proxy servers. Any server not on this list is considered non-enterprise.
        Returns: Optional[List[str]]
        """
        return self._enterprise_proxy_servers
    
    @enterprise_proxy_servers.setter
    def enterprise_proxy_servers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enterpriseProxyServers property value. This is a list of proxy servers. Any server not on this list is considered non-enterprise.
        Args:
            value: Value to set for the enterpriseProxyServers property.
        """
        self._enterprise_proxy_servers = value
    
    @property
    def enterprise_proxy_servers_are_authoritative(self,) -> Optional[bool]:
        """
        Gets the enterpriseProxyServersAreAuthoritative property value. Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false
        Returns: Optional[bool]
        """
        return self._enterprise_proxy_servers_are_authoritative
    
    @enterprise_proxy_servers_are_authoritative.setter
    def enterprise_proxy_servers_are_authoritative(self,value: Optional[bool] = None) -> None:
        """
        Sets the enterpriseProxyServersAreAuthoritative property value. Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false
        Args:
            value: Value to set for the enterpriseProxyServersAreAuthoritative property.
        """
        self._enterprise_proxy_servers_are_authoritative = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enterprise_cloud_resources": lambda n : setattr(self, 'enterprise_cloud_resources', n.get_collection_of_object_values(proxied_domain.ProxiedDomain)),
            "enterprise_internal_proxy_servers": lambda n : setattr(self, 'enterprise_internal_proxy_servers', n.get_collection_of_primitive_values(str)),
            "enterprise_i_p_ranges": lambda n : setattr(self, 'enterprise_i_p_ranges', n.get_collection_of_object_values(ip_range.IpRange)),
            "enterprise_i_p_ranges_are_authoritative": lambda n : setattr(self, 'enterprise_i_p_ranges_are_authoritative', n.get_bool_value()),
            "enterprise_network_domain_names": lambda n : setattr(self, 'enterprise_network_domain_names', n.get_collection_of_primitive_values(str)),
            "enterprise_proxy_servers": lambda n : setattr(self, 'enterprise_proxy_servers', n.get_collection_of_primitive_values(str)),
            "enterprise_proxy_servers_are_authoritative": lambda n : setattr(self, 'enterprise_proxy_servers_are_authoritative', n.get_bool_value()),
            "neutral_domain_resources": lambda n : setattr(self, 'neutral_domain_resources', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def neutral_domain_resources(self,) -> Optional[List[str]]:
        """
        Gets the neutralDomainResources property value. List of domain names that can used for work or personal resource.
        Returns: Optional[List[str]]
        """
        return self._neutral_domain_resources
    
    @neutral_domain_resources.setter
    def neutral_domain_resources(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the neutralDomainResources property value. List of domain names that can used for work or personal resource.
        Args:
            value: Value to set for the neutralDomainResources property.
        """
        self._neutral_domain_resources = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("enterpriseCloudResources", self.enterprise_cloud_resources)
        writer.write_collection_of_primitive_values("enterpriseInternalProxyServers", self.enterprise_internal_proxy_servers)
        writer.write_collection_of_object_values("enterpriseIPRanges", self.enterprise_i_p_ranges)
        writer.write_bool_value("enterpriseIPRangesAreAuthoritative", self.enterprise_i_p_ranges_are_authoritative)
        writer.write_collection_of_primitive_values("enterpriseNetworkDomainNames", self.enterprise_network_domain_names)
        writer.write_collection_of_primitive_values("enterpriseProxyServers", self.enterprise_proxy_servers)
        writer.write_bool_value("enterpriseProxyServersAreAuthoritative", self.enterprise_proxy_servers_are_authoritative)
        writer.write_collection_of_primitive_values("neutralDomainResources", self.neutral_domain_resources)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

