from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
microsoft_tunnel_configuration = lazy_import('msgraph.generated.models.microsoft_tunnel_configuration')
microsoft_tunnel_server = lazy_import('msgraph.generated.models.microsoft_tunnel_server')

class MicrosoftTunnelSite(entity.Entity):
    """
    Entity that represents a Microsoft Tunnel site
    """
    def __init__(self,) -> None:
        """
        Instantiates a new microsoftTunnelSite and sets the default values.
        """
        super().__init__()
        # The site's description (optional)
        self._description: Optional[str] = None
        # The display name for the site. This property is required when a site is created.
        self._display_name: Optional[str] = None
        # When set to true, certificate pinning will be enforced on connections between the Microsoft Tunnel server and Microsoft Tunnel clients. When set to false, certificate pinning will be disabled.
        self._enable_certificate_pinning: Optional[bool] = None
        # The site's Internal Network Access Probe URL
        self._internal_network_probe_url: Optional[str] = None
        # The MicrosoftTunnelConfiguration that has been applied to this MicrosoftTunnelSite
        self._microsoft_tunnel_configuration: Optional[microsoft_tunnel_configuration.MicrosoftTunnelConfiguration] = None
        # A list of MicrosoftTunnelServers that are registered to this MicrosoftTunnelSite
        self._microsoft_tunnel_servers: Optional[List[microsoft_tunnel_server.MicrosoftTunnelServer]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The site's public domain name or IP address
        self._public_address: Optional[str] = None
        # List of Scope Tags for this Entity instance
        self._role_scope_tag_ids: Optional[List[str]] = None
        # The site's automatic upgrade setting. True for automatic upgrades, false for manual control
        self._upgrade_automatically: Optional[bool] = None
        # The site provides the state of when an upgrade is available
        self._upgrade_available: Optional[bool] = None
        # The site's upgrade window end time of day
        self._upgrade_window_end_time: Optional[Time] = None
        # The site's upgrade window start time of day
        self._upgrade_window_start_time: Optional[Time] = None
        # The site's timezone represented as a minute offset from UTC
        self._upgrade_window_utc_offset_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftTunnelSite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftTunnelSite
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftTunnelSite()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The site's description (optional)
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The site's description (optional)
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the site. This property is required when a site is created.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the site. This property is required when a site is created.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def enable_certificate_pinning(self,) -> Optional[bool]:
        """
        Gets the enableCertificatePinning property value. When set to true, certificate pinning will be enforced on connections between the Microsoft Tunnel server and Microsoft Tunnel clients. When set to false, certificate pinning will be disabled.
        Returns: Optional[bool]
        """
        return self._enable_certificate_pinning
    
    @enable_certificate_pinning.setter
    def enable_certificate_pinning(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableCertificatePinning property value. When set to true, certificate pinning will be enforced on connections between the Microsoft Tunnel server and Microsoft Tunnel clients. When set to false, certificate pinning will be disabled.
        Args:
            value: Value to set for the enableCertificatePinning property.
        """
        self._enable_certificate_pinning = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enable_certificate_pinning": lambda n : setattr(self, 'enable_certificate_pinning', n.get_bool_value()),
            "internal_network_probe_url": lambda n : setattr(self, 'internal_network_probe_url', n.get_str_value()),
            "microsoft_tunnel_configuration": lambda n : setattr(self, 'microsoft_tunnel_configuration', n.get_object_value(microsoft_tunnel_configuration.MicrosoftTunnelConfiguration)),
            "microsoft_tunnel_servers": lambda n : setattr(self, 'microsoft_tunnel_servers', n.get_collection_of_object_values(microsoft_tunnel_server.MicrosoftTunnelServer)),
            "public_address": lambda n : setattr(self, 'public_address', n.get_str_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "upgrade_automatically": lambda n : setattr(self, 'upgrade_automatically', n.get_bool_value()),
            "upgrade_available": lambda n : setattr(self, 'upgrade_available', n.get_bool_value()),
            "upgrade_window_end_time": lambda n : setattr(self, 'upgrade_window_end_time', n.get_object_value(Time)),
            "upgrade_window_start_time": lambda n : setattr(self, 'upgrade_window_start_time', n.get_object_value(Time)),
            "upgrade_window_utc_offset_in_minutes": lambda n : setattr(self, 'upgrade_window_utc_offset_in_minutes', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def internal_network_probe_url(self,) -> Optional[str]:
        """
        Gets the internalNetworkProbeUrl property value. The site's Internal Network Access Probe URL
        Returns: Optional[str]
        """
        return self._internal_network_probe_url
    
    @internal_network_probe_url.setter
    def internal_network_probe_url(self,value: Optional[str] = None) -> None:
        """
        Sets the internalNetworkProbeUrl property value. The site's Internal Network Access Probe URL
        Args:
            value: Value to set for the internalNetworkProbeUrl property.
        """
        self._internal_network_probe_url = value
    
    @property
    def microsoft_tunnel_configuration(self,) -> Optional[microsoft_tunnel_configuration.MicrosoftTunnelConfiguration]:
        """
        Gets the microsoftTunnelConfiguration property value. The MicrosoftTunnelConfiguration that has been applied to this MicrosoftTunnelSite
        Returns: Optional[microsoft_tunnel_configuration.MicrosoftTunnelConfiguration]
        """
        return self._microsoft_tunnel_configuration
    
    @microsoft_tunnel_configuration.setter
    def microsoft_tunnel_configuration(self,value: Optional[microsoft_tunnel_configuration.MicrosoftTunnelConfiguration] = None) -> None:
        """
        Sets the microsoftTunnelConfiguration property value. The MicrosoftTunnelConfiguration that has been applied to this MicrosoftTunnelSite
        Args:
            value: Value to set for the microsoftTunnelConfiguration property.
        """
        self._microsoft_tunnel_configuration = value
    
    @property
    def microsoft_tunnel_servers(self,) -> Optional[List[microsoft_tunnel_server.MicrosoftTunnelServer]]:
        """
        Gets the microsoftTunnelServers property value. A list of MicrosoftTunnelServers that are registered to this MicrosoftTunnelSite
        Returns: Optional[List[microsoft_tunnel_server.MicrosoftTunnelServer]]
        """
        return self._microsoft_tunnel_servers
    
    @microsoft_tunnel_servers.setter
    def microsoft_tunnel_servers(self,value: Optional[List[microsoft_tunnel_server.MicrosoftTunnelServer]] = None) -> None:
        """
        Sets the microsoftTunnelServers property value. A list of MicrosoftTunnelServers that are registered to this MicrosoftTunnelSite
        Args:
            value: Value to set for the microsoftTunnelServers property.
        """
        self._microsoft_tunnel_servers = value
    
    @property
    def public_address(self,) -> Optional[str]:
        """
        Gets the publicAddress property value. The site's public domain name or IP address
        Returns: Optional[str]
        """
        return self._public_address
    
    @public_address.setter
    def public_address(self,value: Optional[str] = None) -> None:
        """
        Sets the publicAddress property value. The site's public domain name or IP address
        Args:
            value: Value to set for the publicAddress property.
        """
        self._public_address = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enableCertificatePinning", self.enable_certificate_pinning)
        writer.write_str_value("internalNetworkProbeUrl", self.internal_network_probe_url)
        writer.write_object_value("microsoftTunnelConfiguration", self.microsoft_tunnel_configuration)
        writer.write_collection_of_object_values("microsoftTunnelServers", self.microsoft_tunnel_servers)
        writer.write_str_value("publicAddress", self.public_address)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_bool_value("upgradeAutomatically", self.upgrade_automatically)
        writer.write_bool_value("upgradeAvailable", self.upgrade_available)
        writer.write_object_value("upgradeWindowEndTime", self.upgrade_window_end_time)
        writer.write_object_value("upgradeWindowStartTime", self.upgrade_window_start_time)
        writer.write_int_value("upgradeWindowUtcOffsetInMinutes", self.upgrade_window_utc_offset_in_minutes)
    
    @property
    def upgrade_automatically(self,) -> Optional[bool]:
        """
        Gets the upgradeAutomatically property value. The site's automatic upgrade setting. True for automatic upgrades, false for manual control
        Returns: Optional[bool]
        """
        return self._upgrade_automatically
    
    @upgrade_automatically.setter
    def upgrade_automatically(self,value: Optional[bool] = None) -> None:
        """
        Sets the upgradeAutomatically property value. The site's automatic upgrade setting. True for automatic upgrades, false for manual control
        Args:
            value: Value to set for the upgradeAutomatically property.
        """
        self._upgrade_automatically = value
    
    @property
    def upgrade_available(self,) -> Optional[bool]:
        """
        Gets the upgradeAvailable property value. The site provides the state of when an upgrade is available
        Returns: Optional[bool]
        """
        return self._upgrade_available
    
    @upgrade_available.setter
    def upgrade_available(self,value: Optional[bool] = None) -> None:
        """
        Sets the upgradeAvailable property value. The site provides the state of when an upgrade is available
        Args:
            value: Value to set for the upgradeAvailable property.
        """
        self._upgrade_available = value
    
    @property
    def upgrade_window_end_time(self,) -> Optional[Time]:
        """
        Gets the upgradeWindowEndTime property value. The site's upgrade window end time of day
        Returns: Optional[Time]
        """
        return self._upgrade_window_end_time
    
    @upgrade_window_end_time.setter
    def upgrade_window_end_time(self,value: Optional[Time] = None) -> None:
        """
        Sets the upgradeWindowEndTime property value. The site's upgrade window end time of day
        Args:
            value: Value to set for the upgradeWindowEndTime property.
        """
        self._upgrade_window_end_time = value
    
    @property
    def upgrade_window_start_time(self,) -> Optional[Time]:
        """
        Gets the upgradeWindowStartTime property value. The site's upgrade window start time of day
        Returns: Optional[Time]
        """
        return self._upgrade_window_start_time
    
    @upgrade_window_start_time.setter
    def upgrade_window_start_time(self,value: Optional[Time] = None) -> None:
        """
        Sets the upgradeWindowStartTime property value. The site's upgrade window start time of day
        Args:
            value: Value to set for the upgradeWindowStartTime property.
        """
        self._upgrade_window_start_time = value
    
    @property
    def upgrade_window_utc_offset_in_minutes(self,) -> Optional[int]:
        """
        Gets the upgradeWindowUtcOffsetInMinutes property value. The site's timezone represented as a minute offset from UTC
        Returns: Optional[int]
        """
        return self._upgrade_window_utc_offset_in_minutes
    
    @upgrade_window_utc_offset_in_minutes.setter
    def upgrade_window_utc_offset_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the upgradeWindowUtcOffsetInMinutes property value. The site's timezone represented as a minute offset from UTC
        Args:
            value: Value to set for the upgradeWindowUtcOffsetInMinutes property.
        """
        self._upgrade_window_utc_offset_in_minutes = value
    

