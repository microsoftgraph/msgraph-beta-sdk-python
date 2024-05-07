from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .microsoft_tunnel_server_health_status import MicrosoftTunnelServerHealthStatus

from .entity import Entity

@dataclass
class MicrosoftTunnelServer(Entity):
    """
    Entity that represents a single Microsoft Tunnel server
    """
    # The digest of the current agent image running on this server
    agent_image_digest: Optional[str] = None
    # The display name for the server. This property is required when a server is created and cannot be cleared during updates.
    display_name: Optional[str] = None
    # Indicates when the server last checked in
    last_checkin_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The digest of the current server image running on this server
    server_image_digest: Optional[str] = None
    # Enum of possible MicrosoftTunnelServer health status types
    tunnel_server_health_status: Optional[MicrosoftTunnelServerHealthStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftTunnelServer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftTunnelServer
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftTunnelServer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .microsoft_tunnel_server_health_status import MicrosoftTunnelServerHealthStatus

        from .entity import Entity
        from .microsoft_tunnel_server_health_status import MicrosoftTunnelServerHealthStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "agentImageDigest": lambda n : setattr(self, 'agent_image_digest', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastCheckinDateTime": lambda n : setattr(self, 'last_checkin_date_time', n.get_datetime_value()),
            "serverImageDigest": lambda n : setattr(self, 'server_image_digest', n.get_str_value()),
            "tunnelServerHealthStatus": lambda n : setattr(self, 'tunnel_server_health_status', n.get_enum_value(MicrosoftTunnelServerHealthStatus)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("agentImageDigest", self.agent_image_digest)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastCheckinDateTime", self.last_checkin_date_time)
        writer.write_str_value("serverImageDigest", self.server_image_digest)
        writer.write_enum_value("tunnelServerHealthStatus", self.tunnel_server_health_status)
    

