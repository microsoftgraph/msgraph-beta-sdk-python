from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, microsoft_tunnel_server_health_status

from . import entity

class MicrosoftTunnelServer(entity.Entity):
    """
    Entity that represents a single Microsoft Tunnel server
    """
    def __init__(self,) -> None:
        """
        Instantiates a new microsoftTunnelServer and sets the default values.
        """
        super().__init__()
        # The digest of the current agent image running on this server
        self._agent_image_digest: Optional[str] = None
        # The display name for the server. This property is required when a server is created and cannot be cleared during updates.
        self._display_name: Optional[str] = None
        # Indicates when the server last checked in
        self._last_checkin_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The digest of the current server image running on this server
        self._server_image_digest: Optional[str] = None
        # Enum of possible MicrosoftTunnelServer health status types
        self._tunnel_server_health_status: Optional[microsoft_tunnel_server_health_status.MicrosoftTunnelServerHealthStatus] = None
    
    @property
    def agent_image_digest(self,) -> Optional[str]:
        """
        Gets the agentImageDigest property value. The digest of the current agent image running on this server
        Returns: Optional[str]
        """
        return self._agent_image_digest
    
    @agent_image_digest.setter
    def agent_image_digest(self,value: Optional[str] = None) -> None:
        """
        Sets the agentImageDigest property value. The digest of the current agent image running on this server
        Args:
            value: Value to set for the agent_image_digest property.
        """
        self._agent_image_digest = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftTunnelServer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftTunnelServer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftTunnelServer()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the server. This property is required when a server is created and cannot be cleared during updates.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the server. This property is required when a server is created and cannot be cleared during updates.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, microsoft_tunnel_server_health_status

        fields: Dict[str, Callable[[Any], None]] = {
            "agentImageDigest": lambda n : setattr(self, 'agent_image_digest', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastCheckinDateTime": lambda n : setattr(self, 'last_checkin_date_time', n.get_datetime_value()),
            "serverImageDigest": lambda n : setattr(self, 'server_image_digest', n.get_str_value()),
            "tunnelServerHealthStatus": lambda n : setattr(self, 'tunnel_server_health_status', n.get_enum_value(microsoft_tunnel_server_health_status.MicrosoftTunnelServerHealthStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_checkin_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastCheckinDateTime property value. Indicates when the server last checked in
        Returns: Optional[datetime]
        """
        return self._last_checkin_date_time
    
    @last_checkin_date_time.setter
    def last_checkin_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastCheckinDateTime property value. Indicates when the server last checked in
        Args:
            value: Value to set for the last_checkin_date_time property.
        """
        self._last_checkin_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("agentImageDigest", self.agent_image_digest)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastCheckinDateTime", self.last_checkin_date_time)
        writer.write_str_value("serverImageDigest", self.server_image_digest)
        writer.write_enum_value("tunnelServerHealthStatus", self.tunnel_server_health_status)
    
    @property
    def server_image_digest(self,) -> Optional[str]:
        """
        Gets the serverImageDigest property value. The digest of the current server image running on this server
        Returns: Optional[str]
        """
        return self._server_image_digest
    
    @server_image_digest.setter
    def server_image_digest(self,value: Optional[str] = None) -> None:
        """
        Sets the serverImageDigest property value. The digest of the current server image running on this server
        Args:
            value: Value to set for the server_image_digest property.
        """
        self._server_image_digest = value
    
    @property
    def tunnel_server_health_status(self,) -> Optional[microsoft_tunnel_server_health_status.MicrosoftTunnelServerHealthStatus]:
        """
        Gets the tunnelServerHealthStatus property value. Enum of possible MicrosoftTunnelServer health status types
        Returns: Optional[microsoft_tunnel_server_health_status.MicrosoftTunnelServerHealthStatus]
        """
        return self._tunnel_server_health_status
    
    @tunnel_server_health_status.setter
    def tunnel_server_health_status(self,value: Optional[microsoft_tunnel_server_health_status.MicrosoftTunnelServerHealthStatus] = None) -> None:
        """
        Sets the tunnelServerHealthStatus property value. Enum of possible MicrosoftTunnelServer health status types
        Args:
            value: Value to set for the tunnel_server_health_status property.
        """
        self._tunnel_server_health_status = value
    

