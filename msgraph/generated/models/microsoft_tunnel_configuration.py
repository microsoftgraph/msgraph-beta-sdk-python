from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')

class MicrosoftTunnelConfiguration(entity.Entity):
    """
    Entity that represents a collection of Microsoft Tunnel settings
    """
    @property
    def advanced_settings(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the advancedSettings property value. Additional settings that may be applied to the server
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._advanced_settings
    
    @advanced_settings.setter
    def advanced_settings(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the advancedSettings property value. Additional settings that may be applied to the server
        Args:
            value: Value to set for the advancedSettings property.
        """
        self._advanced_settings = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new microsoftTunnelConfiguration and sets the default values.
        """
        super().__init__()
        # Additional settings that may be applied to the server
        self._advanced_settings: Optional[List[key_value_pair.KeyValuePair]] = None
        # The Default Domain appendix that will be used by the clients
        self._default_domain_suffix: Optional[str] = None
        # The configuration's description (optional)
        self._description: Optional[str] = None
        # When DisableUdpConnections is set, the clients and VPN server will not use DTLS connections to transfer data.
        self._disable_udp_connections: Optional[bool] = None
        # The display name for the server configuration. This property is required when a server is created.
        self._display_name: Optional[str] = None
        # The DNS servers that will be used by the clients
        self._dns_servers: Optional[List[str]] = None
        # When the configuration was last updated
        self._last_update_date_time: Optional[datetime] = None
        # The port that both TCP and UPD will listen over on the server
        self._listen_port: Optional[int] = None
        # The subnet that will be used to allocate virtual address for the clients
        self._network: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of Scope Tags for this Entity instance
        self._role_scope_tag_ids: Optional[List[str]] = None
        # Subsets of the routes that will not be routed by the server
        self._route_excludes: Optional[List[str]] = None
        # The routes that will be routed by the server
        self._route_includes: Optional[List[str]] = None
        # Subsets of the routes that will not be routed by the server. This property is going to be deprecated with the option of using the new property, 'RouteExcludes'.
        self._routes_exclude: Optional[List[str]] = None
        # The routes that will be routed by the server. This property is going to be deprecated with the option of using the new property, 'RouteIncludes'.
        self._routes_include: Optional[List[str]] = None
        # The domains that will be resolved using the provided dns servers
        self._split_d_n_s: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftTunnelConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftTunnelConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftTunnelConfiguration()
    
    @property
    def default_domain_suffix(self,) -> Optional[str]:
        """
        Gets the defaultDomainSuffix property value. The Default Domain appendix that will be used by the clients
        Returns: Optional[str]
        """
        return self._default_domain_suffix
    
    @default_domain_suffix.setter
    def default_domain_suffix(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultDomainSuffix property value. The Default Domain appendix that will be used by the clients
        Args:
            value: Value to set for the defaultDomainSuffix property.
        """
        self._default_domain_suffix = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The configuration's description (optional)
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The configuration's description (optional)
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def disable_udp_connections(self,) -> Optional[bool]:
        """
        Gets the disableUdpConnections property value. When DisableUdpConnections is set, the clients and VPN server will not use DTLS connections to transfer data.
        Returns: Optional[bool]
        """
        return self._disable_udp_connections
    
    @disable_udp_connections.setter
    def disable_udp_connections(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableUdpConnections property value. When DisableUdpConnections is set, the clients and VPN server will not use DTLS connections to transfer data.
        Args:
            value: Value to set for the disableUdpConnections property.
        """
        self._disable_udp_connections = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the server configuration. This property is required when a server is created.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the server configuration. This property is required when a server is created.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def dns_servers(self,) -> Optional[List[str]]:
        """
        Gets the dnsServers property value. The DNS servers that will be used by the clients
        Returns: Optional[List[str]]
        """
        return self._dns_servers
    
    @dns_servers.setter
    def dns_servers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the dnsServers property value. The DNS servers that will be used by the clients
        Args:
            value: Value to set for the dnsServers property.
        """
        self._dns_servers = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "advanced_settings": lambda n : setattr(self, 'advanced_settings', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "default_domain_suffix": lambda n : setattr(self, 'default_domain_suffix', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "disable_udp_connections": lambda n : setattr(self, 'disable_udp_connections', n.get_bool_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "dns_servers": lambda n : setattr(self, 'dns_servers', n.get_collection_of_primitive_values(str)),
            "last_update_date_time": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "listen_port": lambda n : setattr(self, 'listen_port', n.get_int_value()),
            "network": lambda n : setattr(self, 'network', n.get_str_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "route_excludes": lambda n : setattr(self, 'route_excludes', n.get_collection_of_primitive_values(str)),
            "route_includes": lambda n : setattr(self, 'route_includes', n.get_collection_of_primitive_values(str)),
            "routes_exclude": lambda n : setattr(self, 'routes_exclude', n.get_collection_of_primitive_values(str)),
            "routes_include": lambda n : setattr(self, 'routes_include', n.get_collection_of_primitive_values(str)),
            "split_d_n_s": lambda n : setattr(self, 'split_d_n_s', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_update_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdateDateTime property value. When the configuration was last updated
        Returns: Optional[datetime]
        """
        return self._last_update_date_time
    
    @last_update_date_time.setter
    def last_update_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdateDateTime property value. When the configuration was last updated
        Args:
            value: Value to set for the lastUpdateDateTime property.
        """
        self._last_update_date_time = value
    
    @property
    def listen_port(self,) -> Optional[int]:
        """
        Gets the listenPort property value. The port that both TCP and UPD will listen over on the server
        Returns: Optional[int]
        """
        return self._listen_port
    
    @listen_port.setter
    def listen_port(self,value: Optional[int] = None) -> None:
        """
        Sets the listenPort property value. The port that both TCP and UPD will listen over on the server
        Args:
            value: Value to set for the listenPort property.
        """
        self._listen_port = value
    
    @property
    def network(self,) -> Optional[str]:
        """
        Gets the network property value. The subnet that will be used to allocate virtual address for the clients
        Returns: Optional[str]
        """
        return self._network
    
    @network.setter
    def network(self,value: Optional[str] = None) -> None:
        """
        Sets the network property value. The subnet that will be used to allocate virtual address for the clients
        Args:
            value: Value to set for the network property.
        """
        self._network = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this Entity instance
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this Entity instance
        Args:
            value: Value to set for the roleScopeTagIds property.
        """
        self._role_scope_tag_ids = value
    
    @property
    def route_excludes(self,) -> Optional[List[str]]:
        """
        Gets the routeExcludes property value. Subsets of the routes that will not be routed by the server
        Returns: Optional[List[str]]
        """
        return self._route_excludes
    
    @route_excludes.setter
    def route_excludes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the routeExcludes property value. Subsets of the routes that will not be routed by the server
        Args:
            value: Value to set for the routeExcludes property.
        """
        self._route_excludes = value
    
    @property
    def route_includes(self,) -> Optional[List[str]]:
        """
        Gets the routeIncludes property value. The routes that will be routed by the server
        Returns: Optional[List[str]]
        """
        return self._route_includes
    
    @route_includes.setter
    def route_includes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the routeIncludes property value. The routes that will be routed by the server
        Args:
            value: Value to set for the routeIncludes property.
        """
        self._route_includes = value
    
    @property
    def routes_exclude(self,) -> Optional[List[str]]:
        """
        Gets the routesExclude property value. Subsets of the routes that will not be routed by the server. This property is going to be deprecated with the option of using the new property, 'RouteExcludes'.
        Returns: Optional[List[str]]
        """
        return self._routes_exclude
    
    @routes_exclude.setter
    def routes_exclude(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the routesExclude property value. Subsets of the routes that will not be routed by the server. This property is going to be deprecated with the option of using the new property, 'RouteExcludes'.
        Args:
            value: Value to set for the routesExclude property.
        """
        self._routes_exclude = value
    
    @property
    def routes_include(self,) -> Optional[List[str]]:
        """
        Gets the routesInclude property value. The routes that will be routed by the server. This property is going to be deprecated with the option of using the new property, 'RouteIncludes'.
        Returns: Optional[List[str]]
        """
        return self._routes_include
    
    @routes_include.setter
    def routes_include(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the routesInclude property value. The routes that will be routed by the server. This property is going to be deprecated with the option of using the new property, 'RouteIncludes'.
        Args:
            value: Value to set for the routesInclude property.
        """
        self._routes_include = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("advancedSettings", self.advanced_settings)
        writer.write_str_value("defaultDomainSuffix", self.default_domain_suffix)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("disableUdpConnections", self.disable_udp_connections)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("dnsServers", self.dns_servers)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_int_value("listenPort", self.listen_port)
        writer.write_str_value("network", self.network)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_collection_of_primitive_values("routeExcludes", self.route_excludes)
        writer.write_collection_of_primitive_values("routeIncludes", self.route_includes)
        writer.write_collection_of_primitive_values("routesExclude", self.routes_exclude)
        writer.write_collection_of_primitive_values("routesInclude", self.routes_include)
        writer.write_collection_of_primitive_values("splitDNS", self.split_d_n_s)
    
    @property
    def split_d_n_s(self,) -> Optional[List[str]]:
        """
        Gets the splitDNS property value. The domains that will be resolved using the provided dns servers
        Returns: Optional[List[str]]
        """
        return self._split_d_n_s
    
    @split_d_n_s.setter
    def split_d_n_s(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the splitDNS property value. The domains that will be resolved using the provided dns servers
        Args:
            value: Value to set for the splitDNS property.
        """
        self._split_d_n_s = value
    

