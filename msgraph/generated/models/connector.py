from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .connector_group import ConnectorGroup
    from .connector_status import ConnectorStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class Connector(Entity):
    # The external IP address as detected by the the connector server. Read-only.
    external_ip: Optional[str] = None
    # The machine name the connector is installed and running on.
    machine_name: Optional[str] = None
    # The connectorGroup that the connector is a member of. Read-only.
    member_of: Optional[List[ConnectorGroup]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[ConnectorStatus] = None
    # The version property
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Connector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Connector
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Connector()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .connector_group import ConnectorGroup
        from .connector_status import ConnectorStatus
        from .entity import Entity

        from .connector_group import ConnectorGroup
        from .connector_status import ConnectorStatus
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "externalIp": lambda n : setattr(self, 'external_ip', n.get_str_value()),
            "machineName": lambda n : setattr(self, 'machine_name', n.get_str_value()),
            "memberOf": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(ConnectorGroup)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ConnectorStatus)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("externalIp", self.external_ip)
        writer.write_str_value("machineName", self.machine_name)
        writer.write_collection_of_object_values("memberOf", self.member_of)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("version", self.version)
    

